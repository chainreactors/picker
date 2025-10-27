---
title: Cloudflare is faster than Netskope and Zscaler across LATAM
url: https://buaq.net/go-161524.html
source: unSafe.sh - 不安全
date: 2023-05-04
fetch_date: 2025-10-04T11:38:34.972189
---

# Cloudflare is faster than Netskope and Zscaler across LATAM

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

![](https://8aqnet.cdn.bcebos.com/a6b5c5b24ccc921b3644280cf0493796.jpg)

Cloudflare is faster than Netskope and Zscaler across LATAM

Loading...
*2023-5-3 21:0:12
Author: [blog.cloudflare.com(查看原文)](/jump-161524.htm)
阅读量:26
收藏*

---

Loading...

* [![Nicholas Platais](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/Nicholas-Platais--.png)](https://blog.cloudflare.com/author/nicholas/)
* [![Gonzalo Chavarri](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/Gonzalo-Chavarri.jpeg)](https://blog.cloudflare.com/author/gonzalo/)
* [![David Tuber](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/https://blog-cloudflare-com-assets.storage.googleapis.com/2020/07/kutiya-face.png)](https://blog.cloudflare.com/author/tubes/)

This post is also available in [Español](https://blog.cloudflare.com/es-es/cloudflare-is-faster-than-netskope-and-zscaler-across-latam-es-es/) and [Português](https://blog.cloudflare.com/pt-br/cloudflare-is-faster-than-netskope-and-zscaler-across-latam-pt-br/).

![Cloudflare is faster than Netskope and Zscaler across LATAM.](https://blog.cloudflare.com/content/images/2023/05/image16.png)

Last CIO Week, [we showed you how our network stacks up against competitors across several countries.](https://blog.cloudflare.com/network-performance-update-cio-edition/) We demonstrated with our tests that Cloudflare Access is 38% faster than ZScaler (ZPA) worldwide.

Today we wanted to focus on LATAM and show how our network performed against Zscaler and Netskope in Argentina, Brazil, Chile, Colombia, Costa Rica, Ecuador, Mexico, Peru, Uruguay and Venezuela.

With **47 data centers across Latin America and Caribbean, Cloudflare has the largest number of SASE Points of Presence across all vendors**, meaning we can offer our [Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/?ref=blog.cloudflare.com) services closer to the end user and reduce unwanted latency.

![](https://blog.cloudflare.com/content/images/2023/05/Cloudflare-is-faster-than-Netskope-and-Zscaler-across-LATAM.png)

We’ve run a series of tests comparing our Zero Trust Network Access product against Zscaler and Netskope’s comparable products.

For each of these tests, we used 95th percentile Time to First Byte and Response tests, which measure the time it takes for a user to make a request, and get the start of the response (Time to First Byte), and the end of the response (Response). These tests were designed with the goal of trying to measure performance from an end-user perspective.

In this blog we’re going to talk about why performance matters and do a deep dive on what we’re measuring to show that we’re faster.

## Why does performance matter?

Performance matters because it impacts your employees' experience and their ability to get their job done. For example, if Anna is connecting to a hosted, protected application like Salesforce to complete some work, she doesn’t want to be waiting constantly for pages to load or to authenticate her requests. In an access-controlled application, the first thing you do when you connect is you log in. If that login takes a long time, you may get distracted with a random message from a coworker and even when you get authenticated, you still want your normal application experience to be snappy and smooth: users should never notice Zero Trust when it’s at its best.

If these products or experiences are slow, then something worse might happen than your users complaining: they may find ways to turn off the products or bypass them, which puts your company at risk. A Zero Trust product suite is completely ineffective if no one is using it because it’s slow.

Ensuring Zero Trust is fast is critical to the effectiveness of a Zero Trust solution: employees won’t want to turn it off and put themselves at risk if they barely know it’s there at all. Services like Zscaler or Netskope may outperform many older, antiquated solutions, but their network still fails to measure up to a highly performant, optimized network like Cloudflare’s.

## Cloudflare Access: the fastest Zero Trust proxy

Access control needs to be seamless and transparent to the user: the best compliment for a Zero Trust solution is employees barely notice it’s there. Services like Cloudflare Access and Zscaler Private Access (ZPA) allow users to cache authentication information on the provider network, ensuring applications can be accessed securely and quickly to give users that seamless experience they want. So having a network that minimizes the number of logins required while also reducing the [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/?ref=blog.cloudflare.com) of your application requests by delivering the service closer to the user will help keep your Internet experience snappy and reactive.

For these tests, Cloudflare contracted Miercom, a third party who performed a set of tests that was intended to replicate an end-user connecting to a resource protected by Cloudflare, Zscaler and Netskope. Miercom set up application instances in 14 locations around the world, and devised a test that would log into the application through various Zero Trust providers to access certain content. The test methodology is described as follows, but you can look at the full report from Miercom detailing their test methodology [here](https://cloudflare.com/lp/miercom-report-cloudflare-vs-zscaler/?ref=blog.cloudflare.com):

* User connects to the application from a browser mimicked by a Catchpoint instance - new session
* User authenticates against their identity provider
* User accesses resource
* User refreshes the browser page and tries to access the same resource but with credentials already present - existing session

In this test we evaluated Cloudflare against Zscaler and Netskope accessing applications hosted in two specific regions (Brazil and the US south-west). We tested the response time for an existing session, when a user has already been authenticated and that authentication information can be cached.

Here’s how this data looks for each of the 10 countries we tested across LATAM:

### Argentina

![](https://blog.cloudflare.com/content/images/2023/05/argentina.png)

|  | Zero Trust Access - Time to First Byte (App in Brazil) |
| --- | --- |
|  | 95th Percentile (ms) |
| Cloudflare | 1,203 |
| Netskope | 8,319 |
| Zscaler | 5,961 |

When we drill into the data, we see that Cloudflare is faster when connecting from Argentina to an app hosted in Brazil. Cloudflare’s 95th percentile time to first byte times are 75% faster than Zscaler and 85% faster than Netskope.

Cloudflare is also faster when connecting from Argentina to an app hosted in the United States (South West Region). Cloudflare’s 95th percentile time to first byte times are 70% faster than Zscaler and 68% faster than Netskope:

![](https://blog.cloudflare.com/content/images/2023/05/argentina2.png)

|  | Zero Trust Access - Time to First Byte (App in US West) |
| --- | --- |
|  | 95th Percentile (ms) |
| Cloudflare | 1,587 |
| Netskope | 5,082 |
| Zscaler | 5,299 |

### Brazil

![](https://blog.cloudflare.com/content/images/2023/05/unnamed-1.png "Chart")

|  | Zero Trust Access - Time to First Byte (App in Brazil) |
| --- | --- |
|  | 95th Percentile (ms) |
| Cloudflare | 1,525 |
| Netskope | 3,799 |
| Zscaler | 3,916 |

When we drill into the data, we see that Cloudflare is faster when connecting from Brazil to an app hosted in Brazil. Cloudflare’s 95th percentile time to first byte tim...