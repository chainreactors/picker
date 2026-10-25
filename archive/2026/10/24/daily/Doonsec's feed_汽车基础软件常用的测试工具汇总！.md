---
title: 汽车基础软件常用的测试工具汇总！
url: https://mp.weixin.qq.com/s/uB5wg3O14OGxYYV5waxeRQ
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:07:49.327710
---

# 汽车基础软件常用的测试工具汇总！

# 汽车基础软件常用的测试工具汇总！

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**总线监控工具**

**1.1 CANoe**

CANoe 软件是 Vector 公司针对汽车电子行业推出的总线分析工具，其在软件的开发、测试的各个环节都有广泛应用，下述为 CANoe 具体的功能特点：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBiceVZFNFgIib55jG2R2k8Awb1QtiasiaCVvic59X0mVT37EzdEpWEaE3fIQicw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

图 1-1 CANoe 界面示意图

**广泛的总线支持：**支持多种车用网络协议，如 CAN 、LIN 、FlexRay、以太 网、MOST 等，以及一些基于 CAN 的通讯协议，如 J1939、CANopen、ARINC825 和 ISOBUS 等，能满足汽车电子系统中复杂的总线通信需求。

**强大的仿真能力：**可在实验室环境下模拟整车网络通信，帮助工程师在开发初期对 ECU 的功能进行评估，也可用于系统的功能分析、测试以及总线系统和 ECU 的集成，以便尽早发现并解决问题。

**高效的测试功能：**具有测试功能集，能够简化或自动进行测试，并自动生成 测试报告，方便工程师对测试结果进行分析和评估。

**全面的诊断功能：**可与 ECU 进行诊断通信，帮助工程师分析诊断通信过程中的问题，对 ECU 的诊断功能进行验证和测试。

**1.2 INTEWORK VBA**

VBA（INTEWORK VBA）是由经纬恒润推出的一款国产化的总线分析工具，近几年在市场中有不错的表现，具体的功能特点有：

**基本监控与分析：**能够对 CAN 、CANFD 、LIN、以太网等总线数据进行监控和分析，实时采集总线上的报文，并解析报文中的单个信号，帮助工程师掌握总线通信的详细情况。

**节点仿真功能：**可以模拟车辆电子控制单元（ECU）的行为，在总线上发送和接收报文，方便进行系统的集成测试和验证。

**报文发送与回放：**支持用户手动发送特定的报文到总线，用于测试总线系统对特定指令的响应，还可以将之前监控到的总线数据保存下来进行离线回放，以便深入研究历史数据。

**脚本编程支持：**基于 Python 脚本开发环境，用户可以根据自己的需求编写脚本，实现自动化测试、数据处理和复杂的仿真场景，具有较高的灵活性和可扩展性。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBiceQ3DxWZcHOKEl2iaU28O1zicdNWl6x3Qen77K4C8MFIGp8icoPzzg1wC7g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

图 1-2 VBA 界面示意图

**1.3 Wireshark**

Wireshark 是一款免费、开源的网络数据包分析工具，主要应用在汽车网络通信分析的场景。

Wireshark 可以捕获汽车以太网总线上的数据包，对数据包进行详细的分析和解读，帮助工程师了解网络通信的细节，例如分析网络通信中的协议、数据格式、通信频率等。不过，与专业的汽车总线监控工具相比，Wireshark 在汽车领域的应用可能需要更多的配置和专业知识。

**1.4 Vehicle Spy**

Vehicle Spy 是一款综合功能强大且易于上手的软件工具，在工作中有广泛的应用。

**功能特点：**可用于执行诊断、节点/ECU 仿真、数据采集、 自动测试、存储器编辑或校准以及车辆网络总线监控等方面。 几乎支持所有汽车网络，包括 CAN 、CANFD、汽车以太网、LIN 、FlexRay 、K-Line 等。它能够满足汽车电子系统开发和测试过程中的多种需求，为工程师提供了全面的解决方案。

**02**

**静态代码分析工具**

**2.1 Helix QAC**

QAC 工具是一款主要用于 C/C++代码的自动化静态分析工具，可以提供编码规则检查、代码质量度量、软件结构分析、测试结果管理等功能。其功能特点如下：

**代码规则检查全面：**能够对 C/C++代码规则进行自动检查，报告所违反的编程标准和准则，可发现 1200 多种 C 语言问题、800 多种 C++的问题。能准确发现危险的结构、维护和移植中可能发生的问题，帮助开发人员在开发阶段提高代码质量。

**支持多种标准和扩展：**支持多种编程标准（如 ISO 、MISRA C/C++ 、CERT C/C++ 、CWE C/C++ 、AUTOSAR C++等）以及多种其他行业编程规则。

**便捷的操作和报告：**产品界面简洁直观，操作简单，建立工程后加入代码即可进行分析。分析报告形式多样，可输出为 excel 、word 、pdf、图表等。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBiceXuiaMjjFqnJckWztwqKVATXicia3dJL9l9sa3nYaDlvurjvvq7m4gJMxg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

