---
title: PureCrypter Deploys Agent Tesla and New TorNet Backdoor in Ongoing Cyberattacks
url: https://thehackernews.com/2025/01/purecrypter-deploys-agent-tesla-and-new.html
source: The Hacker News
date: 2025-01-29
fetch_date: 2025-10-06T20:12:14.021785
---

# PureCrypter Deploys Agent Tesla and New TorNet Backdoor in Ongoing Cyberattacks

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

# [PureCrypter Deploys Agent Tesla and New TorNet Backdoor in Ongoing Cyberattacks](https://thehackernews.com/2025/01/purecrypter-deploys-agent-tesla-and-new.html)

**Jan 28, 2025**Ravie LakshmananPhishing Attack / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-XDknRCKEi7D29QWiXt3-bqZF5H6GurCrcmD9OW1sGWQWGZNUwxZ0O1yzCLHGpc0rG9laJFmE-ql-EnEWppRHINSRA9Qq72DJNb2p-y8OeZF2_T4Lxkm2py8kzV-lYpZuKXSvDGSrfi6wglbEDMyCpqGK_210u6CwgQuhUHaMKyCNq0sjNgP165xwPHD2/s790-rw-e365/code.jpg)

A financially motivated threat actor has been linked to an ongoing phishing email campaign that has been ongoing since at least July 2024 specifically targeting users in Poland and Germany.

The attacks have led to the deployment of various payloads, such as [Agent Tesla](https://thehackernews.com/2024/07/cybercriminals-target-polish-businesses.html), [Snake Keylogger](https://thehackernews.com/2025/01/hackers-hide-malware-in-images-to.html), and a previously undocumented backdoor dubbed TorNet that's delivered by means of [PureCrypter](https://thehackernews.com/2024/10/new-malware-campaign-uses-purecrypter.html). TorNet is so named owing to the fact that it allows the threat actor to communicate with the victim machine over the TOR anonymity network.

"The actor is running a Windows scheduled task on victim machines—including on endpoints with a low battery—to achieve persistence," Cisco Talos researcher Chetan Raghuprasad [said](https://blog.talosintelligence.com/new-tornet-backdoor-campaign/) in an analysis published today.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The actor also disconnects the victim machine from the network before dropping the payload and then connects it back to the network, allowing them to evade detection by cloud antimalware solutions."

The starting point of the attacks is a phishing email bearing fake money transfer confirmations or order receipts, with the threat actor masquerading as financial institutions and manufacturing and logistics companies. Attached to these messages are files with the extension ".tgz" in a likely attempt to evade detection.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCVTwlJ9B5zL6g3Kf2_dbF-CemuU_SIedI_RjciQBGc33q-tc5pzAXZZuRuwIs2fr4ernkcPIwP-lm6p3sT-fchCEhAXC2hL2-HZ412APG8EBGi-fhi5FMEEsmVXicLTu6_rHNHVDTO6O9gWpPUAw08SAd6OqdaqTQh4Xg2qnMBX4WpguJtXPNzqPogc-H/s790-rw-e365/cisco.jpeg)

Opening the compressed email attachment and extracting the archive contents leads to the execution of a .NET loader that, in turn, downloads and runs PureCrypter directly in memory.

The PureCrypter malware then proceeds to launch the TorNet backdoor, but not before performing a series of anti-debugger, anti-analysis, anti-VM, and anti-malware checks on the victim machine to fly under the radar.

"The TorNet backdoor establishes connection to the C2 server and also connects the victim machine to the TOR network," Raghuprasad noted. "It has the capabilities to receive and run arbitrary .NET assemblies in the victim machine's memory, downloaded from the C2 server, increasing the attack surface for further intrusions."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes days after the threat intelligence firm said it observed a surge in email threats leveraging hidden text salting in the second half of 2024 with an intent to sidestep brand name extraction by email parsers and detection engines.

"Hidden text salting is a simple yet effective technique for bypassing email parsers, confusing spam filters, and evading detection engines that rely on keywords," security researcher Omid Mirzaei [said](https://blog.talosintelligence.com/seasoning-email-threats-with-hidden-text-salting/). "The idea is to include some characters into the HTML source of an email that are not visually recognizable."

To counter such attacks, it's recommended to develop advanced filtering techniques that can detect hidden text salting and content concealment, including detecting use of CSS properties like "visibility" and "display," and adopt visual similarity detection approach (e.g., [Pisco](https://dl.acm.org/doi/10.1145/3658644.3691381)) to enhance detection capabilities.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Email Threat](https://thehackernews.com/search/label/Email%20Threat)[keylogger](https://thehackernews.com/search/label/keylogger)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[PureCrypter](https://thehackernews.com/search/label/PureCrypter)[Tor network](https://thehackernews.com/search/label/Tor%20network)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Conte...