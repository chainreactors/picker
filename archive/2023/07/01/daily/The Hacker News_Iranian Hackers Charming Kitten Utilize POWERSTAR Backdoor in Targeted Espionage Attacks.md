---
title: Iranian Hackers Charming Kitten Utilize POWERSTAR Backdoor in Targeted Espionage Attacks
url: https://thehackernews.com/2023/06/iranian-hackers-charming-kitten-utilize.html
source: The Hacker News
date: 2023-07-01
fetch_date: 2025-10-04T11:57:21.274910
---

# Iranian Hackers Charming Kitten Utilize POWERSTAR Backdoor in Targeted Espionage Attacks

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

# [Iranian Hackers Using POWERSTAR Backdoor in Targeted Espionage Attacks](https://thehackernews.com/2023/06/iranian-hackers-charming-kitten-utilize.html)

**Jun 30, 2023**The Hacker NewsCyber Espionage/ Malware

[![Iranian Hackers](data:image/png;base64... "Iranian Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC4qls6fQ_-M5iFAFX4raY0CaD_EzLdz1yetNAGJaJlp6Z-zCSH6NMiEUPbSCqnf3SRrq1SJTS-py63oaiRPUOUvF7JdioM0B4u9h-6w66ZGoUyeUf5USiCO-OmnDgdBlVKm8IwKMOVngYFztxbvSEb_zRp75jWpwpVVj3QthwwfCCQz5IJceqaj_0HXel/s790-rw-e365/hacking.jpg)

Charming Kitten, the nation-state actor affiliated with Iran's Islamic Revolutionary Guard Corps (IRGC), has been attributed to a bespoke spear-phishing campaign that delivers an updated version of a fully-featured PowerShell backdoor called **POWERSTAR**.

"There have been improved operational security measures placed in the malware to make it more difficult to analyze and collect intelligence," Volexity researchers Ankur Saini and Charlie Gardner [said](https://www.volexity.com/blog/2023/06/28/charming-kitten-updates-powerstar-with-an-interplanetary-twist/) in a report published this week.

The [threat actor](https://thehackernews.com/2023/04/iranian-government-backed-hackers.html) is something of an expert when it comes to employing social engineering to lure targets, often crafting tailored fake personas on social media platforms and engaging in sustained conversations to build rapport before sending a malicious link. It's also tracked under the names APT35, Cobalt Illusion, Mint Sandstorm (formerly Phosphorus), and Yellow Garuda.

Recent intrusions orchestrated by Charming Kitten have made use of other implants such as [PowerLess](https://thehackernews.com/2023/04/iranian-hackers-launch-sophisticated.html) and [BellaCiao](https://thehackernews.com/2023/04/charming-kittens-new-bellaciao-malware.html), suggesting that the group is utilizing an array of espionage tools at its disposal to realize its strategic objectives.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

POWERSTAR is another addition to the group's arsenal. Also called CharmPower, the backdoor was [first publicly documented](https://thehackernews.com/2022/01/iranian-hackers-exploit-log4j.html) by Check Point in January 2022, uncovering its use in connection with attacks weaponizing the Log4Shell vulnerabilities in publicly-exposed Java applications.

It has since been put to use in at least two other campaigns, as documented by PwC in [July 2022](https://thehackernews.com/2022/08/google-uncovers-tool-used-by-iranian.html) and Microsoft in [April 2023](https://thehackernews.com/2023/04/iranian-government-backed-hackers.html).

Volexity, which detected a rudimentary variant of POWERSTAR in 2021 distributed by a malicious macro embedded in DOCM file, said the May 2023 attack wave leverages an LNK file inside a password-protected RAR file to download the backdoor from Backblaze, while also taking steps to hinder analysis.

"With POWERSTAR, Charming Kitten sought to limit the risk of exposing their malware to analysis and detection by delivering the decryption method separately from the initial code and never writing it to disk," the researchers said.

"This has the added bonus of acting as an operational guardrail, as decoupling the decryption method from its command-and-control (C2) server prevents future successful decryption of the corresponding POWERSTAR payload."

The backdoor comes with an extensive set of features that enable it to remotely execute PowerShell and C# commands, set up persistence, collect system information, and download and execute more modules to enumerate running processes, capture screenshots, search for files matching specific extensions, and monitor if persistence components are still intact.

Also improved and expanded from the earlier version is the cleanup module that's designed to erase all traces of the malware's footprint as well as delete persistence-related registry keys. These updates point to Charming Kitten's continued efforts to refine its techniques and evade detection.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Volexity said it also detected a different variant of POWERSTAR that attempts to retrieve a hard-coded C2 server by decoding a file stored on the decentralized InterPlanetary Filesystem ([IPFS](https://thehackernews.com/2022/11/several-cyber-attacks-observed.html)), signaling an attempt to make its attack infrastructure more resilient.

The development coincides with a MuddyWater's (aka Static Kitten) use of previously undocumented command-and-control (C2) framework called [PhonyC2](https://thehackernews.com/2023/06/from-muddyc3-to-phonyc2-irans.html) to deliver malicious payload to compromised hosts.

"The general phishing playbook used by Charming Kitten and the overall purpose of POWERSTAR remain consistent," the researchers said. "The references to persistence mechanisms and executable payloads within the POWERSTAR Cleanup module strongly suggests a broader set of tools used by Charming Kitten to conduct malware-enabled espionage."

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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
[![Facebook Messenger](data:image/png;base64...)Share on Faceboo...