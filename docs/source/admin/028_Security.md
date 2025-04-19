# Security Overview


Components

Louie
Standalone webapp
DB Connectors; Memory; Storage
Self-hosted or louie.ai

Graphistry - reuses for sensitive deps
Standalone webapp
Auth, DB, and viz
Self-hosted or hub.graphistry.com

AI
Via API
OpenAI, Azure OpenAI, others TBA: Any LangChain-compatible
Louie.ai-provided or BYO
Authentication & encryption
TLS, SSO (OIDC), JWT; Reuses Graphistry auth
Example: okta.acme.com -[OIDC]->  hub.graphistry.com -[OAuth2]-> Louie.ai
Secrets encrypted in Graphistry (at-rest + in-flight) & decrypted in Louie.AI

Authorization
RBAC
Organizations
LLM data access: “off”, “metadata”, “any data”

Connectors
Databases, SaaS APIs, BYO LLMs, …
Recommend read-only service account or per-user

Air gapping: Contact

SECURITY PROGRAM
Louie.AI uses Graphistry for accounts, DB, …
Continuous compliance (Drata)
Annual pen testing
Standard policies: Working to SOC2
