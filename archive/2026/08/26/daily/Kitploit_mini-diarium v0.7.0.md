---
title: mini-diarium v0.7.0
url: https://kitploit.com/en/posts/github-fjrevoredo-mini-diarium-v070
source: Kitploit
date: 2026-08-26
fetch_date: 2026-08-27T12:12:43.058008
---

# mini-diarium v0.7.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/11890/d0283f078a368dc6acadfb49a17f2d58a6df428dc52903b4fe0622c98b1449cd.png)

New releaseAug 26, 2026

# mini-diarium v0.7.0

A local-only journal with serious encryption. Free, open source, and never touches the internet.

Share

![Mini Diarium](https://raw.githubusercontent.com/fjrevoredo/mini-diarium/HEAD/public/logo-transparent.svg)

# Mini Diarium

**A local-only journal with serious encryption.**
Free, open source, and never touches the internet.

[![CI](https://github.com/fjrevoredo/mini-diarium/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/fjrevoredo/mini-diarium/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/fjrevoredo/mini-diarium/graph/badge.svg?token=0ABJIE0333)](https://codecov.io/gh/fjrevoredo/mini-diarium)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=fjrevoredo_mini-diarium&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fjrevoredo_mini-diarium)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.7.0-blue)](https://github.com/fjrevoredo/mini-diarium/releases)
[![Platform](https://img.shields.io/badge/platform-Windows_%7C_macOS_%7C_Linux-lightgrey)](https://github.com/fjrevoredo/mini-diarium#download)
[![Follow @MiniDiarium](https://img.shields.io/badge/Follow-@MiniDiarium-000?logo=x&logoColor=white)](https://x.com/MiniDiarium)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy_me_a_coffee-ff5f5f?logo=kofi&logoColor=white)](https://ko-fi.com/fjrevoredo)
[![Donate crypto](https://img.shields.io/badge/Crypto-XMR%20%7C%20BTC%20%7C%20Lightning-FF6600?logo=monero&logoColor=white)](DONATE.md)

[![Tauri v2](https://img.shields.io/badge/Tauri_v2-24C8DB?logo=tauri&logoColor=white)](https://tauri.app)
[![SolidJS](https://img.shields.io/badge/SolidJS-2C4F7C?logo=solid&logoColor=white)](https://solidjs.com)
[![Rust](https://img.shields.io/badge/Rust-CE422B?logo=rust&logoColor=white)](https://www.rust-lang.org)
[![Flathub](https://img.shields.io/flathub/v/io.github.fjrevoredo.mini-diarium?logo=flathub&logoColor=white&label=Flathub)](https://flathub.org/apps/io.github.fjrevoredo.mini-diarium)
[![Microsoft Store](https://img.shields.io/badge/Microsoft_Store-0078D4)](https://apps.microsoft.com/detail/9PJFTX44ZS43)

[mini-diarium.com](https://mini-diarium.com) · [Download](#download) · [Documentation](https://mini-diarium.com/docs) · [Features](#features) · [Philosophy](https://github.com/fjrevoredo/mini-diarium/blob/HEAD/PHILOSOPHY.md) · [Benchmarks](https://fjrevoredo.github.io/mini-diarium/benchmarks/)

![Demo](https://assets.kitploit.com/production/public/readmes/11890/e23f1bbb4cd335f847972f08cc07992963040e0268f867ee26d5dee3ede58723.gif)

## ☕ Support the Project

Mini Diarium is free, open source, and will always be. If you find it useful and want to support its development, consider buying me a coffee on Ko-fi. Every donation goes directly toward keeping this project alive and improving.

[![Buy Me a Coffee on Ko-fi](https://assets.kitploit.com/production/public/readmes/11890/6f9d451c59aee4ba293b6a7ae6b100042f5f28390e455277d4c2fe51f1f6349a.webp)](https://ko-fi.com/fjrevoredo)

Prefer crypto? Monero, Bitcoin, and Lightning are below and in [DONATE.md](https://github.com/fjrevoredo/mini-diarium/blob/HEAD/DONATE.md).

**Donate with crypto (Monero · Bitcoin · Lightning)**

**Monero (XMR)**, standard mainnet address:

root@kitploit:~

```
4ApNmqczyAoWsprSrCMsPNKTGhxaH1Cs6agLVaGiKuBBVSotWK9uj3oVQkWYUX9XUGQJyC9WB7cMofE8wfp5BbUoEdcwbjv
```

**Bitcoin (BTC)**, on-chain native SegWit (bech32):

root@kitploit:~

```
bc1q0y6v888ala2f8r7tm8g30vqt9ma09w9ww4jhum
```

**Bitcoin over Lightning**, a Lightning address that works with Cake Wallet, Phoenix, Zeus, Blink, and Wallet of Satoshi:

root@kitploit:~

```
[email protected]
```

Always verify addresses against [DONATE.md](https://github.com/fjrevoredo/mini-diarium/blob/HEAD/DONATE.md) on `master` before sending. That file also covers network warnings and what donations do and do not buy.

## Download

Download the latest release for your platform from [GitHub Releases](https://github.com/fjrevoredo/mini-diarium/releases).

Requires **Windows 10 (1809)+**, **macOS 10.15 Catalina+**, or **Linux** (Ubuntu 20.04+, Fedora 36+, Arch, or equivalent).

Quick install:

* Windows (Microsoft Store): [apps.microsoft.com/detail/9PJFTX44ZS43](https://apps.microsoft.com/detail/9PJFTX44ZS43)
* Windows (WinGet): `winget install fjrevoredo.MiniDiarium`
* macOS (Homebrew): `brew tap fjrevoredo/mini-diarium` then `brew install --cask mini-diarium`
* Linux (Flatpak): `flatpak install flathub io.github.fjrevoredo.mini-diarium`
* NixOS / Nix (Flakes): `nix run github:fjrevoredo/mini-diarium`

For package formats, first-run notes (Gatekeeper / SmartScreen), and checksum verification, see [docs/INSTALLATION.md](https://github.com/fjrevoredo/mini-diarium/blob/HEAD/docs/INSTALLATION.md).

## Quick Start

1. Launch Mini Diarium
2. Create a password (this encrypts your journal; there is no recovery if forgotten)
3. Write your first entry. It auto-saves as you type
4. Navigate between days with `Ctrl+[` / `Ctrl+]` or click dates on the calendar
5. Lock your journal when you're done

## Background

Mini Diarium is a spiritual successor to [Mini Diary](https://github.com/samuelmeuli/mini-diary) by Samuel Meuli. I loved the original tool. It was simple, private, and did exactly what a journal app should do. Unfortunately, it's been unmaintained for years and its dependencies have aged out. I initially thought about forking it and modernizing the stack, but turned out impractical. So I started over from scratch, keeping the same core philosophy (encrypted, local-only, focused) while rebuilding completely with Tauri 2, SolidJS, and Rust. The result is a lighter, faster app with stronger encryption and a few personal touches.

## Philosophy First

Mini Diarium is intentionally opinionated. The philosophy is not a side note, it is the product:

* **Small, extensible core**: keep core responsibilities tight (encrypt, store, authenticate) and push extras to extension points
* **Boring security**: use established algorithms and audited libraries, never custom crypto
* **Local-only by design**: no cloud sync, no telemetry, no analytics, no hidden network behavior
* **Easy in, easy out**: import from common formats and export in open formats to avoid lock-in
* **Focused scope**: private journaling over feature sprawl
* **Simplicity over cleverness**: fewer moving parts, smaller attack surface, easier maintenance

Read the full principles and how these translates to the architecture in [PHILOSOPHY.md](https://github.com/fjrevoredo/mini-diarium/blob/HEAD/PHILOSOPHY.md).

> [!NOTE]
> Mini Diarium uses AI tooling as leverage for human engineers, never as a replacement. Every change still passes through deliberate design, careful implementation, proper testing, and direct feedback. Responsibility, authorship, and final judgment remain human.

## Features

* **Key file authentication**: unlock your journal with an X25519 private key file instead of (or alongside) your password, like SSH keys for your journal. See [docs/KEY\_FILE\_AUTHENTICATION.md](https://github.com/fjrevoredo/mini-diarium/blob/HEAD/docs/KEY_FILE_AUTHENTICATION.md).
* **Local-only journals**: create journals that auto-unlock on your device (no password prompt) while still encrypting entries at rest.
* **AES-256-GCM encryption**: all entries are encrypted with a random master key. Each auth method holds ...