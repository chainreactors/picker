---
title: 车载DEM诊断模块基础知识详解
url: https://mp.weixin.qq.com/s/yvNOW_kHtjQiKQL630H9Ag
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:27:45.976647
---

# 车载DEM诊断模块基础知识详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA5ibMfJUM08fUBkeBJsW2s5fDIibiccVLZoGObDlicq8ByicRibLgATMyhB9TggDHtIu1c6vrKZkEqroyfibSPcFrl6lnI6mcChXfwqo/0?wx_fmt=jpeg)

# 车载DEM诊断模块基础知识详解

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

**DEM简介**

DEM 是 Autosar 诊断模块的重要组成部分，主要负责处理和存储诊断事件以及关联数据。与 DEM 相关的标准主要包括两个部分：ISO 14229（Unified Diagnostic Service，UDS）和ISO 15031（On-Board Diagnosis，OBD）。

Autosar 架构中的 DEM 模块如图所示，处于整个架构的 BSW 层。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAyRkuvmricjoQVxvjgqMP05IQod7lTnXXWJWO1pPsa3UiaLgy2PAB3s1C9icooxMNdY40WzqNLO0KBicDdxBPUCicnQib6Pibic4sfZZM/640?wx_fmt=jpeg&from=appmsg)

Autosar 框架

DEM 与其他模块的交互如下图所示，DEM 主要与 DCM、NvRAM、FIM、EcuM、SWC 和 BSW 模块交互。其中，EcuM 主要负责控制 DEM 模块的初始化和反初始化；DEM 模块会监控 SWC 和 BSW 模块的运行情况，如果发现有异常则会置起事件，报DTC；NvRAM 主要负责提供内存空间，来保存 DTC、扩展帧和冻结帧数据。DCM 主要负责 UDS 服务的执行，其中14/19 服务为清除 DTC 和读取 DTC 相关信息；FIM 模块根据 DEM 中的状态使能或失能 SWC 的一些功能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaC1DibakRXFdy7zVgibX3Tjektj04dkDR6Kiby55ywdiapVdPcOLedJ9NCdVys2Dria2icTrTOibwY9Z0MsXDDa9X6qTuIe3PkUTCLLug/640?wx_fmt=jpeg&from=appmsg)

DEM 交互对象

**02**

**DEM基础知识**

**2.1 Diagnostic Trouble Code（DTC）**

DTC 是车辆诊断系统中，故障状态的数字通用标识符，不同的 DTC 表示车辆的不同故障。DTC 格式如图所示，由DTC High Byte、DTC Middle Byte、DTC Low Byte 和 DTC Status 组成。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCWJKBd9Uhf1b5Kia6cKVicziafU83vjuialBdk9QndjGydHw1P2eUbQzYBGH1oe0Qsa1sBSHBIJl5ldmfpf0CPV2EAZy6tCRopN9k/640?wx_fmt=png&from=appmsg)

DTC 格式

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCQbrj038QIfmpLNXsqOMosbylHToicaF3y8icjoIlBFuF1PbbCCsQJ20icJWr839vtotEUibZklkwyeTunfOVcoVXzfWOeKaf8QibI/640?wx_fmt=jpeg&from=appmsg)

DTC 格式展开

第一位表示故障所属系统（四种），第二位表示故障类型（四种）

第一位：

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDdxMA0zl4bibnAK5tvJWq4STceBPz91nDFvePoj8lhB5l9xTfYzicSW87DibWlcGdhIefdFicFibzlsXKkvPGicGPmHnDXdk9WcnJnc/640?wx_fmt=jpeg&from=appmsg)

第一位

第二位：

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDthK8CcsdFThJTM0whzm0bcJYAoV9GtnBHEIfJpb6nk86zdjibpZ9jPiaKRo5sVEEVArZ3PTibKXE6fMqrNAq3ONNOp6rCE6tBTo/640?wx_fmt=jpeg&from=appmsg)

第二位

第三至第五位表示发生故障所属的子系统，DTC Low Byte 描述的是故障种类和子类型（如信号、电路、短路等），如果不需要该字节，也可以填充为 0x00。 一般来说，故障种类相同的故障，如 CRC、RollingCounter 故障，它们的故障种类码应该相同。

