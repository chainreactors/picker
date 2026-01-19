---
title: 汽车电子电气TARA分析
url: https://mp.weixin.qq.com/s/BZU1BthRyKF7oX5yJ_j7nA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:37:02.360931
---

# 汽车电子电气TARA分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icdSQzSHVoHVksVPW599ZzcLo4pkXkvcxiczH8duFtN1Q00t933DK0twg/0?wx_fmt=jpeg)

# 汽车电子电气TARA分析

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**01**

**概述**

TARA，全称Threat Analysis and Risk Assessment，威胁分析与风险评估，是汽车电子电气架构中常用的网络安全威胁分析与风险评估方法论。TARA从道路交通参与者角度，确定道路交通参与者受威胁场景影响的程度。

如下图所示，在ISO/SAE 21434中，作为最后一个章节出现，主要包含了资产识别、威胁场景识别、影响等级、攻击路径分析、攻击可行性等级、风险评估上确定、风险处置决策，共7个基本的步骤。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icLSD5zafQiawBPXAYNLAYo5czGd4PYTxFbsZbZXic64X55VOet2BagfbA/640?wx_fmt=png&from=appmsg)

对应着上述七个步骤，TARA分析有七项基本目标：

* 识别资产，它们的网络安全属性，以及它们遭受损害的场景；
* 识别威胁场景；
* 确定损害场景的影响等级；
* 识别实现威胁场景的攻击路径；
* 确定攻击路径实施的难易程度；
* 确定威胁场景的风险值；
* 为威胁场景选择合适的风险处置措施。

**02**

**资产识别**

在资产识别环节，需要识别出TARA目标范围内那些具有网络安全特性的资产，这些资产的网络安全特性遭到破坏时可能产生一些损害场景。通常情况下，这里指的是软性的信息资产（或称为数据资产），在某些特殊情况下，也可能会是硬件资产。

例如，IVI中存储的个人搜索历史记录。这明显是一种资产，该资产对应的需要保护的网络安全属性主要为机密性。损害场景是，当该资产的机密性遭到破坏时，会产生未经数据主体同意的个人敏感信息泄露（这些搜索历史可能反应数据主体的政治倾向、宗教信仰、性取向等等）。

再比如，刹车系统的控制信号，该资产的完整性需要被妥善保护。损害场景是，当刹车系统的控制信号被篡改后，驾驶员的刹车控制指令无法被正确的传送到制动器，导致刹车失败、追尾等严重事故。
如下表所示，资产识别阶段需要确定的主要内容如下。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icibgD9aHtus1GhaIjKaLW1zKjicibiceok8Fy4Ja83mzALHEiaQuUT56HcoA/640?wx_fmt=png&from=appmsg)

**注意：对于上面所述的网络安全属性，最基本的是CIA三元组（Confidentiality-保密性，Integrality-完整性，Availability-可用性），除此之外，还可以衍生出真实性（Authenticity）、不可抵赖性（Non-Repudiation）等。**

**03**

**威胁场景识别**

在威胁场景识别环节，也可以包括或者关联其它更进一步的信息。例如，损害场景，以及资产、攻击者、方法、工具、攻击面之间技术上的相互依赖性。另外，威胁场景识别可以使用小组讨论的方法，也可以使用诸如EVITA、TVRA、PASTA、STRIDE等系统化的威胁建模方法。

针对威胁场景的描述，主要包括三个方面的内容：目标资产、破坏的网络安全属性、对应的危害场景。例如，针对制动ECU的CAN消息欺骗，可以导致CAN消息的完整性丧失，从而导致制动功能的完整性丧失。

如下表所示，威胁场景识别阶段需要确定的主要内容如下。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icyicgRfXnl7cKgqVRphhTaSEPqqjPhq0H57MWQicrE1WxrCd7Dkspibftg/640?wx_fmt=png&from=appmsg)

**注意：一个损害场景可以对应多个威胁场景，反之，一个威胁场景也可以导致多个损害场景。**

**04**

**影响评级**

在影响评级环节，主要从道路使用者可能受到影响的四个维度进行评估：安全（Safety）、财务（Financial）、运行（Operational）、隐私（Privacy），简称SFOP。但是在ISOSAE 21434中也明确说明了这一块：首先，不考虑这四个维度之间的相互关系（比如加权）；其次，可以考虑引入这四个维度之外的其它影响因素。

在对损害场景的影响评级时，除了考虑这几个维度之外，还需要确定每个维度的影响级别，比如：极其严重（severe）、高（major）、中等（moderate）、忽略不计（negligible）。

如下表所示，影响评级环节，需要确定的内容如下。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4iczMTyOp4icFDzLr7sfALYVo0fvekGrJMSbfr0osicNV7l9AibyoDVYMOQg/640?wx_fmt=png&from=appmsg)

**最佳实践说明**

