---
title: 三星RCE零日漏洞遭积极利用
url: https://www.anquanke.com/post/id/312123
source: 安全客-有思想的安全新媒体
date: 2025-09-16
fetch_date: 2025-10-02T20:11:06.076068
---

# 三星RCE零日漏洞遭积极利用

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

# 三星RCE零日漏洞遭积极利用

阅读量**64209**

发布时间 : 2025-09-15 18:23:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/samsung-zero-day-exploited/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

三星已推送2025年9月安全更新，修复**25个三星漏洞（SVE）** 及谷歌、三星半导体提供的安全补丁，以保护Galaxy设备免受多种威胁。用户需**立即安装更新**，防范潜在远程代码执行攻击。

### **核心威胁：零日漏洞CVE-2025-21043**

本次更新重点修复**CVE-2025-21043**——**libimagecodec.quram.so 库中的越界写入漏洞**，影响**Android 13至16全版本设备**。攻击者可通过诱骗用户处理**特制图像**触发漏洞，实现**远程任意代码执行**。

三星确认该漏洞**已被实际利用**，Meta与WhatsApp安全团队通过私下渠道披露了此问题，补丁已修正导致漏洞的错误实现逻辑。

### **其他高风险漏洞**

9月安全维护发布（SMR）还包含两项**高严重性漏洞**修复：

1. **CVE-2025-32100**：公告未披露细节，但评级为高风险。
2. **CVE-2025-21034**：**libsavsvc.so 库越界写入漏洞**，允许本地攻击者执行代码——若设备已感染恶意应用，风险将显著放大。补丁通过**强化输入验证**防止内存损坏。

### **中等风险漏洞与影响范围**

更新同时解决多个中等严重性问题，包括：

1. **One UI Home（CVE-2025-21032）**：不当访问控制漏洞，可能让物理攻击者绕过Kiosk模式。
2. **ContactProvider（CVE-2025-21033）**：本地攻击者可利用此漏洞访问敏感信息。
3. **ImsService组件漏洞**：可能导致通话中断或SIM卡临时禁用。

### **更新指南**

本次安全更新版本为**SMR Sep-2025 Release 1**，未来几周将逐步推送至支持的Galaxy手机与平板。用户可通过 **设置 > 软件更新 > 下载并安装** 检查更新。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/samsung-zero-day-exploited/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312123](/post/id/312123)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/samsung-zero-day-exploited/)

如若转载,请注明出处： <https://cybersecuritynews.com/samsung-zero-day-exploited/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

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
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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