---
title: 从Gartner2024年北美安全峰会看安全运营的技术趋势
url: https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484795&idx=1&sn=8f835c0699be66f615e7b713f67e26dc&chksm=fa002fcfcd77a6d99c87a875e75aae61202079294bd300e83a67cc9f0535a4a426f398afd607&scene=58&subscene=0#rd
source: 专注安管平台
date: 2024-07-20
fetch_date: 2025-10-06T17:43:27.266232
---

# 从Gartner2024年北美安全峰会看安全运营的技术趋势

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t7v7zyOTkMeEziadp1sBictffc7G4iborx5GMn2v0a9tibmjlJfzau9ZlkYT219WdgXicGyWMarKovoqSLanoaCgfCg/0?wx_fmt=jpeg)

# 从Gartner2024年北美安全峰会看安全运营的技术趋势

原创

Benny Ye

专注安管平台

2024年度的Gartner北美安全与风险管理峰会在6月3日至5日在美国召开。这次峰会并没有在媒体（尤其是中国媒体和自媒体）上受到关注，可能是现在Gartner的安全峰会一年多次在全球举办分散了注意力，也可能是现在对于网络安全的创新点过于聚焦在GenAI之上而显得各种安全大会缺乏差异而造成了思考疲劳，抑或国内外的网络安全技术越来越多的分叉导致国内网络安全技术从业者越来越关注自身，而国内当前低迷的网络安全产业市场多少也对人们谈论网络安全的前瞻技术形成了阻碍。

**重点的新兴技术领域**

在《2024年安全与风险管理新兴技术》议题中，Neil McDonald筛选出了5类关键技术：

1）**AI和GenAI**：包括保护AI和利用AI两个方面。在保护AI方面，是Garnter重点关注的方向，涉及的新兴技术包括AI TRISM（AI信任、风险与安全管理）技术、LLM防火墙、在SASE/SSE中增加对AI应用的保护技术，以及AISPM（AI安全姿态管理）。在利用AI方面，Gartner显得十分谨慎，目前的建议就是在现有的安全控制台中增加GenAI接口。

2）**安全平台整合**：这个已经谈了好几年了，主要集中在各个领域内的横向整合，包括面向云的CNAPP，面向边缘接入的SSE和SASE，以及面向安全运营领域的SIEM/SOC与XDR、CTEM的整合，此外还有身份安全平台的出现。Gartner还指出，现在已经出现了跨多个领域的整合平台。

3）**身份即关键基础设施**：也即要保护身份这个关键基础设施。涉及的新兴技术包括ITDR、ISPM（身份安全姿态管理）、机器身份管理，以及无口令认证。

4）**xSPM的崛起**：xSPM（或者简称为SPM，即安全姿态管理）代表了Neil自己提出的自适应安全架构的I（识别）和P（保护）【笔者注：最新的Gartner自适应安全架构的四象限分别是IPDR，其中第一个是I（识别），而原来是P（预测），仅修改了名称，内容未变，估计是为了与CSF的IPDRR中的I保持一致性】的I和P象限，而包括XDR等在内的ITDR则重点聚焦在D和R象限。在各种SPM中，新兴的SPM包括ASPM（应用SPM）、DSPM（数据SPM）、AISPM（人工智能SPM）、SSPM（SaaS SPM）。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMdfqwTT5cJNZB4Gv4cc0TOqWB530Izouib1FG2GSQjsQbwNrGXcu3Bkbuib3ibHL9iaDz5SJXTBbarLpA/640?wx_fmt=png&from=appmsg)

5）**CTEM**：这个也谈了好几年了，新的变化主要是将CTEM从IT环境扩展到OT和CPS环境中。而新兴技术趋势包括CTEM下不同类型产品的相互融合，以及SPM厂商和SIEM厂商的纷纷介入（增加EM方面的功能）。而正是由于SPM厂商和EM（暴露管理）厂商的互相渗透，使得Posture（姿态）和Exposure（暴露）两个概念之间的关系越发微妙。

从安全运营的角度来看，以上5个方面中，有四个方面都跟安全运营有关，包括：安全运营领域是利用GenAI的最佳场合之一；安全运营的平台整合正在塑造新一代的SOC平台；而SPM和EM也都正在融合到全新的SOC框架中。

**安全运营领域的前景展望**

在峰会上，Gartner提出了**三大方面的展望：CTEM和TI（威胁情报）助力安全运营、GenAI赋能SOC、超大规模安全运营**。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMdfqwTT5cJNZB4Gv4cc0TOqRrnmTNr6hHe0uNMHFPsFBpX4lpLicGI8h0nPYGiazGyqUlNNMv4FR9gA/640?wx_fmt=png&from=appmsg)

其中，CTEM和TI有助于帮助收敛攻击面，为安全运营做好事前准备，同时它们获取的信息可以作为后续检测和响应的情境（上下文）数据使用，以加速检测和响应。GenAI能够从多方面赋能SOC，但还很不成熟 ，存在安全隐患，一定要慎重使用【笔者注：Gartner对GenAI一直持谨慎态度】。而如何在现有（小）资源的条件下进行超大规模的安全运营工作正成为越来越迫切的问题，必须有机结合AI与自动化技术。

以下笔者分别从CTEM助力安全运营【注：TI助力安全运营已深入人心，故略过】、GenAI赋能安全运营和超大规模安全运营三个方面进行深入分析。

**CTEM助力安全运营**

**CTEM解析**

结合Gartner观点，笔者认为持续威胁暴露管理(Continuous Threat Exposure Management)是一套包含技术、流程和人员在内的系统性、集成化、迭代性的方法和体系，让企业和组织有意识地持续并一致地评估其数字资产和物理资产的可见性、脆弱性和可访问性，以持续优化提升安全姿态。Gartner将CTEM看作是一个过程和方法，而将EM（Exposure Management，暴露管理）看作是支撑CTEM的技术集合。

EM的核心能力是进行暴露评估和暴露验证，其中暴露评估包括攻击面评估（ASA）【注1】【注2】和漏洞评估与优先级研判（VA&VPT）【注3】，暴露验证主要是使用破坏和攻击模拟（BAS）和自动化渗透测试等网络安全验证技术【注4】。简单地说，EM = ASM + VM + CyVal。

【注1：最新的Gartner ASM市场指南报告中指出ASM中的M（管理）不是一个准确的定义，其实ASM的工作更多是ASA（攻击面评估），由于历史原因也不会改名了，但有的场合会使用ASA。】

【注2：ASA或者说ASM又包括三个技术，分别是EASM、DPRS和CAASM。这里不再展开叙述。】

【注3：这里的漏洞还包括安全配置缺陷和安全防御策略的缺陷。安全配置的缺陷通常使用配置核查工具来识别，而xSPM类产品也都提供相关能力。安全防御策略缺陷则包括了安全及网络设备的安全策略缺陷（譬如防火墙规则缺陷），甚至于安全运营体系（如SOC）的检测、监测和响应策略的缺陷，等等。】

【注4：安全验证技术和工具不仅可以用于暴露验证，即验证暴露的有效性，还能用于安全漏洞以及配置和防御策略缺陷的评估。】

必须指出，CTEM的闭环并不是我们一般所理解的闭环，并不是以暴露面的收敛（包括漏洞缓解），暴露事项（issue）或者工单（ticket)的关闭为结束，而是以“动员”为结束。也就是说，Gartner认为暴露面收敛的具体工作主要是IT和业务部门的事情，安全部门当然也要参与，但不属于安全部门自个儿的事情，因此不在CTEM闭环中。CTEM的闭环最后就是能够将有效的暴露面事项或工单提供给专门的团队和人员，并协助和督促其整改。因此，不要想当然地认为CTEM会真正“管理”和收敛暴露面。

上述CTEM的工作内容也恰恰印证了安全运营工作中资产运行和漏洞运行的工作范围。其中最重要的是安全运营中的漏洞运行工作也是不包括漏洞缓解本身的（尽管有的漏洞缓解工作也能在安全运营团队内部实施），漏洞缓解系统应该另行由安全部门、IT部门和业务部门共同建设与运行。

**EM为SOC提供上下文**

但是，暴露评估和验证的结果对于SOC的检测和响应工作却十分有价值。EM可以为TDIR提供上下文（情境）信息，譬如：精准的资产和漏洞信息可以让分析师编写更加精准（包含资产和漏洞关联信息）的检测规则，并且这些规则可以真正用起来；可以生成更加丰富易懂的告警信息；有助于支撑威胁猎捕；而暴露验证获得的安全控制策略方面的缺陷有助进行威胁建模。总之，有了EM提供的上下文信息，TDIR可以更加高效，也即安全运营更加高效。

**EM可以提升SOC自身弹性/韧性**