为了能够在实施过程中更加顺畅，整体上更加客观（尽管整个评级过程中带有TARA分析人员的较大的主观因素），在实施过程中一般会对SFOP的四个维度赋予不同的权重，这取决于组织在这四个维度上差异化的风险偏好。另外，对于每一个维度中的几个影响级别（可以定义更加精细化的级别）可以赋予不同的分值（可以使用5分制、10分制、100分制等），不同维度上的相同影响级别可以赋予不同的分值，这也跟组织的风险偏好以及目标产品的特点有关系。因此，最终在组织中实施TARA的时候，需要确定的信息可能是如下的形式。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icQYHZnicHYibcJOpkBWXMJyiah5fxeNEldQ2YC1Z38L5W4DCc5qGnWK0Fg/640?wx_fmt=png&from=appmsg)

下面会从SFOP的四个维度分别进行阐述。

**4.1 安全-Safety**

对于Safety维度的影响评级，重点参照了ISO 26262-3:2018，另外也可以参照该标准中的可控性和暴露度进行影响评级。安全评级的基本定级规则如下表所示。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icibTlJqmP1YLTPyp93Sa30YHYNUZ4hQibflzYCEK9aELpv0cpMoLzbAVA/640?wx_fmt=png&from=appmsg)

**4.2 财务**

对于财务维度的影响评级，可以遵循如下表所示的原则。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icRsZ3PJxZCrNGyicAxGOR860kdBrJHXjanuibb9w4qWoY5wCPnoJqLrcw/640?wx_fmt=png&from=appmsg)

**4.3 运行**

对于运行维度的影响评级，可以遵循如下表所示的原则。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icvDxx6j2bZeQmbNHcW0vicUjO1OvMWr1MtIbFujcXFm7YJgicMmsRuyvw/640?wx_fmt=png&from=appmsg)

**4.4 隐私**

对于隐私的影响评级，可以遵循如下表所示的原则。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icibCp6PwnBn8SmIh3xgDSujKWeE0G1icic4F8Fts6Gaeej7lm8PticKTjmw/640?wx_fmt=png&from=appmsg)

**注：在ISO 21434中，相关信息关联到的自然人统一称为“PII principal”，有的地方翻译成PII（Personal Identifiable Information）主体，个人总感觉比较拗口，这里统一采用GDPR的称谓-数据主体（data subject）。**

**05**

**攻击路径分析**

在攻击路径分析环节，需要参照项目的定义文件，或者产品的网络安全specification。除此之外，攻击路径分析中还可以参照已知网络安全事件中的脆弱性、产品开发过程中发现的脆弱性、架构设计文档、之前识别到的相关的攻击路径，以及可能的脆弱性分析等。

从方法论上来讲，主要采用自顶向下和自底向上两种方法实现。

**自顶向下**

分析威胁场景的各种可能的实现方式，并以此推理攻击路径，典型的如攻击树方法、攻击图方法。

**自底向上**

这种情况比较单一，主要是基于已知的漏洞构建攻击路径。

在攻击路径分析中，建议使用“威胁源，攻击面，攻击向量”的模式来描述一条攻击路径。 比如“攻击者通过在CAN总线上发起泛洪攻击，导致制动踏板的指令无法到达制动执行器，从而造成制动功能失效”。

如下表所示，在TARA分析过程中，一般会通过威胁场景ID和攻击路径关联起来。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icOY7C5wM7dgxKdAarUrSpF4z0TyMU8RRqU1kw8RsV6IicthCiauIW06Eg/640?wx_fmt=png&from=appmsg)

**06**

**攻击可行性评级**

攻击可行性评级的主要目的是，给每条攻击路径确定一个攻击可行性的等级。具体的攻击可行性等级，可以基于组织的需要来定义，比如高、中、低。

更进一步，攻击可行性评级的方法有多种，比如基于攻击潜力、基于CVSS、基于攻击向量等。 ISO/SAE 21434中指出可以基于这三种方法中的任何一种进行攻击可行性评级。

**6.1 基于攻击潜力的方法**

主要包括了，攻击所需要的时间、需要的专业知识、对攻击对象的了解程度、攻击的机会窗口，以及攻击所需要的设备的专业度。

**注：在ISO 21434中，针对攻击潜力的所有维度的打分值不太统一，也相对比较凌乱，对于初上手的人来说不太好理解。因为从方法论的角度讲，这些分值都是可以根据组织的情况进行自定义的，博主个人建议还是采用统一的百分制打分更加通用。**

**6.1.1 所需的时间**

攻击所需的时间包括了识别漏洞以及利用漏洞的时间，因此针对这个参数的打分本身也是基于打分时的专家知识状况。例如可以分成如下几个阶段进行打分。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4ic45HrJJxiafA5yt9LRt1lT8KykltHbuNVfSKYq5iaBvIt6mFpibQy34SHw/640?wx_fmt=png&from=appmsg)

**6.1.2 专业知识**

专业知识参数跟攻击者的能力和经验都是有关系的，可以分成如下几个层次进行打分。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icnjxiaSQt8Uic9ibgFiaN8Pk8IQvINF93K7BrLQ9cy9LCr6vCx9GoR2teibA/640?wx_fmt=png&from=appmsg)

