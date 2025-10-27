---
title: Earth Bogle Campaign Unleashes NjRAT Trojan on Middle East and North Africa
url: https://thehackernews.com/2023/01/earth-bogle-campaign-unleashes-njrat.html
source: The Hacker News
date: 2023-01-19
fetch_date: 2025-10-04T04:20:29.990856
---

# Earth Bogle Campaign Unleashes NjRAT Trojan on Middle East and North Africa

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

# [Earth Bogle Campaign Unleashes NjRAT Trojan on Middle East and North Africa](https://thehackernews.com/2023/01/earth-bogle-campaign-unleashes-njrat.html)

**Jan 18, 2023**Ravie LakshmananCyber Threat / Malware

[![NjRAT Trojan](data:image/png;base64... "NjRAT Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvSRgJgJqU8UMBpiycjt5O0nettU_kGvD2uzF3AnuQAKRMZeqIYgGc3NpKRHXGItSOfK2E9NpH3dgq3MMdpn2n7HRThcIsJAcx0koxmoGumvIR9qCcWyKTKe63ksVHBMnflKn0pqku4gnOVZ5_czLCITBczTcR_ZyvyyfW69oet1DKyiGMwIen2LLk/s790-rw-e365/cyberattack.png)

An ongoing campaign dubbed **Earth Bogle** is leveraging geopolitical-themed lures to deliver the NjRAT remote access trojan to victims across the Middle East and North Africa.

"The threat actor uses public cloud storage services such as files[.]fm and failiem[.]lv to host malware, while compromised web servers distribute NjRAT," Trend Micro [said](https://www.trendmicro.com/en_us/research/23/a/earth-bogle-campaigns-target-middle-east-with-geopolitical-lures.html) in a report published Wednesday.

Phishing emails, typically tailored to the victim's interests, are loaded with malicious attachments to activate the infection routine. This takes the form of a Microsoft Cabinet (CAB) archive file containing a Visual Basic Script dropper to deploy the next-stage payload.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Alternatively, it's suspected that the files are distributed via social media platforms such as Facebook and Discord, in some cases even creating bogus accounts to serve ads on pages impersonating legitimate news outlets.

The CAB files, hosted on cloud storage services, also masquerade as sensitive voice recordings to entice the victim into opening the archives, only for the VBScript to be executed, leading to the retrieval of another VBScript file that masks itself as an image file.

[![NjRAT Trojan](data:image/png;base64... "NjRAT Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKHbsDR6155SOn347d-Z3f-49NqaE91p0uWX1msTDxTYTH2eN6ojpMMgqinvOA-etAuaoZAGycRm6f-ZkxcgLBxn-ETk7W2_aOe2d8VCtfpRWcYd1kqxqwiECVMeRpm5ffzwO2MqbmD64sNXTuwUfYcOrk_CPXnfYfngZTi_-koUzlvF5WwNAjky0s/s790-rw-e365/malware-attack-news.png)

The second-stage VBScript, for its part, fetches from an already breached domain a PowerShell script that's responsible for loading the RAT payload into memory and executing it.

NjRAT (aka Bladabindi), first discovered in 2013, has myriad capabilities that allow the threat actor to harvest sensitive information and gain control over compromised computers.

"This case demonstrates that threat actors will leverage public cloud storage as malware file servers, combined with social engineering techniques appealing to people's sentiments such as regional geopolitical themes as lures, to infect targeted populations," the researchers concluded.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[njRAT](https://thehackernews.com/search/label/njRAT)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[VBScript](https://thehackernews.com/search/label/VBScript)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before P...