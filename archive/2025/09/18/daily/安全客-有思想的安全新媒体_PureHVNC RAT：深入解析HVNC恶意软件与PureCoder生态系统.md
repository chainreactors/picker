---
title: PureHVNC RAT：深入解析HVNC恶意软件与PureCoder生态系统
url: https://www.anquanke.com/post/id/312202
source: 安全客-有思想的安全新媒体
date: 2025-09-18
fetch_date: 2025-10-02T20:17:23.363298
---

# PureHVNC RAT：深入解析HVNC恶意软件与PureCoder生态系统

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

# PureHVNC RAT：深入解析HVNC恶意软件与PureCoder生态系统

阅读量**69064**

发布时间 : 2025-09-17 17:36:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/purehvnc-rat-inside-the-hvnc-malware-and-the-purecoder-ecosystem/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Check Point Research（CPR）近期的 forensic 调查揭示了Pure恶意软件家族的细节——这是由威胁 actor “PureCoder” 开发并销售的一系列恶意工具。研究聚焦于一场ClickFix钓鱼活动，该活动导致了为期八天的入侵，攻击者部署了Rust加载器、PureHVNC RAT和Sliver C2框架，以维持持久化并窃取敏感数据。

感染链始于**伪造的招聘广告**，将受害者重定向至ClickFix钓鱼页面。在该页面，恶意PowerShell命令被自动复制到剪贴板，诱骗受害者执行。若命令运行，会下载经过混淆的JavaScript文件，部署第一版PureHVNC RAT。

CPR解释：“访问恶意ClickFix网站后，PowerShell命令会自动复制到剪贴板……执行后，命令会下载并运行恶意JavaScript文件，启动感染链。”

![]()

到第二天，攻击者通过投放**Rust加载器**升级攻击，该加载器会释放另一版PureHVNC RAT（此次使用活动ID “amazon3”）。

攻击核心是**PureHVNC RAT**——一款强大的远程管理工具，提供**隐藏虚拟网络计算（HVNC）** 功能，允许攻击者在用户无感知的情况下远程控制受感染系统。

报告强调：“PureHVNC是PureCoder开发的Pure恶意软件家族产品，具备HVNC能力，使攻击者能控制受感染设备而不被用户察觉。”

### **PureHVNC功能与插件系统**

PureHVNC配备\*\* extensive 插件系统\*\*，支持功能包括：

1. 远程访问摄像头和麦克风
2. 键盘记录与剪贴板监控
3. 反向代理支持（HTTP & SOCKS5）
4. 加密货币地址劫持（BTC、ETH、LTC、XMR等）
5. YouTube和Twitch bots（自动点击广告与订阅）
6. 分布式拒绝服务（DDoS）能力

### **归因与PureCoder生态系统**

调查发现，PureHVNC及相关恶意软件频繁从PureCoder直接控制的**GitHub仓库**拉取文件。归因依据包括：提交记录关联的GitHub账户活动时区为**UTC+0300**（涵盖俄罗斯等地区）。

CPR指出：“分析确认，相关URL和GitHub账户均直接关联Pure恶意软件家族的开发者。”

进一步挖掘发现**PureRAT构建工具**，其中不仅包含支持恶意功能的硬编码GitHub URL，还与PureCoder另一产品**PureCrypter**存在代码重叠。

PureCoder被认为拥有广泛的恶意产品组合，包括：

1. **PureCrypter**：恶意软件混淆器
2. **PureLogs**：信息窃取/日志工具
3. **PureMiner**：静默加密货币挖矿机
4. **Blue Loader**：高级僵尸网络加载器

这些产品在地下论坛和Telegram频道**积极营销**，供各类网络犯罪分子使用。

### **对抗分析与持久化机制**

活动中部署的Rust加载器包含**高级反分析技术**，如检测调试器、逆向工程工具和Windows Defender模拟器API。若怀疑被分析，恶意软件会延迟执行**长达30分钟**以规避沙箱检测。

持久化通过模仿合法计划任务实现，伪装成“Google Updater”隐藏在受感染系统中。

Check Point的调查不仅揭示了PureHVNC RAT的技术深度，还暴露了支撑网络犯罪活动的**Pure恶意软件生态系统**。通过将GitHub仓库、构建工具和基础设施与PureCoder直接关联，研究人员阐明了该开发者在推动大规模恶意活动中的核心作用。

本文翻译自securityonline [原文链接](https://securityonline.info/purehvnc-rat-inside-the-hvnc-malware-and-the-purecoder-ecosystem/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312202](/post/id/312202)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/purehvnc-rat-inside-the-hvnc-malware-and-the-purecoder-ecosystem/)

如若转载,请注明出处： <https://securityonline.info/purehvnc-rat-inside-the-hvnc-malware-and-the-purecoder-ecosystem/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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