---
title: Kimsuky组织：在持续的网络攻击中转向编译HTML 帮助文件
url: https://www.anquanke.com/post/id/294300
source: 安全客-有思想的安全新媒体
date: 2024-03-26
fetch_date: 2025-10-04T12:11:14.965039
---

# Kimsuky组织：在持续的网络攻击中转向编译HTML 帮助文件

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

# Kimsuky组织：在持续的网络攻击中转向编译HTML 帮助文件

阅读量**87710**

发布时间 : 2024-03-25 10:59:39

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/03/n-korea-linked-kimsuky-shifts-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

据观察，与朝鲜有关的威胁组织Kimsuky（又名 Black Banshee、Emerald Sleet 或 Springtail）改变了策略，利用编译的 HTML 帮助 (CHM) 文件作为载体来传播恶意软件以收集敏感数据。

Kimsuky 至少自 2012 年以来一直活跃，其目标是位于韩国以及北美、亚洲和欧洲的实体。

据 Rapid7 称，攻击链利用了武器化的 Microsoft Office 文档、ISO 文件和 Windows 快捷方式 (LNK) 文件，该组织还利用 CHM 文件在受感染的主机上部署恶意软件。

该网络安全公司以过去观察到的类似间谍活动为由，以适度的信心将这一活动归咎于 Kimsuky。

该公司表示：“虽然 CHM 文件最初是为帮助文档而设计的，但它也被用于恶意目的，例如分发恶意软件，因为它们在打开时可以执行 JavaScript。”

CHM 文件在 ISO、VHD、ZIP 或 RAR 文件中传播，打开后执行 Visual Basic 脚本 (VBScript) 以设置持久性并连接到远程服务器以获取负责收集和泄露的下一阶段有效负载敏感数据。

Rapid7 称这些攻击持续且不断演变，针对的是韩国的组织。它还确定了一种替代感染序列，该序列采用 CHM 文件作为起点，删除负责收集信息的批处理文件和连接到 C2 服务器并传输数据的 PowerShell 脚本。

报告称：“作案手法以及代码和工具的重用表明，威胁行为者正在积极使用和完善/重塑其技术和策略，以从受害者那里收集情报。”

博通旗下的赛门铁克透露，Kimsuky 攻击者正在传播冒充韩国合法公共实体应用程序的恶意软件。

赛门铁克表示：“一旦受到威胁，植入程序就会安装 Endor 后门恶意软件。 ” “这种威胁使攻击者能够从受害者那里收集敏感信息或安装其他恶意软件。”

值得注意的是，基于 Golang 的 Endor 与 Troll Stealer（又名 TrollAgent）最近被部署用于针对从韩国建筑相关协会网站下载安全程序的用户的网络攻击。

联合国对朝鲜民族国家行为体在 2017 年至 2023 年间实施的 58 起疑似网络攻击进行了调查，这些攻击为朝鲜进一步发展核武器计划带来了 30 亿美元的非法收入。

报告称：“据报道，侦察总局下属的黑客组织仍在继续发动大量网络攻击。 ” “趋势包括针对国防公司和供应链，以及越来越多地共享基础设施和工具。”

侦察总局 (RGB) 是朝鲜主要的对外情报机构，由被广泛追踪的拉撒路集团及其下属组织安达里尔和布鲁诺罗夫以及金苏基组成的威胁集群组成。

报告进一步补充说：“Kimsuky 对使用生成人工智能（包括大型语言模型）表现出了兴趣，可能用于编码或编写网络钓鱼电子邮件。” “据观察 Kimsuky 使用 ChatGPT。”

本文翻译自 [原文链接](https://thehackernews.com/2024/03/n-korea-linked-kimsuky-shifts-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294300](/post/id/294300)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/03/n-korea-linked-kimsuky-shifts-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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