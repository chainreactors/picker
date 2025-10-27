---
title: Cloudflare is deprecating Railgun
url: https://buaq.net/go-166814.html
source: unSafe.sh - 不安全
date: 2023-06-02
fetch_date: 2025-10-04T11:46:08.350812
---

# Cloudflare is deprecating Railgun

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

![](https://8aqnet.cdn.bcebos.com/297a9cc47cdb9587779801f584ad781a.jpg)

Cloudflare is deprecating Railgun

Loading...
*2023-6-1 21:0:39
Author: [blog.cloudflare.com(查看原文)](/jump-166814.htm)
阅读量:23
收藏*

---

Loading...

* [![Sam Rhea](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/Screenshot-2023-05-24-at-9.15.29-AM.png)](https://blog.cloudflare.com/author/sam/)

![Cloudflare is deprecating Railgun](https://blog.cloudflare.com/content/images/2023/05/image1-63.png)

Cloudflare will deprecate the [Railgun product](https://www.cloudflare.com/website-optimization/railgun/) on January 31, 2024. At that time, existing Railgun deployments and connections will stop functioning. Customers have the next eight months to migrate to a supported Cloudflare alternative which will vary based on use case.

Cloudflare first launched Railgun more than ten years ago. Since then, we have released several products in different areas that better address the problems that Railgun set out to solve. However, we shied away from the work to formally deprecate Railgun.

That reluctance led to Railgun stagnating and customers suffered the consequences. We did not invest time in better support for Railgun. Feature requests never moved. Maintenance work needed to occur and that stole resources away from improving the Railgun replacements. We allowed customers to deploy a zombie product and, starting with this deprecation, we are excited to correct that by helping teams move to significantly better alternatives that are now available in Cloudflare’s network.

We know that this will require migration effort from Railgun customers over the next eight months. We want to make that as smooth as possible. Today’s announcement features recommendations on how to choose a replacement, how to get started, and guidance on where you can reach us for help.

### What is Railgun?

Cloudflare’s reverse proxy secures and accelerates your applications by placing a Cloudflare data center in over 285+ cities between your infrastructure and your audience. Bad actors attempting to attack your applications hit our network first where products like our WAF and DDoS mitigation service stop them. Your visitors and users connect to our data centers where our cache can serve them content without the need to reach all the way back to your origin server.

For some customers, your infrastructure also runs on Cloudflare’s network in the form of Cloudflare Workers. Others maintain origin servers running on anything from a Raspberry Pi to a hyperscale public cloud. In those cases, Cloudflare needs to connect to that infrastructure to grab new content that our network can serve from our cache to your audience.

However, some content cannot be cached. Dynamically-generated or personalized pages can change for every visitor and every session. Cloudflare Railgun [aimed to solve](https://blog.cloudflare.com/railgun-in-the-real-world/) that by determining what was the minimum amount of content that changed and attempting to only send that difference in an efficient transfer - a form of [delta compression](https://blog.cloudflare.com/efficiently-compressing-dynamically-generated-53805/). By reducing the amount of content that needed to be sent to Cloudflare’s network, we could accelerate page loads for end users.

Railgun accomplishes this goal by running a piece of software inside the customer’s environment, the Railgun listener, and a corresponding service running in Cloudflare’s network, the Railgun sender. The pair establish a permanent TCP connection. The listener keeps track of the most recent version of a page that was requested. When a request arrives for a known page, the listener sends an HTTP request to the origin server, determines what content changed, and then compresses and sends only the delta to the sender in Cloudflare’s network.

### Why deprecate a product?

The last major release of Railgun took place eight years ago in 2015. However, products should not be deprecated just because active development stops. We believe that a company should retire a product only when:

* the maintenance impacts the ability to focus on solving new problems for customers and
* when improved alternatives exist for customers to adopt in replacement.

Hundreds of customers still use Railgun today and the service has continued to run over the last decade without too much involvement from our team. That relative stability deterred us from pushing customers to adopt newer technologies that solved the same problems. As a result, we kept Railgun in a sort of maintenance mode for the last few years.

### Why deprecate Railgun now?

Cloudflare’s network has evolved in the eight years since the last Railgun release. We deploy hardware and run services in more than 285 cities around the world, nearly [tripling](https://blog.cloudflare.com/panama-expands-cloudflare-network-to-50-countries/) the number of cities since Railgun was last updated. The hardware itself also advanced, becoming more [efficient and capable](https://blog.cloudflare.com/the-epyc-journey-continues-to-milan-in-cloudflares-11th-generation-edge-server/).

The software platform of Cloudflare’s network developed just as fast. Every data center in Cloudflare’s network can run every service that we provide to our customers. These services range from our traditional reverse proxy products to forward proxy services like Zero Trust to our compute and storage platform Cloudflare Workers. Supporting such a broad range of services requires a platform that can adapt to the requirements of the evolving needs of these products.

Maintaining Railgun, despite having better alternatives, creates a burden on our ability to continue investing in new solutions. Some of these tools that power Railgun are themselves approaching an end of life state. Others will likely present security risks that we are not comfortable accepting in the next few years.

We considered several options before deciding on deprecation. First, we could accept the consequences of inaction, leaving our network in a worse state and our Railgun customers in purgatory. Second, we could run Railgun on dedicated infrastructure and silo it from the rest of our network. However, that would violate our principle that every piece of hardware in Cloudflare runs every service.

Third, we could spin up a new engineering team and rebuild Railgun from scratch in a modern way. Doing so would take away from resources we could otherwise invest in newer technologies. We also believe that existing, newer products from Cloudflare solve the same problems that Railgun set out to address. Rebuilding Railgun would take away from our ability to keep shipping and would duplicate better features already released in other products. As a result, we have decided to deprecate Railgun.

### What alternatives are available?

Railgun addressed a number of problems for our customers at launch. Today, we have solutions available that solve the same range of challenges in significantly improved ways.

We do not have an exact like-for-like successor for Railgun. The solutions that solve the same set of problems have also evolved with our customers. Different use cases that customers deploy Railgun to address will map to different solutions available in Cloudflare today. We have broken out some of the most common reasons that customers used Railgun and where we recommend they consider migrating.

**“I use Railgun to maintain a persistent, secure connection to Cloudflare’s network without the need for a static publicly available IP address.”**
...