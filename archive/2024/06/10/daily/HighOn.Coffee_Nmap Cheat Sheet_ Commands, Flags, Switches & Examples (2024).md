---
title: Nmap Cheat Sheet: Commands, Flags, Switches & Examples (2024)
url: https://highon.coffee/blog/nmap-cheat-sheet/
source: HighOn.Coffee
date: 2024-06-10
fetch_date: 2025-10-06T16:55:20.396234
---

# Nmap Cheat Sheet: Commands, Flags, Switches & Examples (2024)

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

## Nmap Cheat Sheet: Commands, Flags, Switches & Examples (2024) [∞](/blog/nmap-cheat-sheet/ "Permalink")

cheat-sheet

09 Jun 2024
[![Arr0way](https://github.com/Arr0way.png)
Arr0way](https://twitter.com/Arr0way)

The following Nmap cheat sheet aims to explain what Nmap is, what it does, and how to use it by providing Nmap command examples in a cheat sheet style documentation format.

Orignal Published Date: 11th December 2014

## What is Nmap?

**Nmap** (network mapper), the god of port scanners used for network discovery and the basis for most security enumeration during the initial stages of a [penetration test](/penetration-testing/). The tool was written and maintained by Fyodor AKA Gordon Lyon.

[Nmap](http://nmap.org) displays exposed services on a target machine along with other useful information such as the verion and OS detection.

Nmap has made twelve movie appearances, including The Matrix Reloaded, Die Hard 4, Girl With the Dragon Tattoo, and The Bourne Ultimatum.

![Nmap Trinity](/img/nmap-trinity.png)

* [What is Nmap?](#what-is-nmap)
* [What does Nmap do:](#what-does-nmap-do)
* [Download & Install Nmap](#download--install-nmap)
  + [Debian / Ubuntu / Kali](#debian--ubuntu--kali)
  + [Nmap RHEL / Fedora](#nmap-rhel--fedora)
  + [Nmap Windows](#nmap-windows)
  + [Nmap MacOS](#nmap-macos)
* [Nmap Commands](#nmap-commands)
  + [Nmap scan from file](#nmap-scan-from-file)
  + [Nmap Scan all Ports](#nmap-scan-all-ports)
  + [Nmap output formats](#nmap-output-formats)
  + [Nmap Netbios Examples](#nmap-netbios-examples)
  + [Nmap Nikto Scan](#nmap-nikto-scan)
* [Nmap Cheatsheet](#nmap-cheatsheet)
  + [Target Specification](#target-specification)
  + [Host Discovery](#host-discovery)
  + [Scan Techniques](#scan-techniques)
  + [Port Specification and Scan Order](#port-specification-and-scan-order)
  + [Service Version Detection](#service-version-detection)
  + [Script Scan](#script-scan)
  + [OS Detection](#os-detection)
  + [Timing and Performance](#timing-and-performance)
  + [Firewalls IDS Evasion and Spoofing](#firewalls-ids-evasion-and-spoofing)
  + [Nmap Scan Output File Options](#nmap-scan-output-file-options)
  + [Misc Nmap Options](#misc-nmap-options)
* [Nmap Enumeration Command Examples](#nmap-enumeration-command-examples)
  + [Enumerating Netbios](#enumerating-netbios)
  + [Nmap find Netbios name.](#nmap-find-netbios-name)
  + [Nmap Netbios MS08-067](#nmap-netbios-ms08-067)
* [Nmap Scan Tuning & Optimisation](#nmap-scan-tuning--optimisation)
  + [Nmap Rate](#nmap-rate)
  + [Nmap Parallelism](#nmap-parallelism)
  + [Nmap Host Group Sizes](#nmap-host-group-sizes)
  + [Nmap Host Timeout](#nmap-host-timeout)
  + [Nmap Scan Delay](#nmap-scan-delay)
  + [Nmap Disable DNS Lookups](#nmap-disable-dns-lookups)
    - [Nmap Black List Detection?](#nmap-black-list-detection)
  + [Nmap Optimising Portscans for Targets](#nmap-optimising-portscans-for-targets)
* [Nmap FAQ](#nmap-faq)
  + [What is Nmap Used for?](#what-is-nmap-used-for)
  + [Is Nmap Illegal?](#is-nmap-illegal)
  + [Is Nmap a Vulnerability Scanner](#is-nmap-a-vulnerability-scanner)
  + [Why do hackers use Nmap?](#why-do-hackers-use-nmap)
  + [Nmap Download](#nmap-download)
  + [Nmap Scripts List](#nmap-scripts-list)
* [Document Changelog](#document-changelog)

## What does Nmap do:

* Host discovery
* Port discovery / enumeration
* Service discovery
* Operating system version detection
* Hardware (MAC) address detection
* Service version detection
* Vulnerability / exploit detection, using Nmap scripts (NSE)
* Nmap IDS / Portscan Detection & Scan Time Optimisation

## Download & Install Nmap

Nmap can be downloaded from [nmap.org](https://nmap.org/), however commonly Nmap is installed via your Linux distributions package manager:

### Debian / Ubuntu / Kali

How to Install Nmap on Ubuntu, Debian, Kali or other Linux systems using the APT package manager.

```
apt install nmap
```

### Nmap RHEL / Fedora

How to Install Nmap on RHEL, Fedora, CentOS, Rocky Linux or other Linux systems using the DNF package manager.

```
dnf install nmap
```

### Nmap Windows

Download Nmap for Windows and install: [Nmap for Windows](https://nmap.org/download#windows)

### Nmap MacOS

How to install nmap on MacOS using Brew.

```
brew install nmap
```

## Nmap Commands

Basic Nmap scanning command examples, often used at the first stage of enumeration.

| Command | Description |
| --- | --- |
| `nmap -sP 10.0.0.0/24` | Nmap scan the network, listing machines that respond to ping. |
| `nmap -p 1-65535 -sV -sS -T4 target` | A full TCP port scan using with service version detection - `T1-T5` is the speed of the scan. |
| `nmap -v -sS -A -T4 target` | Prints verbose output, runs stealth syn scan, T4 timing, OS and version detection + traceroute and scripts against target services. |
| `nmap -v -sS -A -T5 target` | Prints verbose output, runs stealth syn scan, T5 timing, OS and version detection + traceroute and scripts against target services. |
| `nmap -v -sV -O -sS -T5 target` | Prints verbose output, runs stealth syn scan, T5 timing, OS and version detection. |
| `nmap -v -p 1-65535 -sV -O -sS -T4 target` | Prints verbose output, runs stealth syn scan, T4 timing, OS and version detection + full port range scan. |
| `nmap -v -p 1-65535 -sV -O -sS -T5 target` | Prints verbose output, runs stealth syn scan, T5 timing, OS and version detection + full port range scan. |

##### Agressive scan timings are faster, but could yeild inaccurate results!

T5 uses very aggressive scan timings and could lead to missed ports, T3-4 is a better compromise if you need fast results (depending on if local network or remote).

### Nmap scan from file

| Command | Description |
| --- | --- |
| `nmap -iL ip-addresses.txt` | Scans a list of IP addresses, you can add options before / after. |

### Nmap Scan all Ports

| Command | Description |
| --- | --- |
| `nmap -p- ...