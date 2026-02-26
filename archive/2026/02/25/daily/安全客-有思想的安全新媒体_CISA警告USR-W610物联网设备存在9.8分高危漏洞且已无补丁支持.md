---
title: CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持
url: https://www.anquanke.com/post/id/314851
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:10:00.691358
---

# CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持

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

# CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持

阅读量**19059**

发布时间 : 2026-02-25 14:11:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/no-patch-for-the-eol-cisa-warns-of-critical-9-8-severity-flaw-in-usr-w610-iot-devices/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全和基础设施安全局（**CISA**）发布警告，多款广泛使用的工业物联网设备存在多处**高危漏洞**。通报指出，济南有人物联网技术有限公司（**PUSR**）生产的 **USR‑W610 串口服务器** 存在多项底层安全缺陷。

对管理员而言最严峻的问题是：**该系列设备已正式停止服务（EOL），官方将不再提供任何安全补丁**。

这批漏洞中危害最严重的是 **CVE‑2026‑25715**，**CVSS 评分高达 9.8**，属于**特级高危漏洞**。

该漏洞源于设备管理逻辑的**底层设计缺陷**。

官方通报显示：**设备的 Web 管理界面允许将管理员用户名和密码设置为空值**。

一旦如此配置，对网络安全将是**毁灭性打击**。

报告警告：**设备允许通过 Web 管理界面和 Telnet 服务使用空凭证登录**，这相当于**直接关闭了所有关键管理通道的认证机制**，**同一局域网内的任意攻击者无需密码即可获取完整管理员权限**。

除登录绕过漏洞外，USR‑W610 还缺乏现代加密机制，界面安全设计存在严重问题：

* **明文窃听漏洞（CVE‑2026‑24455）**

  设备**不支持 HTTPS/TLS**，仅使用过时的 HTTP 基础认证。这会导致**流量仅编码不加密**，同一局域网内的攻击者可**轻松截获用户凭证**。
* **密码明文显示漏洞（CVE‑2026‑26049）**

  设备 Web 界面**会在输入框中明文展示密码**，任何能接触到管理界面的人员都可**直接看到管理员密码**，极易通过**偷窥、截图、浏览器表单缓存**等方式泄露。
* **Wi‑Fi 反认证攻击漏洞（CVE‑2026‑26048）**

  设备缺少**管理帧保护机制**，攻击者可发送伪造帧，**对设备发起未经授权的干扰，造成拒绝服务（DoS）**。

设备厂商济南有人物联网技术有限公司已明确表示：**该产品已停止服务，无任何补丁计划**。

这意味着 **USR‑W610（3.1.1.0 及以下版本）** 将**永久存在高危风险**，包括**认证失效、拒绝服务、凭证被窃**等。

由于**不会再有任何修复程序**，CISA 与安全研究人员强烈建议用户：

**立即停用受影响设备，或将其严格隔离在网络分区中，确保未授权设备无法访问其管理接口**。

本文翻译自securityonline [原文链接](https://securityonline.info/no-patch-for-the-eol-cisa-warns-of-critical-9-8-severity-flaw-in-usr-w610-iot-devices/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314851](/post/id/314851)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/no-patch-for-the-eol-cisa-warns-of-critical-9-8-severity-flaw-in-usr-w610-iot-devices/)

如若转载,请注明出处： <https://securityonline.info/no-patch-for-the-eol-cisa-warns-of-critical-9-8-severity-flaw-in-usr-w610-iot-devices/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52
* ##### [黑客利用Facebook广告投放虚假Win11更新实施恶意攻击](/post/id/314844)

  2026-02-25 14:18:43
* ##### [银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件](/post/id/314847)

  2026-02-25 14:18:35

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