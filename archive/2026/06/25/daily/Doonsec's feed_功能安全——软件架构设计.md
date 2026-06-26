---
title: 功能安全——软件架构设计
url: https://mp.weixin.qq.com/s/-Sf_Dfy8KSSnG1xT4UuWWQ
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:07:38.855964
---

# 功能安全——软件架构设计

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCBJ2dYtNzLwTaibwO7ufIVqZiaM7RyZ45C86TP3824gIBhOiaPJ4702M8hwU2X0QbVoUtjCicRcVW9YAan2Qu7RxiazJawA9J3CyJM/0?wx_fmt=jpeg)

# 功能安全——软件架构设计

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**01**

**什么是软件架构设计？**

在20世纪60年代，戴克斯特拉这位上古大神就已经提出软件架构这个概念了，但软件架构真正流行却是从20世纪90年代开始的，由于在Rational和Microsoft内部的相关活动，软件架构的概念开始越来越流行了。

卡内基·梅隆大学的玛丽·肖（Mary Shaw）和戴维·加兰（David Garlan）对软件架构做了很多研究，他们在1994年的一篇文章《软件架构介绍》（An Introduction to Software Architecture）中写到：

“When systems are constructed from many components, the organization of the overall system-the software architecture-presents a new set of design problems.”

简单翻译一下：随着软件系统规模的增加，计算相关的算法和数据结构不再构成主要的设计问题；当系统由许多部分组成时，整个系统的组织，也就是所说的“软件架构”，导致了一系列新的设计问题。

这段话很好地解释了“软件架构”为何先在Rational或者Microsoft这样的大公司开始逐步流行起来。因为只有大公司开发的软件系统才具备较大规模，而只有规模较大的软件系统才会面临软件架构相关的问题，例如：

* 系统规模庞大，内部耦合严重，开发效率低；
* 系统耦合严重，牵一发动全身，后续修改和扩展困难；
* 系统逻辑复杂，容易出问题，出问题后很难排查和修复。

而在功能安全标准中的定义——软件架构设计是指全部软件组件及其在层次结构中的交互。静态方面，如所有软件组件间的接口和数据路径；动态方面，如进程顺序和定时行为，都得到描述。

软件架构设计不必局限于某个微控制器或电控单元，它关系到技术安全概念和系统设计。软件架构设计并不是功能安全独有的要求，只是功能安全在原有的基础上叠加了很多安全方面的设计和考量标准，这使得软件架构设计变得更全面更安全，同时为开发既实现软件安全要求又实现非安全要求的软件架构设计，通常来说安全和非安全性要求应在同一开发过程中处理。 软件架构设计提供了实施软件安全要求和管理软件开发复杂性的方法。

**02**

**软件架构设计依赖关系**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBwJkSUavUq4nibzkahXfbXACHFKTYmYibAfsv29GqynEsYnml4rZTLyMOiaa1EXj50wXXcGwsdeicmlhU8PSQB1hYAJBkC55OzddY/640?wx_fmt=jpeg&from=appmsg)

**03**

**软件架构设计要求和建议**

**1.软件架构设计描述方法**

为确保软件架构设计获取必要信息以允许后续开发活动得到正确且有效的执行，下表列出的软件架构设计的标记法，对软件架构设计进行恰当抽象层级的描述。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBggPynDmbA0kib1bBiaueUGqzwLmQciagfaSwAIPmpcGK91De9XSfkUqqN3xgiaxuictGteCtS4HxUibJf939ZsrmIUrcyhp5cYnD0I/640?wx_fmt=jpeg&from=appmsg)

软件架构设计的标记法

解释：

1. 自然语言：可以补充符号的使用，例如，一些主题更容易用自然语言表达，或者为符号中捕获的决策提供解释和理由，使抽象的设计更容易被理解。
2. 非正式标记法：通常不作为标准的标记方法，描述上比较模糊。
3. 半正式标记法：包括伪代码或使用UML、SysML、Simulink或Stateflow建模。
4. 正式标记法：包括数学或物理学表达式，通常是被证明过的严谨的表达式

**2.软件架构设计必要的性质**

1. 软件架构设计的可验证性； （这表明软件架构设计和软件安全要求之间的双向可追溯性）
2. 可配置软件的适用性；
3. 软件单元设计和实现的可行性；
4. 软件集成测试中，软件架构的可测性；
5. 软件架构设计的可维护性。

