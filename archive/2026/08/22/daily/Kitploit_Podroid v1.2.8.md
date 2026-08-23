---
title: Podroid v1.2.8
url: https://kitploit.com/en/posts/github-extv-podroid-v128
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:01.197600
---

# Podroid v1.2.8

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13125/fb2e1534d4ee15dc48a33288f9b501a369e44cfb38564207582b753e771c0e7c.png)

New releaseAug 22, 2026

# Podroid v1.2.8

A rootless Android app that boots Alpine Linux: run containers (Podman/Docker/LXC) and GUI desktop apps.

Share

![Podroid logo](https://assets.kitploit.com/production/public/readmes/13125/7c1a419247d3f24b7f52a87ef217ef628af16f682be57f600251cbaa1db25a78.png)

# Podroid

**Run Linux containers and a full Linux desktop on your Android phone. No root.**

A real Alpine Linux VM with its own kernel - not a chroot or proot trick - so **Podman, Docker and LXC** behave exactly like they do on a server.

[![Release](https://img.shields.io/github/v/release/ExTV/Podroid?include_prereleases&style=flat-square&label=release&color=blue)](https://github.com/ExTV/Podroid/releases)
[![Downloads](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)](https://github.com/ExTV/Podroid/releases)
[![Stars](https://img.shields.io/github/stars/ExTV/Podroid?style=flat-square&color=yellow)](https://github.com/ExTV/Podroid/stargazers)
[![License](https://img.shields.io/github/license/ExTV/Podroid?style=flat-square)](LICENSE)
![Android 8+](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)
![arm64](https://img.shields.io/badge/arch-arm64-orange?style=flat-square)

[**Website**](https://extv.github.io/Podroid/) · [**Documentation**](https://extv.github.io/Podroid/guide/) · [**Download APK**](https://github.com/ExTV/Podroid/releases/latest)

|  |  |  |  |
| --- | --- | --- | --- |
| ![Home screen before the VM starts](https://assets.kitploit.com/production/public/readmes/13125/fb2e1534d4ee15dc48a33288f9b501a369e44cfb38564207582b753e771c0e7c.png) **Home** | ![Home screen with the VM running and network info](https://assets.kitploit.com/production/public/readmes/13125/ad1634b585fbf91afac03c03f035598e65172e9c3e925a3643d93c7ec45cc739.png) **Running** | ![Built-in terminal showing Alpine system info](https://assets.kitploit.com/production/public/readmes/13125/0396fe2a9bdc0fde5de60fd9d08538c4751843d443a36ce7be25a577b3a26bf5.png) **Terminal** | ![Terminal Quick Settings with themes and fonts](https://assets.kitploit.com/production/public/readmes/13125/d4d46114c43e6a5d507bffc5c52135adfc02f4d9eb18ec1687f90edb98897442.png) **Themes & fonts** |

## What you get

* **Podman, Docker and LXC** - pre-installed, ready the moment it boots
* **A real VM** - Alpine Linux on a custom kernel via QEMU, or hardware-accelerated AVF on supported pKVM devices
* **In-app terminal** - full xterm-256color, 122 color themes, 13 fonts, live resize
* **X11 desktop** - run GUI Linux apps in a built-in viewer with touch, keyboard, mouse and audio
* **USB passthrough**, **SSH**, **port forwarding** and a **guest-to-Android bridge**
* **Container backup**, a **live VM/device status view** and **Downloads-folder sharing** with the guest
* **English and 中文**, no root, any arm64 device on Android 8+

## Quick start

1. [Download the APK](https://github.com/ExTV/Podroid/releases/latest) and install it.
2. Tap **Start VM**, wait for **Ready!**, open the terminal.

root@kitploit:~

```
# rootless containers, straight away
podman run --rm alpine echo "hello from a container"
docker run -d -p 8080:80 nginx

# expose that container to your phone and LAN, right from the VM shell
podroid-forward add 8080 8080 tcp     # TCP or UDP, on both the QEMU and AVF backends
curl http://<phone-ip>:8080
podroid-forward clean                 # remove every rule you added, in one go

# SSH in from your laptop (enable SSH in the setup wizard or Settings)
ssh root@<phone-ip> -p 9922        # password: podroid
```

Setup, the two backends, networking, the X11 viewer and troubleshooting all live in the **[documentation](https://extv.github.io/Podroid/guide/)**.

## Build

root@kitploit:~

```
git clone https://github.com/ExTV/Podroid.git
cd Podroid
./build-all.sh all     # kernel, rootfs, QEMU and APK (needs Docker + Android SDK/NDK)
```

Per-component builds and toolchain details: [CONTRIBUTING.md](https://github.com/extv/podroid/blob/HEAD/CONTRIBUTING.md).

## Contributing

Contributions of every size are welcome: bug reports, kernel-config tweaks, new themes, UI polish, X11 input fixes, anything.

* **Pull requests:** read [CONTRIBUTING.md](https://github.com/extv/podroid/blob/HEAD/CONTRIBUTING.md) first. Keep changes scoped, run `./build-all.sh test` before pushing, and explain *why* in the PR description.
* **Bug reports:** [open an issue](https://github.com/ExTV/Podroid/issues/new) with your device and Android version, a short repro, and the diagnostic log (**Settings → Export Diagnostic Log** in the app).

## Credits

|  |  |
| --- | --- |
| [QEMU](https://www.qemu.org) | Machine emulation |
| [Termux](https://github.com/termux/termux-app) | Terminal emulator engine |
| [Alpine Linux](https://alpinelinux.org) | The guest distribution |

Full list in [CREDITS.md](https://github.com/extv/podroid/blob/HEAD/CREDITS.md).

## License

[GPLv2](https://github.com/extv/podroid/blob/HEAD/LICENSE). If Podroid is useful to you, a [star](https://github.com/ExTV/Podroid/stargazers) helps other people find it.

[Read more](/en/tools/github/extv/podroid?expand=1)

## Categories

[Android Security](/en/categories/android-security)[Container Security](/en/categories/container-security)[Security Virtualization](/en/categories/security-virtualization)[Mobile Security](/en/categories/mobile-security)[Utilities & Frameworks](/en/categories/utilities-frameworks)[Hardware & IoT Security](/en/categories/hardware-iot-security)

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