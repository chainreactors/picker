---
title: 新型恶意软件 DroidLock 现身：锁定安卓设备并索要赎金
url: https://www.anquanke.com/post/id/313730
source: 安全客-有思想的安全新媒体
date: 2025-12-12
fetch_date: 2025-12-13T03:14:06.182868
---

# 新型恶意软件 DroidLock 现身：锁定安卓设备并索要赎金

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

# 新型恶意软件 DroidLock 现身：锁定安卓设备并索要赎金

阅读量**12017**

发布时间 : 2025-12-12 18:01:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-droidlock-malware-locks-android/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()
一款名为**DroidLock**的新型高危恶意软件正通过钓鱼网站瞄准安卓用户，**西班牙语地区**更是其主要攻击目标。

该威胁将勒索软件攻击策略与远程控制功能相结合，对个人及企业设备用户均构成严重风险。

一旦完成安装，DroidLock 会将智能手机变成攻击者可随意操控的**恶意终端**，已然成为移动安全领域的一大隐患。

这款恶意软件的攻击流程分为两个阶段。首先由一个**投放器应用**充当诱饵，它会伪装成合法应用（通常模仿受信任的各类服务），诱导用户安装真正的恶意载荷。

这种伪装手段能帮助 DroidLock 绕过安卓系统的安全限制，进而获取关键的**辅助功能权限**。

安装完成后，恶意软件会同时申请**设备管理员权限**与辅助功能权限，而受害者往往在不了解权限背后风险的情况下便选择授权。

**Zimperium 安全研究团队**在调查过程中，成功剖析了 DroidLock 的复杂架构。

#### 解析 DroidLock 的凭据窃取机制

DroidLock 采用两种截然不同的**悬浮窗攻击技术**，来窃取用户的登录凭据与屏幕解锁图案。

第一种方法是直接在恶意软件代码中嵌入解锁图案绘制界面，当用户尝试解锁设备或打开银行类应用时，该界面会立即弹出。

这个悬浮窗会在用户毫无察觉的情况下，暗中记录下解锁图案。第二种方法则是从攻击者服务器的数据库中，动态加载基于 HTML 开发的悬浮窗。

这些悬浮窗能够完美仿冒正规银行应用与登录界面，诱骗用户在伪造表单中直接输入账号密码等敏感凭据。

一旦用户与这些悬浮窗进行交互，所有输入的信息都会直接发送至攻击者的后台服务器。

这款恶意软件会实时监控用户打开的应用，并与服务器下发的目标应用列表进行匹配。

一旦匹配成功，DroidLock 会立即部署对应的仿冒悬浮窗。这种精准的定向攻击策略，确保攻击者能够聚焦于银行、支付系统等**高价值目标应用**。

![]()

除窃取凭据外，DroidLock 还会**录制屏幕操作行为**，并调用设备摄像头拍摄画面，这有可能导致屏幕上显示的敏感信息（包括一次性验证码与各类身份认证码）遭到泄露。

DroidLock 的勒索弹窗会发出威胁：**若不在 24 小时内缴纳赎金，设备内所有数据都将被销毁**，同时提供联系方式供用户支付赎金。

![]()

与传统加密型勒索软件不同，这款恶意软件根本无需对数据进行加密 —— 它只需发送**恢复出厂设置指令**，就能直接抹除设备中的全部数据。

这使得攻击的预防与检测工作变得至关重要，因为一旦设备被感染，若无专业技术人员协助，数据几乎没有恢复的可能。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-droidlock-malware-locks-android/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313730](/post/id/313730)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-droidlock-malware-locks-android/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-droidlock-malware-locks-android/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **800**

* 粉丝
* **6**

### TA的文章

* ##### [利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌](/post/id/313745)

  2025-12-12 18:24:46
* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马](/post/id/313712)

  2025-12-12 18:04:19
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30

### 相关文章

* ##### [利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌](/post/id/313745)

  2025-12-12 18:24:46
* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马](/post/id/313712)

  2025-12-12 18:04:19
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30
* ##### [Notepad++ 漏洞存在重大风险：攻击者可劫持网络流量，通过更新通道植入恶意软件](/post/id/313725)

  2025-12-12 18:02:46
* ##### [技能缺口持续扩大，INE 聚焦企业培训模式向实践操作转型](/post/id/313735)

  2025-12-12 18:00:56

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