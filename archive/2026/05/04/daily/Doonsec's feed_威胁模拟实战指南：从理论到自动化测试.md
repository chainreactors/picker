---
title: 威胁模拟实战指南：从理论到自动化测试
url: https://mp.weixin.qq.com/s/LEG5DEhMmQ80Z7aAtaAZSA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:01:07.198712
---

# 威胁模拟实战指南：从理论到自动化测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeSHATu2cIPyOhGcElU01DicFFVqLje3MwuFt14zOELZOL9XW3U2T2pTGJMMwnNpkFrGVNVOibPbfww7a55TRGj9GjryyM1PRuKI/0?wx_fmt=jpeg)

# 威胁模拟实战指南：从理论到自动化测试

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 一场关于威胁模拟的深度技术分享，从术语体系到工具实战。演讲者以十年攻击性安全经验，拆解威胁模拟与传统渗透测试的区别，教你如何利用MITRE ATT&CK、Attack Navigator和Caldera等开源工具，建立可重复的针对性测试流程。适合已经具备基本安全能力、希望更主动防御的团队。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcYW4UmMpt19xqjpGA9MicTibJt5micRJf87gFrdJLLib8icBFrruVntjSUHo3QTLWt8nn7NCVQPibcmXDCbiaDbUibzVugV6yMH7YU7Vw/640?wx_fmt=png&from=appmsg)

## 自我介绍：十年攻防老兵

那么我们就直接开始正题。先简单介绍下自己。我从事攻击性安全方面的工作，有十年经验。拿到过不少GX认证和其他资质。现在我在Basalt公司担任新角色。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibcvv7dC3t5rZibxYTVCtprVTr85IczqtJAK6CC7YXBB7fdZwIpfwgQGEzwiceOf3Jq5KCadpKFpdyFnrR79TkIOHrzBhJdhS2KQU/640?wx_fmt=png&from=appmsg)

我们公司最初只接渗透测试，给不同企业做评估。后来转型，更专注于产品安全领域，开发安全产品。转型中拿到了重要的政府客户，这意味着会面临更高层次的国家级攻击者。所以我们需要更深入地研究：怎么才能知道国家级攻击者怎么行动？怎么判断哪些测试是相关的？全部做一遍太费时间，必须筛选。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeNqVQrCqggTQUkEIk2NJAPRwXkVJbgbkr58yWnUDpr9Cfvv6Gaks7tObWZ0iau6I2mxXbKJeiaKJrkzxg8ecKTS2GicbFzsRxj4g/640?wx_fmt=png&from=appmsg)

这就是我对威胁模拟的研究——以及为什么这对我们做这类测试是正确的选择。威胁模拟大致就是：你看到一次攻击，找来渗透测试人员想重现它。分解攻击，分析手法，如果能逐步重现，那你就有了一套完善的模拟方案。

这跟传统渗透测试不一样。传统渗透测试就像牛仔一样无计划地进攻，到处找提权路径。但威胁模拟需要更详细的计划——因为你要模拟一个特定的攻击者。你是基于威胁情报来做渗透测试的。深入理解攻击者，用更结构化的方法，明确已经测试了什么、下次要测什么。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeSw8H5JFlVBjxHwFhTSc2xnjYsyatlPI3fH7xgNJv3Ft0icknOpxg1cOV093J9iaUrOrP6DTmiby97HYv3ThU5ATuvd9yVVEsiaLs/640?wx_fmt=png&from=appmsg)

很多公司年年找同一批人做同样的渗透测试，觉得测了三次没新发现就安全了。然后又买了花里胡哨的XDR方案，CISO到处说“我们已经有黑客认证了，什么攻击都不怕”。其实更好的做法是开始尝试新的攻击向量，看看自己有没有漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeOS5XPictY6pGNHgXD4QQkVibibuNvtOR1W0oeOSbqYFkehnyhNWonXyx3XcObkBAwgIBMIxSEBoadjvQt4iavPzouQBYfQMVI9Jc/640?wx_fmt=png&from=appmsg)

