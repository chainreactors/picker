---
title: Linux USB 音频驱动漏洞或致攻击者执行任意代码
url: https://www.anquanke.com/post/id/306331
source: 安全客-有思想的安全新媒体
date: 2025-04-11
fetch_date: 2025-10-06T22:03:08.600472
---

# Linux USB 音频驱动漏洞或致攻击者执行任意代码

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

# Linux USB 音频驱动漏洞或致攻击者执行任意代码

阅读量**42934**

发布时间 : 2025-04-10 09:47:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/linux-usb-audio-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

Linux 内核中 USB 音频驱动程序存在一个严重漏洞，该漏洞可能导致内存越界读取。最近，SUSE 公司的 Takashi Iwai 编写了一个针对 Linux 内核的补丁，解决了这一问题。

Linux 内核中的 USB 音频驱动程序存在内存越界访问漏洞，这可能使得能够物理接触系统的攻击者利用恶意 USB 设备来提升权限、修改系统内存或运行任意代码。

Linux 内核更新修复 USB 音频漏洞 该修复方案由 Linux 基金会的 Greg Kroah-Hartman 于 2024 年 12 月 14 日提交，提升了使用 USB 音频设备的系统中驱动程序的稳定性和安全性。

****攻击原理****

当 USB 音频设备提供的描述符的 “bLength” 值比预期的结构大小短的时候，就会出现这个漏洞。在原来的代码中，驱动程序盲目地认为 descriptor 是完整的，并试图读取其字段，如 clock ID 或 pin arrays。

如果由于硬件缺陷或蓄意操纵导致描述符被截断，驱动程序可能会读取超出已分配内存缓冲区的范围，访问到相邻的、非预期的区域。

这种内存越界读取可能会从内核内存中泄露敏感数据，比如指针或用户信息，或者通过访问无效内存地址导致系统崩溃。

在最坏的情况下，技术娴熟的攻击者可以将这个漏洞与其他漏洞利用手段结合起来，以提升权限或执行任意代码，不过这样的攻击需要对 USB 设备进行精确控制，并且还需要其他漏洞的配合。

Iwai 在补丁说明中表示：“这次更新是保护与 USB 音频硬件交互的 Linux 系统的一个积极举措。” 该修复方案已被反向移植到稳定的内核分支中，确保各种发行版的用户都能从增强的安全性中受益。

时钟选择器描述符包含一个可变长度数组和其他字段，鉴于其在 USB 音频类（UAC）第 2 版和第 3 版中的复杂性，它将接受更全面的验证。

****加强 USB 音频安全性****

这个问题的根源在于驱动程序未能验证 USB 音频设备提供的时钟描述符的 “bLength” 字段。

如果没有这些检查，长度不足的格式错误或恶意构造的描述符可能会触发超出已分配范围的内存访问，有可能导致系统崩溃或被利用。

这个漏洞最初是由 Google 的 Benoît Sevens 报告的，这凸显了它对更广泛的 Linux 社区的重要性。

该补丁对应的提交记录为 ab011f7439d9bbfd34fd3b9cef4b2d6d952c9bb9，它在时钟描述符验证函数中引入了严格的合理性检查。

此次修改仅涉及 sound/usb/clock.c 文件中的 24 行代码，但对于依赖 Linux 进行音频处理的音乐爱好者、开发人员和企业来说，其影响重大。

建议用户更新他们的内核以包含这个补丁，该补丁可通过下载 linux-ab011f7439d9bbfd34fd3b9cef4b2d6d952c9bb9.tar.gz 获取。

这一事态发展凸显了 Linux 社区持续致力于迅速解决漏洞问题，并维护操作系统坚固可靠的声誉。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/linux-usb-audio-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306331](/post/id/306331)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/linux-usb-audio-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/linux-usb-audio-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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