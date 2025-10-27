---
title: BlackHat Asia 2023 武器库| 开源工作负载解决方案Elkeid
url: https://www.anquanke.com/post/id/288765
source: 安全客-有思想的安全新媒体
date: 2023-05-24
fetch_date: 2025-10-04T11:36:37.831013
---

# BlackHat Asia 2023 武器库| 开源工作负载解决方案Elkeid

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# BlackHat Asia 2023 武器库| 开源工作负载解决方案Elkeid

阅读量**368343**

发布时间 : 2023-05-23 17:17:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

北京时间5月11日-12日，Black Hat Asia 2023（亚洲黑帽大会）在新加坡举办。Black Hat大会被公认为世界信息安全行业的顶级盛会，每年分别在美国、欧洲、亚洲各举办一次安全信息技术峰会。今年和往年一样有众多值得期待的精彩议题的环节，包括分享的议题（Briefings），武器库（Arsenal ），活动大厅（Business Hall ） 。

每年的武器库（Arsenal ）环节会聚集一批安全研究员，为其提供在黑帽社区展示开源工具。2023年的武器库（Arsenal ）涵盖数据取证和事件响应、代码评估、网络攻击/防御、逆向工程等16个方向。

![]()
来自字节跳动内部最佳实践的开源解决方案Elkeid，入选数据取证和事件响应武器库类目。Elkeid可满足主机、容器集群、Serverless等多种工作负载的安全需求。
![]()

# Elkeid的介绍

随着企业业务云化、容器化、云原生化的推进，企业的基础架构与安全需求也在不断的复杂化，并且伴随着新的技术方案的出现，也通常会伴随着新的安全风险，在这样的大背景下，我们希望能够有一套解决方案，能够满足不同工作负载下的安全需求，于是Elkeid诞生了。

## Elkeid的整体架构

![]()

## Elkeid的功能

Elkeid将下方能力整合到一个平台中，以满足不同工作负载复杂的安全需求，同时也实现了多组件能力的关联。

* · Elkeid 具有出色的内核态Runtime行为采集能力，这意味着对于部署的宿主机与其上的容器内的恶意行为均具有识别检测能力。
* · Elkeid 在用户态支持多维度的资产采集、日志采集、恶意文件识别、风险发现等功能。
* · 对于正在运行的业务Elkeid具有RASP能力，可以注入到业务进程中进行反入侵保护，不仅运维人员不需要再安装Agent，业务也不需要重启。
* · 对于K8s本身，Elkeid支持采集到K8s Audit Log，对K8s系统进行入侵检测和风险识别。
* · Elkeid的规则引擎Elkeid HUB也可以很好的与外部多系统对接。

## Elkeid性能如何

* · 目前，Elkeid 完整版本部署规模已达到百万级，覆盖了包括今日头条、抖音、西瓜视频等多个业务线。其稳定性/性能/数据采集能力/检测能力/溯源能力等均得到了实战验证，均有不俗表现。
* · Elkeid 在字节跳动内部的整体策略ATT&CK覆盖率目前已达到56%。
* · 用户态Agent在内部使用平均CPU占用小于1%单核；内存小于30MB。

# 如何使用Elkeid

开源地址：
<https://github.com/bytedance/Elkeid>

文档中心：
<https://elkeid.bytedance.com/>

# 开源后续

目前 Elkeid 的商业化版本已经上线字节跳动旗下的云平台火山引擎，商业化名称为火山引擎CWPP，CWPP从设计之初便遵循为物理机、虚拟机、容器和无服务器工作负载提供一致的保护和可见性的原则。将主机安全、RASP、阻断与响应能力、追溯能力通过插件的方式整合在一个agent上，同时对多云和混合云下也很好的支持，欢迎感兴趣的朋友们点击阅读全文体验。

Elkeid 也会长期维护更新，欢迎各位同行一起沟通交流。欢迎大家通过 GitHub 或飞书扫码加入字节官方 Elkeid 交流群，进行后续的交流和反馈。
![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**火山引擎云安全**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288765](/post/id/288765)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [字节跳动](/tag/%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8)
* [主机安全](/tag/%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8)
* [容器安全](/tag/%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8)
* [多工作负载](/tag/%E5%A4%9A%E5%B7%A5%E4%BD%9C%E8%B4%9F%E8%BD%BD)

**+1**9赞

收藏

![](https://p3.ssl.qhimg.com/t01d7c5cb6fdb04a6cc.png)火山引擎云安全

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t01d7c5cb6fdb04a6cc.png)](/member.html?memberId=165382)

[火山引擎云安全](/member.html?memberId=165382)

火山引擎云安全产品是字节跳动旗下的企业级安全技术服务产品

* 文章
* **40**

* 粉丝
* **4**

### TA的文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [广汽集团×火山引擎：出海合规助力企业新增长](/post/id/311498)

  2025-08-26 10:17:09
* ##### [智能体防御 | 一文了解3种系统提示词加固方法](/post/id/311279)

  2025-08-18 16:34:50

### 相关文章

* ##### [Kubernetes RBAC 最佳安全实践](/post/id/300925)

  2024-10-15 21:29:20
* ##### [BlackHat USA 2024 | vArmor云原生容器沙箱](/post/id/299446)

  2024-08-23 11:17:43
* ##### [一个未公开的容器逃逸方式](/post/id/290540)

  2023-09-07 18:22:32
* ##### [正式开源！字节安全团队自研云原生容器沙箱 vArmor](/post/id/290482)

  2023-08-22 17:08:29
* ##### [机密计算峰会2023 | 打通数据孤岛的PPML能力](/post/id/289673)

  2023-07-12 18:22:34
* ##### [云原生安全2.X 进化论系列|云原生安全2.X未来展望（4）](/post/id/287247)

  2023-03-28 15:22:31
* ##### [云原生安全2.X 进化论系列|云原生安全2.X落地实操（3）](/post/id/286819)

  2023-02-28 17:30:23

### 热门推荐

文章目录

* [Elkeid的整体架构](#h2-0)
* [Elkeid的功能](#h2-1)
* [Elkeid性能如何](#h2-2)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)