EM中的安全验证工具通过对安全漏洞、配置和防御策略缺陷的评估，以及暴露的验证，可以实现对包括TDIR在内的SOC有效性的评估，从而提升SOC自身的弹性。SOC自身策略和安全内容的缺陷也是一种暴露，也需要被识别和验证，譬如发现针对某项不可修复的漏洞的补偿措施（虚拟补丁或者增强监控策略等）的缺陷，识别出低效（导致高误报）的关联分析规则，发现针对某种关键威胁的响应对策的缺失，等等。通过对这类缺陷的识别和验证，有助于提升SOC自身的强度。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcmozicIBJQXaFoVpy4lH55UWpYp9gibq1xmFHicHF2LBPszGPoOrUib7rDhy4084buxuNcYowL6BohJQ/640?wx_fmt=png&from=appmsg)

**从SOC的角度看TDIR和EM**

首先，安全运营（SecOps）是一个很宽泛的概念。如果我们把整个安全生命周期分为规划、建设、运营三个部分的话，安全运营的历程将伴随企业组织的一生。因此，可以**把安全运营看作是持续不断地保障目标网络安全平稳运行，达成组织业务战略目标的永续过程**。安全运营涉及的内容很广泛，从能力方面看，可以分解为IPDRR（识别、保护、检测、响应、恢复）或者类似的变体。从运营对象来看，可以分为工作负载、端点、应用、数据、身份等维度。Gartner将安全运营定义为一个“**通过一套人、流程和技术来识别和管理暴露、监测、检测和响应网络安全威胁与事件，以提升网络弹性**”的过程。SANS则将安全运营的使命定义为“保护业务运营的私密性、完整性和可用性，并最小化非预期事态造成的损失”。

安全运营中心（SOC）则比安全运营更加聚焦，虽然有很多定义，但通常都是指一个包含一系列流程、人员、技术等的组织单元，**核心目标就是抵御网络安全威胁、保障目标网络安全平稳运行**。围绕这个目标，通常会对目标网络实施持续的检测、监测、分析、调查、响应、报告、修复。笔者基于自己的多年实践，认为**安全运营中心可以分为威胁事件运营、资产暴露运营、安全漏洞运营、安全情报运营、防御策略运营、态势决策运营6个方面能力**。其中，威胁事件运营是所有SOC的核心能力，就是指威胁事件的检测与响应，通常依托于SIEM或者Gartner新提出的TDIR。而资产暴露运营和安全漏洞运营则跟Gartner的EM相匹配，以在事前掌握和完善自身安全防御的姿态，同时又与安全情报运营所依托的TIP一道为TDIR提供上下文（情境）信息，提升威胁事件运营的效能。防御策略运营则通过持续的评估、验证和改进来不断提升包括SOC自身在内的防御体系的有效性。最后，态势决策运营持续收集前面5大运营过程中的数据，进行指标计算和态势量化，形成决策，从而动态调整安全保障级别，调配安全防御力量。

在笔者看来，当前国内大部分SOC基本还处于基于SIEM所承载的威胁事件运营阶段。安全情报虽已普遍应用，但客户自身TIP建设及其上的安全情报运营还处于早期。资产暴露运营和安全漏洞运营则还处于初始、分散的阶段，相关信息还处于不全、不准、滞后的状态，尚无法实战，难以赋能威胁事件运营，而这在全球范围内都是一个痛点，也**因此Gartner近几年一直在力推EM/CTEM**。至于防御策略运营、态势决策运营（尤指宏观态势）则更多还停留在纸面上。以2023年发布的网络安全态势感知通用技术要求国标为例，更多还是描述了态势展示的内容，而态势信息的获取与分析则基本与SIEM重合。

**GenAI赋能SOC**

这已经是不争的事实了！从笔者分析的[RSAC2023大会](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484640&idx=1&sn=6ff1f407b3ad35c01efbf35d5a0ded0d&chksm=fa002e54cd77a7425235ca39c42acb32187bd913d3b3ab9ec75c9d2c504fab0f49d75efada57&scene=21#wechat_redirect)和[RSAC2024大会](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484766&idx=1&sn=5b66715c108908d39eb92ecdc964c9f6&chksm=fa002feacd77a6fcdc78bff2275afb83ea403c19d547584bd02669f68550e26c5d27b7303c8b&scene=21#wechat_redirect)的情况看，所有人都知道GenAI用在安全领域的首要场景就是安全运营和SOC。因为GenAI恰好完美地击中了当下安全运营的三大痛点：人才短缺、工作倦怠（告警疲劳）、技能不足。不论是副驾、助理还是智能体，都试图让GenAI驱动的机器人充实到客户的安全运营团队中去。

Gartner预计，到2028年，基于多智能体的威胁检测与事件响应工作将从现在的5%暴涨到70%。同时，Gartner认定届时AI主要还是增强而非替代员工。

**GenAI应用部署模式**

Gartner将GenAI应用分为了4层：基础模型层、微调层、数据检索与提示工程层、应用层。对于使用/开发GenAI应用的人而言，可以采用5种部署模式：直接用第三方的GenAI App、将GenAI嵌入到自己的App中、自己实现数据检索与提示工程、自己实现微调、自己从底层模型开始搭建。显然，从不同的层次开始构建GenAI APP，成本和技术考量都是不同的。如下图所示，展示了GenAI的分层和五种部署模式，其中蓝色块表示采购自第三方的组件。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMeEziadp1sBictffc7G4iborx5PTicawZVDIA0AQRj8qn2SRrc2AyDBNWNrgUot34VyQDuX5d9rSIlmuQ/640?wx_fmt=png&from=appmsg)

