---
title: SLP: a new DDoS amplification vector in the wild
url: https://buaq.net/go-160486.html
source: unSafe.sh - 不安全
date: 2023-04-26
fetch_date: 2025-10-04T11:31:32.135777
---

# SLP: a new DDoS amplification vector in the wild

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

![](https://8aqnet.cdn.bcebos.com/4265863e19918e41dcc83f11ffa69f1f.jpg)

SLP: a new DDoS amplification vector in the wild

Loading...
*2023-4-25 21:7:56
Author: [blog.cloudflare.com(查看原文)](/jump-160486.htm)
阅读量:35
收藏*

---

Loading...

* [![Alex Forster](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/10/me-even-smaller-crushed.png)](https://blog.cloudflare.com/author/alex-forster/)
* [![Omer Yoachimik](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/https://blog-cloudflare-com-assets.storage.googleapis.com/2020/04/Omer-1.png)](https://blog.cloudflare.com/author/omer/)

![](https://blog.cloudflare.com/content/images/2023/04/image13-1-4.png)

Earlier today, April 25, 2023, researchers Pedro Umbelino at [Bitsight](https://www.bitsight.com/blog/new-high-severity-vulnerability-cve-2023-29552-discovered-service-location-protocol-slp) and Marco Lux at [Curesec](https://curesec.com/blog/article/CVE-2023-29552-Service-Location-Protocol-Denial-of-Service-Amplification-Attack-212.html) published their discovery of CVE-2023-29552, a new [DDoS reflection/amplification attack vector](https://www.cisa.gov/news-events/alerts/2014/01/17/udp-based-amplification-attacks) leveraging the SLP protocol. If you are a Cloudflare customer, your services are already protected from this new attack vector.

[Service Location Protocol](https://en.wikipedia.org/wiki/Service_Location_Protocol) (SLP) is a “service discovery” protocol invented by Sun Microsystems in 1997. Like other service discovery protocols, it was designed to allow devices in a local area network to interact without prior knowledge of each other. SLP is a relatively obsolete protocol and has mostly been supplanted by more modern alternatives like UPnP, mDNS/Zeroconf, and WS-Discovery. Nevertheless, many commercial products still offer support for SLP.

Since SLP has no method for authentication, it should never be exposed to the public Internet. However, Umbelino and Lux have discovered that upwards of 35,000 Internet endpoints have their devices’ SLP service exposed and accessible to anyone. Additionally, they have discovered that the UDP version of this protocol has an [amplification factor](https://blog.cloudflare.com/reflections-on-reflections/) of up to 2,200x, which is the third largest discovered to-date.

Cloudflare expects the prevalence of SLP-based DDoS attacks to rise significantly in the coming weeks as malicious actors learn how to exploit this newly discovered attack vector.

### Cloudflare customers are protected

If you are a Cloudflare customer, our [automated DDoS protection system](https://blog.cloudflare.com/deep-dive-cloudflare-autonomous-edge-ddos-protection/) already protects your services from these SLP amplification attacks.

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

[CVE](https://blog.cloudflare.com/tag/cve/)
[Vulnerabilities](https://blog.cloudflare.com/tag/vulnerabilities/)
[DDoS](https://blog.cloudflare.com/tag/ddos/)
[Attacks](https://blog.cloudflare.com/tag/attacks/)
[Mitigation](https://blog.cloudflare.com/tag/mitigation/)

文章来源: https://blog.cloudflare.com/slp-new-ddos-amplification-vector/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)