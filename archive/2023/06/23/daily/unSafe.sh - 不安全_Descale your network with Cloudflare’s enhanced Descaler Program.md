---
title: Descale your network with Cloudflare’s enhanced Descaler Program
url: https://buaq.net/go-169868.html
source: unSafe.sh - 不安全
date: 2023-06-23
fetch_date: 2025-10-04T11:44:31.862641
---

# Descale your network with Cloudflare’s enhanced Descaler Program

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

![](https://8aqnet.cdn.bcebos.com/6e41397f916cbbea2c80a21383f1cbcc.jpg)

Descale your network with Cloudflare’s enhanced Descaler Program

Loading...
*2023-6-22 21:0:38
Author: [blog.cloudflare.com(查看原文)](/jump-169868.htm)
阅读量:17
收藏*

---

Loading...

* [![Corey Mahan](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/01/coreymahan.png)](https://blog.cloudflare.com/author/corey-mahan/)
* [![Denis Kieft](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/cf_headshot_denis_small-copy-square-2.jpg)](https://blog.cloudflare.com/author/denis/)

![Descale your network with Cloudflare’s enhanced Descaler Program](https://blog.cloudflare.com/content/images/2023/06/image2-25.png)

Speed matters, especially when it comes to exiting a slower service and transitioning to a new one. Back in March, 2023, we announced the [Descaler Program](https://blog.cloudflare.com/descaler-program/), a frictionless path to migrate existing Zscaler customers to Cloudflare One. This program makes it easy for customers to make the switch to a [faster](https://blog.cloudflare.com/network-performance-update-cio-edition/), simpler, and more agile foundation for security and network transformation with Cloudflare.

Through repeated engagements with customers of all sizes, we've improved the Descaler tooling to allow Zscaler to Cloudflare configuration migrations to be completed in hours, not days. This accelerated transition has helped organizations meet migration deadlines and eliminate countless hours of manual migration effort without skipping a beat. Today we’re excited to share more stories from customers and the amount of time it took them to ‘descale’.

### Cloudflare One and the Descaler Program

As a quick recap, [Cloudflare One](https://www.cloudflare.com/cloudflare-one/) is our [Secure Access Service Edge (SASE)](https://www.cloudflare.com/learning/access-management/what-is-sase/) platform that combines network connectivity services with [Zero Trust security services](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) on one of the fastest, most resilient and most composable global networks. The platform dynamically connects users to enterprise resources, with identity-based security controls delivered close to users, wherever they are.

At its core, the Descaler Program helps derisk change. It’s designed to be simple and straightforward, with resources to ensure a smooth transition and supporting technology to ensure the migration achieves your organization's goals. The magic of this process is in the technology and its simplicity. Following extract, transform, and load best practices, using supported and documented [API calls](https://www.cloudflare.com/learning/security/api/what-is-api-call/) to your current account, the Descaler toolkit will export your current configuration and settings and transform them to be Cloudflare One-compatible before migrating into a new Cloudflare One account.

A question almost every customer asked was “so, how long is this going to take?”. The answer? As soon as you can meet with the Cloudflare team.

### Migrate in minutes, not months

The speed at which customers are able to move from Zscaler ZIA to [Cloudflare Gateway](https://www.cloudflare.com/products/zero-trust/gateway/) continually gets faster. As the title of this blog post implies, it usually takes more time to set up a meeting with the right technical administrators than to migrate settings, configurations, lists, policies and more to Cloudflare. We’ve seen this time continue to get faster through Descaler engagements. But it wasn’t this way from the onset. To be the fastest at everything we do, it means iterating and learning from customers to find the best solution possible. Here are three customer stories of doing just that.

### Customer migration time: seven days | “Is there a summary available?”

A UK ecommerce giant with 7,500 employees sought a solution that could provide them with faster, safer access to corporate resources and SaaS apps while eliminating the exorbitant costs associated with Zscaler. With Descaler, they achieved this goal in just one week. Our streamlined migration process ensured minimal disruption to their operations, empowering them to seamlessly transition to Cloudflare One before a tight renewal deadline. By reducing the time and cost involved in the migration, they were able to focus on what matters most—driving their business forward.

To better communicate what is available to be moved into Cloudflare Gateway, the team was curious on what objects they had active in their account in a simplified view. Based on this feedback, the Cloudflare team added the option for the Descaler tool to provide a summary of what will be moved to Cloudflare, as shown below.

![](https://blog.cloudflare.com/content/images/2023/06/image3-20.png)

Sample Descaler summary output

### Customer migration time: two days | Lots and lots of lists

For a US-based Fortune 100 oil and gas company with nearly 20,000 employees, the key priority was to streamline their application, network, and security services. With Descaler, they were able to move over more of their security service and achieved this objective in just under two days. Cloudflare’s intuitive dashboard provided them with a single pane of glass to manage all their services efficiently, simplifying their operations and enhancing their overall productivity. The speed at which Descaler facilitated their migration allowed them to seamlessly consolidate their services, unlocking new levels of efficiency and cost savings.

The team had also put a significant amount of effort into curating lists of IP addresses, hostnames, and URLs of sites and services used in their filtering policies. These thousands of items were transformed and loaded into their new Cloudflare production account almost instantly. With some minor testing, they were able to save hours of copying and retain their security intelligence.

### Customer migration time: 24 hours | “What about Terraform?”

Recently a prominent Australian based telecommunications company that owns one of the countries largest fiber networks prioritized employee Internet security and the prevention of malware attacks. Descaler played a crucial role in their quest to protect users and block malware, with a configuration migration time of less than 24 hours. By migrating to Cloudflare One, they ensured their employees had access to robust security features and comprehensive protection, bolstering their defense against potential threats.

Having [Terraform](https://developers.cloudflare.com/cloudflare-one/api-terraform/access-with-terraform/) output was table stakes for this organization and many others the team interacted with. Terraform is a tool for building, changing, and versioning infrastructure, and provides components and documentation for building Cloudflare resources. Without the ability to manage their Cloudflare configuration as infrastructure-as-code, it meant breaking their normal workflows. From this feedback the Descaler team added the option to export the configuration in a shareable Terraform file which was then shared with the customer.

![](https://blog.cloudflare.com/content/images/2023/06/image4-18.png)

### How to get started

Migration times are still getting faster and the overall process even smoother due to iterations like the ones mentioned above. We’re excited to invite new customers to take advantage of the program by signing up using the link below. From there, th...