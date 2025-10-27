---
title: SideWinder 发动新一轮攻击，地理覆盖范围扩大，涉及亚洲、中东、非洲及欧洲众多国家的实体和战略基础设施目标
url: https://www.anquanke.com/post/id/301006
source: 安全客-有思想的安全新媒体
date: 2024-10-18
fetch_date: 2025-10-06T18:49:56.012213
---

# SideWinder 发动新一轮攻击，地理覆盖范围扩大，涉及亚洲、中东、非洲及欧洲众多国家的实体和战略基础设施目标

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

# SideWinder 发动新一轮攻击，地理覆盖范围扩大，涉及亚洲、中东、非洲及欧洲众多国家的实体和战略基础设施目标

阅读量**99198**

发布时间 : 2024-10-17 11:28:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：darkreading

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/sidewinder-wide-geographic-net-attack-spree>

译文仅供参考，具体内容表达以及含义原文为准。

![Coiled snake camoflaged on a piece of wood]()

总部位于印度、难以捉摸的高级持续威胁（APT）组织 SideWinder 针对亚洲、中东、非洲甚至欧洲众多国家的知名实体和战略基础设施目标发动了新一轮攻击，这标志着该组织的地理覆盖范围正在扩大。研究人员发现，这些攻击还表明该组织正在使用一种被称为 “偷窃者机器人”（SteellerBot）的高级后剥削工具包来进一步开展网络间谍活动。

这个由国家支持的组织自2012年开始活跃，2018年公开露面，主要以攻击巴基斯坦、阿富汗、中国和尼泊尔的竞争对手而闻名，在过去六个月里，它的地理范围有所扩大。卡巴斯基的研究人员在 SecureList 博客上的一篇文章中观察到并概述了最新的攻击，首次揭示了 SideWinder 的一些破坏后活动，尽管研究人员进行了多年的研究，但这些活动在很大程度上仍不为人所知。

具体而言，SideWinder 最近的攻击目标包括孟加拉国、吉布提、约旦、马来西亚、马尔代夫、缅甸、尼泊尔、巴基斯坦、沙特阿拉伯、斯里兰卡、土耳其和阿拉伯联合酋长国的实体。受影响的部门多种多样，包括政府和军事实体、物流、基础设施和电信公司、金融机构、大学和石油贸易公司。攻击者还瞄准了阿富汗、法国、中国、印度、印度尼西亚和摩洛哥的外交实体。

至于 StealerBot，研究人员将其描述为 “专为间谍活动设计的高级模块化植入程序”，他们认为该恶意软件是 SideWinder 使用的主要后剥削工具。

**SideWinder 的典型网络攻击链**

虽然地理位置和事后利用策略各不相同，但 SideWinder 在最近的一连串攻击中使用了典型的攻击链。该组织首先发送带有附件的鱼叉式网络钓鱼电子邮件，附件通常是微软 OOXML 文档（即 .docx 或 .xlsx 文件）或 .zip 压缩包，其中又包含一个恶意 .lnk 文件。该文件会触发一个包含各种 JavaScript 和 .NET 下载程序的多级感染链，最终安装 StealerBot 间谍工具以开展进一步活动。

卡巴斯基首席安全研究员詹保罗-德多拉（Giampaolo Dedola）和瓦西里-别尔德尼科夫（Vasily Berdnikov）在文章中写道：“鱼叉式网络钓鱼活动中使用的文件通常包含从公共网站上获取的信息，”这些信息被用来诱使受害者打开文件，并相信它是合法的。在这种情况下，一些电子邮件的诱饵包括公共照片、图像、外交和其他活动的参考资料，而这些可能是预定目标感兴趣的。

攻击中的所有文件都使用了远程模板注入技术，下载存储在攻击者控制的远程服务器上的 .rtf 文件。研究人员说，这些文件是专门为利用CVE-2017-11882而制作的，CVE-2017-11882是微软Office软件中一个已有7年历史的内存损坏漏洞，它可以下载更多的shellcode和恶意软件，而这些shellcode和恶意软件会使用各种技巧来避开沙箱并使分析复杂化。该恶意软件的最终目的是从受感染系统中获取数据并进行网络间谍活动。

**新型偷窃机器人模块化恶意软件**

由攻击者命名的 StealerBot 是一款利用 .NET 开发的模块化植入程序，用于执行间谍活动。研究人员观察到的攻击链不是像通常那样在受感染机器的文件系统中加载恶意软件的组件，而是通过恶意软件的众多模块之一将其加载到内存中，在这种情况下，该模块充当后门加载器，攻击者将其称为 “ModuleInstaller”。

该模块是一个下载器，用于部署 SideWinder 用来在被攻击机器上维持立足点的木马。研究人员指出，这是一个该组织以前使用过的工具，卡巴斯基也观察到了它，但直到现在才公开亮相。

攻击者设计的ModuleInstaller至少会丢弃四个文件：一个合法且已签名的应用程序，用于侧载恶意库；一个作为资源嵌入程序的.config清单，下一阶段需要它来正确加载其他模块；一个恶意库；以及一个加密的有效载荷。“研究人员指出：”我们观察到了投放文件的各种组合。

另一个模块名为 “Orchestrator”，是恶意软件的主要组件，它与 SideWinder 命令与控制（C2）通信，并执行和管理其他恶意软件插件。总而言之，StealerBot 包含多种模块，用于安装其他恶意软件、捕获屏幕截图、记录击键、从浏览器中窃取密码、窃取文件、网络钓鱼 Windows 凭据，以及通过绕过用户账户控制（UAC）提升权限等活动。

**被严重低估的攻击者**

卡巴斯基称，SideWinder 长期以来一直被认为是一个低技能的威胁组织，因为它使用公共漏洞和远程访问木马（RAT）以及恶意 .lnk 文件和脚本作为感染载体。研究人员写道：“只有当你仔细研究他们的行动细节时，他们的真正能力才会显现出来。”

他们说，由于新一轮攻击显示 “该组织的活动范围显著扩大”，那些可能成为攻击目标的人应该提高警惕，意识到该组织带来的威胁。

为了帮助防御者识别其网络中是否存在 SideWinder 及其工具 StealerBot，研究人员在帖子中列出了一份全面的入侵指标（IoCs）列表，涉及攻击的各个阶段。

这些 IoC 包括对恶意文档、.rtf 和 .lnk 文件的引用，以及指向 StealerBot 各个模块的特定 IoC。帖子中还列出了一长串与攻击相关的恶意域和 IP。

本文翻译自darkreading [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/sidewinder-wide-geographic-net-attack-spree)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301006](/post/id/301006)

安全KER - 有思想的安全新媒体

本文转载自: [darkreading](https://www.darkreading.com/cyberattacks-data-breaches/sidewinder-wide-geographic-net-attack-spree)

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/sidewinder-wide-geographic-net-attack-spree>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

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