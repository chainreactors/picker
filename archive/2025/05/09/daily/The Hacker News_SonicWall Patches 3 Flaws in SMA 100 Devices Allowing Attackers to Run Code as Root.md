---
title: SonicWall Patches 3 Flaws in SMA 100 Devices Allowing Attackers to Run Code as Root
url: https://thehackernews.com/2025/05/sonicwall-patches-3-flaws-in-sma-100.html
source: The Hacker News
date: 2025-05-09
fetch_date: 2025-10-06T22:30:42.019879
---

# SonicWall Patches 3 Flaws in SMA 100 Devices Allowing Attackers to Run Code as Root

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

# [SonicWall Patches 3 Flaws in SMA 100 Devices Allowing Attackers to Run Code as Root](https://thehackernews.com/2025/05/sonicwall-patches-3-flaws-in-sma-100.html)

**May 08, 2025**Ravie LakshmananNetwork Security / Vulnerability

[![SonicWall](data:image/png;base64... "SonicWall")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwP_1mxjcUQ5tfmigVsrjlbsaVQkbWo4CpFngWLGAwvtu8_s-kdMhtiKHT62bEcUq3MwoQe7qtpvbXBiHN1x9CBaJUH-o7zCnRafS1Zf31bWQWYpJH5DyQKsveqnoBpLY6Wx7T0hdvGtXtY5CuhWmSV2ZlQhzfRQp8nE9qSJ8OpM9JQh4vPdwozrL24J3K/s790-rw-e365/sonicc.png)

SonicWall has [released](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0011) patches to address three security flaws affecting SMA 100 Secure Mobile Access (SMA) appliances that could be fashioned to result in remote code execution.

The vulnerabilities are listed below -

* **CVE-2025-32819** (CVSS score: 8.8) - A vulnerability in SMA100 allows a remote authenticated attacker with SSL-VPN user privileges to bypass the path traversal checks and delete an arbitrary file potentially resulting in a reboot to factory default settings.
* **CVE-2025-32820** (CVSS score: 8.3) - A vulnerability in SMA100 allows a remote authenticated attacker with SSL-VPN user privileges can inject a path traversal sequence to make any directory on the SMA appliance writable
* **CVE-2025-32821** (CVSS score: 6.7) - A vulnerability in SMA100 allows a remote authenticated attacker with SSL-VPN admin privileges can with admin privileges can inject shell command arguments to upload a file on the appliance

"An attacker with access to an SMA SSL-VPN user account can chain these vulnerabilities to make a sensitive system directory writable, elevate their privileges to SMA administrator, and write an executable file to a system directory," Rapid7 [said](https://www.rapid7.com/blog/post/2025/05/07/multiple-vulnerabilities-in-sonicwall-sma-100-series-2025/) in a report. "This chain results in root-level remote code execution."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

CVE-2025-32819 is assessed to be a patch bypass for a [previously identified flaw](https://www.nccgroup.com/us/research-blog/technical-advisory-sonicwall-sma-100-series-unauthenticated-arbitrary-file-deletion/) reported by NCC Group in [December 2021](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0026).

The cybersecurity company noted that CVE-2025-32819 may have been exploited in the wild as a zero-day based on known indicators of compromise (IoCs) and incident response investigations. However, it's worth noting that SonicWall makes no mention of the flaw being weaponized in real-world attacks.

The shortcomings, that impact SMA 100 Series including SMA 200, 210, 400, 410, 500v, have been addressed in version 10.2.1.15-81sv.

The development comes as [multiple security flaws](https://thehackernews.com/2025/05/sonicwall-confirms-active-exploitation.html) in SMA 100 Series devices have come under active exploitation in recent weeks, including CVE-2021-20035, CVE-2023-44221, and CVE-2024-38475. Users are advised to update their instances to the latest version for optimal protection.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[network security](https://thehackernews.com/search/label/network%20security)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Sonicwall](https://thehackernews.com/search/label/Sonicwall)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[VPN Security](https://thehackernews.com/search/label/VPN%20Security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet ...