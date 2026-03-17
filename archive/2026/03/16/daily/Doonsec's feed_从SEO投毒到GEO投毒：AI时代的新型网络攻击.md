---
title: 从SEO投毒到GEO投毒：AI时代的新型网络攻击
url: https://mp.weixin.qq.com/s/i-2xBlfz0rtugbMgzA4olw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:11:00.068636
---

# 从SEO投毒到GEO投毒：AI时代的新型网络攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibSZAw0490dXyl0r89fcYtU950UYMicyuMLUNI074qStUgZ6t3lgC3j0t7YPiaeLzqxcno1UNpxXXy1B3D8icTr7sjb6JKAN0BUxKA/0?wx_fmt=jpeg)

# 从SEO投毒到GEO投毒：AI时代的新型网络攻击

原创

兰花豆
兰花豆

兰花豆说网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AiaxibnzDXa1asshEnCgBMF2CiayVQfx8e9XK6C8MH2YkouAoA6DRk6ibnPNQ3eSY4Ejfibh8hy8tOGNLnVoicJlWnIg/640?wx_fmt=gif&from=appmsg)![]()

过去十多年，网络攻击的主要方式往往集中在漏洞利用、钓鱼邮件、恶意软件传播等技术手段上。但随着互联网信息获取方式的变化，攻击者开始把目标转向一个新的入口——信息获取渠道本身。

传统互联网时代，人们依赖搜索引擎获取信息；而在AI时代，越来越多的人开始直接向大模型提问。于是，一种新的攻击模式逐渐出现：SEO投毒 + GEO投毒联合攻击。

简单来说：

● SEO投毒：污染搜索引擎结果

● GEO投毒：污染生成式AI模型的知识来源

一旦成功，用户无论是搜索信息还是向AI提问，都有可能获得被攻击者操控的答案。

## 一、什么是SEO投毒攻击

SEO投毒是一种利用搜索引擎优化（SEO）规则进行攻击的技术。攻击者通过操控网页内容、关键词、外链等方式，让恶意网站在搜索引擎结果中排名靠前，从而诱导用户访问。

简单理解就是：

黑客利用搜索引擎规则，把恶意网站“优化”到搜索结果前列。

### 1 攻击原理

搜索引擎在进行网页排名时，会参考很多因素，例如：

● 关键词相关性

● 页面内容质量

● 外链数量

● 网站权威性

攻击者会利用这些规则，通过技术手段操控排名。

常见方式包括：

关键词堆叠

在页面中大量植入热门关键词，例如：

● VPN下载

● Office激活

● AI工具免费版

● 网络安全工具下载

批量生成内容

利用AI自动生成大量技术文章或教程页面，以提升页面数量和搜索权重。

外链农场

通过大量互相引用的网站，提高页面权重。

入侵合法网站

攻击者还会入侵一些正常网站，在其内部植入恶意页面，从而借助合法网站的信誉提升排名。

### 2 攻击流程

SEO投毒通常遵循以下流程：

● 注册大量域名或入侵网站

● 批量生成关键词内容页面

● 通过SEO技术提升搜索排名

● 用户点击进入恶意页面

● 下载木马或进入钓鱼网站

## 二、什么是GEO投毒攻击

随着大模型应用的普及，人们越来越依赖AI获取信息。例如：

● “推荐一款免费的远程控制软件”

● “哪里可以下载某某工具？”

● “如何破解某个软件？”

很多AI工具会直接给出网站链接或下载建议。

于是，一种新的攻击技术出现——GEO投毒（Generative Engine Optimization Poisoning）。

GEO原本是指针对AI搜索和生成式引擎进行内容优化的技术。但攻击者将其用于恶意目的，通过向大模型训练语料或引用数据中注入恶意内容，使AI生成带有恶意信息的回答。

简单理解：

如果SEO投毒是污染搜索引擎，那么GEO投毒就是污染AI答案。

## 三、GEO投毒的攻击思路

GEO投毒通常通过以下方式实现。

### 1 构造大量“可信内容”

攻击者会在互联网发布大量看似正规的内容，例如：

● 技术博客

● 开源项目说明

● 软件下载教程

● AI工具推荐文章

这些内容表面上是正常技术资料，但其中会嵌入恶意链接或下载地址。

### 2 进入AI训练或检索数据

很多大模型使用以下数据来源：

● 开放互联网数据

● 技术论坛

● GitHub项目

● 博客平台

当攻击者发布的内容被这些数据源收录后，就有可能进入AI训练数据或检索数据库。

### 3 影响AI生成结果

当用户询问类似问题时，例如：

“推荐一个免费的远程桌面工具”

AI模型可能会引用被投毒的内容，从而推荐：

● 带木马的软件

● 钓鱼网站

● 恶意下载地址

用户往往对AI答案更加信任，因此更容易中招。

## 四、SEO投毒与GEO投毒的危害

随着AI搜索逐渐普及，这两种攻击方式的危害正在快速扩大。

### 1 恶意软件传播规模化

攻击者可以通过搜索结果或AI回答传播：

● 信息窃取木马

● 挖矿程序

● 勒索软件

● 远控木马

传播范围可能达到全球。

### 2 AI可信度被破坏

