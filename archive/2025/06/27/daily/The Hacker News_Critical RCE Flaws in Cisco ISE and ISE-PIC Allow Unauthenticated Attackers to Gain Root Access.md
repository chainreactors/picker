---
title: Critical RCE Flaws in Cisco ISE and ISE-PIC Allow Unauthenticated Attackers to Gain Root Access
url: https://thehackernews.com/2025/06/critical-rce-flaws-in-cisco-ise-and-ise.html
source: The Hacker News
date: 2025-06-27
fetch_date: 2025-10-06T22:57:06.179375
---

# Critical RCE Flaws in Cisco ISE and ISE-PIC Allow Unauthenticated Attackers to Gain Root Access

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

# [Critical RCE Flaws in Cisco ISE and ISE-PIC Allow Unauthenticated Attackers to Gain Root Access](https://thehackernews.com/2025/06/critical-rce-flaws-in-cisco-ise-and-ise.html)

**Jun 26, 2025**Ravie LakshmananVulnerability, Network Security

[![Unauthenticated Attackers to Gain Root Access](data:image/png;base64... "Unauthenticated Attackers to Gain Root Access")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4mmzQUSkTUltXoDoMWgSHlqS8WsX-pJCUiFi98MaGFXJFpZe09m_V5dxxiJA3LBRmhQ0HC5J9dOJjQ6IMvRmZKhM0dbXerRLQwVmZbeI_JgOgv19vJ3d3YHxXvVHQa_S7Gi1qYOWjQ2tYy7Ui7wq5JSj2DEAuVnFFTZ1MMsK2ZsVX_zqzpA41KGDq_AxR/s790-rw-e365/cisco.jpg)

Cisco has [released](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-unauth-rce-ZAd2GnJ6) updates to address two maximum-severity security flaws in Identity Services Engine (ISE) and ISE Passive Identity Connector (ISE-PIC) that could permit an unauthenticated attacker to execute arbitrary commands as the root user.

The vulnerabilities, assigned the CVE identifiers CVE-2025-20281 and CVE-2025-20282, carry a CVSS score of 10.0 each. A description of the defects is below -

* **CVE-2025-20281** - An unauthenticated remote code execution vulnerability affecting Cisco ISE and ISE-PIC releases 3.3 and later that could allow an unauthenticated, remote attacker to execute arbitrary code on the underlying operating system as root
* **CVE-2025-20282** - An unauthenticated remote code execution vulnerability affecting Cisco ISE and ISE-PIC release 3.4 that could allow an unauthenticated, remote attacker to upload arbitrary files to an affected device and execute those files on the underlying operating system as root

Cisco said CVE-2025-20281 is the result of insufficient validation of user-supplied input, which an attacker could exploit by sending a crafted API request to obtain elevated privileges and run commands.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In contrast, CVE-2025-20282 stems from a lack of file validation checks that would otherwise prevent the uploaded files from being placed in privileged directories.

"A successful exploit could allow the attacker to store malicious files on the affected system and then execute arbitrary code or obtain root privileges on the system," Cisco said.

The networking equipment vendor said there are no workarounds that address the issues. The shortcomings have been addressed in the below versions -

* **CVE-2025-20281** - Cisco ISE or ISE-PIC 3.3 Patch 6 (ise-apply-CSCwo99449\_3.3.0.430\_patch4-SPA.tar.gz), 3.4 Patch 2 (ise-apply-CSCwo99449\_3.4.0.608\_patch1-SPA.tar.gz)
* **CVE-2025-20282** - Cisco ISE or ISE-PIC 3.4 Patch 2 (ise-apply-CSCwo99449\_3.4.0.608\_patch1-SPA.tar.gz)

The company credited Bobby Gould of Trend Micro Zero Day Initiative and Kentaro Kawane of GMO Cybersecurity for reporting CVE-2025-20281. Kawane, who previously reported [CVE-2025-20286](https://thehackernews.com/2025/06/critical-cisco-ise-auth-bypass-flaw.html) (CVSS score: 9.9), has also been acknowledged for reporting CVE-2025-20282.

While there is no evidence that the vulnerabilities have been exploited in the wild, it's essential that users move quickly to apply the fixes to safeguard against potential threats.

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

[cisco](https://thehackernews.com/search/label/cisco)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[network security](https://thehackernews.com/search/label/network%20security)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: ...