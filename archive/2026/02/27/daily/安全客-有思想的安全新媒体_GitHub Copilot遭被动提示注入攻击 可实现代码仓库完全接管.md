---
title: GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管
url: https://www.anquanke.com/post/id/314882
source: 安全客-有思想的安全新媒体
date: 2026-02-27
fetch_date: 2026-02-28T03:49:51.324663
---

# GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管

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

# GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管

阅读量**23251**

发布时间 : 2026-02-27 10:30:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/github-copilot-exploited/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

GitHub Codespaces 中存在一个由 AI 驱动的高危漏洞，名为**RoguePilot**，该漏洞允许攻击者通过在 GitHub Issue 中嵌入恶意指令，悄无声息地劫持代码仓库。

该漏洞由 Orca Research Pod 的研究人员发现，它利用了 GitHub Issues 与 Codespaces 内置 Copilot AI 代理之间的无缝集成，攻击者无需进行任何直接交互，即可触发对仓库的完全接管。

研究人员已向 GitHub 进行了合规漏洞披露，微软在与 Orca 团队协作完成修复工作后，已对此漏洞进行了修补。

### GitHub Copilot 攻击原理

RoguePilot 被归类为**被动提示注入**，这是一种将恶意指令嵌入语言模型会自动处理的数据、内容或开发环境中的攻击方式。

与需要受害者直接与 AI 交互的传统提示注入不同，该攻击在开发者从被植入恶意内容的 GitHub Issue 打开 Codespaces 的瞬间就会触发。当从 Issue 上下文启动 Codespaces 时，GitHub Copilot 会自动将 Issue 描述作为初始提示，从而将不受信任的用户可控内容直接注入 AI 代理的执行环境。

Orca Security 的研究员 Roi Nisimi 通过 HTML 注释标签`<!-- -->`在 GitHub Issue 中嵌入隐藏指令，演示了完整的攻击链。这是 GitHub 的一项标准功能，内容对人类用户不可见，但 Copilot 在处理 Issue 描述时可以完整读取。

一旦 Codespace 被打开，Copilot 就会静默执行注入的指令，不会向开发者发出任何可见警报。

攻击随后通过一个**三阶段数据窃取链**展开。首先，注入的提示指令 Copilot 通过其`run_in_terminal`工具执行`gh pr checkout 2`，拉取一个预先构造的拉取请求。该请求中包含一个名为`1.json`的符号链接，指向`/workspaces/.codespaces/shared/user-secrets-envs.json`—— 存储环境`GITHUB_TOKEN`的文件。

由于 Copilot 的防护机制不会追踪符号链接，AI 代理通过该链接使用`file_read`工具读取密钥文件，不会触发工作空间边界限制。

最后，Copilot 被指令创建一个新的 JSON 文件`issue.json`，其`$schema`属性指向攻击者控制的服务器。这利用了 VS Code 默认开启的`json.schemaDownload.enable`设置，该设置会自动通过 HTTP GET 获取远程 JSON 模式。

攻击者将窃取的`GITHUB_TOKEN`作为 URL 参数附加到该模式请求中，实现对高权限认证令牌的静默外带泄露。获取对仓库具有有效权限的`GITHUB_TOKEN`后，攻击者即可获得**完整读写权限**，完成隐蔽的仓库接管。

Orca Security 将 RoguePilot 描述为一种**新型 AI 介导供应链攻击**：大语言模型的自主能力、终端访问权限、文件读写和联网工具被武器化，反过来攻击本应受其协助的开发者。

该漏洞表明，作为 Codespaces 内自主编码代理运行的 Copilot，无法可靠区分开发者的合法指令与嵌入在 GitHub Issue 或拉取请求中的对抗性内容。

此次攻击**无需特殊权限、无需受害者执行代码、无需社会工程学**，仅需创建一个恶意 GitHub Issue 即可实施，**技术水平较低的威胁行为者也可轻易利用**。

安全专家指出，这是为 AI 代理授予 “上帝模式” 权限、工具、终端访问权和高权限令牌，而底层模型仍采用开放逻辑、将所有处理文本视为可信任内容所直接导致的后果。

Orca 在披露中建议厂商在所有集成大语言模型的开发工具中采用**故障安全默认配置**：将仓库、Issue 和拉取请求内容视为不可信输入；禁止 AI 代理从外部数据源被动接收提示；将`json.schemaDownload.enable`默认设为 false；在工作空间边界内实施严格的符号链接沙箱；为 Codespaces 环境颁发最小权限、短时有效的令牌。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/github-copilot-exploited/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314882](/post/id/314882)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/github-copilot-exploited/)

如若转载,请注明出处： <https://cybersecuritynews.com/github-copilot-exploited/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1030**

* 粉丝
* **6**

### TA的文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42

### 相关文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42
* ##### [未修补的ActiveMQ漏洞引发二次入侵与LockBit勒索攻击](/post/id/314906)

  2026-02-27 10:29:22
* ##### [Claude Code推出远程控制功能 实现移动端全自主开发](/post/id/314902)

  2026-02-27 10:28:57
* ##### [思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用](/post/id/314880)

  2026-02-27 10:28:35

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