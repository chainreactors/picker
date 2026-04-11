---
title: EcuM模块详解
url: https://mp.weixin.qq.com/s/6m6fOpFWAC0MxjvBTiGJaw
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:17:58.320127
---

# EcuM模块详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaA7F8efbcDSbjpjqfopQick9yPM9bjhl8uHpibSOzcyiaibF6VxBOw2KxiaAbkCje6nTlBBdq7Hvpva7l0ysXibbelOBMsNxCPbURJLo/0?wx_fmt=jpeg)

# EcuM模块详解

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571723&idx=2&sn=24eb70d833066f41e9c0eb6b2bc15388&scene=21#wechat_redirect)

**01**

**概述**

ECU管理器模块（ECU Manager）是管理ECU状态的基础软件模块。具体来说，ECU管理器模块负责：

* 初始化和去初始化OS、SchM和BswM以及一些基础软件驱动模块。
* 将ECU配置为关机或者睡眠状态。
* 管理ECU上的所有唤醒事件（wakeup events），并提供唤醒验证机制（Wakeup validation protocol），以区分真实（real）和不稳定（erratic）唤醒事件。

EcuM具有flex与fixed两种状态管理机制，fixed模式状态唯一，跳转目标状态也是固定的，而flex模式跳转状态不唯一，可自行设计。Fixed模式在4.4中被移除。下面只介绍flex模式。

灵活的EcuM（Flexible）本身不再具有自己的状态机，因为基础软件的调度管理模块已经整合进RTE模块，并提供了宽松的模式声明与不同模块间的模式切换 映射，搭配上BswM提供的可配置的规则与对应的执行列表来评估并完成ECU模式切换等行为，所以大多数之前在Fixed模式下的ECU模式已经不在ECU管理器模块中实现。

通常EcuM模块接管控制早期STARTUP阶段和后期SHUTDOWN阶段以及调度被锁定的SLEEP阶段。

EcuM在ECU启动后，经过Boot和启动代码后（非AUTOSAR标准），立刻获得核心控制权，在初始化 SchM和BswM后将控制权委托给BSW模式管理器。在UP阶段ECU管理器模块会对来自SW-C的RUN和POST\_RUN请求进行仲裁，并通知BswM有关的模式状态，并且会对唤醒源进行验证，并通知BswM验证结果，所有这些在UP阶段涉及的操作都是给BswM模式管理提供依据。最后在SHUTDOWN阶段，BswM在配置完ShutdownTarget后会将控制权交还给EcuM。

EcuM在SLEEP阶段配置MCU休眠状态（根据芯片支持情况，选择HALT或者POLL）,并在唤醒之后与集成代码和驱动配合完成预设阶段工作之后，回到UP阶段。下图是所有阶段的示意图，注意图中的阶段只是表征当前EcuM所处阶段，并不是具体的模式，它包含一系列操作序列。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCYxSEjZmyZVGKFo6x9cAVNUibPmyIUE8u0eyic7iaNAiciaud0yuzAF0VicJhnNFib5HeDWIep2xX1ExwgEbmtN2Dn28QtHnv3KtVP0U/640?wx_fmt=png&from=appmsg)

**02**

**启动阶段（STARTUP）**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDzDh6xO41vAjkJHbxSNVy3CeiaGEBuTMse8Tv6Om1RxXVasw6ibFC7WGFQecny7BfwfibU3uwnFHUeUicNDtniawic7JLEYSyH9RpcU/640?wx_fmt=png&from=appmsg)

上图显示了ECU启动阶段涉及的动态行为。在调用EcuM\_Init之前，假定MCU最小系统的初始化过程已经完成（堆栈等已被设置，代码可以被正常运行）。当调用EcuM\_Init时，EcuM将控制ECU启动过程。调用Startos后，ECU Manager模块将暂时放弃控制。要重新获得控制权，Integrator（集成商）可以在操作系统的StartupHook处，挂接EcuMStartupTwo作为其第一个操作，也可以起一个Task来做这件事情。

