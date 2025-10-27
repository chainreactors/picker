---
title: 被特洛伊木马化的jQuery软件包通过“复杂”的供应链攻击传播
url: https://www.anquanke.com/post/id/297789
source: 安全客-有思想的安全新媒体
date: 2024-07-11
fetch_date: 2025-10-06T17:38:33.761217
---

# 被特洛伊木马化的jQuery软件包通过“复杂”的供应链攻击传播

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

# 被特洛伊木马化的jQuery软件包通过“复杂”的供应链攻击传播

阅读量**245384**

发布时间 : 2024-07-10 19:33:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/trojanized-jquery-packages-complex-supply-chain-attack>

译文仅供参考，具体内容表达以及含义原文为准。

网络攻击者再次将目标对准了 JavaScript 开发人员——这一次是“复杂而持久的供应链攻击”，该攻击在 GitHub、Node Package Manager （npm） 和 jsDelivr 存储库中分发流行的 JavaScript 库 jQuery 的木马包。

每个软件包中都包含了一个jQuery的副本，但有一个细微的不同：end函数，作为jQuery原型的一部分，被修改以包含额外的恶意代码，设计用于提取网站表单数据并将其发送到众多URL之一。

Phylum研究团队指出，值得注意的是，攻击者展示出一种不同寻常的命名规则和归属模式的缺乏，这偏离了这类软件供应链攻击的典型特征；由于在各软件包之间具有高度的变化性，这一点显得尤为突出，团队在近期的博客文章中写道。

根据研究，自从5月26日起，未知的攻击者已经开始散布数十个恶意的jQuery软件包。Phylum的研究人员最初在npm（JavaScript运行时Node.js的默认包管理器）上发现了第一个恶意jQuery变体；此变体随后在一个多月的时间内在数十个npm软件包中发布。之后，研究人员在其他平台上，如GitHub，甚至在jsDelivr的CDN托管资源中发现了特洛伊木马化的jQuery实例。

研究人员说，到目前为止，已发布的包裹的数量“相对较小”，总共发现了约68个。这些软件包通常命名为jquery.min.js，还有其他变体如registration.min.js、icon.min.js和fontawesome.js。根据文章，“每个软件包的外泄URL几乎都是独一无二的，攻击者以新用户名在npm下发布。”有时，单一用户会发布多个相关联的恶意jQuery软件包，而其他时候，攻击者在同一项目中包含了多个具有不同名称的文件版本。此外，几乎每个软件包还包含了一些通常不在npm发布中出现的个人文件，如npm缓存文件夹、npm日志文件夹以及termux.properties文件。

“总体而言，这次攻击与我们以往在这个规模上所见到的大多数攻击不同，后者通常具有清晰、明确定义的模式和明显的自动化特征，”团队指出。“在这里，软件包的即兴性质和定制变化性，加上它们发布的长时间跨度，表明每个软件包可能是手工组装和发布的。”

## 是否进行有针对性的供应链攻击？

攻击的手动性质与证据相吻合，表明它似乎是有针对性的努力：恶意软件需要一组特定的受害者操作才能执行。

“要触发恶意软件，用户必须安装其中一个恶意软件包，使用包含的木马化jQuery文件，然后调用end函数或fadeTo函数，”该帖子称。

也就是说，虽然 end 函数本身似乎并没有在使用 jQuery 的开发中直接广泛使用，但来自 jQuery 动画工具包的 fadeTo 函数更广泛地使用了这种 end 方法，该团队指出。

“这种特定的条件链使得人们不清楚这是一次高度针对性的攻击，或者攻击者是否只是很好地融入并随机影响了下载和使用这些软件包的用户，”该帖子称。

此外，尽管触发恶意软件所需的“狭窄条件集”，但软件包的广泛分布意味着攻击可能具有广泛的影响，影响“许多毫无戒心的开发者”，这体现了“供应链威胁行为者日益增长的复杂性和潜在的广泛影响力”，团队强调。

## 需要提高警惕

事实上，恶意npm和其他代码包发布到流行开发者仓库已成为一个严重的安全问题，像朝鲜的Moonstone Sleet这样的国家资助的威胁行为者以及其他攻击者，正在利用这种策略来在整个软件供应链中注入恶意代码，从而以最小的努力达到广泛的攻击面。

供应链攻击利用代码仓库的数量增加，不仅要求开源社区（负责管理项目）保持更高的警觉，也要求组织在向开发者分发之前，扫描用于开发项目的任何代码。

为了帮助使用jQuery的开发者避免安装恶意软件包，Phylum的研究人员在博客文章中列出了与此次行动相关的所有软件包名称、它们的发布时间以及发布者的用户名。他们还列出了一系列与该活动相关的域名。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/trojanized-jquery-packages-complex-supply-chain-attack)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297789](/post/id/297789)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cyberattacks-data-breaches/trojanized-jquery-packages-complex-supply-chain-attack)

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/trojanized-jquery-packages-complex-supply-chain-attack>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Web安全](/tag/Web%E5%AE%89%E5%85%A8)
* [Javascript](/tag/Javascript)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [热点 | 利用AI造谣幼儿园大火被抓，大模型内容安全谁来守护？](/post/id/308685)

  2025-06-20 16:47:19
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [德克萨斯州警告30万份事故报告通过受影响的用户帐户窃取](/post/id/308363)

  2025-06-11 16:42:18
* ##### [新型 Mirai 僵尸网络通过命令注入漏洞感染 TBK DVR 设备](/post/id/308303)

  2025-06-10 13:35:25
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03

### 热门推荐

文章目录

* [是否进行有针对性的供应链攻击？](#h2-0)
* [需要提高警惕](#h2-1)

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