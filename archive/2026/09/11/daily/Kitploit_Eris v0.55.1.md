---
title: Eris v0.55.1
url: https://kitploit.com/en/posts/github-sibexico-eris-v0551
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:18.227360
---

# Eris v0.55.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13047/abd7fbe20d16348c03dfe1c10a152d10b50f1e6b42353c0b48527c2bbf4f7fe3.png)

New releaseSep 11, 2026

# Eris v0.55.1

Desktop PGP workstation

Share

![Windows](https://img.shields.io/badge/Windows-Supported-blue?labelColor=gray&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTAgMGgxMXYxMUgwek0xMyAwaDExdjExSDEzek0wIDEzaDExdjExSDB6TTEzIDEzaDExdjExSDEzeiIvPjwvc3ZnPg==)
![Linux](https://img.shields.io/badge/Linux-Supported-yellow?labelColor=gray&logo=linux)

![Go Version](https://img.shields.io/badge/Go-1.26.1-blue?labelColor=gray&logo=go)
[![Support Me](https://img.shields.io/badge/Support-Me-darkgreen?labelColor=black&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI0ZGRiIgZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMiAxQzUuOTI1IDEgMSA1LjkyNSAxIDEyczQuOTI1IDExIDExIDExIDExLTQuOTI1IDExLTExUzE4LjA3NSAxIDEyIDF6bTAgNGwyLjUgNi41SDIxbC01LjUgNCAyIDYuNUwxMiAxNy41IDYgMjJsMi02LjUtNS41LTRoNi41TDEyIDV6Ii8+PC9zdmc+)](https://sibexi.co/support)

[![Tests passed](https://img.shields.io/badge/Tests-Failed-red?labelColor=gray&logo=github)](https://github.com/sibexico/Eris/actions/runs/34416454373)
[![Tests coverage](https://img.shields.io/badge/Tests%20Coverage-67.4%25-yellow?labelColor=gray&logo=gitextensions)](https://github.com/sibexico/Eris/actions/runs/34416454373)

# Eris

![Eris](https://assets.kitploit.com/production/public/readmes/13047/91550ca1b7d165862478fd5497662adce61fee498fd1ed9eaa65052b8e44deb8.png)

Eris is a desktop PGP workstation written in Go with Fyne.
It stores keys in an encrypted vault and gives you a clean UI for signing, encryption, decryption, and verification.

## Features

* Encrypted local vault for stored keys
* Generate your own key pairs
* Import and manage contact public keys
* Encrypt and sign messages
* Decrypt and verify incoming messages
* Dedicated sign-only and verify-only modes
* Settings tab for switching vaults and changing vault passphrase

## Install

### Windows (Winget)

Install from WinGet with:

root@kitploit:~

```
winget install sibexico.Eris
```

If you already have Eris installed and want the latest published release:

root@kitploit:~

```
winget upgrade sibexico.Eris
```

### Debian/Ubuntu (.deb from Release)

1. Open the latest Release page and download the `.deb` file from Assets.
2. Install it with:

root@kitploit:~

```
sudo apt install ./eris_<version>_linux_<arch>.deb
```

Example:

root@kitploit:~

```
sudo apt install ./eris_1.2.3_linux_x86_64.deb
```

If your distribution prefers `dpkg` first:

root@kitploit:~

```
sudo dpkg -i eris_<version>_linux_<arch>.deb
sudo apt -f install
```

## Build

Build from source if you want a local binary:

Windows:

root@kitploit:~

```
go build -ldflags "-H=windowsgui" -o eris.exe .
```

Linux:

root@kitploit:~

```
go build -o eris .
```

## Run

* Windows: `./eris.exe`
* Linux: `./eris`

## Screenshots

![Eris](https://assets.kitploit.com/production/public/readmes/13047/abd7fbe20d16348c03dfe1c10a152d10b50f1e6b42353c0b48527c2bbf4f7fe3.png)

![Eris](https://assets.kitploit.com/production/public/readmes/13047/e30e5c783631ae5cb772e93b4030720200e1baf5802ca9f1339727d6c8199114.png)

[Read more](/en/tools/github/sibexico/eris?expand=1)

## Categories

[General Purpose Utilities](/en/categories/general-purpose-utilities)[Encryption/Decryption Tools](/en/categories/encryption-decryption-tools)[Cryptography](/en/categories/cryptography)[Privacy](/en/categories/privacy)[Authentication](/en/categories/authentication)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories