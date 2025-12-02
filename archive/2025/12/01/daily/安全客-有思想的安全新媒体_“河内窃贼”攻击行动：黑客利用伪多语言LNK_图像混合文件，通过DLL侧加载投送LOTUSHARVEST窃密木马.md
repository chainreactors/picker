---
title: “河内窃贼”攻击行动：黑客利用伪多语言LNK/图像混合文件，通过DLL侧加载投送LOTUSHARVEST窃密木马
url: https://www.anquanke.com/post/id/313495
source: 安全客-有思想的安全新媒体
date: 2025-12-01
fetch_date: 2025-12-02T03:17:35.249024
---

# “河内窃贼”攻击行动：黑客利用伪多语言LNK/图像混合文件，通过DLL侧加载投送LOTUSHARVEST窃密木马

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

# “河内窃贼”攻击行动：黑客利用伪多语言LNK/图像混合文件，通过DLL侧加载投送LOTUSHARVEST窃密木马

阅读量**14987**

发布时间 : 2025-12-01 17:45:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/operation-hanoi-thief-hackers-use-pseudo-polyglot-lnk-image-to-deploy-lotusharvest-stealer-via-dll-sideloading/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场复杂的新型网络间谍活动正席卷越南科技和招聘行业，通过 **劫持招聘流程** 部署隐蔽的信息窃取器。SEQRITE Labs APT 团队于 2025 年 11 月 3 日发现，该活动利用隐藏在看似无害的 **求职申请中的复杂感染链** 发动攻击。

研究人员将此活动命名为“**河内窃贼行动（Operation Hanoi Thief）**”，命名原因是“最终 payload 具备窃取功能，且简历中的地理位置集中在越南首都河内周边”。

攻击以典型的鱼叉式钓鱼战术启动：恶意邮件包含名为 `Le-Xuan-Son_CV.zip` 的 ZIP 压缩包。受害者在其中会发现一份看似属于软件开发人员“Le Xuan Son”的简历，附带河内地址和 GitHub 个人资料。

为建立可信度，攻击者早在 2021 年就为该“求职者”创建了 **伪造 GitHub 账户**，但细查可发现账户无任何活动，表明其“专为此次钓鱼活动设立”。

### 技术独特性：伪多语言载荷与 FTP 滥用

该活动的技术独特之处在于恶意软件的投递方式：ZIP 文件包含两个文件——文档和快捷方式（LNK 文件）。“威胁 actor 主要使用一种我们称为 **伪多语言载荷（pseudo-polyglot payload）** 的文件类型来隐藏恶意意图”。

名为 `offsec-certified-professional.png` 的文件是数据格式的“缝合怪”：它同时充当视觉诱饵（简历图片）、PDF 文档和恶意批处理脚本容器。

感染链依赖对 Windows 标准工具 `ftp.exe` 的巧妙滥用：当受害者点击 LNK 文件时，它不会直接打开文档，而是触发 `ftp.exe` 执行多语言文件中隐藏的命令。

“ZIP 文件包含两个文件：一个作为诱饵和第二阶段载荷的文档，以及一个触发初始操作的 LNK 文件。”

### LOTUSHARVEST：DLL 侧载与数据窃取流程

脚本执行后，会从图片文件中提取 **Base64 编码的二进制数据**，并将其解码为名为 `MsCtfMonitor.dll` 的恶意 DLL——这是活动的主要武器，研究人员将其命名为 **LOTUSHARVEST**（一种 C++ 植入程序）。

恶意软件采用 **DLL 侧载技术**：将合法 Windows 工具 `ctfmon.exe` 复制到新文件夹，使其在不知情的情况下加载恶意 DLL。激活后，LOTUSHARVEST 作为无情的信息窃取器开始工作。

它专门针对 Google Chrome 和 Microsoft Edge 的浏览器数据，提取内容包括：

1. **浏览历史**：“最近访问的 20 个 URL”
2. **凭据**：存储的登录数据，通过 Windows API 解密

被盗数据随后被泄露至攻击者控制的域名，例如 `eol4hkm8mfoeevs[.]m[.]pipedream[.]net`。

本文翻译自securityonline [原文链接](https://securityonline.info/operation-hanoi-thief-hackers-use-pseudo-polyglot-lnk-image-to-deploy-lotusharvest-stealer-via-dll-sideloading/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313495](/post/id/313495)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/operation-hanoi-thief-hackers-use-pseudo-polyglot-lnk-image-to-deploy-lotusharvest-stealer-via-dll-sideloading/)

如若转载,请注明出处： <https://securityonline.info/operation-hanoi-thief-hackers-use-pseudo-polyglot-lnk-image-to-deploy-lotusharvest-stealer-via-dll-sideloading/>

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
* **760**

* 粉丝
* **6**

### TA的文章

* ##### [Devolutions Server 中存在严重漏洞（CVE-2025-13757），已认证的攻击者可利用SQL注入窃取所有存储的密码](/post/id/313498)

  2025-12-01 17:48:48
* ##### [新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃](/post/id/313501)

  2025-12-01 17:48:27
* ##### [GeoServer 中存在高危漏洞（CVE-2025-58360），可利用未授权的XXE攻击实现文件窃取与服务端请求伪造](/post/id/313505)

  2025-12-01 17:48:01
* ##### [新型恶意软件即服务运营商 TAG-150 利用 ClickFix 诱饵及自定义 CastleLoader，已入侵美国境内 469 台设备](/post/id/313509)

  2025-12-01 17:47:16
* ##### [OpenAI在ChatGPT安卓测试版中启动广告功能测试，引发用户对数据隐私的担忧](/post/id/313514)

  2025-12-01 17:46:49

### 相关文章

* ##### [Devolutions Server 中存在严重漏洞（CVE-2025-13757），已认证的攻击者可利用SQL注入窃取所有存储的密码](/post/id/313498)

  2025-12-01 17:48:48
* ##### [新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃](/post/id/313501)

  2025-12-01 17:48:27
* ##### [GeoServer 中存在高危漏洞（CVE-2025-58360），可利用未授权的XXE攻击实现文件窃取与服务端请求伪造](/post/id/313505)

  2025-12-01 17:48:01
* ##### [新型恶意软件即服务运营商 TAG-150 利用 ClickFix 诱饵及自定义 CastleLoader，已入侵美国境内 469 台设备](/post/id/313509)

  2025-12-01 17:47:16
* ##### [OpenAI在ChatGPT安卓测试版中启动广告功能测试，引发用户对数据隐私的担忧](/post/id/313514)

  2025-12-01 17:46:49
* ##### [美国CISA已将OpenPLC ScadaBR系统中正遭积极利用的XSS漏洞（CVE-2021-26829）列入其关键漏洞目录](/post/id/313517)

  2025-12-01 17:46:23
* ##### [“哈希劫持”攻击手法通过操纵URL片段标识符（#）来操控AI浏览器的行为](/post/id/313521)

  2025-12-01 17:45:53

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