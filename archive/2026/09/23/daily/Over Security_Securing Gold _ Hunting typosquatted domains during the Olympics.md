---
title: Securing Gold : Hunting typosquatted domains during the Olympics
url: https://www.sekoia.com/blog/securing-gold-hunting-typosquatted-domains-during-the-olympics
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:04.116956
---

# Securing Gold : Hunting typosquatted domains during the Olympics

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/securing-gold-hunting-typosquatted-domains-during-the-olympics)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/securing-gold-hunting-typosquatted-domains-during-the-olympics)

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

Securing Gold : Hunting typosquatted domains during the Olympics

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

[Maxime ARQUILLIERE](/authors/maxime-arquilliere)

By

[Amaury-Jacques GARÇON](/authors/amaury-jacques-garcon)

By

[Coline C.](/authors/coline-c)

By

[TDR Team](/authors/threat-detection-research-team)

September 11, 2024

# Securing Gold : Hunting typosquatted domains during the Olympics

Discover how Sekoia.io proactively hunts for typosquatted domains related to the Paris 2024 Olympics to detect and prevent cyber threats.

![Illustration of Paris landmarks and athletes during a major international sporting event](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6a1d9aef9156442e8470be_blog-securing-gold-hunting-typosquatted-domains-during-olympics-img-cover.webp)

## Key takeaways

Sekoia TDR recounts its proactive hunt for domains typosquatting Paris 2024 Olympics sites and what the telemetry showed.

* Across July and August 2024 Sekoia proactively hunted domains typosquatting Paris 2024 Olympics sites.
* DNS fuzzing with DNSTwist and Censys queries flagged more than 650 typosquatted domains from a list of 149 official ones.
* Registrations spiked in the days before the opening ceremony, showing the campaigns' opportunistic nature.
* Nearly half of the domains mimicked ticketing platforms, with others impersonating French government or Olympics sites.
* Telemetry showed few and mostly benign hits, with malicious visits reaching users through phishing emails.

Anticipating Paris 2024 Olympics cyber threats, Sekoia.io has conducted **over July and August 2024** a proactive **hunting of Olympics-typosquatted domains** registered by malicious actors - cybercrime related and possibly APT campaigns - in order to detect any kind of operations though the detection of connexion to typosquatted domains (phishing, C2).

This work is complementary to [our general assessment of cyber threats on Paris Olympics](/blog/securing-gold-assessing-cyber-threats-on-paris-2024), published in January 2024. As stated at that time, every Olympic event is a boon for malicious actors, in particular for cybercrime-related, lucrative actors leveraging the Games to conduct campaigns involving phishing attacks, fraud schemes such as fake ticketing or online betting solutions.

We also estimated a risk for state sponsored-related cyber espionage or destructive operations, but **no major incidents** were reported in open source.

In this blogpost, we will expose our hunting techniques and analyse the suspicious domains we detected.

## **Our hunting typosquatted domains process**

Since early June 2024, the Sekoia Threat Detection & Research (TDR) team has been applying a methodology to **detect domain names attempting to fake official websites** responsible for the Paris 2024 Olympic Games. The objective of this monitoring was to **record the opportunistic websites newly registered**, on a day-to-day basis, and to investigate each infrastructure in detail to find malicious activity.

To achieve this, we established a comprehensive list of **legitimate and official domain** names related to the Olympics. In total, we identified over **149 legitimate domain names pertaining to 110 different sectors**. This list includes official websites dedicated to the Olympic Games, institutional entities, media partners, international partners and the cities in France hosting the events.

Based on this, we setted up DNS Fuzzing using the [DNSTwist](https://github.com/elceef/dnstwist) security tool. It is designed to detect typosquatting and phishing attempts by identifying possible permutations of domain names. It generates potential variations of a domain, checks whether these domains are active and inspects SSL certificates. Furthermore, a Censys request has been designed to monitor SSL certificates granted for newly created domains.

`(
 names:/olympics2024\..*/
 OR names:/jo2024\..*/
 OR names:/olympics2024\..*/
 OR names:/paris2024\..*/
 OR names:/sports.gouv\..*/
 OR names:/pass-jeux\..*/
 OR names:/anticiperlesjeux\..*/
 OR names:/ticketparis2024\..*/
 OR names:/transport-public-paris-2024\..*/
 OR names:/iledefrance-mobilites\..*/
 [...]
)
 AND parsed.validity_peri...