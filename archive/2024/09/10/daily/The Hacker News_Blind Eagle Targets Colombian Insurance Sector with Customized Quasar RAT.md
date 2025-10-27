---
title: Blind Eagle Targets Colombian Insurance Sector with Customized Quasar RAT
url: https://thehackernews.com/2024/09/blind-eagle-targets-colombian-insurance.html
source: The Hacker News
date: 2024-09-10
fetch_date: 2025-10-06T18:31:46.704956
---

# Blind Eagle Targets Colombian Insurance Sector with Customized Quasar RAT

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Blind Eagle Targets Colombian Insurance Sector with Customized Quasar RAT](https://thehackernews.com/2024/09/blind-eagle-targets-colombian-insurance.html)

**Sep 09, 2024**Ravie LakshmananFinancial Security / Malware

[![Customized Quasar RAT](data:image/png;base64... "Customized Quasar RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiILosEDog0FATmR0qjY1DSHeqIKfX5WGPHY3VU4o5rTYHta_z-g9P0NPU4RezzwBPEFCGtZoJ0FR7alTnr9b18rXbQBFi5qc6hGOJ-G8LN_9ab22LT2TCQlzLZ-bpLyi1eIQkeiUKyPMFd54cDs8TVIS0Rz03iHLLxGVT9GDs2paAz5yGQMBrEUGKMrSYY/s790-rw-e365/zscaler.png)

The Colombian insurance sector is the target of a threat actor tracked as **Blind Eagle** with the end goal of delivering a customized version of a known commodity remote access trojan (RAT) referred to as Quasar RAT since June 2024.

"Attacks have originated with phishing emails impersonating the Colombian tax authority," Zscaler ThreatLabz researcher Gaetano Pellegrino [said](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-insurance-sector-blotchyquasar) in a new analysis published last week.

The advanced persistent threat (APT), also [known](https://lab52.io/blog/apt-c-36-recent-activity-analysis/) as AguilaCiega, APT-C-36, and APT-Q-98, has a track record of focusing on organizations and individuals in South America, particularly related to the government and finance sectors in Colombia and Ecuador.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack chains, as [recently documented](https://thehackernews.com/2024/08/blind-eagle-hackers-exploit-spear.html) by Kaspersky, originate with phishing emails that entice recipients into clicking on malicious links that serve as the launchpad for the infection process.

The links, either embedded within a PDF attachment or directly in the email body, point to ZIP archives hosted on a Google Drive folder associated with a compromised account that belongs to a regional government organization in Colombia.

"The lure used by Blind Eagle involved sending a notification to the victim, claiming to be a seizure order due to outstanding tax payments," Pellegrino noted. "This is intended to create a sense of urgency and pressure the victim into taking immediate action."

[![Customized Quasar RAT](data:image/png;base64... "Customized Quasar RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2U2oWdF2_6GzWBneF13ThyphenhyphenKz8hXrjUyIQP-HTdcS1bs03lghnnWDg7EjPZQrMvsUNn8x19NOxyajwIq1dgeGumEV9wA0F_H3QmBVKCJYcDbJ6tfn8F_fQEV4-oexSxIcRVg_EKSKm630SCmJ9WdUZAMFRNlh3GTjqX_l0uoSOxXzyVoiAx5X84NTSVriX/s790-rw-e365/z2.png)

The archive contains within it a Quasar RAT variant dubbed BlotchyQuasar, which packs in additional layers of obfuscation using tools like DeepSea or ConfuserEx to hinder analysis and reverse engineering efforts. It was [previously detailed](https://securityintelligence.com/x-force/x-force-hive0129-targeting-financial-institutions-latam-banking-trojan/) by IBM X-Force in July 2023.

The malware includes capabilities to log keystrokes, execute shell commands, steal data from web browsers and FTP clients, and monitor a victim's interactions with specific banking and payment services located in Colombia and Ecuador.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It also leverages Pastebin as a [dead drop resolver](https://attack.mitre.org/techniques/T1102/001/) to fetch the command-and-control (C2) domain, with the threat actor leveraging Dynamic DNS (DDNS) services to host the C2 domain.

"Blind Eagle typically shields its infrastructure behind a combination of VPN nodes and compromised routers, primarily located in Colombia," Pellegrino said. "This attack demonstrates the continued use of this strategy."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[APT group](https://thehackernews.com/search/label/APT%20group)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data theft](https://thehackernews.com/search/label/data%20theft)[Financial Security](https://thehackernews.com/search/label/Financial%20Security)[Malware](https://thehackernews.com/search/label/Malware)[Obfuscation](https://thehackernews.com/search/label/Obfuscation)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-sec...