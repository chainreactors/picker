---
title: skulto
url: https://kitploit.com/en/tools/github/asteroid-belt/skulto
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:54:53.162390
---

# skulto

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

skulto — Offline and security-first tool for syncing and managing agent skills | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/asteroid-belt/skulto

![](https://assets.kitploit.com/production/public/tools/54493/fe7ab73f41c9aa7e9ea530b39181d92596ea95963a16ceefde64171be397d429-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Scripting & Automation](/en/categories/scripting-automation)[Security Virtualization](/en/categories/security-virtualization)[Utilities & Frameworks](/en/categories/utilities-frameworks)[Supply Chain Security](/en/categories/supply-chain-security)[AI Security](/en/categories/ai-security)

![GitHub](/providers/github.png)asteroid-belt/skulto

# skulto

Offline and security-first tool for syncing and managing agent skills

[View Repository](https://github.com/asteroid-belt/skulto)

502281 day ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Skulto

> Scan AI agent skills for prompt injection before you install them

[![CI](https://github.com/asteroid-belt/skulto/actions/workflows/ci.yml/badge.svg)](https://github.com/asteroid-belt/skulto/actions/workflows/ci.yml)
[![Go Version](https://img.shields.io/badge/Go-1.25+-00ADD8?style=flat&logo=go)](https://go.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

root@kitploit:~

```
   ╔════════════════════════════════════════════════════════╗
   ║    ███████╗██╗  ██╗██╗   ██╗██╗  ████████╗ ██████╗     ║
   ║    ██╔════╝██║ ██╔╝██║   ██║██║  ╚══██╔══╝██╔═══██╗    ║
   ║    ███████╗█████╔╝ ██║   ██║██║     ██║   ██║   ██║    ║
   ║    ╚════██║██╔═██╗ ██║   ██║██║     ██║   ██║   ██║    ║
   ║    ███████║██║  ██╗╚██████╔╝███████╗██║   ╚██████╔╝    ║
   ║    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝     ║
   ╠════════════════════════════════════════════════════════╣
   ║            CROSS-PLATFORM AI SKILLS MANAGEMENT         ║
   ╚════════════════════════════════════════════════════════╝
```

![Skulto Demo](https://raw.githubusercontent.com/asteroid-belt/skulto/main/assets/demo.gif)

## What is Skulto?

[Download Tool](https://github.com/asteroid-belt/skulto)

Skulto is a cross-platform CLI tool for managing AI coding assistant skills across 33 platforms. It provides:

1. **Multi-platform installation** - Install skills to Claude Code, Cursor, Windsurf, Copilot, Codex, Cline, Roo Code, Gemini CLI, Kiro CLI, and 25+ more
2. **Repository management** - Add, sync, and remove skill repositories
3. **Full-text search** - SQLite FTS5-powered search across all indexed skills
4. **Security scanning** - Detect prompt injection and dangerous code patterns
5. **Platform detection** - Automatically detects which AI tools are installed on your system
6. **Interactive TUI** - Bubble Tea-powered terminal interface with collapsible groups, multi-select, and keyboard navigation
7. **URL-based install** - Install directly from GitHub repositories via `skulto install owner/repo`

## Features

![Skill Creation](https://assets.kitploit.com/production/public/readmes/54493/4398d15a09b070738a42656f281be37d3fe13d69af7c82f0610c8bad7d2251f7/65d5451b0e4b5d1cafcce058b7de9cf0932acacf6f3129fdd0f964261431f38b-display-v1.webp)

* **33 platform support** - Claude Code, Cursor, Windsurf, GitHub Copilot, OpenAI Codex, OpenCode, Cline, Roo Code, Gemini CLI, Kiro CLI, Amp, Continue, Goose, Junie, Qwen Code, Trae, and more
* **Platform detection** - Detects installed AI tools and surfaces them in platform choosers
* **Offline-first** - Works without internet after initial sync
* **Fast search** - FTS5-powered full-text search with BM25 ranking (~50ms latency)
* **Git-based sync** - Clone and pull repositories for reliable updates
* **Security scanner** - Detects prompt injection in frontmatter, references, scripts and dangerous patterns with threat levels
* **Smart multi-skill install** - Install multiple skills from a repository URL with per-skill conflict resolution (skip already-installed, add new locations, or skip all)
* **Scope selection** - Install skills globally (`~/`) or per-project (`./`) with separate control per platform
* **Collapsible platform groups** - Detected/preferred platforms at top, all others in a collapsed group across all choosers
* **Install location memory** - Optionally remember your platform/scope choices for future installs
* **Favorites** - Save favorite skills that persist across database resets
* **Recently viewed** - Tracks and displays skills you've recently viewed
* **MCP Server** - Model Context Protocol server for AI tool integration (search, install, manage skills programmatically)
* **Telemetry** - Anonymous usage stats (opt-out with env var in Settings)

### Supported Platforms

Skulto detects and installs skills to 33 AI coding tools:

|  |  |  |  |
| --- | --- | --- | --- |
| Claude Code | Cursor | Windsurf | GitHub Copilot |
| OpenAI Codex | OpenCode | Cline | Roo Code |
| Gemini CLI | Kiro CLI | Amp | Continue |
| Goose | Junie | Kilo Code | Trae |
| Qwen Code | Kimi Code CLI | CodeBuddy | Command Code |
| Crush | Droid | Kode | MCPJam |
| Mux | OpenHands | Pi | Qoder |
| Zencoder | Neovate | Pochi | Antigravity |
| Moltbot |  |  |  |

## Installation

### Homebrew

root@kitploit:~

```
brew install asteroid-belt/tap/skulto
```

To upgrade:

root@kitploit:~

```
brew upgrade asteroid-belt/tap/skulto
```

### Linux Packages

GitHub Releases provide `.deb` and `.rpm` downloads for both `amd64` and
`arm64`. Choose the package format for your distribution and replace the
version below with a release tag:

root@kitploit:~

```
VERSION=vX.Y.Z
ARCH=amd64 # or arm64

# Debian/Ubuntu
curl -LO "https://github.com/asteroid-belt/skulto/releases/download/${VERSION}/skulto_${VERSION#v}_linux_${ARCH}.deb"

# Fedora/RHEL/openSUSE
curl -LO "https://github.com/asteroid-belt/skulto/releases/download/${VERSION}/skulto-${VERSION#v}-1.$([ "$ARCH" = amd64 ] && echo x86_64 || echo aarch64).rpm"

# Download the release checksums, then verify the downloaded asset.
curl -LO "https://github.com/asteroid-belt/skulto/releases/download/${VERSION}/checksums.txt"
sha256sum -c checksums.txt --ignore-missing
```

Install the local file with your distribution's package manager:

root@kitploit:~

```
sudo apt install ./skulto_*.deb
sudo dnf install ./skulto-*.rpm
sudo zypper install ./skulto-*.rpm
```

Each package installs `skulto` and `skulto-mcp` at `/usr/bin/skulto` and
`/usr/bin/skulto-mcp`. Skulto does not require system Git at runtime. These are
GitHub Release downloads, not a configured package repository.

### From Source

root@kitploit:~

```
# Clone the repository
git clone https://github.com/asteroid-belt/skulto.git
cd skulto

# Install dependencies
make deps

# Build (outputs to ./build/)
make build-all

# Run
./build/skulto
```

### Requirements

* Go 1.25+
* (Optional) `GITHUB_TOKEN` for higher API rate limits

## Quick Start

root@kitploit:~

```
# Launch the TUI (guided onboarding on first run)
skulto

# Or install skills directly from a repository URL
skulto install ...