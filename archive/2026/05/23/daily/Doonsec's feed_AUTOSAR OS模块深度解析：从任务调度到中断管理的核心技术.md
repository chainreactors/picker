---
title: AUTOSAR OS模块深度解析：从任务调度到中断管理的核心技术
url: https://mp.weixin.qq.com/s/_c1r0X4Qv_DobVpoghkFEQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:51.467841
---

# AUTOSAR OS模块深度解析：从任务调度到中断管理的核心技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDSBdVcYmRiaV0rvzzWT5icHaGL5trbdqice5zJG6JXUkuKZ7QcTpwfQC43ECjUJic3uhEibbSvHb5BUSzAjJPdvy03cRdupwPm3OPw/0?wx_fmt=jpeg)

# AUTOSAR OS模块深度解析：从任务调度到中断管理的核心技术

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

Autosar (Automotive Open System  Architecture)是一种汽车电子系统的标准化框架，旨在提高汽车电子系统的可重用性、可扩展性和可靠性。OS模块是Autosar中的一个重要模块，用于管理汽车电子系统中的任务和资源。

**01**

**OS模块的基本原理**

OS模块是Autosar中的一个重要模块，主要用于管理汽车电子系统中的任务和资源。在OS模块中，每个任务都有一个独立的任务控制块（Task Control Block，TCB），用于记录任务的状态、优先级、堆栈指针等信息。任务之间通过事件、信号量等同步机制进行通信和协调。OS模块还提供了各种资源（如锁、事件、信号量等），用于管理共享资源的访问。

OS模块还负责调度任务，根据任务的优先级和调度策略（如固定优先级调度、时间片轮转调度等），将CPU时间分配给各个任务。在任务切换时，OS模块还需要保存和恢复任务的上下文，包括寄存器值、堆栈指针等。

除了任务管理和调度，OS模块还提供了一些服务，如时间管理、定时器管理、异常处理等。其中，时间管理用于记录系统时间和处理定时任务，定时器管理用于处理周期性任务，异常处理用于处理CPU异常（如非法指令、内存错误等）。

**02**

**OS 3层的处理级别**

1. 中断级
2. 逻辑级
3. Task级

在Task级别，根据其用户分配优先权Task被调度（没有，全或是混合抢先调度），运行时间方面，是在开始执行时间时被占用，以及在任务完成时被再次释放。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDX1CvE6Cs0jibpxIWQSIh9oWKWHA20yRlFbDJSohs1RunwTtLhD6yFug7sMicfbkkQHQ6Xt4xx64zk96gibCZc0W4ZS09hhx3Hlw/640?wx_fmt=png&from=appmsg)

以下是优先级规则定义：

1. 中断优先于Task；
2. 中断的处理级别由一个或多个中断优先级组成；
3. 中断服务的流程有一个静态分配中断的优先级标准；
4. 对于中断服务例程优先级的分配取决于执行和硬件结构；
5. Task优先级是被用户静态分配的；
6. 0是最低优先级，数值越大优先级越高。

**03**

**Startup和Shundown**

OS 操作系统的启动是通过调用“StartOS()”函数来实现。在标准的 AUTOSAR 项目中，StartOS 函数由 EcuM\_Init 调用。OS系统可以设定不同的应用模式，用户可以在不同的应用模式下运行不同的应用程序，从而在不同的条件下实现不同需求，需要给StartOS指定应用模式参数。 OS系统支持多种应用模式共存，并提供配置选项供用户在系统配置阶段建立和选择所需的应用模式。一旦操作系统启动，应用模式就不能再更换，也就是说在系统运行过程中动态切换应用模式是不允许的。

StartOS()会对OS内部各组件进行初始化，激活自启动任务、报警或调度表。StartOS()的最后，会启动系统定时器，并触发第一次任务调度。如果用户使能了相关 Hook，StartOS 会在所有初始化完成之后，启动系统定时器、触发第一次任务调度之前，调用用户的 Hook，调用顺序为：

1. 调用 OsStartupHook
2. 调用各个 OS-Application 的 OsAppStartupHook

