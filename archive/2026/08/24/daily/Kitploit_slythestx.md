---
title: slythestx
url: https://kitploit.com/en/tools/github/stuxctf/slythestx
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:58:52.146570
---

# slythestx

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

slythestx — Mobile app security auditing tool focused on automating SAST analysis, identifying underlying technologies (React Native, Flutter, Xamarin, native), and enabling deeper testing on rooted or jailbroken devices. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/stuxctf/slythestx

![](https://assets.kitploit.com/production/public/tools/51059/bdc7f6cd3e2bf3834f23c44d55a89d4379b580aa98fce4c23f3d32052b06dacc-display-v1.webp)

[Android Security](/en/categories/android-security)[Static Analysis](/en/categories/static-analysis)[Dynamic Analysis (Sandboxing)](/en/categories/dynamic-analysis-sandboxing)[iOS Security](/en/categories/ios-security)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Mobile App Pentesting](/en/categories/mobile-app-pentesting)[Penetration Testing](/en/categories/penetration-testing)[Mobile Security](/en/categories/mobile-security)[Secret Detection](/en/categories/secret-detection)

![GitHub](/providers/github.png)stuxctf/slythestx

# slythestx

Mobile app security auditing tool focused on automating SAST analysis, identifying underlying technologies (React Native, Flutter, Xamarin, native), and enabling deeper testing on rooted or jailbroken devices.

1221 month ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[View Repository](https://github.com/stuxctf/slythestx)

# 🐍 Slythestx

![Slythestx Logo](https://assets.kitploit.com/production/public/readmes/51059/bdc7f6cd3e2bf3834f23c44d55a89d4379b580aa98fce4c23f3d32052b06dacc/2f9d5fe0af433c070ba64bfcef68c0ebc88bfb95ebc836511a5273b7c33d964b-display-v1.webp)

**The Swiss Army Worm for Mobile Security**
*A unified framework for static code analysis and dynamic vulnerability hunting on iOS and Android.*

![Version](https://img.shields.io/badge/Slythestx-v1.0.2-brightgreen?style=for-the-badge&logo=kali-linux&logoColor=white)
![Security](https://img.shields.io/badge/Security-SAST%20%7C%20DAST-red?style=for-the-badge&logo=target)

[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Node](https://img.shields.io/badge/Node.js-v18+-339933?style=flat-square&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Vite](https://img.shields.io/badge/Vite-Built-646CFF?style=flat-square&logo=vite&logoColor=white)](https://vitejs.dev/)
![Platform](https://img.shields.io/badge/Platform-Multi--OS-lightgrey?style=flat-square&logo=linux)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
![For Educational Purposes Only](https://img.shields.io/badge/%E2%9A%A0%20For-Educational%20Purposes%20Only-red)

[![Buy Me A Coffee](https://assets.kitploit.com/production/public/readmes/51059/485b634752d0d832ed936de61544bf16e5e54dc05146ccca080333c15097d455/c96b3a6c5473495f05da584b68850d08d48233ccdcc51c729a2c15606f0d034c-display-v1.webp)](https://www.buymeacoffee.com/stux)

---

## 📖 Table of Contents

* [Overview](#-overview)
* [Key Features](#-key-features)
* [Architecture](#-architecture)
* [Analyzer Suite](#-analyzer-suite)
* [Quick Start](#-quick-start)
* [Usage](#-usage)
* [Release Notes](#-release--versioning)
* [Roadmap](#-roadmap)
* [Contributing](#-contributing)
* [Disclaimer](#%EF%B8%8F-disclaimer)
* [License](#-license)

---

## ⚡ Overview

**Slythestx** is a mobile-focused security toolkit that brings static analysis (SAST) and dynamic analysis (DAST) together under a single interface. It is built for security researchers and mobile pentesters who need to quickly fingerprint a target's technology stack, audit its source for known-bad patterns, and interact with a live device — all without juggling a dozen separate tools.

The engine ships as a containerized web application, exposing a browser-based dashboard (`http://localhost:3000`) backed by a Node.js/TypeScript analysis core.

---

## ✨ Key Features

---

## 🏗️ Architecture

Slythestx is organized around two core pillars: **analyzers** (static, tech-stack aware inspection modules) and **device drivers** (dynamic interaction with connected iOS/Android hardware).

---

## 🧩 Analyzer Suite

Each analyzer plugs into the core engine and runs when its corresponding technology is detected, keeping scans fast and noise-free.

---

## 🚀 Quick Start

### Prerequisites

* [Docker](https://www.docker.com/) & Docker Compose
* Node.js v18+
* Python 3.10+
* (iOS analysis) A jailbroken iOS device with SSH enabled, or USB connectivity via `libimobiledevice`
* (Android analysis) ADB enabled on the target device

### Installation

root@kitploit:~

```
# Clone the repository
git clone https://github.com/stuxctf/slythestx/
cd slythestx

# --- Windows ---
docker-compose.exe -f docker-compose.yml -f docker-compose.windows.yml build

# --- Linux ---
docker-compose -f docker-compose.yml -f docker-compose.linux.yml build

# Launch the engine
docker-compose up -d
```

### Access the Dashboard

Once the containers are running, open your browser at:

root@kitploit:~

```
http://localhost:3000
```

---

## 🖥️ Usage

1. **Connect a device** — plug in an Android device with USB/WiFi debugging enabled, or an iOS device (USB or SSH for jailbroken devices).
2. **Enumerate apps** — Slythestx lists installed applications with bundle/package ID, name, and version.
3. **Extract & analyze** — pull the APK/IPA, or explore the app's sandbox directly, and let the technology detector route the package to the right analyzers.
4. **Review findings** — inspect detected security measures, flagged secrets, permission issues, and SAST rule matches from the dashboard.
5. **Go dynamic** — tail live device logs, browse the app's data container, or invoke suggested external tools for deeper manual testing.

---

## 📌 Release & Versioning

### 🟢 v1.0.2\_PUBLIC\_ALPHA — *Darkapple*

* **iOS Integration** — USB & SSH support for jailbroken devices, automatic device detection, communication via `libimobiledevice`
* **Application Enumeration** — bundle ID/name/version detection, fast filesystem-based enumeration, USB fallback via `ideviceinstaller`
* **App Container Discovery** — bundle/data container mapping, automatic sandbox path resolution, directory listing (Documents, Library, Preferences, Caches)
* **IPA Extraction** — direct on-device extraction, automatic `Payload` structure creation, fast SFTP download, IPA management endpoints (list/delete/clear)
* **Rootful / Rootless Support** — automatic `PlistBuddy` path detection, compatible with modern jailbreak environments
* **Performance Improvements** — faster SSH enumeration, fewer device calls, optimized plist parsing
* Bug fixes and stability improvements

> 🔜 **In Progress:** Keychain dumping, Cycript integration, and additional security tooling; SSH-based syslog streaming.

### 🟢 v1.0.1 — *ShadowLog*

* **Advanced Logcat Integration** — real-time system log monitoring with custom filt...