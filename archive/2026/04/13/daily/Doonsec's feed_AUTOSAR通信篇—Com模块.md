---
title: AUTOSAR通信篇—Com模块
url: https://mp.weixin.qq.com/s/zEhufuRVoFj-ILsCNZJlDQ
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:43:26.785426
---

# AUTOSAR通信篇—Com模块

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCSe8GWd64HOsFYx3xZzqUCrvf77CVHBUHPL9j8XlX1cNRicCDIwickULEwZCmbv3f2RUcuiaRgEVKfic1olCrkuO6dfV7DK7icAPBo/0?wx_fmt=jpeg)

# AUTOSAR通信篇—Com模块

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**概述**

对不同速率的总线网络提供数据交换；为汽车控制单元应用软件提供了统一的通信环境，为内部和外部通信定义了公共的软件通信接口和行为；

AUTOSAR COM模块进行发送和接收信号，为RTE提供面向信号的接收与发送函数。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA2tyTia8xgLsyo5v4iaBp3xuTQV6vvCNC3ibQ3yAmWJcNs8xDrqXLo33DsKcg3ymVdlE015bNVhaJpxWPfjP59MU2y3A4WkH4xQc/640?wx_fmt=png&from=appmsg)

**02**

**signal信号**

**3种信号值**

**初始值：**AUTOSAR COM模块使用配置参数ComSignalInitValue的低N位初始化发送方和接收方的每个N位的信号类型, 配置的ComSignalInitValues也用于I-PDU的初始化信号。一个信号的ComSignalInitValue可以与ComSignalDataInvalidValue值相同。初始化阶段会清空所有update-bits值。默认情况下，所有I-PDU组应在停止状态，不得由Com\_Init()调用启动。

**数据无效值：**通过调用Com\_InvalidateSignal, AUTOSAR COM模块将在内部执行带有配置ComSignalDataInvalidValue的Com\_SendSignal。ComTransferProperty和传输模式决定了ComSignalDataInvalidValue在总线上的传输。内部执行的带有数据无效值的Com\_SendSignal，会决定被用作过滤器的数据无效值和TMS当前值。VFB仅为复杂数据类型定义一个属性。因此，一个失效的复杂数据类型到一个失效的信号簇的最佳映射是使一个信号簇的所有信号失效。因此，RTE还可以通过调用Com\_InvalidateSignalGroup来请求使整个信号簇无效。

**正常值：**初始化阶段之后的有效值，包括COM部分收发的信号值。

**发送信号属性—Triggered属性+Pending属性**

**Triggered属性-触发：**调用Com\_SendSignal( )服务请求具备Triggered属性的信号发送，可以触发相关I-PDU的发送，但是如果该I-PDU的发送模式被配置为Peiodic时，只更新信号的值，不会触发相关I-PDU的立即发送，而是在下一周期到来时触发发送。

**Pending属性-延迟：**Com\_SendSignal( )服务请求调用具备Pending属性的信号发送，不会触发相关I-PDU的发送。

**信号的初始化**

AUTOSAR COM在Com\_Init()执行时，将初始化所有I-PDU内容，首先用默认值（ComTxIPduUnusedAreasDefault）表示字节，然后根据所包含信号的初始值（ComSignalInitValue)和更新位来表示位。初始化过程中无法使能ECU内部的通信功能。

**信号的对齐方式（大小端）**

（小端）：信号的高位（MSB）放在高字节的高位，信号的低位（LSB）放在低字节的低位；

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBmPBSEOv9Ho8BC30NTOZy28Csn7K5wia8DgEho4FkAgTicTZhDxodjNNYcMSQMNJd20Tl35cDvMaPKImC7pkrqyib9znq9SsMc54/640?wx_fmt=png&from=appmsg)

（大端）：信号的高位（MSB）放在低字节的高位，信号的低位（LSB）放在高字节的低位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAria962t9rMyEticnAWumtcIqBf7bBAibO4E1LWFBStyUP913iaBmnMaXVegajib3MlLEKrviblKvOnpwyDFwrWgkRuuX2SC8kmBXII/640?wx_fmt=png&from=appmsg)

