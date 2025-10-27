---
title: Cloudflare Access is the fastest Zero Trust proxy
url: https://buaq.net/go-153981.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:25.319785
---

# Cloudflare Access is the fastest Zero Trust proxy

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

![](https://8aqnet.cdn.bcebos.com/f43ec65b010babbad38ea45c4c2c3b45.jpg)

Cloudflare Access is the fastest Zero Trust proxy

Loading...
*2023-3-17 23:51:36
Author: [blog.cloudflare.com(查看原文)](/jump-153981.htm)
阅读量:28
收藏*

---

Loading...

* [![David Tuber](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/https://blog-cloudflare-com-assets.storage.googleapis.com/2020/07/kutiya-face.png)](https://blog.cloudflare.com/author/tubes/)

![Cloudflare Access is the fastest Zero Trust proxy](https://blog.cloudflare.com/content/images/2023/03/image6-12.png)

During every Innovation Week, Cloudflare looks at our network’s performance versus our competitors. In past weeks, we’ve focused on how much faster we are compared to [reverse proxies](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/) like Akamai, or platforms that sell serverless compute that compares to our [Supercloud](https://blog.cloudflare.com/welcome-to-the-supercloud-and-developer-week-2022/), like Fastly and AWS. This week, we’d like to provide an update on how we compare to other reverse proxies as well as an update to our application services security product comparison against Zscaler and Netskope. This product is part of our Zero Trust platform, which helps secure applications and Internet experiences out to the public Internet, as opposed to our reverse proxy which protects your websites from outside users.

In addition to our [previous post showing how our Zero Trust platform compared against Zscaler](https://blog.cloudflare.com/network-performance-update-cio-edition/), we also [have previously shared extensive network benchmarking results](https://blog.cloudflare.com/benchmarking-edge-network-performance/) for reverse proxies from 3,000 last mile networks around the world. It’s been a while since we’ve shown you our progress towards being #1 in every last mile network. We want to show that data as well as revisiting our series of tests comparing Cloudflare Access to Zscaler Private Access and Netskope Private Access. For our overall network tests, Cloudflare is #1 in 47% of the top 3,000 most reported networks. For our application security tests, Cloudflare is 50% faster than Zscaler and 75% faster than Netskope.

In this blog we’re going to talk about why performance matters for our products, do a deep dive on what we’re measuring to show that we’re faster, and we’ll talk about how we measured performance for each product.

### Why does performance matter?

We talked about it in our [last blog](https://blog.cloudflare.com/network-performance-update-cio-edition/), but performance matters because it impacts your employees' experience and their ability to get their job done. Whether it’s accessing services through access control products, connecting out to the public Internet through a Secure Web Gateway, or securing risky external sites through Remote Browser Isolation, all of these experiences need to be frictionless.

A quick summary: say Bob at Acme Corporation is connecting from Johannesburg out to Slack or Zoom to get some work done. If Acme’s Secure Web Gateway is located far away from Bob in London, then Bob’s traffic may go out of Johannesburg to London, and then back into Johannesburg to reach his email. If Bob tries to do something like a voice call on Slack or Zoom, his performance may be painfully slow as he waits for his emails to send and receive. Zoom and Slack both recommend low latency for optimal performance. That extra hop Bob has to take through his gateway could decrease throughput and increase his latency, giving Bob a bad experience.

As we’ve discussed before, if these products or experiences are slow, then something worse might happen than your users complaining: they may find ways to turn off the products or bypass them, which puts your company at risk. A Zero Trust product suite is completely ineffective if no one is using it because it’s slow. Ensuring Zero Trust is fast is critical to the effectiveness of a Zero Trust solution: employees won’t want to turn it off and put themselves at risk if they barely know it’s there at all.

Much like Zscaler, Netskope may outperform many older, antiquated solutions, but their network still fails to measure up to a highly performant, optimized network like Cloudflare’s. We’ve tested all of our Zero Trust products against Netskope equivalents, and we’re even bringing back Zscaler to show you how Zscaler compares against them as well. So let’s dig into the data and show you how and why we’re faster in a critical Zero Trust scenario, comparing Cloudflare Access to Zscaler Private Access and Netskope Private Access.

### Cloudflare Access: the fastest Zero Trust proxy

Access control needs to be seamless and transparent to the user: the best compliment for a Zero Trust solution is employees barely notice it’s there. These services allow users to cache authentication information on the provider network, ensuring applications can be accessed securely and quickly to give users that seamless experience they want. So having a network that minimizes the number of logins required while also reducing the latency of your application requests will help keep your Internet experience snappy and reactive.

Cloudflare Access does all that 75% faster than Netskope and 50% faster than Zscaler, ensuring that no matter where you are in the world, you’ll get a fast, secure application experience:

![](https://blog.cloudflare.com/content/images/2023/03/pasted-image-0-10.png)

Cloudflare measured application access across ourselves, Zscaler and Netskope from 300 different locations around the world connecting to 6 distinct application servers in Hong Kong, Toronto, Johannesburg, São Paulo, Phoenix, and Switzerland. In each of these locations, Cloudflare’s P95 response time was faster than Zscaler and Netskope. Let’s take a look at the data when the application is hosted in Toronto, an area where Zscaler and Netskope should do well as it’s in a heavily interconnected region: North America.

![](https://blog.cloudflare.com/content/images/2023/03/pasted-image-0--1--8.png)

| ZT Access - Response time (95th Percentile) - Toronto | |
| --- | --- |
|  | 95th Percentile Response (ms) |
| Cloudflare | 2,182 |
| Zscaler | 4,071 |
| Netskope | 6,072 |

Cloudflare really stands out in regions with more diverse connectivity options like South America or Asia Pacific, where Zscaler compares better to Netskope than it does Cloudflare:

![](https://blog.cloudflare.com/content/images/2023/03/pasted-image-0--2--5.png)

When we look at application servers hosted locally in South America, Cloudflare stands out:

| ZT Access - Response time (95th Percentile) - South America | |
| --- | --- |
|  | 95th Percentile Response (ms) |
| Cloudflare | 2,961 |
| Zscaler | 9,271 |
| Netskope | 8,223 |

Cloudflare’s network shines here, allowing us to ingress connections close to the users. You can see this by looking at the Connect times in South America:

| ZT Access - Connect time (95th Percentile) - South America | |
| --- | --- |
|  | 95th Percentile Connect (ms) |
| Cloudflare | 369 |
| Zscaler | 1,753 |
| Netskope | 1,160 |

Cloudflare’s network sets us apart here because we’re able to get users onto our network faster and find the optimal routes around the world back to the application host. We’re twice as fast as Zscaler and three times faster than Netskope because of this superpower. Across all the different tests, Cloudflare’s Connect times is consistently faster across all 300 testing nodes.

![](https://blog.cloudflare.com/content/images/2023/03/pasted-image-0--3--5.png)

In our [last blog](https:...