OS 操作系统的关闭是通过调用“ShutdownOS()”函数实现。“ShutdownOS()”函数会禁能所有中断,停止系统定时器运行，最终进入死循环。如果用户使能了相关 Hook，ShutdownOS 会在进入结尾处，进入死循环之前，调用用户的 Hook，调用顺序为：（1）调用各个 OS-Application 的 OsAppShutdownHook。（2）调用 OsShutdownHook。

**04**

**Task**

任务是Autosar OS的最小调度单元，它是一个可以独立执行的代码单元，可以访问共享资源、发送和接收消息等。任务可以是预定义的或动态创建的，可以按照优先级进行调度。Autosar OS支持多种不同的任务类 型，包括基本任务、扩展任务、周期任务和自启动任务等。

**1 Task的符合类**

AUTOSAR OS根据不同的软硬件需求，根据每个优先级可能具备的任务个数以及需要的是基本任务还是扩展任务等来定义了四种符合类分别为BCC1，BCC2，ECC1以及ECC2。

BCC1与ECC1不支持多次任务激活请求且每个优先级只能有一个任务；BCC2与ECC2既支持多次任务激活请求，同时也支持每个优先级可以有多个任务。各种符合类之间的兼容关系如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA4cUCzTGqianoRibtyjvCdKBbKdNNCP6fAWYicYpD2o4tRbjgP61icNibjAic8yFoYaoZ3cicQGSNjibm6t7AWcEMFic4P0ib1TJicRl3MUc/640?wx_fmt=png&from=appmsg)

1. BCC1（只对基本的Tasks，所有的Task有不同的优先级，被限制只能有一个请求激活每个Task和每个优先级只能有一个Task）
2. BCC2（象BCC1，但每个优先级可以有多个Task和允许多个请求激活Task）
3. ECC1（象BCC1，增加扩展Tasks）
4. ECC2（象ECC1，但每个优先级可以有多个Task和允许多个请求激活Basic Task）

当 OS 符合类为 BCC1 或 ECC1 时，不支持任务的多次激活，不支持为不同的任务分配相同的优先级。因此每个优先级上有且只有一个任务。当 OS 符合类为 BCC2 或 ECC2 时，支持任务的多次激活，支持为不同的任务分配相同的优先级。此时 OS 会为每个优先级创建任务队列，队列深度与该优先级上任务的个数和最大激活次数相关。

如果操作系统的符合类被配置成 BCC2 或者 ECC2，那么系统将支持任务的多次激活。系统中只有Basic Task能够进行多次激活，Extended Task只能激活一次。所以在配置Basic Task的时候都会配置一个参数叫做Task Activation，意思就是多次激活的次数限制，比方说一个Basic Task1被设置成5ms激活一次，但是此时OS被一个高优先级的任务block住没有时间来运行这个Task，那么这个任务就会出现被激活多次但是没有执行一次的情况，而这里的Task Activation则是限制这个被激活的次数，一旦超出这个次数，则OS会报错。

**2 Task状态模式**

AUTOSAR OS中存在两种任务：

1. 基本任务Basic Task：包含状态Ready，Running，Suspend
2. 扩展任务Extended Task：包含状态Ready，Running，Suspend和Waiting

基本任务则存在以下三种状态：

1. 运行状态(Running)：处于运行状态的任务可能被高优先级任务或者中断抢占从而进入就绪状态，且同一Core中任何时刻只会存在一个任务处于运行状态，任务运行结束后则将自己挂起进入阻塞状态；
2. 就绪状态(Ready):  处于就绪状态的任务由调度器决定是否启动进入运行状态，且该状态时任务切换至运行状态的前提；
3. 阻塞状态(Suspend): 处于阻塞状态的任务是被动的，可以由API函数或Alarm激活进入就绪状态；
4. 等待状态(Waiting)：扩展任务与之相比，多了此状态。当任务的运行需要等待某一或某些事件被置位时，任务进入就绪状态。