**信号的收发**

**a.发送（上层—下层）**

发送过程中，应用层调用COM层提供的信号或信号簇发送函数，根据配置，信号或信号簇的数据经过字节序转换后被更新到I-PDU中相应的位置。AUTOSAR COM规范中同一I-PDU可以设置两种发送模式，对其中各信号的传输模式条件进行计算，I-PDU选择其中一种发送模式进行发送。然后启动发送死限监控，调用PduR\_ComTransmit()函数将I-PDU发送到下层。

根据该信号的配置判定是内部信号还是外部信号。

* 内部发送：直接将信号数据复制到接收信号数据区，并执行通知操作；
* 外部发送：若该信号发送属性为触发triggered，则该信号所属的I-PDU将立即发送（除非该I-PDU发送模式为周期传输模式），若该信号发送属性为延迟pending，则不进行传输，发送时，信号经过字节顺序转换后数据被复制到I-PDU中，同时设置相关更新位信息，然后根据该I-PDU的TMS切换传输模式，进行传输并设置启动相关定时器。

**b.接收（下层—上层）**

接收过程中，当下层接收到I-PDU时，下层将调用COM层提供的指示函数Com\_RxIndication()，取消并重启接收死限监控，将I-PDU的数据从底层拷贝到COM中。调用信号或信号簇的接收函数后，该I-PDU中的信号或信号簇将经过字节顺序转换、符号扩展和接收过滤后，数据被拷贝到应用层。

接收过程要判断是内部信号还是外部信号。

* 内部接收：直接将信号数据复制到接收信号数据区；
* 外部接收：首先判断对于的I-PDU组是否启动，若启动，返回E\_OK，否则返回COM\_STOP，取消并重启该I-PDU的相关死限监控定时器，将数据复制到I-PDU数据区，I-PDU中的信号经过字节书序转换、符号扩展和过滤机制后，复制到接收信号数据区，再执行通知操作，通知上层软件调用相关API函数接收信号。

**字节序转换和符号扩展**

com模块支持的数据类型：boolean，uint8，uint16，uint32，uint64，sint8，sint16， sint32，sint64，uint8[n]，float32和float64，其中uint8[n] 对应于UINT8\_N或UINT8\_DYN。

AUTOSAR COM支持所有有符号和无符号整型数据类型的字节序转换，同时会将非整型数据类型视为对应匹配的整数数据类型，或者不解释它们的内容，防止它们的ComSignalEndianness被配置为OPAQUE。

对于不透明数据字节序的转换，必须配置为OPAQUE。

AUTOSAR COM会扩展接收信号ComSignalType的大小。

注：必须考虑签名数据的平台特定表示。  负值的签名数据将被正确映射。例如：一个10位有符号信号被接收并被Com\_ReceiveSignal复制到一个16位有符号整型变量。 如果接收到signal值为(-3)10进制，类型为sint16，则接收到的10位信号有取值为1111111101b。 当将其复制到16位整型变量时，值将扩展到11111111111101b  。

除了字节顺序转换外，AUTOSAR COM模块不支持ComSignalType FLOAT32或FLOAT64的信号的进一步转换。 也就是说，支持字节顺序转换，但不支持复杂转换或分数、指数、符号或偏差值的标准化。

**信号的过滤机制**

AUTOSAR COM模块会评估每次过滤的条件为真或假；

AUTOSAR COM模块会在接收端滤出想要过滤的信号；

AUTOSAR COM模块应在发送端对传输模式条件(TMC)使用过滤机制，但不应过滤发送端信号；

AUTOSAR COM模块提供的过滤算法：

