---
title: 慢雾出品 | 2026 上半年区块链安全与反洗钱报告
url: https://mp.weixin.qq.com/s/dQmO0h0sWOiFQE1DXmn-Bw
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:02:02.318709
---

# 慢雾出品 | 2026 上半年区块链安全与反洗钱报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCKvg7OSTpyBKfjiaB5tOX484hqugqjo1bnhbYIWAU1rmUDOktUiaZJW2T5OXIQh7SSmy78ibp5khuBbapl8JjbAibicnAPyyhIjo2gg/0?wx_fmt=jpeg)

# 慢雾出品 | 2026 上半年区块链安全与反洗钱报告

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于慢雾科技
，作者慢雾安全团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4FqAumbguXteG2OtztBWwTZ6xLLfTaIQfRvzdJhLZkibQ/0)

**慢雾科技**
.

慢雾科技是一家专注区块链生态安全的公司，成立于 2018 年 1 月，主要通过“威胁发现到威胁防御一体化因地制宜的安全解决方案”服务了全球许多头部或知名的项目，已有商业客户上千家，客户分布在十几个主要国家与地区。

**![](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCLcfRKGvoKnGz4TribjKWoZk9KzVeQwhAGuopXKQXFybibyITf9bl3SxydReuT9reFcOW6x8uLpB0xVUYWewrTwhJ0mDwOGSmlwc/640?wx_fmt=jpeg)

**由于篇幅限制，本文仅罗列分析报告中的关键内容，完整内容可点击文末“阅读原文”获取下载。**

**## 一、概述

2026 年上半年，区块链行业在持续快速发展的同时，安全威胁与监管环境进一步演进，整体风险结构呈现系统化扩展趋势。随着 DeFi、跨链基础设施及 AI Agent 等应用加速落地，攻击面持续外延，安全风险已从智能合约扩展至开发者生态、供应链体系、终端交互环境及用户授权信任链路；同时，AI 技术的普及显著降低社会工程与自动化攻击门槛，推动攻击活动向专业化、规模化与持续化演进。

国家背景黑客组织与高对抗性攻击仍然活跃，Drainer 黑产服务、供应链投毒与 AI 驱动诈骗等攻击形态持续升级，呈现模块化与服务化特征。DeFi 协议、跨链桥及开发者生态仍是高频风险领域，权限滥用与供应链依赖问题持续引发损失，生态信任关系被系统性利用的趋势进一步加深。在监管方面，围绕稳定币、AML 与 VASP 的全球监管框架持续完善，合规要求加速收紧，监管体系正从单点执法转向系统化治理，链上追踪与资产冻结能力同步提升。

**作为区块链安全领域的先行者，慢雾(SlowMist) 始终紧跟技术前沿，在威胁情报、大模型 AI 安全、追踪溯源和合规反洗钱等基础设施建设上持续深耕。在此背景下，本报告聚焦 2026 年上半年的重大安全事件、全球监管演进以及链上反洗钱技术趋势进行分析。希望通过本报告，为行业从业者、安全研究人员及合规负责人提供及时、系统且具有前瞻性的参考，助力生态在强合规与高对抗的新环境下，全面提升对未知风险的识别、响应与预判能力。**

## 二、区块链安全态势

2026 年上半年，区块链行业依旧面临严峻的安全挑战。根据慢雾区块链被黑事件档案库(SlowMist Hacked) 不完全统计，上半年共发生安全事件 182 起，造成损失约 9.56 亿美元。相比 2025 上半年（121 起，损失约 23.73 亿美元），**事件数量同比增长约 50.41%，但整体损失金额同比下降约 59.72%。**

（注：本报告数据基于事件发生时的代币价格，由于币价波动、部分未公开事件以及普通用户的损失未纳入统计等因素，实际损失应高于统计结果。）

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJ9Ks90qXmG6V5MQBonBhlWykUro8akPUu5sJHb0LZGFI7D08mykENiaicticSYjxiaJIYn7ibLeicF8X1zvvia22zFLHiasA0CsbsL8VE/640?wx_fmt=png&from=appmsg)**

（https://hacked.slowmist.io/zh/statistics/?c=all&d=2026）

#### 安全事件概览

（1）按生态分布

* Ethereum 是受攻击最频繁的生态，相关损失约 1.34 亿美元；

