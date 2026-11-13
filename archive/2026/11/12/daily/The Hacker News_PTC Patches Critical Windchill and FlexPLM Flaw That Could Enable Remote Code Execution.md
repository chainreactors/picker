---
title: PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution
url: https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:45.833246
---

# PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution](https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html)

**Ravie Lakshmanan**Nov 12, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi01pvi78xYUtyxbtWQ4L5ddMr1yT2-WBSbAnp3wKXa-bpagXqtyQdxPqA43I1NxJGNLk4He30PS-GYUcd1sOaErtMAtNWL-qQUGfD0Y7wSxAzeYJXRf2lA5yFuznu8m2zRgf2llXMiR3w1H6YOOte5qs_DvRxcv0aPeOxWeIDybl1n58VlpuZPUJ0icWDL/s1700-nu-rw-lo-l85-e365/ptc-flaw.jpg)

PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution.

The security flaw, tracked as **[CVE-2026-126325](https://www.cve.org/CVERecord?id=CVE-2026-126325)**, carries a CVSS v4 score of 9.2 out of a maximum of 10.0.

It has been described as a case of improper input validation and deserialization of untrusted data that could result in remote code execution via crafted requests.

"A critical remote code execution (RCE) vulnerability has been reported in PTC Windchill and PTC FlexPLM," according to a description of the flaw on CVE.org. "The vulnerability may be exploited through the deserialization of untrusted data."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The CVE record lists the following versions as affected -

* **PTC Windchill:** 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.2.0, 12.1.2.0, 13.0.2.0, 13.1.0.0, 13.1.1.0, 13.1.2.0, 13.1.3.0, 13.1.4.0
* **PTC FlexPLM:** 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.2.0, 12.1.2.0, 13.0.2.0, 13.1.0.0, 13.1.1.0, 13.1.2.0, 13.1.3.0

"If your Windchill or FlexPLM environment is hosted by PTC, the patches have been applied on their behalf. No action is required on your part," PTC [said](https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability) in a statement posted on its website.

"If your Windchill or FlexPLM environment is not hosted by PTC, we urge you to apply the patch as soon as possible to help protect your systems."

The disclosure comes nearly five months after another critical remote code execution (RCE) issue in Windchill and FlexPLM ([CVE-2026-12569](https://thehackernews.com/2026/06/cisa-adds-exploited-ptc-windchill-rce.html), CVSS score: 9.3) came under active exploitation.

Then, in July 2026, it [emerged](https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html) that threat actors linked to the Cl0p ransomware operation were weaponizing the flaw as part of a data extortion campaign designed to drop JSP web shells and exfiltrate sensitive product data from manufacturing companies and industrial enterprises.

"PTC software is a textbook target for initial access brokers and ransomware operators and a significant enabler of triple extortion campaigns," Yordan Ganchev, principal threat intelligence specialist at watchTowr, said in a statement shared with The Hacker News.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"It allows malicious actors to reach far and wide within victim networks, encrypt and exfiltrate proprietary data, and disrupt industrial processes. In many cases, the impact across these environments has downstream implications for time-sensitive manufacturing, logistics, and fulfillment processes, resulting in material costs per hour of downtime."

Organizations running PTC Windchill and FlexPLM products are recommended to patch exposed systems as soon as possible and monitor for signs of code execution, backdoor access, or web shells on the host. If patching is not an immediate option, it's essential to apply network restrictions to limit the risk of compromise.

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

[enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access](https://thehackernews.com/2026/11/google-disrupts-13-million-device.html)

[![The Hacker News](data:image/svg+xml;base64...)

Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html)

[![The Hacker News](data:image/svg+xml;base64...)

Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It](https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs](https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-co...