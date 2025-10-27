---
title: 美国NIST《网络安全应用框架：空间运营地面部分》概述
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507495&idx=4&sn=3e7c8fa813680ef00f1987d8d28832a1&chksm=ebfa9907dc8d1011904c6ce7390392a5cca33b0bc29d356785f5b2073560473706c744b7e636&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-01-10
fetch_date: 2025-10-04T03:26:01.258279
---

# 美国NIST《网络安全应用框架：空间运营地面部分》概述

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7trvJgibmicXIFEmaUbjR4V9icTPax2icoLibONic6TRrBbJCdHGMSPIRqwib1uAf9XQk9iaQ9BZNG4PXwBUw/0?wx_fmt=jpeg)

# 美国NIST《网络安全应用框架：空间运营地面部分》概述

安全内参

编者荐语：

NIST IR 8401旨在将网络安全框架应用于卫星指挥和控制。

以下文章来源于天极智库
，作者天极智库

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5dzD2ESOGjvojqJicV8hhMMBdfukZNdBrKk4saLxLafeg/0)

**天极智库**
.

聚焦网络空间安全，提升科技能力建设

“

**天极按**

近日，美国国家标准与技术研究所（NIST）发布了《网络安全应用框架：空间运营地面部分》。NIST广泛使用的网络安全框架包括保护关键基础设施的标准、准则和实践，该自愿性框架旨在帮助组织管理其网络。

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhfntLibySyNZWmgpuwOO7CgvE2Dvmhyn6TFmarw7PXibUUh4PYUSibYQMw/640?wx_fmt=png)

NIST机构间报告（IR）8401旨在将网络安全框架应用于卫星指挥和控制，为空间部门的地面部分创建一个配置文件，努力帮助利益相关者管理风险。该简介的目标是补充一个组织中现有的安全措施。美国政府将空间视为关键基础设施中一个日益重要的元素，NIST的指导意见就是对此的回应。政府拥有的空间业务可以通过租赁商业通信卫星（COMSAT）带宽、商业天基电信服务、购买商业图像以及使用商业卫星总线来承载有效载荷和其他能力等活动得到增强。该机构指出，由于尺寸、重量和功率的限制，在卫星上实施无法实施某些网络安全控制的，因此该指南侧重于空间运营的地面部分。

NIST新的网络安全框架简介可以帮助拥有或运营空间系统的组织确定与空间飞行器总线和有效载荷的指挥和控制有关的系统和流程，识别威胁，保护系统，检测保密性、完整性或可用性的损失，应对事故，并从异常情况中迅速恢复。该简介侧重于两个主要部分：任务操作中心（MOC），它向卫星控制数据处理平台发出指令，并接收来自空间飞行器总线的遥测数据；以及有效载荷控制中心，它与MOC和卫星都进行通信。NIST指南详细说明了网络安全框架的五个核心功能的每一个：识别、保护、检测、响应和恢复。本文件的范围是商业空间地面部分的运行阶段。虽然范围被定义为地面部分，但空间部分的网络安全要求可能会影响到地面部分。空间飞行器有严重的尺寸、重量和功率（SWaP）限制，由于这些限制，在卫星本身实施一些网络安全控制可能是不现实的。应该考虑采取措施，使地面部分能够代表空间飞行器改善安全状况。

目的和目标

卫星地面部分网络安全简介（以下简称简介）旨在作为风险管理计划的一部分，帮助各组织管理构成卫星运行地面部分的系统、网络和资产的网络安全风险。该简介为以下方面提供指导：

* 对卫星指挥、控制和有效载荷系统的系统、流程和组件进行分类，以确定网络安全风险态势，并解决空间段管理和控制中的剩余风险；
* 为卫星指挥、控制和有效载荷系统的系统、程序和组件定义一个理想的网络安全状态；
* 建立明确的和可重复的风险管理方法，将实际的网络安全状态提升到理想的网络安全状态。

