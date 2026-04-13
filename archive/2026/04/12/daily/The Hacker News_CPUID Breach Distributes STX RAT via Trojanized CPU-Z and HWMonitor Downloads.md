---
title: CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads
url: https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html
source: The Hacker News
date: 2026-04-12
fetch_date: 2026-04-13T04:57:16.301459
---

# CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads](https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html)

**Ravie Lakshmanan**Apr 12, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCPq2en6ihCNpYdSr5mWkN43O4Rl3tXYz77I2achAfYSy7Emoaj8fNqmFHLOydg6Ai6DwDKBEKD91ywcO9eT2t-rrFxEiThe79Rsa4dap_UcNZSEdWl9NRGeaMqP_vsbWnKf2mMNHQ86cabK4wlspLPWRHMJ7Gj5guX6ynx57RhsDLbJeSDAdPR_BjGFNU/s1700-e365/downloads.jpg)

Unknown threat actors compromised CPUID ("cpuid[.]com"), a website that hosts popular hardware monitoring tools like CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor, for less than 24 hours to serve malicious executables for the software and deploy a remote access trojan called STX RAT.

The incident lasted from approximately April 9, 15:00 UTC, to about April 10, 10:00 UTC, with the download URLs for CPU-Z and HWMonitor installers replaced with links to malicious websites.

In a [post](https://x.com/d0cTB/status/2042520961824559150) shared on X, CPUID confirmed the breach, attributing it to a compromise of a "secondary feature (basically a side API)" that caused the main site to randomly display malicious links. It's worth noting that the attack did not impact its signed original files.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

According to [Kaspersky](https://securelist.com/tr/cpu-z/119365/), the names of the rogue websites are as follows -

* cahayailmukreatif.web[.]id
* pub-45c2577dbd174292a02137c18e7b1b5a.r2[.]dev
* transitopalermo[.]com
* vatrobran[.]hr

"The trojanized software was distributed both as ZIP archives and as standalone installers for the aforementioned products," the Russian cybersecurity company said. "These files contain a legitimate signed executable for the corresponding product and a malicious DLL, which is named 'CRYPTBASE.dll' to leverage the DLL side-loading technique."

The malicious DLL, for its part, contacts an external server and executes additional payloads, but not before performing anti-sandbox checks to sidestep detection. The end goal of the campaign is to deploy [STX RAT](https://www.esentire.com/blog/stx-rat-a-new-rat-in-2026-with-infostealer-capabilities), a RAT with HVNC and broad infostealer capabilities.

STX RAT "exposes a broad command set for remote control, follow-on payload execution, and post-exploitation actions (e.g., in-memory execution of EXE/DLL/PowerShell/shellcode, reverse proxy/tunneling, desktop interaction)," eSentire said in an analysis of the malware last week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The command-and-control (C2) server address and the connection configuration have been reused from a [prior campaign](https://www.malwarebytes.com/blog/threat-intel/2026/03/a-fake-filezilla-site-hosts-a-malicious-download) that leveraged trojanized [FileZilla installers](https://www.malwarebytes.com/blog/threat-intel/2026/02/fake-7-zip-downloads-are-turning-home-pcs-into-proxy-nodes) hosted on bogus sites to deploy the same RAT malware. The activity was documented by Malwarebytes early last month.

Kaspersky said it has identified more than 150 victims, mostly individuals who were affected by the incident. However, organizations in retail, manufacturing, consulting, telecommunications, and agriculture have also been impacted. Most of the infections are located in Brazil, Russia, and China.

"The gravest mistake attackers made was to reuse the same infection chain involving STX RAT, and the same domain names for C2 communication, from the previous attack related to fake FileZilla installers," Kaspersky said. "The overall malware development/deployment and operational security capabilities of the threat actor behind this attack are quite low, which, in turn, made it possible to detect the watering hole compromise as soon as it started."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data theft](https://thehackernews.com/search/label/data%20theft), [DLL Sideloading](https://thehackernews.com/search/label/DLL%20Sideloading), [Incident response](https://thehackernews.com/search/label/Incident%20response), [Malware](https://thehackernews.com/search/label/Malware), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [watering hole](https://thehackernews.com/search/label/watering%20hole)

Trending News

[![Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](data:image/svg+xml;base64... "Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass")

Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](https://thehackernews.com/2026/04/microsoft-warns-of-whatsapp-delivered.html)

[![New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](data:image/svg+xml;base64... "New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released")

New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](https://thehackernews.com/2026/04/new-chrome-zero-day-cve-2026-5281-under.html)

[![Apple Expands iOS 18.7.7 Update to More Devices to...