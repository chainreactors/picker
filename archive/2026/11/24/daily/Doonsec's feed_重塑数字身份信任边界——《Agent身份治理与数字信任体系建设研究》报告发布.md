---
title: 重塑数字身份信任边界——《Agent身份治理与数字信任体系建设研究》报告发布
url: https://mp.weixin.qq.com/s/18tn-cB5H9XafvFjayGCLA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:46:29.903229
---

# 重塑数字身份信任边界——《Agent身份治理与数字信任体系建设研究》报告发布

# 重塑数字身份信任边界——《Agent身份治理与数字信任体系建设研究》报告发布

原创

徐晓丽
徐晓丽

安全牛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字 关注我们**

随着人工智能技术从内容生成、信息问答向自主规划、工具调用和协同执行演进，AI Agent逐步从辅助人类的智能工具转变为能够参与业务流程、访问数字资源并执行具体操作的新型数字主体。

当Agent开始以数字身份参与业务活动，身份就不再只是访问控制的起点，更成为约束其行为、建立信任和明确责任的关键基础。

传统以人为中心、以静态授权为主的身份治理模式，开始面临新的挑战。如何识别和管理规模化增长的Agent身份，如何约束权限继承与动态委托，如何控制自主执行过程中的安全风险，以及如何建立跨主体、跨平台的数字信任机制，正在成为企业数字化与智能化转型过程中亟待解决的重要问题。

在此背景下，安全牛正式发布《Agent身份治理与数字信任体系建设研究》报告，围绕AI Agent带来的数字身份体系变革，系统研究Agent身份安全风险、政策标准、治理框架、实施路径与产业发展趋势，系统探讨AI Agent时代的身份治理新模式。

【扫码获取报告抢鲜阅读】

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzESZUl0C3o3UkIicu9SQv17icXcZkdFmMHXQ296CSHo9sxfkNSluETyJGarDfORBQ1rYAXyocuAF3Zu54Lk6SOZEDevosWdyBicQo/640?wx_fmt=png&from=appmsg)

总体包括以下七个章节内容：

▪　第一章：AI Agent数字身份体系变革与失控风险

▪　第二章：Agent身份治理政策及标准化现状

▪　第三章：Agent身份风险与治理挑战分析

▪　第四章：Agent身份治理与信任体系框架

▪　第五章：Agent身份治理实施路径与落地建议

▪　第六章：Agent身份治理产业格局与代表性厂商技术路线

▪　第七章：未来发展趋势总结

**一、报告关键发现**

**Agent数字身份：**Agent身份是一组包含身份标识、属性、关联关系、归属关系、授权关系、代理关系的复合型身份信息。

**风险****特征****：**由于Agent具备一定的自主决策与执行能力，任一单点风险都可能沿执行链条传导、放大，进而引发系统性安全事件。呈现围绕“身份—权限—行为—责任”相互关联、动态演化的风险特征。

**治理现状：**全球正从人工智能治理、数字身份、非人身份（NHI）及智能体专项规范等多个方向推进 AI Agent 风险治理。美国、欧盟、新加坡和中国等国家和地区已开展相关政策制定与标准探索，逐步将治理要求延伸至 Agent 身份认证、权限控制、行为监督和责任追溯等关键环节。

**关键技术：**身份治理应以身份数据可信为基础，以权限可管、行为可控、责任可溯为关键目标。包括：身份数据治理与可信认证、零信任动态授权与权限传递约束、Agent行为监测与运行时防护、全链路审计与可信追溯、跨域身份互信与隐私保护五大关键技术。

**竞争****格局：**不同厂商围绕Agent身份安全形成互补与交叉竞争，竞争焦点正在向身份统一化、权限动态化、行为可控化三个层面深化。市场参与者以传统IAM/IGA厂商、PAM/NHI厂商、网络安全厂商以及AI应用/平台类厂商为主。

**未来趋势：**Agent身份治理正成为传统身份安全与AI安全融合的重要领域。短期内，市场仍将呈现多类厂商依托既有优势拓展能力的竞争格局；中长期看，具备身份治理、机器身份与凭证安全、运行时控制及跨平台协同等综合能力的厂商，将更具竞争优势。

**二、Agent驱动的数字身份变革与失控风险**

