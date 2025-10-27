---
title: New SideWinder Cyber Attacks Target Maritime Facilities in Multiple Countries
url: https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html
source: The Hacker News
date: 2024-07-31
fetch_date: 2025-10-06T17:47:03.999019
---

# New SideWinder Cyber Attacks Target Maritime Facilities in Multiple Countries

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

# [New SideWinder Cyber Attacks Target Maritime Facilities in Multiple Countries](https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html)

**Jul 30, 2024**Ravie LakshmananCyber Espionage / Malware

[![Maritime Facilities](data:image/png;base64... "Maritime Facilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhffqOyqjZOhe7FPCybsN1P17DVC4wzMK9_bYDaoYRWA_EDGk2YjSE3axZyrU1vPmfF1TsEyIuHfinAqGRy_FVugLwZuPcfeDRS3T-BL5d6IMnOHCYwsiMH07op3T1Qx4APJs0URzZQxmgGG5dHj1n3xyuXHT-QctmR8ug_eofzi4Ia_Z5RJK8cpWKBiZpB/s790-rw-e365/port.png)

The nation-state threat actor known as SideWinder has been attributed to a new cyber espionage campaign targeting ports and maritime facilities in the Indian Ocean and Mediterranean Sea.

The BlackBerry Research and Intelligence Team, which [discovered](https://blogs.blackberry.com/en/2024/07/sidewinder-targets-ports-and-maritime-facilities-in-the-mediterranean-sea) the activity, said targets of the spear-phishing campaign include countries like Pakistan, Egypt, Sri Lanka, Bangladesh, Myanmar, Nepal, and the Maldives.

[SideWinder](https://thehackernews.com/2023/05/state-sponsored-sidewinder-hacker.html), which is also known by the names APT-C-17, Baby Elephant, Hardcore Nationalist, Leafperforator, Rattlesnake, and Razor Tiger, is assessed to be affiliated with India. It has been operational since 2012, often making use of spear-phishing as a vector to deliver malicious payloads that trigger the attack chains.

"SideWinder makes use of email spear-phishing, document exploitation and DLL side-loading techniques in an attempt to avoid detection and deliver targeted implants," the Canadian cybersecurity company said in an analysis published last week.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The latest set of attacks employ lures related to sexual harassment, employee termination, and salary cuts in order to negatively impact the recipients' emotional state and trick them into opening booby-trapped Microsoft Word documents.

Once the decoy file is opened, it leverages a known security flaw ([CVE-2017-0199](https://thehackernews.com/2024/06/china-linked-valleyrat-malware.html)) to establish contact with a malicious domain that masquerades as Pakistan's Directorate General Ports and Shipping ("reports.dgps-govtpk[.]com") to retrieve an RTF file.

[![SideWinder Cyber Attacks](data:image/png;base64... "SideWinder Cyber Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiq-Id29ylVERZXBVNavBPr3k-eOHG-sReuAEC-qq0ZSct9d1JNxYRRy1P96tiz6V1U00xmvUV4B4Ig1iORgdAV9IMs2ete2Go2nY0kuLUyQgQHr2434dciDMaUBkpbkr-zYzwl4al12u8-N645qNTpHKD7kNQq2z3HiDcwryxbFs264TUbQpt-S4oiczsc/s790-rw-e365/side.png)

The RTF document, in turn, downloads a document that exploits [CVE-2017-11882](https://thehackernews.com/2023/12/hackers-exploiting-old-ms-excel.html), another years-old security vulnerability in the Microsoft Office Equation Editor, with the goal of executing shellcode that's responsible for launching JavaScript code, but only after ensuring that the compromised system is legitimate and is of interest to the threat actor.

It's currently not known what's delivered by means of the JavaScript malware, although the end goal is likely to be intelligence gathering based on prior campaigns mounted by SideWinder.

"The SideWinder threat actor continues to improve its infrastructure for targeting victims in new regions," BlackBerry said. "The steady evolution of its network infrastructure and delivery payloads suggests that SideWinder will continue its attacks in the foreseeable future."

The disclosure comes as a suspected Russian-linked threat actor is [targeting](https://www.broadcom.com/support/security-center/protection-bulletin/russian-linked-malware-campaign-targeting-indian-political-entities) entities interested in Indian political affairs with a Go-based remote access trojan (RAT) that's delivered via a .NET loader launched from Windows shortcut (LNK) files disguised as Office documents. The activity has been codenamed Operation ShadowCat.

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

[BlackBerry](https://thehackernews.com/search/label/BlackBerry)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Microsoft](https://thehackernews.com/search/label/Microsoft)[Spear-Phishing](https://thehackernews.com/search/label/Spear-Phishing)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehac...