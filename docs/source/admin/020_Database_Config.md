# Database Server Configuration

Louie database configuration is in-tool.

Older versions of Louie supported setting database connection information via a deprecated environment variables mode.

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
curl -u admin:changme  https://splunk.host.name.here:8089/services/search/jobs/export  -d search="search * | head 3" -d output_mode=csv`
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

Benefits of database-managed connectors over environment variables are features like automatic secret encryption and easier standup of new instances through automatic profile reuse.


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

```bash
SPARK_TOKEN="dapi...your_token..."
SPARK_WORKSPACE_ID="your_workspace_id"
SPARK_HOST="your_databricks_host.cloud.databricks.com"
```

*Restart services after making changes.*

### Other databases

Contact staff. (Warning: Deprecated.)