随着企业数字化、云化和智能化程度不断提高，参与数字业务活动的主体已经不再局限于自然人，而是逐步扩展至设备、应用程序、服务、工作负载、Agent及各类自动化实体。从演进关系看，行业通常将其划分为：Human Identity、NHI和Agent Identity三个发展阶段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzFRVFjd08JD1QqgndcMXedngIccTFxC5tRULE33Rs6C2HgkHOS2LxbzJhjPQohuRy1ic7PLYuD39Vxa22dGbKTcNYOysib3kMId8/640?wx_fmt=png&from=appmsg)

**其中，****Agent****数字****身份（Agent Identity）****是****AI Agent在数字环境中用于唯一识别其主体、描述其身份属性与归属关系、表征其代理及授权关系，并支撑身份认证、权限控制、信任验证、行为审计与责任追溯的一组数字化身份信息。**

其本质仍属于广义NHI（非人类身份）的范畴。但与传统服务账号、自动化程序最大的区别，在于其具有一定的自主决策和动态执行能力。因此，Agent身份还需要更加完整的身份属性，包括：**独立****标识、****组织归属****、****代理关系****、****任务授权****、****行为审计**。

其特征典型表现为：**主体多元性、行为自主性、****委托代理性****、****权限动态性****、****协作跨域性****、****存续动态化****以及****责任关联性****等多个维度**。这些特征也反映了数字身份治理对象、授权关系和信任机制的进一步演进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzFEeeN5lNn8Unsm8iatgSqTDK9V2WTupRuPd8XTQyhtDf9LkRicll2zknhfoYZLmAiaKZpysMvkoakMJKiadDnNCfBlRdjMO8Lvrb0/640?wx_fmt=png&from=appmsg)

随着AI Agent逐步融入企业数字环境，身份主体及关联凭证规模进一步扩大，风险触发机制也从传统的凭证失陷和异常访问，延伸至自主决策与任务执行过程。受自主行动、多级委托授权和跨主体协作等特征影响，数字身份风险在既有风险基础上，进一步演变为与自主行动、动态授权和跨主体协作紧密关联的复合型风险，呈现出**风险****规模持续扩张、风险触发更加自主、权限放大与风险传导链式****化****、影响范围进一步扩大**等变化。

2026年以来，一系列Agent身份安全相关典型事件正在驱动国际安全组织、第三方咨询机构和产业研究机构围绕AI Agent安全风险展开系统研究。普遍指出：**Agent身份缺失、权限边界不清、凭证管理薄弱以及自主行为缺乏可追踪性，正在成为Agent安全治理的关键问题。**

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzF20SBhdKYRjpRtnJUR3lGFzAxal22NLLoHDOzicIwPFkic2DbDyQehlKGyVAvOl3JzuoBKVaOeIRZwKwYGnPuhTmAAWF1h3Vz7w/640?wx_fmt=png&from=appmsg)

与此同时，产业也开始加速Agent身份治理实践：头部厂商开始发布AI Agent身份管理产品，RSAC将Agent Identity列为2026年网络安全产业的重点议题，开源社区和协议标准化探索也开始向Agent身份的密码学证明和跨主体信任延伸。

**三、Agent身份动态风险模型与治理挑战**

由于Agent自主决策、动态执行和多主体协作等特点，Agent身份的安全风险更为复杂。已经明显超出传统NHI身份“账号泄露、凭证盗用”的范畴。传统IAM、IGA、PAM和NHI等管理体系在主体识别、权限控制、运行时管理和责任追溯等方面面临了更多挑战。

典型的六大挑战分别是：身份对象不统一、身份归属不清、权限动态变化、执行过程不透明、信任边界扩大、行为责任难追溯。

在风险分析层面，**安全牛认为：****由于Agent具备一定的自主决策与执行能力****，任一单点风险都可能****沿执行链条传导、放大，进而引发系统性安全事件****。****其身份风险并非仅表现为传统数字身份与账号层面的孤立风险，而是****会****呈现围绕****“****身份—权限—行为—责任****”****相互关联、动态演化的风险特征。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzGUQticXvfYS7r7zcq2w8Ikak2GZZbeZcFoqA1dvcyIwdCXpm388ictL4sDDcJg6lNItibBItcOk6pEBibFkKa88ibiadACV9SSPkRF0/640?wx_fmt=png&from=appmsg)

从上述模型来看，Agent身份风险重点集中在**身份真实性、权限与授权、行为与责任**三个方面，贯穿身份建立、权限配置、任务执行及协同交互等关键环节。

