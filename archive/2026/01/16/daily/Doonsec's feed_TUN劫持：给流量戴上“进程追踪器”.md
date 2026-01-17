---
title: TUN劫持：给流量戴上“进程追踪器”
url: https://mp.weixin.qq.com/s/E2w1Z9BpYvlLNdKztDZyog
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:26:35.312615
---

# TUN劫持：给流量戴上“进程追踪器”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8q2Zg9sTVHFkB7BhJ3Hynel26YiaKTIUJOvwhgUpibkyodibPdthzpqb2Rw/0?wx_fmt=jpeg)

# TUN劫持：给流量戴上“进程追踪器”

原创

YAK
YAK

Yak Project

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPxhq9ZDnzI4ge0SwCTAMbAvAI5yWUnoBLqzicqmJAtuUiaygZO5lqSGJQ/640?wx_fmt=webp&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qIFWCsBicNEs0bkr4L86iaGxKnADL4fJcE0EpQmbeRcbMPoGC7K3hbBDA/640?wx_fmt=png&from=appmsg)

在上一篇文章中，我们讨论了[如何利用 TUN 设备构建一个基础的流量拦截环境（点击即可查看）。](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247529213&idx=1&sn=62ce90504e95ce98ad15d1e4fb8a055b&scene=21#wechat_redirect)然而，在实际的渗透测试或安全开发场景中，我们经常会遇到一个痛点：**流量是“盲目”的**。

当我们开启 TUN 劫持后，看到的是源源不断的 IP 包和 TCP/UDP 流。但在复杂的现代操作系统中，后台可能有数十个进程在同时联网。如果你只想分析 Chrome 的某个插件流量，或者想审计某个特定恶意软件的连接行为，从海量的 IP 数据中手动筛选目标无疑是大海捞针。

本次更新，我们的 TUN 劫持引入了**进程监控（Process Monitoring）**功能。它打破了网络层与应用层之间的壁垒，让你可以实时看到“哪个进程正在连接哪个 IP”，并实现自动化的流量劫持。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qLkSbuk4bPwhLhXuUN9muEkQOyy9EstPbD8phKpOhmQOsEFXG0A9skQ/640?wx_fmt=png&from=appmsg)

传统的抓包工具往往只关注包内容，而我们的工具在网络层拦截的同时，通过系统底层的调用，实时关联了网络连接与进程 PID。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8q6Ayop4QPtGv8m4JD0xnodAcWiaAvicUTaS7J1zRicTuYpk7AI7pfszCKA/640?wx_fmt=png&from=appmsg)

在工具的“进程列表”选项卡中，你可以看到当前系统中所有活跃的进程。

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qoIrqNV0m9cNYdwp9GdRtLxEK6hL8F45w9tzWaOdBHy84KDtBCSZlgg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qlXArk92su6jWUsmm7k3kJliaOtM2iccF0H3eMD5dFUZCqLRoQ8g9LZtw/640?wx_fmt=png&from=appmsg)

点击“查看信息”，你可以深入到进程内部。工具会展示该进程当前持有的所有 连接，包括源地址、目的地址、目标域名（如有）。这对于识别 CDN 流量或隐藏的 API 调用非常有帮助。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8ql4fbXiakJyfdkdUw8YLl2rskeQ2gwDvoucC4eWSuAxOgRpCDTrc4Zbw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qdufnGeIcHUm0hkQAQjo77KcwOWCSPJoqAic50ibdzGbsJTIG3EKnMsnA/640?wx_fmt=png&from=appmsg)

在发现感兴趣的连接后，如何快速将其导入劫持流程？

在“信息详情”窗口中，每个连接条目后都有一个“添加路由”按钮。一旦点击，该目的 IP 会立刻被推送到我们的 **TUN****路由表**中。此时，该 IP 的所有流量都将通过我们的 TUN 设备进行强行劫持。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8q0q6N9ibfbUibPMWsZkfeJRZKZ5E127rYrLsIHtRQicQSGlW6OBxGl61Og/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8quhVFNiajiax3rcQNyfpVgzVcTF9g4EZPkia6ORZTUkPPdHZ5OFgZLSpibg/640?wx_fmt=png&from=appmsg)

