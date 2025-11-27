---
title: 伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮
url: https://www.anquanke.com/post/id/313431
source: 安全客-有思想的安全新媒体
date: 2025-11-26
fetch_date: 2025-11-27T03:10:50.285020
---

# 伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮

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

# 伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮

阅读量**23171**

发布时间 : 2025-11-26 18:28:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/11/25/fake-windows-update-screen-clickfix/>

译文仅供参考，具体内容表达以及含义原文为准。

一个 **逼真的伪造“Windows 更新”界面** 可能成为诱骗用户感染恶意软件的完美诱饵。再结合多阶段交付链和一些非常规技术，信息窃取者就能具备突破防御所需的一切条件。

### 恶意软件交付活动

“Huntress 自 10 月初以来发现了多个 ClickFix 诱饵网站，它们诱骗受害者运行恶意命令，格式一致且在多起事件中形成独特的执行链，”Huntress 研究人员 Ben Folland 和 Anna Pham 表示。

最初，诱饵页面会显示典型的“人机验证”窗口，要求用户按 Win+R 打开 Windows 运行框，按 CTRL+V 粘贴自动复制到剪贴板的命令，最后按 Enter 运行。

![]()

近期的活动变体采用了另一种诱饵：当潜在目标访问页面时，浏览器进入全屏模式并显示 **高度逼真的 Windows 更新界面**，要求用户执行上述操作“以完成更新”。

若用户遵循指示，感染链即被触发，最终可能感染 **Lumma 或 Rhadamanthys 信息窃取恶意软件**。

研究人员解释：“尽管视觉主题不同，但所有活动均以 `mshta.exe` 命令开头，该命令包含带 IP 地址的 URL，其中第二个八位字节始终为十六进制编码。这最终会部署 .NET 隐写加载器，从 PNG 图像的像素数据中提取经 Donut 打包的 shellcode。”

整个恶意软件的安装和运行过程 **完全在内存中进行**。为躲避端点安全解决方案检测，攻击者使用 **混淆且动态加载的脚本与代码、隐藏 payload，以及“Living-off-the-Land”（利用系统合法程序）技术**。

### ClickFix 攻击防范

ClickFix 目前是恶意软件传播者和初始访问中介最常用且最有效的手段之一，甚至出现了针对技术水平较低攻击者的 ClickFix 主题钓鱼工具包。

攻击指令会根据目标用户的系统（Windows/macOS/Linux）调整，诱饵也在持续更新优化。

研究人员建议管理员 **禁用普通用户设备上的 Windows 运行框**：“通过上述注册表修改或部署 GPO 策略阻止与运行框的交互。”

用户还应接受培训以识别 ClickFix 手法及变体。

研究人员补充：“利用 EDR 遥测监控 `explorer.exe` 衍生 `mshta.exe` 、`powershell.exe` 或其他具有异常命令行的合法系统程序。”

在 macOS 上，攻击者会诱骗用户打开终端并粘贴命令。管理员可通过 MDM 策略限制非管理员用户的终端访问，并阻止未签名脚本执行。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/11/25/fake-windows-update-screen-clickfix/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313431](/post/id/313431)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/11/25/fake-windows-update-screen-clickfix/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/11/25/fake-windows-update-screen-clickfix/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **740**

* 粉丝
* **6**

### TA的文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44

### 相关文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [高级威胁组织ToddyCat升级攻击工具库，新型工具专门窃取Outlook邮件并劫持Microsoft 365访问令牌](/post/id/313434)

  2025-11-26 18:27:40
* ##### [威胁行为体利用Blender基金会官方文件作为载体，传播臭名昭著的StealC V2信息窃取木马](/post/id/313427)

  2025-11-26 18:26:53
* ##### [供应链攻击“Sha1-Hulud”已波及超800个npm软件包与数千个GitHub代码库](/post/id/313439)

  2025-11-26 18:26:16

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