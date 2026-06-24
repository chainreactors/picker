---
title: WhatsApp VBScript Campaign Uses Fake Documents to Install ManageEngine RMM Tool
url: https://thehackernews.com/2026/06/whatsapp-vbscript-campaign-uses-fake.html
source: The Hacker News
date: 2026-06-23
fetch_date: 2026-06-24T06:06:31.790845
---

# WhatsApp VBScript Campaign Uses Fake Documents to Install ManageEngine RMM Tool

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

# [WhatsApp VBScript Campaign Uses Fake Documents to Install ManageEngine RMM Tool](https://thehackernews.com/2026/06/whatsapp-vbscript-campaign-uses-fake.html)

**Ravie Lakshmanan**Jun 23, 2026Malware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDqA3duB8U44C_MQ5PM061Wch2-j7uRvX_D52lK_2Dsm2lxcquuICTnFZ-dhQiQfxxKTnIJz4tf7ffCupdkoU1giCEGhHXLKJ0xC3dw7duptIHq15dD0E5XlkvB9JbKztGCTJOk2iJ53shzUQexv2So6rrFy8djOO1etfsolTM5UbvMUkKvNwNpHqFvS7V/s1700-e365/whatsapp-main.jpg)

Direct messages sent via WhatsApp are being used to distribute malicious Visual Basic Script (VBScript) files that lead to the installation of legitimate Remote Monitoring and Management (RMM) software.

Per findings from Kaspersky, the active campaign is targeting users of WhatsApp Desktop and WhatsApp Web across Malaysia, Brazil, India, Mexico, Singapore, the U.K., Spain, Taiwan, Australia, Russia, and Vietnam. The highest concentration of victims has been reported in Malaysia.

"The threat actor uses deceptive file names masquerading as business and financial documents to persuade recipients to download and execute the attachment," security researcher Fareed Radzi [said](https://securelist.com/whatsapp-vbs-rmm-campaign/120290/). "Once executed, the VBScript initiates a multi-stage infection chain that ultimately results in the installation of legitimate Remote Monitoring and Management (RMM) software, enabling remote access to the victim's system."

It's suspected that the threat actor behind the operation managed to obtain surreptitious access to several WhatsApp accounts and then used them as a distribution vector for the VBScript files across their contacts. That said, exactly how these accounts are compromised is unclear.

The heavily obfuscated VBScript files are dressed up as seemingly harmless business and financial documents, using names like "Financial Reports.vbs" or "Account Statement.vbs." Some of the files are also named in other languages, such as Portuguese, French, German, and Malay, reflective of the global nature of the campaign.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"In addition, the VBScript samples contain extensive comments and metadata intended to mimic legitimate Microsoft Windows Update components," Kaspersky explained. "Many of these comments are written in Chinese and include references to Windows Update modules, certificate validation, system integrity checks, and deployment-related functionality."

The VBScript file is launched using "WScript.exe," which then fetches and runs additional VBScript components required for the next stages of the attack. It's worth noting that the infection chain behaves a little differently based on whether a victim is using WhatsApp Web or the WhatsApp Desktop application.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNTAlZfXuJg2thJGJ214nHfh0n_biESDAMmbg1HmiX5vdntK8Ch7-fjF9zZal3h5fh4UL-_pokKzlASxw7IEDygzhZxWw9SzX801cajmnnih4CJ-R3eN0JM1LlwCOMN-oZyGhTe3_y9dJm9uIt_vQ6RhnVuWAPzdgIk18NOyhBzl6f_VTaabuxxDn-BLWP/s1700-e365/map.jpeg)

In the case of the former, the attack relies on the user downloading the file to their system and then opening it from the downloaded folder or via the browser's download history, assuming it to be a legitimate document. In WhatsApp Desktop, the malware is executed directly within the application, with the process tree revealing that "WhatsApp.Root.exe," the background process associated with the client application, is responsible for spawning "WScript.exe."

The primary objective of the VBScript is to download two secondary VBScript payloads from a remote server, one of which attempts to tamper with Windows User Account Control (UAC) behavior, while the other downloads and executes a ZIP file containing the installation package for ManageEngine RMM Central.

The activity remains unattributed, however, the Russian cybersecurity company said it found infrastructure overlaps ("202.61.160[.]201") with prior activity linked to [Gh0st RAT and ValleyRAT](https://thehackernews.com/2024/06/china-linked-valleyrat-malware.html).

"Users should be cautious when receiving unexpected attachments through WhatsApp, even when they appear to originate from known contacts," Kaspersky said. "Script and executable file types such as VBS, VBE, EXE, BAT, CMD, JS, and PS1 should not be opened unless their legitimacy has been independently verified."

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

[Kaspersky](https://thehackernews.com/search/label/Kaspersky), [Malware](https://thehackernews.com/search/label/Malware), [ManageEngine](https://thehackernews.com/search/label/ManageEngine), [Social Engineering](https://thehackernews.com/search/label/Social%20Engineering), [VBScript](https://thehackernews.com/search/label/VBScript), [WhatsApp](https://thehackernews.com/search/label/WhatsApp), [Windows](https://thehackernews.com/search/label/Windows)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](data:image/svg+xml;base64... "Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild -...