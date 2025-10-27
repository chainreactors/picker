---
title: SIEM的昨天、今天和明天
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651119784&idx=1&sn=a1a6b7426d437be8f1fc0da81fa8103f&chksm=bd14507b8a63d96d107ecc5d25cf3a62f92b7779b8df4f4875d5c8a42645f0a66495d37b4e9b&scene=58&subscene=0#rd
source: 安全牛
date: 2022-11-15
fetch_date: 2025-10-03T22:45:42.808931
---

# SIEM的昨天、今天和明天

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkB5XAicPgxibsQibARuh6rL7AEd4zUeARa6rdDSpMw7FJiaxiabmjb4d6Epv9iaenjQkWhyJyuIqbBnyjKw/0?wx_fmt=jpeg)

# SIEM的昨天、今天和明天

安全牛

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkB5XAicPgxibsQibARuh6rL7AEZLdqYKUwEkgibMlsj3dxz42ghTJlmtEQtn2iavyaRyNxDzJ41IcJVaCQ/640?wx_fmt=jpeg)

SIEM（安全信息事件管理）系统的应用已经超过20年。在此期间，SIEM由最初的边界安全事件关联工具逐渐发展成为企业网络安全治理、风险管理以及合规建设的重要支撑平台。今天，在很多企业中，SIEM已经成为安全团队日常处理威胁事件的优先选项，不仅可以从IT基础架构中的海量信息资源中收集和分析各种攻击活动，同时也是实现安全自动化、DevSecOps、态势感知等安全管理和运营技术的基础。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkB5XAicPgxibsQibARuh6rL7AEvxLyMcBl6ZabF48hjPlH0telmKiaDqRqeIKGOO6oZiaX7QJWC9d7vdYQ/640?wx_fmt=png)

**昨天：从日志聚合到安全运营**

第一代的SIEM产品诞生于本世纪初，起初是被作为一种日志聚合的工具，只是在一些大型头部企业使用，用以解决数据孤岛的问题，同时还可用于历史数据保留和法律合规遵从。最早期的SIEM代表性厂商包括ArcSigh（现隶属Micro Focus）和QRadar（现隶属IBM）等公司。

在第一代SIEM产品中，使用了非常基础的关联引擎，建立非常简单的关联规则，例如“如果看到X、Y和Z，就应该在工单系统中打开工单，并向安全团队发送警报“。由于第一代SIEM产品针对非结构化数据的本地处理能力非常薄弱，可能需要花很长的时间来查询数据，并只能获得事件原因的初步分析。鉴于技术原因，这个时期的SIEM可用性非常糟糕，甚至给一些客户留下了花钱买罪受的感受。

随着时间的推移，企业的数字化转型快速发展，各种安全设备的运营数据开始激增，最早期的SIEM产品逐渐跟不上数据产生的步伐，因为其所使用的结构化数据库无法与时俱进，而编写新的解析器需要很长的开发周期。

当Splunk公司进入SIEM市场后，迅速改变了第一代SIEM厂商的游戏规则。该公司研发了一种灵活而强大的数据存储和搜索引擎，通过索引技术，可以搜索各种类型的原始数据（结构化数据和非结构化数据），并迅速将数据转换成可搜索的事件。这种技术是一项突破，因为它使SIEM工具更容易获取、搜索、存储和显示所有不断增加的数据，并获得洞察分析能力。在2012年，Splunk首次作为领导者出现在Gartner 发布的SIEM魔力象限中，并在此后的很多年占据着市场领导者位置。

根据研究机构SANS在2019年研究报告数据显示，截至2018年底，有超过70％的大型企业开始依赖SIEM系统来进行数据关联、安全分析和运营。同时，很多企业的安全运营中心团队围绕SIEM配备了用于威胁检测/响应、调查/查询、威胁情报分析以及流程自动化/编排的其他工具。SIEM正式发展成为企业安全运营的发动机。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkB5XAicPgxibsQibARuh6rL7AEvxLyMcBl6ZabF48hjPlH0telmKiaDqRqeIKGOO6oZiaX7QJWC9d7vdYQ/640?wx_fmt=png)

**今天：应用成本不断增加**

当以零日攻击为代表的高级威胁大量出现后，SIEM行业的竞争格局再一次开始改变。传统SIEM系统由于存在难以实现精准告警、漏报较为严重等问题，已不是企业安全运营管理的理想选择。作为企业内部安全日志的汇聚器，SIEM的基本功能或许永远不会过时，因为本地安全日志始终是最具价值的威胁情报来源。但安全团队需要尽快升级优化SIEM，配合更多的威胁检测/响应、调查/查询、威胁情报分析以及流程自动化/编排等先进安全能力，以实现更加高效、准确的安全威胁检测。

