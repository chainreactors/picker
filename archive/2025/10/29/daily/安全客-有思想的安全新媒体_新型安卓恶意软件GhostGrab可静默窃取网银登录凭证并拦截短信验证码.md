---
title: 新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码
url: https://www.anquanke.com/post/id/312878
source: 安全客-有思想的安全新媒体
date: 2025-10-29
fetch_date: 2025-10-30T03:10:32.024102
---

# 新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码

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

# 新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码

阅读量**24853**

发布时间 : 2025-10-29 17:27:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-ghostgrab-android-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为**GhostGrab**的复杂Android银行木马已出现在威胁领域，它针对多个地区的金融机构，具备**高级凭证窃取能力**。

该恶意软件在受感染设备上**静默运行**，窃取敏感银行凭证，同时通过短信拦截一次性密码（OTP）。

安全团队观察到，活跃的攻击活动通过**受感染的应用商店**和**恶意广告**分发GhostGrab，引发了对移动银行威胁不断升级的复杂性的担忧。

GhostGrab采用**多层感染策略**，首先通过社会工程战术（通常伪装成合法的 productivity 应用或系统工具）诱骗用户安装。

一旦安装，恶意软件会以标准应用功能为幌子请求**广泛权限**，包括辅助功能服务、短信访问权和悬浮窗权限。

![]()

这些特权使木马能够监控用户活动、捕获屏幕内容并拦截认证消息，而不会立即引起受害者怀疑。

Cyfirma研究人员在常规威胁情报操作中发现了该恶意软件，并指出其采用**精细化手段规避主流银行机构部署的检测机制**。

该木马展现出**高级反分析能力**，包括模拟器检测和调试器检查——当检测到研究环境时，会终止执行。

分析显示，GhostGrab通过**加密通道维持命令与控制（C2）通信**，接收指定目标银行应用和数据泄露协议的更新配置文件。

恶意软件的影响不止于单个账户被盗：威胁行为者利用窃取的凭证进行**未授权资金转移**和**欺诈交易**。

金融机构报告称，与GhostGrab感染相关的账户接管事件有所增加，促使银行加强监控协议并发布客户安全公告。

### **技术架构与数据泄露方法**

GhostGrab实施**复杂的悬浮窗攻击机制**，在合法银行应用之上显示高度逼真的钓鱼界面。

当受害者启动目标金融应用时，恶意软件会动态生成与登录界面**像素级一致的复制品**，在用户输入时捕获凭证。

木马通过注册的广播接收器监控传入短信，筛选符合常见OTP格式的认证码。

提取的凭证和OTP码在传输到远程服务器前会立即使用**AES-256加密**，最大限度减少被网络监控工具检测的风险。

恶意软件通过**系统启动接收器**和**前台服务**维持持久性，确保设备重启或应用终止后核心组件能重新启动。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-ghostgrab-android-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312878](/post/id/312878)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-ghostgrab-android-malware/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-ghostgrab-android-malware/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **630**

* 粉丝
* **6**

### TA的文章

* ##### [重磅！网络安全法迎来重大修改，人工智能治理迈出关键一步](/post/id/312934)

  2025-10-29 17:30:44
* ##### [OpenAI宣布启动重组，非营利基金会将重新掌握公司核心控制权](/post/id/312864)

  2025-10-29 17:29:30
* ##### [威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制](/post/id/312867)

  2025-10-29 17:29:15
* ##### [TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效](/post/id/312872)

  2025-10-29 17:28:56
* ##### [新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码](/post/id/312878)

  2025-10-29 17:27:44

### 相关文章

* ##### [重磅！网络安全法迎来重大修改，人工智能治理迈出关键一步](/post/id/312934)

  2025-10-29 17:30:44
* ##### [OpenAI宣布启动重组，非营利基金会将重新掌握公司核心控制权](/post/id/312864)

  2025-10-29 17:29:30
* ##### [威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制](/post/id/312867)

  2025-10-29 17:29:15
* ##### [TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效](/post/id/312872)

  2025-10-29 17:28:56
* ##### [Docker Compose 中存在路径遍历漏洞（CVE-2025-62725），通过OCI制品可导致任意文件被覆盖](/post/id/312882)

  2025-10-29 17:27:07
* ##### [Wear OS 信息应用存在权限漏洞 (CVE-2025-12080)，可导致无权限应用在未经用户授权的情况下发送短信/RCS消息，且POC已公开](/post/id/312885)

  2025-10-29 17:26:40
* ##### [Magento 中存在严重漏洞（CVE-2025-54236），可导致会话劫持与RCE，且已被活跃利用](/post/id/312888)

  2025-10-29 17:26:05

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