图 2-1 QAC 静态分析结果

**2.2 StatiCode**

StatiCode 是一款静态代码分析工具，可以提供多种语言的质量安全分析和代码度量分析，也可以提供编程标准合规分析。其特点有：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBice30vuNNqgibo1LEV2euLhic2v9ENTyxrdvZ5QIwvbrCABkOfrOJFYUIxA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

图 2-2 StatiCode 静态分析结果

支持C/C++/Java/C#/JavaScript/TypeScript/Golang/PHP/Python 等多种语言。

采用全路径扫描、并行程序分析、数据流、符号执行、抽象解释、作用域分析等检测技术，能够检查内存崩溃、未初始化变量、资源泄露、空指针引用、控制流缺陷、程序假死、除零错误、类型溢出等运行时缺陷。

软件可以从问题严重等级、Top10 统计、趋势、处理状态分布等多种维度展示检测结果，支持多条件组合缺陷查询。展示缺陷上下文细节，帮助技术人员复盘缺陷的产生过程。

**03**

**单元测试工具**

**3.1 Tessy**

Tessy 是一款主要用于动态单元测试的工具，其主要特点如下：

**多种测试用例设计方式：**除了在简洁的界面中手动输入测试用例之外，还支持从 Excel 中导入测试数据，也可以通过脚本编辑器编写测试用例。

**支持多种覆盖度分析：**提供 C0、C1、MC/DC 等多种覆盖情况，可以帮助测试人员全面了解测试的覆盖程度。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBiceCIibhibLicHYawDjBzz6W9wFfpF6EXjHc9IRtJRNf0lMWARbYOcibJ92Pw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

图 3-1 Tessy 工具执行单元测试效果图

**3.2 Google Test**

Google Test（简称为 gtest）是 Google 开发的一个用于 C++程序的单元测试框架。它帮助开发者通过编写和运行测试来验证代码的正确性，并提供了丰富的功能来支持各种测试需求。以下是 Google Test 的一些关键特点：

**简单的测试编写方式：**开发者可以通过定义测试函数来编写单元测试，测试函数一般用TEST 宏来定义。Google Test 让编写测试变得直观且容易理解。

**丰富的断言支持：**Google Test  提供多种断言类型来验证测试结果，如 EXPECT\_EQ、EXPECT\_TRUE、ASSERT\_EQ 等。EXPECT\_\*断言允许测试继续执行，即使断言失败；而 ASSERT\_\*断言则会在失败时立即停止测试。

**测试分组：**可以通过测试用例组将相关的测试组织在一起，便于管理和执行。 每个测试组可以包含多个单独的测试。

**Fixture 支持：**通过测试夹具（Test Fixture），可以为一组测试设置通用的初始化和清理代码。使用夹具有助于减少测试中的重复代码，并确保每个测试在相同的初始条件下运行。

**跨平台支持：**Google Test 可以运行在 Linux 、Windows 、macOS 等多种平台上，具备良好的跨平台兼容性。

**3.3 Catch2**

Catch2 是一个专门针对于 C++设计的单元测试框架，它能够帮助开发者高效地编写和管理单元测试用例，提高代码的质量和可靠性，其具体特点如下：

**自动注册测试用例：**能够自动发现和注册测试用例，无需手动管理测试用例的列表或执行顺序，简化了测试代码的编写和维护。

**支持多种测试场景：**允许以结构化的方式组织测试，可描述不同的测试场景和条件，能够有效的提高复杂的业务逻辑测试覆盖度和效率。

**良好的文档和教程：**拥有详细的文档和丰富的教程，对于初学者来说易于上手，能够快速掌握框架的使用方法。

**04**

**集成测试工具**

**4.1 Tessy**

4.1 TessyTessy  工具除了能够进行单元测试之外还有着强大的集成测试功能。工具内包含了一系列专门的集成测试套件，这些套件符合 ISO 26262  功能安全 标准，专注于ECU（电子控制单元）的模块交互测试和通信协议（如 CAN、 LIN）的集成验证。Tessy提供的测试套件涵盖了模块之间的交互、接口验证、 数据流测试和系统行为验证等方面。其集成测试的优势在于：

测试用例生成和执行自动化，适合复杂的汽车基础软件；

提供 FC/CPC  覆盖率，满足 ISO 26262  等功能安全标准；

支持主流编译器和调试器，与汽车基础软件工具链无缝集成；

直接在目标硬件上运行测试，确保与真实环境一致；

自动生成符合 ISO 26262  的测试报告，便于审核和验证。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBicetN2sd246OwJJibRrKcp7MqNib9OK6V9nIIU91ic7sX9tQG79icrHtQ3PRA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

图 4-1 Tessy 工具执行集成测试效果图

**4.2 VectorCAST**

VectorCAST  是一款专门用于嵌入式软件测试的自动化工具，广泛应用于汽车、航空航天、铁路、医疗等领域，尤其适合对安全性、可靠性要求比较高的系统。

采用高度模块化的设计，以独立模块协同工作的方式实现高效的测试功能。其核心模块包括：

