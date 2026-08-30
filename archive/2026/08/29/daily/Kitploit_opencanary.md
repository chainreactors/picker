---
title: opencanary
url: https://kitploit.com/en/tools/github/thinkst/opencanary
source: Kitploit
date: 2026-08-29
fetch_date: 2026-08-30T07:42:01.239957
---

# opencanary

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

opencanary — Low-resource honeypot that emulates common network services to detect post-breach attacker activity, with extensible protocol modules and configurable alerting. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/thinkst/opencanary

![](https://assets.kitploit.com/production/public/tools/50945/270e6e5425132d6d3f83ea963bed3340f5a6713783588a43a3101c07ca561b86-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Network Security](/en/categories/network-security)[Threat Intelligence](/en/categories/threat-intelligence)[Intrusion Detection](/en/categories/intrusion-detection)[Incident Response](/en/categories/incident-response)[Log Analysis](/en/categories/log-analysis)

![GitHub](/providers/github.png)thinkst/opencanary

# opencanary

Low-resource honeypot that emulates common network services to detect post-breach attacker activity, with extensible protocol modules and configurable alerting.

[View Repository](https://github.com/thinkst/opencanary)

3.0k4094611 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

[Website](http://opencanary.org)

Share

# OpenCanary by Thinkst Canary

![](https://assets.kitploit.com/production/public/readmes/50945/270e6e5425132d6d3f83ea963bed3340f5a6713783588a43a3101c07ca561b86/af33f41d1b8d6773d5032bc8fa8a732d20c6e1931445eff97ae66ae7f29f8d0b-display-v1.webp) OpenCanary is a multi-protocol network honeypot. It's primary use-case is to catch hackers after they've breached non-public networks. It has extremely low resource requirements and can be tweaked, modified, and extended.

[![OpenCanary Tests](https://github.com/thinkst/opencanary/actions/workflows/opencanary_tests.yml/badge.svg)](https://github.com/thinkst/opencanary/actions/workflows/opencanary_tests.yml)
[![Docker build](https://github.com/thinkst/opencanary/actions/workflows/docker-build.yml/badge.svg)](https://github.com/thinkst/opencanary/actions/workflows/docker-build.yml)
[![Publish to PyPI](https://github.com/thinkst/opencanary/actions/workflows/publish.yml/badge.svg)](https://github.com/thinkst/opencanary/actions/workflows/publish.yml)

## Overview

OpenCanary runs as a daemon and implements multiple common network protocols. When attackers breach networks and interact with the honeypot, OpenCanary will send you alerts via a variety of mechanisms.

OpenCanary is implemented in Python, so the core honeypot is cross-platform; however, certain features require specific OSes. Running on Linux will give you the most options. It has extremely low resource requirements; for example, it can be deployed happily on a Raspberry Pi or a VM with minimal resources.

This README describes how to install and configure OpenCanary on Ubuntu Linux and MacOS.

OpenCanary is the Open Source version of our commercial [Thinkst Canary](https://canary.tools) honeypot.

## Table of Contents

* **[Prerequisites](#prerequisites)**
* **[Features](#features)**
* **[Installation](#installation)**
  + [Installation on Ubuntu](#installation-on-ubuntu)
  + [Installation on macOS](#installation-on-macos)
  + [Installation via Git](#installation-via-git)
  + [Installation for Docker](#installation-for-docker)
* **[Configuring OpenCanary](#configuring-opencanary)**
  + [Creating the initial configuration](#creating-the-initial-configuration)
  + [Enabling protocol modules and alerting](#enabling-protocol-modules-and-alerting)
  + [Optional modules](#optional-modules)
    - [SNMP](#snmp)
    - [Portscan](#portscan)
    - [Samba Setup](#samba-setup)
* **[Running OpenCanary](#running-opencanary)**
  + [Directly on Linux or macOS](#directly-on-linux-or-macos)
  + [With docker compose](#with-docker-compose)
  + [With Docker](#with-docker)
* **[Documentation](#documentation)**
* **[Project Participation](#project-participation)**
  + [Contributing](#contributing)
  + [Security Vulnerability Reports](#security-vulnerability-reports)
  + [Bug reports](#bug-reports)
  + [Feature Requests](#feature-requests)
  + [Code of Conduct](#code-of-conduct)

## Prerequisites

* AMD64: Python 3.10+
* ARM64: Python 3.10+
* *Optional* SNMP requires the Python library Scapy
* *Optional* Samba module needs a working installation of Samba
* *Optional* Portscan uses iptables (not nftables) and is only supported on Linux-based operating systems

## Features

* Mimic an array of network-accessible services for attackers to interact with.
* Receive various alerts as soon as potential threats are detected, highlighting the threat source IP address and where the breach may have occurred.

## Installation

The OpenCanary installation essentially involves ensuring the Python environment is ready, then installing the OpenCanary Python package (plus optional extras).

If `uv` is installed, you can use it for virtual environment creation and package installation. If it is not installed, the standard `python`/`pip` flow below continues to work.

### Installation on Ubuntu

Installation on Ubuntu 22.04 LTS or 24.04 LTS:

root@kitploit:~

```
$ sudo apt-get install python3-dev python3-pip python3-virtualenv python3-venv python3-scapy libssl-dev libpcap-dev
$ virtualenv env/
$ . env/bin/activate
$ pip install opencanary
```

Optional `uv` equivalent:

root@kitploit:~

```
$ uv venv env
$ . env/bin/activate
$ uv pip install opencanary
```

Optional extras (if you wish to use the Windows File Share module, and the SNMP module):

root@kitploit:~

```
$ sudo apt install samba # if you plan to use the Windows File Share module
$ pip install scapy pcapy-ng # if you plan to use the SNMP module
```

### Installation on macOS

First, create and activate a new Python virtual environment:

root@kitploit:~

```
$ virtualenv env/
$ . env/bin/activate
```

Optional `uv` equivalent:

root@kitploit:~

```
$ uv venv env
$ . env/bin/activate
```

Macports users should then run:

root@kitploit:~

```
$ sudo port install openssl
$ env ARCHFLAGS="-arch x86_64" LDFLAGS="-L/opt/local/lib" CFLAGS="-I/opt/local/include" pip install cryptography
```

Alternatively, Homebrew x86 users run:

root@kitploit:~

```
$ brew install openssl
$ env ARCHFLAGS="-arch x86_64" LDFLAGS="-L/usr/local/opt/openssl/lib" CFLAGS="-I/usr/local/opt/openssl/include" pip install cryptography
```

Homebrew M1 users run:

root@kitploit:~

```
$ brew install openssl
$ env ARCHFLAGS="-arch arm64" LDFLAGS="-L/opt/homebrew/opt/[email protected]/lib" CFLAGS="-I/opt/homebrew/opt/[email protected]/include" pip install cryptography
```

(The compilation step above is necessary as multiple OpenSSL versions may exist, which can confound the Python libraries.)

Now the installation can run as usual:

root@kitploit:~

```
$ pip install opencanary
$ pip install scapy pcapy-ng # optional
```

With `uv` installed, the equivalent commands are:

root@kitploit:~

```
$ uv pip install opencanary
$ uv pip install scapy pcapy-ng # optional
```

The Windows File Share (smb) module is not available on macOS.

### Installation via Git

To install from source, instead of running pip do the following:

root@kitploit:~

``...