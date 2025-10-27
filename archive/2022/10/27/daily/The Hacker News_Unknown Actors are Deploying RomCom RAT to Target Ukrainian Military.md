---
title: Unknown Actors are Deploying RomCom RAT to Target Ukrainian Military
url: https://thehackernews.com/2022/10/romcom-hackers-circulating-malicious.html
source: The Hacker News
date: 2022-10-27
fetch_date: 2025-10-03T21:04:08.862028
---

# Unknown Actors are Deploying RomCom RAT to Target Ukrainian Military

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

# [Unknown Actors are Deploying RomCom RAT to Target Ukrainian Military](https://thehackernews.com/2022/10/romcom-hackers-circulating-malicious.html)

**Oct 26, 2022**Ravie Lakshmanan

[![RomCom Hackers](data:image/png;base64... "RomCom Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSavoRveYAbP5pdrwI9YfmTuMOCdCPLQOPiGHePQZvA0B3p7H42weqrnD9R9OmNeAvkUkTVynJeFS7cpy-yjIzqKFmTySY2X2fcsRWBdDqGMayUAkdBRQPUzlEaaeG53V5lZZqSV6g112DWSME8HhqRD_BQIoQ5CW_LJAvJz2Bwu9BXGhK3FRJUonQ/s790-rw-e365/hack.jpg)

The threat actor behind a remote access trojan called RomCom RAT has been observed targeting Ukrainian military institutions as part of a new spear-phishing campaign that commenced on October 21, 2022.

The development marks a shift in the attacker's modus operandi, which has been previously attributed to spoofing legitimate apps like Advanced IP Scanner and pdfFiller to drop backdoors on compromised systems.

"The initial 'Advanced IP Scanner' campaign occurred on July 23, 2022," the BlackBerry research and intelligence team [said](https://blogs.blackberry.com/en/2022/10/unattributed-romcom-threat-actor-spoofing-popular-apps-now-hits-ukrainian-militaries). "Once the victim installs a Trojanized bundle, it drops RomCom RAT to the system."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While previous iterations of the campaign involved the use of trojanized Advanced IP Scanner, the unidentified adversarial collective has since switched to pdfFiller as of October 20, indicating an active attempt on part of the adversary to refine tactics and thwart detection.

These lookalike websites host a rogue installer package that results in the deployment of the RomCom RAT, which is capable of harvesting information and capturing screenshots, all of which is exported to a remote server.

[![Malicious Versions of Popular Apps](data:image/png;base64... "Malicious Versions of Popular Apps")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJEXhw9JdJ306lrcBcBNoz16B5o5pyG96h88BMAJaPzx6Hi8w1aAB2K6b03Z7ur0I5SS3JUrgcgWrBc7oJRpBfYYbZMcnXZqSPPkzZWwD9j6O598SJyHjQyX8HAfam3iYuS0_ORLAlfSkvVI48XEIEkyFiCBBo0SCgjqOu193ezIe4Tg8NJKAzzTpH/s790-rw-e365/map.jpg)

The adversary's latest activity directed against the Ukrainian military is a departure in that it employs a phishing email with an embedded link as an initial infection vector, leading to a fake website dropping the next stage downloader.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This downloader, signed using a [valid digital certificate](https://support.microsoft.com/en-us/office/digital-signatures-and-certificates-8186cd15-e7ac-4a16-8597-22bd163e8e96) from "Blythe Consulting sp. z o.o." for an extra layer of evasion, is then used to extract and run the RomCom RAT malware. BlackBerry said the same signer is used by the legitimate version of pdfFiller.

Besides the Ukrainian military, other targets of the campaign include IT companies, food brokers, and food manufacturing entities in the U.S., Brazil, and the Philippines.

"This campaign is a good example of the blurred line between cybercrime-motivated threat actors and targeted attack threat actors," Dmitry Bestuzhev, threat researcher at BlackBerry, told The Hacker News.

"In the past, both groups acted independently, relying on different tooling. Today, targeted attack threat actors rely more on traditional tooling, making attribution harder."

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

[IP Scanner](https://thehackernews.com/search/label/IP%20Scanner)[Phishing Attacks](https://thehackernews.com/search/label/Phishing%20Attacks)[RomCom](https://thehackernews.com/search/label/RomCom)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Mal...