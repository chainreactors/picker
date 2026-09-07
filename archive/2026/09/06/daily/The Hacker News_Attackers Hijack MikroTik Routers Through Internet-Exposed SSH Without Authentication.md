---
title: Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication
url: https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html
source: The Hacker News
date: 2026-09-06
fetch_date: 2026-09-07T06:49:32.684798
---

# Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication

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

# [Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html)

**Swati Khandelwal**Sep 06, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiSiBDO5j21gorWS-UjrLlDl0RzniibBPjfO4xfPBBLbH1yTQIB88G-hUBRtYNufYwkPpVjWWLu0GXk1TB7pv_x8KbQCbfsL5Ft8JlZLa6iZfvuHU-vKSPNq5Li-e9DtoOvZIOXPYmibx9uc_imnug4ZJUog31KwlA3YKmY8ghOpROVQR8mwPj9qb-1kA/s1700-nu-rw-lo-l85-e365/micro.jpg)

Attackers are exploiting MikroTik routers with their Secure Shell (SSH) remote-access service, which is reachable from the internet, to gain full administrative control without authentication, according to [CERT Polska's attack warning](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/), published on September 5.

Successful attacks date to at least September 2. The Hacker News’s September 6 review of the warning found no victim count or attacker identity.

[MikroTik's security update](https://mikrotik.com/supportsec/september-2026-vulnerability/) lists fixed RouterOS releases. CERT says the fixes prevent the observed attacks and recommends immediate installation, followed by a check for unauthorized configuration changes.

According to the [vendor's default firewall explanation](https://forum.mikrotik.com/t/7-24-2-stable-is-released/272800), home MikroTik devices block public access to management ports while their default firewall rules remain intact.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The Hacker News checked CERT's [affected RouterOS versions](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve/) against MikroTik's listed fixes on September 6. Use the [official RouterOS downloads](https://mikrotik.com/download) for your update.

| Affected range reported by CERT | Initial security fix | Update guidance |
| --- | --- | --- |
| From 6.0.0 below 6.49.21 | 6.49.21 | RouterOS 6 security release |
| From 7.0.0 below 7.23.4 | 7.23.4 | Use 7.23.5 on the long-term channel |
| From 7.24 below 7.24.2 | 7.24.2 | Stable channel security release |
| No development range listed in CERT’s disclosure | 7.25beta3 | Development channel fix |

The [7.23.5 regression fix](https://forum.mikrotik.com/t/7-23-5-long-term-is-released/272867) addresses an IPv6 DHCP (Dynamic Host Configuration Protocol) problem introduced in 7.23.4 while retaining the security update.

Until the update can be installed, CERT recommends turning off exposed services or restricting access to trusted management networks, particularly for SSH, WWW/WWW-SSL, and bandwidth-test.

It also advises against initiating Transport Layer Security (TLS) connections or using RouterOS's built-in SSH clients from an unpatched device. These temporary restrictions cover the broader set of vulnerabilities and do not replace the update.

MikroTik's [Flagged status guidance](https://manual.mikrotik.com/docs/system-information-and-utilities/device-mode) states that RouterOS flags a device when startup checks detect suspicious configuration. RouterOS disables those entries and restricts certain functions.

After updating, check the logs and run /system/device-mode/print to inspect that status. Even without a warning, inspect the configuration for unknown users, scripts, and other unrecognized changes.

CERT also points to unexpected highly privileged ops accounts and account-creation logs containing ssh:-2@ as signs to investigate.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

If the warning, logs, or configuration suggest compromise, CERT recommends these recovery steps. Do not clear Flagged before preserving the evidence and completing the analysis.

1. Isolate the router from the network and preserve its logs and configuration before resetting it. CERT’s [preservation guide in Polish](https://wiedza.cert.pl/obsluga-incydentow/zabezpieczanie-danych/urzadzenia-sieciowe/zabezpieczanie-logow-i-konfiguracji-mikrotik/) explains how to export and download the files.
2. Restore factory settings and rebuild using a trusted, verified configuration. Do not blindly restore a full backup from the potentially compromised device.
3. Change passwords, keys and other secrets in use.

CERT calls the reported 2-flaw combination MikroTrick. The Hacker News compared CERT's warning and vulnerability disclosure on September 6. Neither explicitly identifies which 2 vulnerabilities form the observed chain or explains how they combine to give administrative control.

The [7.25beta3 release notes](https://forum.mikrotik.com/t/v7-25beta-development-is-released/272788) have a September 2 changelog date, while the beta and other initial fixes were announced on September 3. The Hacker News compared these release announcements with CERT’s attack timeline on September 6. Those dates do not establish whether a fix was publicly available before the attacks, so zero-day status remains unverified.

The Hacker News has contacted CERT Polska and MikroTik for comment.

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
[**Share on Telegram](#link_share...