**3.避免高度复杂性原则**

为避免因高度复杂性导致的失效，应遵循下表列出的原则设计软件架构

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDnNf938HTvnic3Xu7HtA7Qty38EBsI9AJZJAJZiaCP7vsG7Nib9LNQYuicLOwpJJSUibMicgrt2q5LfYpkPSNh3pCEAnplUCgbsVGiaE/640?wx_fmt=jpeg&from=appmsg)

软件架构设计原则

1a.软件需要采用分层架构，分层架构比较清晰

1b.每个软件模块或组件都不要太大，太大了不好维护，容易出bug

1c.接口的数量不要太多，降低软件组件间的依赖关系

1d.1e.软件尽量模块化，这个颗粒度需要自己根据实际的产品把握

1f.调度合理，没啥可说的，必须要合理

1g.少使用中断，如果用中断必须定义优先级

1h.内存分区隔离保护

1i.适用于共享硬件资源以及共存情况下的共享软件资源。这种资源管理可以以软件或硬件来实现，并且包括防止对共享资源的冲突访问的安全机制和/或过程措施以及检测和处理对共享资源的冲突访问的机制。

其实原则很很简单，就是尽量避免高复杂性，高复杂性包括：

1. 高度分支的控制或数据流；
2. 分配给单一设计元素的需求数量过多；
3. 一个设计元素的接口数量过多或设计元素之间的交互数量过多；
4. 类型复杂或参数数量过多；
5. 全局变量数量过多；
6. 难以提供错误检测和处理的适用性和完整性的证据；
7. 难以达到所需的测试覆盖率
8. 只有少数专家或项目参与者才能理解。

**4.软件架构设计描述**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaC3LQYKMPWibgEOicCeCvYZmlTHIO0zHPic3SOWjia7CviaoEq5ezo1YkULLXkjt5OCKWlvmibvCuY1SxHR8YE8kfkic1Xx3hCr8yja2k/640?wx_fmt=jpeg&from=appmsg)

静态和动态描述

为确定动态行为（如任务、时间片和中断），需要考虑不同的运行状态（如开机、关机、正常运行、标定和诊断）并且定义通讯关系和所分配的系统硬件（如 CPU 和通讯通道）。

**5.软件分区**

1. 共享资源的使用方式应确保软件分区免于干扰；
2. 一个软件分区内的任务彼此之间不能免于干扰。
3. 一个软件分区不能改变其它软件分区的代码或数据，也不能访问其它软件分区的非共享资源。
4. 一个软件分区从共享资源获取的服务不能被另一个软件分区影响。这包括相关资源的性能，以及计划访问资源的使用率、延迟、抖动和持续时间。
5. 由专用的硬件功能或等效方法来支持软件分区（该要求适用于 ASIL D）
6. 执行软件分区的软件部分，按照分配给软件分区要求的相同 ASIL等级进行开发，或按照比分配给软件分区要求的最高 ASIL等级更高的一个ASIL等级进行开发；且一般来说操作系统提供支持软件分区。
7. 在软件集成和测试过程中执行软件分区的验证。

**6.软件组件**

每个与安全相关的软件组件应被归类为下述之一：

1. 新开发的，需要按照功能安全标准开发。
2. 修改后使用的，需要按照功能安全标准修改。
3. 未经修改复用的。，对未经修改重用的安全相关软件组件进行鉴定。

如果在新的设计中引入了新的危害没有被现有的安全目标覆盖，应按照的变更管理流程在危害分析和风险评估中对它们进行介绍和评估。

未体现在安全目标中的新识别危害，通常是非功能性危害。如果这些非功能性危害超出了本标准的范畴，那么建议在危害分析和风险评估中用以下声明“因不属于功能安全的范畴，而未对该危害分配 ASIL”来标注它们，然而，为了参考，允许对其分配一个 ASIL 等级。

**7.功能安全等级**

