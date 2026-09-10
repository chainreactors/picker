---
title: firezone headless-client-1.5.12
url: https://kitploit.com/en/posts/github-firezone-firezone-headless-client-1512
source: Kitploit
date: 2026-09-09
fetch_date: 2026-09-10T06:51:19.775810
---

# firezone headless-client-1.5.12

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/4836/8aa4b2440860598a74ad08b6c841bbd3765178176cb676ce4ad1acfe0e39bad3.png)

New releaseSep 9, 2026

# firezone headless-client-1.5.12

Enterprise-ready zero-trust access platform built on WireGuard®.

Share

![firezone logo](https://assets.kitploit.com/production/public/readmes/4836/f31d616b031c1b8a2d605a9dc98fdb1fd469d7627b0b0dca54f2c6d8956a9801.png)

**Secure remote access that's 3x faster than OpenVPN with zero-trust, peer-to-peer connections**

[Docs](https://www.firezone.dev/kb)
| [Quickstart](https://www.firezone.dev/kb/quickstart)
| [Download Clients](https://www.firezone.dev/kb/client-apps)
| [Discussions](https://github.com/firezone/firezone/discussions)
| [Support](https://www.firezone.dev/support)

---

![firezone](https://img.shields.io/static/v1?logo=github&logoColor=959DA5&label=Test&labelColor=333a41&message=passing&color=3AC358)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/firezone/firezone)
![GitHub closed issues](https://img.shields.io/github/issues-closed/firezone/firezone)
[![X (formerly Twitter) Follow](https://img.shields.io/badge/Follow-@firezonehq-black?style=flat&logo=x)](https://x.com/intent/follow?screen_name=firezonehq)

---

## Overview

[Firezone](https://www.firezone.dev/?utm_source=readme) is an open source
platform to securely manage remote access for any-sized organization. Unlike
most VPNs, Firezone takes a granular, least-privileged approach to access
management with group-based policies that control access to individual
applications, entire subnets, and everything in between.

![architecture](https://assets.kitploit.com/production/public/readmes/4836/d608b105e8d759809890b8e1d9dc649e5b8381b18e135a7cd1430009c82f9a2c.png)

## Getting Started

### Option 1: Cloud (Recommended)

Get started in under 2 minutes with our managed solution.

[**Sign up free →**](https://app.firezone.dev/sign_up?utm_source=readme) *(No credit card required)*

Once you've signed up, follow the instructions in the welcome email to:

1. Install the client on your device
2. Connect to your first resource
3. Configure access policies

## Features

Firezone is:

* **Fast:** Built on WireGuard® to be
  [3-4 times](https://wireguard.com/performance/) faster than OpenVPN with sub-10ms latency overhead.
* **Scalable:** Deploy two or more gateways for automatic load balancing and
  failover.
* **Private:** Peer-to-peer, end-to-end encrypted tunnels prevent packets from
  routing through our infrastructure.
* **Secure:** Zero attack surface thanks to Firezone's holepunching tech which
  establishes tunnels on-the-fly at the time of access.
* **Open:** Our entire product is open-source, allowing anyone to audit the
  codebase.
* **Flexible:** Authenticate users via email, Google Workspace, Okta, Entra ID,
  or OIDC and sync users and groups automatically.
* **Simple:** Deploy gateways and configure access in minutes with a snappy
  admin UI.

Firezone is **not:**

* A tool for creating bi-directional mesh networks
* A full-featured router or firewall
* An IPSec or OpenVPN server

## Performance & Security

### Performance

* **Throughput:** Up to 5 Gbps per connection
* **Latency:** Hole-punched connections eliminate routing overhead
* **Scaling:** Need more capacity? Simply add more gateways
* **Memory Usage:** Lightweight Rust-based data plane requires only a few MB

### Security & Compliance

* **Encryption:** WireGuard® protocol with ChaCha20/Poly1305
* **Authentication:** Multiple SSO providers supported
* **Zero Trust:** All connections authenticated and authorized
* **Audit Logs:** Full activity logging for compliance and monitoring
* **Compliance:** SOC 2 Type I and II compliant (managed offering)

### Comparison with Alternatives

| Feature | Legacy VPN | Firezone |
| --- | --- | --- |
| Setup Time | Hours | 5 minutes |
| Performance | Baseline | 3x faster |
| Architecture | Hub-spoke | Peer-to-peer |
| Zero Trust | ❌ | ✅ |
| Open Source | ❌ | ✅ |

## Contents of this repository

This is a monorepo containing the full Firezone product and its documentation,
organized as follows:

* [elixir](https://github.com/firezone/firezone/blob/main/elixir): Admin portal and control plane
* [rust/](https://github.com/firezone/firezone/blob/main/rust): Data plane and internal Rust libraries:
  + [rust/gateway](https://github.com/firezone/firezone/blob/main/rust/gateway): Gateway - Tunnel server based on WireGuard
    and deployed to your infrastructure.
  + [rust/relay](https://github.com/firezone/firezone/blob/main/rust/relay): Relay - STUN/TURN server to facilitate
    holepunching.
  + [rust/headless-client](https://github.com/firezone/firezone/blob/main/rust/headless-client): Cross-platform CLI client.
  + [rust/gui-client](https://github.com/firezone/firezone/blob/main/rust/gui-client): Cross-platform GUI client.
* [swift/](https://github.com/firezone/firezone/blob/main/swift/apple): macOS / iOS clients.
* [kotlin/](https://github.com/firezone/firezone/blob/main/kotlin/android): Android / ChromeOS clients.
* [policy-templates/](https://github.com/firezone/firezone/blob/main/policy-templates): MDM policy templates (Windows ADMX/ADML, macOS profile manifests) published for admin download and compiled into the Windows client.
* The marketing website and product documentation live in the separate [firezone/website](https://github.com/firezone/website) repository.

## License & Pricing

### Open Source (Apache 2.0 + Elastic 2.0)

* ✅ Full source code available for audit
* ✅ Self-hosting allowed (educational/hobby use)
* ✅ Community support via GitHub Discussions
* ⚠️ Production self-hosting not officially supported

### Cloud - Usage Based

* ✅ Managed hosting with SLA
* ✅ Production-ready with enterprise support
* ✅ Automatic updates and maintenance
* 💰 Starting free, then per-seat pricing
* [**View detailed pricing →**](https://www.firezone.dev/pricing?utm_source=readme)

**Pricing Overview:**

* **Starter:** Free for 6 users with basic features
* **Team:** $5 / user / month with advanced features
* **Enterprise:** Custom pricing with directory sync, compliance, priority support

### Enterprise Features

* 🗂️ **Directory Sync** - Sync users and groups from Google Workspace, Okta, or Entra
* 📝 **Audit Logs** - Complete activity tracking for up to 90 days for compliance
* 🏢 **Priority Support** - Dedicated Slack channel for your organization
* 🎯 **Custom Integrations** - Tailored solutions for your infrastructure

## Frequently asked questions (FAQ)

### Can I self-host Firezone?

Our [license](#license) won't stop you from self-hosting the entire Firezone
product top to bottom, but our internal APIs are changing rapidly so we can't
meaningfully support self-hosting Firezone in production at this time.

If you're feeling especially adventurous and want to self-host Firezone for
**educational** or **hobby** purposes, follow the instructions to spin up a
local development environment in [CONTRIBUTING.md](https://github.com/firezone/firezone/blob/main/docs/CONTRIBUTING.md).

The latest published clients (on App Stores and on
[releases](https://github.com/firezone/firezone/releases)) are only guaranteed
to work with the managed version of Firezone and may not work with a self-hosted
portal built from this repository. This is because Apple and Google can
sometimes delay updates to their app stores, and so the latest published version
may not be compatible with the tip of `main` from this repository.

Therefore, if you're experimenting with self-hosting Firezone, you will probably
want to use clients you build and distribute yourself as we...