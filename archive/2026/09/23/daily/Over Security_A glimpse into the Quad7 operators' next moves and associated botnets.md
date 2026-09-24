---
title: A glimpse into the Quad7 operators' next moves and associated botnets
url: https://www.sekoia.com/blog/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:03.880547
---

# A glimpse into the Quad7 operators' next moves and associated botnets

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets)

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

A glimpse into the Quad7 operators' next moves and associated botnets

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

September 9, 2024

# A glimpse into the Quad7 operators' next moves and associated botnets

Uncover the secrets of the Quad7 botnet and its ever-evolving toolset. Learn about the new backdoors and protocols used by these operators.

![Illustration of a router emitting a network of light beams surrounded by monitoring screens](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6b400ea58101be5a0e5bd5_blog-botnet-7777-img-cover.webp)

## Key takeaways

* The Sekoia TDR team has recently identified new staging servers, leading to the discovery of additional targets, implants, and botnet clusters tied to the Quad7 operators.
* The Quad7 botnet operators seem to be compromising several brands of SOHO routers and VPN appliances, including TP-LINK, Zyxel, Asus, Axentra, D-Link, and Netgear, using multiple vulnerabilities—some of which are previously unknown.
* The Quad7 botnet operators appear to be evolving their toolset, introducing a new backdoor and exploring new protocols, with the aim of enhancing stealth and evading the tracking capabilities of their operational relay boxes (ORBs).
* Given these developments, it is possible that without interception capabilities, tracking the evolution of Quad7 botnets could become nearly impossible in the near future.

**Authors' Note**

This blog post is the second in a series of two on the Quad7 botnet. It presents the botnets operated by the Quad7 operators and deduce their possible next moves. However, if you are new on this topic, you can read the first blog post here: [Solving the 7777 Botnet enigma: A cybersecurity quest](/blog/solving-the-7777-botnet-enigma-a-cybersecurity-quest)

## **Introduction**

Previously, we detailed our investigation on the Quad7 botnet and our live forensic methodology against a TP-LINK router to get related implants on it. Following this first publication, we continued to track this botnet activity and new clusters related to the Quad7 botnet operators.

Before our blogpost on the Quad7 botnet, we started to monitor another botnet, the alogin botnet (aka 63256 botnet) and attributed this botnet to the Quad7 botnet operators with medium confidence. On 7 August 2024, Team Cymru published a [blogpost](https://www.team-cymru.com/post/botnet-7777-are-you-betting-on-a-compromised-router) confirming the two botnets were operated by the same group as they shared some common administration servers.

Recently, we came across several staging servers, leading us to discover **new targets**, **implants** and **botnet clusters** associated with this threat actor. This new discovery allows us to have a glimpse of the Quad7 next moves as it seems that the operators are developing **HTTP reverse shells** and test **new projects** to relay their attacks instead of using simple **open socks proxies** to be more stealthy and prevent tracking.

## **The wildcard login galaxy**

As of this writing, we are aware of five different \*login clusters linked to this threat actor (**alogin**, **xlogin**, **axlogin**, **rlogin** and **zylogin**), which we are temporarily referring to internally as the **Quad7 Botnet Operators**.

The Quad7 botnet (aka 7777 botnet, **xlogin** botnet) is a botnet composed of compromised **TP-Link routers** which have both TCP ports TELNET/7777 and 11288 opened. The 7777 port is the administration port hosting a bind shell with root privileges (xlogin). This bind shell is password protected. The 11288 port is the Socks5 proxy port, mostly password protected, and this proxy is used to relay **M365 accounts brute force attacks**.

The **alogin** botnet is a botnet composed of compromised **Asus routers** which have both TCP ports 63256 and 63260 opened. The TELNET/63256 port is the administration port hosting a bind shell with root privileges (alogin). This bind shell is also password protected. The SOCKS/63260 port is hosting a password protected S...