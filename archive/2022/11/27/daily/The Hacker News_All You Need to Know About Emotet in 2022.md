---
title: All You Need to Know About Emotet in 2022
url: https://thehackernews.com/2022/11/all-you-need-to-know-about-emotet-in.html
source: The Hacker News
date: 2022-11-27
fetch_date: 2025-10-03T23:53:43.693822
---

# All You Need to Know About Emotet in 2022

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

# [All You Need to Know About Emotet in 2022](https://thehackernews.com/2022/11/all-you-need-to-know-about-emotet-in.html)

**Nov 26, 2022**The Hacker News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEih_YN1J4cpKWYNmcM5MwH-NQ70aMumHbF0s-E1fXHWLjXjajfFldUA6cU7RQp1n4S5k_h3rDVx0ve9Pb35DHY3MuT7us7CGup996T5sPtZbj9CFVXDD05s4loemkg6GhiDhDZUUE_QUokTnJFeS1Ze0Tc-KfvCu2MZybHrtAJhmrMlwSuFIOOVIoEL/s790-rw-e365/emotet.png)

For 6 months, the infamous Emotet botnet has shown almost no activity, and now it's distributing malicious spam. Let's dive into details and discuss all you need to know about the notorious malware to combat it.

## Why is everyone scared of Emotet?

[Emotet](https://any.run/malware-trends/emotet?utm_source=hacker_news&utm_medium=article&utm_campaign=emotet1122&utm_content=mtt) is by far one of the most dangerous trojans ever created. The malware became a very destructive program as it grew in scale and sophistication. The victim can be anyone from corporate to private users exposed to spam email campaigns.

The botnet distributes through phishing containing malicious Excel or Word documents. When users open these documents and enable macros, the Emotet DLL downloads and then loads into memory.

It searches for email addresses and steals them for spam campaigns. Moreover, the botnet drops additional payloads, such as Cobalt Strike or other attacks that lead to ransomware.

The polymorphic nature of Emotet, along with the many modules it includes, makes the malware challenging to identify. The Emotet team constantly changes its tactics, techniques, and procedures to ensure that the existing detection rules cannot be applied. As part of its strategy to stay invisible in the infected system, the malicious software downloads extra payloads using multiple steps.

And the results of Emotet behavior are devastating for cybersecurity specialists: the malware is nearly impossible to remove. It spreads quickly, generates faulty indicators, and adapts according to attackers' needs.

## How has Emotet upgraded over the years?

Emotet is an advanced and constantly changing modular botnet. The malware started its journey as a simple banking trojan in 2014. But since then, it has acquired a bunch of different features, modules, and campaigns:

* 2014. Money transfer, mail spam, DDoS, and address book stealing modules.
* 2015. Evasion functionality.
* 2016. Mail spam, RIG 4.0 exploit kit, delivery of other trojans.
* 2017. A spreader and address book stealer module.
* 2021. XLS malicious templates, uses MSHTA, dropped by Cobalt Strike.
* 2022. Some features remained the same, but this year also brought several updates.

This tendency proves that Emotet isn't going anywhere despite frequent "vacations" and even the official shutdown. The malware evolves fast and adapts to everything.

## What features has a new Emotet 2022 version acquired?

After almost half a year of a break, the Emotet botnet returned even stronger. Here is what you need to know about a new 2022 version:

* It drops IcedID, a modular banking trojan.
* The malware loads XMRig, a miner that steals wallet data.
* The trojan has binary changes.
* Emotet bypasses detection using a 64-bit code base.
* A new version uses new commands:

Invoke rundll32.exe with a random named DLL and the export PluginInit

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxZHzhZtPOpAACgy7wzjUeh8eRIlMdYddvAfFv1pkXOr3i5y8TTgMX10LDV1RwdHTrUi83W6oKhjKLOVDbAQBO92xvkiwNUuFXt_Dpm7cWO1I6nIqkVxKQyheLyiQS2scTkCCN02FABT6jKFjeXYbmIOfc4Q0WDx2ppXKGaTU8PtM3gWujBfAwhUEC/s790-rw-e365/code.png)

* Emotet's goal is to get credentials from Google Chrome and other browsers.
* It's also targeted to make use of the SMB protocol to collect company data
* Like six months ago, the botnet uses XLS malicious lures, but it adopted a new one this time:

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivVhQ8gtQLGij62ec3Ejy8M9pMY5qGqh4qPuu-eY3SLyzZ0hi9ypQ_ZOFVimVRELpfSKDgu7goMMoUgznAuv_JhYoHGv9msly2SnqHUfzvnhVDp5IgVcs5AwSK6fGx7Z93u9r3IHXXxvFgosX6aI1q2XoTKnwgWchQnCThFwpmSRN13bZrq1zLVhce/s790-rw-e365/anyrun.png) |
| The Emotet's Excel lure |

## How to detect Emotet?

The main Emotet challenge is to detect it in the system quickly and accurately. Besides that, a malware analyst should understand the botnet's behavior to prevent future attacks and avoid possible losses.

With its long story of development, Emotet stepped up in the anti-evasion strategy. Through the evolution of the process execution chain and malware activity inside the infected system changes, the malware has modified detection techniques drastically.

For example, in 2018, it was possible to detect this banker by looking at the name of the process – it was one of these:

> eventswrap, implrandom, turnedavatar, soundser, archivesymbol, wabmetagen, msrasteps, secmsi, crsdcard, narrowpurchase, smxsel, watchvsgd, mfidlisvc, searchatsd, lpiograd, noticesman, appxmware, sansidaho

Later, in the first quarter of 2020, Emotet started to create specific key into the registry - it writes into the key HKEY\_CURRENT\_USER\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\EXPLORER value with the length 8 symbols (letters and characters).

Of course, Suricata rules always identify this malware, but detection systems often continue beyond the first wave because rules need to update.

Another way to detect this banker was its malicious documents - crooks use specific templates and lures, even with grammatical errors in them. One of the most reliable ways to detect Emotet is by the YARA rules.

To overcome malware's anti-evasion techniques and capture the botnet – use a malware sandbox as the most convenient tool for this goal. In [ANY.RUN](https://any.run/?utm_source=hacker_news&utm_medium=article&utm_campaign=emotet1122&utm_content=landing), you can not only detect, monitor, and analyze malicious objects but also get already extracted c...