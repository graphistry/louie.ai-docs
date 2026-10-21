# Backup and Restore

Back up a Docker Compose Louie server with [restic](https://restic.net/). Restic makes encrypted, deduplicated snapshots and can store them on local or mounted disks, SFTP servers, or cloud object storage. These steps were tested with restic 0.17.

## What to back up

| Data | Location | Notes |
|------|----------|-------|
| Accounts, organizations, sign-in, and database connectors | Graphistry server | Back up with the Graphistry server's own procedure. Graphistry Hub backs up automatically. |
| Data threads, uploaded files, logs, and the Louie database | `/var/louie/data/data/` | Louie's local database is `connectors.db` (SQLite). It holds LLM and organization settings, skills, and conversation history saved on this server. |
| Louie settings | `/var/louie/system.env`, `/var/louie/data/custom.env`, `/var/louie/data/Caddyfile` | `custom.env` holds `JWT_SECRET_LOUIE`, which is needed to read saved credentials after a restore |
| Sandbox settings | `/var/dj/.env`, `/var/dj/sandbox.json`, `/var/dj/sandbox.caddy.json` | |
| Port overrides, if used | `/var/louie/docker-compose.override.yml`, `/var/dj/docker-compose.override.yml` | See [Change the default ports](012_Docker_Compose_Install.md#change-the-default-ports) |

The container images and the files from the release tarball are not backed up. Keep the release files for the version you run, or get them again from Graphistry.

A backup contains secrets, including the OAuth client secret, LLM keys, and `JWT_SECRET_LOUIE`. Restic encrypts every snapshot with the repository password. Store that password separately from the backups: if it is lost, the backups cannot be read.

## 1. Install restic

Install it from your distribution's packages (for example `sudo apt install restic`), or copy the single `restic` binary from [restic releases](https://github.com/restic/restic/releases) to `/usr/local/bin/`. For air-gapped hosts, download the binary and its `SHA256SUMS` on another machine, verify it, and copy it over.

## 2. Create a repository

Pick where backups go and set `RESTIC_REPOSITORY`:

| Destination | `RESTIC_REPOSITORY` example | Also needs |
|-------------|----------------------------|------------|
| Local or mounted disk, NFS | `/mnt/backup/louie` | Use a different disk or machine than `/var/louie` |
| SFTP server | `sftp:backup@backup-host:/srv/restic/louie` | SSH key access |
| Amazon S3 or S3-compatible | `s3:s3.amazonaws.com/<bucket>/louie` | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` |
| Azure Blob Storage | `azure:<container>:/louie` | `AZURE_ACCOUNT_NAME`, `AZURE_ACCOUNT_KEY` |
| Google Cloud Storage | `gs:<bucket>:/louie` | `GOOGLE_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS` |

See the [restic repository documentation](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html) for all options.

Keep the settings in a root-only file so they stay out of shell history:

```bash
sudo install -d -m 700 /root/.louie-backup
openssl rand -hex 32 | sudo tee /root/.louie-backup/password > /dev/null
sudo chmod 600 /root/.louie-backup/password

sudo tee /root/.louie-backup/env > /dev/null <<'EOF'
export RESTIC_REPOSITORY=/mnt/backup/louie
export RESTIC_PASSWORD_FILE=/root/.louie-backup/password
# Cloud repositories: add the credentials from the table above
EOF
sudo chmod 600 /root/.louie-backup/env
```

Copy the password file somewhere safe, away from this server. Then create the repository:

```bash
sudo bash -c 'source /root/.louie-backup/env && restic init'
```

## 3. Back up

The Louie app and API write to the connector database. Stop them for the few seconds the backup takes, so the snapshot is consistent. Users see a short interruption.

```bash
sudo bash -c '
  source /root/.louie-backup/env
  cd /var/louie && DC_SILENT=1 ./dc stop louie api
  restic backup --tag louie \
    /var/louie/system.env /var/louie/data \
    /var/dj/.env /var/dj/sandbox.json /var/dj/sandbox.caddy.json \
    $(ls /var/louie/docker-compose.override.yml /var/dj/docker-compose.override.yml 2>/dev/null)
  cd /var/louie && DC_SILENT=1 ./dc start louie api
'
```

Check the result:

```bash
sudo bash -c 'source /root/.louie-backup/env && restic snapshots --tag louie && restic check'
```

### Schedule it

Save the backup command above as `/root/.louie-backup/backup.sh` (`chmod 700`), and run it nightly from root's crontab (`sudo crontab -e`):

```
30 2 * * * /root/.louie-backup/backup.sh >> /var/log/louie-backup.log 2>&1
```

### Keep a limited history

```bash
sudo bash -c 'source /root/.louie-backup/env && restic forget --tag louie --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune'
```

You can add this line to the end of `backup.sh`.

## 4. Restore

Restore onto the same Louie version that made the backup. If you are rebuilding a server, first install that version from its release files, following steps 1 and 2 of [Docker Compose Install (Tarball)](012_Docker_Compose_Install.md): load the images and unpack.

1. Stop both services:

   ```bash
   cd /var/dj    && sudo ./dc down
   cd /var/louie && sudo ./dc down
   ```

2. List the snapshots, and pick one:

   ```bash
   sudo bash -c 'source /root/.louie-backup/env && restic snapshots --tag louie'
   ```

3. Restore it to its original paths. Use `latest` or a snapshot ID:

   ```bash
   sudo bash -c 'source /root/.louie-backup/env && restic restore latest --tag louie --target /'
   ```

   Restic restores file ownership and permissions when run as root. Files that exist in the snapshot replace the current ones. Files that are not in the snapshot are left in place.

4. Reset data permissions, then start Louie first and the sandbox service second:

   ```bash
   cd /var/louie && sudo bash bin/data_permissions.sh
   cd /var/louie && sudo ./dc up -d --no-build --pull never
   cd /var/dj    && sudo ./dc up -d --no-build --pull never
   ```

5. Verify as in [Docker Compose Install (Tarball)](012_Docker_Compose_Install.md): containers are healthy, sign-in works, and earlier threads and saved connectors are present.

To restore a single file instead, for example an older `custom.env`, restore into a temporary folder and copy what you need:

```bash
sudo bash -c 'source /root/.louie-backup/env && restic restore latest --tag louie --target /tmp/louie-restore --include /var/louie/data/custom.env'
```

Delete the temporary folder afterwards, because it contains secrets.

## AWS Marketplace image

Servers launched from the Louie AWS Marketplace image also include restic helper scripts in `/var/louie/etc/scripts`. The commands on this page work on those servers too.
