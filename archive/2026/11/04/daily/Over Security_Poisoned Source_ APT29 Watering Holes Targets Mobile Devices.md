---
title: Poisoned Source: APT29 Watering Holes Targets Mobile Devices
url: https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits
source: Over Security
date: 2026-11-04
fetch_date: 2026-11-05T08:44:58.029617
---

# Poisoned Source: APT29 Watering Holes Targets Mobile Devices

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits)

[fr](/fr)

Solutions

Tailored cybersecurity built for your specific challenges and industry

By Use Case

[Self-hosted deployment](/solutions/self-hosted)[SIEM replacement](/solutions/siem-replacement)[Stack integration](/solutions/cybersecurity-stack-integration)[Continuous threat detection](/solutions/real-time-threat-detection)[Automated incident response](/solutions/automated-incident-response)[Alert fatigue relief](/solutions/reduce-alert-fatigue)

By Vertical

[Healthcare](/solutions/healthcare)[Technology](/solutions/technology)[Energy & Utilities](/solutions/energy-utilities)[Government](/solutions/government)[Manufacturing](/solutions/manufacturing)[MSSP](/solutions/mssp)

Platform

Give your analysts their time back

UNIFIED Platform

[Autonomous SOC Platform](/platform)[Cyber Threat Intelligence](/platform/intelligence)

PLATFORM IntegrationS

[Integrations catalog](/integrations)

Products

[Sekoia Defend

SIEM](/platform/defend)[Sekoia Intelligence

CTI](/platform/intelligence)[Sekoia Digital Risk

DRP](/platform/digital-risk)[Sekoia Reveal

CAASM](/platform/reveal)[Sekoia Elevate

Agentic SOC analyst](/platform/elevate)

See Sekoia in action

Curious about what our platform can do? Take a self-guided tour and explore the features that security teams rely on.

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)

Partners

Join a powerful ecosystem of cyber experts, continuous training, and shared success

Partners

[Our business partners](/our-business-partners)[Why become a partner?](/why-become-a-business-partner)[Partner portal](https://sekoia.introw.io/)

Services

[Training courses](/training-courses)[Sekoia university](https://training.sekoia.com/account/login/)

Join our business partner ecosystem

Grow your business alongside Sekoia. Join a thriving network of partners and unlock new revenue opportunities in cybersecurity.

[Become a partner](/become-a-partner)

Why Sekoia?

Our story, our world-class team, and our latest updates

About us

[About Sekoia](/about)[About TDR team](/about-threat-detection-research-team)[Customer reviews](/our-customers)[Join us](/join-us)

Newsroom

[Newsroom](/newsroom)[Brand kit](https://share.sekoia.com/s/MH3CJ6Q8o5BC6Q6)

Resources

Deepen your cyber knowledge with expert insights, reports, and real-world case studies

Blog

[Blog](/blog)

glossary

[Cyberglossary](/glossary)

Resource center

[Case studies](/resources-category/case-studies)[Solution briefs](/resources-category/solution-briefs)[Webinars](/resources-category/webinars)[Reports](/resources-category/reports)

[View all](/resources)

Stay ahead of cyber threats

Get the latest insights on threat intelligence, SOC best practices and Sekoia product updates delivered straight to your inbox.

[Subscribe](https://go.sekoia.com/Preference-center-EN.html)

Clear

Solutions

Platform

Integrations

Partners

Company

Newsroom

Blog

Glossary

Case studies

Solution briefs

Webinars

Reports

Others

Recommended

![]()

The new era of cybersecurity: AI-guided SOC and human-machine collaboration.

The new era of cybersecurity: AI-guided SOC and human-machine collaboration.✕

Show more

![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)![](https://cdn.prod.website-files.com/69aaa27bc8027f082ae84b86/6ab62024f7d63abe309a94fd_search-placeholder.svg)

Recent

Recommended

[Home](/)[Blog](/blog)

Poisoned Source: APT29 watering holes target mobile devices with n-day exploits

All categories & topics

[Threat Research & Intelligence](/category/threat-research-intelligence)

[Detection Engineering](/category/detection-engineering)

[SOC Insights & Other News](/category/soc-insights-other-news)

[Product News](/category/product-news)

[TDR Team](/category/tdr)

[AI](/category/ai-security)

[Cloud](/category/cloud-security)

[Integrations](/category/integrations)

[Compliance](/category/compliance)

[APT](/category/apt)

[Cybercrime](/category/cybercrime)

[Phishing](/category/phishing)

[Ransomware](/category/ransomware)

[Stealer](/category/stealer)

[ClickFix](/category/clickfix)

Summarize with AI

Share

Copied !

[Threat Research & Intelligence](/category/threat-research-intelligence)

[TDR Team](/category/tdr)

[APT](/category/apt)

25 min

November 4, 2026

By

[Amaury Garçon](/authors/amaury-jacques-garcon)

By

[Félix AIME](/authors/felix-aime)

By

[Robin Kwiatkowski](/authors/robin-kwiatkowski)

By

[TDR Team](/authors/threat-detection-research-team)

# Poisoned Source: APT29 watering holes target mobile devices with n-day exploits

Sekoia TDR investigates a large-scale APT29 watering hole campaign targeting iOS and Android users through compromised websites, fake domains, and a supply-chain attack. Discover how n-day exploits were used to steal cookies, Wi-Fi passwords, and device data.

![A bear peers above the surface of a misty forest lake, surrounded by glowing blue digital circuit patterns and smartphones held at the water’s edge.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6ae4d5177632391ddde0a6a0_blog-flint-2026-047-poisoned-source.webp)

## Key takeaways

Sekoia TDR investigates a large-scale APT29 watering hole campaign targeting iOS and Android users through compromised websites, fake domains, and a supply-chain attack. Discover how n-day exploits were used to steal cookies, Wi-Fi passwords, and device data.

* Sekoia TDR identified a large-scale watering hole campaign using three infection vectors: compromised legitimate websites, Adversary-in-the-Middle-like impersonating high-profile websites, and a compromise of a Ukrainian web analytics service.
* The injected Javascript code collects browser and device attributes. Then, the delivery infrastructure delivers a platform-specific n-day exploit chain targeting either iOS or Android.
* The final payloads aim to steal browser cookies, and in some cases, Wi-Fi passwords or full mobile device data. This collection is consistent with intelligence-gathering objectives and may allow the intrusion set to reuse authenticated sessions and access browser-based services, including webmail accounts.
* Based on technical overlaps, operational patterns, victimology and infrastructure, we assess with moderate to high confidence that this campaign was conducted by APT29, a Russian nexus intrusion set widely attributed to the Foreign Intelligence Service of the Russian Federation (SVR).
* Sekoia TDR team is coordinating with the CERTs of affected countries to support victim identification and assess options for disrupting the watering hole infrastructure.

## Introduction

In mid-October 2026, Sekoia's Threat Detection & Research (TDR) team uncovered a **large-scale watering hole campaign** involving the compromise or the **cloning** of several high-profile websites in the US, Ukraine, Czech Republic, and Bulgaria. In parallel, we assess that the intrusion set carried out a supply-chain compromise of a **Ukrainian web analytics service**, exp...