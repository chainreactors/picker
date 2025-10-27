---
title: New Ursnif Variant Likely Shifting Focus to Ransomware and Data Theft
url: https://thehackernews.com/2022/10/latest-ursnif-variant-shifts-focus-from.html
source: The Hacker News
date: 2022-10-21
fetch_date: 2025-10-03T20:33:18.235613
---

# New Ursnif Variant Likely Shifting Focus to Ransomware and Data Theft

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

# [New Ursnif Variant Likely Shifting Focus to Ransomware and Data Theft](https://thehackernews.com/2022/10/latest-ursnif-variant-shifts-focus-from.html)

**Oct 20, 2022**Ravie Lakshmanan

[![Ursnif malware](data:image/png;base64... "Ursnif malware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeNc1IVkYzCyV-Pa8KfHk_bFCvv_q1MlojS3N-S7rvO4VQ_jq7dUASEGQ7oOXNUyKmYmgvSDGueVafCpMs2ciGtlNMDKE7OpX-fEKFfBsiFM1k1miKIoodDq9Y0HzGZf0OYYIbd1o5cK_7AzYB5vwPf1qNUbdr1mYVAX3i9jdvn0Odwe06n1A6xUr2/s790-rw-e365/hex.jpg)

The Ursnif malware has become the latest malware to shed its roots as a banking trojan to revamp itself into a generic backdoor capable of delivering next-stage payloads, joining the likes of Emotet, Qakbot, and TrickBot.

"This is a significant shift from the malware's original purpose to enable banking fraud, but is consistent with the broader threat landscape," Mandiant researchers Sandor Nemes, Sulian Lebegue, and Jessa Valdez [disclosed](https://www.mandiant.com/resources/blog/rm3-ldr4-ursnif-banking-fraud) in a Wednesday analysis.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The refreshed and refactored variant, first spotted by the Google-owned threat intelligence firm in the wild on June 23, 2022, has been codenamed LDR4, in what's being seen as an attempt to lay the groundwork for potential ransomware and data theft extortion operations.

Ursnif, also called Gozi or ISFB, is one of the oldest banker malware families, with [the earliest documented attacks](https://www.secureworks.com/research/gozi) going as far back as 2007. Check Point, in August 2020, mapped the "[divergent evolution of Gozi](https://research.checkpoint.com/2020/gozi-the-malware-with-a-thousand-faces/)" over the years, while pointing out its fragmented development history.

[![Ursnif malware](data:image/png;base64... "Ursnif malware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZtC4s9Wv0o-ycMaYWHoCj1t7l2Ei1cNHCwhmnfseO3dGsx4yWN-QP5SSG8ypQCd7N-PQn6U6hv1nk6lfMdjIM0-BRnRCqmh6xFgdjWnrrTF40Sk52c10ybk2iHSm3G01PS_7FRjudYblgLjzs6-reYhT-W6ZwS3N1LxQ9UbYmTp16xkBletUZT1UE/s790-rw-e365/malware.jpg)

Almost a year later in late June 2021, a Romanian threat actor, Mihai Ionut Paunescu, was [arrested](https://thehackernews.com/2021/06/hackers-wanted-in-us-for-spreading-gozi.html) by Colombian law enforcement officials for his role in propagating the malware to no fewer than a million computers from 2007 to 2012.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The latest attack chain detailed by Mandiant demonstrates the use of recruitment and invoice-related email lures as an initial intrusion vector to download a Microsoft Excel document, which then fetches and launches the malware.

The major refurbishment of Ursnif eschews all its banking-related features and modules in favor of retrieving a [VNC module](https://en.wikipedia.org/wiki/Virtual_Network_Computing) and gaining a remote shell into the compromised machine, which are carried out by connecting to a remote server to obtain said commands.

"These shifts may reflect the threat actors' increased focus towards participating in or enabling ransomware operations in the future," the researchers said.

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

[Emotet](https://thehackernews.com/search/label/Emotet)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[Qakbot](https://thehackernews.com/search/label/Qakbot)[Trickbot](https://thehackernews.com/search/label/Trickbot)[Ursnif](https://thehackernews.com/search/label/Ursnif)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](h...