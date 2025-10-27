---
title: Routing information now on Cloudflare Radar
url: https://buaq.net/go-173078.html
source: unSafe.sh - 不安全
date: 2023-07-28
fetch_date: 2025-10-04T11:52:36.115986
---

# Routing information now on Cloudflare Radar

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

![](https://8aqnet.cdn.bcebos.com/bd9b83a576a3e725ca4784a0f3f3e7a3.jpg)

Routing information now on Cloudflare Radar

Loading...
*2023-7-27 21:0:30
Author: [blog.cloudflare.com(查看原文)](/jump-173078.htm)
阅读量:21
收藏*

---

Loading...

* [![Mingwei Zhang](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/07/mingwei-selfie-square.jpeg)](https://blog.cloudflare.com/author/mingwei/)

![Routing information now on Cloudflare Radar](https://blog.cloudflare.com/content/images/2023/07/New-Routing-Page-in-Radar-1.png)

Routing is one of the most critical operations of the Internet. Routing decides how and where the Internet traffic should flow from the source to the destination, and can be categorized into two major types: intra-domain routing and inter-domain routing. Intra-domain routing handles making decisions on how individual packets should be routed among the servers and routers within an organization/network. When traffic reaches the edge of a network, the inter-domain routing kicks in to decide what the next hop is and forward the traffic along to the corresponding networks. [Border Gateway Protocol](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) (BGP) is the de facto inter-domain routing protocol used on the Internet.

Today, we are introducing another section on Cloudflare Radar: the [Routing](https://radar.cloudflare.com/routing/) page, which focuses on monitoring the BGP messages exchanged to extract and present insights on the IP prefixes, individual networks, countries, and the Internet overall. The new routing data allows users to quickly examine routing status of the Internet, examine secure routing protocol deployment for a country, identify routing anomalies, validate IP block reachability and much more from globally distributed vantage points.

It’s a detailed view of how the Internet itself holds together.

![](https://blog.cloudflare.com/content/images/2023/07/image6-4.png)

## Collecting routing statistics

The Internet consists of tens of thousands of interconnected organizations. Each organization manages its own internal networking infrastructure autonomously, and is referred to as an autonomous system (AS). ASes establish connectivity among each other and exchange routing information via BGP messages to form the current Internet.

When we open the Radar Routing page the “Routing Statistics” block provides a quick glance on the sizes and status of an autonomous system (AS), a country, or the Internet overall. The routing statistics component contains the following count information:

* The number of ASes on the Internet or registered from a given country;
* The number of distinct prefixes and the routes toward them observed on the global routing table, worldwide, by country, or by AS;
* The number of routes categorized by Resource Public Key Infrastructure (RPKI) validation results (valid, invalid, or unknown).

We also show the breakdown of these numbers for IPv4 and IPv6 separately, so users may have a better understanding of such information with respect to different IP protocols.

![](https://blog.cloudflare.com/content/images/2023/07/image5-3.png)

For a given network, we also show the BGP announcements volume chart for the past week as well as other basic information like network name, registration country, estimated user count, and sibling networks.

![](https://blog.cloudflare.com/content/images/2023/07/image7.png)

## Identifying routing anomalies

BGP as a routing protocol suffers from a number of [security weaknesses](https://blog.cloudflare.com/is-bgp-safe-yet-rpki-routing-security-initiative/). In the new Routing page we consolidate the [BGP route leaks](https://blog.cloudflare.com/route-leak-detection-with-cloudflare-radar/) and BGP hijacks detection results in one single place, showing the relevant detected events for any given network or globally.

![](https://blog.cloudflare.com/content/images/2023/07/image1-11.png)

The BGP Route Leaks table shows the [detected BGP route leak events](https://blog.cloudflare.com/route-leak-detection-with-cloudflare-radar/). Each entry in the table contains the information about the related ASes of the leak event, start and end time, as well as other numeric statistics that reflect the scale and impact of the event. The BGP Origin Hijacks table shows the detected potential [BGP origin hijacks](https://www.cloudflare.com/learning/security/glossary/bgp-hijacking). Apart from the relevant ASes, time, and impact information, we also show the key evidence that we collected for each event to provide additional context on why and how likely one event being a BGP hijack.

With this release, we introduce another anomaly detection: RPKI Invalid [Multiple Origin AS (MOAS)](https://www.cs.colostate.edu/~massey/pubs/conf/massey_imw01.pdf) is one type of routing conflict where multiple networks (ASes) originate the same IP prefixes at the same time, which goes against [the best practice recommendation](https://datatracker.ietf.org/doc/html/rfc1930#section-7). Our system examines the most recent global routing tables and identifies MOASes on the routing tables. With the help of [Resource Public Key Infrastructure (RPKI)](https://en.wikipedia.org/wiki/Resource_Public_Key_Infrastructure), we can further identify MOAS events that have origins that were proven RPKI invalid, which are less likely to be [legitimate cases](https://www.usenix.org/system/files/sec22-qin.pdf). Users and operators can quickly identify such anomalies relevant to the networks of interest and take actions accordingly.

![](https://blog.cloudflare.com/content/images/2023/07/image8.png)

The Routing page will be the permanent home for all things BGP and routing data in the future; we will gradually introduce more anomaly detections and improve our pipeline to provide more security insights.

## Examining routing assets and connectivity

Apart from examining the overall routing statistics and anomalies, we also gather information on the routing assets (IP prefixes for a network and networks for a country) and networks’ connectivity.

Tens of thousands autonomous systems (ASes) connect to each other to form the current Internet. The ASes differ in size and operate in different geolocations. Generally, larger networks are more well-connected and considered “upstream” and smaller networks are less connected and considered “downstream” on the Internet. Below is an example connectivity diagram showing how two smaller networks may connect to each other. AS1 announces its IP prefixes to its upstream providers and propagates upwards until it reaches the large networks AS3 and `AS4`, and then the route propagates downstream to smaller networks until it reaches AS6.

![](https://blog.cloudflare.com/content/images/2023/07/image4-5.png)

In the routing page, we examine what IP prefixes any given AS originates, as well as the interconnections among ASes. We show the full list of IP prefixes originated for any given AS, including the breakdown lists by RPKI validation status. We also show the detected connectivity among other ASes categorized into upstream, downstream and peering connections. Users can easily search for any ASes upstream, downstream, or peers.

![](https://blog.cloudflare.com/content/images/2023/07/image3-4.png)

For a given country, we show the full list of networks registered in the country, sorted by the number of IP prefixes originated from the corresponding networks. This allows users to quickly glance and find networks from any given country. The table is also searchable by network name or AS number.

![...