**基于风险分析，安全牛认为：****AI Agent身份治理面临的核心挑战，集中体现为身份主体多元化、权限控制动态化、协作关系复杂化、生命周期持续演化、行为追溯链条不完整以及跨平台信任机制不完善六个方面。**

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzEPENSkjIJkwZNP54lcZSejeiaKl7nia4vebLCpNf4cicybkfDvGI3ezaXJjefzAibn8dqm3Fox1EuNAoE6tGSMletoNVIcDwZuPEw/640?wx_fmt=png&from=appmsg)

这也集中反映出传统IAM以人类用户为核心的身份治理模式，在应对自主智能体、多主体协作及动态权限管理等新需求时存在的局限性。进入AI时代，身份治理的对象、授权逻辑与责任追溯机制均在发生变化，传统IAM需要从**身份管理对象****、****权限治理逻辑****、****信任与责任机制**三个方面实现关键转变。

**四、Agent身份治理核心目标与体系框架**

Agent环境下，身份可信不等于行为可信，身份认证成功也不意味着后续操作天然获得授权。Agent身份治理的关键，在于将身份、权限、行为、信任和责任纳入统一治理链路，使信任判断能够转化为具体的授权决策和运行时控制措施。

**安全牛认为，Agent身份治理的核心****目标****是实现Agent身份可信、权限可控、行为可管、责任可溯****。**治理原则上，需要**以数字身份为基础，以身份属性为依据，以持续信任评估为核心，以动态授权为手段**，推动Agent身份治理从传统的静态身份认证与访问管理，向自主执行、动态委托和跨域协作的数字信任治理演进。

在体系架构层面，面向AI Agent的数字信任体系，**应****以统一身份治理为基础、以数字信任****机制****为支撑、以动态授权为核心、以全链路审计为保障，建立贯穿Agent身份创建、认证、委托、授权、运行和退出的全生命周期治理机制。**将人员、设备、应用、服务、机器及AI Agent等多元主体纳入统一治理框架，打通身份数据、认证凭证、权限关系、行为风险与审计记录之间的关联。

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzEk8CbdT8rItV2nibGT0Dz0HampkK0PB8q7NajRKiaklHPwnLftRwqibrWAmKBevS11jHxIpBM7lf3gyJMJjTDoU1a2RtpteJah38/640?wx_fmt=png&from=appmsg)

在关键技术方面，身份数据治理与可信认证技术、零信任动态授权与委托权限约束技术、Agent身份行为监测与运行时安全控制技术、全链路审计与可信追溯技术以及跨域身份互信与隐私保护，五类技术协同共同构成Agent身份治理与数字信任体系的关键技术支撑。

**五、Agent身份治理评估模型与建设建议**

尽管报告提出了AI Agent身份治理的总体架构，但要将架构转化为可执行、可验证、可持续运营的治理能力，还需要结合企业现有IAM、特权访问管理（PAM）、云安全、API安全和安全运营体系，明确建设优先级、实施步骤、技术改造路径及合规要求。

为有效量化Agent身份治理水平或能力建设水平，报告按身份与数据治理、认证与信任、权限与委托、运行时防护、审计与责任、跨域协同六个维度，将Agent身份治理成熟度划分为L1-L5五个等级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzEOtrTkG6Lp0FGek0BbI0HaMjzq8P7kGSKul8zghT98JKVKYswpHOvLnX2A7q6iaF3NgHPdjak9NG0htv5GT0ibviaENyGwLws4gs/640?wx_fmt=png&from=appmsg)

实际建设中，成熟度提升不宜简单理解为采购更多安全产品，而应结合Agent应用规模、业务风险和现有身份安全基础，分阶段推进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzEyiaoWVPuMe6teZKcb3J9UbM8VHE1djibic76PPCw0ayq9ozFBeDrp0d7LkueDoXn9IQ4svZiatPiakF2QsNXz1ohqgSzzSto4bcf8/640?wx_fmt=png&from=appmsg)

**六、产业格局与代表性厂商实践**

数字身份市场自2020年起，受零信任架构普及、云服务渗透加速以及AI技术迭代升级等多重因素影响，市场格局始终处于动态演化与整合之中，尤其是以美国为主的国际市场。

综合国内外产业发展来看，当前Agent身份治理尚处于技术体系形成和产业实践探索阶段，整体呈现出以现有数字身份体系为基础、以非人类身份（NHI）治理为切入点、以动态授权和运行时控制为重点、以跨域互信和全生命周期治理为发展方向的演进特征。

