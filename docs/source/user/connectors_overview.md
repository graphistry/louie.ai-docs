# Data Connectors

Louie.AI supports a wide variety of data connectors that allow you to connect to different data sources and services. These connectors provide seamless access to your data for analysis and visualization.

## Available Connectors

### Database Connectors
- **MySQL** - Connect to MySQL, the open-source relational database
- **PostgreSQL** - Connect to PostgreSQL, the open-source relational database  
- **MSSQL** - Connect to Microsoft SQL Server
- **BigQuery** - Run interactive petabyte-scale analytics in BigQuery SQL
- **CockroachDB** - Connect to CockroachDB, the distributed, resilient relational database

### Cloud & Analytics Platforms
- **Databricks** - Run lakehouse-scale analytics with a unified SQL interface
- **Spanner** - Configuration for Google Cloud Spanner
- **Splunk** - Splunk search for real-time observability & security analytics

### Graph & Vector Databases
- **Neptune** - Visualize network relationships in Amazon's Neptune graph database
- **OpenSearch** - Vector search and analyze massive datasets with an open-source engine

## Connector Status

Connectors display their health status in the interface:
- **Green indicators** - Healthy connections
- **Other indicators** - May require attention or re-indexing

You can ask Louie to re-index connectors when needed to refresh the connection and data availability.

## Getting Started

To add a new connector to your organization:
1. Click the **"+ ADD CONNECTOR"** button
2. Select your desired connector type
3. Configure the connection settings
4. Test and save the connection
