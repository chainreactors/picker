---
title: Who tracked internet users in 2021–2022
url: https://buaq.net/go-137176.html
source: unSafe.sh - 不安全
date: 2022-11-26
fetch_date: 2025-10-03T23:47:27.947493
---

# Who tracked internet users in 2021–2022

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

![]()

Who tracked internet users in 2021–2022

Every time you go online, someone is watching over you. The services you use, the webs
*2022-11-25 16:0:7
Author: [securelist.com(查看原文)](/jump-137176.htm)
阅读量:25
收藏*

---

Every time you go online, someone is watching over you. The services you use, the websites you visit, the apps on your phone, smart TVs, gaming consoles, and any networked devices collect data on you with the help of trackers installed on web pages or in software. The websites and services send this data to their manufacturers and partners whose trackers they use. Companies are looking for all kinds of information on you: from device specifications to the way you are using a service, and the pages you are opening. Data thus collected primarily helps companies, firstly, to understand their customers better and improve the products by analyzing the user experience, and, secondly, to predict user needs and possibly even manipulate them. Besides, the more an organization knows about you, the better it can personalize ads that it shows you. These ads command higher rates than random ones and therefore generate higher profits.

Understanding who is collecting the data and why requires you to have free time and to know where to look. Most services have published privacy policies, which should ideally explain in detail what data the service collects and why. Sadly, these policies are seldom transparent enough. Worried about this lack of transparency, users and privacy watchdogs put pressure on technology companies. Certain tech giants recently started adding tools to their ecosystems that are meant to improve the data collection transparency. For example, upon the first run of an app downloaded from the App Store, Apple inquires if the user is willing to allow that app to track their activity. However, not every service provides this kind of warnings. You will not see a prompt like that when visiting a website, even if you are doing it on an Apple device.

Browser privacy settings and special extensions that recognize tracking requests from websites and block these can protect you from tracking as you surf the web. That is how our Do Not Track (DNT) extension works. Furthermore, with the user’s consent, DNT collects anonymized data on what tracking requests are being blocked and how frequently. This report will look at companies that collect, analyze, store user data, and share it with partners, as reported by DNT.

## Statistics collection principles

This report uses anonymous statistics collected between August 2021 and August 2022 by the Do Not Track component, which blocks loading of web trackers. The statistics consist of anonymized data provided by users voluntarily. We have compiled a list of 25 tracking services that DNT detected most frequently across nine regions and certain individual countries. 100% in each case represents the total number of DNT detections triggered by all 25 tracking services.

DNT (disabled by default) is part of Kaspersky Internet Security, Kaspersky Total Security, and Kaspersky Security Cloud.

## Global web tracking giants

Six tracking services made the TOP 25 rankings in each of the regions at hand. Four of them are owned by Google: Google Analytics, Google AdSense, Google Marketing Platform, and YouTube Analytics. The remaining two are owned by Meta and Criteo, which we will cover later.

### Google

Our last report, published in 2019, took a [close look](https://securelist.com/data-collectors/94339/#google) at Google’s trackers: DoubleClick, Google AdSense, Google Analytics, and YouTube Analytics. This was right around the time when the search giant announced plans to rebrand the DoubleClick advertising platform and merge it with its advertising ecosystem. Today, DoubleClick is part of [Google Marketing Platform](https://en.wikipedia.org/wiki/Google_Marketing_Platform), although the tracking URLs have not changed and continue to function as before. For convenience, our statistics will refer to that tracking service as “Google Marketing Platform (ex-DoubleClick)”.

***Share of DNT detections triggered by Google Marketing Platform (ex-DoubleClick) trackers in each region, August 2021 — August 2022 ([download](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/11/24141754/01-en-tracker-report.png))***

Google Marketing Platform (ex-DoubleClick) had its largest shares in our TOP 25 rankings for South Asia (32.92%) and the Middle East (32.84%). These were followed by its shares in Africa and Latin America: 25.37% and 24.64%, respectively. The lowest share (just 7.05%) of Google Marketing Platform (ex-DoubleClick) DNT detections in our regional TOP 25 rankings of the busiest tracking services were observed in the CIS.

A further tracking service operated by Google, Google Analytics, collects data on website visitors and provides detailed statistics to clients. That service, too, accounts for a fairly large share of DNT detections across the world.

**Share of DNT detections triggered by Google Analytics trackers in each region, August 2021 — August 2022 ([download](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/11/24141823/02-en-tracker-report.png))**

A look at the share of Google Analytics in various regions will reveal a similar pattern to the Google Marketing Platform (ex-DoubleClick). Google Analytics received its largest shares of detections in South Asia (18.04%), Latin America (17.97%), Africa (16.56%) and the Middle East (16.44%). Its smallest share was in the CIS: 9.06%.

**Share of DNT detections triggered by Google AdSense trackers in each region, August 2021 — August 2022 ([download](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/11/24141855/03-en-tracker-report.png))**

Another tracking system operated by Google is Google AdSense context ad service. This, again, had its highest percentages in the Middle East (5.27%), Africa (4.63%), Latin America (4.44%), and South Asia (4.44%). Here, too, the CIS ranked last with just 1.45% of detections triggered by the service.

Rounding out the list of Google’s tracking services is YouTube Analytics. It provides YouTube bloggers with data on their audiences that its trackers collect and analyze.

**Share of DNT detections triggered by YouTube Analytics trackers in each region, August 2021 — August 2022 ([download](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/11/24141930/04-en-tracker-report.png))**

The Middle East (8.04%), South Asia (7.79%), Africa (5.97%), and Latin America (5.02%) again accounted for the highest shares of detections. At the bottom of the region list this time around is North America (1.82%), rather than the CIS (2.54%). The low percentage is no indication of YouTube’s insignificant presence in the region. The small share of YouTube Analytics in the region was likely due to fierce competition among services that collect and analyze data. We will revisit this later.

### Meta (Facebook)

Facebook Custom Audiences by Meta, which provides targeted advertising services, was present in each of the regions along with Google’s tracking services. Services like that collect various types of user data, analyze these, and segment the audience to ensure better ad targeting. An advertiser who uses a targeting service wins by having their products shown to the people who are the likeliest to be interested. Compared to smaller advertising providers, Facebook Custom Audiences covers a significantly larger audience. Our data shows, however, that Meta was second to Google in terms of presence in all regions of the w...