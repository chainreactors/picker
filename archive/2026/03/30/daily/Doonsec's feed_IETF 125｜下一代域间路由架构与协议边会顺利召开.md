---
title: IETF 125｜下一代域间路由架构与协议边会顺利召开
url: https://mp.weixin.qq.com/s/e-E1xM9KNBCD2YrfG1FvGg
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:33:47.668911
---

# IETF 125｜下一代域间路由架构与协议边会顺利召开

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaJcPGD01bWVbzJ4jVC5LKZiaN0EoIxpag75TZRafceq4YPynt9ZTWAKIRiaWPK7yflxqwpJUCTCMZRMlIX9xbUqDs1FDpbG1lSONO6JPskQX4/0?wx_fmt=jpeg)

# IETF 125｜下一代域间路由架构与协议边会顺利召开

原创

赛博新经济
赛博新经济

赛博新经济

![]()

在小说阅读器中沉浸阅读

2026 年 3 月 18 日，IETF 125 期间，IDRNG Side Meeting 顺利召开。会议汇聚了来自全球运营商、设备厂商、科研机构及标准组织的国际专家学者，在 AI 驱动技术范式变革的时代背景下，共同探讨域间路由体系的未来发展路径。

IDRNG（Next-Generation Inter-Domain Routing Architecture and Protocols）是由清华大学与中关村实验室联合发起的研究小组，聚焦域间路由架构与协议的演进，致力于汇聚学术界与产业界多方力量，共同探索下一代互联网路由体系的发展方向与关键技术路径。
Github仓库: https://github.com/IDRNG/
邮件列表: idrng@irtf.org
订阅链接: https://mailman3.irtf.org/mailman3/lists/idrng.irtf.org/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWWc3WqhuZL5ia7UOLaPOVn1Y54Klicy8iaNzESiaWxJadqHe21Gf0T42CNMny3NSIiblEyt7s9u1lBia0h4qtZjoZJqkc0tPbsb7MPzs/640?wx_fmt=png)

**01**

议程回顾：从机制演进到体系重构

会议由清华大学李琦主持，从互联网域间路由的发展脉络出发，回顾了 BGP 体系的长期演进路径，并结合AI 时代的技术趋势，介绍了当前域间路由所面临的关键瓶颈与潜在机遇。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWVUrSctuu3nea9VpDew3PlXdu6iaJwquVaZYbiaJt4QwGYzKLjvxNlXicN2iamAlibJDbiaKHm80MLe1IlIRDzBK7CseCjS9Iabv5jzU/640?wx_fmt=png)

随后，多位国际专家围绕标准化机制、部署实践与现实挑战等方面，分别做了主题报告：

* MANRS 指导委员会成员、ZDNS 副主任、首席科学家马迪系统介绍了“How we develop, adopt and maintain MANRS documents: The MANRS Development Process”，从社区共识构建与最佳实践推广角度，揭示了路由安全协同治理的演进逻辑。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXOHrUKiahMES63C4IuwB2Aq0UsUuiaJFmicn35AIWc4taoFZwMeeDkicdtYJ6ybg8IKKWQ5vWVhAInXmOsUtS1bJhYh8tvel8aFss/640?wx_fmt=png)

* IETF IDR 工作组主席 Susan Hares 在“Reducing Time to BGP Changes”中，深入探讨了如何缩短BGP机制从理念提出到规模部署之间的周期，指出标准化流程与产业协同之间的关键耦合关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWVIsD9vuh3PwPeDWxqQjibjJRTQZgickT5ibIja14KyTWAsX4CcJJ0DadC5yhQAKWuH5m1TYIZ001BPxsXLyVau3s2ZKfYgic2LruE/640?wx_fmt=png)

* Virginia Tech 李纬同通过“When RPKI Meets Reality: Understanding the causes and risks of RPKI-Invalid”，从数据与测量角度分析了 RPKI INVALID 现象的成因与潜在风险，揭示了现实部署环境中的复杂性与不确定性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWXaOwv1YrGcfElBuibLG50OibKOTzybSDTpx5LibCVNncK7iaaArlOYiaO83Ef9zCyW5bHSUB72X2xb1dlAiaetGFRm6poN7guFp9Kn4/640?wx_fmt=png)

* 中国联通王翠翠围绕“The Routing Deadlock: Challenges We Can No Longer Ignore”，从工程实践出发，系统剖析了域间路由在安全性、可扩展性与可管理性之间长期存在的结构性张力。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXcAL7paAOhvsPfs7A7RUHddQnbShA62rcGLpUYUFdkcFkGjLqPvwX5VAvBE7M797PFxYMwoVPGO02QamRWZ9grwuBIy2zrG4g/640?wx_fmt=png)

