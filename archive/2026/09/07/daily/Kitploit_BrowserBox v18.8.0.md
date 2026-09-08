---
title: BrowserBox v18.8.0
url: https://kitploit.com/en/posts/github-browserbox-browserbox-v1880
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:40:56.452477
---

# BrowserBox v18.8.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7160/394f607ef705665239d97ee6563d9a1c830c69c1d1282612cd488bf74da543b9.png)

New releaseSep 7, 2026

# BrowserBox v18.8.0

💚🇺🇸🗽Secure remote browsing anywhere, any way you like it.

Share

![BrowserBox Logo](https://assets.kitploit.com/production/public/readmes/7160/9d79258ff6adf1c9f67b12fcfb5beef3b8c925f59c40f9086ab9968dbe1528e1.jpg)

# BrowserBox by DOSAYGO

**Secure, modern Remote Browser Isolation (RBI) with a clientless experience**

[![License Required](https://img.shields.io/badge/License-Required-red)](https://dosaygo.com#license)
[![BrowserBox Secure RBI](https://img.shields.io/badge/BrowserBox-Secure%20RBI-blue)](https://dosaygo.com)
[![NIST 800-53 Alignment](https://img.shields.io/badge/NIST%20800--53-Alignment-green)](https://dosaygo.com/nist800-53.html)
[![HIPAA Ready](https://img.shields.io/badge/HIPAA-Ready-purple)](https://dosaygo.com/hipaa.html)
[![DLP Options](https://img.shields.io/badge/DLP-Options-pink)](https://dosaygo.com/dlp.html)

**🔐 NEW in v18.0.1 — Passkey authentication on macOS:** sign in to websites with real passkeys inside your remote browser.
Passkeys are created and stored on your Mac's Secure Enclave and unlocked with Touch ID via the
[**BrowserBox Passkeys helper**](https://github.com/BrowserBox/BrowserBox/releases/latest/download/browserbox-passkeys-macos.dmg) —
a small signed & notarized app that BrowserBox prompts you to download when a site requests a passkey. Your keys never leave your device.

**💻 Try it in your terminal — access BrowserBox over SSH via KRNL:**
`ssh krnl.duetbrowser.com`
A full text-mode browser demo, no install and no signup. [Learn more about KRNL →](https://win9-5.com/krnl)

**🇺🇸 NEWS — USA Edition (v17.7.6), coming July 4, 2026:** our most stable BrowserBox yet.
Enhanced streaming stability under co-located and heavy-workload deployments, full suppression of invisible browser prompts that could capture input,
per-user managed browser policy, cross-origin iframe instrumentation (preview) for containers and strict-isolation sites — and 60 FPS streaming re-validated end to end.

**🆕 APRIL 2026:** [**Hyper-Frame**](https://www.hyper-frame.art) — the unlimited iframe — is live!
Embed any website, automate remote browsers, and build web-in-web apps. [Try the live console →](https://www.hyper-frame.art/console)

**Windows 98½ Demo:** Try BrowserBox with our nostalgic [Windows 98½ demo](https://win9-5.com/demo) — free 17-minute cloud browser sessions, no signup required.
**Cloud API:** Purchase minutes and create on-demand cloud browser sessions via REST API.
[API Docs](https://win9-5.com/api/) · [Pricing](https://win9-5.com/pricing/) · [Live Demo](https://win9-5.com/demo) · [Hyper-Frame](https://www.hyper-frame.art)

Happy Birthday, America the Beautiful 🎉🗽

---

BrowserBox is a remote browser isolation (RBI) platform. It streams a full, modern browser to any client — 60 FPS, low latency — and runs on Windows, macOS, Linux, and containers. **A product key is required for all self-hosted usage.**

**At a glance:**

* Clientless RBI — no plugins, no downloads for end users
* 60 FPS streaming with real responsiveness
* Embeds anywhere via `<hyper-frame>` ([Hyper-Frame](https://www.hyper-frame.art)) or `<browserbox-webview>`
* Cloud API for ephemeral sessions, no self-hosting needed
* Works on Windows, macOS, Linux, and containers like Podman, and LXC
* Policy controls, DLP, and audit-friendly workflows

[ASCIInema Recordings](https://asciinema.org/~dosaygo) | [Live Demo](https://win9-5.com/demo) | [Cloud API](https://win9-5.com/api/) | [Pricing](https://win9-5.com/pricing/) | [Current Customer Guide PDF](https://github.com/browserbox/browserbox/blob/main/docs/CUSTOMER-GUIDE.pdf) | [Support](/cdn-cgi/l/email-protection#1475647d5476667b63677166767b6c3a7d7b)

Official sites: [BrowserBox](https://browserbox.io), [DOSAYGO](https://dosaygo.com), [Hyper-Frame](https://www.hyper-frame.art), [CloudTabs](https://browse.cloudtabs.net)

---

> **Notice: Legacy source code removed (March 2026)**
>
> When BrowserBox transitioned to a binary distribution model in late 2025, we retained legacy source code in this repository for a six-month period to give existing customers time to migrate. That period is now over and all legacy source has been removed.
>
> Current BrowserBox source is private and proprietary. It diverges significantly from the legacy code that was previously housed here -- by over 1,000 commits -- with extensive bug fixes, security hardening, and performance enhancements that are absent from the legacy codebase and any forks thereof.
>
> Legacy source code may still be visible in third-party forks as a historical curiosity. That code is **not open source**. Permission is **not** granted to use that source in your products, to train AI models, or to re-implement BrowserBox functionality from it. These acts violate BrowserBox terms. See [LICENSE.md](https://github.com/browserbox/browserbox/blob/main/LICENSE.md) and [TRADEMARK.md](https://github.com/browserbox/browserbox/blob/main/TRADEMARK.md).
>
> Current source is available to customers above a threshold ACV as part of due diligence, on request. Contact [[email protected]](/cdn-cgi/l/email-protection#aad9cbc6cfd9eacec5d9cbd3cdc584c9c5c7).

---

## Table of Contents

1. [Why BrowserBox?](#1-why-browserbox)
2. [Key Benefits](#2-key-benefits)
3. [Who Uses It](#3-who-uses-it)
4. [Real-World Use Cases](#4-real-world-use-cases)
5. [Core Features](#5-core-features)
6. [What's New](#6-whats-new)
7. [See It In Action](#7-see-it-in-action)
8. [Supported Network Topologies](#8-supported-network-topologies)
9. [Platform Compatibility](#9-platform-compatibility)
10. [Install](#10-install)
11. [Quick Start](#11-quick-start)
12. [Documentation](#12-documentation)
13. [GitHub Actions](#13-github-actions)
14. [Cloud API](#14-cloud-api)
15. [Embed BrowserBox](#15-embed-browserbox)
16. [Advanced Usage](#16-advanced-usage)
17. [License Compliance & Privacy](#17-license-compliance--privacy)
18. [FAQ](#18-faq)
19. [Licensing](#19-licensing)
20. [Support](#20-support)
21. [About DOSAYGO](#21-about-dosaygo)

---

## 1. Why BrowserBox?

The web is genuinely dangerous, and standard browsing pushes that risk directly onto your network and your endpoints. BrowserBox flips the model: the browser runs on a server you control, and clients receive a rendered stream — so malware, exploits, and sketchy sites never touch user devices. Security teams get isolation without fighting users over endpoint agents. SaaS builders can embed a full browsing experience into their products without headless brittleness. Regulated organizations get audit trails and DLP controls baked in.

* Threat containment: browser exploits hit the server, not the endpoint
* True clientless access: any modern browser, zero installs for end users
* Embeddable: build web products that include real, live browsing
* Automation-ready: a real browser, not a headless approximation

---

## 2. Key Benefits

* **Threat isolation:** malware, exploits, and bad sites hit the server — not client devices
* **Clientless:** works in any browser, zero install for end users
* **Cross-platform:** Windows, macOS, Linux (Debian, Ubuntu, RHEL, CentOS, NixOS), and containers like LXC
* **Smooth UX:** low-latency rendering, 60 FPS
* **Solid CLI and embedding API** for builders and integrators

---

## 3. Who Uses It

* **Security teams** — isolate browsing risk from corporate endpoints
* **SaaS builders and integrators** — embed live browser sessions in products
* **IT and ops** — access internal web UIs from anywhere, without broad netw...