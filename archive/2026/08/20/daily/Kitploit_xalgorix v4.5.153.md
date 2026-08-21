---
title: xalgorix v4.5.153
url: https://kitploit.com/en/posts/github-xalgord-xalgorix-v45153
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:33.891953
---

# xalgorix v4.5.153

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7609/488e08a41fbdb1845b2872e7495d3d053d2552f94aec4f7fbca06efcc4c25937.png)

New releaseAug 20, 2026

# xalgorix v4.5.153

Autonomous AI pentesting agents — real-time reconnaissance, vulnerability detection, and exploitation orchestration. Go + TypeScript.

Share

![Xalgorix — AI Autonomous Penetration Testing Platform](https://assets.kitploit.com/production/public/readmes/7609/4ccbce5390d26ec3c09bfe6d0bc86897edc133236127bcac15dfab37bed13ecc.png)

[![Go](https://img.shields.io/badge/Go-1.24+-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/License-Apache_2.0-10b981?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux-111111?style=for-the-badge&logo=linux&logoColor=white)](#-installation)
[![Hosted](https://img.shields.io/badge/Hosted-www.xalgorix.com-6d28d9?style=for-the-badge&logo=icloud&logoColor=white)](https://www.xalgorix.com/)
[![GitHub stars](https://img.shields.io/github/stars/xalgord/xalgorix?style=for-the-badge&logo=github&color=yellow)](https://github.com/xalgord/xalgorix/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xalgord/xalgorix?style=for-the-badge&logo=github&color=blue)](https://github.com/xalgord/xalgorix/network/members)
[![GitHub release](https://img.shields.io/github/v/release/xalgord/xalgorix?style=for-the-badge&logo=github&color=green)](https://github.com/xalgord/xalgorix/releases)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/xalgord/xalgorix)

[![xalgord/xalgorix | Trendshift](https://trendshift.io/api/badge/trendshift/repositories/35278/daily?language=Go)](https://trendshift.io/repositories/35278?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-35278)

# Xalgorix — Open-source AI pentester that *proves* vulnerabilities

**Most scanners detect. Xalgorix proves.** An autonomous LLM agent works a full pentest methodology, then an **independent verifier re-exploits every finding** before it's reported — so you get proof, not a pile of maybes to triage. Self-hosted, private, and bring-your-own-LLM. Built in Go + TypeScript.

[🚀 Quick Start](#-quick-start) ·
[💡 Why Xalgorix](#-why-xalgorix) ·
[✨ Features](#-features) ·
[🎯 Use Cases](#-use-cases) ·
[☁️ Hosted Cloud](https://www.xalgorix.com/) ·
[📖 Docs](https://docs.xalgorix.com)

---

## 🚀 Quick Start

**Install (one line):**

root@kitploit:~

```
curl -sSL https://www.xalgorix.com/install | bash
```

This downloads the prebuilt binary for your platform (Linux amd64/arm64) from the latest release. Then run the interactive setup wizard:

root@kitploit:~

```
xalgorix --setup
```

Choose your provider, confirm a model, and enter the API key when prompted. For best results, use a current frontier model with strong reasoning, long-context performance, and reliable tool calling—such as the latest capable GPT, Claude, or Gemini model available to you. Smaller or local models remain supported, but may require more supervision during long autonomous scans. Xalgorix stores the key privately in `~/.xalgorix.env` (mode `0600`) and can launch the dashboard for you. Local Ollama needs no API key.

If you choose not to launch immediately, start later with `xalgorix --web` and open `http://127.0.0.1:9137`. You can change providers or advanced options at any time under **Settings → LLM**, or rerun `xalgorix --setup`.

**Or run with Docker — batteries included, no toolchain needed:**

root@kitploit:~

```
docker run --rm -p 9137:9137 \
  --privileged \
  -v xalgorix-data:/data \
  xalgord/xalgorix:latest
```

`--privileged` gives the toolset the same host-like access it has when run natively as root. Docker's default sandbox drops capabilities (like `NET_ADMIN`) and applies a seccomp filter, which breaks low-level tools (iptables/route changes, ARP-spoof/MITM, tun/tap VPNs, ptrace-based debuggers, masscan interface tuning). Since an image can't grant itself these, they must be set at run time. The container is a disposable, network-isolated scanning sandbox running as root — privileged is the intended posture; never expose the dashboard publicly without auth. Prefer least-privilege? Swap `--privileged` for `--cap-add=NET_ADMIN --cap-add=NET_RAW --cap-add=SYS_PTRACE --security-opt seccomp=unconfined`.

Open `http://localhost:9137`. You **don't need an LLM key to start** — the dashboard launches without one; set the model + API key under **Settings → LLM** (it persists to the `/data` volume). If you don't pass `XALGORIX_USERNAME`/`XALGORIX_PASSWORD`, a random admin password is generated and printed to the container logs on first run.

**Easiest — Docker Compose** (maps the port + a persistent volume for you):

root@kitploit:~

```
curl -sSLO https://raw.githubusercontent.com/xalgord/xalgorix/main/docker-compose.yml
docker compose up -d
docker compose logs -f   # shows the generated admin password on first start
```

The image ships an extensive offensive-security toolset preinstalled (nmap, nuclei, httpx, subfinder, katana, ffuf, gobuster, sqlmap, masscan, dalfox, feroxbuster, and more) **and** keeps every package manager (apt, go, cargo, pipx, npm) available so the agent can still auto-install anything missing at runtime. It runs as root inside the container by design — treat the container as a disposable, network-isolated scanning sandbox and never expose the dashboard without auth. (amd64 image; the installer above covers arm64.)

**Or build from source** (needs Go 1.25+ and Node.js):

root@kitploit:~

```
git clone https://github.com/xalgord/xalgorix.git
cd xalgorix
make build
sudo install -m 755 build/xalgorix /usr/local/bin/xalgorix
```

> [!TIP]
> Prefer zero setup? A fully managed version runs at [www.xalgorix.com](https://www.xalgorix.com/) — click-to-scan, no install or API keys required.

### 🤖 Review pull requests automatically — free GitHub App

Want a security review on every pull request with zero setup? Install the **[Xalgorix GitHub App](https://github.com/apps/xalgorix)**. It reads each PR's diff and comments a security review — injection, broken auth/IDOR, SSRF, secrets, unsafe patterns — right on the pull request. Updates in place on new commits, and you can comment **`@xalgorix review`** to re-run on demand. No workflow file, no API key, no account — and it's free.

[**➕ Add Xalgorix to GitHub →**](https://github.com/apps/xalgorix/installations/new)

For merge gating and full exploit-verified pentests in CI, use the [hosted scanner](https://www.xalgorix.com/) or the GitHub Action.

> [!IMPORTANT]
> Use Xalgorix only on systems you own or have explicit permission to test.

> [!TIP]
> Prefer not to self-host? A fully managed version is available at [www.xalgorix.com](https://www.xalgorix.com/) — click-to-scan, no install or API keys required.

## 📚 Contents

|  |  |  |
| --- | --- | --- |
| 🚀 [Quick Start](#-quick-start) | 🔩 [Configuration](#-configuration) | 🧾 [Environment Variables](#-environment-variables) |
| 🔎 [Overview](#-overview) | 🆙 [Upgrading](#-upgrading-from-previous-versions) | 🔤 [Provider Prefixes](#-provider-prefixes) |
| 💡 [Why Xalgorix](#-why-xalgorix) | 🏃 [Running](#-running) | 💻 [CLI Reference](#-cli-reference) |
| 🎯 [Use Cases](#-use-cases) | 🧰 [Service Mode](#-service-mode) | 📡 [API Summary](#-api-summary) |
| 📸 [Screenshots](#-screenshots) | 🔁 [Web UI Workflow](#-web-ui-workflow) | 💾 [Data Storage](#-data-storage) |
| ✨ [Features](#-features) | 🔀 [Scan Modes](#-scan-modes) | 🧪 [Development](#-development) |
| 📥 [Installation](#-installation) | 📂 [Scan Your Code](#-scan-your-code-no-target-needed) | ...