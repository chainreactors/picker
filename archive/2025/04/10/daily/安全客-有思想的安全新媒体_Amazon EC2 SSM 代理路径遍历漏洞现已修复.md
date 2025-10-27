---
title: Amazon EC2 SSM 代理路径遍历漏洞现已修复
url: https://www.anquanke.com/post/id/306297
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:04:05.433095
---

# Amazon EC2 SSM 代理路径遍历漏洞现已修复

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

# Amazon EC2 SSM 代理路径遍历漏洞现已修复

阅读量**46951**

发布时间 : 2025-04-09 10:14:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/04/amazon-ec2-ssm-agent-flaw-patched-after.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员披露了Amazon EC2 Simple Systems Manager （SSM）代理中一个现已修复的安全漏洞的详细信息。如果该漏洞被成功利用，攻击者可能会实现权限提升和代码执行。

网络安全公司 Cymulate 在一份与 The Hacker News 分享的报告中称，该漏洞可能使攻击者在文件系统上非预期的位置创建目录，以 root 权限执行任意脚本，并且很可能通过将文件写入系统的敏感区域来提升权限或进行恶意活动。

Amazon SSM 代理是 Amazon Web Services（AWS）的一个组件，它使管理员能够在 EC2 实例和本地服务器上进行远程管理、配置和执行命令。

该软件处理在 SSM 文档中定义的命令和任务，这些文档可以包含一个或多个插件，每个插件负责执行特定的任务，例如运行 Shell 脚本或自动化部署及配置相关的活动。

此外，SSM 代理会根据插件规范动态创建目录和文件，通常会将插件 ID 作为目录结构的一部分。这也带来了安全风险，因为对这些插件 ID 的验证不当可能会导致潜在的漏洞。

Cymulate 发现的是一个路径遍历漏洞，这是由于对插件 ID 的验证不当而产生的。该漏洞可能使攻击者能够操纵文件系统并以提升的权限执行任意代码。这个问题源于 pluginutil.go 文件中一个名为 “ValidatePluginId” 的函数。

安全研究人员 Elad Beber 表示：“这个函数未能正确清理输入内容，使得攻击者能够提供包含路径遍历序列（例如../）的恶意插件 ID。”

由于这个漏洞，攻击者在创建 SSM 文档时（例如 ../../../../../../malicious\_directory），基本上可以提供一个精心构造的插件 ID，从而在底层文件系统上执行任意命令或脚本，为权限提升和其他漏洞利用后的操作铺平道路。

在 2025 年 2 月 12 日进行了负责任的漏洞披露之后，该漏洞于 2025 年 3 月 5 日随着 Amazon SSM 代理 3.3.1957.0 版本的发布而得到修复。

根据该项目维护者在 GitHub 上分享的版本说明，“添加并使用 BuildSafePath 方法，以防止在编排目录中出现路径遍历问题。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/04/amazon-ec2-ssm-agent-flaw-patched-after.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306297](/post/id/306297)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/04/amazon-ec2-ssm-agent-flaw-patched-after.html)

如若转载,请注明出处： <https://thehackernews.com/2025/04/amazon-ec2-ssm-agent-flaw-patched-after.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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