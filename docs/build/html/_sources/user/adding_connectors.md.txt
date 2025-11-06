# Adding Data Connectors

This guide walks you through the process of adding new data connectors to your Louie.AI organization.

## Step 1: Access Connector Management

1. Navigate to your organization's main interface
2. Look for the connector status panel (usually on the left side)
3. Click the **"+ ADD CONNECTOR"** button

## Step 2: Select Connector Type

The "Select a Connector Type" dialog will display all available connectors:


Choose from the available options:
- **Databricks** - Lakehouse-scale analytics
- **Neptune** - Amazon's graph database
- **OpenSearch** - Vector search engine
- **Splunk** - Real-time observability & security
- **Spanner** - Google Cloud distributed database
- **PostgreSQL** - Open-source relational database
- **MySQL** - Popular relational database
- **MSSQL** - Microsoft SQL Server
- **BigQuery** - Google's analytics data warehouse
- **CockroachDB** - Distributed SQL database

## Step 3: Configure Connection Settings

After selecting a connector type, you'll see a configuration form specific to that connector. 

### Example: Google Cloud Spanner Configuration


For Spanner, you'll need to provide:
- **Name** - A descriptive name for your connector
- **Instance ID** - The Spanner instance identifier
- **Database ID** - The specific database name
- **Service-Account JSON** - Authentication credentials

### Common Configuration Fields

Most connectors require similar information:
- **Connection Name** - A friendly name for identification
- **Host/Server** - The database server address
- **Port** - Connection port (if applicable)
- **Database Name** - The specific database to connect to
- **Authentication** - Username/password or service account credentials

## Step 4: Test and Save

1. Fill in all required fields (marked with red asterisks)
2. Use the **"View"** button to preview JSON configurations if available
3. Click **"Dry Run Changes"** to test the connection
4. If the test is successful, click **"Save"** to create the connector

## Step 5: Verify Connection

After saving:
1. The new connector should appear in your connector list
2. Check that the status indicator shows as healthy (green)
3. If there are issues, you can edit the connector settings, check the logs for error details, or ask Louie to re-index

## Managing Existing Connectors

- **Edit** - Click the settings icon next to a connector to modify its configuration
- **Re-index** - Ask Louie to refresh the connector if data seems outdated
- **Status Monitoring** - Keep an eye on connector health indicators

## Troubleshooting

If you encounter issues:
- Verify all required fields are filled correctly
- Check network connectivity to your data source
- Ensure authentication credentials are valid and have proper permissions
- Contact your administrator if you need help with service account setup

## Best Practices

- Use descriptive names for your connectors
- Test connections before saving
- Regularly monitor connector health
- Keep authentication credentials secure and up to date
- Document any special configuration requirements for your team 