**VectorCAST/C++ 和 VectorCAST/Ada：**分别支持 C/C++  和 Ada 语言的单元测试和集成测试，进而提供自动生成测试用例的功能。

**VectorCAST/QA：**集成测试模块，专注于代码覆盖率分析和回归测试。 此外，通过与 CI/CD 工具链结合，完成测试过程的持续集成和质量保证。

**VectorCAST/Manage：**项目管理模块，用于管理多个测试环境、报告生成和测试进度跟踪。

**Stub 和 Mock 支持模块：**提供对外部依赖的模拟功能，实现未完成模块的隔离测试。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBiceDfgqnCSAF8BhiaicY2MGLCXkzeNEyWBp6cQ7ZEzYJhRDlAMnUoFEqAQQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

图 4-2 VectorCAST 工具图

**4.3 Cantata**

Cantata  是一款功能强大的 C/C++  软件测试工具，特别是在嵌入式和高可靠性领域中表现出色。其软件设计具有高度模块化、用户友好性和自动化的特点，其架构和功能的设计完全针对嵌入式系统和复杂集成测试的需求。 具体模块介绍如下：

**测试框架模块：**这是Cantata核心设计之一，让用户只需关注测试逻辑的设计。测试框架包括测试用例函数、初始化代码和断言代码。

**Stub 和 Mock  模块：**专为嵌入式开发设计，支持模块间依赖的隔离测试。Stub  和 Mock  功能能够动态生成，方便用户模拟未实现模块或硬件接口。

**数据驱动模块：**支持导入外部测试数据文件（如 CSV 、Excel），将测试逻辑与测试数据分离，实现数据驱动测试。

此外，Cantata  内置的回归测试机制，能够自动检测代码变更，识别受影响的测试用例并重新运行，从而确保代码更新后的系统稳定性。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBicelYW3qzt8L8wIrxdG2pCXC51iaxHAFASZjBpqicvCZs7TjmcYFtsmsUYQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

图 4-3 Cantata  管理视图

**05**

**性能测试工具**

**5.1 AbsInt**

AbsInt 是一款应用于性能测试的静态分析工具，该工具能够在代码开发、控制器集成阶段评估资源使用率，指导芯片选型和工程优化、保证堆栈空间分配合理性、保证任务周期的稳定性，规避软件中函数执行时间的不合理风险。

在 AbsInt 工具中集成丰富的功能套件，能够支持用户应对不同的使用场景：

**AIT WCET Analyzer：**最差情况执行时间分析工具，针对特定的处理器和编译器，能够分析出接近实际运行情况的最差执行时间。

**StackAnalyzer：**最差情况堆栈使用量分析工具，可针对特定的处理器族和编译器， 自动分析出任务的最差堆栈使用量，防止堆栈溢出或资源浪费。

**TimingProfiler：**代码执行时间分析工具，针对特定的处理器族和编译器，能从初期开始对代码执行时间进行持续分析和评估。

**特点优势：**作为代码静态分析工具，可直接导入编译后的二进制可执行文件进行自动分析；具有图形化显示功能，可为优化提供依据；能遍历所有程序执行路径，对所有场景有效且无需提供测试用例。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBiceN3sjADjF1pDTnBu74ofgEVNl67VNl9eU5gL3KyViaPdSdvaoSSbUcog/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

图 5-1 AbsInt 执行方案

**5.2 RVS**

RVS（Rapita Verification Suite）工具是一款嵌入式系统在板测试工具，其能够进行自动化时间性能分析，并为复杂嵌入式系统提供可视化任务调度和时序追踪，其功能套件主要有：

**RapiTime：**软件时间性能分析工具，可提供函数级、代码段级的最差情况执行时间、最大执行时间、最小执行时间、平均执行时间、高水位执行时间的测量和统计，帮助用户定位性能瓶颈和软件优化重点。

**RapiTask：**软件任务调度和事件分析工具，可视化软件任务调度和事件跟踪，帮助用户解决在使用复杂调度行为（如多核、多线程）的嵌入式系统时可能面临的挑战，如定位时序错误、系统容量和负载问题等。

**特点优势：**产品符合 ISO-26262、DO178B/C、IEC-61508 等行业标准，兼容多种操作系统和编程语言，广泛支持各类编译环境及各类目标芯片。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9OJGxtib2XVDu9QhWluicBicecUTiafUmqicJib1antQSiboF6bDx8KKgDz9GxRbq9tCSoztQyqMJD09ibEg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

图 5-2 RVS 系统级分析效果图

**5.3 Gliwa T1**

GliwaT1 可以满足开发流程中不同阶段对嵌入式时间的需求，对函数执行时间、控制器负荷、多核稳定性等均具备成熟资质，GliwaT1 工具包含如下几类分析内容：

**静态代码分析：**分析时间工具读取应用程序源代码或二进制代码，计算指定代码段执行的时间下限 BCET 和时间上限 WCET。

**代码仿真：**模拟某种MCU 下给定二进制代码的运行，并考虑流水线与缓...