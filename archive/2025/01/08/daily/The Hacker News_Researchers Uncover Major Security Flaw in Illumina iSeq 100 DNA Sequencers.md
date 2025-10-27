---
title: Researchers Uncover Major Security Flaw in Illumina iSeq 100 DNA Sequencers
url: https://thehackernews.com/2025/01/researchers-uncover-major-security-flaw.html
source: The Hacker News
date: 2025-01-08
fetch_date: 2025-10-06T20:14:58.416683
---

# Researchers Uncover Major Security Flaw in Illumina iSeq 100 DNA Sequencers

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

# [Researchers Uncover Major Security Flaw in Illumina iSeq 100 DNA Sequencers](https://thehackernews.com/2025/01/researchers-uncover-major-security-flaw.html)

**Jan 07, 2025**Ravie LakshmananFirmware Security / Malware

[![DNA Sequencers](data:image/png;base64... "DNA Sequencers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJlT5tYtaLJ5khiZPA4hcLejgSNqaZdCGG8nqteULrlZ6grBSiJ-z0-l6kGRwuxwuyIBBGH5FQaBZi1MU0h7Zqk8IHM5J2J7lj59qHKL-vfcMc9_hLDTgHvQcIeyC8dC03EiqozXTOVMjoo4VQWJ9dTQiS9iT_4jdy9dLRMLJagyje71TdgNvqduRehGGy/s790-rw-e365/dna.png)

Cybersecurity researchers have uncovered firmware security vulnerabilities in the Illumina iSeq 100 DNA sequencing instrument that, if successfully exploited, could permit attackers to brick or plant persistent malware on susceptible devices.

"The Illumina iSeq 100 used a very outdated implementation of [BIOS](https://en.wikipedia.org/wiki/BIOS) firmware using CSM [Compatibility Support Mode] mode and without Secure Boot or standard firmware write protections," Eclypsium [said](https://eclypsium.com/blog/genetic-engineering-meets-reverse-engineering-dna-sequencers-vulnerable-bios/) in a report shared with The Hacker News.

"This would allow an attacker on the system to overwrite the system firmware to either 'brick' the device or install a firmware implant for ongoing attacker persistence."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While the Unified Extensible Firmware Interface ([UEFI](https://en.wikipedia.org/wiki/UEFI)) is the modern replacement for the Basic Input/Output System (BIOS), the firmware security company said the iSeq 100 boots to an old version of BIOS (B480AM12 - 04/12/2018) that has known vulnerabilities.

Also noticeably absent are protections to tell the hardware where it can read and write firmware, thereby allowing an attacker to modify device firmware. Also not enabled is Secure Boot, thereby allowing malicious changes to the firmware to go undetected.

[![DNA Sequencers](data:image/png;base64... "DNA Sequencers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicQ8UqJTduNgIFj2oAtVK9FWaBe_bfljb3WXi_XdvjkWcNoIqS_pMLpXp9C0wMwNIrBbbEvQA8YOH_mujPCQmlKQMSGuPzmoR8Jei1xxtwpAjR9_Fy7lJMtSxIe-UnV1jbi4Cu3G33Zg0t17IBLIP-E6oLgRnJFRqhPfp0GFQlzWbnBQ-DpwRdP1O0UffF/s790-rw-e365/dnasequencer.png)

Eclypsium pointed out that it's not advisable for newer high-value assets to support CSM, as it's chiefly meant for old devices that can't be upgraded and need to maintain compatibility. Following responsible disclosure, Illumina has released a fix.

In a hypothetical attack scenario, an adversary could target unpatched Illumina devices, escalate their privileges, and write arbitrary code to the firmware to either brick the system or manipulate it to produce unintended outcomes, such as altering the presence or absence of hereditary conditions and faking DNA research.

Eclypsium notes that their "analysis was limited specifically to the iSeq 100 sequencer device" and that similar issues may be present in other medical or industrial devices owing to the fact that the problems have been traced back to an original equipment manufacturer (OEM) motherboard made by IEI Integration Corp.

"This is a perfect example of how mistakes early in the supply chain can have far reaching impacts across many types of devices and vendors," it said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is not the first time severe vulnerabilities have been disclosed in DNA gene sequencers from Illumina. In April 2023, a critical security flaw ([CVE-2023-1968](https://thehackernews.com/2023/04/cisa-warns-of-critical-flaws-in.html), CVSS score: 10.0) could have made it possible to eavesdrop on network traffic and remotely transmit arbitrary commands.

"The ability to overwrite firmware on the iSeq 100 would enable attackers to easily disable the device, causing significant disruption in the context of a ransomware attack. This would not only take a high-value device out of service, it would also likely take considerable effort to recover the device via manually reflashing the firmware," Eclypsium said.

"This could significantly raise the stakes in the context of a ransomware or cyberattack. Sequencers are critical to detecting genetic illnesses, cancers, identifying drug-resistant bacteria, and for the production of vaccines. This would make these devices a ripe target for state-based actors with geopolitical motives in addition to the more traditional financial motives of ransomware actors."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DNA Sequencing](https://thehackernews.com/search/label/DNA%20Sequencing)[firmware](https://thehackernews.com/search/label/firmware)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)[Secure Boot](https://thehackernews.com/search/label/Secure%20Boot)[Threat Analysis](https://thehackernews.com/search/label/Threat%20Analysis)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop ...