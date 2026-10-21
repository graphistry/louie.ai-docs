# Docker Compose Install (Tarball)

Install or upgrade a self-hosted Louie server on a single Linux host from the release tarballs. This works on air-gapped hosts: only the download needs internet access, and it can happen on a different machine.

If Graphistry sent you an installer kit (`01_download.sh`, `02_install.sh`, and a README), you can use it to run these same steps for you. This page documents what the kit does, so you can install by hand, check the kit's work, or troubleshoot.

## Release files

Each release is two files with the same version and build timestamp. You need both.

| File | Size (approx.) | Contents |
|------|------|----------|
| `louie-bulwarks-<version>-<timestamp>.tar.gz` | 160 KB | Compose files, configuration templates, helper scripts |
| `containers-<version>-<timestamp>.tar.gz` | 2.6 GB | Container images for Louie and the sandbox (code execution) service |

Graphistry provides them in one of two ways:

- **Download links.** These links work without an AWS account and expire on the date Graphistry gives you. Anyone who has a link can download the release until then, so keep the links out of tickets, chat channels, and shared drives.
- **Offline bundle.** Both files on physical media or through your secure file transfer, for hosts with no internet access.

Ask your Graphistry contact for the SHA-256 checksums of both files, and check them before installing:

```bash
sha256sum louie-bulwarks-*.tar.gz containers-*.tar.gz
```

The bulwarks file holds two nested tarballs:

- `bulwarks-louie.tar.gz` contains the Louie app, API, and web proxy, and installs into `/var/louie`.
- `bulwarks-dj.tar.gz` contains the sandbox service that runs Python code for Louie, and installs into `/var/dj`. Its version can differ from Louie's. The `VERSION_DJ` file in the Louie folder names the sandbox version each release needs.

## Requirements

- Linux x86_64 host with root or sudo access. Ubuntu 22.04 or 24.04 is recommended.
- Docker Engine 24 or later with the Docker Compose v2 plugin. `docker compose version` must work.
- Disk: at least 30 GB free in the Docker data folder (usually `/var/lib/docker`) for the images, plus 3 GB for the downloaded files.
- RAM: 8 GB minimum, 16 GB recommended. Each concurrent code run uses up to 2 GB more. See [System Requirements](006_System_Requirements.md).
- Ports 80 and 443 for Louie users.
- Ports 8081 and 8082 must be free. The sandbox service uses them on the host, and users do not need to reach them, so keep them blocked from other networks.
- A Graphistry server for sign-in: Graphistry Hub or your own Graphistry deployment.
- An LLM provider. See [LLM Configuration](008_LLM_Configuration.md).

A GPU is not required.

## 1. Load the container images

```bash
sudo docker load -i containers-<version>-<timestamp>.tar.gz
```

This takes several minutes. It loads version-tagged images, such as `graphistry/louie:<version>`, plus `latest` aliases that the Compose files use. It also loads third-party images: `caddy`, `alpine:latest`, and the OpenTelemetry collector. If the host already has its own `alpine:latest`, this load replaces it.

## 2. Unpack

```bash
mkdir -p /tmp/louie-release
tar -xzf louie-bulwarks-<version>-<timestamp>.tar.gz -C /tmp/louie-release

sudo mkdir -p /var/louie /var/dj
sudo tar -xzf /tmp/louie-release/bulwarks-louie.tar.gz -C /var/louie
sudo tar -xzf /tmp/louie-release/bulwarks-dj.tar.gz -C /var/dj

cat /var/louie/VERSION /var/louie/VERSION_DJ /var/dj/VERSION
```

`VERSION` should show the Louie version you are installing. The `VERSION_DJ` file and `/var/dj/VERSION` should show the same sandbox version.

The tarballs ship configuration templates (`*.example`) only, never live configuration files. Unpacking a newer release over an existing install does not overwrite your settings.

## 3. Create the configuration files

Copy each template only where the file does not exist yet:

