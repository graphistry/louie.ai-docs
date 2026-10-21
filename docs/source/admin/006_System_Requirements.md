# System Requirements

To self-host Louie, ensure the following system requirements are met:

## Recommended Requirements

Ex: AWS instance type m6i

- **Disk Space**: 128GB+
- **CPU**: 8+ vCPUs
- **RAM**: 16+ GB

### Scaling

Increase RAM and cores by active users. Louie aggressively pages out inactive sessions and uses a reactive execution model, so if you are familiar with Python notebooks like Jupyter, you can plan utilization by thinking of Louie as a more resource-efficient version.

## Minimum Requirements

Ex: AWS t3 instance

- **Disk Space**: 20GB total
  - 15GB for the system
  - 5GB for data
- **CPU**: 4 vCPUs
- **RAM**: 4GB total
  - 3GB for the system
  - 1GB for usage

## Docker Compose Installs

The container images need about 30GB of free disk in the Docker data folder, in addition to data. Docker Engine 24+ with the Compose v2 plugin is required. See [Docker Compose Install (Tarball)](012_Docker_Compose_Install.md).

## Additional Notes

- **Graphistry Instance**: Requires a Graphistry Hub account or self-hosting a Graphistry GPU server (cloud, on-prem)
- **LLM Providers**: Supports OpenAI, Azure OpenAI, Anthropic Claude, Groq, and more. GPT-4o+ grade models are preferred.
- **Security Ports**:
  - **Web Users**: HTTP/HTTPS (Ports 80/443)
  - **Admin Access**: SSH (Port 22)
  - **Sandbox service (Docker Compose installs)**: Ports 8081 and 8082 must be free on the host; users do not need to reach them
  - **Connectors**: Necessary ingress/egress for database connections.
- **Future Options**:
  - GPU instances and LLM self-hosting support are upcoming features.