1. 应将软件安全要求分配给软件组件。因此，每个软件组件应按照分配给它的要求中最高的 ASIL等级来进行开发。根据这一分配，进一步细化软件安全要求可能是必要的。
2. 如果嵌入式软件不得不实现不同 ASIL等级的软件组件，或实现安全相关及非安全相关的软件组件，除非软件组件符合功能安全标准中定义的兼容性准则，否则全部嵌入式软件必须按照最高 ASIL等级来处理。
3. 如果在新的设计中引入了新的危害没有被现有的安全目标覆盖，应按照的变更管理流程在危害分析和风险评估中对它们进行介绍和评估。
4. 未体现在安全目标中的新识别危害，通常是非功能性危害。如果这些非功能性危害超出了本标准的范畴，那么建议在危害分析和风险评估中用以下声明“因不属于功能安全的范畴，而未对该危害分配 ASIL”来标注它们，然而，为了参考，允许对其分配一个 ASIL 等级。

**8.安全机制**

1. 当分配给软件的技术安全要求没有对软件安全机制的使用进行直接要求时，那么应在系统层面对软件安全机制的使用进行评审，以分析对系统行为的潜在影响。
2. 输入和输出数据的范围检查；
3. 合理性检查（例如，使用所需行为的参考模型、断言检查或比较来自不同来源的信号）；
4. 数据错误检测（例如错误检测代码和多重数据存储）；
5. 通过外部元件（例如 ASIC 或其他软件元件）监控程序执行执行看门狗功能。 监控可以是逻辑监控或时间监控或两者兼而有之；
6. 程序执行的时间监控；
7. 设计中存在多种冗余；
8. 在与授予或拒绝对安全相关共享资源的访问有关的软件或硬件中实现的访问冲突控制机制。

**9.故障处理机制**

1. 静态恢复机制（例如恢复块、向后恢复、向前恢复和重复恢复）；
2. 通过优先考虑功能来实现降级，以尽量减少潜在故障对功能安全的不利影响；
3. 设计中的同质冗余，主要侧重于控制执行类似软件的硬件中的瞬态故障或随机故障的影响（例如软件的时间冗余执行）；
4. 设计中的多样化冗余意味着每个并行路径中的软件不同，并且主要侧重于预防或控制软件中的系统故障；
5. 数据纠错码；
6. 在与授予或拒绝对安全相关共享资源的访问有关的软件或硬件中实施的访问权限管理。

可以在系统层面对软件安全机制（包括通用鲁棒性机制）进行审查，分析对系统行为的潜在影响以及与技术安全要求的一致性。

**10.资源上限**

应该对嵌入式软件所需资源进行上限预估

1. 执行时间，例如函数运行的时间，操作写入的时间
2. 存储空间，例如用于存储堆和栈的 RAM，用于存储程序和非易失数据的 FLASH。
3. 通讯资源。 例如SPI，SCI，CAN通信等

**11.验证方法**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDlia7ZM1WZukg5GickiauuUIJlzt47mlgFjmgezdxnIX2Pu5N2xGdcZFHXN5waD9qxnvWfiavALQdNLgSdeaniamYVfGUfCUTqto3w/640?wx_fmt=jpeg&from=appmsg)

软件架构验证方法

**04**

**常用的安全机制**

**1.应用层常用的安全机制**

应用层的安全机制通常是依赖于功能安全需求和技术安全需求，并且需要技术安全概念去明确定义的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCr9ohbeDETEcibhMeBWAO3BWt5ceN0gKTwuFnSsZM7bk1InS0D2icP3wjBUbFIqEPjLTr7o7bItsGZJ8Cb0ibAuH7mqRgAj0On5I/640?wx_fmt=jpeg&from=appmsg)

应用层通用的安全机制

**2.底层常用的安全机制**

底层安全机制指的是与芯片功能安全的相关的特性，通常是由半导体厂商推荐的安全机制。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBTpVmcCPM01Tl0Sz1jq332WnCD3mYPLuzrEJc8oYeDSxLy3TicfMiaeIHpiafm72v1tKQmm0QMudJk19WsCc59qzd96ic6sKkgDLA/640?wx_fmt=jpeg&from=appmsg)

底层通用的安全机制

**3.安全的设计方法**

安全的设计方法也属于安全机制的一部分，这些方法可以在一定程度上避免失效或错误的发生。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaBicrK8L2VYq8HZq8MNRtAdWyMAojNJ6fw30uFYvicOGvuSbROA7yYOm3Gun1VTFLEE1icgJpoLoZYeSzvB043LK1zmQa1wCgvC8U/640?wx_fmt=jpeg&from=appmsg)

安全的设计方法

来源：

https://zhuanlan.zhihu.com/p/671821514

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0...