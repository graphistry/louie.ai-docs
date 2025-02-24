# Custom JWT Refresh (Optional)

You can configure the JWT token refresh interval to ensure tokens are refreshed before they expire.

## Steps

1. **Edit the Configuration File**: `/var/louie/data/custom.env`

   ```bash
   JWT_REFRESH_S=1800  # Refresh tokens 30 minutes before expiration
   ```

   - Adjust `JWT_REFRESH_S` based on the `GRAPHISTRY_JWT_EXPIRATION_DELTA` set in your Graphistry server.

2. **Restart the Server**:

   ```bash
   cd /var/louie
   ./dc up -d --force-recreate caddy louie
   ```

*This setting helps maintain continuous authentication without interruption.*