* BSC 生态紧随其后，损失约 3,635 万美元；

* Arbitrum 位列第三，损失约 493 万美元。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCL7RDrr5zD2RdlUG5DbPKHeQAiarjibVLUF5nsoU1AUOKiaEXYQPkJoFBmEeM05TNfiaK1aVvlgDtSbZlVHQakBYoyBVS4qzjlicy4E/640?wx_fmt=png&from=appmsg)**

****（2）按项目类型****

* DeFi 项目仍是最常遭受攻击的领域：2026 上半年共发生 116 起 DeFi 类型的安全事件，约占上半年事件总数（182 起）的 63.74 %，损失约 4.9 亿美元。对比 2025 上半年（ 92 起，损失  4.7 亿美元）损失同比约 4.26  %。

* 跨链桥事件共发生 20 起，累计造成约 3.46 亿美元损失。其中最严重的一起为 Kelp DAO 事件，该事件因采用 LayerZero 跨链桥的单一验证节点（1-of-1 DVN）配置，被攻击者通过入侵 LayerZero RPC 基础设施并实施 DDoS 攻击，伪造跨链消息，单次损失约 2.92 亿美元，成为 2026 年上半年损失最大的安全事件。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIFfgN0PgySbJgUFkcfMa4z8omrBB4HO9JfnbrvvHL5JA79CZIibpv69ibwTPkFSs2sZku6pwicq1ia5wa0oymNoAYtL6KPePX5hKE/640?wx_fmt=png&from=appmsg)**

（3）按攻击原因

* 从事件数量来看，合约/逻辑漏洞仍是最主要的攻击方式，共发生 85 起；

* 其次是私钥/凭证泄漏，共 17 起；

* 供应链攻击位列第三，共 12 起。

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJS9sA5WK4GtiafRNvNCuotwevLibGEnj6HZ1iaC0D0qLoLVYkOIyXUjdxmQ2Lf8uX72kaVrB8RUlXJaP8QUn9x9SltGg7FLfxJ3A/640?wx_fmt=png&from=appmsg)******

**####

* 从损失金额来看，供应链攻击以约 2.98 亿美元的总损失位居首位，主要受 Kelp DAO 单笔约 2.92 亿美元损失事件影响；

* 合约/逻辑漏洞和私钥/凭证泄漏分别造成约 1.52 亿美元和 1.30 亿美元损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJueeDJiaGic38QxXMUY58dVsWDCYic6ictETwqIwWxuZOa8W7cOMO1GnPyicUEGYuNt0ECVqNaPt4ibMx5yYsdbNIUibFBpnB4gdW7RY/640?wx_fmt=png&from=appmsg)

**整体来看，2026 年上半年区块链安全威胁呈现出“事件分散化、损失集中化”的特点。虽然大多数安全事件仍源于合约/逻辑漏洞等传统攻击方式，但高额损失正越来越集中于基础设施、跨链系统及供应链等关键环节，表明攻击者正持续向更高价值、更高影响的目标转移。**

####**

**#### 攻击手法

以下为 2026 年上半年呈现出较高活跃度与代表性的攻击手法类型。

1. 钓鱼攻击

钓鱼攻击正在显著呈现“平台化伪装 + 多阶段交互 + 动态投毒”的演化趋势。攻击者更倾向于利用浏览器扩展、搜索引擎广告、邮件系统以及主流安全验证流程等高可信渠道作为攻击入口，通过借助平台自身的信任体系降低用户警觉性。

2. 社会工程攻击

**社会工程攻击已成为 Web3 用户资产面临的主要风险之一。这类攻击倾向于利用真实业务场景和用户信任，通过招聘面试、商务合作、社交互动等方式诱导目标主动完成危险操作。与此同时，生成式 AI 的普及进一步提升了攻击的真实性、针对性和规模化能力，个性化话术、深度伪造音视频以及定制化钓鱼内容不断降低用户识别难度，使攻击重心进一步从技术漏洞转向人与业务流程。**

3. 供应链投毒

**供应链投毒攻击在区块链及更广泛的开源生态中持续高发，攻击手法从简单的包名仿冒、账号劫持，演进为对开发者全链路信任关系的系统性利用。攻击者不再满足于入侵单一库或基础设施，而是将视野扩展至包管理生态、CI/CD 流水线、CDN 分发链路乃至 AI Agent 插件市场，通过投毒“被信任的软件组件”，实现对大量下游用户的间接攻击。这类攻击影响范围广、溯源困难，且极易与社会工程手段形成叠加。**