```bash
cd /var/louie
sudo cp -n system.env.example system.env
sudo cp -n data/custom.env.example data/custom.env
sudo cp -n data/Caddyfile.example data/Caddyfile
sudo chmod 600 system.env data/custom.env

cd /var/dj
sudo cp -n env.example .env
sudo cp -n sandbox.json.example sandbox.json
sudo cp -n sandbox.caddy.json.example sandbox.caddy.json
```

| File | Purpose |
|------|---------|
| `/var/louie/system.env` | Defaults, and documentation for every setting. Usually left unchanged. |
| `/var/louie/data/custom.env` | Your settings. Values here override `system.env`. Readable by root only. |
| `/var/louie/data/Caddyfile` | Web proxy: ports, hostname, TLS |
| `/var/dj/.env` | Sandbox service settings |
| `/var/dj/sandbox.json` | Resource limits for each code run (memory, CPU, processes) |

### Louie settings

Put these in `/var/louie/data/custom.env`:

```bash
# Graphistry sign-in. See "Authentication Registration & TLS".
OA2_HOST='https://hub.graphistry.com'               # or your own Graphistry server URL
OA2_REDIRECT_URL_BASE='https://louie.example.com'   # the address users open Louie at, no trailing slash
OA2_CLIENT_ID='<client id>'
OA2_CLIENT_SECRET='<client secret>'

# LLM provider: set at least one. See system.env for every provider.
OPENAI_API_KEY='<your OpenAI API key>'
```

Generate a key for encrypting stored credentials, once:

```bash
echo "JWT_SECRET_LOUIE='$(openssl rand -hex 32)'" | sudo tee -a /var/louie/data/custom.env > /dev/null
```

Keep `JWT_SECRET_LOUIE` unchanged after first start. Changing it makes credentials that users have already saved, such as database connector passwords, unreadable.

### Sandbox settings

The sandbox service starts a short-lived container for each code run. It asks the host's Docker to mount folders into that container, so these two settings must be **host** paths. The template leaves them commented out. Without them every code run fails, even though all containers report healthy.

```bash
echo 'DATA_ROOT_PATH="/var/louie/data/data/datathreads"'                   | sudo tee -a /var/dj/.env > /dev/null
echo 'SANDBOX_CADDYFILE_PATH="/var/dj/infra/sandbox_caddy/Caddyfile"'     | sudo tee -a /var/dj/.env > /dev/null
```

If you installed into folders other than `/var/louie` and `/var/dj`, use those paths instead.

## 4. Register Louie with Graphistry

Louie signs users in through Graphistry using OAuth2. Register an OAuth application on the Graphistry server named in `OA2_HOST`, with exactly this redirect URI:

```
<OA2_REDIRECT_URL_BASE>/oauth/callback
```

For example, `https://louie.example.com/oauth/callback`. The scheme (`http` or `https`), the host, any port, and the path must match exactly. A mismatch shows as `Mismatching redirect URI` on the Graphistry sign-in page.

- **Graphistry Hub:** send your Graphistry contact the redirect URI, your Hub organization name, and the usernames to enable. They return the client ID and secret.
- **Self-hosted Graphistry:** follow [Authentication Registration & TLS](011_Authentication_Registration.md).

Put the client ID and secret in `custom.env`.

## 5. Set data permissions

```bash
cd /var/louie && sudo bash bin/data_permissions.sh
```

This gives the Louie containers' user (UID 1000) ownership of `/var/louie/data/data`.

## 6. Start Louie, then the sandbox service

Start Louie first. It creates the `louie_public` Docker network that the sandbox service joins.

```bash
cd /var/louie && sudo ./dc up -d --no-build --pull never
cd /var/dj    && sudo ./dc up -d --no-build --pull never
```

`--no-build --pull never` makes Docker use only the images you loaded, which matters on air-gapped hosts.

The containers restart automatically when Docker starts, so Louie comes back after a reboot.

## 7. Verify

1. All containers report `(healthy)` within a few minutes:

   ```bash
   docker ps --format 'table {{.Names}}\t{{.Status}}'
   ```

   You should see `louie-louie-1`, `louie-api-1`, `louie-caddy-1`, `dj-louie-maestro-1`, `dj-maestro-caddy-1`, and `dj-sandbox-reaper-1`.

