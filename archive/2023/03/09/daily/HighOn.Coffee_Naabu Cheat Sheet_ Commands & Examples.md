---
title: Naabu Cheat Sheet: Commands & Examples
url: https://highon.coffee/blog/naabu-cheat-sheet/
source: HighOn.Coffee
date: 2023-03-09
fetch_date: 2025-10-04T09:01:58.731551
---

# Naabu Cheat Sheet: Commands & Examples

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

## Naabu Cheat Sheet: Commands & Examples [∞](/blog/naabu-cheat-sheet/ "Permalink")

cheat-sheet

08 Mar 2023
[![Arr0way](https://github.com/Arr0way.png)
Arr0way](https://twitter.com/Arr0way)

* [What is Naabu?](#what-is-naabu)
* [Naabu vs Nmap](#naabu-vs-nmap)
* [What does Naabu do:](#what-does-naabu-do)
* [Download & Install Naabu](#download--install-naabu)
  + [Naabu Linux Install](#naabu-linux-install)
  + [Kali](#kali)
* [Naabu Example Command Options](#naabu-example-command-options)
  + [Naabu Scan All Ports](#naabu-scan-all-ports)
* [Naabu Input File, Fast Scan + Verify Port 21](#naabu-input-file-fast-scan--verify-port-21)
* [Naabu Fast Scan, Verify, Nmap Services](#naabu-fast-scan-verify-nmap-services)
* [Document Changelog](#document-changelog)

The following Naabu cheat sheet aims to explain what Naabu is, what it does, and how to install it and use it by providing Nabuu command examples in a cheat sheet style documentation format.

## What is Naabu?

Naabu is a simple port scanner written in Golang by Project Discovery, with a goal of being simple and fast.

## Naabu vs Nmap

Why use Naabu over [Nmap](https://highon.coffee/blog/nmap-cheat-sheet/), the primary reason for me personally is the automatic IP deduplication. Meaning, when performing subdomain or domain enumeration of a target organisation, and you feed Naabu an input file of domain or subdomain it will resolve them and only scan unique IP addresses, so you are not wasting time and resources scanning the same target IP address twice.

![Naabu Cheat Sheet](/img/naabu-command-cheat-sheet.jpg)

## What does Naabu do:

* Host discovery
* Automatic IP Deduplication for DNS port scan
* Port discovery / enumeration
* SYN/CONNECT/UDP probe based scanning
* Passive port scanning via Shodan
* Performs IPv4/IPv6 port scanning
* Can be configured to call Nmap to run NSE scripts post port detection
* Multiple input support - STDIN/HOST/IP/CIDR/ASN
* Multiple output format support - JSON/TXT/STDOUT

## Download & Install Naabu

You can obtain Naabu via the [Project Discovery Github](https://github.com/projectdiscovery/naabu).

### Naabu Linux Install

```
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
```

### Kali

Kali has a package for Naabu (caveat, it may not be the latest version):

```
sudo apt install naabu
```

## Naabu File Input Options

Naabu input options, allowing Naabu to read and proccess data from input files.

| Command | Description |
| --- | --- |
| `-host string[]` | hosts to scan ports for (comma-separated) |
| `-list, -l string` | list of hosts to scan ports (file) |
| `-exclude-hosts, -eh string` | hosts to exclude from the scan (comma-separated) |
| `-exclude-file, -ef string` | list of hosts to exclude from scan (file) |

## Naabu Port Options

| Command | Description |
| --- | --- |
| `-port, -p string` | ports to scan (80,443, 100-200 |
| `-top-ports, -tp string` | top ports to scan (default 100) |
| `-exclude-ports, -ep string` | ports to exclude from scan (comma-separated) |
| `-ports-file, -pf string` | list of ports to exclude from scan (file) |
| `-exclude-cdn, -ec` | skip full port scans for CDN's (only checks for 80,443) |

## Nabu Rate Limiting

| Command | Description |
| --- | --- |
| `-c int` | general internal worker threads (default 25) |
| `-rate int` | packets to send per second (default 1000) |

## Naabu Scan Output Options

| Command | Description |
| --- | --- |
| `-o, -output string` | file to write output to (optional) |
| `-json` | write output in JSON lines format |
| `-csv` | write output in csv format |

## Naabu Configuration Options

| Command | Description |
| --- | --- |
| `-scan-all-ips, -sa` | scan all the IP's associated with DNS record |
| `-scan-type, -s string` | type of port scan (SYN/CONNECT) (default "s") |
| `-source-ip string` | source ip |
| `-interface-list, -il` | list available interfaces and public ip |
| `-interface, -i string` | network Interface to use for port scan |
| `-nmap` | invoke nmap scan on targets (nmap must be installed) - Deprecated |
| `-nmap-cli string` | nmap command to run on found results (example: -nmap-cli 'nmap -sV') |
| `-r string` | list of custom resolver dns resolution (comma separated or from file) |
| `-proxy string` | socks5 proxy |
| `-resume` | resume scan using resume.cfg |
| `-stream` | stream mode (disables resume, nmap, verify, retries, shuffling, etc) |

## Naabu Optimization Options

| Command | Description |
| --- | --- |
| `-retries int` | number of retries for the port scan (default 3) |
| `-timeout int` | millisecond to wait before timing out (default 1000) |
| `-warm-up-time int` | time in seconds between scan phases (default 2) |
| `-ping` | ping probes for verification of host |
| `-verify` | validate the ports again with TCP verification |

## Naabu Debug Options

| Command | Description |
| --- | --- |
| `-debug` | display debugging information |
| `-verbose, -v` | display verbose output |
| `-no-color, -nc` | disable colors in CLI output |
| `-silent` | display only results in output |
| `-version` | display version of naabu |
| `-stats` | display stats of the running scan |
| `-si, -stats-interval` | int number of seconds to wait between showing a statistics update (default 5) |

## Naabu Example Command Options

The following are real world examples of Naabu commands.

### Naabu Scan All Ports

```
naabu -p 0-65535
```

## Naabu Input File, Fast Scan + Verify Port 21

```
cat 21.txt | ~/go/bin/naabu -verify -ec -rate 9000 -retries 1 -p 21 -warm-up-time 0 -c 50 -silent -o ftp.txt
```

## Naabu Fast Scan, Verify, Nmap Services

Naabu input file, scan all ports, output to text, fast scan, verify open ports, use Nmap to perform service enumeration

```
naabu -list subdomains.txt -verify -ec -rate 9000 -retries 1 -p 0-65535 -warm-up-time 0 -c 50 -nmap-cli "nmap -sV -oG nmap-naabu-out" -silent -o naab...