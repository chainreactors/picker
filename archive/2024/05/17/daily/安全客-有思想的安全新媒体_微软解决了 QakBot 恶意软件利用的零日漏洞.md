---
title: 微软解决了 QakBot 恶意软件利用的零日漏洞
url: https://www.anquanke.com/post/id/296539
source: 安全客-有思想的安全新媒体
date: 2024-05-17
fetch_date: 2025-10-06T17:14:34.520629
---

# 微软解决了 QakBot 恶意软件利用的零日漏洞

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

# 微软解决了 QakBot 恶意软件利用的零日漏洞

阅读量**98910**

发布时间 : 2024-05-16 11:39:40

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/zero-day-exploited-by-qakbot-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

微软修补了一个零日漏洞，攻击者利用该漏洞在易受影响的 Windows 系统上分发 QakBot 和其他恶意软件有效负载。

该漏洞编号为CVE-2024-30051，是由于桌面窗口管理器 (DWM) 核心库中基于堆的缓冲区溢出而导致的权限提升缺陷。微软表示，成功利用该漏洞将授予攻击者“系统权限”。

“这些类型的错误通常与代码执行错误相结合来接管目标，并且经常被勒索软件（攻击者）使用，” 零日计划的达斯汀·蔡尔兹（Dustin Childs）说。

桌面窗口管理器 (dwm.exe) 在 Windows Vista 中引入，是一个合成窗口管理器，可呈现 Windows 中的所有 GUI 效果，如透明窗口、实时任务栏缩略图、Flip3D，甚至高分辨率显示器支持。

应用程序不会直接在屏幕上绘制。相反，他们将窗口图像写入内存中的特定位置。然后，Windows 将所有这些窗口组合并创建一个“复合”视图，然后将其发送到监视器。这允许 Windows 在显示窗口时添加透明度和动画等效果。

卡巴斯基研究人员在调查另一个 Windows DWM 核心库权限升级漏洞（编号为 CVE-2023-36033）时发现了此漏洞，该漏洞也被用作攻击中的零日漏洞。

在分析与最近的漏洞和相关攻击相关的数据时，卡巴斯基研究人员发现了一个于 4 月 1 日上传到 VirusTotal 的有趣文件。该文件的名称暗示它包含有关 Windows 漏洞的详细信息。

该文件包含有关 Windows DWM 漏洞的信息（用蹩脚的英语编写），可利用该漏洞将权限升级到系统级别，利用过程几乎与 CVE-2023-36033 攻击中使用的过程相同，“但该漏洞不同， “研究人员说。

最初由于该文档的质量和缺乏利用该漏洞的关键细节而受到怀疑，进一步调查证实了另一个能够进行权限升级的零日漏洞的合法性。卡巴斯基立即向微软报告了这一问题，导致其被指定为 CVE-2024-30051，并随后在本月的补丁星期二进行了修补。

**QakBot 利用的零日漏洞**
在向微软报告后，卡巴斯基继续监控利用此缺陷的漏洞和攻击。

“四月中旬，我们发现了针对此零日漏洞的利用。我们已经看到它与 QakBot 和其他恶意软件一起使用，并相信多个威胁行为者可以访问它，”卡巴斯基说。

Childs 表示，谷歌威胁分析小组、DBAPPSecurity WeBin 实验室和谷歌旗下的 Mandiant 的安全研究人员也向微软报告了该零日漏洞，指出恶意软件攻击中可能存在广泛的利用。

“不要等待测试和部署此更新，因为既然补丁可用于逆向工程，那么漏洞利用可能会增加，” Childs 说。

美国网络安全和基础设施安全局还将 CVE-2024-30051 添加到其已知利用的漏洞目录中，并指示所有联邦机构在 6 月 4 日之前完成修补过程。

一旦用户有足够的时间更新其 Windows 系统，卡巴斯基计划披露 CVE-2024-30051 的技术细节。

**QakBot 从银行木马到初始访问代理的旅程**
QakBot，也称为 Qbot，于 2008 年作为银行木马出现，用于窃取凭据、网站 cookie 和信用卡以实施金融欺诈。 QakBot 运营商多年来发展成为初始访问代理，与其他威胁团体合作，为勒索软件攻击、间谍活动和数据盗窃提供对企业和家庭网络的初始访问。

在 FBI 牵头的一次名为“猎鸭行动”的多国执法行动之后，QakBot 的基础设施于 2023 年 8 月被拆除。但微软在 12 月份发现QakBot 在针对酒店业的网络钓鱼活动中卷土重来。

执法部门将 QakBot 感染与 700,000 台受害计算机联系起来，其中包括针对全球企业、医疗保健提供者和政府机构的勒索软件攻击，据保守估计，这些攻击造成了数亿美元的损失。

多年来，Qakbot 一直是各种勒索软件团伙及其附属机构的初始感染媒介，包括 Conti、ProLock、Egregor、REvil、RansomExx、MegaCortex 以及最近的 Black Basta。

另一个零日修复
Microsoft 在 2024 年 5 月补丁星期二版本中修补了 59 个 CVE，其中 1 个被评为“严重”，57 个被评为“重要”，1 个被评为“中等”。

该补丁还修复了 QakBot 所利用的另一个零日漏洞。另一个漏洞编号为CVE-2024-30040，在 CVSS 等级上被评为“重要”，是一个 Windows MSHTML 平台安全功能绕过漏洞。 MSHTML 是 Microsoft Windows 版本的 Internet Explorer 的专有浏览器引擎。

微软表示：“该漏洞绕过了 Microsoft 365 和 Microsoft Office 中的 OLE 缓解措施，从而保护用户免受易受攻击的 COM/OLE 控件的影响。”

通过社交方式诱使受害者打开恶意文档的黑客将能够通过在 Microsoft 办公应用程序套件中传递 OLE 缓解措施来执行任意代码。

本文翻译自 [原文链接](https://thecyberexpress.com/zero-day-exploited-by-qakbot-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296539](/post/id/296539)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/zero-day-exploited-by-qakbot-malware/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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