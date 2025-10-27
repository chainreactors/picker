---
title: Cisco Fixes Two Critical Flaws in Smart Licensing Utility to Prevent Remote Attacks
url: https://thehackernews.com/2024/09/cisco-fixes-two-critical-flaws-in-smart.html
source: The Hacker News
date: 2024-09-06
fetch_date: 2025-10-06T18:31:53.376109
---

# Cisco Fixes Two Critical Flaws in Smart Licensing Utility to Prevent Remote Attacks

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

# [Cisco Fixes Two Critical Flaws in Smart Licensing Utility to Prevent Remote Attacks](https://thehackernews.com/2024/09/cisco-fixes-two-critical-flaws-in-smart.html)

**Sep 05, 2024**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0pdAfBVqKScsbfrhpJakVugyR-dj5ozY_kco-HZ8Sm1aQMLa9Quql4NHGF0BJANx8BTL4vZHXgkbI6jtTAYjgrPnjq9jfgNNTMUOi5OX9ypF-RP9Hm2Qyev1BRkRPwr9eg9n7niGnixjoiEhPEamZAI61vPIt5gG9iAG_aWxrAW1U33MQWWYupat6Cc7Q/s790-rw-e365/cisc.jpg)

Cisco has released security updates for two critical security flaws impacting its Smart Licensing Utility that could allow unauthenticated, remote attackers to elevate their privileges or access sensitive information.

A brief description of the two vulnerabilities is below -

* CVE-2024-20439 (CVSS score: 9.8) - The presence of an undocumented static user credential for an administrative account that an attacker could exploit to log in to an affected system

* CVE-2024-20440 (CVSS score: 9.8) - A vulnerability arising due to an excessively verbose debug log file that an attacker could exploit to access such files by means of a crafted HTTP request and obtain credentials that can be used to access the API

While these shortcomings are not dependent on each other for them to be successful, Cisco [notes](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cslu-7gHMzWmw) in its advisory that they "are not exploitable unless Cisco Smart Licensing Utility was started by a user and is actively running."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The flaws, which were discovered during internal security testing, also do not affect Smart Software Manager On-Prem and Smart Software Manager Satellite products.

Users of Cisco Smart License Utility versions 2.0.0, 2.1.0, and 2.2.0 are advised to update to a fixed release. Version 2.3.0 of the software is not susceptible to the bug.

Cisco has also released updates to resolve a command injection vulnerability in its Identity Services Engine (ISE) that could permit an authenticated, local attacker to run arbitrary commands on an underlying operating system and elevate privileges to root.

The flaw, tracked as CVE-2024-20469 (CVSS score: 6.0), requires an attacker to have valid administrator privileges on an affected device.

"This vulnerability is due to insufficient validation of user-supplied input," the company [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-injection-6kn9tSxm). "An attacker could exploit this vulnerability by submitting a crafted CLI command. A successful exploit could allow the attacker to elevate privileges to root."

It impacts the following versions -

* Cisco ISE 3.2 (3.2P7 - Sep 2024)
* Cisco ISE 3.3 (3.3P4 - Oct 2024)

The company has also warned that a proof-of-concept (PoC) exploit code is available, although it's not aware of any malicious exploitation of the bug.

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

[cisco](https://thehackernews.com/search/label/cisco)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[network security](https://thehackernews.com/search/label/network%20security)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[Remote Access](https://thehackernews.com/search/label/Remote%20Access)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Networks Portals Jump 500...