举个例子，比如 DTC 显示码为 U023587，根据上述规则， U = 0x11，0 = 0x00，U0 = 0x1100 = 0xC。因此，DTC 故障码为 C23587。

拓展：在 DCM 模块有一个 85 服务可以抑制 DTC 的报出。一般叫 Control DTC Setting，如果打开该服务，那么 DTC 将不能置出。

**2.2 DTC Status**

DTC Status 字节中 8 个 bit 分别代表不同的含义，如图所示。在 Configurator 中，根据需求可以选择你需要的 bit 位，一般常用位为 bit0 和 bit3。Bit0 为最近一次测试失败，bit3 为确定 DTC 故障可以被记录到 NvRAM中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCTpxSV28ecoe9ianJGhboNt7uSntzVUBicCbDd7J4xXKV4fJWjdZbwBPOIlm4DnseJbmgXxr7Z2U8VWwuoNamKStqFjheicPrwKA/640?wx_fmt=jpeg&from=appmsg)

DTC 状态

举例说明，比如读取到的 DTC status 为 0x50。那么转为二进制则为 0x0101 0000，对应 bit6 和 bit4 置起，根据表格可以看到，从上次故障清除后，还未对 DTC 进行检测，且本次操作循环也未对 DTC 进行检测。根据 DTC status 的值，可以考虑是否是 Event 的前置条件没有满足，导致未检测。再比如读取到的 DTC status 为 0x27。那么转为二进制则为 0x0010 0111，对应 bit0，bit1，bit2 和 bit5 置起，bit3 没有置位，说明本次循环有故障置出，但是并未到达记录的条件。

**2.3 DTC Debounce策略**

为了防止出现故障误报的现象，ISO 14229 中规定了 Debounce 功能，只有满足一定条件时，才能确认故障发生，也就是 confirmedDTC（DTC Status bit3）置位。Debounce 分为基于计数器的 Debounce 策略和基于时间的 Debounce 策略。

**2.3.1 基于计数器的 Debounce 策略**

基于计数器的 Debounce 策略有以下参数，参数的含义如图。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCSibEsjibDupR6BhIfJkEVvdibcPf4WaiaY946K2etZcoYNevQc09B7zpEMPaNIj6hWdBG17KjlP1wmbYbsVg4ibkF9PmUGGRajjAs/640?wx_fmt=jpeg&from=appmsg)

Debounce 参数

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaD6z1ygibJ9u2ciaRKEMiaUibOA5jjSCM3Q95fVabB6ozJdmguibRbwmmAfnerfwHsj6R1kYWCYrSdMFxFTRuWDKSGAlibESJ55yNGlo/640?wx_fmt=jpeg&from=appmsg)

时序图

基于计数器的 Debounce 原理如图所示，当第一次测试结果为 Prefailed，计数器开始计数。如果第二次测试结果仍为 Prefailed，则 Fault Detection Counter 增加，增加的步长为 DemDebounceCounter IncrementStepSize，当 Fault Detection Counter 等于 Failed 时，才算故障满足失败条件，确定被记录。如果第二次测试结果为 Prepassed，则 Fault Detection Counter 直接跳到 DemDebounceCounterJumpDown Value 开始重新计数。反之，Prepassed 的逻辑也相同。但若测试结果是 Failed 或 Passed，则直接通过，不需要Debounce。

拓展：除此以外，还有一个配置为 unconfirmedDTCLimit，它的作用是在 fault detection counter 到达 failed 之前还有一个 threshold。用于预警曾经有过失败但未到达当前故障的记录条件，引起警惕。

**2.3.2 基于时间的 Debounce 策略**

基于时间的 Debounce 策略有以下参数，参数的含义如图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDOAxRYNK3FPbuxRlicMDN8ia1tSffOugqTlZuWlJzw1SmiaBhUWbpe282lQPfNLL0dt5HdNCrwkicFFlYdbmpFdib5zTC8AEjqVdZI/640?wx_fmt=jpeg&from=appmsg)

Debounce 参数

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA4ajXicWfmrLoAfbFGY5emUaaekVX4Jypto5sTMqRjaaqtCmQkIkpwLzOHicvmib0JVSNsa35fNsbkqLnt6m4p1icRPPncQ6CPzQE/640?wx_fmt=jpeg&from=appmsg)

