---
title: OnionHop v3.8.1
url: https://kitploit.com/en/posts/github-center2055-onionhop-v381
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:50:53.903396
---

# OnionHop v3.8.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13108/9aca447fc44246b2a536fd6d3d8ce7eada8a6bb128f6b207463903c219b18d79.png)

New releaseAug 21, 2026

# OnionHop v3.8.1

Privacy-first Desktop app that routes your traffic through Tor - Anonymous browsing made simple

Share

# OnionHop V3

![OnionHop Logo](https://assets.kitploit.com/production/public/readmes/13108/80a8bbe598d747699c1a29ea1e403b417c61ccd0a27abb29ed3f62b8d204ceed.png)

[![OnionHop V3 UI Screenshot](https://assets.kitploit.com/production/public/readmes/13108/9aca447fc44246b2a536fd6d3d8ce7eada8a6bb128f6b207463903c219b18d79.png)](assets/onionhop-v3-ui.png)

[![Download Latest Release](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)](https://github.com/center2055/OnionHop/releases/latest)
[![Support on Ko-Fi](https://img.shields.io/badge/Support-Ko--Fi-ff5f5f?style=for-the-badge&logo=kofi&logoColor=white)](https://ko-fi.com/center2055)

![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-000000?style=flat&logo=apple&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)

**OnionHop V3** is a modern, **cross-platform** desktop app (Windows, macOS and Linux) that routes your traffic through **Tor**. It can run Tor as a local SOCKS proxy or as a system-wide tunnel, automatically pick a working connection strategy for your network with **Smart Connect**, scan and apply working bridges for censored networks across every transport, and even let you volunteer as a Snowflake proxy.

> **Disclaimer**
> OnionHop is provided "as-is". Tor usage can be illegal or restricted in some jurisdictions. You are responsible for complying with local laws and regulations.

---

## What's new in V3 (since v2.7)

V3 is a ground-up rebuild on a new cross-platform UI stack, with a much smarter connection engine and a far wider set of censorship-resistant transports.

* **Now cross-platform** — native desktop builds for **Windows**, **macOS** (signed & notarized universal app) and **Linux** (AppImage). Same app, native look on each OS.
* **Redesigned UI** — Fluent/native look (FluentAvalonia), light/dark/follow-system themes, an accent picker, an integrated chromeless title bar on Windows and native window chrome on macOS, and **8 languages** (English, German, French, Chinese, Russian, Persian, Azerbaijani, and Sorani Kurdish).
* **Smart Connect** — an offline censorship "brain" that auto-picks the best connection strategy for your network and country: it knows where Tor is blocked, prefers transports that survive there, pre-tests bridge reachability, races strategies in parallel, fails fast off dead paths, and remembers what worked on each network so the next connect is instant.
* **Three Tor engines** — **Classic** (`tor.exe`, full control: bridges, country/entry/exit pinning, control-port New Identity), **Arti** (the Rust Tor implementation with native bridge/PT config), and **ArtiHop** (shortened 2-hop Guard→Exit circuits for lower latency).
* **More censorship-resistant transports** — obfs4, **snowflake** (with optional AMP-cache fronting), **webtunnel**, **conjure**, meek, and **dnstt** (a DNS tunnel that gets Tor through when only DNS is allowed).
* **Bridge Scanner** — fetch and reachability-test bridges of every transport, see color-coded latency, and one-click apply the ones that actually work on your network.
* **More bridge sources** — the official Tor bridge service, the censorship-resistant [OnionHop Bridges Collector](https://github.com/center2055/OnionHop-Bridges-Collector) (derived from [Delta-Kronecker/Tor-Bridges-Collector](https://github.com/Delta-Kronecker/Tor-Bridges-Collector)), built-in community bridges, and a thin-set top-up so a tiny live fetch is automatically backed by bundled bridges.
* **Relays browser** — search the live Tor relay list by nickname, country, role, flags and bandwidth, and pin a preferred entry/middle/exit.
* **Command-line interface** — a full-featured TUI (`OnionHopV3.Cli`) with a live status dashboard, connect/scan/bridges/snowflake/relays commands and settings persistence. Windows, Linux and macOS packages are built by CI.
* **Stronger leak protection** — optional full DNS-over-Tor, a kill switch, UDP blocking in TUN mode, and an in-app WebRTC/UDP privacy notice.
* **Volunteer as a Snowflake proxy** — help censored users reach Tor, straight from Settings.
* **Quality-of-life** — decoupled system-proxy toggle (turn it off while Tor stays connected), an opt-in persistent admin helper to skip repeat UAC prompts in TUN mode (off by default), an in-app changelog, and Bitcoin donations.

---

## Download

Grab the latest build for your platform from **[Releases](https://github.com/center2055/OnionHop/releases/latest)**:

| Platform | File | Notes |
| --- | --- | --- |
| **Windows** | `OnionHop-Setup-v3.exe` | Installer (self-contained, .NET runtime bundled) |
| **Windows** | `OnionHopV3-Portable-…win-x64.zip` | Portable, no install |
| **Linux** | `OnionHop-x86_64.AppImage` | `chmod +x` and run |
| **macOS** | `OnionHop-3.x-macOS.dmg` | Signed & notarized; universal (Apple Silicon + Intel) — from the [macOS repo](https://github.com/rana-gmbh/onionhopMac/releases/latest) |
| **Windows CLI** | `OnionHop-CLI-Setup-3.x.exe` / portable ZIP | Terminal interface |
| **Linux CLI** | `OnionHopCLI-…linux-x64.tar.gz` | Terminal interface |
| **macOS CLI** | `OnionHopCLI-…macos-arm64.tar.gz` (Apple Silicon) / `…macos-x64.tar.gz` (Intel) | Terminal interface; signed & notarized — from the [macOS repo](https://github.com/rana-gmbh/onionhopMac/releases/latest) like the DMGs |

> The macOS `.dmg` is published from the dedicated, code-signing [rana-gmbh/onionhopMac](https://github.com/rana-gmbh/onionhopMac/releases/latest) repository.

---

## Getting started

1. **Install** the build for your OS (above). The Windows installer and the macOS/Linux bundles are self-contained — the .NET 9 runtime is bundled.
2. **Choose a mode**

   * **Proxy Mode (recommended, no admin):** runs Tor locally and points the OS system proxy at Tor's local SOCKS5 endpoint. Best compatibility for proxy-aware apps.
   * **TUN/VPN Mode (admin):** system-wide routing via **sing-box** (Wintun on Windows, the system TUN on macOS/Linux); needed for apps that ignore proxy settings. Leak-resistant (DNS through Tor, UDP blocked).
3. **Connect**

   * Leave **Smart Connect** on to let OnionHop pick the best strategy automatically, **or** pick a **Tor engine** / **Exit Location** / **Bridges** yourself.
   * In a censored network, enable **Bridges** or open the **Scanner** to find bridges that work in your region.
   * Click **Connect**.

Notes

* `.onion` sites require a Tor-aware client (Tor Browser recommended) or SOCKS remote DNS (e.g., Firefox "Proxy DNS when using SOCKS v5").
* Country/relay pinning and control-port New Identity require the **Classic** engine. Arti and ArtiHop support OnionHop bridge/PT configuration, but Classic remains the most complete choice for manual circuit control.

---

## Tor engines

| Engine | Hops | Admin | Bridges / pinning / NEWNYM | Notes |
| --- | --- | --- | --- | --- |
| **Classic** (`tor.exe`) | 3 | no (Proxy) | bridges, pinning, NEWNYM | Most features; recommended for censorship + manual circuit control |
| **Arti** | 3 | no | bridges/PT | Rust Tor implementation (SOCKS runtime) |
| **ArtiHop** | 2 (Guard→Exit) | no | bridges/PT | Lower latency, weaker anonymity |

Use **Classic** when you need country pinning...