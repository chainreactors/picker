---
title: Royal Ransomware Threat Takes Aim at U.S. Healthcare System
url: https://thehackernews.com/2022/12/royal-ransomware-threat-takes-aim-at-us.html
source: The Hacker News
date: 2022-12-13
fetch_date: 2025-10-04T01:21:17.173770
---

# Royal Ransomware Threat Takes Aim at U.S. Healthcare System

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

# [Royal Ransomware Threat Takes Aim at U.S. Healthcare System](https://thehackernews.com/2022/12/royal-ransomware-threat-takes-aim-at-us.html)

**Dec 12, 2022**Ravie LakshmananHealthcare IT / Ransomware

[![Healthcare System Ransomware](data:image/png;base64... "Healthcare System Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPk_dsf6BcC-4TkKbJnPRGC7ZCd3h8KAl-mRwNza7IFj_OaSNV6JOe3UveEF26IBjLJVyMu_8m7vtv0N-W4D9-6nMDFS9iioSnr7Jn8-hL0mh6fnmypb5UOuhCM_BMHdbgT6___iPtnOlPSCRcekD95qmmitllLdSpVsogXgalu76tuqNg0z0vKnha/s790-rw-e365/royal.png)

The U.S. Department of Health and Human Services (HHS) has cautioned of ongoing Royal ransomware attacks targeting healthcare entities in the country.

"While most of the known ransomware operators have performed Ransomware-as-a-Service, Royal appears to be a private group without any affiliates while maintaining financial motivation as their goal," the agency's Health Sector Cybersecurity Coordination Center (HC3) [said](https://www.hhs.gov/sites/default/files/royal-ransomware-analyst-note.pdf) [PDF].

"The group does claim to steal data for double-extortion attacks, where they will also exfiltrate sensitive data."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Royal ransomware, per [Fortinet FortiGuard Labs](https://www.fortinet.com/blog/threat-research/ransomware-roundup-royal-ransomware), is said to be active since at least the start of 2022. The malware is a 64-bit Windows executable written in C++ and is launched via the command line, indicating that it involves a human operator to trigger the infection after obtaining access to a targeted environment.

Besides deleting volume shadow copies on the system, Royal utilizes the OpenSSL cryptographic library to encrypt files to the AES standard and appends them with a ".royal" extension.

The [ransomware](https://blog.bushidotoken.net/2022/11/the-continuity-of-conti.html) "expands the concept of partial encryption, which means it has the ability to encrypt a predetermined portion of the file content and base its partial encryption on a flexible percentage encryption, which makes detection more challenging for anti-ransomware solutions," Cybereason [disclosed](https://www.cybereason.com/blog/royal-ransomware-analysis) in a new analysis.

"Royal ransomware employs multiple threads in order to accelerate the encryption process," the cybersecurity company further added.

Last month, Microsoft disclosed that a group it's tracking under the name [DEV-0569](https://thehackernews.com/2022/11/microsoft-warns-of-hackers-using-google.html) has been observed deploying the ransomware family through a variety of methods.

This includes malicious links delivered to victims by means of malicious ads, fake forum pages, blog comments, or through phishing emails that lead to rogue installer files for legitimate apps like Microsoft Teams or Zoom.

The files are known to harbor a malware downloader dubbed BATLOADER, which is then used to deliver a wide variety of payloads such as Gozi, Vidar, and BumbleBee, in addition to abusing genuine remote management tools like Syncro to deploy Cobalt Strike for subsequent ransomware deployment.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The ransomware gang, despite its emergence only this year, is believed to comprise experienced actors from other operations, indicative of the ever-evolving nature of the threat landscape.

"Originally, the ransomware operation used BlackCat's encryptor, but eventually started using Zeon, which generated a ransomware note that was identified as being similar to Conti's," the HHS said. "This note was later changed to Royal in September 2022."

The agency further noted that Royal ransomware attacks on healthcare have primarily focused on organizations in the U.S., with payment demands ranging from $250,000 to $2 million.

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

[cryptography](https://thehackernews.com/search/label/cryptography)[FortiGuard](https://thehackernews.com/search/label/FortiGuard)[Fortinet](https://thehackernews.com/search/label/Fortinet)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[OpenSSL](https://thehackernews.com/search/label/OpenSSL)[ransomware](https://thehackernews.com/search/label/ransomware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews....