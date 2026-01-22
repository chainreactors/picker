---
title: Zoom and GitLab Release Security Updates Fixing RCE, DoS, and 2FA Bypass Flaws
url: https://thehackernews.com/2026/01/zoom-and-gitlab-release-security.html
source: The Hacker News
date: 2026-01-21
fetch_date: 2026-01-22T03:36:33.401008
---

# Zoom and GitLab Release Security Updates Fixing RCE, DoS, and 2FA Bypass Flaws

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

# [Zoom and GitLab Release Security Updates Fixing RCE, DoS, and 2FA Bypass Flaws](https://thehackernews.com/2026/01/zoom-and-gitlab-release-security.html)

**Ravie Lakshmanan**Jan 21, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwPQt59QKpm9rpNLriqoUsKPzbWcBj9P-u1ZdIn5xhxR6hgRztxdSAXN5bgEnDvd4uEEBgW4Imr_g-__YN0NY3-vLa_vEuYIwRzlrnRF3s0Vz8wDb937XfoxDbpPFapWvz0wH5TO2rK-32zQ2WLv8_loqE9rZIn_x5RzgtTyxrOQcUN-POOgDziDZNngjf/s1600-e365/zoom-gitlab.jpg)

Zoom and GitLab have released security updates to resolve a number of security vulnerabilities that could result in denial-of-service (DoS) and remote code execution.

The most severe of the lot is a critical security flaw impacting Zoom Node Multimedia Routers (MMRs) that could permit a meeting participant to conduct remote code execution attacks. The vulnerability, tracked as **CVE-2026-22844** and discovered internally by its Offensive Security team, carries a CVSS score of 9.9 out of 10.0.

"A command injection vulnerability in Zoom Node Multimedia Routers (MMRs) before version 5.2.1716.0 may allow a meeting participant to conduct remote code execution of the MMR via network access," the company [noted](https://www.zoom.com/en/trust/security-bulletin/zsb-26001/) in a Tuesday alert.

Zoom is recommending that customers using Zoom Node Meetings, Hybrid, or Meeting Connector deployments update to the latest available MMR version to safeguard against any potential threat.

There is no evidence that the security flaw has been exploited in the wild. The vulnerability affects the following versions -

* Zoom Node Meetings Hybrid (ZMH) MMR module versions prior to 5.2.1716.0
* Zoom Node Meeting Connector (MC) MMR module versions prior to 5.2.1716.0

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

### GitLab Releases Patches for Severe Flaws

The disclosure comes as GitLab [released](https://about.gitlab.com/releases/2026/01/21/patch-release-gitlab-18-8-2-released/) fixes for multiple high-severity flaws affecting its Community Edition (CE) and Enterprise Edition (EE) that could result in DoS and a bypass of two-factor authentication (2FA) protections. The shortcomings are listed below -

* **CVE-2025-13927** (CVSS score: 7.5) - A vulnerability that could allow an unauthenticated user to create a DoS condition by sending crafted requests with malformed authentication data (Affects all versions from 11.9 before 18.6.4, 18.7 before 18.7.2, and 18.8 before 18.8.2)
* **CVE-2025-13928** (CVSS score: 7.5) - An incorrect authorization vulnerability in the Releases API that could allow an unauthenticated user to cause a DoS condition (Affects all versions from 17.7 before 18.6.4, 18.7 before 18.7.2, and 18.8 before 18.8.2)
* **CVE-2026-0723** (CVSS score: 7.4) - A vulnerability that could allow an individual with existing knowledge of a victim's credential ID to bypass 2FA by submitting forged device responses (Affects all versions from 18.6 before 18.6.4, 18.7 before 18.7.2, and 18.8 before 18.8.2 )

Also remediated by GitLab are two other medium-severity bugs that could also trigger a DoS condition (CVE-2025-13335, CVSS score: 6.5, and CVE-2026-1102, CVSS score: 5.3) by configuring malformed Wiki documents that bypass cycle detection and sending repeated malformed SSH authentication requests, respectively.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[denial of service](https://thehackernews.com/search/label/denial%20of%20service)[Gitlab](https://thehackernews.com/search/label/Gitlab)[network security](https://thehackernews.com/search/label/network%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[two-factor authentication](https://thehackernews.com/search/label/two-factor%20authentication)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Zoom](https://thehackernews.com/search/label/Zoom)

Trending News

[![⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More")

⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](https://thehackernews.com/2026/01/weekly-recap-fortinet-exploits-redline.html)

[![n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](data:image/svg+xml;base64... "n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens")

n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)

[![New Advanced Linux VoidLink Malware Targets Cloud and container Environments](data:image/svg+xml;base64... "New Advanced Linux VoidLink Malware Targets Cloud and container Environments")

New Advanced Linux VoidLink Malware Targets Cloud and container Environments](https://thehackernews.com/2026/01/new-advanced-linux-voidlink-malware.html)

[![Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow](data:image/svg+xml;base64... "Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow")

Critical Node.js Vulnerability Can Cause Server Crashes via async\_hooks Stack Overflow](https://thehackernews.com/2026/01/critical-nodejs-vulnerability-can-cause.html)

[![Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution...