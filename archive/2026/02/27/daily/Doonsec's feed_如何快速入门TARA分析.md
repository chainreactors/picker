---
title: 如何快速入门TARA分析
url: https://mp.weixin.qq.com/s/qpW-WP1KeS7DGGaMRLaf8g
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:54:42.678661
---

# 如何快速入门TARA分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDD7yWYx6ADe7xLV5d2S5AFr6NJrAoBAmUUfsxuiahR0rTeibxls5D7POFJ66HA4KaicpUGuIQnoKEVkO1zJF5HCB6zhWiciaPibjEIo/0?wx_fmt=jpeg)

# 如何快速入门TARA分析

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247566311&idx=2&sn=27d2cf53ef824bfde9b824f90e864ec6&scene=21#wechat_redirect)

在当今信息化时代，车联网与智能车的有机联合，其搭载了先进的车载传感器、控制器、执行器等装置，能够与外部网络、道路基础设施以及其他车辆进行实时通信和数据交换，因此汽车承载的代码量比以前多了很多，以前传统燃油车上的代码量是1亿，现在我们平时用到的多功能，在车上可以听音乐，可以看视频，大概有4亿到5亿的代码量。到2025年，预测代码量会超过10亿，不仅有娱乐功能，而且智能驾驶本身所消耗的代码量很多，因为有一些本地的算力、模型等不是实时上云的，也有一些上云的交互。在这么多代码量的新势力软件定义汽车的发展下，汽车网络安全问题日益突显，已经成为企业和个人必须面对的重要问题。

为了保护汽车网络安全，OEM及Tier1均需要进行威胁分析与风险评估（TARA），以便及时发现和解决潜在的安全威胁。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGhbgdyIfn6GPIVakicI8cUZ4DlPlyRoBacSDicmbpIAjEMoKaQCkGWkIrg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**01**

**什么是TARA**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGh7VicmtHqqbjQZoJSMxdicsgsoLL8qHAryhlm8LnKWJcPjI8DpF93J4lA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

TARA全称Threat Analysis and Risk Assessment，威胁分析与风险评估，是汽车电子电气架构中常用的网络安全威胁分析与风险评估方法论。TARA从道路交通参与者角度，确定道路交通参与者受威胁场景影响的程度。在ISO/SAE 21434中，作为最后一个章节出现，主要包含了资产识别、威胁场景识别、影响等级、攻击路径分析、攻击可行性等级、风险评估上确定、风险处置决策，共7个基本的步骤。

TARA始于概念阶段，严格意义上来说应开始于产品立项的早期阶段，此时的整车应具备初始的电子电器架构，即高级抽象阶段的EE架构。这样，TARA才会有具体的分析对象。TARA是一个全面的、系统化的安全分析方法并贯穿整个产品生命周期，从而确保产品的网络安全性得到全面的保障。

* 在设计阶段，TARA可以帮助设计人员识别潜在的安全风险和漏洞，并提供相应的解决方案。
* 在开发阶段，TARA可以帮助开发人员进行代码审查和漏洞修复，确保代码的安全性。
* 在测试和验证阶段，TARA可以帮助测试人员进行安全测试和验证，确保产品的安全性符合预期。
* 在运维阶段，TARA可以帮助维护人员进行漏洞修复和安全更新，确保产品的安全性得到持续的保障。

**02**

**OEM和Tier1在TARA分析上的关联和差异**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGheHcBViaib8bvLVnXmFzZyxUbOXRsqXneQy69IRcJSXhZg6nMVYXKUFJw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

为了保障汽车的安全性和可靠性，汽车制造商和零部件供应商都在积极开展TARA工作，那他们之间的区别和联系分别是什么呢？

OEM作为汽车产业链的上游，它首先要从整车的角度去开展TARA评估工作，识别潜在的安全威胁和漏洞，并确定每个威胁的风险等级和优先级。

OEM识别网络安全目标，并将其转换为车辆网络安全需求并分发给对应的零部件供应商。