**02**

深度讨论：从“可用互联网”走向“智能可信互联网”

围绕域间路由体系的未来演进，与会专家展开了多维度、跨层次的深入讨论，呈现出若干值得关注的重要趋势：

1. **从协议设计到部署现实：演进路径成为核心约束**

Tony Li 基于其长期参与 BGP 及相关机制设计的经验指出，下一代路由技术的成功不仅取决于机制本身的先进性，更依赖于其在现网环境中的可部署性与演进路径设计。

Susan Hares 进一步强调，渐进式演进与社区协同仍然是推动互联网协议持续演进的核心方法论。

2. **AI 驱动的新范式：从“理解协议”到“自动化网络”**

Joseph Potvin 分享了利用 LLM 辅助解析 RFC 文档与协议逻辑的探索实践，通过结构化表达协议语义，为自动化验证、配置生成与工具链构建提供了新的技术路径。

这一方向引发广泛共鸣。与会专家认为，AI 有望在以下方面带来深刻变革：

* 提升复杂网络系统的可理解性
* 推动运维体系向自动化与智能化演进
* 支撑大规模网络中的策略一致性与动态优化

域间路由，正在从“人工驱动的复杂系统”，迈向“机器可理解、可推理、可协同的智能系统”。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWsZ2Ek9QHEiaVtXzNFbNSPlteofftqJFkTNJI31jEGd2MccN7CX32sSvU0IxFDlOnVTYDcljrmdGUdwkQr8XHPiaqqc3be54Whs/640?wx_fmt=png)

3. **路由安全：从单点机制走向多方协同与可观测体系**

围绕 RPKI 及相关验证机制，Michael Hollyman 从一线工程实践出发指出，单一机制难以覆盖复杂攻击面，未来需要构建：

* 更强的全局监测与数据分析能力
* 更高水平的数据一致性保障机制
* 面向运维的可观测性体系

多方协同与跨系统联动，正在成为提升互联网路由安全韧性的关键。

4. **架构创新：多路径探索与技术多样性并存**

讨论中，以 SCION 为代表的新型网络架构被多次提及。其在特定场景中的实践，为突破传统 BGP 体系的结构性限制提供了重要参考。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWU5ibOh4fnvltanmySk8ic2HE79HMo7qgbEnGzyGtkIqsZa8Hsv0xibNrp6E2643RmiclD9Kvvjp6LdPp7XFtiajPKZ7p1Rx8uohuzc/640?wx_fmt=png)

在讨论的最后，IRTF 主席 Dirk Kutscher 对本次边会进行了点评。他指出，本次会议围绕 BGP 安全等关键问题汇集了多方面的研究与实践探索，初步展现出若干具有研究潜力且面向实际问题的方向，但整体仍处于议题发散与探索阶段。

他进一步提出，未来需要更加聚焦社区的核心关注点，并思考该方向是延续现有 BGP 相关问题的讨论平台，还是进一步发展为面向未来的研究导向议题。在此基础上，应逐步凝练更加连贯的研究议程，并加强问题归纳与社区联动，推动形成持续性的研究活动。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWV3KZYWAhIkDZorUwLR3Io8IVwwwxIprKib5HhfpNicPica5SokZ9b61bnnWfrKAhIY3ibkoKvr90CSltdJdwaoEetpW2iaOKAyduSg/640?wx_fmt=png)

**03**

总结

本次 IDRNG 边会顺利召开，汇聚了来自全球、不同背景的路由领域专家，对于推动构建开放、多元、面向未来的交流平台具有重要意义。在全球互联网持续演进的背景下，这种跨界协同与持续探索，将为构建更加安全、高效、智能的网络路由基础设施持续注入动力。

随着相关讨论的不断深入，IDRNG 有望进一步凝练研究议题，吸引更多社区力量参与，共同推动域间路由体系迈向新的发展阶段。

**参考资料：**

IDRNG IETF 125: https://github.com/IDRNG/125meeting

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVianBKqe9LBRDkFTe4vrBHA8VVOcs0wauglpkBn55FibV2m5bZBmgkLTFrNzLQ93ELgWjYuhFv2WDIdA/0?wx_fmt=png)

赛博新经济

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVianBKqe9LBRDkFTe4vrBHA8VVOcs0wauglpkBn55FibV2m5bZBmgkLTFrNzLQ93ELgWjYuhFv2WDIdA/0?wx_fmt=png)

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