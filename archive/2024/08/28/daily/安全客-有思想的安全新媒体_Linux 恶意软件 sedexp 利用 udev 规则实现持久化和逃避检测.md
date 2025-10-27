---
title: Linux 恶意软件 sedexp 利用 udev 规则实现持久化和逃避检测
url: https://www.anquanke.com/post/id/299514
source: 安全客-有思想的安全新媒体
date: 2024-08-28
fetch_date: 2025-10-06T18:03:46.586274
---

# Linux 恶意软件 sedexp 利用 udev 规则实现持久化和逃避检测

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

# Linux 恶意软件 sedexp 利用 udev 规则实现持久化和逃避检测

阅读量**63054**

发布时间 : 2024-08-27 11:04:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167567/malware/linux-malware-sedexp.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 研究人员发现了一种名为 sedexp 的新型隐蔽 Linux 恶意软件，它使用 Linux udev 规则来实现持久性并逃避检测。

Aon 的 Cyber Solutions 发现了一个名为 sedexp 的新恶意软件家族，它依赖于一种鲜为人知的 Linux 持久性技术。该恶意软件至少自 2022 年以来一直很活跃，但多年来基本上未被发现。专家指出，该恶意软件采用的持久性方法目前尚未被 MITRE ATT&CK 记录。

该技术允许恶意软件在受感染的系统上保持持久性并隐藏信用卡撇取器代码。

Sedexp 使用 *udev* 规则来维护持久性。*Udev* 是一个系统组件，用于管理 Linux 系统上的设备事件，使其能够根据设备的属性识别设备，并配置规则以在设备插入或移除时触发操作。这种对 *udev* 规则的创新使用使 sedexp 作为一种持久化机制脱颖而出。

“在最近的一次调查中，Stroz Friedberg 发现了使用 udev 规则来保持持久性的恶意软件。这种技术允许恶意软件在每次发生特定设备事件时执行，使其隐蔽且难以检测，“AON 发布的[**报告**](https://www.aon.com/en/insights/cyber-labs/unveiling-sedexp)写道。“此规则确保在加载 */dev/random* 时运行恶意软件。*/dev/random* 是一个用作随机数生成器的特殊文件，被各种系统进程和应用程序用来获取加密操作、安全通信和其他需要随机性的功能的熵。它在每次重启时由操作系统加载，这意味着此规则将有效地确保 sedexp 脚本在系统重启时运行。

*sedexp* 恶意软件有两个显着特点：

1. **反向 Shell 功能：**它允许攻击者远程保持对受感染系统的控制。
2. **Stealth 的内存修改：**该恶意软件修改内存以从 or 等命令中隐藏包含字符串“sedexp”的文件，有效地隐藏了 webshell、修改后的 Apache 配置文件和 *udev* 规则本身。`ls``find`

研究人员认为，恶意软件 sedexp 背后的威胁行为者是出于经济动机。

“sedexp 的发现表明，除了勒索软件之外，出于经济动机的威胁行为者已经进化出了复杂性。利用很少使用的持久性技术（如 udev 规则）凸显了对全面和高级取证分析的需求。“组织应不断更新其检测能力，实施全面的安全措施来减轻此类威胁，并确保聘请有能力的 DFIR 公司完成对任何可能受损的服务器的取证审查。”

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167567/malware/linux-malware-sedexp.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299514](/post/id/299514)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167567/malware/linux-malware-sedexp.html)

如若转载,请注明出处： <https://securityaffairs.com/167567/malware/linux-malware-sedexp.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

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

* [研究人员发现了一种名为 sedexp 的新型隐蔽 Linux 恶意软件，它使用 Linux udev 规则来实现持久性并逃避检测。](#h2-0)

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