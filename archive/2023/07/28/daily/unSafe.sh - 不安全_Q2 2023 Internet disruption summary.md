---
title: Q2 2023 Internet disruption summary
url: https://buaq.net/go-173079.html
source: unSafe.sh - 不安全
date: 2023-07-28
fetch_date: 2025-10-04T11:52:37.364133
---

# Q2 2023 Internet disruption summary

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

![](https://8aqnet.cdn.bcebos.com/47c52db1371c34442dd375f5e20b7f84.jpg)

Q2 2023 Internet disruption summary

Loading...
*2023-7-27 21:0:2
Author: [blog.cloudflare.com(查看原文)](/jump-173079.htm)
阅读量:16
收藏*

---

Loading...

* [![David Belson](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/11/David-Belson.jpeg)](https://blog.cloudflare.com/author/david-belson/)

This post is also available in [Deutsch](https://blog.cloudflare.com/de-de/q2-2023-internet-disruption-summary-de-de/), [Français](https://blog.cloudflare.com/fr-fr/q2-2023-internet-disruption-summary-fr-fr/), [日本語](https://blog.cloudflare.com/ja-jp/q2-2023-internet-disruption-summary-ja-jp/).

![Q2 2023 Internet disruption summary](https://blog.cloudflare.com/content/images/2023/07/Global-Latency_new-colours-1.png)

Cloudflare operates in more than 300 cities in over 100 countries, where we interconnect with over 12,000 network providers in order to provide a broad range of services to millions of customers. The breadth of both our network and our customer base provides us with a unique perspective on Internet resilience, enabling us to observe the impact of Internet disruptions.

The second quarter of 2023 was a particularly busy one for Internet disruptions, and especially for government-directed Internet shutdowns. During the quarter, we observed many brief disruptions, but also quite a few long-lived ones. In addition to the [government-directed Internet shutdowns](#government-directed), we also observed partial or complete outages due to [severe weather](#severe-weather), [cable damage](#cable-damage), [power outages](#power-outages), general or unspecified [technical problems](#technical-problems), [cyberattacks](#cyberattacks), [military action](#military-action), and [infrastructure maintenance](#infrastructure-maintenance).

As we have noted in the past, this post is intended as a summary overview of observed disruptions, and is not an exhaustive or complete list of issues that have occurred during the quarter.

## Government directed

Late spring often marks the start of a so-called “exam season” in several Middle Eastern and African countries, where students sit for a series of secondary school exams. In an attempt to prevent cheating on these exams, governments in the countries have taken to implementing wide-scale Internet shutdowns covering time periods just before and during the exams. We have covered these shutdowns in the past, including [Sudan](https://blog.cloudflare.com/sudans-exam-related-internet-shutdowns/) and [Syria](https://blog.cloudflare.com/syria-exam-related-internet-shutdowns/) in 2021 and [Syria, Sudan, and Algeria](https://blog.cloudflare.com/syria-sudan-algeria-exam-internet-shutdown/) in 2022. This year, we saw governments in [Iraq, Algeria](https://blog.cloudflare.com/exam-internet-shutdowns-iraq-algeria/), and Syria taking such actions.

### Iraq

In the weeks prior to the start of this year’s shutdowns, it was [reported](https://www.kurdistan24.net/en/story/31453-Iraq%E2%80%99s-communication-ministry-refuses-to-enforce-internet-blackout-for-final-exams) that the Iraqi Ministry of Communications had announced it had refused a request from the Ministry of Education to impose an Internet shutdown during the exams as part of efforts to prevent cheating. Unfortunately, this refusal was short-lived, with shutdowns ultimately starting two weeks later.

In Iraq, two sets of shutdowns were observed: one impacted networks nationwide, except for the Kurdistan Region, while the other impacted networks within the Kurdistan Region. The former set of shutdowns were related to 9th and 12th grade exams, and were scheduled to occur from June 1 through July 15, between 04:00 and 08:00 local time (01:00 - 05:00 UTC). The graphs below show that during June, shutdowns took place on June 1, 4, 6, 8, 11, 13, 15, 17, 21, 22, 24, 25, and 26, resulting in significant disruptions to Internet connectivity. The shutdowns were implemented across a number of network providers, including [AS203214 (HulumTele](https://radar.cloudflare.com/as203214)), [AS59588 (Zain)](https://radar.cloudflare.com/as59588), [AS199739 (Earthlink)](https://radar.cloudflare.com/as199739), [AS203735 (Net Tech)](https://radar.cloudflare.com/as203735), [AS51684 (Asiacell)](https://radar.cloudflare.com/as51684), and [AS58322 (Halasat)](https://radar.cloudflare.com/as58322). The orange-highlighted areas in the graphs below show traffic on each network provider dropping to zero during the shutdowns.

As noted above, exam-related Internet shutdowns were also implemented in the Kurdistan region of Iraq. One [report](https://www.basnews.com/en/babat/809911) quoted the Minister of Education of the Kurdistan Regional Government as stating "*The Internet will be turned off as needed during exams, but just like in previous years, the period of the Internet shutdown will not be lengthy, but rather short.*” To that end, the observed shutdowns generally lasted about two hours, occurring between 06:30 and 08:30 local time (03:30 - 05:30 UTC) on June 3, 6, 10, 13, 17, and 24. The graphs below show the impact across three network providers in the region: [AS21277 (Newroz Telecom)](https://radar.cloudflare.com/as21277), [AS48492 (IQ Online)](https://radar.cloudflare.com/as48492), and [AS59625 (KorekTel)](https://radar.cloudflare.com/as59625).

Additional details about both sets of Internet shutdowns in Iraq can be found in our June 13 blog post: [*Exam-related Internet shutdowns in Iraq and Algeria put connectivity to the test*](https://blog.cloudflare.com/exam-internet-shutdowns-iraq-algeria/).

### Algeria

2023 marks the [sixth year](https://www.newarab.com/news/algeria-blocks-internet-stop-cheating-during-final-exams) that Algeria has disrupted Internet connectivity to prevent cheating during nationwide exams. In [2022](https://blog.cloudflare.com/syria-sudan-algeria-exam-internet-shutdown/), we noted that “*it appears that the Algerian government has shifted to a content blocking-based approach, instead of a wide-scale Internet shutdown.*” It appears that the same approach was taken this year, as we again observed two nominal drops in traffic during each of the exam days, rather than a complete loss of traffic. These traffic shifts were observed on mobile network providers [AS33779 (Ooredoo/Wataniya)](https://radar.cloudflare.com/as33779), [AS327931 (Djezzy/Optimum)](https://radar.cloudflare.com/as327931), and [AS327712 (Mobilis/Telecom Algeria)](https://radar.cloudflare.com/as327712). The first disruption takes place between 08:00 - 12:00 local time (07:00 - 11:00 UTC), with the second occurring between 14:00 - 17:00 local time (13:00 - 16:00 UTC).

### Syria

After implementing four exam-related Internet shutdowns in 2022, this year saw just two. On June 25 and 26, Internet shutdowns took place between 05:00 - 08:30 local time (02:00 - 05:30 UTC). [Syrian Telecom (AS29256)](https://radar.cloudflare.com/as29256), the government-affiliated telecommunications company, informed subscribers in a [Facebook post](https://www.facebook.com/syriantelecomcompany/posts/pfbid02vPpu2tTyEtxsaqupSF3MvqxrsMLTvJGpzYVvwzoQ3CFX3xuZJ23euJFkXxdZbtubl) that the Internet would be cut off at the request of the [Ministry of Education](http://www.syrianeducation.org.sy/).

### Senegal

In Senegal, [violent protests](https://www.reuters.com/world/africa/senegals-protest-hit-capital-left-with-looted-shops-debris-2023-06-03/) over the sentencing of opposition leader Ousmane Sonko to jail led the government to [restrict access to platforms](https:/...