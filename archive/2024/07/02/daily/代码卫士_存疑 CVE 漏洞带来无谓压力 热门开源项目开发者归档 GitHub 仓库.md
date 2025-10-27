---
title: 存疑 CVE 漏洞带来无谓压力 热门开源项目开发者归档 GitHub 仓库
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519930&idx=2&sn=acd4b1226ac3021b5aa91433e3f657f5&chksm=ea94bfd0dde336c6a6ba483f21d5d9572e139fb0e5cd5ac1a9ccde95f91e2330823dfbc71c20&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-02
fetch_date: 2025-10-06T17:46:07.276236
---

# 存疑 CVE 漏洞带来无谓压力 热门开源项目开发者归档 GitHub 仓库

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIzP0ewgKhjz7XtR74eFOTmCj3dbExBJDLXR0JNiaqK1PXBhW42OeJ8rg/0?wx_fmt=jpeg)

# 存疑 CVE 漏洞带来无谓压力 热门开源项目开发者归档 GitHub 仓库

Ax Sharma

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIgicmyV2uPHgCahcKFAjGX3XpEZ1sLSJnP7smNHv9wukia0xczgE9EXwA/640?wx_fmt=gif&from=appmsg)

**热门开源项目 “ip”最近归档 GitHub 仓库，换句话说，其开发人员将其设为“只读”。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIOwbFttNmrCoQ69NYia8OnAuJEibDE29pLTicX6GaPictHkvnUMfFkEvUmw/640?wx_fmt=gif&from=appmsg)

该项目的开发者 Fedor Indutny 因针对该项目的一个CVE漏洞，在互联网引发热议。遗憾的是，Indutny的案例并非孤例。近来，开源开发人员收到的未经确认的针对他们项目的可探讨的，或者在某些情况下完全是恶意的CVE报告数量在增多。这种报告可引发项目用户不必要的恐慌，引发安全扫描器生成不必要的告警，而这些最终成为令开发人员头疼的问题。

**GitHub 仓库“node-ip”归档**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIibAE3uRanMMwbOsLlDvP4rRxCmAia5B9hltYZD8fpTkD410VHS9RlcRQ/640?wx_fmt=gif&from=appmsg)

本月早些时候，“node-ip”项目的作者Fedor Indutny归档了该项目的 GitHub 仓库，实际使其变为“只读”，并限制了人们设立issue（讨论）、拉取请求或提交commit的能力。

“node-ip” 项目位于npmjs.com 注册表上，因为 “ip” 程序包的周下载量达到1700万次，使其成为 JavaScript 开发人员使用的最为热门的IP地址解析工具。

上周二即6月25日，Indutny在社交媒体解释了自己归档 “node-ip” 的原因。他指出，“过去几个月来有一件事一直困扰着我，这也是我在 GitHub 归档 node-ip 仓库的原因。”归档与今年年初该项目中披露的漏洞CVE-2023-42282有关。他在帖子中提到，“有人给我的npm包提了一个可疑的CVE，然后我开始从收到 ‘npm audit’ 告警的人们那里收到消息。”在应用程序中使用其它开源项目如 npm 包和依赖的Node.js 开发人员可以运行 “npm audit” 命令查看应用所用的项目中是否存在相关漏洞。

该漏洞与该工具未正确地识别以标准格式如十六进制提供的私有IP地址有关。它将导致 “node-ip” 工具将私有IP地址如 “0x7f.1…”（代表 127.1）识别为公开地址。如果有应用程序仅依赖于 node-ip 来查看所提供的IP地址是否是公开的，则非标准的输入将导致受影响的 node-ip 工具返回不一致的结果。

**“可疑的”安全影响**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIibAE3uRanMMwbOsLlDvP4rRxCmAia5B9hltYZD8fpTkD410VHS9RlcRQ/640?wx_fmt=gif&from=appmsg)

公开来源表明，CVE-2023-42282最初的CVSS评分为9.8，为“严重”级别。尽管 Indutny 确实在后续版本中修复了该漏洞，但他对该漏洞是**真正的**漏洞且严重性提升存疑。

他此前要求GitHub 撤销该CVE漏洞，表示，“我认为该漏洞的安全影响有待商榷。虽然我无意将该模块用于任何安全相关的检查，我非常好奇不可信的输入如何可被传递到 ip.isPrivate 或 ip.isPublic函数，之后被用于验证网络连接来自何处。”

质疑CVE并非简单的任务，正如GitHub 安全团队的一名成员解释道。它要求项目维护人员追踪最初发布CVE漏洞的CVE编号发布机构 (CNA)。CAN 一般由NIST的NVD和MITRE担任。而在过去几年来，技术公司和安全厂商也加入其中，也可颁发CVE编号。这些CVE编号、漏洞描述以及所报严重性评级之后被安全数据库如 GitHub 安全公告同步和重新发布。

Indutny 在社交媒体发文后，GitHub 调低了该漏洞在其数据库中的严重性并建议Indutny 启用非公开漏洞报送选项，更好地管理收到的报告，去除噪音。截至目前，该漏洞在NVD上的严重性评级是“严重”。

**不断增多的麻烦**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIibAE3uRanMMwbOsLlDvP4rRxCmAia5B9hltYZD8fpTkD410VHS9RlcRQ/640?wx_fmt=gif&from=appmsg)

CVE体系最初旨在帮助安全研究员以道德的方式报送项目中的漏洞，负责任地报送后将它们进行分类。最近该系统吸引社区成员报送未经验证的报告。

虽然其中很多CVE是由负责任的研究人员善意报送且代表的是可信的安全漏洞，但最近一些安全爱好者新手和漏洞猎人很明显是“收集”CVE漏洞来丰富自己的简历，而非报送能够构成真实的利用风险的安全漏洞。

