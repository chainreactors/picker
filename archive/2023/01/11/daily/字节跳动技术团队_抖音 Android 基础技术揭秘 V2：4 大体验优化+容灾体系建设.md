---
title: 抖音 Android 基础技术揭秘 V2：4 大体验优化+容灾体系建设
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247501089&idx=1&sn=23466e315f1dd0fd68b3d3cb283417aa&chksm=e9d30ec3dea487d5b4e314f798d1c7d8da42df91ace32b85026e0575cefc5fa16930a88a1812&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2023-01-11
fetch_date: 2025-10-04T03:32:52.653442
---

# 抖音 Android 基础技术揭秘 V2：4 大体验优化+容灾体系建设

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOiaiaq2JEnWlIewMiagfV9F4vQOStDIvQTgic3tmYUfhN9NjhcqfpmKHl4Hrfic6csVPP9K8tXE8BGgXuA/0?wx_fmt=jpeg)

# 抖音 Android 基础技术揭秘 V2：4 大体验优化+容灾体系建设

等你报名的

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

在 12 月 10 日举办的字节跳动技术沙龙首期『抖音 Android 基础技术大揭秘』专场上，来自抖音基础技术 Android 团队的工程师们体系性地向业界分享了包括《抖音大型应用架构演进与思考》《抖音稳定性优化思路和疑难案例实战分析》《抖音启动优化实践》《抖音包体积优化体系建设》《抖音端智能优化用户体验的探索和实践》在内的技术实践，受到了广大 Android 工程师们的好评。

然而关于 Android 基础技术的难题仍未穷尽——内存优化怎么做？网络体验如何极致优化？播放体验优化如何畅享丝滑？功耗优化如何解决用户电量焦虑？线上容灾体系又该如何建设？

2 月 4 日，『抖音 Android 基础技术大揭秘』沙龙第二期重磅来袭，用一场实践驱动的技术分享开启你的新年技术之旅。本期字节跳动技术沙龙免费报名通道现已开启，**戳文末阅读原文或扫描长图海报二维码即可报名预约直播**！除了一下午的沉浸式技术分享，我们还为参会者准备了精美的礼品福利抽奖，千万别错过！

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiaiaq2JEnWlIewMiagfV9F4vQ3pMW3Ub8qGttJtl9ZECTrZjsvWopUp9YCz4yaQ0cZ8gF22iaMhupwwA/640?wx_fmt=png)

# 1. 演讲主题

## 1.1 抖音内存优化实践

### 内容简介

内存作为 App 运行中的一种全局资源，间接影响性能体验，直接影响稳定性体验，是影响用户体验关键因素之一。此次分享主要讲述抖音基础技术团队如何通过工具、流程建设，疑难问题攻坚以及通用优化黑科技探索几个方向解决内存带来的稳定性和性能问题。

### 精彩看点

* 初级工程师可以了解内存泄漏的本质和不同类型的 OOM 常见解决方法。
* 中级工程师可了解抖音内存优化在性能提升方向的建设和思路。
* 高级工程师可了解抖音在内存通用优化黑科技的建设及解决方案。

### 讲师信息

**潘林林丨** **抖音基础技术 Android 架构师**

2016 年本科毕业，在毕业之前和初期主导和参与多款 App 开发，14 年便有独立制作的 App 上传至应用市场并取得累计超过 10w 次的下载量。在 17 年之后进入手机厂商工作，前后参与系统和相机子系统的稳定性和性能优化，21 年初进入字节参与质量方向稳定性和内存的优化。

## 1.2 抖音网络体验优化实践

### 内容简介

网络能力是一个 App 的重要基础能力之一，直接关系到 App 的可用性和用户的基本体验。针对网络能力的优化可以显著提升业务指标，也可以直接降低公司的支出成本。本次分享主要从网络体验、网络成本和研发效能等方向展开，分享优化的思路及实践案例。

### 精彩看点

* 初级工程师可以了解请求的发送流程和一些通用优化策略。
* 中级工程师可以了解如何根据业务的监控数据制定优化策略。
* 高级工程师可以了解抖音网络体验优化的长期规划及最新进展。

### 讲师信息

**谈晶晶丨** **抖音** **基础技术 Android 架构师**

毕业于南京大学，先后就职于 Marvell、Dynosense、爱奇艺等公司，并于 2022 年加入字节跳动抖音 Android 客户端基础技术团队，目前专注于抖音 Android 的网络体验优化工作，对 Android 网络优化有较为丰富的经验。

## 1.3 抖音客户端容灾体系建设实践

### 内容简介

抖音作为承载公司重要业务的日活亿级别大型 App，每天 App 承载业务都在不断增长、工程规模和研发人数都呈爆发型增长。如何保证 App 的稳定性，使其成为业务开展的稳定基石，成为了基础技术-质量团队重要课题。此次分享主要围绕线上容灾的最佳实践，以及这些实践背后的质量体系建设思路进行展开。

### 精彩看点

* 了解客户端线上容灾体系是什么、它的价值是什么。
* 了解抖音在客户端容灾体系方向的探索和实践，包括一些具体案例的思路和方案。
* 了解抖音在客户端容灾体系建设上的长线思路，并了解我们的最新探索方向。

