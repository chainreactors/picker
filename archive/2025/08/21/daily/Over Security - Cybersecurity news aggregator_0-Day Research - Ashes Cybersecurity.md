---
title: 0-Day Research - Ashes Cybersecurity
url: https://ashes-cybersecurity.com/0-day-research/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-21
fetch_date: 2025-10-07T00:50:03.287781
---

# 0-Day Research - Ashes Cybersecurity

[Skip to content](#content)

AshES Cybersecurity

* [Home](https://ashes-cybersecurity.com/)
* [Our Services](https://ashes-cybersecurity.com/our-services/)
* [Portfolio](https://ashes-cybersecurity.com/portfolio/)
* [Contact](https://ashes-cybersecurity.com/contact/)
* [0-Day Research](https://ashes-cybersecurity.com/0-day-research/)
  + [Elastic EDR 0-day, Part I](https://ashes-cybersecurity.com/0-day-research/)
  + [Elastic EDR 0-day, Part II: Technical Evidence and the Trigger](https://ashes-cybersecurity.com/elastic-edr-0-day-part-2/)

* [Home](https://ashes-cybersecurity.com/)
* [Our Services](https://ashes-cybersecurity.com/our-services/)
* [Portfolio](https://ashes-cybersecurity.com/portfolio/)
* [Contact](https://ashes-cybersecurity.com/contact/)
* [0-Day Research](https://ashes-cybersecurity.com/0-day-research/)
  + [Elastic EDR 0-day, Part I](https://ashes-cybersecurity.com/0-day-research/)
  + [Elastic EDR 0-day, Part II: Technical Evidence and the Trigger](https://ashes-cybersecurity.com/elastic-edr-0-day-part-2/)

## When Defenders Become the Attackers: The Elastic EDR 0-Day (RCE + DoS)

[**Part 2: Click here for Elastic EDR 0-day Part II – Technical Evidence and the Trigger**](https://ashes-cybersecurity.com/elastic-edr-0-day-part-2/)

**Introduction**

Security software is supposed to defend. But what happens when the very tool trusted to protect enterprises becomes the weapon?

In my latest research I uncovered a 0-day vulnerability in Elastic’s Endpoint Detection and Response (EDR) kernel driver “**elastic-endpoint-driver.sys”**. This flaw allows the EDR to be turned against its own host system. It enables a catastrophic sequence of attacks that go far beyond a simple crash.

**A High Level overview of the attack chain**

The Elastic driver 0-day is not just a stability bug. It enables a full attack chain that adversaries can exploit inside real environments.

Step 1: EDR Bypass:
With the help of Ashes Cybersecurity’s custom C based Loader, the attacker is able to bypass Elastic’s security solutions (Elastic Agent + Elastic Defend)

Step 2: Remote Code Execution (RCE):
With detection bypassed, the attacker is able execute low privileged malicious code on the system with no risk of being detected or blocked by the EDR.

Step 3: Persistence:
Once code execution is established, the attacker plants a custom kernel driver, to interact with the vulnerable Elastic Endpoint Driver (“elastic-endpoint-driver.sys”)

Step 4: Privileged Persistent Denial of Service:
The flaw allows the driver itself to exhibit malware-like behaviour and attack its own host.

![](https://ashes-cybersecurity.com/wp-content/uploads/2025/08/full.png)

**The 0-day in Detail**

The 0-day resides in Elastic’s Microsoft signed kernel driver “elastic-endpoint-driver.sys”. Under specific conditions the driver mishandles memory operations inside privileged kernel routines, causing a system crash that can be reliably and repeatedly triggered. The flaw occurs in a code path where a user-mode controllable pointer is passed into a kernel function without proper validation. This results in a **CWE-476: NULL Pointer Dereference**, where the pointer references invalid memory regions at kernel level.

The crash occurs at a specific offset inside “elastic-endpoint-driver.sys” where the instruction call cs:InsertKernelFunction is executed with rcx dereferencing a user-controlled pointer. If the pointer is NULL, freed, or corrupted (e.g. via race or double free), the kernel routine dereferences it without validation, leading to a BSOD.

This vulnerable code path can be exercised during normal system activity, such as specific compilation or process injection attempts. When the driver mishandles the memory pointer, it can be forced into a kernel-level crash. For proof-of-concept demonstration, I used a custom driver to reliably trigger the flaw under controlled conditions. This shows that the vulnerability does not rely on traditional malware, the Elastic driver itself exhibits the malicious behavior once the faulty code path is reached.

In practice this vulnerability enables a complete attack chain: bypassing EDR monitoring, enabling remote code execution with reduced visibility, establishing persistence, and finally turning the driver into a weapon. This makes the Elastic EDR 0-day one of the most severe categories of vulnerability: a signed, trusted security component that can be repurposed into a persistent, privileged weapon embedded inside every host that runs Elastic EDR.

**Proof of Concept (Custom EXE + Custom SYS)**

 To prove that the flaw is reliably reproducible in realistic conditions, I wrote my own Proof of Concept involving a Custom C based research Loader and a Custom driver file. The C based Loader performs the following functions

* EDR Bypass.
* Executes code to load the custom driver
* Configures persistence to reload the driver on reboot
* Reboots the system.

The custom Driver performs the following functions:

* Interacts with the vulnerable elastic-endpoint-driver.sys to ask a simple question on all subsequent system boots.

This causes Elastic’s driver to exhibit malware like behaviour and cause a BSOD (Blue/Black Screen of Death) and renders the protected system unstable and unusable until the driver is removed.

[<https://ashes-cybersecurity.com/wp-content/uploads/2025/08/vid0.mp4>](https://ashes-cybersecurity.com/wp-content/uploads/2025/08/vid0.mp4?_=1)

[<https://ashes-cybersecurity.com/wp-content/uploads/2025/08/ElasticEDRBypassFinal-online-video-cutter.com_.mp4>](https://ashes-cybersecurity.com/wp-content/uploads/2025/08/ElasticEDRBypassFinal-online-video-cutter.com_.mp4?_=2)

**Real World Impact**

The implications of this 0-day are extreme.

* Enterprise Risk: Every organization running Elastic’s Defenses (SIEM + EDR) is effectively carrying a potential attacker inside its own trusted defenses.
* Weaponization at Scale: Adversaries could trigger this flaw to remotely and repeatedly disable Enterprise endpoints protected by Elastic.
* **Collapse of Trust:** A signed kernel driver turning hostile is the nightmare scenario for defenders. It undermines confidence not only in Elastic and Microsoft but in any security vendor shipping privileged signed drivers.

This is not a theoretical bug, it is an unpatched 0-day, reproducible today, and awaiting exploitation in the wild..

**Disclosure Timeline**

June 2nd, 2025: Discovery of the 0-day
June 11th, 2025: Disclosure attempt via HackerOne
July 29th, 2025: Disclosure attempt via ZDI
August 16th, 2025: Independent Disclosure

Affected Product:

**Filename: elastic-endpoint-driver.sys**

Product version: 8.17.6 (tested version, but all subsequent versions are currently affected since no patch is available yet)

Signature: Microsoft Windows Hardware Compatibility Publisher

                   Elasticsearch, Inc.

**IOCs**

elastic-endpoint-driver.sys     A6B000E84CB68C5096C0FD73AF9CEF2372ABD591EC973A969F58A81CF1141337

**Closing Notes from the Researcher**

Elastic’s EDR 0-day demonstrates the harshest truth about Cybersecurity today. When a security driver can be turned into a weapon against its own host it is no longer defense. It is a liability.

A defender that crashes, blinds or disables its own system on command is indistinguishable from malware. Until Elastic acknowledges and patches this issue, customers remain exposed to a live 0-day that can be used against them.

The problem is not just Elastic. The problem is a security industry that has broken trust with its users and researchers. Unless the security industry reforms, the line between defender and attacker will continue to blur.

Edit 1: Added more technical details in the paragraph “The 0-day in Detail”

Edit 2: The vulnerability was discovered during user-mode testing operations related to Ashes Cybersecurity Pvt Ltd. No security boundaries were crossed in                order to discover the flaw.

            Ashes Cybersecurity Pvt Ltd. is...