* ALWAYS: 总是通过，若一个信号的过滤算法配置为ALWAYS，那么这个信号的TMC永远为True
* NEVER: 总是不通过，若一个信号的过滤算法配置为NEVER，那么这个信号的TMC永远为False；
* MASKED\_NEW\_EQUALS\_X: 若一个信号的过滤算法配置为MASKED\_NEW\_EQUALS\_X时，只有当新值与掩码按位与后等于设定的某一值时，这个信号的TMC才等于True；
* MASKED\_NEW\_DIFFERS\_X: 若一个信号的过滤算法配置为MASKED\_NEW\_DIFFERS\_X时，只有当新值与掩码按位与之后不等于设定的某一值时，这个信号的TMC才为True；
* MASKED\_NEW\_DIFFERS\_MASKED\_OLD: 若一个信号的过滤算法配置为MASKED\_NEW\_DIFFERS\_MASKED\_OLD时，只有当新值与掩码按位与之后的值不等于旧值与掩码按位与之后的值时，这个信号的TMC才为True；
* NEW\_IS\_WITHIN: 若一个信号的过滤算法配置为NEW\_IS\_WITHIN时，只有当新值在某一设定的范围内时，这个信号的TMC才为True；
* NEW\_IS\_OUTSIDE: 若一个信号过滤算法配置为NEW\_IS\_OUTSIDE时，只有当新值不在某一设定的范围内时，这个信号的TMC才为True；
* ONE\_EVERY\_N:若一个信号的过滤算法配置为ONE\_EVERY\_N时，该信号值每更新N次，这个信号的TMC值为True；

注：对于ComSignalType FLOAT32、FLOAT64、UINT8\_N或UINT8\_DYN的信号，AUTOSAR COM模块应只支持配置为ALWAYS、NEVER或ONE\_EVERY\_N的ComFilterAlgorithm  ；对于ComSignalType配置为BOOLEAN的信号，AUTOSAR COM模块应只支持ComFilterAlgorithm配置为

ALWAYS；NEVER；MASKED\_NEW\_EQUALS\_X；MASKED\_NEW\_DIFFERS\_X；MASKED\_NEW\_DIFFERS\_MASKED\_OLD； ONE\_EVERY\_N；

**过滤处理：**

如果AUTOSAR COM模块在接收端过滤掉一个信号（信号簇），即filter condition的结果为false，则AUTOSAR COM模块应丢弃该信号（信号簇），不进行处理，及不会将该信号的值放入old\_value中；

如果AUTOSAR COM模块将一个信号的过滤器计算为true(值没有被过滤掉)，那么AUTOSAR COM模块应将该信号的值放入old\_value中；

如果在send-API编写相应的信号之前对过滤器进行了计算，则需要有一种方法来确定该信号的过滤器状态。 一些筛选器需要new\_value来计算筛选器。 然而，这只有在使用send-API更新信号之后才可用。 因此，有必要在第一次发送之前为new\_value定义过滤器使用的值。

对于配置的接收滤波器MASKED\_NEW\_DIFFERS\_MASKED\_OLD的信号, AUTOSAR COM模块将处理该信号在接收截止日期监测超时后收到的第一个值，就像该值已经通过了过滤条件一样；

在相关的I-PDU的RX截止超时后AUTOSAR COM模块会让过滤器MASKED\_NEW\_DIFFERS\_MASKED\_OLD传递任何值。

**03**

**上下层数据传递**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBGcfXBxdDtxCtiaACEVqjWIk1fibosCwWFvibaSoGdJ46cWK3zFcn3QcB9eKK8icRPxDfFWufnCQzLsLNPMMcTBZoMZ9UPn04sWGM/640?wx_fmt=png&from=appmsg)

AUTOSAR COM提供了基本的通信服务，它有明确的上层模块RTE(Runtime Environment)和下层模块PDU Router。

**com层与下层PDUR层的相互通信**

AUTOSAR COM模块使用了两套PDU路由器的上位机的并集层模块api。 这是用于使用TP和的上层模块的api和不使用TP的上层模块的api。AUTOSAR COM模块传输i- pdu的通过完整的i-pdu传输或是分裂后通过TP层传输。

下层PDU Router对AUTOSAR COM模块的功能需求包括:

* 输入I-PDUs的指示 用于发送I-PDUs的发送接口，
* 包括通信控制器是否已发送I-PDU的确认
* 触发接口，使PDU router能够引起来自AUTOSAR COM模块的传输
* 用于TP通信的缓冲区处理

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCrh61K1a9BvldibRCrqJ2PGXHPOibAb82rI6S10B4ibY7NeQd0cbZynpO1NuF0icUBSho8SnpCQf4dLic51KJGGYmpYzB8GMVN9dEc/640?wx_fmt=png&from=appmsg)

