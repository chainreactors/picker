---
title: Flutter 深度用户，字节跳动如何落地实践？
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500568&idx=1&sn=762e7f3bb3937dbb87688241a46f1387&chksm=e9d308fadea481ece01284cbcca15c5b56d704f5c67135556b214702583f13cb419d13feb9f2&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2022-12-14
fetch_date: 2025-10-04T01:24:41.138972
---

# Flutter 深度用户，字节跳动如何落地实践？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOhf1Cth3SibjXnGdztjsu9qsKuQlu4iaDKr2Ko95DJU2IculgTG29SibSuhe7OgdOny7dKc3RzJ4qiabw/0?wx_fmt=jpeg)

# Flutter 深度用户，字节跳动如何落地实践？

等你报名的

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

『一次开发，多端运行』是研发同学所追求的极致效率，如何用一套代码逻辑解决 Android / iOS 双端的开发向来是客户端工程师们所头疼的问题。而在当前的跨平台开发范式中，由 Google 开源的 Flutter 成为了最受欢迎的方案之一。

在 2022 年 5 月举办的 Google I / O 大会上，Flutter 3.0 版本正式发布，开发者可以通过一个代码库立足 iOS、Android、Web、Windows、macOS、Linux 六大平台，大会数据显示目前全球已经有超过 50 万应用由 Flutter 构建完成。

字节跳动是 Flutter 的深度用户，早在其开源之初便投入了深度的使用、优化与反馈共建。截至 2021 年，字节跳动有超过 70 多款 App 使用 Flutter 开发，累计有超过 600 多位 Flutter 开发者。针对 Flutter 落地过程中出现过的包体积过大、性能收益不明显等问题，字节跳动技术团队均做了大量的优化，并向社区提报大量 PR 并被成功 merge。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhf1Cth3SibjXnGdztjsu9qsAebJLo76qd6RrpyVuuhmfabcHcLRmeTKIgfm8JY41oYNX6D8DZA1NQ/640?wx_fmt=png)

2023 年 1 月 14 日下午 2 点，字节跳动技术沙龙将作《深度解析 Flutter 技术探索与实践》主题分享，带来包括新一代渲染引擎 Impeller、Android 系统渲染线程 GLFunctor 的应用以及 HappinessX 开发套件强大功能等多个分享。此外，阿里集团 aliflutter 组织 Hummer 引擎技术专家也将作为特邀嘉宾带来精彩分享。本期沙龙线上直播免费报名通道已开启，**戳文末阅读原文或扫描长图海报二维码即可报名预约直播！**除了一下午的沉浸式技术分享，我们还为参会者准备了精美的礼品福利抽奖，千万别错过！

# 1. 演讲主题

## 1.1 深入理解 Impeller 渲染原理

### 演讲简介

本次演讲将首先介绍新一代渲染引擎 Impeller 的项目背景与架构设计，再对 Impeller 的渲染流程进行较为深入的分析，最后以具体例子来说明 Impeller 是如何将内容渲染出来的。

### 精彩看点

* 应用开发工程师可以了解 Impeller 项目的项目背景和基本原理。
* 引擎开发工程师可以了解 Impeller 的架构设计和渲染流程以及细节实现。

### 讲师信息

**章志坚：字节跳动** **Flutter** **Infra 工程师**

Flutter Member，Impeller Contributor，热爱 Flutter 技术，对 Flutter Engine 有着深入的理解，热爱开源，为Flutter Engine 贡献过 100 多个 PR（其中有 30 多个提交给了 Impeller）。

## 1.2 GLFunctor 在 Flutter 的探索与应用

### 演讲简介

首先介绍 Android 系统渲染线程的黑科技 GLFunctor 的原理，然后介绍我们如何利用 GLFunctor 来渲染 Flutter 页面，并优化 Flutter 的内存占用、解决 Flutter PlatformView 的疑难杂症，最后介绍实际应用中的落地效果。

### 精彩看点

* 加深对 Android RenderSurface、PlatformView 原理的理解
* 对 Flutter 等自渲染技术实现卡片、PlatformView 有一定借鉴作用

### 讲师信息

**王莹：字节跳动** **Flutter** **infra 工程师**

负责 Flutter 引擎方向相关工作，在 Flutter 基础设施建设、性能稳定性优化方面有丰富的经验。

