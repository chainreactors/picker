---
title: Exploring the Benefits of MITRE ATT&CK in Sekoia SOC Platform
url: https://www.sekoia.com/blog/how-sekoia-io-uses-the-mitre-attck-framework-to-enhance-soc-capabilities
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:02.852991
---

# Exploring the Benefits of MITRE ATT&CK in Sekoia SOC Platform

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/how-sekoia-io-uses-the-mitre-attck-framework-to-enhance-soc-capabilities)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/how-sekoia-io-uses-the-mitre-attck-framework-to-enhance-soc-capabilities)

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

How Sekoia uses the MITRE ATT&CK framework to enhance SOC capabilities

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

[SOC Insights & Other News](/category/soc-insights-other-news)

[Integrations](/category/integrations)

By

[Fabien DOMBARD](/authors/fabien-dombard)

July 3, 2024

# How Sekoia uses the MITRE ATT&CK framework to enhance SOC capabilities

At Sekoia, the integration of the MITRE ATT&CK framework into our Security Operations Center (SOC) platform is a cornerstone of our approach to cybersecurity. The ATT&CK framework serves as a comprehensive knowledge base of cyber adversary behaviours.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7dbd6cac9e5521ddda8a_ai-generated-7999383_1280.webp)

## Key takeaways

Sekoia explains how it maps its detection rules and data sources to the MITRE ATT&CK framework to strengthen SOC coverage.

* Sekoia uses the MITRE ATT&CK framework as a cornerstone of its SOC platform and detection approach.
* ATT&CK catalogues adversary tactics and techniques, supporting threat modelling, coverage assessment and threat hunting.
* Sekoia maps its catalogue of around 900 Sigma rules to ATT&CK techniques to reveal coverage and gaps.
* Each data source, or intake, is also mapped to ATT&CK, with the mappings published on GitHub and in the documentation.
* The post notes ATT&CK only covers known techniques, so Sekoia adds machine learning to surface undocumented threats.

This blogpost is part of a series of articles covering our vision of cybersecurity and analyzing the benefits of SOC platforms for modern organizations.

At Sekoia.io, the integration of the MITRE ATT&CK framework into our Security Operations Center (SOC) platform is a cornerstone of our approach to cybersecurity. The ATT&CK framework serves as a comprehensive knowledge base of cyber adversary behavior and a taxonomy for adversarial actions across their lifecycle. It consists of two main parts: ATT&CK for Enterprise, which covers behaviors against enterprise IT networks and cloud environments, and ATT&CK for Mobile, focusing on behaviors against mobile devices. By meticulously evaluating this framework, we ensure that our defenses are not only comprehensive but also relevant to our clients' unique needs. This method offers substantial benefits, providing a broad perspective on potential threats while aligning with industry standards. Let’s see why and how.

## What is the MITRE ATT&CK framework?

The MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) framework is a comprehensive matrix that catalogs the tactics and techniques employed by cyber adversaries. It was originally developed by the U.S. Department of Homeland Security in collaboration with the MITRE Corporation in 2015 as an open reference standard to help all defenders improve their security postures against modern adversaries in cyberspace. Indeed, this framework is pivotal for threat modeling and enhancing security defenses, enabling organizations to understand the security risks linked to specific threats and refine their detection and prevention strategies. On the [official MITRE ATT&CK Framework page](https://attack.mitre.org/matrices/enterprise/), you'll find this extensive matrix.

![Mittre Att&ck framework](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b1fc97352943877fc9_6a92a29adae089660dfc2e73_6a2a7dbf6cac9e5521dddc0d.webp)

Mittre Att&ck framework

The top horizontal columns of the matrix outline various Tactics, beginning with Initial Access, Execution, Persistence, among others. Each tactic is linked to documented techniques, which are derived from observations of different Adversary Groups, as shared by cybersecurity researchers in threat intelligence reports.

The MITRE ATT&CK framework serves multiple purposes, including:

* Enhancing existing detection technologies within an organization.
* Assessing an organization's visibility against potential attacks.
* Strengthening the organization’s current threat intelligence capabilities.
* Facilitating adversary simulations between Red and Blue Teams to identify weaknesses.
* Advancing the maturity of an organization’s Threat Hunting Program.

It’s essential to understand that the tactics and techniques documented in the MITRE ATT&CK matrix represent knowledge that...