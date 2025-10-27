---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 48
url: https://buaq.net/go-137235.html
source: unSafe.sh - 不安全
date: 2022-11-26
fetch_date: 2025-10-03T23:47:19.939645
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 48

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

![](https://8aqnet.cdn.bcebos.com/be3153905b8ffb1748de4e4c2c239393.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 48

The GoodWe give thanks this week to the good people at Interpol along with fraud investigators fro
*2022-11-25 22:0:39
Author: [www.sentinelone.com(查看原文)](/jump-137235.htm)
阅读量:20
收藏*

---

## The Good

We give thanks this week to the good people at Interpol along with fraud investigators from 30 countries around the world for bringing us [HAECHI-III](https://www.interpol.int/News-and-Events/News/2022/Cyber-enabled-financial-crime-USD-130-million-intercepted-in-global-INTERPOL-police-operation) – a cybercrime busting operation that has resulted in almost 1000 arrests and seizure of approximately $130 million in virtual assets.

HAECHI-III is (as the name suggests) the third iteration of a coordinated law enforcement operation aimed at international cybercrime operations. Almost a year ago to date, we reported on [HAECHI-II](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-49-3/), which led to a similar number of arrests but only bagged around $27 million of illicit funds. The greater return this time round was a result of targeting voice phishing, romance scams, sextortion, investment fraud, and money laundering associated with illegal online gambling. The cops also leveraged financial experts to help them identify money mules and money laundering activities.

![romance scams, sextortion, investment fraud](https://www.sentinelone.com/wp-content/uploads/2022/11/HAECHI-III.jpeg)

Among the 1600 or so cases closed thanks to the operation was one that involved call center scammers in Austria and India impersonating Interpol officers and duping victims out of over $150,000. Victims of a [business email correspondence](https://www.sentinelone.com/cybersecurity-101/business-email-compromise-bec/) (BEC) scam in Ireland were also thankful for the return of €1.2 million as one of HAECHI-III’s many successes.

Aside from the arrests and asset seizures, authorities also seized or blocked 2800 bank and virtual-asset accounts linked to financial crimes during the 5-month operation, which ran from June to November 2022.

## The Bad

This week’s bad news concerns users of Amazon, Paypal, Steam and Roblox in 111 countries who are being targeted with info-stealers by Russian-speaking cybercrime gangs.

A new [report](https://www.group-ib.com/media-center/press-releases/professional-stealers/) claims that almost 900,000 devices were infected and over 50 million account passwords stolen by the gangs in the first seven months of 2022. Mainly using info-stealers like [Raccoon](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-44-4/) and Redline, the gangs use [Telegram groups](https://www.sentinelone.com/blog/top-10-telegram-cybersecurity-groups-you-should-join/) as a means to coordinate their criminal activities, including generating malicious content and aiding communication between members.

![infostealer malware](https://www.sentinelone.com/wp-content/uploads/2022/11/infostealer-theft-scaled.jpg)

Info-stealers target caches in browsers like Chrome, Firefox and Edge to steal saved account passwords, bank card details and crypto wallet information from infected machines. The stolen data is then sold on [darknet markets](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/) or used directly by the cybercriminals themselves for [account takeover](https://www.sentinelone.com/blog/anatomy-of-automated-account-takeovers/) or online fraud.

According to the researchers, the first seven months of 2022 saw around $6 million worth of data and bank card details stolen by 34 active Telegram groups. The Russian-speaking cybercriminals’ top targets were users in the United States, Brazil, India, and Germany. The most frequently stolen data was PayPal account credentials and Amazon account credentials. However, a five-fold increase in the theft of passwords for gaming services provided by Steam, Roblox and EpicGames was also reported.

Info-stealers typically require some social engineering of the victim – often in the form of downloading and running suspicious software including fake AV software, fake video player or other “software updates”, and free or cracked apps. A recent info-stealer campaign delivering RedLine used a fake version of popular GPU utility [MSI Afterburner](https://www.bleepingcomputer.com/news/security/fake-msi-afterburner-targets-windows-gamers-with-miners-info-stealers/) to infect victims.

Aside from being cautious and avoiding downloading software from unknown sources, users are advised to use password managers rather than storing credentials in browsers and to regularly clear browser cookies.

## The Ugly

While we’re on the subject of info-stealers, users of Facebook business accounts have been the targets of a cybercrime campaign conducted through social media site LinkedIn and messaging software WhatsApp, it was [reported](https://www.bleepingcomputer.com/news/security/ducktail-hackers-now-use-whatsapp-to-phish-for-facebook-ad-accounts/) this week.

A Vietnamese-linked operation dubbed ‘Ducktail’ is believed to be responsible for luring Facebook business account owners into downloading and launching malware capable of stealing credentials and allowing the attackers to hijack their accounts. Facebook business accounts have high privileges and access to the Business Manager panel can give an attacker control over settings, permissions and financial details, including credit card numbers.

![facebook phishing](https://www.sentinelone.com/wp-content/uploads/2022/11/facebook-phishing.jpg)

The report says that the threat actors behind Ducktail used these compromised accounts to run their own Facebook ad campaigns at the victim’s expense. It is thought that so far the operation has caused around $600,000 worth of losses to businesses.

Initially reported in June of this year, the info-stealing malware used in the operation was delivered to victims via lures on LinkedIn related to brands and products relevant to the victim. In the latest activity reported this week, victims have reportedly also been targeted through WhatsApp and Telegram.

Once the target accepts and launches the Ducktail malware, it steals stored session cookies and interacts with a number of Facebook API endpoints to collect access tokens, [2FA codes](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/), IP addresses and geolocation data that allows the threat actors to impersonate the victim and log in from their own devices. Independent research from [Zscaler](https://www.zscaler.com/blogs/security-research/new-php-variant-ducktail-infostealer-targeting-facebook-business-accounts) also identified a [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) campaign last month aimed at the same targets.

Facebook account managers are encouraged to review the roles and permissions associated with their accounts and to follow the recommendations [here](https://www.facebook.com/business/news/tips-to-keep-your-facebook-account-and-business-page-secure).

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-48-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)