由上图可以看出，Startup阶段按照OS启动作为分水岭，可分为StartPreOS与StartPostOS两个子阶段。经历过Startup阶段之后，则会进入到UP阶段。STARTUP阶段的目的是将基础软件模块初始化到通用模式管理设施（Generic Mode Management facilities，包括BswM以及SchM等）可操作的点。

**StartPreOS Sequence**

下表按顺序描述了StartPreOS Sequence涉及的动作。

1. 调用EcuM\_AL\_SetProgrammableInterrupts：EcuM\_AL\_SetProgrammableInterrupts函数由集成商实现在EcuM\_Callout\_Stubs.c模板文件（模板文件只有函数名定义，函数体为空）中，在具有可编程中断优先级的ECU上，启动OS之前完成这些优先级的设置。
2. 调用EcuM\_AL\_DriverInitZero：根据集成商在ISOLAR中的配置，EcuM\_AL\_DriverInitZero函数生成在EcuM\_Cfg\_Startup.c文件中，此初始化列表应包含不使用post-build参数的低级BSW模块与MCAL驱动。
3. 调用EcuM\_DeterminePbConfiguration：EcuM\_DeterminePbConfiguration集成商实现在EcuM\_Callout\_Stubs.c文件中,仅在使用了post-build参数可选特性被使用的时候，用户可在ISOLAR中配置根据对应Pin高低状态来选择，若没有则生成的EcuM\_Callout\_Stubs.c模板文件会默认返回EcuM\_EcuMConfigurations\_cpcast[0]。
4. Check consistency of configuration data：检查pre-compile与link-time的参数与post-build参数之间的依赖性，保证ECU Code Image与ECU Post-Build Data Image之间的一致性。如果检验失败则EcuM\_ErrorHook调用。
5. EcuM\_AL\_DriverInitOne：包含了在启动OS之前必要的驱动初始化列表，集成商在ISOLAR中进行配置，代码生成在EcuM\_Cfg\_Startup.c文件中。
6. Get reset reason：调用MCU驱动模块提供的Mcu\_GetResetReason获取重启原因，并根据在ISOLAR中配置的ECU唤醒源与重启原因的对应关系，调用EcuM\_SetWakeupEvent设置对应的唤醒事件。
7. Select default shutdown target：根据ISOLAR中配置的EcuMDefaultState以及对应的reset或sleep mode来完成默认关闭阶段的配置（off则无mode）。
8. EcuM\_LoopDetection：如果循环检测使能，将会在每次启动阶段调用EcuM\_LoopDetection，函数模板在EcuM\_Callout\_Stubs.c中，由集成商实现具体内容。
9. Start OS：启动操作系统。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC3cpherPqQYVHduqNU2nnQg97SWicDSR3JmtiaSIAxYERmWeLBe7ibCCKbHDiad4roiawLVibnAc6Xza2VK11IyWzicKnz0ia4amSMKw4/640?wx_fmt=png&from=appmsg)

**StartPostOS Sequence**

下表按顺序描述了StartPostOS Sequence涉及的动作。

1. Start BSW Scheduler：启动基础软件调度模块，现在这个模块已经融入到RTE，不用再单独启动。
2. Init BSW Mode Manager：初始化BswM模块。
3. Init BSW Scheduler：调用SchM\_Init（）完成初始状态的配置通知。
4. Start Scheduler Timing：因为基础软件调度模块已于RTE合并，此处不在单独启动。
5. BswM\_MainFunction：调度BswM的主处理函数，完成BSW后续的基础软件初始化以及GPT定时器启动，最终OS正常开始调度任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCE6jic1N3WoffLuhT7PCOrHVALibcrT1wS5qJcibqAfCYTQtLXl3vItJX0Cickr3PAfPiav1djMtvZeicIKqf5SrFhd9lDzGxHZR5uY/640?wx_fmt=png&from=appmsg)

**参数一致性检查**

