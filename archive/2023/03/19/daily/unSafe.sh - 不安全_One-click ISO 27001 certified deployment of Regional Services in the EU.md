---
title: One-click ISO 27001 certified deployment of Regional Services in the EU
url: https://buaq.net/go-154083.html
source: unSafe.sh - 不安全
date: 2023-03-19
fetch_date: 2025-10-04T10:01:52.135229
---

# One-click ISO 27001 certified deployment of Regional Services in the EU

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

![](https://8aqnet.cdn.bcebos.com/9dcc01aa3db6fe1c623aa32d8bd3a76a.jpg)

One-click ISO 27001 certified deployment of Regional Services in the EU

Loading...
*2023-3-18 23:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-154083.htm)
阅读量:19
收藏*

---

Loading...

* [![Achiel van der Mandele](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2019/04/avatar.png)](https://blog.cloudflare.com/author/achiel/)

![](https://blog.cloudflare.com/content/images/2023/03/Regional-Services-one-click-limit-traffic-to-ISO-27001-certified-colos-only.png)

Today, we’re very happy to announce the general availability of a new region for Regional Services that allows you to limit your traffic to only [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) certified data centers inside the EU. This helps customers that have very strict requirements surrounding which data centers are allowed to decrypt and service traffic. Enabling this feature is a one-click operation right on the Cloudflare dashboard.

### Regional Services - a recap

In 2020, we saw an increase in prospects asking about data localization. Specifically, increased regulatory pressure limited them from using vendors that operated at global scale. We launched [Regional Services](https://blog.cloudflare.com/introducing-regional-services/), a new way for customers to use the Cloudflare network. With Regional Services, we put customers back in control over which data centers are used to service traffic. Regional Services operates by limiting exactly which data centers are used to decrypt and service HTTPS traffic. For example, a customer may want to use only data centers inside the European Union to service traffic. Regional Services operates by leveraging our global network for DDoS protection but only decrypting traffic and applying Layer 7 products inside data centers that are located inside the European Union.

We later followed up with the [Data Localization Suite](https://www.cloudflare.com/data-localization/) and additional regions: [India, Singapore and Japan](https://blog.cloudflare.com/regional-services-comes-to-apac/).

With Regional Services, customers get the best of both worlds: we empower them to use our global network for volumetric DDoS protection whilst limiting where traffic is serviced. We do that by accepting the raw TCP connection at the closest data center but forwarding it on to a data center in-region for decryption. That means that only machines of the customer’s choosing actually see the raw HTTP request, which could contain sensitive data such as a customer’s bank account or medical information.

### A new region and a new UI

Traditionally we’ve seen requests for data localization largely center around countries or geographic areas. Many types of regulations require companies to make promises about working only with vendors that are capable of restricting where their traffic is serviced geographically. Organizations can have many reasons for being limited in their choices, but they generally fall into two buckets: compliance and contractual commitments.

More recently, we are seeing that more and more companies are asking about security requirements. An often asked question about security in IT is: how do you ensure that something is safe? For instance, for a data center you might be wondering how physical access is managed. Or how often security policies are reviewed and updated. This is where certifications come in. A common certification in IT is the [ISO 27001 certification](https://en.wikipedia.org/wiki/ISO/IEC_27001):

Per the [ISO.org](https://www.iso.org/isoiec-27001-information-security.html):

> *“ISO/IEC 27001 is the world’s best-known standard for information security management systems (ISMS) and their requirements. Additional best practice in data protection and cyber resilience are covered by more than a dozen standards in the ISO/IEC 27000 family. Together, they enable organizations of all sectors and sizes to manage the security of assets such as financial information, intellectual property, employee data and information entrusted by third parties.”*

In short, ISO 27001 is a certification that a data center can achieve that ensures that they maintain a set of security standards to keep the data center secure. With the new Regional Services region, HTTPS traffic will only be decrypted in data centers that hold the ISO 27001 certification. Products such as WAF, Bot Management and Workers will only be applied in those relevant data centers.

The other update we’re excited to announce is a brand new User Interface for configuring the Data Localization Suite. The previous UI was limited in that customers had to preconfigure a region for an entire zone: you couldn’t mix and match regions. The new UI allows you to do just that: each individual hostname can be configured for a different region, directly on the DNS tab:

![](https://blog.cloudflare.com/content/images/2023/03/pasted-image-0--5--3.png)

Configuring a region for a particular hostname is now just a single click away. Changes take effect within seconds, making this the easiest way to configure data localization yet. For customers using the Metadata Boundary, we’ve also launched a self-serve UI that allows you to configure where logs flow:

![](https://blog.cloudflare.com/content/images/2023/03/image-13.png)

We’re excited about these new updates that give customers more flexibility in choosing which of Cloudflare’s data centers to use as well as making it easier than ever to configure them. The new region and existing regions are now a one-click configuration option right from the dashboard. As always, we love getting feedback, especially on what new regions you’d like to see us add in the future. In the meantime, if you’re interested in using the Data Localization Suite, please reach out to your account team.

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
[Data Localization](https://blog.cloudflare.com/tag/data-localization/)
[Compliance](https://blog.cloudflare.com/tag/compliance/)
[Certification](https://blog.cloudflare.com/tag/certification/)
[Regional Services](https://blog.cloudflare.com/tag/regional-services/)

Related Posts

January 07, 2022 3:57PM

[## Cloudflare Innovation Weeks 2021](https://blog.cloudflare.com/2021-innovations-weeks/)

As we start planning our 2022 Innovation Weeks, we are reflecting back on the highlights from each of these weeks...

By

March 17, 2022 12:59PM

[## Clientless Web Isolation is now generally available](https://blog.cloudflare.com/clientless-web-isolation-general-availability/)

Today, we’re excited to announce that Clientless Web Isolation is ...