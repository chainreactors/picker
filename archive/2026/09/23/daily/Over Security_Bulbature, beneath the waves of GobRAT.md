---
title: Bulbature, beneath the waves of GobRAT
url: https://www.sekoia.com/blog/bulbature-beneath-the-waves-of-gobrat
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:05.125846
---

# Bulbature, beneath the waves of GobRAT

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/bulbature-beneath-the-waves-of-gobrat)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/bulbature-beneath-the-waves-of-gobrat)

[fr](/fr)

Solutions

Tailored cybersecurity built for your specific challenges and industry

By Use Case

[SIEM replacement](/solutions/siem-replacement)[Stack integration](/solutions/cybersecurity-stack-integration)[Continuous threat detection](/solutions/real-time-threat-detection)[Automated incident response](/solutions/automated-incident-response)[Alert fatigue relief](/solutions/reduce-alert-fatigue)

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

CTI](/platform/intelligence)[Sekoia Reveal

CAASM](/platform/reveal)[Sekoia Elevate

AI SOC agents](/platform/elevate)

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

[Home](/)[Blog](/blog)

Bulbature, beneath the waves of GobRAT

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

Share

Copied !

[Threat Research & Intelligence](/category/threat-research-intelligence)

[TDR Team](/category/tdr)

[APT](/category/apt)

By

[TDR Team](/authors/threat-detection-research-team)

By

[Amaury-Jacques GARÇON](/authors/amaury-jacques-garcon)

By

[Félix AIME](/authors/felix-aime)

October 2, 2024

# Bulbature, beneath the waves of GobRAT

Since mid 2023, Sekoia Threat Detection & Research team (TDR) investigated an infrastructure which controls compromised edge devices transformed into Operational Relay Boxes used to launch offensive cyber attack.

![Hooded developer with a panda logo working at a multi-monitor workstation against a glowing digital globe.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaab09c946bbc1a18344f12_blog-bulbature-img-cover.webp)

## Key takeaways

Sekoia TDR maps the GobRAT and Bulbature infrastructure that turns edge devices into relay boxes for offensive operations.

* Since mid-2023 Sekoia TDR has tracked an infrastructure of 63 servers controlling compromised edge devices turned into relay boxes.
* Infected devices download two malwares from staging servers: the GobRAT backdoor and the previously undocumented Bulbature implant.
* GobRAT offers full RAT features and relays DDoS and exploitation attacks, while Bulbature turns devices into on-demand proxies.
* Recovered admin panels let operators run brute-force, web-exploit and DDoS campaigns and generate rotating proxy tunnels.
* A July 2023 export listed nearly 75,000 relay boxes, most US-based Asus or Qnap routers, and Sekoia attributes the threat to China.

## Key Takeaways

* Since mid 2023, Sekoia Threat Detection & Research team (TDR) investigated an infrastructure which controls compromised edge devices transformed into Operational Relay Boxes used to launch offensive cyber attack.

* The infrastructure has constantly evolved with a total of 63 servers identified and analysed, and is still operating at the time of publication of this report.

* On some servers, it is possible to find installation scripts as well as the GobRAT and Bulbature malware. Other servers provide a view of the administration interface used to manage compromised hosts and launch attacks.

* Several traces lead us to suggest that this infrastructure might be used by several operators originating from China.

## Context

On 9 October 2023, the Threat Detection & Research (TDR) team published a private report regarding an **attack campaign on edge devices** also documented by the [JPCERT/CC](https://blogs.jpcert.or.jp/en/2023/05/gobrat.html) on 29 May 2023. Since then, **the network infrastructure has remained active** and dozens of new hosts were deployed with the same characteristics as those initially identified. These hosts are monitored via the Sekoia C2 Tracker project and are capitalised within the Sekoia Intelligence Center (IC).

In our 2023 report, we assessed that this infrastructure was very likely used to support operations of multiple intrusion sets, likely of Chinese origin, due to certain traces attributing the attacks and the victimology observed, which mainly included **edge devices transformed into Operational Relay Boxes (ORB).** For some years now, we observe that China uses **edge devices as ORB to conduct offensive cyber campaigns**, as previously reported in link with the [Quad7 operator](https://blog.sekoia.io/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets/) or the [APT31 infrastructure](https://blog.sekoia.io/walking-on-apt31-infrastructure-footprints/). Although there was few open source information on GobRAT, TDR decided to investigate this threat in depth.

This investigation is still in progress as of October 2024, and we will focus on **highlighting the infrastructure** and **the different types of hosts** identified. The cut-off date for indicators included in this report is 5 September 2024.

## **Initial findings**

The initial findings came from a self-signed certificate that was used on a staging host identified by the JPCERT/CC:

|  |  |
| --- | --- |
| **Subject DN** | C=AU, ST=Some-State, O=Internet Widgits Pty Ltd |
| **Issuer DN** | C=AU, ST=Some-State, O=Internet Widgits Pty Ltd |
| **Serial Number** | Decimal: 587046745646849621397962336094648657285118811505 |
| **Validity Period** | 2021-...