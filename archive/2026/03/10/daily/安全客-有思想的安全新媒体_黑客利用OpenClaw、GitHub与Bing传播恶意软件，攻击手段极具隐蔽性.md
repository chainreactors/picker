---
title: 黑客利用OpenClaw、GitHub与Bing传播恶意软件，攻击手段极具隐蔽性
url: https://www.anquanke.com/post/id/315083
source: 安全客-有思想的安全新媒体
date: 2026-03-10
fetch_date: 2026-03-11T04:03:31.585167
---

# 黑客利用OpenClaw、GitHub与Bing传播恶意软件，攻击手段极具隐蔽性

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

# 黑客利用OpenClaw、GitHub与Bing传播恶意软件，攻击手段极具隐蔽性

阅读量**22542**

发布时间 : 2026-03-10 13:59:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Victoria Mossi，文章来源：webpronews

原文地址：<https://www.webpronews.com/hackers-are-using-openclaw-github-and-bing-to-spread-malware-in-a-disturbingly-clever-way/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

攻击者正在利用开源游戏 **OpenClaw** 的 GitHub 复刻仓库实施攻击，并通过 **Bing 搜索引擎优化投毒**推广恶意下载包，在安装完整可运行游戏的同时，秘密植入信息窃取类恶意软件。微软尚未就其搜索引擎遭操纵一事作出回应。

一款正规的开源游戏已被黑客利用作为恶意软件分发载体，整套攻击链设计**异常精密**。研究人员发现，针对 **OpenClaw**（1997 年经典平台游戏《Captain Claw》的免费开源重制版）的攻击活动，正通过 GitHub 仓库与被篡改的 Bing 搜索结果，诱骗用户下载信息窃取木马。

该攻击模式如下：

攻击者**复刻（Fork）** 官方 OpenClaw 仓库，在自己的版本中注入恶意代码，然后通过手段让 Bing 将其毒化仓库列为**置顶搜索结果**。任何在微软搜索引擎中搜索该游戏的用户，都可能轻易进入恶意仓库而非正版项目。这是**SEO 投毒**与**软件供应链攻击**相结合的典型案例。

据 TechRadar 报道，该攻击由安全研究员 **Ax Sharma** 发现。他指出，这些复刻仓库伪装极为逼真，足以迷惑普通用户。攻击者并非简单植入明显的恶意载荷，而是修改了游戏安装器，**在正版游戏安装过程中同步静默运行一个可执行程序**，大幅提升了检测难度。

该恶意软件属于**信息窃取程序**。一旦安装，便会针对浏览器保存的凭据、会话 Cookie、加密货币钱包数据以及其他储存在受害者设备上的敏感信息。它会主动连接**命令与控制服务器（C2）**，并尽可能窃取数据回传。虽然行为属于此类威胁的常规模式，**但其传播方式让该攻击活动格外突出**。

GitHub 长期以来都是此类滥用行为的目标。该平台自带的**可信属性**—— 开发者通常比随机下载更信任其上代码 —— 使其成为理想攻击载体。而复刻（Fork）是 GitHub 的核心功能，因此用户创建热门项目副本时**不会出现明显警示**。攻击者正是刻意利用了这种信任。

但此次事件中 **Bing 的角色尤为关键**。

尽管谷歌占据搜索主导地位，但 Bing 仍承担大量查询，尤其是通过 **Microsoft Edge 默认搜索**、Copilot 集成，以及微软服务标准化的企业环境。攻击者专门针对 Bing 做恶意页面优化，而非谷歌，这是**精准定向选择**。

这表明他们目标是**未修改默认浏览器设置**的用户，这类人群通常技术敏感度较低，也正是可能在不核查来源的情况下，下载怀旧游戏重制版的群体。

这些恶意仓库究竟伪装得如何？

它们**高度复刻正版 OpenClaw 项目**，包含完整的 README、编译说明与发布二进制包。差异极为隐蔽：仅修改编译脚本、安装包，并在发布压缩包中捆绑额外可执行文件。除非逐行对比原版与复刻版本，否则几乎无法察觉。

这并非孤立事件。Bleeping Computer 等安全媒体已报道，攻击者**滥用 GitHub 基础设施传播恶意软件**正成为趋势。今年早些时候，Phylum 与 Checkmarx 的研究人员记录了多起攻击活动：利用虚假 GitHub Star、拼写劫持包名、篡改仓库元数据提升恶意项目曝光度。而 OpenClaw 事件则将**搜索引擎操纵**加入了攻击工具箱。

微软尚未公开回应，为何恶意复刻仓库能在 Bing 结果中**排名如此靠前**。这本身就是问题。若 Bing 算法能被如此轻易利用，展示携带恶意软件的 GitHub 仓库，便令人质疑微软搜索索引流程中的安全保障 ——**尤其微软同时拥有 GitHub**。

对安全团队与开发者而言，核心警示清晰且必须重申：

**不要仅凭外观信任 GitHub 仓库**，即便出现在搜索结果中。务必通过仓库所有者、创建时间、提交记录、Star 数量确认是否为原版项目。**创建时间新、社区互动极少的复刻仓库均为高危信号**。

机构还应检查终端防护是否能检测此类**侧面加载恶意软件**。OpenClaw 安装器本身可正常运行、游戏能正常游玩，这意味着用户**不会立刻察觉异常**。恶意组件在后台运行，而受害者正在畅玩 1997 年的经典游戏。手段**巧妙且高效**。

这背后还有更广泛的警示：

开源游戏与爱好者项目正**日益成为高价值目标**，因为它们的维护团队规模更小，安全基础设施弱于主流开源库。几乎不会有人对《Captain Claw》重制版使用软件成分分析工具。攻击者深知这一点。

而 Bing 这一切入点也绝非小众问题。

微软正通过 Windows 默认设置、Copilot、Edge 强力推广 Bing。每一台新安装的 Windows 都默认使用 Bing，每一次 Copilot 查询都经由 Bing。若搜索结果完整性能被如此轻易破坏，**攻击面将极为庞大**。

官方原版 OpenClaw 项目（GitHub 原仓库）**依然安全**。问题完全出在被篡改植入恶意软件的**非官方复刻仓库**。如果你近期下载过 OpenClaw—— 尤其通过 Bing 搜索结果而非直链 —— 请**立即扫描系统**。

据报道，GitHub 已下架部分恶意复刻仓库，但双方的**猫鼠游戏**仍将持续。新复刻可在数分钟内创建。除非 GitHub 与微软上线更激进的恶意仓库检测机制，或 Bing 加强危险仓库链接过滤，否则这类攻击模式**将持续有效**。

本文翻译自webpronews [原文链接](https://www.webpronews.com/hackers-are-using-openclaw-github-and-bing-to-spread-malware-in-a-disturbingly-clever-way/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315083](/post/id/315083)

安全KER - 有思想的安全新媒体

本文转载自: [webpronews](https://www.webpronews.com/hackers-are-using-openclaw-github-and-bing-to-spread-malware-in-a-disturbingly-clever-way/)

如若转载,请注明出处： <https://www.webpronews.com/hackers-are-using-openclaw-github-and-bing-to-spread-malware-in-a-disturbingly-clever-way/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1070**

* 粉丝
* **6**

### TA的文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18

### 相关文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18
* ##### [Viber即时通讯软件存在TLS漏洞，Cloak代理模式失效并导致用户暴露](/post/id/315068)

  2026-03-10 14:01:44
* ##### [黑客可利用间接提示注入攻击 借助外部内容操控AI智能体](/post/id/315071)

  2026-03-10 14:01:03

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