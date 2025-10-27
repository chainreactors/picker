---
title: Vice Society Ransomware Attackers Adopt Robust Encryption Methods
url: https://thehackernews.com/2022/12/vice-society-ransomware-attackers-adopt.html
source: The Hacker News
date: 2022-12-24
fetch_date: 2025-10-04T02:27:57.565089
---

# Vice Society Ransomware Attackers Adopt Robust Encryption Methods

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

# [Vice Society Ransomware Attackers Adopt Robust Encryption Methods](https://thehackernews.com/2022/12/vice-society-ransomware-attackers-adopt.html)

**Dec 23, 2022**Ravie LakshmananRansomware / Endpoint Security

[![Vice Society Ransomware](data:image/png;base64... "Vice Society Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9OFonreS_ZXcpHQ7Cmz3WassPXTBk2hISxhe5dcBm_ZHQSHE-KVNmerXGcVYCAQA2DjAmxKp8LqQLh29Vh_v-LFUMH6MbqKWgBGnKvmgs3Vh9u3nHvcZHZPk5xaL3A9MXtPvyKU6y1zA7SLI0hzrfGNbC899FWRGq0FC0E8Ao3dUY5SdyiqvwtTuRNw/s790-rw-e365/ransomware.png)

The Vice Society ransomware actors have switched to yet another custom ransomware payload in their recent attacks aimed at a variety of sectors.

"This ransomware variant, dubbed '**PolyVice**,' implements a robust encryption scheme, using [NTRUEncrypt](https://en.wikipedia.org/wiki/NTRUEncrypt) and [ChaCha20-Poly1305](https://en.wikipedia.org/wiki/ChaCha20-Poly1305) algorithms," SentinelOne researcher Antonio Cocomazzi [said](https://www.sentinelone.com/labs/custom-branded-ransomware-the-vice-society-group-and-the-threat-of-outsourced-development/) in an analysis.

[Vice Society](https://thehackernews.com/2022/12/vice-society-ransomware-attackers.html), which is tracked by Microsoft under the moniker DEV-0832, is an intrusion, exfiltration, and extortion hacking group that first appeared on the threat landscape in May 2021.

Unlike other ransomware gangs, the cybercrime actor does not use file-encrypting malware developed in-house. Instead, it's known to deploy third-party lockers such as Hello Kitty, Zeppelin, and RedAlert ransomware in their attacks.

Per SentinelOne, indications are that the threat actor behind the custom-branded ransomware is also selling similar payloads to other hacking crews based on PolyVice's extensive similarities to ransomware strains Chily and SunnyDay.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This implies a "Locker-as-a-Service" that's offered by an unknown threat actor in the form of a builder that allows its buyers to customize their payloads, including the encrypted file extension, ransom note file name, ransom note content, and the wallpaper text, among others.

The shift from Zeppelin is likely to have been spurred by the [discovery of weaknesses](https://blog.unit221b.com/dont-read-this-blog/0xdead-zeppelin) in its encryption algorithm that enabled researchers at cybersecurity company Unit221B to devise a decryptor in February 2020.

Besides implementing a hybrid encryption scheme that combines asymmetric and symmetric encryption to securely encrypt files, PolyVice also makes use of partial encryption and multi-threading to speed up the process.

It's worth pointing out that the recently discovered Royal ransomware [employs](https://thehackernews.com/2022/12/royal-ransomware-threat-takes-aim-at-us.html) similar tactics in a bid to evade anti-malware defenses, Cybereason disclosed last week.

[![Royal Ransomware](data:image/png;base64... "Royal Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEuJuV8DiBRl7vgRnfrMIFo5tQSTP4yMe-Z67ZiqvD5li-q8tSS76do6cYzJCx19SqenJNwc_sZqVvc7q4Ejq0256D7B4Rjb31hMri57I33AvdADj2uXHG3BpYpzge4QoH30rkVSpqwSy8dCaTMhv7KeLgeFl3f0z4mpy3aNjD9OrX6I_rRnBoMLdl/s790-rw-e365/trendmicro.png)

[Royal](https://www.trendmicro.com/en_us/research/22/l/conti-team-one-splinter-group-resurfaces-as-royal-ransomware-wit.html), which has its roots in the now-defunct [Conti ransomware](https://thehackernews.com/2022/08/conti-cybercrime-cartel-using-bazarcall.html) operation, has also been observed to utilize [call back phishing](https://thehackernews.com/2022/11/luna-moth-gang-invests-in-call-centers.html) (or telephone-oriented attack delivery) to trick victims into installing remote desktop software for initial access.

## Leaked Conti Source Code Fuels Emerging Ransomware Variants

[![Conti ransomware source code](data:image/png;base64... "Conti ransomware source code")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7LI0nYyiQaZQcEgoc7mpTAVWUiPzsg4kJvL3azWFfr5s3rcDCRzYuWgm_orpQ4bUHP43UtBpJZb7Je90Dp-AV3UwquAZCRRquSbjekg88sjBiJIqW0pHiIDP3dwZ0CQywsCq9ukRoW7-aV_zHHadI-Z0VObJo653HGdyTbSpaXm1txEchPTmCL2Jq/s790-rw-e365/conti-ransomware.png)

In the meanwhile, the leak of Conti source code earlier this year has spawned a number of new ransomware strains such as Putin Team, ScareCrow, [BlueSky](https://thehackernews.com/2022/08/hackers-behind-cuba-ransomware-attacks.html), and Meow, Cyble [disclosed](https://blog.cyble.com/2022/12/22/new-ransomware-strains-emerging-from-leaked-contis-source-code/), highlighting how such leaks are making it easier for threat actors to launch different offshoots with minimum investment.

"The ransomware ecosystem is constantly evolving, with the trend of hyperspecialization and outsourcing continuously growing," Cocomazzi said, adding it "presents a significant threat to organizations as it enables the proliferation of sophisticated ransomware attacks."

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

[Conti Ransomware](https://thehackernews.com/search/label/Conti%20Ransomware)[hacking news](https://thehackernews....