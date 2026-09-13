---
title: Tourmaline
url: https://kitploit.com/en/tools/github/v-pun215/tourmaline
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:28.747553
---

# Tourmaline

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/v-pun215/tourmaline

![](https://assets.kitploit.com/production/public/tools/54801/23fdce9120ec69b38d9d376ae904031cc1dae160b2a9ed58c97f3355aafdde20-display-v1.webp)

[Indicator of Compromise (IOC) Management](/en/categories/ioc-management)[Reverse Engineering](/en/categories/reverse-engineering)[Malware Analysis](/en/categories/malware-analysis)[Digital Forensics](/en/categories/digital-forensics)[Cryptography](/en/categories/cryptography)[Command and Control](/en/categories/command-and-control)[Threat Intelligence](/en/categories/threat-intelligence)[Learning & Education](/en/categories/education)[Incident Response](/en/categories/incident-response)[DNS Analysis](/en/categories/dns-analysis)

![GitHub](/providers/github.png)v-pun215/tourmaline

# Tourmaline

4261 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

Reverse engineering notes, deobfuscated source, IOCs, and YARA rules for the Tourmaline ClickFix Python RAT, covering its DNS tunnel and blockchain dead-drop C2.

[View Repository](https://github.com/v-pun215/tourmaline)

# Tourmaline

I recently stumbled upon a piece of cleverly designed malware that calls itself "Torumaline".

This README is very kindly written by Claude as I was super busy with exams at the time of this repository's inception.

Exploiting and decrypting this malware took a huge chunk of my time from math prep!

Read the [blogpost!](https://vihaan.dev/blog/inside-tourmaline)

> **FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY**
> All samples are provided for malware analysis and defensive research. Do not execute outside a sandboxed, air-gapped environment.

---

## Overview

**Tourmaline** (`Tourmaline.exe`) is a sophisticated, multi-stage Windows infostealer/backdoor distributed via a **ClickFix campaign** - a fake Cloudflare "Verify you are human" browser popup that tricks users into manually running a malicious command or installer.

The binary is a custom-built **Inno Setup 6.7.0 (Revision 2, 64-bit offsets)** installer that bundles a full Python 3.11 runtime and two stages of obfuscated Python payload. It establishes a persistent backdoor with:

* **DNS tunneling** C2 over UDP port 53 (masquerading as `microsoft.com` queries)
* **Ethereum blockchain dead-drop** for C2 IP distribution (Sepolia testnet)
* **ChaCha20-encrypted** task execution channel
* **ECDSA-signed** commands to prevent sinkholing
* **Anti-sandbox time-lock** (100M iteration countdown, bypassable in O(1))

---

## Repository Structure

root@kitploit:~

```
tourmaline/
├── README.md                  # This file
├── LICENSE                    # Research use license
├── .gitignore
│
├── src/                       # Extracted & deobfuscated source code
│   ├── stage1_loader.py       # Stage 1: Original obfuscated XOR time-lock loader (main.py)
│   ├── stage2_backdoor.py     # Stage 2: Deobfuscated core backdoor (from QGBdu.dxf)
│   └── decrypt_payload.py     # Utility: O(1) payload key recovery & decryption
│
├── iocs/                      # Indicators of Compromise
│   ├── indicators.json        # Structured IOC data (IPs, hashes, domains, registry)
│   ├── indicators.csv         # Flat CSV for SIEM import
│   └── rules.yar              # YARA detection rules
│
└── samples/                   # Malware samples (password-protected)
    ├── README.md              # Sample archive instructions
    ├── Tourmaline_sample.zip  # Password: infected - contains Tourmaline.exe
    └── QGBdu.dxf             # Raw encrypted Stage 2 payload blob
```

---

## Infection Vector

The malware is distributed via **ClickFix** - a social engineering technique where a compromised or attacker-controlled website overlays a fake Cloudflare CAPTCHA or browser verification page. The overlay instructs the victim to:

1. Press `Win+R`
2. Paste a command (copied to clipboard by the page's JavaScript)
3. Press Enter

The pasted command downloads and silently executes `Tourmaline.exe`. The installer runs `/VERYSILENT /SUPPRESSMSGBOXES /NORESTART`.

---

## Binary Format

> **Note:** Stock `innoextract 1.9` cannot extract this binary — it only supports Revision 1. Revision 2 uses 64-bit offsets and requires custom parsing (see `src/decrypt_payload.py`).

---

## Execution Flow

root@kitploit:~

```
Tourmaline.exe
│
├─ Inno Setup installer runs silently
│   ├─ Extracts Python 3.11 runtime to %APPDATA%\Tourmaline\
│   ├─ Extracts main.py (Stage 1 loader)
│   ├─ Extracts QGBdu.dxf (encrypted Stage 2 blob)
│   ├─ Kills any existing pythonw.exe instances
│   └─ Registers persistence (Task Scheduler / registry)
│       └─ Name: "TourmalineUpdate" / "Hardware monitoring service"
│
├─ Stage 1: main.py (XOR Time-Lock Loader)
│   ├─ Counts _n from 99,999,999 → 0 (anti-sandbox delay ~hours on slow VMs)
│   ├─ At each _n, constructs 33-byte XOR key: struct.pack('>I', _n) + hardcoded_suffix
│   ├─ Tests key against known plaintext header of QGBdu.dxf
│   └─ On match: decrypts QGBdu.dxf entirely and exec()s the result
│       └─ O(1) bypass: known-plaintext attack on first 4 bytes (see below)
│
└─ Stage 2: QGBdu.dxf → Python backdoor
    ├─ Reads MachineGuid from HKLM\SOFTWARE\Microsoft\Cryptography
    ├─ Derives mutex Global\Tourmaline_<hash>
    ├─ Resolves C2 IP via Ethereum dead-drop (Sepolia testnet)
    ├─ Establishes DNS tunnel to C2
    └─ Poll-execute loop: fetches tasks, exec()s Python, returns output
```

---

## Stage 1 — Anti-Sandbox Time-Lock (O(1) Bypass)

The loader (`main.py`) uses a countdown from `99,999,999` to find the XOR decryption key. On a real machine this completes in seconds (because `_n` starts high and the true value is near `14,511,188`). In a sandbox with a short time limit, the loop never completes.

**Key structure:**

root@kitploit:~

```
full_key = struct.pack('>I', _n) + bytes.fromhex('2b0cffe07b06ac25793b3f00cfaa2dd5881c2d6378165247539dbbdaeb')
```

Since we know the first 16 bytes of the plaintext (`g1 = lambda l6,` ), we can recover `_n` instantly via known-plaintext XOR attack:

root@kitploit:~

```
key_prefix = bytes(ciphertext[i] ^ known_plaintext[i] for i in range(4))
# Result: key_prefix = 00dd6c54 → _n = 14,511,188
```

Use `src/decrypt_payload.py` to reproduce this.

---

## Stage 2 — Core Backdoor Architecture

### Configuration (Hardcoded)

### Blockchain Dead-Drop (C2 Resilience)

The malware calls an Ethereum smart contract on the **Sepolia testnet** to retrieve the active C2 IP address. This means the attacker can change the C2 IP at any time by updating the contract — traditional IP blocklist-based C2 disruption is ineffective.

root@kitploit:~

```
Contract : 0x2d7a04cca0c34005f58393f30ac725e25f19e5f5
Selector : 0xeb9fd6fe
Network  : Ethereum Sepolia (chainId 11155111)
RPC      : https://ethereum-sepolia-rpc.publicnode.com
Result   : ChaCha20-encrypted blob containing current C2 IP
```

The returned data is decrypted with the hardcoded ChaCha20 key to reveal the live C2 address. At time of analysis, this resolved to **`158.94.211.185`** (ver...