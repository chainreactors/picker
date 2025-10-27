---
title: How Kinsta used Workers and Workers KV to improve cache hit rates by 56%
url: https://buaq.net/go-169779.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:41.205037
---

# How Kinsta used Workers and Workers KV to improve cache hit rates by 56%

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

![](https://8aqnet.cdn.bcebos.com/b3736094742dd4c9c1cc6c6baf6a67b3.jpg)

How Kinsta used Workers and Workers KV to improve cache hit rates by 56%

Loading...
*2023-6-21 21:0:2
Author: [blog.cloudflare.com(查看原文)](/jump-169779.htm)
阅读量:16
收藏*

---

Loading...

* [![Steven Bonisteel (Guest Author)](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/sb_400x400.jpg)](https://blog.cloudflare.com/author/steven/)
* [![Paulo Paracutu (Guest Author)](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/5y9C4ShT_400x400.jpg)](https://blog.cloudflare.com/author/paulo-paracutu-guest-author/)

This is a guest post by Kinsta about their use of our platform.

![How Kinsta used Workers and Workers KV to improve cache hit rates by 56%](https://blog.cloudflare.com/content/images/2023/06/image2-18.png)

At [Kinsta](https://kinsta.com/), we’re obsessed with speed: Our Application Hosting, Database Hosting and Managed WordPress Hosting services all run on the Google Cloud Platform’s fastest Premium Tier Network and C2 Machines, and we rely on Cloudflare to keep the pedal to the metal for tens of thousands of customers who want to deliver their content around the world with speed and security.

While making that happen, we’ve learned a thing or two about using Cloudflare Workers and Workers KV to provide optimized caching rules for static and dynamic content.

In early 2023, we doubled down on Cloudflare cache wrangling, making caches more responsive to client-side configuration changes while also shifting the heavy lifting behind broadcasting feature updates away from our admins on the backend and into Cloudflare Workers. A key result was a dramatic increase in the share of customer data successfully cached, increasing 56.3% between October 2022 and March 2023.

![](https://blog.cloudflare.com/content/images/2023/06/image5-10.png)

Cloudflare Workers and Workers KV allow us to programmatically customize every request and response with minimal effort and lower latency. We no longer need to deploy changes to hundreds of thousands of containers when we want to implement new features; we can replicate or implement the feature with Workers and deploy it everywhere with a few commands and clicks, saving us days of work and maintenance.

### Request routing with Workers KV and Workers

Every Kinsta-hosted domain is a key, and its value contains at least the core settings, like the origin's IP and port, and a unique random ID. With this data easily available in Workers KV, we can use Workers to analyze, manipulate, and route requests to their expected backend. We also use Workers KV to store customer optimization options like Polish, Image Resizing, and Auto Minify.

To route requests to custom IPs and ports, we use resolveOverride, a Cloudflare-specific [Request property](https://developers.cloudflare.com/workers/runtime-apis/request/#requestinitcfproperties). Here's an example:

```
<pre><code class="language-javascript">
// Assign KV values to variables
const { customBackend } = kvdata.kinstaConf;

// Override the backend
cf.resolveOverride = customBackend;
</code></pre>
```

However, while Workers KV worked well to route requests, we soon noticed inconsistent responses in our cache. Sometimes a customer activated Polish and, due to Workers KV's one-minute cache, new requests arrived before Workers KV fully propagated the change, causing us to cache non-optimized assets. When this happened, the client had to clear their cache again manually. Not the ideal scenario. Clients got frustrated, and we wasted API operations and GCP bandwidth, constantly purging caches.

### Cache key is the key

Since we always read the domain's Workers KV data, we realized we could route requests and customize the cache key, appending things like the domain's ID and features that could affect the asset, like Polish. Today, our cache key is heavily customized to quickly reflect every client's change in our panel or API. By modifying the cache key using Workers KV's data, nobody needs to worry about clearing the cache anymore. As soon as Workers KV propagates the changes, the cache key also changes and we request and cache a fresh asset.

The easiest way to customize the cache key is to append `query params` to it. For example:

```
<pre><code class="language-javascript">
let cacheKey = `${request.url}?custom-cache-param-polish=lossy`
</code></pre>
```

Of course, you need to check the URL for existing parameters to determine which connector to use — `?` or `&` — and ensure you are using a unique identifier.

Then, you can use this new cache key to save the response with Cache API or Fetch — or both.

### Workers KV Cache

Workers KV operations are affordable, but the numbers can pile up when you trigger billions of reading operations daily.

Thanks to our cache key customization, we realized we could cache the Workers KV data with Cache API, saving on reading operations and possibly lowering the latency by avoiding multiple Workers KV GET requests per visitor. Since the cached response is now based on the request's URL combined with KV data, we no longer need to worry about caching stale content.

![](https://blog.cloudflare.com/content/images/2023/06/image3-16.png)![](https://blog.cloudflare.com/content/images/2023/06/image1-23.png)

However, unlike many applications, we can't cache Workers KV for extended periods. Kinsta's customers are constantly trying new features, changing Polish and Auto Minify settings, sometimes excluding pages or extensions from being cached, and they want to see their changes in production as soon as possible.

That's when we decided to microcache our Workers KV data — caching dynamic or constantly-changed content for a very short period of time, usually less than 60 seconds.

It’s pretty simple to implement your own Workers KV caching logic. For example:

```
<pre><code class="language-javascript">
const handleKVCache = async (event, myCustomDomain) => {
  // Try to get KV from cache first
  const cache = caches.default;
  let site_data = await cache.match( `https://${myCustomDomain}/some-string-ID-kv-data/` );

  // Valid KV cache match
  if (site_data && site_data.status === 200) {
    // ... modify your cached data if necessary, then return it
    return site_data;
  }

  // Invalid cache (expired, miss, etc), get data from KV namespace
  site_data = await KV_NAMESPACE.get(myCustomDomain.toLowerCase());

  // Cache valid KV responses with Cache API
  if (site_data) {
    let kvResponse = new Response(JSON.stringify(site_data), {status: 200});
    kvResponse.headers.set("Cache-Control", "public, s-maxage=30");
    event.waitUntil(cache.put(`https://${myCustomDomain}/some-string-ID-kv-data/`, kvResponse));
  }

  return site_data;
};
</code></pre>
```

(Optionally, you could use [FlareUtils' BetterKV](https://flareutils.pages.dev/betterkv/).)

At Kinsta, we implemented a 30-second cache TTL for Workers KV data, decreasing read operations by about 80%.

![](https://blog.cloudflare.com/content/images/2023/06/image4-14.png)

Read operations

### Learn more

Want to learn more about Workers and Workers KV? Check out the Cloudflare Workers KV developer [documentation](https://developers.cloudflare.com/workers/learning/how-kv-works/), or read our dedicated [homepage](https://www.cloudflare.com/en-gb/products/workers-kv/).

We protect
[entire corporate networks](https://www.cloudflare.com/network-services/),
help customers build
[Internet-scale applications efficiently](https://workers.cloudflare.com/),
accelerate ...