---
title: Armenian Entities Hit by New Version of OxtaRAT Spying Tool
url: https://thehackernews.com/2023/02/armenian-entities-hit-by-new-version-of.html
source: The Hacker News
date: 2023-02-18
fetch_date: 2025-10-04T07:28:03.286641
---

# Armenian Entities Hit by New Version of OxtaRAT Spying Tool

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

# [Armenian Entities Hit by New Version of OxtaRAT Spying Tool](https://thehackernews.com/2023/02/armenian-entities-hit-by-new-version-of.html)

**Feb 17, 2023**Ravie LakshmananCyber Threat / Surveillanceware

[![OxtaRAT Spying Tool](data:image/png;base64... "OxtaRAT Spying Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj508eJrnZwy3cYi0OrCuNpw3dcqv6U4i1pDrEymlbcsb-Gz-TWN1tPi6rh6XnXZHIicP7COzO-XXQGbymUruIPTtIh3VTTm30r7pkCliHbK2Md98JciC6D1G81GusWwKlH8J6OdYsZlU3JvvgNVnrwbeU8HAXgo-XHt1u_DHlYKv-C2YHH1M-0XfM/s790-rw-e365/cyberattack.png)

Entities in Armenia have come under a cyber attack using an updated version of a backdoor called **OxtaRAT** that allows remote access and desktop surveillance.

"The tool capabilities include searching for and exfiltrating files from the infected machine, recording the video from the web camera and desktop, remotely controlling the compromised machine with TightVNC, installing a web shell, performing port scanning, and more," Check Point Research [said](https://research.checkpoint.com/2023/operation-silent-watch-desktop-surveillance-in-azerbaijan-and-armenia/) in a report.

The latest campaign is said to have commenced in November 2022 and marks the first time the threat actors behind the activity have expanded their focus beyond Azerbaijan.

"The threat actors behind these attacks have been targeting human rights organizations, dissidents, and independent media in Azerbaijan for several years," the cybersecurity firm noted, calling the campaign Operation Silent Watch.

The late 2022 intrusions are significant, not least because of the changes in the infection chain, the steps taken to improve operational security, and equip the backdoor with more ammunition.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The starting point of the attack sequence is a self-extracting archive that mimics a PDF file and bears a PDF icon. Launching the purported "document" opens a decoy file while also stealthily executing malicious code hidden inside an image.

A polyglot file that combines compiled AutoIT script and an image, OxtaRAT features commands that permit the threat actor to run additional commands and files, harvest sensitive information, perform reconnaissance and surveillance via a web camera, and even pivot to other.

OxtaRAT has been [put to use](https://www.qurium.org/alerts/phishing-attack-against-azerbaijani-political-and-human-right-activities/) by the [adversary](https://www.qurium.org/alerts/azerbaijan/yet-another-targeted-malware-against-azerbajani-political-activists/) as far back as June 2021, albeit with significantly reduced functionality, indicating an attempt to constantly update its toolset and fashion it into a Swiss Army knife malware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi88ycQSljt1wmPbb09XnB9nM0OEacTKR23zwBUbyrufxWS2XItdmKvOkgSsK8WL2EL0w7c4B4ZvJc4evaxQzS5PrSGEgFWH7Fh6R7T0HWdaxJMmFkIh2w3_97HI0zSMOFIXI4NdohQGIF9G_TVrKt_Op-7yBd1EKDh9STha-pf0GnX5Bel4ern_h4L/s790-rw-e365/cyber.png)

The November 2022 attack also stands out for a number of reasons. The first is that the .SCR files that activate the kill chain already contain the OxtaRAT implant as opposed to acting as a downloader to fetch the malware.

"This saves the actors from needing to make additional requests for binaries to the C&C server and attracting unnecessary attention, as well as hides the main malware from being easily discovered on the infected machine, as it looks like a regular image and bypasses type-specific protections," Check Point explained.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The second striking aspect is the geofencing of command-and-control (C2) domains that host the auxiliary tools to Armenian IP addresses.

Also of note is the ability of OxtaRAT to run commands for port scanning and to test the speed of an internet connection, that latter of which is likely used as a way to hide the "extensive" data exfiltration.

"OxtaRAT, which previously had mostly local recon and surveillance capabilities, can now be used as a pivot for active reconnaissance of other devices," Check Point said.

"This may indicate that the threat actors are preparing to extend their main attack vector, which is currently social engineering, to infrastructure-based attacks. It also might be a sign that the actors are moving from targeting individuals to targeting more complex or corporate environments."

"The underlying threat actors have been maintaining the development of Auto-IT based malware for the last seven years, and are using it in surveillance campaigns whose targets are consistent with Azerbaijani interests."

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

[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[surveillance](https://thehackernews.com/search/label/surveillance)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "So...