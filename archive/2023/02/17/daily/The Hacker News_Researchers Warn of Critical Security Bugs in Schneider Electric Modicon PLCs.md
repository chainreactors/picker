---
title: Researchers Warn of Critical Security Bugs in Schneider Electric Modicon PLCs
url: https://thehackernews.com/2023/02/researchers-warn-of-critical-security.html
source: The Hacker News
date: 2023-02-17
fetch_date: 2025-10-04T07:17:11.612373
---

# Researchers Warn of Critical Security Bugs in Schneider Electric Modicon PLCs

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

# [Researchers Warn of Critical Security Bugs in Schneider Electric Modicon PLCs](https://thehackernews.com/2023/02/researchers-warn-of-critical-security.html)

**Feb 16, 2023**Ravie LakshmananCritical Infrastructure / Cybersecurity

[![plc scada vulnerability](data:image/png;base64... "plc scada vulnerability")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpYornV7JDRvEFaFRJTX6E2foVdpE00NqMuOySAisJZoalR15gWIL07l0r795VTV0YKWRPdO_3DJBF5arZvGJiBQlWDACoxhnSrWHZ8OPUgnLXNZ6ZzxW9QwbiWyzgeZHqw8thTV4oSNAvUwKKoiT6q2dQZL3OUyuSGCTRrBlN6BPFErI30dqQVv0E/s790-rw-e365/plc.png)

Security researchers have disclosed two new vulnerabilities affecting Schneider Electric Modicon programmable logic controllers (PLCs) that could allow for authentication bypass and remote code execution.

The flaws, tracked as [CVE-2022-45788](https://nvd.nist.gov/vuln/detail/CVE-2022-45788) (CVSS score: 7.5) and [CVE-2022-45789](https://nvd.nist.gov/vuln/detail/CVE-2022-45789) (CVSS score: 8.1), are part of a [broader collection](https://thehackernews.com/2022/06/researchers-disclose-56-vulnerabilities.html) of [security defects](https://thehackernews.com/2022/11/3-new-vulnerabilities-affect-ot.html) tracked by Forescout as OT:ICEFALL.

Successful exploitation of the bugs could enable an adversary to execute unauthorized code, denial-of-service, or disclosure of sensitive information.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity company said the shortcomings can be chained by a threat actor with known flaws from other vendors (e.g., [CVE-2021-31886](https://thehackernews.com/2021/11/13-new-flaws-in-siemens-nucleus-tcpip.html)) to achieve deep lateral movement in operational technology (OT) networks.

[![plc scada vulnerability](data:image/png;base64... "plc scada vulnerability")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgS9jXN4Yvf55SGsCiTrN3uVFzlc4rBIO-JVqXx9CYswpEyEZkECmh3tcxDsfMdCTeGKr2YnCgVZCDS8iYgOzIbFjPlyCKFYEkyvhGbsgVzMXEDN1IJsVwvN901f_zpEGDGJ6LdHAWe2eWgNVTai-_vV6xJuhkKfzJBHYfXPa1h5WqeUWQQG9_20jTO/s790-rw-e365/HACKING.png)

"Deep lateral movement lets attackers gain deep access to industrial control systems and cross often overlooked security perimeters, allowing them to perform highly granular and stealthy manipulations as well as override functional and safety limitations," Forescout [said](https://www.forescout.com/blog/deep-lateral-movement-in-ot-networks-when-is-a-perimeter-not-a-perimeter/).

A highly intricate proof-of-concept (PoC) cyber-physical attack devised by the San Jose-based firm found that the flaws could be weaponized to bypass safety guardrails and inflict damage upon a movable bridge infrastructure.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

With threat actors concocting [sophisticated malware](https://thehackernews.com/2022/04/us-warns-of-apt-hackers-targeting.html) to disrupt industrial control systems, the deep lateral movement afforded by these flaws could permit adversaries to use an "uninteresting device as a staging point for moving towards more interesting targets."

The findings come close on the heels of 38 security flaws that were [revealed](https://thehackernews.com/2023/02/critical-infrastructure-at-risk-from.html) in wireless industrial internet of things (IIoT) devices and which could grant an attacker a direct line of access to OT networks, according to cybersecurity company Otorio.

Taken together, the weaknesses also underscore the real threats to physical operations from IoT devices, cloud-based management platforms, and nested OT networks.

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

[Authentication bypass](https://thehackernews.com/search/label/Authentication%20bypass)[hacking news](https://thehackernews.com/search/label/hacking%20news)[PLC Hacking](https://thehackernews.com/search/label/PLC%20Hacking)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Schneider](https://thehackernews.com/search/label/Schneider)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credent...