**国际方面，**报告以Microsoft、Palo Alto、Okta、Palantir为代表梳理了国外厂商的Agent身份治理技术路线。尽管这些厂商不能代表国外Agent身份治理的整体情况，但作为赛道标杆，其产品落地思路与架构设计具备较强的参考价值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzGsWkbZSb4XUVtp5ZxJmeGZ2avBU38iclAhyVzefdLlPzxVF4oicFicrpxzdXCzLS8o0ewKpnF0JP6qIZbnXUfn4Qg7xXL70AXVZU/640?wx_fmt=png&from=appmsg)

其中，Palantir将运行时权限与Ontology资源和操作结合，以统一业务平台为治理载体，将Agent身份、业务权限和实际执行过程关联起来。

**国内方面，**基于访谈，报告汇集了国内十家厂商的访谈及方案资料。覆盖IAM、PAM、密码、零信任及综合安全等路线。整体来看，国内Agent身份安全产业初步形成以“身份治理为基础、机器身份与凭证安全为支撑、运行时访问控制为关键、零信任与审计运营为保障”的能力格局。这些代表性厂商分别是：**格尔软件、竹云科技、芯盾时代、绿盟科技、保旺达、宁盾科技、领信数科、能睿科技、安讯奔、建恒信安**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzHUzEbo5womWibrP8MWBj0lcbjFUCv4TiaPEhSCBbeYTZ3syH8fX0jsrElgMqoLUzg3BevpycI45XaNYtTdUSiak1mciat9NyurNSo/640?wx_fmt=png&from=appmsg)

其中，格尔软件**主张基于密码学建立****身份信任体系，以智能体安全平台实现Agent全生命周期管理，同时结合多网关实现智能体行为控制。**其方案“以可信智能体平台与AI安全产品支撑企业智能化应用”在本次报告中具有较好的代表性。

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzHDy0DyUVicePpsYReSricuDO8YWdHEdv333FaCY3qUBWOVJAFAvMesrwUicMib4wsQYiaQBmeXhgeHq7qldGj1B8RthmvjX0ZdHDvA/640?wx_fmt=png&from=appmsg)

相比通过扩展Agent账号管理能力实现身份治理的技术路径，其突出特点在于将身份治理、信任传递和业务执行控制进行一体化设计。方案更加突出数字身份、密码信任与Agent运行时安全控制的深度融合。同时，兼容证书、Token、DID/VC及联邦认证等多种身份与信任机制。该方案，一方面，可以为企业在既有身份管理和安全基础设施上逐步引入Agent身份治理能力提供了可行性支撑；另一方面，场景上既能覆盖自研Agent、第三方Agent以及多智能体协作等典型场景，也能为未来具身智能实体身份管理提供统一身份底座。

**七、未来发展趋势**

结合相关研究，安全牛认为Agent身份治理将会在市场和技术方面将呈现以下发展趋势。

**（一）从市场趋势看：****Agent身份治理正成为传统身份安全与AI安全融合的重要领域。**短期内，市场将延续多类厂商依托既有优势拓展能力边界的竞争格局；中长期看，能够兼顾企业级身份治理、机器身份与凭证安全、Agent运行时控制以及跨平台协同能力的厂商，更有机会在复杂企业场景中建立差异化竞争优势。

**（二）****从技术演进来看， Agent身份治理正在形成身份主体独立化、权限管理动态化、安全边界运行时化、信任验证持续化、治理体系全生命周期化****五个相互关联的发展趋势。**

Agent身份治理的技术演进，本质上是将传统以用户身份和资源访问为中心的安全管理模式，逐步转变为以Agent数字主体为核心，覆盖身份归属、权限委托、行为执行、持续信任和责任追溯的综合治理模式。其最终目标是实现Agent身份可识别、权限可约束、行为可监测、信任可验证、责任可追溯。

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzESZUl0C3o3UkIicu9SQv17icXcZkdFmMHXQ296CSHo9sxfkNSluETyJGarDfORBQ1rYAXyocuAF3Zu54Lk6SOZEDevosWdyBicQo/640?wx_fmt=png&from=appmsg)

【扫码获取报告抢鲜阅读】

**相关阅读**

[从虚假开户到跨平台套现：拆解合成身份欺诈的完整攻击链与防御策略](https://mp.weixin.qq.com/s?__biz=MjM5Njc...