为了跟上威胁发展的步伐，现代的SIEM产品需要更深入地了解所存储的数据，并运用更多的网络智能技术来应对挑战，用户和实体行为分析（UEBA）和机器学习技术应运而生。各大安全厂商都积极尝试将新一代SIEM产品与 UEBA、安全编排、自动化和响应 ( SOAR ) 和扩展检测和响应 ( XDR ) 结合起来，以实现更加智能化的威胁检测和响应能力。

在Gartner最新发布的2022安全运营技术成熟度曲线中，对主流的安全运营技术进行了分析。报告认为，SIEM技术已步入稳步发展并趋进成熟的阶段，这个分析也正符合市场的现状，很多企业在安全运营中已把SIEM作为主要实现平台。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkB5XAicPgxibsQibARuh6rL7AE741lnh9fcdJS8qZFxbAvJfs8LjZnxPnhGPm7qhgWksSOVNIzVG95Xg/640?wx_fmt=png)

从理论上讲，更多的数据可以提供更好的洞察力，但这也容易错过一些严重的安全威胁，而且还会产生较多误报。一旦重要报警与大量误报信息同时出现时，就会导致重要报警数据淹没在海量的误报及非重要报警中，无法立即响应真实报警。

由于总体安全运营数据爆炸式增长，导致SIEM应用成本快速增长，每年在SIEM方案升级上的投入让企业难以承受。为了控制应用成本，许多企业的安全团队必须做出艰难的决定，决定他们实际将多少（以及哪些类型的）数据提取到SIEM中进行分析，其余的数据只能存储在没有处理能力的系统中，无法及时得到处理和分析，这会带来巨大的安全风险。

鉴于SIEM技术目前的应用成本挑战，企业组织需要根据自身的需求，选用更好、更具成本效益的技术解决方案。服务化的SIEM方案可以实现高度智能化的分析和检测，同时价格也更加合理、透明，这对于很多中小企业、初创公司和非营利组织来说，是一种比较合适的选择。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkB5XAicPgxibsQibARuh6rL7AEvxLyMcBl6ZabF48hjPlH0telmKiaDqRqeIKGOO6oZiaX7QJWC9d7vdYQ/640?wx_fmt=png)

**明天：SIEM的未来在云端**

根据Gartner的研究数据，全球SIEM产品市场已从从2020年的34.1亿美元增长到了2021年的41亿美元，取得了20%的增长率。SIEM市场发展的主要驱动因素仍然是检测、响应、攻击面管理以及合规。未来，企业希望未来的SIEM产品能够在宽度和深度两个方面同时满足其数字化业务发展和安全防护的需要。

新一代SIEM产品继续不断吸纳新的功能，包括SOAR、UEBA、TIP、自服务安全分析、持续威胁内容创建、Incident管理等，这需求SIEM产品进一步转变架构策略以适应客户需求，而最终指向就是云化Cloud SIEM（包括云原生化和云托管）。云技术不仅可以让SIEM整合更多威胁检测引擎，实现更快的运营数据分析，还可以有效降低企业的应用成本。

Gartner分析师认为，Cloud SIEM将会成为未来SIEM产品发展的首要形态，这也意味着SIEM的架构发生了重大变化。云化的好处不仅是顺应云时代和远程办公时代的需要，更重要的是为了降低SIEM自身的部署和维护的负担，将重点投入到基于SIEM的安全运行上。Cloud SIEM对中小型企业来说是非常理想的选择。

此外，对于不想在SIEM上投入太多资源的企业来说，由托管安全服务提供商（MSSP）来运营SIEM也是一个很好的选择。但是首先需要清楚的了解角色和责任。总的来说，未来的云SIEM提供商更多的职责是初期建设部署和优化完善SIEM产品的功能更新；MSSP的职责主要是中后期的威胁场景分析应用及事件跟踪处置，而企业用户只需要提出应用需求和确认决策。

**参考链接：**

https://www.cybersecurity-insiders.com/the-evolution-of-siem-where-its-been-and-where-it-is-going/

相关阅读

[告别孤立的安全告警！立刻升级SIEM的五大理由](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651112554&idx=1&sn=7b2d431fce73f929f523241bbdf0edf4&chksm=bd1474b98a63fdaf3e7fccb1afa154e85fcdb245668ae130c6da155b1457fa9d836ed226eb52&scene=21#wechat_redirect)

[每一个成功的SOAR背后，都有一个成熟的SIEM](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651090852&idx=1&sn=a17c5819349244033339f128a0f30de7&chksm=bd14df778a635661d3fc999d13f41b6303f3e5421199a139e67c612a5e0365217869f397b490&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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