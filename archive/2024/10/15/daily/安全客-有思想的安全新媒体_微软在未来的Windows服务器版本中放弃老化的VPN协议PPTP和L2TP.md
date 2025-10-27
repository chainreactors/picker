---
title: 微软在未来的Windows服务器版本中放弃老化的VPN协议PPTP和L2TP
url: https://www.anquanke.com/post/id/300842
source: 安全客-有思想的安全新媒体
date: 2024-10-15
fetch_date: 2025-10-06T18:45:33.486956
---

# 微软在未来的Windows服务器版本中放弃老化的VPN协议PPTP和L2TP

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

# 微软在未来的Windows服务器版本中放弃老化的VPN协议PPTP和L2TP

阅读量**62361**

发布时间 : 2024-10-14 15:42:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/microsoft-deprecates-aging-vpn-protocols-pptp-and-l2tp-in-future-windows-server-versions/>

译文仅供参考，具体内容表达以及含义原文为准。

微软在即将推出的 Windows Server 版本中淘汰了老旧的点对点隧道协议 (PPTP) 和二层隧道协议 (L2TP)，从而在增强 VPN 安全性方面迈出了重要一步。虽然这些协议长期以来一直是 Windows VPN 的组成部分，但微软鼓励用户过渡到更现代、更安全的替代协议： 安全套接字隧道协议 (SSTP) 和 Internet 密钥交换版本 2 (IKEv2)。

“微软在最近的一份声明中指出：”随着技术的发展，我们的安全协议也必须与时俱进。“作为我们提供最高级别安全和性能的持续承诺的一部分，我们将在未来的 Windows Server 版本中淘汰 PPTP 和 L2TP 协议。”

值得注意的是，弃用并不意味着立即删除。“微软澄清说：”被弃用的功能将继续工作并得到全面支持，直到它们被正式移除。“我们相信您已经将产品生命周期纳入了您的管理策略。即便如此，弃用通知也可以跨越几个月或几年的时间，以帮助您进行必要的过渡。”

此举并不令人意外，因为 PPTP 和 L2TP 存在安全漏洞已有时日。随着威胁环境的不断变化，这些协议已不再被认为足够强大，能够满足现代安全标准。

微软提倡采用 SSTP 和 IKEv2，理由是它们具有卓越的安全性、性能和可靠性。SSTP 利用 SSL/TLS 加密技术提供安全的通信通道，并能无缝穿越防火墙。IKEv2 拥有强大的加密算法、稳健的身份验证和更高的性能，因此特别适合移动用户。

虽然未来的 Windows Server 版本仍允许使用 PPTP 和 L2TP 进行 VPN 输出连接，但将不再支持基于这些协议的输入连接。这一变化旨在引导用户使用更安全的 VPN 配置。

为了促进平稳过渡，微软提供了有关如何安装和配置 SSTP/IKEv2 以实现 VPN 服务器功能的详细说明。

这一停用标志着 Windows Server VPN 功能的重大转变，它优先考虑安全性并鼓励采用现代协议。通过过渡到 SSTP 和 IKEv2，企业可以确保其网络通信在面对不断变化的网络威胁时保持安全、高效和可靠。

本文翻译自securityonline [原文链接](https://securityonline.info/microsoft-deprecates-aging-vpn-protocols-pptp-and-l2tp-in-future-windows-server-versions/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300842](/post/id/300842)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/microsoft-deprecates-aging-vpn-protocols-pptp-and-l2tp-in-future-windows-server-versions/)

如若转载,请注明出处： <https://securityonline.info/microsoft-deprecates-aging-vpn-protocols-pptp-and-l2tp-in-future-windows-server-versions/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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