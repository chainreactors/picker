---
title: 超越ClickFix：新型攻击滥用Windows搜索功能分发MetaStealer窃密木马
url: https://www.anquanke.com/post/id/311761
source: 安全客-有思想的安全新媒体
date: 2025-09-03
fetch_date: 2025-10-02T19:32:32.434937
---

# 超越ClickFix：新型攻击滥用Windows搜索功能分发MetaStealer窃密木马

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

# 超越ClickFix：新型攻击滥用Windows搜索功能分发MetaStealer窃密木马

阅读量**54817**

发布时间 : 2025-09-02 16:07:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/beyond-clickfix-a-new-attack-abuses-windows-search-to-deliver-metastealer/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Huntress研究人员经过一年追踪发现，ClickFix社交工程攻击（通过伪装验证码诱使用户执行恶意代码）正出现危险演变。最新分析显示，攻击者开始将ClickFix技术与**Windows搜索协议滥用**和**PDF诱饵伪装**相结合，最终投放自2022年活跃的商业化信息窃取软件MetaStealer。

ClickFix攻击的核心在于诱骗用户”修复”虚假问题。Huntress解释称：”攻击者通过钓鱼信息引导用户访问包含验证码的网页，说服其通过复制粘贴命令到Windows运行框或PowerShell的方式执行’修复’，实则启动感染链。”

但攻击技术持续进化。”数月前攻击者转向类似技术**FileFix**，改用**Windows文件资源管理器**替代运行对话框，”Huntress指出。这些变种表明社交工程和”普通”流程（如验证码）正被持续武器化。

报告详细描述了最新攻击活动：始于托管在anydeesk[.]ink的虚假AnyDesk安装程序。受害者访问网站后会看到伪造的Cloudflare Turnstile验证，提示”点击验证人类身份”。Huntress写道：”至此所有迹象都符合ClickFix活动特征。”但此次攻击并未引导至运行框或PowerShell，而是滥用Windows搜索协议（search-ms URI），将受害者重定向至文件资源管理器。

进入资源管理器后，受害者被引导至攻击者控制的SMB共享，其中包含伪装成”**Readme Anydesk.pdf**“的**快捷方式LNK文件**。点击该文件即触发下一阶段攻击。

![]()

Huntress研究人员发现，恶意LNK文件同时投递了**合法的AnyDesk安装程序**（用于消除怀疑）和虚假PDF文件——实则为MSI安装包。攻击者采用了一项巧妙技巧：”该虚假PDF被配置为获取%COMPUTERNAME%环境变量作为子域名，这是攻击者从受害者处窃取信息的聪明手段。”

在MSI包内，研究人员发现：

1. **恶意DLL**（CustomActionDLL）；
2. **CAB压缩包**：包含1.js（清理脚本）和ls26.exe（MetaStealer投放器）

使用Private EXE Protector保护的MetaStealer执行了其典型的信息窃取行为：盗取加密货币钱包凭证、收集系统凭据和渗出文件。

ClickFix、FileFix及现今的混合攻击之所以猖獗，是因为它们将**社交工程与半合法工作流程相结合**。用户自以为在修复验证错误，通过自主操作无意间绕过了传统安全控制。正如Huntress所警告：”这类需要手动交互的攻击之所以有效，部分原因在于它们可能规避安全解决方案。”

本文翻译自securityonline [原文链接](https://securityonline.info/beyond-clickfix-a-new-attack-abuses-windows-search-to-deliver-metastealer/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311761](/post/id/311761)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/beyond-clickfix-a-new-attack-abuses-windows-search-to-deliver-metastealer/)

如若转载,请注明出处： <https://securityonline.info/beyond-clickfix-a-new-attack-abuses-windows-search-to-deliver-metastealer/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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