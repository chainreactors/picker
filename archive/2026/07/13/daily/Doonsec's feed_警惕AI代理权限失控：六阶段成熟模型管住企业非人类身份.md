---
title: 警惕AI代理权限失控：六阶段成熟模型管住企业非人类身份
url: https://mp.weixin.qq.com/s/E4jC_7bfLVJeERHkFq1_-w
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:43:38.982225
---

# 警惕AI代理权限失控：六阶段成熟模型管住企业非人类身份

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpeM9QoXNAe4OicKLibsFlcywowG4dL9jn7uxGrVwqWE0iaqNRgp8Q1pUd7FS01p8PuRIU07svH5ZzOrib5SZetjIMlibPaxumhgkyJs/0?wx_fmt=jpeg)

# 警惕AI代理权限失控：六阶段成熟模型管住企业非人类身份

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

2026年，智能体AI与自主代理成为行业趋势，企业面临一项全新的重大挑战：标准的身份与访问管理（IAM）体系，并非为管控这类非人类主体而设计。

去年的一次客户项目中，一个拥有生产环境Kubernetes集群常驻访问权限的大语言模型部署代理，因推送了格式错误的配置，引发了长达四小时的服务中断。

在IAM系统中，该代理显示为一个持有长期有效API密钥的服务账号，无多因素认证（MFA），也没有定向的权限撤销路径。

当事件复盘团队询问是哪位人员授权了该代理的最后一次操作时，在场无人能答。

过去一年里，我在三个不同行业、使用三套不同厂商方案的项目中，都见过类似的问题始终得不到答案。

如今每位首席信息安全官（CISO）的汇报材料里，都会有一页介绍智能体AI。

但极少有材料会说明，从身份层面来看，这些代理究竟是什么。这一缺口才是更危险的隐患。

前者是战略问题，后者是管控问题——而最终审计人员、事件响应团队和董事会追问的，恰恰是后者。

高德纳（Gartner）研究总监亚历克斯・迈克尔斯发布的《2026年网络安全顶级趋势》指出，这一缺口的两面——智能体AI监督（趋势1）与IAM体系适配AI代理（趋势4），正是今年重塑网络风险格局的核心因素。

本文提出了一套面向非人类身份与代理类身份（NHI）的六阶段成熟度模型，列出了生产环境部署前必须满足的六项最低要求。

同时点明了访问与身份领域最具决定性的一项汇报原则：绝不能将人类身份治理与非人类身份治理的结果取算术平均值。

![图图 (5).png](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpeG57yueCYdDv6ibnib82ptrv9C1lExxzibcOT3t1fuENIfcbVlPj6iaCme9QGkAhcQ5zNBjMNGr744xEwhdXF2uB7fqUIp5hKOobY/640?wx_fmt=png&from=appmsg)

**为什么代理系统会打破现有身份模型**

传统服务账号仅执行范围狭窄、可预测的任务：拉取备份、运行定时报表、对构建产物进行签名。

其权限范围在设计阶段就已固定，配套的管控措施——密钥轮换、凭证保管、审计机制——也都有成熟的方案。

代理系统的运行逻辑完全不同。

它接收一个目标意图，将其拆解为执行步骤，自主调用它认为合适的工具或API，最终产出结果，而每一步具体动作并非提前逐一指定。

库平格科尔（KuppingerCole）2026年发布的《非人类身份管理领导力罗盘》指出，在许多企业环境中，非人类身份的数量已超过人类用户，部分场景下比例可达25:1甚至50:1。

这份由首席分析师马丁・库平格主导撰写的报告同时提到，围绕“入职-调岗-离职”生命周期搭建的管理工具，从设计上就无法在如此规模下完成对这类身份的发现、归因与管控。

开放式Web应用程序安全项目（OWASP）生成式AI安全项目已分两个阶段梳理了由此产生的攻击面：

