---
title: 深入解析AUTOSAR CP入侵检测系统管理（IdsM）规范
url: https://mp.weixin.qq.com/s/Mm3I-I5o1jXemCtbLQUX-g
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:50.929438
---

# 深入解析AUTOSAR CP入侵检测系统管理（IdsM）规范

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBaeiay4vbk8BtDwBcxQzbPQDXaVgJl84AwLickrZ04lSeHVg95nrBws2yGBz6TAB5dSItZibahFbxHrAQ9GNzibTwrMvSIoOian1PI/0?wx_fmt=jpeg)

# 深入解析AUTOSAR CP入侵检测系统管理（IdsM）规范

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

在当今日益复杂的汽车网络环境中，车辆的安全性能成为了制造商和消费者共同关注的焦点。为了应对潜在的网络攻击和未经授权的访问，AUTOSAR联盟开发了一系列安全相关的规范，其中之一便是入侵检测系统管理器（IdsM）。

**01**

**概念介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD1yPpmyb66x601Npc701nibYq7Q5bm5Dq5oicDmdEU1d9yYQDbJPHhKsQsTyV6KO80cbhWyULNVv6iaDMjFC8dS2tKiaXRZp7KAw8/640?wx_fmt=png&from=appmsg)

**安全传感器（Security Sensor）**

在AUTOSAR架构中，安全传感器（Security Sensor）扮演着至关重要的角色，其基本定义为能够产生安全事件的任何组件。根据AUTOSAR的当前版本，检测安全事件的职责主要落在安全传感器上，而非IdsM或IdsR组件，后者的主要职能是传输安全事件。在AUTOSAR标准中，基础软件模块（BSW）、复杂设备驱动程序（CDD）和业务组件（SWC）均具备充当安全传感器的能力，它们将安全事件（SEv）上报给IdsM进行进一步处理。

AUTOSAR对BSW模块能够报告的安全事件类型进行了标准化，每个BSW模块的规范文档中都会列出它所生成的安全事件类型。这些事件由相应的模块进行报告。此外，业务组件还有能力报告那些在AUTOSAR中未被标准化的自定义安全事件类型。为了详细指定特定ECU所报告的安全事件类型的属性，可以使用安全性摘要（SecXT）这一工具。通过这种方式，AUTOSAR确保了安全事件的有效识别和处理，从而增强了整个车辆系统的安全性。

**入侵检测系统管理器（IdsM）**

入侵检测系统管理器在车辆网络安全中扮演着关键角色，其主要职责可以归纳为以下几点：

1. **安全事件的传输：**IdsM的首要任务是接收本ECU内各个传感器产生的安全事件（以下简称为SEv），并将这些事件传递给车内的集中式IdsR组件。IdsR组件进一步将这些安全事件上传至云端，以便进行集中管理和分析。
2. **事件检测与过滤：**IdsM配备了一套可配置的过滤器，用于对收到的安全事件进行检测和筛选。这些过滤器组成了一个“过滤器链”，只有通过过滤器链的SEv才会被认定为合格的安全事件（QSEv），从而确保了事件处理的准确性和有效性。
3. **本地事件存储：**根据配置需求，IdsM还可以将QSEv传输至安全事件存储器（Sem），实现在本地ECU上的存储。这样，即使在无法实时传输至云端的情况下，关键的安全事件也能被保存下来，供后续的离线分析使用。

通过这些功能，IdsM不仅加强了车辆对潜在威胁的检测能力，还为安全事件的后续处理和分析提供了坚实的基础。

**安全事件存储器（Sem）**

安全事件存储器（Sem）是一种专用于汽车电子控制单元（ECU）的存储解决方案，旨在保存与安全相关的事件数据。作为诊断事件管理器（Dem）模块的一部分，Sem提供了一块用户可配置的内存区域，专门用于存储由入侵检测系统管理器（IdsM）生成的安全事件（SEv）。Sem的核心功能是在ECU内部持久化安全事件信息，以便进行深入分析和后续处理，从而支持对潜在网络威胁的有效响应和防范。

**入侵检测系统报告器（IdsR）**

入侵检测系统报告器（IdsR）是一个关键组件，负责从车辆内多个电子控制单元（ECU）中的IdsM实例收集安全事件。IdsR的主要作用是对收集到的安全事件数据进行增强，例如通过添加地理位置信息等上下文数据，从而提供更全面的事件视图。根据原始设备制造商（OEM）的具体需求，IdsR能够将这些富集后的数据传输到车辆安全运营中心（VSOC），在那里安全事件可以利用安全信息和事件管理（SIEM）解决方案进行深入分析。需要注意的是，AUTOSAR并未直接提供IdsR的具体规范，而是留给OEM和系统集成商根据实际需求进行定制和实现。

**车辆安全运营中心（VSOC）**

车辆安全运营中心（VSOC）是一个专门设计用于监控、分析和响应车辆网络安全事件的集中式平台。随着汽车行业日益依赖于复杂的电子和网络系统，VSOC成为了确保车辆及其乘客安全的关键基础设施。VSOC主要负责事件收集与聚合、实时监控与分析、威胁情报、响应与恢复、合规性与报告等。

**02**

**功能概述**

IdsM模块作为AUTOSAR入侵检测系统（IDS）的核心部分，负责接收来自车载安全传感器的安全事件（SEv）。这些事件可能是由软件组件（SW-C）或复杂设备驱动程序（CDD）生成的。IdsM通过一系列可配置的过滤器对这些事件进行处理，最终生成合格的车载安全事件（QSEv）。这些QSEv可以被存储在本地事件存储器（如Dem/Sem模块）中，或者被发送到其他ECU或安全运营中心（SOC）进行进一步分析。

Autosar中，对于IDS系统主要有如下用例：

* UC1: Collect data about security events (SEv)
* UC2: Filter qualified onboard security events (QSEv) from security event data
* UC3: Locally store QSEv records
* UC4: Forward QSEv to ECU with SOC connection
* UC5: Provide access to locally stored QSEv records
* UC6: Re-configure qualification parameters during operation
* UC7: Update IdsM configuration
* UC8: Protect IdsM configuration
* UC9: Protect IdsM data in transit and in rest

**03**

**模块处理**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBuuRdVpuAy6Lk8X39FYJUOHqkUkqEKpibDOiaN2h1F1pLfYYCxEArNdic8gHzxnX6ZoMKWjBicghxsWf26IJEtvyIEIjaJ3lA1Ko0/640?wx_fmt=png&from=appmsg)

IdsM模块的设计允许它处理各种类型的安全事件，并通过过滤器链对事件进行分类和处理。这些过滤器包括状态过滤器、采样过滤器、聚合过滤器和阈值过滤器等。每个过滤器都有特定的功能，例如，状态过滤器可以基于车辆的当前状态决定是否丢弃事件，而聚合过滤器则可以将多个事件合并 为一个事件，以减少网络负载。

**04**

**依赖关系**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBHwPiaY95yWLZDdNxLXKkvnPedlC00KFIRviauxICJBTsS4ic7S9tjT4JX4djtcCPJUgWC0hZRpBic8oqhVPRiadiaJDsLkGjS6P6M4/640?wx_fmt=png&from=appmsg)

如上图所示IdsM模块与多个AUTOSAR模块有交互，包括诊断通信管理器（Dcm）、非易失性内存（NvM）模块、PDU路由器（PduR）等。这些交互确保了IdsM能够在整个系统中有效地收集和处理安全事件。

**05**

**配置规范**

文档提供了IdsM模块的详细配置规范，包括事件缓冲区、上下文数据缓冲区、事件定义、过滤器链、时间戳和签名等。这些配置参数允许系统开发者根据具体需求定制IdsM的行为，以适应不同的应用场景和安全要求。

**06**

**通信协议**

Autosar 定义得事件传输格式如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDWLvn9KO9FiaLozYqzZ3PbrGzaufVMkGsuuNxrZ32LUpudYMmHm38z8xMNYuiaWfD3ze6KV7POXfC5wAXqPhyaJ13efsPkR0rI0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgl7KVj1gj5LTjUWyM9hCrTq11SIT6sgYSkTcz1GgWzezBMV23l0HqHcUDNaMmfrbmibA26mZSKoRxdO8m1aE6wxTduq5s3HLY/640?wx_fmt=png&from=appmsg)

**07**

**Autosar标准事件定义**

**Standardized\_SecurityEvents\_KeyM**

* id-1: KEYM\_SEV\_INST\_ROOT\_CERT\_OP
* id-2: KEYM\_SEV\_UPD\_ROOT\_CERT\_OP
* id-3: KEYM\_SEV\_INST\_INTERMEDIATE\_CERT\_OP
* id-4: KEYM\_SEV\_UPD\_INTERMEDIATE\_CERT\_OP
* id-5: KEYM\_SEV\_CERT\_VERIF\_FAILED

**Standardized\_SecurityEvents\_SoAd**

* id-50: SOAD\_SEV\_DROP\_PDU\_RX\_TCP
* id-6: SOAD\_SEV\_DROP\_PDU\_RX\_UDP
* id-7: SOAD\_SEV\_DROP\_MSG\_RX\_UDP\_LENGTH
* id-8: SOAD\_SEV\_DROP\_MSG\_RX\_UDP\_SOCKET
* id-9: SOAD\_SEV\_REJECTED\_TCP\_CONNECTION

**Standardized\_SecurityEvents\_TcpIp**

