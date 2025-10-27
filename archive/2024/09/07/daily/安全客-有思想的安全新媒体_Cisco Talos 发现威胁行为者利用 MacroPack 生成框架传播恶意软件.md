---
title: Cisco Talos 发现威胁行为者利用 MacroPack 生成框架传播恶意软件
url: https://www.anquanke.com/post/id/299865
source: 安全客-有思想的安全新媒体
date: 2024-09-07
fetch_date: 2025-10-06T18:22:26.066872
---

# Cisco Talos 发现威胁行为者利用 MacroPack 生成框架传播恶意软件

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

# Cisco Talos 发现威胁行为者利用 MacroPack 生成框架传播恶意软件

阅读量**91438**

发布时间 : 2024-09-06 11:16:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/malware-attackers-using-macropack-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

根据 Cisco Talos 的新调查结果，威胁行为者可能正在使用专门用于红队练习的工具来为恶意软件提供服务。

有问题的程序是一个名为 MacroPack 的有效负载生成框架，用于生成 Office 文档、Visual Basic 脚本、Windows 快捷方式和其他格式，用于渗透测试和社会工程评估。它由法国开发人员 Emeric Nasi 开发。

这家网络安全公司表示，它发现了从中国、巴基斯坦、俄罗斯和美国上传到 VirusTotal 的工件，这些工件都是由 MacroPack 生成的，用于提供各种有效载荷，例如 Havoc、Brute Ratel 和 PhantomCore 的新变体，这是一种远程访问木马 （RAT），归因于一个名为 Head Mare 的黑客组织。

“在我们剖析的所有引起我们注意的恶意文档中，一个共同的特征是存在四个非恶意 VBA 子例程，”Talos 研究员 Vanja Svajcer 说。

“这些子例程出现在所有样本中，并且没有被混淆。它们也从未被任何其他恶意子例程或任何文档中的其他任何地方使用过。

这里需要注意的一个重要方面是，这些文档的诱饵主题多种多样，从指示用户启用宏的通用主题到似乎来自军事组织的官方外观文档。这表明不同的威胁行为者参与其中。

还观察到一些文档利用作为 MacroPack 一部分提供的高级功能，通过使用马尔可夫链创建看似有意义的函数和变量名称来隐藏恶意功能，从而绕过反恶意软件启发式检测。

在 2024 年 5 月至 7 月期间观察到的攻击链遵循一个三步过程，需要发送一个包含 MacroPack VBA 代码的诱杀 Office 文档，然后解码下一阶段的有效负载，最终获取并执行最终的恶意软件。

这一发展表明，威胁行为者不断更新策略以应对中断，并采用更复杂的代码执行方法。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/malware-attackers-using-macropack-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299865](/post/id/299865)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/malware-attackers-using-macropack-to.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/malware-attackers-using-macropack-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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