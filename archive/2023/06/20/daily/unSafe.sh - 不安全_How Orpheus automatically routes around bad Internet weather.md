---
title: How Orpheus automatically routes around bad Internet weather
url: https://buaq.net/go-169403.html
source: unSafe.sh - 不安全
date: 2023-06-20
fetch_date: 2025-10-04T11:47:04.375142
---

# How Orpheus automatically routes around bad Internet weather

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

![](https://8aqnet.cdn.bcebos.com/a43fed51411461c21daed75546418a5c.jpg)

How Orpheus automatically routes around bad Internet weather

Loading...
*2023-6-19 21:0:49
Author: [blog.cloudflare.com(查看原文)](/jump-169403.htm)
阅读量:14
收藏*

---

Loading...

* [![Chris Draper](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/06/blog_headshot.jpg)](https://blog.cloudflare.com/author/chris-draper/)
* [![Braden Ehrat](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/2019-Profile-Pic-2.jpeg)](https://blog.cloudflare.com/author/braden/)

![How Orpheus automatically routes around bad Internet weather](https://blog.cloudflare.com/content/images/2023/06/image2-6.png)

Cloudflare’s mission is to help build a better Internet for everyone, and [Orpheus](https://blog.cloudflare.com/orpheus/) plays an important role in realizing this mission. Orpheus identifies Internet connectivity outages beyond Cloudflare’s network in real time then leverages the scale and speed of Cloudflare’s network to find alternative paths around those outages. This ensures that everyone can reach a Cloudflare customer’s [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) no matter what is happening on the Internet. The end result is powerful: Cloudflare  protects customers from Internet incidents outside our network while maintaining the average latency and speed of our customer’s traffic.

A little less than two years ago, Cloudflare made [Orpheus automatically available to all customers for free](https://blog.cloudflare.com/orpheus/). Since then, Orpheus has saved 132 billion Internet requests from failing by intelligently routing them around connectivity outages, prevented 50+ Internet incidents from impacting our customers, and made our customer’s origins more reachable to everyone on the Internet. Let’s dive into how Orpheus accomplished these feats over the last year.

### Increasing origin reachability

One service that Cloudflare offers is a [reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/) that receives Internet requests from end users then applies any number of services like [DDoS protection](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/), [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/), [load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/), and / or [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/). If the response to an end user’s request isn’t cached, Cloudflare routes the request to our customer’s origin servers. To be successful, end users need to be able to connect to Cloudflare, and Cloudflare needs to connect to our customer’s origin servers. With end users and customer origins around the world, and ~20% of websites using our network, this task is a tall order!

Orpheus provides origin reachability benefits to everyone using Cloudflare by identifying invalid paths on the Internet in real time, then routing traffic via alternative paths that are working as expected. This ensures Cloudflare can reach an origin no matter what problems are happening on the Internet on any given day.

### Reducing 522 errors

At some point while browsing the Internet, you may have run into this [522 error](https://support.cloudflare.com/hc/en-us/articles/115003011431-Troubleshooting-Cloudflare-5XX-errors#522error).

![](https://blog.cloudflare.com/content/images/2023/06/image3-4.png)

This error indicates that you, the end user, was unable to access content on a Cloudflare customer’s origin server because Cloudflare couldn’t connect to the origin. Sometimes, this error occurs because the origin is offline for everyone, and ultimately the origin owner needs to fix the problem. Other times, this error can occur even when the origin server is up and able to receive traffic. In this case, some people can reach content on the origin server, but other people using a different Internet routing path cannot because of connectivity issues across the Internet.

Some days, a specific network may have excellent connectivity, while other days that network may be congested or have paths that are impassable altogether. The Internet is a massive and unpredictable [network of networks](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/), and the “weather” of the Internet changes every day.

When you see this error, Cloudflare attempted to connect to an origin on behalf of the end user, but did not receive a response back from the origin. Either the connection request never reached the origin, or the origin’s reply was dropped on the way back to Cloudflare. In the case of 522 errors, Cloudflare and the origin server could both be working as expected, but packets are dropped on the network path between them.

These 522 errors can cause a lot of frustration, and Orpheus was built to reduce them. The goal of Orpheus is to ensure that if at least one Cloudflare data center can connect to an origin, then anyone using Cloudflare’s network can also reach that origin, even if there are Internet connectivity problems happening outside of Cloudflare’s network.

### Improving origin reachability for an example customer using Cloudflare

Let’s look at a concrete example of how Orpheus makes the Internet better for everyone by saving an origin request that would have otherwise failed. Imagine that you’re running an e-commerce website that sells dog toys online, and your store is hosted by an origin server in Chicago.

Imagine there are two different customers visiting your website at the same time: the first customer lives in Seattle, and the second customer lives in Tampa. The customer in Seattle reaches your origin just fine, but the customer in Tampa tries to connect to your origin and experiences a problem. It turns out that a construction crew accidentally damaged an Internet fiber line in Tampa, and Tampa is having connectivity issues with Chicago. As a result, any customer in Tampa receives a 522 error when they try to buy your dog toys online.

This is where Orpheus comes in to save the day. Orpheus detects that users in Tampa are receiving 522 errors when connecting to Chicago. Its database shows there is another route from Tampa through Boston and then to Chicago that is valid. As a result, Orpheus saves the end user’s request by rerouting it through Boston and taking an alternative path. Now, everyone in Tampa can still buy dog toys from your website hosted in Chicago, even though a fiber line was damaged unexpectedly.

![](https://blog.cloudflare.com/content/images/2023/06/image1-7.png)

### How does Orpheus save requests that would otherwise fail via only BGP?

[BGP (Border Gateway Protocol)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) is like the postal service of the Internet. It’s the protocol that makes the Internet work by enabling data routing. When someone requests data over the Internet, BGP is responsible for looking at all the available paths a request could take, then selecting a route.

BGP is designed to route around network failures by finding alternative paths to the destination IP address after the preferred path goes down. Sometimes, BGP does not route around a network failure at all. In this case, Cloudflare still receives BGP advertisements that an origin network is reachable via a particular [autonomous system (AS)](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/), when actually packets sent through...