---
title: Solving the 7777 Botnet enigma: A cybersecurity quest
url: https://www.sekoia.com/blog/solving-the-7777-botnet-enigma-a-cybersecurity-quest
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:03.368025
---

# Solving the 7777 Botnet enigma: A cybersecurity quest

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/solving-the-7777-botnet-enigma-a-cybersecurity-quest)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/solving-the-7777-botnet-enigma-a-cybersecurity-quest)

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

Solving the 7777 Botnet enigma: A cybersecurity quest

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

By

[TDR Team](/authors/threat-detection-research-team)

By

[Félix AIME](/authors/felix-aime)

By

[Pierre-Antoine DUCHANGE](/authors/pierre-antoine-duchange)

By

[Charles Meslay](/authors/charles-meslay)

By

[Grégoire CLERMONT](/authors/gregoire-clermont)

By

[Jérémy SCION](/authors/jeremy-scion)

July 23, 2024

# Solving the 7777 Botnet enigma: A cybersecurity quest

Discover 7777 botnet (aka Quad7) and its activity, targets, and use of TP-Link routers in Microsoft 365 attacks in our latest investigation.

![www.sekoia.com/blog/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6b400ea58101be5a0e5bd5_blog-botnet-7777-img-cover.webp)

## Key takeaways

* Sekoia.io investigated the mysterious 7777 botnet (aka. Quad7 botnet), published by the independent researcher Gi7w0rm inside the "The curious case of the 7777 botnet"\* blogpost.
* This investigation allowed us to intercept network communications and malware deployed on a TP-Link router compromised by the Quad7 botnet in France.
* To our understanding, the Quad7 botnet operators leverage compromised TP-Link routers to relay password spraying attacks against Microsoft 365 accounts without any specific targeting.
* Therefore, we link the Quad7 botnet activity to possible long term business email compromise (BEC) cybercriminal activity rather than an APT threat actor, even though certain mysteries remain regarding the exploits used to compromise the routers, the geographical distribution of the botnet and the attribution of this activity cluster to a specific threat actor.
* The insecure architecture of this botnet led us to think that it can be hijacked by other threat actors to install their own implants on the compromised TP-Link routers by using the Quad7 botnet accesses.

**Authors' Note**

This blog post is the first in a series of two on the Quad7 botnet. It introduces the topic by examining what lies behind compromised routers. If you want to learn more about other botnets operated by the same group, you can read the second post here: [**A glimpse into the Quad7 operators' next moves and associated botnets.**](/blog/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets)

\*You can also read "[The curious case of the 7777 botnet](https://gi7w0rm.medium.com/the-curious-case-of-the-7777-botnet-86e3464c3ffd)" blogpost.

## **Introduction**

On October 19, 2023, independent researchers [Gi7w0rm](https://x.com/Gi7w0rm) and [Dunstable Toblerone](https://x.com/DunstableToble1) published a blog post about **a botnet nicknamed the `Quad7` or `7777` botnet**, related to the TCP port 7777 opened on compromised devices displaying a mysterious xlogin: banner. This botnet is known in open source for deploying **Socks5 proxies on compromised devices to relay extremely slow “bruteforce” attacks against Microsoft 365 accounts** of many entities around the world.

At Sekoia.io, we have detected these attacks on 0.11% of our monitored Microsoft 365 accounts and have been tracking this botnet since our [Intrinsec](https://www.intrinsec.com) colleagues shared their findings with us. As this botnet was quite mysterious, targeting our customers and nobody had published on it since Gi7w0rm’s blog post, "[The Curious Case of the 7777 Botnet](https://gi7w0rm.medium.com/the-curious-case-of-the-7777-botnet-86e3464c3ffd)," we decided to investigate it.

This blog post will present the full investigation, our successes, and our failures, as it is always interesting to be transparent and provide feedback to the threat intelligence community and teams that may deal with similar IOT/SOHO threats in the future.

## **Are all of these compromised TP-Links?**

When we started our investigation on this threat, we began by examining what kind of assets had been compromised. This botnet is quite old and constantly evolving, with **the number of unique IP addresses involved dropping from 16,000 in August 2022, to ~7,000 in July 2024**. The geographic distribution of compromised devices is quite surprising, as Bulgaria remains the most infected country, followed by...