# Network Architecture


## AWS

Louie deployment in AWS involves several components configured within an AWS Tenant:

- **AWS Tenant**: The main AWS environment where Louie is deployed.
- **Firewall**: VPN for web users to securely access the application.
- **Louie EC2 Instance**: Hosts the Louie application.
- **Graphistry EC2 Instance**: Hosts the Graphistry server for visualization and authentication services.
- **SSO**: Single Sign-On integration with your organization's identity provider.

**Data Flow Diagram:**

![Network Architecture](../images/Louie_Network_Architecture.png)