AUTOSAR将配置按照固件生成的过程分为了三类，Precompile、Linktime以及PostBuild。这三类比较重要的就是PostBuild类配置，这类配置可以单独放到一个存储区域，这个区域可以被单独刷写（通过Flash擦写工具，通过UDS服务），这样（例如上图中的ECU Post Build Data Image写入地址0x8000\_0000中）。

这个时候就需要验证单独更新的这部分参数是否与其余的参数是配套的，如果不配套则会出现很多意想不到的问题，AUTOSAR的方式是对Precompile、Linktime进行哈希算法得到一个例如MD5值，并将这个值写于PostBuild参数中，这样就可以在代码运行时从PostBuild参数中拿出这个MD5值与上图中的ECU Code Image中的MD5值相对比。

**03**

**运行阶段（UP Phase）**

在运行阶段，ECU的状态由BswM来控制，EcuM\_MainFunction会定期执行，完成下面三个任务。

* 检查唤醒源是否被唤醒，并将唤醒源的状态通知其他模块，并在必要时启动唤醒验证。
* 更新闹钟定时器（Alarm Clock timer）。
* 仲裁RUN和POST\_RUN的请求和释放。

当闹钟服务存在时，EcuM\_MainFunction主功能将更新闹钟定时器，这里主要针对在Sleep模式下进行定时唤醒功能的实现，在EcuM框架下实现这个功能很少，这里就不赘述了。

下图为唤醒验证过程，看起来比较复杂，下图的动态流程以Can模块为唤醒源，集成代码负责重新启动和停止CAN模块唤醒功能（特定帧或别的判决唤醒方式），唤醒源存在之后会告知EcuM,并通知ComM与BswM存在验证过的唤醒源，如果超时了也没有，则通知BswM唤醒源现在为废弃的状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBiaUKRLvLJzSUp13sWibf04eyZbs68ulaHwFicUA8O7lTMyiaNhZ0En4eVLf2vodRNv2m0xzKDTxMtMwibz8W7psbljkrnpxjlpl5U/640?wx_fmt=png&from=appmsg)

EcuM用一种数据类型定义了所有的启动和唤醒源，我们统一称为唤醒源。下面这五种唤醒源为ISOLAR自动配置的，并不会触发验证过程，直接。

* ECUM\_WKSOURCE\_POWER
* ECUM\_WKSOURCE\_RESET
* ECUM\_WKSOURCE\_INTERNAL\_RESET
* ECUM\_WKSOURCE\_INTERNAL\_WDG
* ECUM\_WKSOURCE\_EXTERNAL\_WDG

ECU状态管理器为SW-C提供接口以请求和释放RUN模式和可选的POST\_RUN模式。在ECUM\_CFG\_MODE\_HANDLING==STD\_ON时，EcuMFlex对SW-C发出的请求和释放进行仲裁，并将结果传送给BswM。因为只有BswM可以决定何时可以转换到不同的模式，所以EcuM和BswM之间的合作是必需的。外EcuM将当前请求的仲裁通知BswM。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDj0Scz1Q2ribGOHYwPq0ZrichIq8hoyVnonnxlsyFm1uh6tLejcmhcVCJVrMvEfRYXIaCicsxafCyQarkCbHJEoyO7I2lBQY9aVg/640?wx_fmt=png&from=appmsg)

现在的状态管理都放到了BswM里，什么时候要进入睡眠状态已经由应用程序决定了，所以唤醒源的验证以及对RUN和POST\_RUN的仲裁已经不常用了。

**04**

**关闭阶段（SHUTDOWN Phase）**

这个阶段出现在调用EcuM\_GoDown()之后，Ecum首先检验当前的ShutdownTarget是否为ECUM\_SHUTDOWN\_TARGET\_OFF或者ECUM\_SHUTDOWN\_TARGET\_RESET，如果是才正式修改GoDown的全局变量，EcuM\_MainFunction会根据此全局变量执行对应的关闭阶段行为，ISOLAR会根据AUTOSAR默认创建三个重启模式，如果ShutdownTarget选择ECUM\_SHUTDOWN\_TARGET\_RESET的话可以配置选择对应模式，并在关闭阶段根据对应模式自定义一些行为。

