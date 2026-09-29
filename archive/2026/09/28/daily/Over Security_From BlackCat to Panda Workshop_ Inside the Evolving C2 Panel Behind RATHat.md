---
title: From BlackCat to Panda Workshop: Inside the Evolving C2 Panel Behind RATHat
url: https://www.cleafy.com/cleafy-labs/from-blackcat-to-panda-workshop-inside-the-evolving-c2-panel-behind-rathat
source: Over Security
date: 2026-09-28
fetch_date: 2026-09-29T07:41:17.563800
---

# From BlackCat to Panda Workshop: Inside the Evolving C2 Panel Behind RATHat

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Read more

d[![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Discover

NYX

Autonomous Fraud Operations

|

Autonomous AI investigation by Cleafy -

in minutes, not hours.

Learn More

Read more

d](https://nyx.cleafy.com/)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Read more

d

[![Cleafy Logo](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/6031121f255fb120fa9d4d05_Cleafy-logo.svg)](/)

* Solutions

  g

  [Fraud xDR](/platform)[Nyx](https://nyx.cleafy.com/)

  Resources

  [Documents](/resources/documents)[Insights](/resources/insights)[LABS report](/labs)[Webinars](/webinars)[Events](/events)
* [Who it's for](/industries)
* [LABS](/threat-intelligence)
* Resources

  g

  [Documents](/resources/documents)[Insights](/resources/insights)[LABS report](/labs)[Webinars](/webinars)[Events](/events)

  Resources

  [Documents](/resources/documents)[Insights](/resources/insights)[LABS report](/labs)[Webinars](/webinars)[Events](/events)
* Company

  g

  [About us](/about-us)[Careers](/careers)[Partners](/partners)[Press](/press)[News](/news)

  Company

  [About us](/about-us)[Careers](/careers)[Partners](/partners)[Press](/press)[News](/news)
* [Support](https://support.cleafy.com/)
* [Get in touch](/get-in-touch)

[Support](https://support.cleafy.com/)[Get in touch](/get-in-touch)

Malware-as-a-Service

Artificial Intelligence

ATS

RAT

# From BlackCat to Panda Workshop: Inside the Evolving C2 Panel Behind RATHat

###### Published:

###### 28/9/26

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDF  guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key Points

* RATHat's Android malware remained largely static from late 2025 to September 2026, while its **Command-and-Control (C2) panel was replaced entirely** and went through three generations in six months, rebranded from **BlackCat** to **Panda Workshop**.
* The panel works as a **complete malware factory**: it builds, signs, and publishes new samples from the console, **rebuilds them on a schedule** to evade hash-based detection, without the operator touching the hosting infrastructure.
* With a single click from the panel, the operator deploys a **native Go service** through the device's own wireless debugging, **gaining shell-level control** that sits outside the Android permission model, remains reachable through a **reverse tunnel,** and outlives the removal of the malicious app until reboot.
* Licensing controls and **nearly 100 separate deployments** since April 2026, used in parallel against Europe, LATAM, and South-Eastern Asia, are consistent with a **Malware-as-a-Service (MaaS) model** in which each affiliate runs a dedicated instance.
* **Gemini** is used on both sides of the operation: the malware **asks an LLM where to tap** when its automation fails on an unfamiliar phone, and the panel uses one to estimate victims' bank balances from their SMS.

### Executive Summary

RATHat is an Android banking trojan recently documented in [public reporting](https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts), distinguished by an architecture in which the malicious application is only the entry point. Once granted the Accessibility Service, the application enables **wireless debugging** on its own, pairs with the device's ADB daemon to **obtain a shell**, and uses it to stage a native Go service and an FRP client that opens a **reverse tunnel** to the operator. The service runs outside the application's process and permission model, keeps its own channel to the C2, and survives the removal of the application until the next reboot. A shell that the malware grants itself, rather than a permission the user grants the application, **is** **a model other families may adopt**, and security controls should extend to this scope.

The operation's visible investment, however, lies in its infrastructure. Samples from late 2025, February 2026, and the current campaigns share the same implant design with limited changes, while the operator **C2 panel was replaced entirely**. Three generations were recovered, all written in Simplified Chinese and live between April and September 2026: an unversioned first release self-identifying as **BlackCat**, followed by **Panda Workshop** V5 and V6. V5 renamed the entire API surface, introduced two-factor authentication for operators, and added an AI balance-scoring widget; V6 obfuscated the whole frontend, added a phishing download-page builder, and consolidated its AI features on Gemini. The panel builds, packs, signs and publishes new samples without the operator leaving the console, and can **regenerate its payload on a fixed schedule** to defeat hash-based detection. Account caps and role-gated sections exist to constrain the panel's own users, and pivoting on its frontend artifacts resolves the three generations to **nearly 100 separate deployments** since April 2026, nearly half on a single Singapore ASN. That footprint, together with parallel campaigns across Europe, LATAM, and South-Eastern Asia, is consistent with a **MaaS model**.

AI appears on both sides of the operation. The malware calls **Gemini models directly from the device**, with an API key embedded in its configuration, to locate on-screen controls when its static automation fails on unknown OEM skins or languages. The panel uses an LLM to extract bank balances from the collected SMS messages and to **score each device**. The device-side use deserves attention beyond this campaign: an LLM that reads the interface and returns the next action makes a **return of ATS**, without the per-target engineering that made it expensive, a scenario worth preparing for rather than a speculative one.

### Introduction

**RATHat** was recently documented in [public reporting](https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts) as an Android banking trojan distributed through malvertising and smishing against victims in Europe, LATAM and South-Eastern Asia. What separates it from a conventional Android RAT is that the Android application is only the entry point. Once the Accessibility Service is granted, the application drives the device through its own settings to enable **wireless debugging**, reads the pairing code off the screen and pairs with the local ADB daemon, **obtaining a shell on the phone**. It uses that shell to deploy a native **Go service**, executed outside the application's own process, and to stage an **FRP client** that opens a **reverse tunnel** to the operator's infrastructure.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/6aba2b6ac5c4fb977faa30ec_76753c13.png)

Figure 1 - RATHat Architecture

That architecture is not new to this campaign. The same design is present in samples distributed at the **end of 2025** under a crypto trading bot decoy, and in a February 2026 campaign using a "StripChat" decoy against South-Eastern Asia. Comparing those samples with the current ones shows how little the implant itself moved over the period. However, the infrastructure behind it did not follow the same pattern. The early samples connect to a panel **internally namedFisher**, which no longer serves any of the deployments associated with the recent campaigns: between February and September 2026 the operator console was rebranded, re-namespaced, hardened and extended with new capabilities across three successive generations, while the malware it controls stayed broadly the same.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/6aba2b6ac5c4fb977faa30e3_4e351bd1.png)

Figure 2 - Earlier Campaigns Delivering RATHat (February 2026)

This art...