# Sandbox (Code Execution)

Louie runs the Python code it writes, and code that users write, in short-lived sandbox containers. A separate service in `/var/dj` manages those containers. This page covers how the sandbox works, its required settings, ports, resource limits, cleanup, and how to check it.

## How it works

| Component | Container | Role |
|-----------|-----------|------|
| Sandbox launcher (maestro) | `dj-louie-maestro-1` | API that creates and deletes sandboxes. It uses the host's Docker through `/var/run/docker.sock`. |
| Launcher proxy | `dj-maestro-caddy-1` | Entry point Louie calls (`SANDBOX_URL`, default `http://maestro-caddy`), over the shared `louie_public` Docker network. |
| Sandbox reaper | `dj-sandbox-reaper-1` | Finds sandbox containers and networks left behind by failed or abandoned runs. |
| Sandbox | `louie-sandbox_<id>` | Runs one piece of code, using the `graphistry/louie-sandbox` image. |
| Sandbox proxy | `louie-sandbox_caddy_<id>` | Connects Louie to that one sandbox. |

For each code run:

1. Louie asks the launcher for a sandbox.
2. The launcher creates a private Docker network for this run, marked `internal`, so the code has no internet or LAN access.
3. It starts the sandbox container on that network, and a sandbox proxy that joins both the private network and `louie_public`.
4. Louie sends the code through the proxy and streams back the output and saved results.
5. Louie deletes the sandbox, its proxy, and its network.

The sandbox container mounts these host folders, all under `DATA_ROOT_PATH`:

| Inside the sandbox | Host folder | Access |
|--------------------|-------------|--------|
| `/opt/input` | `<DATA_ROOT_PATH>/sandbox/<org>/<user>/<run>/input/` | Read-only |
| `/opt/output` | `<DATA_ROOT_PATH>/sandbox/<org>/<user>/<run>/output/` | Read-write |
| `/opt/parquet` | `<DATA_ROOT_PATH>/assets/parquet/<org>/<user>/dthread/<thread>/` | Read-only |
| `/opt/py_env` | `<DATA_ROOT_PATH>/../py_envs/sandbox` (custom packages) | Read-only |

## Required settings

The launcher asks the host's Docker to mount the folders above, so these settings in `/var/dj/.env` must be **host** paths. The shipped `env.example` leaves them commented out. Without them, every code run fails, while all containers still report healthy.

```bash
DATA_ROOT_PATH="/var/louie/data/data/datathreads"
SANDBOX_CADDYFILE_PATH="/var/dj/infra/sandbox_caddy/Caddyfile"
```

Apply changes with `cd /var/dj && sudo ./dc up -d --no-build --pull never`.

Optional settings in `/var/dj/.env`:

| Setting | Default | Purpose |
|---------|---------|---------|
| `PYENV_PATH` | `<DATA_ROOT_PATH>/../py_envs/sandbox` | Host folder of extra Python packages. See [Python Sandbox Custom Pip Packages](026_Python_Package_Config.md). |
| `SANDBOX_IMAGE_DEFAULT` | `graphistry/louie-sandbox:latest` | Sandbox image. A GPU image exists but is not part of the standard release files; contact Graphistry. |
| `CONTAINER_PREFIX` | `louie-sandbox` | Name prefix for sandbox containers. The reaper uses it too. |

Optional settings in `/var/louie/data/custom.env`:

| Setting | Default | Purpose |
|---------|---------|---------|
| `SANDBOX_URL` | `http://maestro-caddy` | Where Louie reaches the launcher |
| `SANDBOX_READY_TIMEOUT_S` | `300` | How long Louie waits for a new sandbox to become ready |

## Resource limits

`/var/dj/sandbox.json` limits each sandbox container. `/var/dj/sandbox.caddy.json` limits each sandbox proxy. The defaults are:

```json
{
  "mem_limit": "2g",
  "cpu_shares": 512,
  "cpu_period": 100000,
  "cpu_quota": 50000,
  "pids_limit": 100
}
```

