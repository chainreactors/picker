---
title: 针对多国政府官员的黑客攻击还在继续……
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535607&idx=3&sn=f572a98292351e1e82888575e4e5f251&chksm=fa93fd36cde474200fc0fad1d030127d95e09469597d984665921682130d2c4a10a359f80595&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-21
fetch_date: 2025-10-04T10:09:41.000098
---

# 针对多国政府官员的黑客攻击还在继续……

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOzYu3hBbP8xykccbm78Jpz0icfA1nmIRWMXeQgleGVJndibpgqCH2NRf2Q/0?wx_fmt=jpeg)

# 针对多国政府官员的黑客攻击还在继续……

网络安全应急技术国家工程中心

自2021年以来，被称为Winter Vivern的高级持续威胁与针对印度、立陶宛、斯洛伐克和梵蒂冈政府官员的活动有关。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QmbJGbR2j6zdbKBrA9Y253GfLPl2hrkazCgoibCTt3UEKEQDEAPUsQFLUdVrF0jb36VVAwficP99dAg01FjC79cQ/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

SentinelOne 在与黑客新闻分享的一份报告中称，该活动针对波兰政府机构、乌克兰外交部、意大利外交部以及印度政府内部的个人。

“特别令人感兴趣的是APT以私营企业为目标，包括在正在进行的战争中支持乌克兰的电信组织。”高级威胁研究员汤姆黑格尔说。

Winter Vivern，也被追踪为UAC-0114，上个月在乌克兰计算机应急响应小组(CERT-UA)详细介绍了针对乌克兰和波兰国家当局的新恶意软件活动后引起了人们的注意，该活动旨在传播一种名为 Aperetif 的恶意软件。

此前记录该组织的公开报告显示，它利用包含XLM宏的武器化Microsoft Excel文档在受感染主机上部署PowerShell植入程序。

虽然威胁行为者的来源尚不清楚，但攻击模式表明该集群符合支持白俄罗斯和俄罗斯政府利益的目标。

UAC-0114 采用了多种方法，从网络钓鱼网站到恶意文档，这些方法都是为目标组织量身定制的，以分发其自定义有效负载并获得对敏感系统的未授权访问。

在2022年，年中观察到的一批攻击中，Winter Vivern 设置了凭据网络钓鱼网页，以引诱印度政府合法电子邮件服务email.gov.in的用户。

典型的攻击链涉及使用伪装成病毒扫描程序的批处理脚本来触发 Aperetif 木马从参与者控制的基础设施（例如受感染的WordPress站点）的部署。

Aperetif 是一种基于 Visual C++ 的恶意软件，具有收集受害者数据、维护后门访问以及从命令和控制 (C2) 服务器检索额外有效载荷的功能。

“Winter Vivern APT 是一个资源有限但极富创造力的组织，他们在攻击范围内表现出克制，”黑格尔说，“他们引诱目标参与攻击的能力，以及他们以政府和高价值私营企业为目标，都表明了他们行动的复杂程度和战略意图。”

虽然 Winter Vivern 可能已经成功地在很长一段时间内避开了公众的视线，但一个不太担心保持低调的组织是 Nobelium，它与 APT29（又名 BlueBravo、Cozy Bear 或 The Dukes）有重叠。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6zdbKBrA9Y253GfLPl2hrkaY7ia9EGSGat0CGwCcibl8ptDM7O6qutSskAiauh3ZV7B7g6Ivcw65Eibtg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

因2020年12月的SolarWinds供应链妥协而臭名昭著的克里姆林宫支持的民族国家组织继续发展其工具集，开发新的自定义恶意软件，如MagicWeb和GraphicalNeutrino。

这也归因于另一场针对欧盟外交实体的网络钓鱼活动，特别强调“帮助乌克兰公民逃离该国并向乌克兰政府提供帮助”的机构。

“Nobelium 积极收集有关在俄乌战争中支持乌克兰的国家的情报信息，”黑莓表示。“威胁行为者会仔细跟踪地缘政治事件，并利用它们来增加成功感染的可能性。”

该公司的研究和情报团队发现的网络钓鱼电子邮件包含一个武器化文档，其中包含一个指向HTML文件的链接。

这些武器化的URL托管在位于萨尔瓦多的合法在线图书馆网站上，具有与LegisWrite和eTrustEx相关的诱饵，欧盟国家使用这两者进行安全文件交换。

活动中提供的HTML投放程序（称为ROOTSAW或EnvyScout）嵌入了一个ISO映像，而该映像又旨在启动一个恶意动态链接库 (DLL)，该库有助于通过Notion的API传送下一阶段的恶意软件。

Recorded Future 曾于2023年1月披露了流行的笔记应用程序 Notion 用于C2通信的情况。值得注意的是，APT29使用了Dropbox、Google Drive、Firebase和Trello等各种在线服务，试图逃避检测。

“Nobelium 仍然非常活跃，同时针对美国、欧洲和中亚的政府组织、非政府组织(NGO)、政府间组织(IGO)和智库开展多项活动.”微软上个月表示。

调查结果发布之际，企业安全公司 Proofpoint 披露了自2021年初以来与俄罗斯结盟的威胁行为者TA499（又名Lexus和Vovan）策划的攻击性电子邮件活动，以诱骗目标参与录制的电话或视频聊天并提取有价值的信息。

该公司表示：“威胁行为者一直在从事稳定的活动，并将其目标扩大到包括为乌克兰人道主义工作提供大笔捐款或公开声明俄罗斯虚假信息和宣传的知名商人和知名人士。”

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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