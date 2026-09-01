---
title: wifit3 v0.0.5
url: https://kitploit.com/en/posts/github-derv82-wifit3-v005
source: Kitploit
date: 2026-08-31
fetch_date: 2026-09-01T06:59:45.582300
---

# wifit3 v0.0.5

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50012/2efdf06fe93e90c9b114d815ee6a0f847a42f4259fba335ee71e94a3c6c88fa6.gif)

New releaseAug 31, 2026

# wifit3 v0.0.5

Wifite but USB-only & cross-platform.

Share

# wifit3: USB Wireless Auditor

> A wireless auditor that runs on Linux and Windows, comes with its own built-in drivers.

> *At least* one of the [supported USB adapters](#supported-hardware) is **required**.

![Wifit3 splash / adapter picker](https://assets.kitploit.com/production/public/readmes/50012/04606166e4819097d373eac8e473da43c3c80449f1e3c4ed8b2652ada7a80d96.png)

![Wifit3 in action: WPS PushButton PSK capture](https://assets.kitploit.com/production/public/readmes/50012/2efdf06fe93e90c9b114d815ee6a0f847a42f4259fba335ee71e94a3c6c88fa6.gif)

wifit3 is fundamentally different from its predecessor, [wifite2](https://github.com/derv82/wifite2):

* Only supports certain popular USB cards (see [Supported Hardware](#supported-hardware)).
* Bundles its own driver stack (see [Mini-Drivers](#mini-drivers)), avoiding headaches with native wireless drivers (Windows NDIS, Linux driver conflicts).
* Talks to wireless cards directly from userland *after* setup.
  + `sudo` is required to set up permissions on Linux (udev/modprobe).
  + Admin is required to install [WinUSB drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/usbcon/introduction-to-winusb-for-developers) on Windows (automated).
  + After setup/install, wifit3 runs without privilege escalation.
* *Far* fewer dependencies: PyUSB/libusb (USB) and Textual/Rich (TUI).
  + No aircrack, airmon, reaver, bully, hcxdumptool, etc.

## Status: Beta *("Works On My Machine")*

[Thoroughly tested](https://github.com/derv82/wifit3/blob/HEAD/docs/SUPPORTED-HARDWARE.md) only on my own machine, with the cards I physically own.

Other wireless cards with a supported chipset may not behave as expected.

Bug reports are genuinely welcome: [open an issue](https://github.com/derv82/wifit3/issues).

## Features

* **Multi-card**: listen on every plugged-in and supported device, improves capturing; TX device selection.
* **Live scan**: lists Access Points (APs) with channel hopping, signal, encryption, WPS state, and WPA3/SAE detection.
* **VAP Decloaking**: identifies and tags hidden Virtual APs (VAPs) with its physical AP.
* **Live packet dashboard**: real-time traffic sparklines (beacons, data, injects, deauths) for the focused target.
* **PMKID**: passive capture and active harvest, saves as HashCat `.hc22000` filetype.
* **WPA/WPA2 handshakes**: passive 4-way capture and deauth-triggered capture, proper handshake validation, compact PCAP and `.hc22000` saves.
* **WPS PushButton Extraction**: detects when an AP's WPS button is pressed, automatically extracts PSK.
* **WPS PIN Brute-force**: resumable WPS PIN brute-force sessions.
* **WEP suite**: ARP replay, ChopChop, fake auth, PTW key recovery. For anyone trapped in 2006.
* **WiFFy**: helpful assistant that provides useful messages during the WinUSB installation process.

## Screenshots

| Scanner | Focus (single target) |
| --- | --- |
| ![Scanner](https://assets.kitploit.com/production/public/readmes/50012/24709c5d2e682635dbc1f238f6235658c265012351095aff0e197c74abb30b1b.png) | ![Focus](https://assets.kitploit.com/production/public/readmes/50012/cd1d31407229a1c28724255310dbc246dff51dc521e84fd2404c1594caaecc5d.png) |

## Supported hardware

*If your USB device is not listed there, wifit3 will not work with it.*

A matching chipset does not guarantee that your wireless card will work.

| Chipset | Bands | Cards (Make + Model) |
| --- | --- | --- |
| Atheros AR9271 | 2.4 GHz | ALFA AWUS036**NHA**, TP-Link TL-WN722N V1 |
| MediaTek MT7610U | 2.4 / 5 GHz | ALFA AWUS036**ACHM**, Panda PAU0B |
| MediaTek MT7612U | 2.4 / 5 GHz | ALFA AWUS036**ACM** |
| MediaTek MT7921AU | 2.4 / 5 GHz | ALFA AWUS036**AXML**, Panda PAU0F |
| MediaTek MT7925U | 2.4 / 5 GHz | Netgear A9000 |
| Realtek RTL8812AU | 2.4 / 5 GHz | ALFA AWUS036**ACH** |
| Realtek RTL8814AU | 2.4 / 5 GHz | ALFA AWUS1900 |
| Realtek RTL8821AU | 2.4 / 5 GHz | ALFA AWUS036**ACS**, TP-Link Archer T2U Plus/Nano |
| Realtek RTL8821CU | 2.4 / 5 GHz | Auscoumer 600 Mbps |
| Realtek RTL8922AU | 2.4 / 5 GHz | ASUS USB-BE93 |
| Realtek RTL8822BU | 2.4 / 5 GHz | TP-Link T3U Plus |
| Realtek RTL8187L | 2.4 GHz | ALFA AWUS036**H** |
| Realtek RTL8188EUS | 2.4 GHz | TP-Link TL-WN722N v2/v3 |
| Ralink RT2570 | 2.4 GHz | Buffalo Nintendo Wi-Fi USB Controller |
| Ralink RT3070 | 2.4 GHz | ALFA AWUS036**NH** |
| Ralink RT5370 | 2.4 GHz | LOTEKOO 150 Mbps |
| Ralink RT5372 | 2.4 GHz | Panda PAU05/PAU06 |
| Ralink RT5572 | 2.4 / 5 GHz | Panda PAU09 N600 |

See [Supported Hardware](https://github.com/derv82/wifit3/blob/HEAD/docs/SUPPORTED-HARDWARE.md) for detailed information about each card's capabilities and performance.

## Install

### Download (recommended)

Grab a prebuilt binary from the [**Releases**](https://github.com/derv82/wifit3/releases/latest)

* **Windows** — download `wifit3-windows-x64.exe` and run it.
* **Linux** — download `wifit3-linux-x64`, then `chmod +x wifit3-linux-x64 && ./wifit3-linux-x64`.
* **macOS (Apple Silicon + Intel):**
  1. Download `wifit3-macos-universal2`
  2. Bypass quarantine: `xattr -d com.apple.quarantine wifit3-macos-universal2 && chmod +x wifit3-macos-universal2`
  3. Run it: `./wifit3-macos-universal2`

### Run from source

Wifit3 uses [`uv`](https://docs.astral.sh/uv/) (requires internet access to pull dependencies for the first run):

root@kitploit:~

```
uv sync
uv run wifit3
```

### Build

Build using `uv run pyinstaller wifit3.spec --noconfirm --clean` (Windows: `dist/wifit3.exe`, Linux/OSX: `dist/wifit3`).

### First-run setup

**Windows**: Wifit3 offers to install the **WinUSB** driver for your device. The bundled installer
self-elevates for that one step (a single UAC prompt), after which no Administrator privileges are needed to run Wifit3.

**Linux**: Wifit3 offers to create udev and modprobe rules which enable userland access. These rules blocklist
the card's kernel driver (so the kernel stops grabbing it). Afterward Wifit3 runs without `sudo`.

**macOS**: No driver install is needed. macOS asks to allow the USB device on first plug-in: choose
*Allow*, afterwards wifit3 can see & interact with the device.

### Uninstall

Click the red `Uninstall` button on Wifit3's Splash screen to uninstall

* **Windows:** Uninstalls WinUSB driver, relinquishing control to Windows' installed driver.
* **Linux:** Deletes udev & modprobe rules, kernel assumes control of the driver after a replug.

## Thanks

Wifit3 only exists because of the people who reverse-engineered and maintained the Linux
drivers we ported from.

**Biggest thanks: Christian "kimo" B. ([@kimocoder](https://github.com/kimocoder))**, who
took over **wifite2** when its original maintainer (me) stepped away and has kept it alive and
evolving for years since (and maintains `aircrack-ng`'s RTL8188EUS DKMS driver, which we port here).

**Special thanks: Sandman**, close friend and the master to my Linux & wireless-hacking apprenticeship.

A few more of the driver authors we ported from:

* **Nick Morrow** ([@morrownr](https://github.com/morrownr)) — the out-of-tree Realtek USB
  DKMS drivers (RTL8812AU / RTL8814AU / RTL8821AU / RTL8822BU) that keep these cards alive.
* **Stanislaw Gruszka**, **Ivo van Doorn**, and the **rt2x00** team — the Ralink drivers.
* **Lorenzo Bianconi** and **Felix Fietkau** — MediaTek `mt76`.
* **Sujith Manoharan** and the **ath9k** team; **Bitterblue Smith** and the Realtek **rtw88** team.

The full list (every substantive contribut...