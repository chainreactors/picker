---
title: DNS 泄漏以及如何防止
url: https://einverne.github.io/post/2024/06/dns-leak.html
source: Verne in GitHub
date: 2024-06-10
fetch_date: 2025-10-06T16:54:18.727298
---

# DNS 泄漏以及如何防止

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# DNS 泄漏以及如何防止

Posted on 06/09/2024
, Last modified on 06/09/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-06-09-dns-leak.md)

## 什么是 DNS 泄漏

DNS 泄露（DNS Leak）是指当使用虚拟专用网络（VPN）或其他匿名工具时，域名系统（DNS）查询数据绕过加密隧道，直接通过用户的本地 ISP（互联网服务提供商）进行解析。这意味着用户的浏览活动可能被 ISP 监视或记录，进而暴露了用户的实际 IP 地址和在线活动。

在深入探讨 DNS 泄露之前，有必要了解 DNS 的基本工作原理。DNS 是互联网的电话簿，当用户输入一个域名（如www.example.com）时，DNS将其转换为对应的IP地址（如192.0.2.1），以便计算机能够理解和访问该网站。

通常情况下，用户的设备会向 ISP 的 DNS 服务器发送请求进行解析。然而，当用户使用 VPN 时，所有的流量应通过加密的 VPN 隧道传输，并由 VPN 提供商的 DNS 服务器处理 DNS 请求。

DNS 泄露的原因
DNS 泄露可能由于以下几个原因发生：

操作系统配置问题：一些操作系统可能会忽略 VPN 设置，继续使用本地 DNS 服务器。
VPN 设置不当：不正确的 VPN 配置可能导致 DNS 请求未能通过 VPN 隧道传输。
VPN 软件缺陷：某些 VPN 软件存在缺陷，无法正确处理 DNS 请求。
IPv6 配置问题：如果 VPN 只处理 IPv4 流量，而未配置 IPv6，IPv6 流量可能会直接泄露。

## 如何检测 DNS 检测

检测 DNS 泄漏有很多方法，最简单的方法就是找一个在线的检测工具。

在线检测 DNS 泄漏的工具，通过用户访问网页的时候，在网站上生成多个域名解析请求，通过用户的设备发起，网站通过脚本捕获并记录这些域名请求结果，这些网站根据 DNS 响应，判断是哪个 DNS 服务器处理的，然后通过对比 DNS 服务器 IP 地址与公共 DNS 服务器 ISP DNS 服务器进行匹对。

如果检测的 DNS 服务器属于用户的 ISP 或者其他不安全的 DNS 服务器，而非用户期待的 DNS 服务器，则说明了 DNS 泄漏。

## DNS 泄漏会造成什么影响

### 暴露用户的真实 IP 地址

即使用户使用 VPN 或者其他匿名网络访问工具来隐藏其真实的 IP 地址，但是如果 DNS 请求没有通过 VPN 隧道，而是通过用户自己的 ISP 解析，那么 ISP 和其他潜在的监听者仍然可以看到用户的真实 IP 地址，这意味着用户的地理位置和身份可能被暴露。

DNS 请求包含了用户访问的域名，如果这些请求通过 ISP 解析，ISP 可以记录和分析用户的浏览历史，这使得用户的在线活动变得不再私密，并且可能被用户于广告投放，数据挖掘，甚至在某些国家可能被政府监控。

### 潜在的网络攻击

DNS 泄漏还可能使得用户更容易成为攻击的目标，比如，攻击者可以利用 DNS 请求来识别用户网络行为，实施 DNS 劫持或中间人攻击，将用户引导至伪造的网站或恶意服务器，从而窃取敏感信息或传播恶意软件。

### 信息过滤和审查

某些政府或地区，政府或 ISP 会对用户访问的内容进行过滤和审查。通过 DNS 泄漏，政府或 ISP 可以轻松跟踪和组织用户访问被审查或禁止的网站，从而限制用户的互联网自由。

## 如何防止 DNS 泄漏

* 使用可靠的 VPN 服务，并且配置 VPN 的 DNS，将所有的网络请求通过 VPN 进行
* 手动配置 DNS 服务器
* 如果 VPN 不支持 IPv6，则禁用 IPv6
* 操作系统和路由器配置静态路由，或自行搭建安全的 DNS 服务器，比如 [AdGuard Home](https://blog.einverne.info/post/2020/05/use-adguard-home-to-block-ads.html) [[PiHole]] 等

## Related Posts

* [DNS 泄漏以及如何防止](/post/2024/06/dns-leak.html) - 06/09/2024

---

* [← Previous（前一篇）](/post/2024/06/money-to-hong-kong.html "从内地到香港出金最佳的方法")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/06/estonia-e-residency.html "爱沙尼亚电子居民申请记录")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/06/dns-leak.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [dns 17](/tags.html#dns)
* [dns-leak 1](/tags.html#dns-leak)
* [host 2](/tags.html#host)
* [domain-resolve 1](/tags.html#domain-resolve)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").