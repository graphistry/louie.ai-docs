# Backups

## Account Data, Connectors, and Metadata

- **Location**: Stored on the associated Graphistry account.
- **Backup Procedures**: Follow standard Graphistry backup procedures.
  - If using Graphistry Hub (cloud), backups run automatically.
- **Security**: Connector credentials are encrypted at rest and in transit.

## Data Threads (Louie Server)

- **Location**: Stored locally on the Louie server in `/var/louie/data`.
- **Configuration Files**: Include `/var/louie/.env`, `/var/louie/Caddyfile`, `/var/dj/sandbox.json`, `/var/dj/sandbox.caddy.json`.
- **Recommendation**: Regularly perform off-device backups using tools like `restic` or managed network storage.
  - Restic binaries and sample scripts are preinstalled; see `/var/louie/etc/scripts`.

## Upcoming Features

- **Cloud-Native Storage Drivers**: Contact us for information on upcoming support for cloud-native storage options.

*Ensure backups are secured and comply with your organization's data retention policies.*