该简介并不作为一个合规检查表，本文件也没有定义具体的要求，以保证运行系统的可接受的剩余风险水平。使用该简介将帮助各组织。

* 识别系统和流程，以实现对空间运载工具和有效载荷的指挥和控制，并确定性能要求；
* 确定对卫星地面部分和支持基础设施的已知和预期威胁；
* 通过政策、培训、复原力和访问控制来保护地面部分所依赖的系统；
* 检测地面部分的保密性、完整性或可用性的损失；
* 及时、有效、有弹性地应对遥测、跟踪和指挥（TT&C）的保密性被破坏以及卫星指令或遥测的操纵或丢失；
* 及时、有效、有弹性地从异常情况中恢复。

使用范围

## 基线概况着重于卫星地面部分的两个组成部分，如图1左侧所描述。

* 任务操作中心（MOC），向卫星控制数据处理平台发出指令，并接收来自空间飞行器总线的遥测信息；
* 有效载荷控制中心（PCC），可向寄存在不同组织的总线上的有效载荷发出指令并接收响应（即，有效载荷驻留在空间飞行器上，而空间飞行器的总线操作由独立的MOC执行）。(请注意，图1是一个简化图。航天器上可能有多个有效载荷，对应于多个PCC，或者可能有多个PCC与一个MOC对接)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhhvlG9l0UaJvm4sUbfia1TuXfMibtNCWOzrseqNVQD4sric5SicIibTiaNydQ/640?wx_fmt=png)

图1.商业空间运营的卫星地面部分组件

该简介的范围包括任何与卫星总线或有效载荷互动的系统、网络或能力，用于查询、指挥、控制和状态（C&S），或指挥和控制（C2）。图2显示了哪些组件在简介的范围内和范围外。范围外的项目被单独评估和管理，因其可能存在不同的需求和影响。

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhXQAC2yAg16xUmQ4iaphmmNkRZDU92cZOIDv0v4icuaK8RBP98pbMBJNg/640?wx_fmt=png)

该范围不包括空间飞行器本身或空间系统的用户部分，支持利益相关者的能力。

* 对地面部分的网络安全及其对空间部分的总线和有效载荷的相应影响做出有风险的决定；
* 选择基于风险的方法，最大限度地减少破坏或操纵卫星总线和有效载荷的指挥和遥测的潜在影响；
* 考虑有关空间部分的安全管理和恢复的规划和行动；

目标受众

目标受众包括拥有、运营或管理空间系统并寻求评估或提升其当前安全态势的公共和私营组织。

* 风险管理人、网络安全专业人员，以及其他在地面系统风险管理中发挥作用的人员；
* 研究空间系统和空间网络生态系统的独特网络安全需求的研究人员和分析人员；
* 适用于具有不同程度的风险管理经验利益攸关者，包括具有以下特点的组织：
* 已经采用NIST网络安全框架来帮助识别、评估和管理网络安全风险；
* 熟悉网络安全框架并希望改善其风险状况；
* 不熟悉网络安全框架，但需要实施或加强风险管理工作。

预期用途

## 企业可以将其作为其风险管理工作的一部分，旨在增强而不是取代这种工作。同时有助于根据业务目标对网络安全活动进行优先排序，并确定标准、实践和其他指导可以帮助管理风险的领域。

**1****风险管理**

### 风险管理是识别、评估和应对与一个组织的任务目标有关的风险的持续过程。为了管理风险，组织应了解任何潜在的影响以及事件发生的可能性，还应该考虑可能影响或告知网络安全决策的法定和政策要求。该简介为利益相关者提供了一个灵活的方法，以便在与卫星总线或有效载荷接口时管理风险。同时提供了一个起点，各组织可以从中定制自身的风险管理方法。旨在与现有的风险管理流程一起使用，以提供额外的风险管理考虑。

**2****网络安全框架**

### 通过行业和政府之间的合作，网络安全框架[NIST-CSF]提供了基于现有标准、准则和实践的优先、灵活、基于风险和自愿的指导，以帮助企业更好地理解、管理和沟通网络安全风险。网络安全框架包括三个主要部分。

