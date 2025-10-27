---
title: New Research Delves into the World of Malicious LNK Files and Hackers Behind Them
url: https://thehackernews.com/2023/01/new-research-delves-into-world-of.html
source: The Hacker News
date: 2023-01-20
fetch_date: 2025-10-04T04:26:08.767102
---

# New Research Delves into the World of Malicious LNK Files and Hackers Behind Them

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

# [New Research Delves into the World of Malicious LNK Files and Hackers Behind Them](https://thehackernews.com/2023/01/new-research-delves-into-world-of.html)

**Jan 19, 2023**Ravie LakshmananThreat Intelligence / Malware

[![Malicious LNK Files](data:image/png;base64... "Malicious LNK Files")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxUo-3pj1zuNT76h4bHrogXLoj14k5e-466G4BJVlIZauopKJZRs2yCLg4j_oWYtUs7sKVpaB07H7PSYb5K-tMz6vy0cNrxZPHjHYjFSt-dl0Nl72HVi8wUfmj7SXCto8ISXJKLRLLToBjeRA_JK48Ow7omrQHwhQGbjK5EZ5Osc_vzf7BZveCX2ZK/s790-rw-e365/malware.png)

Cybercriminals are increasingly leveraging malicious LNK files as an initial access method to download and execute payloads such as Bumblebee, IcedID, and Qakbot.

A recent study by cybersecurity experts has shown that it is possible to identify relationships between different threat actors by analyzing the metadata of malicious LNK files, uncovering information such as the specific tools and techniques used by different groups of cybercriminals, as well as potential links between seemingly unrelated attacks.

"With the increasing usage of LNK files in attack chains, it's logical that threat actors have started developing and using tools to create such files," Cisco Talos researcher Guilherme Venere said in a [report](https://blog.talosintelligence.com/following-the-lnk-metadata-trail/) shared with The Hacker News.

This comprises tools like [NativeOne](https://research.checkpoint.com/2020/breaking-through-windows-defenses-analysing-mlnk-builder/)'s [mLNK Builder](https://resecurity.com/blog/article/shortcut-based-lnk-attacks-delivering-malicious-code-on-the-rise) and [Quantum Builder](https://thehackernews.com/2022/06/new-quantum-builder-lets-attackers.html), which allow subscribers to generate rogue shortcut files and evade security solutions.

Some of the major malware families that have used LNK files for initial access include Bumblebee, IcedID, and Qakbot, with Talos identifying connections between Bumblebee and IcedID as well as Bumblebee and Qakbot by examining the artifacts' metadata.

Specifically, multiple samples of LNK files leading to IcedID and Qakbot infections and those that were used in different Bumblebee campaigns have all been found to share the same Drive Serial Number.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

LNK files have also been employed by advanced persistent threat (APT) groups like Gamaredon (aka Armageddon) in its [attacks](https://cert.gov.ua/article/39086) aimed at [Ukrainian government entities](https://thehackernews.com/2022/09/russian-gamaredon-hackers-target.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFsFtGueW1zdjrLNQtzOzWjOO_CxRE_LeeBDYp5E_QEoxl2MGdGFuwWsGYYLtuosL_3moQIdAmrpv4SVG1-29qzD1RTyUqNd1jglk48DCH4D7vt5EmYABrTFtRUicLgivGOlwaj28nbLsf-wQtra5DtEaZLV_irtzjZjDpwrNUlrxvD5GSKUCplJcr/s790-rw-e365/lnk.png)

The noticeable spike in campaigns using malicious shortcuts is seen as a [reactive](https://thehackernews.com/2022/04/emotet-testing-new-delivery-ideas-after.html) [response](https://thehackernews.com/2022/07/hackers-opting-new-attack-methods-after.html) to Microsoft's decision to disable macros by default in Office documents downloaded from the Internet, prompting threat actors to embrace alternative attachment types and delivery mechanisms to distribute malware.

Recent analyses from Talos and Trustwave have disclosed how APT actors and commodity malware families alike are [weaponizing](https://thehackernews.com/2022/12/apt-hackers-turn-to-malicious-excel-add.html) Excel add-in (XLL) files, [OneNote attachments](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/trojanized-onenote-document-leads-to-formbook-malware/), and Publisher macros to drop remote access trojans on compromised machines.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

What's more, threat actors [have](https://thehackernews.com/2022/12/new-malvertising-campaign-via-google.html) [been](https://thehackernews.com/2023/01/the-evolving-tactics-of-vidar-stealer.html) [observed](https://thehackernews.com/2023/01/raccoon-and-vidar-stealers-spreading.html) taking advantage of rogue [Google Ads](https://support.google.com/adspolicy/answer/6020954) and search engine optimization (SEO) poisoning to push off-the-shelf malware like BATLOADER, IcedID, Rhadamanthys Stealer, and Vidar to victims searching for a slew of legitimate software.

BATLOADER, associated with an intrusion set tracked by Trend Micro as [Water Minyades](https://www.trendmicro.com/en_us/research/23/a/batloader-malware-abuses-legitimate-tools-uses-obfuscated-javasc.html), is an "evasive and evolutionary malware" that's capable of installing additional malware, including Cobalt Strike, Qakbot, Raccoon Stealer, RedLine Stealer, SmokeLoader, Vidar, and ZLoader.

"Attackers are imitating the websites of popular software projects to trick victims into infecting their computers and buying search engine adverts to drive traffic there," HP Wolf Security researcher Patrick Schläpfer [said](https://threatresearch.ext.hp.com/adverts-mimicking-popular-software-leads-to-malware/).

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
[![Facebook Messenger](data:image/png;base64...)Share on Fa...