Tier1需要遵守OEM分发的车辆网络安全需求，同时也需要从零部件的角度出发，识别零部件层面的风险，最后需要根据不同的安全需求制定合适的安全措施。

最后，Tier1需要对自己的产品进行测试，确保符合网络安全的要求，并支持OEM在整车层面的网络安全测试。

**03**

**TARA分析的框架‍**

TARA是ISO 21434框架中的一个重要组成部分，是一种系统化的方法，用于识别和评估可能对汽车网络安全系统或个人造成威胁和风险的潜在因素。

通过TARA分析，可以帮助汽车软件供应商评估网络安全的脆弱性，理解潜在威胁，并制定相应的风险管理措施。关于TARA分析报告，其主要内容如下：

1）汽车软件工程项目边界描述

2）项目网络安全涉及敏感数据保护描述

3）项目功能概述

4）项目数据接口描述

5）信息资产

6）资产损害场景影响等级评估

7）威胁场景识别和攻击路径分析

8）风险分析及对策

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGh1U64BxqFF4QWFCoGNFiaRPfYAGia3lqwE7QniciaG1iaIYv7awhfgBDmC4g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**04**

**事项定义（Item Definition）**

事项定义是TARA分析的第一步，也是非常关键的一步。它是整个TARA分析的基础，决定了后续分析的方向和深度。事项定义就好比是建筑高楼大厦时的打地基的环节，如果地基打得不牢固，那么整个建筑就会不稳定，甚至倒塌。同样地，如果事项定义不清晰、不准确，那么后续的分析就会失去方向，无法得出有用的结论。

首先，我们应该要清楚，什么是Item? 简而言之，一句话，Item就是我们分析的对象。

其次，Item Definition 需要做什么？具体地说，就是要明确我们保护的对象是什么？

为了能够清晰地回答上面提出的这个问题，减少工程师错误解读的可能性，我们需要一些最有价值的输入，包括但不限于：

●   EE架构图

●   系统架构图

●   功能描述及功能清单

●   数据流图

●   已部署的安全措施

…

除此之外，对于现阶段工作中不明确的因素（比如，某造型设计未做最终决定， 或者某技术未经验证等）可以做出对应的声明，即假设。

同时，对于需要考虑的客观情况，比如不是所有的ECU都能部署硬件安全模块（HSM），比如TARA分析时候要尊重高优先级ECU，比如法规要求、标准的要求等，也需要一一列出，即约束。

**05**

**资产识别**

在进行资产识别之前，我们需要完成Item definition，并经过专家团评审，这是因为Item definition是TARA分析的基础，只有Item definition完成后，我们才能更好地去识别Item的各种网络安全资产。

**首先，何为资产？**

资产是在Item definition后被识别出的需要被保护的任何数据，功能或者资源，分析对象的不同，资产也会有所不同。

资产识别没有标准化的方法，但可以从以下方面考虑，比如基于用户功能进行识别（如OTA， 诊断等功能）， 基于用途分类（如固件， 数据等）等。

请注意，当资产分析得到的资产列表过于繁杂庞大，最好的办法就是对资产进行分组。如果有内容相近的安全资产，可以考虑合并这些资产，以使分析更精简。如果资产具有相同的目标和相同的攻击路径，那么也可以考虑合并这些资产。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGhg2t0WKuQFXzY3G7ibOIz5xHntcZaoYmM3NhDFJOUUdFgqRcNZf01LZA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

其次，关于资产属性，网络安全属性三元素：机密性、完整性和可用性。其他网络安全属性，如真实性、不可抵赖及授权等，都是建立在这三个核心要素的基础上的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGhQOrWPt9icZoxRKWBGL08sicGBgyj5Eia1tNyIgknqMW8os7fmmTvib7E4w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

