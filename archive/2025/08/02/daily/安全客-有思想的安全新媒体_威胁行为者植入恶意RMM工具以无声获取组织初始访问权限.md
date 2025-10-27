---
title: 威胁行为者植入恶意RMM工具以无声获取组织初始访问权限
url: https://www.anquanke.com/post/id/310790
source: 安全客-有思想的安全新媒体
date: 2025-08-02
fetch_date: 2025-10-07T00:18:03.688518
---

# 威胁行为者植入恶意RMM工具以无声获取组织初始访问权限

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

# 威胁行为者植入恶意RMM工具以无声获取组织初始访问权限

阅读量**79800**

发布时间 : 2025-08-01 17:13:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/threat-actors-embed-malicious-rmm-tools/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场利用合法远程监控与管理（RMM）工具发起的高度复杂网络攻击活动，正对欧洲组织构成严重威胁，法国和卢森堡尤其成为重点攻击目标。

自2024年11月以来，攻击者通过精心设计的PDF文档传播恶意链接，这些链接指向RMM安装程序，从而成功绕过传统的邮件安全机制与恶意软件检测系统。

这一攻击手法标志着**社会工程攻击策略的进化**，黑客利用人们对合法运维工具的天然信任，大大提升了攻击的隐蔽性与成功率。

攻击重点集中在能源、政府、银行和建筑等**高价值行业**，而卢森堡作为目标尤其值得关注——其人均GDP居欧洲前列，是财务驱动型网络犯罪的理想猎物。

![]()

*用于针对荷兰某房地产机构的 PDF 文件（来源 ——Withsecure 公司）*

与以往大范围传播不同，这波攻击采用**高度定向策略**，通过行业相关的PDF内容和本地化语言，展现出对目标地区商业环境的深度了解。

攻击邮件以**精心伪造的社会工程内容**为核心，常常冒充目标机构的高级员工，使用仿冒域名或真实企业邮箱，增强可信度，提升钓鱼成功率。

![]()

*用于分发恶意 PDF 的社会工程学邮件（来源 ——Withsecure 公司）*

安全公司WithSecure通过对PDF元数据及投递机制的分析，识别出这波攻击活动的模式。他们指出攻击者持续使用直接嵌入的下载链接，指向合法RMM平台，如FleetDeck、Atera、Bluetrait和ScreenConnect。

值得注意的是，攻击者还**滥用Zendesk等受信任平台**来分发含恶意链接的PDF文件，从而绕过邮件网关等传统防御系统。这一变化显示出攻击者在策略上的精准与老练。

## PDF投递机制详解

本轮攻击在技术上的高明之处在于“以简驭繁”，巧妙利用合法平台的基础设施。每个PDF文件内都嵌有一个直接下载链接，链接地址由攻击者通过注册合法RMM服务账号生成，具备唯一访问密钥，安装后即可与攻击者账户建立远程控制连接。

例如FleetDeck的链接格式如下：

```
hxxps://agent[.]fleetdeck[.]io/[UNIQUE_IDENTIFIER]?win
```

元数据分析还发现，文档的作者字段使用了七个不同的名称，例如“Dennis Block”和“Guillaume Vaugeois”，文档创建工具包括Microsoft Word、Canva与ILovePDF。这种**有意为之的多样性**显然旨在干扰依赖元数据特征分析的检测系统，增强攻击的隐匿性。

这类RMM工具的另一个风险在于：一旦用户点击并安装，**无需额外配置或验证过程**，攻击者便可立即获得目标设备的远程访问权限，极大地降低了攻击门槛并加快入侵速度。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/threat-actors-embed-malicious-rmm-tools/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310790](/post/id/310790)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/threat-actors-embed-malicious-rmm-tools/)

如若转载,请注明出处： <https://cybersecuritynews.com/threat-actors-embed-malicious-rmm-tools/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**10赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [PDF投递机制详解](#h2-0)

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