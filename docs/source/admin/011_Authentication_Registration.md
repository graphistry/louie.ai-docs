# Authentication Registration & TLS

Configuration file: `/var/louie/data/custom.env`

## 1. Setup Authentication

**Note:** The application requires authentication to load.

### If Using Graphistry Hub (Default)

- Create a free or paid Hub account at [graphistry.com/get-started](https://graphistry.com/get-started).
- No additional configuration is necessary for authentication.

### If Using a Single Hub User (Experimental)

- Set the `GRAPHISTRY_*` fields with your hub.graphistry.com credentials for a global user.

## 2. Set Your Louie URL

Include the protocol in the `custom.env` file:

```bash
OA2_REDIRECT_URL_BASE='https://your.louie-server.xyz'
```

## 3. Setup DNS & TLS

Configure custom DNS and TLS in `/var/louie/data/Caddyfile`, similar to the Graphistry server configuration.

## 4. Restart the Server

```bash
cd /var/louie
./dc up -d --force-recreate caddy louie
```

## 5. Notify Graphistry Server Administrator

Provide the following information:

- `OA2_REDIRECT_URL_BASE` setting
- Organization name
- Usernames

---

## Configuring Private Graphistry Servers as OAuth2 Provider for Louie

**Skip this section if using Graphistry Hub.**

Louie user authentication is handled from a Graphistry server, such as via Graphistry Hub or a self-hosted Graphistry server. Graphistry server accounts support username/pass, SSO, and API keys.

### If using Graphistry Hub (https://www.graphistry.com/get-started):

Notify Graphistry staff with your:
- OA2_REDIRECT_URL_BASE (previous slide) 	
- Graphistry Hub org name
- Graphistry Hub username(s)

### If self-hosting Graphistry:

Configure your self-hosted Graphistry to be an OAuth2 provider for Louie

TODO(tcook): add screenshots

### Steps:

1. **Access Graphistry Server Administration Panel.**

2. **Create a New OAuth2 Client:**

   - Set **User** to admin ID (typically `1`).
   - Set **Redirect URIs** to your Louie server URL.
   - Set **Confidential** and **Authorization Code** grant type.
   - Provide a name (e.g., "Louie OAuth2 Client").
   - Set **Algorithm** to `HS256` (HMAC with SHA-256).

3. **Save the Client ID & Client Secret:**

   - The client secret will be hashed and inaccessible after saving, so make sure to record it.

4. **Update Louie Configuration:**

   - In `/var/louie/data/custom.env`, set:

     ```bash
     OA2_HOST='https://your.graphistry-server.xyz'
     OA2_CLIENT_ID='your_client_id'
     OA2_CLIENT_SECRET='your_client_secret'
     ```

5. **Restart the Louie Server:**

   ```bash
   cd /var/louie
   ./dc up -d --force-recreate caddy louie
   ```

*Ensure that the Louie server URL is correctly set and that it matches the redirect URIs configured in the OAuth2 client.*