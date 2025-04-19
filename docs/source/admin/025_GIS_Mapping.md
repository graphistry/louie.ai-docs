# GIS Mapping Service Configuration

Louie includes GIS mapping capabilities using Mapbox or alternative tile providers.

## Default Configuration

- Uses Graphistry’s Mapbox account.
- Users’ browsers fetch background map tiles from Mapbox.com.

## Switching to a Custom Mapbox Account

In `/var/louie/data/custom.env`, set:

```bash
KEPLER_MAPBOX_TOKEN="your_mapbox_token"
```

## Using an Alternative Tile Provider

- **Custom Tile Provider**:

  ```bash
  KEPLER_TILE_HOST="http://your_tile_service:8080"
  ```

- **OpenStreetMap (OSM)**:

  ```bash
  KEPLER_OPENSTREETMAP=true
  ```

## Restart Services

After making changes, restart the Louie service:

```bash
cd /var/louie
./dc up -d --force-recreate louie
```

*Contact staff for assistance with custom GIS mapping service configurations.*
