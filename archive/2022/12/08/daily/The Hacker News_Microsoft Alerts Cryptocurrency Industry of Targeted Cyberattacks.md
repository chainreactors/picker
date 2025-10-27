---
title: Microsoft Alerts Cryptocurrency Industry of Targeted Cyberattacks
url: https://thehackernews.com/2022/12/microsoft-alerts-cryptocurrency.html
source: The Hacker News
date: 2022-12-08
fetch_date: 2025-10-04T00:55:47.358946
---

# Microsoft Alerts Cryptocurrency Industry of Targeted Cyberattacks

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

# [Microsoft Alerts Cryptocurrency Industry of Targeted Cyberattacks](https://thehackernews.com/2022/12/microsoft-alerts-cryptocurrency.html)

**Dec 07, 2022**Ravie LakshmananCryptocurrency / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIaD6H0r0xhslaRDWEHaAi2oulIDYrssMbY4RJbASKhfME-s-1PsBj2hgdAA1Bs609EsJrryx7ldon0fcfeC9rOeIioHcOdt197kwrjxMst-hAEnUKMySoDx_sqkjoF4jlPZxaIOalf2OSAEiW9MAYbQDgN-NXfrTFEHhjcY3f8dPGCoA3i8_bD9Hn/s790-rw-e365/ms.png)

Cryptocurrency investment companies are the target of a developing threat cluster that uses Telegram groups to seek out potential victims.

Microsoft's Security Threat Intelligence Center (MSTIC) is tracking the activity under the name **DEV-0139**, and builds upon a recent report from Volexity that attributed the same set of attacks to North Korea's [Lazarus Group](https://thehackernews.com/2022/12/north-korean-hackers-spread-applejeus.html).

"DEV-0139 joined Telegram groups used to facilitate communication between VIP clients and cryptocurrency exchange platforms and identified their target from among the members," the tech giant [said](https://www.microsoft.com/en-us/security/blog/2022/12/06/dev-0139-launches-targeted-attacks-against-the-cryptocurrency-industry/).

The adversary subsequently impersonated another cryptocurrency investment company and invited the victim to join a different Telegram chat group under the pretext of asking for feedback on the trading fee structure used by exchange platforms across VIP tiers.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth pointing out that the [VIP program](https://www.binance.com/en-us/fee/schedule) is [designed](https://learn.bybit.com/trading/crypto-trading-fees-comparison/) to [reward](https://help.crypto.com/en/articles/4756522-what-is-the-exchange-vip-program) [high-volume traders](https://www.kraken.com/features/fee-schedule) with exclusive trading fee incentives and discounts based on their crypto activity in the past 30 days.

This attack chain notably dovetails with Volexity's analysis of an October 2022 campaign, wherein the threat actor pivoted from using MSI installer files to a weaponized [Microsoft Excel document](https://www.virustotal.com/gui/file/abca3253c003af67113f83df2242a7078d5224870b619489015e4fde060acad0) displaying the supposed cryptocurrency coin rates.

Microsoft described the document as containing likely accurate data to increase the chances of success of the campaign, suggesting that DEV-0139 is well versed with the inner workings of the cryptocurrency sector.

The malware-laced Excel file, for its part, is tasked with executing a malicious macro that's used to stealthily drop and execute a second Excel worksheet, which, in turn, includes a macro that downloads a PNG image file hosted on OpenDrive.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDiRTSW0YYE3LSvL1h3Def0q-Ee7ECYiUdTaTd3MKNFbMfZZaXbKxg9GM2uqbsG8gay-JGw7WV1dwrIQj2Y_lXehBn3uaHXVhsx86uQVcy9ORK8G37PBR33c-_mfQx75iLH-5rlirq63NwqLYG0BwEsoD6xHRaQD8oVlUjbLleMS7W0IdPHaUvjTrn/s790-rw-e365/hack.png)

This image file contains three executables, each of which is used to launch the next-stage payload, ultimately paving the way for a backdoor that lets the threat actor remotely access the infected system.

Furthermore, the fee structure spreadsheet is password-protected in a bid to convince the target into enabling macros, thereby initiating the malicious actions. A metadata analysis of the file shows that it was created on October 14, 2022 by a user named Wolf.

DEV-0139 has also been linked to an alternative attack sequence in which an MSI package for a fake application named "CryptoDashboardV2" is delivered in place of a malicious Excel document to deploy the same implant.

The backdoor mainly enables remote access to the host by gathering information from the targeted system and connecting to a command-and-control (C2) server to receive additional commands.

"The cryptocurrency market remains a field of interest for threat actors," Microsoft said. "Targeted users are identified through trusted channels to increase the chance of success."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In recent years, Telegram has not only witnessed [widespread adoption](https://techcrunch.com/2022/08/10/as-telegram-grows-in-size-so-does-crypto-traders-dependence-on-the-app/) in the cryptocurrency industry, but also been co-opted by threat actors looking to discuss zero-day vulnerabilities, offer stolen data, and market their services through the popular messaging platform.

"With users losing confidence in the anonymity offered by forums, illicit marketplaces are increasingly turning to Telegram," Positive Technologies [disclosed](https://www.ptsecurity.com/ww-en/analytics/cybercriminal-market-in-telegram/) in a new study of 323 public Telegram channels and groups with over one million subscribers in total.

"The number of unique cyberattacks is constantly growing, and the market for cybercriminal services is expanding and moving into ordinary social media and messaging apps, thereby significantly lowering the entry threshold for cybercriminals."

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
[![Face...