如果AI推荐的资源带有恶意内容，会严重影响用户对AI系统的信任。

### 3 企业品牌被冒用

攻击者可能伪造：

● 企业官网

● 技术工具下载站

● 官方软件更新站

用户很难辨别真假。

### 4 供应链攻击风险增加

开发者如果从AI推荐的网站下载工具或代码，也可能把恶意组件引入软件供应链。

## 五、如何防御SEO与GEO投毒

面对这种新型攻击，需要从多个层面进行防护。

### 1 企业层面

加强品牌监测

持续监控：

● 企业品牌关键词

● 产品名称

● 软件名称

及时发现仿冒网站。

加强威胁情报监测

通过威胁情报平台识别：

● 仿冒域名

● 恶意下载站

● 钓鱼网站

官方渠道明确

企业应明确：

● 官方下载地址

● 官方技术文档

● 官方客服渠道

避免用户从非官方渠道获取资源。

### 2 AI平台层面

AI厂商需要加强：

数据清洗

在模型训练数据中识别：

● 恶意链接

● 可疑软件下载站

● 垃圾内容

答案安全检测

在AI生成答案时对外部链接进行安全检测。

可信来源机制

优先引用：

● 官方网站

● 权威技术社区

● 可信软件仓库

### 3 个人用户层面

普通用户也应提高安全意识：

尽量使用官方渠道下载软件

不要从搜索结果中的不明网站下载。

不要完全相信AI推荐链接

即使是AI给出的链接，也要核实来源。

警惕“破解版”“免费激活工具”

很多恶意软件正是通过这些关键词传播。

## 六、结语

互联网的信息入口正在发生变化：

● 过去是搜索引擎时代

● 现在正在进入AI生成时代

攻击者也在快速适应这种变化，从SEO投毒升级到GEO投毒。

当搜索结果和AI答案都可能被污染时，网络安全面临新的挑战。

未来的安全防御，不仅要保护系统和网络，还要保护信息生态本身的可信度。

因为在AI时代，被污染的信息，本身就可能成为最危险的攻击武器。

END

了解更多知识，欢迎关注ima知识库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibRnTKgSeH2iaYbwibJRx9I0ogNjO7wiaGPrNcsp8wlPHbZkFYS06bN186BqzrDTepEkOcl9KC38ibvfxV4E6iazLMPjiaLDqFsgx4rSg/640?wx_fmt=png&from=appmsg)

推荐阅读

[十五五规划里的网络安全机会在哪里？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492741&idx=1&sn=70ba67bfad6a41a469006e8d43f0b8b4&scene=21#wechat_redirect)

2026-03-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibT9lfHoZ7icDHsBkIMLPhI23eqicRibgYYCJ4IZkwoic8auiarvicsoUQB91johctUtnmuRbiazPoWGr9UbWXoXrGrdE32JQVNTAic9JaE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492741&idx=1&sn=70ba67bfad6a41a469006e8d43f0b8b4&scene=21#wechat_redirect)

[养“龙虾”的现实与困境：从小龙虾养殖谈到OpenClaw的安全边界](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492736&idx=1&sn=8c0817afe1d8aa29346c34907fa9cf5c&scene=21#wechat_redirect)

2026-03-13

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibShWooXSqhHOyCzfMKDe6CmMsVSTfAZc6przky2d33TG7xiaFXQleOtLiakdF6hlv6jJ6LYBeAOQ6aVkD6MIMJV58SV7sicXGFPnA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492736&idx=1&sn=8c0817afe1d8aa29346c34907fa9cf5c&scene=21#wechat_redirect)

[IP数据云——Geo IP毫秒级数据响应，全球IPv4/IPv6双栈支持！](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492728&idx=1&sn=1b16a569ca28a4154646779118d2496f&scene=21#wechat_redirect)

2026-03-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibRUqONx6o2EaS06ljTjOUAZcUtBvdf2DZpbPSOmaQliaJys55fkcqbsKJyCkTjiaTMGl9enT6ic1TpcS22AhalhZibMicibVATB6VXAI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492728&idx=1&sn=1b16a569ca28a4154646779118d2496f&scene=21#wechat_redirect)

[安全大模型是怎么炼成的？一文讲透微调与对齐](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492705&idx=1&sn=d2c7a4ea7bc6413439407d5b205d5f26&scene=21#wechat_redirect)

2026-03-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibS78fvehVZuovBmpg85rjkjCSFK91IWaIkJzdsZTLNJI2EL99HticusGpscVB4f9LGjcD0vNMlTDHJ3GUt21jwLZQSIznqZLPDA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492705&idx=1&sn=d2c7a4ea7bc6413439407d5b205d5f26&scene=21#wechat_redirect)

[网安人士必知的机器学习之分类模型效果指标](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492698&idx=1&sn=ecad355f32b5811cdb6542f75524af09&scene=21#wechat_redirect)

2026-03-08

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTAFc568sbeADennhfGUibsUdfZqGCNWKUN3cSLxOGAXI0KGqYibTjDkDsjfDHDXqXXZicZYOFeQsQ1l9mZuPvskRc6LA92wPcSFc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492698&idx=1&sn=ecad355f32b5811cdb6542f75524af09&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

兰花豆说网络安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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