### 讲师信息

**张雪飞丨** **抖音****基础技术 Android 架构师**

2015 年研究生毕业，先后就职于摩托罗拉、阿里巴巴并于 2021 年加入字节跳动抖音 Android 客户端基础技术团队，长期从事于 Android 底层相关工作，目前专注抖音客户端容灾体系建设相关工作。对 Android 大型 App 线上线下容灾有较为丰富的经验。

## 1.4 抖音播放体验优化实践

### 内容简介

视频播放作为抖音的基础功能，其体验的好坏直接关系到整个 App 的使用体验。本次分享将介绍抖音播放体验优化的开展思路，并分享首帧、卡顿等方向的优化案例。

### 精彩看点

* 初级工程师可以了解抖音播放体验的一些通用的优化策略。
* 中级工程师可以了解如何根据业务形态来进行特定的优化。
* 高级工程师可以了解抖音播放体验的优化思路以及最新进展。

### 讲师信息

**罗泽鑫丨** **抖音****基础技术 Android 资深工程师**

毕业于北京邮电大学，于 2017 年加入字节跳动，目前主要负责抖音播放体验的相关优化工作。

## 1.5 抖音功耗优化实践

### 内容简介

功耗是影响用户体验的重要因素，较高的功耗会引发用户的电量焦虑，也容易带来发热的不好体验，本次分享将介绍抖音功耗优化的思路与实践案例。

### 精彩看点

* 初级工程师可以了解功耗的基础概念和硬件概念。
* 中级工程师可以了解抖音在功耗优化的建设和思路。
* 高级工程师可以了解抖音功耗优化的长期思路和最近进展。

### 讲师信息

**高原丨** **抖音****基础技术 Android 资深工程师**

毕业于北京邮电大学，2015 年进入华为从事 Android 手机系统的功耗优化的工作，2021 年加入字节跳动，目前主要负责抖音的功耗体验优化工作。

# 2. 活动详情

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiaiaq2JEnWlIewMiagfV9F4vQKyIfWaJ7PVJO4FOkWQSZjboWppq7JfIKlO5B3F0nkh9V6Quc98YWEQ/640?wx_fmt=png)

# 3. 抖音 Android 基础技术系列沙龙

为了全面、体系化地向大家展示抖音 Android 端的技术和工程实践，后续将以每月一期的节奏与大家相约，总计 5 期，共 25 个 topic。如此珍贵的体系化分享，千万不要错过！

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiaiaq2JEnWlIewMiagfV9F4vQMNt1WUH9TuqiasCrUb8tTCORicRqvQtSbptianMk8cKFqJW8UwwZ7ta6g/640?wx_fmt=png)

# 4. 沙龙介绍

字节跳动技术沙龙，是由字节跳动技术社区 ByteTech 发起的，面向全行业开发者的技术交流活动。通过搭建一个包容、开放、自由的交流平台，促进前沿技术的普及与落地，帮助技术团队和开发者快速成长。字节跳动技术沙龙的技术分享来源于字节跳动一线技术专家，针对热点技术方向和实践总结，为技术团队和开发者呈现一场场可供参考的技术盛宴。

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC6RyGcCclHibMw08rYZOOtkfZud4IA4b3ORre5LScE0yBXTg19E6cQ4XbOP7iaWfVREuT3Dgxc4p3hw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7IHABFmuMlWQkSSzOMicicfBLfsdIjkOnDvssu6Znx4TTPsH8yZZNZ17hSbD95ww43fs5OFEppRTWg/640?wx_fmt=gif)

[● SpriteJS：图形库造轮子的那些事儿](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247501068&idx=1&sn=4839629ea06fa805b24196105f3e14c7&chksm=e9d30eeedea487f8fbae2564d764b525fef669df5613e46294d6a6a28e1edd7a341dec728c61&scene=21#wechat_redirect)

[● 从100w核到450w核：字节跳动超大规模云原生离线训练实践](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500979&idx=1&sn=880f9dd458a96709269756e1f64a4a40&chksm=e9d30f51dea48647408de90732a9abd1cc7a173e568b36d9b9a24b16d0ccde4c91112f96b504&scene=21#wechat_redirect)

[●](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)[【活动推荐】Flutter 深度用户，字节跳动如何落地实践？](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500979&idx=2&sn=0f9e0cbac39fd5942e4d9a5f0084cff4&chksm=e9d30f51dea48647496a4f79e7a285e5c66104beafc9e71d3fc68ae2d1ae6718e540cc47ee7d&scene=21#wechat_redirect)

[●](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)[火山引擎 DataLeap 的 Data Catalog 系统公有云实践](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500746&idx=1&sn=49798c1d670fb596acead96995d3f122&chksm=e9d30828dea4813ec70e9756bcf9c76b1e9f41c015f4469a0d93350289ad4cdd74d10eaa2cfe&scene=21#wechat_redirect)

****![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOia2iaibTtxS07yz5OzyDhIBx1qbKx6I2nU2hVIL34oAWvJ1aQTHgFKX8QzdhtFDq2sk19UxydLypTyA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)**阅读原文，限时免费报名！**

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