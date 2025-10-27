---
title: Windows 降级攻击有可能使已打补丁的系统遭受旧漏洞的攻击
url: https://www.anquanke.com/post/id/298973
source: 安全客-有思想的安全新媒体
date: 2024-08-10
fetch_date: 2025-10-06T17:59:24.393230
---

# Windows 降级攻击有可能使已打补丁的系统遭受旧漏洞的攻击

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

# Windows 降级攻击有可能使已打补丁的系统遭受旧漏洞的攻击

阅读量**39949**

发布时间 : 2024-08-09 14:43:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/windows-downgrade-attack-risks-exposing.html>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft表示，它正在开发安全更新，以解决两个漏洞，据称这两个漏洞可能被滥用于对Windows更新架构进行降级攻击，并用旧版本替换当前版本的操作系统文件。

下面列出了这些漏洞 –

* **CVE-2024-38202** （CVSS 分数：7.3） – Windows 更新堆栈特权提升漏洞CVE-2024-38202 （CVSS score： 7.3） – Windows Update Stack Elevation of Privilege Vulnerability
* **CVE-2024-21302** （CVSS 评分：6.7） – Windows 安全内核模式特权提升漏洞CVE-2024-21302 （CVSS score： 6.7） – Windows Secure Kernel Mode Elevation of Privilege Vulnerability

SafeBreach Labs 研究员 Alon Leviev 因发现和报告这些漏洞而受到赞誉，他在 Black Hat USA 2024 和 DEF CON 32 上展示了这些发现

这家科技巨头表示，CVE-2024-38202 植根于 Windows 备份组件，允许“具有基本用户权限的攻击者重新引入以前缓解的漏洞或规避基于虚拟化的安全 （VBS） 的某些功能”。

但是，它指出，试图利用该漏洞的攻击者必须说服管理员或具有委托权限的用户执行系统还原，从而无意中触发该漏洞。

第二个漏洞还涉及支持 VBS 的 Windows 系统中的权限提升情况，这实际上允许攻击者用过时的版本替换 Windows 系统文件的当前版本。

CVE-2024-21302 的后果是，它可能会被武器化，以重新引入以前解决的安全漏洞、绕过 VBS 的某些功能并泄露受 VBS 保护的数据。

列维耶夫详细介绍了一个名为Windows Downdate的工具，他说它可以用来将“完全修补的Windows机器容易受到数千个过去漏洞的影响，将修复的漏洞变成零日漏洞，并使’完全修补’一词在世界上任何Windows机器上都毫无意义。

Leviev补充说，该工具可以“接管Windows更新过程，以在关键操作系统组件上制作完全无法检测，不可见，持续和不可逆的降级，这使我能够提升权限并绕过安全功能。

此外，Windows Downdate 能够绕过验证步骤，例如完整性验证和受信任的安装程序强制执行，从而有效地降级关键操作系统组件，包括动态链接库 （DLL）、驱动程序和 NT 内核。

除此之外，这些问题还可能被利用来降级 Credential Guard 的隔离用户模式进程、安全内核和 Hyper-V 的虚拟机监控程序，以暴露过去的权限提升漏洞，以及禁用 VBS 以及虚拟机监控程序保护的代码完整性 （HVCI） 等功能。

最终的结果是，一个完全修补的Windows系统可能会容易受到数千个过去漏洞的影响，并将修复的缺点变成零日漏洞。

这些降级会产生额外的影响，因为操作系统报告系统已完全更新，同时阻止安装将来的更新，并禁止通过恢复和扫描工具进行检测。

Leviev 说：“我能够在 Windows 内的虚拟化堆栈上实现降级攻击是可能的，因为设计缺陷允许权限较低的虚拟信任级别/环更新位于特权更高的虚拟信任级别/环中的组件。

“这非常令人惊讶，因为 Microsoft 的 VBS 功能是在 2015 年发布的，这意味着我发现的降级攻击面已经存在了近十年。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/windows-downgrade-attack-risks-exposing.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298973](/post/id/298973)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/windows-downgrade-attack-risks-exposing.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/windows-downgrade-attack-risks-exposing.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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