时序图

基于时间的 Debounce 原理如图所示，当测试结果为 Prefailed 时，计时器开始计时，如果到时间限制，还没有出现 Prepassed 或 Passed，则记录为 Failed，如 t1 时刻。Prepassed 的逻辑与此相同，如 t2 时刻。

当测试结果为 Prepassed 时，计时器开始计时，但是还未到时间限制时，测试结果出现了 Prefailed，则 Fault Detection Counter 直接跳回到 0 开始重新计时，如 t3 时刻。如果测试结果出现了 Failed 或 Passed，则直接通过，不需要 Debounce。

拓展：其实上述两种策略均只考虑当前操作循环，另外还有一个 debounce 策略会考虑连续多次操作循环均报错才会 confirmed 为历史故障，称为 confirmedDTCLimit。

**2.4 DTC Aging策略**

在诊断系统中，如果满足一定的条件，可以认为系统已经从故障中恢复。原因是，在一个相对较长的过程中，如果车辆没有发生这个故障，我们可以认为这个故障是一个偶发的现象，也可以认为现在的车辆处于一个相对稳定的状态，所以需要设置 DTC 的故障恢复条件。

Aging Counter 的例子，如图所示。Aging Counter 在完成测试未失败的操作周期后，开始递增。因此，Aging Counter 开始计数的条件为：testFailed=0，pendingDTC=0，confirmedDTC=1。当完全满足老化标准时（例如，DTCAging Counter达到特定值），confirmedDTC 设置为 0，DTC 会从内存中清除掉。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDwfE7k26Xf1LEqmW6MtPfux2WrzicYBwLRgUO937RicQnGtygkUm1hgX0GxqawaflibhLMKia3dyj1tp6ibpp8H6E4do5DLg6K037s/640?wx_fmt=jpeg&from=appmsg)

时序图

拓展：上述策略只是其中一种，Aging 在 Vector 提供的文档中，有六种策略，如图所示，可以根据需求选择对应的策略。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBTrPmgwibGS6uaFz9odydia72lDYDhMrLjialu6ZyW6Q2tqBKtXRD3Jar8VYbk1W1L7FX7cJnjuwjWJ5Y8iaNqxlSfeaqvbJW4VLY/640?wx_fmt=jpeg&from=appmsg)

Aging 策略

**2.5 Extended Data 和 Snapshot Data**

扩展数据与冻结帧数据是辅助工程师进行诊断的数据。扩展数据会在 pendingDTC 置位后，与 DTC 一同保存在NvRAM 中。扩展数据有 Fault Detection Counter、Aging Counter、Event Id 和 Occurrence Counte r等。冻结帧数据在记录发生故障时的工况（由一系列的 DID 组成，如 Environment Temperature、ECU Voltage、Vehicle Speed 和行驶里程等数据），当 confirmedDTC 置位时，将记录冻结帧。可以通过 DCM 的 19 04 和 19 06 服务读取它们的值。例如 19 06 XX XX XX CC（XX XX XX：DTC code，CC：需要读取的数据 ID）。

拓展：扩展数据和冻结帧都可以配置不同的 trigger 和是否 update。用户可以灵活使用。

**03**

**Precondition 和 Precondition group**

在对 Event 进行监控时，通常会设置一些前提条件，当这些条件全部满足时，才对这个 Event 进行监控，否则不对 Event 进行监控。常见的 precondition 有对电压的判断，有对通讯状态的判断，有对其他 Event 状态的判断等等。这些单个的 precondition 组成了一个 precondition group，它们之间的关系是多对多的，如图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBzLkA8E8XAEG9db2iaxaHfZoVfiaHvibp4nPumEHukljDYYUQGibNo1hhfSe7vO1cIoibOZdpAicNzj0oibObLF43z6QibLyDrOFaqHL4/640?wx_fmt=jpeg&from=appmsg)

Precondition 和 Precondition Group 映射关系

DEM 模块正常运行后，会周期性的检测这些 precondition，一旦条件不满足则会立即停止检测该 Event。Event 和 precondition group 的对应关系是多对一的关系，即一个 precondition group 可以关联多个 Event，但是一个 Event 只能有一个 precondition group。

来源：知乎@DaVinci

https://zhuanlan.zhihu.com/p/661669914

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jp...