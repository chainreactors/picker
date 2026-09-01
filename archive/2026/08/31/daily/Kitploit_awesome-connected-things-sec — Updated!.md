---
title: awesome-connected-things-sec — Updated!
url: https://kitploit.com/en/posts/github-v33ru-awesome-connected-things-sec-ff4329506e2824e3a8d548a915502c7d841d9963f187e8366985aaafd54fa212
source: Kitploit
date: 2026-08-31
fetch_date: 2026-09-01T06:59:46.571944
---

# awesome-connected-things-sec — Updated!

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/48362/e2bdf22a796f2bdbfac266212c1887ee624b3bdffb853ca5b2484dd1357cde77.png)

UpdatedAug 31, 2026

# awesome-connected-things-sec — Updated!

A Curated list of Security Resources for all connected things

Share

# 🔐 Awesome Connected Things Security Resources

Security research and exploitation techniques for IoT, embedded, industrial, and automotive systems.

[![](https://assets.kitploit.com/production/public/readmes/48362/e2bdf22a796f2bdbfac266212c1887ee624b3bdffb853ca5b2484dd1357cde77.png)](https://github.com/V33RU/awesome-connected-things-sec)

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
![](https://img.shields.io/github/stars/V33RU/awesome-connected-things-sec?style=flat-square&logo=github&label=Stars&color=gold)
![](https://img.shields.io/github/forks/V33RU/awesome-connected-things-sec?style=flat-square&logo=git&label=Forks&color=blue)
![](https://img.shields.io/github/license/V33RU/awesome-connected-things-sec?style=flat-square&label=License&color=green)
![](https://img.shields.io/github/last-commit/V33RU/awesome-connected-things-sec?style=flat-square&label=Updated&color=red)
![](https://img.shields.io/badge/Resources-900+-blueviolet?style=flat-square)

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=58A6FF%C2%A2er=true&vCenter=true&random=false&width=600&lines=Firmware+%E2%80%A2+Wireless+%E2%80%A2+Hardware+%E2%80%A2+Protocols;UART+%E2%86%92+JTAG+%E2%86%92+SWD+%E2%86%92+Firmware+%E2%86%92+Root;Hack+The+Planet,+One+Device+At+A+Time)

[![](https://img.shields.io/badge/%F0%9F%8F%AD_ICS-SCADA_&_OT-ff6b6b?style=for-the-badge)](https://github.com/V33RU/awesome-connected-things-sec/blob/main/docs/ICS/Industrial-Control-Systems.md)
[![](https://img.shields.io/badge/%F0%9F%9A%97_AUTO-CAN_&_ECU-4ecdc4?style=for-the-badge)](https://github.com/V33RU/awesome-connected-things-sec/blob/main/docs/Automotive/automotive-security.md)
[![](https://img.shields.io/badge/%F0%9F%A4%96_ROBOTICS-ROS_&_DDS-8b5cf6?style=for-the-badge)](https://github.com/V33RU/awesome-connected-things-sec/blob/main/docs/Robotics/robotics-security.md)
[![](https://img.shields.io/badge/%F0%9F%93%9A_AWESOME-COLLECTION-a855f7?style=for-the-badge)](https://github.com/V33RU/awesome-connected-things-sec/blob/main/docs/awesome-collection.md)
[![](https://img.shields.io/badge/%F0%9F%A4%9D_CONTRIBUTE-JOIN_US-f59e0b?style=for-the-badge)](https://github.com/V33RU/awesome-connected-things-sec/blob/main/contributing.md)

[![](https://img.shields.io/badge/%E2%9A%A1_Hardware-Hacking-dc2626?style=flat-square)](#hardware-attacks)
[![](https://img.shields.io/badge/%F0%9F%93%B6_Bluetooth-BLE-2563eb?style=flat-square)](#bluetooth--ble)
[![](https://img.shields.io/badge/%F0%9F%92%BE_Firmware-Analysis-16a34a?style=flat-square)](#firmware-security)
[![](https://img.shields.io/badge/%F0%9F%93%A1_Wireless-Protocols-9333ea?style=flat-square)](#wireless-protocols)
[![](https://img.shields.io/badge/%F0%9F%9B%A0%EF%B8%8F_Tools-Arsenal-ea580c?style=flat-square)](#tools)
[![](https://img.shields.io/badge/%F0%9F%8E%AE_Labs-CTFs-0891b2?style=flat-square)](#labs-and-ctfs)

[![](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/iotsrg)
[![](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/EH9dxT9)
[![](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/v33riot)
[![](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/veeraiot)

---

## Contents

* [Hardware Attacks](#hardware-attacks)
  + [Fundamentals](#fundamentals)
  + [Interface Attacks](#interface-attacks)
  + [Memory Extraction](#memory-extraction)
  + [Side-Channel and Fault Injection](#side-channel-and-fault-injection)
  + [PCIe and DMA Attacks](#pcie-and-dma-attacks)
* [Wireless Protocols](#wireless-protocols)
  + [RF Fundamentals](#rf-fundamentals)
  + [Bluetooth / BLE](#bluetooth--ble)
  + [Zigbee / Z-Wave](#zigbee--z-wave)
  + [LoRa / LoRaWAN](#lora--lorawan)
  + [Matter / Thread](#matter--thread)
  + [Cellular (GSM/LTE/5G)](#cellular-gsmlte5g)
  + [NFC/RFID](#nfcrfid)
  + [DECT (Digital Enhanced Cordless Telecommunications)](#dect-digital-enhanced-cordless-telecommunications)
  + [Wi-Fi](#wi-fi)
  + [USB](#usb)
  + [UWB (Ultra-Wideband)](#uwb-ultra-wideband)
  + [TETRA](#tetra)
* [Firmware Security](#firmware-security)
  + [Fundamentals](#fundamentals-1)
  + [Extraction](#extraction)
  + [Static Analysis Tools](#static-analysis-tools)
  + [Dynamic Analysis and Emulation](#dynamic-analysis-and-emulation)
  + [OTA Update Security](#ota-update-security)
  + [RTOS Security](#rtos-security)
  + [Reverse Engineering Tools](#reverse-engineering-tools)
  + [Online Assemblers](#online-assemblers)
  + [ARM Exploitation](#arm-exploitation)
  + [Binary Analysis](#binary-analysis)
  + [Secure Boot](#secure-boot)
  + [UEFI Security](#uefi-security)
  + [Symlink Attacks](#symlink-attacks)
  + [Router Firmware Analysis](#router-firmware-analysis)
  + [Router Exploitation](#router-exploitation)
  + [Secure Boot Bypasses](#secure-boot-bypasses)
* [Network and Web Protocols](#network-and-web-protocols)
  + [MQTT](#mqtt)
  + [CoAP](#coap)
  + [mTLS](#mtls)
  + [IoT Protocols Overview](#iot-protocols-overview)
* [Cloud and Backend Security](#cloud-and-backend-security)
  + [AWS IoT Security](#aws-iot-security)
  + [Firebase / Cloud Misconfigurations](#firebase--cloud-misconfigurations)
* [Mobile Application Security](#mobile-application-security)
  + [Android](#android)
  + [iOS](#ios)
* [Industrial and Automotive](#industrial-and-automotive)
  + [ICS/SCADA](#icsscada)
  + [Automotive Security](#automotive-security)
  + [EV Chargers](#ev-chargers)
* [Payment Systems](#payment-systems)
  + [ATM Hacking](#atm-hacking)
  + [Payment Village](#payment-village)
* [Tools](#tools)
  + [Hardware Tools](#hardware-tools)
  + [Software Tools](#software-tools)
  + [Fuzzing Tools](#fuzzing-tools)
  + [Pentesting Operating Systems](#pentesting-operating-systems)
  + [Search Engines](#search-engines)
* [Defensive Security](#defensive-security)
  + [Threat Modeling](#threat-modeling)
  + [Secure Development](#secure-development)
  + [Incident Response](#incident-response)
* [Learning Resources](#learning-resources)
  + [Training Platforms](#training-platforms)
  + [Cheatsheets](#cheatsheets)
  + [Vulnerability Guides](#vulnerability-guides)
  + [Pentesting Guides](#pentesting-guides)
  + [YouTube Channels](#youtube-channels)
  + [Books](#books)
  + [IoT Series](#iot-series)
* [Labs and CTFs](#labs-and-ctfs)
  + [Vulnerable Applications](#vulnerable-applications)
  + [CTF Competitions](#ctf-competitions)
  + [Continuous Learning Platforms](#continuous-learning-platforms)
  + [Lab Setup](#lab-setup)
* [Research and Community](#research-and-community)
  + [Technical Research](#technical-research)
  + [Blogs](#blogs)
  + [Community Platforms](#community-platforms)
  + [Villages](#villages)
  + [Researchers to Follow](#researchers-to-follow)
  + [Device-Specific Research](#device-specific-research)
  + [TrustZone and TEE Research](#trustzone-and-tee-research)
  + [Pwn2Own Research](#pwn2own-research)
* [MCP / AI Agent](#mcp--ai-agent)
  + [Bluetooth Reverse Engineering](#bluetooth-reverse-engineering)

## Hardware Attacks

### Fundamentals

* [IoT Hardware Guide](https://www.postscapes.com/internet-of-things-hardware/)
* [Intro to Hardware Hacking - Dumping Your First Fir...