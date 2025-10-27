---
title: Part 2: Rethinking cache purge with a new architecture
url: https://buaq.net/go-169775.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:35.240671
---

# Part 2: Rethinking cache purge with a new architecture

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

![](https://8aqnet.cdn.bcebos.com/6fee3318bc02ea9772710341f5590cce.jpg)

Part 2: Rethinking cache purge with a new architecture

Loading...
*2023-6-21 21:0:47
Author: [blog.cloudflare.com(查看原文)](/jump-169775.htm)
阅读量:17
收藏*

---

Loading...

* [![Zaidoon Abd Al Hadi](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/05/Screen-Shot-2021-05-20-at-10.45.44-AM.png)](https://blog.cloudflare.com/author/zaidoon/)

![Part 2: Rethinking cache purge with a new architecture](https://blog.cloudflare.com/content/images/2023/06/image4-12.png)

In [Part 1: Rethinking Cache Purge, Fast and Scalable Global Cache Invalidation](https://blog.cloudflare.com/part1-coreless-purge/), we outlined the importance of cache invalidation and the difficulties of purging caches, how our existing purge system was designed and performed, and we gave a high level overview of what we wanted our new Cache Purge system to look like.

It’s been a while since we published the first blog post and it’s time for an update on what we’ve been working on. In this post we’ll be talking about some of the architecture improvements we’ve made so far and what we’re working on now.

## Cache Purge end to end

We touched on the high level design of what we called the “coreless” purge system in part 1, but let’s dive deeper into what that design encompasses by following a purge request from end to end:

![](https://blog.cloudflare.com/content/images/2023/06/image3-13.png)

### Step 1: Request received locally

An API request to Cloudflare is routed to the nearest Cloudflare data center and passed to an **API Gateway worker**. This worker looks at the request URL to see which service it should be sent to and forwards the request to the appropriate upstream backend. Most endpoints of the Cloudflare API are currently handled by centralized services, so the **API Gateway worker** is often just proxying requests to the nearest “core” data center which have their own gateway services to handle authentication, authorization, and further routing. But for endpoints which aren’t handled centrally the **API Gateway worker** must handle [authentication](https://www.cloudflare.com/learning/access-management/what-is-authentication/) and route authorization, and then proxy to an appropriate upstream. For cache purge requests that upstream is a **Purge Ingest worker** in the same data center.

### Step 2: Purges tested locally

The **Purge Ingest worker** evaluates the purge request to make sure it is processible. It scans the URLs in the body of the request to see if they’re valid, then attempts to purge the URLs from the local data center’s cache. This concept of **local purging** was a new step introduced with the coreless purge system allowing us to capitalize on existing logic already used in every data center.

By leveraging the same ownership checks our data centers use to serve a zone’s normal traffic on the URLs being purged, we can determine if those URLs are even cacheable by the zone. Currently **more than 50%** of the URLs we’re asked to purge can’t be cached by the requesting zones, either because they don’t own the URLs (e.g. a customer asking us to purge https://cloudflare.com) or because the zone’s settings for the URL prevent caching (e.g. the zone has a “bypass” cache rule that matches the URL). All such purges are superfluous and shouldn’t be processed further, so we filter them out and avoid broadcasting them to other data centers freeing up resources to process more legitimate purges.

On top of that, generating the cache key for a file isn’t free; we need to load zone configuration options that might affect the cache key, apply various transformations, et cetera. The cache key for a given file is the same in every data center though, so when we purge the file locally we now return the generated cache key to the **Purge Ingest worker** and broadcast that key to other data centers instead of making each data center generate it themselves.

### Step 3: Purges queued for broadcasting

![purge request to small colo, ingest worker sends to queue worker in T1](https://blog.cloudflare.com/content/images/2023/06/image2-15.png)

Once the local purge is done the **Purge Ingest worker** forwards the purge request with the cache key obtained from the local cache to a **Purge Queue worker**. The queue worker is a [Durable Object](https://developers.cloudflare.com/workers/learning/using-durable-objects/) worker using its persistent state to hold a queue of purges it receives and pointers to how far along in the queue each data center in our network is in processing purges.

The queue is important because it allows us to automatically recover from a number of scenarios such as connectivity issues or data centers coming back online after maintenance. Having a record of all purges since an issue arose lets us replay those purges to a data center and “catch up”.

But Durable Objects are globally unique, so having one manage all global purges would have just moved our centrality problem from a core data center to wherever that Durable Object was provisioned. Instead we have dozens of Durable Objects in each region, and the **Purge Ingest worker** looks at the load balancing pool of Durable Objects for its region and picks one (often in the same data center) to forward the request to. The Durable Object will write the purge request to its queue and immediately loop through all the data center pointers and attempt to push any outstanding purges to each.

While benchmarking our performance we found our particular workload exhibited a “goldilocks zone” of throughput to a given Durable Object. On script startup we have to load all sorts of data like network topology and data center health–then refresh it continuously in the background–and as long as the Durable Object sees steady traffic it stays active and we amortize those startup costs. But if you ask a single Durable Object to do too much at once like send or receive too many requests, the single-threaded runtime won’t keep up. Regional purge traffic fluctuates a lot depending on local time of day, so there wasn’t a static quantity of Durable Objects per region that would let us stay within the goldilocks zone of enough requests to each to keep them active but not too many to keep them efficient. So we built load monitoring into our Durable Objects, and a **Regional Autoscaler worker** to aggregate that data and adjust load balancing pools when we start approaching the upper or lower edges of our efficiency goldilocks zone.

### Step 4: Purges broadcast globally

![multiple regions, durable object sends purges to fanouts in other regions, fanout sends to small colos in their region](https://blog.cloudflare.com/content/images/2023/06/image1-22.png)

Once a purge request is queued by a **Purge Queue worker** it needs to be broadcast to the rest of Cloudflare’s data centers to be carried out by their caches. The Durable Objects will broadcast purges directly to all data centers in their region, but when broadcasting to other regions they pick a **Purge Fanout worker** per region to take care of their region’s distribution. The fanout workers manage queues of their own as well as pointers for all of their region’s data centers, and in fact they share a lot of the same logic as the **Purge Queue workers** in order to do so. One key difference is fanout workers aren’t Durable Objects; they’re normal worker scripts, and their queues are purely in memory as opposed to being backed by Durable Object state. This means not all queue worker Durable Objects are talking to the...