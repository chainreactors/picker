---
title: 2026 年该挖什么漏洞
url: https://mp.weixin.qq.com/s/U4gV259Ib4GImp-eqJq5Uw
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:35:50.336179
---

# 2026 年该挖什么漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3Q8fQao9DTmH0nAfib3POEPt3kEDjR027SwAnia2Az5OElovNKC1HxOEQ/0?wx_fmt=jpeg)

# 2026 年该挖什么漏洞

Appsec.pt

securitainment

![]()

在小说阅读器中沉浸阅读

Bug Bounty 是一个竞争极为激烈的领域。想要在众多猎人中脱颖而出，你必须明确自己该找什么——而不是漫无目的地四处乱试。

漏洞类别的流行程度会随多种因素而变化：漏洞猎人是否在关注它？开发者是否还在犯这种错误？LLM 生成的代码是否容易出现这类漏洞？诸如此类。

## Web LLM 攻击

几年前，各家公司纷纷争相将 AI 模型集成到自己的服务中。当时，不少猎人通过挖掘这些系统的缺陷收获了丰厚的奖金。

时至 2026 年，许多 AI 模型已经与 RAG（一种让 LLM 能够读取用户提供的文档和文件的技术）以及内部 API 相结合，以增强其能力和实用性。

这本是好事，但同时也暴露出巨大的攻击面，可供漏洞猎人加以利用。

我在阅读其他猎人的 writeup 以及关注 HackerOne 的 Hacktivity 时注意到，许多猎人似乎已经完全忘记了去挖掘 LLM 相关的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3BUiblJYlqkXwVG5j9QNttAPkrIGAbygCCrDBgmlQPXRIYLAO76tib29g/640?wx_fmt=png&from=appmsg)

HackerOne 上 Prompt Injection 的统计数据

看看 Bugcrowd 的 VRT 中列出的各类 AI 相关漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt37LAaFmubEspNZOqFItRd6ADBPRHLJ7bjOxsfZKLYZEy3yCLQXkmK8g/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3ibD78WSiaA1As6lFGPHXMYJSGt28f8GwMGDqWiaqgyLLrVjEQeyliafUYA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt38X9skGaPlqK0iaYgiak4CBWv2nqwMkKafwURvjxESEuC3BJxecVAIlBQ/640?wx_fmt=png&from=appmsg)

可以看到，与 LLM 相关的可利用漏洞数量众多！

在大多数部署了 AI 功能的目标中，你最有可能发现的主要漏洞包括：Prompt Injection、System Prompt Leakage，以及 Training Data Leakage（或通过 RAG 嵌入的公司数据泄露）。

此外，速率限制不足和 HTML 注入在这类基础设施中也相对容易发现。

我计划近期撰写一篇文章，深入探讨这些漏洞以及如何在真实目标中挖掘它们。

## 凭证填充攻击

凭证填充（Credential Stuffing）攻击近来呈上升趋势，企业对此的安全意识也随之增强。

越来越多的公司开始意识到凭证泄露的危险性，因为这可能带来各种严重后果。

举例来说，根据攻击者获取的凭证类型，他们可能得以访问管理后台、获取本应付费才能查看的内容、接触内部数据等。

如果你想为 Bug Bounty 目标寻找泄露的凭证，就需要一个数据泄露搜索引擎。市面上有多个不错的选择（如我在这篇文章中介绍的），但我目前使用的是 BreachCollection，因为它的界面和性价比都是最优的。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3GKpvyndLNAdVCibb9CteehwEbVdiaiafib2819zFyicIROwFWTMoOPHWlGA/640?wx_fmt=png&from=appmsg)

查找泄露凭证（本文已做脱敏处理）

在收集泄露凭证之前，你首先需要确定是要查找内部凭证还是用户凭证。

如果查找内部凭证，主要需要执行「邮箱域名查询」。在这类查询中，BreachCollection 会检索所有邮箱域名与目标匹配的凭证（如 `user@target.com`）。

如果查找用户凭证，则需要执行「域名查询」。在这类查询中，BreachCollection 会检索所有可用于登录目标域名的凭证。

有时，你也可能通过域名查询找到员工或内部凭证，正如我在这篇 writeup 中所展示的那样。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3ibjaOBziaOaUHiacaMSwSLWdcTRq2r3ogFS3bFEyoIicluU4icEBpx7NOYQ/640?wx_fmt=png&from=appmsg)

查找泄露凭证已成为我 Bug Bounty 侦察流程中不可或缺的一环，为此我开发了一款工具，它集成了 BreachCollection API，可以在获取 Wayback Machine 中所有 URL 的同时，自动收集目标的泄露凭证。你可以在这里查看。

我还在 BreachCollection 的控制面板中设置了邮件提醒，这样每当我关注的 Bug Bounty 目标出现新的泄露凭证时，我就能第一时间收到通知，迅速核实并提交报告。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3DeDAZvezH352ETVicxaTSSLF7tTaicAoMmkiaribNaMmewtF5TUmyRPMnw/640?wx_fmt=png&from=appmsg)

## 竞态条件（条件竞争）

竞态条件（Race Condition）是 Web 应用中最酷的漏洞类型之一。

它发生在检查约束的时间点与执行操作的时间点之间存在足够大的时间窗口，使得攻击者能够趁机利用。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3bgUYwsHgTv8kvctgKK9ibHHlo0iaIkNNPELpbDz0OdibZRPW6Uiam73yicg/640?wx_fmt=png&from=appmsg)

实际上，竞态条件在今年会变得更容易挖掘，原因有几点。几年前，大多数大型公司开始从单体架构（所有服务组件运行在单一服务器上）转向微服务架构（不同服务运行在不同服务器上）。

微服务架构比单体架构更容易出现竞态条件，因为数据库锁定（即在某个进程正在修改数据库时，阻止其他进程同时修改，从而避免竞态条件）在微服务架构中实现起来要困难得多。

此外，随着 AI 在开发者群体中日益普及，大家对这类问题的关注度越来越低，更专注于快速交付产品。

对于开发者而言，解决竞态条件需要深思熟虑。这恰恰为漏洞猎人提供了绝佳的机会，让你在 Bug Bounty 中更容易取得成功。

如果你想更详细地了解这类漏洞的原理，可以阅读我的文章，其中介绍了成为竞态条件专家所需的一切知识。

## 结论

随着 Web 开发趋势的演变，我们作为漏洞猎人的方法论也必须与时俱进。

无论是 AI 集成带来的更大攻击面、凭证泄露的威胁，还是微服务架构引发的竞态条件挑战，对于那些愿意在别人忽视之处深入挖掘的人来说，机会比比皆是。

欢迎在评论区留下你的问题！

**祝狩猎顺利，2026 年收获满满！**

---

> Which Bugs to Hunt for in 2026
>
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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