---
title: 【NDSS 2022 论文分享】基于无线网流量指纹分析的APP行为隔空识别
url: https://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312701&idx=1&sn=d1439a37bbef1c524b11812da22a9a9c&chksm=8bc489f3bcb300e5540ba2db1581b3ee3cd158ae78b9820d5824d21b022cb5f464ff9e32daad&scene=58&subscene=0#rd
source: 网安国际
date: 2023-03-21
fetch_date: 2025-10-04T10:09:49.537296
---

# 【NDSS 2022 论文分享】基于无线网流量指纹分析的APP行为隔空识别

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSUicxIxviayyVkn1M8Rnuku3siczC40l8LJkP8qTFJEuR5mboVawEowkEBibrjWiae5bvCZ1icjZdPM98Tg/0?wx_fmt=jpeg)

# 【NDSS 2022 论文分享】基于无线网流量指纹分析的APP行为隔空识别

原创

李剑锋

网安国际

**前言**

本文根据英文原文“Packet-Level Open-World App Fingerprinting on Wireless Traffic.”整理撰写。原文发表在Network and Distributed Systems Security (NDSS) Symposium 2022. 作者在完成英文原文工作时，为香港理工大学博士后。本文较原文有所删减，详细内容可参考原文。

01

**介绍**

智能手机、平板电脑等移动设备在现代生活中无处不在。从信息检索到即时通讯，从购物到娱乐，无数的移动APP赋予了这些设备深刻重塑人们生活方式的能力。最近流行的O2O平台APP（例如：食品配送）通过弥合在线信息和实体企业之间的鸿沟进一步加深了这一趋势。

