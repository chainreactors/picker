---
title: ARTEX 韩语版，是钓鱼还是真实？
url: https://mp.weixin.qq.com/s/O02K5qIPRtrIo3oTQFd_GQ
source: Doonsec's feed
date: 2026-10-08
fetch_date: 2026-10-09T08:10:04.588424
---

# ARTEX 韩语版，是钓鱼还是真实？

# ARTEX 韩语版，是钓鱼还是真实？

zhoufish
zhoufish

ZhouFi网安分享

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

*NEWS TODAY*

**AI自主渗透测试框架 ARTEX 韩语版发布**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kh3EZZgjLW4Hm8Wd6sNdbH3yLlibnMShUQoq0icZevZibwsPxM7U0AUo3WiauZdUq9icAqFyicOib2icSSNXgNick1ukkbl7rOUmzh6l4Wc/640?wx_fmt=png&from=appmsg)

能自主完成从侦察到入侵的全流程

近期，一个名为 artex-ko 的开源项目在 GitHub 上引发了安全圈的关注。它是知名自主渗透测试框架 ARTEX 的韩语本地化版本，由开发者 jiwoochris 维护。

这个项目之所以值得关注，不仅因为它代表了 AI 在网络安全领域的前沿应用，更因为其原版框架近期被曝出与一起针对韩国金融机构的真实攻击事件有关。

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kiagZZCicGB5zcicbrLAibaYueEQzYetrglFzQFwZRMZq2r7BW6d6fbJicMxGibw8eZMEEbnsKhblHiaKU7tHl8vGCGIXKgfBC9ficNVOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kgYXCsTbM7j14HJ0niaa43NVbKbK37CJoZhBVjsKnvJaia5brfOHepYCMBsvsUuTClPcdnPiaQBFWbfQfZJ9OxEhgm182eWuOULmo/640?wx_fmt=png&from=appmsg)

*NEWS TODAY*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5khD5dia4h4iccLl7acL8Kjd6CKgTlFdebLjceibG1xnmYGRU3j3N8AdpcWc4ckP2jbib3j54sExtne6y1E0U1xiaJan7dSp6v0m3f3M/640?wx_fmt=png&from=appmsg)

**仓库项目**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kiaCibhdfU8AxMAfibvMNicNFHFcgS6ZVnicdE23lQSxwic2pTHBMYCnyetcuTiaPLl1x5UIzLD1buQrKljiamCNOBJAvJHKFPAreGbM4I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5khGKXH6dHO26GzTXojw3t9iaOxyrdeKibQgO2OBapp8TRwP0IBE4rEcmvxC0CFLLsYRIyuYgkq3tunZAvpwFnmHibAibKnbicgGDic68/640?wx_fmt=png&from=appmsg)

*NEWS TODAY*

**它到底能做什么？**

简单来说，ARTEX 是一个由大语言模型驱动的多智能体自主渗透测试系统。你给它一个目标，它就能像人类渗透测试员一样，自主完成从信息侦察、漏洞发现到权限获取的完整攻击链。

它的核心能力包括：

多智能体协作

系统内部划分为 planner（规划者）、worker（执行者）和 mainagent（人机交互）等角色。planner 负责判断当前进展并生成新的测试意图，worker 则领取具体任务去实际执行。

双图结构设计

这是 ARTEX 架构上最精妙的地方。它把数据分成了两张相互关联的图：

资产图（共享）：记录"目标是什么"，包括域名、子域名、IP、服务、端点等

探索图（任务独立）：记录"测到哪里了"，包括目标、意图、事实、发现的漏洞等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kjs6clHEN45908mgjicoib6ib3xHntNvJZmibE721ibfoMHvHxhG2ZoqZ7f5vwPrh9L4tKw8j2osRy8kmEY3omtHj5P7j9dmz9mwdq8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kjiaG0dJeZsClmJVdpNF9Mj3o0jFibHvVicMrqMWFqVwE1MXxkmj3nUVzPjCed7HfruoP9G6kJNF2GuweFeLrzDAqIo6p07dOfO7o/640?wx_fmt=png&from=appmsg)

两张图通过锚点连接，可以清楚地知道某个漏洞是在测试哪个资产时发现的。

技术栈

Go 语言后端 + Next.js 前端，整个前端被嵌入到一个单一二进制文件中，部署非常方便。数据存储在 PostgreSQL 中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kgOL6WyYZKmHicS7vP2Ty8KzTYO9N0It9HbA3pvkP3wo7LHdPYicyF60yd9XLVnLSVpfIdUggTnHZicF5xicX8uz4uRT66VRLtpacg/640?wx_fmt=png&from=appmsg)

*NEWS TODAY*

**韩语版做了什么？**

