
# Launching

Containers automatically start on boot. To verify the status and manage the services, follow the steps below.


## URLs

- **Louie Main Landing Page**: `https://<your_site>`
- **API Documentation & Playground**: `https://<your_site>/api/docs`
  - Uses Graphistry JWT authentication.
  - Includes OpenAPI JSON specification.

## Logging into server

```
ssh -i my_key.pem ubuntu@my.public.ip
```

Containers automatically starts on boot

## Service Directories

- **Louie Services** (`/var/louie`):
  - `louie`
  - `api`
  - `caddy`
- **DJ Services** (`/var/dj`):
  - `louie-maestro`
  - `maestro-caddy`
- **Sandbox Instances**:
  - `louie-sandbox-<id>`
  - `louie-caddy-sandbox-<id>`


## Managing Services with Docker Compose


### `dc` alias

Use `./dc` script as a shorter alias for running `docker compose` commands in both directories

### Checking Container Status - List all running containers:

```bash
docker ps
```

### Check the status of services

```bash
cd /var/louie && docker compose ps
cd /var/dj && docker compose ps
```

### View Logs

```bash
./dc logs -f -t --tail=100 caddy
```

### Restarting Louie

Navigate to the Louie directory and restart the services:

```bash
cd /var/louie/
./dc up -d --force-recreate louie api caddy
```


### Upcoming - Contact for more information

GPU instances
LLM self-hosting
Cloud-native storage

