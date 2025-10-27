---
title: MRCP在美团语音交互中的实践和应用
url: https://mp.weixin.qq.com/s?__biz=MjM5NjQ5MTI5OA==&mid=2651773049&idx=1&sn=299b8c20a251bbd66ce1074c4cfb5dba&chksm=bd1201348a658822565beb4178fac19d665e37391349e8a5e93bb2c7ef012f8a6541cd153a31&scene=58&subscene=0#rd
source: 美团技术团队
date: 2023-03-10
fetch_date: 2025-10-04T09:04:25.181880
---

# MRCP在美团语音交互中的实践和应用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUvj8nEbNmAoQtqNGmbqrlYYVUYZfDw1nKwJb9byPHCYAic5HOFiaNCubiaskicANxvVMpwXyE76CsAlg/0?wx_fmt=jpeg)

# MRCP在美团语音交互中的实践和应用

原创

唐锐 森彬 子丰等

美团技术团队

![](https://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsVsE4Nicq51WdnKEhcaEEYDS4h6jA6JOZ3fnENgFV1B6ianDTqaQ3nzNOjvHUB79ocldrVj4YlkAW6g/640?wx_fmt=png)

**总第555****篇**

**2023年 第007篇**

![](https://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsU2zk0q52HtKQjubeUEyZHBic5ADGrKxgSd0tibyMiasOHXjb46qFBw7PTfuWAxXzWq32lDkL05icwkMg/640?wx_fmt=png "undefined")

当你和智能语音机器人对话交互时，你是否好奇电话背后的机器人如何“听懂”你的意思，又如何像人一样“回答”你的问题？其中比较重要的技术就是 MRCP。本文主要介绍了 MRCP 在美团语音交互中的实践和应用，基于美团自研的语音识别及语音合成能力，我们提升了外呼通话的成功率，并且保证了更好的用户体验。

* 一、背景

+ 1.1 MRCP 是什么
+ 1.2 MRCP 使用场景
+ 1.3 美团自研的 ASR/TTS 能力
+ 1.4 我们为什么需要 MRCP

* 二、设计与实现

+ 2.1 设计目标
+ 2.2 总体系统架构
+ 2.3 关键技术组件
+ 2.4  MRCP-Server 模块结构
+ 2.5 部署方案

* 三、实践与应用效果

+ 3.1 应用范围
+ 3.2 应用效果

* 四、结语
* 五、名词解释

## 一、背景

智能语音对话作为人工智能领域最先落地的分支之一，可以实现与人进行自然语言多轮对话，其核心技术在近年来不断地发展成熟，包括语音识别、自然语言理解、对话管理等。伴随着技术的成熟，越来越多的电话机器人开始走进我们的生活，这些电话机器人在客户服务、智能销售、通知触达等场景发挥着重要的作用。

当你和智能语音机器人对话交互时，你是否好奇电话背后的机器人如何“听懂”你的意思，又如何像人一样“回答”你的问题？经典的技术实现路径是：机器人首先通过“语音识别（ASR）”将用户输入语音识别成文字，再通过“自然语言理解（NLU）”识别意图，之后根据意图、系统信号等输入结合对话管理技术得到相应的回复，最后通过“语音合成（TTS）”生成语音播报给电话对端的用户。但要将 ASR、TTS 这些技术应用到电话系统上，还需要一些额外的工作和技术支撑，其中比较重要的技术之一也就是本文将要介绍的 **MRCP**。

备注：本文涉及较多的专业名词，我们特别在文末附上了名词解释，以帮助大家进行阅读。

### |  1.1 MRCP 是什么

MRCP（Media Resource Control Protocol, MRCP）是一种通讯协议，中文定义是：媒体资源控制协议，用于语音服务器向客户端提供各种语音服务（如语音识别和语音合成）。该协议定义了控制媒体处理资源所必需的请求（Request）、应答（Response）和事件（Event）等消息，它需要借助 RTP（Real-Time Transport Protocol, 实时传输协议）创建一个媒体会话、借助 SIP（Session Initiation Protocol, 会话初始化协议） 和 SDP（Session Description Protocol, 会话描述协议） 创建一个控制会话来实现媒体资源服务器端和客户端之间的控制[1]。

在传统的语音应用中，各集成商必须针对不同的 ASR/TTS 厂商提供的 API 接口进行专门的集成开发，不同 ASR/TTS 引擎的接口各不相同，从而导致了集成过程的复杂性和局限性。因此，在实现语音和网络技术集成方面必须需要比较规范的协议来进行处理。MRCP 协议是目前针对媒体资源和 IP 网络起草的标准协议。有了 MRCP 协议后，ASR/TTS 厂商提供 MRCP 协议的标准统一接口，语音集成开发商们不必再针对特定的 ASR/TTS 进行开发，为各种语音应用开发提供了更加灵活的选择，并有效地降低业务开发周期和成本[2]。

以语音合成（TTS）为例，图 1 展示了一个 MRCP 客户端连接媒体资源服务器的流程，在连接中会创建一个媒体会话和一个控制会话。假设连接成功，此时 MRCP 客户端对服务器端发起了一个 SPEAK 语音合成的请求，处理此请求的过程中包括了3个消息指令：`SPEAK`指令表示发送语音合成请求，`IN-POGRESS`指令表示正在处理中，`SPEAK—COMPLETE`指令表示处理完成[3]。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUvj8nEbNmAoQtqNGmbqrlYsz129v9Qr5d2VaZMAiaWaxXgVEVQcBzUNG8gpOZ2IBibOjacxp5FY0dQ/640?wx_fmt=jpeg)

图1 MRCP 协议交互

MRCP 协议的消息格式和 HTTP 消息格式类似，如下以一次语音合成的 MRCP 消息为例，展示了 MRCP 消息的主要构成。

发起语音合成请求：

```
MRCP/2.0 380 SPEAK 14321
Channel-Identifier: 43b9ae17@speechsynth
Content-Type: application/ssml+xml
Content-Length: 253

您好，有什么能帮助您？
```

IN-PROGRESS 响应消息：

```
MRCP/2.0 119 14321 200 IN-PROGRESS
#消息长度是119 bytes,ID是14321，200 表示成功，正在处理中
Channel-Identifier: 43b9ae17@speechsynth
Speech-Marker: timestamp=857206027059
```

COMPLETE 响应消息：

```
MRCP/2.0 157 SPEAK-COMPLETE 14321 COMPLETE
Channel-Identifier: 43b9ae17@speechsynth
Speech-Marker: timestamp=861500994355
#表示SPEAK请求的正常处理结束
Completion-Cause: 000 normal
```

### |  1.2 MRCP 使用场景

目前，语音行业几乎所有的重要厂商都承诺支持 MRCP。MRCP 使用场景丰富，它支持目前最热门的开源语音通信平台 [Asterisk](https://www.asterisk.org) 和 [FreeSWITCH](https://signalwire.com/freeswitch) ，并且提供了丰富的接口文档，其中呼叫中心就是一个典型的案例。一个简单的呼叫中心如下图 2 所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUvj8nEbNmAoQtqNGmbqrlYPhgMpDJM6LicY5lluXd3FR2b4OU2jicscBDRvcgpSp5enHyicaoGt29bg/640?wx_fmt=jpeg)

图2 简单呼叫中心系统示意

1. 当分机拨打外呼用户时，需要从运营商那里获得一条电话通讯线路，FreeSWITCH 指定路由通过网关到达运营商线路，通过运营商基础网络、连接用户通讯设备终端。
2. 智能语音服务通过 MRCP 协议与 FreeSWITCH 进行对接，用户接通电话后，智能语音服务从呼叫中心设备中实时获取声音讯号，将语音讯号转化为文本流实时输出，并将要回复的文本话术经过语音合成转化为语音讯号，交由呼叫中心进行语音播报。

在此场景中可以看到，采用 MRCP 协议，**调用方仅需要面向 MRCP 接口撰写程序，而无需考虑不同语音引擎产品之间的差异**，可以真正做到**一次开发、多种环境下应用**，任何支持 MRCP 标准的语音引擎都可以被无缝集成和调用。

### |  1.3 美团自研的 ASR/TTS 能力

自 2018 年起至今，美团语音交互部持续投入语音识别（ASR）和语音合成（TTS）的自主研发，目前已形成平台级的服务能力。美团语音识别重点针对美团场景进行优化，相比通用场景的识别率更高；参考 2022 年的数据，在电话呼叫场景的测试集中，美团语音识别的字准率达到 94.6%（很多业界头部厂商的字准率在 89% 左右）。在骑手语音助理、客服中心语音转译、美团 App / 外卖 App语音助理等典型业务场景中进行了落地和应用。

美团语音合成从美团各场景出发，建立起从端到云一体化，全面覆盖客服、配送、听书等各个方向的合成音色群，并支持不同数据量级的语音定制化能力，做到了通用场景好、特色场景精、定制周期短。其中现有声音的客服场景效果已领先于行业，具有小样本声音克隆、强表现力的配音能力，在性能和效果层面达到了业界一流水准；同时，美团语音合成在美团外卖配送、美团商家端、美团打车、美团客服等核心业务场景落地，支持日均亿级别的调用。

### |  1.4 我们为什么需要 MRCP

#### 1.4.1 赋能内部业务

随着美团自研的 ASR/TTS 逐步达到业界一流水平，美团内部越来越多业务接入美团自研的 TTS 和 ASR 能力。特别是 TTS，在应用的业务场景中取得超过外采系统捷通华声的效果，但在业务对接和优化过程中，也存在一些问题，可以概括为音色机械、音色不统一、合成延时过高等。

这几类问题，主要是在业务升级替换音色过程中，采取了将业务系统（如外呼系统）与语音的合成和识别能力的 HTTP/RPC 接口直接对接的方式，这种方式不仅投入大，需要逐个业务系统、逐个流程的对接，也容易因为系统复杂性、运营疏漏等问题出现音色不统一等体验问题。因此，按行业通用标准，以 MRCP 将语音合成和识别与电话系统直接对接的方式，可以有效地降低业务使用、升级语音能力的成本，平滑地提升用户体验。

**音色不统一示例**：对话流程中，一部分固定的话术文本使用的提前合成好的音频文件，另一部分动态的话术文本（如，录音中“请问你是某某店吗”）采用的实时合成的音频，两部分拼接在一起播放，音色不统一。

**延时过高示例**：部分业务对于动态话术文本，特别是本身句子较长的话术，待一整句合成完成后再播放到用户，给用户带来严重的迟滞感。

#### 1.4.2 支撑对外商业化

另一方面，越来越多美团外部企业如中通天鸿、微呼科技、马上消费金融等，认可并计划接入美团语音自研的 TTS 和 ASR 能力；预期以标准的 MRCP 协议完成对接，在客户服务、通知触达、电话提示语音识别等场景，提升其呼叫中心的基础用户体验。

## 二、设计与实现

### |  2.1 设计目标

如下图 3 所示，美团的小美机器人平台、木星通讯平台分别提供不同类型的语音对话机器人能力。以语音合成（TTS）为例，这些机器人平台直接调用 TTS 引擎的服务接口，将合成好的语音文件交由电话软交换平台（如FreeSWITCH）去播报，如链路 ① 所示。

我们的目标是将这种调用关系简化，以标准 MRCP 下的语音合成服务对接电话软交换平台，那么上述机器人平台则只用核心关注机器人的对话逻辑，将具体的语音合成逻辑解耦出来，那么链路 ② 所传递的内容即为机器人待播报的话术文本，由电话软交换平台去调用和处理语音合成。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUvj8nEbNmAoQtqNGmbqrlYloK8ZDTtJliaHpdNiaCFW0iaJPGslIqfgVL6oTE04OWcGibN5gObRibNJXw/640?wx_fmt=jpeg)

图3 语音能力与业务系统对接方式比较

总而言之，目标结合自研流式 TTS 和 ASR 能力，建设 MRCP 协议下标准的语音合成和识别服务，达到：

* 支持标准协议下的 TTS 和 ASR 能力对接方式，追齐业界主流厂商能力。
* 以横向可扩展、业务解耦的方式，支持和助力美团内部业务，在智能外呼、内呼热线等场景下提升用户体验；并为美团语音能力的对外商业化探索，提供更好的支撑。

### |  2.2 总体系统架构

#### 2.2.1 系统层次架构

在系统层次上，围绕联络场景，美团语音交互部正在建设全联络场景智能化的平台化解决方案。具体来说，美团智能对话平台 AICC（AI for Contact Center），基于美团语音交互部领先的语音识别、自然语言理解、多轮对话、知识图谱等人工智能技术，为美团业务提供智能文字客服（在线客服）、智能语音客服（热线客服）、智能外呼、智能营销、智能质检等完整解决方案；帮助业务从传统服务模式向智能服务模式转型，助力美团业务的服务成本优化、客户服务体验提升，实现客户服务及营销智能化升级。

AICC 的层次架构如下图 4 所示，从整个 AICC 架构来看，TTS 和 ASR 处于语音技术平台，提供语音合成和识别的 PaaS 级能力；相应地，MRCP-TTS、MRCP-ASR扩充已有的 HTTP/RPC 接口的能力范围。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUvj8nEbNmAoQtqNGmbqrlYoqhLUdbvapyPJcHUMFtzrVKfpkgln2YuYUtjoB9DJh2iapnBPJY6UtA/640?wx_fmt=jpeg)

