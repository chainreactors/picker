---
title: Alert: New Electromagnetic Attacks on Drones Could Let Attackers Take Control
url: https://thehackernews.com/2023/06/alert-new-electromagnetic-attacks-on.html
source: The Hacker News
date: 2023-06-29
fetch_date: 2025-10-04T11:49:09.356294
---

# Alert: New Electromagnetic Attacks on Drones Could Let Attackers Take Control

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

# [Alert: New Electromagnetic Attacks on Drones Could Let Attackers Take Control](https://thehackernews.com/2023/06/alert-new-electromagnetic-attacks-on.html)

**Jun 28, 2023**Ravie LakshmananFirmware Security / Tech

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAg7wxU_z9A9fN0ODlb1JYLBSmzylXdTNOOjjEBp7GQCSlWfc7vFabni9igknUeocwhT7CO7LtcwCSfkP3g_P0H9gr7C4GF-GUmWT2hZ2jNp3Vgon4zTYJfDA3nbgA8aVYJ4371lILxSAwSiBRJijOMBVtlXaxXOJq7Atfud_AuNrE2IkclNUuXLd9w94/s790-rw-e365/drone.jpg)

Drones that don't have any known security weaknesses could be the target of electromagnetic fault injection (EMFI) attacks, potentially enabling a threat actor to achieve arbitrary code execution and compromise their functionality and safety.

The research comes from IOActive, which [found](https://ioactive.com/exploring-the-security-configuration-of-amd-platforms-3/) that it is "feasible to compromise the targeted device by injecting a specific EM glitch at the right time during a firmware update."

"This would allow an attacker to gain code execution on the main processor, gaining access to the Android OS that implements the core functionality of the drone," Gabriel Gonzalez, director of hardware security at the company, said in a report published this month.

The [study](https://labs.ioactive.com/2023/06/applying-fault-injection-to-firmware.html), which was undertaken to determine the current security posture of Unmanned Aerial Vehicles (UAVs), was carried out on [Mavic Pro](https://www.dji.com/global/mavic), a popular quadcopter drone manufactured by DJI that employs various security features like signed and encrypted firmware, Trusted Execution Environment ([TEE](https://thehackernews.com/2021/10/researchers-break-intel-sgx-with-new.html)), and Secure Boot.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Side-channel attacks typically work by indirectly gathering information about a target system by exploiting unintended information leakages arising from variations in power consumption, electromagnetic emanations, and the time it takes to perform different mathematical operations.

EMFI aims to induce a hardware disruption by placing a metal coil in close physical proximity to the Android-based Control CPU of the drone, ultimately resulting in memory corruption, which could then be exploited to achieve code execution.

"This could allow an attacker to fully control one device, leak all of its sensitive content, enable ADB access, and potentially leak the encryption keys," Gonzalez said.

As for mitigations, it's [recommended](https://cwe.mitre.org/data/definitions/1319.html) that drone developers incorporate hardware- and software-based [EMFI countermeasures](https://vtechworks.lib.vt.edu/handle/10919/81906).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is not the first time IOActive has [highlighted](https://ioactive.com/resources/library/) uncommon attack vectors that could be weaponized to target systems. In June 2020, the company [detailed](https://ioactive.com/warcodes-attacking-ics-through-industrial-barcode-scanners/) a novel method that makes it possible to attack industrial control systems (ICS) using barcode scanners.

Other assessments have illustrated [security misconfigurations](https://ioactive.com/do-you-blindly-trust-lorawan-networks-for-iot/) in the Long Range Wide Area Network ([LoRaWAN](https://en.wikipedia.org/wiki/LoRa)) protocol that make it susceptible to hacking and cyber attacks as well as [vulnerabilities](https://ioactive.com/remote-writing-trailer-air-brakes-with-rf/) in the Power Line Communications ([PLC](https://www.cisa.gov/news-events/ics-advisories/icsa-22-063-01)) component used in tractor trailers.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Drone hacking](https://thehackernews.com/search/label/Drone%20hacking)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-...