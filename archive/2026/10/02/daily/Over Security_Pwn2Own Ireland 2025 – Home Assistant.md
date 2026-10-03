---
title: Pwn2Own Ireland 2025 – Home Assistant
url: https://blog.compass-security.com/2026/10/pwn2own-ireland-2025-home-assistant/
source: Over Security
date: 2026-10-02
fetch_date: 2026-10-03T07:13:12.695907
---

# Pwn2Own Ireland 2025 – Home Assistant

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Pwn2Own Ireland 2025 – Home Assistant](https://blog.compass-security.com/2026/10/pwn2own-ireland-2025-home-assistant/ "Pwn2Own Ireland 2025 – Home Assistant")

[October 2, 2026](https://blog.compass-security.com/2026/10/pwn2own-ireland-2025-home-assistant/ "Pwn2Own Ireland 2025 – Home Assistant")
 /
[Emanuele Barbeno](https://blog.compass-security.com/author/ebarbeno/)
 /
[0 Comments](https://blog.compass-security.com/2026/10/pwn2own-ireland-2025-home-assistant/#respond)

## Introduction

Pwn2Own is a renowned hacking competition organized by the Zero Day Initiative (ZDI), where security researchers demonstrate previously unknown vulnerabilities in popular software, operating systems, browsers, IoT devices, and other technologies. Having participated in both the [2023](https://blog.compass-security.com/2024/03/pwn2own-toronto-2023-part-1-how-it-all-started/) and [2024](https://blog.compass-security.com/2025/06/pwn2own-ireland-2024-ubiquiti-ai-bullet/) editions of Pwn2Own, we decided to take another shot in 2025. This time, our goal was to avoid collisions, where multiple teams discover the same vulnerability during the same event, leading to reduced prize money and fewer Master of Pwn points.

This blog post walks through our journey from discovery to full exploitation. We start by exploring the Home Assistant device architecture, then detail how we found a remote code execution vulnerability in an add-on. From there, we show how we leveraged it to pivot to the underlying operating system and achieve root-level access. We conclude with our experience at the Pwn2Own 2025 Cork edition.

## Target Selection

We started by looking at several different targets. Our initial list included the Wyze Cam Pan v3 and the Synology CC400W from the surveillance system category, the Brother MFC-J1010DW from the printer category, the Philips Hue Bridge and the Home Assistant Green from the smart home category.

After assessing the various targets, we shifted our focus to the Home Assistant Green due to the progress we had made on that platform. This led us to the discovery of an exploit chain that resulted in an unauthenticated remote code execution vulnerability.

## Device Overview

Home Assistant is a free, open-source smart home platform designed to centralize control of all your IoT devices. The Home Assistant Green device is the dedicated hardware product made for Home Assistant:

[![](https://blog.compass-security.com/wp-content/uploads/2026/07/image-2-1024x618.png)](https://blog.compass-security.com/wp-content/uploads/2026/07/image-2.png)

Home Assistant is designed as a layered platform, with each component responsible for a specific part of the system:

* The **Home Assistant OS** is the underlying operating system that powers the device. It provides a lightweight, purpose-built Linux environment that includes container management, networking, storage, and hardware support. Most users never interact directly with the OS; its primary role is to provide a stable foundation for the Home Assistant platform.
* The **Supervisor** is the orchestration and management layer that sits between the operating system and the application workloads. It is responsible for lifecycle management of Home Assistant Core and add-ons, including installation, updates, configuration, health monitoring, backups, and inter-container networking. The Supervisor exposes an HTTP API to facilitate communication between the Core and various add-ons. By default, this API is restricted to internal communication and is not exposed to the external network or the local LAN.
* The **Home Assistant Core** is the application itself; the home automation engine that users interact with daily. It manages integrations, automations, dashboards, devices, and entities. Core is responsible for collecting data from connected devices, processing automation logic, and exposing everything through the web interface and APIs.
* **Add-ons** are optional applications that run alongside Home Assistant Core in isolated containers. They extend the platform with additional services such as MQTT brokers, databases, media servers, Zigbee coordinators, or custom automation tools. Each add-on executes in its own isolated container with well-defined permissions and access controls.

Except for the OS, all of these components run as Docker containers. The Home Assistant Core container exposes port `8123`, which serves as the management interface for the web application. While the Core communicates directly with the internal Supervisor APIs, add-ons may optionally interact with these same endpoints, depending on their configuration:

[![](https://blog.compass-security.com/wp-content/uploads/2026/07/image-3-1024x582.png)](https://blog.compass-security.com/wp-content/uploads/2026/07/image-3.png)

For a more detailed overview of the architecture, please refer to the [official documentation](https://developers.home-assistant.io/docs/architecture_index/).

## Apps / Add-Ons

While our initial investigation of the Home Assistant management interface revealed several weaknesses, we were unable to chain them into a full RCE. In addition, to minimize the risk of a collision with other participants, we decided to expand our scope to include official add-ons.

Home Assistant uses containerized add-ons to extend its functionality. These applications run as isolated Docker containers managed by the Home Assistant Supervisor. Depending on their configuration, add-ons can expose additional services, communicate with the Core via internal APIs, and can be configured to start automatically alongside the main system.

Add-ons are categorized into two types:

* **Official Add-ons:** Developed and maintained directly by the Home Assistant project.
* **Community Add-ons:** Maintained by third-party developers and exist outside of the core project.

We focused our efforts on official add-ons, as targeting the core ecosystem might present a more impactful scenario. After evaluating several available add-ons, we identified **Music Assistant** as a primary target. Music Assistant is a music library manager available as a Home Assistant add-on. It manages both offline and online music sources and can stream music to various supported players inside the local network.

After installation, the Music Assistant add-on provides a web interface integrated into the Home Assistant management console. This interface requires Home Assistant authentication:

[![](https://blog.compass-security.com/wp-content/uploads/2026/07/image-4-1024x681.png)](https://blog.compass-security.com/wp-content/uploads/2026/07/image-4.png)

## Music Assistant Remote Analysis

### Unprotected Service Exposure

We performed a network scan to check for additional exposed services on the Music Assistant container, which identified port `8095` as open:

```
$ nmap -p- 10.0.0.9
[CUT BY COMPASS]
PORT      STATE  SERVICE
111/tcp   open   rpcbind
4357/tcp  open   qsnet-cond
8000/tcp  open   http-alt
8095/tcp  open   unknown
8097/tcp  open   sac
8123/tcp  open   polipo
18555/tcp open   unknown
[CUT BY COMPASS]
```

This port exposes the same web interface integrated into the Home Assistant management console. As shown below, the interface can be accessed without authentication:

[![](https://blog.compass-security.com/wp-content/uploads/2026/07/image-5-1024x892.png)](https://blog.compass-security.com/wp-co...