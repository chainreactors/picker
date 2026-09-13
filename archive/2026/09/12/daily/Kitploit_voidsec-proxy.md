---
title: voidsec-proxy
url: https://kitploit.com/en/tools/github/voidsecsoftwares/voidsec-proxy
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:30.609761
---

# voidsec-proxy

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/voidsecsoftwares/voidsec-proxy

![](https://assets.kitploit.com/production/public/tools/54809/ded554ebf299ea39d6c85cfc9e10b6f8d2b5bbbcba6525e74836875a2a4a1acd-display-v1.webp)

[Password Cracking](/en/categories/password-cracking)[Reconnaissance](/en/categories/reconnaissance)[Encryption/Decryption Tools](/en/categories/encryption-decryption-tools)[Port Scanning](/en/categories/port-scanning)[DNS & Subdomain Enumeration](/en/categories/dns-subdomain-enumeration)[Data Exfiltration](/en/categories/data-exfiltration)[Web Security](/en/categories/web-security)[Steganography](/en/categories/steganography)[Digital Forensics](/en/categories/digital-forensics)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Penetration Testing](/en/categories/penetration-testing)

[Shellcode Generation](/en/categories/shellcode-generation)

![GitHub](/providers/github.png)voidsecsoftwares/voidsec-proxy

# voidsec-proxy

Multi-module offensive security toolkit for SOCKS5 proxy chaining, port scanning, DNS enumeration, hash cracking, reverse shell generation, steganography, and anonymization.

