---
title: Researchers Detail New Attack Method to Bypass Popular Web Application Firewalls
url: https://thehackernews.com/2022/12/researchers-detail-new-attack-method-to.html
source: The Hacker News
date: 2022-12-11
fetch_date: 2025-10-04T01:13:03.462464
---

# Researchers Detail New Attack Method to Bypass Popular Web Application Firewalls

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

# [Researchers Detail New Attack Method to Bypass Popular Web Application Firewalls](https://thehackernews.com/2022/12/researchers-detail-new-attack-method-to.html)

**Dec 10, 2022**Ravie LakshmananWeb App Firewall / Web Security

[![Web Application Firewalls](data:image/png;base64... "Web Application Firewalls")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-w1xVYrSGCATjd9jsHC3v5VXTA751frowKneHnwHdZboKBmNawRO13DAlhw1m0U7Fedd6aOgj7lJfBsEvT6qpjOpxXq9mM4q46-B8SJVQO5EP6KPbClgqIQEAMat-YhqUXSJE_oDa2w9yte9pW9G1PJfu4tBbeqaVkFE4ow1uf1_ZRGRrglyKQ2Ja/s790-rw-e365/web-app-firewall.png)

A new attack method can be used to circumvent web application firewalls (WAFs) of various vendors and infiltrate systems, potentially enabling attackers to gain access to sensitive business and customer information.

Web application firewalls are a [key line of defense](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/) to help filter, monitor, and block HTTP(S) traffic to and from a web application, and safeguard against attacks such as cross-site forgery, cross-site-scripting (XSS), file inclusion, and SQL injection (SQLi).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The generic bypass "involves appending [JSON syntax](https://en.wikipedia.org/wiki/JSON) to SQL injection payloads that a WAF is unable to parse," Claroty researcher Noam Moshe [said](https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf). "Most WAFs will easily detect SQLi attacks, but prepending JSON to SQL syntax left the WAF blind to these attacks."

The industrial and IoT cybersecurity company said its technique successfully worked against WAFs from vendors like Amazon Web Services (AWS), Cloudflare, F5, Imperva, and Palo Alto Networks, all of whom have since released updates to support JSON syntax during SQL injection inspection.

[![Web Application Firewalls](data:image/png;base64... "Web Application Firewalls")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9QEvMZoDsVWLSbI8shJ0ash5MHSxO7TxBujP2pZ8p1QtL2sQwn1T93EM5nnar0SPoMzlxlQR0S4Z8_LslUw5tc9oE4iaJSufUQX60-37EGfvzh5dlaqQJU_iVcrUEZoY_QzG9YIgzF1X2SaMe3aTFEsgiBGE64jL0_bc8xxIiLnYvegtT1RSuXXoZ/s790-rw-e365/code.png)

With WAFs acting as a security guardrail against malicious external HTTP(S) traffic, an attacker with capabilities to get past the barrier can obtain initial access to a target environment for further post-exploitation.

The bypass mechanism devised by Claroty banks on the lack of JSON support for WAFs to craft rogue SQL injection payloads that include JSON syntax to skirt the protections.

"Attackers using this novel technique could access a backend database and use additional vulnerabilities and exploits to exfiltrate information via either direct access to the server or over the cloud," Moshe explained. "This is a dangerous bypass, especially as more organizations continue to migrate more business and functionality to the cloud."

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

[Amazon Web Services](https://thehackernews.com/search/label/Amazon%20Web%20Services)[Claroty](https://thehackernews.com/search/label/Claroty)[CloudFlare](https://thehackernews.com/search/label/CloudFlare)[F5](https://thehackernews.com/search/label/F5)[Imperva](https://thehackernews.com/search/label/Imperva)[iot security](https://thehackernews.com/search/label/iot%20security)[Palo Alto Networks](https://thehackernews.com/search/label/Palo%20Alto%20Networks)[Web Application Firewall](https://thehackernews.com/search/label/Web%20Application%20Firewall)[website security](https://thehackernews.com/search/label/website%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom an...