2025年2月发布的《智能体AI威胁与缓解分类法》，以及同年晚些时候更具实操性的《智能体应用OWASPTop10》（类别ASI01至ASI10）。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfLSrjPdqXsHAmqiaYFTl3bnDaOjibsGzeHXszSf2272AHGooN1PxoX0b6PXtEJ4cOYEBT2ADFRy3Rg6Q7VrjAprgGAvhaiaicZZiag/640?wx_fmt=png&from=appmsg)

其中值得关注的结论是，风险等级最高的四项风险里，有三项都属于身份范畴：

工具误用与利用（ASI02）、身份与权限滥用（含委托信任与继承信任）（ASI03），以及超出预期行为运行的异常代理（ASI10）。

第四项智能体供应链漏洞（ASI04）也与身份问题密切相关。

美国网络安全与基础设施安全局（CISA）联合五眼联盟于2026年5月1日发布的首份相关倡议——《审慎采用智能体AI服务》，也得出了相同结论。

该倡议由美国国家安全局、澳大利亚信号局下属的澳大利亚网络安全中心、加拿大网络安全中心、新西兰国家网络安全中心与英国国家网络安全中心共同发布，将权限风险列为核心关切。

互联网安全中心（CIS）随后在2026年4月发布报告，指出提示注入是叠加风险最高的安全问题。

美国国家标准与技术研究院（NIST）也于2026年2月启动了AI代理标准倡议，目前正在起草配套的正式标准。

换言之，智能体AI带来的最主要风险类别，并非新型加密技术或某种全新的攻击手段。

而是现有IAM模型从未需要管控的、权限范围无边界的身份主体。

**代理上线生产前的六项最低要求**

在讨论成熟度之前，首先要守住底线。

以下六项要求是一条基准线：达不到这条线，代理系统就不具备在企业环境中负责任部署的条件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpc0qyrMOZLActzyAartAonvV1WGT5sYGo2BprkfwOtghzu3IBFsQHWLztpFXSHlO6vVYqduwATXsZlnI9Aibs0EZqsoB9hiaJKjY/640?wx_fmt=png&from=appmsg)

这些要求来自我在制药、能源、金融、制造业项目中收集的事故与审计发现。

它们在现代IAM与特权访问管理（PAM）平台上技术上均可实现——但多数企业现有的IAM体系通常都做不到。

1. 每个代理都拥有唯一可归因的非人类身份。禁止多个代理共用服务账号，也禁止代理与人类管理员共用账号。

2. 权限采用“代表执行”模式授予。代理以指定的人类主体名义执行操作，继承该主体的权限，且权限限定于明确的用途范围内。代理自身不得拥有常驻权限。

3. 不得使用长期有效凭证。API密钥有效期不得超过1小时，代码中不得嵌入密钥。仅允许使用短期、与上下文绑定的凭证，且发现异常时可立即撤销。

4. 通过安全信息与事件管理（SIEM）系统集成，实现完整审计追踪。每一项代理操作都需记录时间戳、执行身份、指令发出人、输入上下文与执行结果。

5. 持续重新认证。对于长期运行的代理，需按固定间隔基于风险重新验证身份，而非仅在会话启动时验证一次。

6. 实时撤销能力。数秒内断开代理与系统连接的能力是必备项，这是唯一能在代理类事件发生过程中真正控制事态的管控手段。

无法满足全部六项要求的企业，面临的不是代理治理问题，而是部署就绪度问题。

下文的模型默认第三阶段已满足全部要求；在此之前都属于发现阶段。

**六阶段非人类身份成熟度模型**

多数企业的成熟度评估，都以人类身份为标尺衡量访问与身份管理水平：

是否有统一IAM、特权访问是否强制多因素认证、入职-调岗-离职生命周期是否顺畅。

这些问题依然重要，但覆盖范围不足。

一家企业如果人类身份治理达到第4阶段，而代理治理仅处于第1阶段，那它的身份管理体系并不成熟——只是一半管理完善，另一半完全盲区。

以下六阶段模型为递进式设计——每个阶段都默认已满足之前所有阶段的要求。

责任合规的门槛在第3阶段。

在我看来，未达到第3阶段就将代理系统投入生产，无法向董事会、监管机构或事件复盘团队交代。

