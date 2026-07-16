---
title: 汽车ECU软件测试
url: https://mp.weixin.qq.com/s/UBZeCeTWe4QwiEX384NTjQ
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:53:53.131746
---

# 汽车ECU软件测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA1cvNQ9EzWEB7c7OiayOA3TWZiczjxncME0H7P4ZfpSEicvEW3WHCmbgiaG68NBpibHWRqbTSCUG4ibIyk043dzpiblQ0nu8ToTyYB2g/0?wx_fmt=jpeg)

# 汽车ECU软件测试

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDeWXtQ5YUxJYVRMicwTibxb8GN5kJkxMsawlqTUVPpKGMxr7fgCqWcKISkuJkK0O2BbGJ9eId6uf2qbmmTGmwbfNE7KAwbgVOG4/640?wx_fmt=png&from=appmsg)

我们就以ISO26262软件部分描述的V型开发流程为线索，举一个实际例子来说明。对V型开发流程不熟悉的同学欢迎去看我以前写的文章和回答，这里就不再赘述了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCs55HDNaPjFkLbKCFTdEDIGLkYTCD0kA3VU77PRuCmMgbfvznfX3uFdricR2ibZaL9f0WKCDJLNYrAbGpLoriaT3pDn26pdddhFA/640?wx_fmt=jpeg&from=appmsg)

图1. V型开发流程

**一、先编一个需求吧**

假设现在我写了一个系统级的需求（System Requirement），也就是图1里的“Technical Safety Concept”:

(这里多说一句和测试无关的话，所有的Techincal Safety Concept都是系统级需求，不是软件需求，面试的时候别搞混了)

System Requirement

The Adaptive Cruise Control (ACC) function shall only be active when the ego-vehicle is traveling between 30kph and 120 kph.[ACC-SysReq 001]

Once ACC deactivated, it cannot resume automatically.[ACC-SysReq 002]

这家车企比较怂，它的自适应巡航功能只能在30公里到120公里每小时之间激活，并且一旦退出后不可再自动激活。

为了简单起见，我们先不管第二条需求了，只看第一条。下面我把这个系统需求写成软件需求（Software Requirement）：

Software Requirement

The signal ACC Active State shall be set to READY if the following conditions are fulfilled[ACC-Req 001]:

* Safe Vehicle Speed is greater or equal to 30kph AND
* Safe Vehicle Speed is less than or equal to 120kph.

The signal ACC Active State shall be set to SUPPRESSED if the following conditions are fulfilled[ACC-Req 002]:

* Safe Vehicle Speed is less than 30kph OR
* Safe Vehicle Speed is greater than 120kph.

再接下来软件设计文档里， 也就是图1的Architectual Design里可以写：

Design Requirement

Acc\_ActSt shall equal to READY if:

* SafeVehSpd is greater or equal to 30kph AND
* SafeVehSpd is less than or equal to 120kph.

Acc\_ActSt shall equal to SUPPRESSEDif:

* SafeVehSpd is less than 30kph OR
* SafeVehSpd is greater than 120kph.

好了，这就是个最简单的需求例子。根据这个需求，你写了几行代码来实现。我们假设用C代码，在原有的C文件acc.c中加入了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBaIfeg2BicKKCcvfswpXzHYmZo4pxdT0tn3x1TJgTKU0D3Dv7QH6vFrZEFeL9vPCMOic671hVHJo7F6UMdyZDFtXCFPzbicficap4/640?wx_fmt=png&from=appmsg)

有同学可能会说，你有病啊写成这样，第一个if语句写完了直接写else不就完了嘛。对， 但是我也不知道客户以后会怎么改这个需求，也许会对其他速度段增加新的状态，所以我就先写个else if在这里，方便以后扩展。

到这一步，"V"模型的左半边你就做完了，现在我们开始来测试。

**二、单元测试**

写完代码编译成功以后，先开始进行单元测试，也就是图中的“Software Unit Verification”。顾名思义，就是把你这个新编写或者修改过的单元（单独的C文件，在本例中是acc.c)与整个工程隔离开，单独测试其输入输出。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCflLfHPDSVvoaSlfT6nvApraVp79Ohm2IIapyxpwMDcTViaVnr3xYvhibu96s5X3mv4z5icFBA1uiaLz1qMxXpy0icr7M4ibxXNL18A/640?wx_fmt=jpeg&from=appmsg)

