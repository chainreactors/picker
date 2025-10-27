---
title: Smart Hints make code-free performance simple
url: https://buaq.net/go-169404.html
source: unSafe.sh - 不安全
date: 2023-06-20
fetch_date: 2025-10-04T11:47:05.185822
---

# Smart Hints make code-free performance simple

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

![](https://8aqnet.cdn.bcebos.com/05779b2903a642f7bce9bf423f051cd7.jpg)

Smart Hints make code-free performance simple

Loading...
*2023-6-19 21:0:38
Author: [blog.cloudflare.com(查看原文)](/jump-169404.htm)
阅读量:13
收藏*

---

Loading...

* [![Alex Krivit](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2018/08/RE0BQ6EF_400x400.jpg)](https://blog.cloudflare.com/author/alex/)

![Smart Hints make code-free performance simple](https://blog.cloudflare.com/content/images/2023/06/image4-3.png)

Today, we’re excited to announce how we’re making Early Hints and [Fetch Priorities](https://web.dev/fetch-priority/) automatic using the power of Cloudflare’s network. Almost a [year ago](https://blog.cloudflare.com/early-hints-performance/) we launched [Early Hints](https://blog.cloudflare.com/early-hints/). Early Hints are a method that allows web servers to asynchronously send instructions to the browser whilst the web server is getting the full response ready. This gives proactive suggestions to the browser on how to load the webpage faster for the visitor rather than idly waiting to receive the full webpage response.

In initial lab experiments, we observed page load improvements exceeding 30%. Since then, we have sent about two-trillion hints on behalf of over 150,000 websites using the product.

In order to effectively use Early Hints on a website, HTTP link headers or HTML link elements must be configured to specify which assets should be preloaded or which third-party servers should be preconnected. Making these decisions requires understanding how your website interacts with browsers, and identifying render-blocking assets to hint on without implementing prioritization strategies that [saturate network bandwidth](https://blog.cloudflare.com/early-hints-performance/#:~:text=It%E2%80%99s%20quite%20possible,mobile%20connection%20settings.) on non-critical assets (i.e. you can’t just Early Hint everything and expect good results).

For users who possess this knowledge and can configure Early Hints at the origin (or via a Worker), it works seamlessly. However, for users who lack access to their origin server (e.g. SaaS platforms), or are unsure about the optimal assets to preload/prioritize, or simply prefer to focus on building their own application, the question arises: "*As an intermediary server, shouldn't Cloudflare know the best way to prioritize my website for performance*?"

The answer is **yes**, which is why we’re excited to start talking about how Smart Hints will determine the best priority for web assets without developers needing to configure anything. If you’re interested in helping us beta test this feature, you can sign up [here](https://dash.cloudflare.com?to=/:account/:zone/speed/optimization) and we will contact you with further instructions on helping us test Smart Hints later this year.

### Background

When you visit a webpage, your browser is actually requesting numerous individual resources from the server. These resources include everything from visible elements like images, text, and videos, to the behind-the-scenes logic (JavaScript, etc.) that powers the website analytics, functionality, and more. The order in which these resources are loaded by the browser plays a crucial role in determining how quickly users can view and interact with the page.

![](https://blog.cloudflare.com/content/images/2023/06/image3-2.png)

When your browser receives a response from the server, it parses the HTML response sequentially, from start to finish.When the HTML response arrives in the browser, it is split into two parts: the `<head>` and the `<body>`.

The `<head>` section appears at the beginning of the HTML response and contains essential elements like stylesheets, scripts, and other instructions for the browser. Stylesheets define how the page should look, while scripts provide the necessary logic for interactive features and functionality.1

While stylesheets are important to load quickly as browsers will wait for them to know how to display content to the visitor, scripts are interesting because they can behave differently based on instructions provided to the browser. If a script lacks specific instructions (defer/async/inline for example), it can become a "blocking" resource. When the browser encounters a blocking script resource, it pauses processing the webpage and waits until the script is fully loaded and completely executed. This ensures that the script's functionality is available for the visitor to use. However, this blocking behavior can delay the display of content to the user, as the browser needs to wait for the script to finish before proceeding further.

Until the browser reaches the `<body>` section of the document, there is nothing visible to the visitor. That's why it's crucial to optimize the loading process of the `<head>` section as much as possible. By minimizing the time it takes for stylesheets and blocking scripts to load, the browser can start rendering the page content sooner, allowing visitors to see and interact with the webpage faster.

Achieving optimal web performance can be a complex challenge. While browsers are generally in charge of determining the order of loading different resources it needs to build a page, there have been a variety of tools that have been released recently ([Early Hints](https://blog.cloudflare.com/early-hints-performance/), [Fetch Priority](https://web.dev/fetch-priority/), [Lazy-Loadin](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)g, [H2](https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/) Priorities) to help developers specify unique resource priority for browsers to improve website load performance. Although these tools and methods for specifying resource priority can be effective, they require implementation and testing to make sure they are implemented correctly.

### Prioritization Tools

Two methods that have gained a lot of popularity for improving website performance have been Early Hints and Fetch Priorities. These tools help give browsers information about how it should load resources in the correct order to improve performance of critical resources.

*Early Hints*

Early Hints allow the server to provide some information to the client before the final response is available.

When a client sends a request to a server, the server can respond with an "early hint" to provide a clue about the final response. This early hint is a separate response that includes headers related to the final response, such as important static objects that can be fetched early, and links to where to get related resources.

![](https://blog.cloudflare.com/content/images/2023/06/image1-4.png)

The purpose of Early Hints is to allow the client to start processing the received information while waiting for the final response. The client can use the Early Hint to initiate early resource preloading, and preconnecting to servers that will have information for the final response, which can lead to faster page load times.

*Fetch Priority*

Another powerful tool in optimizing resource loading is Fetch Priorities, previously known as Priority Hints.

When analyzing a webpage, web browsers often prioritize the fetching of resources such as scripts and stylesheets to optimize the download sequence and efficiently use bandwidth. The priorities assigned to these resources are determined by browsers based on factors like resource type, placement within the webpage, and its location within the HTML response. For instance, images within the visible area for the visitor sho...