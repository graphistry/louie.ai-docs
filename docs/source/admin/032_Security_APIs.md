
# Security APIs

## Auth & logs


Authentication
JWT
Generate tokens via user/pass, SSO, and personal API key
Language-neutral REST, +  convenient clients in Python, JS
https://hub.graphistry.com/docs/api/1/rest/auth/

Logging & monitoring
Add /health to your Caddyfile to expose (example available)
Docker containers report health status (30s) and autorestart
Docker logging, with INFO+ containing login audit trails
Standard Docker log forwarding, e.g., Splunk or sidecars


## Introspection API


API: /api/capabilities

API UI at /api/docs
 Site staff/admins see site 
configuration & capabilities 

Org admins see org capabilities

Note: Does not support SSO

 
```bash
curl -X 'GET' \
  'http://localhost:8000/api/capabilities' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer ***'
```

=>

```json
{
  "site": {
    "auth_host": "https://www.zzz.gov.uk",
    "llm_privacy_level": "NO_LLM",
  },
  "org": {
    "connectors": [
      {
        "id": "d1603ce3-3074-4de9-8982-20c8dab7fd78",
        "type": "DatabricksConnectorConfig",
        "title": "zzz",
        "connected": true
      }
    ],
    "tools": [
      {"name": "DatabricksPassthroughAgent"},
    ],
    "models": [],
    "model_prefs": { }
  }
}
```

## Test items disabled


API
/api/docs
Test specific agents via API & its UI
Success status in last JSON item  

```json
[
  {
    "dthread_id": null
  },
  {
    "success": false,
    "error": "Agent not found: TextAgent"
  }
]
```

JWT token

Query + agent

Run