![图图 (1).png](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfX1fhaFkU3CQbj54KZZP1pADclkodYicb2Y1mKHVQmbRNzg7N2clca6wW1kNsQqqwqf7uwunXBFoFC3R4xLBqfvHsN5IA0cpCk/640?wx_fmt=png&from=appmsg)

第4和第5阶段需要展开说明。

因为从这两个阶段开始，模型不再局限于访问控制，而是开始对行为进行治理。

“有界”指代理的授权范围有明确的不可逾越的边界。

“可审查”指每一项操作都记录了意图、执行过程与结果。

“可回滚”指操作在造成不可逆影响前可以撤销——对于涉及物理流程、金融交易或对外承诺的环境，这是一项硬性约束。

“自调节”指系统可检测代理行为的异常，并在人工来得及响应前主动介入。

**“人工介入”不等于有效治理**

有一个普遍的认知误区，会让企业高估自身的代理治理水平。

人们普遍认为，决策流程中有人工介入就等于足够的监督，事实并非如此。

如果要求一个人审批成百上千项代理操作，却没有时间逐一核查，那这不是管控，只是带有人工签名的审批自动化。

人工审核的效率，跟不上自主系统的操作量级。

成熟的治理模式会正视这一点。

它将管控从事项审批转向结构性约束：从根本上限定代理可执行的操作范围，监控其行为异常，并确保监督机制对委托人负责，而非对执行系统负责。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfRpIThVBcP7LfrriakYPDED6efNnmz642scDWvIlro9ibiahrDNzcBCjNfA0RCcJ4PKJYRQhMmEjcykfnsSx7SKqSqgZz8uZ6zmQ/640?wx_fmt=png&from=appmsg)

如果一家企业的代理治理完全依赖人工逐项审批，无论审批记录有多详尽，都达不到模型的第4阶段。

第4阶段要求的是结构性边界约束，而非靠人力堆砌的规模化审核。

**以OWASP标准作为可审计的证据依据**

成熟度评估很容易沦为主观的自评打分。

上文提到的OWASP风险分类可以转化为具体的审计问题，让每个阶段都有可核查的依据。

![图图 (2).png](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfIH8ibLHAjExWsueEjEWMA2hjv4Gs1vQZHvHTq53YSHSBuLLpn6Kz3ibFfrZ3a85MduWzsOTaqbw4JL7y6eCyocQVs6qM3ibmBRY/640?wx_fmt=png&from=appmsg)

最右侧的列至关重要。

一个常见的评分误区是，企业因为满足了简单要求——比如唯一身份、基础日志——就给自己打高分，却没有解决高难度的要求。

将高阶阶段与高难度标准绑定，可以避免这种评分虚高。

**人类身份与非人类身份应分开汇报**

最具决定性的汇报原则，就是拒绝取算术平均值。

成熟度雷达图中的访问与身份维度，不能把第4阶段的人类身份治理水平和第1阶段的代理身份治理水平，合并成一个看起来稳妥的中间值。

两项评分可以放在同一坐标轴下，但必须分开呈现。

当前项目中的一个典型发现是：

人类身份治理处于第4阶段——统一IAM、多因素认证、生命周期管理完善——而代理治理仅处于第1阶段。

代理刚完成清点，仍通过长期API密钥、共享服务账号进行认证，也没有独立的审计追踪。

合并平均后得分会在第2到3阶段之间，看起来尚可接受。

分开汇报则会清晰显示：这部分未被管理的身份，恰恰是操作范围最大、最不可预测的身份类别。

只有看清这一点，才能推动优先排期的治理规划；而合并得分会掩盖这一核心问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpcOIycvV3qecpJic0OD6ibm6q8HaysDKR9V5qCEOYmcJC0Hnl1pWmArLII1pmWXTDoKs4wME6N6ibD3y3z8dlNenhJknxjD6Ff9mo/640?wx_fmt=png&from=appmsg)

**指定问责负责人测试**

如果我在新项目中只做一项诊断，那一定是这项。

针对环境中每一套投产的代理系统，问一个问题：如果该代理造成损害，具体由谁来负责？

