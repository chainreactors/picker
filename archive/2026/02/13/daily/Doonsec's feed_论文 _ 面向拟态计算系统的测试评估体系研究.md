---
title: 论文 | 面向拟态计算系统的测试评估体系研究
url: https://mp.weixin.qq.com/s/YcY3psV1oZNi-FOGeLNL1A
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:05:27.836159
---

# 论文 | 面向拟态计算系统的测试评估体系研究

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CKMdBPsMHD8opu6uicZObGpAKw1GWqoXP9ibcXMPRhjb5nCia27YlOG4BdqIvvv6tWh41FpiahUdW9yExQeMtgicPQDmnfJibJElh5cdT2atFo4jA/0?wx_fmt=jpeg)

# 论文 | 面向拟态计算系统的测试评估体系研究

内生安全联盟

![]()

在小说阅读器中沉浸阅读

以下文章来源于信息通信技术与政策
，作者贺倩，金伟 等

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM70svguaJUzoWS36OpWqXMM24ia4VlolVuDdAMHaVvREfA/0)

**信息通信技术与政策**
.

工业和信息化部主管、中国信息通信研究院主办的专业学术期刊。定位于“信息通信技术前沿的风向标，信息社会政策探究的思想库”。

**作者简介**

**贺倩**

中国信息通信研究院安全研究所网络安全部高级工程师，主要从事网络安全领域的相关研究工作。

**金伟**

中国信息通信研究院安全研究所网络安全部工程师，主要从事网络安全、数据基础设施领域的相关研究工作。

**徐昊天**

之江实验室高级研究专员，主要从事二进制安全与物联网安全领域的相关研究工作。

***论文引用格式：***

贺倩, 金伟, 徐昊天. 面向拟态计算系统的测试评估体系研究\*[J]. 信息通信技术与政策, 2025, 51(10): 40-44.

**面向拟态计算系统的测试评估体系研究**

**贺倩1  金伟1  徐昊天2**

（1 中国信息通信研究院安全研究所，北京 100191；

2 之江实验室，杭州 311121）

**摘要：**随着各项新型技术的快速发展，日益增长的计算资源需求与当前有限的计算资源和固化的分配模式产生了一定的矛盾，优化计算资源分配、提升计算资源利用效率成为亟待解决的问题。拟态计算系统通过异构资源按需分配、硬件资源池化、动态重构资源等机制能够灵活快速高效地分配计算资源，充分发挥计算资源执行效率，大幅提升系统整体计算能效比。通过梳理测试评估指标、建立测试评估模型、开展应用场景实践进行拟态计算系统测试评估体系的研究，从而明确拟态计算系统功能的先进性以及对于计算效率的提升情况。

**关键词：**拟态计算；拟态计算架构；测试评估体系

**0  引言**

人工智能、云计算、移动通信等各项技术的广泛应用，在带来技术变革和科技增益的同时还产生了巨大的计算资源需求。计算资源作为推动新技术创新和产业发展的关键基础，目前存在资源分配不均衡、利用效率偏低等问题，制约了技术的进一步创新。拟态计算系统能够动态化改变计算结构，并结合相关软硬件使用，实现高性能和高效能计算处理能力，对于有限的计算资源进行基于效能的重新分配，一定程度上能够缓解计算资源的供需矛盾。为对拟态计算系统中的动态可伸缩性和弹性敏捷度等特性开展科学性评估，明晰拟态计算系统带来的计算资源效率提升情况，应开展面向拟态计算系统的测试评估体系研究，从技术和应用角度梳理多维度评估指标，建立涵盖功能、性能、效能的评测评估体系。

**1  拟态计算系统及体系架构**

拟态计算系统提出了一种主动认知可重构的计算体系结构，能够根据任务、资源、服务质量、安全要求、时效性等不同需求改变计算处理架构，调节计算和存储能力，变换成与当前所需最为适配的结构形态以获更高计算效能[1]。主要实现方式是将计算资源、存储资源、互连结构等形成异构可重构资源池，在识别需求和应用变化的同时，结合感知系统中当前可以利用的计算处理资源，依据尽可能高效的原则，主动根据计算环境和应用任务在不同阶段、不同时段、不同资源条件、不同服务质量、不同经济要求下的特定需求，动态选择或生成合适的计算结构来提供服务，从而实现高效的计算资源配置和使用。

拟态计算系统的体系架构如图1所示，包括异构硬件资源层、基础服务层、异构资源管理层、应用部署层、编译工具/语言层、计算结构在线优化支持层6个部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKMdBPsMHDibiamV9PxMAh9nUTJ3AG5NqSCXxuWA6T3l2JwmWbCGPS7AW4T08xy4DibZK0Pia8tNeIjZxkWTicGYjML3xlGEH7K1EcuV7OanjKMA/640?wx_fmt=jpeg)

**图1   拟态计算系统体系架构组成**

异构硬件资源层是拟态计算系统计算、存储与互连资源的物理实体，包含的异构资源种类和数量根据应用领域计算特征和计算规模确定，各类模块内部（板卡间、芯片间及芯片内）或之间通过互连网络实现通信与数据交互，为上层应用提供基础算力。

