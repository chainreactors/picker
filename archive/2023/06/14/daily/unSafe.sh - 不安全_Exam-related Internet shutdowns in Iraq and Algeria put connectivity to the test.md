---
title: Exam-related Internet shutdowns in Iraq and Algeria put connectivity to the test
url: https://buaq.net/go-168575.html
source: unSafe.sh - 不安全
date: 2023-06-14
fetch_date: 2025-10-04T11:44:49.669098
---

# Exam-related Internet shutdowns in Iraq and Algeria put connectivity to the test

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

![](https://8aqnet.cdn.bcebos.com/b2ee8efdc1f73d911a6e3ea943e8c095.jpg)

Exam-related Internet shutdowns in Iraq and Algeria put connectivity to the test

Loading...
*2023-6-13 21:18:16
Author: [blog.cloudflare.com(查看原文)](/jump-168575.htm)
阅读量:19
收藏*

---

Loading...

* [![David Belson](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/11/David-Belson.jpeg)](https://blog.cloudflare.com/author/david-belson/)

![](https://blog.cloudflare.com/content/images/2023/06/1937.png)

Over the last several years, governments in a number of countries in the Middle East/Northern Africa (MENA) region have taken to implementing widespread nationwide shutdowns in an effort to prevent cheating on nationwide academic exams. Although it is unclear whether such shutdowns are actually successful in curbing cheating, it is clear that they take a financial toll on the impacted countries, with [estimated losses](https://www.accessnow.org/mena-internet-shutdowns-during-exams/) in the millions of US dollars.

During the first two weeks of June 2023, we’ve seen Iraq implementing a series of multi-hour shutdowns that will reportedly occur through mid-July, as well as Algeria taking similar actions to prevent cheating on baccalaureate exams. Shutdowns in Syria were [reported](https://smex.org/syria-internet-shutdowns-planned-despite-promises-to-keep-it-on/) to begin on June 7, but there’s been no indication of them in traffic data as of this writing (June 13). These actions echo those taken in [Iraq, Syria, Sudan, and Algeria](https://blog.cloudflare.com/q2-2022-internet-disruption-summary/) in 2022 and in [Syria](https://blog.cloudflare.com/syria-exam-related-internet-shutdowns/) and [Sudan](https://blog.cloudflare.com/sudans-exam-related-internet-shutdowns/) in 2021.

*(Note: The interactive graphs below have been embedded directly into the blog post using a new [Cloudflare Radar feature](https://twitter.com/CloudflareRadar/status/1666078235384479745). This post is best viewed in landscape mode when on a mobile device.)*

### Iraq

Iraq had [reportedly committed](https://www.kurdistan24.net/en/story/31453-Iraq%E2%80%99s-communication-ministry-refuses-to-enforce-internet-blackout-for-final-exams) on May 15 to **not** implementing Internet shutdowns during the 2023 exam season, with a [now unavailable page](https://moc.gov.iq/?page=312) on the Iraqi Ministry of Communications web site (although [captured in the Internet Archive’s Wayback Machine](https://web.archive.org/web/20230515211944/https%3A//moc.gov.iq/?page=312)) noting (via Google Translate) “*Her Excellency the Minister of Communications, Dr. Hayam Al-Yasiri: We rejected a request to cut off the internet service during the ministerial exams.*” However, that commitment was apparently short-lived, as the first shutdown was implemented just a couple of weeks later, on June 1. The shutdowns observed across Iraq thus far have impacted networks and localities nationwide, with the exception of the autonomous Kurdistan region. However, networks in that region have experienced their own set of connectivity restrictions due to local exams.

In Iraq, the impact of the shutdowns between 04:00 - 08:00 local time (01:00 - 05:00 UTC) is clearly visible at a country level, as seen in the figure below.

The impact is, of course, also visible in the network-level graphs shown below, with traffic dropping to or near zero during each of the four-hour shutdown windows.

The shutdowns are also visible in the BGP announcement activity from the impacted networks, with spikes in announcement volume clearly visible around the shutdown windows each day that they have occurred. The announcement activity represents withdrawals ahead of the shutdown, removing routes to prefixes within the network, effectively cutting them off from the Internet, and updates after the shutdown period has ended, restoring the previously withdrawn routes, effectively reconnecting the prefixes to the Internet. (Additional announcement activity may also be visible for periods outside of the scheduled shutdowns, and is likely unrelated.)

While the shutdowns discussed above didn’t impact the Kurdistan region of Iraq, that region has also chosen to [implement their own shutdowns](https://www.basnews.com/en/babat/809911). In the Kurdistan region, exams started June 3, we saw shorter traffic disruptions across three local network providers on June 3, 6, 10, and 13. The disruptions lasted from 06:30 - 07:30 local time (03:30 to 04:30 UTC) on the 3rd, and 06:40 - 08:30 local time (03:30 to 05:30 UTC) on the 6th, 10th, and 13th). Impacted regions include Erbil, Sulaymaniyah, and Duhok.

BGP announcement activity for the impacted networks in the Kurdistan region did not show the same patterns as those observed on the other Iraqi network providers discussed above.

Both sets of shutdowns in Iraq are also visible in traffic to Cloudflare’s [1.1.1.1 DNS resolver](https://1.1.1.1/dns/), although they highlight a difference in usage between the autonomous Kurdistan region and the rest of the country. The “totalTcpUdp” graph (blue line) below shows requests made to the resolver over UDP or TCP on [port 53](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=2), the standard port used for DNS requests. The “totalDoHDoT” graph (orange line) below shows requests made to the resolver using [DNS-over-HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/) or [DNS-over-TLS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/) using port [443](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=8) or [853](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=15) respectively.

In the “totalTcpUdp” graph, we can see noticeable drops in traffic that align with the dates and times where we observed the traffic disruptions across Kurdistani networks. This drop in DNS traffic, combined with the lack of BGP announcement activity, suggests that the Internet disruptions in the Kurdistan region may be implemented as widespread blocking of Internet traffic, rather than routing-based shutdowns.

![](https://blog.cloudflare.com/content/images/2023/06/June-13---Iraq---1111---tcpudp.png)

In the “totalDoHDoT” graph below, we can see noticeable drops in traffic that align with the dates and times where we observed the traffic disruptions in the rest of Iraq.

![](https://blog.cloudflare.com/content/images/2023/06/June-13---Iraq---1111---dohdot.png)

It isn’t immediately clear why there is a difference in the use of 1.1.1.1 between the two parts of the country.

### Algeria

In Algeria, it appears that the country is following a [similar pattern as that seen in 2021 and 2022](https://blog.cloudflare.com/syria-sudan-algeria-exam-internet-shutdown/), with two multi-hour Internet disruptions each day. Also similar to last year, it appears that they are pursuing a content blocking-based approach, instead of the wide-scale Internet shutdowns implemented in 2021, as impacted networks are not experiencing complete outages, nor do they show patterns of BGP announcement activity.

A [published report](https://www.trtafrika.com/fr/africa/algerie-demarrage-des-epreuves-du-baccalaureat-lacces-a-internet-perturbe-13577416) indicates that two Internet disruptions will be implemented each day between June 11 and June 15. The first takes place between 08:00 - 12:00 local time (07:00 - 11:00 UTC), with the second occurring between 14:00 - 17:00 loc...