图4 MRCP在AICC层次架构中的位置关系

#### 2.2.2 系统间调用关系

以热线电话机器人的系统调用过程为例，MRCP 在系统中所处的位置以及同其他各环节的配合关系如下图 5 所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUvj8nEbNmAoQtqNGmbqrlYqIE8OJPs8st0uxeQ8N4x1bsDiar0gyLkgomWOkKEOsgfphv8Uj6ia8UA/640?wx_fmt=jpeg)

图5 MRCP服务调用关系

1. FreeSWITCH 电话软交换平台，负责和运营商打通通讯线路，以具备基础的电话通讯能力。
2. FreeSWITCH 除了以内置模块（

   如 mod\_java

   ）的方式开发控制接口外，也以 ESL（

   Event Socket Library

   ）的 Inbound/Outbound 方式开放接口，提供事件监听、通话控制等能力。
3. ESL Server 将监听到的事件、消息传递给具体的业务逻辑，可以提供通讯层所有的事件供监听和处理，籍此实现机器人的语音对话交互能力。
4. 将调语音相关的事件和信号处理解耦以后来看，热线、在线机器人的交互逻辑则可以简化、抽象为统一的模型和系统。
5. 管理配置台主要负责一般对话机器人所需要的意图、槽位的定义、管理和配置任务型对话流程。
6. 配置管理也可对 ASR、TTS 引擎需要的领域知识进行管理，比如客服领域的词库、样本数据集的持续标注等。
7. 本文所述的MRCP在系统调用中处于此位置：在FreeSWITCH 收到合成/识别请求后，发起与 MRCP-Server 的交互，MRCP-Server 调用内部实现的 MRCP-TTS Plugin 与 MRCP-ASR Plugin 分别完成相应的合成或识别结果。
8. ASR Engine 和 TTS Engine 指美团语音自研的语音合成和语音识别引擎，MRCP 通过 HTTP/RPC 接口与之完成通讯。

