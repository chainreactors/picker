---
title: LemonDuck利用EternalBlue漏洞进行加密挖掘攻击
url: https://www.anquanke.com/post/id/300586
source: 安全客-有思想的安全新媒体
date: 2024-10-09
fetch_date: 2025-10-06T18:48:57.476573
---

# LemonDuck利用EternalBlue漏洞进行加密挖掘攻击

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

# LemonDuck利用EternalBlue漏洞进行加密挖掘攻击

阅读量**60661**

发布时间 : 2024-10-08 11:33:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/lemonduck-exploits-eternalblue-vulnerability-for-cryptomining-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

来自奥法和NetbyteSEC安全研究人员的最新报告揭示了LemonDuck恶意软件的死灰复燃，该恶意软件现在正在利用微软服务器消息块（SMB）协议中的EternalBlue漏洞（CVE-2017-0144）来促进加密攻击。臭名昭著的漏洞 EternalBlue最早被臭名昭着的 WannaCry 勒索软件利用，它仍然是 LemonDuck等恶意软件的关键入侵点，后者瞄准网络资源来挖掘加密货币，同时逃避检测。

LemonDuck被确认为一种复杂的加密挖矿恶意软件，使用多种攻击向量，包括钓鱼电子邮件、强力密码攻击和SMB攻击。一旦它能够访问一个易受的系统，它就会建立控制并利用机器的处理能力进行加密。“LemonDuck 使用PowerShell来避免检测，部署各种恶意有效载荷，并针对系统进行加密劫持，”研究人员指出。

攻击始于对SMB服务的蛮干攻击，利用EternalBlue漏洞获取未经授权的访问。在报告的案例研究中，研究人员透露，攻击者来自台湾台中市的一个IP，成功地破坏了一个SMB服务，授予他们管理权限。根据该报告，“攻击者为C:驱动器创建了一个隐藏的管理共享，使得在受害者不知情的情况下能够远程访问。”

攻击者一旦获得访问权，就会使用批处理文件p.bat来发起一系列恶意操作。这些操作包括复制恶意文件（msInstall.exe），对其进行重命名，以及设置防火墙规则以将流量重定向到远程服务器。报告指出，“该批处理文件还执行一个编码为 base64的PowerShell脚本，从远程URL下载其他恶意软件，并安排任务以确保持久执行。”

LemonDuck的主要目标是利用系统资源进行加密挖掘。为了达到这个目的，恶意软件使用各种技术来保持持久性和避免被检测到。其中一种方法包括禁用Windows Defender实时保护，并将整个C:驱动器添加到排除列表中，确保安全软件忽略恶意活动。该报告强调，“此恶意软件能够禁用Windows Defender的实时保护，并为整个C:驱动器和PowerShell进程，以避免被检测。”

该恶意软件还操纵网络设置，在与DNS相关的规则下打开TCP端口（65532、65531、65539），并使用端口代理将出站流量伪装成合法的DNS请求。这使得恶意软件能够与其命令与控制（C2）服务器通信并泄漏数据，而不会在典型的网络监控系统中引起警报。

该报告提供了几个与LemonDuck相关的折衷指标（IOC），包括IP地址、URL和恶意可执行文件。攻击中标记的关键URL之一是http://t.amynx.com/gim.jsp,用于下载额外的恶意软件有效载荷。VirusTotal 已将此URL标记为恶意，并将其与加密活动联系起来。

为了减轻这些攻击，我们敦促组织对其系统进行补丁，以抵御已知的漏洞，特别是 EternalBlue （CVE-2017-0144）。定期更新软件并使用能够检测网络横向移动的高级安全解决方案，对于防止 LemonDuck 这样的恶意软件站稳脚跟至关重要。

LemonDuck 恶意软件继续发展，采用了强力SMB漏洞、加密有效载荷和高级规避技术相结合的方式来破坏易受的系统。正如报告所指出的，“对于组织来说，确保定期更新所有操作系统和软件以防范已知漏洞（包括 EternalBlue （CVE-2017-0144））至关重要，以最大限度地降低被泄露的风险。”

本文翻译自securityonline [原文链接](https://securityonline.info/lemonduck-exploits-eternalblue-vulnerability-for-cryptomining-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300586](/post/id/300586)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/lemonduck-exploits-eternalblue-vulnerability-for-cryptomining-attacks/)

如若转载,请注明出处： <https://securityonline.info/lemonduck-exploits-eternalblue-vulnerability-for-cryptomining-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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