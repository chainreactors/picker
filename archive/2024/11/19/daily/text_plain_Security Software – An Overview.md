---
title: Security Software – An Overview
url: https://textslashplain.com/2024/11/18/security-software-an-overview/
source: text/plain
date: 2024-11-19
fetch_date: 2025-10-06T19:18:29.004521
---

# Security Software – An Overview

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Security Software – An Overview

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-11-182025-09-03](https://textslashplain.com/2024/11/18/security-software-an-overview/)Posted in[design](https://textslashplain.com/category/design/), [security](https://textslashplain.com/category/security/), [tech](https://textslashplain.com/category/tech/)Tags:[Defender](https://textslashplain.com/tag/defender/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/)

I’ve spent nearly my entire professional career in **software security**: designing software to prevent abuse by bad actors. I’ve been battling the bad guys for over two decades now, from hunting security bugs in Microsoft Office (*I once won an Xbox for finding a vulnerability that allowed malicious clipart take over your computer*) to designing security mitigations in Internet Explorer, Google Chrome, Edge, and Windows, to building tools to allow other good actors to find and kill security bugs.

[In 2022](https://textslashplain.com/2022/07/22/iwebbrowser3beforenavigate/), I left the world of ***software security*** for the world of ***security software***, rejoining some old friends now on the Microsoft Defender team. The difference seems slight but it’s a big one– instead of trying to keep an otherwise-useful software product secure from attackers, now the entire point of my product is to **protect users**.

*If not for adversaries, my product would have no reason to exist.*

## What Is “Protection”?

The goal of protection is to **prevent bad actors from abusing technology to cause loss** for protectees. While those losses can take many direct forms, most fall into several categories:

* Loss of **money** (compromise of bank/credit accounts, ransoms paid to recover data)

* Loss of **productivity** (loss of device/service availability, time to recover from incidents, etc.)

* Loss of **data** (destruction of potentially irretrievable data)

* Loss of **reputation** (bad PR, loss of customer/public trust, embarrassing secrets exposed)

* **Legal** ramifications

Beyond losses caused by bad actors, protection features must avoid *other* losses:

* Loss of **productivity** *due to* *protection* in the *absence* of an attacker (e.g. false positives, application compatibility breakage, performance hits, user confusion, all leading to lower productivity)

* Loss of **regulatory approval** (e.g. failure to demonstrate *compliance* with infosec standards could result in loss of permission to operate in a regulated industry)

* Loss of **peace of mind** (e.g. failure to explain protection/posture results in user feeling unsafe/unconfident because they worry about attacks)

Avoiding these *other losses* is absolutely critical– the cure must not be worse than the disease, both for society and for our business. I often joke: “*You start having a real hard time selling fire extinguishers if even* one *of them* ever *burns down a building*.”

### Framing: Protection Levers

To provide protection, vendors of security software invest in several related areas:

* **Sensors** – Allow watching events of interest to determine when an attack may be imminent or underway. *Examples: AV File system monitor, Network Protection connection monitor.*

* **Throttles** – Allow control of the behavior of the system to prevent events when an attack is suspected or detected. *Examples: Edge’s Anti-phish blocking, Defender’s File System filter, Defender’s Network Protection connection disruption.*

* **Intelligence** – *Intelligence* guides how to react to sensed data in order to block attacks with throttles, without interfering with the normal operation of the system. Intelligence includes both **Threat Intelligence** (indicators of compromise and indicators of attack (IoC/IoA) as well as **Compatibility Intelligence** (“Known good” software and services that are legitimate and should not be blocked.) *Examples: SmartScreen Web Defense Service, Application Reputation Service, AV Signatures & Behavior Monitoring. In some cases, customers might provide their own intelligence via 3P TI or via direct knowledge of their own usage of IT.*

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-32.png?w=596)](https://textslashplain.com/wp-content/uploads/2024/11/image-32.png)

Beyond these core protection levers, two other levers are important for the overall protection story:

* **Remediations** – The ability to act upon specialized intelligence to recover from an attack. For instance, after a ransomware incident is disrupted, what can we do to help the user? e.g. password change workflows, file recovery from OneDrive or Volume Shadow Copy, etc.

* **UX / Visibility** – The ability of the user or a regulator to understand protection state and feel confident if the protection state is “good”, or to recognize the need for reconfiguration if it is not.

These levers work together to build higher level protection concepts:

* Sensor + Intelligence = Detector

* Sensor + Throttle + Intelligence = Blocker

* Intelligence + Remediations = Recovery

Improvements in each of these areas can increase the level of protection, and we can unlock new protections with either the introduction of new capabilities in each area, or a new combinations of levers.

#### Other Uses for Sensors and Throttles

Sensors and Throttles are powerful primitives that have uses beyond traditional protection scenarios.

For example, an enterprise may combat **insider threats** and enforce **regulatory compliance** by using sensors and throttles to build **Information Rights Management** products like [Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview).

Sensors and Throttles are also often used to achieve non-protection goals, sometimes called **Control scenarios**. For example, combining the Web Defense Sensors and Throttles with a list of site categories enables **[Web Content Filtering](https://learn.microsoft.com/en-us/defender-endpoint/web-content-filtering)** to enforce an organization’s Acceptable Use Policy (“*No gambling sites may be used at work*“).

---

## My Journey to Security Software

The last two years has been a whirlwind of learning: security software is a huge and very profitable industry, and as such there’s an entire universe of complexity and a new encyclopedia of acronyms and terms of art to learn. Even “Microsoft Defender” is a bit of a misnomer– it’s not one product, but an entire *line of products* designed to protect both enterprises and consumers from attack.

At a very high level, my product, **Microsoft Defender for Endpoint**, breaks down into two major components: Endpoint Protection (EPP) and Endpoint Detection and Response (EDR). These days, most of my work accrues to MDE’s EPP.

### EPP

The primary goal of Endpoint Protection is to protect the user against threats on their individual endpoint device. Most EPP features focus on preventing **initial access** (attacks that allow an attacker to get malicious code running on the device in the first place). Modern endpoint protection software does not rely solely on static signatures (file hashes or byte sequences), going beyond to [emulate unknown code](https://i.blackhat.com/us-18/Thu-August-9/us-18-Bulazel-Windows-Offender-Reverse-Engineering-Windows-Defenders-Antivirus-Emulator.pdf) and watch for suspicious behavior of processes as they execute.

Every Windows user gets many of the most important EPP features for free, including MSAV (Microsoft Antivirus) which protects against viruses and malware, and [SmartScreen](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/), which protects against web-borne threats (phishing, malware, and [techscams](https://textslashplain.com/2023/09/12/attack-techniques-fullscree...