一个没有指定问责负责人的代理，就像人人都用、却没人负责的公用工作站。

模型的第5阶段正式要求，每个部署的代理都要有指定的问责负责人。

这么做是出于运营需求，而非官僚形式：“谁对这套系统负责”这个问题，必须在事故发生前就有答案，而非事故发生时才去追问。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpdmEbfyav8wjclVADrBI9Ja6xdT6aXOKjtchlbE7ua140JdkBDEFZ5qqCMIGR0Go4Qu1FvH8ZkrzqRvyf2Sv1vibWvGp5wZbHzE/640?wx_fmt=png&from=appmsg)

在实践中，这份问责责任最好绑定到原本就承担对应流程运营风险的角色——通常是业务部门的资产负责人。

将责任锚定在业务侧，可以避免代理系统落入IT、安全与业务之间的组织灰色地带——而无人归因的操作，恰恰就诞生在这种灰色地带中。

本文提出的成熟度模型是一个基础框架。

落地它最坦诚的第一步，不是追求高分，而是如实评分，将人类与非人类身份治理分开汇报。

并将两者的差距作为智能体AI时代安全路线图的首要事项——赶在下一个代理上线生产之前。

原文链接：https://www.csoonline.com/article/4194548/agentic-ai-identity-a-6-stage-maturity-model-for-non-human-identities.html

**安在企业（用户）会员服务**

**助力全生命周期安全意识提升**

“安在企业（用户）会员服务”，为所有企业提供一站式的网络安全支援服务，包括意识宣传、培训教育、效果检验、专业圈子、知识社区、专业培训、参选评奖等多个板块，助力网安从业者高效履职，实现个人与企业安全能力同步升级。

**[小投入大防护！安在推出企业（用户）会员服务](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)，点击标题阅读详情。**

深度贴合企业不同规模、安全水平投入以及员工安全意识的不同发展阶段，特设5级安全意识培训服务体系，为企业用户量身匹配适配的安全意识解决方案。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfxauQUKv5E2gfFrpMBAz1Um7FAY4ontydFQQ1ZKtH1AnXs3kfYxtOYX55xrRBM2pFYicz2sqACyjd4u1CO2iaAFCYLIbgMGS58M/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpevFQuuGbgqzRQXxpZt2NQG9gkeSfhrKIBL6NVagjD9IYhtko4pjEdkrmiaAFfGAYPQN06Cs2MSLG4HGqExqL1OJ9n0ZSmibwO9Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

本文展示所有类型素材，均包含在企业（用户）会员服务中，如有意向，欢迎垂询。

**加入诸子云知识星球**

获取更多“安全意识资料”和“网络安全报告”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpevtB5U1iad3jHVWSBznd4wGSnt15KjDpDvdDAzWfLewNRoKHVyCNTCEIVkuJAZOyUvKSibQZJfe43xQsofxEKuB4xuj2gzBG4EM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfphwUVRfsnQ4tHXQicImFKOyric81wyOR6UtibaU9W2nPpF2bIflBltg8S0vJMmYEDrEkWN30lpxicg5YUyLDu0fAlCgX3ibJBX8Ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcHLAPdhJaKhut2fLyfnDD0ofblclhTxwQtdjZ9Wnsgw7qtANaolbmpYLhf9mCW9ib2vDial19qZnEibibEZkAcOVPZVTA9QsD5EeY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcaBf7luDbkibnkcG6SFanyicuIePMSYCXyZ4dpRTDOuRkj4IwafHmia3a61q1QmasWkERH6vhD4eicgePFZCERRib6zAefEHxWz3cY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcoibvzpu3KUfibMYf9yTU7VWPXP10LBBkle2fQKqqdVk7zLYiaoh0bHWxmovw4aqY0icMXYfqY2TW0LibL3W2NVG5u6ibA9aDyzsF8I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpfHuRbxczmKK36HLRfSVxysIgBAQMVFSdVGCDascdwN2jmE6LickWQ9nyK1k0fVcibLIYwaseCvT2VtXEoVubWyMLdmf9jRo59JY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz...