---
title: Cisco Issues Warning for Unpatched Vulnerabilities in EoL Business Routers
url: https://thehackernews.com/2023/01/cisco-issues-warning-for-unpatched.html
source: The Hacker News
date: 2023-01-15
fetch_date: 2025-10-04T03:57:50.564994
---

# Cisco Issues Warning for Unpatched Vulnerabilities in EoL Business Routers

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

# [Cisco Issues Warning for Unpatched Vulnerabilities in EoL Business Routers](https://thehackernews.com/2023/01/cisco-issues-warning-for-unpatched.html)

**Jan 14, 2023**Ravie LakshmananNetwork Security / Bug Report

[![Cisco Router](data:image/png;base64... "Cisco Router")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIAtROloGI6Tt-u2jH243k2dxz9poGMQN3wiy4CuJRJLejT8XXe7WUolNWNUzHu0aiQlsBydrxD9aWAhZnUj8oAmzqRSKQmFb2Welo811wVchr9hYC-c7BV_4VgEZsy249AT6nHYrG5f22fl77Poa7hF4MYug-EAfdqo-q87ixKtQYPkbyzLrm6CT_/s790-rw-e365/cisco.jpg)

Cisco has warned of two security vulnerabilities affecting end-of-life (EoL) Small Business RV016, RV042, RV042G, and RV082 routers that it said will not be fixed, even as it acknowledged the public availability of proof-of-concept (PoC) exploit.

The [issues](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sbr042-multi-vuln-ej76Pke5) are rooted in the router's web-based management interface, enabling a remote adversary to sidestep authentication or execute malicious commands on the underlying operating system.

The most severe of the two is CVE-2023-20025 (CVSS score: 9.0), which is the result of improper validation of user input within incoming HTTP packets.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A threat actor could exploit it remotely by sending a specially crafted HTTP request to vulnerable routers' web-based management interface to bypass authentication and obtain elevated permissions.

The lack of adequate validation is also the reason behind the second flaw tracked as CVE-2023-20026 (CVSS score: 6.5), permitting an attacker with valid admin credentials to achieve root-level privileges and access unauthorized data.

"Cisco has not released and will not release software updates to address the vulnerabilities," the company said. "Cisco Small Business RV016, RV042, RV042G, and RV082 Routers have entered the end-of-life process."

As workarounds, administrators are recommended to disable remote management and block access to ports 443 and 60443. That said, Cisco is cautioning users to "determine the applicability and effectiveness [of the mitigation] in their own environment and under their own use conditions."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Hou Liuyang of Qihoo 360 Netlab has been credited with discovering and reporting the flaws to Cisco.

The network equipment major further noted that while it's aware of PoC code in the wild, it said that it has not observed any malicious use of the vulnerabilities in real-world attacks.

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

[cisco](https://thehackernews.com/search/label/cisco)[network security](https://thehackernews.com/search/label/network%20security)[Router hacking](https://thehackernews.com/search/label/Router%20hacking)[router security](https://thehackernews.com/search/label/router%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64... "Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware")
...