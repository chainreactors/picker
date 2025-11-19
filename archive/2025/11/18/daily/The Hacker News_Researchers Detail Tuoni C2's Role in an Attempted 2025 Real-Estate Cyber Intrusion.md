---
title: Researchers Detail Tuoni C2's Role in an Attempted 2025 Real-Estate Cyber Intrusion
url: https://thehackernews.com/2025/11/researchers-detail-tuoni-c2s-role-in.html
source: The Hacker News
date: 2025-11-18
fetch_date: 2025-11-19T03:14:54.527885
---

# Researchers Detail Tuoni C2's Role in an Attempted 2025 Real-Estate Cyber Intrusion

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Researchers Detail Tuoni C2's Role in an Attempted 2025 Real-Estate Cyber Intrusion](https://thehackernews.com/2025/11/researchers-detail-tuoni-c2s-role-in.html)

**Nov 18, 2025**Ravie LakshmananMalware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0fEPwtke4h6m4SAYqYOUAQSTCvVaghxz5SGIgAKzQlXlriWAB02H4u9ueIs8oX7vH4a3Xx46gIt-0qC_eEECEMdyBADDmMnoNvbNM-5wIwkVPSo0f88Sy2Ik5bvBQdxtwRWGO6vQvzj_rPWpAYJbfOuGNK0q6yNhyE9QR5h98xsW7d8A6yBQ8p0P5bt4G/s790-rw-e365/c2.jpg)

Cybersecurity researchers have disclosed details of a cyber attack targeting a major U.S.-based real-estate company that involved the use of a nascent command-and-control (C2) and red teaming framework known as **Tuoni**.

"The campaign leveraged the emerging Tuoni C2 framework, a relatively new, command-and-control (C2) tool (with a free license) that delivers stealthy, in-memory payloads," Morphisec researcher Shmuel Uzan [said](https://www.morphisec.com/blog/morphisec-thwarts-sophisticated-tuoni-c2-attack-on-us-real-estate-firm/) in a report shared with The Hacker News.

Tuoni is advertised as an advanced C2 framework designed for security professionals, facilitating penetration testing operations, red team engagements, and security assessments. A "Community Edition" of the software is [freely available](https://github.com/shell-dot/tuoni) for download from GitHub. It was first released in early 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

The attack, per Morphisec, unfolded in mid-October 2025, with the unknown threat actor likely leveraging social engineering via [Microsoft Teams impersonation](https://thehackernews.com/2025/06/former-black-basta-members-use.html) for initial access. It's suspected that the attackers likely posed as trusted vendors or colleagues to deceive an employee at the company into running a PowerShell command.

The command, for its part, downloads a second PowerShell script from an external server ("kupaoquan[.]com"), which, in turn, employs steganographic tricks to conceal the next-stage payload within a bitmap image (BMP). The primary goal of the embedded payload is to extract shellcode and execute it directly in memory.

This results in the execution of "TuoniAgent.dll," which corresponds to an [agent](https://docs.shelldot.com/HowToUse/Terminology.html) that operates within the targeted machine and connects to a C2 server (in this case, "kupaoquan[.]com"), allowing for remote control.

"While Tuoni itself is a sophisticated but traditional C2 framework, the delivery mechanism showed signs of AI assistance in code generation, evident from the scripted comments and modular structure of the initial loader," Morphisec added.

The attack, although ultimately unsuccessful, demonstrates continued abuse of red teaming tools for malicious purposes. In September 2025, Check Point [detailed](https://thehackernews.com/2025/09/threat-actors-weaponize-hexstrike-ai-to.html) the use of an artificial intelligence (AI)-powered tool called HexStrike AI to rapidly accelerate and simplify vulnerability exploitation.

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

[Command and Control](https://thehackernews.com/search/label/Command%20and%20Control)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[powershell](https://thehackernews.com/search/label/powershell)[Red Team](https://thehackernews.com/search/label/Red%20Team)[social engineering](https://thehackernews.com/search/label/social%20engineering)[Steganography](https://thehackernews.com/search/label/Steganography)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More")

⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](https://thehackernews.com/2025/11/weekly-recap-hyper-v-malware-malicious.html)

[![Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic](data:image/svg+xml;base64... "Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic")

Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic](https://thehackernews.com/2025/11/microsoft-uncovers-whisper-leak-attack.html)

[![WhatsApp Malware 'Maverick' Hijacks Browser Sessions to Target Brazil's Biggest Banks](data:image/svg+xml;base64... "WhatsApp Malware 'Maverick' Hijacks Browser Sessions to Target Brazil's Biggest Banks")

WhatsApp Malware 'Maverick' Hijacks Browser Sessions to Target Brazil's Biggest Banks](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html)

[![Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack](data:image/svg+xml;base64... "Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack")

Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Z...