4. AI 驱动的攻击

********AI 技术已深度融入攻击链，显著提升攻击的自动化与隐蔽性。一方面，攻击者利用生成式 AI 强化钓鱼、社会工程与恶意代码投递，使深度伪造（Deepfake）、自动化话术生成与虚假内容传播更加逼真与规模化；另一方面，AI Agent 的普及使攻击面扩展至“认知—执行信任链”，攻击者可通过提示注入、记忆污染及工具权限滥用等方式，操控 Agent 执行非预期操作，进一步放大实际资产与系统风险。********

5. **密码学攻击**

**2026 年上半年，区块链安全威胁呈现出明显的分层演进特征。早期攻击多集中于智能合约业务逻辑漏洞或简单私钥泄露，而当前攻击者已将目光转向区块链底层信任根基——密码学原语与协议机制的工程实现层面。这些攻击往往利用数学细节、密钥生命周期管理、证明系统集成或多方计算方案中的细微偏差，实现精准、高效且难以发现的资金转移。本节将结合典型案例系统梳理密码学安全在跨链桥、钱包、保险库及隐私协议中的风险图谱。**

## 三、反洗钱态势

本节主要涉及全球监管动态、资金冻结 / 归还数据、网络犯罪组织与隐私协议**四个部分。**

#### 全球监管动态**

**####**

****2026 年上半年，全球虚拟资产监管持续深化，监管重点已由行业准入逐步延伸至稳定币、反洗钱(AML)、虚拟资产服务提供商(VASP)、跨境资金流动及风险治理等多个领域，整体呈现出“制度完善、规则细化、执法强化”的发展趋势。亚洲、欧洲、美洲及中东等主要司法辖区相继推进稳定币监管框架、完善 VASP 许可制度及 AML/CFT 合规要求，并进一步加强对跨境交易、资产托管、RWA、衍生品及隐私资产等重点领域的监管。本小节整理了 2026 上半年各国监管政策动态，具体条目可点击文末“阅读原文”获取。**

****资金冻结 / 归还数据****

*** 2026 上半年遭受攻击后仍能收回或冻结损失资金的事件共有 18 起。在这 18 起事件中，被盗资金总计约 3.89 亿美元，其中将近 1.18 亿美元被返还/冻结，占 2026 上半年总损失的 12.3 %。

* 此外，在慢雾 InMist Lab 威胁情报合作网络的大力支持下，2026 上半年慢雾(SlowMist) 协助客户、合作伙伴及公开被黑事件冻结/追回资金约 516 万美元。**

#### 网络犯罪组织

1. **Lazarus Group**

朝鲜国家背景黑客组织 Lazarus Group 持续活跃于全球加密货币攻击活动，在供应链渗透、社会工程、DeFi 协议攻击、跨链基础设施攻击及后续资金洗钱等方面均表现出高度专业化特征。其攻击已形成“入侵—盗窃—洗钱”的完整作战链路，并广泛利用隐私协议、跨链桥、DeFi 借贷及混币服务构建多层资金转移网络，持续提升攻击隐蔽性与资产追踪难度。本节将结合其典型洗钱模式及代表性安全事件，对 Lazarus Group 的攻击特点进行分析。

2. **Drainers**

2026 年上半年，Drainer-as-a-Service (DaaS) 黑产生态持续演进，在老牌 Drainer 服务退出后，新一代平台迅速完成迭代与替代，整体呈现出专业化、平台化和产业化的发展趋势。运营者通过提供成熟的钓鱼基础设施、恶意合约模板、多链支持及自动化部署工具，以联盟分成模式降低攻击门槛，推动钓鱼攻击规模化扩散。与此同时，Drainer 平台不断融合 AI 技术、多链兼容、自动化运营及反检测能力，使攻击链条更加成熟，进一步加大了 Web3 用户资产安全防护和链上风险治理的难度。本节将结合典型 DaaS 平台，对其运营模式与攻击特点进行分析。

隐私协议

近年来，隐私协议的发展已逐渐从单一混币模式演进为更加多元的隐私基础设施。一方面，以 Tornado Cash 为代表的经典混币协议仍保持较高活跃度；另一方面，Railgun 等协议将隐私能力延伸至 DeFi 交互与资产管理场景，而 Hinkal、Privacy Pools 等项目则进一步探索可验证隐私与选择性披露等机制，在保护用户隐私的同时兼顾合规需求。本节将对上半年主要隐私协议的资金流入情况进行统计分析，以观察当前链上隐私生态的发展趋势及其安全意义。

（注：统计数据基于 Dune Analytics Dashboard 及自建查询结果整理，相关链接见报告原文。）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJ6licbB5cLxFAbaN9WwicCdF13HJFJ9g6s2McBYNETYbaC8erfQFqcPrB5zSHZYWpibNjO65ZIwsUYKvKmhnyGlInk90XjfrPqaY/640?wx_fmt=png&from=appmsg)

*** 从资金规模来看，Tornado Cash 仍保持绝对领先地位，累计流入约 6.91 亿美元，约占全部统计资金的 71%；Railgun 累计流入约 2.22 亿美元，占比约 23%；Hinkal、Privacy Pools 与 zkBOB 合计约占 6%。

* 相比资金规模，更值得关注的是资金结构的变化。除 Tornado Cash 外，Railgun、Hinkal、Privacy Pools 等协议新增资金均以稳定币为主，其中 Railgun 稳定币流入占比接近 90%。这一趋势表明，隐私协议的使用场景正逐渐从传统匿名提现扩展至稳定币转账、链上资产管理及 DeFi 交互等更加多元化的应用。**

##**

**## 四、总结

回顾 2026 年上半年，区块链安全风险持续演进，攻击面进一步由智能合约扩展至开发者供应链、终端设备、浏览器扩展及 AI Agent 等更广泛的生态环节，攻击方式也更加智能化、持续化。与此同时，链上资金转移与洗钱活动依然活跃，全球监管体系围绕反洗钱(AML)、稳定币、虚拟资产服务提供商(VASP) 等重点领域持续完善，推动行业治理逐步由事后响应迈向风险预防与体系化建设。在技术创新与风险演进并行的背景下，提升区块链生态的整体安全能力，已成为行业长期健康发展的重要基础。

面对不断变化的安全挑战，慢雾始终坚持以技术创新推动安全能力建设，持续探索人工智能在威胁情报、链上追踪、风险分析及反洗钱等领域的深度应用。围绕 AI Agent 安全，慢雾构建了[“五层递进式数字堡垒”综合防护体系](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504418&idx=1&sn=5b2e03843a623b955d80e596b8c1ccae&scene=21#wechat_redirect)，并推出 [SlowMist Agent Security Skill](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504542&idx=1&sn=877bb46e71ffb4b97ef69748773ee304&scene=21#wechat_redirect)、[MistTrack Skills](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504357&idx=1&sn=c632f2459fe03685f87d2016f1d825ee&scene=21#wechat_redirect) 和 [MistEye Security Gate（安全前置闸门技能）](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504920&idx=1&sn=6452ec12fb825b3a0b91ca5be8f009d8&scene=21#wechat_redirect)等安全能力，助力开发者与企业提升 AI Agent 的安全韧性，积极应对提示词注入、供应链投毒等新型风险。

## 五、免责声明

本报告内容基于我们对区块链行业的理解、慢雾区块链被黑档案库 SlowMist Hacked 以及反洗钱追踪系统 MistTrack 的数据支持。但由于区块链的“匿名”特性，我们在此并不能保证所有数据的绝对准确性，也不能对其中的错误、疏漏或使用本报告引起的损失承担责任。同时，本报告不构成任何投资建议或其他分析的根据。本报告中若有疏漏和不足之处，欢迎大家批评指正。

完整报告可通过文末 **“阅读原文”** 下载，也可直接访问以下链接获取：

中文：https://drive.google.com/file/d/1zfngTKU3\_dr10QqXKsQNe1kMhHtfQ7J0/view

英文：****https://drive.google.com/file/d/15qFJu9X-mKXO98lG63LLll0PzywT9Xxw/view********

**往期回顾**

[慢雾出品 | 2025 区块链安全与反洗钱年度报告](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504119&idx=1&sn=9e6afef4262207a8da1f16a66368ced6&scene=21#wechat_redirect)

[慢雾出品 | 2025 年上半年区块链安全与反洗钱报告](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=22...