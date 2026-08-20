---
title: lamda v10.6
url: https://kitploit.com/en/posts/github-firerpa-lamda-v106
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:54:27.111046
---

# lamda v10.6

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F7312%2F75917ce25b1633e21ddbd6c56de557586171dedb0863597c014589892eb31d97.png&w=3840&q=75)

New releaseAug 19, 2026

# lamda v10.6

Android Full-Stack Device Control Platform: WebRTC/H.264 remote desktop, UI/OCR/image-matching automation, one-click MITM, built-in Frida, proxy/VPN/frp/P2P networking, MCP/Agent, 160+ APIs, designed for multi-device clusters and engineered deployments.

Share

# **FIRERPA Android** ｜ AI-Powered Automation

![FIRERPA](https://raw.githubusercontent.com/firerpa/lamda/HEAD/image/logo.svg)

![](https://img.shields.io/badge/python-3.6+-blue.svg?logo=python&labelColor=yellow)
![](https://img.shields.io/badge/android-6.0+-blue.svg?logo=android&labelColor=white)
![](https://img.shields.io/badge/root/non--root--mode-green.svg?logo=android&labelColor=black)
![](https://img.shields.io/badge/Built--in%20MCP-000.svg?logo=anthropic&labelColor=black)

###### An all-in-one Android automation framework that combines on-device services, AI-ready agents, and extensible tool invocation.

[Documentation](https://device-farm.com/docs/en/) | [使用文档](https://device-farm.com/docs/zh/) | [TELEGRAM](https://device-farm.com/contact#telegram) | [QQ Group](https://device-farm.com/contact#QQ) | [SKILLS](https://github.com/firerpa/skills) | [llms-full.txt](https://device-farm.com/llms-full.txt) | [中文版本](README.zh.md)

FIRERPA is an **all-in-one Android device control platform**. The server runs directly on the device with **no extra runtime dependencies**; it **supports multiple generations of Android** and works **with or without root**. On the PC side, the Python client library orchestrates UI automation, remote operations, traffic capture, Hook-based reverse engineering, network proxying, distributed networking, AI agents, and **MCP** through a single service and API. Compared with stitching together Appium, mitmproxy, frida-server, adb, uiautomator2, and ad-hoc scripts and ops tools, FIRERPA offers **one source of capabilities, unified configuration, connected workflows, and a stack built for multi-device, long-running, production use**.

## Remote Desktop & Live Streaming

FIRERPA provides a browser-based remote desktop: view and control the device in real time without installing a dedicated PC client, over LAN or across networks. Streaming supports both **MJPEG** and **H.264**, with software and hardware encoding backends. Frame rate (up to 60fps), resolution scale, bitrate, and quality can be tuned to device capability and network conditions—reducing bandwidth and improving smoothness on weak links. **WebRTC** is also supported, with configurable STUN/TURN servers for better NAT traversal and lower end-to-end latency in public or cross-region setups.

The remote desktop supports **multi-user concurrent access** for collaborative debugging, demos, and training. **Bidirectional clipboard** sharing and **live audio** (Android 10+) are included, along with an integrated terminal, drag-and-drop uploads, and browser-based file browsing and downloads—all over a single port. Built-in **visual layout inspection** highlights elements, supports Tab traversal, shows coordinates and RGB values, and exports the XML layout tree so you can validate selectors and automation logic in the same UI, shortening the loop from screen to script.

![demo](https://assets.kitploit.com/production/public/readmes/7312/251d9eed35540aadebab75dec6f3a59aaeb7c4b5f93ee39e8f74dcb8b0cfa68d.gif)

Remote desktop and RPC support **end-to-end TLS** and service-certificate access control, with optional custom WebUI login passwords to reduce exposure on public networks. Remote desktop capabilities can also be embedded into your own web apps over WebSocket (live video, touch, terminal, keys, etc.), with `allow_origin` for cross-origin integration—suitable for productizing real-device control.

## UI Automation

FIRERPA provides a full selector-based automation system: text, resourceId, description, scrollable, and other common matchers, plus **child / sibling** chaining for duplicate elements, deep hierarchies, or controls without distinctive attributes. At the element level: screenshots, wait for appear/disappear, corner/center coordinates, exists checks, Unicode input, stepped swipes, fling scrolling, scroll-to-end, and more. It can **coexist with other accessibility services** on Android 8.0+ and improves WebView node discovery for hybrid apps.

The **UI Watcher** listens for UI changes in real time and runs clicks, key events, or counters when conditions match—useful for auto-dismissing agreements, update prompts, ads, and other interruptions. Multiple selector conditions and per-event enable/disable are supported; transient screens can be counted.

**Virtual Display** is a differentiator: create isolated background displays on the device and run apps and automation there **without affecting the main screen**—e.g. auto-reply on a virtual display while you use the phone normally. The virtual-display API mirrors the main device API (`d.xxx` → `vd.xxx`); Watchers can be scoped to a virtual display. The WebUI supports **multi-display view and switching** in remote desktop—ideal for background tasks, parallel work, and human-in-the-loop plus machine automation.

For scenes without a standard view tree (games, custom-drawn UI), FIRERPA offers **OCR** and **image matching**. OCR supports paddleocr, easyocr, and custom HTTP backends; in clusters, recognition can run centrally instead of loading models on every PC, with GPU acceleration and flexible text matching. Image matching runs **on the device** (template or SIFT), without consuming PC resources; SIFT is robust to rotation, scale, and lighting. **Multi-touch** supports recording, replay, programmatic construction, and binary persistence for complex gestures and pressure.

Architecturally, FIRERPA uses a client/server model—better for **centralized scheduling, versioning, and fleet control** than on-device script runners like AutoJS; lighter than Appium; **more stable than uiautomator2 in multi-device scenarios**. The docs position it as a **functional superset** of common Android automation stacks—automation, capture, Hook, and ops can be chained in code on one platform without switching tools.

## Packet Capture & MITM

FIRERPA offers **one-click MITM capture**: automatic system root CA install, proxy setup, handling of Android version differences, and automatic network restore on exit—no manual cert or proxy toggling. Global capture, per-package capture, live request/response editing, shared mitmweb, and upstream HTTP proxy for **international traffic** are supported. Built-in **QUIC downgrade** reduces QUIC interference. Capture still works when PC and device only share a single FIRERPA port (e.g. ADB connect or frp forwarding).

Beyond one-click scripts, MITM is fully **API-driven**: install/uninstall system CAs compatible with mitmproxy, Fiddler, Charles, etc.; embed capture in automation pipelines alongside UI steps and Frida hooks. A Windows **startmitm.exe** is available without a Python install.

## Network, Proxy & Connectivity

On the device, FIRERPA provides full proxy support: **HTTP / HTTPS / SOCKS5 / Shadowsocks** (multiple ciphers), per-app proxy (including multi-user clones), DNS proxy, UDP proxy, LAN bypass, coexistence with OpenVPN, and **auto-connect** to configured proxies at startup. Proxies support **IPv6 and UDP** for complex networks.

**Device HTTP bridge proxy (tunnel2)** provides reverse-proxy capability: point your PC or browser HTTP proxy at the phone and traffic is forwarded through th...