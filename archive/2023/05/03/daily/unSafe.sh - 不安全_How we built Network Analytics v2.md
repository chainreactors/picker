---
title: How we built Network Analytics v2
url: https://buaq.net/go-161391.html
source: unSafe.sh - 不安全
date: 2023-05-03
fetch_date: 2025-10-04T11:38:44.531934
---

# How we built Network Analytics v2

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

![](https://8aqnet.cdn.bcebos.com/f38e06628f84cd9792e7a96ccabd5283.jpg)

How we built Network Analytics v2

Loading...
*2023-5-2 21:0:52
Author: [blog.cloudflare.com(查看原文)](/jump-161391.htm)
阅读量:32
收藏*

---

Loading...

* [![Alex Forster](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/10/me-even-smaller-crushed.png)](https://blog.cloudflare.com/author/alex-forster/)
* [![Clément Joly](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/cl_joly.jpeg)](https://blog.cloudflare.com/author/clement-joly/)

![How we built Network Analytics v2](https://blog.cloudflare.com/content/images/2023/05/image1-4.png)

Network Analytics v2 is a fundamental redesign of the backend systems that provide real-time visibility into network layer traffic patterns for Magic Transit and Spectrum customers. In this blog post, we'll dive into the technical details behind this redesign and discuss some of the more interesting aspects of the new system.

To protect Cloudflare and our customers against [Distributed Denial of Service (DDoS) attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/?ref=blog.cloudflare.com), we operate a sophisticated in-house DDoS detection and mitigation system called dosd. It takes samples of incoming packets, analyzes them for attacks, and then deploys mitigation rules to our global network which drop any packets matching specific attack fingerprints. For example, a simple network layer mitigation rule might say “drop UDP/53 packets containing responses to DNS ANY queries”.

In order to give our Magic Transit and Spectrum customers insight into the mitigation rules that we apply to their traffic, we introduced a new reporting system called "Network Analytics" back in 2020. Network Analytics is a data pipeline that analyzes raw packet samples from the Cloudflare global network. At a high level, the analysis process involves trying to match each packet sample against the list of mitigation rules that dosd has deployed, so that it can infer whether any particular packet sample was dropped due to a mitigation rule. Aggregated time-series data about these packet samples is then rolled up into one-minute buckets and inserted into a ClickHouse database for long-term storage. The Cloudflare dashboard queries this data using our public GraphQL APIs, and displays the data to customers using interactive visualizations.

## What was wrong with v1?

This original implementation of Network Analytics delivered a ton of value to customers and has served us well. However, in the years since it was launched, we have continued to significantly improve our mitigation capabilities by adding entirely new mitigation systems like [Advanced TCP Protection](https://developers.cloudflare.com/ddos-protection/tcp-protection/?ref=blog.cloudflare.com) (otherwise known as flowtrackd) and [Magic Firewall](https://blog.cloudflare.com/introducing-magic-firewall/). The original version of Network Analytics only reports on mitigations created by dosd, which meant we had a reporting system that was showing incomplete information.

Adapting the original version of Network Analytics to work with Magic Firewall would have been relatively straightforward. Since firewall rules are “stateless”, we can tell whether a firewall rule matches a packet sample just by looking at the packet itself. That’s the same thing we were already doing to figure out whether packets match dosd mitigation rules.

However, despite our efforts, adapting Network Analytics to work with flowtrackd turned out to be an insurmountable problem. flowtrackd is “stateful”, meaning it determines whether a packet is part of a legitimate connection by tracking information about the other packets it has seen previously. The original Network Analytics design is incompatible with stateful systems like this, since that design made an assumption that the fate of a packet can be determined simply by looking at the bytes inside it.

## Rethinking our approach

[Rewriting](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/?ref=blog.cloudflare.com) a working system is not usually a good idea, but in this case it was necessary since the fundamental assumptions made by the old design were no longer true. When starting over with Network Analytics v2, it was clear to us that the new design not only needed to fix the deficiencies of the old design, it also had to be flexible enough to grow to support future products that we haven’t even thought of yet. To meet this high bar, we needed to really understand the core principles of network observability.

In the world of on-premise networks, packets typically chain through a series of appliances that each serve their own special purposes. For example, a packet may first pass through a [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/?ref=blog.cloudflare.com), then through a [router](https://www.cloudflare.com/learning/network-layer/what-is-a-router/?ref=blog.cloudflare.com), and then through a [load balancer](https://www.cloudflare.com/learning/performance/what-is-load-balancing/?ref=blog.cloudflare.com), before finally reaching the intended destination. The links in this chain can be thought of as independent “network functions”, each with some well-defined inputs and outputs.

![](https://blog.cloudflare.com/content/images/2023/05/download-3.png)

A key insight for us was that, if you squint a little, Cloudflare’s software architecture looks very similar to this. Each server receives packets and chains them through a series of independent and specialized software components that handle things like [DDoS mitigation](https://www.cloudflare.com/learning/ddos/ddos-mitigation/?ref=blog.cloudflare.com), firewalling, reverse proxying, etc.

![](https://blog.cloudflare.com/content/images/2023/05/download--1--1.png)

After noticing this similarity, we decided to explore how people with traditional networks monitor them. Universally, the answer is either Netflow or sFlow.

![](https://blog.cloudflare.com/content/images/2023/05/download--2--1.png)

Nearly all on-premise hardware appliances can be configured to send a stream of Netflow or sFlow samples to a centralized flow collector. Traditional network operators tend to take these samples at many different points in the network, in order to monitor each device independently. This was different from our approach, which was to take packet samples only once, as soon as they entered the network and before performing any processing on them.

Another interesting thing we noticed was that Netflow and sFlow samples contain more than just information about packet contents. They also contain lots of metadata, such as the interface that packets entered and exited on, whether they were passed or dropped, which firewall or ACL rule they hit, and more. The metadata format is also extensible, so that devices can include information in their samples which might not make sense for other samples to contain. This flexibility allows flow collectors to offer rich reporting without necessarily having to understand the functions that each device performs on a network.

The more we thought about what kind of features and flexibility we wanted in an analytics system, the more we began to appreciate the elegance of traditional network monitoring. We realized that we could take advantage of the similarities between Cloudflare’s software architecture and “network functions” by having each software component emit its own packet samples with its own ...