---
title: Budibase存在高危漏洞 可导致生产环境密钥全面泄露
url: https://www.anquanke.com/post/id/315099
source: 安全客-有思想的安全新媒体
date: 2026-03-11
fetch_date: 2026-03-12T04:06:39.698372
---

# Budibase存在高危漏洞 可导致生产环境密钥全面泄露

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

# Budibase存在高危漏洞 可导致生产环境密钥全面泄露

阅读量**26628**

发布时间 : 2026-03-11 14:00:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/total-platform-compromise-critical-9-6-cvss-flaws-in-budibase-expose-production-secrets/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

知名开源低代码平台 **Budibase** 日前发布紧急安全补丁，修复两项**高危漏洞**。这两个漏洞分别为 **CVE‑2026‑30240** 和 **CVE‑2026‑31816**，**攻击者可绕过身份认证，窃取生产环境中的敏感密钥**。

其中**最具威胁**的是 **CVE‑2026‑31816**，CVSS 评分高达 **9.1**。

漏洞源于平台用于保护所有服务端接口的 `authorized()` 中间件，因 `isWebhookEndpoint()` 函数中的正则表达式未做边界限定，导致请求校验逻辑异常。**攻击者只需在任意请求的参数中拼接类似 `?/webhooks/trigger` 的路径特征，即可欺骗服务器跳过全部身份认证与权限校验**。

### 漏洞影响

**完全权限绕过**：攻击者无需用户名、密码即可访问全部 API 接口。

**数据全面暴露**：获得数据表、记录、自动化流程与插件的完整增删改查权限。

**无交互攻击**：纯网络层面利用，无需钓鱼、无需用户操作即可触发。

如果说第一个漏洞打开了系统大门，那么 **CVE‑2026‑30240**（CVSS **9.6**）可让拥有 “构建者” 权限的用户彻底攻陷整个平台。

该漏洞存在于渐进式 Web 应用（PWA）的 ZIP 处理接口中。**用户上传构造好的恶意 ZIP 压缩包（内含篡改的 `icons.json`），可利用未做过滤的 `path.join()` 实现路径遍历攻击**。

攻击者能够读取服务器上任意文件，包括 `/proc/1/environ`，该文件通常存储**全部环境变量**。

### 漏洞影响

**密钥窃取**：可窃取 JWT 密钥、数据库凭证、API 令牌等核心敏感信息。

**跨租户风险**：在 Budibase 云服务中，单个租户的构建者可窃取平台全局密钥，影响所有用户。

**实测验证**：研究人员已在生产环境复现成功，**成功获取 19 项核心密钥**，包括 AWS IAM 密钥与 OpenAI API 密钥。

上述漏洞组合可实现**对整个平台的完全攻陷**。

一旦泄露 **JWT\_SECRET**，攻击者可伪造任意用户的管理员令牌；窃取 **API\_ENCRYPTION\_KEY** 后，则能解密系统中所有存储的数据源密码。

本文翻译自securityonline [原文链接](https://securityonline.info/total-platform-compromise-critical-9-6-cvss-flaws-in-budibase-expose-production-secrets/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315099](/post/id/315099)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/total-platform-compromise-critical-9-6-cvss-flaws-in-budibase-expose-production-secrets/)

如若转载,请注明出处： <https://securityonline.info/total-platform-compromise-critical-9-6-cvss-flaws-in-budibase-expose-production-secrets/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
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