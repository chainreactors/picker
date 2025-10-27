---
title: Every request, every microsecond: scalable machine learning at Cloudflare
url: https://buaq.net/go-169402.html
source: unSafe.sh - 不安全
date: 2023-06-20
fetch_date: 2025-10-04T11:47:03.412642
---

# Every request, every microsecond: scalable machine learning at Cloudflare

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

![](https://8aqnet.cdn.bcebos.com/787b5e01ad8627f179a9aa4532e1d1c5.jpg)

Every request, every microsecond: scalable machine learning at Cloudflare

Loading...
*2023-6-19 21:0:51
Author: [blog.cloudflare.com(查看原文)](/jump-169402.htm)
阅读量:17
收藏*

---

Loading...

* [![Alex Bocharov](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2018/02/27b2849.jpg)](https://blog.cloudflare.com/author/alex-bocharov/)

![Every request, every microsecond: scalable machine learning at Cloudflare](https://blog.cloudflare.com/content/images/2023/06/image7-3.png)

In this post, we will take you through the advancements we've made in our machine learning capabilities. We'll describe the technical strategies that have enabled us to expand the number of machine learning features and models, all while substantially reducing the processing time for each HTTP request on our network. Let's begin.

## Background

For a comprehensive understanding of our evolved approach, it's important to grasp the context within which our machine learning detections operate. Cloudflare, on average, serves over **46 million HTTP requests per second**, surging to more than 63 million requests per second during peak times.

Machine learning detection plays a crucial role in ensuring the security and integrity of this vast network. In fact, it classifies the largest volume of requests among all our detection mechanisms, providing the final [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) decision for **over 72%** of all HTTP requests. Going beyond, we run several machine learning models in shadow mode for every HTTP request.

At the heart of our machine learning infrastructure lies our reliable ally, [CatBoost](https://catboost.ai/). It enables ultra low-latency model inference and ensures high-quality predictions to detect novel threats such as [stopping bots targeting our customers' mobile apps](https://blog.cloudflare.com/machine-learning-mobile-traffic-bots/). However, it's worth noting that **machine learning model inference** is just one component of the overall latency equation. Other critical components include **machine learning feature extraction and preparation**. In our quest for optimal performance, we've continuously optimized each aspect contributing to the overall latency of our system.

Initially, our machine learning models relied on **single-request features**, such as presence or value of certain headers. However, given the ease of spoofing these attributes, we evolved our approach. We turned to **inter-request features** that leverage aggregated information across multiple dimensions of a request in a sliding time window. For example, we now consider factors like the number of unique user agents associated with certain request attributes.

The extraction and preparation of inter-request features were handled by **Gagarin**, a Go-based feature serving platform we developed. As a request arrived at Cloudflare, we extracted dimension keys from the request attributes. We then looked up the corresponding machine learning features in the [multi-layered cache](https://github.com/thibaultcha/lua-resty-mlcache). If the desired machine learning features were not found in the cache, a **memcached "get" request** was made to Gagarin to fetch those. Then machine learning features were plugged into CatBoost models to produce detections, which were then surfaced to the customers via Firewall and Workers fields and internally through our [logging pipeline to ClickHouse](https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/). This allowed our data scientists to run further experiments, producing more features and models.

![](https://blog.cloudflare.com/content/images/2023/06/image3-3.png)

Previous system design for serving machine learning features over Unix socket using Gagarin.

Initially, Gagarin exhibited decent latency, with a median latency around **200 microseconds** to serve all machine learning features for given keys. However, as our system evolved and we introduced more features and dimension keys, coupled with increased traffic, the cache hit ratio began to wane. The median latency had increased to **500 microseconds** and during peak times, the latency worsened significantly, with the p99 latency soaring to roughly **10 milliseconds**. Gagarin underwent extensive low-level tuning, optimization, profiling, and benchmarking. Despite these efforts, we encountered the limits of inter-process communication (IPC) using Unix Domain Socket (UDS), among other challenges, explored below.

### Problem definition

In summary, the previous solution had its drawbacks, including:

* **High tail latency**: during the peak time, a portion of requests experienced increased  latency caused by CPU contention on the Unix socket and Lua garbage collector.
* **Suboptimal resource utilization:** CPU and RAM utilization was not optimized to the full potential, leaving less resources for other services running on the server.
* **Machine learning features availability**: decreased due to memcached timeouts, which resulted in a higher likelihood of false positives or false negatives for a subset of the requests.
* **Scalability constraints**: as we added more machine learning features, we approached the scalability limit of our infrastructure.

Equipped with a comprehensive understanding of the challenges and armed with quantifiable metrics, we ventured into the next phase: seeking a more efficient way to fetch and serve machine learning features.

## Exploring solutions

In our quest for more efficient methods of fetching and serving machine learning features, we evaluated several alternatives. The key approaches included:

**Further optimizing Gagarin**: as we pushed our Go-based memcached server to its limits, we encountered a lower bound on latency reductions. This arose from IPC over UDS synchronization overhead and multiple data copies, the serialization/deserialization overheads, as well as the inherent latency of garbage collector and the performance of hashmap lookups in Go.

**Considering Quicksilver**: we contemplated using [Quicksilver](https://blog.cloudflare.com/tag/quicksilver/), but the volume and update frequency of machine learning features posed capacity concerns and potential negative impacts on other use cases. Moreover, it uses a Unix socket with the memcached protocol, reproducing the same limitations previously encountered.

**Increasing multi-layered cache size:** we investigated expanding cache size to accommodate tens of millions of dimension keys. However, the associated memory consumption, due to duplication of these keys and their machine learning features across worker threads, rendered this approach untenable.

**Sharding the Unix socket**: we considered sharding the Unix socket to alleviate contention and improve performance. Despite showing potential, this approach only partially solved the problem and introduced more system complexity.

**Switching to RPC:** we explored the option of using RPC for communication between our front line server and Gagarin. However, since RPC still requires some form of communication bus (such as TCP, UDP, or UDS), it would not significantly change the performance compared to the memcached protocol over UDS, which was already simple and minimalistic.

After considering these approaches, we shifted our focus towards investigating alternative Inter-Process Communication (IPC) mechanisms.

### IPC mechanisms

Adopting a [first principles](https://en.wikipedia.org/wiki/First_principle) design a...