1. 该框架的核心提供了一个使用通用语言的理想网络安全活动和结果的目录3。该核心指导组织管理和减少网络安全风险，以补充组织现有的网络安全和风险管理流程；
2. 该框架的实施层为组织如何看待网络安全风险管理提供了背景。这些层级有助于组织了解是否拥有一个有效的和可重复的网络安全风险管理程序，以及网络安全风险管理与更广泛的组织风险管理决策的结合程度；
3. 框架概况是根据核心的结果定制的，以符合组织要求。预案主要用于确定和优先考虑改善组织的网络安全的机会.

该框架的核心部分在五个并行和连续的功能中提出了标准、准则和实践，这些功能如下所述。

1. 识别：发展组织理解，以管理系统、资产、数据和能力的网络安全风险。识别功能中的活动是有效使用网络安全框架的基础，使一个组织能够以符合其风险管理战略和业务需求的方式关注并优先处理其工作；
2. 保护：制定和实施适当的保障措施，以确保关键基础设施服务的提供。保护功能中的活动支持限制或遏制潜在网络安全事件的影响的能力；
3. 检测：制定和实施适当的活动，以确定网络安全事件的发生。检测功能中的活动能够及时发现网络安全事件；
4. 响应：制定和实施适当的活动，对发现的网络安全事件采取行动。响应功能中的活动支持遏制潜在网络安全事件的影响的能力；
5. 恢复：制定和实施适当的活动，以保持弹性，并恢复由于网络安全事件而受到损害的任何能力或服务。恢复功能中的活动支持及时恢复到正常运作，减少网络安全事件的影响，并为整体改进提供洞察力和指导。

当考虑到这些功能时，这些功能为一个组织的网络安全风险管理的生命周期提供了一个高层次的战略观点。然后，框架的核心部分为每个功能确定了基本类别和子类别。108个子类别是离散的网络安全成果，被组织成23个类别，如"资产管理"和"保护性技术"。图3描述了该框架核心的基本结构。

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhv65ibr6J7yNBDiaPVKOyhibgia1QH4TopMVCSpaHqMg4NaWQBfA6StOGEA/640?wx_fmt=png)

图3.框架核心的结构

网络安全框架是基于结果的，重点是网络安全功能，而不是组件。网络安全框架简介并不打算提供具体的实施指导；然而，简介将提供现有标准、指南和实践的信息参考，为组织实现每个子类别的预期结果提供实际指导。图4显示了资产管理类别中两个子类别及其信息参考的例子。

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhvtmRib4dGelyIhjB2EiccMe3QEy3GGS1ADcPQsnTUrA0DXTY2o6hiaTwQ/640?wx_fmt=png)

网络安全框架简介是在网络安全框架的核心范围内对一个组织的评估。目标是由组织选择的一套子类别，它与组织有关，以实现理想的网络安全状态。当一个目标子类别在当前配置文件中缺失或没有得到充分实施时，就会出现偏差。网络安全框架就其目的和使用提供了额外的指导。

**基线概况**

## 本节通过使用网络安全框架创建，表格总结了一个功能的类别中的子类别。根据设计，网络安全框架具有内在的灵活性，以适应不同组织的独特环境和需求。企业与本简介中的假设之间的偏差将影响子类别的适用性。因此，建议利益相关者在其组织的背景下审查所有的子类别。

**0****1**

**识别功能**

### 识别功能是风险评估过程的基础；风险管理从业人员应该从识别功能开始。为了管理风险和资产，首先必须对它们进行识别。对组织的任务和业务目标、威胁环境、资产和脆弱性的考虑将对整个风险管理决策产生重大影响，也将影响其他四项功能（即，保护、检测、反应、恢复）。识别功能的目标包括：

