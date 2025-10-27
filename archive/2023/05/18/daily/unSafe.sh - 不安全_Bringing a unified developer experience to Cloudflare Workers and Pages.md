---
title: Bringing a unified developer experience to Cloudflare Workers and Pages
url: https://buaq.net/go-163802.html
source: unSafe.sh - 不安全
date: 2023-05-18
fetch_date: 2025-10-04T11:38:34.880284
---

# Bringing a unified developer experience to Cloudflare Workers and Pages

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

![](https://8aqnet.cdn.bcebos.com/674e985031f0f24fd00cd91e94b065bb.jpg)

Bringing a unified developer experience to Cloudflare Workers and Pages

Loading...
*2023-5-17 21:0:48
Author: [blog.cloudflare.com(查看原文)](/jump-163802.htm)
阅读量:35
收藏*

---

Loading...

* [![Nevi Shah](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/07/Screen-Shot-2021-07-26-at-3.28.33-PM.png)](https://blog.cloudflare.com/author/nevi/)
* [![Natalie Rogers](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/08/Screen-Shot-2022-08-18-at-12.00.51-PM-2.png)](https://blog.cloudflare.com/author/natalie/)

![Bringing a unified developer experience to Cloudflare Workers and Pages](https://blog.cloudflare.com/content/images/2023/05/image4-13.png)

Today, we’re thrilled to announce that Pages and Workers will be joining forces into one singular product experience!

We’ve all been there. In a surge of creativity, you visualize in your head the application you want to build so clearly with the pieces all fitting together – maybe a server side rendered frontend and an SQLite database for your backend. You head to your computer with the wheels spinning. You know you can build it, you just need the right tools. You log in to your Cloudflare dashboard, but then you’re faced with an incredibly difficult decision:

*Cloudflare Workers or Pages?*

Both seem so similar at a glance but also different in the details, so which one is going to make your idea become a reality? What if you choose the wrong one? What are the tradeoffs between the two? These are questions our users should never have to think about, but the reality is, they often do. Speaking with our wide community of users and customers, we hear it ourselves! Decision paralysis hits hard when choosing between Pages and Workers with both products made to build out serverless applications.

In short, we don’t want this for our users — especially when you’re on the verge of a great idea – no, a big idea. That’s why we’re excited to show off the first milestone towards bringing together the best of both beloved products — Workers and Pages into **one powerful development platform!** This is the beginning of the journey towards a shared fate between the two products, so we wanted to take the opportunity to tell you why we were doing this, what you can use today, and what’s next.

## More on the “why”

The relationship between Pages and Workers has always been intertwined. Up until today, we always looked at the two as siblings — each having their own distinct characteristics but both allowing their respective users to build rich and powerful applications. Each product targeted its own set of use cases.

Workers first started as a way to extend our [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/?ref=blog.cloudflare.com) and then expanded into a highly configurable general purpose compute platform. Pages first started as a static web hosting that expanded into [Jamstack](https://www.cloudflare.com/learning/performance/what-is-jamstack/?ref=blog.cloudflare.com) territory. Over time, Pages began acquiring more of Workers' powerful compute features, while Workers began adopting the rich developer features introduced by Pages. The lines between these two products blurred, making it difficult for our users to understand the differences and pick the right product for their application needs.

We know we can do better to help alleviate this decision paralysis and help you move fast throughout your development experience.

## Cool, but what do you mean?

Instead of being forced to make tradeoffs between these two products, we want to bring you the best of the both worlds: a single development platform that has both powerful compute and superfast static asset hosting – that seamlessly integrates with our portfolio of storage products like R2, Queues, D1, and others, and provides you with rich tooling like CI/CD, git-ops workflows, live previews, and flexible environment configurations.

### All the details in one place

Today, a lot of our developers use both Pages and Workers to build pieces of their applications. However, they still live in separate parts of the Cloudflare dashboard and don’t always translate from one to the other, making it difficult to combine and keep track of your app’s stack. While we’re still vision-boarding the look and feel, we’re planning a world where users have the ability to manage all of their applications in one central place.

![](https://blog.cloudflare.com/content/images/2023/05/image1-44.png)

No more scrambling all over the dashboard to find the pieces of your application – you’ll have all the information you need about a project right at your fingertips.

### Primitives

With Pages and Workers converging, we’ll also be redefining the concept of a “project” , introducing a new blank canvas of possibilities to plug and play. Within a project, you will be able to add (1) static assets, (2) serverless functions (Workers), (3) resources or (4) any combination of each.

To unlock the full potential of your application, we’re exploring project capabilities that allow you to auto-provision and directly integrate with resources like KV, Durable Objects, R2 and D1. With the possibility of all of these primitives on a project, more importantly, you'll be able to safely perform rollbacks and previews, as we'll keep the versions of your assets, functions and resources in sync with every deployment. No need to worry about any of them becoming stale on your next deployment.

![](https://blog.cloudflare.com/content/images/2023/05/image5-8.png)

### Deployments

One of Pages’ most notable qualities is its git-ops centered deployments. In our converged world, you’ll be able to optionally connect, build and deploy git repos that contain any combination of static assets, serverless functions and bindings to resources, as well as take advantage of the same high-performance CI system that exists in Pages today.

Like Pages, you will be able to preview deployments of your project with unique URLs protected by Cloudflare Access, available in your PRs or via Wrangler command. Because we know that great ideas take lots of vetting before the big release, we’ll also have a first-class concept of environments to enable testing in different setups.

### Local development

Arguably one of the most important parts to consider is our local development story in a post-converged world. This developer experience should be no different from how we’re converging the products. In the future, as you work with our Wrangler CLI, you can expect a unified and predictable set of commands to use on your project – e.g. a simple `wrangler dev` and `wrangler deploy`. Using a configuration file that applies to your entire project along with all of its components, you can have the confidence that your command will act on the entire project – not just pieces of it!

## What are the benefits?

With Workers and Pages converging, we’re not just unlocking all the golden developer features of each product into one development platform. We’re bringing all the performance, cost and load benefits too. This includes:

* **Super low latency** with globally distributed static assets and compute on our network that is just 50ms away from 95% of Internet-connected world-wide population.
* **Free egress** and also free static asset hosting.
* **Standards-based JavaScript runtime** with seamless compatibility across the packages and libraries you're already familiar with.

## Seamless migrations for all

If...