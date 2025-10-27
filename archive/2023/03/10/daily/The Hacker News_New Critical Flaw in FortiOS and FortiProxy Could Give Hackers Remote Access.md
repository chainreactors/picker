---
title: New Critical Flaw in FortiOS and FortiProxy Could Give Hackers Remote Access
url: https://thehackernews.com/2023/03/new-critical-flaw-in-fortios-and.html
source: The Hacker News
date: 2023-03-10
fetch_date: 2025-10-04T09:11:54.087328
---

# New Critical Flaw in FortiOS and FortiProxy Could Give Hackers Remote Access

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

# [New Critical Flaw in FortiOS and FortiProxy Could Give Hackers Remote Access](https://thehackernews.com/2023/03/new-critical-flaw-in-fortios-and.html)

**Mar 09, 2023**Ravie LakshmananNetwork Security / Firewall

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6-TaG1XxJU9BpBDBUSTcG7I9lBJp8URntopfS53g8n_9hE0EiF2l55hHY8q4bIcJs8Gb6pO1N68jd9x7OmUAL9cBvT4KXNlDCn9AuDQwDF_aAFnFdLgYIsr3WGbd5FhxF9xnk0iEUJWeVItwtmTfSayHy_IgRXJBuPK7IxnO-oOT0v6Ef3hFzXsOM/s790-rw-e365/fortnet.png)

Fortinet has released fixes to [address 15 security flaws](https://www.fortiguard.com/psirt?date=03-2023), including one critical vulnerability impacting FortiOS and FortiProxy that could enable a threat actor to take control of affected systems.

The issue, tracked as **CVE-2023-25610**, is rated 9.3 out of 10 for severity and was internally discovered and reported by its security teams.

"A buffer underwrite ('buffer underflow') vulnerability in FortiOS and FortiProxy administrative interface may allow a remote unauthenticated attacker to execute arbitrary code on the device and/or perform a DoS on the GUI, via specifically crafted requests," Fortinet [said](https://www.fortiguard.com/psirt/FG-IR-23-001) in an advisory.

[Underflow bugs](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/BufferOverflows.html), also called [buffer underruns](https://cwe.mitre.org/data/definitions/124.html), occur when the input data is shorter than the reserved space, causing unpredictable behavior or leakage of sensitive data from memory.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Other possible consequences include memory corruption that could either be weaponized to induce a crash or execute arbitrary code.

Fortinet said it's not aware of any malicious exploitation attempts against the flaw. But given that prior flaws in software have come under active abuse in the wild, it's essential that users move quickly to apply the patches.

The following versions of FortiOS and FortiProxy are impacted by the vulnerability -

* FortiOS version 7.2.0 through 7.2.3
* FortiOS version 7.0.0 through 7.0.9
* FortiOS version 6.4.0 through 6.4.11
* FortiOS version 6.2.0 through 6.2.12
* FortiOS 6.0 all versions
* FortiProxy version 7.2.0 through 7.2.2
* FortiProxy version 7.0.0 through 7.0.8
* FortiProxy version 2.0.0 through 2.0.11
* FortiProxy 1.2 all versions
* FortiProxy 1.1 all versions

Fixes are available in FortiOS versions 6.2.13, 6.4.12, 7.0.10, 7.2.4, and 7.4.0; FortiOS-6K7K versions 6.2.13, 6.4.12, and 7.0.10; and FortiProxy versions 2.0.12, 7.0.9, and 7.0.9.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As workarounds, Fortinet is recommending that users either disable the HTTP/HTTPS administrative interface or limit IP addresses that can reach it.

The disclosure comes weeks after the network security company issued fixes for [40 vulnerabilities](https://thehackernews.com/2023/02/fortinet-issues-patches-for-40-flaws.html), two of which are rated Critical and impact FortiNAC (CVE-2022-39952) and FortiWeb (CVE-2021-42756) products.

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

[Firewall](https://thehackernews.com/search/label/Firewall)[Fortinet](https://thehackernews.com/search/label/Fortinet)[FortiOS](https://thehackernews.com/search/label/FortiOS)[FortiProxy](https://thehackernews.com/search/label/FortiProxy)[network security](https://thehackernews.com/search/label/network%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/20...