---
title: Network performance update: Speed Week 2023
url: https://buaq.net/go-169871.html
source: unSafe.sh - 不安全
date: 2023-06-23
fetch_date: 2025-10-04T11:44:36.168685
---

# Network performance update: Speed Week 2023

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

![](https://8aqnet.cdn.bcebos.com/004f4e72c2a7c1c6ed89f93582bdbe12.jpg)

Network performance update: Speed Week 2023

Loading...
*2023-6-22 21:0:14
Author: [blog.cloudflare.com(查看原文)](/jump-169871.htm)
阅读量:16
收藏*

---

Loading...

* [![Onur Karaagaoglu](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/Onur.jpeg)](https://blog.cloudflare.com/author/onur/)

![Network performance update: Speed Week 2023](https://blog.cloudflare.com/content/images/2023/06/image5-13.png)

We constantly measure our own and other networks' performance, and look for ways to improve our performance; and share our results.

In this post we are going to share the most recent updates, and tell you about our tools and processes that we use to monitor and improve our network performance.

### First, the results

In July, 2022, we started taking a more granular look down to every single network and taking actions for the specific networks where we have some room for improvement. Cloudflare was already the fastest provider for most of the networks around the world (we define a network as country and AS number pair). Taking a closer look at the numbers, Cloudflare was ranked #1 in 33% of the networks and was within 2 ms or 5% of the #1 provider for 8% of the networks that we measured in terms of the 95th percentile TCP Connection Time. For reference, our closest competitor on that front was the fastest for 20% of networks.

As of May 31, 2023 those numbers have improved significantly. Today, Cloudflare is the fastest provider for 46% of networks—and was within 2 ms (95th percentile TCP Connection Time) or 5% of the fastest provider for 10% of the networks that we measured—whereas our closest competitor is now the fastest for 18% of networks.

Below is the change in percentage of networks that each provider is the fastest over time for Cloudflare and other services.

![](https://blog.cloudflare.com/content/images/2023/06/image3-22.png "Chart")

### Our tooling and process

We use Real User Measurements (RUM) and fetch a small file from Cloudflare, Akamai, CloudFront, Fastly and Google Cloud CDN. Browsers around the world report the performance of those providers from the perspective of the end-user network they are on. The goal is to provide an accurate picture of where different providers are faster, and more importantly, where Cloudflare can improve. You can read more about the methodology in the original Speed Week blog post [here](https://blog.cloudflare.com/benchmarking-edge-network-performance/).

Using the RUM data, we are able to measure various performance metrics, such as TCP Connection Time, Time to First Byte (TTFB), Time to Last Byte (TTLB), for ourselves and other networks.

One of the most important tools that we use for measuring and improving our performance is what we call Performance Benchmarks Dashboard. That's the dashboard where we can analyze the data that we collect in different dimensions.

Here are the metrics that we monitor based on some of the dimensions.

The first metric we closely monitor is the percent of networks that we are ranked #1 in terms of TCP Connection Time. That's a key performance indicator that we evaluate ourselves against.

![](https://blog.cloudflare.com/content/images/2023/06/image4-19.png)

The second metric we monitor is our overall performance in each country. This gives us visibility into the countries or regions that we need to pay closer attention to and take action towards improving our performance. Those actions will be listed later. Orange indicates the countries that Cloudflare is the fastest provider based on the TCP Connection Time.

![](https://blog.cloudflare.com/content/images/2023/06/image6-5.png)

The third set of metrics we use are TCP Connection Time and TTLB. The number of networks where we are #1 in terms of 95th percentile TCP Connection Time is one of our key performance indicators. We actively monitor and work on improving that metric. More on that later.

![](https://blog.cloudflare.com/content/images/2023/06/image1-32.png)

Using all the metrics listed above, the Performance Benchmarks Dashboard helps us to find networks where we can improve our performance. Our engineering teams monitor that dashboard and investigate the underlying reasons for degraded performance if there are any and the action items are displayed on the dashboard until they are resolved.

![](https://blog.cloudflare.com/content/images/2023/06/image2-30.png)

Once we identify a particular network to improve, we investigate the root cause and document the action items to improve our performance. Those actions generally fall under three categories.

The first category is establishing peering with that network in a specific location so that users can take the optimum path. That’s a critical component of a better Internet! [Here](https://blog.cloudflare.com/cloudflare-connected-in-over-300-cities/) is our more detailed blog post about that from earlier this week.

The second category is expanding our compute capacity in a specific data center so that we can serve the users at the closest data center.

And finally, we apply traffic engineering actions to make sure that the network is served in the optimum way. Traffic engineering actions are generally manual configurations that we apply, in case the path that’s chosen by the routing protocols is not the most performant path.

### What’s next

The data we collect gives us a granular view of every network that connects to Cloudflare and we constantly optimize our infrastructure to improve Cloudflare’s performance. We won’t rest until we’re #1 everywhere.

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
[Network Performance Update](https://blog.cloudflare.com/tag/network-performance-update/)

Related Posts

January 07, 2022 3:57PM

[## Cloudflare Innovation Weeks 2021](https://blog.cloudflare.com/2021-innovations-weeks/)

As we start planning our 2022 Innovation Weeks, we are reflecting back on the highlights from each of these weeks...

By

June 21, 2023 2:00PM

[## Workers KV is faster than ever with a new architecture](https://blog.cloudflare.com/faster-workers-kv-architecture/)

With the new architecture powering Workers KV our service will become faster and more scalable than ever. We have significantly reduced cold read probability, and enabled KV to serve over a trillion requests a month...

By

June 20, 2023 2:00PM

[## INP. Get ready for the new Core Web Vital](https://blog.cloudflare.com/inp-get-ready-for-the-new-core-web-vital/)

On May 10, 2023, Google announced that INP will replace FID in the Core Web Vitals in March 2024. The Core Web Vitals play a role in the Google Sear...