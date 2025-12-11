---
title: SmbCrawler – SMB Share Discovery and Secret-Hunting
url: https://www.darknet.org.uk/2025/11/smbcrawler-smb-share-discovery-and-secret-hunting/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-10
fetch_date: 2025-12-11T03:24:39.671810
---

# SmbCrawler – SMB Share Discovery and Secret-Hunting

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# SmbCrawler – SMB Share Discovery and Secret-Hunting

November 24, 2025

Views: 770

SmbCrawler is a credentialed SMB spider that takes domain credentials and a list of hosts, then aggressively walks network shares for you. It checks permissions, crawls directory trees, auto-downloads interesting files, and reports likely secrets such as passwords, SSH keys, configuration files, DPAPI blobs, and database dumps. For internal red teams, it is a purpose-built engine for turning “we have a foothold” into “we own the file servers”.

![SmbCrawler - SMB Share Discovery and Secret-Hunting](https://www.darknet.org.uk/wp-content/uploads/2025/11/SmbCrawler-SMB-Share-Discovery-and-Secret-Hunting-640x427.jpg)

## Overview

Every serious internal pentest or red-team engagement ends up abusing SMB misconfiguration. Shared drives still hold plaintext creds, exported mailboxes, unprotected backups, and “temporary” dumps that never got cleaned up. Doing this manually with basic tools and Windows Explorer is slow and noisy. SmbCrawler solves that by automating the boring parts:

* Take credentials once.
* Feed it hostnames, IP ranges, or Nmap XML.
* Let it enumerate shares, permissions, and directory structures at scale.
* Automatically pull down files that match secret-hunting profiles into a structured SQLite-backed data store.

The result is an internal discovery and exfil pipeline that you can run in hours, not days, with a repeatable output format you can grep, query, and report from.

## Features

From the live README, SmbCrawler ships with a carefully designed feature set:

* **Flexible target input** – accepts hostnames, single IPs, IP ranges or Nmap XML files as input.
* **Permission checks** – tests authentication as guest and as supplied user, share access, and (optionally) write access by creating a temporary directory.
* **Configurable crawl depth** – control how deep to walk each share, with separate profiles to override depth for specific paths.
* **Pass-the-hash support** – operate with NTLM hashes instead of cleartext passwords when necessary.
* **Interesting file detection** – ships with profiles that flag and download likely high-value files (credentials, configs, dumps, keys).
* **Threaded, pausable engine** – multi-threaded crawling with runtime controls to pause, skip hosts or shares, and inspect status.
* **SQLite-backed output** – writes findings to a SQLite database and a structured output directory, plus optional interactive HTML reporting.

## Installation

SmbCrawler is a Python tool published on PyPI. The author explicitly recommends using `pipx` so you do not pollute your system Python. Installation examples from the README:

# Minimal install
pipx install smbcrawler
# Recommended install with binary conversion helpers (PDF, XLSX, DOCX, ZIP...)
pipx install "smbcrawler&#91;binary-conversion]"

|  |  |
| --- | --- |
| 1  2  3  4  5 | # Minimal install  pipx install smbcrawler    # Recommended install with binary conversion helpers (PDF, XLSX, DOCX, ZIP...)  pipx install "smbcrawler&#91;binary-conversion]" |

The extra `[binary-conversion]` dependency pulls in MarkItDown so SmbCrawler can convert common binary formats to text before scanning them for secrets. For red-team use, you almost always want this turned on.

## Usage

The README’s quick example shows a typical crawl against a file of targets with domain credentials:

$ smbcrawler crawl -i hosts.txt -u pen.tester -p iluvb0b -d contoso.local -t 10 -D 5

|  |  |
| --- | --- |
| 1 | $ smbcrawler crawl -i hosts.txt -u pen.tester -p iluvb0b -d contoso.local -t 10 -D 5 |

That command:

* Uses `hosts.txt` as the target list.
* Authenticates as `pen.tester` in the `contoso.local` domain.
* Spawns 10 worker threads (`-t 10`).
* Crawls each share up to depth 5 (`-D 5`).

At runtime, you can interact with the crawler:

* `p` – pause and selectively skip hosts or shares.
* `<space>` – print current progress.
* `s` – show a more detailed status view.

The profile system does the heavy lifting. Profiles (YAML) define which files, directories, and shares are “interesting”, where to dig deeper, and which secrets to flag. You can supply your own profiles alongside the built-in defaults to target specific line-of-business apps or internal naming schemes.

## Attack Scenario

**Objective:** turn one compromised Windows credential into complete knowledge of SMB data exposure, plus a curated bag of loot, in a single engagement sprint.

1. Obtain valid domain credentials via phishing, password spraying or a prior foothold.
2. Enumerate potential SMB hosts using existing tools (for example [keimpx](https://www.darknet.org.uk/2010/02/keimpx-open-source-smb-credential-scanner/) or Nmap scripts) and export them to a target file.
3. Run SmbCrawler with a shallow depth (for example `-D 1`) and optional write checks to map which hosts and shares are readable and writable. Save this as a dedicated crawl file.
4. Use the initial database to prioritise “high-value” shares, then rerun SmbCrawler with deeper depth and tuned profiles against a reduced host set.
5. From the SQLite database and downloaded files, extract passwords, SSH keys, VPN configs, DPAPI blobs, application secrets and database dumps. Feed those into lateral movement tooling such as [NetExec](https://www.darknet.org.uk/2025/10/netexec-network-execution-toolkit-for-windows-and-active-directory/) to pivot further.
6. Optionally, map resulting privileges and paths in Active Directory with [BloodHound](https://www.darknet.org.uk/2019/06/bloodhound-hacking-active-directory-trust-relationships/), turning share-level findings into full graph-based attack paths.

## Red Team Relevance

SmbCrawler hits a rare sweet spot between practicality and depth. It is fast enough to run routinely on real client networks, and opinionated enough to surface valuable loot instead of dumping terabytes of junk. From a red-team perspective, you can:

* Quantify SMB exposure: “X hosts, Y readable shares, Z with write access, N high-value secrets found”.
* Build repeatable playbooks for different client environments by shipping pre-tuned profiles with your engagement kit.
* Tighten operational security: SmbCrawler lets you avoid noisy manual browsing and random PowerShell scripts scattered through jump boxes.

It also plays nicely with other offensive SMB tooling already covered on Darknet. Combine share discovery and credential validation (keimpx, CredNinja, NetExec) with SmbCrawler’s deep crawl to show how quickly a motivated attacker can move from “one set of creds” to “everyone’s home drive” in a typical enterprise.

## Detection and Mitigation

From the blue-team side, SmbCrawler’s capabilities translate directly into controls you should prioritise:

* **Audit share permissions regularly** – especially “Everyone” and “Authenticated Users” access on sensitive roots and profile shares.
* **Harden write access** – limit where regular users can create directories and files; SmbCrawle...