---
title: Unveiling the Gaps: Linux EDR Telemetry in Focus
url: https://kostas-ts.medium.com/unveiling-the-gaps-linux-edr-telemetry-in-focus-1290a010ad1b
source: Over Security - Cybersecurity news aggregator
date: 2024-12-18
fetch_date: 2025-10-06T19:44:27.912446
---

# Unveiling the Gaps: Linux EDR Telemetry in Focus

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1290a010ad1b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkostas-ts.medium.com%2Funveiling-the-gaps-linux-edr-telemetry-in-focus-1290a010ad1b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkostas-ts.medium.com%2Funveiling-the-gaps-linux-edr-telemetry-in-focus-1290a010ad1b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Unveiling the Gaps: Linux EDR Telemetry in Focus

[![Kostas](https://miro.medium.com/v2/resize:fill:64:64/1*BtTfw89t0Sfap1SKrF3hvA.jpeg)](/?source=post_page---byline--1290a010ad1b---------------------------------------)

[Kostas](/?source=post_page---byline--1290a010ad1b---------------------------------------)

7 min read

·

Dec 17, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

## Introduction

Visibility serves as the cornerstone for understanding and mitigating modern threats. The **EDR Telemetry Project** was established as a comprehensive effort to evaluate the depth and breadth of telemetry provided by Endpoint Detection and Response (EDR) solutions for Windows systems. Its purpose has been to illuminate the gaps that often go unnoticed, providing an objective measure of whether defenders can depend on these tools to identify, analyze, and respond confidently to adversarial activity.

> If you don’t have medium Premium, you can read this blog here: [https://kostas-ts.medium.com/unveiling-the-gaps-linux-edr-telemetry-in-focus-1290a010ad1b?sk=2f3ced9dbd47c83acd9e6b8fe26af119](/unveiling-the-gaps-linux-edr-telemetry-in-focus-1290a010ad1b?sk=2f3ced9dbd47c83acd9e6b8fe26af119)

As the project moved forward, we noticed an important area where we could improve: the need to put more emphasis on Linux systems. Linux is no longer a niche platform; it is the backbone of modern IT. From cloud environments to enterprise workloads and critical infrastructure, Linux powers much of what we depend on daily.

The decision to expand the project to include Linux was necessary. Withattackers increasingly targeting Linux environments with sophisticated threats, defenders must have the tools to monitor and respond effectively. This article delves into why Linux telemetry matters, our approach to testing, and what the results reveal about the current state of Linux EDR solutions.

## The Rising Tide of Linux Threats

For years, Linux enjoyed a reputation as a “safe” operating system. Its smaller market share compared to Windows, combined with its robust permission model, made it less attractive to attackers. That era is over.

* Attackers are now actively targeting Linux systems with specialized malware, such as the **perfctl malware**, which was designed to evade detection and compromise millions of servers ([AquaSec, 2024](https://www.aquasec.com/blog/perfctl-a-stealthy-malware-targeting-millions-of-linux-servers/)).
* Ransomware families like **Helldown** have also been observed expanding their capabilities to encrypt Linux systems, a sign of the growing value attackers see in these environments ([Sekoia, 2024](https://blog.sekoia.io/helldown-ransomware-an-overview-of-this-emerging-threat/)).
* These threats often exploit the unique characteristics of Linux environments, such as exposed Docker services, misconfigured Apache Hadoop instances, or vulnerable Redis deployments ([Cado Security, 2024](https://www.cadosecurity.com/blog/spinning-yarn-a-new-linux-malware-campaign-targets-docker-apache-hadoop-redis-and-confluence)). The ability to evade detection through stealthy techniques — like kernel-level exploitation — adds to the challenge.

This trend underscores the critical need for enhanced Linux telemetry. Without it, defenders face blind spots that attackers can easily exploit. The challenge lies in detecting and understanding these attacks promptly to respond effectively, highlighting the importance of a swift response.

## Expanding the EDR Telemetry Project to Linux

Adding Linux to the EDR Telemetry Project wasn’t a simple extension of the Windows framework. It required a complete rethinking of how to approach telemetry testing. Linux environments operate differently, with processes, services, and user activities managed in ways unique to the platform.

For instance, while Windows has well-defined service management through the Service Control Manager (SCM), Linux services are often managed via **systemd**, **cron**, or **init.d**. Monitoring service creation or modification on Linux means tracking changes to specific directories, such as `/etc/systemd/system` or `/var/spool/cron`.

Similarly, capturing user account changes requires monitoring system calls rather than relying on high-level process activity, as one might on Windows. This nuanced approach ensures the testing reflects real-world Linux operations and avoids superficial comparisons with Windows systems.

Through collaboration with the community — on platforms like [GitHub](https://github.com/tsale/EDR-Telemetry/issues/21), discord conversations in the EDR Telemetry Server and during one-on-one discussions— the framework was refined to focus on meaningful events. This collaboration improved the testing methodology and highlighted the importance of tailoring solutions to Linux’s unique needs.

## Methodology and Testing Framework

Creating a comprehensive framework for testing Linux telemetry required a focus on accuracy, transparency, and relevance. Below, we outline the guiding principles and provide a detailed explanation of the categories and events tested.

## Guiding Principles for Testing

1. **Default Configurations**
   To ensure fairness, all EDR solutions were tested with their default configurations. This reflects how these tools are deployed in real-world scenarios, where defenders may not have the time or expertise to fine-tune every setting. Testing with default setups highlights out-of-the-box capabilities and identifies areas where additional configuration may be needed.
2. **Syscall-Based Event Generation**
   The testing script uses system calls (syscalls) to generate events directly. By bypassing high-level processes like command-line utilities, we ensure the results focus on actual telemetry capabilities rather than inferred activities.
   ***For example —*** *user account creation events were generated using syscalls directly, bypassing the need to execute* `useradd` *or* `adduser` *commands.*
3. **Linux-Specific Context**
   Linux environments operate differently from Windows, so the testing framework was tailored to address these differences. Categories and events were chosen to reflect real-world attacker behaviours and defender needs, ensuring the results were relevant and actionable.

## Categories and Events Tested

The testing categories and events include:

**Process Activity**

* **Process Creation:** Tracks when a process is started.
* **Process Termination:** Detects when a process ends, crucial for identifying potential tampering.

**File Manipulation**

* **File Creation, Modification, Deletion:** Covers all aspects of file lifecycle, esse...