* ECUM\_RESET\_MCU
* ECUM\_RESET\_WDGM
* ECUM\_RESET\_IO

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAkviaXFicnZ0ibMevRia6Gic4nxlNu2Aw4pongMjHibKhcoB0efZVQ9N91HxCspv7OzDdlywfG1QASpcs9on3726lYRXZaErTvySzCU/640?wx_fmt=png&from=appmsg)

**OffPreOS Sequence**

下表按顺序描述了OffPreOS Sequence涉及的动作。

1. De-init BSW Mode Manager：取消BswM初始化（BswM\_Deinit）。
2. De-init BSW Scheduler：取消基础软件调度初始化（SchM\_Deinit）。
3. Check for pending wakeup events：目的是检测关机期间发生的唤醒事件。
4. 如果唤醒事件挂起，设置RESET为shutdown target：只有当检测到挂起的唤醒事件允许立即启动时，才应执行此操作（这块在ETAS生成的静态代码里没有看到体现）。
5. ShutdownOS：关闭OS。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCH8fm3ocTcs4vxcwagcricLTS0WBgPhmNe7XWelz2abAW8iaXf12ONQlIzlr32F41LQSagqLJLQythondicfKlic3S9bwl88aXZtY/640?wx_fmt=png&from=appmsg)

**OffPostOS Sequence**

OffPostOs序列实现了在操作系统关闭后达到关闭目标的最后步骤。EcuM\_Shutdown()启动该序列,其挂接在Os的回调函数Os\_Cbk\_InShutdown()。ShutdownTarget可以是ECUM\_SHUTDOWN\_TARGET\_RESET或ECUM\_SHUTDOWN\_TARGET\_OFF，其中具体的复位模式由ShutdownModeType决定,默认ISOLAR会创建上文提到的ECUM\_RESET\_MCU等三种模式。

下表按顺序描述了OffPostOS Sequence涉及的动作。

1. 调用EcuM\_OnGoOffTwo：集成商自定义的动作。
2. 调用EcuM\_AL\_Reset 或者 EcuM\_AL\_SwitchOff：取决于所选择的ShutdownTarget（RESET or OFF）

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAT48NtOMib089OsveHlSyNHlDKGrgNvJTj6g7QEQHhPjQq1oR92FDDEDpA1VA6iaZ69ibo95SZhumn9wibV5DZqp7ePny2HFSRWPg/640?wx_fmt=png&from=appmsg)

**05**

**测试设备在线睡眠阶段（SLEEP Phase）**

ECU在SLEEP阶段整个板卡处于低功耗（saves energy）状态。不同的微控制器 对低功耗模式有不同的实现，最常见的实现为核心不执行任何代码，在核心进入这种模式之前，通过配置相应的唤醒中断（IO口电平转换或者定时器超时）会将核心唤醒，这种模式可以使用ECU管理器模块提供的Halt睡眠模式。

还有另外一种，例如瑞萨平台，它的低功耗模式(STOP)是可以执行代码的，Mcu\_SetMode (MCU\_STOP\_MODE)进入低功耗模式之后可以轮询检测各个IO口状态，状态变化之后可以离开这种模式，这种模式可以使用ECU管理器模块提供的Polling睡眠模式。

还有一种外围芯片（电源芯片和CAN收发器配合）完成休眠唤醒的方式，微控制芯片可以通过不喂狗等方式使电源芯片停止对微控制器供电，此时休眠，微控制器直接掉电了，但是CAN收发器还有供电，在满足唤醒要求（接收到特定帧等情况），它会通过自己的INH引脚反映到电源管理芯片上的WAKE引脚,上升沿来重启电源管理芯片。

规范里使用SLEEP作为ShutdownTarget时，EcuM\_GoDownHaltPoll函数会启动两种控制流。具体哪种控制流取决于EcuMS...