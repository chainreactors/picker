---
title: easywall v2.14.0
url: https://kitploit.com/en/posts/github-jp1337-easywall-v2140
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:45.336131
---

# easywall v2.14.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/43596/12d87b1f20c9a0ddf0121ca4a82e73b615f3e7b79e55e0162dd410828878d0ff.png)

New releaseSep 4, 2026

# easywall v2.14.0

Web interface for the nftables firewall on Linux, written in Go. The apply undoes itself after 120 seconds unless you confirm it — you cannot lock yourself out. Debian & Docker install.

Share

![](https://raw.githubusercontent.com/jp1337/easywall/HEAD/web/static/icon.svg)

# easywall

*Your firewall. Your rules. No surprises.*

[![Tests](https://img.shields.io/github/actions/workflow/status/jp1337/easywall/test.yml?branch=main&label=tests&logo=github&logoColor=white)](https://github.com/jp1337/easywall/actions/workflows/test.yml)
[![Build](https://img.shields.io/github/actions/workflow/status/jp1337/easywall/build.yml?branch=main&label=build&logo=github&logoColor=white)](https://github.com/jp1337/easywall/actions/workflows/build.yml)
[![Security](https://img.shields.io/github/actions/workflow/status/jp1337/easywall/security.yml?branch=main&label=security&logo=github&logoColor=white)](https://github.com/jp1337/easywall/actions/workflows/security.yml)
[![Coverage](https://img.shields.io/codecov/c/github/jp1337/easywall?logo=codecov&logoColor=white&label=coverage)](https://codecov.io/gh/jp1337/easywall)

[![Latest release](https://img.shields.io/github/v/release/jp1337/easywall?logo=github&logoColor=white&label=release)](https://github.com/jp1337/easywall/releases/latest)
[![Go version](https://img.shields.io/github/go-mod/go-version/jp1337/easywall?logo=go&logoColor=white&label=go)](https://go.dev)
[![GPL-3.0](https://img.shields.io/github/license/jp1337/easywall?logo=opensourceinitiative&logoColor=white&label=license&color=blue)](https://www.gnu.org/licenses/gpl-3.0)
[![Discord](https://img.shields.io/badge/discord-join-5865F2?logo=discord&logoColor=white)](https://discord.gg/3zJMvChvUA)
[![Support on Ko-fi](https://img.shields.io/badge/ko--fi-support-13C3FF?logo=kofi&logoColor=white)](https://ko-fi.com/jp1337)

[**Live demo**](https://demo.easywall-project.org) ·
[**Documentation**](https://easywall-project.org) ·
[Changelog](https://github.com/jp1337/easywall/blob/main/CHANGELOG.md)

nftables through a web interface that cannot lock you out: **every apply reverts
itself unless you confirm it.**

![The easywall dashboard: firewall status with acceptance state, pending changes and last apply; tiles counting TCP ports, UDP ports, blacklist, whitelist, custom rules and forwarding; and a recent-activity list.](https://assets.kitploit.com/production/public/readmes/43596/614cbeca6ebf752bf79ddc8d910eb14f46b45390f1cb5b8f53032578aed5fb40.png)

## The idea

Editing a rule changes nothing. Applying it changes everything — for 120 seconds.
If the new rules cut your connection you cannot click Confirm, and *not* confirming
is what brings the old rules back.

![State machine: editing leads to Staged, applying leads to Live, confirming within the window leads to Confirmed, and letting the window expire leads to Rolled back, from where the staged edits are still available.](https://raw.githubusercontent.com/jp1337/easywall/HEAD/docs/assets/diagrams/apply-flow-light.svg)

## Architecture

Two processes. The one exposed to the network holds no privilege worth stealing.

![Browser talks HTTPS to easywall-web, which runs unprivileged; easywall-web talks typed JSON over a Unix socket to easywall-core, which runs as root and speaks netlink to the nftables table inet easywall.](https://raw.githubusercontent.com/jp1337/easywall/HEAD/docs/assets/diagrams/architecture-light.svg)

A complete rewrite of the original easywall — Python, Flask, `iptables` via
subprocess — which was archived in 2022 after a CVE. Both root causes are gone:
the privileges live in a different process, and the apply path builds Go structs
instead of a command line. [How it works →](https://easywall-project.org/architecture/)

## Install

![Decision tree: just looking leads to demo mode; Debian or Ubuntu leads to the .deb package; already running containers leads to Docker; otherwise build from source.](https://raw.githubusercontent.com/jp1337/easywall/HEAD/docs/assets/diagrams/install-choice-light.svg)

root@kitploit:~

```
# Debian / Ubuntu — amd64 and arm64
ARCH=$(dpkg --print-architecture)
wget https://github.com/jp1337/easywall/releases/latest/download/easywall_$ARCH.deb
sudo dpkg -i easywall_$ARCH.deb && sudo apt-get install -f

# Docker
git clone https://github.com/jp1337/easywall.git && cd easywall && docker compose up -d

# From source — Go 1.27+, nftables
git clone https://github.com/jp1337/easywall.git && cd easywall
make build && sudo make install
sudo systemctl enable --now easywall-core easywall-web
```

Then open `https://localhost:12227`. The first visit
[sets up the account and stages the first rules](https://easywall-project.org/installation/first-run/).

## What you get

|  |  |
| --- | --- |
| **Ports** | TCP and UDP, single or range, with per-rule SSH brute-force routing |
| **Blacklist & whitelist** | IPv4, IPv6 and CIDR, evaluated before any port rule |
| **Protection modules** | Twelve, five on by default — floods, scans, bogons, fragments, broadcast/multicast/anycast |
| **Port forwarding** | NAT redirects with protocol selection |
| **Custom rules** | Raw nftables, syntax-checked before it is applied |
| **Export / import** | The whole rule set as JSON |
| **Audit log** | What changed and when, one JSON object per line |
| **Docker coexistence** | Owns `table inet easywall`, touches nothing else |
| **English, Deutsch, Français** | Switchable in the interface, including before sign-in. A language may be partial: what it is missing renders English, and the gap is reported rather than hidden |
| **Light & dark** | Follows the OS, with a manual toggle; both contrast-checked |

## Built with

|  |  |
| --- | --- |
| Go 1.27, single binary | `go-chi/chi` · `html/template` |
| nftables via `google/nftables` | direct netlink, no `nft` subprocess |
| Argon2id | `golang.org/x/crypto`, 16-byte salt per password |
| CSRF | `net/http.CrossOriginProtection`, Go 1.25 native |
| Design system | [`DESIGN.md`](https://github.com/jp1337/easywall/blob/main/DESIGN.md) + Tailwind v4 — no third-party UI library |
| Fonts | Inter + JetBrains Mono, self-hosted, ~145 KB — works air-gapped |
| CI | `govulncheck`, `gosec`, CodeQL, `-race`, and an integration suite against a real kernel |

## Getting help

|  |  |
| --- | --- |
| A question, or something not behaving | [Discord](https://discord.gg/3zJMvChvUA) |
| A bug, or a feature you want | [GitHub issues](https://github.com/jp1337/easywall/issues) |
| A security vulnerability | [Security advisory](https://github.com/jp1337/easywall/security/advisories/new) — **not** Discord, and not a public issue |

## Contributing

Setup, commit conventions and the review checklist: [CONTRIBUTING.md](https://github.com/jp1337/easywall/blob/main/CONTRIBUTING.md).
Anything visual goes through [`DESIGN.md`](https://github.com/jp1337/easywall/blob/main/DESIGN.md) first.

Security issues: **not** as a public issue — use
[GitHub Security Advisories](https://github.com/jp1337/easywall/security/advisories/new).

## License

GPL-3.0 — see [LICENSE](https://github.com/jp1337/easywall/blob/main/LICENSE).

[Read more](/en/tools/github/jp1337/easywall?expand=1)

## Categories

[Defensive Tools](/en/categories/defensive-tools)[Configuration Auditing](/en/categories/configuration-auditing)[Network Access Control](/en/categories/network-access-control)[Network Security](/en/categories/network-security)[Misconfiguration](/en/categories/misconfiguration)

### Most Pop...