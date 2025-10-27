---
title: Anubis Ransomware Encrypts and Wipes Files, Making Recovery Impossible Even After Payment
url: https://thehackernews.com/2025/06/anubis-ransomware-encrypts-and-wipes.html
source: The Hacker News
date: 2025-06-17
fetch_date: 2025-10-06T22:57:04.803465
---

# Anubis Ransomware Encrypts and Wipes Files, Making Recovery Impossible Even After Payment

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

# [Anubis Ransomware Encrypts and Wipes Files, Making Recovery Impossible Even After Payment](https://thehackernews.com/2025/06/anubis-ransomware-encrypts-and-wipes.html)

**Jun 16, 2025**Ravie LakshmananMalware / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCx5P2gekfKc6pd0Szl1UGY9QwGT9N17qEjQuI4tzc2z11VLIeYeUTJBisXgLDD7WWoAk57tCowGmeL0SpElxkU3eFTnXwbuWq63TVF_Jy4h9S2Ef1jN-BIl4JANxg1Le5XQ78alOcvhKEwBCl39785PgHPPCMqCg6XqZCrm55yVL0_0VPF5PGGr8XgLVr/s790-rw-e365/anubis.jpg)

An emerging ransomware strain has been discovered incorporating capabilities to encrypt files as well as permanently erase them, a development that has been described as a "rare dual-threat."

"The ransomware features a 'wipe mode,' which permanently erases files, rendering recovery impossible even if the ransom is paid," Trend Micro researchers Maristel Policarpio, Sarah Pearl Camiling, and Sophia Nilette Robles [said](https://www.trendmicro.com/en_us/research/25/f/anubis-a-closer-look-at-an-emerging-ransomware.html) in a report published last week.

The ransomware-as-a-service (RaaS) operation in question is named Anubis, which [became active](https://www.kelacyber.com/blog/anubis-a-new-ransomware-threat/) in December 2024, claiming victims across [healthcare, hospitality, and construction sectors](https://www.halcyon.ai/attacks?group=Anubis) in Australia, Canada, Peru, and the U.S. Analysis of early, trial samples of the ransomware suggests that the developers initially named it Sphinx, before tweaking the brand name in the final version.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth noting that the e-crime crew has no ties to an [Android banking trojan](https://thehackernews.com/2019/01/android-malware-play-store.html) and a [Python-based backdoor](https://thehackernews.com/2025/04/fin7-deploys-anubis-backdoor-to-hijack.html) of the same name, the latter of which is attributed to the financially-motivated FIN7 (aka GrayAlpha) group.

"Anubis runs a flexible affiliate program, offering negotiable revenue splits and supporting additional monetization paths like data extortion and access sales," the cybersecurity company said.

The affiliate program follows an 80-20 split, allowing affiliate actors to take 80% of the ransom paid. On the other hand, data extortion and access monetization schemes offer a 60-40 and 50-50 split, respectively.

Attack chains mounted by Anubis involve the use of phishing emails as the initial access vector, with the threat actors leveraging the foothold to escalate privileges, conduct reconnaissance, and take steps to delete volume shadow copies, before encrypting files and, if necessary, wipe their contents.

This means that the file sizes are reduced to 0 KB while leaving the file names or their extensions untouched, making recovery impossible and, therefore, exerting more pressure on victims to pay up.

"The ransomware includes a wiper feature using /WIPEMODE parameter, which can permanently delete the contents of a file, preventing any recovery attempt," the researchers said.

"Its ability to both encrypt and permanently destroy data significantly raises the stakes for victims, amplifying the pressure to comply -- just as strong ransomware operations aim to do."

The discovery of Anubis' destructive behavior comes as Recorded Future detailed new infrastructure associated with the FIN7 group that's being used to impersonate legitimate software products and services as part of a campaign designed to [deliver NetSupport RAT](https://thehackernews.com/2024/05/fin7-hacker-group-leverages-malicious.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Mastercard-owned threat intelligence firm said it identified three unique distribution vectors over the past year that have employed bogus browser update pages, fake 7-Zip download sites, and [TAG-124](https://thehackernews.com/2025/02/crazy-evil-gang-targets-crypto-with.html) (aka 404 TDS, Chaya\_002, Kongtuke, and LandUpdate808) to deliver the malware.

While the fake browser update method loads a custom loader dubbed MaskBat to execute the remote access trojan, the remaining two infection vectors employ another custom PowerShell loader dubbed PowerNet that decompresses and executes it.

"[MaskBat] has similarities to [FakeBat](https://thehackernews.com/2024/07/fakebat-loader-malware-spreads-widely.html) but is obfuscated and contains strings linked to GrayAlpha," Recorded Future's Insikt Group [said](https://www.recordedfuture.com/research/grayalpha-uses-diverse-infection-vectors-deploy-powernet-loader-netsupport-rat). "Although all three infection vectors were observed being used simultaneously, only the fake 7-Zip download pages were still active at the time of writing, with newly registered domains appearing as recently as April 2025."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Wiping](https://thehackernews.com/search/label/Data%20Wiping)[FIN7](https://thehackernews.com/search/label/FIN7)[healthcare](https://thehackernews.com/search/label...