**GenAI应用类型**

目前，仅就用于SecOps的GenAI应用而言，大体上可以分为三种类型：聊天机器人、AI助理/副驾、智能体。三种类型的难度依次上升。目前，主流的SecOps厂商聚焦于AI助理/副驾（譬如[微软的Copilot、SentinelOne的Purple AI](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484640&idx=1&sn=6ff1f407b3ad35c01efbf35d5a0ded0d&chksm=fa002e54cd77a7425235ca39c42acb32187bd913d3b3ab9ec75c9d2c504fab0f49d75efada57&scene=21#wechat_redirect)），而初创企业（如[Dropzone AI](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484766&idx=1&sn=5b66715c108908d39eb92ecdc964c9f6&chksm=fa002feacd77a6fcdc78bff2275afb83ea403c19d547584bd02669f68550e26c5d27b7303c8b&scene=21#wechat_redirect)）则更多聚焦于智能体。下图展示了不同类型下的厂商示例。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMeEziadp1sBictffc7G4iborx5syqcbERqrxMPNERaD3oz3lViaB2wTNOAyAkZy4gWbdbJoHuvLrZZezw/640?wx_fmt=png&from=appmsg)

下图展示了当下主流的AI助理/副驾的工作原理，核心就是提示工程和RAG。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMeEziadp1sBictffc7G4iborx5PsvwP1wMMbWiaMP1sym67qLicPkORQABczXYicU7K6lITzduGgjMKQ7cA/640?wx_fmt=png&from=appmsg)

Gartner表示，以当前最重要的大语言模型（LLM）为例，它其实并不真的“智能”。在笔者看来，往深了讲，它的“智能”都基于你喂给它的语料和对它使用各种安全运营工作套路的训练，抑或各种静态知识库。此外，LLM尚未真正取代现有的威胁检测引擎，大部分情况下都是LLM基于你自然语言的输入生成检测规则或代码，然后还是由原来那个检测分析引擎去跑。此时，大模型不会让你的检测引擎变好，而只是加速这个引擎的使用速度，降低引擎使用难度。而即便未来可以通过自然语言来生成检测/调查/猎捕的规则或代码了，对于分析师的业务领域技能的要求依然不会降低，因为如果分析师不能问出正确的问题，也不会得到预期的结果。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMeEziadp1sBictffc7G4iborx5ZVB1NtIcntQJqKU5GsMFbgAnMiczvZymwibSib4ian7fD67spYRDVVxGzA/640?wx_fmt=png&from=appmsg)

**GenAI赋能SOC的用例**

在本次峰会上，多位分析师都列举了自己心中的主要GenAI赋能SOC的用例，以下是笔者综合多位分析师观点的一份用例清单。注意，以下用例主要都工作在AI助理/副驾模式下。

1. 增强威胁检测能力：查询/规则生成、告警分析、告警信息解释、告警富化
2. 简化检测工程：生成检测代码/规则
3. 加速安全事件响应：事件解释、事件调查与信息增强、生成事件响应建议/计划/剧本
4. 提升工作流程效率：GenAI功能有机整合到现有UI中、工作流程提示
5. 加速SOC度量：总结事件响应过程、生成资产/漏洞/事件报告、生成日报周报等报告
6. 提供培训：培训新手使用本系统、安全运营实战教学、安全知识教学
7. 助力攻击面管理：资产/漏洞识别、资产/漏洞去重与合并
8. 简化情报分析：交互式威胁情报分析
9. 辅助攻击演练：生成攻击场景、攻击模拟、桌面推演

**SOC使用GenAI的禁忌**

Gartner对GenAI一向特别谨慎，因为GenAI本身存在很多不确定性（譬如准确性、可解释性、可信度、隐私问题等）。Gartner不断敬告大家，使用Gen...