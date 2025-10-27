---
title: Cloudflare Snippets is now available in alpha
url: https://buaq.net/go-169774.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:34.152821
---

# Cloudflare Snippets is now available in alpha

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

![](https://8aqnet.cdn.bcebos.com/6ce9d9adcaa3e869baecf14128e5f931.jpg)

Cloudflare Snippets is now available in alpha

Loading...
*2023-6-21 21:0:50
Author: [blog.cloudflare.com(查看原文)](/jump-169774.htm)
阅读量:19
收藏*

---

Loading...

* [![Matt Bullock](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/09/headshot.jpeg)](https://blog.cloudflare.com/author/matt-bullock/)

Today we are excited to announce that [Cloudflare Snippets](https://blog.cloudflare.com/snippets-announcement/) is available in alpha. In the coming weeks we will be opening access to our waiting list.

![](https://blog.cloudflare.com/content/images/2023/06/image5-9.png)

### What are Snippets?

Over the past two years we have released a number of new rules products such as Transform Rules, Cache Rules, Origin Rules, Config Rules and Redirect Rules. These new products give more control to customers on how we process their traffic as it flows through our global network. The feedback on these products so far has been overwhelmingly positive. However, our customers still occasionally need the ability to do more than the out-of-the-box functionality allows. Not just adding an HTTP header - but performing some advanced calculation to create the output.

For these cases, Cloudflare Snippets comes to the rescue. Snippets are small pieces of user created JavaScript that are run by Cloudflare before your website, API or application is served to the user. If you're familiar with [Cloudflare Workers](https://developers.cloudflare.com/workers/), our robust developer platform, then you'll find Snippets to be a familiar addition. For those who are not, Snippets are designed to be easily created, tested, and deployed. Providing you with the ability to deploy your custom JavaScript Snippet to our [global network](https://www.cloudflare.com/en-gb/network/) in a matter of seconds.

While Snippets are built on top of the Workers Platform, they do have a number of differences. The first lies in how Snippets operate within the [Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/about/rulesets/) as a dedicated new phase, similar to [Transform Rules](https://blog.cloudflare.com/transform-rules-requests-transform-and-roll-out/) and [Cache Rules](https://blog.cloudflare.com/introducing-cache-rules/). This means that customers can select and execute a Snippet based on any Ruleset Engine filter. This gives customers the flexibility to run a Snippet on every request or apply it selectively based on various criteria they provide, such as specific bot scores, country of origin, or certain cookies.

Moreover, Snippets are cumulative in nature, allowing users to have multiple Snippets that execute if they meet the defined conditions. For instance, one Snippet could add an HTTP header and another rewrite the URL, both of which will be executed if their respective conditions are met.

Users now have the flexibility to choose between using a rule for simple, no-code-required tasks, such as adding a basic response Cookie header with Transform Rules, or writing a Cloudflare Snippet for more complex cookie functionality, such as dynamically changing the host or date within the cookie value. Snippets empower customers to get the job done quickly and effortlessly within the Cloudflare ecosystem, without incurring extra expenses (though a fair usage cap applies).

### The difference between Snippets and Workers

Another significant advantage is that Cloudflare Snippets are available across all plan levels at no extra cost. This empowers customers to migrate their simple workloads from legacy solutions like VCL to the Cloudflare platform, actively reducing their monthly expenses.

Whether you're on the Free, Pro, Business, or Enterprise plan, Snippets are at your disposal. Free plan users have access to five Snippets per zone, while Pro, Business, and Enterprise plans offer 10, 25, and 50 Snippets per zone, respectively.

In terms of resources, Cloudflare Snippets are lightweight compared to Workers. They have a maximum execution time of 5ms, a maximum memory of 2MB, and a total package size of 32KB. These limits are more than sufficient for common use cases like modifying HTTP headers, rewriting URLs, and routing traffic tasks that do not require the additional features and resources Cloudflare Workers has to offer.

Snippets also run before Workers; this means that users will be able to move simple logic out of a Cloudflare Worker into Snippets or use Cloudflare Workers and its features to further modify a request. The [Traffic Sequence UI](https://blog.cloudflare.com/traffic-sequence-which-product-runs-first/) has also been updated to incorporate Snippets allowing you to easily understand how all the products fit together and understand how HTTP requests flow between them.

![](https://blog.cloudflare.com/content/images/2023/06/image4-13.png)

### What can you build with Cloudflare Snippets?

Snippets allow customers to migrate their existing workloads to Cloudflare. For example, customers that wish to set a dynamic cookie on all of their responses for a percentage of requests can use the `math.random` function within their Snippet.

![](https://blog.cloudflare.com/content/images/2023/06/Screenshot-2023-06-12-at-15.40.26.png)

By leveraging the Ruleset Engine, we can improve the implementation by moving the set cookie logic to the rule instead of executing it on every response or handling it within a Snippet. For example if I only want to set this cookie on my shop subdomain and only for German or UK customers I can create the following rule.

![](https://blog.cloudflare.com/content/images/2023/06/pasted-image-0-1.png)

This approach ensures that the snippet will only execute when necessary, minimizing additional processing and reducing the complexity of the code required.

We are excited to see what other use cases Cloudflare Snippets unlock for our customers.

### Using Snippets

Snippets are located within the Rules section of the Cloudflare Dashboard. Here customers can use the UI to write, preview and deploy their first Snippet.

![](https://blog.cloudflare.com/content/images/2023/06/pasted-image-0--1-.png)

As with all Cloudflare products users can deploy their Snippets via the API and Terraform. Allowing users to easily incorporate Snippets within their CI/CD pipelines. The added benefit of using the Ruleset engine allows users to test their code on a subset of traffic. For example, by specifying your own office IP or secret header within the filter that will only trigger the Snippet if present. Finally we will be integrating Snippets within the [Account Request Tracer](https://developers.cloudflare.com/api/operations/account-request-tracer-request-trace) allowing users to easily identify all Rules that are executing on a specific request.

### How did we build Snippets?

During Developer Week, we discussed the process of [Building Cloudflare on Cloudflare](https://blog.cloudflare.com/building-cloudflare-on-cloudflare/), using our Cloudflare Workers developer platform to enhance our products in terms of speed, robustness, and ease of development. Snippets, the latest Cloudflare product, is built on top of Workers for Platforms.

![](https://blog.cloudflare.com/content/images/2023/06/pasted-image-0--2-.png)

A snippet is a piece of user-defined JavaScript that, upon creation, generates a unique Snippet ID. This Snippet ID is then associated with a user-defined rule created using the Rule Engine syntax. When a rule is created, a unique Rule ID is assigned to it. The Snippet ID and Rule ID are then lin...