图2. 单元测试只关心某个具体的软件单元

汽车行业呢，首先就是做MISRA 规则测试。MISRA 测试是静态测试的一种，用来检验代码是否符合一系列具体的编程规则。这里我们假设用的测试工具是QAC。

就我写的这段，估计啊会报出一个warning, 因为 “else” 这个分枝事实上是无法触发的，而MISRA的其中一个规则就是所有代码都必须可触发，所谓“Accessible”。当然啦，这里我是有意为之，所以可以注释一下就放过去了。

下一个步骤是进行Polyspace测试。Polyspace工具可以进一步可以帮助判断算法在计算过程中，会不会产生诸如数组index超范围、overflow、被除数是零之类的bug 。我们这个例子中只有逻辑判断，所以其实不需要做Polyspace测试。

接下来进行功能测试。在功能测试中，我们要：

1. 分析待测单元有哪些输入信号和输出信号
2. 编写一系列的输入信号值，并同时写出这些输入信号值所对应的正确的输出信号值。我们把这个叫做“测试集”。
3. 以测试集中的输入信号值为输入，运行单元代码。如果输出信号的值和测试集中的正确输出信号值相同，则功能测试通过。

编写测试集的一个基本原则是要把所有的代码都覆盖到，并且尽量测试所有判断逻辑。上面所示的例子非常简单，只有一个输入变量 SafeVehSpd 和一个输出变量 Acc\_ActSt。

我们需要把输入变量按判断逻辑分成若干个Equivalent Class 。在这个例子中，（假设 SafeVehSpd 是 Unsigned int 型, 速度范围的上限是500 kph）输入信号SafeVehSpd 就可以分成三个 Equivalent Class:

i. [0, 30）

ii. [30, 120]

iii. (120,500]

于是在这三个Equivalent Class里随机各取一个值，就能测试所有代码逻辑了。但是实际测试中，我们往往还进一步要求进行边界测试, 也就取每个Equivalent Class的两端的值来进行测试。这就涉及到精度问题了。假设这段代码是定点运算，车速数值由10bit 表示，前述车速上限是500， 于是车速的精度就是 500/（2^10） = 0.48828125。

所以严格来说，测试集需要测试的输入变量SafeVehSpd的值有6个，分别是 0 ，29.5117188 ，30 ， 120 ， 120.48828125 ， 500 。

当然，现在很多工具支持自动生成测试集，所以不用程序员费劲巴力的去算这些破玩意儿了。

需要说明的是，就算进行了完善的功能测试，也并不能保证功能就没有bug....因为实际工程中中各种输入信号的组合是无穷无尽的，再加上时序等等因素，功能测试不可能穷尽所有的实际情况，我们只是尽力而为。

汽车行业比较流行的单元测试工具有Cantata、VectorCAST 等等。

**三、软件集成测试**

单元测试完成以后，就要把测试好的软件单元放到整个工程里来测试。这一步对应了图1中的“software verification and integration"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCezhRYv1pr39wNLd3oO4QQxejcPklHSE5gouoR8SicgUUXxbcUk9dey6dPCQ4EF1Du3SzbdsUK2L3RhvEfJRArLWkc4RXcTic1g/640?wx_fmt=png&from=appmsg)

图3.集成测试关注整个系统的输入输出

在单元测试中，我们通过直接改变SafeVehSpd 的值来进行测试。而事实上，SafeVehSpd 数值的源头，来自CAN 总线上的车轮轮速数据。

假设如图3所示，从轮速传感器，由CAN总线传来的原始车轮轮速信号WheelSpdRaw 先经过通信接口模块 COM\_IF.c处理 ，再经过车速计算模块VehSpd.c计算以后 ,才得到信号SafeVehSpd 。那么在集成测试中，我们需要通过更改WheelSpdRaw这个信号的数值来对acc.c中的代码进行测试。这是为了验证acc.c模块和其他模块的接口是否正确以及各个模块之间是否有冲突。

进行软件集成测试的时候，图示的三个模块其实合并在了一起形成了一个“黑盒”，我们只关心最初的输入信号WheelSpdRaw 和最终的输出信号Acc\_ActSt 之间的逻辑。

在实际工程中，COM\_IF.c、VehSpd.c 和 Acc.c 三个模块很可能是由三个工程师在同时并行开发的，这就可能导致任何一个模块单独进行集成测试都通过不了。这时候就需要由项目经理或者product owner提前进行沟通协调，确保所有功能都更新以后，三个模块一起进行集成测试。

软件集成测试流行的工具和单元测试一样， 也是Cantata之流。

软件单元测试和软件集成测试都可以被称为软件在环测试（Software in the loop , SIL)。

