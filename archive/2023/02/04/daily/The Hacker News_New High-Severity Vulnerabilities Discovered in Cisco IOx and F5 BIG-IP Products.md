---
title: New High-Severity Vulnerabilities Discovered in Cisco IOx and F5 BIG-IP Products
url: https://thehackernews.com/2023/02/new-high-severity-vulnerabilities.html
source: The Hacker News
date: 2023-02-04
fetch_date: 2025-10-04T05:43:42.613222
---

# New High-Severity Vulnerabilities Discovered in Cisco IOx and F5 BIG-IP Products

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

# [New High-Severity Vulnerabilities Discovered in Cisco IOx and F5 BIG-IP Products](https://thehackernews.com/2023/02/new-high-severity-vulnerabilities.html)

**Feb 03, 2023**Ravie LakshmananNetwork Security / Vulnerability

[![Cisco IOx and F5 BIG-IP Products](data:image/png;base64... "Cisco IOx and F5 BIG-IP Products")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUIgOH_f5-Mz0a7W05ertlXt3bxhKdmtrb6CQdR_8zHb9Czro2T9MT-e3U6d3eOYvNY9Itj0s3s0-DJEEtr_vXPj_nkhlrcuqUTLzHhHWnFOR6aXBkp2Jn6NT3TOtVF_rEo8iK4qbeFMchNY5gSU8puNeyFCzi8DgpBMgkFxD4KvF7nxVbFTANR1p_/s790-rw-e365/f5-cisco.png)

F5 has warned of a high-severity flaw impacting BIG-IP appliances that could lead to denial-of-service (DoS) or arbitrary code execution.

The issue is rooted in the iControl Simple Object Access Protocol ([SOAP](https://www.f5.com/glossary/simple-object-access-protocol-soap)) interface and affects the following versions of BIG-IP -

* 13.1.5
* 14.1.4.6 - 14.1.5
* 15.1.5.1 - 15.1.8
* 16.1.2.2 - 16.1.3, and
* 17.0.0

"A format string vulnerability exists in iControl SOAP that allows an authenticated attacker to crash the iControl SOAP CGI process or, potentially execute arbitrary code," the company [said](https://my.f5.com/manage/s/article/K000130415) in an advisory. "In appliance mode BIG-IP, a successful exploit of this vulnerability can allow the attacker to cross a security boundary."

Tracked as CVE-2023-22374 (CVSS score: 7.5/8.5), security researcher Ron Bowes of Rapid7 has been credited with discovering and reporting the flaw on December 6, 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Given that the iCOntrol SOAP interface runs as root, a successful exploit could permit a threat actor to remotely trigger code execution on the device as the root user. This can be achieved by inserting arbitrary [format string characters](https://en.wikipedia.org/wiki/Printf_format_string#Type_field) into a query parameter that's passed to a logging function called syslog, Bowes [said](https://www.rapid7.com/blog/post/2023/02/01/cve-2023-22374-f5-big-ip-format-string-vulnerability/).

F5 noted that it has addressed the problem in an engineering hotfix that is available for supported versions of BIG-IP. As a workaround, the company is recommending users restrict access to the iControl SOAP API to only trusted users.

## Cisco Patches Command Injection Bug in Cisco IOx

The disclosure comes as Cisco released updates to fix a flaw in Cisco IOx application hosting environment (CVE-2023-20076, CVSS score: 7.2) that could open the door for an authenticated, remote attacker to execute arbitrary commands as root on the underlying host operating system.

The [vulnerability](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iox-8whGn5dL) impacts devices running Cisco IOS XE Software and have the Cisco IOx feature enabled, as well as 800 Series Industrial ISRs, Catalyst Access Points, CGR1000 Compute Modules, IC3000 Industrial Compute Gateways, IR510 WPAN Industrial Routers.

Cybersecurity firm Trellix, which identified the issue, said it could be weaponized to inject malicious packages in a manner that can persist system reboots and firmware upgrades, leaving which can only be removed after a factory reset.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"A bad actor could use CVE-2023-20076 to maliciously tamper with one of the affected Cisco devices anywhere along this supply chain," it [said](https://www.trellix.com/en-us/about/newsroom/stories/research/when-pwning-cisco-persistence-is-key-when-pwning-supply-chain-cisco-is-key.html), warning of potential threats to the broader supply chain. "The level of access that CVE-2023-20076 provides could allow for backdoors to be installed and hidden, making the tampering entirely transparent for the end user."

While the exploit requires the attacker to be authenticated and have admin privileges, it's worth noting that adversaries can find a variety of ways to escalate privileges, such as phishing or by banking on the possibility that users may have failed to change the default credentials.

Also discovered by Trellix is a [security check bypass](https://thehackernews.com/2022/09/15-year-old-unpatched-python.html) during [TAR archive extraction](https://www.trellix.com/en-us/about/newsroom/stories/research/trellix-advanced-research-center-patches-vulnerable-open-source-projects.html), which could allow an attacker to write on the underlying host operating system as the root user.

The networking equipment major, which has since remediated the defect, said the vulnerability poses no immediate risk as "the code was put there for future application packaging support."

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

[F5 BIG-IP](https://thehackernews.com/search/label/F5%20BIG-IP)[F5 Networks](https://thehackernews.com/search/label/F5%20Networks)[hacking news](https://thehackernews.com/search/label/hacking%20news)[network security](https://thehackernews.com/search/label/network%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base...