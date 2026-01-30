---
title: SolarWinds Fixes Four Critical Web Help Desk Flaws With Unauthenticated RCE and Auth Bypass
url: https://thehackernews.com/2026/01/solarwinds-fixes-four-critical-web-help.html
source: The Hacker News
date: 2026-01-29
fetch_date: 2026-01-30T04:04:27.401913
---

# SolarWinds Fixes Four Critical Web Help Desk Flaws With Unauthenticated RCE and Auth Bypass

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

# [SolarWinds Fixes Four Critical Web Help Desk Flaws With Unauthenticated RCE and Auth Bypass](https://thehackernews.com/2026/01/solarwinds-fixes-four-critical-web-help.html)

**Ravie Lakshmanan**Jan 29, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6GfPr6A1uY8KhmAw_BnWkdf6psUxmcTyTGGRQmw4LwX7cYRCH1CIS_hoATQj0ZLWSWI2brY2fVOsyx5vtncgWgg7D3KFpyIp4cazlOS1ByTGkRPY0ZjHBMelCGtrLsCktO8_bmIa48L8voQKre51yUDBaNY8qO_c-imAcN9Cj3FKLx3KQ12wYFxs0OOGV/s1700-e365/solarwinds.jpg)

SolarWinds has [released](https://www.solarwinds.com/trust-center/security-advisories) security updates to address multiple security vulnerabilities impacting SolarWinds Web Help Desk, including four critical vulnerabilities that could result in authentication bypass and remote code execution (RCE).

The list of vulnerabilities is as follows -

* **CVE-2025-40536** (CVSS score: 8.1) - A security control bypass vulnerability that could allow an unauthenticated attacker to gain access to certain restricted functionality
* **CVE-2025-40537** (CVSS score: 7.5) - A hard-coded credentials vulnerability that could allow access to administrative functions using the "client" user account
* **CVE-2025-40551** (CVSS score: 9.8) - An untrusted data deserialization vulnerability that could lead to remote code execution, which would allow an unauthenticated attacker to run commands on the host machine
* **CVE-2025-40552** (CVSS score: 9.8) - An authentication bypass vulnerability that could allow an unauthenticated attacker to execute actions and methods
* **CVE-2025-40553** (CVSS score: 9.8) - An untrusted data deserialization vulnerability that could lead to remote code execution, which would allow an unauthenticated attacker to run commands on the host machine
* **CVE-2025-40554** (CVSS score: 9.8) - An authentication bypass vulnerability that could allow an attacker to invoke specific actions within Web Help Desk

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

While Jimi Sebree from Horizon3.ai has been credited with discovering and reporting the first three vulnerabilities, watchTowr's Piotr Bazydlo has been acknowledged for the remaining three flaws. All the issues have been addressed in [WHD 2026.1](https://documentation.solarwinds.com/en/success_center/whd/content/release_notes/whd_2026-1_release_notes.htm).

"Both CVE-2025-40551 and CVE-2025-40553 are critical deserialization of untrusted data vulnerabilities that allow a remote unauthenticated attacker to achieve RCE on a target system and execute payloads such as arbitrary OS command execution," Rapid7 [said](https://www.rapid7.com/blog/post/etr-multiple-critical-solarwinds-web-help-desk-vulnerabilities-cve-2025-40551-40552-40553-40554/).

"RCE via deserialization is a highly reliable vector for attackers to leverage, and as these vulnerabilities are exploitable without authentication, the impact of either of these two vulnerabilities is significant."

While CVE-2025-40552 and CVE-2025-40554 have been described as authentication bypasses, they could also be leveraged to obtain RCE and achieve the same impact as the other two RCE deserialization vulnerabilities, the cybersecurity company added.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-HKei7OuHjmW4CwqV_dSO_wfZEMRBk_odLFhrqQgrR76y0U3GhpDJ-B0dnW7wbQHOMSE9t7MoZFpnABckyn6fjref3DUtuaL_melRae4tI-XMbZURF3EPkI-RTVS0wzwgRyb0MzMB0Jkgsq2o_SbhaFW5RFDHc08UzuYBjYhMVzowbemywiRYzdA1b2oZ/s1700-e365/solar.jpg)

In recent years, SolarWinds has released fixes to resolve several flaws in its Web Help Desk software, including [CVE-2024-28986](https://thehackernews.com/2024/08/solarwinds-releases-patch-for-critical.html), [CVE-2024-28987](https://thehackernews.com/2024/08/hardcoded-credential-vulnerability.html), [CVE-2024-28988, and CVE-2025-26399](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html). It's worth noting that CVE-2025-26399 addresses a patch bypass for CVE-2024-28988, which, in turn, is a [patch bypass](https://www.solarwinds.com/trust-center/security-advisories/cve-2024-28988) of CVE-2024-28986.

In late 2024, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://thehackernews.com/2024/10/cisa-warns-of-active-exploitation-in.html) CVE-2024-28986 and CVE-2024-28987 to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

In a post explaining CVE-2025-40551, Horizon3.ai's Sebree [described](https://horizon3.ai/attack-research/cve-2025-40551-another-solarwinds-web-help-desk-deserialization-issue/) it as yet another deserialization vulnerability stemming from the AjaxProxy functionality that could result in remote code execution. To achieve RCE, an attacker needs to carry out the following series of actions -

* Establish a valid session and extract key values
* Create a LoginPref component
* Set the state of the LoginPref component to allow us to access the file upload
* Use the JSONRPC bridge to create some malicious Java objects behind the scenes
* Trigger these malicious Java objects

With flaws in Web Help Desk having been weaponized in the past, it's essential that customers move quickly to update to the latest version of the help desk and IT service management platform.

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

[cybersecurity](https://thehackernews.com/search/label/...