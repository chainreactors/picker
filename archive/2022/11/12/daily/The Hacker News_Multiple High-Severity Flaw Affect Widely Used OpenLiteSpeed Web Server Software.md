---
title: Multiple High-Severity Flaw Affect Widely Used OpenLiteSpeed Web Server Software
url: https://thehackernews.com/2022/11/multiple-high-severity-flaw-affect.html
source: The Hacker News
date: 2022-11-12
fetch_date: 2025-10-03T22:35:27.715404
---

# Multiple High-Severity Flaw Affect Widely Used OpenLiteSpeed Web Server Software

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

# [Multiple High-Severity Flaws Affect Widely Used OpenLiteSpeed Web Server Software](https://thehackernews.com/2022/11/multiple-high-severity-flaw-affect.html)

**Nov 11, 2022**Ravie Lakshmanan

[![OpenLiteSpeed Web Server](data:image/png;base64... "OpenLiteSpeed Web Server")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_-EdJeU_uVILW_99oksRiZ_uPgG3VJmHeQ002SkTQR8VlICYqzqubVg_iehAPxBUlIx3eejWZayKuS2QJP_L5mDr1fgXnr_Y_GEWEqFy0dISfIsb3GRq_MGhMO7ODnw1eKASFlR7_BKiDKX5YggHalvA4P_6PkSaBwHalVGe0ZHro4W00z94Uyxpy/s790-rw-e365/openlitespeed.jpg)

Multiple high-severity flaws have been uncovered in the open source OpenLiteSpeed Web Server as well as its enterprise variant that could be weaponized to achieve remote code execution.

"By chaining and exploiting the vulnerabilities, adversaries could compromise the web server and gain fully privileged remote code execution," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/openlitespeed-vulnerabilities/) in a Thursday report.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[OpenLiteSpeed](https://github.com/litespeedtech/openlitespeed), the open source edition of LiteSpeed Web Server, is the sixth most popular web server, accounting for 1.9 million unique servers across the world.

The first of the three flaws is a directory traversal flaw ([CVE-2022-0072](https://github.com/advisories/GHSA-f532-g5cf-vhjp), CVSS score: 5.8), which could be exploited to access forbidden files in the web root directory.

[![OpenLiteSpeed Web Server](data:image/png;base64... "OpenLiteSpeed Web Server")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7Ke9JG7VFmHuM_E44E1E4S4rIkfWT1YECTBzJVtSIEYha-eJiYbAGIszJovcG0-VyYX2EpkaO_Yn9yUTV70GMpPWE6E5uFIdy7cRUk9McqSUn--dcg23bM9zpFgUzvKUSP3sitl9HSbU6GmufADhGph_DeRERGFVDhPtSx_HKk0F_-Yf5e6y2nHko/s790-rw-e365/hack.jpg)

The remaining two vulnerabilities ([CVE-2022-0073](https://github.com/advisories/GHSA-p42f-x6hp-xv84) and [CVE-2022-0074](https://github.com/advisories/GHSA-p85c-c374-mg9g), CVSS scores: 8.8) relate to a case of privilege escalation and command injection, respectively, that could be chained to achieve privileged code execution.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"A threat actor who managed to gain the credentials to the dashboard, whether by brute-force attacks or social engineering, could exploit the vulnerability in order to execute code on the server," Unit 42 researchers Artur Avetisyan, Aviv Sasson, Ariel Zelivansky, and Nathaniel Quist said of CVE-2022-0073.

Multiple versions of OpenLiteSpeed (from 1.5.11 up to 1.7.16) and LiteSpeed (from 5.4.6 up to 6.0.11) are impacted by the issues, which have been addressed in versions [1.7.16.1](https://github.com/litespeedtech/openlitespeed/releases) and [6.0.12](https://store.litespeedtech.com/store/index.php?rp=/announcements/451) following responsible disclosure on October 4, 2022.

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

[LiteSpeed Server](https://thehackernews.com/search/label/LiteSpeed%20Server)[OpenLiteSpeed](https://thehackernews.com/search/label/OpenLiteSpeed)[web server](https://thehackernews.com/search/label/web%20server)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.ht...