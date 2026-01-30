---
title: Meet IClickFix: a widespread WordPress-targeting framework using the ClickFix tactic
url: https://blog.sekoia.io/meet-iclickfix-a-widespread-wordpress-targeting-framework-using-the-clickfix-tactic/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-29
fetch_date: 2026-01-30T04:04:09.362342
---

# Meet IClickFix: a widespread WordPress-targeting framework using the ClickFix tactic

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Meet IClickFix: a widespread WordPress-targeting framework using the ClickFix tactic

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue, Amaury G. and Sekoia TDR](#molongui-disabled-link)
January 29 2026

0

19 minutes reading

***This post was originally distributed as a private FLINT report to our customers on 6 January 2026.***

## Table of contents

* [Introduction](#h-introduction)
* [Threat hunting of emerging adversary clusters](#h-threat-hunting-of-emerging-adversary-clusters)
  + [Tracking ClickFix clusters in the wild](#h-tracking-clickfix-clusters-in-the-wild)
* [From compromised WordPress to infected system](#h-from-compromised-wordpress-to-infected-system)
  + [IClickFix delivery stages](#h-iclickfix-delivery-stages)
  + [NetSupport RAT infection](#h-netsupport-rat-infection)
* [IClickFix’s spread in the wild](#h-iclickfix-s-spread-in-the-wild)
  + [Compromised WordPress worldwide](#h-compromised-wordpress-worldwide)
  + [Historical data](#h-historical-data)
* [Conclusion](#h-conclusion)
* [IoCs & Technical details](#h-iocs-amp-technical-details)
  + [IoCs](#h-iocs)
  + [YARA rules](#h-yara-rules)
* [External references](#h-external-references)

## Introduction

In November 2025, during our threat hunting routine for unveiling emerging adversary clusters, **TDR analysts identified a widespread malware distribution campaign** leveraging the **ClickFix** social engineering tactic through a **Traffic Distribution System** (TDS).

This cluster uses a malicious JavaScript framework injected into **compromised WordPress** sites to display the ClickFix lure and deliver NetSupport RAT. Because the initial JavaScript includes the distinctive HTML tag `ic-tracker-js`, we named the malicious framework “***IClickFix***”.

Historical analysis of *IClickFix* reveals that this cluster has been active since at least December 2024, **compromising over 3,800 WordPress sites**. As reported by the Walmart Global Tech security team[1](#17ef1e98-3956-4a4e-9535-ef4ef7ed40bc), this cluster uses a Traffic Distribution System (TDS) to redirect selected visitors and deliver the next-stage payload, enhancing *IClickFix*’s stealth.

TDR analysts first encountered this ClickFix cluster in February 2025, when it was in its early stages. We observed it distributing Emmenhtal Loader, which ultimately downloaded XFiles Stealer. At that time, *IClickFix* had not yet reached sufficient scale to warrant an in-depth analysis.

Like the ClearFake threat[2](#c4d71ffe-6428-48eb-9f1c-1d205d0bc5ee), ***IClickFix* employs a multi-stage JavaScript loader** that presents a fake Cloudflare Turnstile CAPTCHA challenge using the ClickFix social engineering tactic. The ClickFix command, once copied into the victim’s clipboard, executes a PowerShell command that downloads and executes an obfuscated PowerShell script, ultimately dropping NetSupport RAT.
This report provides a technical analysis of the persistent *IClickFix* framework, the adversary’s infrastructure, and its technical evolution throughout 2025.

## Threat hunting of emerging adversary clusters

In November 2025, we unveiled the *IClickFix* framework and its associated infrastructure using two distinct threat hunting methodologies:

* An internal tool designed to **detect watering hole attacks** across thousands of monitored websites belonging to strategic organisations in government, defense, energy, telecom, and other verticals.
* Generic YARA rules deployed on scanning platforms to **detect pages employing** the **ClickFix** social engineering tactic.

### Exposing watering hole attacks

In late 2025, Sekoia TDR analysts **deployed a new capability for detecting watering hole attacks**.

A **watering hole attack** is a strategic attack where operators compromise a legitimate website known to be frequented by a specific target group, effectively ambushing users who visit the trusted source. This tactic is often leveraged by **state-sponsored actors** to conduct espionage against specific sectors (like defense or finance) by targeting a distinct community of interest, but also serves as a potent vector for broader **cybercrime operations**.

When our monitoring began in November, the Ghanaian Allied Health Professions Council government WordPress website `ahpc.gov[.]gh` was flagged after the main page includes a malicious JavaScript snippet that interacts with the URL `hxxps://ototaikfffkf[.]com/fffa.js`, registered a few months earlier.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/01/image-8-997x1024.png)

*Figure 1. Screenshot of the Ghanaian Allied Health Professions Council compromised website*

Although the initial indicators suggested a targeted watering‑hole, we quickly observed the same JavaScript snippet across multiple unrelated websites spanning different sectors and countries. This pattern indicates a mass distribution rather than a targeted approach against the government in Ghana.

### Tracking ClickFix clusters in the wild

Sekoia TDR analysts actively track pages that implement the ClickFix social engineering tactic, given its widespread adoption by cybercriminals and nation-state-sponsored threat groups. In particular, we have developed generic YARA rules detecting ClickFix pages, using keywords, resource patterns, and JavaScript functions.

By November 2025, while analysing detection results from the urlquery scanning service[3](#606da113-8bda-4ea3-9900-05361a339c3a), one of these rules triggered alerts for resources retrieved from multiple scanned URLs. The detected resources consisted of HTML pages, served by the malicious framework and containing ClickFix-related strings, including:

```
Verify you are human
please follow these steps
<b>Ctrl + V</b>
<b>Win + R</b>
Pr...