基本任务与扩展任务的状态机切换如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBqdIW64Wh8d5iaIN5OoKlZa4Up5RLV1XsV6ianX2dMXeayTtHDz5ZQJAib0pibzXdOsszibd5Uud1xY3ian0mPr9F0YFOfh8tOjwYr0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDx9bKicPteDGNnxmQibmAAYTdG0oicUkpayzUJrnm7jWlOuJRvvppVU7TJl6THjMUF1wyHPcb9DMPKYWWRkouiaJ5eKQDRIc5qOLY/640?wx_fmt=png&from=appmsg)

基本任务没有等待状态，所以只能在任务启动与终结时进行同步，基本任务的优点就是占用较小的任务与执行时间。

扩展任务则包含多个同步点，没有同步请求的麻烦，当进一步的条件无法满足时，任务则会切换至等待状态，其缺点也很明显，会占用较多的内存和执行时间。

**3 Task调度策略**

OS根据任务是否会抢占有三个不同的配置，分别是：

1. 在完全抢占调度策略下，所有 OS 的任务均为可抢占的。高优先级任务会抢占低优先级任务
2. 在完全非抢占调度策略下，所有 OS 的任务均为不可抢占的。任何任务在运行时，都不会被其他任务抢占
3. 在混合调度策略下，用户可配置任务是否可抢占。

OS 中所有的任务都是静态配置的，在系统启动时就已经存在了。

可以使用系统服务函数或“ChainTask()”来激活一个任务。系统服务函数“ActivateTask()”将处于挂起状态的任务转换为就绪状态，如果在某任务运行过程中调用了 ActivateTask()，且当前任务为可抢占任务，则ActivateTask()会基于优先级进行任务调度。如果当前任务为不可抢占任务，则ActivateTask()不会触发调度。系统服务函数“ChainTask()”会终止当前正在运行的任务，同时激活一个新任务，然后会触发一次系统调度。在真实应用，其实这两个函数用的不多，瞎勾吧用的话会对系统任务的运行状态造成不可控的时序因素。一般就是使用ActivateTask()来激活Extended Task，Extended Task只需要激活一次，Extended Task启动后，然后就是处于 WAIT 状态等待event，event发生执行后再次等待下一次event；而Basic Task则需要用Alarm来周期性激活，因为Basic Task每次运行完都需要调用TerminateTask()进入阻塞态。其实简单来说，Extended Task像是一个死循环，而Basic Task更像是一个Callback。

**1、全抢占式调度**

对于完全抢占式任务调度策略而言，当前运行的任务可在任何时刻被高优先级任务打断而被迫释放处理器控制权，具备最高优先级的任务从就绪状态转入运行状态，而当前任务被抢占从而进入就绪状态，同时保留现场环境，待下次运行时恢复。

如下图所示为完全抢占式任务调度策略，TaskA为扩展任务，TaskB与TaskC为基本任务，优先级TaskA > TaskB > TaskC。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAzWg0VOpnYrNUULUDicVLyHJnToyDFSCpPBGZ32WYHbjxdCPANa1ZkdH9JCQJpf2n8licVveuichV7uH1adCiar0NoObZsHFtZ5lo/640?wx_fmt=png&from=appmsg)

**场景1：**

当前TaskC处于运行状态，当激活TaskB进入到就绪状态时，由于TaskB优先级高于TaskC，所以TaskC被迫释放处理器控制权，调度器开始调度TaskB从就绪状态变为运行状态，直到TaskB运行完成之后，在调度TaskC继续运行。

**场景2：**

当前TaskC处于运行状态，激活TaskA与TaskB分别进入就绪状态，由于TaskA优先级高于TaskB，所以TaskA抢占内核运行, 但是由于Resource1仍被TaskC占用，而TaskA无法访问到共享资源Resource1，则被迫进入到等待状态，TaskB开始运行。TaskB运行结束后挂起之后则重新运行TaskC，TaskC运行结束后释放Resource1，进入TaskA得以由等待状态转入运行状态。

此时你会发现高优先级的任务TaskA由于共享资源被占用的原因导致不能先于TaskB运行的现象，该现象也被称为优先级反转现象。

为了解决该问题，在此需要提到AUTOSAR OS的优先级天花板模式：即将访问共享资源的任务优先级在占用资源的过程中提升至共享资源任务的最高优先级之上，从而避免优先级反转现象的发生。

