---
title: AuraStealer信息窃密木马活跃传播，攻击者依托48个C2域名持续攻击用户
url: https://www.anquanke.com/post/id/314998
source: 安全客-有思想的安全新媒体
date: 2026-03-04
fetch_date: 2026-03-05T04:05:43.737571
---

# AuraStealer信息窃密木马活跃传播，攻击者依托48个C2域名持续攻击用户

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

# AuraStealer信息窃密木马活跃传播，攻击者依托48个C2域名持续攻击用户

阅读量**20007**

发布时间 : 2026-03-04 10:33:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/aurastealer-infostealer/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络威胁分子正在大规模部署一款名为 **AuraStealer** 的新型信息窃密木马。该木马拥有不断扩大的客户群体、**48 个已确认的 C2 命令控制域名**，并通过 TikTok、破解软件网站等流行平台发起多轮攻击活动。

AuraStealer 于 **2025 年年中**出现在俄语系网络犯罪论坛，在 LummaC2 遭打掉后，迅速成为其继任者与竞争对手。

该恶意软件以**订阅制**出售，分为基础版与高级版，由名为 **AuraCorp** 的团队宣传推广。团队宣称拥有 5–11 年安全相关经验，并具备专业化开发流程。

研究人员指出，尽管早期版本成熟度不及 Rhadamantys、Vidar 等老牌窃密木马，但**开发速度极快，功能更新频繁**。

![]()

根据相关论坛帖子与信息，AuraStealer 开发者称已快速吸引大批从 Lumma、StealC、Vidar、Rhadamantys 迁移而来的客户，显示其在黑产生态中**扩散速度极快**。

在本次报告中（2026 年 1 月已同步给客户），Intrinsec 威胁情报团队提供了高价值、可落地的上下文情报，帮助机构理解并防御此类网络威胁。

该项目的后续路线图还包括加入**代码虚拟化**保护，大幅提升逆向分析难度。

### AuraStealer 信息窃密木马概况

分析师已梳理出 **48 个 AuraStealer C2 域名**，其中大量使用廉价且易滥用的 `.SHOP` 与 `.CFD` 顶级域。

这些域名包括：

`auracorp.cfd`、`mscloud.cfd`、`magicupdate.cfd`、`gamedb.shop`、`browsertools.shop`、`clocktok.cfd` 等。

它们均通过 **Cloudflare** 代理隐藏真实后端服务器。

每个域名使用独立的 Cloudflare 源站证书，但**全部指向同一套后端架构**，疑似为单台服务器，运行的组件版本均已过时：

Apache 2.2.22、PHP 5.4.45、CodeIgniter 3.1.11、Symfony 3.4.26。

![]()

研究人员通过关联恶意软件配置、HTTP 头与全网测绘引擎，发现了与特定版本对应的域名集群。

早期版本（1.0.x–1.2.x）主要使用 `.SHOP` 域名，而最新的 1.5.2 样本更倾向使用 `.CFD`，表明攻击者正在**逐步将基础设施从 .SHOP 切换到 .CFD**。

LuxHost 与 Nicenic 作为部分域名的注册商或 DNS 服务商，进一步证明这些域名集群由同一团伙控制。

在从 VirusTotal 超过 200 个 AuraStealer 样本配置中提取出的 **21 个 C2 域名**的历史截图里，均出现了相同的登录页面。

![]()

### AuraStealer 传播方式

AuraStealer 攻击活动采用灵活的投递链，结合**社会工程学**与通用加载器分发。

其中一个主要传播渠道是 **TikTok 上的 ClickFix 骗局**：

短视频声称可免费激活 Windows、Microsoft 365、Adobe 系列、Netflix、Spotify 等，并诱导受害者以管理员权限执行一行 PowerShell 命令。

该命令会下载并执行远程 PowerShell 脚本，最终释放 AuraStealer 载荷，例如从 `file-epq.pages.dev/updater.exe` 下载。

除 TikTok 外，AuraStealer 还通过自解压压缩包、假冒系统清理工具（如 Gcleaner）、通用加载器传播，并将自身注入合法 Windows 进程，如 `regasm.exe`、`SndVol.exe`。

多轮攻击活动使用 **Donut shellcode 加载器** 或 **Soulbind 加载器**，从攻击者控制的服务器下载 AuraStealer，例如：

94.154.35.115、130.12.180.43。

这些主机还分发 Stealc、Rhadamanthys、Vidar、SalatStealer、NJRAT 等多种远控与窃密木马。

### 强悍的反分析与对抗机制

AuraStealer 运营者通过 `auracorp.cfd` 的 Web 管理面板控制感染终端，支持数据面板、载荷生成、日志筛选、Telegram 机器人报警等功能。

![]()

其登录流程内置 **JavaScript 工作量证明（PoW）** 机制，强制浏览器计算前 16 位为 0 的 SHA‑256 哈希才能提交表单，可抵御绝大多数自动化扫描器、简单脚本与暴力破解。

管理面板代码中出现**俄语字符串**，进一步指向俄语系攻击者。

在终端侧，**1.5.2 版本**采用高强度混淆与反分析技术：

间接控制流、异常驱动 API 哈希、XOR 加密字符串、虚拟机与沙箱检测、调试器检测、完整性校验，甚至在检测到钩子或断点时触发**隐藏栈破坏**。

该窃密木马会对部分独联体地区实施**地理定位放行**，显示出明确的地域投放策略。

### 数据窃取能力

通过自检后，AuraStealer 可从 **100 多款浏览器、70 多款应用**中窃取凭证与敏感数据，包括：

加密货币钱包、两步验证工具、VPN 客户端、密码管理器、远程控制软件等。

所有数据通过 **AES‑CBC 加密的 HTTPS** 传输到轮替 C2 服务器的三个专用接口：`apilive`、`apiconf`、`apisend`。

凭借不断扩充的功能、持续扩张的基础设施与活跃的攻击活动，AuraStealer 正从一款新兴窃密木马**快速成长为高风险凭证窃取威胁**，已成为安全防御方必须重点监控的目标。

本文翻译自gbhackers [原文链接](https://gbhackers.com/aurastealer-infostealer/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314998](/post/id/314998)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/aurastealer-infostealer/)

如若转载,请注明出处： <https://gbhackers.com/aurastealer-infostealer/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28

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