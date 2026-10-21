# Changelog

All notable changes to this repo are documented in this file.

The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and all PyGraphistry-specific breaking changes are explictly noted here.

## [Development]

### Added

* Admin guide: Docker Compose install from release tarballs, including air-gapped hosts, upgrade, and troubleshooting (`012_Docker_Compose_Install`), listed under Deployment with Distributions
* Admin guide: changing default host ports (80/443/8081/8082) with `docker-compose.override.yml`, kept across upgrades
* User guide: Skills overview (`069_Skills`) and Skill Authoring guide (`070_Skill_Authoring`), under Advanced Topics
* Integration guide: launch templated Louie investigations from external applications, with a Splunk recipe (`071_Launch_Deep_Links`)

### Fixed

* Admin guide: OAuth2 redirect URI is `<OA2_REDIRECT_URL_BASE>/oauth/callback`, not the bare Louie URL (`011_Authentication_Registration`)
* Admin guide: empty Deployment section now lists its pages, including Network Architecture, Container Architecture and AWS Requirements, which were not linked from any menu
* Admin guide: broken image path for the network architecture diagram (`004_Network_Architecture`)

### Infra

* Sphinx port
* CI
