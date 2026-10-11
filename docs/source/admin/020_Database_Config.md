# Database Server Configuration

Louie database connections are configured within the Louie UI.

Older versions of Louie supported setting database connection information via environment variables (now deprecated).

## Key concepts

Louie connectors are database-managed by the paired Graphistry server.

Connectors are associated with each organization or personal account.

A benefit of managed connectors is new Louie servers can be stood up with existing connector information already stored in the Graphistry server.

Louie will crawl a database upon first connection by a user so that Loiue will see what they can see.

### Known limitations

Currently, only one connector of each type can be loaded.

## System configuration

To configure Graphistry-managed connectors, set the following in `/var/louie/data/custom.env`:

```bash
USE_MANAGED_CONNECTORS=True
GRAPHISTRY_ENCRYPTION_KEYS="your_encryption_keys"
GRAPHISTRY_SIGNING_KEY="your_signing_key"
GRAPHISTRY_SIGNING_SALT="your_signing_salt"
```

You can find these in your [Graphistry configuration files](https://graphistry-admin-docs.readthedocs.io/en/latest/app-config/connector-management.html).

Restart services after making changes.

Contact Graphistry staff for assistance with managed connectors and Databricks configuration.

## Louie's application database

This database stores Louie data such as data threads, skills, and locally
managed connector or LLM settings. It is separate from the databases and
Splunk instances that users add as connectors. Choose its backend with
`DATABASE_TYPE` and the matching database settings for your deployment.
PostgreSQL can be shared by API workers and replicas. A configured SQLite
database persists across worker restarts when its file is on durable storage;
in Kubernetes, the default `host-data` volume is an `emptyDir`, so enable a
PVC with `persistence.enabled` or `persistence.existingClaim` before relying
on persistence across Pod replacement.

An API image containing [#4077](https://github.com/graphistry/graphistrygpt/pull/4077)
uses the configured application database even when
`USE_LOCAL_CONNECTOR_STORAGE`, `USER_CONFIGURE_LLM_MODELS`, and
`ENABLE_ORG_LLM_SETTINGS` are **all false**. Older API images in that exact
configuration used a separate temporary SQLite database in each worker.
Upgrading does not transfer those temporary rows. While old workers are
still running, block and drain writes, inventory and back up each worker's
temporary database, and reconcile any needed rows into the configured
database before replacing the workers. Rows belonging to workers that
already stopped may be unrecoverable. See the
[Helm worker-local recovery gate](https://github.com/graphistry/graphistrygpt/blob/6ab7afdf65480acd229ee3ee9d8803ab7271766c/helm/louie/README.md#worker-local-row-recovery-gate)
for the full procedure.

Prepare and migrate the configured database before serving API traffic.
The API waits for its schema to reach the Alembic head and fails startup if
it does not become ready within the configured window; API workers do not
run migrations concurrently. `API_DB_SCHEMA_WAIT_SECONDS` defaults to 240
seconds, with a minimum of two seconds for PostgreSQL or one for SQLite.
If a migration needs longer, increase the wait and the serving process's
startup timeout together. For PostgreSQL, connection and statement probes
use `API_DB_SCHEMA_PROBE_TIMEOUT_SECONDS` (five seconds by default), with
`API_DB_SCHEMA_PROBE_WALL_SECONDS` (30 seconds by default) bounding each
probe process. These settings do not replace the overall schema wait.

Check the **app image** before rollout: chart `0.1.21` still defaults to
Louie image `0.18.15`, which does not contain #4077. Set `image.tag` to a
released image containing the change; installing the chart alone does not
change old API behavior. Follow the
[Helm database upgrade procedure](https://github.com/graphistry/graphistrygpt/blob/6ab7afdf65480acd229ee3ee9d8803ab7271766c/helm/louie/README.md#api-storage-selection-when-upgrading-the-app-image)
for backup, restore, and validation steps.

## Indexing

Louie builds a semantic layer to understand what is in the database by gathering database schemas and samples. When a connector is per-user, meaning different users may have different data available, Loiue will index on a per-connecting-user basis. 

Indexing occurs at connector creation time and on account login.

Users can always reindex via the connector panel.

## Security

- Authentication

    Connectors such as Databricks support federated authentication. For example,  each database user can use their own Databricks SSO or personal PAT token, and thus securely use only the data allowed by Databricks Unity Catalog.

    We generally recommend limiting database user privileges. For example, limit service accounts to read-only access, and consider using multiple organizations, each with a different database profiles.

- Secrets encryption

    Sensitive connector information stored in Graphistry is encrypted both at rest and in database memory.

- Secure protocols

   Louie connects to Graphistry as part of its OAuth2 flow, and then connector access is access controlled by the usual organization and user level RBAC. All traffic is with TLS.

## Setting up and testing a connector

The connector management panel can be reached from the Louie UI on the bottom-left by expanding the connector panel. Connectors can be inspected, created, edited, and removed from the connector management panel.

The asset log tab in the connector panel is especially useful as a way to monitor indexing behavior or connection errors.

## Database Connector Configuration

### Databricks

The standard flow enables Databricks SSO and Unity Catalog.

1. Configure Databricks:

  - Go to `Manage Account->Settings->App Connections->Add Connection` 

    - Give it an Application Name

    - Set the redirect URL to: 
https://${LOUIE_HOSTNAME}/plugin/oauth/callback

    - Select “All APIs” for the Access Scope

    - **Uncheck** Generate a client secret 

    - Click `Add`, and save the generated `Client ID` for the following step 

      For more information, see [Enable or disable partner OAuth applications](https://docs.databricks.com/en/integrations/enable-disable-oauth.html#enable-custom-oauth-applications-using-the-databricks-ui)


2. Configure Louie:

    - `Add connector -> Databricks`

      - Name of your choice

      - Host: `your_databricks_host.cloud.databricks.com`

      - Workspace ID: `your_workspace_id`

      - Cluster ID: `your_cluster_id`
        - Tip: When inspecting a `Shared Compute Cluster` in Databricks, the url will be like `https://your_databricks_host.cloud.databricks.com/compute/cluster/12345678`, where `12345678` is the cluster ID.

      - Pick Token Auth, SSO Auth, or PAT Table Auth (predefined JSON table of per-user PAT tokens). Contact staff for more information here.

    - Save and start indexing. When indexing is done, the status indicator in the bottom left panel will switch from in-progress to green.

3. Try several test queries once the connector status in the bottom left area goes green:

  - `Hey Louie, what is in Databricks?`

  - `Great, pull 10 rows from table <table_name>`


### Splunk

1. Ensure your Splunk account is setup for use:


    - Ensure the REST API port (default: 8089) is open

      - Splunk Cloud: [Contact Splunk](https://docs.splunk.com/Documentation/SplunkCloud/latest/RESTTUT/RESTandCloud)

   - Authorize your Splunk user for REST API access and the intended default search indexes

    - Test Splunk is reachable and the account is authorized from your Louie server:

```bash
curl -u ${SPUNK_USER}:${SPLUNK_PASSWORD} https://splunk.host.name.here:8089/services/search/jobs/export  -d search="search * | head 3" -d output_mode=csv`
```


2. Configure Louie for Splunk:

    - `Add connector -> Splunk`

      - Host: `your_splunk_host`
      - API Port: `8089`
      - Protocol: `https`
      - Username/Password: Your service account

    - Save and start indexing. When indexing is done, the status indicator in the bottom left panel will switch from in-progress to green.

3. Try several test queries once the connector status in the bottom left area goes green:

  - `Hey Louie, what is in Splunk?`

  - `Great, pull 10 rows from index <index_name>`


## Deprecated: Connections as environment variables

We encourage users to switch to database-managed connectors.

Benefits of database-managed connectors over environment variables are features like automatic secret encryption and easier deployment of new instances through automatic profile reuse.


### Edit Configuration File


Modify the `/var/louie/data/custom.env` file with your database settings.

### Restart Services

After making changes, restart the Louie and API services:

```bash
cd /var/louie
./dc up -d --force-recreate louie api
```

### Ex: Databricks Configuration

#### Mode 1: Per-User Databricks SSO Authentication

1. **Create an App Connection in Databricks:**

   - Navigate to **Manage Account** > **Settings** > **App Connections** > **Add Connection**.
   - Provide an **Application Name**.
   - Set the **Redirect URL** to:

     ```
     https://<your_louie_server>/sso/databricks/callback
     ```

   - Select **All APIs** for the Access Scope.
   - Uncheck **Generate a client secret**.
   - Click **Add** and copy the generated **Client ID**.

2. **Configure Louie:**

   In `/var/louie/data/custom.env`, set:

   ```bash
   SPARK_TOKEN=""  # Note this is set to an empty string
   SPARK_HOST="your_databricks_host.cloud.databricks.com"
   SPARK_WORKSPACE_ID="your_workspace_id"
   DATABRICKS_OAUTH_CLIENT_ID="your_client_id"
   ```

3. **Restart Services:**

   ```bash
   cd /var/louie
   ./dc up -d --force-recreate louie api
   ```

*Ensure that the Databricks instance is reachable by the Louie server for authentication.*

#### Mode 2: Shared Service Account (Not Recommended for High-Security Environments)

1. **Configure Louie:**

   In `/var/louie/data/custom.env`, set:

```bash
SPARK_TOKEN="dapi...your_token..."
SPARK_WORKSPACE_ID="your_workspace_id"
SPARK_HOST="your_databricks_host.cloud.databricks.com"
```

2. **Restart Services:**

   ```bash
   cd /var/louie
   ./dc up -d --force-recreate louie api
   ```


### Other databases

Contact staff.