**com层有上层RTE层通信**

com模块为RTE提供面向信号的数据接口：

* 将AUTOSAR信号打包传送给I-PDUs
* 将接收到的I-PDUs打包并将接收到的信号提供给RTE
* 将接收到的I-PDUs信号路由到I-PDU进行传输
* 将接收到的I-PDUs中的信号簇路由到I-PDU中进行传输
* 通信传输控制(I-PDU组的启动/停止)
* 发送请求的复制
* 保证传输I-PDUs之间的最小距离
* 接收信号监控(信号超时)
* 传入信号的过滤机制
* 不同的通知机制
* 提供初始值和更新指示
* 字节顺序的转换
* 符号扩展
* 每个I-PDU支持两种不同的传输模式
* 基于信号的网关
* 支持大型和动态长度数据类型
* 支持I-PDU计数器和I-PDU复制

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDvXW1FLqInhEMg4IG184tBclicpPwPZCKjj0q0IbaLibd5qU58fibrHJ9Az7SAMS9WliaibbmfatN95TlnGn4ya8fawEjYKnhQawdE/640?wx_fmt=png&from=appmsg)

**信号传输模式**

* 直接/N次传输模式（Direct/n-times模式）：包含于该I-PDU的任何具备Triggered属性的信号及信号组的更新都会触发I-PDU的立即发送，当上层面模块调用Com\_SendSignal( )/Com\_SendSignalGroup( )更新信号或者信号组时，Com层根据配置需求发送n次该I-PDU。
* 周期传输模式（Periodic 模式）：用户配置发送周期，只有该I-PDU的周期到来时才会触发该I-PDU的发送，上层模块调用Com\_SendSignal()/Com\_SendSignalGroup( )只更新信号及信号组的内容。
* 混合传输模式：Direct/n-times和Periodic的混合模式，当上层模块调用Com\_SendSignal( )/Com\_SendSignalGroup( )请求该I-PDU包含的信号/信号组的发送时，将会触发该I-PDU的直接n次发送，同时，用户配置的周期到来也会触发该I-PDU的发送。
* None传输模式：无论何时COM层不能够触发拥有该发送模式的I-PDU的发送，只有PduR模块调用Com\_TriggerTransmit()服务才能够触发该I-PDU的发送。

在AUTOSAR COM规范中允许为每个I-PDU静态配置两种不同的传输模式，ComTxModeTrue和ComTxModeFalse。在AUTOSAR COM规范中通过传输模式切换，来选择I-PDU中的其中一种传输模式进行传输。

先使用过滤机制判断I-PDU中各信号的发送模式条件，同时更新I-PDU中的信号。

通过各信号的判断结果来计算该I-PDU的TMS（transmission mode selector）。若至少有一个C( 与IPDUk中的信号Si相关)为True，则TMS为True，对应I-PDU以用户配置的ComTxModeTrue的发送模式发送；若所有C(Si,IPDUk)都为False，则TMS为False，对应I-PDU以用户配置的ComTxModeFalse的发送模式发送。

发送模式条件TMC+发送模式选择TMS

* 发送端信号的TMC（发送模式条件）的计算与接收端的信号过滤机制相同，但是，在发送端信号过滤并不会丢弃任何的信号，而只是用于计算信号TMC的值。
* 发送端的TMS，一个I-PDU的TMS的值是根据其所有下属的信号的TMC结果决定的，若一个I-PDU下属的信号中至少有一个信号的TMC计算为True，那么这个I-PDU的TMS为True，只有该I-PD下属的所有的信号的TMC都计算为False时，该I-PDU的TMS才为False。

每个I-PDU配置两种发送模式，在程序运行过程中，某I-PDU的发送模式是由TMS来决定，若一个I-PDU的TMS根据上述的算法计算为True，那么该I-PDU将以配置的True状态下的发送模式进行发送。当一个I-PDU下属的某个信号的过滤算法配置为A...