## 1.3 Hummer 在复杂图片业务场景的优化

### 内容简介

1. Flutter 的图片模块的演进和现状
2. Hummer 针对实际业务场景的优化
3. Flutter 技术在图片业务的总结

### 精彩看点

* 业务开发人员能够了解图片业务的哪些问题是可以解决的
* 引擎开发人员能够了解某些优化的方向和技术

### 讲师信息

**曾锦和 - 阿里集团 aliflutter 组织** **Hummer** **引擎技术专家**

来自阿里集团智信事业群，aliflutter 组织 hummer 引擎、阿里 h5 前端组织 u4 webview 渲染引擎的核心成员。负责稳定性、内存、图片渲染等基础模块。在渲染引擎领域深耕多年，擅长使用各种技术解决复杂问题。

## 1.4 HappinessX 开发套件

### 演讲简介

Happinessx 提供了一套基于 GetX 极致简洁高效的 Flutter 业务开发范式，同时配套的 AS 插件帮助进一步建立开发规范，是 Flutter 业务开发的提效利器。

### 精彩看点

* 了解 Flutter 开发中 ，如何选用合适的状态管理方案，让开发更高效规范
* 利用 Android Studio 的 plugin，能做出哪些提效开发工具

### 讲师信息

**曾晶：****幸福里****客户端****工程师**

幸福里客户端开发，18 年开始重度使用flutter，涉及大型纯 flutter 工程开发，混合工程开发，flutter 基础建设，技术栈广泛

**乔文豪：****幸福里****客户端****工程师**

幸福里客户端开发，20 年开始使用 flutter，涉及纯 flutter 工程开发，混合工程开发，对 AS 插件有良好实践。

# 2. 活动详情

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhf1Cth3SibjXnGdztjsu9qsGboFTrfNo2aWALjTHjPY6TVRCXlNy7DY4oYMJOwwibhreIMyNRiaf4oA/640?wx_fmt=png)

# 3.关于我们

字节跳动技术沙龙，是由字节跳动技术社区 ByteTech 发起的，面向全行业开发者的技术交流活动。通过搭建一个包容、开放、自由的交流平台，促进前沿技术的普及与落地，帮助技术团队和开发者快速成长。字节跳动技术沙龙的技术分享来源于字节跳动一线技术专家，针对热点技术方向和实践总结，为技术团队和开发者呈现一场场可供参考的技术盛宴。

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC6RyGcCclHibMw08rYZOOtkfZud4IA4b3ORre5LScE0yBXTg19E6cQ4XbOP7iaWfVREuT3Dgxc4p3hw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7IHABFmuMlWQkSSzOMicicfBLfsdIjkOnDvssu6Znx4TTPsH8yZZNZ17hSbD95ww43fs5OFEppRTWg/640?wx_fmt=gif)

[● 性能提升 2.5 倍！字节开源高性能 C++ JSON 库 sonic-cpp](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500498&idx=1&sn=e01be5757c8912c8c166b79be9bfdddb&chksm=e9d30930dea480262e047ae22c4754d0e0e6053b044fef61481cb4ba9dff1cfb79c24d15c867&scene=21#wechat_redirect)

[●](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)[优先级反转那些事儿](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500476&idx=1&sn=988ab57a632a7bccfa310440fbd2cd48&chksm=e9d3095edea48048e641806c8ec570473d8834ea7159986c565bd6b0b6b3f22717d1e343854a&scene=21#wechat_redirect)

[●](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)[火山引擎 RTC 助力抖音百万并发“云侃球”](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500395&idx=1&sn=1d994b2e435976cf801aa1fc3a9be668&chksm=e9d30989dea4809fc341ca97c9c55b50a6540e4d24743c4c972551f4f10e3e4f2632d612e99a&scene=21#wechat_redirect)

[●](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)[一文读懂火山引擎云数据库产品及选型](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500361&idx=1&sn=520f559c59b684d836b4ce1b101bc62c&chksm=e9d309abdea480bd022a1e7b3006b9c652fc6ae71696c5018e541fbed38d728896be24d34589&scene=21#wechat_redirect)

****![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOia2iaibTtxS07yz5OzyDhIBx1qbKx6I2nU2hVIL34oAWvJ1aQTHgFKX8QzdhtFDq2sk19UxydLypTyA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)**“阅读原文”，限时免费报名！**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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