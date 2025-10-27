---
title: 欺骗性验证码：ClickFix 活动利用剪贴板注入传播恶意软件
url: https://www.anquanke.com/post/id/307746
source: 安全客-有思想的安全新媒体
date: 2025-05-27
fetch_date: 2025-10-06T22:23:28.271924
---

# 欺骗性验证码：ClickFix 活动利用剪贴板注入传播恶意软件

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

# 欺骗性验证码：ClickFix 活动利用剪贴板注入传播恶意软件

阅读量**47428**

发布时间 : 2025-05-26 13:09:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/deceptive-captcha-clickfix-campaign-uses-clipboard-injection-to-deliver-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![从 CAPTCHA 到 Lumma Stealer 的感染链示例]()

从 CAPTCHA 到 Lumma Stealer 的感染链示例 | 图片: SentinelOne

威胁行为者已经加强了一项新的社交工程活动,称为“ClickFix”,其中嵌入受损或克隆网站的虚假CAPTCHA提示诱使用户通过剪贴板注入和Windows Run对话框滥用来启动恶意软件。

在最近的一份报告中,SentinelOne揭示了这种欺骗性技术在过去一年中是如何演变的,将用户疲劳与巧妙地使用合法的Windows工具来执行Lumma Stealer和NetSupport RAT等恶意有效载荷相结合。

*“受害者经过社会工程改造,以解决恶意挑战,导致执行PowerShell代码,然后是额外的有效载荷*,”研究人员解释说。

攻击始于一个看似无害的CAPTCHA提示,用户在受损的网站上遇到,虚假的登录门户,钓鱼电子邮件,甚至社交媒体链接。受害者被引导通过一个感觉熟悉的序列 – 验证你是人类,解决一个难题 – 但以更险恶的东西结束。

![剪贴板注入,Windows 运行对话框滥用]()

[Malicious](https://securityonline.info/mcafee-premium-review-all-around-protection-for-your-digital-life-but-is-it-the-best/)恶意的CAPTCHA挑战导致命令执行 | 图片:SentinelOne

*“受害者需要解决CAPTCHA……*然后将剪贴板中的隐藏内容粘贴到Windows’Run’对话框中。

嵌入的脚本将恶意的 PowerShell 或 mshta 命令复制到剪贴板。粘贴到运行对话框并执行后,它会联系命令和控制服务器以下载恶意软件。

ClickFix严重依赖可信系统二进制文件(Living Off the Land Binaries,LOLBins)来绕过传统防御。攻击者通常使用以下工具:

* PowerShell – 用于执行编码的有效载荷。
* mshta.exe – 加载恶意 HTA 内容。
* certutil.exe – 解码或下载二进制文件。

*“Certutil.exe也经常与PowerShell命令或脚本结合使用*,”SentinelOne指出。

ClickFix 活动与几个臭名昭著的恶意软件家族有关:

* Lumma Stealer – 针对浏览器数据、凭据和加密货币钱包的信息窃取者。
* NetSupport RAT – 用于完整系统访问的合法远程管理工具。
* SectopRAT – 一种隐秘的远程访问工具,能够启动隐藏的第二个桌面进行浏览器操作。

*“最常观察到的[有效负载]导致各种信息窃取木马和远程访问工具的下载和推出*,”报告指出。

ClickFix 的独特之处在于它的简单性。没有零日漏洞,没有隐藏的iframe – 只是一个令人信服的假CAPTCHA和用户愿意将命令粘贴到Windows中。

*“ClickFix依赖于用户对反垃圾邮件机制的疲劳*,”SentinelOne警告说。*“事实证明,*欺骗受害者以这种方式感染自己是非常有效的。

本文翻译自securityonline [原文链接](https://securityonline.info/deceptive-captcha-clickfix-campaign-uses-clipboard-injection-to-deliver-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307746](/post/id/307746)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/deceptive-captcha-clickfix-campaign-uses-clipboard-injection-to-deliver-malware/)

如若转载,请注明出处： <https://securityonline.info/deceptive-captcha-clickfix-campaign-uses-clipboard-injection-to-deliver-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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