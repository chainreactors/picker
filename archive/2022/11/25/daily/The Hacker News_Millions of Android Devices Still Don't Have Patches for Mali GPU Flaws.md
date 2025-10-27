---
title: Millions of Android Devices Still Don't Have Patches for Mali GPU Flaws
url: https://thehackernews.com/2022/11/million-of-android-devices-still-dont.html
source: The Hacker News
date: 2022-11-25
fetch_date: 2025-10-03T23:45:55.513144
---

# Millions of Android Devices Still Don't Have Patches for Mali GPU Flaws

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

# [Millions of Android Devices Still Don't Have Patches for Mali GPU Flaws](https://thehackernews.com/2022/11/million-of-android-devices-still-dont.html)

**Nov 24, 2022**Ravie Lakshmanan

[![Android Devices](data:image/png;base64... "Android Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjL8SpMdZOqjM2-RsKHi5mXnASyjBGh8o83J2GDDjyGBZAev3wSElvOMbIGMDO4_1N1uJkDBbVGgOjAkp34tiCNwYVpes6dNm1rgF0rzwz8ezDRcSBTGSh1sxKxFS3Rc0zPQHiLRixf8GBUnvKGad_7S1iMQ3iWHV2qKMpZg_zzdE53KiqWNXDDJIcw/s790-rw-e365/android-hacking.jpg)

A set of five medium-severity security flaws in Arm's Mali GPU driver has continued to remain unpatched on Android devices for months, despite fixes released by the chipmaker.

Google Project Zero, which discovered and reported the bugs, said Arm addressed the shortcomings in July and August 2022.

"These fixes have not yet made it downstream to affected Android devices (including Pixel, Samsung, Xiaomi, Oppo, and others)," Project Zero researcher Ian Beer [said](https://googleprojectzero.blogspot.com/2022/11/mind-the-gap.html) in a report. "Devices with a Mali GPU are currently vulnerable."

The vulnerabilities, collectively tracked under the identifiers [CVE-2022-33917](https://nvd.nist.gov/vuln/detail/CVE-2022-33917) (CVSS score: 5.5) and [CVE-2022-36449](https://nvd.nist.gov/vuln/detail/CVE-2022-36449) (CVSS score: 6.5), concern a case of improper memory processing, thereby allowing a non-privileged user to gain access to freed memory.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The second flaw, CVE-2022-36449, can be further weaponized to write outside of buffer bounds and disclose details of memory mappings, according to an [advisory](https://developer.arm.com/Arm%20Security%20Center/Mali%20GPU%20Driver%20Vulnerabilities) issued by Arm. The list of affected drivers is below -

**CVE-2022-33917**

* Valhall GPU Kernel Driver: All versions from r29p0 – r38p0

**CVE-2022-36449**

* Midgard GPU Kernel Driver: All versions from r4p0 – r32p0
* Bifrost GPU Kernel Driver: All versions from r0p0 – r38p0, and r39p0
* Valhall GPU Kernel Driver: All versions from r19p0 – r38p0, and r39p0

A successful exploitation of the flaws could permit an attacker with permissions to execute native code in an app context to seize control of the system and bypass Android's permissions model to gain broad access to user data.

Google told The Hacker News that the fix provided by Arm is currently undergoing testing for Android and Pixel devices, and that it's expected to be shipped in the coming weeks. Other Android handset makers are required to take the patch to comply with future security patch level ([SPL](https://source.android.com/docs/security/bulletin)) requirements.

The findings once again highlight how patch gaps can render millions of devices vulnerable at once and put them at risk of heightened exploitation by threat actors.

"Just as users are recommended to patch as quickly as they can once a release containing security updates is available, so the same applies to vendors and companies," Beer said.

"Companies need to remain vigilant, follow upstream sources closely, and do their best to provide complete patches to users as soon as possible."

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

[Android](https://thehackernews.com/search/label/Android)[Google Project Zero](https://thehackernews.com/search/label/Google%20Project%20Zero)[GPU Driver](https://thehackernews.com/search/label/GPU%20Driver)[Kernel Driver](https://thehackernews.com/search/label/Kernel%20Driver)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnyw...