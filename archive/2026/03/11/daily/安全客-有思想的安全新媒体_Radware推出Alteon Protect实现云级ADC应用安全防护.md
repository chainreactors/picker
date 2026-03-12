---
title: Radware推出Alteon Protect实现云级ADC应用安全防护
url: https://www.anquanke.com/post/id/315102
source: 安全客-有思想的安全新媒体
date: 2026-03-11
fetch_date: 2026-03-12T04:06:41.570633
---

# Radware推出Alteon Protect实现云级ADC应用安全防护

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

# Radware推出Alteon Protect实现云级ADC应用安全防护

阅读量**22815**

发布时间 : 2026-03-11 14:00:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sean Mitchell，文章来源：securitybrief

原文地址：<https://securitybrief.asia/story/radware-s-alteon-protect-brings-cloud-scale-adc-security>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Radware 正式发布 **Alteon Protect** 安全组件，专为其 Alteon 应用交付控制器（ADC）产品线设计，可将设备本地防护能力与 Radware 云安全平台深度联动。

该产品面向在**本地基础设施与公有云混合环境**中运行 Web 应用与 API 的企业机构。Radware 表示，借助该方案可直接扩展应用安全能力，**无需通过新增网络链路转发流量，也无需扩容硬件设备**。

### 混合架构防护模式

Alteon Protect 采用**云端检测、本地设备执行**的分离架构。云端提供实时防护引擎与检测算法，ADC 在本地完成低延迟安全策略执行。

Radware 指出，这一架构旨在应对 Web 应用与 API 面临的日益增长的攻击流量，包括**应用层 DDoS 攻击、自动化机器人流量以及 API 接口滥用**等威胁。

Alteon Protect 可**实时检测并缓解七层 Web DDoS 攻击、API 滥用、机器人攻击及 Web 应用威胁**，所有防护动作均在本地设备完成，可避免将 SSL 证书上传至云端。

ADC 部署在应用前端，负责负载均衡、流量调度与 SSL 卸载等核心功能。许多企业已将 ADC 作为 Web 应用防火墙与安全策略的统一管控点。Radware 此举也顺应行业趋势：**将更多安全检测与分析能力上云，同时让流量处理保持在应用就近节点**。

### 部署方式

Alteonon Protect 支持企业直采部署与托管服务两种模式。Radware、运营商及安全托管服务商（MSSP）均可提供**自管理或全托管**服务形态。

客户可在本地与云环境中直接部署，或通过服务商渠道启用。该模式符合多数企业的安全服务使用习惯，尤其适合需要**集中策略管理、持续安全更新且不希望新增硬件**的团队。

Radware 表示，该产品主要面向两类客户：

* 对企业用户：**无需替换现有 ADC，即可叠加云端安全能力**。
* 对托管服务商与运营商：架构原生支持**多租户交付**。

### 授权模式

产品扩容与 Radware **全局弹性授权体系**绑定，可根据业务需求弹性提升安全防护容量，具体定价暂未公布。

Radware 同时为新老客户提供相关支持计划，以降低评估与部署门槛，但未披露具体商务条款与适用条件。

### 市场背景

近年来，安全团队正将传统 Web 应用防护机制适配至**API 优先开发、微服务与高强度加密**场景，这一转变让应用层威胁受到更多关注，包括凭据填充、业务逻辑滥用、高频非流量型请求攻击等。

与此同时，许多企业希望**减少将解密流量传入第三方平台**，证书与密钥管理的运维限制也影响了架构选型。Alteonon Protect 正是基于这一背景设计：**防护执行留在本地 ADC，分析与更新依托云端完成**。

Radware 首席运营官 Gabi Malka 表示，许多企业在部署时需要在性能、防护与成本之间权衡取舍。

“企业不应在性能、防护与成本之间被迫取舍，”Malka 称，“Alteon Protect 现代化升级了 ADC 安全模型，将**云端增强 WAF、七层 DDoS 防护、机器人防护与 API 安全**与本地低延迟执行相结合，在保护现有投资的同时，为客户提供持续、云级规模的安全能力。”

Radware 介绍，Alteon Protect 是其**AI 驱动云安全平台**的重要组成部分。公司面向云与本地环境提供应用安全与交付产品，专注防护 Web 应用、API 与网络基础设施，抵御 DDoS 与自动化机器人等攻击。

Alteon Protect 现已面向企业开放部署，并通过运营商与 MSSP 渠道提供服务，实现**云端检测、Alteon 设备本地执行**的一体化安全架构。

本文翻译自securitybrief [原文链接](https://securitybrief.asia/story/radware-s-alteon-protect-brings-cloud-scale-adc-security)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315102](/post/id/315102)

安全KER - 有思想的安全新媒体

本文转载自: [securitybrief](https://securitybrief.asia/story/radware-s-alteon-protect-brings-cloud-scale-adc-security)

如若转载,请注明出处： <https://securitybrief.asia/story/radware-s-alteon-protect-brings-cloud-scale-adc-security>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1080**

* 粉丝
* **6**

### TA的文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37

### 相关文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37
* ##### [黑客利用微软Teams诱骗员工开放远程访问权限](/post/id/315110)

  2026-03-11 13:59:13
* ##### [微软推出365 E5升级套件与Agent 365 AI管控平台](/post/id/315113)

  2026-03-11 13:58:42
* ##### [GhostClaw伪装成OpenClaw窃取开发者设备数据](/post/id/315116)

  2026-03-11 13:58:16

### 热门推荐

文章目录

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