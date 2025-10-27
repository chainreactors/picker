---
title: Understanding end user-connectivity and performance with Digital Experience Monitoring, now available in beta
url: https://buaq.net/go-169869.html
source: unSafe.sh - 不安全
date: 2023-06-23
fetch_date: 2025-10-04T11:44:33.671830
---

# Understanding end user-connectivity and performance with Digital Experience Monitoring, now available in beta

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

![](https://8aqnet.cdn.bcebos.com/c0d920ee0a4f6d32b823d1acd52b27a2.jpg)

Understanding end user-connectivity and performance with Digital Experience Monitoring, now available in beta

Loading...
*2023-6-22 21:0:28
Author: [blog.cloudflare.com(查看原文)](/jump-169869.htm)
阅读量:13
收藏*

---

Loading...

* [![Shruti Pokalori Nejad](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/_tmp_mini_magick20230419-40-15akzv2.jpg)](https://blog.cloudflare.com/author/shruti/)

![Understanding end user-connectivity and performance with Digital Experience Monitoring. Now available in beta.](https://blog.cloudflare.com/content/images/2023/06/image1-26.png)

Organizations that replace their corporate network and security appliances with a cloud-based solution trust that provider with how their employees work each and every day. Cloudflare One, our comprehensive [Secure Access Service Edge (SASE)](https://www.cloudflare.com/learning/access-management/what-is-sase/) offering, helps more than 10,000 organizations deploy a remote access and Internet security solution that is [faster than industry competitors](https://blog.cloudflare.com/network-performance-update-cio-edition/). Starting today, administrators can measure that experience on their own and hold us accountable to that standard.

Cloudflare’s [Digital Experience Monitoring](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/) (DEX) product gives teams of any size the same toolkit that we use to measure our own global network that powers nearly one-fourth of the Internet each day. Customers of Cloudflare One can now measure the experience that their team members have connecting to the Internet - whether they need that data for troubleshooting, evaluating carrier and ISP performance, or just understanding how their employees work.

We are excited to share today that DEX is now in open beta for all Cloudflare One customers. Administrators can begin running tests and evaluating network performance with any device enrolled using the Cloudflare One agent. Today’s announcement opens up these tools to every customer, but we are just getting started - we want your feedback to help us continue to improve the experience as we build more observability into Cloudflare’s SASE solution.

### Monitor performance & availability of public or private applications with Synthetic Application Monitoring

Picture this: you're at the helm of a diverse team, using Google Mail as their main communication hub. When everyone worked from the same office, spotting a slowdown with Google Mail or its provider was relatively straightforward. But in today's remote environment, ensuring the consistent performance of such a critical resource can become a labyrinthine task.

Synthetic Application Monitoring shines a light through this maze. With the ability to schedule HTTP GET tests that target Gmail at specified intervals, you're not merely monitoring performance — you're safeguarding your team's access to crucial communication lines, irrespective of their global locations.

![](https://blog.cloudflare.com/content/images/2023/06/image11-2.png)

What sets Synthetic Application Monitoring apart isn't just its user-friendly setup, but the powerful insights derived from Cloudflare's extensive network. With our network's global reach, you can track response time averages from various locations, painting a realistic picture of your application's performance as experienced by your users worldwide.

![](https://blog.cloudflare.com/content/images/2023/06/Screenshot-2023-06-22-at-11.41.44.png)![](https://blog.cloudflare.com/content/images/2023/06/image12.png)

Test results visualize resource fetch times, exemplifying the unique strengths of Cloudflare's expansive network. The HTTP GET tests harness the speed and reliability of the nearest data center in our network, providing an accurate reflection of your users' experiences. This graph translates raw data into an easy-to-read timeline, helping you identify trends, spot anomalies, and optimize application performance using the insights garnered.

![](https://blog.cloudflare.com/content/images/2023/06/image2-20.png)

With DEX, you get a reliable and precise view of server and DNS response times from around the world. The time series format allows you to spot trends, identify peak periods, and pinpoint potential issues with ease. This isn't just data—it's actionable intelligence that helps you optimize server configurations, DNS settings, and ultimately, your users' digital experience. Essentially, these charts are more than visual aids; they are strategic tools, using Cloudflare's network to enhance your application's performance management.

![](https://blog.cloudflare.com/content/images/2023/06/image6-3.png)

The time series chart depicting HTTP status codes is another powerful tool in the DEX arsenal. Drawing from the wealth of data traversing our globally distributed network, it lets you quickly visualize the frequency of each status code over time. This granular perspective allows you to detect and investigate anomalies, such as a sudden surge of client or server errors. By making HTTP status codes more comprehensible, it equips you to swiftly identify and troubleshoot potential issues that can impact user experience.

Synthetic Application Monitoring is more than a product; it's a strategic ally that harnesses the might of Cloudflare's network, ensuring your applications deliver the reliable, high-quality experience your users expect and deserve.

### Understand the state of WARP-enrolled devices with Fleet Status

Zero Trust solutions replace legacy private networks with a model that assumes all connection attempts are suspicious. A [Zero Trust network](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) denies access attempts by default and forces every connection or request to prove that access should be granted.

A large component of proof is the identity of the end user, but the device itself also provides a signal about access rights. Whether the device is managed by the enterprise, healthy and patched, or assigned to a given user can determine permissions within Cloudflare One. For customers who rely on Cloudflare One to give their users a secure path to the rest of the Internet, the device also becomes an on-ramp for those team members connecting through Cloudflare.

We kept hearing from customers who wanted to better understand their device fleet using the data that Cloudflare could gather.

As part of today’s launch, we are introducing Fleet Status. Fleet Status provides real-time insights into the status of all of your client devices’ connection, mode, and location on both a global and per-device basis. This is achieved via Cloudflare WARP. Cloudflare WARP is a client which allows companies to protect corporate devices by securely and privately sending traffic from those devices to Cloudflare’s global network, where Cloudflare Gateway can apply advanced web filtering. The WARP client also makes it possible to apply advanced Zero Trust policies that check for a device’s health before it connects to corporate applications.

![](https://blog.cloudflare.com/content/images/2023/06/image4-16.png)

Fleet Status, with its data visualizations, detailed per-device views, and time-series charts, transforms the way administrators understand their deployment. Picture a network administrator who oversees a fleet of WARP-enrolled devices scattered worldwide, each contributing to the organization's vital operations. Suddenly, an issue arises. A gr...