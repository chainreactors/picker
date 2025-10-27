---
title: 反复出现的 Windows 漏洞可能暴露用户凭据
url: https://www.anquanke.com/post/id/301401
source: 安全客-有思想的安全新媒体
date: 2024-10-31
fetch_date: 2025-10-06T18:51:25.901771
---

# 反复出现的 Windows 漏洞可能暴露用户凭据

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

# 反复出现的 Windows 漏洞可能暴露用户凭据

阅读量**51815**

发布时间 : 2024-10-30 15:36:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：darkreading

原文地址：<https://www.darkreading.com/vulnerabilities-threats/recurring-windows-flaw-could-expose-user-credentials>

译文仅供参考，具体内容表达以及含义原文为准。

![Password hash with salt crypt function concept 3d illustration]()

从Windows 7到目前的Windows 11版本的所有Windows客户端都存在一个0-day漏洞，该漏洞可能允许攻击者从受影响系统的用户那里捕获NTLM身份验证哈希。

ACROS Security的研究人员本周向微软报告了这个漏洞。他们在为CVE-2024-38030编写补丁时发现了这个问题，CVE-2024-38030是一个中等严重性的Windows主题仿冒漏洞，微软在其7月的 security update 中对其进行了缓解。

**之前两个漏洞的变种**

ACROS发现的这个漏洞与CVE-2024-38030非常相似，它实现了一种称为身份验证强制攻击的方式，易受攻击的设备实质上被诱使向攻击者的系统发送NTLM哈希——用户密码的加密表示。Akamai的研究员Tomer Peled在分析微软针对CVE-2024-21320的修复方案时发现了CVE-2024-38030，CVE-2024-21320是另一个更早的Windows主题仿冒漏洞，他发现了这个问题并报告给了微软。ACROS发现的是一个与Peled之前报告的两个漏洞相关的新漏洞。

Windows主题文件允许用户通过壁纸、屏幕保护程序、颜色和声音自定义Windows桌面界面的外观。Akamai研究员Peled发现的这两个漏洞都与主题处理到“BrandImage”或“Wallpaper”这两个图像资源的文件路径的方式有关。Peled发现，由于验证不当，攻击者可以操纵到这些资源的合法路径，以致使Windows自动发送带有用户NTLM哈希的经过身份验证的请求到攻击者的设备。

正如Peled向《Dark Reading》解释的那样，“主题文件格式是一个.ini文件，带有多个’键，值’对。我最初发现了两个可以接受文件路径的键，值对。”

最初的漏洞（CVE-2024-21320）源于这样一个事实：键，值对接受了UNC路径——用于识别网络资源（如共享文件和文件夹）的一种标准化格式——用于网络驱动器，Peled指出。“这意味着一个带有UNC路径的武器化主题文件可以触发带有用户身份验证的外出连接，而他们却不知道。”微软通过在文件路径上添加一个检查来确保它不是一个UNC路径来修复了这个问题。但是，Peled说，微软用于这种验证的函数允许一些绕过，这就是Peled发现第二个漏洞（CVE-2024-38030）的原因。

**微软将“按需”采取行动**

ACROS Security本周报告的问题是第三个根植于同一文件路径问题的Windows主题仿冒漏洞。“我们的研究人员在10月初为CVE-2024-38030编写补丁时发现了这个漏洞，目的是为我们许多用户仍在使用的旧版Windows系统提供补丁，”ACROS Security的首席执行官Mitja Kolsek说。“我们于2024年10月28日将此问题报告给了微软，但我们没有发布详细信息或概念验证，我们计划在微软公开提供他们自己的补丁后这样做。”

微软的一位发言人通过电子邮件表示，公司意识到了ACROS的报告，并将“按需”采取行动，以帮助保护客户。该公司似乎还没有为这个新问题发布CVE（漏洞标识符）。

与Akamai发现的两个之前的Windows主题仿冒漏洞一样，ACROS发现的这个新漏洞也不需要攻击者具备任何特殊权限。“但是他们必须以某种方式让用户将主题文件复制到他们电脑上的其他文件夹，然后用显示图标的视图打开该文件夹，”Kolsek说。“当用户访问攻击者的网站时，该文件也可能自动下载到他们的下载文件夹，在这种情况下，攻击者将不得不等待用户稍后查看下载文件夹。”

Kolsek建议组织尽可能禁用NTLM，但承认这样做可能会导致依赖它的任何网络组件出现功能问题。“攻击者只能成功攻击启用NTLM的计算机。”他说。“另一个要求是由恶意主题文件发起的请求能够到达攻击者在互联网或相邻网络上的服务器，这是防火墙通常应该阻止的，”他指出。因此，攻击者更可能在有针对性的活动中利用这个漏洞，而不是在大规模利用中。

Akamai的Peled说，在没有技术细节的情况下很难知道ACROS的漏洞是什么。“但这可能又是另一个绕过检查的UNC绕过，或者可能是在原始修补过程中遗漏了另一个键，值对。”他说。“UNC路径格式非常复杂，允许奇怪的组合，这使得检测它们非常困难。这可能就是为什么修复如此复杂的原因。”

本文翻译自darkreading [原文链接](https://www.darkreading.com/vulnerabilities-threats/recurring-windows-flaw-could-expose-user-credentials)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301401](/post/id/301401)

安全KER - 有思想的安全新媒体

本文转载自: [darkreading](https://www.darkreading.com/vulnerabilities-threats/recurring-windows-flaw-could-expose-user-credentials)

如若转载,请注明出处： <https://www.darkreading.com/vulnerabilities-threats/recurring-windows-flaw-could-expose-user-credentials>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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