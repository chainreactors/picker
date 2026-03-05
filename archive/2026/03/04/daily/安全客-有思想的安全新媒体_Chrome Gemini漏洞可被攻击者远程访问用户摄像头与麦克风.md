---
title: Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风
url: https://www.anquanke.com/post/id/314994
source: 安全客-有思想的安全新媒体
date: 2026-03-04
fetch_date: 2026-03-05T04:05:41.057050
---

# Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风

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

# Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风

阅读量**22829**

发布时间 : 2026-03-04 10:34:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/chrome-gemini-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌浏览器 **Gemini Live** 集成组件中发现一处**高危漏洞**，编号为 **CVE-2026-0628**，该漏洞将用户置于严重的隐私与安全风险之下。

研究人员发现，该漏洞可被**恶意浏览器扩展**利用，从而**劫持 Gemini 侧边栏**，实现对用户**摄像头、麦克风及本地文件的未授权访问**。

将 AI 助手集成进网页浏览器，形成所谓的**智能代理浏览器**，从根本上改变了浏览器的安全格局。

Chrome 中的 Gemini Live 等功能，需要对浏览器环境拥有**深层高权限访问**，才能完成实时内容总结、自动化执行等任务。

| CVE ID | 严重级别 | 受影响组件 | 利用机制 | 影响 | 状态 |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-0628 | 高危 | Google Chrome Gemini Live 面板 | 基于 `declarativeNetRequests` API 注入 JavaScript | 未授权访问摄像头、麦克风、文件及屏幕截图 | 已修复（2026 年 1 月） |

AI 能够 “看见用户所见” 的这种多模态能力，**显著扩大了攻击面**。

这类 AI 组件本身具备高权限，意味着其中的漏洞**可绕过传统浏览器安全模型**。

### 针对 Gemini 面板的利用方式

Palo Alto Networks Unit 42 研究人员指出，**CVE-2026-0628** 的核心问题在于：Chrome 在**侧边栏**中加载 Gemini Web 应用（`https://gemini.google.com/app`）与在普通标签页加载时，采用的安全处理机制不同。

![]()

按照设计，使用 **`declarativeNetRequests` API** 的浏览器扩展可以拦截并修改 HTTPS 请求，广告拦截工具普遍使用该能力。

在普通标签页的 Gemini 应用中注入 JavaScript 并不会获得特殊权限，但在 **Gemini 面板**中注入则极为危险。

为支持复杂的 AI 任务，Chrome 为该面板赋予了**更高权限**，例如读取本地文件、访问多媒体设备等。

攻击者通过在面板中劫持应用，即可**窃取这些高权限**。

### 潜在影响与缓解措施

成功利用该漏洞后，攻击者可在 **Gemini 面板的高权限环境**内执行任意代码，可能导致严重后果：

* 未经用户同意**开启摄像头与麦克风**
* 访问操作系统中的**本地文件与目录**
* 对任意 HTTPS 网站**截取屏幕**
* 借助可被信任的 Gemini 面板界面**实施高隐蔽钓鱼攻击**

上述行为仅需极低的用户交互即可完成，**用户只需打开 Gemini 面板**就可能被利用。

Unit 42 已于 2025 年 10 月向谷歌进行了**合规漏洞上报**，官方在 2026 年 1 月初发布了修复补丁。

该事件凸显了 **AI 与浏览器集成**带来的全新安全挑战，也说明随着这类技术发展，持续安全监控至关重要。

本文翻译自gbhackers [原文链接](https://gbhackers.com/chrome-gemini-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314994](/post/id/314994)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/chrome-gemini-vulnerability/)

如若转载,请注明出处： <https://gbhackers.com/chrome-gemini-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [AuraStealer信息窃密木马活跃传播，攻击者依托48个C2域名持续攻击用户](/post/id/314998)

  2026-03-04 10:33:55

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