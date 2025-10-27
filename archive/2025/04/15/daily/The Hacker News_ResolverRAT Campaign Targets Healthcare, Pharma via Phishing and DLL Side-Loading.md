---
title: ResolverRAT Campaign Targets Healthcare, Pharma via Phishing and DLL Side-Loading
url: https://thehackernews.com/2025/04/resolverrat-campaign-targets-healthcare.html
source: The Hacker News
date: 2025-04-15
fetch_date: 2025-10-06T22:09:11.147726
---

# ResolverRAT Campaign Targets Healthcare, Pharma via Phishing and DLL Side-Loading

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

# [ResolverRAT Campaign Targets Healthcare, Pharma via Phishing and DLL Side-Loading](https://thehackernews.com/2025/04/resolverrat-campaign-targets-healthcare.html)

**Apr 14, 2025**Ravie LakshmananMalware / Cybercrime

[![ResolverRAT Campaign](data:image/png;base64... "ResolverRAT Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgix_43i4U2O57aK8hiqnp67hzJV2T6PAAz3IOzHGgyhDGT_nxaXPUjVqTFcMmEQ7UG2Q_XUFFwf3bsMk5H8YadvlYuvivTJJIno6L-vwWncP8CXxv9uW2BelEIswXVU6oCe7GcYRTUxEEd5rx-MORiXEyFq0H5-K7nU-7kCX6qlEWRwmQWPHs1lvwkwg6D/s790-rw-e365/healthcare-cyberattack.jpg)

Cybersecurity researchers have discovered a new, sophisticated remote access trojan called ResolverRAT that has been observed in attacks targeting healthcare and pharmaceutical sectors.

"The threat actor leverages fear-based lures delivered via phishing emails, designed to pressure recipients into clicking a malicious link," Morphisec Labs researcher Nadav Lorber [said](https://www.morphisec.com/blog/new-malware-variant-identified-resolverrat-enters-the-maze/) in a report shared with The Hacker News. "Once accessed, the link directs the user to download and open a file that triggers the ResolverRAT execution chain."

The activity, observed as recently as March 10, 2025, shares infrastructure and delivery mechanism overlap with phishing campaigns that have distributed information stealer malware such as Lumma and Rhadamanthys, as documented by [Cisco Talos](https://thehackernews.com/2024/11/new-phishing-kit-xiu-gou-targets-users.html) and [Check Point](https://thehackernews.com/2024/11/steelfox-and-rhadamanthys-malware-use.html) last year.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A notable aspect of the campaign is the use of localized phishing lures, with the emails crafted in the languages predominantly spoken in the targeted countries. This includes Hindi, Italian, Czech, Turkish, Portuguese, and Indonesian, indicating the threat actor's attempts to cast a wide net through region-specific targeting and maximize infection rates.

The textual content in the email messages employs themes related to legal investigations or copyright violations that seek to induce a false sense of urgency and increase the likelihood of user interaction.

The infection chain is characterized by the use of the DLL side-loading technique to initiate the process. The first stage is an in-memory loader that decrypts and executes the main payload while also incorporating a bevy of tricks to fly under the radar. Not only does the ResolverRAT payload use encryption and compression, but it also exists only in memory once it's decoded.

"The ResolverRAT's initialization sequence reveals a sophisticated, multi-stage bootstrapping process engineered for stealth and resilience," Lorber said, adding it "implements multiple redundant persistence methods" by means of Windows Registry and on the file system by installing itself in different locations as a fallback mechanism.

Once launched, the malware utilizes a bespoke certificate-based authentication prior to establishing contact with a command-and-control (C2) server such that it bypasses the machine's root authorities. It also implements an IP rotation system to connect to an alternate C2 server if the primary C2 server becomes unavailable or gets taken down.

Furthermore, ResolverRAT is fitted with capabilities to sidestep detection efforts through certificate pinning, source code obfuscation, and irregular beaconing patterns to the C2 server.

"This advanced C2 infrastructure demonstrates the advanced capabilities of the threat actor, combining secure communications, fallback mechanisms, and evasion techniques designed to maintain persistent access while evading detection by security monitoring systems," Morphisec said.

The ultimate goal of the malware is to process commands issued by the C2 server and exfiltrate the responses back, breaking data over 1 MB in size into 16 KB chunks so as to minimize the chances of detection.

The campaign has yet to be attributed to a specific group or country, although the similarities in lure themes and the use of DLL side-loading with previously observed phishing attacks allude to a possible connection.

"The alignment [...] indicates a possible overlap in threat actor infrastructure or operational playbooks, potentially pointing to a shared affiliate model or coordinated activity among related threat groups," the company said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as CYFIRMA detailed another remote access trojan codenamed Neptune RAT that uses a modular, plugin-based approach to steal information, maintain persistence on the host, demand a $500 ransom, and even overwrite the Master Boot Record (MBR) to disrupt the normal functioning of the Windows system.

It's being propagated freely via GitHub, Telegram, and YouTube. That said, the GitHub profile associated with the malware, called the [MasonGroup](https://web.archive.org/web/20250409204243/https%3A//github.com/masongroup) (aka FREEMASONRY), is no longer accessible.

"Neptune RAT incorporates advanced anti-analysis techniques and persistence methods to maintain its presence on the victim's system for extended periods and comes packed with dangerous features," the company [noted](https://www.cyfirma.com/research/neptune-rat-an-advanced-windows-rat-with-system-destruction-capabilities-and-password-exfiltration-from-270-applications/) in an analysis published last week.

It includes a "crypto clipper, password stealer with capabilities to exfiltrate over 270+ different applications' credentials, ransomware capabilities, and live desktop monitoring, making it an extremely serious threat."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](...