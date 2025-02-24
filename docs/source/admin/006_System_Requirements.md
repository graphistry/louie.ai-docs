# System Requirements

TODO(tcook):  combine with 009_AWS_Requirements.md and also rename from AWS so we can easily add Azure/others as they come along 

To self-host L.O.U.I.E., ensure the following system requirements are met:

## Minimum Requirements

- **AWS Instance Type**: t3
- **Disk Space**: 20GB total
  - 15GB for the system
  - 5GB for data
- **CPU**: 4 vCPUs
- **RAM**: 4GB total
  - 3GB for the system
  - 1GB for usage

## Recommended Requirements

- **AWS Instance Type**: m6i
- **Disk Space**: 128GB+
- **CPU**: 8+ vCPUs
- **RAM**: 16+ GB
  - **Note**: Approximately 1GB RAM per active user.

## Additional Notes

- **Graphistry Instance**: Requires a Graphistry Hub account or an AWS account with GPU quota.
- **LLM Providers**: Supports OpenAI, Azure OpenAI, Anthropic Claude, and Groq Mixtral. GPT-4 grade models are preferred.
- **Security Ports**:
  - **Web Users**: HTTP/HTTPS (Ports 80/443)
  - **Admin Access**: SSH (Port 22)
  - **Connectors**: Necessary ingress/egress for database connections.
- **Future Options**:
  - GPU instances and LLM self-hosting support are upcoming features.
