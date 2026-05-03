---
title: 万字长文详解AUTOSAR存储栈（NvM、MemIf、Fee）
url: https://mp.weixin.qq.com/s/e3B1v78E7tF1LL7_BTjpBQ
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:18.738522
---

# 万字长文详解AUTOSAR存储栈（NvM、MemIf、Fee）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaC0hibjAvhKogDudz61OZx9QOJJ01NWr4Ze5Te8OjL93gxzgz7X6p2KGBSOUBylfUe2zr8n6eRZtJzMQL2GiaMkOaycdU0kmiaiaTU/0?wx_fmt=jpeg)

# 万字长文详解AUTOSAR存储栈（NvM、MemIf、Fee）

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**01**

**AUTOSAR规范解析**

**NV数据处理指南**

本章介绍AUTOSAR规范中对非易失性存储器相关的基本概念，以及应用软件组件可用的各种存取机制。我们首先从一些基本概念入手进行介绍，然后提供了所有从应用程序(最终用户)访问非易失性存储器的实际用例，帮助您更好的理解存储栈的使用。

**缩略语**

* NV：Non-volatile为非易失。
* NvM：NVRAM Manager为非易失性存储器管理。
* NVRAM Block：NVRAM块是管理和存储NV数据所需的结构体。
* NV Block：NV块是一个基本存储对象。它表示“NVRAM Block”中驻留在NV存储器中的部分。
* RAM Block：RAM块是一个基本存储对象。它表示驻留在RAM中的“NVRAM Block”的部分。
* RAM Mirror：RAM镜像是NvM内部缓冲区，用于在NMBlockUseSyncMechanism设置为True时缓存读取和写入NVRAM块的RAM块中的数据。
* ROM Block：ROM块是一个基本存储对象。它表示驻留在ROM中的“NVRAM Block”部分。
* ROM：Read-Only Memory 只读存储器。
* RTE：Runtime Environment 运行时环境。
* SW-C：Software Component 软件组件。

**NvM及其特点**

可更改性和持久性是与ECU内部数据相关联的重要属性。数据参数首先如果是可更改的，而且需要在上\下电循环中使用，那么数据就必须存储在非易失性存储器中。在AUTOSAR中，NV Data指代存储在非易失性存储器内的数据，应用程序应该只能通过NVRAM Manager(NvM)访问非易失性存储器。该模块提供数据管理和维护所需的所有服务(同步/异步)。

下图显示了应用程序和内存堆栈之间的交互以及所涉及的模块。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw91kaiceLyaibfAAoEcEwnhfBiaLse5jU31zWxTaNpmpicVOdt5FnaNmxsGB1Wnia2E1stKGmfGuR6wt2A/640?wx_fmt=png&from=appmsg)

“基本存储对象”是“NVRAM Block”的最小实体。多个“基本存储对象”可用于构建NVRAM块。“基本存储对象”可以驻留在不同的存储器位置(RAM/ROM/NV存储器)中。下面介绍这些基本的存储对象：

* RAM Block：它表示在“NVRAM Block”中驻留在RAM中的部分。它由用户数据和(可选的)CRC值和(可选的)NV块头组成。它用于保存实时数据。这是“NVRAM Block”的可选部分。
* ROM Block：“ROM块”是“NVRAM Block”的可选部分，它驻留在ROM中。ROM块的内容具有持久性，在程序执行过程中不能被修改，并且驻留在ROM/Flash中。它被用于在“NV Block”空白或损坏的情况下提供默认数据。
* NV Block：它表示“NVRAM Block”中驻留在NV存储器中的部分。“NV块”是“NVRAM Block”的强制性部分。NV块的内容具有持久性，可以在程序执行期间修改，并且驻留在Flash中。它由CRC值和(可选地)NV块头组成。它用于保存跨上\下电周期的数据参数。
* Administrative Block：“管理块”是“NVRAM Block”的强制性部分。管理块的内容具有非持久性，并且驻留在RAM中。它用于保存对应NVRAM块的属性/错误/状态信息以及特定于NVRAM管理类型为“数据集”的块索引。

NvM支持以下NVRAM块管理类型:

