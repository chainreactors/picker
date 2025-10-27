---
title: Cloudflare's global network grows to 300 cities and ever closer to end users with connections to 12,000 networks
url: https://buaq.net/go-169405.html
source: unSafe.sh - 不安全
date: 2023-06-20
fetch_date: 2025-10-04T11:47:06.074520
---

# Cloudflare's global network grows to 300 cities and ever closer to end users with connections to 12,000 networks

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

![](https://8aqnet.cdn.bcebos.com/0c373f3a554460ba4e55f24948370357.jpg)

Cloudflare's global network grows to 300 cities and ever closer to end users with connections to 12,000 networks

Loading...
*2023-6-19 21:0:16
Author: [blog.cloudflare.com(查看原文)](/jump-169405.htm)
阅读量:19
收藏*

---

Loading...

* [![Damian Matacz](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/03/PXL_20220909_052319947.PORTRAIT-3.jpg)](https://blog.cloudflare.com/author/damian/)
* [![Marcelo Affonso](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/04/026181C3-AFC0-469A-96B7-DF2BD202FA09.jpeg)](https://blog.cloudflare.com/author/marcelo/)
* [![Tom Paseka](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2017/03/1120d8a.jpg)](https://blog.cloudflare.com/author/tom-paseka/)
* [![Joanne Liew](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2020/12/Screenshot-2020-09-25-at-1.00.58-AM.png)](https://blog.cloudflare.com/author/joanne-liew/)

![Cloudflare's global network grows to 300 cities and ever closer to end users with connections to 12,000 networks](https://blog.cloudflare.com/content/images/2023/06/12-000-networks-1.png)

We make no secret about how passionate we are about building a world-class global [network](https://www.cloudflare.com/network/) to deliver the best possible experience for our customers. This means an unwavering and continual dedication to always improving the breadth (number of cities) and depth (number of interconnects) of our network.

**This is why we are pleased to announce that Cloudflare is now connected to over 12,000 Internet networks in over 300 cities around the world!**

The Cloudflare global network runs every service in every data center so your users have a consistent experience everywhere—whether you are in [Reykjavík](https://blog.cloudflare.com/reykjavik-cloudflares-northernmost-location/), [Guam](https://blog.cloudflare.com/cloudflare-deployment-in-guam/) or in the vicinity of any of the 300 cities where Cloudflare lives. This means all customer traffic is processed at the data center closest to its source, with no backhauling or performance tradeoffs.

Having Cloudflare’s network present in hundreds of cities globally is critical to providing new and more convenient ways to serve our customers and their customers. However, the breadth of our infrastructure network provides other critical purposes. Let’s take a closer look at the reasons we build and the real world impact we’ve seen to customer experience:

### Reduce latency

Our network allows us to sit approximately 50 ms from 95% of the Internet-connected population globally. Nevertheless, we are constantly reviewing network performance metrics and working with local regional Internet service providers to ensure we focus on growing underserved markets where we can add value and improve performance. So far, in 2023 we’ve already added 12 new cities to bring our network to over 300 cities spanning 122 unique countries!

| City |
| --- |
| Albuquerque, New Mexico, US |
| Austin, Texas, US |
| Bangor, Maine, US |
| Campos dos Goytacazes, Brazil |
| Fukuoka, Japan |
| Kingston, Jamaica |
| Kinshasa, Democratic Republic of the Congo |
| Lyon, France |
| Oran, Algeria |
| São José dos Campos, Brazil |
| Stuttgart, Germany |
| Vitoria, Brazil |

In May, we activated a new data center in Campos dos Goytacazes, Brazil, where we interconnected with a regional network provider, serving 100+ local ISPs. While it's not too far from Rio de Janeiro (270km) it still cut our 50th and 75th percentile latency measured from the TCP handshake between Cloudflare's servers and the user's device in half and provided a noticeable performance improvement!

![](https://blog.cloudflare.com/content/images/2023/06/image1-8.png)

### Improve interconnections

A larger number of local interconnections facilitates direct connections between network providers, content delivery networks, and regional Internet Service Providers. These interconnections enable faster and more efficient data exchange, content delivery, and collaboration between networks.

Currently there are approximately 74,0001 AS numbers routed globally. An [Autonomous System](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) (AS) number is a unique number allocated per ISP, enterprise, cloud, or similar network that maintains Internet routing capabilities using BGP. Of these approximate 74,000 ASNs, 43,0002 of them are stub ASNs, or only connected to one other network. These are often enterprise, or internal use ASNs, that only connect to their own ISP or internal network, but not with other networks.

It’s mind blowing to consider that Cloudflare is directly connected to 12,372 unique Internet networks, or approximately 1/3rd of the possible networks to connect globally! This direct connectivity builds resilience and enables performance, making sure there are multiple places to connect between networks, ISPs, and enterprises, but also making sure those connections are as fast as possible.

A previous example of this was shown as we started connecting more locally. As seen in this [blog post](https://blog.cloudflare.com/30-more-traffic-in-less-than-a-blink-of-an-ey/) the local connections even increased how much our network was being used: better performance drives further usage!

At Cloudflare we ensure that infrastructure expansion strategically aligns to building in markets where we can interconnect deeper, because increasing our network breadth is only as valuable as the number of local interconnections that it enables. For example, we recently connected to a local ISP (representing a new ASN connection) in Pakistan, where the 50th percentile improved from ~90ms to 5ms!

![](https://blog.cloudflare.com/content/images/2023/06/image2-7.png)

### Build resilience

Network expansion may be driven by reducing latency and improving interconnections, but it’s equally valuable to our existing network infrastructure. Increasing our geographic reach strengthens our redundancy, localizes failover and helps further distribute compute workload resulting in more effective capacity management. This improved resilience reduces the risk of service disruptions and ensures network availability even in the event of hardware failures, natural disasters, or other unforeseen circumstances. It enhances reliability and prevents single points of failure in the network architecture.

Ultimately, our commitment to strategically expanding the breadth and depth of our network delivers improved latency, stronger interconnections and a more resilient architecture - all critical components of a better Internet! If you’re a network operator, and are interested in how, together, we can deliver an improved user experience, we’re here to help! Please check out our [Edge Partner Program](https://www.cloudflare.com/partners/peering-portal/) and let’s get connected.

........

We protect
[entire corporate networks](https://www.cloudflare.com/network-services/),
help customers build
[Internet-scale applications efficiently](https://workers.cloudflare.com/),
accelerate any
[website
or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/),
[ward off DDoS
attacks](https://www.cloudflare.com/ddos/), keep
[hackers at
bay](https://www.cloudflare.com/application-security/),
and can help you on
[your journey to Zero Trust](https://www.cloudflare.com/products...