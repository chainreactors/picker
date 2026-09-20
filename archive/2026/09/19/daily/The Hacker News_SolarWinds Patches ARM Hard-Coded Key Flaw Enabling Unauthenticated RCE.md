---
title: SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE
url: https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
source: The Hacker News
date: 2026-09-19
fetch_date: 2026-09-20T07:17:01.997045
---

# SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html)

**Ravie Lakshmanan**Sep 19, 2026Vulnerability / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXW-SaTg898BaxxlrDjSCrcm6ZYDgxoeuYCBY4QNWs6Nt5RhyphenhyphenCf4iSIyodz-7jk8rTqUT8hjlMT74dIf6ZjL_pD5NmiNbAHhsZwzw2rakJUDaU1tVeEvKw7Az3tMf34Xwh3ffToJeI1tpTQ8rAR8AvVn2XTupFgfhehb9sHClHDDGeDd4Y9z4oUf5CYPoS/s1700-nu-rw-lo-l85-e365/solar.jpg)

SolarWinds has released security updates to address a high-severity flaw in Access Rights Manager (ARM) that, if successfully exploited, could lead to an unauthenticated remote code execution vulnerability.

The vulnerability, tracked as **[CVE-2026-28326](https://www.solarwinds.com/trust-center/security-advisories/cve-2026-28326)**, is rated 8.8 out of 10.0 on the CVSS scoring system. The issue affects all versions of Access Rights Manager 2026.2 and prior.

"SolarWinds Access Rights Manager was reported to be affected by an unauthenticated remote code execution vulnerability," SolarWinds said in an advisory released on September 17, 2026. "The issue stems from a hard-coded static key."

The company credited Armadin security researcher Kai Huang with discovering and reporting the flaw, which has been [patched in ARM 2026.2.1](https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2026-2-1_release_notes.htm). SolarWinds makes no mention of the vulnerability being exploited in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

The development comes nearly two months after the company [shipped](https://www.solarwinds.com/trust-center/security-advisories) fixes for a critical flaw impacting Web Help Desk (WHD) (CVE-2026-28323, CVSS score: 9.8) that could result in a SAML authentication bypass when the SAML 2.0 authentication method is enabled.

Another vulnerability relates to a denial-of-service (DoS) vulnerability (CVE-2026-28299, CVSS score: 8.2) that could cause the Web Help Desk server to crash due to insufficient memory. Both issues have been resolved in WHD 2026.2.1.

SolarWinds has also released fixes for 16 flaws impacting Serv-U (CVE-2026-28302, from CVE-2026-28304 through CVE-2026-28317, CVE-2026-28321, CVE-2026-28323) that could lead to privilege escalation, remote code execution, and the creation of administrator accounts.

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

[enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Identity Security](https://thehackernews.com/search/label/Identity%20Security), [SolarWinds](https://thehackernews.com/search/label/SolarWinds), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

[![The Hacker News](data:image/svg+xml;base64...)

Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up](https://thehackernews.com/2026/09/google-gemini-broke-into-real-company.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads](https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html)

[![The Hacker News](data:image/svg+xml;base64...)

Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root](https://thehackernews.com/2026/09/public-exploits-released-for-four-linux.html)

[![The Hacker News](data:image/svg+xml;base64...)

New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html)

[![The Hacker News](data:image/svg+xml;base64...)

Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories](https://thehackernews.com/2026/09/threatsday-self-rewriting-agents-800.html)

[![The Hacker News](data:image/svg+xml;base64...)

Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)

[![The Hacker News](data:image/svg+xml;base64...)

Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers](https://thehackernews.com/2026/09/three-threat-groups-target-russian.html)

[![The Hacker News](data:image/svg+xml;base64...)

Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories](https://thehackern...