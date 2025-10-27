---
title: 黑客散布 XORIndex 恶意软件，隐藏于 67 个恶意 npm 软件包中
url: https://www.anquanke.com/post/id/310169
source: 安全客-有思想的安全新媒体
date: 2025-07-17
fetch_date: 2025-10-06T23:27:53.361060
---

# 黑客散布 XORIndex 恶意软件，隐藏于 67 个恶意 npm 软件包中

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

# 黑客散布 XORIndex 恶意软件，隐藏于 67 个恶意 npm 软件包中

阅读量**69712**

发布时间 : 2025-07-16 18:14:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/north-korean-xorindex-malware-hidden-in-67-malicious-npm-packages/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**黑客在 npm 投放 67 个恶意软件包，传播 XORIndex 恶意加载器**

朝鲜关联的黑客组织近日在 Node Package Manager（npm）在线软件仓库中投放了 67 个恶意软件包，用于将一种名为 **XORIndex** 的新型恶意加载器传播至开发者系统中。

据软件包安全平台 Socket 的研究人员披露，这些恶意软件包的总下载量已超过 17,000 次，他们认为这些行为是“**Contagious Interview（传染式面试）**”行动的一部分。该行动自今年 4 月以来持续活跃，并在上月投放了 35 个用于投递信息窃取程序和后门的 npm 软件包。

![]()

### 攻击背景与方式

“Contagious Interview” 是一个由朝鲜政府支持的网络间谍活动，主要以开发者为目标，诱骗其点击伪装成招聘机会的链接，进而在目标系统中执行恶意代码。

攻击目的多样，包括收集敏感信息以便后续入侵企业系统，或窃取受害者的加密资产。

npm 是 Node.js 的默认软件包管理工具，广泛用于 JavaScript 开发。但由于其开放性，也常被攻击者用于投放恶意程序。

此次投放的 67 个恶意软件包中，多个名称模仿了真实开源项目，如：

* `vite-meta-plugin`
* `vite-postcss-tools`
* `vite-logging-tool`
* `vite-proc-log`
* `pretty-chalk`
* `postcss-preloader`
* `js-prettier`
* `flowframe`
* `figwrap`
* `midd-js`、`middy-js`

当开发者安装上述软件包后，攻击者在 `postinstall` 阶段执行一个脚本，从而运行 **XORIndex Loader** —— 一种新型加载器，与此前已知的 **HexEval Loader** 类似。

XORIndex Loader 会收集受害者主机信息，用于制定攻击策略，并将数据回传至攻击者的命令控制（C2）服务器。该服务器托管于云服务平台 Vercel 上。

随后，C2 服务器会返回一个或多个 JavaScript 代码片段，并通过 `eval()` 执行。这些代码通常包含两种已知后门程序：**BeaverTail** 与 **InvisibleFerret**，均与“Contagious Interview”行动相关。

这两款恶意程序支持远程访问、数据窃取，并具备下载其他恶意组件的能力。研究人员指出，朝鲜黑客不断将旧工具与新变种组合使用，并对其进行微调以规避检测。一旦 npm 清理了相关恶意包，攻击者便会换用新账户和新名称再次上线。

Socket 表示：“Contagious Interview 行动的攻击者将持续扩展其恶意软件组合，轮换使用新的 npm 账号和变种包，复用 HexEval Loader、BeaverTail、InvisibleFerret 等组件，并持续部署如 XORIndex Loader 等新型加载器。我们预计，这类恶意加载器将在未来通过形式稍有不同的新软件包中持续出现，以逃避安全检测。”

Socket 已将所有相关恶意包上报 npm 平台，但警告称部分仍可能留存。

### 安全建议

* 严格核对所下载软件包名称，警惕名称近似**（“typosquatting”）**陷阱；
* 仅信任知名开源项目及信誉良好的发布者；
* 审查软件仓库的近期更新记录，识别是否存在批量自动操作迹象；
* 若有能力，务必检查源代码是否存在混淆行为；
* 在沙盒或隔离环境中运行未知库，以确保安全后再投入使用。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/north-korean-xorindex-malware-hidden-in-67-malicious-npm-packages/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310169](/post/id/310169)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/north-korean-xorindex-malware-hidden-in-67-malicious-npm-packages/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/north-korean-xorindex-malware-hidden-in-67-malicious-npm-packages/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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