在之前的 tun 劫持模块中，用户需要手动发现一个 IP，然后手动将其添加到路由表中。但在面对现代复杂应用时，这种操作模式已经不够使用了。

本次更新关键在于实现了**针对进程的持续劫持**。无论你是指定一个具体的 **PID**，还是通过 **Glob 模式** 匹配一组进程，工具都会进入一个自动化的闭环逻辑，持续添加目标进程的连接到劫持目标中。

**1、为什么“持续性”是刚需？**

以 Chrome 为例，它是一个典型的多进程、高频连接应用。

* **连接瞬时性：** 很多 API 请求或短连接在几秒钟内就结束了。当你手动查到它的 IP 并准备添加路由时，连接可能已经关闭。
* **域名多变：** 现代 Web 应用背后是成百上千个 CDN 节点和微服务。
* **PID 漂移：** 渲染进程（Renderer）经常会因为页面刷新或标签页关闭而销毁并重启，产生全新的 PID。

如果靠人工去“盯”，效率极低。我们的“持续劫持”功能将这个过程变成了**自动进行。**

**2、Glob 模式：大规模自动化拦截的入口**

不同于传统的精确匹配，Glob 模式允许你利用通配符（如 *`*Chrome*`*、*`Electron`*）一次性覆盖整个应用族群。

* **一键锁定：** 输入 *`*Chrome*`*，工具会自动关联当前所有的 Chrome 进程。
* **新进程自动收纳：** 最重要的是，如果在劫持过程中 Chrome 启动了新的子进程（例如你新开了一个标签页），Glob 监控逻辑会**实时感知**到这个新进程的加入，并自动将其纳入劫持范围。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8quwK2KMxsC7BfH4TAwcrt4v0JJJqfISRnIoCwvMpl7W5lXeV0gOTvwg/640?wx_fmt=png&from=appmsg)

当你在工具中点击“劫持”后，后台会启动如下自动化流水线：

**1、动态扫描与 Glob 模糊匹配**

工具后台维持着一个扫描任务，它会定期轮询系统进程树。通过引入 **Glob 模式匹配**，你不再需要死盯着某个 PID，只需输入期望的匹配字符串，就会自动将所有匹配到的进程拉入“劫持预备役”。

**2、一进程一协程**

* 每当扫描器发现符合条件的新进程，都会为其启动一个协程持续监控此进程
* 该协程会监控目标进程的 网络连接状态。一旦该进程有新的的网络连接，协程会立刻捕获其目标 IP。
* 捕获到 IP 后，无需人工干预，会自动将其写入路由表并指向 TUN 设备。

通过这种设计，你只需要在界面上点一次“劫持”，剩下的工作——**发现新进程、启动监控协程、提取新连接****IP****、下发****路由表**——全部自动完成。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qNnjOV0MoZ8ok8JmZIw8GEiaGaZq29A1dDqL59nu5LSrJzYjR9vWDK3A/640?wx_fmt=png&from=appmsg)

**1、启动环境：** 打开工具，开启 TUN 设备。

**2、设置规则：** 在进程列表搜索框输入 *`*Chrome*`*，点击“劫持”。

**3、触发流量：** 在 Chrome 中访问任意网站。

**4、实时审计：** 点击“已劫持任务”中的“查看信息”，你会发现工具已经自动捕获了 Chrome 正在访问的后端服务器 IP。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qib2AicyKQzZL6lhz5Ciaf021n6RFlwOMTkiaHljEAf6qVQhPOSk7XmYOjA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qwEB3esaDBnFULoAVez0MdAp0ulohzdicbxZarPHiaEuNTdXfEXqgBn7Q/640?wx_fmt=jpeg)

本次“进程监控”的更新，标志着我们的 TUN 劫持工具从一个“底层网络工具”进化为了一个“应用级分析利器”。通过 **Glob 模式匹配** 和 **实时路由添加**，我们极大缩短了从发现目标到实施劫持的操作链路。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeniamzzt7HujbP1h9ojOV8qee9xAByDA1Orfl6UsHE5J6PVttehRAswMu2bpXOwO2rr03QFk1UuFg/640?wx_fmt=png&from=appmsg)

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![图片](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

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