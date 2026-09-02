---
title: librepods nightly-53679cc
url: https://kitploit.com/en/posts/github-librepods-org-librepods-nightly-53679cc
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:10.922631
---

# librepods nightly-53679cc

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7308/dd79739201ddda9382b9f24871abdd8b39e75645fe7c341831c76ed98b61f805.png)

New releaseSep 1, 2026

# librepods nightly-53679cc

AirPods liberated from Apple's ecosystem.

Share

> [!WARNING]
> librepods.org is not an official website of the LibrePods project. It inaccurately claims to be the official website of the project by claiming copyrights and using the LibrePods logo in the footer. And at the same time, they say that the project is not affiliated with the LibrePods project or its developers.
>
> Please report any other such websites to [[email protected]](/cdn-cgi/l/email-protection#7b161e3b101a0d12081355030201)

![LibrePods](https://assets.kitploit.com/production/public/readmes/7308/dd79739201ddda9382b9f24871abdd8b39e75645fe7c341831c76ed98b61f805.png)

[![](https://img.shields.io/github/downloads/kavishdevar/librepods/total?label=GitHub%20Downloads)](https://github.com/kavishdevar/librepods/releases/latest)
[![](https://github.com/kavishdevar/librepods/actions/workflows/ci-android.yml/badge.svg)](https://github.com/kavishdevar/librepods/actions/workflows/ci-android.yml)
[![](https://github.com/kavishdevar/librepods/actions/workflows/ci-linux-rust.yml/badge.svg)](https://github.com/kavishdevar/librepods/actions/workflows/ci-linux-rust.yml)
[![](https://img.shields.io/github/issues/kavishdevar/librepods)](https://github.com/kavishdevar/librepods/issues)
[![](https://img.shields.io/discord/1441416992027574375?logoColor=white&color=5865F2&label=Discord)](https://discord.gg/HhG4ycVum4)

# What is LibrePods?

LibrePods allows you to use AirPods features that are exclusive to Apple devices. It implements the proprietary protocol used to exchange data between AirPods and Apple devices, enabling features like changing noise control modes, fast ear detection, accurate battery status, head gestures, conversational awareness, and more on non-Apple platforms.

# Feature availability

| Feature | Linux | Android |
| --- | --- | --- |
| Changing Listening Mode | ✅ | ✅ |
| Ear detection | ✅ | ✅ |
| Battery status | ✅ | ✅ |
| Renaming AirPods Note for AndroidOn Android, you need to re-pair your AirPods after renaming them because Android might not use the latest name. | ✅ | ✅ |
| Loud Sound Reduction | 🔴 | ⚪ |
| Head Gestures | ⛔ | ✅ |
| Conversational Awareness | ✅ | ✅ |
| Automatically connect to AirPods | ✅ | ✅ |
| Hearing Aid | 🔴 | ⚪ |
| Transparency Mode customization | 🔴 | ⚪ |
| Multi-device connectivity (Bluetooth Multipoint; 2 devices only) | ⚪ | ⚪ |
| Other accessibility configs (click to expand)  * Press speed * Press and Hold duration * Noise Cancellation with single AirPod * Volume control on swipe * Volume swipe speed | 🔴 | ✅ |
| Other general configs  * Press and Hold to cycle between listening modes/invoke digital assistant (invoking digital assistant needs a recent firmware) * Configure call controls * Personalized volume * Loud Sound Reduction (needs [VendorID spoofing](#vendorid-spoofing)) * Microphone side * Pause media when falling asleep (needs a recent firmware) * Enable `Off listening mode` to switch to `Off` | 🔴 | ✅ |
| [Head-tracked Spatial Audio](#spatial-audio) | ❓ | ❓ |
| [Heart Rate Monitoring](#heart-rate-monitoring) | ⛔ | 🔴 |
| [Find My](#find-my) | ❓ | ❓ |
| [High quality two-way audio](#high-quality-two-way-audio) | 🔴 | 🔴 |

| Symbol | Meaning |
| --- | --- |
| ✅ | Implemented and works well |
| ⚪ | Needs [VendorID spoofing](#vendorid-spoofing); use at your own risk |
| 🔴 | Not implemented yet; planned |
| ⛔ | Will not be implemented |
| ❓ | Unknown |

## Find My

The following features related to Find My are planned, but require further RE and might need root on Android:

* Add your AirPods to the Find My network
* Play sound through charging case to find it
* Notify when leaving behind
* Toggle case charging sounds

## Spatial Audio

The app does not currently provide head tracking information to Android for the OS to perform HRTF. This has not been explored completely, and it might need root.

Spatializing stereo sound is beyond this project's scope and will never be available. Many OEMs have an implementation of their own for this.

## Heart Rate Monitoring (AirPods Pro 3 and later)

This is being worked upon, check the #⁠reverse-engineering channel on the LibrePods Discord server for more information. If it is ever implemented, it will most likely need root on Android.

## High quality two-way audio

On iOS/iPadOS, you can continue using A2DP while AirPods send the audio stream from its microphone over AACP.

Since this needs deeper integration with audio on Android, it will most likely need root.

# Installation

* [**Android**](https://github.com/librepods-org/librepods/blob/HEAD/android/README.md)
* [**Linux**](https://github.com/librepods-org/librepods/blob/HEAD/linux/README.md)

# VendorID Spoofing

Turns out, if you change the VendorID in DID Profile to that of Apple, you get access to several special features!

You can do this on Linux by editing the DeviceID in `/etc/bluetooth/main.conf`. Add this line to the config file `DeviceID = bluetooth:004C:0000:0000`. For android you can enable the `act as Apple device` setting in the app's settings (shown only when Xposed is available and LibrePods module is enabled).

## Multi-device Connectivity

Upto two devices can be simultaneously connected to AirPods, for audio and control both. Seamless connection switching. The same notification shows up on Apple device when Android takes over the AirPods as if it were an Apple device ("Move to iPhone"). Android also shows a popup when the other device takes over.

## Accessibility Settings and Hearing Aid

Accessibility settings like customizing transparency mode (amplification, balance, tone, conversation boost, and ambient noise reduction), and loud sound reduction can be configured.

All hearing aid customizations can be done from Android (linux soon), including setting the audiogram result. The app doesn't provide a way to take a hearing test because it requires much more precision. It is much better to use an already available audiogram result.

# Protocol and Reverse Engineering

Please refer to the Wireshark dissector plugin by Nojus ([@pabloaul](https://github.com/pabloaul)) for more information on the protocols used: [pabloaul/apple-wireshark](https://github.com/pabloaul/apple-wireshark)

The dissector had not been used in LibrePods for most of the implementation; I had reverse engineered the protocol myself before this dissector was made. But many (future) features including two-way high quality audio and spatial audio would not have been possible without their RE efforts!

# Use of AI

## Android app

These parts of the app were completely AI-generated:

* Head Gestures - all of it, including logic and the UI
* The offset setup with r2+the xposed module (both versions)
* Troubleshooter and LogCollector

Rest everything- the background service, the Bluetooth manager classes (AACP and ATT), the entire UI, even the smallest components were written manually.

Some parts of the UI components were borrowed from [Kyant0's demo app](https://github.com/Kyant0/AndroidLiquidGlass/tree/master/catalog), which is licensed under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Linux (rewrite)

The `aacp.rs` and the `att.rs` files were translated from Kotlin to Rust with AI. Some parts of the `media_controller.rs` file, mainly the pulse integration, was also AI-generated.

# Supporters

A huge thank you to everyone supporting the project!

|  |  |  |
| --- | --- | --- |
| [![davdroman](https://assets.kitploit.com/p...