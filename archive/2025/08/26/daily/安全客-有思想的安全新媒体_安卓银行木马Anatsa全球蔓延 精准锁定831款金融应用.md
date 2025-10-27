---
title: 安卓银行木马Anatsa全球蔓延 精准锁定831款金融应用
url: https://www.anquanke.com/post/id/311442
source: 安全客-有思想的安全新媒体
date: 2025-08-26
fetch_date: 2025-10-07T00:18:05.465171
---

# 安卓银行木马Anatsa全球蔓延 精准锁定831款金融应用

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

# 安卓银行木马Anatsa全球蔓延 精准锁定831款金融应用

阅读量**38865**

发布时间 : 2025-08-25 17:46:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/anatsa-android-trojan-expands-its-global-reach-and-targets-831-financial-apps/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安卓生态系统持续面临精密银行木马的顽固威胁。Zscaler ThreatLabz团队通过持续监控谷歌Play商店分发的恶意应用，揭示了Anatsa（又名TeaBot）恶意软件的最新演变趋势。

研究人员指出：”**Anatsa**恶意软件最初于2020年出现，是一种能够窃取凭证、记录键盘输入并实施欺诈交易的安卓银行木马。”虽然早期活动主要针对欧美地区650余家金融机构，但最新行动已显著扩大范围。ThreatLabz发现”Anatsa最新变种已瞄准全球831家金融机构，新增德国、韩国等目标国以及加密货币平台”。

这种扩张表明网络犯罪分子正调整恶意软件策略，不仅针对传统银行业，还开始 exploiting新兴金融科技和加密市场。

攻击始于上传至官方**Google Play**商店的诱饵应用，这些应用通常伪装成文档阅读器或文件管理器。它们在安装阶段表现正常，但后续会从命令控制（C2）服务器获取恶意载荷。

ThreatLabz解释称：”Anatsa使用投放器技术，威胁分子在官方商店部署看似正常的诱饵应用。安装后，木马会从C2服务器静默下载伪装成更新的恶意载荷。”这些诱饵应用多数极具人气——”单个应用下载量超5万次”，证明该分发手段的有效性。

该恶意软件已采用多项新型反分析技术。研究人员指出：”父安装程序现使用动态生成的数据加密标准（DES）密钥在运行时解密每个字符串，大幅提升对抗静态分析工具的能力。”

关键更新包括：

1. 使用DES实现字符串运行时解密
2. 通过设备特定载荷限制规避分析环境
3. 利用畸形APK归档文件绕过静态检测机制
4. 以动态载荷投递取代旧方法，直接安装Anatsa有效载荷

一旦安装，恶意软件便会请求**READ\_SMS、SYSTEM\_ALERT\_WINDOW和USE\_FULL\_SCREEN\_INTENT**等广泛权限，用于凭证窃取和持久化驻留。

Anatsa的核心目标仍是凭证收割。通过滥用无障碍服务，它会显示针对受害者设备上银行或金融应用定制的虚假登录页面。

ThreatLabz强调：”Anatsa主要通过显示从C2服务器下载的虚假银行登录页面来窃取凭证。这些页面根据用户设备检测到的金融机构应用进行定制。”甚至连Robinhood等热门应用也遭仿冒，通过伪造”系统维护”界面诱骗受害者泄露敏感信息。

Anatsa并非唯一滥用Google Play的恶意软件。ThreatLabz还识别出”来自不同恶意软件家族的77款恶意应用，累计安装量超1900万次”。研究人员观察到广告软件、Joker、Harly和银行木马数量激增，而Facestealer和Coper等家族呈下降趋势。

对用户而言，建议虽简单却至关重要——仔细核查应用权限并仅从可信开发者处安装。对企业来说，主动检测与监控对于缓解绕过传统应用商店防御的威胁至关重要。

本文翻译自securityonline [原文链接](https://securityonline.info/anatsa-android-trojan-expands-its-global-reach-and-targets-831-financial-apps/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311442](/post/id/311442)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/anatsa-android-trojan-expands-its-global-reach-and-targets-831-financial-apps/)

如若转载,请注明出处： <https://securityonline.info/anatsa-android-trojan-expands-its-global-reach-and-targets-831-financial-apps/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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