---
title: CISA Flags Critical WatchGuard Fireware Flaw Exposing 54,000 Fireboxes to No-Login Attacks
url: https://thehackernews.com/2025/11/cisa-flags-critical-watchguard-fireware.html
source: The Hacker News
date: 2025-11-13
fetch_date: 2025-11-14T03:13:42.756888
---

# CISA Flags Critical WatchGuard Fireware Flaw Exposing 54,000 Fireboxes to No-Login Attacks

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [CISA Flags Critical WatchGuard Fireware Flaw Exposing 54,000 Fireboxes to No-Login Attacks](https://thehackernews.com/2025/11/cisa-flags-critical-watchguard-fireware.html)

**Nov 13, 2025**Ravie LakshmananVulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPj6dtQtZKcXl4TjnJfg2t7WniTYLkQ1NLwaQzVB6A-EXj3b3kn6ZGSrAi4AkjkI2HcbdmEGePORP5d1Z7b2awdGjIQD9TCCOPr0YLUUjU4Bazi9LsKY3f0XNvp343duOjEucfDaZaOlkV3tMntsNHp5ilw6Uef2D6_tt2nl3pgbVkQXwH6edgVhUuD8SQ/s790-rw-e365/firewall1.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday [added](https://www.cisa.gov/news-events/alerts/2025/11/12/cisa-adds-three-known-exploited-vulnerabilities-catalog) a critical security flaw impacting **WatchGuard Fireware** to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, based on evidence of active exploitation.

The vulnerability in question is CVE-2025-9242 (CVSS score: 9.3), an out-of-bounds write vulnerability affecting Fireware OS 11.10.2 up to and including 11.12.4\_Update1, 12.0 up to and including 12.11.3 and 2025.1. It was patched by WatchGuard in September.

"WatchGuard Firebox contains an out-of-bounds write vulnerability in the OS iked process that may allow a remote unauthenticated attacker to execute arbitrary code," CISA said in an advisory.

Details of the vulnerability were [shared](https://thehackernews.com/2025/10/researchers-uncover-watchguard-vpn-bug.html) by watchTowr Labs last month, with the cybersecurity company stating that the issue stems from a missing length check on an identification buffer used during the IKE handshake process.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"The server does attempt certificate validation, but that validation happens after the vulnerable code runs, allowing our vulnerable code path to be reachable pre-authentication," security researcher McCaulay Hudson noted.

In an [update to its advisory](https://www.watchguard.com/wgrd-psirt/advisory/wgsa-2025-00015) on October 21, 2025, WatchGuard said it has evidence suggesting active exploitation of the flaw, sharing three indicators of compromise (IoCs) associated with the activity -

* An IKE\_AUTH request log message with an abnormally large IKE\_AUTH request IDi payload greater than 100 bytes
* During a successful exploit, the iked process will hang, interrupting VPN connections
* After a failed or successful exploit, the iked process will crash and generate a fault report on the Firebox

According to [data](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=30&source=isakmp_vulnerable&source=isakmp_vulnerable6&tag=cve-2025-9242%2B&dataset=unique_ips&limit=100&group_by=geo&stacking=stacked&auto_update=on) from the Shadowserver Foundation, more than 54,300 Firebox instances remain vulnerable to the critical bug as of November 12, 2025, down from a high of 75,955 on October 19.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge8EZqFEbobGUpuLarkKHAb_CSkGuydTX0_qIcLmY6QvysmTFttEfcvUI-7gDtV7dPONWuXmtlBHp63rgrdIox3dxigwEO5L8RBqtFSOA8Np6byNMzStHLMzRqrpQ9YPAyTQnM_Q4FB1sYf5Ts7Oa1dYfjwoBKjN2P3q57qwl1to6lEYUqoWGdTR2pX0Fc/s790-rw-e365/1000033717.png) |
| Number of exposed WatchGuard Firebox instances |

Roughly 18,500 of these devices are in the U.S., the scans reveal. Italy (5,400), the U.K. (4,000), Germany (3,600), and Canada (3,000) round up the top five. Federal Civilian Executive Branch (FCEB) agencies are advised to apply WatchGuard's patches by December 3, 2025.

The development comes as CISA also added [CVE-2025-62215](https://thehackernews.com/2025/11/microsoft-fixes-63-security-flaws.html) (CVSS score: 7.0), a recently disclosed flaw in Windows kernel, and [CVE-2025-12480](https://thehackernews.com/2025/11/hackers-exploiting-triofox-flaw-to.html) (CVSS score: 9.1), an improper access control vulnerability in Gladinet Triofox, to the KEV catalog. Google's Mandiant Threat Defense team has attributed the exploitation of CVE-2025-12480 to a threat actor it tracks as UNC6485.

*(The story was updated after publication to include information from WatchGuard confirming active exploitation efforts.)*

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[exploit](https://thehackernews.com/search/label/exploit)[Fireware](https://thehackernews.com/search/label/Fireware)[network security](https://thehackernews.com/search/label/network%20security)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[WatchGuard](https://thehackernews.com/search/label/WatchGuard)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: Lazarus Hits Web3, Intel/AMD TEEs Cracked, Dark Web Leak Tool and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Laz...