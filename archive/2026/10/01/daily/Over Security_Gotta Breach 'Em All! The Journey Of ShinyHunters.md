---
title: Gotta Breach 'Em All! The Journey Of ShinyHunters
url: https://www.sekoia.com/blog/gotta-breach-em-all-the-journey-of-shinyhunters
source: Over Security
date: 2026-10-01
fetch_date: 2026-10-02T07:49:28.024522
---

# Gotta Breach 'Em All! The Journey Of ShinyHunters

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/gotta-breach-em-all-the-journey-of-shinyhunters)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/gotta-breach-em-all-the-journey-of-shinyhunters)

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

Gotta breach 'em all! The journey of ShinyHunters

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

[Cybercrime](/category/cybercrime)

By

[Enzo Saez](/authors/enzo-saez)

By

[TDR Team](/authors/threat-detection-research-team)

By

[Robert (Bobby) Venal](/authors/robert-bobby-venal)

October 1, 2026

# Gotta breach 'em all! The journey of ShinyHunters

ShinyHunters has outlasted forum takedowns, multiple arrests, and its own founders' convictions. This report traces six years of activity and tactical evolution. From stolen S3 buckets to zero-day exploits, we attempted to explain why the brand keeps surviving what should have ended it.

![Pixel-art illustration of a cyberattack marketplace: hackers sell “shiny stolen records” and fictional creatures for exorbitant prices while a monitor displays “data breach in progress,” stolen user account and payment information, and frightened victims confront the attackers.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aba6efce1a4c13e52feff3e_blog-gotta-breach-em-all-the-journey-of-shinyhunters-img-cover.webp)

## Key takeaways

Co-authored by Sekoia and Beazley Security, this report traces six years of ShinyHunters' activity with first-hand incident response from a 2026 Oracle PeopleSoft compromise.

* ShinyHunters now spans multiple distinct clusters operating under one shared name, which is why the brand has survived years of arrests and indictments that took out individual members.
* Each year's targeting has tracked whatever access method was cheapest to exploit at scale. S3 buckets and GitHub tokens, Snowflake accounts lacking MFA, OAuth-abused Salesforce integrations and PeopleSoft zero-day.
* The group's publicized breach figures have repeatedly outstripped what victim companies ultimately confirm, meaning every claim warrants independent verification.
* The group's apparent shift from APAC/India toward the US and Western Europe isn't a strategic choice, but a byproduct of which platforms or flaws it was exploiting at the time. The one exception being France, where 2025 arrests exposed victims tied directly to the operators' own nationality.

## Introduction

Sekoia’s Threat Detection & Research (TDR) team has been actively tracking ShinyHunters for several months. Today, ShinyHunters is best understood not as a fixed gang but as **a financially motivated data theft and extortion brand**. A group that has persisted since 2020 across changing membership, surviving multiple arrests and forum seizures along the way.

The name comes from the Pokémon community, where "shiny hunters" are dedicated gamers whose purpose is to find rare color variant ("shiny") Pokémon, like their early forum avatar which was **a shiny Umbreon**. In that context, could shiny hunting be working through targets methodically until something rare and valuable surfaces? Personally identifiable information (PII), credentials, and extensive user databases align with this framework.

![Screenshot of a ShinyHunters forum profile showing an enlarged avatar depicting a blue, fox-like fantasy creature with glowing markings and stars.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aba707e8a86fceb5f9b27f8_blog-shinyhunters-forums-avatar.webp)

ShinyHunters' forums avatar

In practice, the group, today, functions as a decentralized network of threat clusters operating under a common alias. We assess with high-confidence their link with "[**The Com**](https://www.youtube.com/watch?v=TydZRumQUj8)", the broader cybercrime community that also includes **Scattered Spider** and **Lapsus$**, an association that became explicit in 2025 with the formation of **Scattered Lapsus$ Hunters**. Their modus operandi remains consistent throughout: obtain valid credentials or access, exfiltrate bulk data, then monetize the breach through extortion or illicit sales. **What has changed over time is *how* they get access**. The evolution of this threat actor is defined by a clear progression in their access methodologies:

* Early phase: Traditional phishing and large-scale forum credentials dumps.
* Transition phrase: Exploitation of infostealer data targeting cloud infrastructure lacking Multi...