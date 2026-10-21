# Changelog

All notable changes to this repo are documented in this file.

The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and all PyGraphistry-specific breaking changes are explictly noted here.

## [Development]

### Added

* Admin guide: Docker Compose install from release tarballs, including air-gapped hosts, upgrade, and troubleshooting (`012_Docker_Compose_Install`), listed under Deployment with Distributions
* Admin guide: Upgrade page (`013_Upgrade`): backup, load, unpack, settings review, restart order, verification, rollback, old image cleanup
* Admin guide: Sandbox page (`031_Sandbox_Network_Architecture`, was a stub): components, per-run isolation and mounts, required host paths, resource limits, ports and firewall, reaper cleanup, verification, troubleshooting
* Admin guide: changing default host ports (80/443/8081/8082) with `docker-compose.override.yml`, kept across upgrades
* User guide: Skills overview (`069_Skills`) and Skill Authoring guide (`070_Skill_Authoring`), under Advanced Topics
* Integration guide: launch templated Louie investigations from external applications, with a Splunk recipe (`071_Launch_Deep_Links`)

### Fixed

* Admin guide: Backup and Restore (`027_Backups`) rewritten with tested restic commands for Docker Compose installs, including what to back up, scheduling, retention, and full and single-file restore; replaces outdated paths (`/var/louie/.env`, `/var/louie/Caddyfile`)
* Admin guide: Supported LLMs (`007_LLM_Support`) rewritten for current providers (adds Bedrock, Vertex AI, Fireworks, OpenAI-compatible self-hosted); removes GPT-3.5, Google BARD, cost estimate, and stale "upcoming" list
* Admin guide: LLM Configuration (`008`) recommended and default models updated to the 0.18.x GPT-5.6 defaults (`gpt-5.6-sol`, `-luna`, `-terra`); replaces gpt-4o examples and the undefined `LLM_MODEL` / `LLM_MODEL_SMART` settings with `LLM_MODEL_DEFAULT` and per-role overrides
* Admin guide: consistent paths and restart commands (`011`, `015`, `100` no longer use undefined `$LOUIE_HOME`; restarts after `custom.env` changes include `api`); current sandbox container names (`010`); sandbox ports corrected to 8081 and 9000-9999 (`012`)
* Admin guide: OAuth2 redirect URI is `<OA2_REDIRECT_URL_BASE>/oauth/callback`, not the bare Louie URL (`011_Authentication_Registration`)
* Admin guide: empty Deployment section now lists its pages, including Network Architecture, Container Architecture and AWS Requirements, which were not linked from any menu
* Admin guide: broken image path for the network architecture diagram (`004_Network_Architecture`)
* Admin guide: OAuth2 setup screenshots referenced files that were never committed (`static/oauth-setup-01.png`, `-02.png`); now uses the existing `admin/images/OAUTH_Setup.png` navigation screenshot (`011_Authentication_Registration`)

### Infra

* Sphinx port
* CI
