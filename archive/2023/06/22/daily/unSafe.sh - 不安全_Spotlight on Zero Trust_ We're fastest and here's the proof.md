---
title: Spotlight on Zero Trust: We're fastest and here's the proof
url: https://buaq.net/go-169776.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:36.277297
---

# Spotlight on Zero Trust: We're fastest and here's the proof

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

![](https://8aqnet.cdn.bcebos.com/d4272b8379e1a15ad2b704f16f18b7c8.jpg)

Spotlight on Zero Trust: We're fastest and here's the proof

Loading...
*2023-6-21 21:0:38
Author: [blog.cloudflare.com(查看原文)](/jump-169776.htm)
阅读量:17
收藏*

---

Loading...

* [![David Tuber](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/kutiya-face-1.png)](https://blog.cloudflare.com/author/tubes/)

![Spotlight on Zero Trust: We're fastest and here's the proof](https://blog.cloudflare.com/content/images/2023/06/image3-18.png)

In [January](https://blog.cloudflare.com/network-performance-update-cio-edition/) and in [March](https://blog.cloudflare.com/network-performance-update-security-week-2023/) we posted blogs outlining how Cloudflare performed against others in Zero Trust. The conclusion in both cases was that Cloudflare was faster than Zscaler and Netskope in a variety of Zero Trust scenarios. For Speed Week, we’re bringing back these tests and upping the ante: we’re testing more providers against more public Internet endpoints in more regions than we have in the past.

For these tests, we tested three Zero Trust scenarios: Secure Web Gateway (SWG), Zero Trust Network Access (ZTNA), and Remote Browser Isolation (RBI). We tested against three competitors: Zscaler, Netskope, and Palo Alto Networks. We tested these scenarios from 12 regions around the world, up from the four we’d previously tested with. The results are that Cloudflare is the fastest Secure Web Gateway in 42% of testing scenarios, the most of any provider. Cloudflare is 46% faster than Zscaler, 56% faster than Netskope, and 10% faster than Palo Alto for ZTNA, and 64% faster than Zscaler for RBI scenarios.

In this blog, we’ll provide a refresher on why performance matters, do a deep dive on how we’re faster for each scenario, and we’ll talk about how we measured performance for each product.

### Performance is a threat vector

Performance in Zero Trust matters; when Zero Trust performs poorly, users disable it, opening organizations to risk. Zero Trust services should be unobtrusive when the services become noticeable they prevent users from getting their job done.

Zero Trust services may have lots of bells and whistles that help protect customers, but none of that matters if employees can’t use the services to do their job quickly and efficiently. Fast performance helps drive adoption and makes security feel transparent to the end users. At Cloudflare, we prioritize making our products fast and frictionless, and the results speak for themselves. So now let’s turn it over to the results, starting with our secure web gateway.

### Cloudflare Gateway: security at the Internet

A secure web gateway needs to be fast because it acts as a funnel for all of an organization’s Internet-bound traffic. If a secure web gateway is slow, then any traffic from users out to the Internet will be slow. If traffic out to the Internet is slow, users may see web pages load slowly, video calls experience jitter or loss, or generally unable to do their jobs. Users may decide to turn off the gateway, putting the organization at risk of attack.

In addition to being close to users, a performant web gateway needs to also be well-peered with the rest of the Internet to avoid slow paths out to websites users want to access. Many websites use CDNs to accelerate their content and provide a better experience. These CDNs are often well-peered and embedded in last mile networks. But traffic through a secure web gateway follows a forward proxy path: users connect to the proxy, and the proxy connects to the websites users are trying to access. If that proxy isn’t as well-peered as the destination websites are, the user traffic could travel farther to get to the proxy than it would have needed to if it was just going to the website itself, creating a hairpin, as seen in the diagram below:

![](https://blog.cloudflare.com/content/images/2023/06/image1-24.png)

A well-connected proxy ensures that the user traffic travels less distance making it as fast as possible.

To compare secure web gateway products, we pitted the Cloudflare Gateway and WARP client against Zscaler, Netskope, and Palo Alto which all have products that perform the same functions. Cloudflare users benefit from Gateway and Cloudflare’s network being embedded deep into last mile networks close to users, being peered with over 12,000 networks. That heightened connectivity shows because Cloudflare Gateway is the fastest network in 42% of tested scenarios:

![](https://blog.cloudflare.com/content/images/2023/06/image6-2.png)

| Number of testing scenarios where each provider is fastest for 95th percentile HTTP Response time (higher is better) | |
| --- | --- |
| Provider | Scenarios where this provider is fastest |
| Cloudflare | 48 |
| Zscaler | 14 |
| Netskope | 10 |
| Palo Alto Networks | 42 |

This data shows that we are faster to more websites from more places than any of our competitors. To measure this, we look at the 95th percentile HTTP response time: how long it takes for a user to go through the proxy, have the proxy make a request to a website on the Internet, and finally return the response. This measurement is important because it’s an accurate representation of what users see. When we look at the 95th percentile across all tests, we see that Cloudflare is 2.5% faster than Palo Alto Networks, 13% faster than Zscaler, and 6.5% faster than Netskope.

| 95th percentile HTTP response across all tests | |
| --- | --- |
| Provider | 95th percentile response (ms) |
| Cloudflare | 515 |
| Zscaler | 595 |
| Netskope | 550 |
| Palo Alto Networks | 529 |

Cloudflare wins out here because Cloudflare’s exceptional peering allows us to succeed in places where others were not able to succeed. We are able to get locally peered in hard-to-reach places on the globe, giving us an edge. For example, take a look at how Cloudflare performs against the others in Australia, where we are 30% faster than the next fastest provider:

![](https://blog.cloudflare.com/content/images/2023/06/image2-19.png)

Cloudflare establishes great peering relationships in countries around the world: in Australia we are locally peered with all of the major Australian Internet providers, and as such we are able to provide a fast experience to many users around the world. Globally, we are peered with over 12,000 networks, getting as close to end users as we can to shorten the time requests spend on the public Internet. This work has previously allowed us to deliver content quickly to users, but in a Zero Trust world, it shortens the path users take to get to their SWG, meaning they can quickly get to the services they need.

Previously [when we performed these tests](https://blog.cloudflare.com/network-performance-update-cio-edition/), we only tested from a single Azure region to five websites. Existing testing frameworks like Catchpoint are unsuitable for this task because performance testing requires that you run the SWG client on the testing endpoint. We also needed to make sure that all of the tests are running on similar machines in the same places to measure performance as well as possible. This allows us to measure the end-to-end responses coming from the same location where both test environments are running.

In our testing configuration for this round of evaluations, we put four VMs in 12 cloud regions side by side: one running Cloudflare WARP connecting to our gateway, one running ZIA, one running Netskope, and one running Palo Alto Networks. These VMs made requests every five minutes to the 1...