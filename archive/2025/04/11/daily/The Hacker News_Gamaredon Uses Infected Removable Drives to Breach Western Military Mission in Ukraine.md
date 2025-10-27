---
title: Gamaredon Uses Infected Removable Drives to Breach Western Military Mission in Ukraine
url: https://thehackernews.com/2025/04/gamaredon-uses-infected-removable.html
source: The Hacker News
date: 2025-04-11
fetch_date: 2025-10-06T22:07:17.431964
---

# Gamaredon Uses Infected Removable Drives to Breach Western Military Mission in Ukraine

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

# [Gamaredon Uses Infected Removable Drives to Breach Western Military Mission in Ukraine](https://thehackernews.com/2025/04/gamaredon-uses-infected-removable.html)

**Apr 10, 2025**Ravie LakshmananCyber Espionage / Malware

[![Breach Western Military](data:image/png;base64... "Breach Western Military")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwR21ShS13dKr0T30qTpjQNmTQhGTMZ3oIpL_olpCgJ2p8hVdvEC81OLFZSpbXpSM0Rjc8Zk2D3Qgxo336D-7lPQn0kQC_sDLBNL2xZA1x80RpwS5MssnbCuOJcT3jP5s3YelpT8NHGeshMjYFXUQi9ygQhdiRMEl3-t8CwD-XkY4JqPdbyyVldsYgro7r/s790-rw-e365/russian-hackers.jpg)

The Russia-linked threat actor known as **[Gamaredon](https://thehackernews.com/2024/12/hackers-leveraging-cloudflare-tunnels.html)** (aka Shuckworm) has been attributed to a cyber attack targeting a foreign military mission based in Ukraine with an aim to deliver an updated version of a known malware called GammaSteel.

The group targeted the military mission of a Western country, per the Symantec Threat Hunter team, with first signs of the malicious activity detected on February 26, 2025.

"The initial infection vector used by the attackers appears to have been an infected removable drive," the Broadcom-owned threat intelligence division [said](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack started with the creation of a Windows Registry value under the UserAssist key, followed by launching "mshta.exe" using "explorer.exe" to initiate a multi-stage infection chain and launch two files.

The first file, named "NTUSER.DAT.TMContainer00000000000000000001.regtrans-ms," is used to establish communications with a command-and-control (C2) server that's obtained by reaching out to specific URLs associated with legitimate services like Teletype, Telegram, and Telegraph, among others.

The second file in question, "NTUSER.DAT.TMContainer00000000000000000002.regtrans-ms," is designed to infect any removable drives and network drives by creating shortcut files for every folder to execute the malicious "mshta.exe" command and hide it.

Subsequently on March 1, 2025, the script was executed to contact a C2 server, exfiltrate system metadata, and receive, in return, a Base64-encoded payload, which is then used to run a PowerShell command engineered to download an obfuscated new version of the same script.

The script, for its part, connects to a hard-coded C2 server to fetch two more PowerShell scripts, the first of which is a reconnaissance utility capable of capturing screenshots, run systeminfo command, get details of security software running on the host, enumerate files and folders in Desktop, and list running processes.

The second PowerShell script is an improved version of [GammaSteel](https://thehackernews.com/2024/04/russias-apt28-exploited-windows-print.html), a known information stealer that's capable of exfiltrating files from a victim based on an extension allowlist from the Desktop and Documents folders.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This attack does mark something of an increase in sophistication for Shuckworm, which appears to be less skilled than other Russian actors, though it compensates for this with its [relentless focus on targets in Ukraine](https://thehackernews.com/2025/03/russia-linked-gamaredon-uses-troop.html)," Symantec said.

"While the group does not appear to have access to the same skill set as some other Russian groups, Shuckworm does now appear to be trying to compensate for this by continually making minor modifications to the code it uses, adding obfuscation, and leveraging legitimate web services, all to try lower the risk of detection."

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

[Advanced Persistent Threats](https://thehackernews.com/search/label/Advanced%20Persistent%20Threats)[Command and Control](https://thehackernews.com/search/label/Command%20and%20Control)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Information Stealer](https://thehackernews.com/search/label/Information%20Stealer)[Malware](https://thehackernews.com/search/label/Malware)[powershell](https://thehackernews.com/search/label/powershell)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-se...