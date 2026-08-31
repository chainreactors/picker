---
title: openclaw v2026.8.1-beta.2
url: https://kitploit.com/en/posts/github-openclaw-openclaw-v202681-beta2
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:51.541604
---

# openclaw v2026.8.1-beta.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7051/627811641168fd3e6bd4701478ee398e9f31b40ed9b8bd1790760e47692e44fe.png)

New releaseAug 30, 2026

# openclaw v2026.8.1-beta.2

Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞

Share

# OpenClaw 🦞 — Your assistant, on your devices, in your chats

![OpenClaw — EXFOLIATE! EXFOLIATE! Your AI assistant, running on your own devices.](https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-banner-dark.png)

[![CI status](https://img.shields.io/github/actions/workflow/status/openclaw/openclaw/ci.yml?branch=main&style=flat-square&label=ci)](https://github.com/openclaw/openclaw/actions/workflows/ci.yml)
[![npm version](https://img.shields.io/npm/v/openclaw?style=flat-square&label=npm)](https://www.npmjs.com/package/openclaw)
[![Node.js version](https://img.shields.io/node/v/openclaw?style=flat-square)](https://nodejs.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Discord](https://img.shields.io/discord/1456350064065904867?label=discord&logo=discord&logoColor=white&color=5865F2&style=flat-square)](https://discord.gg/clawd)

OpenClaw is an AI assistant that runs on your devices and meets you in the channels you already use. It connects models, tools, messaging channels, and optional companion apps through one Gateway, for a single operator or for a team whose members trust each other: the same gateway runs as a personal assistant on one laptop or as a shared [team deployment](https://docs.openclaw.ai/start/teams), and configuration is the only difference. The architecture case — trusted gateway, untrusted execution, deterministic policy — is in [Why OpenClaw](https://docs.openclaw.ai/start/why-openclaw).

[Website](https://openclaw.ai) · [Docs](https://docs.openclaw.ai) · [Getting started](https://docs.openclaw.ai/start/getting-started) · [Why OpenClaw](https://docs.openclaw.ai/start/why-openclaw) · [Showcase](https://docs.openclaw.ai/start/showcase) · [FAQ](https://docs.openclaw.ai/help/faq) · [Vision](https://github.com/openclaw/openclaw/blob/HEAD/VISION.md) · [DeepWiki](https://deepwiki.com/openclaw/openclaw)

## Install

The installer supports macOS, Linux, and Windows. It provisions a supported Node.js runtime when needed.

root@kitploit:~

```
# macOS / Linux / WSL2
curl -fsSL https://openclaw.ai/install.sh | bash
```

root@kitploit:~

```
# Windows PowerShell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

Already manage Node.js? Install the published package instead (Node 22.22.3+, 24.15+, or 25.9+):

root@kitploit:~

```
npm install -g openclaw@latest --allow-scripts=openclaw
```

That command is for npm 12 or npm 11.16+. On npm 11.15 and earlier, omit
`--allow-scripts=openclaw`. See the
[installation guide](https://docs.openclaw.ai/install) for the lifecycle script
contract, Docker, Nix, and other deployment paths.

## Quick start

On a fresh install, the installer scripts start onboarding automatically.
Complete the wizard they open. If you installed the package directly with npm,
pnpm, or Bun, run:

root@kitploit:~

```
openclaw onboard --install-daemon
```

After onboarding:

root@kitploit:~

```
openclaw gateway status
openclaw dashboard
```

Onboarding verifies model access, creates the workspace, and configures the Gateway. The last command opens the Control UI; send a message there to confirm the assistant is working. See the [getting started guide](https://docs.openclaw.ai/start/getting-started) for channel setup and troubleshooting.

## How it fits together

* The [Gateway](https://docs.openclaw.ai/gateway) is the local control plane for sessions, tools, events, and channel connections.
* The [Control UI](https://docs.openclaw.ai/web/control-ui), CLI, and [TUI](https://docs.openclaw.ai/web/tui) connect to the Gateway.
* [Channels](https://docs.openclaw.ai/channels) bring the assistant to WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, and other messaging services.
* [Companion apps and nodes](https://docs.openclaw.ai/platforms) add voice, Canvas, camera, screen, and device-local actions on supported platforms.

OpenClaw works with hosted and local [model providers](https://docs.openclaw.ai/concepts/model-providers). Its [tools](https://docs.openclaw.ai/tools), [skills](https://docs.openclaw.ai/tools/skills), and [plugins](https://docs.openclaw.ai/plugins) extend what an assistant can do.

## Security

Treat inbound messages as untrusted input. DM-capable channels pair unknown senders by default; approve a pairing request with `openclaw pairing approve <channel> <code>`.

Tools run on the host for the main session unless you configure sandboxing. Read the [security guide](https://docs.openclaw.ai/gateway/security), [exposure runbook](https://docs.openclaw.ai/gateway/security/exposure-runbook), and [sandboxing guide](https://docs.openclaw.ai/gateway/sandboxing) before connecting other users or exposing the Gateway remotely.

## Documentation

| Goal | Start here |
| --- | --- |
| Configure models and auth | [Models](https://docs.openclaw.ai/concepts/models) · [Model providers](https://docs.openclaw.ai/concepts/model-providers) |
| Connect a messaging service | [Channels](https://docs.openclaw.ai/channels) |
| Add tools, skills, and plugins | [Tools](https://docs.openclaw.ai/tools) · [Skills](https://docs.openclaw.ai/tools/skills) · [Plugins](https://docs.openclaw.ai/plugins) · [ClawHub](https://clawhub.ai) |
| Run apps and device nodes | [Platforms](https://docs.openclaw.ai/platforms) · [Nodes](https://docs.openclaw.ai/nodes) |
| Use the CLI and chat commands | [CLI reference](https://docs.openclaw.ai/cli) · [Slash commands](https://docs.openclaw.ai/tools/slash-commands) |
| Configure or operate the Gateway | [Configuration](https://docs.openclaw.ai/gateway/configuration) · [Architecture](https://docs.openclaw.ai/concepts/architecture) · [Updating](https://docs.openclaw.ai/install/updating) · [Release channels](https://docs.openclaw.ai/install/development-channels) |

## Development

The repository is a pnpm workspace. Plain `npm install` at the repository root is not supported.

root@kitploit:~

```
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm build
pnpm ui:build
```

See [CONTRIBUTING.md](https://github.com/openclaw/openclaw/blob/HEAD/CONTRIBUTING.md) for the contribution workflow and the [source setup guide](https://docs.openclaw.ai/start/setup) for the development loop.

## Community

OpenClaw is developed in the open by the [OpenClaw Foundation](https://openclaw.org), a non-profit. See [CONTRIBUTING.md](https://github.com/openclaw/openclaw/blob/HEAD/CONTRIBUTING.md) for maintainers and contribution guidelines; AI-assisted PRs are welcome.

Use the [issue chooser](https://github.com/openclaw/openclaw/issues/new/choose) for bugs and feature requests, ask setup questions in [Discord](https://discord.gg/clawd), and report vulnerabilities through [SECURITY.md](https://github.com/openclaw/openclaw/blob/HEAD/SECURITY.md). New capabilities usually belong in plugins built on the [plugin SDK](https://docs.openclaw.ai/plugins/building-plugins) and shared through [ClawHub](https://clawhub.ai).

OpenClaw was built for **Molty**, a space lobster AI assistant, by Peter Steinberger and the community. Explore the [project lore](https://docs.openclaw.ai/start/lore), [soul.md](https://soul.md), [Peter's site](https://steipete.me), [Star History](https://www.star-history.com/#openclaw/openclaw&type=date&legend=top-left), and [@openclaw](https://x.com/openclaw).

Special thanks to [Mario Zechner](https:/...