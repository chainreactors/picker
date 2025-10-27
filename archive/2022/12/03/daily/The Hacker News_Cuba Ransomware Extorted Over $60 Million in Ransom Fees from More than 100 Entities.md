---
title: Cuba Ransomware Extorted Over $60 Million in Ransom Fees from More than 100 Entities
url: https://thehackernews.com/2022/12/cuba-ransomware-extorted-over-60.html
source: The Hacker News
date: 2022-12-03
fetch_date: 2025-10-04T00:26:42.369823
---

# Cuba Ransomware Extorted Over $60 Million in Ransom Fees from More than 100 Entities

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

# [Cuba Ransomware Extorted Over $60 Million in Ransom Fees from More than 100 Entities](https://thehackernews.com/2022/12/cuba-ransomware-extorted-over-60.html)

**Dec 02, 2022**Ravie LakshmananData Security / Incident Response

[![Cuba Ransomware](data:image/png;base64... "Cuba Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8tTIoIM0jQbURH5PDnsmJRHY_lsHAklLsSwnnCy4L7peXJqw9IBIpKPUPJkyvg7_m2_n7uzGNLygUAk9J5Dn1ZMtuO--1mRGpLx-qpO8G7CW-Gwx2PUYYtWv5OuALZiA0xTKhEua4hbOnjAEwvt7sqxbdY3BamBoL-I5UxsUNssvzOcfgQIAVuHC0/s790-rw-e365/cuba-ransomware.png)

The threat actors behind Cuba (aka COLDDRAW) ransomware have received more than $60 million in ransom payments and compromised over 100 entities across the world as of August 2022.

In a new advisory shared by the U.S. Cybersecurity and Infrastructure Security Agency (CISA) and the Federal Bureau of Investigation (FBI), the agencies [highlighted](https://www.cisa.gov/uscert/ncas/current-activity/2022/12/01/stopransomware-cuba-ransomware) a "sharp increase in both the number of compromised U.S. entities and the ransom amounts."

The ransomware crew, also known as [Tropical Scorpius](https://thehackernews.com/2022/08/hackers-behind-cuba-ransomware-attacks.html), has been observed targeting financial services, government facilities, healthcare, critical manufacturing, and IT sectors, while simultaneously expanding its tactics to gain initial access and interact with breached networks.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth noting that despite the name "Cuba," there is no evidence to suggest that the actors have any connection or affiliation with the island country.

The entry point for the attacks involves the exploitation of known security flaws, phishing, compromised credentials, and legitimate remote desktop protocol (RDP) tools, followed by distributing the ransomware via [Hancitor](https://blogs.blackberry.com/en/2021/07/threat-thursday-hancitor-malware) (aka Chanitor).

Some of the flaws incorporated by Cuba into its toolset are as follows -

* [**CVE-2022-24521**](https://thehackernews.com/2022/04/microsoft-issues-patches-for-2-windows.html) (CVSS score: 7.8) - An elevation of privilege vulnerability in Windows Common Log File System (CLFS) Driver
* [**CVE-2020-1472**](https://thehackernews.com/2020/09/detecting-and-preventing-critical.html) (CVSS score: 10.0) - An elevation of privilege vulnerability in Netlogon remote protocol (aka ZeroLogon)

"In addition to deploying ransomware, the actors have used 'double extortion' techniques, in which they exfiltrate victim data, and (1) demand a ransom payment to decrypt it and, (2) threaten to publicly release it if a ransom payment is not made," CISA noted.

Cuba is also said to share links with the operators of RomCom RAT and another ransomware family called Industrial Spy, according to recent findings from BlackBerry and Palo Alto Networks Unit 42.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The RomCom RAT is [distributed](https://thehackernews.com/2022/11/hackers-using-rogue-versions-of-keepass.html) through trojanized versions of legitimate software such as SolarWinds Network Performance Monitor, KeePass, PDF Reader Pro, Advanced IP Scanner, pdfFiller, and Veeam Backup & Replication that are hosted on counterfeit lookalike websites.

The advisory from CISA and FBI is the latest in a series of alerts the agencies have issued about different ransomware strains such as [MedusaLocker](https://www.cisa.gov/uscert/ncas/alerts/aa22-181a), [Zeppelin](https://www.cisa.gov/uscert/ncas/alerts/aa22-223a), [Vice Society](https://thehackernews.com/2022/10/vice-society-hackers-are-behind-several.html), [Daixin Team](https://thehackernews.com/2022/10/cisa-warns-of-daixin-team-hackers.html), and [Hive](https://thehackernews.com/2022/11/hive-ransomware-attackers-extorted-100.html).

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

[CISA](https://thehackernews.com/search/label/CISA)[Cuba Ransomware](https://thehackernews.com/search/label/Cuba%20%20Ransomware)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patc...