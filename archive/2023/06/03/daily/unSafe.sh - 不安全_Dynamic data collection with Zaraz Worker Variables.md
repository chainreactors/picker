---
title: Dynamic data collection with Zaraz Worker Variables
url: https://buaq.net/go-166993.html
source: unSafe.sh - 不安全
date: 2023-06-03
fetch_date: 2025-10-04T11:44:51.201355
---

# Dynamic data collection with Zaraz Worker Variables

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

![](https://8aqnet.cdn.bcebos.com/8b62c903901cbd3a2f4ed6a5a8fadbab.jpg)

Dynamic data collection with Zaraz Worker Variables

Loading...
*2023-6-2 21:0:37
Author: [blog.cloudflare.com(查看原文)](/jump-166993.htm)
阅读量:36
收藏*

---

Loading...

* [![Tom Klein](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/unnamed--1-.jpg)](https://blog.cloudflare.com/author/tom-klein/)
* [![Lucas Kostka](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/Lucas-Kostka.jpg)](https://blog.cloudflare.com/author/lucas-kostka/)

![](https://blog.cloudflare.com/content/images/2023/06/image7-1.png)

## Bringing dynamic data to the server

Since its inception, Cloudflare Zaraz, the server-side third-party manager built for speed, privacy and security, has strived to offer a way for marketers and developers alike to get the data they need to understand their user journeys, without compromising on page performance. Cloudflare Zaraz makes it easy to transition from traditional client-side data collection based on marketing pixels in users’ browsers, to a server-side paradigm that shares events with vendors from the edge.

When implementing data collection on websites or mobile applications, analysts and digital marketers usually first define the set of interactions and attributes they want to measure, formalizing those requirements along technical specifications in a central document (“tagging plan”). Developers will later implement the required code to make those attributes available for the third party manager to pick it up. For instance, an analyst may want to analyze page views based on an internal name instead of the page title or page pathname. They would therefore define an example “page name” attribute that would need to be made available in the context of the page, by the developer. From there, the analyst would configure the tag management system to pick the attribute’s value before dispatching it to the analytics tool.

Yet, while the above flow works fine in theory, the reality is that analytics data comes from multiple sources, in multiple formats, that do not always fit the initially formulated requirements.

The industry accepted solution, such as Google Tag Manager’s “Custom JavaScript variables” or Adobe’s “Custom Code Data Elements”, was to offer a way for users to dynamically invoke custom JavaScript functions on the client, allowing them to perform cleaning (like removing [PII](https://www.cloudflare.com/learning/privacy/what-is-pii/) data from the payload before sending it to Google Analytics), transformations (extracting specific product attributes out of a product array) or enrichment (making an API call to grab the current user’s CRM id to stitch user sessions in your analytics tool) to the data before dispatch by the third-party manager.

![](https://blog.cloudflare.com/content/images/2023/06/image5.png)

*Example of Google Tag Manager custom javascript variable that aggregates individual items prices from a javascript array of product information.*

Having the ability to run custom JavaScript is a powerful feature that offers a lot of flexibility and yet, was a missing part of Cloudflare Zaraz. While some workarounds existed, it did not really fit with Cloudflare Zaraz’s objective of high-performance. We needed a way for our users to provide custom code to be executed fast, server-side. Quite fast, it was clear that Cloudflare Workers, the globally distributed serverless V8-based JavaScript runtime was the solution.

## Worker Variables to the rescue

Cloudflare Zaraz Worker Variables is powered by Cloudflare Workers, our platform for running custom code on the edge, but let’s take a step back and work through how Cloudflare Zaraz is implemented.

When making a request to a website proxied by Cloudflare, a few things will run before making it to your origin. This includes the [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/), [DDoS mitigation](https://www.cloudflare.com/learning/ddos/ddos-mitigation/), [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/), and also something called First-Party Workers.

These First-Party Workers are Cloudflare Workers with special permissions. Cloudflare Zaraz is one of them. Our Worker is built in a way that allows variables to be replaced by their contents. Those variables can be used in places where you would be reusing hardcoded text, to make it easier to make changes to all places where it would be used. For example, the name of your site, a secret key, etc:

![](https://blog.cloudflare.com/content/images/2023/06/download.png)

These variables can then be used in any of Cloudflare Zaraz’s components, by selecting them right from the dashboard as a property, or as part of a component’s settings:

![](https://blog.cloudflare.com/content/images/2023/06/download--1-.png)

When using a Worker Variable, instead of replacing your variable with a hardcoded string, we instead execute the custom code hosted in your own Cloudflare Worker that you have associated with the variable. The response of which is then being used as the variable’s value. Calling one worker from within the Cloudflare Zaraz Worker is done using [Dynamic Dispatch](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/get-started/dynamic-dispatch/).

In our Cloudflare Zaraz Worker, calling Dynamic Dispatch is very similar to how your regular, everyday worker might do it. From having a binding in our wrangler.toml:

```
...
unsafe.bindings = [
  { name = "DISPATCHER", type = "dynamic_dispatch", id_prefix = "", first_party = true },
]
```

To having our code responsible for variables actually call your worker:

```
if (variable.type === 'worker') {
  // Get the persistent ID of the Worker
  const mutableId = variable.value.mutableId
  // Get the binding for the specific Worker
  const workerBinding = context.env.DISPATCHER.get(mutableId)
  ...
  // Execute the Worker and return the response
  const workerResponse = await workerBinding.fetch(
    new Request(String(url || context.url || 'http://unknown')),
    {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(payload),
    }
  )
  ...
  return workerResponse
}
```

## Benefits of Cloudflare Zaraz Worker Variables

Cloudflare Workers is a world-class solution to build complex applications. Together with Cloudflare Zaraz, we feel that makes it the ideal platform to orchestrate your data workflows:

**Build with context:**  Cloudflare Zaraz automatically shares the context as part of the call to the Cloudflare Zaraz Worker, allowing you to use that data as input to your functions. Cloudflare Zaraz offers a Web API which customers can use to track important events in their users' journeys. Along with the [Web API](https://developers.cloudflare.com/zaraz/web-api/), Zaraz offers ways for users to define custom attributes, called “Track properties” and “Variables”, that allow our customers to provide additional context to the event getting sent to a vendor. The Cloudflare Zaraz context holds every attribute that was tracked by Cloudflare Zaraz as part of the current visitor session along with other generic attributes like the visitors’ device cookies for instance.

**Speed:** In comparison to manually calling a worker from client-side JavaScript, this saves the roundtrip to the Worker’s HTTP endpoint and gives you access to Cloudflare Zaraz properties, allowing you to work with client-side data right from the edge.
...