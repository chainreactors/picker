---
title: Emulating and Detecting Scattered Spider-like Attacks
url: https://www.sekoia.com/blog/emulating-and-detecting-scattered-spider-like-attacks
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:03.538097
---

# Emulating and Detecting Scattered Spider-like Attacks

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/emulating-and-detecting-scattered-spider-like-attacks)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/emulating-and-detecting-scattered-spider-like-attacks)

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

Emulating and Detecting Scattered Spider-like Attacks

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

[Detection Engineering](/category/detection-engineering)

[TDR Team](/category/tdr)

[Cybercrime](/category/cybercrime)

[Cloud](/category/cloud-security)

[Phishing](/category/phishing)

By

[TDR Team](/authors/threat-detection-research-team)

By

[Guillaume COUCHARD](/authors/guillaume-couchard)

By

[Erwan CHEVALIER](/authors/erwan-chevalier)

July 24, 2024

# Emulating and Detecting Scattered Spider-like Attacks

Explore a use-case scenario demonstrating how to detect scattered spider attacks in AWS environments and enhance your cloud security.

![Conceptual cybersecurity graphic illustrating cyber attacks versus defense with shields, padlocks, and threat icons.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaab748f8704cf2417dd12d_blog-emulating-and-detecting-scattered-spider-img-cover.webp)

## Key takeaways

Sekoia and Mitigant emulate and detect Scattered Spider-like attacks in AWS to demonstrate a Threat-Informed Defense strategy.

* Sekoia TDR and Mitigant show how to detect Scattered Spider-like attacks in AWS using a Threat-Informed Defense strategy.
* The approach combines three pillars: Sekoia Defend for detection, Sekoia Intelligence for CTI and Mitigant for attack emulation.
* A seven-stage AWS kill chain is emulated, from phishing-based initial access to malicious S3 replication for data theft.
* Sekoia rules catch high-signal events like serial console access and password policy changes, tied to MITRE ATT&CK techniques.
* For noisy events such as CreateUser or Lambda access, customers are better placed to write tailored rules using their own context.

*Written by* [*Mitigant*](https://www.mitigant.io/) *(Kennedy Torkura) and Sekoia Threat Detection and Research (TDR) team (Erwan Chevalier and Guillaume Couchard).*

## Introduction

Enterprises are increasingly using cloud infrastructure to take advantage of its underlying benefits. Unlike traditional data centres, cloud infrastructure affords business agility at a cheaper cost. Consequently, several organisations are migrating workloads to the cloud. However, cybercriminals have also noticed this trend and have started targeting cloud workloads.

Defending cloud infrastructure is more complex than defending on-premises infrastructure. Enterprises often need support with interpreting and implementing the appropriate security controls that align with the shared security responsibility model, significantly for threat detection and response. One approach to address this gap is to leverage third-party products that provide effective cloud threat detection and response.

![Emulating and Detecting Scattered Spider-like Attacks on AWS](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaab7a480002cd083fdfc60_Emulating%20and%20Detecting%20Scattered%20Spider-like%20Attacks%20on%20AWS.webp)

Emulating and Detecting Scattered Spider-like Attacks on AWS

## Aim of This Article

This article provides a use-case scenario demonstrating how defenders can address detection gaps in AWS environments. This will be achieved by combining [Mitigant Cloud Attack Emulation](https://www.mitigant.io/en/platform/cloud-attack-emulation) and the Sekoia Security Operations Center (SOC) Platform. Furthermore, this article discusses how organisations can adopt a Threat-Informed Defense strategy by combining security measures, Cyber Threat Intelligence, and evaluation/testing. This strategy enables organisations to detect and respond effectively to threats lurking in their AWS infrastructure. We provide details of how Extended Detection and Response (XDR) and adversary emulation can be synergized to defend against malicious threat actors.

## Threat Scenario

To demonstrate the importance of using a combined approach of a SOC Platform and adversary emulation, a threat scenario has been formulated based on a real-life attack observed by the Sekoia platform. The scenario is based on real events that emulate the Scattered Spider threat actor. It also demonstrates the effectiveness of leveraging a Threat-Informed Defense Strategy (TIDS).

The Scattered Spider threat actor is a cyber-criminal gang that has become notorious recently. Scattered Spider targets financial institutions, telecommunication organisations, and tech...