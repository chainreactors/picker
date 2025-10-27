---
title: Juniper Networks Releases Critical Security Update for Routers
url: https://thehackernews.com/2024/07/juniper-networks-releases-critical.html
source: The Hacker News
date: 2024-07-02
fetch_date: 2025-10-06T17:47:02.698813
---

# Juniper Networks Releases Critical Security Update for Routers

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

# [Juniper Networks Releases Critical Security Update for Routers](https://thehackernews.com/2024/07/juniper-networks-releases-critical.html)

**Jul 01, 2024**Ravie LakshmananVulnerability / Network Security

[![Juniper Networks](data:image/png;base64... "Juniper Networks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-zbcR4_Lvs3PkKZbBO14_dLXYg1cDVrLrfNIppNW9NY7r6c61pm0vfqeNFquENaZmtwh8MxNiIRjLeJPi4eDRx6Im8VBqFXUtYiKkflx4dLhAEhyphenhyphenMZdkCYrKab_HaVoVTwWlpQLixa8bYnRWrRum9V31yZGamztt0G5bG5cOvMFqfj7RfGjGGpPjghBam/s790-rw-e365/juniper.png)

Juniper Networks has released out-of-band security updates to address a critical security flaw that could lead to an authentication bypass in some of its routers.

The vulnerability, tracked as CVE-2024-2973, carries a CVSS score of 10.0, indicating maximum severity.

"An Authentication Bypass Using an Alternate Path or Channel vulnerability in Juniper Networks Session Smart Router or Conductor running with a redundant peer allows a network based attacker to bypass authentication and take full control of the device," the company [said](https://supportportal.juniper.net/s/article/2024-06-Out-Of-Cycle-Security-Bulletin-Session-Smart-Router-SSR-On-redundant-router-deployments-API-authentication-can-be-bypassed-CVE-2024-2973?language=en_US) in an advisory issued last week.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to Juniper Networks, the shortcoming affects only those routers or conductors that are running in high-availability redundant configurations. The list of impacted devices is listed below -

* Session Smart Router (all versions before 5.6.15, from 6.0 before 6.1.9-lts, and from 6.2 before 6.2.5-sts)
* Session Smart Conductor (all versions before 5.6.15, from 6.0 before 6.1.9-lts, and from 6.2 before 6.2.5-sts)
* WAN Assurance Router (6.0 versions before 6.1.9-lts and 6.2 versions before 6.2.5-sts)

The networking equipment maker, which was bought out by Hewlett Packard Enterprise (HPE) for approximately $14 billion earlier this year, said it found no evidence of active exploitation of the flaw in the wild.

It also said that it discovered the vulnerability during internal product testing and that there are no workarounds that resolve the issue.

"This vulnerability has been patched automatically on affected devices for MIST managed WAN Assurance routers connected to the Mist Cloud," it further noted. "It is important to note that the fix is applied automatically on managed routers by a Conductor or on WAN assurance routers has no impact on data-plane functions of the router."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In January 2024, the company also rolled out fixes for a critical vulnerability in the same products ([CVE-2024-21591](https://thehackernews.com/2024/01/critical-rce-vulnerability-uncovered-in.html), CVSS score: 9.8) that could enable an attacker to cause a denial-of-service (DoS) or remote code execution and obtain root privileges on the devices.

With multiple security flaws affecting the company's SRX firewalls and EX switches [weaponized](https://thehackernews.com/2023/11/cisa-sets-deadline-patch-juniper-junos.html) by threat actors last year, it's essential that users apply the patches to protect against potential threats.

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

[Authentication bypass](https://thehackernews.com/search/label/Authentication%20bypass)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[network security](https://thehackernews.com/search/label/network%20security)[router security](https://thehackernews.com/search/label/router%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Dat...