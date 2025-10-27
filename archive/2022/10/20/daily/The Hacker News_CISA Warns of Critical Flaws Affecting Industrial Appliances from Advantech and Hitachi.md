---
title: CISA Warns of Critical Flaws Affecting Industrial Appliances from Advantech and Hitachi
url: https://thehackernews.com/2022/10/cisa-warns-of-critical-flaws-affecting.html
source: The Hacker News
date: 2022-10-20
fetch_date: 2025-10-03T20:26:24.089020
---

# CISA Warns of Critical Flaws Affecting Industrial Appliances from Advantech and Hitachi

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

# [CISA Warns of Critical Flaws Affecting Industrial Appliances from Advantech and Hitachi](https://thehackernews.com/2022/10/cisa-warns-of-critical-flaws-affecting.html)

**Oct 19, 2022**Ravie Lakshmanan

[![Advantech and Hitachi](data:image/png;base64... "Advantech and Hitachi")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLjzLOVv3BWS-qURNWBeOfnXikgJFdgp73GWCM3yAKS5ypYQX18cJIFiyLm_niGccOfAwajfE-e6L5r71WWSV5USZt-eRWqpZQym8oAfIowEBancbxlqHxCyuBBc-Isgu-pOxs4DvZA4X2CGqF6U_jtwwZ9XehprpOkPpLGNl5hqZ6IrP_4gqIOP84/s790-rw-e365/cisa.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday released two Industrial Control Systems (ICS) [advisories](https://www.cisa.gov/uscert/ncas/current-activity/2022/10/18/cisa-releases-two-industrial-control-systems-advisories) pertaining to severe flaws in Advantech R-SeeNet and Hitachi Energy APM Edge appliances.

This consists of three weaknesses in the R-SeeNet monitoring solution, successful exploitation of which "could result in an unauthorized attacker remotely deleting files on the system or allowing remote code execution."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The list of issues, which affect R-SeeNet Versions 2.4.17 and prior, is as follows -

* **CVE-2022-3385 and CVE-2022-3386** (CVSS scores: 9.8) - Two stack-based buffer overflow flaws that could lead to remote code execution
* **CVE-2022-3387** (CVSS score: 6.5) - A path traversal flaw that could enable a remote attacker to delete arbitrary PDF files

Patches have been made available in version [R-SeeNet version 2.4.21](https://icr.advantech.cz/products/software/r-seenet) released on September 30, 2022.

Also published by CISA is an update to a December 2021 advisory about multiple flaws in Hitachi Energy Transformer Asset Performance Management ([APM](https://www.hitachienergy.com/in/en/offering/product-and-system/transformers/transformer-service/advanced-services-for-transformers/asset-management-solutions/apm-edge)) Edge products that could render them inaccessible.

The 29 vulnerabilities, collectively assigned a CVSS score of 8.2, stem from security holes in open source software components such as OpenSSL, LibSSL, libxml2, and GRUB2 bootloader. Users are recommended to update to APM Edge version 4.0 to remediate the bugs.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The twin alerts come less than a week after CISA [published 25 ICS advisories](https://www.cisa.gov/uscert/ncas/current-activity/2022/10/13/cisa-releases-twenty-five-industrial-control-systems-advisories) on October 13, 2022, spanning several vulnerabilities across devices from [Siemens](https://thehackernews.com/2022/10/critical-bug-in-siemens-simatic-plcs.html), Hitachi Energy, and Mitsubishi Electric.

According to OT cybersecurity and asset monitoring company SynSaber, 681 ICS product vulnerabilities were reported via CISA in the first half of 2022, out of which 152 are rated Critical, 289 are rated High, 205 are rated Medium, and 35 are rated Low in Severity.

What's more, 54 of the Critical/High-rated CVEs have no patch or any mitigation available from the vendors, accounting for 13% of the total reported flaws and remaining "forever-day vulnerabilities."

"It's important for asset owners and those defending critical infrastructure to understand when remediations are available, and how those remediations should be implemented and prioritized," SynSaber [said](https://synsaber.com/resources/ics-vulnerabilities-h1-2022/).

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Siemens](https://thehackernews.com/search/label/Siemens)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target As...