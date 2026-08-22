---
title: iDescriptor v0.6.2
url: https://kitploit.com/en/posts/github-idescriptor-idescriptor-v062
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:03.364813
---

# iDescriptor v0.6.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9718/1faa48a795a2a346894262030a7459fe3df066c95d490f5636dcdac4c539fef0.png)

New releaseAug 21, 2026

# iDescriptor v0.6.2

A free, open-source, and cross-platform iDevice management tool

Share

![](https://assets.kitploit.com/production/public/readmes/9718/ab2930aca5c4efbb3b5e3fda2b915b6b37721fd2d55df2520f6734719550dc82/800914f888e2174e78307cf471c7182da08569765bb4f82435c670bfe208bb1d-display-v1.webp)

Cross-platform, open-source and free idevice management tool written in Rust ![](https://rustacean.net/assets/rustacean-orig-noshadow.svg) and Qt

[![GitHub](https://img.shields.io/github/license/iDescriptor/iDescriptor)](https://github.com/iDescriptor/iDescriptor/blob/main/LICENSE)
[![CodeFactor](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/iDescriptor/iDescriptor/issues)
[![Build](https://img.shields.io/github/actions/workflow/status/iDescriptor/iDescriptor/build-linux.yml?branch=main&logo=Github)](https://github.com/iDescriptor/iDescriptor/actions/workflows/build.yml)
[![Crowdin](https://badges.crowdin.net/idescriptor/localized.svg)](https://crowdin.com/project/idescriptor)
[![GitHub tag (latest SemVer pre-release)](https://img.shields.io/github/v/tag/iDescriptor/iDescriptor?include_prereleases&label=version)](https://github.com/iDescriptor/iDescriptor/tags)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)
![](https://shields.io/badge/-Rust-3776AB?style=flat&logo=rust)
![Language](https://img.shields.io/badge/C++-20-hotpink.svg)
![Qt](https://img.shields.io/badge/Qt-6-brightgreen.svg)
[![AppImage](https://img.shields.io/badge/AppImage-available-brightgreen)](https://github.com/iDescriptor/iDescriptor/releases)
[![AppImage](https://img.shields.io/badge/Arch_AUR-available-brightgreen)](https://aur.archlinux.org/packages/idescriptor-git)

[![AppImage](https://img.shields.io/badge/OpenCollective-1F87FF?style=for-the-badge&logo=OpenCollective&logoColor=white)](https://opencollective.com/idescriptor)

Sponsored by

[![](https://raw.githubusercontent.com/idescriptor/idescriptor/HEAD/resources/repo/cape.svg)](https://www.cape.co/)

first-of-its kind private and secure consumer cellular service in the US

## Download

### DO NOT DOWNLOAD FROM ANY WEBSITE CLAIMING TO BE US WE ONLY HAVE <https://idescriptor.github.io> AND RELEASES WILL BE MADE FROM THIS REPO ONLY

[![Get it on Flathub](https://flathub.org/api/badge?svg&locale=en)](https://flathub.org/apps/io.github.idescriptor.iDescriptor)
[![Install from AUR](https://img.shields.io/badge/Arch_AUR-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)](https://aur.archlinux.org/packages/idescriptor-git)
[![NixOS Package](https://img.shields.io/badge/NixOS-5277C3?logo=nixos&logoColor=fff)](https://search.nixos.org/packages?channel=unstable&query=idescriptor#show=idescriptor)
[![pi-apps-badge](https://raw.githubusercontent.com/Botspot/pi-apps/master/icons/badge.png?raw=true)](https://github.com/Botspot/pi-apps)

[![Download for Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/iDescriptor/iDescriptor/releases/latest)
[![Download for macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/iDescriptor/iDescriptor/releases/latest)
[![Download for Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/iDescriptor/iDescriptor/releases/latest)

### Installation Instructions

#### Windows

* **Installer (.msi)**: Download and run the installer. Recommended for most users.
* **Portable (.zip)**: Extract and run `iDescriptor.exe`. No installation required.
* **Choco** :

root@kitploit:~

```
 choco install idescriptor --version=0.1.0
```

#### macOS

* **Apple Silicon**: Download the `.dmg` file for M1/M2/M3/MX Macs.

  Open the `.dmg` and drag iDescriptor to Applications.

After moving the app to Applications, run the code below

root@kitploit:~

```
xattr -c ~/Applications/iDescriptor.app
```

[Click here to learn more about why this is needed](#damaged-error-on-macos).

* **Intel**: Download the `.dmg` file for Intel-based Macs.

  Open the `.dmg` and drag iDescriptor to Applications.

  You shouldn't run into any issues on Intel Macs but if you do, [check this out](#damaged-error-on-macos).

#### Linux

* **AppImage**: Download, and then run

root@kitploit:~

```
  chmod +x iDescriptor*.AppImage
```

* **Arch Linux**: Install from AUR:

root@kitploit:~

```
  yay -S idescriptor-git
```

---

# Windows 11 (Acrylic) - v0.6.0

![](https://assets.kitploit.com/production/public/readmes/9718/072b5d6c14a519f6fa67b584306dfad87c2688a842f8e0f6fef76996bf7ecf69/722cac408df115de043df5a483e991b912ec96a7a438f9da924df7fa08b398e2-display-v1.webp)

# Windows 11 - v0.6.0

![](https://assets.kitploit.com/production/public/readmes/9718/a08d62e7074ea9e16764e3996ad4a104bf2297fd4c1d41b5b9805755a3e3916b/f082e73480afd0adda793af9059ff5bee02ddf4b6889f5f1ce8c7e96d35e6815-display-v1.webp)

# macOS - v0.6.0

![](https://assets.kitploit.com/production/public/readmes/9718/f4d5cfbd23e8b04bb4d23cdca51b33756968483bc7f913b04fba2c58788e3f63/fbfec1aea9ba707f273b1975b788312369e1a7992c596fc64b65c67d6a31e9c8-display-v1.webp)

# Linux (Gnome, Custom Window Enabled) - v0.6.0

![](https://assets.kitploit.com/production/public/readmes/9718/ff6cfac591d7d7e465784530f8ccb9ee89cd2b11b18588789d9ca0732b6424b3/d0b7b2019d5ffe99d61799fb33cf1de65eb5cc3145dda8ed8447adc25c16c828-display-v1.webp)

# Linux (Gnome) - v0.6.0

![](https://assets.kitploit.com/production/public/readmes/9718/71302cc635fa5ffcf9bd2f710fa92f3dc4ec59c7ae6ffcd1dcad58cf47bc4b6e/3739e2c57fa749793b99508fb46c436dcfcc399651d22ef82e1f02e2bef8418e-display-v1.webp)

# Linux (Ubuntu) - v0.6.0

![](https://assets.kitploit.com/production/public/readmes/9718/ebae9f5910382a667d981b7bd90bd6681cdcfd6b80e78f93887de62c52f9059d/d46849dabb8144807242e921e4c5a070bf456461021d3e93f8173eef793885f6-display-v1.webp)

## Features

### Connection

| Feature | Status | Notes |
| --- | --- | --- |
| USB Connection | ✅ Implemented | Fully supported on Windows, macOS, and Linux. |
| Wireless Connection | ✅ Implemented | Starting from v0.4.0 |

### Tools

| Feature | Status | Notes |
| --- | --- | --- |
| [AirPlay](#airplay) | ✅ Implemented | Cast your device screen to your computer. |
| [Download & Install Apps From Apple Store](#app-store) | ✅ Implemented | Download and install apps directly from the Apple Store. |
| [Battery Information](#battery-information) | ✅ Implemented | Read detailed battery info from device. |
| [Virtual Location](#virtual-location) | ✅ Implemented | Simulate GPS location. |
| [Device Backups](#device-backups) | ✅ Implemented (Experimental) | Backup your data from device (iOS 13-26) |
| [iFuse Filesystem Mount](#ifuse-filesystem-mount) | ✅ Implemented | Mount the device's filesystem. (Windows & Linux only) |
| Gallery | ✅ Implemented | - |
| File Explorer | ✅ Implemented | Explore the device's filesystem. |
| Wireless Gallery Import | ✅ Implemented | Import photos wirelessly (requires the Shortcuts app on the iDevice). |
| [Cable Info](#cable-info) | ✅ Implemented | Check authenticity of connected USB cables and more. |
| [Network Device Discovery](#network-device-discovery) | ✅ Implemented | Discover and monitor devices on your local network. |
| [SSH Terminal](#ssh-terminal) **(Jailbroken)** | ✅ Implemented | Open up a terminal on your iDevice. |
| Query MobileGestalt | ✅ Implemented | Read detailed hardware and s...