基础服务层承载各项系统启动、运行和管理等功能，开展任务创建、任务编排、任务提交等管理工作，监控任务状态与资源状态，获取全局资源状态，并联合硬件资源信息感知模块构建资源类型、使用状态、功能与容量、IP地址以及访问接口等资源信息库。

异构资源管理层完成对基础构件库、资源信息库和硬件资源信息库的管理。其中，基础构件库存储领域专用基础构件，在应用任务加载到拟态计算系统上时，可在基础构件库中直接选择基础构件完成计算结构构建；资源信息库将系统的计算处理功能抽象成处理单元，并屏蔽异构资源之间的差异性，进而实现资源统一管理、统一调度；硬件资源信息库包含异构硬件资源占用情况、运行情况以及故障情况等信息，这些信息主要用于支撑应用任务在异构硬件资源上的合理分配。

应用部署层构建基于共性元素抽象聚合而成的基础算核库，为不同应用的计算全流程构建提供支撑；并对不同应用任务在异构资源上运行的代价进行算核分析，包括功耗、内存、传输带宽等，分析不同任务在异构资源上的合理分配，从而提高计算全流程的性能与效能。

编译工具/语言层通过将计算任务分割成小块，并在异构硬件资源上将其分配给多个同时运行的线程或进程，以实现并行处理从而提高计算效率。

计算结构在线优化支持层对异构资源和应用任务进行整体认知，在线实现资源供给对任务需求适配的优化，并重新生成优化后的计算结构。通过对应用业务功能、资源、处理负荷、效能需求等需求和实际场景的感知与认知，基于对以往经验的学习和适当的推理，以优化效能并适应环境和需求的变化为目的，能够认知并决策出一个合理的重构机制和实现方式，从而进一步优化控制和调度整个计算体系。

**2  拟态计算系统的核心机制**

**2.1  异构计算部件按需分配**

拟态计算系统能够将不同的异构计算部件，如主处理器、协处理器、众核加速器等不同类型的处理器进行抽象化，形成可统一分配调度的计算部件。以应用算法、架构、性能之间的关系作为拟态计算系统架构设计的基础，以耦合方式通过高速网络连接不同性能和功能的计算部件，形成并行计算环境，并通过合理分配计算任务到最适合的处理单元上，以提高整体计算效率和性能。

**2.2  计算资源动态可重构**

拟态计算系统通过智能化地选择和配置计算资源，通过计算资源动态可重构特性，在恰当的场合和时机选择合适的实现方案或算法，从而在给定约束条件下逼近计算效能的最优值，提高系统的计算处理效能和能效比，同时保持高度的灵活性和适应性。

**2.3  硬件资源池化**

硬件资源池化是将计算、存储和网络等物理硬件资源整合成一个或多个共享的资源池的技术和策略。通过硬件资源池化，可重构的拟态计算系统将分散的计算单元、存储设备和网络组件等资源集中管理，形成统一的资源池，以便更灵活、高效地分配和使用这些资源，实现资源的动态分配和优化利用，提高系统的灵活性和可扩展性，是实现高效计算的重要基础。

**3  拟态计算系统测试评估指标与模型研究**

**3.1  拟态计算系统测试评估模型建立**

建立拟态计算系统测试评估模型需要统筹拟态计算系统中各模块主要功能实现，并覆盖拟态计算系统三大核心机制，形成针对功能、性能、效率提升的多维度、可量化测试评估模型，具体如图2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKMdBPsMHDickUFybfFXSiaSDqnewJkVhqbFbFfrlticvq77nzKlBOMJrJO2Scr3CZ0vHxd1IlyajSdZib8GMF3iaDS5duu7jU7JRMaATgZchQZU/640?wx_fmt=jpeg)

**图2   拟态计算系统测试评估模型**

**3.2  拟态计算系统核心评估指标**

3.2.1  系统能效比

拟态计算系统的系统能效比是通过比对在不同应用场景中使用拟态计算系统和基准通用系统二者性能/效能来验证拟态计算系统在不同应用场景下计算性能/效能的提升情况。

![](https://mmbiz.qpic.cn/mmbiz_png/CKMdBPsMHD8t1dfSjhD7lT2IhNWiaNF5B5bey83iaYbCvG0aGhpMQZf6BdYiazAFoJ2mSkCYX8fRRCSRUklKl721dvbmJcwsw9NIXccXjBoN3s/640?wx_fmt=png)

3.2.2  单节点任务切换时间

在拟态计算系统应用中会涉及单个节点执行多个任务，并随着调度指令在不同任务之间快速切换的情况。评估任务切换的最大时间可以估算使用拟态计算系统会产生的额外时间消耗，也可以体现拟态计算系统的计算效率。

衡量任务的切换时间可在评估环境中加入硬件或软件实现的计数器，其中计数器从任务K1结束瞬间开始计数，到任务K2开始瞬间计数结束，计数结果记为N。系统中通过记录所有任务的切换周期最大值*Nmax*，就可以计算出任务的最大切换时间如公式（5）所示。

Δ*Tmax*=*Nmax/*Frequency**（5）

其中，*Frequency*为计数器的运行频率，根据上述公式即可得到拟态计算系统的切换时间。

**4  拟态计算系统的测试评估部署及初步实践**

拟态计算系统测试评估场景如图3所示，需要部署多台拟态计算服务器构成算力集群，各拟态计算服务器通过交换机进行互联，形成测试评估中的计算环境。管理服务器集群可直接通过与拟态计算服务器的连接，对处理数据和计算结果进行上传/下发，用于部署运行管理平台、全栈式工具链、算核库等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CKMdBPsMHDibjiaJ1KrL6k7X355k5LEfR5KR4icycYRZOwMfyl1WALqtLYdx13cIibPtsPSqMa60YlOvgV0djHJ9gnIbZZqgw32Yia5kPZaMmSb8/640?wx_fmt=jpeg)

**图3   拟态计算系统测试评估场景**

在不同应用场景中进行拟态计算系统测试时，在构建拟态计算系统测试评估环境的基础上，需要将专用典型应用场景测试程序和数据集部署并运行到拟态计算系统及用作基线的通用服务器集群上，构成整体评估环境。以智能交通应用场景为例，测试环境下部署了相同数量节点的拟态计算系统与搭载Intel Xeon Silver 4314处理器的通用服务器集群进行对比。据笔者统计，单节点拟态计算系统性能提升50.21倍，效能提升80.82倍，8节点拟态计算系统性能提升48.16倍，效能提升77.21倍，客观体现拟态计算系统的计算效能提升情况。

**5  结束语**

拟态计算系统以创新性的理念和开拓性的架构设计在提升计算效率和计算资源分配方面提供了突破性解决方案。研究拟态计算系统的测试评估体系可科学性地量化其在计算效率提升、功能实现、性能等方面的表现，通过与通用计算系统的对比更能体现其在计算能效方面的提升情况，助力拟态计算系统在各应用领域的广泛使用，推动其从理论走向实践，释放高效计算的潜力。

Research on the testing and evaluation system for mimic computing systems

HE Qian1, JIN Wei1, XU Haotian2

（1 Security Research Institute, China Academy of Information and Communications Technology, Beijing 100191, China；

2 Zhijiang Lab, Hangzhou 311121, China）

Abstract: With the rapid development of various new technologies, the growing demand for computing resources has created a certain contradiction between the current limited computing resources and rigid allocation patterns. Optimizing the allocation of computing resources and improving the utilization efficiency of computing resources have become urgent priority problems to be addressed. The mimic computing system can flexibly and efficiently allocate computing resources through mechanisms such as on-demand allocation of heterogeneous resources, hardware resource pooling, and dynamic resource reconfiguration, fully leveraging the execution efficiency of computing resources and significantly enhancing the overall computing efficiency ratio. To clarify the progressiveness of the mimic computing system and its improvement in computing efficiency, this paper conducts research on the testing and evaluation system of the mimic computing system by sorting out testing and evaluation indicators, establishing testing and evaluation models, and carrying out application scenario practices.

Keywords: mimic computing system; mimic computing framework; testing and evaluation system

![](https://mmbiz.qpic.cn/mmbiz_gif/bQv07rEoSgnASDXC53WkoCVAbC73AzGr2gJ1hkgmLJf47DcQBvKhS65n8gFR9Rfr2aeIbyMIbxguySA37OaCNA/640?wx_fmt=gif)

本文刊于**《信息通信技术与政策》**2025年 第10期

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibv12OpHaeiajGrysc573Ysm2djfd5Qo5IEbAgJhgptDfLtqByCLdN4BCQw4GWDyickVzjiaveTmulOITsNDiaLCONQ/640?wx_fmt=png&from=appmsg)

来源：全国网安标委

![图片](https://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pWeAYKXsf7pB3M1GTJoicVOO9oITecrZeNtxqmmALz8LHQosj13WV1mOhJpslTDgADLuLUGWOjCIxQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

  —  热点文章  —

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/LGic9LOngPZibPeawxIlysHAL4BBibOkwlGdzuDGfYd1HU8Cslrpx337MkOIW1noc32zFookqPCxxiao7b57bB5y5Q/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jRRfTC292pV8CpUy943MyiabpIpFT4PAX46ibz8blSMOwlWUc9sWCaibFVgtyicgAs0sfaHDm2ok1VdfvKnC3iaeAXg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535092&idx=1&sn=eb246a0566f3e6dfe2811641fe9d3f25&scene=21#wechat_redirect)

[邬江兴院士——携手建设人工智能时代中国学派 走出不同于西方的人工智能安全治理新路径](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535092&idx=1&sn=eb246a0566f3e6dfe2811641fe9d3f25&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jRRfTC292pVNO1PFmO8TnRHbiaMevCYJN95V81bAarIDbyQUGEC26fmcQxcPuWtFbTakl0oVI88Bxib77EwHVJDw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535009&idx=2&sn=26573ffb694a62e9047843e525a5a611&scene=21#wechat_redirect)

[第五届网络空间内生安全学术...