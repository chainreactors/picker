---
title: New Linux Ransomware Strain BlackSuit Shows Striking Similarities to Royal
url: https://thehackernews.com/2023/06/new-linux-ransomware-strain-blacksuit.html
source: The Hacker News
date: 2023-06-04
fetch_date: 2025-10-04T11:46:47.230896
---

# New Linux Ransomware Strain BlackSuit Shows Striking Similarities to Royal

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

# [New Linux Ransomware Strain BlackSuit Shows Striking Similarities to Royal](https://thehackernews.com/2023/06/new-linux-ransomware-strain-blacksuit.html)

**Jun 03, 2023**Ravie LakshmananEndpoint Security / Linux

[![Linux Ransomware](data:image/png;base64... "Linux Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKj8Z7rui-M7hqSXsiDd70DbOuErF4KYni7y83WYlLpeBp1nurusvmMezzyPLZa0l9-UvbKM9oC8DHlSgZVuOHzJbPvVNw9B0nujVH5QsUsOVUzrzZEkhgKaT__hfAfXfayzK2UbjOxqPCUInGhiYnpFDr5lFkXN69Cbykr8JfVxyBLX3XmehH39Cn/s790-rw-e365/ransomware.jpg)

An analysis of the Linux variant of a new ransomware strain called BlackSuit has covered significant similarities with another ransomware family called [Royal](https://thehackernews.com/2023/03/us-cybersecurity-agency-raises-alarm.html).

Trend Micro, which examined an x64 VMware ESXi version targeting Linux machines, said it identified an "extremely high degree of similarity" between Royal and BlackSuit.

"In fact, they're nearly identical, with 98% similarities in functions, 99.5% similarities in blocks, and 98.9% similarities in jumps based on BinDiff, a comparison tool for binary files," Trend Micro researchers [noted](https://www.trendmicro.com/en_us/research/23/e/investigating-blacksuit-ransomwares-similarities-to-royal.html).

A comparison of the Windows artifacts has identified 93.2% similarity in functions, 99.3% in basic blocks, and 98.4% in jumps based on BinDiff.

BlackSuit [first came to light](https://twitter.com/Unit42_Intel/status/1653760405792014336) in early [May 2023](https://thehackernews.com/2023/05/new-ransomware-gang-ra-group-hits-us.html) when Palo Alto Networks Unit 42 drew attention to its ability to target both Windows and Linux hosts.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In line with other ransomware groups, it runs a double extortion scheme that steals and encrypts sensitive data in a compromised network in return for monetary compensation. Data associated with a single victim has been listed on its dark web leak site.

The latest findings from Trend Micro show that, both BlackSuit and Royal use OpenSSL's AES for encryption and utilize similar [intermittent encryption](https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/) techniques to speed up the encryption process.

The overlaps aside, BlackSuit incorporates additional command-line arguments and avoids a different list of files with specific extensions during enumeration and encryption.

"The emergence of BlackSuit ransomware (with its similarities to Royal) indicates that it is either a new variant developed by the same authors, a copycat using similar code, or an affiliate of the Royal ransomware gang that has implemented modifications to the original family," Trend Micro said.

Given that [Royal](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html) is an offshoot of the [erstwhile Conti team](https://thehackernews.com/2022/05/conti-ransomware-gang-shut-down-after.html), it's also possible that "BlackSuit emerged from a splinter group within the original Royal ransomware gang," the cybersecurity company theorized.

The development once again underscores the [constant state of flux](https://thehackernews.com/2023/06/improved-blackcat-ransomware-strikes.html) in the [ransomware ecosystem](https://therecord.media/wazawaka-cyber-most-wanted-interview-click-here), even as new threat actors emerge to tweak existing tools and generate illicit profits.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This includes a new ransomware-as-a-service (RaaS) initiative codenamed [NoEscape](https://blog.cyble.com/2023/06/01/noescape-ransomware-as-a-service-raas/) that Cyble said allows its operators and affiliates to take advantage of triple extortion methods to maximize the impact of a successful attack.

Triple extortion refers to a [three-pronged approach](https://www.akamai.com/blog/security/defeating-triple-extortion-ransomware) wherein data exfiltration and encryption is coupled with distributed denial-of-service (DDoS) attacks against the targets in an attempt to disrupt their business and coerce them into paying the ransom.

The DDoS service, per Cyble, is available for an added $500,000 fee, with the operators imposing conditions that forbid affiliates from striking entities located in the Commonwealth of Independent States ([CIS](https://en.wikipedia.org/wiki/Commonwealth_of_Independent_States)) countries.

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

[encryption](https://thehackernews.com/search/label/encryption)[linux](https://thehackernews.com/search/label/linux)[ransomware](https://thehackernews.com/search/label/ransomware)[vmware](https://thehackernews.com/search/label/vmware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Fla...