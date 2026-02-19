---
title: Grandstream GXP1600 VoIP Phones Exposed to Unauthenticated Remote Code Execution
url: https://thehackernews.com/2026/02/grandstream-gxp1600-voip-phones-exposed.html
source: The Hacker News
date: 2026-02-18
fetch_date: 2026-02-19T04:22:07.946246
---

# Grandstream GXP1600 VoIP Phones Exposed to Unauthenticated Remote Code Execution

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Grandstream GXP1600 VoIP Phones Exposed to Unauthenticated Remote Code Execution](https://thehackernews.com/2026/02/grandstream-gxp1600-voip-phones-exposed.html)

**Ravie Lakshmanan**Feb 18, 2026Network Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJkDWw2o7gwfV4NseVpa6WnSALfRD1COOQfDjRYsORg5EN_NXyMNj43q0uSXkGZbgNC6kUJx-suEri4OMmg1v9UULThdAImIdK04DyIkj4iabnRcDqfl2bUXFWz-nsGeR7y8W0YC1ykqt3VauFhW7saH9iblk6kA8KTEKcG74A4fPWPf9BAmH4ifiiu2Hv/s1700-e365/root.jpg)

Cybersecurity researchers have disclosed a critical security flaw in the Grandstream GXP1600 series of VoIP phones that could allow an attacker to seize control of susceptible devices.

The vulnerability, tracked as **CVE-2026-2329**, carries a CVSS score of 9.3 out of a maximum of 10.0. It has been described as a case of unauthenticated stack-based buffer overflow that could result in remote code execution.

"A remote attacker can leverage CVE-2026-2329 to achieve unauthenticated remote code execution (RCE) with root privileges on a target device," Rapid7 researcher Stephen Fewer, who discovered and reported the bug on January 6, 2026, [said](https://www.rapid7.com/blog/post/ve-cve-2026-2329-critical-unauthenticated-stack-buffer-overflow-in-grandstream-gxp1600-voip-phones-fixed/).

According to the cybersecurity company, the issue is rooted in the device's web-based API service ("/cgi-bin/api.values.get") and is accessible in a default configuration without requiring authentication.

This endpoint is designed to fetch one or more configuration values from the phone, such as the firmware version number or the model, through a colon-delimited string in the "request" parameter (e.g., "request=68:phone\_model"), which is then parsed to extract each identifier and append it to a 64 byte buffer on the stack.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"When appending another character to the small 64 byte buffer, no length check is performed to ensure that no more than 63 characters (plus the appended null terminator) are ever written to this buffer," Fewer explained. "Therefore, an attacker-controlled 'request' parameter can write past the bounds of the small 64 byte buffer on the stack, overflowing into adjacent stack memory."

This means that a malicious colon-delimited "request" parameter sent as part of an HTTP request to the "/cgi-bin/api.values.get" endpoint can be used to trigger a stack-based buffer overflow, allowing the threat actors to corrupt the stack contents and ultimately achieve remote code execution on the underlying operating system.

The vulnerability affects GXP1610, GXP1615, GXP1620, GXP1625, GXP1628, and GXP1630 models. It has been addressed as part of a [firmware update](https://www.grandstream.com/support/firmware) ([version 1.0.7.81](https://firmware.grandstream.com/Release_Note_GXP16xx_1.0.7.81.pdf)) released late last month.

In a [Metasploit exploit module](https://github.com/rapid7/metasploit-framework/pull/20983) developed by Rapid7, it has been demonstrated that the vulnerability could be exploited to gain root privileges on a vulnerable device and chain it with a post-exploitation component to extract credentials stored on a compromised device.

Furthermore, the remote code execution capabilities can be weaponized to reconfigure the target device to use a malicious Session Initiation Protocol (SIP) proxy, effectively enabling the attacker to intercept phone calls to and from the device and eavesdrop on VoIP conversations. A [SIP proxy](https://www.nextiva.com/blog/sip-proxy-server.html) is an intermediary server in VoIP networks to establish and manage voice/video calls between endpoints.

"This isn't a one-click exploit with fireworks and a victory banner," Rapid7's Douglas McKee [said](https://www.rapid7.com/blog/post/ve-phone-listening-cold-war-vulnerability-modern-voip/). "But the underlying vulnerability lowers the barrier in a way that should concern anyone operating these devices in exposed or lightly-segmented environments."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Firmware Security](https://thehackernews.com/search/label/Firmware%20Security), [network security](https://thehackernews.com/search/label/network%20security), [rapid7](https://thehackernews.com/search/label/rapid7), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [VoIP Security](https://thehackernews.com/search/label/VoIP%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond](data:image/svg+xml;base64... "OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond")

OT Security, In Practice: 4 Cross‑Industry Trends fr...