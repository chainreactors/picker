---
title: FSB 黑客攻破巴基斯坦的 APT 风暴-0156
url: https://www.anquanke.com/post/id/302479
source: 安全客-有思想的安全新媒体
date: 2024-12-06
fetch_date: 2025-10-06T19:33:48.274197
---

# FSB 黑客攻破巴基斯坦的 APT 风暴-0156

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

# FSB 黑客攻破巴基斯坦的 APT 风暴-0156

阅读量**77973**

发布时间 : 2024-12-05 15:31:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：darkreading

原文地址：<https://www.darkreading.com/threat-intelligence/russian-fsb-hackers-breach-pakistan-storm-0156>

译文仅供参考，具体内容表达以及含义原文为准。

![The title screen for 1988's "Spy vs. Spy" arcade game]()

代表俄罗斯国家情报机构行事的黑客已经攻破了在巴基斯坦活动的黑客的网络，利用他们的间谍活动从阿富汗和印度的政府、军事和国防目标窃取信息。

2022 年 12 月，网络安全和基础设施安全局（CISA）将 Secret Blizzard（又名 Turla）与俄罗斯联邦安全局（FSB）联系在一起，它进入了另一个高级持续性威胁（APT）Storm-0156（又名 Transparent Tribe、SideCopy、APT36）运行的服务器。它很快扩展到 33 个由 Storm-0156 运营的独立指挥控制 (C2) 节点，并于 2023 年 4 月入侵了其黑客同伴拥有的个人工作站。

微软和黑莲实验室的研究人员说，从那时起，Secret Blizzard 就能从 Storm-0156 的网络攻击中窃取敏感信息，这些信息来自阿富汗政府机构和印度军事及国防目标。

**间谍与间谍**

具有讽刺意味的是，威胁行动者–甚至那些为民族国家工作的威胁行动者–可能很容易成为其他威胁行动者的猎物。正如 Black Lotus 实验室研究员 Ryan English 所解释的那样，他们通常不会努力保护自己的基础设施。“如果你花大量时间将自己的网络打造成堡垒，那么你花在进攻上的时间就会减少。说到底，这是一个时间和成本问题，”他说。

即使网络攻击者想提高网络安全性，他们也会面临独特的挑战。最近，一个威胁行为者尝试使用 Palo Alto 的 Cortex 扩展检测和响应 (XDR) 进行实验，就证明了这一点。通过安装 Cortex，他们无意中为 Palo Alto 研究人员提供了一个了解其操作的窗口。

目前还不清楚 Secret Blizzard 是如何获得进入第一台 Storm-0156 服务器的初始权限的，但 “我们认为他们是从公开报告中识别出 [Storm-0156] C2 节点的。因此，他们的进攻团队几乎是像威胁研究员那样工作的–花时间查看公开报告，寻找进入别人的东西的可能性，”English 说。

不过，他补充说：“他们并不满足于公开的信息。他们可能进行了一些侦察。我们认为，他们使用了一些远程桌面透视技术，以进入目标的其他（基础设施）。这可不是一件容易的事。”

**暴雪从 Storm-0156 窃取的秘密**

由于掌握了 C2 节点和工作站，Secret Blizzard 对 Storm-0156 的工具、战术、技术和程序（TTPs）以及已经从受害者那里窃取的数据拥有广泛的可见性和控制权。它利用所有这一切，取得了强大的创造性效果。

在某些情况下，俄罗斯人利用 Storm-0156 的服务器向现有受害者的系统植入后门。这样，他们就可以从阿富汗外交部、情报总局（GDI）和外国领事馆等多个政府机构窃取敏感信息。

不过，针对印度的目标，Secret Blizzard 采取了不同的策略。只有一次，它针对印度国内的实体部署了后门 “TwoDash”。相反，它针对 Storm-0156 本身部署了后门，窃取了巴基斯坦人已经从印度军事和国防目标窃取的敏感记录。微软推测，“秘密暴雪在阿富汗和印度采取的方法不同，可能反映了俄罗斯领导层的政治考虑、联邦安全局内部不同的地理责任区，或者是微软威胁情报部门的收集漏洞”。

**通过隐蔽实现前所未有的安全**

威胁行动者经常合作，但研究人员还没有发现任何其他组织像 Secret Blizzard 这样，为了共享目标访问权限而互相黑客攻击。

这也不是 Secret Blizzard 第一次这样做。首先在 2017 年，该组织访问了属于伊朗 APT 34（又名 Hazel Sandstorm、OilRig、Crambus）的工具和基础设施。在即将发布的一篇博文中，微软将披露秘密暴雪在乌克兰开展的另一次活动的细节，在此期间，它使用了属于其他两个威胁行为体的机器人和后门。

还有去年爆出的案件。今年 1 月，Mandiant 报告了与 Secret Blizzard 有关的活动。今年 4 月，卡巴斯基声称该活动是由总部位于哈萨克斯坦的 APT Tomiris（又名 Storm-0473）实施的。现在看来，Mandiant 的猜测是正确的：Secret Blizzard 是幕后黑手，但通过使用 Tomiris 的后门迷惑了研究人员。根据这一最新进展，Dark Reading 已经联系了卡巴斯基。

托米里斯的烟幕弹说明了秘密暴雪的方法的好处。当然，只入侵一个 APT，它就能访问属于该 APT 所有受害者的基础设施和敏感数据。但除了效率之外，它还可以利用这种访问权限来掩盖自己的活动，将其伪装成来自另一个威胁行为者。

English 回忆说，上个月，“我参加了 CyberWarCon，当时有几个人在聊天，他们说：’你知道吗，我们最近没有听到 Turla 的消息。’然后我就开始大笑。”

本文翻译自darkreading [原文链接](https://www.darkreading.com/threat-intelligence/russian-fsb-hackers-breach-pakistan-storm-0156)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302479](/post/id/302479)

安全KER - 有思想的安全新媒体

本文转载自: [darkreading](https://www.darkreading.com/threat-intelligence/russian-fsb-hackers-breach-pakistan-storm-0156)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/russian-fsb-hackers-breach-pakistan-storm-0156>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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