[View Repository](https://github.com/voidsecsoftwares/voidsec-proxy)

3343 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

# voidsec-proxy

root@kitploit:~

```
 ██╗   ██╗ ██████╗ ██╗██████╗ ███████╗███████╗ ██████╗
 ██║   ██║██╔═══██╗██║██╔══██╗██╔════╝██╔════╝██╔════╝
 ██║   ██║██║   ██║██║██║  ██║███████╗█████╗  ██║
 ╚██╗ ██╔╝██║   ██║██║██║  ██║╚════██║██╔══╝  ██║
  ╚████╔╝ ╚██████╔╝██║██████╔╝███████║███████╗╚██████╗
   ╚═══╝   ╚═════╝ ╚═╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
```

**v3.0.0** | **18 modules** | **50+ commands** | **zero dependencies**

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
![Platform: Linux](https://img.shields.io/badge/platform-Linux-orange.svg)
[![Version: 3.0.0](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/VoidSecSoftwares/voidsec-proxy)

> Not another script kiddie tool. This one actually does something.

---

## Table of Contents

* [Installation](#installation)
* [Quick Start](#quick-start)
* [Commands Reference](#commands-reference)
  + [proxy](#proxy) — SOCKS5 chain rotation
  + [scan](#scan) — port scanner
  + [dns](#dns) — DNS toolkit
  + [crack](#crack) — hash cracking
  + [password](#password) — password generator
  + [mutate](#mutate) — wordlist mutator
  + [recon](#recon) — network reconnaissance
  + [web](#web) — web fingerprinting
  + [exfil](#exfil) — covert channels & encoding
  + [encrypt](#encrypt) — AES-GCM file encryption
  + [shred](#shred) — secure file deletion
  + [stego](#stego) — steganography
  + [shell](#shell) — reverse shell generator
  + [forensic](#forensic) — file analysis
  + [anon](#anon) — anonymization
  + [plugin](#plugin) — plugin management
  + [config](#config) — configuration
* [Proxies File Format](#proxies-file-format)
* [Plugin API](#plugin-api)
* [License](#license)

---

## Installation

root@kitploit:~

```
# Clone the repository
git clone https://github.com/VoidSecSoftwares/voidsec-proxy.git

# Enter the directory
cd voidsec-proxy

# Install (basic)
pip install -e .

# Install with crypto support (AES-GCM, ChaCha20, steganography)
pip install -e ".[crypto]"
```

**Requirements:** Python 3.8+ | Zero mandatory dependencies

---

## Quick Start

root@kitploit:~

```
# Start a SOCKS5 proxy chain
voidsec-proxy proxy -f proxies.txt

# Scan a target
voidsec-proxy scan -t 10.0.0.1

# Resolve DNS
voidsec-proxy dns example.com

# Generate a password
voidsec-proxy password -l 20 -c 5

# Full recon on a target
voidsec-proxy recon -t 10.0.0.1
```

---

## Commands Reference

### proxy

SOCKS5 proxy chain with automatic rotation.

root@kitploit:~

```
# Basic usage
voidsec-proxy proxy -f proxies.txt

# Custom listen address and port
voidsec-proxy proxy -f proxies.txt -l 0.0.0.0 -p 1080

# Shuffle proxy order on start
voidsec-proxy proxy -f proxies.txt -s
```

### scan

Multi-threaded TCP port scanner with banner grabbing.

root@kitploit:~

```
# Scan common ports
voidsec-proxy scan -t 10.0.0.1

# Scan specific ports
voidsec-proxy scan -t 10.0.0.1 -p 22,80,443,3389

# Scan port range, export to JSON
voidsec-proxy scan -t 10.0.0.1 -r 1-1000 -o results.json -f json
```

### dns

DNS resolution, reverse lookups, and subdomain enumeration.

root@kitploit:~

```
# Resolve A records
voidsec-proxy dns example.com

# Multiple record types
voidsec-proxy dns example.com -t A -t MX -t TXT

# Reverse DNS lookup
voidsec-proxy dns 8.8.8.8 -r

# Subdomain enumeration
voidsec-proxy dns example.com -e -w wordlist.txt
```

### crack

Hash cracking with wordlist support.

root@kitploit:~

```
# Crack MD5 hash
voidsec-proxy crack --hash 5f4dcc3b5aa765d61d8327deb882cf99 -t md5 -w rockyou.txt

# Hash text with SHA256
voidsec-proxy crack --hash-text "hello" -t sha256

# Hash file
voidsec-proxy crack --hash-file secret.bin -t sha512
```

### password

Password generator with strength auditing.

root@kitploit:~

```
# Generate 5 passwords, 20 chars each
voidsec-proxy password -l 20 -c 5

# Audit a password
voidsec-proxy password -a "MyP@ssw0rd"

# Generate 6-word passphrase
voidsec-proxy password --passphrase -l 6
```

### mutate

Wordlist mutation engine.

root@kitploit:~

```
# Apply all mutations
voidsec-proxy mutate -w wordlist.txt -o mutated.txt -m leet,upper,append_num,dups

# Leet speak + numbers
voidsec-proxy mutate -w wordlist.txt -o out.txt -m leet,append_num
```

### recon

Full network reconnaissance.

root@kitploit:~

```
# Full recon (IP, geo, ASN, open ports)
voidsec-proxy recon -t 10.0.0.1

# WHOIS lookup
voidsec-proxy recon --whois example.com

# IP geolocation
voidsec-proxy recon --geo 8.8.8.8

# ASN lookup
voidsec-proxy recon --asn 8.8.8.8

# Traceroute
voidsec-proxy recon --traceroute 8.8.8.8
```

### web

Web application fingerprinting and directory brute-force.

root@kitploit:~

```
# Full fingerprint
voidsec-proxy web -u https://target.com

# Header analysis
voidsec-proxy web --headers https://target.com

# Directory brute-force
voidsec-proxy web --dirbust https://target.com -w wordlist.txt
```

### exfil

Covert channels and data encoding.

root@kitploit:~

```
# Encode data
voidsec-proxy exfil --encode "secret data" -m base64
voidsec-proxy exfil --encode "secret data" -m morse
voidsec-proxy exfil --encode "secret data" -m dns

# Decode data
voidsec-proxy exfil --decode "dGVzdA==" -m base64

# Vigenere cipher
voidsec-proxy exfil --vigenere "encrypted" --key "secret"
```

### encrypt

AES-GCM file encryption.

root@kitploit:~

```
# Encrypt a file
voidsec-proxy encrypt -i secret.txt -o secret.enc -p "mypassword"

# Decrypt a file
voidsec-proxy encrypt -i secret.enc -o secret.txt -p "mypassword" -d
```

| Flag | Description |
| --- | --- |
| `-i, --input` | Input file (required) |
| `-o, --output` | Output file (required) |
|  |

### shred

Secure file deletion with multiple passes.

root@kitploit:~

```
# Shred file ...