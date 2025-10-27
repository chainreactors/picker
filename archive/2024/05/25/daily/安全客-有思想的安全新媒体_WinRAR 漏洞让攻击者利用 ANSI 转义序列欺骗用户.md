---
title: WinRAR 漏洞让攻击者利用 ANSI 转义序列欺骗用户
url: https://www.anquanke.com/post/id/296784
source: 安全客-有思想的安全新媒体
date: 2024-05-25
fetch_date: 2025-10-06T17:17:08.744367
---

# WinRAR 漏洞让攻击者利用 ANSI 转义序列欺骗用户

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

# WinRAR 漏洞让攻击者利用 ANSI 转义序列欺骗用户

阅读量**138626**

发布时间 : 2024-05-24 11:52:14

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybersecuritynews.com/winrar-flaw-deceive-users/>

译文仅供参考，具体内容表达以及含义原文为准。

Windows 上流行的文件压缩和归档实用程序 WinRAR 中发现了一个严重漏洞。

该漏洞编号为 CVE-2024-36052，影响 WinRAR 7.00 之前的版本，允许攻击者使用 ANSI 转义序列欺骗屏幕输出。

问题源于 WinRAR 缺乏对 ZIP 档案中文件名的正确验证和清理。Siddharth Dushantha 发现了这个漏洞。

当使用 WinRAR 提取包含名称中带有ANSI 转义序列的文件的特制 ZIP 档案时，该应用程序无法正确处理转义序列。

相反，它将它们解释为控制字符，允许攻击者操纵显示的文件名并可能诱骗用户运行恶意文件。

ANSI 转义序列是用于控制命令行界面和终端中文本格式和外观的特殊代码。大多数序列以 ASCII 转义字符 (ESC、\x1B) 开头，后跟括号字符 ([)，并嵌入到文本中。

通过制作包含这些序列的恶意档案，攻击者可以操纵显示的输出并欺骗用户相信他们正在打开无害的文件，例如 PDF 或图像。

当用户尝试在WinRAR中打开看似无害的文件时，由于对文件扩展名处理不当，漏洞就会被触发。

Dushantha表示，WinRAR 的 ShellExecute 函数没有启动预期的文件，而是收到了错误的参数并执行了隐藏的恶意脚本，例如批处理文件 (.bat) 或命令脚本 (.cmd) 。

![]()

然后，该脚本可以在受害者的设备上安装恶意软件，同时显示诱饵文档以避免引起怀疑。

值得注意的是，此漏洞特定于 Windows 上的 WinRAR，与影响 Linux 和 UNIX 平台上的 WinRAR 的 CVE-2024-33899 不同。

WinRAR 的 Linux 和 UNIX 版本也容易受到通过 ANSI 转义序列的屏幕输出欺骗和拒绝服务攻击。

为了减轻此漏洞带来的风险，建议用户更新到 WinRAR 7.00 或更高版本，其中包含针对该问题的修复。

此外，打开来自不受信任来源的档案时要小心谨慎，并在 Windows 中启用文件扩展名可见性，可以帮助防止此类攻击。

该漏洞于 2024 年 5 月 23 日公开披露，WinRAR 用户必须立即采取行动，保护他们的系统免受恶意行为者的潜在利用。

本文翻译自 [原文链接](https://cybersecuritynews.com/winrar-flaw-deceive-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296784](/post/id/296784)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybersecuritynews.com/winrar-flaw-deceive-users/>

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

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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