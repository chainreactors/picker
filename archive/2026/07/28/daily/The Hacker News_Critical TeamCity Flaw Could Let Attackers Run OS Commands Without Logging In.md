---
title: Critical TeamCity Flaw Could Let Attackers Run OS Commands Without Logging In
url: https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html
source: The Hacker News
date: 2026-07-28
fetch_date: 2026-07-29T05:04:27.407185
---

# Critical TeamCity Flaw Could Let Attackers Run OS Commands Without Logging In

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Critical TeamCity Flaw Could Let Attackers Run OS Commands Without Logging In](https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html)

**Ravie Lakshmanan**Jul 28, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiX3xcF2Bm9BY5obe-T5JItuKynq8bPijOxp14p5damNEjPGtAbYyuLSqp6vKN_KkhPx1qYeTXHxpgnZllCrtLvDaDuJNyHpY1qV0i8KWCe79_bnFtBtTRPCTU28LcN7OFM26h_WZdxeM3KPWBK4dlp0jY8JKrs1UILNR0qRgtxhKJqCcrht69sc3gcwsU/s1700-e365/tc.jpg)

JetBrains is [urging customers](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/) of on-premise versions of TeamCity to update to the latest version following the discovery of a critical security issue that could result in arbitrary code execution.

The vulnerability, assigned **CVE-2026-63077** (CVSS score: 9.8), affects all TeamCity On-Premises versions. It has been addressed in versions 2025.11.7 and 2026.1.3. TeamCity Cloud instances have already been updated. JetBrains has credited Antoni Tremblay with discovering and reporting the flaw on July 10, 2026.

"If exploited, this flaw may enable an unauthenticated attacker with HTTP(S) access to a TeamCity server to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process," JetBrains said.

The flaw allows unauthenticated remote code execution via the agent polling protocol to sidestep authentication checks and achieve command execution. Depending on the privileges granted to the TeamCity server process, a successful compromise can lead to the exposure of TeamCity data, configurations, and stored credentials, or modification of server state.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Besides releasing versions 2025.11.7 and 2026.1.3, JetBrains has released a [security patch plugin](https://download.jetbrains.com/teamcity/plugins/internal/fix_CVE_2026_63077.zip) for versions 2017.1+ so that customers who are unable to apply an update can still patch their environments. There is no evidence to indicate that the flaw has been exploited in the wild.

"The security patch plugin will address only the vulnerability described above (CVE-2026-63077)," JetBrains cautioned. "We always recommend upgrading your server to the latest version to benefit from many other security updates."

As best practices, customers are advised to consider requiring VPN connections or implementing an extra layer of security to prevent unauthorized access to internet-facing TeamCity servers.

"Even exposing the TeamCity login screen or REST API can provide attackers with potential entry points to exploit newly disclosed vulnerabilities," it added.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Authentication bypass](https://thehackernews.com/search/label/Authentication%20bypass), [CI/CD Security](https://thehackernews.com/search/label/CI/CD%20Security), [DevOps](https://thehackernews.com/search/label/DevOps), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [server security](https://thehackernews.com/search/label/server%20security), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](data:image/svg+xml;base64... "New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit")

New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](https://thehackernews.com/2026/07/new-bit2watt-attack-could-let-cloud.html)

[![Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](data:image/svg+xml;base64... "Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs")

Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html)

[![Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC](data:image/svg+xml;base64... "Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC")

Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC](https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html)

[![AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code](data:image/svg+xml;base64... "AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code")

AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code](https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html)

[![Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs](data:image/svg+xml;base64... "Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs")

Apple Fixes Hide My Email Bug That Exposed Real ...