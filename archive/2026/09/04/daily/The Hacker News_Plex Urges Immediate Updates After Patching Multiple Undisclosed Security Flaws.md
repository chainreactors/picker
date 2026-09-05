---
title: Plex Urges Immediate Updates After Patching Multiple Undisclosed Security Flaws
url: https://thehackernews.com/2026/09/plex-urges-immediate-updates-after.html
source: The Hacker News
date: 2026-09-04
fetch_date: 2026-09-05T06:30:36.398542
---

# Plex Urges Immediate Updates After Patching Multiple Undisclosed Security Flaws

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

# [Plex Urges Immediate Updates After Patching Multiple Undisclosed Security Flaws](https://thehackernews.com/2026/09/plex-urges-immediate-updates-after.html)

**Ravie Lakshmanan**Sep 04, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7RQQCR9QxY1NZ80GCfpUjvGGcw9QDirshH7KrSyc097EIaNqLLVGgnnlOE095qTOt2q9CTu91gJ_Pf7Y9-AcZahb35e7XG2YrA8D4O0FPwVRSzBzMT5ecKzu0bnAxP603K5q8R_7IZrE-iSAAJQsmMWXBt8IPwHIIz3u6Kf-okZyo0G1fLoe9VOzZEEQF/s1700-nu-rw-lo-l85-e365/plex.jpg)

Plex is urging users to update their instances to the latest version following the release of an update that patches multiple security flaws.

The fixes are available in Plex Media Server 1.43.3 and Plex Desktop 1.115.0. The streaming media service did not elaborate on what those issues are, but said CVE identifiers have been requested for them.

"We recommend all server owners and Desktop users update to the latest version as soon as possible," Plex [said](https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319) in an announcement this week. "If you're running Plex Media Server on a NAS device, the updated version may not be available in their package manager yet, but you can install the package manually."

In August 2025, Plex [addressed](https://thehackernews.com/2025/09/weekly-recap-whatsapp-0-day-docker-bug.html#:~:text=Plex%20Servers%20Susceptible%20to%20New%20Flaw) a high-severity security flaw ([CVE-2025-34158](https://nvd.nist.gov/vuln/detail/cve-2025-34158), CVSS score: 8.5), an [authentication bug](https://github.com/lufinkey/vulnerability-research/blob/main/CVE-2025-34158/README.md) that stemmed from the "/myplex/account" endpoint incorrectly exposing the server owner's account details, including their administrative access token, even when accessed by any authenticated non-owner or lower-privileged user.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Additionally, a subsequent "/api/resources" API call can be used to reveal other servers accessible by that server owner, potentially exposing the owner's entire Plex infrastructure to unauthorized access. The combination of the two API calls creates an exploit chain that can lead to infrastructure discovery.

Data from Censys [shows](https://platform.censys.io/search?q=host.services.software%3A%28vendor%3A%22Plex%22+and+product%3A%22Media+Server%22%29+or+host.services.hardware%3A%28vendor%3A%22Plex%22+and+product%3A%22Media+Server%22%29+or+host.services.operating_systems%3A%28vendor%3A%22Plex%22+and+product%3A%22Media+Server%22%29) that there are more than 360,000 devices exposing the Plex Media Server web interface, although it's worth noting that not all of them are vulnerable.

Vulnerabilities in Plex Media Server have been exploited by threat actors from time to time. In February 2021, Plex released a security update to resolve an issue that allowed attackers to [cause an affected server](https://thehackernews.com/2021/02/cybercriminals-now-using-plex-media.html) to "reflect" UDP packets in order to increase the volume of a denial-of-service (DoS) attack against another server.

The hotfix ([Plex Media Server v1.21.3.4014 or newer](https://forums.plex.tv/t/security-regarding-ssdp-reflection-amplification-ddos/687162)) ensures that the server will only respond to UDP requests from the local network (LAN) and not the public internet (WAN).

Notably, the August 2022 breach of LastPass was [driven](https://thehackernews.com/2023/03/lastpass-hack-engineers-failure-to.html) by attackers implanting keylogger malware on an employee's home computer after compromising it through a Plex Media Server vulnerability (CVE-2020-5741, CVSS score: 7.2).

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

[network security](https://thehackernews.com/search/label/network%20security), [Plex](https://thehackernews.com/search/label/Plex), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account](https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More](https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html)

[![The Hacker News](data:image/svg+xml;base64...)

Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data](https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

WhatsApp Adds Multiple Passkeys for Phishing-Resistant Sign-Ins Across iOS and Android](https://thehackernews.com/2026/08/whatsapp-adds-multiple-passkeys-for.html)

[![The Hacker News](data:image/svg+xml;base64...)

A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw](https://thehackernews.com/2...