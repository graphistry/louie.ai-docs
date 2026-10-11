# Backups

## Account Data, Connectors, and Metadata

- **Location**: Stored on the associated Graphistry account.
- **Backup Procedures**: Follow standard Graphistry backup procedures.
  - If using Graphistry Hub (cloud), backups run automatically.
- **Security**: Connector credentials are encrypted at rest and in transit.

## Louie application database and files

- **Database**: Back up the configured Louie PostgreSQL database or SQLite
  file. It holds data such as data threads and skill metadata. The Helm chart
  does not create, back up, or restore PostgreSQL. For SQLite, use a
  consistent SQLite backup while writes are drained; do not copy a database
  over one opened by a running app Pod.
- **Files**: Back up data threads, assets, and file-backed skills from the
  effective `host-data` and `SKILL_FILE_STORAGE_PATH` locations. Skill
  database rows do not contain their `SKILL.md` or resource files. The
  default Helm `host-data` volume is `emptyDir` and disappears with its Pod;
  a new PVC does not inherit those files. Restore and verify them before
  starting replacement app containers.
- **Configuration**: Include `/var/louie/.env`, `/var/louie/Caddyfile`,
  `/var/dj/sandbox.json`, and `/var/dj/sandbox.caddy.json` where used. Store
  backups off-device with tools such as `restic` or managed network storage;
  sample scripts are in `/var/louie/etc/scripts`.

Before replacing an older API image that ran with
`USE_LOCAL_CONNECTOR_STORAGE`, `USER_CONFIGURE_LLM_MODELS`, and
`ENABLE_ORG_LLM_SETTINGS` all false, follow the
[worker-local recovery gate](https://github.com/graphistry/graphistrygpt/blob/6ab7afdf65480acd229ee3ee9d8803ab7271766c/helm/louie/README.md#worker-local-row-recovery-gate).
Each running worker may hold needed rows in its own temporary SQLite file;
a backup of the configured database cannot recover those rows. Block and
drain writes across old workers and the configured target, snapshot each
worker before it exits, and verify any reconciled rows and referenced files
on the replacement. If the workers' effective settings or write history are
unknown, use the same gate.

For a new PVC, seed the stopped workload's final paths before its app
containers start, then restore the intended replica count and verify
preexisting rows and file contents before reopening traffic. If rolling
back to an API image before #4077 with all three flags off, avoid serving
writes: that image cannot see configured-database records and writes to
worker-local temporary SQLite. Inventory any rollback workers before they
exit, recover needed rows, and return to an image containing the fix. See
the [Helm upgrade procedure](https://github.com/graphistry/graphistrygpt/blob/6ab7afdf65480acd229ee3ee9d8803ab7271766c/helm/louie/README.md#api-storage-selection-when-upgrading-the-app-image)
for the complete sequence.

## Upcoming Features

- **Cloud-Native Storage Drivers**: Contact us for information on upcoming support for cloud-native storage options.

*Ensure backups are secured and comply with your organization's data retention policies.*
