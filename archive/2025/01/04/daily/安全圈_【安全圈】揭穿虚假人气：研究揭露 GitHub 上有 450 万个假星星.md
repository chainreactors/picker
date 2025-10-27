---
title: 【安全圈】揭穿虚假人气：研究揭露 GitHub 上有 450 万个假星星
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067112&idx=1&sn=425e0c2e12fd7778269f7fa579522d47&chksm=f36e7968c419f07e35b42cc902697e4cfd76a13a6536a8a32ff9dfe128b2e939352bece6b075&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-04
fetch_date: 2025-10-06T20:11:18.929514
---

# 【安全圈】揭穿虚假人气：研究揭露 GitHub 上有 450 万个假星星

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaRXBZQHFJ0ZBLJTa9CQlib2wKrGQx9cK6wAv2gAJeiaMOZBwmHEic4DdpeHSr6uA2MoTjJiamcDMz7Cg/0?wx_fmt=jpeg)

# 【安全圈】揭穿虚假人气：研究揭露 GitHub 上有 450 万个假星星

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

GitHub

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaRXBZQHFJ0ZBLJTa9CQlib2Yeia3uib6eZPHLrZVkaoPr0lCNdOz2djXvkKbibhMTwn4bGiaBPgkXcn5g/640?wx_fmt=other&from=appmsg)

卡内基梅隆大学、北卡罗来纳州立大学和 Socket 的研究人员开展的一项研究对 GitHub 星级评定系统的完整性提出了质疑。该团队发现，虚假“星级”数量激增，令人担忧，这些“星级”被用来操纵全球领先开源平台上存储库的受欢迎程度。

该研究使用名为 StarScout 的检测工具系统地分析了超过 20 TB 的 GitHub 元数据，识别出超过 450 万个疑似虚假星星，涉及超过 15,000 个存储库。研究人员详细说明，这些星星经常被用来扩大短暂的恶意软件活动或虚假夸大存储库的知名度，通常伪装成游戏作弊程序、加密货币机器人或盗版软件。

GitHub 星星数是至关重要的受欢迎程度信号，影响着软件供应链中开发人员的选择甚至决策。然而，这些星星数很容易被滥用。正如研究人员指出的那样，“星星数是最广泛使用的受欢迎程度信号，但它也存在被人为夸大（即伪造）的风险，从而降低了其作为决策信号的价值，并给所有 GitHub 用户带来了安全风险。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaRXBZQHFJ0ZBLJTa9CQlib22x0WB2CpNjRZUhvN5IcVKGXBicFN5p4L6cMGCaicVFxDZYNUMsO3lbJw/640?wx_fmt=other&from=appmsg)

来源：arxiv

研究发现了多种欺诈行为，包括：

* 机器人网络：自动化账户大量生成星星。
* 众包操纵：模仿真实活动的人为操作的方案。
* 虚假增长黑客：为寻求知名度而增加非恶意存储库星级的策略。

受益于假星星的恶意存储库构成了切实的威胁。正如研究人员所强调的那样，“大多数假星星都用于推广伪装成盗版软件、游戏作弊软件或加密货币机器人的短命恶意软件存储库。” 在一个引人注目的案例中，一个虚假声称是区块链实用程序的存储库被发现包含旨在窃取加密货币的经过高度混淆的恶意软件。

分析显示，这些虚假星星活动在 2024 年达到顶峰，当年 7 月，超过 15.8% 的存储库获得了 50 颗或更多星星，涉及欺诈活动。许多存储库在被发现后被删除，但问题的规模凸显了采取对策的迫切需要。

为了解决这一日益严重的问题，研究人员开发了StarScout，这是一种可扩展的工具，能够识别盯着看的行为中的异常模式。它利用了两种核心检测策略：

1. 低活动签名：识别在变为非活动状态之前已启动最少数量存储库的帐户。
2. Lockstep 签名：检测短时间内针对特定存储库的账户组协调活动。

这种方法使团队能够发现假星集中度较高的存储库，同时最大限度地减少误报。

研究结果对 GitHub 星星数量作为质量或可信度指标的可靠性提出了质疑。研究人员警告称：“星星数量是一种不可靠的质量指标，不应将其用于高风险决策”，并提倡对存储库进行多方面的评估，包括活动指标和安全审计。

对于 GitHub 平台管理员来说，该研究建议采用加权人气指标并增强检测机制，以更好地识别和消除欺诈活动。随着软件供应链越来越依赖开源组件，确保星号等信任信号的完整性至关重要。

来源：https://securityonline.info/unmasking-fraudulent-popularity-study-exposes-4-5-million-fake-stars-on-github/

***END***

阅读推荐

[【安全圈】2024 年最大的网络安全和网络攻击事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=1&sn=a9ecd46a4afe0c77216a405c825a1e9a&scene=21#wechat_redirect)

[【安全圈】美国财政部遭遇重大网络安全事件 怀疑与中国有关](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=2&sn=2680436663695b4f81edee2d0c8108b1&scene=21#wechat_redirect)

[【安全圈】新的“DoubleClickjacking”漏洞可绕过网站的劫持保护](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=3&sn=6a10a23e41cc2e64a94951ad4f2b52a7&scene=21#wechat_redirect)

[【安全圈】至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=4&sn=6f97d873b84e125e9f9c5c98947bace2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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