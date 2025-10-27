---
title: NimDoor 高级加密窃密木马：进程被杀后可自动“复活”
url: https://www.anquanke.com/post/id/309335
source: 安全客-有思想的安全新媒体
date: 2025-07-04
fetch_date: 2025-10-06T23:29:00.008647
---

# NimDoor 高级加密窃密木马：进程被杀后可自动“复活”

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

# NimDoor 高级加密窃密木马：进程被杀后可自动“复活”

阅读量**59867**

发布时间 : 2025-07-03 14:58:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源： bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/nimdoor-crypto-theft-macos-malware-revives-itself-when-killed/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在一场针对 Web3 与加密货币机构的攻击行动中，**朝鲜国家背景黑客组织正使用一款新型 macOS 恶意软件家族“NimDoor”进行渗透入侵**。

研究人员在对其载荷分析过程中发现，该攻击活动采用了异常手法，**并引入了一种此前未见的“基于信号的持久化机制”**，显著增强了木马的抗清除能力。

### 利用 Telegram 诱导执行伪装更新

攻击链起始于攻击者通过 Telegram 联系目标，诱导其点击更新链接。该链接伪装为 Zoom SDK 更新，**通过 Calendly 日程平台和钓鱼邮件分发**，诱导用户运行恶意安装包。这一策略与近期被 Huntress 安全平台归因于朝鲜 BlueNoroff 组织的战术高度相似。

### 高级 macOS 恶意代码部署细节

据 SentinelOne 安全公司今日发布的报告，攻击者使用 C++ 和 Nim 编译语言构建二进制文件（统称为 NimDoor），这一组合在 macOS 攻击中极为罕见。

其中，“**installer**”二进制文件负责初始化与配置部署路径，并将另外两个恶意组件投放至系统中，分别命名为：

* `GoogIe LLC`（注意为字母“i”伪装为“l”）
* `CoreKitAgent`

`GoogIe LLC` 组件主要负责收集环境信息，并生成十六进制编码的配置文件写入临时目录。它还在系统中创建一个名为 `com.google.update.plist` 的 **macOS LaunchAgent** 以实现**登录自启动持久化**，并用于存储后续阶段所需的身份验证密钥。

### 核心木马具备“复活”能力

NimDoor 框架中的核心负载是 `CoreKitAgent`，这是一个基于事件驱动的恶意二进制文件，利用 **macOS 的 kqueue 机制** 实现异步控制执行流程。

它内部实现了一个拥有 **10 种状态切换机制的状态机**，通过硬编码的状态表根据运行时条件灵活切换攻击逻辑。

其**最具标志性的特点**是对 `SIGINT` 和 `SIGTERM` 系统信号的处理逻辑——**这两类信号通常用于终止进程，但 CoreKitAgent 会在接收到这些信号后自动触发“重部署流程”，实现自我恢复与持久化重建。**

> “CoreKitAgent 一旦捕获到终止信号，就会重新写入 LaunchAgent、恢复 GoogIe LLC 加载器、以及自身木马程序副本，并通过 `addExecutionPermissions_user95startup95mainZutils_u32` 函数赋予可执行权限，”SentinelLABS 解释称。

这种机制**确保用户主动结束进程或简单查杀行为无法彻底清除恶意代码**，使得该木马具备极高的生存能力。

### 数据窃取与远程控制

CoreKitAgent 会解码并执行一个十六进制编码的 AppleScript 脚本，该脚本每隔 30 秒向攻击者控制服务器发送“心跳”，并使用 `osascript` 命令执行远程指令，实现轻量级后门控制。

与此同时，另一个名为 `zoom_sdk_support.scpt` 的组件会触发第二条攻击链，执行 `trojan1_arm64` 木马并发起 WSS（加密 WebSocket）通信，随后下载两个脚本：

* `upl`：从浏览器中提取数据，抓取 Keychain 凭据、`.bash_history` 和 `.zsh_history`，并通过 `curl` 上传至 `dataupload[.]store`。
* `tlgrm`：专注于窃取 Telegram 数据库与 `.tempkeyEncrypted` 文件，**可能用于解密用户通信内容。**

`zoom_sdk_support.scpt` 本身还通过插入一万多行空行进行混淆处理，**提高安全产品检测难度**。

### 木马特征与攻击者能力评估

综合分析显示，NimDoor 框架及其相关后门组件，是目前归因于朝鲜背景攻击者的 **最复杂的 macOS 恶意软件家族之一**。

其模块化结构提供高度灵活性，而信号机制与 AppleScript 搭配的隐匿执行方式，**体现出朝鲜黑客组织正在不断进化工具链，以实现更强的跨平台攻击能力。**

SentinelLABS 报告中还公布了本次攻击所涉及的 **域名、文件路径、脚本和二进制文件的 IoC（攻击指标）**，为加密货币与 Web3 行业提供预警和检测线索。

本文翻译自 bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/nimdoor-crypto-theft-macos-malware-revives-itself-when-killed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309335](/post/id/309335)

安全KER - 有思想的安全新媒体

本文转载自:  [bleepingcomputer](https://www.bleepingcomputer.com/news/security/nimdoor-crypto-theft-macos-malware-revives-itself-when-killed/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/nimdoor-crypto-theft-macos-malware-revives-itself-when-killed/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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