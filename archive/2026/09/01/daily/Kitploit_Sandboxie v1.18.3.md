---
title: Sandboxie v1.18.3
url: https://kitploit.com/en/posts/github-sandboxie-plus-sandboxie-v1183
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:11.150543
---

# Sandboxie v1.18.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/46180/3dc1129e356b02108cb12aa581dda3547096231c8a93299ae78b3318b2639d55.png)

New releaseSep 1, 2026

# Sandboxie v1.18.3

Windows sandbox-based isolation tool for running untrusted programs and web browsing in a secure virtual environment without permanent system changes.

Share

# Sandboxie Plus / Classic

EN | [中文](./README_zh_CN.md)

[![Plus license](https://img.shields.io/badge/Plus%20license-Custom%20-blue.svg)](./LICENSE.Plus) [![Classic license](https://img.shields.io/github/license/Sandboxie-Plus/Sandboxie?label=Classic%20license&color=blue)](./LICENSE.Classic) [![GitHub Release](https://img.shields.io/github/release/sandboxie-plus/Sandboxie.svg)](https://github.com/sandboxie-plus/Sandboxie/releases/latest) [![GitHub Pre-Release](https://img.shields.io/github/release/sandboxie-plus/Sandboxie/all.svg?label=pre-release)](https://github.com/sandboxie-plus/Sandboxie/releases) [![GitHub Build Status](https://github.com/sandboxie-plus/Sandboxie/actions/workflows/main.yml/badge.svg)](https://github.com/sandboxie-plus/Sandboxie/actions) [![GitHub Codespell Status](https://github.com/sandboxie-plus/Sandboxie/actions/workflows/codespell.yml/badge.svg)](https://github.com/sandboxie-plus/Sandboxie/actions/workflows/codespell.yml) [![WinGet Build Status](https://github.com/sandboxie-plus/Sandboxie/actions/workflows/winget.yml/badge.svg)](https://github.com/sandboxie-plus/Sandboxie/actions/workflows/winget.yml) [![Gurubase](https://img.shields.io/badge/Gurubase-Ask%20Sandboxie%20Guru-006BFF)](https://gurubase.io/g/sandboxie)

[![Roadmap](https://img.shields.io/badge/Roadmap-Link%20-blue?style=for-the-badge)](https://www.wilderssecurity.com/threads/updated-sandboxie-plus-roadmap.456886/) [![Join our Discord Server](https://img.shields.io/badge/Join-Our%20Discord%20Server%20for%20bugs,%20feedback%20and%20more!-blue?style=for-the-badge&logo=discord)](https://discord.gg/S4tFu6Enne)

| System requirements | Release notes | Contribution guidelines | Security policy | Code of Conduct |
| --- | --- | --- | --- | --- |
| Windows 7 or higher (64-bit) | [CHANGELOG.md](https://github.com/sandboxie-plus/sandboxie/blob/HEAD/CHANGELOG.md) | [CONTRIBUTING.md](https://github.com/sandboxie-plus/sandboxie/blob/HEAD/CONTRIBUTING.md) | [SECURITY.md](https://github.com/sandboxie-plus/sandboxie/blob/HEAD/SECURITY.md) | [CODE\_OF\_CONDUCT.md](https://github.com/sandboxie-plus/sandboxie/blob/HEAD/CODE_OF_CONDUCT.md) |

Sandboxie is a sandbox-based isolation software for Windows NT-based operating systems that creates a secure operating environment in which applications can be run or installed without permanently modifying local & mapped drives or the Windows registry. An isolated virtual environment allows controlled testing of untrusted programs and web surfing.

Sandboxie allows you to create virtually unlimited sandboxes and run them alone or simultaneously to isolate programs from the host and each other, while also allowing you to run as many programs simultaneously in a single box as you wish.

**Note: This is a community fork that took place after the release of the Sandboxie source code and not the official continuation of the previous development (see the [project history](#project-history) and [#2926](https://github.com/sandboxie-plus/Sandboxie/issues/2926)).**

## ⏬ Download

[Latest Release](https://github.com/sandboxie-plus/Sandboxie/releases/latest)

## ✨ Changelog

[EN](./CHANGELOG.md)

## 🚀 Features

Sandboxie is available in two editions, Plus and Classic. They both share the same core components, this means they have the same level of security and compatibility.
What's different is the availability of features in the user interface.

Sandboxie Plus has a modern Qt-based UI, which supports all new features that have been added since the project went open source:

* Snapshot Manager - takes a copy of any box in order to be restored when needed
* Maintenance menu - allows to uninstall/install/start/stop Sandboxie driver and service when needed
* Portable mode - you can run the installer and choose to extract all files to a directory
* Additional UI options to block access to Windows components like printer spooler and clipboard
* More customization options for Start/Run and Internet access restrictions
* Privacy mode sandboxes that protect user data from illegitimate access
* Security enhanced sandboxes that restrict the availability of syscalls and endpoints
* Global hotkeys to suspend or terminate all boxed processes
* A network firewall per sandbox which supports Windows Filtering Platform (WFP)
* The list of sandboxes can be searched with the shortcut key Ctrl+F
* A search function for Global Settings and Sandbox Options
* Ability to import/export sandboxes to and from 7z files
* Integration of sandboxes into the Windows Start menu
* A browser compatibility wizard to create templates for unsupported browsers
* Vintage View mode to reproduce the graphical appearance of Sandboxie Control
* A troubleshooting wizard to assist users with their problems
* An Add-on manager to extend or add functionality via additional components
* Protections of sandboxes against the host, including the prevention of taking screenshots
* A trigger system to perform actions, when a sandbox goes through different stages, like initialization, box start, termination or file recovery
* Make a process not sandboxed, but its child processes sandboxed
* Force programs to automatically use a user-provided SOCKS5 proxy
* DNS control by blocking or redirecting
* Limit the amount of memory space a single process in the sandbox can occupy and the total amount of memory space all processes can occupy, and You can limit the total number of sandboxed processes per box
* A completely different token creation mechanism from Sandboxie's pre-open-source version makes sandboxes more independent in the system
* Encrypted Sandbox - an AES-based reliable data storage solution
* Prevent sandboxed programs from generating unnecessary unique identifier in the normal way
* An internal INI editor that aids the user with visual hints and tooltips on the settings they have configured or want to add
* The ability to configure an external text editor, beside the system default
* Control over the alpha transparency of the border
* A custom UAC-dialog, allowing to fake permission, grant them or cancel the elevation attempt
* Modern icons, while you can use the old-school ones in certain places
* You can change the font of the user interface
* Custom colors or icons can be used for sandboxes or groups

More features can be spotted by finding the sign `=` through the shortcut key Ctrl+F in the [CHANGELOG.md](https://github.com/sandboxie-plus/sandboxie/blob/HEAD/CHANGELOG.md) file.

Sandboxie Classic has the old no longer developed MFC-based UI, hence it lacks native interface support for Plus features. Although some of the missing features can be configured manually in the Sandboxie.ini configuration file or even replaced with [custom scripts](https://sandboxie-website-archive.github.io/www.sandboxie.com/old-forums/viewforum1a2d1a2d.html?f=22), the Classic edition is not recommended for users who want to explore the latest security options.

## 📚 Documentation

A GitHub copy of the [Sandboxie documentation](https://sandboxie-plus.github.io/sandboxie-docs) is currently maintained, although more volunteers are needed to keep it updated with the new changes. It is recommended to also check the following labels to track current issues: [Labels · sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie/labels).

A pa...