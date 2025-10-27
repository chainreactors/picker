---
title: 成果分享｜【NDSS 25】复旦大学系统软件与安全实验室在移动生态安全研究取得新进展
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247491245&idx=1&sn=44f864f93993866f8380909cc7f2f83e&chksm=fdeb9ad3ca9c13c5e11fe5e57ae792aa6c64d007b07461782c4ca8af0cbfeed8fa392f78e57e&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2024-11-01
fetch_date: 2025-10-06T19:18:00.620297
---

# 成果分享｜【NDSS 25】复旦大学系统软件与安全实验室在移动生态安全研究取得新进展

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1H3DKkkCJb9A9ucdPQianMRUFwcI4JxxIiagb1wlJclSRVQQgdSBHR5jsg/0?wx_fmt=jpeg)

# 成果分享｜【NDSS 25】复旦大学系统软件与安全实验室在移动生态安全研究取得新进展

原创

复旦白泽战队

复旦白泽战队

复旦大学系统软件与安全实验室在移动生态安全研究取得新进展。本团队曾剖析小程序生态中多种身份混淆安全问题[1]（荣获USENIX Security 2022 Distinguished Paper奖项），而此项研究则延续了对域名身份安全的探讨，从移动互联网生态视角下看，聚焦于世界头部企业们的私有URL链接缩短服务的安全性，揭示了本该倍受用户信赖的服务却在短链接生成管理上存在安全隐患。研究团队构建了自动化的安全测试工具Ditto，发现当下四分之一的服务可能被网络罪犯利用来制作钓鱼链接，甚至是绕过软件系统中的访问控制远程执行恶意代码。论文将这样一种攻击手段称为“错误引导攻击”（如同魔术中的Misdirection），其潜在安全威胁涉及上亿用户。该论文已被网络安全领域CCF-A会议NDSS 2025接收。

[1] Identity confusion in WebView-based mobile app-in-app ecosystems （USENIX Security 2022）

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1HAUpibyicJFdMiaWfQL6IouCMRh1RyiccC5wCIDAIxjv5y0JGzJic9ZAy9icQ/640?wx_fmt=png&from=appmsg)

01

**背景介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1Hib31GYcuDojpVCU1rh6WGsnIkibNr2Mgd7hXE1TD2icNOQAJShGhN5fLw/640?wx_fmt=png&from=appmsg)

短链接生成服务是互联网平台中的一项重要业务功能，它可以更好地帮助内容提供者实施内容分享和用户跟踪。但由于公开的短链接服务经常被用于垃圾邮件和恶意软件的分发，许多著名的企业都更倾向于去开发私有的短链接服务（Dedicated URL Shortening Service，简称DUSS）。DUSS一般都使用跟企业有强关联的域名，这样其生成的短链接就可以继承厂商本身具备的良好声誉；并且DUSS仅为厂商所信任的URL提供链接缩短服务。

从移动营业厅推送广告到大众点评分享美食，DUSS生成的短链接在我们的日常生活中无处不在。世界五百强前10名的企业中，就有8家企业拥有自己的DUSS。

02

**威胁模型**

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1Hib31GYcuDojpVCU1rh6WGsnIkibNr2Mgd7hXE1TD2icNOQAJShGhN5fLw/640?wx_fmt=png&from=appmsg)

私有性质的短链接会让用户隐式地认为，访问这些私有的短链接等同于访问值得信赖的网络内容。然而这种私有短链接服务的安全检查一旦存在缺陷，也可以重定向到一个恶意域名。更严重的是，被滥用的私有短链接服务由于被一些用户和基于域名的安全检查信任，攻击者可以利用这种信任关系在下游软件中加载恶意页面，实现远程代码注入等严重的攻击。本文中将这样一种攻击形式称为**错误引导攻击**（Misdirection Attack）。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1HtAxUyusNh9Q70Q6Lg1BQjAgiaBpdJb63FqA7Rnt9ZZ5DiakR3xX3yRaQ/640?wx_fmt=png&from=appmsg)

本团队首次系统性地对此类攻击展开了深度分析，并发现由于私有短链接服务的缺陷向下游软件引入了多种安全威胁，对用户和多项移动以及web业务场景造成严重危害。本项研究围绕以下研究问题：

**研究问题****1**：DUSS的安全设计是什么？它们的潜在攻击面是什么？

**研究问题2**：如何自动检测现有的众多DUSS是否存在安全缺陷？

**研究问题3**：此类攻击对社交网络用户和Domain-based Checker有什么安全影响？

03

**“初窥”DUSS安全性**

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1Hib31GYcuDojpVCU1rh6WGsnIkibNr2Mgd7hXE1TD2icNOQAJShGhN5fLw/640?wx_fmt=png&from=appmsg)

考虑到DUSS生态缺少公开信息，研究团队首先使用了一种自上而下的方法，从社交网络平台上公开的URL中收集关于DUSS的蛛丝马迹。如下图所示，团队设计了多个维度的二元分类模块，从3大流行社交网络平台的海量URL中识别出由88个独立的DUSS生成的短链接。根据链接域名解析信息，团队进一步推断出DUSS服务的部署模式分为自开发DUSS和第三方托管DUSS两大类。前者的链接生成和解析都是企业自主可控，即会将短链接域名解析到自己的服务器，而后者由知名短链接服务商来提供短链接解析服务，厂商把域名的DNS配置到第三方域名解析服务。

