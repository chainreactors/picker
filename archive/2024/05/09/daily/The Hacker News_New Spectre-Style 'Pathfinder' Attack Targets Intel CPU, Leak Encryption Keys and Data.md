---
title: New Spectre-Style 'Pathfinder' Attack Targets Intel CPU, Leak Encryption Keys and Data
url: https://thehackernews.com/2024/05/new-spectre-style-pathfinder-attack.html
source: The Hacker News
date: 2024-05-09
fetch_date: 2025-10-06T17:30:06.776892
---

# New Spectre-Style 'Pathfinder' Attack Targets Intel CPU, Leak Encryption Keys and Data

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

# [New Spectre-Style 'Pathfinder' Attack Targets Intel CPU, Leak Encryption Keys and Data](https://thehackernews.com/2024/05/new-spectre-style-pathfinder-attack.html)

**May 08, 2024**Ravie LakshmananData Encryption / Hardware Security

[![Encryption Keys](data:image/png;base64... "Encryption Keys")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCsXxKSHjymsIMRDDrahsvY3mz_fB0fJj8ZZiVAsOCuyhG7SsO0WlvM_jMqvLhVvvEAsX0Pi2sbuDgu8ZMlNRaK_OkANH4GzvsL8K7TYEcyI-dvPzbHMC-H-1lYURtObXu8WLtF56ou9HUkmg_6mRikd1gp6KOXuDMgvV-LdLOogFHxVGWx2pOeVchbVx6/s790-rw-e365/cpu.png)

Researchers have discovered two novel attack methods targeting high-performance Intel CPUs that could be exploited to stage a key recovery attack against the Advanced Encryption Standard (AES) algorithm.

The techniques have been collectively dubbed **Pathfinder** by a group of academics from the University of California San Diego, Purdue University, UNC Chapel Hill, Georgia Institute of Technology, and Google.

"Pathfinder allows attackers to read and manipulate key components of the branch predictor, enabling two main types of attacks: reconstructing program control flow history and launching high-resolution Spectre attacks," Hosein Yavarzadeh, the lead author of the [paper](https://dl.acm.org/doi/10.1145/3620666.3651382), said in a statement shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This includes extracting secret images from libraries like libjpeg and recovering encryption keys from AES through intermediate value extraction."

Spectre is the name given to a [class of side-channel attacks](https://thehackernews.com/2024/04/researchers-uncover-first-native.html) that exploit [branch prediction](https://en.wikipedia.org/wiki/Branch_predictor) and [speculative execution](https://en.wikipedia.org/wiki/Speculative_execution) on modern CPUs to read privileged data in the memory in a manner that sidesteps isolation protections between applications.

The latest attack approach targets a feature in the branch predictor called the Path History Register ([PHR](https://ieeexplore.ieee.org/document/955033)) – which keeps a record of the last taken branches -- to induce branch mispredictions and cause a victim program to execute unintended code paths, thereby inadvertently exposing its confidential data.

Specifically, it introduces new primitives that make it possible to manipulate PHR as well as the prediction history tables (PHTs) within the conditional branch predictor (CBR) to leak historical execution data and ultimately trigger a Spectre-style exploit.

In a set of demonstrations outlined in the study, the method has been found effective in extracting the secret AES encryption key as well as leaking secret images during processing by the widely-used libjpeg image library.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Following responsible disclosure in November 2023, Intel, in an [advisory](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2024-04-26-001.html) released last month, said Pathfinder builds on [Spectre v1 attacks](https://thehackernews.com/2024/03/ghostrace-new-data-leak-vulnerability.html) and that previously deployed mitigations for Spectre v1 and traditional side-channels mitigate the reported exploits. There is [no evidence](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7015.html) that it impacts AMD CPUs.

"[This research] demonstrates that the PHR is vulnerable to leakage, reveals data unavailable through the PHTs (ordered outcomes of repeated branches, global ordering of all branch outcomes), exposes a far greater set of branching code as potential attack surfaces, and cannot be mitigated (cleared, obfuscated) using techniques proposed for the PHTs," the researchers said.

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

[AMD](https://thehackernews.com/search/label/AMD)[CPU Security](https://thehackernews.com/search/label/CPU%20Security)[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data encryption](https://thehackernews.com/search/label/data%20encryption)[data security](https://thehackernews.com/search/label/data%20security)[encryption](https://thehackernews.com/search/label/encryption)[ethical hacking](https://thehackernews.com/search/label/ethical%20hacking)[Intel](https://thehackernews.com/search/label/Intel)[speculative execution](https://thehackernews.com/search/label/speculative%20execution)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Ev...