我喜欢引用一句话：“如果你未能制定计划，你就是在计划失败。”这对我而言是威胁模拟和仿真的好总结。制定计划再测试，不是乱撞。

## 术语体系：对手仿真 vs 模拟

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tiber5MKw4ibytQ7iatqGdckF7JI5WZylcdzSCaofPhALMuPHjBxglr00ib2kQRxf9QTeMic4Q8XvOic2hPUoXDOELPm8Qh1MTEJgwgeo/640?wx_fmt=png&from=appmsg)

先说清楚两个概念：对手仿真，就是只关注一个威胁行为者，看他采取了哪些步骤、用什么攻击方式。而威胁模拟，是同时考虑多个威胁方，比如多个勒索软件组织，你可以把它们组合起来，预测下一次勒索软件攻击会是什么样子。如果你能防范这类威胁方（至少是有记录的），就能领先一步。另外还有微观模拟等术语，但我今天主要讲这些。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibfwm0xCWVK8mOTkd8Td5G43aVGPJ7kVEqSeVV6FnCcuOXYNmlPp0xwqa1JI8WaVv1JokRWP9iaVR7IQIQqNgAxkia9LIGTZpCPiaE/640?wx_fmt=png&from=appmsg)

## 实施威胁模拟的五步法

对我来说，拆解威胁模拟的步骤，才能理解怎么在自己公司落地。第一步：理解自己的组织。你作为安全负责人，先要搞清楚自己运营在什么领域——石油？能源？生物制药？这样你才能分析哪类攻击者会想攻击你。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcJgibFEteSkiapsJ9rywq4UYwnTwrmxt3nqlh3B80S69icRje5eMyNlKmcTv3EwEbvGtHNQ1VwLwR1G11Y98siaUWwJiaoPZriayicxk/640?wx_fmt=png&from=appmsg)

一旦清楚要保护什么、为什么保护，识别攻击者就容易多了。有数百种攻击者可能想渗透进你公司，但你需要筛选出最关键的那些。然后提取他们的TTPs（战术、技术与程序）。注意，TTPs必须跟你组织相关——比如你连邮件服务器都没跑，那分析鱼叉式钓鱼就没意义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfTqK6l4vSepqNH5kOdqjgEcPNwvsbV2DTric18a81UZhX6D5y6hHVqtjjQXVXQRchbFPWCBYGBUDNhbagrbIIAic2PNh5ABia1Jc/640?wx_fmt=png&from=appmsg)

知己知彼，百战不殆。但网络安全里最难的是你很难知道谁会攻击你。如果你不知道谁在攻击你，你怎么主动防御？威胁模拟就是让你在攻击真正发生之前，主动测试自己的防御能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdaCib5dFYxce2tmpibyLaLXrCEw4FGXHmSBCOWgdmWkbCNaiaLokHlybqhLvWgS6LezEhJRLUgWImpwIPRXMcteF5LRv88lZX5dU/640?wx_fmt=png&from=appmsg)

威胁模拟的基本抽象层级分为：动机（为什么攻击）、内容（攻击什么）、实施方法（怎么攻击）。动机跟公司类型强相关——科研机构守IP，能源公司守运营稳定性。攻击者可能想彻底摧毁系统，让所有系统下线且无法恢复。你还要考虑杀伤链的各个阶段，从初始访问到数据渗出。

所有这一切都归结于了解自己的组织。如果你没有清晰的资产清单，连自己用什么技术栈都不知道，那遇到数据泄露你都判断不出跟自己有没有关系。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibfc8HSBatsWbcvRDUtOd02cib45FN3XGxccc6UAqt2wRd9Jr0u1F7MGdHDKa8vbJfRnBzlLNhmlHHzV38vI8x2XzAfY0XxVQGMI/640?wx_fmt=png&from=appmsg)