在资产识别环节，需要识别出TARA目标范围内那些具有网络安全特性的资产，这些资产的网络安全特性遭到破坏时可能产生一些损害场景。通常情况下，这里指的是软性的信息资产（或称为数据资产），在某些特殊情况下，也可能会是硬件资产。

例如，IVI中存储的个人搜索历史记录。这明显是一种资产，该资产对应的需要保护的网络安全属性主要为机密性。损害场景是，当该资产的机密性遭到破坏时，会产生未经数据主体同意的个人敏感信息泄露（这些搜索历史可能反应数据主体的政治倾向、宗教信仰、性取向等等）。

再比如，刹车系统的控制信号，该资产的完整性需要被妥善保护。损害场景是，当刹车系统的控制信号被篡改后，驾驶员的刹车控制指令无法被正确的传送到制动器，导致刹车失败、追尾等严重事故。

最后，在实际应用中，依据客户的需求，我们对不同资产的各网络属性进行分析。

**06**

**威胁场景识别‍**

在威胁场景识别环节，也可以包括或者关联其它更进一步的信息。例如，损害场景，以及资产、攻击者、方法、工具、攻击面之间技术上的相互依赖性。另外，威胁场景识别可以使用小组讨论的方法，也可以使用诸如EVITA、TVRA、PASTA、STRIDE等系统化的威胁建模方法。

威胁场景识别是指通过对环境、人员、设备等因素的分析，识别出可能存在的威胁场景，以便采取相应的安全措施。

这种方法可以帮助OEM或Tier1识别潜在的安全威胁，从而制定相应的安全策略和措施，保护企业或组织的安全和利益。威胁场景识别通常包括对物理安全、网络安全、人员安全等方面的分析。

对于威胁场景的识别，作为计划在欧洲市场销售汽车的OEM，需要考虑UNECE UN-R155法规附录5A中所列举的一系列威胁场景。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGhDEMlVTa5lN77icpbb5b5H8k4kNSjtico2cPZ1z8guLKsjRRn5c1CV7Hw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

针对威胁场景的描述，主要包括三个方面的内容：目标资产、破坏的网络安全属性、对应的危害场景。例如，针对制动ECU的CAN消息欺骗，可以导致CAN消息的完整性丧失，从而导致制动功能的完整性丧失。

而损害场景是指一个或多个安全目标受到攻击的现实情况。例如：知识产权或大批量用户账号的泄露可以作为典型的损害场景。

下面这些通用的损害场景可以作为参考：

* 对车辆，驾驶员，乘客或第三方造成危害
* 可利用该物品进行进一步攻击
* 侵犯隐私
* 功能限制或拒绝
* 操纵系统特性
* 虚假主张
* 知识产权泄露
* 品牌损害

注意：一个损害场景可以对应多个威胁场景，反之，一个威胁场景也可以导致多个损害场景。

**07**

**影响评级（Impact Rating）**

对于每个损害场景，影响等级是指成功发动一次攻击所造成的伤害，它是根据安全、财务、操作及隐私四个维度来评价的，各维度评价的标准即依据可参考下图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGhDKJCRjkz3KyBMf7LHOSILLBeLJa1VeOs13MJC7bialKQp3j7iatm2Iiaw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

但是在ISOSAE 21434中也明确说明了这一块：首先，不考虑这四个维度之间的相互关系（比如加权）；其次，可以考虑引入这四个维度之外的其它影响因素。

为了能够在实施过程中更加顺畅，整体上更加客观（尽管整个评级过程中带有TARA分析人员的较大的主观因素），在实施过程中一般会对SFOP的四个维度赋予不同的权重，这取决于组织在这四个维度上差异化的风险偏好。

另外，对于每一个维度中的几个影响级别（可以定义更加精细化的级别）可以赋予不同的分值（可以使用5分制、10分制、100分制等），不同维度上的相同影响级别可以赋予不同的分值，这也跟组织的风险偏好以及目标产品的特点有关系。

