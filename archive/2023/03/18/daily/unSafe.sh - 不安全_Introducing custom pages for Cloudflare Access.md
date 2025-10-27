---
title: Introducing custom pages for Cloudflare Access
url: https://buaq.net/go-153982.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:30.747347
---

# Introducing custom pages for Cloudflare Access

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

![](https://8aqnet.cdn.bcebos.com/53a9da1dbf7cc8c1e75e844648575056.jpg)

Introducing custom pages for Cloudflare Access

Loading...
*2023-3-17 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-153982.htm)
阅读量:20
收藏*

---

Loading...

* [![Kenny Johnson](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2020/12/0DA903DE-E315-43D5-B0DE-39870448303D.jpeg)](https://blog.cloudflare.com/author/kenny/)

![Access Custom Pages](https://blog.cloudflare.com/content/images/2023/03/image4-14.png)

Over 10,000 organizations rely on Cloudflare Access to connect their employees, partners, and contractors to the applications they need. From small teams on our [free plan](https://www.cloudflare.com/plans/zero-trust-services/) to some of the world’s largest enterprises, Cloudflare Access is the Zero Trust front door to how they work together. As more users start their day with Cloudflare Access, we’re excited to announce new options to customize how those users experience our [industry-leading](https://www.cloudflare.com/analysts/) Zero Trust solution. We’re excited to announce customizable Cloudflare Access pages including login, blocks and the application launcher.

### Where does Cloudflare Access fit in a user’s workflow today?

Most teams we work with start their [Zero Trust journey](https://zerotrustroadmap.org/) by replacing their existing virtual private network (VPN) with Cloudflare Access. The reasons vary. For some teams, their existing VPN allows too much trust by default and Access allows them to quickly build segmentation based on identity, device posture, and other factors. Other organizations deploy Cloudflare Access because they are exhausted from trying to maintain their VPN and dealing with end user complaints.

When those administrators begin setting up Cloudflare Access, they connect the resources they need to protect to Cloudflare’s network. They can deploy a Cloudflare Tunnel to create a secure, outbound-only, connection to Cloudflare, rely on our existing DNS infrastructure, or even force SaaS application logins through our network. Administrators can then layer on granular Zero Trust rules to determine who can reach a given resource.

To the end user, Cloudflare Access is just a security guard checking for identity, device posture, or other signals at every door. In most cases they should never need to think about us. Instead, they just enjoy a [much faster experience](https://blog.cloudflare.com/network-performance-update-cio-edition/) with less hassle. When they attempt to reach an application or service, we check each and every request and connection for proof that they should be allowed.

When they do notice Cloudflare Access, they interact with screens that help them make a decision about what they need. In these cases we don’t just want to be a silent security guard - we want to be a helpful tour guide.

![](https://blog.cloudflare.com/content/images/2023/03/Screenshot-2023-03-17-at-10.57.03.png)

Cloudflare Access supports the ability for administrators to configure multiple identity providers simultaneously. Customers love this capability when they work with contractors or acquired teams. We can also configure this only for certain applications. When users arrive, though, we need to know which direction to send them for their initial authentication. We present this selection screen, along with guiding text provided by the administrator, to the user.

![](https://blog.cloudflare.com/content/images/2023/03/image2-22.png)

When teams move their applications behind Cloudflare Access, we become the front door to how they work. We use that position to present the user with all of the applications they can reach in a portal that allows them to click on any tile to launch the application.

![](https://blog.cloudflare.com/content/images/2023/03/image1-40.png)

In some cases, the user lacks sufficient permissions to reach the destination. Even though they are being blocked we still want to reduce confusion. Instead of just presenting a generic browser error or dropping a connection, we display a block page.

### Why do these need to change?

More and more large enterprises are starting to adopt a Zero Trust VPN replacement and they’re [selecting Cloudflare](https://blog.cloudflare.com/why-cios-select-cloudflare-one/) to do so. Unlike small teams that can send a short Slack message about an upcoming change to their employee workflow, some of the CIOs and CSOs that deploy Access need to anticipate questions and curiosity from tens of thousands of employees and contractors.

Those users do not know what Cloudflare is and we don’t need them to. Instead, we just want to securely connect them to the tools they need. To solve that, we need to give IT administrators more space to communicate and we need to get our branding out of the way.

### What will I be able to customize?

Following the release of Access page customization, administrators will be able to customize: the login screen, access denied errors and the Access Application Launcher.

### What’s next?

We are building page customization in Cloudflare Access following the existing template our reverse proxy customers can use to modify pages presented to end users. We’re excited to bring that standard experience to these workflows as well.

Even though we’re building on that pattern, we still want your feedback. Ahead of a closed beta we are looking for customers who want to provide input as we fine tune this new configuration option. Interested in helping shape this work? Let us know [here](https://cloudflare.com/lp/access-page-customization).

We protect
[entire corporate networks](https://www.cloudflare.com/network-services/),
help customers build
[Internet-scale applications efficiently](https://workers.cloudflare.com/),
accelerate any
[website
or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/),
[ward off DDoS
attacks](https://www.cloudflare.com/ddos/), keep
[hackers at
bay](https://www.cloudflare.com/application-security/),
and can help you on
[your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://1.1.1.1/) from any device to get started with
our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a
new career direction, check out [our open
positions](https://cloudflare.com/careers).

[Security Week](https://blog.cloudflare.com/tag/security-week/)
[Cloudflare Access](https://blog.cloudflare.com/tag/access/)

文章来源: https://blog.cloudflare.com/access-custom-pages/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)