---
title: Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动
url: https://www.anquanke.com/post/id/312444
source: 安全客-有思想的安全新媒体
date: 2025-09-30
fetch_date: 2025-10-02T12:03:37.781897
---

# Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动

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

# Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动

阅读量**46679**

发布时间 : 2025-09-29 18:04:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/morte-botnet-unveiled-a-rapidly-growing-loader-as-a-service-campaign-exploiting-routers-and-enterprise-apps/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

CloudSEK威胁情报团队（TRIAD）曝光了一场复杂的僵尸网络活动，该活动通过**基于Web的命令注入漏洞**系统性攻陷SOHO路由器、物联网（IoT）设备和企业应用程序。这场依赖\*\*“加载器即服务（LaaS）”模式\*\*的攻击已活跃至少六个月，并呈现快速增长趋势。

CloudSEK观察到，今年夏季恶意活动出现**爆发式增长**：“2025年7-8月期间，该活动的攻击量激增230%，部署了包括Morte二进制文件和加密货币挖矿载荷在内的多架构恶意软件。”

此次发现得益于CloudSEK分析师获取了暴露的**命令与控制（C2）日志**，从而揭示了攻击者基础设施和技术的详细信息。

该僵尸网络严重依赖通过Web界面进行的命令注入，滥用**未充分 sanitize 的POST参数**（如ntp、syslog、hostname字段）。CloudSEK解释：“攻击者将shell命令注入未过滤的POST参数（例如ntp、remote\_syslog、hostname、ping），使设备执行wget/curl | sh命令。”

![]()

关键技术包括：

1. 通过暴力破解或凭证喷洒攻击**滥用默认凭证（admin:admin）**；
2. 利用固件升级和诊断端点执行任意代码；
3. 使用BusyBox工具实现**跨平台载荷投递**；
4. 在数十个IP间轮换基础设施以逃避下架。

该活动还利用已知漏洞，例如**CVE-2019-16759（vBulletin预认证RCE）**、**CVE-2019-17574（WordPress Popup Maker插件漏洞）** 和**CVE-2012-1823（PHP-CGI RCE）**。

设备被攻陷后，攻击者采用分阶段投递策略：

1. **小型shell脚本作为dropper**；
2. 安装morte.x86、morte.x86\_64等原生二进制文件以实现**持久化**；
3. 部署加密货币挖矿载荷，劫持设备资源牟利。

CloudSEK指出：“连接到挖矿池或使用JSON-RPC getwork/eth\_getWork的载荷表明，挖矿是主要 monetization 手段。”

除加密劫持外，僵尸网络还支持**基于HTTP的C2轮询**，使操作者能够下发命令、收集侦察信息，并决定保留访问权供后续使用或转售。

攻击范围覆盖消费者与企业生态系统：

1. SOHO路由器和嵌入式Linux设备；
2. 企业应用，尤其是**Oracle WebLogic、WordPress和vBulletin服务器**；
3. 固件和路由器诊断页面，如wlwps.htm 、wan\_dyna.html 、login.shtml 。

被攻陷的设备可被重新用于DDoS攻击、挖矿或在地下市场转售。

CloudSEK警告，该活动仍在持续进化：“我们有充分信心确定，威胁行为者将继续快速利用漏洞，并在未来6个月内**大幅扩展目标设备列表**。”

由于采用“加载器即服务”模式，其基础设施可能被多个犯罪团伙武器化，加速其在全球威胁格局中的增长和持久性。

本文翻译自securityonline [原文链接](https://securityonline.info/morte-botnet-unveiled-a-rapidly-growing-loader-as-a-service-campaign-exploiting-routers-and-enterprise-apps/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312444](/post/id/312444)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/morte-botnet-unveiled-a-rapidly-growing-loader-as-a-service-campaign-exploiting-routers-and-enterprise-apps/)

如若转载,请注明出处： <https://securityonline.info/morte-botnet-unveiled-a-rapidly-growing-loader-as-a-service-campaign-exploiting-routers-and-enterprise-apps/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53

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