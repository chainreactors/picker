---
title: MuddyWater replaces Atera by custom MuddyRot implant
url: https://www.sekoia.com/blog/muddywater-replaces-atera-by-custom-muddyrot-implant-in-a-recent-campaign
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:03.022955
---

# MuddyWater replaces Atera by custom MuddyRot implant

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/muddywater-replaces-atera-by-custom-muddyrot-implant-in-a-recent-campaign)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/muddywater-replaces-atera-by-custom-muddyrot-implant-in-a-recent-campaign)

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

MuddyWater replaces Atera by custom MuddyRot implant in a recent campaign

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

July 15, 2024

# MuddyWater replaces Atera by custom MuddyRot implant in a recent campaign

Find out how MuddyWater have changed their infection chain and employed a new implant dubbed "MuddyRot" by Sekoia TDR analysts.

![Iranian flag waving behind bare tree branches under a blue sky.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aad4d7c3eda28517735b43b_blog-muddywater-replaces-atera-img-cover.webp)

## Key takeaways

Sekoia TDR analyses MuddyRot, a custom implant MuddyWater adopted in place of the Atera RMM tool in a recent campaign.

* Sekoia TDR analysed a June 2024 MuddyWater campaign, the Iranian MOIS-linked intrusion set active against Western and Middle Eastern targets.
* The group dropped its usual Atera RMM tool for a new custom implant Sekoia named MuddyRot.
* The infection now hides download links inside decoy PDFs pointing to Egnyte-hosted ZIP archives.
* MuddyRot is a C x64 implant offering a reverse shell, file transfer and scheduled-task persistence over a raw TCP socket on port 443.
* The return to a homemade implant likely reflects tighter vendor monitoring of abused RMM tools, aiding tracking of MuddyWater.

*This report was originally published for our customers on 20 June 2024.*

*Today, the Check Point Research (CPR) team* [*published*](https://research.checkpoint.com/2024/new-bugsleep-backdoor-deployed-in-recent-muddywater-campaigns/) *a report on the same implant, providing details of recent MuddyWater campaigns.*

## Introduction

On June 9 2024, ClearSky [tweeted](https://x.com/ClearskySec/status/1799829814011994120) about a new campaign associated with the MuddyWater intrusion set, employed by the Iranian intelligence service MOIS (Ministry of Intelligence) against Western and Middle Eastern entities. According to the source, MuddyWater is suspected of targeting Turkey, Azerbaijan, Jordan, Saudi Arabia, and Israel, although the full list of targeted countries has not been confirmed during our investigation.

By examining the posted hashes and relevant infrastructure, we found that compared to previous campaigns, this time MuddyWater changed their infection chain and did not rely on the legitimate Atera remote monitoring and management tool (RMM) as a validator. Instead, we observed that they used a new and undocumented implant. Sekoia TDR analysts dubbed this tool ”MuddyRot”.

This report aims to compare past and current infection chains associated with MuddyWater and present a technical analysis of the “MuddyRot” malware, a new validator in the intrusion set’s arsenal.

## Technical analysis

### Recent infection chain

The MuddyWater intrusion set is known to rely primarily on two intrusion vectors when targeting Windows environments. They use public exploits to compromise internet-exposed servers, such as Exchange or SharePoint servers, and then move laterally within the network. Additionally, they send spear phishing emails from previously compromised email accounts to bypass security measures and increase the emails’ legitimacy in the recipient’s eyes.

On April 22 2024, our fellows at HarfangLab [published](https://harfanglab.io/en/insidethelab/muddywater-rmm-campaign/) a blogpost on recent MuddyWater infection chains leading to the installation of [SimpleHelp](https://simple-help.com/) (2023) and [Atera](https://www.atera.com/) (2023-2024). These infection chains involved an email (or possibly an instant messaging message) sent from a compromised account. The email included a link to an online storage service hosting a malicious ZIP archive, which contained the remote monitoring and management software.

In the recently observed campaigns, MuddyWater seems to have changed this infection chain by embedding the links in PDF files instead of emails. The one-page PDF used resembles MuddyWater’s recent emails—straightforward, without any images, and with decoys related to online courses or webinars to face cyber threats, as shown below. By clicking the embedded links, the user is redirected to a ...