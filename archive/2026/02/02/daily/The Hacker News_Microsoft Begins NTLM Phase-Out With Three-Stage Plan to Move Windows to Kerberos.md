---
title: Microsoft Begins NTLM Phase-Out With Three-Stage Plan to Move Windows to Kerberos
url: https://thehackernews.com/2026/02/microsoft-begins-ntlm-phase-out-with.html
source: The Hacker News
date: 2026-02-02
fetch_date: 2026-02-03T04:11:06.245695
---

# Microsoft Begins NTLM Phase-Out With Three-Stage Plan to Move Windows to Kerberos

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Microsoft Begins NTLM Phase-Out With Three-Stage Plan to Move Windows to Kerberos](https://thehackernews.com/2026/02/microsoft-begins-ntlm-phase-out-with.html)

**Ravie Lakshmanan**Feb 02, 2026Kerberos / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZOf9qxdul5asVTIVQe4P6l_tPfVmbnsfVrt3cNmU3_q5qDeFcqXdve4AgXe-z7gCGozXQ3z0wDZnXn_-bynodpDfeUQaM5T4CFWpZUcGsbD-R-JS93Jp_1R37WQkCU4gLLpFjDxkN6T2DpAXXthKXl4QDIe_D486n18bp4_yyxt2DuVz2-zLjTybVQFDS/s1700-e365/windows.jpg)

Microsoft has [announced](https://techcommunity.microsoft.com/blog/windows-itpro-blog/advancing-windows-security-disabling-ntlm-by-default/4489526) a three-phase approach to phase out New Technology LAN Manager (NTLM) as part of its efforts to shift Windows environments toward stronger, Kerberos-based options.

The development comes more than two years after the tech giant [revealed](https://thehackernews.com/2023/10/microsoft-to-phase-out-ntlm-in-favor-of.html) its plans to deprecate the legacy technology, citing its susceptibility to weaknesses that could facilitate relay attacks and allow bad actors to gain unauthorized access to network resources. NTLM was [formally deprecated](https://thehackernews.com/2024/05/windows-11-to-deprecate-ntlm-add-ai.html) in [June 2024](https://learn.microsoft.com/en-us/windows/whats-new/deprecated-features#deprecated-features) and no longer receives updates.

"NTLM consists of security protocols originally designed to provide authentication, integrity, and confidentiality to users," Mariam Gewida, Technical Program Manager II at Microsoft, explained. "However, as security threats have evolved, so have our standards to meet modern security expectations. Today, NTLM is susceptible to various attacks, including replay and man-in-the-middle attacks, due to its use of weak cryptography."

Despite the deprecated status, Microsoft said it continues to find the use of NTLM prevalent in enterprise environments where modern protocols like Kerberos cannot be implemented due to legacy dependencies, network limitations, or ingrained application logic. This, in turn, exposes organizations to security risks, such as replay, relay, and pass-the-hash attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

To mitigate this problem in a secure manner, the company has adopted a three-phase strategy that paves the way for NTLM to be disabled by default -

* Phase 1: Building visibility and control using [enhanced NTLM auditing](https://support.microsoft.com/en-us/topic/overview-of-ntlm-auditing-enhancements-in-windows-11-version-24h2-and-windows-server-2025-b7ead732-6fc5-46a3-a943-27a4571d9e7b) to better understand where and why NTLM is still being used (Available now)
* Phase 2: Addressing common roadblocks that prevent a migration to NTLM through features like IAKerb and local Key Distribution Center (KDC) (pre-release), as well as updating core Windows components to prioritize Kerberos authentication (Expected in H2 2026)
* Phase 3: Disabling NTLM in the next version of Windows Server and associated Windows client, and requiring explicit re-enablement through new policy controls

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRB4jSKT-ymw8T7BbMuZngCqPMWAfkqTfAN0SRyiheEw8PuAq9Mr-2WfA16Pp8PlfY_T6J01NgwGbuQsKnMilLvVWcGTu_ZsGHlGUv3sE5cJJgNhARGqLWcYeqJKBZ2RncOGHBWriZsGlnwCgV1Jp6988r08kY3r3gITwa9Ywj80URYIrd74zLVvA3U_7b/s1700-e365/ntlm-timeline.png)

Microsoft has positioned the transition as a major step toward a passwordless, phishing-resistant future. This also requires organizations relying on NTLM to conduct audits, map dependencies, migrate to Kerberos, test NTLM-off configurations in non-production environments, and enable Kerberos upgrades.

"Disabling NTLM by default does not mean completely removing NTLM from Windows yet," Gewida said. "Instead, it means that Windows will be delivered in a secure-by-default state where network NTLM authentication is blocked and no longer used automatically."

"The OS will prefer modern, more secure Kerberos-based alternatives. At the same time, common legacy scenarios will be addressed through new upcoming capabilities such as Local KDC and IAKerb (pre-release)."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Kerberos](https://thehackernews.com/search/label/Kerberos), [Microsoft](https://thehackernews.com/search/label/Microsoft), [network security](https://thehackernews.com/search/label/network%20security), [NTLM](https://thehackernews.com/search/label/NTLM), [Windows](https://thehackernews.com/search/label/Windows)

Trending News

[![Critical Grist-Core Vulnerability Allows RCE Attacks via Spreadsheet Formulas](data:image/svg+xml;base64... "Critical Grist-Core Vulnerability Allows RCE Attacks via Spreadsheet Formulas")

Critical Grist-Core Vulnerability Allows RCE Attacks via Spreadsheet Formulas](https://thehackernews.com/2026/01/critical-grist-core-vulnerability.html)

[![Microsoft Office Zero-Day (CVE-2026-21509) - Em...