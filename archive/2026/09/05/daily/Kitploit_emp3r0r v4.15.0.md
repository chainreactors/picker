---
title: emp3r0r v4.15.0
url: https://kitploit.com/en/posts/github-jm33-m0-emp3r0r-v4150
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:32.847331
---

# emp3r0r v4.15.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/388/61c478dfa5ca274ec99bb7547c0402e30ce10a0ff2f61d78721cf4d687563cc4.png)

New releaseSep 5, 2026

# emp3r0r v4.15.0

Self‑healing Gossip Mesh C2 with Assisted Peer Discovery, Cross-Platform BOF Execution, and Scriptable Agents.

Share

![emp3r0r](https://assets.kitploit.com/production/public/readmes/388/73c4ac7800cb1c221dd61e97f3f9ccad66bc8c5dea12ad532ea7765746d423b6.png)

### emp3r0r

**A self-healing, memory-only C2 for Linux and Windows — agents that survive broken links, never touch disk, and script their way through the Win32 API.**

[![Discord](https://img.shields.io/badge/Discord-Join%20Server-7289da?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/vU98aQtk9f)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-ff69b4?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sponsors/jm33-m0)

![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/jm33-m0/emp3r0r?filename=core/go.mod)
[![Tests](https://github.com/jm33-m0/emp3r0r/actions/workflows/test.yml/badge.svg)](https://github.com/jm33-m0/emp3r0r/actions/workflows/test.yml)
![GitHub License](https://img.shields.io/github/license/jm33-m0/emp3r0r)
[![GitHub release](https://img.shields.io/github/release/jm33-m0/emp3r0r.svg)](https://github.com/jm33-m0/emp3r0r/releases)

---

![emp3r0r operator console screenshot](https://github.com/user-attachments/assets/8952f405-2af9-4840-b57f-086498f389b8)

## What is emp3r0r?

emp3r0r is a post-exploitation framework and C2 built for Linux and Windows environments where stealth and resilience aren't optional. Instead of assuming a reliable connection back to one server, agents form a self-healing mesh that keeps working when links break. Instead of asking the target for Python or PowerShell, they execute everything in memory. And instead of limiting you to one platform's tricks, emp3r0r runs Windows BOFs, Linux objects, and Starlark scripts — all fileless, all in-process.

---

## Key Highlights & Unique Features

### 🐍 Scriptable Agents (Embedded Starlark Engine & Win32 API Proxy)

Every agent carries its own scripting engine, so you can drop in new post-exploitation logic without compiling or shipping binaries.

* Scripts run entirely in memory — no Python, Bash, or PowerShell required on the target, and no command interpreters spawned.
* A full set of built-in APIs covers file I/O, HTTP, command execution, and more, straight from script code.
* On Windows, scripts can call native Win32 functions directly — the agent proxies straight into system DLLs.
* Modules are plain Starlark files with a small JSON manifest, so adding your own is easy and fileless.

**Why this matters:** writing and extending agent functionality becomes as simple as editing a script, with none of the footprint of dropping an interpreter or a new binary on the target.

---

### 🔐 TOFU Cryptographic Identity Pinning

Agents bind their identity to a cryptographic key the first time they talk to you — and that binding never changes.

* Re-enrollment with different credentials is treated as an impostor and rejected.
* Removing an agent is an explicit operator decision, not something a stolen key can do quietly.

**Why this matters:** session hijacking and agent cloning simply don't happen; every agent you talk to is the one you enrolled.

---

### 🔒 Perfect Forward Secrecy (PFS)

Every C2 and peer link uses ephemeral ECDH keys with session-derived encryption keys.

**Why this matters:** even if a long-term key is compromised later, it can't be used to decrypt traffic that already passed.

---

### 🕸️ Autonomous P2P Gossip Mesh Network

Agents discover each other and relay traffic through a gossip mesh, so the operation doesn't collapse when one link or one server disappears.

* Peers connect over camouflage mTLS 1.3 or reliable UDP (KCP), with every hop encrypted.
* Traffic routes around dead relays automatically — no manual proxy surgery mid-operation.
* Segments with no direct C2 access still stay reachable through their neighbors.

**Why this matters:** the network does the pivoting for you. Cut a link, lose a box, or block the C2 — agents re-route on their own.

---

### 📂 P2P Filesystem

Files move between agents directly, not just through the C2.

* Transfers ride encrypted peer-to-peer tunnels, so internal networks don't bottleneck on your server.
* Files are cached in agent memory as encrypted blobs and served to peers on demand.
* If no peer has a file, the agent fetches it from the C2 automatically.

**Why this matters:** delivery is fast and mostly invisible to the C2 channel — ideal for egress-restricted environments.

---

### 📡 Multi-Protocol Listeners & Pluggable Stagers

Getting an agent in is treated as seriously as keeping it alive.

* HTTP, TCP, and UDP listeners with reliable framing and customizable HTTP profiles.
* A roughly 2KB stager built on direct Linux syscalls — no libc, no toolchain on the target.
* Pluggable stager transports and self-unpacking packers let you blend initial access into whatever channel your target allows, and defeat static signature matching along the way.
* Stage and agent code respect read/write/execute discipline — never RWX.

**Why this matters:** small, adaptable, and memory-hygienic initial access means you can land on hosts that would otherwise be out of reach.

---

### 🧩 Native Cross-Platform BOF & PICO Support (COFF, ELF & PICO)

Run compiled C modules in-process on either platform:

* Windows COFF/BOF binaries with typed argument packing.
* Linux ELF relocatable objects loaded straight into agent memory.
* Crystal-Kit PICO modules with SilentMoonwalk callstack spoofing.
* Kerbeus-BOF, Remote-OPs, and a Situational Awareness suite ship ready to use.

**Why this matters:** BOFs are only as good as their loader — emp3r0r runs them in-process with no new process and no trace left behind, on both Linux and Windows.

---

### 🔑 Windows Tokens, Netonly Sessions & Kerberos Tickets (PTT)

Once you're on a Windows host, emp3r0r lets you *become* the users on it — without ever dropping a tool.

* Steal an access token from any running process and use it everywhere: Go modules, Starlark, BOFs.
* Create disposable netonly sessions (`make_token`) that keep your agent's own identity and only borrow the target user's for outbound access — any password works, nothing is ever validated.
* Import Kerberos tickets (`import_ticket`) into those sessions for full pass-the-ticket: your network identity becomes the ticket's (say, the Domain Admin) while your local identity never changes.
* Every module accepts `--token`, `--user`, and `--ticket`, so switching identity is one flag away — including creating a session and loading a ticket in a single command.
* Tickets live per logon session, so the DA material stays quarantined in a disposable session you can purge, and the agent process itself stays clean.

**Why this matters:** lateral movement to machines running no agent at all — SMB shares, service control, CIFS — becomes a normal part of your workflow, authenticated as the user you've borrowed, not as a tool on disk.

---

### 🧦 SOCKS5 Pivoting & Operator-Side tun2socks

Pivot without burning another implant: the C2 runs a SOCKS5 proxy that relays through the agent you select, and the operator side can go one step further with a transparent TUN device.

* `socks_start 1080` gives you a SOCKS5 endpoint on the C2 that tunnels through the chosen agent — point proxychains or any tool at it and you're inside the target network.
* `tun2socks start --route 10.10.0.0/24` creates a TUN device tha...