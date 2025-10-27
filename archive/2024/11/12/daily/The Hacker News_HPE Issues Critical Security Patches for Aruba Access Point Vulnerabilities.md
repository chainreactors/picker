---
title: HPE Issues Critical Security Patches for Aruba Access Point Vulnerabilities
url: https://thehackernews.com/2024/11/hpe-issues-critical-security-patches.html
source: The Hacker News
date: 2024-11-12
fetch_date: 2025-10-06T19:23:38.550205
---

# HPE Issues Critical Security Patches for Aruba Access Point Vulnerabilities

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

# [HPE Issues Critical Security Patches for Aruba Access Point Vulnerabilities](https://thehackernews.com/2024/11/hpe-issues-critical-security-patches.html)

**Nov 11, 2024**Ravie LakshmananVulnerability / Risk Mitigation

[![Aruba Access Point Vulnerabilities](data:image/png;base64... "Aruba Access Point Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnDOJOB5IXfN-vkTOBsFk4_4kQ_caeEJZWMTM2bT-Ohcq5jVFZmBEFjzzXqLz4vKvjJuOGRRRqoWIuZuCzwkLQtcMQNEbvwHKJiQEmXNEJARPpYfaiBGOA3RxtJvs6skF8SE2KHc0WT6EteSNIyQUFvtdhfTSjQ1GpSzAiB5nlCT9-WX0csziel3HVHt3w/s790-rw-e365/hpe.png)

Hewlett Packard Enterprise (HPE) has released security updates to address multiple vulnerabilities impacting Aruba Networking Access Point products, including two critical bugs that could result in unauthenticated command execution.

The flaws affect Access Points running Instant AOS-8 and AOS-10 -

* AOS-10.4.x.x: 10.4.1.4 and below
* Instant AOS-8.12.x.x: 8.12.0.2 and below
* Instant AOS-8.10.x.x: 8.10.0.13 and below

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The most severe among the six newly patched vulnerabilities are CVE-2024-42509 (CVSS score: 9.8) and CVE-2024-47460 (CVSS score: 9.0), two critical unauthenticated command injection flaws in the CLI Service that could result in the execution of arbitrary code.

"Command injection vulnerability in the underlying CLI service could lead to unauthenticated remote code execution by sending specially crafted packets destined to the PAPI (Aruba's Access Point management protocol) UDP port (8211)," HPE [said](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw04722en_us&docLocale=en_US) in an advisory for both the flaws.

"Successful exploitation of this vulnerability results in the ability to execute arbitrary code as a privileged user on the underlying operating system."

It's advised to enable cluster security via the cluster-security command to mitigate CVE-2024-42509 and CVE-2024-47460 on devices running Instant AOS-8 code. However, for AOS-10 devices, the company recommends blocking access to UDP port 8211 from all untrusted networks.

Also resolved by HPE are four other vulnerabilities -

* CVE-2024-47461 (CVSS score: 7.2) - An authenticated arbitrary remote command execution (RCE) in Instant AOS-8 and AOS-10
* CVE-2024-47462 and CVE-2024-47463 (CVSS scores: 7.2) - An arbitrary file creation vulnerability in Instant AOS-8 and AOS-10 that leads to authenticated remote command execution
* CVE-2024-47464 (CVSS score: 6.8) - An authenticated path traversal vulnerability leads to remote unauthorized access to files

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As workarounds, users are being urged to restrict access to CLI and web-based management interfaces by placing them within a dedicated VLAN, and controlling them via firewall policies at layer 3 and above.

"Although Aruba Network access points have not previously been reported as exploited in the wild, they are an attractive target for threat actors due to the potential access these vulnerabilities could provide through privileged user RCE," Arctic Wolf [said](https://arcticwolf.com/resources/blog/cve-2024-42509-cve-2024-47460/). "Additionally, threat actors may attempt to reverse-engineer the patches to exploit unpatched systems in the near future."

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

[Access Point](https://thehackernews.com/search/label/Access%20Point)[Command Injection](https://thehackernews.com/search/label/Command%20Injection)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[HP Enterprise](https://thehackernews.com/search/label/HP%20Enterprise)[Networking](https://thehackernews.com/search/label/Networking)[Patching](https://thehackernews.com/search/label/Patching)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Risk Mitigation](https://thehackernews.com/search/label/Risk%20Mitigation)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexit...