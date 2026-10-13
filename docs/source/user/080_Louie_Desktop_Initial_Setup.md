# Louie Desktop — Initial Setup

Louie Desktop runs Louie as a native application, with the same notebooks,
agents and connectors as the browser.

## Download

All builds are at **[download.louie.ai](https://download.louie.ai)**, which
always offers the current release.

| Platform | Build | Requirements |
|---|---|---|
| **macOS** | `Louie-<version>-arm64.dmg` | Apple Silicon (M-series). macOS 11 Big Sur or later |
| **Windows** | `Louie-<version>-win.exe` | x64 |
| **Linux** | `Louie-<version>-amd64.deb` | x86_64, Debian-based: Debian, Ubuntu, Pop!_OS, Mint |

8 GB RAM is recommended.

There is no Intel (x86_64) macOS build — the mac release is Apple Silicon only.

## Install

**macOS** — open the `.dmg` and drag Louie to Applications. The build is signed
and notarized, so Gatekeeper will open it without a security prompt.

**Windows** — run the `.exe` installer.

**Linux** — install the `.deb`:

```bash
sudo dpkg -i Louie-<version>-amd64.deb
sudo apt-get install -f
```

## First launch

On first launch Louie asks you to sign in with your Graphistry account. See
[Signing In to Louie Desktop](081_Louie_Desktop_Sign_In.md).

Once signed in you have your notebooks, folders and any connectors your
organization has configured.

## Getting help

If something goes wrong during installation, contact <support@louie.ai>.
