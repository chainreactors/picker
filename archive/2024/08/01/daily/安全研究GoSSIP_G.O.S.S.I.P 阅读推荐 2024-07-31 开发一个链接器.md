---
title: G.O.S.S.I.P 阅读推荐 2024-07-31 开发一个链接器
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498584&idx=1&sn=e6575e72bbbc3974b1564d1b397533db&chksm=c063d581f7145c9714b0f02603db68bded614e6bb58ab9e27daed735f43aaa31f1cd34f40f81&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-01
fetch_date: 2025-10-06T18:04:54.334541
---

# G.O.S.S.I.P 阅读推荐 2024-07-31 开发一个链接器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HAqB2EkXVPdxdFIGZ0AKHc69yWKmvKqDMTOv4icbDuA0rl5s32b80T0lTskULoZ7qEE57SWu9jJ2A/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-07-31 开发一个链接器

原创

G.O.S.S.I.P

安全研究GoSSIP

7月的最后一期阅读推荐，我们要介绍的是一系列来自清华博士的技术blog（https://jia.je/）中《开发一个链接器》系列文章：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HAqB2EkXVPdxdFIGZ0AKHcO0z0WBawNF3GeeXOoJJ7I3jl0oxPlticIsFgticANU94saWa7EQx9VWw/640?wx_fmt=png&from=appmsg)

尽管很多人可能都知道有两本很著名的书《Linker and Loader》和《程序员的自我修养——链接、装载与库》，但是关于链接器也就是linker应该怎么实现，书里面似乎并没有太多的细节。这大概是因为linker的工作看起来就是比较的枯燥无味，但是真正去做一遍，你会学到很多很多的细节（至少编辑部觉得以前这方面确实是眼高手低，纸上得来终觉浅）。而且《开发一个链接器》系列文章在写作上也很友好（毕竟清华博士），稍微理解这方面的技术细节就不会有什么阅读障碍（说实话，很多技术写作者的文笔是真心烂，所以你以后读不懂技术文章，首先怀疑一下是不是作者的小学语文就没及格）。

话不多说，我们进入文章的正题，这一系列文章一共四篇，内容承接关系也非常清楚：

1. 第一篇博客：支持单个 ELF 对象文件的链接

1. https://jia.je/software/2024/02/18/write-a-linker-1/

2. 第二篇博客：支持多个 ELF 对象文件的链接

1. https://jia.je/software/2024/03/30/write-a-linker-2/

3. 第三篇博客：支持生成动态库

1. https://jia.je/software/2024/04/06/write-a-linker-3/

4. 第四篇博客：支持动态链接

1. https://jia.je/software/2024/04/07/write-a-linker-4/

实际上，开发一个迷你版但是全功能（支持多个ELF对象文件链接、支持动态库生成、同时支持动态库与静态对象文件合并链接）的linker并不复杂，作者甚至只用了区区1000行的Rust代码就完成了这个工作：

https://github.com/jiegec/cold/tree/master/src

这么好的技术文章，不让更多人读到真是太可惜了！大家快快点赞和转发吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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