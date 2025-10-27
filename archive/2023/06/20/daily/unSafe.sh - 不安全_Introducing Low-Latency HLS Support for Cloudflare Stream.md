---
title: Introducing Low-Latency HLS Support for Cloudflare Stream
url: https://buaq.net/go-169401.html
source: unSafe.sh - 不安全
date: 2023-06-20
fetch_date: 2025-10-04T11:47:02.098706
---

# Introducing Low-Latency HLS Support for Cloudflare Stream

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

![](https://8aqnet.cdn.bcebos.com/848b171efa861bbcd2f02f97aca463e6.jpg)

Introducing Low-Latency HLS Support for Cloudflare Stream

Loading...
*2023-6-19 21:0:57
Author: [blog.cloudflare.com(查看原文)](/jump-169401.htm)
阅读量:20
收藏*

---

Loading...

* [![Taylor Smith](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/IMG_20210814_131541002.jpg)](https://blog.cloudflare.com/author/tsmith/)

![Introducing Low-Latency HLS Support for Cloudflare Stream](https://blog.cloudflare.com/content/images/2023/06/image5-4.png)

Stream Live lets users easily scale their live streaming apps and websites to millions of creators and concurrent viewers without having to worry about bandwidth costs or purchasing hardware for real-time encoding at scale. Stream Live lets users focus on the content rather than the infrastructure — taking care of the codecs, protocols, and bitrate automatically. When we launched Stream Live last year, we focused on bringing high quality, feature-rich streaming to websites and applications with HTTP Live Streaming (HLS).

Today, we're excited to introduce support for *Low-Latency* HTTP Live Streaming (LL-HLS) in a closed beta, offering you an even faster streaming experience. LL-HLS will reduce the latency a viewer may experience on their player from highs of around 30 seconds to less than 10 in many cases. Lower latency brings creators even closer to their viewers, empowering customers to build more interactive features like Q&A or chat and enabling the use of live streaming in more time-sensitive applications like sports, gaming, and live events.

### Broadcast with less than 10-second latency

LL-HLS is an extension of HLS and allows us to reduce *glass-to-glass latency* — the time between something happening on the broadcast end and a user seeing it on their screen. This includes everything from broadcaster encoding to client-side buffering because we know the experience is driven by what a user sees, not when a byte is delivered into a buffer. Depending on encoder and player settings, broadcasters' content can be playing on viewers' screens in less than ten seconds.

Our addition of LL-HLS support builds on all the best parts of Stream including simple, predictable pricing. You never have to pay for ingest (broadcasting to us), compute (encoding), or egress. It costs \$5 per 1,000 minutes of video stored per month and \$1 per 1,000 minutes of video viewed per month. This allows you to stream with peace of mind, knowing there are no surprise fees.

Other platforms tack on live recordings as a separate add-on feature, and those recordings only become available minutes or even hours after a live stream ends. With Cloudflare Stream, Live segments are automatically recorded and immediately available for on-demand playback.

Stream also provides both a built-in web player and HLS manifests to use in a compatible player of your choosing. This enables you or your users to go live using the same protocols and tools that broadcasters big and small use to go live to YouTube or Twitch, but gives you full control over access and presentation of live streams.

We also provide access control with signed URLs allowing you to protect your content, sharing with only certain users. This allows you to restrict access so only logged in members can watch a particular video, or only let users watch your video for a limited time period. And of course, Stream is powered by Cloudflare's global network for fast delivery worldwide, with points of presents within 50ms of 95% of the Internet connected population.

![](https://blog.cloudflare.com/content/images/2023/06/image2-8.png)

Left: Broadcasting to Stream Live using OBS. Right: Watching that same Stream. Note the five second difference in the NIST clock between the source and the playback.

Powering the LL-HLS experience involved making several improvements to our underlying infrastructure. One of the largest challenges we encountered was that our existing architecture involved a pipeline with multiple buffers as long as the keyframe interval. This meant Stream Live would introduce a delay of up to five times the keyframe interval. To resolve this, we simplified a portion of our pipeline — now, we work with individual frames rather than whole keyframe-intervals, but without giving up the economies of scale our approach to encoding provides. This decoupling of keyframe interval and internal buffer duration lets us dramatically reduce latency in HLS, with a maximum of twice the keyframe interval.

### Getting started with the LL-HLS beta

As we prepare to ship this new functionality, we're [looking for beta testers](https://docs.google.com/forms/d/e/1FAIpQLSeZ2NBuAXC75aDJllhVA0itW0TZ1w4s48TvFm-eP7R1h9Hc9g/viewform?usp=sf_link) to help us test non-production workloads. To participate in the beta, your application should be configured with these settings:

* H.264 video codec
* Constant bitrate
* Keyframe interval (GOP size) of 2s
* No B Frames
* Using the Stream built-in player

Getting started with Stream Live only takes a few minutes. Create a Live Input in the Cloudflare dashboard, then Stream will automatically provide RTMPS and SRT endpoints to broadcast your feed to us as well as an HTML embed for our built-in player and the HLS manifest for a custom player.

![](https://blog.cloudflare.com/content/images/2023/06/image4-6.png)![](https://blog.cloudflare.com/content/images/2023/06/image3-7.png)

This connection information can be added easily to a broadcast application like OBS to start streaming immediately:

![](https://blog.cloudflare.com/content/images/2023/06/image1-9.png)

Customers in the LL-HLS beta will need to make a minor adjustment to the built-in player embed code, but there are no changes to Live Input configuration, dashboard interface, API, or existing functionality.

### Sign up today

LL-HLS is Stream Live’s latest tool to bring your creators and audiences together. After the beta period, this feature will be generally available to all new and existing Stream subscriptions with no pricing changes or contract requirements --- all part of building the fastest, simplest serverless live streaming platform. [Join our beta](https://docs.google.com/forms/d/e/1FAIpQLSeZ2NBuAXC75aDJllhVA0itW0TZ1w4s48TvFm-eP7R1h9Hc9g/viewform?usp=sf_link) to start test-driving Low-Latency HLS!

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
[your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://1.1.1.1/) from any device to get started with
our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a
new career direction, check out [our open
positions](https://cloudflare.com/careers).

[Speed Week](https://blog.cloudflare.com/tag/speed-week/)
[Live Streaming](https://blog.cloudflare.com/tag/live-streaming/)
[Video](https://blog.cloudflare.com/tag/video/)
[HLS](https://blog.cloudflare.com/tag/hls/)

文章来源: http://blog.cloudflare.com/low-latency-hls-support-for-cloudflare-stream/
 如有侵权请联系:admin#unsafe.sh

© [unSa...