因此，最终在组织中实施TARA的时候，需要确定的信息可能是如下的形式。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGh3c0icypC7G9XA5iaa8L3VqAP9C3ib67twicaCdwAicdD52AibXSdye9iaBfVA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

**08**

**攻击路径分析**

在攻击路径分析环节，需要参照项目的定义文件，或者产品的网络安全specification。除此之外，攻击路径分析中还可以参照已知网络安全事件中的脆弱性、产品开发过程中发现的脆弱性、架构设计文档、之前识别到的相关的攻击路径，以及可能的脆弱性分析等。从方法论上来讲，主要采用自顶向下和自底向上两种方法实现。

* 自顶向下，分析威胁场景的各种可能的实现方式，并以此推理攻击路径，典型的如攻击树方法、攻击图方法。
* 自底向上，这种情况比较单一，主要是基于已知的漏洞构建攻击路径。

在攻击路径分析中，建议使用“威胁源，攻击面，攻击向量”的模式来描述一条攻击路径。比如“攻击者通过在CAN总线上发起泛洪攻击，导致制动踏板的指令无法到达制动执行器，从而造成制动功能失效”。在TARA分析过程中，一般会通过威胁场景ID和攻击路径关联起来。

威胁分析是以攻击树为核心的，攻击树是一种用于威胁建模和分析的图形化工具，它可以帮助识别和评估系统中的潜在威胁，并提供一种可视化的方式来描述攻击者如何利用系统中的漏洞来实现攻击目标。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGhm1kh0LDzUNSicA6Pg2y5B5Qmb0dOrIK67DX8YKaKSLQIovMz7IslMKQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

汽车TARA威胁分析采用攻击树的方式主要是因为攻击树具有的如下优势：

* 可视化：攻击树可以将复杂的威胁模型可视化，可以更加直观地了解系统中的威胁和漏洞。通过攻击树，可以清晰地看到攻击者如何利用系统中的漏洞来实现攻击目标，从而更好地评估系统的安全性。
* 层次化：攻击树可以将威胁分解为多个子威胁，并将其组织成一个层次结构，这种层次化的结构可以帮助更好地理解威胁的复杂性。
* 可重用性：攻击树是一种可重用的威胁建模工具，可以在不同的系统中使用，这种可重用性可以帮助更好地利用已有的威胁模型，从而更快地评估系统的安全性。
* 可扩展性：可以根据需要添加新的威胁节点，从而适应不同的系统和威胁模型。
* 可量化：攻击树可以实现量化威胁的风险和影响。通过对攻击树中的节点进行评估，可以计算出每个节点的风险值和影响值。
* 评分一致性：攻击树可以保证相同的攻击路径其攻击可行性评分保持一致。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ZhsBNqVmTQa3gTDLmGOGhcia51AiawRaqNLzBJicITCrdseo14kHgLgR2vhBJEemZzzK32ejnZIMHg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

**09**

**攻击可行性评级**

攻击可行性评级的主要目的是，给每条攻击路径确定一个攻击可行性的等级。具体的攻击可行性等级，可以基于组织的需要来定义，比如高、中、低。

更进一步，攻击可行性评级的方法有多种，比如基于攻击潜力、基于CVSS、基于攻击向量等。ISO/SAE 21434中指出可以基于这三种方法中的任何一种进行攻击可行性评级。

**基于攻击潜力**

主要包括了，攻击所需要的时间、需要的专业知识、对攻击对象的了解程度、攻击的机会窗口，以及攻击所需要的设备的专业度。

注：在ISO 21434中，针对攻击潜力的所有维度的打分值不太统一，也相对比较凌乱，对于初上手的人来说不太好理解。因为从方法论的角度讲，这些分值都是可以根据组织的情况进行自定义的，个人建议还是采用统一的百分制打分更加通用。

与影响评级一样，攻击可行性评级的时候，每一个维度的权重，以及每一个维度的分值定义，在没有强制（或通用）标准的情况下，组织可以根据自己的实际情况来定义。攻击可行性的评分是最核心的内容，因...