* id-10: TCPIP\_SEV\_ARP\_IP\_ADDR\_CONFLICT
* id-11: TCPIP\_SEV\_DROP\_INV\_PORT\_TCP
* id-12: TCPIP\_SEV\_DROP\_INV\_PORT\_UDP
* id-13: TCPIP\_SEV\_DROP\_INV\_IPV4\_ADDR
* id-14: TCPIP\_SEV\_DROP\_INV\_IPV6\_ADDR

**Standardized\_SecurityEvents\_EthIf**

* id-15: ETHIF\_SEV\_DROP\_UNKNOWN\_ETHERTYPE
* id-16: ETHIF\_SEV\_DROP\_VLAN\_DOUBLE\_TAG
* id-17: ETHIF\_SEV\_DROP\_INV\_VLAN
* id-18: ETHIF\_SEV\_DROP\_ETH\_MAC\_COLLISION

**Standardized\_SecurityEvents\_CanIf**

* id-19: CANIF\_SEV\_TX\_ERROR\_DETECTED
* id-20: CANIF\_SEV\_RX\_ERROR\_DETECTED
* id-21: CANIF\_SEV\_ERRORSTATE\_PASSIVE
* id-22: CANIF\_SEV\_ERRORSTATE\_BUSOFF

**Standardized\_SecurityEvents\_Dcm**

* id-23: DIAG\_SEV\_WRITE\_INVALID\_DATA
* id-24: DIAG\_SEV\_SECURITY\_ACCESS\_DENIED
* id-25: DIAG\_SEV\_COMMUNICATION\_CONTROL\_SWITCHED\_OFF
* id-26: DIAG\_SEV\_SERVICE\_NOT\_SUPPORTED
* id-27: DIAG\_SEV\_SUBFUNCTION\_NOT\_SUPPORTED
* id-28: DIAG\_SEV\_INCORRECT\_MESSAGE\_LENGTH\_OR\_FORMAT
* id-29: DIAG\_SEV\_REQUEST\_SEQUENCE\_ERROR
* id-30: DIAG\_SEV\_REQUEST\_OUT\_OF\_RANGE
* id-31: DIAG\_SEV\_REQUESTED\_ACTIONS\_REQUIRES\_AUTHENTICATION
* id-32: DIAG\_SEV\_SECURITY\_ACCESS\_NUMBER\_OF\_ATTEMPTS\_EXCEEDED
* id-33: DIAG\_SEV\_SECURITY\_ACCESS\_INVALID\_KEY
* id-34: DIAG\_SEV\_SECURITY\_ACCESS\_REQUIRED\_TIME\_DELAY\_NOT\_EXPIRED
* id-35: DIAG\_SEV\_NUMBER\_OF\_FAILED\_AUTHENTICATION\_ATTEMPTS\_EXCEEDED
* id-36: DIAG\_SEV\_CERTIFICATE\_FAILURE
* id-37: DIAG\_SEV\_ECU\_UNLOCK\_SUCCESSFUL
* id-38: DIAG\_SEV\_AUTHENTICATION\_SUCCESSFUL
* id-39: DIAG\_SEV\_CLEAR\_DTC\_SUCCESSFUL
* id-40: DIAG\_SEV\_ECU\_RESET
* id-41: DIAG\_SEV\_WRITE\_DATA
* id-42: DIAG\_SEV\_REQUEST\_DOWNLOAD
* id-43: DIAG\_SEV\_DTC\_SETTING\_SWITCHED\_OFF

**Standardized\_SecurityEvents\_SecOc**

* id-44: SECOC\_SEV\_MAC\_VERIFICATION\_FAILED
* id-45: SECOC\_SEV\_FRESHNESS\_NOT\_AVAILABLE

**Standardized\_SecurityEvents\_IDSM**

* id-46: IDSM\_INTERNAL\_EVENT\_NO\_EVENT\_BUFFER\_AVAILABLE
* id-47: IDSM\_INTERNAL\_EVENT\_NO\_CONTEXT\_DATA\_BUFFER\_AVAILABLE
* id-48: IDSM\_INTERNAL\_EVENT\_TRAFFIC\_LIMITATION\_EXCEEDED
* id-49: IDSM\_INTERNAL\_EVENT\_COMMUNICATION\_ERROR

**08**

**总结**

AUTOSAR IdsM规范文档为车辆网络安全提供了一个坚实的基础。通过标准化的安全事件处理流程和强大的配置能力，IdsM模块能够有效地提高车辆对网络攻击的防御能力。随着汽车行业对网络安全的重视日益增加，IdsM将成为未来车辆安全架构中不可或缺的一部分。

来源：CSDN博主「Code\_Shawn」

https://blog.csdn.net/qq\_27718973/article/details/137183414

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=224...