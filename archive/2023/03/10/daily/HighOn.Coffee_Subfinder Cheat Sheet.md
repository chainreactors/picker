---
title: Subfinder Cheat Sheet
url: https://highon.coffee/blog/subfinder-cheat-sheet/
source: HighOn.Coffee
date: 2023-03-10
fetch_date: 2025-10-04T09:09:06.670807
---

# Subfinder Cheat Sheet

* [Home](/)
* [Blog](/blog/)
* [About](/about/)
* [Services](/services/)

# [HighOn.Coffee ![Logo](/img/highoncoffee.png)](/)

* [Home](/)
* [Blog](/blog/)
* [About](/about/)
* [Services](/services/)

Navigate the blog…
Home

Katana Cheat Sheet - Commands, Flags & Examples
Nmap Cheat Sheet: Commands, Flags, Switches & Examples (2024)
ADB Commands Cheat Sheet - Flags, Switches & Examples Tutorial
httpx Cheat Sheet - Commands & Examples Tutorial
SQLMap Cheat Sheet: Flags & Commands for SQL Injection
Nikto Cheat Sheet - Commands & Examples
Subfinder Cheat Sheet
Naabu Cheat Sheet: Commands & Examples
Reverse Shell Cheat Sheet: PHP, ASP, Netcat, Bash & Python
Insecure Direct Object Reference (IDOR): Definition, Examples & How to Find
DNS Tunneling dnscat2 Cheat Sheet
SSH Lateral Movement Cheat Sheet
Android Pen Testing Environment Setup
Password Reset Testing Cheat Sheet
SSRF Cheat Sheet & Bypass Techniques
Pen Testing Tools Cheat Sheet
LFI Cheat Sheet
HowTo: Kali Linux Chromium Install for Web App Pen Testing
InsomniHack CTF Teaser - Smartcat2 Writeup
InsomniHack CTF Teaser - Smartcat1 Writeup
FristiLeaks 1.3 Walkthrough
SickOS 1.1 - Walkthrough
The Wall Boot2Root Walkthrough
/dev/random: Sleepy Walkthrough CTF
/dev/random Pipe walkthrough
Lord of the Root Walkthrough CTF
Vim Cheat Sheet [2022 Update] + NEOVIM
Jenkins RCE via Unauthenticated API
SkyTower - Walkthrough
Zorz Walkthrough
Systemd Cheat Sheet
Freshly Walkthrough
MacBook - Post Install Config + Apps
FartKnocker - Walkthrough
nbtscan Cheat Sheet
enum4linux Cheat Sheet - Commands & Examples
Linux Local Enumeration Script
Security Harden CentOS 7
SSH & Meterpreter Pivoting Techniques
Sokar - Walkthrough
Tr0ll 2 Walkthrough
Tr0ll 1 Walkthrough
Linux Commands Cheat Sheet
Pen Testers Lab: Shellshock CVE-2014-6271 - Walkthrough
LAMP Security CTF8 - Walkthrough
Kioptrix Level 2014 Walkthrough
LAMP Security CTF7 - Walkthrough
LAMP Security CTF6 - Walkthrough
LAMP Security CTF5 - Walkthrough
LAMP Security CTF4 - Walkthrough
Kioptrix Level 1.2 Walkthrough
Kioptrix Level 1.1 Walkthrough
Kioptrix Level 1 Walkthrough

## Subfinder Cheat Sheet [∞](/blog/subfinder-cheat-sheet/ "Permalink")

cheat-sheet

09 Mar 2023
[![Arr0way](https://github.com/Arr0way.png)
Arr0way](https://twitter.com/Arr0way)

![Subfinder Logo](/img/subfinder-logo.png)

* [What is Subfinder](#what-is-subfinder)
* [Install Subfinder](#install-subfinder)
* [Subfinder API Setup](#subfinder-api-setup)
  + [Subfinder Config File](#subfinder-config-file)
  + [Subfinder API Sources](#subfinder-api-sources)
* [Example Subfinder API Config File](#example-subfinder-api-config-file)
* [Subfinder Usage](#subfinder-usage)
* [Example Subfinder Commands](#example-subfinder-commands)
  + [Find Subdomains Single Domain](#find-subdomains-single-domain)
  + [Verify Subfinder Results With HTTPX](#verify-subfinder-results-with-httpx)
  + [Subfinder + Naabu Portscan](#subfinder--naabu-portscan)
* [Conclusion](#conclusion)
* [Document Changelog](#document-changelog)

## What is Subfinder

Subfinder is a passive subdomain discovery tool made by Project Discovery. The following subfinder cheat sheet provides an overview of the command flags for Subfinder and common command examples for real world usage. Subfinder can be used to obtain a number of valid subdomains both passively and actively, to identify more attack surface for [penetration testing](/penetration-testing/) or bug bounty recon or assessment.

## Install Subfinder

```
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

##### Configure API Keys

Subfinder works straight after install, however with API keys (even a free key) will improve passive subdomain results.

Subfinder Flags & Syntax

root:~#
subfinder -h

## Subfinder API Setup

Configuring Subfinder to use free or paid API services will likely improve the discovered domains the tool can find. You can list the sources Subfinder uses by running `subfinder -ls`.

### Subfinder Config File

In order to setup subfinder API keys you need to create or modify the existing configuration file. The filesystem location for the subfinder config file is at: `$HOME/.config/subfinder/provider-config.yaml` the subfinder config file needs to be populated with the API keys that you will need to obtain from the various sources that have (kindly) been listed below.

### Subfinder API Sources

Subfinder supports the following data API sources:

| NAME | URL |
| --- | --- |
| BeVigil | `https://bevigil.com/osint-api` |
| BinaryEdge | `https://binaryedge.io` |
| BufferOver | `https://tls.bufferover.run` |
| C99 | `https://api.c99.nl/` |
| Censys | `https://censys.io` |
| CertSpotter | `https://sslmate.com/certspotter/api/` |
| Chaos | `https://chaos.projectdiscovery.io` |
| Chinaz | `http://my.chinaz.com/ChinazAPI/DataCenter/MyDataApi` |
| DNSDB | `https://api.dnsdb.info` |
| Fofa | `https://fofa.info/static_pages/api_help` |
| FullHunt | `https://fullhunt.io` |
| GitHub | `https://github.com` |
| Intelx | `https://intelx.io` |
| PassiveTotal | `http://passivetotal.org` |
| quake | `https://quake.360.cn` |
| Robtex | `https://www.robtex.com/api/` |
| SecurityTrails | `http://securitytrails.com` |
| Shodan | `https://shodan.io` |
| ThreatBook | `https://x.threatbook.cn/en` |
| VirusTotal | `https://www.virustotal.com` |
| WhoisXML API | `https://whoisxmlapi.com/` |
| ZoomEye | `https://www.zoomeye.org` |
| ZoomEye API | `https://api.zoomeye.org` |
| dnsrepo | `https://dnsrepo.noc.org` |
| Hunter | `https://hunter.qianxin.com/` |
| Facebook | `https://developers.facebook.com` |
| BuiltWith | `https://api.builtwith.com/domain-api` |

## Example Subfinder API Config File

The following is an example of the API config file:

```
binaryedge:
  - 0bf8919b-aab9-42e4-9574-d3b639324597
  - ac244e2f-b635-4581-878a-33f4e79a2c13
censys:
  - ac244e2f-b635-4581-878a-33f4e79a2c13:dd510d6e-1b6e-4655-83f6-f347b363def9
certspotter: []
passivetotal:
  - [email protected]:sample_password
redhuntlabs:
  - ENDPOINT:API_TOKEN
  - https://reconapi.redhuntlabs.com/community/v1/domains/subdomains:joEPzJJp2AuOCw7teAj63HYrPGnsxuPQ
securitytrails: []
shodan:
  - AAAAClP1bJJSRMEYJazgwhJKrggRwKA
github:
  - ghp_lkyJGU3jv1xmwk4SDXavrLDJ4dl2pSJMzj4X
  - ghp_gkUuhkIYdQPj13ifH4KA3cXRn8JD2lqir2d4
zoomeyeapi:
  - 4f73021d-ff95-4f53-937f-83d6db719eec
quake:
  - 0cb9030c-0a40-48a3-b8c4-fca28e466ba3
facebook:
  - APP_ID:APP_SECRET
intelx:
  - HOST:API_KEY
  - 2.intelx.io:s4324-b98b-41b2-220e8-3320f6a1284d
```

Above file source: https://docs.projectdiscovery.io/tools/subfinder/install#post-install-configuration

## Subfinder Usage

How to use Subfinder to find domains:

| Flag | Description |
| --- | --- |
|  |  |
| --- | --- |
| `-d, -domain string[]` | domains to find subdomains for |
| `-dL, -list string` | file containing list of domains for subdomain discovery |
| `-s, -sources string[]` | specific sources to use for discovery (-s crtsh,github). Use -ls to display all available sources. |
| `-recursive` | use only sources that can handle subdomains recursively (e.g. subdomain.domain.tld vs domain.tld) |
| `-all` | use all sources for enumeration (slow) |
| `-es, -exclude-sources string[]` | sources to exclude from enumeration (-es alienvault,zoomeye) |
| `-m, -match string[]` | subdomain or list of subdomain to match (file or comma separated) |
| `-f, -filter string[]` | subdomain or list of subdomain to filter (file or comma separated) |
| `-rl, -rate-limit int` | maximum number of http requests to send per second |
| `-t int` | number of concurrent goroutines for resolving (-active only) (default 10) |
| `-o, -output string` | file to write output to |
| `-oJ, -json` | write output in JSONL(ines) format |
| `-oD, -output-dir string` | directory to write output (-dL only) |
| `-cs, -collect-sources` | include all sources in the output (-json only) |
| `-oI, -ip` | include host IP in output (-active only) |
| `-config string` | flag config file (default "$HOME/.config/subf...