2. The web server answers:

   ```bash
   curl -s -o /dev/null -w '%{http_code}\n' http://localhost/web-api/statuses/   # expect 200
   ```

3. Open `OA2_REDIRECT_URL_BASE` in a browser. You are sent to the Graphistry sign-in page and back to Louie.
4. Start a new thread and ask a simple question, which confirms the LLM connection.
5. Ask Louie to *"use Python to list the first 20 prime numbers"*, which confirms the sandbox service. A `louie-sandbox-<id>` container appears in `docker ps` while the code runs.

For HTTPS, set your hostname and certificates in `/var/louie/data/Caddyfile` (see [Authentication Registration & TLS](011_Authentication_Registration.md)), then restart with `cd /var/louie && sudo ./dc up -d --no-build --pull never caddy`.

## Upgrade

1. Back up your configuration and data:

   ```bash
   sudo tar -czf /root/louie-backup-$(date +%Y%m%d).tar.gz \
     /var/louie/system.env /var/louie/data /var/dj/.env /var/dj/sandbox.json /var/dj/sandbox.caddy.json
   ```

   `/var/louie/data` holds the user data, including the connector database (`/var/louie/data/data/connectors.db`). See also [Backups](027_Backups.md).

2. Load the new images, and unpack the new bulwarks tarball over the existing folders (steps 1 and 2). Your configuration files are kept.
3. Compare `/var/louie/system.env.example` and `/var/dj/env.example` with your files, and add any new settings you want. Check that the two sandbox paths from step 3 are still set.
4. Restart both services in order (step 6). `up -d` recreates the containers on the new images. Database migrations run automatically when Louie starts.
5. Verify (step 7).

To roll back, load the previous release's images, unpack its bulwarks tarball, restore the backup, and restart.

## Start, stop, and restart

```bash
cd /var/dj    && sudo ./dc down                                  # stop the sandbox service
cd /var/louie && sudo ./dc down                                  # stop Louie
cd /var/louie && sudo ./dc up -d --no-build --pull never         # start Louie first
cd /var/dj    && sudo ./dc up -d --no-build --pull never         # then the sandbox service
```

After changing `custom.env`, apply it with:

```bash
cd /var/louie && sudo ./dc up -d --no-build --pull never --force-recreate louie api
```

For more service commands, see [Launching](010_Logon_and_Services.md).

## Troubleshooting

| Symptom | Cause and fix |
|---------|---------------|
| Download returns HTTP 403 | The download links expired. Ask your Graphistry contact for new links. |
| Checksum does not match | The download is corrupted or incomplete. Download the file again. |
| `network louie_public declared as external, but could not be found` | The sandbox service was started before Louie. Start `/var/louie` first. |
| `Mismatching redirect URI` at sign-in | The URI registered on Graphistry is not exactly `<OA2_REDIRECT_URL_BASE>/oauth/callback`. |
| `invalid_client` at sign-in | `OA2_CLIENT_ID` or `OA2_CLIENT_SECRET` does not match the registered application. |
| Sign-in hangs or times out | The Louie host cannot reach `OA2_HOST` over HTTPS. Check firewalls and proxies. |
| Code runs fail, and `docker logs dj-louie-maestro-1` shows `None/sandbox/... includes invalid characters` | `DATA_ROOT_PATH` is not set in `/var/dj/.env`. Set both sandbox paths (step 3), then run `cd /var/dj && sudo ./dc up -d --no-build --pull never`. |
| Docker tries to pull or build images | Add `--no-build --pull never` to `./dc up`. |
| Port 80 or 443 already in use | Another web server is running. Stop it, or change the published ports in `/var/louie/docker-compose.yml`. |
| A container is not healthy | Run `docker logs <container name>` and send the output to your Graphistry contact. |

Some releases log `No account context available ... USER_CONFIGURE_LLM_MODELS is enabled` at startup even when that setting is off. This message does not indicate a problem.