* Native NVRAM block：原生NVRAM块是最简单的块管理类型，它允许以最小的开销从NV内存中进行存储/检索。它包含一个NV Block，一个RAM Block，以及零到一个ROM Block以及一个Administrative Block。
* Redundant NVRAM block：相比原生NVRAM块，冗余NVRAM块提供了增强的容错性、可靠性和可用性。它增加了对数据破坏的抵抗力。冗余NVRAM块包含两个NV块，一个RAM块和一个管理块。如果与冗余NVRAM块关联的NV块被视为无效(例如在读取过程中)，将尝试使用来自未损坏NV块的数据恢复NV块。它包含两个NV Block，一个RAM Block，以及零到一个ROM Block以及一个Administrative Block。
* Dataset NVRAM block：它可以表示大小相等数据块的数组。应用程序可以一次性访问该数据块中的一个。它包含一个到NvMNvBlockNum个NV Block，一个RAM Block，零个到NvMNvBlockNum个ROM Block以及一个Administrative Block。数据集(NV+ROM块)的总数必须小于255。用户通过使用 NvM\_SetDatalndex（）设置相应的索引来访问特定数据集元素。索引从0到NvMNvBlockNum-1的元素表示NV块，而索引从NvMNvblockNum到NVMNVBlockNum+NvMRomBlockNum-1中的元素表示 ROM 块。NVRAM 块用户必须在访问数据元素之前确保已经选择有效的数据集索引。

在使用NvM模块时，支持两种类型的RAM同步机制（隐式/显式）。

在隐式同步中，应用程序和NvM可以并发访问一个公共RAM块（由应用程序提供）。应用程序通过调用NvM提供的API可以读取/写入NVRAM到/从公共RAM块。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw91kaiceLyaibfAAoEcEwnhfBoKdnPaCQo5vzqO8Eic68G2FrCFMYSND3oTKmdB9ed6PP4O5xn37Efuw/640?wx_fmt=png&from=appmsg)

在隐式同步中，应用程序和NvM可以并发访问一个公共RAM块（由应用程序提供）。应用程序通过调用NvM提供的API可以读取/写入NVRAM到/从公共RAM块。

* 应用程序首先需要将写入的数据填充到准备好的RAM块。
* 应用程序调用NVM\_WriteBlock或NvM\_WritePRAMBlock，将RAM指针传递给NvM，并将控制转移到NVM模块。
* 从现在开始，应用程序不得修改RAM块，直到通过轮询来查询到请求的成功或失败。在此期间，RAM块的内容可以被读取。
* 应用程序可以轮询来获取请求的状态，也可以通过回调函数异步通知。
* 在完成NvM模块操作之后，RAM块可进行修改以重复使用。

多Block的写入过程如下（NvM\_WriteAll）：

* EcuM或BswM发出NvM\_WriteAll请求，该请求将控制转移到NvM模块。
* EcuM或BswM可以使用轮询来获取请求的状态，或者可以通过回调函数得到通知。

在显式同步中，NvM中定义了一个RAM镜像，用于与SW-C的RAM块交换数据。NvM回调API将SW-C提供的RAM数据写入RAM镜像，最后NvM将RAM镜像中的数据写入到NV块。应用程序通过NvM模块的回调程序来双向传输数据。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw91kaiceLyaibfAAoEcEwnhfBFAwTCJtoYuqv2Pz62aRZcibBtNh51uR5b7GWhqiaezKz7VU09nKvpWiaw/640?wx_fmt=png&from=appmsg)

这种方式的优点是应用程序可以有效地控制其RAM块。NvM负责使用ReadRamBlockFromNvM/WriteRamBlockToNvM配置的两个回调函数将一致的数据复制到NvM模块的RAM镜像中，由NvM负责确保整个读取/写入过程中RAM镜像的一致性问题。缺点是针对每种类型的操作都需要额外的RAM，且镜像RAM的大小与使用此机制的最大NVRAM块的大小相同。

如果有一个模块(例如NvBlockSwComponentType，或者用户自己建立的一个NvM\_SWC)，它从NvM模块的角度来看是NVRAM块的所有者，来同步不同的SW-C，则可以允许不同SW-C间共享NVRAM块。

