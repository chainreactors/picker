---
title: Speeding up your (WordPress) website is a few clicks away
url: https://buaq.net/go-169867.html
source: unSafe.sh - 不安全
date: 2023-06-23
fetch_date: 2025-10-04T11:44:30.416887
---

# Speeding up your (WordPress) website is a few clicks away

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

![](https://8aqnet.cdn.bcebos.com/e7f76b370f9e092c91c779b6494c09fb.jpg)

Speeding up your (WordPress) website is a few clicks away

Loading...
*2023-6-22 21:0:58
Author: [blog.cloudflare.com(查看原文)](/jump-169867.htm)
阅读量:17
收藏*

---

Loading...

* [![Alex Krivit](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2018/08/RE0BQ6EF_400x400.jpg)](https://blog.cloudflare.com/author/alex/)
* [![Patrick Meenan (Guest Author)](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2018/08/PatPerfCalendar.jpg)](https://blog.cloudflare.com/author/patrick-meenan/)

![Speeding up your (WordPress) website is a few clicks away](https://blog.cloudflare.com/content/images/2023/06/image1-31.png)

Every day, website visitors spend far too much time waiting for websites to load in their browsers. This waiting is partially due to browsers not knowing which resources are critically important so they can prioritize them ahead of less-critical resources. In this blog we will outline how millions of websites across the Internet can improve their performance by specifying which critical content loads first with Cloudflare Workers and what Cloudflare will do to make this easier by default in the future.

Popular Content Management Systems (CMS) like WordPress have made attempts to influence website resource priority, for example through techniques like [lazy loading images](https://make.wordpress.org/core/2020/07/14/lazy-loading-images-in-5-5/). When done correctly, the results are magical. Performance is optimized between the CMS and browser without needing to implement any changes or coding new prioritization strategies. However, we’ve seen that these default priorities have opportunities to improve greatly.

In this co-authored blog with Google’s Patrick Meenan we will explain where the opportunities exist to improve website performance, how to check if a specific site can improve performance, and provide a small JavaScript snippet which can be used with Cloudflare Workers to do this optimization for you.

### What happens when a browser receives the response?

Before we dive into where the opportunities are to [improve website performance](https://www.cloudflare.com/learning/performance/speed-up-a-website/), let’s take a step back to understand how browsers load website assets by default.

After the browser sends a [HTTP request](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) to a server, it receives a HTTP response containing information like status codes, headers, and the requested content. The browser carefully analyzes the response's status code and response headers to ensure proper handling of the content.

Next, the browser processes the content itself. For HTML responses, the browser extracts important information from the <head> section of the HTML, such as the page title, stylesheets, and scripts. Once this information is parsed, the browser moves on to the response <body> which has the actual page content. During this stage, the browser begins to present the webpage to the visitor.

![](https://blog.cloudflare.com/content/images/2023/06/image2-28.png)

If the response includes additional 3rd party resources like CSS, JavaScript, or other content, the browser may need to fetch and integrate them into the webpage. Typically, browsers like Google Chrome delay loading images until after the resources in the HTML <head> have loaded. This is also known as “[blocking](https://developer.chrome.com/en/docs/lighthouse/performance/render-blocking-resources/)” the render of the webpage. However, developers can override this blocking behavior using [fetch priority](https://web.dev/fetch-priority/) or other methods to boost other content’s priority in the browser. By adjusting an important image's fetch priority, it can be loaded earlier, which can lead to significant improvements in crucial performance metrics like LCP ([Largest Contentful Paint](https://web.dev/optimize-lcp/#:~:text=LCP%20measures%20the%20time%20from%20when%20the%20user%20initiates%20loading%20the%20page%20until%20the%20largest%20image)).

Images are so central to web pages that they have become an essential element in measuring website performance from [Core Web Vitals](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/). LCP measures the time it takes for the largest visible element, often an image, to be fully rendered on the screen. Optimizing the loading of critical images (like [LCP images](https://web.dev/optimize-lcp/#:~:text=LCP%20measures%20the%20time%20from%20when%20the%20user%20initiates%20loading%20the%20page%20until%20the%20largest%20image)) can greatly enhance performance, improving the overall user experience and page performance.

But here's the challenge – a browser may not know which images are the most important for the visitor experience (like the LCP image) until rendering begins. If the developer can identify the LCP image or critical elements before it reaches the browser, its priority can be increased at the server to boost website performance instead of waiting for the browser to naturally discover the critical images.

In our Smart Hints [blog](https://blog.cloudflare.com/smart-hints), we describe how Cloudflare will soon be able to automatically prioritize content on behalf of website developers, but what happens if there’s a need to optimize the priority of the images right now? How do you know if a website is in a suboptimal state and what can you do to improve?

Using Cloudflare, developers should be able to improve image performance with heuristics that identify likely-important images before the browser parses them so these images can have increased priority and be loaded sooner.

### Identifying Image Priority opportunities

Just increasing the fetch priority of all images won't help if they are lazy-loaded or not critical/LCP images. [Lazy-loading](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/) is a method that developers use to generally improve the initial load of a webpage if it includes numerous out-of-view elements. For example, on Instagram, when you continually scroll down the application to see more images, it would only make sense to load those images when the user arrives at them otherwise the performance of the page load would be needlessly delayed by the browser eagerly loading these out-of-view images. Instead the highest priority should be given to the LCP image in the viewport to improve performance.

So developers are left in a situation where they need to know which images are on users' screens/viewports to increase their priority and which are off their screens to lazy-load them.

Recently, we’ve seen attempts to influence image priority on behalf of developers. For example, by [default](https://make.wordpress.org/core/2020/07/14/lazy-loading-images-in-5-5/), in WordPress 5.5 all images with an [IMG tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) and [aspect ratios](https://en.wikipedia.org/wiki/Aspect_ratio_%28image%29) were directed to be lazy-loaded. While there are plugins and other methods WordPress developers can use to boost the priority of LCP images, lazy-loading all images in a default manner and not knowing which are LCP images can cause artificial performance delays in website performance (they’re [working on this](https://make.wordpress.org/core/2023/05/02/proposal-for-enhancing-lcp-image-performance-with-fetchpriority/) though, and have partially resolved this for [block themes](https://make.w...