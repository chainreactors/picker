---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 52
url: https://buaq.net/go-141184.html
source: unSafe.sh - 不安全
date: 2022-12-24
fetch_date: 2025-10-04T02:24:43.367004
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 52

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/33a864b15f0eab476c909d177ebd5fb0.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 52

The GoodThis week, Microsoft joined Google and Meta (aka Facebook) in being the next tech giant to
*2022-12-23 22:0:16
Author: [www.sentinelone.com(查看原文)](/jump-141184.htm)
阅读量:18
收藏*

---

## The Good

This week, Microsoft joined Google and Meta (*aka* Facebook) in being the next tech giant to be slapped with a fine by French privacy watchdog [CNIL](https://www-cnil-fr.translate.goog/fr/cookies-sanction-de-60-millions-deuros-lencontre-de-microsoft-ireland-operations-limited?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp) for violation of Europe’s [GDPR](https://www.sentinelone.com/blog/gdpr-turns-two-has-anything-really-changed/) laws.

CNIL hit Google and Meta with $68 million and $170 million fines respectively earlier this year for failing to offer users of their products transparent ways to reject tracking cookies. On Thursday, Microsoft got a ticking off to the tune of around $64 million for cookies deposited by its web search engine bing.com.

![](https://www.sentinelone.com/wp-content/uploads/2022/12/data-privacy-scaled.jpg)

According to an investigation by CNIL, when a user visited bing.com, advertising cookies were placed on their device without user consent. The site also failed to offer a button allowing users to refuse the deposit of cookies as easily as to accept them.

In addition to the fine, CNIL ordered Microsoft to obtain consent for the use of cookies and trackers of any person residing in France within 3 months or face fines of $64,000 per day of delay.

[Data privacy laws](https://assets.sentinelone.com/gdpr/gdpr-datasheet-1#page=1) in the US and Europe have gathered strength over the last few years as the potential dangers of the mass collection of data pertaining to users’ online behavior have become more apparent. While such fines have limited financial impact on giants like Microsoft, Google and Meta, they are a reminder to companies everywhere that data privacy laws have teeth and users’ rights to privacy must be respected.

## The Bad

Extortion gang Vice Society, which made a name for itself attacking [healthcare](https://assets.sentinelone.com/leaders/sentinel-one-healthc) and [education](https://www.sentinelone.com/blog/cyber-risks-in-the-education-sector-why-cybersecurity-needs-to-be-top-of-the-class/) targets throughout 2021 and 2022 with off-the shelf ransomware like [HelloKitty](https://www.sentinelone.com/labs/hellokitty-ransomware-lacks-stealth-but-still-strikes-home/) and [Zeppelin](https://www.sentinelone.com/blog/endpoint-identity-and-cloud-top-cyber-attacks-of-2022-so-far/), has pivoted to a new custom-branded ransomware researchers have dubbed [PolyVice](https://www.sentinelone.com/labs/custom-branded-ransomware-the-vice-society-group-and-the-threat-of-outsourced-development/).

[SentinelLabs](https://www.sentinelone.com/labs/) revealed this week that the Vice Society group has been deploying payloads that are functionally identical to those of Chily and Sunnyday ransomware. According to their analysis, the payloads only differ in the section where the ransomware campaign details are stored, such as the encrypted file extension, ransom note, hardcoded master key, and wallpaper.

[![Code similarities between PolyVice and Chily Ransomware](https://www.sentinelone.com/wp-content/uploads/2022/12/PolyVice_1.jpg)

Code similarities between Vice Society and Chily Ransomware](https://www.sentinelone.com/labs/custom-branded-ransomware-the-vice-society-group-and-the-threat-of-outsourced-development/)[![Code similarities between PolyVice and SunnyDay Ransomware](https://www.sentinelone.com/wp-content/uploads/2022/12/PolyVice_13.jpg)

Code similarities between Vice Society and SunnyDay Ransomware](https://www.sentinelone.com/labs/custom-branded-ransomware-the-vice-society-group-and-the-threat-of-outsourced-development/)

[PolyVice ransomware](https://www.sentinelone.com/labs/custom-branded-ransomware-the-vice-society-group-and-the-threat-of-outsourced-development/) uses sophisticated encryption methods, including [partial encryption](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/) for large files, and a hybrid encryption scheme that combines asymmetric encryption with the NTRUEncrypt algorithm and symmetric encryption with the ChaCha20-Poly1305 algorithm.

As Vice Society has no known history of developing its own ransomware payloads, the level of sophistication along with the similarities to payloads used by other ransomware groups suggests that an individual or group with expertise in ransomware development is selling custom-branded ransomware payloads to multiple threat actors.

The ability of ransomware groups to outsource development and other services from the larger crimeware ecosystem means that new threat actor groups need little more than initial funding and some basic management capabilities to get new campaigns under way. Expect to see a proliferation of low-skilled crimeware operators picking off more schools, healthcare organizations, and others without adequate defences as we [move into 2023](https://www.sentinelone.com/blog/sentinelones-cybersecurity-predictions-2023-whats-next/).

## The Ugly

It’s been a tough year for password manager developer LastPass, as the fallout from a breach that began back in August continued to cause worries this week to the company and its customers.

The breach earlier in the year, LastPass initially [said](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/), had been limited to a small part of the LastPass development environment and the theft of some source code and proprietary LastPass technical information. A further breach in late November leveraged data stolen in August and saw “unusual activity within a third-party cloud storage service” that allowed an unknown actor to gain access to “elements of [LastPass] customers’ information”.

This week, the company updated its advisory revealing that the threat actor had made off with “basic customer account information and related metadata including company names, end-user names, billing addresses, email addresses, telephone numbers, and the IP addresses from which customers were accessing the LastPass service.”

The company was at pains to point out that LastPass customer vaults remain unaffected as LastPass does not hold copies of customers’ master passwords and vaults are encrypted with 256-bit encryption. However, LastPass users may be subject to [phishing attempts](https://www.sentinelone.com/blog/the-dangers-of-social-engineering-how-to-protect-your-organization/) and those who did not follow [recommendations](https://support.lastpass.com/help/what-is-the-lastpass-master-password-lp070014) for creating a strong password could be susceptible to [brute force attacks](https://www.sentinelone.com/blog/detecting-brute-force-password-attacks/).

Despite the serious nature of this breach, users everywhere are reminded that password managers are an essential part of [good password security](https://www.sentinelone.com/cybersecurity-101/password-security-business-tips/).

> Pour one out for all of the security practitioners who are going to have to patiently explain that using a password manager is still good, actually, to people who have glanced at a headline about the latest LastPass breach.
>
> — Eva (@evacide) [December 23, 2022](https://twitter.com/evacide/status/1606139362172813313?ref_src=twsrc%5Etfw)

文章来源: https://www.sentinelone.com/blog/the-good...