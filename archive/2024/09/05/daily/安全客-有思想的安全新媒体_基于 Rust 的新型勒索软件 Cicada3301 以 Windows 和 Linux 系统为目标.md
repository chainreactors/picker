---
title: 基于 Rust 的新型勒索软件 Cicada3301 以 Windows 和 Linux 系统为目标
url: https://www.anquanke.com/post/id/299773
source: 安全客-有思想的安全新媒体
date: 2024-09-05
fetch_date: 2025-10-06T18:20:02.586196
---

# 基于 Rust 的新型勒索软件 Cicada3301 以 Windows 和 Linux 系统为目标

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

# 基于 Rust 的新型勒索软件 Cicada3301 以 Windows 和 Linux 系统为目标

阅读量**126068**

发布时间 : 2024-09-04 14:49:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/new-rust-based-ransomware-cicada3301.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员解开了一种名为 Cicada3301 的新勒索软件变体的内部工作原理，该变体与现已解散的 BlackCat（又名 ALPHV）操作有相似之处。

“Cicada3301 勒索软件似乎主要针对中小型企业 （SMB），可能是通过利用漏洞作为初始访问媒介的机会主义攻击，”网络安全公司 Morphisec 在与 The Hacker News 分享的一份技术报告中表示。

Cicada3301 用 Rust 编写，能够针对 Windows 和 Linux/ESXi 主机，于 2024 年 6 月首次出现，通过 RAMP 地下论坛上的广告邀请潜在的附属公司加入他们的勒索软件即服务 （RaaS） 平台。

勒索软件的一个值得注意的方面是可执行文件嵌入了受感染用户的凭据，然后使用这些凭据来运行 PsExec，这是一种可以远程运行程序的合法工具。

Cicada3301 与 BlackCat 的相似之处还延伸到它使用 ChaCha20 进行加密，使用 fsutil 来评估符号链接和加密重定向文件，以及IISReset.exe停止 IIS 服务和加密可能被锁定以进行修改或删除的文件。

与 BlackCat 的其他重叠包括删除卷影副本、通过操作 bcdedit 实用程序禁用系统恢复、增加 MaxMpxCt 值以支持更高的流量（例如，SMB PsExec 请求）以及使用 wevtutil 实用程序清除所有事件日志。

Cicada3301 还观察到停止本地部署的虚拟机 （VM），这是 Megazord 勒索软件和燕螺王勒索软件之前采用的行为，并终止了各种备份和恢复服务和包含数十个进程的硬编码列表。

除了在加密过程中维护排除文件和目录的内置列表外，勒索软件还针对总共 35 个文件扩展名 – sql、doc、rtf、xls、jpg、jpeg、psd、docm、xlsm、ods、ppsx、png、raw、dotx、xltx、pptx、ppsm、gif、bmp、dotm、xltm、pptm、odp、webp、pdf、odt、xlsb、ptox、mdf、tiff、docx、xlsx、xlam、 potm 和 txt 的

Morphisec 表示，其调查还发现了 EDRSandBlast 等其他工具，这些工具将易受攻击的签名驱动程序武器化以绕过 EDR 检测，BlackByte 勒索软件组织过去也采用了这种技术。

这些发现是在 Truesec 对 Cicada3301 的 ESXi 版本的分析之后得出的，同时还发现有迹象表明该组织可能与 Brutus 僵尸网络的运营商合作，以获得对企业网络的初始访问权限。

“无论 Cicada3301 是 ALPHV 的更名，他们拥有与 ALPHV 相同的开发人员编写的勒索软件，或者他们只是复制了 ALPHV 的一部分来制作自己的勒索软件，时间线表明 BlackCat 的消亡和首先是 Brutus 僵尸网络的出现，然后是 Cicada3301 勒索软件操作，可能都可能是相互关联的，“该公司指出。

针对 VMware ESXi 系统的攻击还需要使用间歇性加密来加密大于设定阈值 （100 MB） 的文件，并使用名为“no\_vm\_ss”的参数来加密文件，而不会关闭主机上运行的虚拟机。

Cicada3301 的出现也促使涉足“神秘”密码谜题的同名“非政治运动”发表声明，称它与勒索软件计划无关。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/new-rust-based-ransomware-cicada3301.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299773](/post/id/299773)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/new-rust-based-ransomware-cicada3301.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/new-rust-based-ransomware-cicada3301.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [勒索攻击](/tag/%E5%8B%92%E7%B4%A2%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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