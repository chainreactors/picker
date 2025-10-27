---
title: 请教：如何使用 wireguard 作为链式代理的出口节点 - V2EX
url: https://buaq.net/go-156576.html
source: unSafe.sh - 不安全
date: 2023-04-03
fetch_date: 2025-10-04T11:29:39.690013
---

# 请教：如何使用 wireguard 作为链式代理的出口节点 - V2EX

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

![]()

请教：如何使用 wireguard 作为链式代理的出口节点 - V2EX

前一段时间看到 Project X 的 通过 Cloudflare Warp 增强代理安全性 一文，今天没有别的事，感觉可以浪费一点生命，但是最终还是失败了。遇到了一些疑惑，想请教一下各位大佬。我想
*2023-4-2 21:3:42
Author: [v2ex.com(查看原文)](/jump-156576.htm)
阅读量:1109
收藏*

---

前一段时间看到 Project X 的 [通过 Cloudflare Warp 增强代理安全性](https://xtls.github.io/document/level-2/warp.html) 一文，今天没有别的事，感觉可以浪费一点生命，但是最终还是失败了。遇到了一些疑惑，想请教一下各位大佬。

我想要配置链式代理的最大原因是担心机场的安全性。Project X 的原文也提到了这一点：

> 保护用户私密性的一个方法，就是在客户端使用链式代理。Warp 使用的 WireGuard 轻量级 VPN 协议会在代理层内增加一层加密。对于机场而言，用户所有流量的目标都是 Warp ，从而最大程度保护自己的隐私。

### 问题 1: 原文的说明中提到“在服务端分流回国流量至 warp”。请问这一步是必须的吗？

* 如果是必须的，即要求能够控制服务端的出站配置，那完全无助于提升安全性：因为显然普通用户不可能控制机场的配置。而如果需要用户再利用自己的 VPS 创建一个节点，控制这个节点的配置来将流量导向 warp ，那也是无意义的：因为流量流向用户自己的 VPS 以后，已经达成了防止泄露流量信息给机场这一目的
* 如果非必须，那才会有问题 2：

### 问题 2: 要如何配置，才能完成使用 wireguard 作为链式代理的出口节点这一要求呢？

我已经（略为艰难地）获得了一个能够在 Clash Verge (内核选用 Clash meta) 中成功连接的 wireguard 类型的代理，同时还拥有机场提供的可用节点，并创建了如下结构的 clash 配置文件

```
proxies:
  - {name: 机场节点 1, server: server.xyz, port: 21584, type: vmess, uuid: xxx, alterId: 1, cipher: auto, tls: true, skip-cert-verify: false}
  # (此处省略若干机场节点)
  - {name: warp-github, type: wireguard, server: 162.159.193.10, port: 2408, ip: 172.16.0.2, ipv6: ipv6-addr, public-key: bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=, private-key: xxx-private-key, mtu: 1280, udp: true, reserved: [219,212,139] }
proxy-groups:
  - name: 🔰 选择节点
    type: select
    proxies:
      - 机场节点 1
      - warp-github
      - relay
      - DIRECT
  - name: relay
    type: relay
    proxies:
      - 机场节点 1
      - warp-github
rules:
 - MATCH,🔰 选择节点
```

在使用这个配置时，如果我单独选择“机场节点 1”或者“warp-github”，代理都能正常工作。但是当为选择“relay”时，代理就不工作了。`relay`规则的配置我是参考的文档，配置并不复杂，不理解为什么它不能工作。以下是我在写这个主题的时候暂时想到的一些方向和疑问：

* 链式代理对代理链中的节点协议是否有要求？
* clash meta 支持链式代理，也支持 wireguard ，但也许它不支持将 wireguard 作为链式代理使用？

### 问题 3: 有没有已经验证可行性的 wireguard 链式代理实践工具链或者博文推荐？

恳请各位大佬不吝赐教

文章来源: https://v2ex.com/t/929231#reply1
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)