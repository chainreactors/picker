---
title: 2023 Pwn2Own 温哥华大赛公布目标和奖金
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515297&idx=1&sn=33f273731b9c3642e6bd57eadb2fa55c&chksm=ea948dcbdde304dd5bdce8ceb813d29a9a4882b4bd207bc2ee833661aaa1e3b8579b1175e134&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-14
fetch_date: 2025-10-04T03:53:25.881428
---

# 2023 Pwn2Own 温哥华大赛公布目标和奖金

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRsopR0py9qMwUUEVviawsjf9wtpw4jl89YDdqwtONNC8XCUiamiaNepxTXNtFGSlMTIiaibjnPUKx2lBQ/0?wx_fmt=jpeg)

# 2023 Pwn2Own 温哥华大赛公布目标和奖金

ZDI

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfRslITzFHvzvVSmaPAQ7kEozCzmmy06V2N0k7OeI2jJWib0Ze8yIvEZw/640?wx_fmt=gif)

**ZDI 发布博客文章指出，2023年Pwn2Own温哥华大赛将在当地时间3月22日至24日举行。本次比赛仍然是混合模式，参赛选手可选择远程或现场参赛。特斯拉回归成为大赛合作伙伴。这次大赛共分7个类别，增加了Steam 虚拟机逃逸类别，即电动车的蒸汽引擎类别，以及其它新类别。另外，特斯拉Model 3和Model S也将成为目标，最高奖励是60万美元美金另加汽车本身。VMware 也将再次成为大赛赞助商。大赛奖金池将超过100万美元，其中包括特斯拉汽车。大赛类别包括：虚拟机、web浏览器、企业应用、服务器、本地提权、企业通信以及汽车。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfdKCOsT8D37RhicbNy00WxMxiaND5tJoZJ8fadYddCD4tEbswuibUflaFg/640?wx_fmt=gif)

**虚拟机类**

赞助商VMware 这次提供的目标是VMware ESXi 和 VMware Workstation，奖金分别为15万美元和8万美元。微软也回归，将为成功的Hyper-V客户端guest-to-host提权提供25万美元的奖励，是虚拟机类的最高奖金额。OracleBox 本次提供4万美元的奖励。

该类别还提供额外奖金。如果参赛选手能够逃逸guest OS，之后通过一个Windows 内核漏洞（不包括VMware ESXi）在主机OS上实现提权，则可获得额外的5万美元和5个破解冠军积分点，从而将Hyper-V的最高奖励拉升到30万美元。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjf68qp0hY5yDxiaJozoGMEOEMpdTk5YfEhsJW3wib6prcaibhpPEaaLMVgA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfdKCOsT8D37RhicbNy00WxMxiaND5tJoZJ8fadYddCD4tEbswuibUflaFg/640?wx_fmt=gif)

**Web 浏览器类**

虽然浏览器是“传统的”Pwn2Own目标，但仍在继续做出微调，从而保证它们的相关性。去年大赛重新引入仅渲染类exploit，今年的奖金额度增加到6万美元。不过，如果选手拥有Windows内核提权或沙箱逃逸漏洞，则可分别获得10万美元或15万美元的奖励。如果exploit同时适用于Chrome和Edge，则可获得2.5万美元的额外奖励。基于Windows的目标将在VMware Workstation 虚拟机上运行。因此，所有浏览器（除Safari外）均可获得VMware逃逸额外奖励。如选手能够以这种方式攻陷浏览器，同时可通过逃逸VMware Workstation虚拟机的方式在主机操作系统上执行代码，则可额外获得8万美元奖励和8个积分点。Apple Safari和Mozilla Firefox仍需要完整的exploit。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjfHqQmHk79ObxN7LQsHGd6MmnnRhmDuUjhbGGlthHI3ChrUFVDj5HUibA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfdKCOsT8D37RhicbNy00WxMxiaND5tJoZJ8fadYddCD4tEbswuibUflaFg/640?wx_fmt=gif)

**企业应用类**

企业应用类包括Adobe Reader和多个Office组件，本次大赛允许应用在M系列的MacBook上运行。如选手能够实现沙箱逃逸的exploit或内核提权的Reader exploit，则分别可获得5万美元和10万美元的奖励。Word、Excel和PowerPoint 也是有效目标。基于微软Office的目标会在适用的情况下启用受保护视图。Adobe Reader将在适用情况下启用受保护模式。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjfG0eFzTfCBNbTiatYxaLUwoZMNq2drVqSgclTpzEodxvZomTIYKiaicRicg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfdKCOsT8D37RhicbNy00WxMxiaND5tJoZJ8fadYddCD4tEbswuibUflaFg/640?wx_fmt=gif)

**服务器类**

本次大赛在服务器类中增加了ISC BIND和微软DNS Server。如能够在这两个目标上实现成功利用，则可分别获得20万或15万美元的奖励。去年曾将Samba增加到该类别但并没有选手选择。微软Windows RDP/RDS提供的奖励最多为20万美元。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjficXYnnnsG8VFXnnnictukk7GmZef6Eoh9sZbGb2KtO2zcn4K2bIEgSibA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfdKCOsT8D37RhicbNy00WxMxiaND5tJoZJ8fadYddCD4tEbswuibUflaFg/640?wx_fmt=gif)