artex-ko 不是简单的翻译。为了保持 AI 的判断性能，项目内部的推理提示词（prompt）维持原文不变，只把面向用户的输出（探测结果、摘要、报告、对话回复）强制转为韩语。

此外，韩语版还补充了韩国本地的法律提示，包括《信息通信网法》和《个人信息保护法》的相关警示。

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kgp2vJibdHiaca6WDuHbwO76j8hkqBMZibzd6oic395X0ntpm2Qo1BwJiaVBMKdchH8zqZMKT31rcQxO9H7daJcyEmhpmqf0dhkfxDE/640?wx_fmt=png&from=appmsg)

*NEWS TODAY*

**一个必须正视的警告**

项目 README 中有一段**非常醒目的安全警告**，值得每一位关注者认真对待：

2026 年 10 月，韩国多家媒体报道称，调查当局在**针对韩国金融机构的个人信息泄露攻击**中，发现了原版 ARTEX 被使用的迹象，相关调查正在进行中。

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kjrLh8KvwOq4jAq1kIf8PSiavFmeCvS7a57WQUI7H9hz9wOuQoLZibDKzic7Dhv8tEOmA8Q85xBmCicPWl7tLN0PbBxl9ibgaEvr5CU/640?wx_fmt=png&from=appmsg)

正因如此，韩语版的发布目的被明确定义为：帮助防守方理解自主 AI 攻击的运作原理，从而建立检测和防御能力，而非协助攻击。

项目作者反复强调：只能在你自己拥有或获得书面明确授权的目标上使用。在韩国，未经授权对他人网络进行扫描或入侵，可能同时触犯《信息通信网法》和《个人信息保护法》。学习测试建议在 OWASP Juice Shop、DVWA 这类故意设计为脆弱的本地隔离环境中进行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kgGxTUeoZ2pQTzc0pHHcVy9XMAc5oKl012lQsO0gicd8w31yIN3qKES5EMtTexJFmNR7exw2MvsSVfiagysCibRMKeTFj7ShANeaY/640?wx_fmt=png&from=appmsg)

*NEWS TODAY*

**当前状态与注意事项**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5khJphVTyFpdxJHKpsYZaWQEP4OJKhAEC6ibWz9Ur1y44rVMa6RqspTicMRnpXyuXBFt7cmAYVNZzJUTOQ0DAvbqd4Yafib7Ysxrhg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kh36DuNANR5Qib2TOkUDPI2FB2YYxZ1fKyLlhCCn7Pgzc6pQ39ZK7wwMiclhYibSkv0qNRl6psFFgyAA5GpCq8SU8us1KN9PLRcRU/640?wx_fmt=png&from=appmsg)

截至 2026 年 10 月上旬，该项目在 GitHub 上已获得约 300 颗星，周增长 33 星，处于上升趋势。项目创建于 10 月 3 日，许可证为 AGPL-3.0，目前尚无正式 release。

有一个重要的使用细节：如果你打算用 Docker Compose 方式部署，需要注意 `docker-compose.yml` 中拉取的是上游作者发布的中文镜像，并不包含韩语界面。要看到韩语版的实际效果，目前需要从源码编译单二进制文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOTHxR4ic5kjYXHK6nKDIBS7Wz8fxlEUtwZq3q0FBPWhwa1R86SySAdDvQ8LrPqeXNrib7zZCXxX7pztxqlSFicccTXibApUPnMCIDTh24Ovrek/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kiaia6gE1qickV0WKXaTpPUp3XmcC7ljuSFFjx9hhicOJ9V8KUnNlfL57jticuIMouJcaM3IsTZDx7tWuPwibcZr1Cqxiarz6ZVp9G8do/640?wx_fmt=png&from=appmsg)

*NEWS TODAY*

**最后思考**

ARTEX 的出现标志着一个趋势：AI 智能体正在从"辅助工具"走向"自主执行者"。当一个系统能够自主规划、执行、并从结果中学习时，它在攻防两端的影响都是深远的。

对于安全从业者，理解这类工具的工作原理，或许比恐惧它更有价值。而对于普通读者，知道它的存在和潜在风险，也是一种必要的认知。

![](https://mmbiz.qpic.cn/mmbiz_png/GOTHxR4ic5kjjGeE03J8aKxwJibrgWFqkOD11ciaEFjhWrianUAY9K3jExWhjD1sSccrbMqCbTJvN3ppV2cEM8I0mjQP7ibicsiciaBJGiceEF7iaN4tM/640?wx_fmt=png&from=appmsg)

想要原版的朋友三连私信后台。

项目地址：github.com/jiwoochris/artex-ko

仅供安全研究与防御学习使用

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XicquaFUCrUwImfJ2MuXnFzKa4EqZmVGiapAbsWiaMR2hoic1Ox8QZHnla5xibqSC5gu99vPNwD7WBzqybuibPnmXMUw/0?wx_fmt=png)

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