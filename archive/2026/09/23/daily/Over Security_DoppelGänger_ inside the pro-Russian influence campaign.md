---
title: DoppelGänger: inside the pro-Russian influence campaign
url: https://www.sekoia.com/blog/master-of-puppets-uncovering-the-doppelganger-pro-russian-influence-campaign
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:01.577795
---

# DoppelGänger: inside the pro-Russian influence campaign

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/master-of-puppets-uncovering-the-doppelganger-pro-russian-influence-campaign)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/master-of-puppets-uncovering-the-doppelganger-pro-russian-influence-campaign)

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

Master of Puppets: Uncovering the DoppelGänger pro-Russian influence campaign

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

By

[TDR Team](/authors/threat-detection-research-team)

By

[Coline C.](/authors/coline-c)

By

[Amaury-Jacques GARÇON](/authors/amaury-jacques-garcon)

By

[Kilian SEZNEC](/authors/kilian-seznec)

May 21, 2024

# Master of Puppets: Uncovering the DoppelGänger pro-Russian influence campaign

Uncover the details of the DoppelGänger campaign, a Russian influence operation aimed at undermining support for Ukraine.

![Cybersecurity operations center with operators working beneath a large illuminated Russian flag backdrop.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aad4eb37b411a234fcf6594_blog-master-of-puppets-img-cover.webp)

## Key takeaways

Sekoia TDR dissects the pro-Russian DoppelGanger influence campaign, its website network, redirection infrastructure and a new cluster.

* DoppelGanger is an ongoing Russian influence campaign, active since 2022, attributed to the entities Structura and the Social Design Agency.
* It aims to weaken support for Ukraine and deepen divisions across France, Germany, the US, Ukraine and other Western countries.
* The operation combines typosquatted media sites and pseudo-independent outlets, amplified by inauthentic social media accounts.
* A multi-stage redirection chain funnels users from social posts to disinformation sites, with Keitaro tracking campaign effectiveness.
* Sekoia uncovered a new Russian-language cluster and a control panel showing more than 26 million site visits, confirming the campaign stays active.

*This report was originally published for our customers on 14 May 2024.*

## **Executive summary**

* The DoppelGänger campaign is an ongoing influence campaign, starting from May 2022 and attributed to the Structura National Technologies (Structura) and the Social Design Agency (SDA), which are two Russian entities.
* The primary goal of DoppelGänger is to diminish support for Ukraine in the wake of Russian aggression and to foster divisions within nations backing Ukraine. It targets audiences in France, Germany, Ukraine, and the United States, but also in the United Kingdom, Lithuania, Switzerland, Slovakia, Israel and Italy.
* The campaign is supported by a network with two categories of news websites: typosquatted legitimate media outlets and organisations, and independent news websites.
* Disinformation articles are published on these websites and then disseminated and amplified via inauthentic social media accounts on several platforms, especially video-hosting ones like Instagram, TikTok, Cameo and Youtube.
* Sekoia observed a correlation between the number of articles published per country and events like domestic protests, decisions on Ukraine military aid or Russian sanctions, and national budget voting periods.
* The redirection process used in the DoppelGänger campaign is done using 3 stages of redirection. The first stage provides thumbnail metadata to the social network. The second stage downloads and executes an obfuscated JS script from the third stage and further leverages it to redirect the user to the disinformation article website. The third stage allows the attacker to monitor campaign effectiveness using Keitaro.
* Sekoia analysts uncovered a new cluster linked to this campaign and monitored by a control panel. The panel intends to manage several disinformation websites in parallel. They publish mostly content in Russian, which points to a probable different objective from what was observed previously. Our hypothesis is that the Russian-agencies Structura and SDA steering the campaign are also in charge of Russian-speaking propaganda missions on behalf of Moscow.

## **Introduction**

On the eve of 2024, an election year in which more than 54% of the world's population will be called to the polls, the pro-Russian influence campaign DoppelGänger has been given special attention by Western democracies. This type of operation consists of intentionally spreading false or inaccurate information for malicious purposes.

Investigations publicly released throughout 2023 have emphasised the s...