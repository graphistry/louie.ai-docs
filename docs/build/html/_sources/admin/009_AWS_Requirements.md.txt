# AWS Requirements

To deploy Louie on AWS, ensure the following requirements are met.

## Minimum Configuration

- **AWS Instance Type**: t3
- **Disk Space**: 20GB total
  - 15GB for the system
  - 5GB for data
- **CPU**: 4 vCPUs
- **RAM**: 4GB total
  - 3GB for the system
  - 1GB for usage

## Recommended Configuration

- **AWS Instance Type**: m6i
- **Disk Space**: 128GB+
- **CPU**: 8+ vCPUs
- **RAM**: 16+ GB
  - **Note**: Approximately 1GB RAM per active user.

## Security Groups and Ports

- **Web Users**: Allow HTTP/HTTPS traffic (Ports 80/443)
- **Admin Access**: Allow SSH access (Port 22)
- **Connectors**: Allow necessary ingress/egress for database connections

## Instance Creation

- **GPU Instances**: Contact us for information on GPU instance support.
- **LLM Self-Hosting**: Support for self-hosted LLMs is upcoming.
- **Cloud-Native Storage**: Upcoming features for cloud-native storage.

*Ensure proper security measures are in place, including firewalls and access controls.*