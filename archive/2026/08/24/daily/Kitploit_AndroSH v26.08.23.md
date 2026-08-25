---
title: AndroSH v26.08.23
url: https://kitploit.com/en/posts/github-ahmed-alnassif-androsh-v260823
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:59:10.845531
---

# AndroSH v26.08.23

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9438/0b6ed88e17bd3522abd6fc3c3672d2e8a679ebd55be702895dbba0c897de3420.png)

New releaseAug 24, 2026

# AndroSH v26.08.23

AndroSH No-Root Multi-Distro Linux on Android via Shizuku/ADB - Run Arch, Fedora, Alpine, Debian, Ubuntu, Kali, Void, Manjaro, OpenSUSE & Chimera with full system integration, proot isolation & Termux:X11 GUI.

Share

# AndroSH - Run Linux Distributions on Android (No Root, ADB/Shizuku Powered)

**Run and manage full Linux distributions on your Android device - no root required.**

[![Tests](https://github.com/ahmed-alnassif/AndroSH/actions/workflows/tests.yml/badge.svg)](https://github.com/ahmed-alnassif/AndroSH/actions/workflows/tests.yml)
[![GitHub Stars](https://img.shields.io/github/stars/ahmed-alnassif/AndroSH)](https://github.com/ahmed-alnassif/AndroSH/stargazers)
[![Python](https://img.shields.io/badge/python-3.8+-green)](https://python.org)
[![License](https://img.shields.io/badge/license-GPLv3-orange)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android-success)](https://www.android.com)

![AndroSH Mobile Showcase](https://assets.kitploit.com/production/public/readmes/9438/a4edb8815ebca0fde7738d96503897a680bcd0aaf4c21f1b329f30c3a56b6ec3.png)

## Table of Contents

* [Quick Start](#quick-start)
* [Features](#features)
* [Supported Distributions](#supported-distributions)
* [Overview](#overview)
* [Screenshots](#screenshots)
* [Architecture](#architecture)
* [Installation](#installation)
* [Updating](#updating)
* [Usage](#usage)
* [Use Cases](#use-cases)
* [Security & Privacy](#security--privacy)
* [Components & Sources](#components--sources)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)
* [Support](#support)

## Quick Start

> [!Important]
> **Before you start:** install and run [Shizuku](https://github.com/RikkaApps/Shizuku/releases/latest) first. If you're new to AndroSH, read the full [Installation](#installation) section below - it covers Shizuku setup and troubleshooting.

root@kitploit:~

```
# In Termux
apt update && apt install -y python git
git clone --depth 1 https://github.com/ahmed-alnassif/AndroSH.git
cd AndroSH
pip install -r requirements.txt
python main.py install

androsh setup demo --distro debian --type stable
androsh launch demo
```

## Features

* **Multi-distro**: run several Linux distributions side by side (Arch, Fedora, Alpine, Debian, Ubuntu, Kali, Void, Manjaro, Chimera, openSUSE)
* **ADB/Shizuku-powered Linux**: run full Linux distributions through Android's elevated Shell layer, with direct Android system integration - no root required
* **SQLite-backed**: fast, reliable tracking of your environments
* **Isolated**: each Linux environment runs through PRoot with userspace filesystem/process isolation
* **GUI support**: works with Termux:X11 for a full desktop environment - [setup guide](https://github.com/ahmed-alnassif/AndroSH/discussions/6#discussioncomment-15720947)

## Supported Distributions

![Debian](https://img.shields.io/badge/Debian-Supported-A81D33?logo=debian&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Supported-E95420?logo=ubuntu&logoColor=white)
![Arch Linux](https://img.shields.io/badge/Arch-Supported-1793D1?logo=archlinux&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali-Supported-557C94?logo=kalilinux&logoColor=white)
![Alpine](https://img.shields.io/badge/Alpine-Supported-0D597F?logo=alpinelinux&logoColor=white)
![Fedora](https://img.shields.io/badge/Fedora-Supported-51A2DA?logo=fedora&logoColor=white)
![Void Linux](https://img.shields.io/badge/Void-Supported-478061?logo=voidlinux&logoColor=white)
![Manjaro](https://img.shields.io/badge/Manjaro-Supported-35BF5C?logo=manjaro&logoColor=white)
![Chimera Linux](https://img.shields.io/badge/Chimera-Supported-000000?logo=linux&logoColor=white)
![OpenSUSE](https://img.shields.io/badge/OpenSUSE-Supported-35BF5C?logo=opensuse&logoColor=white)

Every distribution above ships from a verified rootfs source and runs in an isolated proot environment - no root required.

## Overview

AndroSH lets you deploy and manage multiple full Linux distributions on Android by running PRoot through the ADB/Shizuku execution layer. This provides elevated Android-side execution without root while retaining direct Android system integration from inside the Linux environments.

| Capability | AndroSH | Typical Alternatives |
| --- | --- | --- |
| Multiple distros at once | Yes | Usually one distro only |
| Environment management | SQLite + CLI | Manual file handling |
| Android system integration | ADB/Shizuku execution | Varies by solution |
| Multiple isolated instances | Yes | Single instance |
| Root required | No (ADB/Shizuku) | Often requires bootloader unlock |

## Screenshots

| Command | Preview | What it shows |
| --- | --- | --- |
| `androsh launch kali` | [View](https://github.com/ahmed-alnassif/androsh/blob/HEAD/Assets/Screenshots/launch-kali.png) | Launching the Kali NetHunter environment |
| `androsh list` | [View](https://github.com/ahmed-alnassif/androsh/blob/HEAD/Assets/Screenshots/list-available.png) | All available distributions |
| `androsh lsd` | [View](https://github.com/ahmed-alnassif/androsh/blob/HEAD/Assets/Screenshots/list-installed.png) | Environments you've already installed |

## Architecture

root@kitploit:~

```
Android Device → ADB/Shizuku Execution Context→ Proot Virtualization → Linux Environment(s)
```

root@kitploit:~

```
graph TD
    A[Android Device] --> B[ADB / Shizuku]
    B --> C[Android Shell Execution Context]
    C --> D[PRoot]

    D --> E[Alpine]
    D --> F[Debian]
    D --> G[Ubuntu]
    D --> H[Kali NetHunter]

    E --> I[Android System Integration]
    F --> I
    G --> I
    H --> I

    I --> K[Android Command Execution]
    I --> L[Android Filesystem Access]
    I --> M[Android Network Access]

    style D fill:#FF6B00,color:white
    style I fill:#4CAF50,color:white
```

From inside any distro, you can reach into the Android system directly:

root@kitploit:~

```
# List installed Android packages
pm list packages -f

# Kernel info
cat /proc/version

# Android system properties
getprop | grep version

# Network routes
ip route show
```

## Installation

### Requirements

* Android device with [Shizuku](https://github.com/RikkaApps/Shizuku/releases/latest) installed and running
* Python 3.8+
* [Termux](https://github.com/termux/termux-app/releases/latest) or a compatible terminal emulator
* At least 2 GB free storage

### Setup

root@kitploit:~

```
# Install prerequisites in Termux
apt update && apt install -y python git

# Get AndroSH
git clone --depth 1 https://github.com/ahmed-alnassif/AndroSH.git
cd AndroSH

# Install dependencies
pip install -r requirements.txt

# Make the `androsh` command available globally
python main.py install
```

> [!Tip]
> when you run `androsh setup`, AndroSH automatically checks whether Shizuku is configured correctly and walks you through fixing it if not.

## Updating

root@kitploit:~

```
cd AndroSH
git pull
pip install -r requirements.txt
```

## Usage

### Deploy an environment

root@kitploit:~

```
androsh setup production --distro debian --type stable
```

### Launch it

root@kitploit:~

```
androsh launch production
# You're now root inside the Debian environment
root@localhost:~# apt update && apt install python3 git
```

### Manage environments

root@kitploit:~

```
androsh list                       # See what's available to install
androsh lsd                        # See what's already installed
androsh clean production           # Free up space / ...