下面是使用显式同步单Block的写入过程：

* 下面是使用显式同步单Block的写入过程：
* 应用程序首先需要将写入的数据填充到准备好的RAM块。
* 应用程序发出NvM\_WriteBlock或NvM\_WritePRAMBlock请求。
* 应用程序可以在此期间修改RAM块，直到NvM模块调用NvMWriteRamBlockToNvM。
* 如果 NvM 模块调用NvMWriteRamBlockToNvM，则应用程序必须为NvM模块请求的目的地拷贝与特定RAM一致的RAM块副本。应用程序可以使用返回值E\_NOT\_OK 来表示数据不一致。NvM 模块将接受否定返回值NvMRepeatMirrorOperations次，然后推迟请求并继续其下一个请求，直到拷贝成功。
* 拷贝成功之后，SW-C可以再次操作之前准备好的特定RAM块。
* SW-C可以使用轮询来获取请求的结果状态，也可以通过回调函数异步得到通知。

NvM模块内部使用CRC生成例程(8/16/32位)来生成并检查NVRAM块的CRC，这是可配置选项。NvM模块通过实现基于CRC的比较机制来提供跳过未更改数据的写入。可以通过设置配置参数NvMBlockUseCRCCompMechanism来启用基于CRC比较机制。

NvM模块在读取管理类型为“NATIVE”和REDUNDANT”的NVRAM块时通过加载默认值(如果通过参数NvMRomBlockDataAddress 或参数NvMInitBlockCallback配置)提供隐式错误恢复。通过调用 NvM\_RestoreBlockDefaults，所有块管理类型都可以明确的检索ROM数据，对于DATASET管理类型必须在调用此API之前设置相关索引(指向ROM 块)。NvM模块写入NVRAM块时提供的错误恢复机制是通过执行写入重试(不管NVRAM块管理类型如何)。

在写验证的情况下，当RAM块被写入NV存储器时，NV块会立即被读回并与RAM块中的原始内容进行比较。如果RAM块中的原始内容与读回内容不相同，则执行写重试，如果生产错误报告使能，则向DEM报告生产代码错误NVM\_E\_VERIFY\_FAILED。如果回读操作失败，则不执行读取重试。

对于某些NVRAM块，可能需要在NvM\_ReadAll期间保留相应RAM块的数据内容不被重写，以防存储在相应NV块中的数据比存储在RAM块中的数据更旧(例如，在RAM中的数据尚未写入NV存储器时的热重置)。在这种情况下，RAM块必须保存在重置安全的RAM区域，并且配置参数CalcRamBlockCrc必须设置为TRUE(这意味着相应的NV块也具有配置的CRC)，并且参数NvMSetRamBlockStatusApi必须设置为TRUE。在每次改变RAM块数据内容后，必须为相应的NVRAM块调用NvMSetRamBlockStatus，入参BlockChanged设置为TRUE。NVRAM管理器随后将重新计算此RAM块的CRC并将结果存储在分配在重置安全RAM区域的内部变量中。当然，这种NVRAM块必须配置有效的永久RAM块(NvMRamBlockDataAddress)或使用显式同步回调函数(NvMReadRamBlockFromNvM)。

如果配置参数NvMSetRamBlockStatusApi被设置为FALSE的值，则NVRAM管理器在NvM\_WriteAll过程中将RAM块的数据内容复制到所有配置为WriteAll(配置参数NvMSelectBlockForWriteAll被设置为TRUE的值)且具有永久RAM块(NvMRamBlockDataAddress)或显式同步回调函数(NvMReadRamBlockFromNvM)的相应NV块。为了最大程度地减少NV存储器的写入次数，最好只将那些RAM块与NV块内容不一致的RAM块复制到相应的NV块。为了在NvM\_WriteAll过程中启用此功能，必须将配置参数NvMSetRamBlockStatusApi设置为TRUE。在这种情况下，NVRAM块用户在每次对RAM块数据进行更改后通过调用对应NVRAM块的NvM\_SetRamBlockStatus来通知NVRAM Manager参数已经被修改。这样，在NVM\_WriteAll执行期间只有BlockChanged为TRUE的Block才会被处理。