事物都具有两面性。APP为用户提供优质服务的同时，也伴随着用户数据的收集、传输、存储甚至共享，引发严重的隐私问题。例如，被黑客攻陷的云服务器可能导致灾难性的隐私泄露。这类攻击基本上都是由于软件缺陷造成的。尽管威胁巨大，但这些缺陷是稀缺的，一旦发现，将立即被修复，以避免严重后果。数据传输通道是另一个脆弱点。尽管加密通信被广泛采用，移动应用仍然容易受到APP指纹( AF ）攻击。攻击者识别与目标APP相关的用户活动来推断用户隐私。这样的威胁已经日益加重。首先，智能家居等APP化物联网系统迅速普及，将网络空间攻击扩展到物理世界。因此，泄露敏感信息（例如：用户动态和已安装的带有安全缺陷的物联网设备）不仅可能危及用户的隐私安全，也可能危及用户的物理安全。其次，COVID - 19疫情前所未有地影响了个人的生活习惯。人们经历了封控，不得不习惯于在网上做一切事。从虚拟会议到在线教育，潜在地扩大了AF攻击的攻击面。

现有的AF攻击一般通过在无线接入点（AP）捕获TCP / IP流量来进行。不幸的是，它们的实用性受到限制。这是因为攻击者需要攻陷无线AP或与网络管理员合谋才能获得捕获TCP / IP流量的权限。相反，WiFi嗅探器可以使攻击者隔空（over the air）被动地捕获移动设备和无线AP之间的802.11无线帧而不被察觉。通过利用WiFi嗅探器，攻击者无需要控制无线AP，也不需要网络管理员授予的权限，从而降低了AF攻击的门槛。例如，攻击者可以在门外发起AF攻击，并识别与各种APP(如智能家居APP）相关的用户活动，以推断室内的人员动态，用于侦察目的。然而，现有的AF攻击在应用于无线流量时会受到四重挑战的阻碍，无法完全解决这些挑战。

■ 目的地址隐藏:由于网络层、传输层和应用层数据加密封装在802.11无线帧的帧体中，原始的目的地址信息，如远程服务器的IP地址和域名将被隐藏。因此，利用目标地址信息的AF攻击不适用于802.11无线帧。

■ 样本边界不可见:由于802.11无线帧中的传输层端口是不可见的，无法识别和提取移动流量的TCP / UDP网络流。因此，需要提取网络流作为流量样本的AF攻击无法处理802.11无线帧。在网站指纹( WF )攻击中广泛使用的另一种解决方案是将流量样本提取为由数据包之间明显的时间间隔分隔的加密流量片段。遗憾的是，这样的方案很难被AF攻击所借鉴，因为应用流量要复杂得多，很难找到合适的时间间隔阈值来分离不同APP产生的流量。

■ APP并发：由于移动用户在实际中可能同时使用不同的APP，不同APP生成的数据包可能会强烈地混合在一起。例如，用户使用Flipboard阅读新闻，同时使用Apple Music听音乐。如果攻击者想要分析与Flipboard相关的用户活动，那么Apple Music产生的数据包自然会成为可能影响识别准确率的噪声。自Android 7以来，情况变得更加糟糕，因为两个APP可以通过分割屏幕同时位于前台。由于802.11无线帧在加密帧体中隐藏了网络层和传输层端口，不同APP产生的数据包无法被分组到不同的网络流中进行进一步识别。现有的AF攻击都无法处理APP并发。

■ 开放世界识别：现有的大多数AF攻击在封闭世界假设下工作。也就是说，识别阶段呈现的APP也必须在模型训练时呈现。否则，当面对一个在模型训练中未见的APP时，就会被错误地归类为已知APP。在实际应用中，由于Android和iOS都拥有超过370万个应用，因此无法枚举所有APP并收集其流量用于模型训练。一个可能的改进是进行开放世界识别，并为每个APP训练一个一对一的二分类器。开放世界识别能够处理在模型训练过程中未见的APP，因为它们将被分类为每个分类器的负类，而不是已知的APP。然而，开放世界的识别是一项有难度的任务。一方面，攻击者需要尽可能多的APP来收集其流量作为负样本进行模型训练。另一方面，越多的APP作为负类又会导致更严重的样本不平衡。

本工作提出了一种新的AF攻击，名为PACKETPRINT，通过解决上述挑战来识别与目标APP相关的用户活动。首先，PACKETPRINT从数据包大小和数据包方向而不是目的地址信息中提取特征，从而免疫于目的地隐藏。其次，本工作利用数据包大小的短时序列模式来实现流量分割。因此，PACKETPRINT不依赖于可见边界来分割不同应用产生的无线流量，能够自动定位目标APP产生数据包的所有可能时间段。第三，PACKETPRINT通过利用数据包到达的结构模式来识别APP流量，进行标签感知的特征映射，以提取与APP相关的结构模式，同时自适应地忽略与之无关的结构模式。这样，PACKETPRINT实现了抗噪声并且解决了APP并行问题。最后，PACKETPRINT利用数据包到达的可区分性特征进行开放世界识别，该特征综合了不同时间尺度的结构模式，捕获了长时间的上下文信息。本工作的主要贡献如下：

■ PACKETPRINT是首个能够处理开放世界环境中的未分段加密流量且能应对APP并发的AF攻击。本工作在设计中解决了多个具有挑战性的问题，包括目的地址隐藏、样本边界不可见、APP并行和开放世界识别。为了解决这些技术挑战，本工作提出了两种新的模型，即序列XGBoost ( S-XGBoost )和层次化词袋模型( H-BoW )。

■ 本工作实现了PACKETPRINT原型，并通过大量实验对其进行了评估。实验结果表明，PACKETPRINT性能始终优于基线方法。对于开放世界应用识别，平均F1值为0.884，对于APP内用户行为识别，平均F1值为0.959。此外，PACKETPRINT具有良好的迁移能力，能够进行跨数据集识别。

02

**方法概述**

**1.威胁模型**

本工作中考虑的攻击者使用WiFi嗅探器捕获加密流量。他的目标是从无线加密流量中识别与目标APP相关的用户活动。根据训练数据集，识别的可以是粗颗粒的信息（即用户在用哪些APP）或细粒的信息（例如，用户如何与这些APP交互）。

本工作假设攻击者基于帧头中提取的源/目标MAC地址，可以将802.11无线帧划归到不同的移动设备。但是，他无法获取IP报头的源/目的地地址、传输层分组的源/目标端口，以及应用层分组的明文负载，因为这些信息被加密封装在802.11无线帧中。

此外，与大多数WF攻击不同，本工作不认为由不同APP生成的数据包可以根据数据包的时间间隔被合理地分割为不同样本。这是因为不同APP和后台服务产生的数据包可能混合在一起。本工作也不假设一次只有一个APP在运行，这是因为移动用户可能同时使用不同的APP。最后，本工作考虑开放世界设定下的AF攻击。因此，所提方法需要应对训练阶段未知的APP。

**2.PACKETPRINT工作流程**

不失一般地，本工作假设目标APP为A。为从无线加密流量中识别与A相关的用户活动，PACKETPRINT将解决四大挑战，包括C1：目标地址隐藏、C2：样本边界不可见、C3: APP并行以及C4：开放世界识别。图1展示了PACKETPRINT的总体工作流程。

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSUicxIxviayyVkn1M8Rnuku3sTdRYCN1X1CSvr1rpbWmU9eSD2NucqYPy2XsWgKfIz3GTUb0sR4s8Eg/640?wx_fmt=png)

**图1：PACKETPRINT框架结构**

■ 流量预处理：使用WiFi嗅探器对加密的无线流量进行捕获。PACKETPRINT由于仅提取数据包大小和数据包方向特征，而无需获取目标地址，从而绕过了挑战C1。为便于后续分析，PACKETPRINT首先通过协议过滤、数据包大小归一化和数据包大小过滤对无线流量进行预处理。协议过滤旨在过滤掉管理类型和控制类型帧，只留下数据类型帧供进一步分析，因为应用层数据只封装在数据类型帧中。数据包大小归一化旨在将802.11帧大小转化为TCP/IP数据包大小。数据包大小过滤的目的是为每个目标APP构建一个数据包大小（同时考虑数据包大小和数据包方向）列表，以滤除频繁出现在其他APP流量中的数据包大小。这将带来双重好处：1）需要分析的数据包数量显著减少，2）减少了挑战C3带来的交错噪声。

■ 流量分割：PACKETPRINT既不依赖传输层端到端信息也不依赖数据包时间间隔来解决挑战C2，因为这些信息在加密的无线流量中不可用。相反，PACKETPRINT通过自适应地定位由目标APP生成数据包的所有可能的时间段来实现样本分割。本工作将目标APP可能出现时间段称为目标段。为此，本工作提出了一种新的指标，即序列相似性（S-similarity）来描述数据包由目标APP产生的可能性，并提出序列XGBoost（S-XGBoost）来计算数据包与目标APP的S-similarity。具有较高S-similarity的数据包被称为锚点数据包。与其他时段相比，锚点数据包将密集分布在目标段内。因此，本工作通过锚点聚类来定位目标段。

■ 流量识别：在开放世界设定下，若仅基于S-similarity进行流量识别易于产生假阳性，因为某些目标段中的数据包或许不是目标APP产生的。换言之，前一步骤中包含的某些目标片段可能与A无关。因此，PACKETPRINT将识别与A相关的所有目标片段。为此，本工作提出了另一种新的指标，即成分相似性（C-similarity），从结构特征的角度来量化目标段内的数据包是否是目标APP生成。最终，若某目标片段的C-similarity大于预设阈值，则认定目标APP确实在该片段内运行。为了计算C-similarity，本工作利用层次结构词袋（H-BoW）模型来提取不同时间尺度上易于识别的结构特征。H-BoW通过特征映射将小时间尺度的结构模式压缩映射为大时间尺度的单词。通过分层特征映射获得“单词”后，本工作利用组合优化，用这些“单词”有效地表示语义特征，然后训练具有概率输出的分类器，以计算目标片段与目标片段与A的C-similarity。H-BoW有两大优势：首先，特征映射通过监督学习方式构建，因此能自动忽略与A无关的结构模式。这样一来，H-BoW能够噪声容忍，从而克服挑战C3。其次，H-BoW由于整合了不同时间尺度的结构特征，能够生成具有分辨力的目标APP流量表示，从而有效降低假阳性风险以应对挑战C4。

除了APP识别之外，PACKETPRINT还可以识别更细粒度的应用内用户操作。为此，PACKETPRINT需要收集由这些用户操作生成的无线流量，然后为每个用户操作构建独立的S-XGBoost模型及H-BoW模型。在识别阶段，PACKETPRINT首先识别并定位对目标APP所在的目标流量片段，再从这些流量段中进一步独立识别该APP的细粒度用户操作。

*（本文只选取原文中部分章节，更多精彩内容敬请期待后续出版的《网络安全研究进展》）*

**作者简介**

李剑锋博士目前是西安交通大学助理教授。他于2018年3月从西安交通大学控制科学与工程专业获得博士学位。随后，分别在新加坡南洋理工大学和香港理工大学从事博士后研究工作。其研究兴趣集中在网络安全、流量分析和网络监控等方向，已在USENIX Security, NDSS, S&P, CCS, INFOCOM, TON, TIFS和Information Sciences等高水平国际会议和期刊上发表论文25篇，申请授权国家发明专利18项、软件著作权3项。

**相关阅读**

[【S&P 2022论文分享】移动博彩诈骗的数据分析](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312680&idx=1&sn=bf14db7f4985fedc996f4cac62337707&chksm=8bc489e6bcb300f02e44dbb4404bc70b3f103bd57a130b238ef30cb418f1b0eb4d476e1b023c&scene=21#wechat_redirect)

[【USENIX Security  2022论文分享】揭示垂直联邦学习中存在的标签推断攻击](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312275&idx=1&sn=f453438c42b5676b01f01acbe495e28d&chksm=8bc48f5dbcb3064b23fbb8a9246394716afd7917e37199d4f21da340745defd2db404efc7d21&scene=21#wechat_redirect)

[【DSN 2022论文分享】Invoke-Deobfuscation: 基于AST和语义保持的PowerShell脚本反混淆](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312255&idx=1&sn=260c8da492bfa3b4867c41be6d37909d&chksm=8bc48f31bcb306275802f97a29880f761de59c02ecd1cdccc4e627c4f638e02ee2bb1574da3a&scene=21#wechat_redirect)

[【NDSS 2022论文分享】Android系统跨上下文不一致的访问控制](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312223&idx=1&sn=13723e1612b7fefd42f1b4a86ddd0e1a&chksm=8bc48f11bcb30607911066fd8422191796d34cd127189df5e4b0fcf51678fd5c5aba33c0644e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSUicxIxviayyVkn1M8Rnuku3sLW8KYlcicWaTnkG8GXhGkLJUhF5emG4ichLNBkXzDqwcEMXwCPjMmGUA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSUicxIxviayyVkn1M8Rnuku3sHsLLNibgRmeibp5dZocMD63c90sjYysiaxCicoPyh8quHVnN4sFmjib9JTw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

网安国际

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

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