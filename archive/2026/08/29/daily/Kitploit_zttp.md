---
title: zttp
url: https://kitploit.com/en/tools/gitlab/nihal799/zttp
source: Kitploit
date: 2026-08-29
fetch_date: 2026-08-30T07:42:00.746557
---

# zttp

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

zttp — Zero-trust SSH bastion proxy with Vault-backed key management, RBAC policy enforcement, full session recording, and admin TUI for auditable access to production infrastructure. | Kitploit

[Tools](/en/tools)/![GitLab](/providers/gitlab.png)GitLab/nihal799/zttp

![](https://assets.kitploit.com/production/public/tools/53548/9a97b4e32c760a8774ddc8246282cd86d183a057a4027730cf875b1697f6bc4a-display-v1.webp)

[Authentication & Authorization](/en/categories/authentication-authorization)[Cloud Infrastructure Security](/en/categories/cloud-infrastructure-security)[Defensive Tools](/en/categories/defensive-tools)[Network Security](/en/categories/network-security)[DevSecOps](/en/categories/devsecops)[Identity & Access Management (IAM)](/en/categories/identity-access-management)

![GitLab](/providers/gitlab.png)nihal799/zttp

# zttp

Zero-trust SSH bastion proxy with Vault-backed key management, RBAC policy enforcement, full session recording, and admin TUI for auditable access to production infrastructure.

[View Repository](https://gitlab.com/nihal799/zttp)

402 months ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Website](https://gitlab.com/Nihal799/zttp)

# ZTTP — Zero-Trust Transparent Proxy

> **A hardened, self-hosted SSH bastion host** with Vault-backed key management, RBAC policy enforcement, full session recording, and an interactive admin TUI — designed for teams who need auditable, zero-trust access to production infrastructure.

---

## Table of Contents

* [Why ZTTP](#why-zttp)
* [Architecture Overview](#architecture-overview)
* [Feature Highlights](#feature-highlights)
* [Prerequisites](#prerequisites)
* [Quick Start — Server](#quick-start--server)
* [Quick Start — Client](#quick-start--client)
* [Configuration](#configuration)
* [Roles & RBAC Policy](#roles--rbac-policy)
* [Admin Console](#admin-console)
* [Audit Logs & Session Recordings](#audit-logs--session-recordings)
* [Building from Source](#building-from-source)
* [Makefile Reference](#makefile-reference)
* [Screenshots & Demo](#screenshots--demo)
* [Project Structure](#project-structure)
* [Security Model](#security-model)
* [Contributing](#contributing)
* [License](#license)

---

## Why ZTTP

Modern engineering teams need a way to give developers **the minimum access required** to do their jobs — no more, no less. Traditional SSH key distribution is error-prone: keys get shared, forgotten on laptops, and revoked days too late.

ZTTP solves this by acting as the **single door** into your infrastructure:

---

## Architecture Overview

root@kitploit:~

```
Developer Laptop
      │
      │  zttp
      │  (Under the hood: SSH over port 2224)
      ▼
┌─────────────────────────────────────────────────────────┐
│                     ZTTP Proxy                          │
│                                                         │
│  ① Auth Gate     — bcrypt/Argon2id login TUI           │
│  ② RBAC Engine   — environment-aware policy check      │
│  ③ Vault Fetch   — ephemeral SSH key retrieval         │
│  ④ Bridge        — transparent TCP tunnel              │
│  ⑤ Audit Writer  — ttyrec frame recorder               │
└──────────┬──────────────────────────────────────────────┘
           │  ssh (private IP, ephemeral key)
           ▼
     Target Server
```

**Infrastructure services (Docker Compose):**

---

## Feature Highlights

* 🔐 **Zero-trust authentication** — Interactive SSH login TUI with bcrypt password hashing, rate limiting, and account lockout after 5 failed attempts
* 🛡️ **RBAC policy engine** — Per-role, per-environment access control with a single optimized PostgreSQL JOIN (no round-trips)
* 🗝️ **Vault-backed SSH keys** — Private keys never touch disk; fetched ephemerally per session from HashiCorp Vault
* 📹 **Full session recording** — All sessions are recorded in `.ttyrec` format with timestamped frames
* 🖥️ **Interactive Admin TUI** — Full terminal UI for user management, server registration, access grants, and log review
* 🔍 **Audit Log Viewer** — Browse sessions by server, replay recordings, or read clean text logs directly from the admin console
* ⚡ **Kill Switch** — gRPC endpoint to terminate any live session instantly
* 📋 **Admin Action Log** — Every administrative action (user creation, access grants, log viewing) is logged to a persistent audit trail
* 🌍 **Multi-platform client** — Single-binary CLI for Linux, macOS (amd64/arm64), and Windows

---

## Prerequisites

**Server (proxy host):**

* Docker ≥ 24 and Docker Compose ≥ 2.20
* A public or LAN-accessible IP on port `2224`
* `make` (optional, but recommended)

**Developer (client):**

* Any SSH client (`ssh` command)
* Linux, macOS, or Windows machine

---

## Quick Start — Server

### 1. Clone the repository

root@kitploit:~

```
git clone https://gitlab.com/Nihal799/zttp.git
cd zttp
```

### 2. Configure your environment

root@kitploit:~

```
cp .env.example .env
```

Edit `.env` and set at minimum:

root@kitploit:~

```
PROXY_NODE_IP=<your-server-public-ip>
POSTGRES_PASSWORD=<a-strong-password>
VAULT_TOKEN=<a-strong-vault-token>
```

> ⚠️ **Never commit your `.env` file.** It is listed in `.gitignore`.

### 3. Start all services

root@kitploit:~

```
make docker-up
# or directly:
docker compose -f deploy/docker-compose.yml up -d --build
```

### 4. Verify services are healthy

root@kitploit:~

```
make docker-ps
curl http://localhost:8080/healthz
```

### 5. Build and publish the CLI installers

root@kitploit:~

```
make release PROXY_ADDR=<your-server-ip>:2224
```

This cross-compiles clients for all platforms and auto-updates `dist/install.sh` and `dist/install.ps1` with the correct server URL. The Nginx container serves these at `http://<your-server-ip>:8555/`.

---

## Quick Start — Client

### Linux / macOS

root@kitploit:~

```
curl -fsSL http://<proxy-ip>:8555/install.sh | bash
```

### Windows (PowerShell, run as Administrator)

root@kitploit:~

```
irm http://<proxy-ip>:8555/install.ps1 | iex
```

### Connect

Once installed, connect to the ZTTP gateway:

root@kitploit:~

```
zttp
# or directly:
ssh -p 2224 <your-username>@<proxy-ip>
```

You will be presented with a terminal login screen. After authentication, you'll see a list of servers you are authorized to access.

---

## Configuration

All configuration is via environment variables (or `.env` file). See `.env.example` for the full reference.

---

## Roles & RBAC Policy

ZTTP uses a **role-based** model. Each user is assigned a role; each role has a policy that defines which server **environments** it can access.

> Roles and server assignments are managed through the **Admin Console** (see below). The RBAC engine performs all checks in a single PostgreSQL query — it never exposes *why* access was denied to the client (enumeration protection).

---

## Admin Console

Connect to the `zttp-admin` server from the gateway menu, or log in with an account that has the `security-admin` role.

The Admin Console provides:

> All admin actions are logged to `admin-actions.log` inside the audit v...