于是，开发人员和项目维护人员已开始反击。

2023年9月，著名软件项目 “curl” 的创建人Daniel Stenberg 指责对该项目中拒绝服务漏洞的“恶意 curl 问题CVE-2020-19909”报送。从NVD的历史记录来看，该漏洞的评分为9.8或为“严重”级别，但随着后续对它造成的实际安全影响进行讨论后，掉到了“低危”级别的评分3.3。Stenberg 批评称，“这并非个例，也并非首次发生，这种事情已存在了多年。我并不喜欢围绕漏洞的哲学思考。它们干扰了真正的问题，我认为没有任何意义。用很多编译器很容易测试出该漏洞如何在很多平台上发挥作用。在任何平台上它都并不是一个安全问题。” Stenberg提到，这个“无聊的漏洞”说明它可导致异常行为，而并非可被滥用的安全缺陷。

另外一个npm项目 micromatch 的周下载量达到6400万次，被报送了多个高危的ReDoS 漏洞，其创建人被社区人员追着询问。其创建人 Jon chlinkert 提到CVE-2024-4067时提到，“你能给出至少一个执行了 micromatch 的库或分支易受该漏洞影响，以便我们查看它是真实存在而非理论上的漏洞吗？”他显然并未收到令人满意的 PoC 利用，他回应报送者称，“我总是遇到除了你对自己实施外甚至不能算作漏洞的情况。如底层库中的正则无法被浏览器访问，除非你允许用户以 web 表单的格式提交只是由你自己的应用程序使用的正则表达式。我要求列举真实库如何遇到这些‘漏洞’，而你从未提供。”而最近本文作者从第三方处获悉该项目存在潜在“风险”，这似乎是当下应该做的负责任的事情。然而，遗憾的是，它并非可利用的漏洞，而只是一份令人讨厌的报告（很类似于 CVE-2024-4067），而它导致开发人员被追着问。

为未经验证的漏洞报告颁发CVE编号，不仅为项目维护人员带来麻烦，还导致项目、创建人及更广泛的客户群体遭DoS攻击。开发者安全解决方案（如 npm audit）旨在阻止易受攻击组件触及应用程序，在检测到已知漏洞时可能会触发告警，而设置有可能导致build被破坏。

有人在2023年评论恶意curl CVE漏洞时指出，“Jackson 在几个月前就面临这种问题，有人报送了一个严重的CVE漏洞并破坏了全球所有的build。”而该问题并非项目的安全问题，而是Java递归性数据结构的内在本质。

**平衡点在哪？**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIibAE3uRanMMwbOsLlDvP4rRxCmAia5B9hltYZD8fpTkD410VHS9RlcRQ/640?wx_fmt=gif&from=appmsg)

这类反复发生的事件引发一个问题：如何平衡？

不断报送理论意义上的漏洞可导致开源开发人员（很多是志愿者）因区分噪音而筋疲力尽。

另一方面，如果包括新手在内的安全践行者们对安全漏洞坐视不管，以便不会对项目维护人员带来不便，这种行为是道德的吗？

第三个问题与不存在活跃维护人员的项目有关。被遗弃的软件项目多年未得到更新但其中包含很多漏洞，即使被披露也不会得到修复，也不存在原始维护人员的联系方式。在这种情况下CAN和漏洞奖励平台等中介就无从应对。

收到研究人员的漏洞报告时，这些组织机构可能无法总是能够充分审计每个独立报送的报告。无法与现已缺席的项目维护人员进行联系，他们可能会在“负责任披露”窗口期失去后分配CVE编号并发布。

这些问题还不存在简单的答案。

只有在安全研究人员、开发人员和厂商社区协力找到有效的解决方案时，开发人员才不会让恶意报告拖得筋疲力尽，而CVE系统才不会充斥着在纸面上看似可靠但实际却存疑的夸张“漏洞”。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA：多数重要的开源项目未使用内存安全代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519901&idx=1&sn=32d7347010a5e163854477e5c2232e19&chksm=ea94bff7dde336e13576de0daf2daadc290e35b0e3b4c7d7b385038100a61ef8c962de61267a&scene=21#wechat_redirect)

[开源的Judge0 中存在多个沙箱逃逸漏洞，可导致系统遭完全接管](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519400&idx=2&sn=e79b7a5da52b70449d7f2d6c99c8cab2&chksm=ea94bdc2dde334d48c4fc1fc698133c71550c937353091502e020643ff271de8656b39d98e84&scene=21#wechat_redirect)

[OWASP 发布十大开源软件风险清单（详解版）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519303&idx=1&sn=df6dc31715e4c8d70ad22fe31af7eb03&chksm=ea94bd2ddde3343b6e37f517febd2d68bba0fe206dde6bab42bf696389f1ca4723bbdf8ccf78&scene=21#wechat_redirect)

[开源AI框架 Ray 的0day已用于攻陷服务器和劫持资源](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519162&idx=1&sn=3872fcc82018e2c561d9e4e7574f0c8e&chksm=ea94bad0dde333c6d504e2c7680caabb4badc973dd03223bab93d5b62e5469c4db22d966adf9&scene=21#wechat_redirect)

[CISA：注意 Chrome 和 Excel 解析库中已遭利用的开源漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518582&idx=2&sn=3e7fcf93d7c3d8fa193fcb72ed6c2347&chksm=ea94b81cdde3310af6e572040db0f7c2aba6bf5314cdb417d0ad4e7fffa194153e99860228a1&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/dev-rejects-cve-severity-makes-his-github-repo-read-only/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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