**注：这里指的主要还是在网络安全领域或者渗透测试领域的专业知识，注意区别于下面针对攻击对象的专业知识。**

**6.1.3 针对攻击目标的专业知识**

对攻击对象的了解程度跟攻击者获取的攻击对象相关的信息的详细程度（或者说信息量）有关系。针对攻击对象的了解程度可以从如下几个层次进行打分。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icIUZ4iaJkste7WfXmkWp6OzXU5XFEMETvPUgeehECmuw8dZ8LvEmenUg/640?wx_fmt=png&from=appmsg)

**6.1.4 机会窗口**

机会窗口与成功实施攻击的访问条件有关系，比如时间、类型等。机会窗口结合了访问控制类型（如逻辑的、物理的）、访问时间（如受限的、不受限的）等等。依赖于攻击的类型，可能包括发现可能的目标、侵入目标、对目标的勘探、对目标实施攻击的时间、保持不被发现、规避检测与控制等等。针对机会窗口，可以从如下几个层面进行打分。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4iciaQm2ojKib8qgvxQodjLgMzQYib0F3ecs2ZYiavUvQibnibMVaEmnPgU2SoQ/640?wx_fmt=png&from=appmsg)

**6.1.5 设备工具**

攻击采用的设备工具可以有如下几个层次的打分。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4ic62C3FFbw4h905ic7QXUAfwbOOqbJLagVCY9XtCMROQnchlYovwWDbRQ/640?wx_fmt=png&from=appmsg)

**6.1.6 基于攻击潜力的攻击可行性评级**

与影响评级一样，攻击可行性评级的时候，每一个维度的权重，以及每一个维度的分值定义，在没有强制（或通用）标准的情况下，组织可以根据自己的实际情况来定义。下图展示了采用基于攻击潜力的方法进行攻击可行性评级，并且为每个维度赋予了不同的权重。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icZlTd5HIb7icNn8EE2l553mjqYiaBmXx7Z9H0iavIqk0DvBfNlGQ0e85fw/640?wx_fmt=png&from=appmsg)

**6.2 基于CVSS的方法**

为了评定信息技术的安全漏洞，常用的方法是CVSS。在CVSS的基本指标组中的“可利用性指标”可以用来评估攻击的可行性。可利用性指标主要包括：攻击矢量、攻击复杂性、需要的特权、用户互动。

对于CVSS指标的评估，需要根据预先定义的范围，为每个指标设定数字值。整体的可利用性指标值可以根据下面的简单公式计算产生。

**E = 8.22 × V × C × P × U**

其中，E是整体可利用性指标值；V是攻击矢量指标值，范围是[0.2, 0.85]；C是攻击复杂性指标，范围是[0.44, 0.77]； P是所需特权的指标值，范围是[0.27, 0.85]；U是用户互通的指标值，范围是[0.62, 0.85]。这样一来，可利用性指标的范围在[0.12, 3.89]。

下表是ISO 21434中给出的CVSS可利用性指标与攻击可行性之间的映射示例，每个范围都是等距的。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4ic1f4vxaPjYd89rb8Xz3GZTYf0KiaXOQtaV9y3Th3f2SbkPHXqax7ib9UA/640?wx_fmt=png&from=appmsg)

**注：只采用可利用性指标本身并不是严格符合CVSS对指标的要求。因此在ISO 21434中，缺失的影响度量可以用其它方式进行补偿。 理论上来讲，CVSS的可利用性指标是一个不错的工具，还可以用来评价概念性的弱点、缺陷等。**

**6.3 基于攻击向量的方法**

主要是通过评估攻击路径中的主要攻击向量，来确定攻击的可行性等级。基于攻击向量的方法反映了攻击路径可能被利用的场景。 对于攻击可行性评级来说，攻击者在越远（可以是逻辑的，也可以是物理的）的地方利用攻击路径，可行性评级就越高。这里假设从网络上利用漏洞的潜在攻击者数量大于从物理上访问攻击对象的潜在攻击者数量。下表展示了基于攻击向量的方法中，攻击可行性评级与攻击向量之间的映射关系。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icLRDgh70KoshJUbNEWPGsNxbAKDR4ZpbrY03nT2GWLbHDUrPz29m2tg/640?wx_fmt=png&from=appmsg)

**07**

**风险值确定**

对于每一种威胁场景，需要根据其相关损害场景的影响，以及相关攻击路径的攻击可行性来确定风险值。

如果一个威胁场景可以对应一个以上的损害场景；或者一个损害场景在一个以上的影响类别中产生影响，则建议给每个影响等级单独确定一个风险值。

此外，如果一个威胁场景可以与一个以上的攻击路径相对应，则可以将相关的攻击可行性评级结果酌情汇总，比如将攻击可行性评级最大的攻击路径赋予威胁场景。

威胁场景的风险值应设置在[1, 5]上，其中1代表最小的风险，5代表最大的风险。

在实践中，可以使用风险矩阵法或定义好的风险公式来确定威胁场景的风险值，风险矩阵法比较常用。下图所示的是ISO 21434附录中给出的...