即若TaskC运行过程中占用共享资源Resource1，此时即使存在需占用共享资源的高优先级任务TaskA被激活，也必须保证TaskC运行结束之后才能执行TaskA，也就意味着在重要代码执行之前，应采用资源保护机制，以免被高优先级的任务打断。

**2、非抢占式调度**

用非抢占式调度策略，那么当前运行状态的任务在任何时刻都不会其他高优先级任务所抢占，任务的切换只会发生在任务完成时。

非抢占式调度策略的问题在于任务执行时间不确定，系统调度实时性较差。如下图所示为非抢占式调度策略，可见即使高优先级任务 TaskB被激活切换至就绪状态，也必须等到TaskC执行结束之后才能够被调度。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDGlgxliamAgiclxgE1WkezxGQD0JxH403bfHTy4uWHNmicxJjKPRl11D7yJiaEGSrWgm6Mc7P9sTajrrqMMXoWMRz9nNdxJoDUpR0/640?wx_fmt=png&from=appmsg)

**4 Task调度时序图**

在软件架构设计时，为了保证CPU的负载率以及任务的前置条件，需要将每个SWC的Runnable进行定义，根据SWC的属性进行设计，如下图所示。

在原则上，需要定义一些主要规则：

1. SWC对时间要求不高的，尽量将Runnable的时间放长点。
2. 相同Task的Runnable，可以设计多个Task，通过Offset的设置，避开同一周期的Task同时运行。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDJPYe0U6ibNzwP3jLTyApOfOdHKuT1VhAH1olDXRagPGicUnzvWtJKa6iaRzicpeYmOzeadpsv8KnZPUEBvRyDocFjLVRnIYQW8tc/640?wx_fmt=png&from=appmsg)

**5 Task调度构成图**

在软件架构设计时，为了让软件架构更加清晰，可以分成三类：

1. ECU在怠速和空转时的任务处理；
2. ECU在上电或唤醒，下电或睡眠时的任务处理，以及总线收发通讯任务和消息处理任务；
3. ECU在Normal模式下运行时的任务处理（这里主要处理和执行功能所需的任务）；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCVNsFkGJ1iaoKHwiazZzWLwBKib7yb1sBibc3ZDu3gTdedVxvIPxibGOWTtcjZXAiaCamDgo5OUYbJvHKEf32iataKmFbozDllic2yPV0/640?wx_fmt=png&from=appmsg)

**05**

**Counter**

在AUTOSAR OS模块中，Counter是一种特殊的服务，用于提供时间测量和管理功能。它可以用来计算时间间隔、定期执行任务、延迟任务的执行等。

Counter可以用来测量时间间隔，从而实现时间管理功能。在AUTOSAR OS中，Counter的时间单位是tick，也就是时钟节拍。时钟节拍是指系统中固定时间间隔的单位，通常以微秒、毫秒或秒为单位。通过计算tick数，可以得到具体的时间间隔。

Counter可以用于任务调度，以实现实时控制系统的实时性和稳定性。通过设置Counter的周期和最大值，可以实现定期执行任务的功能。例如，在控制系统中，可能需要以固定的时间间隔执行任务以确保系统的稳定性。在这种情况下，可以使用Counter机制来定期执行任务，从而实现系统的实时性和稳定性。

Counter概念的引入是为了实现对硬件计数器以及软件计数器的管理，为Alarm与Schedule table提供支持。

即多个Alarm可以共用一个Counter，一个Schedule Table只能由一个Counter来驱动 。 Counter按照AUTOSAR定义可分为以下两种：

1. SystemCounter：该Counter的增加由硬件外设驱动，如Gpt或者timer等；
2. UserDefinedCounter：Counter的增加通过调用API函数IncrementCounter来实现，且每次只能增加1；

基本原则： 优先使用SystemCounter，因为可以根据Task的激活状况来减少无意义的时钟中断；

如下图所示，则较为清晰的表现了Counter，Schedule Table以及Alarm三者之间的关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDJYpMdNVJc5XJt...