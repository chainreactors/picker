---
title: Critical RCE Flaw Reported in Spotify's Backstage Software Catalog and Developer Platform
url: https://thehackernews.com/2022/11/critical-rce-flaw-reported-in-spotifys.html
source: The Hacker News
date: 2022-11-16
fetch_date: 2025-10-03T22:56:00.321951
---

# Critical RCE Flaw Reported in Spotify's Backstage Software Catalog and Developer Platform

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

# [Critical RCE Flaw Reported in Spotify's Backstage Software Catalog and Developer Platform](https://thehackernews.com/2022/11/critical-rce-flaw-reported-in-spotifys.html)

**Nov 15, 2022**Ravie Lakshmanan

[![Backstage Software Catalog and Developer Platform](data:image/png;base64... "Backstage Software Catalog and Developer Platform")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj78CnnxiTFZQfug-195AQePmJ3YmNvURpEfJ-BCiBoxol_nuWF2XAYsbtRZ_Gj_9hXUtu7WkmYvVdcfZd_L6gnPw1a4X279xD9vgUR_v8EMnBSmla00WzWa4e-A8E5x2JWOzMv7O7-NC8_Z4TJr4os1gOLSM5Q_17bBVfH8z5UhPoEGIu7oM8r3auX/s790-rw-e365/backstage.jpg)

Spotify's Backstage has been discovered as vulnerable to a severe security flaw that could be exploited to gain remote code execution by leveraging a recently disclosed bug in a third-party module.

The vulnerability (CVSS score: 9.8), at its core, takes advantage of a critical sandbox escape in vm2, a popular JavaScript sandbox library ([CVE-2022-36067](https://thehackernews.com/2022/10/researchers-detail-critical-rce-flaw.html) aka Sandbreak), that came to light last month.

"An unauthenticated threat actor can execute arbitrary system commands on a Backstage application by exploiting a vm2 sandbox escape in the Scaffolder core plugin," application security firm Oxeye said in a [report](https://www.oxeye.io/blog/remote-code-execution-in-spotifys-backstage) shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Backstage](https://github.com/backstage/backstage) is an open source [developer portal](https://backstage.io/blog/2020/03/16/announcing-backstage) from Spotify that allows users to create, manage, and explore software components from a unified "[front door](https://engineering.atspotify.com/2021/03/happy-birthday-backstage-spotifys-biggest-open-source-project-grows-up-fast/)." It's used by [many companies](https://github.com/backstage/backstage/blob/master/ADOPTERS.md) like Netflix, DoorDash, Roku, and Expedia, among others.

According to Oxeye, the flaw is rooted in a tool called [software templates](https://backstage.io/docs/features/software-templates/software-templates-index) that can be used to create components within Backstage.

|  |
| --- |
| [![Backstage Software Catalog and Developer Platform](data:image/png;base64... "Backstage Software Catalog and Developer Platform")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3b95O8NlskM61Bq_kwwgIwh0TSZFkQdLUWg9wMxiFvaFILgF1L7Efu7XPGdzUAxEDvE_aKrUI77i31InmrfnlsqjQMfIo1vj4quA4TaXMWQCdK8hmvxuYxuNkI1bdbhsyLmn-TDhkTunDph7fZ2mkF1aRiEsHYUx25jmVIX4R4Um-hh9_WtQlQw22/s790-rw-e365/code.jpg) |
| Screenshot shows Backstage calling the renderTemplate function (that calls renderString2) twice in the event of an error. |

While the template engine utilizes vm2 to mitigate the risk associated with running untrusted code, the sandbox escape flaw in the latter made it possible to execute arbitrary system commands outside of the security perimeter.

Oxeye said it was able to identify more than 500 publicly-exposed Backstage instances on the internet, which could then be remotely weaponized by an adversary without requiring any authorization.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Following responsible disclosure on August 18, the issue was addressed by the project maintainers in [version 1.5.1](https://github.com/backstage/backstage/releases/tag/v1.5.1) released on August 29, 2022.

"The root of any template-based VM escape is gaining JavaScript execution rights within the template," the Israeli company noted. "By using 'logic-less' template engines such as [Mustache](https://mustache.github.io/), you can avoid introducing server-side template injection vulnerabilities."

"Separating the logic from the presentation as much as possible can greatly reduce your exposure to the most dangerous template-based attacks," it further added.

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

[JavaScript](https://thehackernews.com/search/label/JavaScript)[Spotify Backstage](https://thehackernews.com/search/label/Spotify%20Backstage)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exp...