---
title: Cursor IDE被植入恶意 VSCode 插件，导致 50 万美元加密货币被盗
url: https://www.anquanke.com/post/id/310063
source: 安全客-有思想的安全新媒体
date: 2025-07-16
fetch_date: 2025-10-06T23:39:04.145825
---

# Cursor IDE被植入恶意 VSCode 插件，导致 50 万美元加密货币被盗

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

# Cursor IDE被植入恶意 VSCode 插件，导致 50 万美元加密货币被盗

阅读量**64139**

发布时间 : 2025-07-15 18:21:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/malicious-vscode-extension-in-cursor-ide-led-to-500k-crypto-theft/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款伪装成合法插件的恶意扩展程序被植入 Cursor AI IDE（基于 VSCode 的 AI 编程环境），通过远程访问工具和信息窃取器感染开发者设备，导致一名俄罗斯加密货币开发者损失 50 万美元。这起事件暴露了开放插件生态在供应链安全上的严重风险。

**假冒“Solidity Language”插件藏恶意代码，操控远程控制工具**

Cursor IDE 支持 Open VSX，这是 Visual Studio Marketplace 的替代平台，允许用户安装兼容 VSCode 的插件扩展功能。卡巴斯基（Kaspersky）报告称，他们受邀调查一起安全事件——一名从事加密货币开发的俄罗斯开发者在使用 Cursor IDE 后，其电脑上存储的加密货币被盗，损失高达 50 万美元。

尽管该开发者声称电脑“干净”，且未安装任何杀毒软件，但卡巴斯基研究员 Georgy Kucherin 通过分析其硬盘镜像，在 `.cursor/extensions` 目录中发现了名为 `extension.js` 的恶意 JavaScript 文件。这个插件自称是**“Solidity Language”**，用于高亮显示以太坊智能合约语法，实则伪装成一个合法插件，来源于 Open VSX 注册表。

该恶意插件执行了来自远程服务器 `angelic[.]su` 的 PowerShell 脚本，用于下载和安装其他恶意组件。其中包括检查并安装远程管理工具 **ScreenConnect**。一旦安装，攻击者即可完全远程控制受害者的电脑。

**多阶段感染链：从远程访问到信息窃取**

借助 ScreenConnect，攻击者上传并执行了 VBScript 文件，进一步投递了多个恶意载荷。攻击最终阶段，恶意脚本从 `archive[.]org` 下载了一个可执行文件，其中包含名为 **VMDetector** 的加载器，它随后安装了以下恶意软件：

* **Quasar RAT**：一款远程访问木马，可执行任意命令。
* **PureLogs stealer**：信息窃取器，可提取浏览器中的登录凭据、认证 Cookie 以及加密货币钱包数据。

**伪造下载量与排名，诱导用户误信插件合法**

根据卡巴斯基的调查，这款插件在被 Open VSX 下架前已被下载 **5.4 万次**，但研究人员认为该下载量是人为刷量，以增强插件可信度。

更令人担忧的是，攻击者在插件下架第二天，又上传了一个几乎一模一样的版本，名为“solidity”，并将其伪造下载次数提升至近 **200 万次**。

![]()

通过操控算法和刷量，他们成功让该恶意插件在搜索结果中排在合法插件前面，误导开发者下载。

研究人员还发现，Visual Studio Code 官方插件市场中也出现了类似恶意扩展，例如 **“solaibot”、“among-eth”、“blankebesxstnion”**，其攻击手法与上述一致，同样通过 PowerShell 脚本投递 ScreenConnect 与窃密程序。

**卡巴斯基警告：开放插件生态已成为攻击者乐园**

卡巴斯基警告称，开源仓库和插件市场正日益成为恶意软件的传播温床。加密货币行业尤为脆弱，因为其开发项目大量依赖开源工具和库，而攻击者正是借助这一信任机制来进行投毒。

> “恶意插件和包依旧是加密行业面临的重要威胁。许多项目依赖开源仓库中的工具，但这些仓库中往往隐藏着伪装精巧的恶意组件。下载任何工具前，请务必谨慎核查来源和代码。”

> “如果你安装的插件与其宣传功能不符，应立即怀疑其合法性，并检查其源代码是否存在恶意行为。”

此次事件再次警示开发者和企业：在使用任何第三方扩展和工具时，必须采取安全审查流程，防止供应链成为攻击突破口。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/malicious-vscode-extension-in-cursor-ide-led-to-500k-crypto-theft/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310063](/post/id/310063)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/malicious-vscode-extension-in-cursor-ide-led-to-500k-crypto-theft/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/malicious-vscode-extension-in-cursor-ide-led-to-500k-crypto-theft/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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