你可能会想：TTPs这东西到底是什么？为什么用它？渗透测试人员会说“我们通过鱼叉式钓鱼初始访问，通过木马PDF建立C2”。蓝队讨论的是邮件异常、DNS外泄。其实他们说的是同一件事，只是语言不同。TTPs就是这套共同语言。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tiben19P9XibDbT3SwUh1B0HUvopo6aLyEwN16M0lv9OdB9iaa2BCXiaFDyYF04kibF4lIQcve8xvkNmT8EzOBlxFzr6XyFzdphuoiago/640?wx_fmt=png&from=appmsg)

为什么TTPs是攻击者最难改变的东西？如果你只看签名（哈希值、IP地址、工具名），攻击者换起来很容易。但想改变整套技术——从硬件投递切换到新建C2服务器——难度就大多了。所以大多数框架（比如MITRE ATT&CK）都聚焦于TTPs而不是哈希值这类指标。

## 筛选相关威胁行为者

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdF5QxRfF5h1I6kXe8ZGpK9I8YRwEMN7kvUnoJ2NmicXDrTlr7Qia4SYJ0l7eWDNzZiccISrQltonialoTqG7BSA0kc0cFucVccvNc/640?wx_fmt=png&from=appmsg)

当你开始分析哪些威胁行为者跟你相关时，需要深入分析动机。你关注的地理区域？比如你在北约国家，可能更关注中国或俄罗斯的国家行为体。如果你是发电厂，可能还需要关注周边非北约国家。还要看技术栈是否匹配——这个攻击者用的攻击方式是否跟你的基础设施相关？你们组织在Twitter上很活跃、发表大量政治立场？那可能招来其他威胁行为者。

另外一个因素：这个攻击者过去12个月是否持续活跃？通常给额外风险权重。如果你为军方提供软件，可能沦为供应链攻击目标。所以有多种方法判断相关性和不相关性。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfYFlnkmLabbySzjQYKkl0ibU6Tl1VKuD5fsSY3wlCbL37c7lNy3Ofib520qVcgXXjicwLicgFjNheFqTJ7QEtpZx4ba3nG0J99Ygc/640?wx_fmt=png&from=appmsg)

简单介绍一下MITRE ATT&CK框架。你可以在attack.mitre.org直接访问，不用下载任何东西。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeSPYfNGSqJmpCtiblQ73DzPCoUBG3K3HYUUChRWSvoaqicPiby9ngrO1385HF8P2WKQpquM3f2r5GM8bdFQBoG4FQdTUSdpUjD3E/640?wx_fmt=png&from=appmsg)

比如你点开一个已知威胁行为者——像“高级威胁29”（APT29），就能看到它的描述（针对北约成员国，喜欢攻击研究机构），使用的技术，以及相关的取证报告。这阅读材料很扎实。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd4vichTX4TaOnNkCq5WOmGuY8us9qsuXdeFSral02AEyUENYPw3DRfWHrCTz9f9XZIbz2R0YTQeibBUSjQU0btBPwz3sq3PCy2k/640?wx_fmt=png&from=appmsg)

如果你觉得从PDF里筛选内容麻烦，MITRE开发了一个很好用的工具叫Attack Navigator。你可以把威胁行为者分组，点击查看。可以离线运行，在GitHub上能找到。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdfbHiaBdiaIdH5VU5sNQEBuS548kFPx06qVj5CO0bHqbuSRtLZYIXHqPAeI3zictOnw3XAY85BlLl2Mre37T8fWK1g5houWHH9Io/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibewbn7ynqiaNptwicfYGCH30eDRHDvq1Olib1LEBkbS6st16judM3sFhDKNd4dibjyWWjKTVGPCZib8ibca7OpqeFrkic1GWBSGINpVkQ/640?wx_fmt=png&from=appmsg)Attack Navigator会高亮显示攻击者使用了哪些技术（侦察、扫描、凭证登录、鱼叉式钓鱼附件等）。你可以开始规划自己的测试活动，验证你自身抵御这类攻击的能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdgVqZKOicc2cpaI0mAibwrLp4JX0wTCaWUg7RvH3ZyRlOcIIFv5QPrHFic0sQNvjLhHQBFACJU2NYNc1zlx60GbAJiaKiaNn8RujwY/640?wx_fmt=png&from=appmsg)

MITRE还提供了完整的威胁模拟方案，分三个阶段。你可以扫码下载文档，也可以直接访问链接。建议先阅读，再开始自己写计划。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdJib5sAb2mmutBSIP0U79lUjHcDCibpHpIe8kK2ucibPk0zYREN6JHAXLQHVkXdoXESzKWembbb56TGq45VyZfQeWWjbmjAGZxhg/640?wx_fmt=png&from=appmsg)

现在你可以制定自己的计划了。看看哪些工具适合发现，哪些命令会被EDR检测到。这是一份非常详细的攻击实施计划，对渗透测试人员来说是个很好的开始。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdKiaLfich4h3qIj523zGFWXMibOxibBSpcT3aDoziawq5snicaiaYBs5pcnPicZrEBfJiaJpPfQsAwtLuZ1udBPney6IcRUHiaFels0akr8/640?wx_fmt=png&from=appmsg)

看看他们能用这些命令做什么，你的安全方案能覆盖哪些。我们把计划分成三个阶段：第一阶段是初始入侵（怎么获得初始访问权限，怎么停下一切），第二阶段是网络传播（怎么横向移动、发现新主机），第三阶段是数据外泄（怎么收集、压缩、外带数据）。Attack Navigator里会详细展示这些术语。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibf3niaiaCAZRpMO4oOkFv00Wqe5Qiafb69L6Ko5XCCHcfpzJPUuicibgFVFrXpuqeWcRlIdxjIaAJiahSibsQKZg9e0xNwJPNFebzmkqo/640?wx_fmt=png&from=appmsg)

在Attack Navigator里，第一部分是初始立足点，中间展示网络传播，最后是数据外泄。好的，趁我清醒继续讲——框架体系多如牛毛。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfLY4hhNIbbdagEtlicnzRxcjBxtZQmMqZAuHWaLBJAC6UARgibmIQnQ5HAaibbC3QiaU2LeKx74iaEHIDde6JlM7peeDRYdJzCRnRo/640?wx_fmt=png&from=appmsg)

比如统一杀伤链框架，也很简洁。它同样分初始立足点、网络传播、数据外泄三阶段。每个步骤可能多次发生，要清楚收集目标和观察目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdkQicrWgBnbkFibIB1U2RyuSia4jwadVGXCG7ibbkTT5vYibSKspnUEzIsr5vlCQGicIuXjeGJLdPSSmKvUvX2R0ia2FTshISC9hscWE/640?wx_fmt=png&from=appmsg)

强烈建议你深入研究MITRE提供的模拟计划，结构非常完善，能为你写自己的计划提供参考。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfrKD4goia2O1un059nQqIq2gpdG6ZoUcnEdBW8icicab8nw7hUdY1PO9egKnXxiapoVDIVx7TkicnpeIWfO4hV9xah6oAddzrRssBM/640?wx_fmt=png&from=appmsg)

在研究完计划或目标威胁行为者之后，你会得到一个“受影响版本”的摘要——不是缩减信息，而是对测试人员更相关的信息。你需要提取出来。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd6HiaCXFJBP5n9HYonj5BEvBDzRYcAaKjRzgMSTHp9pI3d7VbEXJQQMweCRa0RvqvooGz5FGyv9CIzuGKM5grFNXSYbfFGBJ6s/640?wx_fmt=png&from=appmsg)

像之前说的，你可以有一本“现场手册”。同样在之前那个网站，里面列出了不同C2框架的命令、已做的事情和命令实现方式。这是查看检测的好方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcvCTW5nLlEiazvRicNicxibTibA3RZRMiaVMolAgmVHEMROO5rXVClMZTwMJwgjnibKtxEFuIdmzqlerkPR6Gw0j5Dv39Tk3o9s13Ricc/640?wx_fmt=png&from=appmsg)

在渗透测试任务中，公司通常建立自己的配置文...