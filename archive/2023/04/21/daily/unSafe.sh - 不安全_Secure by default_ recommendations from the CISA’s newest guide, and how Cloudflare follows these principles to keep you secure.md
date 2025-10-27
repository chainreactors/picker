---
title: Secure by default: recommendations from the CISA’s newest guide, and how Cloudflare follows these principles to keep you secure
url: https://buaq.net/go-159674.html
source: unSafe.sh - 不安全
date: 2023-04-21
fetch_date: 2025-10-04T11:32:29.888694
---

# Secure by default: recommendations from the CISA’s newest guide, and how Cloudflare follows these principles to keep you secure

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

![](https://8aqnet.cdn.bcebos.com/e11dd2c03ed6d852969af408269de7b2.jpg)

Secure by default: recommendations from the CISA’s newest guide, and how Cloudflare follows these principles to keep you secure

Loading...
*2023-4-20 21:44:42
Author: [blog.cloudflare.com(查看原文)](/jump-159674.htm)
阅读量:24
收藏*

---

Loading...

* [![Patrick R. Donahue](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/https://blog-cloudflare-com-assets.storage.googleapis.com/2020/04/me0-1.png)](https://blog.cloudflare.com/author/patrick/)
* [![Ed Conolly](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/04/me-square.jpeg)](https://blog.cloudflare.com/author/ed-conolly/)

![Secure by default: recommendations from the CISA’s newest guide, and how Cloudflare follows these principles to keep you secure](https://blog.cloudflare.com/content/images/2023/04/image1-13.png)

When you buy a new house, you shouldn’t have to worry that everyone in the city can unlock your front door with a universal key before you change the lock. You also shouldn’t have to walk around the house with a screwdriver and tighten the window locks and back door so that intruders can’t pry them open. And you *really* shouldn’t have to take your alarm system offline every few months to apply critical software updates that the alarm vendor could have fixed with better software practices before they installed it.

Similarly, you shouldn’t have to worry that when you buy a network discovery tool it can be [accessed by any attacker until you change the password](https://threatpost.com/cisco-patches-critical-default-password-bug/142814/), or that your expensive hardware-based firewalls [can be recruited to launch DDoS attacks](https://www.darkreading.com/vulnerabilities-threats/cisa-palo-alto-firewall-bug-active-exploit) or [run arbitrary code](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-138a) without the [need to authenticate](https://www.bleepingcomputer.com/news/security/fortinet-warns-of-new-critical-unauthenticated-rce-vulnerability).

This “default secure” posture is the focus of a [recently published guide](https://www.cisa.gov/sites/default/files/2023-04/principles_approaches_for_security-by-design-default_508_0.pdf) jointly authored by the Cybersecurity and Infrastructure Agency (CISA), NSA, FBI, and six other international agencies representing the United Kingdom, Australia, Canada, Germany, Netherlands, and New Zealand. In the guide, the authors implore technology vendors to follow *Secure-by-Design* and *Secure-by-Default* principles, shifting the burden of security as much as possible *away* from the end-user and back *towards* the manufacturer:

> *The authoring agencies strongly encourage every technology manufacturer to build their products in a way that prevents customers from having to constantly perform monitoring, routine updates, and damage control on their systems to mitigate cyber intrusions. Manufacturers are encouraged to take ownership of improving the security outcomes of their customers. Historically, technology manufacturers have relied on fixing vulnerabilities found after the customers have deployed the products, requiring the customers to apply those patches at their own expense. Only by incorporating Secure-by-Design practices will we break the vicious cycle of creating and applying fixes.*

In this post we’ll review some of the authors’ recommendations, discuss how Cloudflare applies these principles to the products that we build, and provide some suggestions on what other organizations can do to support similar initiatives internally.

### Secure-by-Default: building products that require minimal hardening

Cloudflare makes cybersecurity products that protect [employees, applications, and networks](https://www.cloudflare.com/everywhere-security/) from attack. Typically, the ideas for new products and features come from one of two places: i) customers who are expressing a risk they’re worried about; or ii) our own internal Security team asking for help better securing Cloudflare’s internal network from threats. (The products that we build for our Security team are also then made available to our customers, once they’re battle tested internally.)

Wherever the source, when a product manager thinks through a new product offering, they first socialize the idea around the company for feedback. Often this feedback includes encouragement to make the product more “magical”. What this means in practice is that customers should have to do less, but get more; our job is essentially to make security administrators’ lives easier so they can focus their time where it’s most needed. An early example of this approach can be found in our blog post announcing [Universal SSL](https://blog.cloudflare.com/introducing-universal-ssl/) in 2014:

> *For all customers, we will now automatically provision a SSL certificate on CloudFlare's network that will accept HTTPS connections for a customer's domain and subdomains.*

The idea sounds simple but in 2014 this approach to SSL/TLS was unique in the industry: every other platform required customers to take some action before their website was encrypted-in-transit using HTTPS to protect against snooping and impersonation. Security administrators either had to go acquire the certificate themselves and upload (and renew) it, or manually perform some steps to demonstrate ownership to a certificate authority (CA). Because Cloudflare both manages authoritative DNS for our customers and runs a global reverse proxy, we can take care of all these steps automagically. Additionally, as new SSL/TLS attacks are discovered, we [automatically improve](https://blog.cloudflare.com/staying-on-top-of-tls-attacks/) how our servers negotiate encryption with browsers and API clients to keep our customers secure. No customer configuration or oversight is required.

We agree with CISA’s statement that “[t]he complexity of security configuration should not be a customer problem.” And aim to build products that materially improve security with little to no customer action beyond putting their employees, applications, and networks behind Cloudflare:

> *Secure-by-Default products are those that are secure to use “out of the box” with little to no configuration changes necessary and security features available without additional cost. Together, these two principles move much of the burden of staying secure to manufacturers and reduce the chances that customers will fall victim to security incidents resulting from misconfigurations, insufficiently fast patching, or many other common issues.*

Another example of our Secure-by-Default approach is how we protect against “0 day” attacks in our Web Application Firewall [using machine learning](https://blog.cloudflare.com/data-generation-and-sampling-strategies/) (ML). Zero day attacks are security vulnerabilities discovered by attackers or researchers before the software vendor is aware of the issue (or has had a chance to release a patch). Often the attack is exploited “in the wild” before customers are able to plug the holes in their systems, or their upstream security vendors are able to virtually patch the issue. A recent, widely-exploited 0 day was [Log4j](https://blog.cloudflare.com/cve-2021-44228-log4j-rce-0-day-mitigation/); software manufacturers using this library in their code raced to update their software as quickly as possible. But many took days, weeks, or even months to do so.

Cloudflare is proud of the speed at which we responded to Log4j, and the fact we provide the highest severity WAF protecti...