---
title: emp3r0r v4.11.0
url: https://kitploit.com/en/posts/github-jm33-m0-emp3r0r-v4110
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:50:54.637663
---

# emp3r0r v4.11.0

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

New releaseAug 21, 2026

# emp3r0r v4.11.0

Self‑healing Gossip Mesh C2 with Assisted Peer Discovery, Cross-Platform BOF Execution, and Scriptable Agents.

Share

![emp3r0r](https://assets.kitploit.com/production/public/readmes/388/73c4ac7800cb1c221dd61e97f3f9ccad66bc8c5dea12ad532ea7765746d423b6.png)

### emp3r0r

**Self‑healing Gossip Mesh C2 with Assisted Peer Discovery, Cross-Platform BOF Execution, and Scriptable Agents.**

[![Discord](https://img.shields.io/badge/Discord-Join%20Server-7289da?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/vU98aQtk9f)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-ff69b4?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sponsors/jm33-m0)

![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/jm33-m0/emp3r0r?filename=core/go.mod)
[![Tests](https://github.com/jm33-m0/emp3r0r/actions/workflows/test.yml/badge.svg)](https://github.com/jm33-m0/emp3r0r/actions/workflows/test.yml)
![GitHub License](https://img.shields.io/github/license/jm33-m0/emp3r0r)
[![GitHub release](https://img.shields.io/github/release/jm33-m0/emp3r0r.svg)](https://github.com/jm33-m0/emp3r0r/releases)

---

![Screenshot From 2026-08-10 19-37-20](https://assets.kitploit.com/production/public/readmes/388/5b4f801fefd82e8a66f4a3ea35cbd95ed0e2e71a6074e7eccdad70a8ebfa3dcd.png)

## What is emp3r0r?

emp3r0r is an advanced, zero-trust post-exploitation framework and command & control (C2) system designed for Linux and Windows target environments. Built from the ground up to operate in high-security environments, emp3r0r combines **autonomous gossip mesh networking**, **fileless memory-only execution**, **cross-platform BOF loading**, **inter-agent file transfer**, and **in-memory scriptable agents** to deliver superior stealth, operational control, and operational security (OPSEC).

---

## Key Highlights & Unique Features

### 🐍 Scriptable Agents (Embedded Starlark Engine & Win32 API Proxy)

emp3r0r agents feature an embedded **Starlark scripting engine** (a Python dialect implemented purely in Go). Scripts execute filelessly in memory without requiring Python, Bash, or PowerShell installed on the target.

* **Zero Host Dependencies:** Executes standalone scripts without spawning command interpreters (`/bin/sh`, `powershell.exe`) or relying on installed runtimes.
* **Built-in Agent Go APIs:** Exposed functions for filesystem operations (`read_file`, `write_file`, `list_dir`, `mkdir`, `remove`, `exists`), HTTP networking (`http_get`, `http_post`), command execution (`exec_cmd`), and hashing (`crypto_hash`).
* **Dynamic Win32 API Proxy:** On Windows targets, Starlark scripts can dynamically load system DLLs and execute native Win32 APIs (`win_call`, `win_alloc`, `win_free`, `win_read_mem`) directly from script code without compiling native C code.
* **Modular Integration:** Starlark scripts are defined using JSON manifests (`config.json`) for seamless CLI parameter parsing and distribution.

**Why this matters:** Traditional C2 script modules require host interpreters or process spawning, leaving heavy disk or command-line execution traces. emp3r0r's scriptable agents execute complex logic entirely in memory with native system interaction.

---

### 🔐 TOFU Cryptographic Identity Pinning

emp3r0r enforces **Trust-On-First-Use (TOFU)** with strict UUID and public-key pinning upon agent enrollment.

* **Immutable Binding:** Once enrolled, an agent's UUID is pinned to its cryptographic public key. Re-enrollment with altered credentials is rejected as an impersonation attempt.
* **Controlled Reset:** De-registration requires explicit operator authorization via `forget_agent`.

**Why this matters:** Prevents session hijacking, agent cloning, and silent identity drift across operational environments.

---

### 🔒 Perfect Forward Secrecy (PFS)

All C2 and peer communications enforce **ECDH key exchange** with **HKDF-derived session keys**.

* **Ephemeral Keys:** Each session generates unique encryption keys.
* **Decoupled Security:** Compromising long-term keys or an individual agent cannot compromise past or parallel communications.

**Why this matters:** Prevents retrospective decryption of intercepted network captures.

---

### 🕸️ Autonomous P2P Gossip Mesh Network

Agents in egress-restricted or isolated network segments autonomously discover peers and tunnel traffic via a gossip-based (Memberlist) mesh network.

* **Pluggable Peer Transports:** Support for camouflage **mTLS 1.3** (using ephemeral certificates) and **KCP** (reliable UDP).
* **End-to-End Encryption:** All inter-agent mesh hops are wrapped in AES-GCM encryption.
* **Low Network Footprint:** Direct agent-to-agent relaying eliminates unnecessary broadcast noise and centralized C2 connection chokepoints.

**Why this matters:** Pivoting across segmented networks occurs autonomously without requiring constant operator intervention or static proxy setups.

---

### 📂 P2P Filesystem

Direct agent-to-agent file sharing via P2P relay transport (mTLS/KCP) to accelerate file delivery across internal networks.

* **Encrypted P2P Tunnels:** Tunnel transfers across peers using mTLS/KCP to bypass egress restrictions and reduce central C2 bandwidth bottlenecks.
* **Smart In-Memory File Caching**: Files are cached in agent memory as encrypted blobs; can be seamlessly served for other agents to download on demand. When requesting a file, agents look at their local memfs, then other peers, finally the C2.
* **Automatic C2 Relay Fallback:** If a target peer lacks the requested file, it dynamically fetches and streams it from the C2 server on demand.

**Why this matters:** Direct agent-to-agent file sharing maximizes transfer speeds, bypasses network chokepoints, and reduces direct C2 traffic visibility.

---

### 📡 Multi-Protocol Listeners & Stagers

Flexible Stage 0 downloader stagers and protocol listeners for initial access and payload delivery.

* **Multi-Protocol Listeners:** Embedded and standalone HTTP, TCP, and UDP listeners with reliable sequence-acknowledgment framing and custom HTTP profiles.
* **Standalone C Downloader Stager:** Built with direct, libc-independent Linux syscalls for compatibility across distributions without symbol errors.
* **Tiny Payload Size:** While emp3r0r agent binaries are ~20MB without compression, this stager is below 1.5KB; the sRDI-like payload it fetches from emp3r0r listener, is ~8MB (compressed from agent binary in ELF shared object format).
* **Flexible Formats:** Compiles into raw position-independent shellcode (`.bin`), standalone ELF executables, or shared objects (`.so`).
* **In-Memory Hardening:** Allocates stage memory with read-write permissions, de-obfuscates payloads, and enforces read-execute prior to reflectively executing Stage 1.

---

### 🧩 Native Cross-Platform BOF Support (COFF & ELF)

Execute in-memory binary modules on both Windows and Linux targets:

* **Windows COFF Loaders:** Run Windows BOF binaries filelessly with typed parameter packing (`int`, `short`, `cstr`, `wstr`, `binary`).
* **Linux ELF Object Loaders:** Load ELF relocatable object files (`.o`) directly into agent memory on Linux.
* **Bundled BOF Suites:** Built-in support for Kerbeus-BOF, Remote-OPs, and Situational Awareness (SA) module collections.

**Why this matters:** Eliminates process creation overhead and circumvents command-line monitoring by running compiled C modules in-process.

---

### 🔑 On-Demand Windows Token Manipulation

Agen...