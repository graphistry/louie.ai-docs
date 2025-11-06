# Security Decisions

## Hosting

**Graphistry:** Accounts, DB, graph visualizations
- SaaS: hub.graphistry.com
- AWS/Azure Marketplace (single-node)
- Manual: docker-compose, kubernetes

**Louie:** Application
- SaaS: louie.ai
- AWS Marketplace
- Manual: docker-compose
- Whether to enable sandboxed Python

**OpenSearch:** Optional - conversational memory & text indexing
- AWS managed service
- Self-hosted

**Off-node storage & backups**
- Graphistry; aws/azure/gcp; manual restic

## Authentication

- Built-in (user/pass)
- SSO (OIDC)

**Note:** Configure OAuth2 between Louie<>Graphistry

## Connectors

- Ensure Louie <> API/DBs
- Decide shared read-only service account vs per-user DB connections

## Authorization

**Sharing units:** Individuals, Organization(s)

## Web

Ensure user, admin access to each component: Graphistry, Louie, physical/cloud resources, OS, connectors

## Guard Rails

See UI Guide section on Guard Rails
