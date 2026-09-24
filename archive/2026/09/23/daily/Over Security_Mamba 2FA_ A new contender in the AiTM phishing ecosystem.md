---
title: Mamba 2FA: A new contender in the AiTM phishing ecosystem
url: https://www.sekoia.com/blog/mamba-2fa-a-new-contender-in-the-aitm-phishing-ecosystem
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:05.315633
---

# Mamba 2FA: A new contender in the AiTM phishing ecosystem

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/mamba-2fa-a-new-contender-in-the-aitm-phishing-ecosystem)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/mamba-2fa-a-new-contender-in-the-aitm-phishing-ecosystem)

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

Mamba 2FA: A new contender in the AiTM phishing ecosystem

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

[Cybercrime](/category/cybercrime)

[Phishing](/category/phishing)

By

[Grégoire CLERMONT](/authors/gregoire-clermont)

By

[TDR Team](/authors/threat-detection-research-team)

October 7, 2024

# Mamba 2FA: A new contender in the AiTM phishing ecosystem

Discover Mamba 2FA, a previously unknown adversary-in-the-middle (AiTM) phishing kit, sold as phishing-as-a-service (PhaaS).

![Striped snake surrounded by email envelopes on a digital grid landscape.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aad4c2ba1a97a8098005642_blog-mamba-2fa-a-new-contender-img-cover.webp)

## Key takeaways

Sekoia TDR uncovers Mamba 2FA, an Adversary-in-the-Middle phishing-as-a-service kit targeting Microsoft 365 accounts.

* Mamba 2FA is an Adversary-in-the-Middle phishing kit targeting Microsoft 365, sold as a service since at least March 2024.
* Phishing pages use the Socket.IO library to relay credentials and MFA inputs to a backend in real time.
* It offers OneDrive, SharePoint, generic sign-in and voicemail templates and reflects an organisation's custom branding.
* Stolen credentials and cookies are sent instantly to the attacker through a Telegram bot at $250 for 30 days.
* The infrastructure splits into rotating link domains and longer-lived relay servers, now hidden behind commercial proxies.

## Introduction

In late May 2024, Sekoia’s Threat Detection & Research (TDR) team received an insight from a partner about an ongoing phishing campaign leveraging HTML attachments that mimicked [Microsoft 365](/blog/userauthenticationmethod-microsoft-365-decode) login pages. The phishing pages were able to relay some methods of multi-factor authentication (MFA), and made use of the Socket.IO JavaScript library to communicate via websockets with a backend server. At first, these characteristics look like [the *Tycoon 2FA* phishing-as-a-service platform](/blog/tycoon-2fa-an-in-depth-analysis-of-the-latest-version-of-the-aitm-phishing-kit), but further inspection found that the campaign leveraged **a previously unknown adversary-in-the-middle (AiTM) phishing kit**, that Sekoia track as ***Mamba 2FA***.

TDR illuminated the infrastructure hosting the phishing pages and developed detection rules to identify Entra ID accounts compromised via this kit. Retro-hunting uncovered that several Sekoia XDR customers have been targeted by campaigns leveraging *Mamba 2FA* in the previous months, suggesting a **widespread threat**. Finally, during this investigation we identified that the kit was **sold as** [**phishing-as-a-service**](/blog/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1) **(PhaaS)**.

On 26 June 2024, [ANY.RUN published an analysis of a phishing campaign](https://any.run/cybersecurity-blog/analysis-of-the-phishing-campaign/) that matched the characteristics and infrastructure of *Mamba 2FA*. Since then, and likely in reaction to this publication, the phishing kit and associated infrastructure have undergone several significant changes.

## Characteristics of *Mamba 2FA* phishing pages

### URL structure and domain names

As of October 2024, the URLs of *Mamba 2FA* phishing pages have the following structure:

`https://{domain}/{m,n,o}/?{Base64 string}`

For example:

`https://tubope[.]com/n/?c3Y9bzM2NV8xX25vbSZyYW5kPVZFUnhiR1k9JnVpZD1VU0VSMjUwOTIwMjRVMDgwOTI1NTk=`

The phishing page is displayed only if a valid Base64 parameter is present. If the parameter is absent or invalid, the page is blank.

However, the phishing kit also tries to detect automated web browsers and security sandboxes. In this case, the visitor is redirected to `https://google.com/404/`.

### Base64-encoded parameter

Once decoded, the Base64 parameter follows the structure of a URL query string, with 3 field-value pairs. For example:

`sv=o365_1_nom&rand=VERxbGY=&uid=USER25092024U08092559`

* `sv` controls the appearance of the phishing page
* `rand` is a Base64-encoded pseudo-random string, whose function is unknown
* `uid` is presumed to be a unique identifier for each customer of the PhaaS platform

#### Targeted email address

The email address targeted by the phishing att...