* 确定业务或操作环境和组织的目的；
* 确定所有资产，包括硬件、软件、人员、角色和责任，以及资产的重要性。
* 确定提供地面部分功能的基础设施；以及
* 确定当前和趋势的脆弱性、威胁，以及威胁实现后的影响，以评估风险。网络安全框架中的识别功能定义了六个类别，在表1中进行了总结。每个类别至少有一个适用于地面部分的子类别。然而，组织应审查识别功能中的所有子类别，以防其中任何一个适用于组织的环境。

网络安全框架中的识别功能定义了六个类别，在表1中进行了总结。每个类别至少有一个适用于地面部分的子类别。然而，组织应审查识别功能中的所有子类别，以防其中任何一个适用于组织的环境。

表1.识别功能的基线概况

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhdwz5G7Ge91wmH8ZsKMTE15icvUcXO3qVibCeprbyxxl0xxrwFIjO0MAA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickh7icGDSUVTT90j6EQkeZMIFoXicNmXXeRg8adCNlhWiaR2ibmUiabqBEr6jg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhjMHppagOegfQakqSTCoeicwzxth7BPDgnicP6PjsTtbz6CQJKAAB2p5g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhTYfC3OrRHACqpe9v2icAmKoDib49vKXBaRZ8mKw68PayxTAy5ibhYv74g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickh9fJoNiblMPba4pbfM7Y1NZnbzNIXwkmwNcHw2r879TxZgAFSDibTOaPw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickh3gpn8UNvic0sHruML8LHBr1LJzc4Ykvta0lx4qfnWT35QcvvbxUALUw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhgd5aPVC8zoliarf0uWLK6r44MsCTZwS9TxF1IZK2ibKBR6l5gxvX83DQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhqBPL9g60UCZQkKhCmhpAUPu97BPyLqg4gpzUe7M1BX60aWBRt52p6A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhQs0YwaLdOAfw9PZ4tVscYibnseoHbibn0jHXic9gOt66JU7C7CrSjQicjg/640?wx_fmt=png)

**0****2**

**保护功能**

### 保护功能包括：开发、实施和验证措施，以防止地面部分的保证或功能的丧失。此外，保护功能还包括：通过计划和准备活动实现对网络安全事件的响应和恢复，而风险缓解的执行则在响应和恢复功能中解决。地面部分正变得逐步依赖互联和基于云的地面基础设施，然而，传统的空间操作和空间飞行器本身使用定制的软件和硬件，这些软件和硬件通常不是为成为现代高度互联的网络生态系统的一部分而创建的。

保护功能的目标包括：

* 保护格式化和传输命令的系统，使其达到所需的保证水平；
* 保护接收和处理来自卫星的遥测或其他数据的系统；
* 如果威胁发生了，保护地面部分，以通过经核实的反应和恢复计划保持足够的操作水平，并防止对空间部分的不利影响。

保护功能定义了六个类别，在表2中进行了总结。每个类别至少有一个适用于地面部分的子类别。然而，各组织应审查保护功能中的所有子类别，以防其中任何一个适用于本组织的环境。

表2.保护功能的基线概况

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickh4nxt6nsbdA6yCtKbF5wGIHd2fcWvBX8b9mKiaAsiaGVKMesAE8vhaSVw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhE69Vu4JTqI9VPGfk6uZDb0ukVv2cicOMJnNg4iaxeh8bDAaxIibeFicuuA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhdCDjxXiaqMBxXpj3rYIV99SGKiaomRWicjgibG5E0qSu96lrQUkcYcPmKA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickh8BY7nGSuedseogxIdhiagsqQDfhTEjibK68q0Xz4aItwfI4ia042wj6Og/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhk4SbYkQglN0PnG54VQJPLHDFAUXBkwb1w9GgS4acoXKnxFbbVdJlKQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhe4E0wrCYfqnuEFs68b228oxlrzr3s2vekEeSQeXiatnS7BibC9hFEA4Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGDYKHjOZyCPddkfhGwVJYnRrWickhEAKYxFVn2G6uZrcgPkgRohyNrqib9JHib3ZzNJn88pZ5j0pm5R34icw9Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/VIQiaGD...