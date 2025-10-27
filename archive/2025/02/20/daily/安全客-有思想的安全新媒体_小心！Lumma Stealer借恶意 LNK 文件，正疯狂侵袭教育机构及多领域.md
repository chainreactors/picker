---
title: 小心！Lumma Stealer借恶意 LNK 文件，正疯狂侵袭教育机构及多领域
url: https://www.anquanke.com/post/id/304484
source: 安全客-有思想的安全新媒体
date: 2025-02-20
fetch_date: 2025-10-06T20:33:19.008919
---

# 小心！Lumma Stealer借恶意 LNK 文件，正疯狂侵袭教育机构及多领域

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

# 小心！Lumma Stealer借恶意 LNK 文件，正疯狂侵袭教育机构及多领域

阅读量**63125**

|评论**1**

发布时间 : 2025-02-19 10:54:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/lumma-stealer-malware-campaign-targets-educational-institutions-with-deceptive-pdf-lures/>

译文仅供参考，具体内容表达以及含义原文为准。

![Lumma Stealer stealer]()

来源：CloudSEK

CloudSEK 的一份新报告显示，一场正在进行的恶意软件攻击活动正在传播名为 Lumma Stealer 的信息窃取程序，该活动主要针对教育机构，但也影响到了其他各个领域。这场攻击活动使用伪装成合法 PDF 文档的恶意 LNK（快捷方式）文件，诱骗用户启动一个多阶段的感染过程。

攻击者利用受攻击的教育机构的基础设施，在 WebDAV 服务器上托管恶意文件。用户会被以查看学费结构或其他看似无害的文档为由，引诱下载这些文件。当用户点击这些恶意的 LNK 文件时，会执行一个 PowerShell 命令，该命令会下载并运行经过混淆处理的 JavaScript 代码。最终，这段代码会导致 Lumma Stealer 有效载荷的部署。

报告中指出：“这场攻击活动的主要感染途径是使用精心制作成看似合法 PDF 文档的恶意 LNK（快捷方式）文件。” 这些 LNK 文件利用 “独特的特性” 来 “欺骗用户并绕过安全措施，使其成为渗透系统和网络的有效工具”。

一旦被执行，Lumma Stealer 可以窃取各种敏感数据，包括密码、浏览器信息以及加密货币钱包的详细信息。然后，该恶意软件会尝试连接到命令与控制（C2）服务器，以窃取已盗取的数据。

Lumma Stealer 采用了多种逃避检测的技术：

1.混淆的 JavaScript 执行 —— 最初的 LNK 文件会运行一个 PowerShell 脚本，该脚本隐藏在 JavaScript 覆盖代码中。

2.AES 加密有效载荷 —— 该恶意软件会下载一个经过 AES 加密的有效载荷，并使用硬编码密钥以 CBC 模式对其进行解密。

3.数学混淆 ——PowerShell 脚本使用基本的算术技术来隐藏其真实功能。

一旦部署完成，Lumma Stealer 会将窃取到的数据泄露到命令与控制（C2）服务器，使攻击者能够获取密码、加密货币钱包以及浏览器会话的详细信息。

有趣的是，报告指出，该恶意软件还包含一个 Steam 网址，作为备用通信渠道。研究人员解释说：“如果样本无法访问其拥有的每个 C2 域名，它就会使用 Steam 连接。”

正如 CloudSEK 所警告的那样，这场攻击活动仍在继续，很可能会出现新的攻击变种。企业、政府和教育机构必须保持警惕，并积极主动地防范这种迅速演变的网络威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/lumma-stealer-malware-campaign-targets-educational-institutions-with-deceptive-pdf-lures/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304484](/post/id/304484)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/lumma-stealer-malware-campaign-targets-educational-institutions-with-deceptive-pdf-lures/)

如若转载,请注明出处： <https://securityonline.info/lumma-stealer-malware-campaign-targets-educational-institutions-with-deceptive-pdf-lures/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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