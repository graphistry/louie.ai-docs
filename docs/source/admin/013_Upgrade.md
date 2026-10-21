# Upgrade (Docker Compose)

Upgrade a Louie server that was installed from release tarballs to a newer release. Your settings, data, and port overrides are kept. Plan for a few minutes of downtime while the containers restart.

## Before you start

- Get both release files for the new version, and check their SHA-256 checksums. See [Release files](012_Docker_Compose_Install.md#release-files).
- Ask your Graphistry contact for the release notes. Look for new required settings and database changes.
- Make sure the host has room for the new images: about 30 GB free in the Docker data folder. To free space after the upgrade, see [Clean up old images](#clean-up-old-images).
- Note the current version:

  ```bash
  cat /var/louie/VERSION /var/louie/VERSION_DJ
  ```

## 1. Back up

Take a backup right before upgrading. Follow [Backup and Restore](027_Backups.md), or run your scheduled backup script by hand. Check that the new snapshot is listed:

```bash
sudo bash -c 'source /root/.louie-backup/env && restic snapshots --tag louie --latest 1'
```

The backup is how you roll back. New releases can change the database when they start, and an older release may not work with the changed database.

## 2. Load the new images

```bash
sudo docker load -i containers-<new version>-<timestamp>.tar.gz
```

The running containers are not affected until you restart them.

## 3. Unpack the new release files

```bash
mkdir -p /tmp/louie-release
tar -xzf louie-bulwarks-<new version>-<timestamp>.tar.gz -C /tmp/louie-release
sudo tar -xzf /tmp/louie-release/bulwarks-louie.tar.gz -C /var/louie
sudo tar -xzf /tmp/louie-release/bulwarks-dj.tar.gz -C /var/dj

cat /var/louie/VERSION /var/louie/VERSION_DJ /var/dj/VERSION
```

This replaces the compose files, scripts, and `*.example` templates. It does not touch these files, which the release files never contain:

- `/var/louie/system.env`, `/var/louie/data/custom.env`, `/var/louie/data/Caddyfile`
- `/var/dj/.env`, `/var/dj/sandbox.json`, `/var/dj/sandbox.caddy.json`
- `docker-compose.override.yml` in either folder
- Your data in `/var/louie/data/data`

## 4. Review settings

Compare the new templates with your files, and add any new settings you need:

```bash
sudo diff /var/louie/system.env.example /var/louie/system.env
sudo diff /var/dj/env.example /var/dj/.env
```

Check that the sandbox host paths are still set in `/var/dj/.env`. See [Sandbox: required settings](031_Sandbox_Network_Architecture.md#required-settings).

```bash
sudo grep -E '^(DATA_ROOT_PATH|SANDBOX_CADDYFILE_PATH)=' /var/dj/.env
```

## 5. Restart

Start Louie first, then the sandbox service. `up -d` recreates every container whose image or settings changed.

```bash
cd /var/louie && sudo bash bin/data_permissions.sh
cd /var/louie && sudo ./dc up -d --no-build --pull never
cd /var/dj    && sudo ./dc up -d --no-build --pull never
```

Database changes run automatically when Louie starts. Watch for them with `docker logs -f louie-louie-1`.

## 6. Verify

Run the checks in [Docker Compose Install: Verify](012_Docker_Compose_Install.md#7-verify):

- Containers are healthy.
- Sign-in works.
- A chat answers.
- A Python code run works.
- Earlier threads are still there.

Then confirm the new version:

```bash
cat /var/louie/VERSION
docker ps --format 'table {{.Names}}\t{{.Image}}'
```

## Roll back

If the new release does not work, return to the previous one:

1. Stop both services:

   ```bash
   cd /var/dj    && sudo ./dc down
   cd /var/louie && sudo ./dc down
   ```

2. Unpack the previous release's bulwarks file over `/var/louie` and `/var/dj` (step 3). Load its images too, if you have removed them.
3. Restore the backup taken in step 1, following [Backup and Restore: Restore](027_Backups.md#4-restore). This brings back the data as it was before the database changed.
4. Start Louie, then the sandbox service, and verify.

## Clean up old images

After the new release has run well for a while, remove the previous version's images to free disk space. List them, then remove the ones tagged with the old versions:

```bash
docker images --format '{{.Repository}}:{{.Tag}}\t{{.Size}}' | grep -E 'graphistry/louie'
sudo docker rmi graphistry/louie:<old version> graphistry/louie-caddy:<old version>
```

The sandbox images (`graphistry/louie-sandbox`, `graphistry/louie-maestro`) have their own versions, listed in `/var/louie/VERSION_DJ`. Remove an old one only if the version differs from the current one.
