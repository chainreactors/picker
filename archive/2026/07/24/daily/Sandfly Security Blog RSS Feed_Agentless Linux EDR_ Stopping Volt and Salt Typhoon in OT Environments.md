---
title: Agentless Linux EDR: Stopping Volt and Salt Typhoon in OT Environments
url: https://sandflysecurity.com/blog/agentless-linux-edr-stopping-volt-and-salt-typhoon-in-ot-environments
source: Sandfly Security Blog RSS Feed
date: 2026-07-24
fetch_date: 2026-07-25T04:59:24.399981
---

# Agentless Linux EDR: Stopping Volt and Salt Typhoon in OT Environments

[Meet Sandfly @ Black Hat 2026 · Free 3-month Pro license. Claim Now](/blog/sandfly-is-coming-to-black-hat-usa-2026)

[Partners](/partners)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Agentless Linux EDR: Stopping Volt and Salt Typhoon in OT Environments

24 July 2026

Embedded Linux

## Key Takeaways

* **The Threat:** Nation-state groups like Volt Typhoon and Salt Typhoon are targeting critical Operational Technology (OT) infrastructure using "Living off the Land" techniques to evade detection.
* **The Warning:** Recent advisories from the Cybersecurity and Infrastructure Security Agency (CISA), including the [2025 Threat Assessment and advisory AA25-239](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a), confirm these groups are actively pre-positioning for disruptive attacks.
* **The Problem:** Traditional Endpoint Detection and Response (EDR) agents have compatibility issues, may trigger kernel panics, and impact performance in complex OT networks.
* **The Solution:** Sandfly Security utilizes agentless security. This method operates via standard SSH to detect intruders without compatibility risks, avoids risky kernel hooks, and maintains system performance even in hardware constrained environments.

## The Shift in Critical Infrastructure Threats

At Sandfly, we work with many customers in the critical infrastructure space and frequently deal with unusual Operational Technology (OT) applications and hardware. OT infrastructure security is an interesting area because it almost always involves Linux, and it often involves systems that cannot go down for any reason. This is exactly the type of environment where agentless security like Sandfly excels.

In particular, OT security presents several significant challenges where traditional agent-based Linux EDR solutions have a tough time operating:

* They often run on custom Linux versions and hardware.
* They may be running older versions of Linux and are not updated regularly.
* They run on a mix of CPUs, ranging from standard x86 (Intel/AMD) to ARM, MIPS, PowerPC, and more.
* They are often left unmonitored, making them juicy targets for nation-state attackers.

Two of the most formidable threats currently active are Chinese state-sponsored groups dubbed Volt Typhoon and Salt Typhoon. They specialize in targeting and compromising OT infrastructure.

According to recent joint advisories from CISA, the NSA, and the FBI (advisory [AA25-239](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a)), these advanced persistent threat actors exhibit tactics that extend beyond traditional espionage. While Salt Typhoon focuses heavily on massive-scale data theft by exploiting telecommunications infrastructure, Volt Typhoon actively pre-positions itself within power grids, water treatment facilities, and communication networks. The CISA threat assessment indicates that this positioning is designed to enable disruptive or destructive cyberattacks during potential future geopolitical conflicts.

Both groups evade detection by targeting edge networks and exploiting the soft underbelly of OT environments: Linux-based embedded devices, legacy servers, and routing equipment. For security teams, protecting these environments creates a paradox. You need deep visibility to catch stealthy intruders, but traditional endpoint security tools are often too dangerous to install on varied, mission-critical OT systems.

## "Linux" is an Umbrella Term

At Sandfly, we have a tremendous amount of experience working in mission-critical and OT environments that run Linux. Here are three examples where we are trusted in extremely critical OT environments:

* [**Vay**](https://sandflysecurity.com/why-sandfly/case-studies/vays-remote-driving-fleet)**:** A teledriving vehicle company where Sandfly is used to monitor remotely driven vehicles operating on public roads where safety is paramount.
* [**Ericsson**](https://sandflysecurity.com/blog/ericsson-partners-with-sandfly-to-strengthen-telecom-security)**:** Trusted to protect their telecommunications customers and equipment globally.
* [**Car Manufacturer**](https://sandflysecurity.com/why-sandfly/case-studies/automotive-manufacturer-achieves-complete-linux-security-visibility)**:** Used on systems serving assembly lines for a major automobile manufacturer.

So when we talk about protecting OT systems, we are not just spewing marketing. Rather, we have practical, real-world experience watching some of the most important networking gear on the planet.

The primary challenge with protecting OT systems is that they rely heavily on Linux, and "Linux" is simply an umbrella term. Because the operating system is incredibly adaptable, a Linux deployment can be anything from a massive GPU cluster training an artificial intelligence model to a highly constrained embedded device in an IP camera or robot.

This extreme variety is where agent-based Endpoint Detection and Response (EDR) solutions reveal massive coverage gaps. While a traditional EDR vendor might claim they "support Linux," OT security teams must immediately ask the following critical questions:

* **Which distributions?** The ecosystem is deeply fragmented across dozens of commercial and open-source distributions.
* **Which kernel versions?** Thousands of unique Linux kernels exist, and OT vendors frequently compile custom kernels to suit highly specialized hardware.
* **Which CPU architectures?** While standard x86 processors dominate corporate servers, the smaller networking devices making up the OT edge rely heavily on ARM or MIPS architectures.
* **What are the resource costs?** This is the ultimate dealbreaker. Technologies like eBPF have solved some of the past kernel monitoring problems, but performance impacts still exist. We have repeatedly heard from customers that agents routinely consume 10% to 30% or more of system resources, which can immediately cripple or crash an OT system.

Sandfly can handle all of these scenarios, from cloud-based deployments down to a tiny Linux controller buried in a broom closet. Because agent-based systems cannot deploy across this wide range of hardware, many security teams are left with massive visibility gaps where attackers like Salt Typhoon and Volt Typhoon can infiltrate and remain undetected for extended periods. Sandfly aims to stop that because we are designed to watch everything reliably and leave no blind spots.

## What is "Living off the Land" and Why Do the Typhoons Use It?

Volt Typhoon and Salt Typhoon do not operate like typical hackers. When infiltrating a facility, they rarely drop noisy, recognizable malware files that trigger alarms. Instead, they utilize *Living off the Land* (LOTL). LOTL is a cyberattack technique where adversaries use legitimate, pre-installed administrative tools (like SSH, netcat, bash scripts, and more) to execute attacks, allowing them to evade traditional signature based malware detection. This is because these tools are not malware, but just being used maliciously.

Once these attackers compromise public facing edge devices with outdated firmware or weak credentials, they proxy their traffic to look like normal network activity. By hijacking legitimate system utilities, they blend in seamlessly with the daily activities of system administrators. Further, because they avoid introducing third party malware, traditional detection solutions may remain completely blind to their presence.

Finding these stealthy intruders requires analyzing system state and behavior, which typically demands EDR capabilities. However, bringing traditional EDR agents into an operational technology space introduces a severe set of risks that an agentless approach like Sandfly completely avoids.

## Why Does Traditional EDR Fail in OT Environments?

Operational Technology runs the physical world. A crashed workstation in a corporate IT environmen...