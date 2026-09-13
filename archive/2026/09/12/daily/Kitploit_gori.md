---
title: gori
url: https://kitploit.com/en/tools/github/hahwul/gori
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:29.065498
---

# gori

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/hahwul/gori

![](https://assets.kitploit.com/production/public/tools/54802/e819690aafa11d4d995c1c0871c4715800ac98c0b0b428321e34607b79982241-display-v1.webp)

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Web Proxies & Interception](/en/categories/web-proxies-interception)[Scripting & Automation](/en/categories/scripting-automation)[Web Application Exploitation](/en/categories/web-application-exploitation)[API Security Testing](/en/categories/api-security-testing)[Information Gathering](/en/categories/information-gathering)[Web Security](/en/categories/web-security)[Fuzzing](/en/categories/fuzzing)[Penetration Testing](/en/categories/penetration-testing)[Utilities & Frameworks](/en/categories/utilities-frameworks)[Red Teaming](/en/categories/red-teaming)

9510271 day ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

![GitHub](/providers/github.png)

hahwul/gori

# gori

A fast, keyboard-driven HTTP intercepting proxy and hacking & pentesting toolkit for the terminal.

[View Repository](https://github.com/hahwul/gori)[Website](https://gori.hahwul.com)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![](https://assets.kitploit.com/production/public/readmes/54802/e819690aafa11d4d995c1c0871c4715800ac98c0b0b428321e34607b79982241/32ff33c5ac1cbb93e58001838f4dc915325bc4e4290dbf4d5464f9ce5d49ae78-display-v1.webp)

Hack from the terminal.

[![](https://img.shields.io/badge/CONTRIBUTIONS-WELCOME-000000?style=for-the-badge&labelColor=black)](https://github.com/hahwul/gori/blob/main/.github/CONTRIBUTING.md)
[![](https://img.shields.io/github/v/release/hahwul/gori?style=for-the-badge&color=black&labelColor=black&logo=web)](https://github.com/hahwul/gori/releases)
[![](https://img.shields.io/badge/Crystal-000000?style=for-the-badge&logo=crystal&logoColor=white)](https://crystal-lang.org)

[Installation](#installation) •
[Usage](#usage) •
[Documentation](https://github.com/hahwul/gori/blob/main/docs) •
[Contributing](https://github.com/hahwul/gori/blob/main/.github/CONTRIBUTING.md)

---

**gori** (고리 — Korean for *ring, link, loop*) sits in the loop between your client and its target,
capturing every request and response as a *flow* you can replay, fuzz, and scan across HTTP/1.1,
HTTP/2, WebSocket, gRPC, and SSE, and intercept in flight on HTTP/1.1 and HTTP/2. Core assessment
actions that cross surfaces use the same engines, and those workflows are also
available through `gori run` and MCP, so scripts and AI agents can drive the same engagement.
The [capability matrix](https://gori.hahwul.com/reference/capabilities/) names the protocol and
surface limits explicitly.

![gori TUI — the History tab listing captured HTTP flows](https://raw.githubusercontent.com/hahwul/gori/main/docs/static/images/tui/readme.svg)

**Features**

### Capture & Intercept

* Capturing proxy for HTTP/1.1, HTTP/2, WebSocket, gRPC, and SSE
* Intercept on HTTP/1.1 and HTTP/2, gRPC included: hold, edit, forward, or drop in flight — and per-message on an HTTP/1.1 WebSocket, opt in with `proto:ws`
* Searchable History of every flow, with a query language for filtering
* Scope rules, hostname overrides, and match & replace

### Replay, Fuzz & Decode

* Repeater workbench for crafting and re-sending requests (incl. WebSocket & gRPC)
* Intruder-style Fuzzer with four attack modes
* Decoder pipeline for chained encode / decode / hash, including signed session cookies
* Side-by-side Comparer for diffing two flows
* Inline JWT / SAML / GraphQL / protobuf / MessagePack / CBOR decoding, hex view, and pretty-printing
* Copy any request as cURL, Python, `fetch`, Go, httpie, or a CSRF PoC

### Discover & Scan

* Prism passive & light-touch active vulnerability scanner
* Param Miner for hidden-parameter discovery
* Authorize matrix: replay one request under several identities to find broken access control
* Sequencer for grading the randomness of session, CSRF, and reset tokens
* Cookie workbench to verify, crack, and re-sign Flask / Rack / Django session cookies
* OAST collector for confirming blind SSRF, XXE, and injection out of band
* Findings triage with Markdown / JSON export

### Keyboard-first Workflow

* Command palette (`Ctrl-P`) and context space menu (`Space`) reach every action
* Rebindable hotkeys and switchable colour themes
* Mouse support, multi-line editing, and go-to-line navigation

### Headless & Scriptable

* `gori run` exposes the core project and testing workflows for non-interactive use
* MCP server (`gori mcp`) exposes those workflows to AI agents (it does not start a capture proxy)

## Installation

### Quick install (macOS / Linux)

root@kitploit:~

```
curl -fsSL https://gori.hahwul.com/install.sh | bash
```

Then update later with `gori update` (self-update for binary installs; package-manager guidance for Homebrew / Snap / AUR).

### Homebrew

root@kitploit:~

```
brew tap hahwul/gori
brew install gori
```

### Nix

The repo is a flake, so it runs without being installed:

root@kitploit:~

```
nix run github:hahwul/gori
nix profile install github:hahwul/gori   # or keep it
```

### From source

Requires [Crystal](https://crystal-lang.org/) `>= 1.21.0` and `pkg-config`.

root@kitploit:~

```
git clone https://github.com/hahwul/gori.git
cd gori
shards build --release
```

The binary is written to `bin/gori`.

> For system libraries (Brotli / Zstd), offline builds, and other options, see the
> [Installation guide](https://gori.hahwul.com/getting-started/installation/).

## Usage

gori runs one engine and one project behind three entry points. Drive it yourself, hand it to an
AI agent, or script it, and pick the one that fits who is at the controls.

### For humans: `gori` (TUI)

Start the proxy and open the interactive terminal UI. No subcommand needed:

root@kitploit:~

```
gori
```

The proxy listens on `127.0.0.1:8070` by default, and a short first-run wizard picks the
**global default** bind and theme (projects can pin their own later). To intercept HTTPS, trust
gori's root CA. The quickest path is the palette's **Open browser** (`Ctrl-P`), which launches a
browser already trusted and proxied. Captured traffic lands in **History**; press `Ctrl-P` for the
command palette or `Space` for context actions.

root@kitploit:~

```
gori --listen 0.0.0.0 --port 8080   # global bind for this run only (not persisted)
```

### For AI agents: `gori mcp` (MCP server)

`gori mcp` is a [Model Context Protocol](https://modelcontextprotocol.io) server. An AI client
spawns it over stdio, reads your traffic, and drives the same tools you do. Let gori write the
config for your agent, then restart the client:

root@kitploit:~

```
gori mcp --install-claude-code   # Claude Code   (~/.claude.json)
gori mcp --install-claude        # Claude Desktop
gori mcp --install-codex         # OpenAI Codex
gori mcp --install-agy           # Antigravity CLI
gori mcp --install-grok          # Grok
gori mcp --install-hermes        # Hermes        (~/.hermes/config.yaml)
gori mcp --install-pi            # Pi            (~/.pi/agent/mcp.json)
``...