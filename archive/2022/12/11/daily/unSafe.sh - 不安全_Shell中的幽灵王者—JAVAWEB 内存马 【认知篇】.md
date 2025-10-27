---
title: Shell中的幽灵王者—JAVAWEB 内存马 【认知篇】
url: https://buaq.net/go-139453.html
source: unSafe.sh - 不安全
date: 2022-12-11
fetch_date: 2025-10-04T01:10:23.153899
---

# Shell中的幽灵王者—JAVAWEB 内存马 【认知篇】

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

![](https://8aqnet.cdn.bcebos.com/68396fb8f48ee6d03ae6d23a7cfb6d64.jpg)

Shell中的幽灵王者—JAVAWEB 内存马 【认知篇】

Goby社区第 21 篇技术分享文章全文共：6700 字   预计阅读时间：17 分钟自我介绍：大家好，我是 su18。无论是个人博客还是社区，已经很久没写技术文章了，原因有很多，时间、精力、心态等等
*2022-12-10 16:56:28
Author: [mp.weixin.qq.com(查看原文)](/jump-139453.htm)
阅读量:35
收藏*

---

![](https://mmbiz.qpic.cn/mmbiz_gif/GGOWG0fficjLTMIjhRPrloPMpJ4nXfwsIjLDB23mjUrGc3G8Qwo770yYCQAnyVhPGKiaSgfVu0HKnfhT4v5hSWcQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIL5d8xFK4FFG2hKG8EqiaPPDCrYWrbCpAg6VzuAUx1Hyjrcg9oQgqb5RlmoN9OdBzvOMowfzurCTA/640?wx_fmt=png)

Goby社区第 21 篇技术分享文章

全文共：6700 字   预计阅读时间：17 分钟

**自我介绍**：大家好，我是 su18。

无论是个人博客还是社区，已经很久没写技术文章了，原因有很多，时间、精力、心态等等。但在开源社区也算比较活跃，由于工作需要，今年 6 月份我编写并开源了一个项目 ysuserial，在原项目的基础上进行了优化、处理，并增添了很多新功能。

在随后的日子里，我不定期的把在网上看到的、学习到的、研究出来的内容实现并汇总一部分在这个项目里，除了反序列化相关的技术外，我还着重在项目中添加了直接打入内存马的功能，目前项目中已经支持了各种各样常见的内存马，虽然公开的代码在利用上并不是特别深入，但很通用及全面，并经过多个版本的测试。

关于内存马相关的技术文章，我曾经也写过两篇 《JavaWeb 内存马一周目通关攻略》、《JavaWeb 内存马二周目通关攻略》发表在个人博客上，从技术上介绍了常见的几种内存马的实现，事实上这个系列还可以写很多篇，并且可以持续进行深入。去年我也曾经站在 RASP 的角度写过内存马的查杀和防御项目，也分享过一些 PPT。

后来随着时间的推移，我又看到了很多师傅、厂商及平台在实战中使用的不同的内存马的实现，包括不同中间件、不同框架、CMS 等可利用的内存马。我发现大家都不局限于现有的模式，思维发散，从植入、利用、流量上面都进行了很多的 DIY。

再后来我意识到，内存马的使用已经越来越普及，相关的文章也越来越多，但即便如此，很多师傅在咨询我相关的问题时，还是感觉对相关的概念有所模糊，而且在技术的使用上，还是存在着一些不低的门槛，所以这次我打算从一些新的角度切入，再谈谈相关的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) **01 前言**

如果要给 Webshell 分个等级，JavaWeb 内存马一定是现阶段当之无愧的 Shell 之王，”它”何德何能？

传统的 Webshell 后门，无论如何花费心思隐藏、如何变化，在现有的防御措施下都已经无法有效长期在目标系统内存留，防御措施简单列举：

* 对于终端安全：有文件监控、防篡改、EDR；
* 对于后门：有 Webshell 查杀、流量监测；
* 对于网络层面：有防火墙防止反连、反向代理系统隐藏真实 IP；
* 等等。

目前主流的防御措施针对 Webshell 的静态检出率在 90% 以上，在部分环境下甚至完全无法落地，防御方可以做到快速应急响应。正因为这些限制，内存马技术得以诞生并快速发展，无文件攻击、内存 Webshell、进程注入等基于内存的攻击手段也受到了越来越多的师傅青睐，在实战环境中已占得一席之地。可以毫不夸张的说，内存马相关技术将会是未来渗透工程师必须要会使用的安全技术。

本篇名为《JavaWeb 内存马 【认知篇】》，为什么是Java？

1. 对于企业级用户来讲，Java 是范围最大、使用最广、生态最全的编程语言，因此使用 Java 开发的中间件也是最多的，使用的人也是最多的；

2. Java 安全目标行业关注较多，研究较多。

---

文章来源: http://mp.weixin.qq.com/s?\_\_biz=MzI4MzcwNTAzOQ==&mid=2247521497&idx=1&sn=50e062aa20930102e6b787711d0e214a&chksm=eb847f79dcf3f66f1ac0d14065fdef2576393e9142f36c5add4e738eebbf3b71410a79e759ef&mpshare=1&scene=1&srcid=1209niNVcQFMD7zQt6BUKPQ1&sharer\_sharetime=1670662584820&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)