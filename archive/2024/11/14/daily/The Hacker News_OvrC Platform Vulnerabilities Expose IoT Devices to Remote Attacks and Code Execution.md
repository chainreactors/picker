---
title: OvrC Platform Vulnerabilities Expose IoT Devices to Remote Attacks and Code Execution
url: https://thehackernews.com/2024/11/ovrc-platform-vulnerabilities-expose.html
source: The Hacker News
date: 2024-11-14
fetch_date: 2025-10-06T19:32:31.074791
---

# OvrC Platform Vulnerabilities Expose IoT Devices to Remote Attacks and Code Execution

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

# [OvrC Platform Vulnerabilities Expose IoT Devices to Remote Attacks and Code Execution](https://thehackernews.com/2024/11/ovrc-platform-vulnerabilities-expose.html)

**Nov 13, 2024**Ravie LakshmananCloud Security / Vulnerability

[![OvrC Platform Vulnerabilities](data:image/png;base64... "OvrC Platform Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYzZX7_Va9M1AzcOl_pvrUvmifGqxwCeTcpfRTe-H8-N8-eOSDpMaQmMjD-RPtyZiEhG7b236iUS20kDvyDd_ey0cYR1R0x5PdGv1zp-PiLxZkQNVfCBvtFxISnNdAcYrc8qOER230pAn9Lbx51mRwZ81ZFnnY8TrmkZkNQ6cKtqPVCItuF1hNBwBbWTj9/s790-rw-e365/mac.png)

A security analysis of the OvrC cloud platform has uncovered 10 vulnerabilities that could be chained to allow potential attackers to execute code remotely on connected devices.

"Attackers successfully exploiting these vulnerabilities can access, control, and disrupt devices supported by OvrC; some of those include smart electrical power supplies, cameras, routers, home automation systems, and more," Claroty researcher Uri Katz [said](https://claroty.com/team82/research/the-problem-with-iot-cloud-connectivity-and-how-it-exposed-all-ovrc-devices-to-hijacking) in a technical report.

Snap One's OvrC, pronounced "oversee," is advertised as a "revolutionary support platform" that enables homeowners and businesses to remotely manage, configure, and troubleshoot IoT devices on the network. According to its website, OvrC solutions are deployed at over 500,000 end-user locations.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to a [coordinated advisory](https://www.cisa.gov/news-events/ics-advisories/icsa-23-136-01) issued by the U.S. Cybersecurity and Infrastructure Security Agency (CISA), successful exploitation of the identified vulnerabilities could allow an attacker to "impersonate and claim devices, execute arbitrary code, and disclose information about the affected device."

The flaws have been found to impact OvrC Pro and OvrC Connect, with the company releasing fixes for eight of them in May 2023 and the remaining two on November 12, 2024.

"Many of these issues we found arise from neglecting the device-to-cloud interface," Katz said. "In many of these cases, the core issue is the ability to cross-claim IoT devices because of weak identifiers or similar bugs. These issues range from weak access controls, authentication bypasses, failed input validation, hardcoded credentials, and remote code execution flaws."

As a result, a remote attacker could abuse these vulnerabilities to bypass firewalls and gain unauthorized access to the cloud-based management interface. Even worse, the access could be subsequently weaponized to enumerate and profile devices, hijack devices, elevate privileges, and even run arbitrary code.

[![OvrC Platform Vulnerabilities](data:image/png;base64... "OvrC Platform Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6RKd98BkT1ZxhSoMe7bc0XULF9_Vzq43M3g9pPi4jvWKzKVa2TJYFSwKp_RFtSRAdKHDn8mcS335CopBBQAsoUCMqpekNAvwbyz0aJt3pksUyDEZz3LFqTEAGgkS8Oiemz4PfeqkzZqJq7oy2OMWlk-vNS36ODmHkCiHC25A0L0B_d5mrGrl_GqmoH8XW/s790-rw-e365/chart.png)

The most severe of the flaws are listed below -

* **CVE-2023-28649** (CVSS v4 score: 9.2), which allows an attacker to impersonate a hub and hijack a device
* **CVE-2023-31241** (CVSS v4 score: 9.2), which allows an attacker to claim arbitrary unclaimed devices by bypassing the requirement for a serial number
* **CVE-2023-28386** (CVSS v4 score: 9.2), which allows an attacker to upload arbitrary firmware updates resulting in code execution
* **CVE-2024-50381** (CVSS v4 score: 9.1), which allows an attacker to impersonate a hub and unclaim devices arbitrarily and subsequently exploit other flaws to claim it

"With more devices coming online every day and cloud management becoming the dominant means of configuring and accessing services, more than ever, the impetus is on manufacturers and cloud service providers to secure these devices and connections," Katz said. "The negative outcomes can impact connected power supplies, business routers, home automation systems and more connected to the OvrC cloud."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Nozomi Networks [detailed](https://www.nozominetworks.com/blog/security-flaws-discovered-in-goahead-might-affect-web-servers-over-embedded-iot-devices) three security flaws impacting EmbedThis [GoAhead](https://www.embedthis.com/goahead/), a compact web server used in embedded and IoT devices, that could lead to a denial-of-service (DoS) under specific conditions. The vulnerabilities (CVE-2024-3184, CVE-2024-3186, and CVE-2024-3187) have been patched in GoAhead version 6.0.1.

In recent months, multiple security shortcomings have also been [uncovered](https://www.nozominetworks.com/blog/vulnerabilities-in-johnson-controls-exacqvision-web-service-expose-security-systems-to-video-stream-hijacking) in Johnson Controls' exacqVision Web Service that could be combined to take control of video streams from surveillance cameras connected to the application and steal credentials.

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
[**Share on Telegram](#link...