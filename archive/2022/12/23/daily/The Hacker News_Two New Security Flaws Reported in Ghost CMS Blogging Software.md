---
title: Two New Security Flaws Reported in Ghost CMS Blogging Software
url: https://thehackernews.com/2022/12/two-new-security-flaws-reported-in.html
source: The Hacker News
date: 2022-12-23
fetch_date: 2025-10-04T02:23:38.639010
---

# Two New Security Flaws Reported in Ghost CMS Blogging Software

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

# [Two New Security Flaws Reported in Ghost CMS Blogging Software](https://thehackernews.com/2022/12/two-new-security-flaws-reported-in.html)

**Dec 22, 2022**Ravie LakshmananWebsite Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFGDCfmj2ulxTT_aOBhz1mYaybmVN0KDOnq2eJZdz0u9KeNeTxlZPsxnMzLRzo60NfSgiBCDoMJ86HwXjm4fDdSNbl7Ev8odE88_oHB-YkUg_dAIT2ZGZpLF2ldEXcj2OEKJdJ3BTT8o5Dek52yZUMUXQ_vsPd40onj2zT7zhBJeDxAKkZR6lz6nXh/s790-rw-e365/ghostcms.png)

Cybersecurity researchers have detailed two security flaws in the JavaScript-based blogging platform known as [Ghost](https://ghost.org/explore/), one of which could be abused to elevate privileges via specially crafted HTTP requests.

Ghost is an open source blogging platform that's [used](https://trends.builtwith.com/cms/Ghost) in more than 52,600 live websites, most of them located in the U.S., the U.K., German, China, France, Canada, and India.

Tracked as CVE-2022-41654 (CVSS score: 9.6), the authentication bypass vulnerability allows unprivileged users (i.e., members) to make unauthorized modifications to newsletter settings.

Cisco Talos, which [discovered](https://blog.talosintelligence.com/vulnerability-spotlight-authentication-bypass-and-enumeration-vulnerabilities-in-ghost-cms/) the shortcoming, said it could enable a member to change the system-wide default newsletter that all users are subscribed to by default.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Even worse, the ability of a site administrator to inject JavaScript into the newsletter by default could be exploited to trigger the creation of arbitrary administrator accounts when attempting to edit the newsletter.

"This gives unprivileged users the ability to view and change settings they were not intended to have access to," Ghost [noted](https://github.com/TryGhost/Ghost/security/advisories/GHSA-9gh8-wp53-ccc6) in an advisory published on November 28, 2022. "They are not able to escalate their privileges permanently or get access to further information."

The CMS platform blamed the bug due to a "gap" in its API validation, adding it found no evidence that the issue has been exploited in the wild.

Also patched by Ghost is an enumeration vulnerability in the login functionality (CVE-2022-41697, CVSS score: 5.3) that could lead to the disclosure of sensitive information.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Per Talos, this flaw could be leveraged by an attacker to enumerate all valid users of Ghost by supplying an email address, which could then be used to narrow down potential targets for a next-stage phishing attack.

The flaws have been addressed in the Ghost (Pro) managed hosting service, but users who self-host the service and run a version between 4.46.0 and 4.48.7 or any version of v5 up to and including 5.22.6 are required to update to versions 4.48.8 and 5.22.7.

*(The story has been updated with a revised CVSS score for CVE-2022-41654 based on an advisory issued by Cisco Talos.)*

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

[Ghost CMS](https://thehackernews.com/search/label/Ghost%20CMS)[JavaScript](https://thehackernews.com/search/label/JavaScript)[software security](https://thehackernews.com/search/label/software%20security)

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

Fortra GoAnywhere CVSS 10 Flaw Ex...