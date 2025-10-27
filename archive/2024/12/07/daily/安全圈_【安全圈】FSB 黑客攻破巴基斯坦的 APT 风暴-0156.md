---
title: 【安全圈】FSB 黑客攻破巴基斯坦的 APT 风暴-0156
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066435&idx=2&sn=e1768cc7c8b066ea102465a04c755140&chksm=f36e7ec3c419f7d5b417b07f85d9e4cd3aa392d85a37a9819b361b656094ccf0dcbaf903d725&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-07
fetch_date: 2025-10-06T19:40:12.927264
---

# 【安全圈】FSB 黑客攻破巴基斯坦的 APT 风暴-0156

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgdme7EAeBhHP74oFZvnicp3ia7ibNA4nMkAhSmcLuaJeibwuE9yxeLLuqibSAliaVFpXSa6fNmw2GNAnPQ/0?wx_fmt=jpeg)

# 【安全圈】FSB 黑客攻破巴基斯坦的 APT 风暴-0156

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgdme7EAeBhHP74oFZvnicp3jHnh17LN3fvQKqj44K3dlxiaSYq5Peb1UCuicFL02qm1JZmSBf4BATuQ/640?wx_fmt=jpeg&from=appmsg)

俄罗斯国家情报机构行事的黑客已经攻破了在巴基斯坦活动的黑客的网络，利用他们的间谍活动从阿富汗和印度的政府、军事和国防目标窃取信息。

2022 年 12 月，网络安全和基础设施安全局（CISA）将 Secret Blizzard（又名 Turla）与俄罗斯联邦安全局（FSB）联系在一起，它进入了另一个高级持续性威胁（APT）Storm-0156（又名 Transparent Tribe、SideCopy、APT36）运行的服务器。它很快扩展到 33 个由 Storm-0156 运营的独立指挥控制 (C2) 节点，并于 2023 年 4 月入侵了其黑客同伴拥有的个人工作站。

微软和黑莲实验室的研究人员说，从那时起，Secret Blizzard 就能从 Storm-0156 的网络攻击中窃取敏感信息，这些信息来自阿富汗政府机构和印度军事及国防目标。

间谍与间谍

具有讽刺意味的是，威胁行动者–甚至那些为民族国家工作的威胁行动者–可能很容易成为其他威胁行动者的猎物。正如 Black Lotus 实验室研究员 Ryan English 所解释的那样，他们通常不会努力保护自己的基础设施。“如果你花大量时间将自己的网络打造成堡垒，那么你花在进攻上的时间就会减少。说到底，这是一个时间和成本问题，”他说。

即使网络攻击者想提高网络安全性，他们也会面临独特的挑战。最近，一个威胁行为者尝试使用 Palo Alto 的 Cortex 扩展检测和响应 (XDR) 进行实验，就证明了这一点。通过安装 Cortex，他们无意中为 Palo Alto 研究人员提供了一个了解其操作的窗口。

目前还不清楚 Secret Blizzard 是如何获得进入第一台 Storm-0156 服务器的初始权限的，但 “我们认为他们是从公开报告中识别出 [Storm-0156] C2 节点的。因此，他们的进攻团队几乎是像威胁研究员那样工作的–花时间查看公开报告，寻找进入别人的东西的可能性，”English 说。

不过，他补充说：“他们并不满足于公开的信息。他们可能进行了一些侦察。我们认为，他们使用了一些远程桌面透视技术，以进入目标的其他（基础设施）。这可不是一件容易的事。”

暴雪从 Storm-0156 窃取的秘密

由于掌握了 C2 节点和工作站，Secret Blizzard 对 Storm-0156 的工具、战术、技术和程序（TTPs）以及已经从受害者那里窃取的数据拥有广泛的可见性和控制权。它利用所有这一切，取得了强大的创造性效果。

在某些情况下，俄罗斯人利用 Storm-0156 的服务器向现有受害者的系统植入后门。这样，他们就可以从阿富汗外交部、情报总局（GDI）和外国领事馆等多个政府机构窃取敏感信息。

不过，针对印度的目标，Secret Blizzard 采取了不同的策略。只有一次，它针对印度国内的实体部署了后门 “TwoDash”。相反，它针对 Storm-0156 本身部署了后门，窃取了巴基斯坦人已经从印度军事和国防目标窃取的敏感记录。微软推测，“秘密暴雪在阿富汗和印度采取的方法不同，可能反映了俄罗斯领导层的政治考虑、联邦安全局内部不同的地理责任区，或者是微软威胁情报部门的收集漏洞”。

通过隐蔽实现前所未有的安全

威胁行动者经常合作，但研究人员还没有发现任何其他组织像 Secret Blizzard 这样，为了共享目标访问权限而互相黑客攻击。

这也不是 Secret Blizzard 第一次这样做。首先在 2017 年，该组织访问了属于伊朗 APT 34（又名 Hazel Sandstorm、OilRig、Crambus）的工具和基础设施。在即将发布的一篇博文中，微软将披露秘密暴雪在乌克兰开展的另一次活动的细节，在此期间，它使用了属于其他两个威胁行为体的机器人和后门。

还有去年爆出的案件。今年 1 月，Mandiant 报告了与 Secret Blizzard 有关的活动。今年 4 月，卡巴斯基声称该活动是由总部位于哈萨克斯坦的 APT Tomiris（又名 Storm-0473）实施的。现在看来，Mandiant 的猜测是正确的：Secret Blizzard 是幕后黑手，但通过使用 Tomiris 的后门迷惑了研究人员。根据这一最新进展，Dark Reading 已经联系了卡巴斯基。

托米里斯的烟幕弹说明了秘密暴雪的方法的好处。当然，只入侵一个 APT，它就能访问属于该 APT 所有受害者的基础设施和敏感数据。但除了效率之外，它还可以利用这种访问权限来掩盖自己的活动，将其伪装成来自另一个威胁行为者。

***END***

阅读推荐

[【安全圈】Crypto.com 与 HackerOne 一起推出 200 万美元的漏洞赏金计划](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=1&sn=8b5178681a68125be7487364041e0e92&scene=21#wechat_redirect)

[【安全圈】立即修复，微软驱动程序关键漏洞已被APT组织利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=2&sn=c856137ec845bc74a8a86abc23c1eb69&scene=21#wechat_redirect)

[【安全圈】谷歌浏览器类型混淆漏洞让攻击者能够执行远程代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=3&sn=28c802936604146904c583d74c14846f&scene=21#wechat_redirect)

[【安全圈】知名伏特加品牌因勒索攻击而倒闭](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=4&sn=7bf50178818225897c7e681c7ddab487&scene=21#wechat_redirect)

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

阅读原文

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