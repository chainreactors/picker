---
title: Atlassian Releases Patches for Critical Flaws Affecting Crowd and Bitbucket Products
url: https://thehackernews.com/2022/11/atlassian-releases-patches-for-critical.html
source: The Hacker News
date: 2022-11-20
fetch_date: 2025-10-03T23:18:16.570578
---

# Atlassian Releases Patches for Critical Flaws Affecting Crowd and Bitbucket Products

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

# [Atlassian Releases Patches for Critical Flaws Affecting Crowd and Bitbucket Products](https://thehackernews.com/2022/11/atlassian-releases-patches-for-critical.html)

**Nov 19, 2022**Ravie Lakshmanan

[![Atlassian](data:image/png;base64... "Atlassian")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXWvoG3Wa2O4iFP8_YIndzkCWMmuv9PIBNhyHdxMESLUy5-NEOPklfY8GfEfsAjbezb2jW6-Cs1Z45TmiwQAGS2DdMEJQ3dKjOpoQCvPLHSXD_nsfTUIWxYqab5F2I2fwbAXTnwoiDg0XH7tszfZjRPJFQgQ0GVOFQ3-xRruQkpcGmW7oBIfz8Lfmo/s790-rw-e365/jira.jpg)

Australian software company Atlassian has rolled out security updates to address [two critical flaws](https://confluence.atlassian.com/security/november-2022-atlassian-security-advisories-overview-1167844594.html) affecting Bitbucket Server, Data Center, and Crowd products.

The issues, tracked as [**CVE-2022-43781**](https://confluence.atlassian.com/bitbucketserver/bitbucket-server-and-data-center-security-advisory-2022-11-16-1180141667.html) and [**CVE-2022-43782**](https://confluence.atlassian.com/crowd/crowd-security-advisory-november-2022-1168866129.html), are both rated 9 out of 10 on the CVSS vulnerability scoring system.

CVE-2022-43781, which Atlassian said was introduced in version 7.0.0 of Bitbucket Server and Data Center, affects versions 7.0 to 7.21 and 8.0 to 8.4 (only if mesh.enabled is set to false in bitbucket.properties).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The weakness has been described as a case of command injection using environment variables in the software, which could allow an adversary with permission to control their username to gain code execution on the affected system.

As a temporary workaround, the company is recommending users turn off the "Public Signup" option (Administration > Authentication).

"Disabling public signup would change the attack vector from an unauthenticated attack to an authenticated one which would reduce the risk of exploitation," it noted in an advisory. "ADMIN or SYS\_ADMIN authenticated users still have the ability to exploit the vulnerability when public signup is disabled."

The second vulnerability, CVE-2022-43782, concerns a misconfiguration in Crowd Server and Data Center that could permit an attacker to invoke privileged API endpoints, but only in scenarios where the bad actor is connecting from an IP address added to the Remote Address configuration.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Introduced in Crowd 3.0.0 and identified during an internal security review, the shortcoming impacts all new installations, meaning users who upgraded from a version prior to Crowd 3.0.0 are not vulnerable.

It's not uncommon for flaws in Atlassian and Bitbucket to be [subjected](https://thehackernews.com/2022/08/hackers-exploited-atlassian-confluence.html) to [active exploitation](https://thehackernews.com/2022/09/hackers-targeting-unpatched-atlassian.html) in the wild, making it imperative that users move quickly to apply the patches.

Last month, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [warned](https://thehackernews.com/2022/10/cisa-warns-of-hackers-exploiting.html) that a command injection flaw in Bitbucket Server and Data Center (CVE-2022-36804, CVSS score: 9.9) was being weaponized in attacks since late September 2022.

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

[Atlassian](https://thehackernews.com/search/label/Atlassian)[BitBucket](https://thehackernews.com/search/label/BitBucket)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a We...