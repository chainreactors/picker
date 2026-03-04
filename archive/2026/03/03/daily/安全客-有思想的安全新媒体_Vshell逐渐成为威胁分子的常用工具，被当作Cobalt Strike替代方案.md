---
title: Vshell逐渐成为威胁分子的常用工具，被当作Cobalt Strike替代方案
url: https://www.anquanke.com/post/id/314951
source: 安全客-有思想的安全新媒体
date: 2026-03-03
fetch_date: 2026-03-04T04:02:07.842945
---

# Vshell逐渐成为威胁分子的常用工具，被当作Cobalt Strike替代方案

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

# Vshell逐渐成为威胁分子的常用工具，被当作Cobalt Strike替代方案

阅读量**17543**

发布时间 : 2026-03-03 10:00:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/vshell-gains-traction-among-threat-actors/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款基于 **Go 语言**开发的**命令与控制（C2）框架**，最初在中文攻防安全社区推广，如今正悄然扩大影响力，受到越来越多威胁行为者的关注。他们希望以此作为灵活、低成本的替代方案，取代昂贵的商业攻击工具。

这款工具名为 **Vshell**，早已从早期的基础远程访问工具（RAT）进化升级，现已成为全球企业防御方必须正视的安全威胁。

Vshell 最早出现于 **2021 年**，最初定位为一款轻量级 C2 平台，通过 **AntSword（蚁剑）** 网页后门框架进行控制。

其核心设计目标是对已攻陷的 **Windows 和 Linux 主机**进行管理，并强力支持**内网穿透、横向移动**等后渗透操作。

该工具的第三版用一句标语直接瞄准 Cobalt Strike 用户，清晰表明其定位：

**“Cobalt Strike 难用？试试 Vshell！”**

这对那些觉得商业攻击模拟工具**过于昂贵或操作复杂**的威胁分子构成了直接吸引力。

Censys 分析师通过持续扫描识别出了暴露在公网的 Vshell 部署实例，发现多个公开的 Web 目录中存在配置了**数百个在线客户端代理**的 Vshell 管理面板。

其中一个恢复的面板显示，同时在线的客户端多达 **286 个**，每个客户端都可作为流量中继，用于**隧道穿透与内网横向移动**。

这些发现表明，Vshell 已跻身主流滥用攻击框架之列，在真实网络攻击活动中的地位日益重要。

这款工具的使用者并不只是零散攻击者。

**2025 年**期间，Vshell 出现在多起已公开披露的攻击行动中，包括：

* DRAGONCLONE 行动
* 归属于 UNC5174 组织的 SNOWLIGHT 行动
* 2025 年 8 月曝光的一起钓鱼攻击活动（Vshell 为主要后渗透框架）

不同威胁组织均在使用这一趋势表明：

Vshell 已**不再是小众工具**，而是在整个黑产攻击生态中成熟普及、广受信赖的核心能力。

到 **第 4 版**时，Vshell 新增了**授权控制**、界面重新设计，并通过**伪装成 Nginx** 流量混入正常业务流量中。

2024 年之后，该工具疑似转为**私密开发**，表明开发者仍在持续投入，提升其**生存能力与规避检测能力**。

截至此时，Censys 通过扫描已监测到 **超过 850 个活跃的 Vshell 监听器**，足见该框架在公网基础设施中的部署规模之大。

### Vshell 的多协议 C2 架构

Vshell 区别于普通远控木马的核心特点，是其**高度灵活的监听器系统**，可为攻击者提供丰富的通信信道，维持对被控主机的控制。

在其中文标注为「监听管理」**的界面中，攻击者可在中央控制面板统一配置**多协议入站连接处理器。

Vshell 支持的通信方式包括：

* TCP
* KCP/UDP
* WebSocket
* DNS
* DNS-over-HTTPS（DoH）
* DNS-over-TLS（DoT）
* 甚至可通过 S3 存储桶实现对象存储服务（OSS）连接

多数监听器默认使用 **TCP/8084 端口**，但因其可灵活切换至 **DNS 类信道**，导致 Vshell 在网络边界极难被封堵。

其中 **DoH 与 DoT 信道**尤其难以防御，因为它们将 C2 流量隐藏在加密 DNS 查询中，而多数网络监控工具**默认不会检测这类流量**。

这种设计理念**直接对标 Cobalt Strike 架构**：

由中央团队服务端（teamserver）管理多个木马植入程序，同时为攻击者提供完整的会话控制、数据传输与隧道功能。

新版 Vshell 面板已采用**摘要认证（digest authentication）**，减少了防御方此前用于检测的特征指纹，使其**识别难度持续上升**。

### 防御建议

防御方应监控所有**对外暴露的基础设施**，尤其是 Web 服务器与防火墙，排查 Vshell 部署痕迹。

网络团队应重点检查 **DoH 与 DoT 流量**中的异常行为，这类信道常被用于 C2 通信。

由于 Vshell 基于 NPS 构建，可复用针对 NPS 流量的检测规则。

安全团队应定期在环境中执行**威胁狩猎查询**，并对匹配 Vshell 监听器特征的**外连通信**建立告警机制。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/vshell-gains-traction-among-threat-actors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314951](/post/id/314951)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/vshell-gains-traction-among-threat-actors/)

如若转载,请注明出处： <https://cybersecuritynews.com/vshell-gains-traction-among-threat-actors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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