---
title: Recapping Speed Week 2023
url: https://buaq.net/go-170418.html
source: unSafe.sh - 不安全
date: 2023-06-27
fetch_date: 2025-10-04T11:44:48.929091
---

# Recapping Speed Week 2023

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

![](https://8aqnet.cdn.bcebos.com/3f6cdaa6077cee8d13af78803f789e6c.jpg)

Recapping Speed Week 2023

Loading...
*2023-6-26 21:0:7
Author: [blog.cloudflare.com(查看原文)](/jump-170418.htm)
阅读量:24
收藏*

---

Loading...

* [![Sam Marsh](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/09/Screenshot-2022-09-27-at-12.55.51.png)](https://blog.cloudflare.com/author/sam-marsh/)

![Recapping Speed Week 2023](https://blog.cloudflare.com/content/images/2023/06/image1-42.png)

Speed Week 2023 is officially a wrap.

In our [Welcome to Speed Week 2023](https://blog.cloudflare.com/welcome-to-speed-week-2023/) blog post, we set a clear goal:

> ***“This week we will help you measure what matters. We’ll help you gain insight into your performance, from Zero Trust and API’s to websites and applications. And finally we’ll help you get faster. Quickly.”.***

This week we published five posts on how to measure performance, explaining which metrics and approaches make sense and why. We had a deep dive on the latest Core Web Vital, “[Interaction to Next Paint](https://blog.cloudflare.com/inp-get-ready-for-the-new-core-web-vital/)”, what it means and how we can help. There was a post on Time To First Byte (TTFB) and why it isn't a [good](https://blog.cloudflare.com/ttfb-is-not-what-it-used-to-be/) way to measure good web performance. We also wrote about how to [measure](https://blog.cloudflare.com/how-we-think-about-zero-trust-performance/) Zero Trust performance, and announced the [Internet](https://blog.cloudflare.com/introducing-radar-internet-quality-page/) Quality page of Cloudflare Radar - giving everyone the ability to compare Internet connection quality across Internet Service Providers, countries, and more.

We launched new products such as [Observatory](https://blog.cloudflare.com/cloudflare-observatory-generally-available/), [Digital Experiencing Monitoring](https://blog.cloudflare.com/digital-experience-monitoring-beta/) and [Timing Insights](https://blog.cloudflare.com/introducing-timing-insights/). These products give an incredible window into how your applications and websites are performing through the eyes of website visitors and your employees.

Next, we showed how we continue to be the fastest, with fresh posts on how we have the [fastest network](https://blog.cloudflare.com/speed-week-2023-network-performance-update/), [fastest Secure Web Gateway](https://blog.cloudflare.com/spotlight-on-zero-trust/), [fastest Zero Trust Network Access](https://blog.cloudflare.com/spotlight-on-zero-trust/) and [fastest Remote Browser Isolation](https://blog.cloudflare.com/spotlight-on-zero-trust/) solutions. There was even an update on [how our global network grew to 300 cities](https://blog.cloudflare.com/cloudflare-connected-in-over-300-cities/). The Cloudflare network is at the center of everything we do, and every product we build benefits from the speed and scale it provides and the proximity to the user.

There were also a number of great product announcements which make speed simple, single button performance boosts to accelerate your traffic. [Smart Hints](https://blog.cloudflare.com/smart-hints/), [HTTP/3 Prioritization,](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/) [Argo for UDP](https://blog.cloudflare.com/turbo-charge-gaming-and-streaming-with-argo-for-udp/), [Brotli end-to-end](https://blog.cloudflare.com/this-is-brotli-from-origin/), [LL-HLS for Stream](https://blog.cloudflare.com/low-latency-hls-support-for-cloudflare-stream/) and [Ricochet for API Gateway](https://blog.cloudflare.com/speeding-up-apis-ricochet-for-api-gateway/) all make speed simple - giving you an immediate speed boost on your traffic for *very* minimal, if any configuration.

We also showed how AI / ML continue to play a big part at Cloudflare, with posts discussing why running [AI inference on Cloudflare's network](https://blog.cloudflare.com/globally-distributed-ai-and-a-constellation-update/) makes performance sense, and how we both [scale and run](https://blog.cloudflare.com/scalable-machine-learning-at-cloudflare/) machine learning at the [microseconds level.](https://blog.cloudflare.com/how-cloudflare-runs-ml-inference-in-microseconds/)

Finally, we wrote about how we are making it easier than ever for customers to migrate to Cloudflare from legacy vendors via our [Turpentine](https://blog.cloudflare.com/turpentine-v2-migration-program/) and [Descaler](https://blog.cloudflare.com/descaler-program-update/) programs.

We’re on a mission to be the fastest at everything we do, and to make it simple for our customers to get the best performance.

In case you missed any of the announcements, take a look at the summary and navigation guide below.

### AI / Machine Learning

| Announcement | Summary |
| --- | --- |
| [Globally distributed AI and a Constellation update](https://blog.cloudflare.com/globally-distributed-ai-and-a-constellation-update/) | Announcing new Constellation features, explaining why it’s the first globally distributed AI platform and why deploying your machine learning tasks in our global network is advantageous. |
| [Every request, every second: scalable machine learning at Cloudflare](https://blog.cloudflare.com/scalable-machine-learning-at-cloudflare/) | Describing the technical strategies that have enabled us to expand the number of machine learning features and models, all while substantially reducing the processing time for each HTTP request on our network. |
| [How Orpheus automatically routes around bad Internet weather](https://blog.cloudflare.com/orpheus-saves-internet-requests-while-maintaining-speed/) | A little less than two years ago, Cloudflare made Orpheus automatically available to all customers for free. Since then, Orpheus has saved 132 billion Internet requests from failing by intelligently routing them around connectivity outages, prevented 50+ Internet incidents from impacting our customers, and made our customer’s origins more reachable to everyone on the Internet. Let’s dive into how Orpheus accomplished these feats over the last year. |
| [How Cloudflare runs machine learning inference in microseconds](https://blog.cloudflare.com/how-cloudflare-runs-ml-inference-in-microseconds/) | How we optimized bot management’s machine learning model execution. To reduce processing latency, we've undertaken a project to rewrite our bot management technology, porting it from Lua to Rust, and applying a number of performance optimizations. This post focuses on optimizations applied to the machine-learning detections within the bot management module, which account for approximately 15% of the latency added by bot detection. By switching away from a garbage collected language, removing memory allocations, and optimizing our parsers, we reduce the P50 latency of the bot management module by 79μs - a 20% reduction. |

### Zero Trust

| Announcement | Summary |
| --- | --- |
| [Spotlight on Zero Trust: we're fastest and here's the proof](https://blog.cloudflare.com/spotlight-on-zero-trust/) | Cloudflare is the fastest Secure Web Gateway in 42% of testing scenarios, the most of any provider. Cloudflare is 46% faster than Zscaler, 56% faster than Netskope, and 10% faster than Palo Alto for ZTNA, and 64% faster than Zscaler for RBI scenarios. |
| [Understanding end user-connectivity and performance with Digital Experience Monitoring, now available in beta](https://blog.cloudflare.com/digital-experience-monitoring-beta/) | DEX allows administrators to monitor their WARP Deployment and create predefined application tests. Features include ...