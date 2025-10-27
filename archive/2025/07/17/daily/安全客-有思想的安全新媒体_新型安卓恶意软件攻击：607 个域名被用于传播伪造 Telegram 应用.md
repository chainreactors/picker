---
title: 新型安卓恶意软件攻击：607 个域名被用于传播伪造 Telegram 应用
url: https://www.anquanke.com/post/id/310149
source: 安全客-有思想的安全新媒体
date: 2025-07-17
fetch_date: 2025-10-06T23:27:40.597645
---

# 新型安卓恶意软件攻击：607 个域名被用于传播伪造 Telegram 应用

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

# 新型安卓恶意软件攻击：607 个域名被用于传播伪造 Telegram 应用

阅读量**93683**

发布时间 : 2025-07-16 18:19:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/fake-telegram-apps-domains-android-malware-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

BforeAI 公司旗下 PreCrime 实验室的最新研究显示，一场**新型威胁攻击**正通过数百个恶意域名诱骗**安卓用户**下载**伪造的 Telegram 应用**。近几周，该攻击活动利用**仿冒网站、二维码重定向以及植入危险权限和远程执行功能的篡改版 APK 文件**实施攻击。

威胁情报团队已识别出 **607 个**与该攻击相关的域名，这些域名均伪装成 Telegram 官方下载页面，其中多数通过 Gname 域名注册商注册，服务器位于中国。部分网站使用 “teleqram”“telegramapp”“telegramdl” 等近似域名**模仿正品品牌**，针对那些可能忽略细微拼写差异的用户。

#### **虚假应用，真实危害**

BforeAI 于周二向Hackread提前披露的博客文章指出，受害者会被诱导通过链接或二维码下载看似为 Telegram Messenger 的应用。

研究人员还发现了**两个版本**的 APK 文件，大小分别为 60MB 和 70MB。安装后，该应用表面上与正品无异，却**暗中获取广泛权限并启用远程命令执行功能**。

值得注意的是，此次攻击中使用的钓鱼网站伪装成**个人博客或非官方粉丝页**。典型案例会将用户重定向至 **zifeiji (.) asia**，该网站采用 Telegram 的图标、下载按钮和配色风格，页面标题充斥着中文 SEO 短语（如 “纸飞机官网下载”），目的显然是提高搜索可见度，同时掩盖应用的真实意图。

#### **Janus漏洞重现**

恶意 APK **采用较旧的 v1 签名方案**，因此易受Janus漏洞影响 —— 该漏洞波及**安卓 5.0 至 8.0** 版本。借助这一漏洞，威胁者可在**不改变签名**的情况下向合法 APK 中**植入恶意代码**。在本次攻击中，恶意软件保留了**有效的签名**，从而**绕过标准检测机制**。

应用侵入设备后，会利用**明文协议（HTTP、FTP）**广泛访问外部存储，还包含与 MediaPlayer 交互的代码，并通过套接字接收和执行远程命令。这种控制能力可被用于**监控用户活动、窃取文件或发起进一步攻击**。

需要说明的是，Janus漏洞（CVE-2017-13156）是安卓设备的严重安全缺陷，攻击者可借此修改合法 APK 或 DEX 文件而不改变其加密签名，使恶意应用看似可信且未被篡改。

#### **Firebase 数据库滥用风险持续**

一项关键发现与已停用的 Firebase 数据库（tmessages2 (.) firebaseio (.) com）有关，该数据库此前被攻击者使用。尽管原始数据库已下线，但研究人员警告，任何攻击者均可注册同名新 Firebase 项目使其重新激活。

硬编码至该端点的旧版恶意软件会**自动连接至攻击者控制的新数据库**，这一策略延长了攻击活动的存续周期，即便原始操作者停止活动也不受影响。

![]()

*分发恶意 Telegram APK 的页面模仿博客布局，诱导用户安装该应用。此应用会请求一系列权限，鉴于这些权限存在被滥用的可能性，已按风险等级进行分类。（图片来源：BforeAI）*

#### **植入追踪脚本**

恶意基础设施还使用追踪 JavaScript（如托管于 telegramt (.) net 的 ajs.js），该脚本**收集设备和浏览器信息并发送至远程服务器**，其中包含注释掉的代码 —— 用于向安卓用户显示悬浮下载横幅。这种设置旨在**通过自动检测设备和定制用户体验提高安装率**。

#### **域名分布详情**

在 607 个域名中，**顶级域名使用情况**如下：

* **.com：316 个**
* **.top：87 个**
* **.xyz：59 个**
* **.online：31 个**
* **.site：24 个**

大量注册.com 域名显然是为了增加**可信度**，而使用低成本域名则有助于**广泛传播**。

#### **组织防范措施**

为降低暴露风险，BforeAI 建议组织采取多项关键预防措施：一是**建立自动化域名监控机制**，在可疑或仿冒网站激活前及时发现；二是**利用多个威胁情报源扫描 APK 文件、URL 及相关哈希值**，确认其安全性；

在条件允许的情况下，**拦截 APK 或 SVG 附件的传输**（尤其当这些文件类型与业务需求无关时）；最后，务必**对用户开展培训**，使其避免从非官方网站下载应用 —— 即便页面看似合法或模仿知名品牌。

钓鱼技术已日趋复杂，此次攻击表明，Janus等旧漏洞仍能被用于针对毫无防备的用户。**二维码、拼写仿冒（typosquatting）及云服务滥用**等手段的结合，使其 sophistication 远超简单过滤机制的应对能力。

本文翻译自hackread [原文链接](https://hackread.com/fake-telegram-apps-domains-android-malware-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310149](/post/id/310149)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/fake-telegram-apps-domains-android-malware-attack/)

如若转载,请注明出处： <https://hackread.com/fake-telegram-apps-domains-android-malware-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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