**本地提权类**

该类是Pwn2Own大赛的经典类别，主要关注来自一般用户并可导致以高权限用户身份执行代码的攻击。选手必须利用一个内核漏洞提升权限。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjfEmwiatZCd4e1u2Vwr7Q3pibU9dVv6qTshNf3iaAhibiceoqFpFYvsclFeyQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfdKCOsT8D37RhicbNy00WxMxiaND5tJoZJ8fadYddCD4tEbswuibUflaFg/640?wx_fmt=gif)

**企业通信类**

ZDI在2021年引入该类，反映这些工具在我们现代远程工作中的重要性。去年的大赛中包括对微软Teams的零点击利用。成功利用必须通过和选手通信来攻陷目标应用。一些案例通信请求可以是音频通话、视频会议或信息。Zoom 和微软Teams提供了7.5万美元的奖励。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjfqlkGYXBdH8pLyDibWPnYia0MS5m2bQBiaCpXzU6WuQoH5lK2lLdicW6wtA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRsopR0py9qMwUUEVviawsjfdKCOsT8D37RhicbNy00WxMxiaND5tJoZJ8fadYddCD4tEbswuibUflaFg/640?wx_fmt=gif)

**汽车类**

Pwn2Own 大赛在2019年引入汽车类别，并奖励了一辆特斯拉Model 3。今年对成功利用的复杂性要求提高。特斯拉配备了多个安全层，今年提供了不同级别的奖励，在某些情况下还提供了额外奖励。选手可对特斯拉Model 3（Intel 或基于Ryzen）或者特斯拉Model S（基于Ryzen）。第一级别获得最多奖励并且代表完整的汽车攻陷，因此奖励金最高。选手必须在汽车的多个系统中跳转，即需要复杂的利用链才能在汽车的三个不同的子系统上执行任意代码。

除了汽车本身和50万奖励外，选手还可获得额外奖励，获得60万的总奖励。这是Pwn2Own 历史上的单个最高奖励目标。如果有人达成这一目标，则意味着获得60个积分点，从而获得几乎不可超越的地位。多个不同级别包括不同的外奖励类型和奖励金。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjfbZt4nsEzx2j6n1hIFkLu4ykiahdPYlquBhl0icJMoIrpFZej7QJ0tRkw/640?wx_fmt=png)

ZDI指出，虽然完成演示的复杂性难以表述，但还是希望有人能够炫技并开走汽车。

该类的第二个奖励级别虽然不像第一个级别那样复杂，但仍然需要攻击者在其中某些汽车的子系统跳转。该级别要求选手在两个不同的子系统上执行任意代码。如果选手包括可选目标，则第二级别的奖励是40万美元。第二个级别的选手仍然有机会开走特斯拉。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjfHWxosGbiaF8QIC4nwoSrLJGyChcQU9q7S0zyibmDOniansjqiaUcNnQ5RQ/640?wx_fmt=png)

第三级别的目标利用也同样困难，但只需攻陷一个子系统就可获胜，但这仍然并非易事。不过并非第三级别中的所有实例就能开走汽车。本次大赛还引入了Steam虚拟机逃逸类作为攻击向量。其中一些目标也增加了额外奖励，不过要开走特斯拉，则需要个拿下标记有“包括汽车”的选择。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRsopR0py9qMwUUEVviawsjfN51W4fBOHX2yrHNtzicTAfYPye6UTqxtQe26bNzMBR3oe38SVD8W9ZQ/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Pwn2Own 2023迈阿密春季黑客大赛公布目标和奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514911&idx=1&sn=edfb9902c59192447f4321dcba4b8d8d&chksm=ea948a75dde30363473d0e6eb0d684bc020aeaedc29885efc225876e18dd85ea482860ebc6b8&scene=21#wechat_redirect)

[Pwn2Own 2022多伦多大赛Master of Pwn 诞生](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514975&idx=1&sn=092fe6b1273fbcc30a4f95941bbb65cf&chksm=ea948a35dde30323ac771eceed8d6b0cf4f156d112d38a5021da7664d261d78ae4626ec760a7&scene=21#wechat_redirect)

[Pwn2Own 2022多伦多大赛确定目标和奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513770&idx=1&sn=5add0c86a1dc441c5bc3cced0fc8dff5&chksm=ea9487c0dde30ed6b5ac62548162b39108da3ebfc869c793d8bed447fd2dae4b566efc58e74f&scene=21#wechat_redirect)

[Pwn2Own 2022迈阿密大赛落幕  去年春季赛冠军蝉联Master of Pwn](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511504&idx=1&sn=8b4fc83a50611faeb66599c8ede17787&chksm=ea949cbadde315ac262fa80134e5021adec56b55766b3f478081e48a1fbaa319f2d4431dcdb7&scene=21#wechat_redirect)

**原文链接**

https://www.zerodayinitiative.com/blog/2023/1/11/announcing-pwn2own-vancouver-for-2023

题图：Pexels License‍

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