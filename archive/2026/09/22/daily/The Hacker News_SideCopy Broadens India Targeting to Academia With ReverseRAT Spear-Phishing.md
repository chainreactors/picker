---
title: SideCopy Broadens India Targeting to Academia With ReverseRAT Spear-Phishing
url: https://thehackernews.com/2026/09/sidecopy-broadens-india-targeting-to.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:53.871809
---

# SideCopy Broadens India Targeting to Academia With ReverseRAT Spear-Phishing

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

# [SideCopy Broadens India Targeting to Academia With ReverseRAT Spear-Phishing](https://thehackernews.com/2026/09/sidecopy-broadens-india-targeting-to.html)

**Ravie Lakshmanan**Sep 22, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVXTuBFDgZyaNFTznwdu5HXSKuVHU5xpM7JDvXP_Ra-68CsYd68bb6xMWPXbjmsM5oO211hZgzIN0NENk_cMBZZpL88LMsIaNkfSEpIWRRzyjRt7Ke6ZMeUXvIKcH3ncgDouKN8FGuunAFQFMolel0GgTBm1lzdVDH28WpWFUCI4Fvl9ju0q4Vv0S55PVx/s1700-nu-rw-lo-l85-e365/word-school.jpg)

The threat actor known as **SideCopy** has been observed using spear-phishing lures to target academic institutions in India, expanding their strategic focus beyond government entities.

"SideCopy campaign operations typically initiate through spear-phishing campaigns that leverage the abuse of mshta.exe to execute malicious scripts and circumvent standard security protocols," Trellix researchers Boggavarapu R S S Srinivas Gupta and Ravishankar N C [said](https://www.trellix.com/blogs/research/sidecopy-threat-intel-mshta-execution-rat-deployment/) in a technical report.

"This delivery mechanism facilitates the deployment of a remote access trojan (RAT), which serves as the central pillar of their offensive infrastructure."

Active since at least 2019, [SideCopy](https://cyble.com/threat-actor-profiles/sidecopy/) (aka TAG-140) is an advanced persistent threat (APT) group that originates from Pakistan, and shares overlaps with the [Transparent Tribe](https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html) cluster. Historically, the threat actor has primarily targeted Indian defense forces and government officials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

In a report published in June 2026, Seqrite Labs [attributed](https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html) SideCopy to a spear-phishing campaign targeting Afghanistan's Ministry of Finance with an open-source remote access trojan called Xeno RAT.

The latest attack chain documented by Trellix uses spear-phishing to deliver a weaponized ZIP archive, within which exists a Windows shortcut (LNK) with a spoofed PDF icon and a .DOCX extension ("commskll.docx.lnk") to make the malicious file look legitimate.

The LNK file is used to fetch an obfuscated HTML Application (HTA) from a remote server ("docsportal[.]in") and execute it using "mshta.exe," which then proceeds to reflectively load a DLL payload. The malware makes use of an anti-forensic self-deletion routine that deletes the HTA file once the subsequent stage is initialized.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9mfDAw7FmjS5ZKa8qAf1NexMEUtbf8eE_8FRNutRU_GSrgEhKbN8Knoxg3Om845RRP1S1BMtqBW3rfXtxCfB_ebOowlsrDCXluuWkXU05L6YRih-8b3Zb1JTgK-e-QaFg6sjLQDoTGD3cuDHerOucnjPZ5A4ciyAzneJBCcIQO-HF6j84OLwbL49RpffV/s1700-nu-rw-lo-l85-e365/side.jpg)

The DLL serves as a dropper for three embedded components -

* appT.bat, a batch script that's launched by means of a Windows Registry Run Key to execute "startT.hta" using "mshta.exe" without requiring user interaction
* startT.hta, a secondary exploit stage that contains the obfuscated final payload
* commskl.docx, a decoy document

"The obfuscated code within startT.hta executes a multi-stage deobfuscation routine to reconstruct a two-part XAML payload directly in memory," Trellix explained, adding it's responsible for reflectively loading an embedded DLL ("ioluegnt.dll").

"To evade disk-based detection, the malware decodes its core payload into volatile memory space, transitioning from a Base64-encoded string to an active, in-memory process via .NET Deserialization."

The DLL is a remote access trojan named ReverseRAT, which has been [put to use](https://thehackernews.com/2021/06/pakistan-linked-hackers-targeted-indian.html) by SideCopy [since early 2021](https://thehackernews.com/2023/02/researchers-warn-of-reverserat-backdoor.html) to facilitate data exfiltration, remote execution, and persistence. It's equipped to gather system metadata, a list of installed software, screenshots, passwords, and clipboard content; perform file operations; run commands; set up persistence via Registry; upload files; and spawn a shell session.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

The command-and-control (C2) traffic is encrypted using a hard-coded cryptographic key ("NMXIKS09?:709,!~lnsYUS"). The harvested data is exfiltrated via port 5863 to "dns.educationportals[.]biz," which resolves to the IP address "45.61.157[.]22."

"The current activities of SideCopy underscore a disciplined and highly strategic approach to intelligence collection," Trellix concluded. "While their historical focus has been on Indian government entities, their recent pivot toward academic institutions highlights an expanding set of strategic priorities."

"By continuously refining their infection stages, most notably through the heavy abuse of mshta.exe and complex, multilayered obfuscation, they remain a formidable and adaptive adversary for regional security."

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_...