---
title: Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code
url: https://thehackernews.com/2026/09/critical-vmware-workstation-and-fusion.html
source: The Hacker News
date: 2026-09-05
fetch_date: 2026-09-06T06:40:18.234340
---

# Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code

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

# [Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code](https://thehackernews.com/2026/09/critical-vmware-workstation-and-fusion.html)

**Ravie Lakshmanan**Sep 05, 2026Vulnerability / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzExwAd4Vsd2Xz-9kex6ucfK6MDmftPVCfiOGQICWDKrgxMJ6fOj0EttLP2kpYBDv4xSYdrEXt8Wntz916Oa2tyrMnaSHDLH9vb5RF4ncjvwdkeFU8GwaqWvT6zLHRTKIF-BOGK8p24Im4NwqlqZxTokMsYOfXSBdA0-jXxMbMozfjdK-iyyavdAywjAAh/s1700-nu-rw-lo-l85-e365/vmware-host.jpg)

Broadcom has released security updates for two security flaws impacting VMware Workstation and Fusion, including one critical bug that could result in arbitrary code execution under certain conditions.

The vulnerability, tracked as **CVE-2026-59346** (CVSS score: 9.3), is an integer-overflow vulnerability that a local attacker with elevated privileges can exploit to run arbitrary code.

"A malicious actor with local administrative privileges on a virtual machine with VMXNET3 virtual network adapter may exploit this issue to execute code on the host," Broadcom [said](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38288) in an alert.

The tech giant credited @h4urek, @cameudis, and Stan S for discovering the issue.

Also patched by Broadcom is a stack-based buffer-overflow vulnerability in HGFS (**CVE-2026-59347**, CVSS score: 8.1), which can be exploited by a bad actor with local administrative privileges on a virtual machine to execute code as the virtual machine's VMX process running on the host.

Yeonghyeon Choi and Tianchu Chen of Tencent Xuanwu Lab have been acknowledged for reporting the flaw.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

In both cases, successful exploitation hinges on an attacker already possessing local administrative privileges, although it's worth noting that they can be obtained through a separate compromise through phishing or exploiting weak user configurations.

The two vulnerabilities affect VMware Workstation and VMware Fusion versions 25H2 and 26H1. Broadcom said there are no workarounds that address the two vulnerabilities, adding that they have been patched in VMware Workstation 26H1u1 and VMware Fusion 26H1u1.

Although there is no evidence that the security flaws have been exploited in the wild, vulnerabilities in VMware products have been an attack magnet.

As recently as last month, threat actors were observed [actively exploiting](https://thehackernews.com/2026/08/suspected-china-nexus-actor-exploits.html) two shortcomings in VMware vCenter, namely CVE-2026-59309 and CVE-2026-59310, with the latter suspected to be weaponized by a China-nexus advanced persistent threat (APT) actor.

The activity, which started five calendar days after public disclosure of the flaw, is estimated to have breached 361 unique victim IP addresses across 47 countries. Most of the infections were concentrated in Germany (55), the U.S. (41), Turkey (38), Iran (26), and France (25).

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

[Virtualization Security](https://thehackernews.com/search/label/Virtualization%20Security), [VMware](https://thehackernews.com/search/label/VMware), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw](https://thehackernews.com/2026/08/a-malicious-webpage-could-poison-your.html)

[![The Hacker News](data:image/svg+xml;base64...)

Critical Gitea RCE Actively Exploited as Reported Attack Drops Miner-Like Payload](https://thehackernews.com/2026/08/critical-gitea-rce-actively-exploited.html)

[![The Hacker News](data:image/svg+xml;base64...)

Claude Opus 4.6 Bypasses Gym Booking Limit, Cancels Other Users' Reservations in Tests](https://thehackernews.com/2026/08/claude-opus-46-bypasses-gym-booking.html)

[![The Hacker News](data:image/svg+xml;base64...)

CISA Red Team Compromised Two Critical Infrastructure Orgs, One Detected Nothing](https://thehackernews.com/2026/08/cisa-red-team-compromised-two-critical.html)

[![The Hacker News](data:image/svg+xml;base64...)

FBI Disrupts...