团队取样了排名前15的DUSS调研其安全风险面，发现除一些仅在后端控制台里静态生成短链接之外，许多DUSS都提供短链生成API接口，让客户端应用（例如网页、移动应用）动态生成短链接，暴露出广泛的攻击面。团队基于第三方服务商提供的安全开发文档进行分析和测试，总结了DUSS常采用的三类安全检查，以及每种检查可能存在的攻击向量。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1HwnoNl4V4MLS1u2fKIr4WGSBjAep000usuHrxhzibqOy34CbYL0E81aA/640?wx_fmt=png&from=appmsg)

04

**“测试”DUSS漏洞**

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1Hib31GYcuDojpVCU1rh6WGsnIkibNr2Mgd7hXE1TD2icNOQAJShGhN5fLw/640?wx_fmt=png&from=appmsg)

基于前面的调研，团队发现DUSS链接生成API都会被企业自家开发的移动应用所使用， 因此测试一个DUSS是否安全也得从这些API下手。为了支持自动且规模化的安全分析，团队设计了工具Ditto（整体架构图如下），该工具通过API推断，动态API触发和决策树指导的漏洞挖掘来对DUSS展开安全性测试。

Ditto首先通过静态分析提取Web API的相关调用行为与UI事件可达性，以此推断出可能的DUSS API。其次，Ditto使用一个动态API触发来验证是否是DUSS API，并通过对短链接生成API的长链接的来源进行后向追踪和插桩修改，以此生成合法的API测试请求。第三，Ditto通过一个最小决策树降低无效的测试用例，并保证测试用例无毒无害，用最少的测试次数来挖掘短链接API的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1HAFDUH9EPXHsz22tOica7TqIPoicNgWibFDgtribHuZqLOnK9RwT7hnkqQQ/640?wx_fmt=png&from=appmsg)

最终，Ditto在377个移动应用中识别出50个私有短链接生成API，仅用373个测试用例就找到了**22**个有漏洞的DUSS。

05

**“实证”攻击危害性**

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1Hib31GYcuDojpVCU1rh6WGsnIkibNr2Mgd7hXE1TD2icNOQAJShGhN5fLw/640?wx_fmt=png&from=appmsg)

除了能发起钓鱼攻击，团队还总结了错误引导攻击能攻破的常被下游软件使用的五类安全检查，包括Applink 验证、外链警告、OAuth重定向等。团队实证了这22个漏洞DUSS企业的下游软件安全性，发现有11个安全检查仅能被错误引导攻击攻破，而剩下的21个安全检查则是能受到任何恶意链接的攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW8754fBcnjibkQGIwjGgSEJ1HyYrffU8WwAJRV6ex82NjWgawdzVS857UHG2FhGta0jP1jZw3zBuJQg/640?wx_fmt=png&from=appmsg)

**研究团队介绍**

张智搏（学生一作），系统软件与安全实验室21级硕转博，本科毕业于复旦大学信息安全专业。主要研究方向为移动安全攻防与漏洞挖掘等，并在IEEE S&P、USENIX Security等知名会议上发表过学术论文，曾获USENIX Security 2022杰出论文奖。

张章越（学生二作），系统软件与安全实验室二年级硕士生，本科毕业于复旦大学信息安全专业。研究方向为移动安全，web资源滥用，WebView漏洞挖掘等。

张磊，助理研究员、硕导，研究兴趣涉及系统安全，重点研究开源软件中的漏洞。这包括漏洞发现和分析、利用和自动修复。迄今为止，已带领团队发现了 300 多个具有 CVE ID 的零日漏洞，并获得了包括谷歌、阿里巴巴、蚂蚁金服、华为、Apache、Eclipse、红帽和 VMware 在内的多家知名企业的认可。在A类会议和期刊发表论文十余篇，获得2022年USENIX安全会议杰出论文奖，2024年ACM FSE会议杰出论文奖，ACM China SIGSAC 优秀博士论文奖。另带队获得第二届中国研究生网络安全创新大赛一等奖（并获优秀指导教师）。

个人主页：https://zxlfd.github.io/

洪赓，助理研究员、硕导。研究聚焦于网络犯罪治理、人工智能安全治理等，目前已在IEEE S&P、ACM CCS、NDSS等网络安全国际顶级会议上发表多篇高水平学术论文，并主持国家自然科学基金青年项目等重要研究课题。其研制的反诈骗网站/APP侦查研判系统在执法机关得到广泛装备，发现的网络黑产风险漏洞获得腾讯、蚂蚁金服、京东、新浪等公司致谢。曾获ACM SIGSAC China优博奖、ACM CCS 2018亮点论文奖并指导学生获得全国大学生“挑战杯”课外学术竞赛全国总决赛特等奖等荣誉。

个人主页：https://ghong.site/

素材：张章越、张智搏

排版：孙福特

责编：邬梦莹、林紫涵

审核：张琬琪、洪赓、林楚乔

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、知乎、微博搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过