### |  2.3 关键技术组件

要实现一个工业可用的 MRCP Server，有两个关键技术能力：一是 MRCP 协议本身的支持，二是 MRCP Server 的高可用，如多节点的负载均衡。

#### 2.3.1 MRCP 协议实现

对于 MRCP 协议的实现，不仅仅需要支持 MRCP 协议本身，也需要支持一套完整的协议栈，包括文章开头部分提到的 SIP、RTP 协议等，这是一个复杂且庞大的工作。

参考业界的一般做法，我们选择基于开源的 [UniMRCP](https://www.unimrcp.org/) 完成这些工作。UniMRCP 是一个开源的、跨平台的 MRCP 协议实现，由 C/C++ 语言编写，包括了 MRCP 客户端和服务端两个部分，它封装了 SIP、SDP、MRCPv1、MRCPv2、RTP/RTCP 协议栈，并为语音服务集成商提供了一致的 API[4]。

UniMRCP 完成了 MRCP 协议栈的封装，并没有实现 ASR 或 TTS ；基于其对底层协议栈的完整支持，我们在 UniMRCP的框架下实现相应的 Recog（ASR）和 Synth（TTS）插件（即 MRCP-TTS Plugin，MRCP-ASR Plugin），并改造适配美团日志框架、监控打点等基础技术组件，从而保障服务的稳定性和可维护性。

#### 2.3.2 MRCP Server 负载均衡

对于实现 MRCP-Server 的负载均衡，我们选用开源的 [Kamailio](https://www.kamailio.org/w/) 来完成。Kamailio 的前身叫 Openser，作为出色的 SIP proxy，在大并发量使用时常常用于负载均衡媒体服务器，对 Asterisk、FreeSWITCH、MRCP 等实现集群能力[5]。Kamailio 经常与 FreeSWITCH 配合使用，最常用的场景是 Kamailio 作呼叫负载均衡服务器（一般主备配置），FreeSWITCH做媒体相关的处理如转码、放音、录音、呼叫排队等。

### |  2.4  MRCP-Server 模块结构

由于 UniMRCP 提供的基础框架已经实现了服务接口、连接管理、协议管理，如何加载自定义插件，以及系统层的日志框架；并且 TTS 引擎与 ASR 引擎作为基础的依赖，已以 HTTP/RPC 协议的方式提供稳定的基础语音服务。因此，开发工作是在 UniMRCP 的基础上进行 TTS/ASR 插件的开发，模块结构如下图 6 所示，主要新增的模块已在图中标灰，其中：

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUvj8nEbNmAoQtqNGmbqrlY42KICMKougQwhPVBwIoPjRaA73ibKk59k...