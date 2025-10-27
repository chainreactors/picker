---
title: Apple Warns of 3 New Vulnerabilities Affecting iPhone, iPad, and Mac Devices
url: https://thehackernews.com/2023/02/apple-warns-of-3-new-vulnerabilities.html
source: The Hacker News
date: 2023-02-23
fetch_date: 2025-10-04T07:54:21.636555
---

# Apple Warns of 3 New Vulnerabilities Affecting iPhone, iPad, and Mac Devices

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

# [Apple Warns of 3 New Vulnerabilities Affecting iPhone, iPad, and Mac Devices](https://thehackernews.com/2023/02/apple-warns-of-3-new-vulnerabilities.html)

**Feb 22, 2023**Ravie LakshmananEndpoint Security / Software Update

[![iPhone, iPad, and Mac Vulnerabilities](data:image/png;base64... "iPhone, iPad, and Mac Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEih7mJXv6IXXF3ENs2cS4vwpCPQoSFdI3A4Zt83tVp-K8Tc3CrTDuT0d4nHyAiTj_v_-sHmGCvNszFDRyS6Me2omtCGc35R6oJ7eszH2t9QktE-ERWfP21sErA4gRTO-beNveLRuT-wYghgnOjfb_0zhEOCNaN5rA225F8SRRooEq0LCK3gDCJQZt7r/s790-rw-e365/apple.jpg)

Apple has revised the [security advisories](https://thehackernews.com/2023/01/apple-issues-updates-for-older-devices.html) it released last month to include three new vulnerabilities impacting [iOS, iPadOS](https://support.apple.com/en-us/HT213606), and [macOS](https://support.apple.com/en-us/HT213605).

The first flaw is a [race condition](https://en.wikipedia.org/wiki/Race_condition) in the Crash Reporter component (CVE-2023-23520) that could enable a malicious actor to read arbitrary files as root. The iPhone maker said it addressed the issue with additional validation.

The two other vulnerabilities, credited to Trellix researcher Austin Emmitt, reside in the [Foundation framework](https://developer.apple.com/documentation/foundation) (CVE-2023-23530 and CVE-2023-23531) and could be weaponized to achieve code execution.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"An app may be able to execute arbitrary code out of its sandbox or with certain elevated privileges," Apple said, adding it patched the issues with "improved memory handling."

The medium to high-severity vulnerabilities have been patched in iOS 16.3, iPadOS 16.3, and macOS Ventura 13.2 that were shipped on January 23, 2023.

[![iPhone, iPad, and Mac Vulnerabilities](data:image/png;base64... "iPhone, iPad, and Mac Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVS-ZByxZ3xOdZgUrEdLXbdYjF-I36XQeb0ste79ikNB28ecm-lYamU3Xbbr82ui-o5DSvGLFd88pgBpXE0pvH9h4FVPUtdg0o46EwYzH8B-_HFjp8SCQPRlylP-mvx8VjcuHaZCm8aSDqFdRSEnk7UesAWZ-gnz6cqPlOAo38vAMF260MBfDdgWu_/s790-rw-e365/appl.png)

Trellix, in its own report on Tuesday, [classified](https://www.trellix.com/en-us/about/newsroom/stories/research/trellix-advanced-research-center-discovers-a-new-privilege-escalation-bug-class-on-macos-and-ios.html) the two flaws as a "new class of bugs that allow bypassing code signing to execute arbitrary code in the context of several platform applications, leading to escalation of privileges and sandbox escape on both macOS and iOS."

The bugs also bypass mitigations Apple put in place to address zero-click exploits like [FORCEDENTRY](https://thehackernews.com/2021/09/apple-issues-urgent-updates-to-fix-new.html), which was leveraged by Israeli mercenary spyware vendor NSO Group to deploy Pegasus on targets' devices.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As a result, a threat actor could exploit these vulnerabilities to break out of the sandbox and execute malicious code with elevated permissions, potentially granting access to calendar, address book, messages, location data, call history, camera, microphone, and photos.

Even more troublingly, the security defects could be abused to install arbitrary applications or even wipe the device. That said, exploitation of the flaws requires an attacker to have already obtained an initial foothold into it.

"The vulnerabilities above represent a significant breach of the security model of macOS and iOS which relies on individual applications having fine-grained access to the subset of resources they need and querying higher privileged services to get anything else," Emmitt said.

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

[Apple](https://thehackernews.com/search/label/Apple)[Apple macOS](https://thehackernews.com/search/label/Apple%20macOS)[iPhone hacking](https://thehackernews.com/search/label/iPhone%20hacking)[patch update](https://thehackernews.com/search/label/patch%20update)[software update](https://thehackernews.com/search/label/software%20update)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit...