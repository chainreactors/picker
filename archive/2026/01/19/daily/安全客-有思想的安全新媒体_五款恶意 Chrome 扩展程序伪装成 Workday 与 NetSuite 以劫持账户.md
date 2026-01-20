---
title: 五款恶意 Chrome 扩展程序伪装成 Workday 与 NetSuite 以劫持账户
url: https://www.anquanke.com/post/id/314386
source: 安全客-有思想的安全新媒体
date: 2026-01-19
fetch_date: 2026-01-20T03:30:33.785862
---

# 五款恶意 Chrome 扩展程序伪装成 Workday 与 NetSuite 以劫持账户

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

# 五款恶意 Chrome 扩展程序伪装成 Workday 与 NetSuite 以劫持账户

阅读量**15544**

发布时间 : 2026-01-19 16:49:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2026/01/five-malicious-chrome-extensions.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员发现了五款新的恶意 Google Chrome 浏览器扩展，它们**伪装成**人力资源（HR）和企业资源计划（ERP）平台（如 Workday、NetSuite 和 SuccessFactors），以**劫持受害者账户**。

“这些扩展协同工作，窃取身份验证令牌，阻断安全响应能力，并通过会话劫持实现完全账户接管。”Socket 安全研究员 Kush Pandya 在周四的报告中表示。

这些扩展的名称如下：

* DataByCloud Access（ID: oldhjammhkghhahhhdcifmmlefibciph，发布者：databycloud1104）——251 次安装
* Tool Access 11（ID: ijapakghdgckgblfgjobhcfglebbkebf，发布者：databycloud1104）——101 次安装
* DataByCloud 1（ID: mbjjeombjeklkbndcjgmfcdhfbjngcam，发布者：databycloud1104）——1,000 次安装
* DataByCloud 2（ID: makdmacamkifdldldlelollkkjnoiedg，发布者：databycloud1104）——1,000 次安装
* Software Access（ID: bmodapcihjhklpogdpblefpepjolaoij，发布者：Software Access）——27 次安装

截至撰写时，除 Software Access 外，其他四款均已从 Chrome 应用商店下架。尽管如此，它们仍可在 Softonic 等第三方软件下载网站获取。这些插件被宣传为 “生产力工具”，声称能提供 Workday、NetSuite 等平台的 “高级功能访问权限”。其中 DataByCloud 1 和 DataByCloud 2 最早发布于 2021 年 8 月 18 日。

尽管使用了两个不同的发布者，但基于**完全相同的功能和基础设施模式**，研究人员判定这是一场**协同攻击活动**。攻击流程包括：将 Cookie 窃取到攻击者控制的远程服务器、通过操纵 DOM 树阻止安全管理页面访问、以及通过 Cookie 注入实现会话劫持。

安装后，DataByCloud Access 会请求对 Workday、NetSuite 和 SuccessFactors 域名的以下权限：cookies、management、scripting、storage 和 declarativeNetRequest。它还会收集指定域名的身份验证 Cookie，并**每 60 秒**发送到 “api.databycloud [.] com”。

“Tool Access 11（v1.4）通过清空页面内容并跳转到无效 URL，阻止用户访问 Workday 中的 44 个管理页面。”Pandya 解释说。“该扩展会阻断身份验证管理、安全代理配置、IP 范围管理和会话控制界面。”

这是通过 DOM 操纵实现的：扩展会维护一个页面标题列表并持续监控。DataByCloud 2 则将被阻断的页面扩展到 56 个，新增了密码修改、账户停用、双因素认证设备管理和安全审计日志访问等关键功能。它同时针对生产环境和 Workday 的沙箱测试环境 “workdaysuv [.] com”。

相比之下，DataByCloud 1 复制了 DataByCloud Access 的 Cookie 窃取功能，同时集成了使用开源库 DisableDevtool 来**阻止开发者工具调试**的功能。两款扩展均对其 C2 通信进行加密。

五款扩展中最复杂的是 Software Access，它不仅能窃取 Cookie，还能从 “api.software-access [.] com” 接收被盗的 Cookie，并将其**注入浏览器**，从而实现直接的会话劫持。此外，它还会保护密码输入框，防止用户查看输入的凭据。

“该功能会从服务器载荷中解析 Cookie，删除目标域名的现有 Cookie，然后遍历提供的 Cookie 数组，使用 chrome.cookies.set () 逐个注入。”Socket 表示。“这会将受害者的身份验证状态直接安装到威胁 actor 的浏览器会话中。”

值得注意的是，所有五款扩展都包含一个**完全相同的 23 个安全相关 Chrome 扩展列表**，例如 EditThisCookie、Cookie-Editor、ModHeader、Redux DevTools 和 SessionBox。它们会监控这些扩展的存在并向威胁 actor 发送告警。

Socket 认为，这很可能是为了判断浏览器是否安装了可能干扰其 Cookie 窃取目标或暴露其行为的工具。此外，五款扩展共享相同的扩展 ID 列表，这意味着它们要么来自同一威胁 actor（使用不同发布者账号），要么使用了同一个工具包。

Chrome 用户如果安装了上述任何插件，应立即从浏览器中删除，并重置密码，同时检查是否存在来自陌生 IP 或设备的未授权访问。

“持续的凭据窃取、管理界面阻断和会话劫持相结合，会导致安全团队即使检测到未授权访问，也无法通过正常渠道进行补救。”Socket 警告说。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2026/01/five-malicious-chrome-extensions.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314386](/post/id/314386)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2026/01/five-malicious-chrome-extensions.html)

如若转载,请注明出处： <https://thehackernews.com/2026/01/five-malicious-chrome-extensions.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **930**

* 粉丝
* **6**

### TA的文章

* ##### [1340 亿美元豪赌：马斯克起诉 OpenAI，加州监管重拳同时砸向 xAI](/post/id/314365)

  2026-01-19 16:54:15
* ##### [CVE-2026-0695：ConnectWise PSA 2026.1 修复高危跨站脚本（XSS）漏洞](/post/id/314368)

  2026-01-19 16:53:36
* ##### [虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话](/post/id/314370)

  2026-01-19 16:53:09
* ##### [未修补的远程代码执行漏洞：Livewire Filemanager 文件上传缺陷（CVE-2025-14894）影响 Laravel 应用](/post/id/314374)

  2026-01-19 16:52:22
* ##### [Deno 高危漏洞可导致密钥泄露（CVE-2026-22863）与代码执行（CVE-2026-22864）](/post/id/314377)

  2026-01-19 16:51:31

### 相关文章

* ##### [1340 亿美元豪赌：马斯克起诉 OpenAI，加州监管重拳同时砸向 xAI](/post/id/314365)

  2026-01-19 16:54:15
* ##### [CVE-2026-0695：ConnectWise PSA 2026.1 修复高危跨站脚本（XSS）漏洞](/post/id/314368)

  2026-01-19 16:53:36
* ##### [虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话](/post/id/314370)

  2026-01-19 16:53:09
* ##### [未修补的远程代码执行漏洞：Livewire Filemanager 文件上传缺陷（CVE-2025-14894）影响 Laravel 应用](/post/id/314374)

  2026-01-19 16:52:22
* ##### [Deno 高危漏洞可导致密钥泄露（CVE-2026-22863）与代码执行（CVE-2026-22864）](/post/id/314377)

  2026-01-19 16:51:31
* ##### [2026 年会迎来微芯片植入的 “ChatGPT 时刻” 吗？](/post/id/314380)

  2026-01-19 16:51:12
* ##### [大规模清理行动：X 平台禁用 “信息金融”，彻底打击 AI 生成的加密垃圾帖](/post/id/314383)

  2026-01-19 16:50:29

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