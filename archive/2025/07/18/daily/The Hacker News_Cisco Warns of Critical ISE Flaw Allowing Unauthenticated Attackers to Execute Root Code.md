---
title: Cisco Warns of Critical ISE Flaw Allowing Unauthenticated Attackers to Execute Root Code
url: https://thehackernews.com/2025/07/cisco-warns-of-critical-ise-flaw.html
source: The Hacker News
date: 2025-07-18
fetch_date: 2025-10-07T00:01:13.004145
---

# Cisco Warns of Critical ISE Flaw Allowing Unauthenticated Attackers to Execute Root Code

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

# [Cisco Warns of Critical ISE Flaw Allowing Unauthenticated Attackers to Execute Root Code](https://thehackernews.com/2025/07/cisco-warns-of-critical-ise-flaw.html)

**Jul 17, 2025**Ravie LakshmananVulnerability / Network Security

[![Critical ISE Flaw](data:image/png;base64... "Critical ISE Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRCiH6eZrjSn9ryr5SGE90dJtEGicGevcdJ1otagCN-nKe86YcCiTUYs6e-w-nK2hscnVrRetOjt7vni-TTH4oBJwg5v1olyJtnXbiFZOfQVbEsWkAU1ebQP6FevCpRnahMTaCQasHNIdCDKxFwWL7Oo5XTpclSi9eaPjYudEVTqgz8e-VYEct4myG-2Ik/s790-rw-e365/cisco.jpg)

Cisco has disclosed a new maximum-severity security vulnerability impacting Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) that could permit an attacker to execute arbitrary code on the underlying operating system with elevated privileges.

Tracked as CVE-2025-20337, the shortcoming carries a CVSS score of 10.0 and is similar to [CVE-2025-20281](https://thehackernews.com/2025/06/critical-rce-flaws-in-cisco-ise-and-ise.html), which was patched by the networking equipment major late last month.

"Multiple vulnerabilities in a specific API of Cisco ISE and Cisco ISE-PIC could allow an unauthenticated, remote attacker to execute arbitrary code on the underlying operating system as root. The attacker does not require any valid credentials to exploit these vulnerabilities," the company [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-unauth-rce-ZAd2GnJ6) in an updated advisory.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"These vulnerabilities are due to insufficient validation of user-supplied input. An attacker could exploit these vulnerabilities by submitting a crafted API request. A successful exploit could allow the attacker to obtain root privileges on an affected device."

Kentaro Kawane of GMO Cybersecurity has been credited with discovering and reporting the flaw. Kawane was previously [acknowledged](https://thehackernews.com/2025/06/critical-rce-flaws-in-cisco-ise-and-ise.html) for two other critical Cisco ISE flaws (CVE-2025-20286 and CVE-2025-20282) and another [critical bug](https://thehackernews.com/2025/07/fortinet-releases-patch-for-critical.html) in Fortinet FortiWeb (CVE-2025-25257)

CVE-2025-20337 affects ISE and ISE-PIC releases 3.3 and 3.4, regardless of device configuration. It does not impact ISE and ISE-PIC release 3.2 or earlier. The issue has been patched in the following versions -

* Cisco ISE or ISE-PIC Release 3.3 (Fixed in 3.3 Patch 7)
* Cisco ISE or ISE-PIC Release 3.4 (Fixed in 3.4 Patch 2)

There is no evidence that the vulnerability has been exploited in a malicious context. That said, it's always a good practice to ensure that systems are kept up-to-date to avoid potential threats.

The disclosure comes as The Shadowserver Foundation [reported](https://x.com/Shadowserver/status/1945407662805454871) that threat actors are likely exploiting [publicly released exploits](https://thehackernews.com/2025/07/fortinet-releases-patch-for-critical.html) associated with CVE-2025-25257 to drop web shells on susceptible Fortinet FortiWeb instances since July 11, 2025.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As of July 15, there are [estimated](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=7&source=compromised_iot&source=compromised_website&source=compromised_website6&tag=fortiweb-compromised%2B&dataset=unique_ips&limit=100&group_by=geo&stacking=stacked&auto_update=on) to be 77 infected instances, down from 85 the day before. The majority of the compromises are concentrated around North America (44), Asia (14), and Europe (13).

Data from the attack surface management platform Censys shows that there are 20,098 Fortinet FortiWeb appliances online, excluding honeypots, although it's currently not known how many of these are vulnerable to CVE-2025-25257.

"This flaw enables unauthenticated attackers to execute arbitrary SQL commands via crafted HTTP requests, leading to remote code execution (RCE)," Censys [said](https://censys.com/advisory/cve-2025-25257).

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

[cisco](https://thehackernews.com/search/label/cisco)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Fortinet](https://thehackernews.com/search/label/Fortinet)[network security](https://thehackernews.com/search/label/network%20security)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos:...