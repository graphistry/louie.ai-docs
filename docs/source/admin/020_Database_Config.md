# Database Server Configuration

To update the database server configuration, follow these steps:

## Edit Configuration File

Modify the `/var/louie/data/custom.env` file with your database settings.

## Restart Services

After making changes, restart the Louie and API services:

```bash
cd /var/louie
./dc up -d --force-recreate louie api
```

## Databricks Configuration

### Mode 1: Per-User Databricks SSO Authentication

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

### Mode 2: Shared Service Account (Not Recommended for High-Security Environments)

```bash
SPARK_TOKEN="dapi...your_token..."
SPARK_WORKSPACE_ID="your_workspace_id"
SPARK_HOST="your_databricks_host.cloud.databricks.com"
```

*Restart services after making changes.*

## Managed Connectors

To use Graphistry-managed connectors, configure the following in `/var/louie/data/custom.env`:

```bash
USE_MANAGED_CONNECTORS=True
GRAPHISTRY_ENCRYPTION_KEYS="your_encryption_keys"
GRAPHISTRY_SIGNING_KEY="your_signing_key"
GRAPHISTRY_SIGNING_SALT="your_signing_salt"
```

*Restart services after making changes.*

*Contact Graphistry staff for assistance with managed connectors and Databricks configuration.*
