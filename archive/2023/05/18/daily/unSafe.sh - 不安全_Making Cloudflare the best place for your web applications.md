---
title: Making Cloudflare the best place for your web applications
url: https://buaq.net/go-163804.html
source: unSafe.sh - 不安全
date: 2023-05-18
fetch_date: 2025-10-04T11:38:36.063478
---

# Making Cloudflare the best place for your web applications

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

![](https://8aqnet.cdn.bcebos.com/c6a327b07ea2455a66275f4cd21c67b2.jpg)

Making Cloudflare the best place for your web applications

Loading...
*2023-5-17 21:0:19
Author: [blog.cloudflare.com(查看原文)](/jump-163804.htm)
阅读量:35
收藏*

---

Loading...

* [![Igor Minar](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/10/FJe_qxl8_400x400.jpeg)](https://blog.cloudflare.com/author/igor/)

![](https://blog.cloudflare.com/content/images/2023/05/image1-38.png)

Hey web developers! We are about to shake things up a bit here at Cloudflare and wanted to give you a heads-up, so that you know what we are doing and where we are going. You might know Cloudflare as one of the best places to come to when you need to protect, speed up, or scale your web application, but increasingly Cloudflare is also becoming the best place to *deploy and run* your application!

**Why deploy your application to Cloudflare?** Two simple reasons. First, it removes lots of hassle of managing many separate systems and allows you to develop, deploy, monitor, and tune your application all in one place. Second, by deploying to Cloudflare directly, there is so much more we can do to optimize your application and get it to the hands, ears, or eyes of your users more quickly and smoothly.

**So what’s changing?** Quite a bit, actually. I’m not going to bore you with rehashing all the details as my most-awesome colleagues have written separate blog posts with all the details, but here is a high level rundown.

### Cloudflare Workers + Pages = awesome development platform

Cloudflare Pages and Workers are merging into a single unified development and application hosting platform that offers:

* Super low latency globally: your static assets and compute are less than [50ms away from 95% of the world’s Internet-connected population](https://www.cloudflare.com/network/?ref=blog.cloudflare.com).
* Free egress including free static asset hosting.
* Standards-based JavaScript and WASM runtime that already serves over 10 million requests per second at peak globally.
* Access to powerful features like [R2](https://www.cloudflare.com/products/r2/?ref=blog.cloudflare.com) (object storage with an S3-compatible API), low-latency globally replicated [KV storage](https://www.cloudflare.com/products/workers-kv/?ref=blog.cloudflare.com), [Queues](https://developers.cloudflare.com/queues/?ref=blog.cloudflare.com), [D1 database](https://developers.cloudflare.com/d1/?ref=blog.cloudflare.com), and many more.
* Support for GitOps and CI/CD workflows and preview environments to boost development velocity.
* … and so much more.

While mathematically proven to be wrong, we stubbornly believe that 1+1=3, and in this case this translates to Cloudflare Pages + Workers = way more than the sum of the parts. In fact, it’s an awesome foundation for one of a kind development platform that we are thrilled to be building for you.

We started this product convergence journey a few quarters ago, and early on agreed upon not leaving any of the existing applications behind. Instead, we’ll be bringing them over to this new world. Today we are ready to start sharing the incremental results, with so much more to come over the upcoming quarters. Want to know more? My colleague Nevi posted lots of spicy details in [her blog post](https://blog.cloudflare.com/pages-and-workers-are-converging-into-one-experience).

### Smart Placement for Workers takes us beyond the edge!

Smart placement is, to put it simply, revolutionary for Cloudflare. It enables a new compute paradigm on our platform, unmatched by any other application hosting providers today. Do you have a typical full-stack application built with one of the many popular web frameworks? This feature is for you! And it works with both Workers and Pages!

While previously we always executed all applications at the “edge” of our global network — meaning, as close to the user as possible. With smart placement, we intelligently determine the best location within our network where the compute (your application) should run. We do this by observing your application’s behavior and what other network resources or endpoints the application interacts with. We then transparently spawn your application at an optimal location, usually close to where your data is stored, and route the incoming requests via our network to this location.

Smart placement enables applications to run near to the data these applications need to get stuff done. This is especially powerful for applications that interact with databases, object stores, or other backend endpoints, especially if these are centralized and not globally distributed.

Your user or clients requests still enter our lightning fast network in one of our 285+ datacenters in the world, close to their current location, but instead of spawning the application right there, we route the request to the most optimal datacenter, the one that is near the data or backend system the application talks to.

This doesn’t mean that compute at the edge is not cool anymore! It is! There are still many use-cases where running your application at the edge makes sense, and smart placement will determine this scenario and keep the application at the edge if that’s the right place for it to be. A/B testing, localization, asset serving, and others are use-cases that should almost always happen at the edge.

Sounds interesting? Check out this [visual demo](https://smart-placement-demo.pages.dev/?ref=blog.cloudflare.com) and read up on [Smart Placement in a blog post from my colleague Tanushree](https://blog.cloudflare.com/announcing-workers-smart-placement/) to get started.

### Develop locally or in the browser!

We continue to deliver on our goal to build the best development environment integrated directly into our lightning fast and globally distributed application platform. We’re launching [Wrangler](https://developers.cloudflare.com/workers/get-started/guide/?ref=blog.cloudflare.com#1-start-a-new-project-with-wrangler-the-workers-cli) v3, with complete support for local-by-default development workflow. Powered by the open-source Cloudflare Workers JavaScript runtime — [workerd](https://github.com/cloudflare/workerd?ref=blog.cloudflare.com#readme), this change reduces development server startup time by 10x and script reload times by 60x — boosting your productivity and keeping you in the flow longer.

In the dashboard, we're introducing an upgraded and far more powerful online editor powered by [VSCode](https://code.visualstudio.com/?ref=blog.cloudflare.com) – you can now finally edit multiple JavaScript modules in your browser, get an accurate edge preview of your code, friendly error pages, and type checking!

Finally, in both our dashboard editor and Wrangler, we've updated our workerd-customized [Chrome DevTools](https://developer.chrome.com/docs/devtools/?ref=blog.cloudflare.com) to the latest version, providing even greater debugging and profiling capabilities, wherever you choose to work.

This is just the first wave of improvements to our development tooling space, you’ll see us iterating in this space over the next few quarters, but in the meantime, check out in-depth posts from Adam, Brendan, and Samuel with [all the Wrangler v3 details](https://blog.cloudflare.com/wrangler3) and [VSCode and dash editor improvements](https://blog.cloudflare.com/improved-quick-edit).

### Increased memory, CPU, and application size limits and simplified pricing!

In the age of AI, WASM, and powerful full-stack applications, we’ve noticed that developers are hitting our current re...