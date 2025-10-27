---
title: Tinyproxy曝出严重漏洞，影响全球52000台主机
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247543592&idx=2&sn=36a0c4efffe2c6e20d2b1b7a5b2b15b1&chksm=c1e9a779f69e2e6f3aadb5f0ab593fb5828ec25c048956d6aa81ef7751a99c1383490e8cd643&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-05-09
fetch_date: 2025-10-06T17:17:10.081948
---

# Tinyproxy曝出严重漏洞，影响全球52000台主机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvppIavZMWw8ThqE48ITLDoK8WCxBLPhcC5PWUn8icJcjvm47zfxgK5HPsYFvFZIrZdRD6iayvfiar7A/0?wx_fmt=jpeg)

# Tinyproxy曝出严重漏洞，影响全球52000台主机

关键基础设施安全应急响应中心

近日，攻击面管理公司 Censys 分享了一组数据：截至 2024 年 5 月 3 日，在90310台主机中，有 52000 台（约占 57%）运行着有漏洞的 Tinyproxy 版本。

这些可能受到漏洞影响的主机分布于美国（32846 台）、韩国（18358 台）、中国（7808 台）、法国（5208 台）和德国（3680 台）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ib2adDiaSzFJ8oqFMDc3LhgUuqnGSOaa8GjdHgOxlVTXxdjeRrlQO4mwUk5kf42Cxcq0cLEVDc246Q/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

该漏洞是HTTP/HTTPS代理工具中一个未修补的重要安全漏洞，被追踪为 CVE-2023-49606，CVSS 得分为 9.8，Cisco Talos 将其描述为一个影响 1.10.0 和 1.11.1 版本（即最新版本）的免用漏洞。

Talos在上周的一份报告中提到：攻击者可通过精心构造的HTTP头触发先前释放内存的重复使用，导致内存破坏且可能导致远程代码执行。攻击者需要发送未经身份验证的HTTP请求以触发此漏洞。

换句话说，未经身份验证的威胁行为者可以发送特制的 HTTP 连接头，从而引发内存破坏，导致远程代码执行。

Tinyproxy 是一个轻量级的开源 HTTP 代理守护程序，专注于简单性和效率。根据 HTTP 规范，客户端提供的标头表示代理在最终 HTTP 请求中必须删除的 HTTP 标头列表。代理从请求中删除这些 HTTP 标头，向远程服务器执行请求，并将响应发送回客户端。Tinyproxy 在函数中正是这样做的：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ib2adDiaSzFJ8oqFMDc3LhgU058TkXvLEXicdQiaXOV7jLBTMPpkwjqHsDpZVa1q28dSJWDKvgJrBA3w/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

首先，我们应该注意到客户端发送的 HTTP 标头驻留在键值存储中。该代码搜索 和 标头，并在 （1） 处获取它们的值，如前所述，这是一系列要删除的 HTTP 标头。客户端列出的每个 HTTP 标头在 （3） 处被删除。从本质上讲，和 标头值中的每个 HTTP 标头都用作从 中删除的键。最后，在 （4） 处，HTTP 标头本身被删除。

在函数中，我们看到：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ib2adDiaSzFJ8oqFMDc3LhgUWXbb4xWicdauCNFVoCklnOYvk8Afp25cVdnUe4UukXJL9dO9sVOpVicQ/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

对于具体提供的，其哈希值计算为 （5）。使用哈希值，在 （6） 处检索并释放键值的指针。最后，键本身从（7）的哈希图中删除。

现在考虑一下当客户端发送 HTTP 标头时会发生什么。出于演示目的，我们将它们区分为。在 （1） 处检索标头的值，这当然是 。在 （3） 处，该值用作 处的变量。在（5）处计算字符串的哈希值，与完全相同。请注意，哈希值也不区分大小写。在 （6） 处，哈希用于检索和释放 HTTP 标头值的指针，即 。因此，此时代码已释放了 的内存。在 （7） 处，现在包含过时指针的变量被重用，从而导致释放后使用方案。

很明显，此漏洞可用于执行内存损坏并获得代码执行权限。

去年 12 月 22 日，塔洛斯公司报告了这一漏洞，并发布了该漏洞的概念验证（PoC），描述了如何利用解析 HTTP 连接的问题来触发崩溃，并在某些情况下执行代码。

Tinyproxy 的维护者在上周末提交的一组文件中，指责 Talos 将报告发送到了一个已经不再使用的电子邮件地址，并补充说他们是在 2024 年 5 月 5 日被 Debian Tinyproxy 软件包维护者发现的。

rofl0r 提到：没有人在 GitHub 上提交问题，也没有人在提及的 IRC 聊天中提到漏洞。如果在 Github 或 IRC 上报告了该问题，该漏洞会在一天内得到修复。该公司建议用户在最新版本发布后及时更新。

**参考资料：**

https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html

https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过