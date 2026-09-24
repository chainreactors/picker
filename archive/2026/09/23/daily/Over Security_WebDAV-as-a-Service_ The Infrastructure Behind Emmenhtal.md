---
title: WebDAV-as-a-Service: The Infrastructure Behind Emmenhtal
url: https://www.sekoia.com/blog/webdav-as-a-service-uncovering-the-infrastructure-behind-emmenhtal-loader-distribution
source: Over Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:04.307517
---

# WebDAV-as-a-Service: The Infrastructure Behind Emmenhtal

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

* Solutions
* Platform
* Partners
* Company
* Resources

[en](/blog/webdav-as-a-service-uncovering-the-infrastructure-behind-emmenhtal-loader-distribution)

[fr](/fr)

[Take a tour](https://sekoia.storylane.io/share/8zdjfok9atpn)[GET A demo](/contact)

[en](/blog/webdav-as-a-service-uncovering-the-infrastructure-behind-emmenhtal-loader-distribution)

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

WebDAV-as-a-Service: Uncovering the infrastructure behind Emmenhtal loader distribution

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

[Marc NEBOUT](/authors/marc-nebout)

By

[TDR Team](/authors/threat-detection-research-team)

September 19, 2024

# WebDAV-as-a-Service: Uncovering the infrastructure behind Emmenhtal loader distribution

This blogpost examines the use of WebDAV technology in hosting malicious files related to the Emmenhtal loader, then analyses the various final payloads delivered through this infrastructure.

![Network of server towers connected to a cloud security node over a global map.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aad4cbb56dca1c4c4ddbaaa_blog-webdav-as-a-service-img-cover.webp)

## Key takeaways

Sekoia TDR examines the WebDAV Infrastructure-as-a-Service distributing the Emmenhtal loader and its many payloads.

* Since December 2023 Sekoia TDR has tracked WebDAV infrastructure distributing the memory-only Emmenhtal loader, also called PeakLight.
* Malicious LNK files hosted on WebDAV servers invoke the trusted mshta.exe binary to fetch the loader from separate infrastructure.
* Over 100 WebDAV servers delivered a wide range of payloads including DarkGate, Amadey, Lumma, Remcos and many others.
* The variety of malware, recurring test files and consistent hosting providers suggest an Infrastructure-as-a-Service operation.
* Splitting the LNK host from the payload server across trusted autonomous systems complicates detection and attribution.

*This report was originally published for our customers on 30 August 2024.*

## **Introduction**

Since December 2023, Sekoia TDR team monitored a specific infrastructure involved in the distribution of the Emmenhtal loader. Emmenhtal is a stealthy malware loader known for its effectiveness in distributing various commodity infostealers worldwide. This loader has attracted attention from cybersecurity researchers, with detailed analyses provided by [Orange Cyberdefense](https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide) and [Google Cloud's Threat Intelligence team](https://cloud.google.com/blog/topics/threat-intelligence/peaklight-decoding-stealthy-memory-only-malware?hl=en).

The Emmenhtal loader, also known as PeakLight, operates in a memory-only manner, making it difficult to detect and analyse. It is primarily used to distribute other malicious payloads, including well-known infostealers that target sensitive information.

This blogpost begins by examining the use of WebDAV technology in hosting malicious files related to the Emmenhtal loader, then analyses the various final payloads delivered through this infrastructure, and concludes by exploring the possibility that the infrastructure is being offered as-a-service to multiple threat actors.

## **Use of WebDAV technology for malicious file hosting**

In our investigation of the infrastructure distributing the Emmenhtal loader, TDR analysts identified the use of WebDAV (Web Distributed Authoring and Versioning) technology to host malicious files. WebDAV, an extension of the HTTP protocol, allows for the management of files on web servers, including uploading, editing, and deleting files remotely. Even though WebDAV has legitimate applications in collaborative environments, threat actors have increasingly leveraged this technology to facilitate malicious activities.

The Emmenhtal loader, first detailed by Orange Cyberdefense for its role in distributing commodity infostealers, was later analysed by Google Cloud’s Threat Intelligence team, which uncovered its sophisticated memory-only execution strategy under the name PeakLight. These analyses underscore the significant and evolving threat posed by Emmenhtal as it continues to deliver new infostealers.

In one of the infection chains described by Orange Cyberdefense and Google, the user is initially redirected to the WebDAV server through a drive-by compromise while visiting some websites. This process results in a preview of an *explorer.exe* window connected to the WebDAV server, where the m...