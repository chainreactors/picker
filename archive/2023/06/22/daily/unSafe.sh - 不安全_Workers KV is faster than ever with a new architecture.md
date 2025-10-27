---
title: Workers KV is faster than ever with a new architecture
url: https://buaq.net/go-169778.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:40.381832
---

# Workers KV is faster than ever with a new architecture

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

![](https://8aqnet.cdn.bcebos.com/fe3b0d2611eb70137fbdaf4f445d8a39.jpg)

Workers KV is faster than ever with a new architecture

Loading...
*2023-6-21 21:0:12
Author: [blog.cloudflare.com(查看原文)](/jump-169778.htm)
阅读量:12
收藏*

---

Loading...

* [![Charles Burnett](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/04/Profile-Pic.jpeg)](https://blog.cloudflare.com/author/charles/)
* [![Vitali Lovich](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/09/IMG_1567.jpg)](https://blog.cloudflare.com/author/vitali/)

![Workers KV is faster than ever with a new architecture](https://blog.cloudflare.com/content/images/2023/06/image3-15.png)

We’re excited to announce a significant performance improvement coming to Workers KV, focused on dramatically improving cold read performance and reducing latency, even for long tail access patterns.

Developers using KV have seen great performance on hot reads, but ask why their 95th percentile latency — often on a key (or set of keys) that hadn’t been accessed recently or in that region — was higher than expected. We took this feedback to heart: we’ve been working feverishly on a new caching layer for KV behind the scenes, which enables customers to achieve much more frequent hot reads, reduced worst case latency times, better flexibility and control over cache TTLs, and much faster consistency over our previous iterations, and it’s now live for all KV users.

The best part? Developers using KV don’t need to change anything to benefit from this increased performance.

## What is Workers KV?

[Workers KV](https://blog.cloudflare.com/workers-kv-is-ga/) is a key value store designed for read heavy use-cases and applications powered by Cloudflare’s network. KV’s focus on read-heavy use-cases allows it to serve hot (cached) reads in milliseconds, which makes it ideal for storing per-application or customer configuration data, routing configuration, multivariate (A/B testing) configurations, and even small asset data that you need to serve quickly.  Anything that you can serialize and need quickly you can store in KV, all the way up to 25 MiB worth of data per each individual key, with no cap on total data stored.

## The problem

KV might be optimized for read-heavy workloads, but it’s critical that writes are globally available quickly enough that they’re useful for your application. Under typical conditions, the convergence delay for an eventually consistent system like KV is approximately one minute, globally: a write from one location should be able to be observed by all readers. Typical conditions are great, but typical unfortunately didn’t mean “always”. It could take significant time to restore global consistency where regions like North America and Europe are reading the same value. We needed to improve not just the average convergence, but the worst case as well.

Speaking of consistency, setting a long cache [Time to Live](https://developers.cloudflare.com/workers/runtime-apis/kv/#cache-ttl) (cacheTTL) for reads would result in a situation where you won’t notice a write for the entire cacheTTL duration, as the existing cached data had not timed out yet. This means you have to trade off read latency for infrequently accessed keys against noticing writes. Developers using KV have been consistent in their feedback: a higher cache TTL should improve performance, but not multiply the time it takes for KV to converge on a write to that key.

Lastly, our cold read times also left room for improvement. While [cache hits](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/) are fast in KV, a cache miss would result in a request being routed all the way to our storage backends. While this is slow for everyone, it was particularly slow for folks in regions not immediately in the US or EU.This is poor performance that doesn’t represent what we can achieve with our global presence.

## Our solution

### A new horizontally scaled tiered cache

We’ve revamped Workers KV to be powered by a new tiered cache implementation. This implementation is written as a Worker service. We reuse the Dynamic Dispatch infrastructure developed for [Workers for Platforms](https://blog.cloudflare.com/workers-for-platforms/) which lets us jump from our old KV worker into our new caching service within hundreds of microseconds. Importantly, this means we don’t impact cache hit performance to implement this new transparent caching layer. We leverage the same infrastructure powering [Smart Placement](https://blog.cloudflare.com/announcing-workers-smart-placement/) to implement the tiering.

Before we re-designed KV, our topology looked like this:

![](https://blog.cloudflare.com/content/images/2023/06/Before-we-re-designed-KV--our-topology-looked-like-this.png)

All data centers in Cloudflare’s network can reach out to the origin in the event of a cache miss or to do a background refresh.

### Cache TTL and efficiency

Our design goal was clear and ambitious: “*can we relax honoring the cacheTTL constraint without violating it*”? While this seems contradictory, the motivation is clear: we want to minimize the need to communicate with our storage backends while honoring the user-facing semantics of the cacheTTL setting, as it can have security implications if violated (e.g. if you use it to store and validate security tokens). Answering this design question also manages to simultaneously solve many of the problems outlined earlier.

### Comparing existing solutions

First, let’s look at the design constraints for two eventually consistent storage systems at Cloudflare: [Quicksilver](https://blog.cloudflare.com/introducing-quicksilver-configuration-distribution-at-internet-scale/) and [Tiered CDN](https://blog.cloudflare.com/introducing-regional-tiered-cache/).

Quicksilver gives us global consistency within seconds using a push architecture to replicate the data across all machines at Cloudflare. That architecture however doesn’t scale for Workers KV’s needs, which can have terabytes of data just within one namespace. This would be too much to replicate to every single data center.

By comparison, the tiered CDN cache is a pull mechanism where each hop pulls a more recent version of the asset into the local cache on access. That scales better because we only use storage for assets that are accessed, which works well with most use-cases where the vast majority of data is never retrieved. However, a pull based architecture is insufficient because it can only let us aggregate traffic across broader regions but we still can’t decouple how long we serve from the cache from the cacheTTL.

Push based architectures let us know when an asset is updated and enable scalable storage. By blending the properties of both systems, we can decouple how long we store the assets in cache from the cacheTTL. And that’s exactly what we did: KV now uses a hybrid push/pull caching layer where data centers closest to customers will pull from the regional data centers that are a little bit farther away. Writes will broadcast to all regional data centers that a key has been updated, so that the regional data center will remove that key from the local cache.

![](https://blog.cloudflare.com/content/images/2023/06/Traditional-regional-tiered-cache-topology.png)

Traditional [regional tiered cache topology](https://blog.cloudflare.com/introducing-regional-tiered-cache/)

We can solve this problem by taking advantage of the fact that we semantically understand the write operations that are happening within Worke...