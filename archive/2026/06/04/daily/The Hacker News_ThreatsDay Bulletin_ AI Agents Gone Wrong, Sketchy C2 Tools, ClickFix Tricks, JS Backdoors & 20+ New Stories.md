---
title: ThreatsDay Bulletin: AI Agents Gone Wrong, Sketchy C2 Tools, ClickFix Tricks, JS Backdoors & 20+ New Stories
url: https://thehackernews.com/2026/06/threatsday-bulletin-ai-agents-gone.html
source: The Hacker News
date: 2026-06-04
fetch_date: 2026-06-05T06:14:26.702330
---

# ThreatsDay Bulletin: AI Agents Gone Wrong, Sketchy C2 Tools, ClickFix Tricks, JS Backdoors & 20+ New Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [ThreatsDay Bulletin: AI Agents Gone Wrong, Sketchy C2 Tools, ClickFix Tricks, JS Backdoors & 20+ New Stories](https://thehackernews.com/2026/06/threatsday-bulletin-ai-agents-gone.html)

**Ravie Lakshmanan**Jun 04, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOsPH2SzhBWTxhXi2KCJw0YY29azn2hLkDQwQhyrjmwaRIXQfCAPNIjej3_TBd6VJm1JqWSs2EoI2jiWyVHENmhtd1alqSEqlJC8WxUk4b5zWUqszQ8akhGzRmCHf8OL7wMTZiWLYZDzHRXY8unPcsh2QMTfyTH0XeRszrwCunK2DazuZIF9oNKQUFxlqN/s1700-e365/thh.jpg)

It got stupid again.

The internet still feels held together with tape. Bad plugins, old bugs, fake tools, trusted apps doing shady things. Same mess, new wrapper. And now the weird stuff is normal. Forums go down and come back worse. Cheap hackers get better toys. AI starts breaking real systems. Great.

Read the whole thing before it ruins your week anyway.

1. Unauthenticated SSRF risk

   [Cisco Patches Unified Communications Manager Flaw](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)

   Cisco has [released](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW) fixes to address a high-severity security flaw in Unified Communications Manager (CVE-2026-20230, CVSS score: 8.6) that could allow an unauthenticated, remote attacker to conduct server-side request forgery (SSRF) attacks through an affected device. "This vulnerability is due to improper input validation for specific HTTP requests," Cisco said. "An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device. A successful exploit could allow the attacker to write files to the underlying operating system that could be used later to elevate to root." The issue has been addressed in Cisco Unified CM and Unified CM SME Release versions 14SU6 and 15SU5. Cisco said it's aware of the availability of proof-of-concept exploit code for the flaw, but noted there is no evidence of active exploitation. It credited an independent security researcher working with SSD Secure Disclosure for reporting the vulnerability.
2. Mobile spyware operation

   [Russia Claims Large-Scale Operation Targeting High-Ranking Officials](https://www.fsb.ru/fsb/press/message/single.htm%21id%3D10440695%40fsbMessage.html)

   Russia's Federal Security Service (FSB) has disclosed details of what it described as a "large-scale action" undertaken by foreign intelligence services to stealthily implant spyware on the mobile devices of high-ranking officials in the country. "This software was utilized to exfiltrate existing data, intercept ongoing conversations, and conduct covert audio and video surveillance of the immediate surroundings of the electronic devices, with the ultimate objective of obtaining sensitive information," the FSB [said](https://www.fsb.ru/fsb/press/message/single.htm%21id%3D10440695%40fsbMessage.html). Russia did not reveal who was behind the attacks, but noted the "representatives of foreign intelligence services" leveraged the technical capabilities of major international IT corporations to exfiltrate sensitive data from the devices. This specifically included the exploitation of mobile communication channels, the agency added. An investigation into the activity is ongoing, with the FSB also initiating a criminal case to investigate the matter.
3. Layered keylogger lures

   [VIP Keylogger Campaigns Analyzed](https://www.splunk.com/en_us/blog/security/behind-the-code-layered-defense-evasion-vip-keylogger.html)

   Threat actors have been relying on social engineering over the past few months to push [VIP Keylogger](https://thehackernews.com/2025/01/hackers-hide-malware-in-images-to.html) via loaders written in JavaScript, batch scripts, and Visual Basic Script (VBS). "Attackers are masquerading as legitimate business communications such as bank payment notifications, procurement orders, and logistics updates to lure users into opening malicious files," Splunk [said](https://www.splunk.com/en_us/blog/security/behind-the-code-layered-defense-evasion-vip-keylogger.html).

   [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0qoMEYJo_YnXNZzuLFLN_-0eW8ry-McxMmFZnNIcuuFS6V-SvW8qQuCwsmNEzyp8lDQ8Bxfm_4PeMbqkJEQQLdEcHp76XbmZmzNXXS8PPGabJkev9mNoUDQrQJcf6tiEuhmhErPSeTXABWiZ48jSJFDTToCHYflJTlY_oku2EeYx2FsnXpEKdyH_JmY1B/s1700-e365/vip.png)
4. Crypto sanctions escalation

   [U.S. Sanctions Nobitex Crypto Exchange](https://home.treasury.gov/news/press-releases/sb0519)

   The U.S. Treasury's Office of Foreign Assets Control (OFAC) has announced sanctions against Nobitex, Iran's largest cryptocurrency exchange, for facilitating payments related to terrorist activities. "Nobitex has provided significant support to the regime, processing more than 50 percent of all Iranian digital asset inflows in 2025 and facilitating payments tied to Iran's terrorist activities, sanctions evasion efforts, and Islamic Revolutionary Guard Corps (IRGC)-linked transactions, including activity associated with IRGC-affiliated ransomware actors," the Treasury [said](https://home.treasury.gov/news/press-releases/sb0519). The sanctions also extend to Nobitex's chairman, co-founder, and former CEO, Amir Hossein Rad, as well as other Nobitex leaders and officials, and three other exchanges: Wallex, Bitpin, and Ramzinex. According to [Chainalysis](https://www.chainalysis.com/blog/ofac-sanctions-iranian-crypto-exchanges-june-2026/), Nobitex processed over 50% of all Iranian digital asset inflows last year. The four exchanges accounted for roughly $7.7 billion, 78% of Iran's USD 9.9 billion in attributed 2025 crypto volume, per [TRM Labs](https://www.trmlabs.com/resources/blog/three-enforcement-layers-in-five-months-ofac-designates-irans-domestic-crypto-exchanges).
5. Cybercrime forum fallout

   [XSS Takes Fractures Cybercrime Underground](https://flashpoint.io/blog/u...