| Field | Meaning |
|-------|---------|
| `mem_limit` | Memory cap per sandbox. Plan host RAM as Louie's own use plus `mem_limit` times the number of code runs at once. |
| `cpu_quota` / `cpu_period` | CPU cap. `50000 / 100000` is half of one CPU core. |
| `cpu_shares` | Relative CPU weight when the host is busy |
| `pids_limit` | Maximum processes per sandbox |

After editing either file, restart the launcher: `cd /var/dj && sudo ./dc up -d --no-build --pull never --force-recreate louie-maestro`. New sandboxes use the new limits.

## Ports and firewall

| Host port | Opened by | Needed by |
|-----------|-----------|-----------|
| 8081 | Launcher proxy (`maestro-caddy`) | Local checks only. Louie uses the internal Docker network. |
| 9000-9999 | One sandbox proxy per running code run, opened and closed on demand | Not needed outside the host. Louie uses the internal Docker network. |

The compose file also lists port 8082 for the launcher. Docker does not publish it, because the launcher is attached only to an internal network.

Users never need to reach these ports. They have no authentication, so block them from other machines:

- **8081:** bind it to the host only with an override file. See [Change the default ports](012_Docker_Compose_Install.md#change-the-default-ports).
- **9000-9999:** block the range at your network firewall or cloud security group. Host firewalls such as `ufw` do not filter ports that Docker publishes. If you need host-level rules, see Docker's [packet filtering and firewalls](https://docs.docker.com/engine/network/packet-filtering-firewalls/) guide.

## Cleanup (sandbox reaper)

Louie deletes each sandbox when its run ends. If a run is interrupted, for example by a restart in the middle of a run, containers and networks can be left behind. The reaper finds them by their `dj.*` labels.

By default the reaper runs in **dry-run mode**. It logs what it would remove but removes nothing. To let it clean up, set this in `/var/dj/.env` and restart the sandbox service:

```bash
REAPER_DRY_RUN=0
```

| Setting | Default | Purpose |
|---------|---------|---------|
| `REAPER_DRY_RUN` | `1` | `1` only logs, `0` removes |
| `REAPER_MAX_AGE_SECONDS` | `21600` (6 hours) | Sandboxes older than this are removed |
| `REAPER_GRACE_SECONDS` | `1800` | Minimum age before anything is considered |
| `REAPER_INTERVAL_SECONDS` | `300` | Time between sweeps |

Check what it finds with `docker logs --tail 20 dj-sandbox-reaper-1`. Each sweep logs `scanned`, `eligible`, and `reaped` counts.

## Verify

1. All three service containers are healthy:

   ```bash
   docker ps --filter name=dj- --format 'table {{.Names}}\t{{.Status}}'
   ```

2. In Louie, ask: *"use Python to list the first 20 prime numbers"*. Louie shows the code and its output.
3. While it runs, `docker ps --filter label=dj.component` shows a `louie-sandbox_<id>` and a `louie-sandbox_caddy_<id>` container. They disappear when the run ends.

## Troubleshooting

| Symptom | Cause and fix |
|---------|---------------|
| Code runs fail. `docker logs dj-louie-maestro-1` shows `None/sandbox/... includes invalid characters` | `DATA_ROOT_PATH` is not set in `/var/dj/.env`. See [Required settings](#required-settings). |
| Code runs fail with `No such image` | The sandbox image is not loaded. Reload the release's container images (`docker load`). |
| Code runs time out on a busy host | Raise `SANDBOX_READY_TIMEOUT_S`, or add CPU and RAM. |
| A package is missing in the sandbox | Add it as described in [Python Sandbox Custom Pip Packages](026_Python_Package_Config.md). |
| Leftover `louie-sandbox_*` containers pile up | The reaper is in dry-run mode. Set `REAPER_DRY_RUN=0`. |
| `network louie_public ... could not be found` when starting `/var/dj` | Start Louie (`/var/louie`) first. It creates that network. |