**四、硬件在环测试（HIL）**

软件在环测试完成以后，下一个步骤就是硬件在环测试（Hardware in the loop, HIL），对应了图1中的 “Testing of embedded software”。有一些企业在HIL之前还会进行一次PIL （Processor in the loop）测试，这里就不讨论了。

HIL test也是集成测试的一种。前面说的软件集成测试，是运行在PC 仿真环境中的，而实际ECU无论是算力、内存、各种硬件性能等等方面和PC环境都有很大的不同，所以相同的功能还要继续在实际硬件环境中再测试一遍。

也就是说，HIL test与软件集成测试最大的不同在于，前者运行于实际硬件中，而后者只是运行在计算机仿真环境下。

硬件在环测试的主要工具是实际的零部件。比如测试ACC功能的话可以是ADAS控制器，或者是集成了ACC功能的毫米波雷达、摄像头等。除此之外还要有一个实验台架提供必要的运行环境、电力供应和总线接口。

常用的HIL test工具比如dspace的那些死贵死贵的测试环境，dspace control desk。

和软件集成测试一样，HIL test也是改变原始的CAN信号（例子中的WheelSpdRaw）来进行测试，只不过，这一次不是直接改变WheelSpdRaw在内存中的数值，而是通过HIL test 台架真的向ECU通过CAN 发送真实的WheelSpdRaw信号。

HIL test的测试集，也就是测试用例（test case）需要和软件需求 Software Requirement 严格对应，可以是一对一，一对多或者多对一都可以。所有的 HIL test case 都必须根据一条对应的Software Requirement 写出，但是条件就没有单元测试时候那么苛刻了。

比如为了测试需求ACC-Req 001，HIL test case 可以写成：

1. Turn ECU on;
2. Set all wheel speed at 0;
3. Turn ACC function on;
4. Observe ACC status to be SUPPRESSED;
5. Gradually increase all wheel speed to 31 kph;
6. Observe ACC status change to READY after 30 kph;
7. Gradually increase all wheel speed to 121 kph;
8. Observe ACC status change to SUPPRESSED;
9. Gradually decrease all wheel speed to 119 kph;
10. Observe ACC status change to READY below 120 kph;
11. Gradually decrease all wheel speed to 29 kph;
12. Observe ACC status change to SUPPRESSED;
13. Turn ECU off.

需要把trigger和recover的情况都覆盖到。事实上这个测试用例也可以用来测试ACC-Req 002， 这就是“一对多”的情况。

**五、实车测试**

实车测试就很好理解了，在所有前述测试都通过以后，工程师上车来实际测试相关功能。这对应了图1中的“System and item integration and testing”。实车测试用例需要根据系统需求来制定。

对于本文的例子，可以写成：

1.着车后打开ACC功能，保持车辆静止。观察仪表盘，ACC 功能未启动。

2. 将汽车加速至30kph，再次打开ACC 功能， 观察仪表盘，ACC启动。将汽车减速至29kph，观察仪表盘，ACC 功能退出。

3. 将汽车加速至110 kph， 打开ACC 功能， 观察仪表盘， ACC 启动。 将汽车加速到121kph，观察仪表盘，ACC 功能退出。

来源：知乎@木城

https://zhuanlan.zhihu.com/p/336330751

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](http...