NvM模块在启动期间(即在处理请求NvM\_ReadAIl时)，可能会因为程序升级，导致新程序对存储的参数布局与旧程序存在差异，那么此时的参数获取行为将受到两个配置参数NvMDynamicConfiguration和NvMResistantToChangedSw的影响。对于配置参数NvMCalcRamBlockCrc设置为TRUE的NVRAM块，NvM在执行读取等操作时首先会检查对应RAM块数据的有效性。如果检测到RAM块内容无效，或者参数NvMCalcRamBlockCrc设置为FALSE，则会进一步检查NV Block的有效性。检测到有效的NV块将复制到其对应的RAM块。如果检测到无效NV Block，则将加载默认数据(如果通过参数NvMRomBlockDataAddress或参数NvMInitBlockCallback进行了配置)。在ECU项目中，当程序不需要对存储布局不一致做出反应时，需将参数NvMDynamicConfiguration设置为FALSE。如果NVRAM块的布局已更改，而已存储在NV Memory中的NV块仍与旧布局相对应则在NvM\_ReadAll过程中可能出现严重问题。这方面的一个例子是，当添加一个新的NVRAM块时，许多其他块的标识符可能隐式地被更改，这可能导致从NV存储器读取错误的数据。对于这种情况，可以配置NvM模块，使其不会尝试使用NV存储器的数据初始化RAM块。这必须通过将配置参数NvMDynamicConfiguration的值设置为TRUE来完成，还需通过集成器修改配置参数NvmCompiledConfigurlD向NvM模块指示NVRAM配置已经发生变化。NvM模块使用单独的NVRAM块将该值存储在NV内存中。每次执行启动过程(NvM ReadAll)时，NvM模块将NV存储器中存储的值与配置参数 NvmCompiledConfigurlD的值进行比较。在这种情况下，根据相应配置参数NvMResistantToChangedSw的值，NvM模块在处理NvM\_ReadAll期间有两种不同的方法初始化NVRAM块。

* 如果需要忽略相应NV块的数据，而是默认数据(如果通过参数NvMRomBlockDataAddress或 NvMlnitBlockCallback)应被加载，参数 NvMResistantToChangedSw的值应该设置为FALSE。
* 即使在配置更改的情况下，仍然需要用来自NV块的数据初始化RAM块，配置参数NvMResistantToChangedSw应设置为TRUE。行为将与没有发生配置更改时相同。

对于将 NvMResistantToChangedSw设置为TRUE的块，集成器必须确保在ECU 的剩余生命周期内不得更改以下配置参数，否则将无法从NV内存中成功检索数据:

* NvMResistantToChangedSw（必须不能从TRUE改成FALSE）
* ShortName
* NvMBlockUseCrc
* NvmBlockCrcType（如果NvMBlockUseCrc设置为真）
* NvMStaticBlockIDCheck
* NvmNvramDeviceId
* NvmBlockManagementType
* NvmNvBlockLength
* NvmNvBlockBaseNumber

NvM模块在处理NvM\_WriteAll期间，NV存储器中的值将被对应RAM中的值所覆盖。根据所用模块NvM、Fee和Ea的实施情况，可能会有其他限制。请参阅相应的用户手册。

**通过RTE访问NvM**

涉及的Interfaces有以下两种：

* Client-server interface：客户端/服务器interface提供了一些可以在NvMService上由客户端调用的操作。如果是由NvM为SW-C提供的服务，则NvM充当服务器，SW-C充当客户端。此外，NvM可以使用此类接口向应用程序提供通知，在这种情况下，客户端和服务器的角色被交换。
* NvDataInterface：非易失性数据interface定义了要在非易失性的块组件和软件组件之间交换的多个VariableDataPrototype。这些VariableDataPrototype可以映射为在非易失性块组件中实现的完整RAM块或RAM块的元素。

若通过服务组件访问NV Data，则NvM配置为ServiceSwComponent。在这里，想要读/写数据到NVRAM的SW-C需要使用客户端/服务器接口提供的标准的NvM服务。读者可以在后边的实例介绍中涉及的实例1和实例2看到具体的实现。使用这种方法的好处有以下几种：

* 使用SW-C模板实现基本的通用配置以容纳Nv...