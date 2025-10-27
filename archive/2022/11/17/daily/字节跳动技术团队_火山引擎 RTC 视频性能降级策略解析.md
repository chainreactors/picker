---
title: 火山引擎 RTC 视频性能降级策略解析
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499952&idx=1&sn=66c7465372f8f9bdd220261275b28389&chksm=e9d30b52dea482443f4482fb8aca13316ba28cd677b062c35998172883e0d0d86082d6a07a23&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2022-11-17
fetch_date: 2025-10-03T23:02:26.854988
---

# 火山引擎 RTC 视频性能降级策略解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLK6OtUVnuPToxBgClOMZlW3IrnibItc9cKPnv1KNSzayic9NaRK8Mubxg/0?wx_fmt=jpeg)

# 火山引擎 RTC 视频性能降级策略解析

原创

杨建群

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

# 1.  背景

随着 RTC 使用场景的不断复杂化，新特性不断增多，同时用户对清晰度提升的诉求也越来越强烈，这些都对客户端机器性能提出了越来越高的要求 (越来越高的分辨率，越来越复杂的编码器等)。但机器性能差异千差万别，同时用户的操作也不可预知，**高级特性的使用和机器性能的矛盾客观存在**。当用户机器负载过高时，我们需要适当降级视频特性来减轻系统复杂性，确保重要功能正常使用，提升用户体验。

视频性能降级能做什么？

一是解决因设备性能不足、突发的性能消耗冲击（如杀毒软件）带来的用户音视频体验问题（如视频卡顿、延时高、设备卡死）等问题；

二是提升一些高级功能的渗透率，例如默认情况下开启视频超分，设备性能不足的情况下主动关闭；

三是降低部分场景的设备功耗，例如当电脑使用电池供电的时候，通过关闭视频超分、降低视频帧率等方式主动降低一些功耗。

# 2.  前置基础

RTC 提供了一种性能降级机制，在性能负载过高时，触发降级；在性能负载降低后，触发升级。一套完整的性能降级方案，需要产品具备一些基本的降级能力，比如：支持动态修改视频分辨率、帧率，支持发布多路视频流(simulcast)，支持 SVC，支持按需发布/订阅等。

## 2.1 Simulcast

> 关键词：同样的视频源，多种分辨率，差异化的分辨率需求

所谓 Simulcast，就是将**一个视频源**输入编码输出成多个分辨率的视频帧，在**发送端编码多路不同分辨率**的大小流，下行接收端可以选择**订阅其中任意一种分辨率**的同源视频流。它可以满足**多人通话场景**，不同用户对于**分辨率的差异化需求**。在实际应用中，Simulcast 变得更加灵活多变，发挥的作用也越来越大。除了满足用户差异化的分辨率需求外，还可以**有效解决下行弱网/性能问题**，提升用户体验。比如在下行用户网络交较差或者性能较差时，可以给用户转发低分辨率的视频，确保用户可以拥有流畅的观看体验。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLOic6XdTia2LN6X7YKNBjXzmLicGvf4EmKEibhE9uuDn0haukzqprq8TdmA/640?wx_fmt=png)

## 2.2 SVC

> 关键词：单路流，分层编码

SVC（Scalable Video Coding, 可适应视频编码）是指，**一****条视频码流**可以分成**多个层级(layer)** **，** 在保证整条流的可解码性的情况下，用户可以根据层级的优先级选择丢弃某些层级的全部或部分片段，得到不同帧率（temporal / 时域）/分辨率（spatial / 空域）/ 画质（quality / 质量）的视频流。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLp3VNNcXtUSM6qGEgtflibDwicufv5CACoHbgia77fftTEc0rd9xicFQM8g/640?wx_fmt=png)

## 2.3 按需发布

按需发布简单来说，就是让发布端知道哪些分辨率的流有人订阅，哪些分辨率的流没人订阅，然后**仅发布那些有人订阅的视频流**。用户没有订阅的流，即使性能或者带宽再好，也不会发送。通常情况下，按需发布端需要配合 Simulcast 使用，但也不是必要条件。按需发布的初衷，是为了节省性能和带宽资源，减少不必要的资源浪费。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLS0b71FsVL2zLbQtZjbcG4Rz60rIh72zDrib4oysqhy2Cv6TYheLicGiag/640?wx_fmt=png)

按需发布

# 3.  常见的视频性能降级手段

RTC 对于 CPU 和 GPU 的消耗通常较高，并且 RTC 对于实时性有近乎苛刻的要求 (通常 RTC 通话要求在 400ms 以内，云游戏场景甚至要求 100ms 以内)，这**对算法处理速度以及平稳性有很高的要求**。单帧处理耗时的长短，意味着视频帧率的上限，而处理耗时的平稳性，也会影响视频流畅性的整体感受（因为实时性的要求，RTC 通常不会设置过大的 jitter buffer 来平滑抖动，当帧处理耗时抖动较大时，会在观看端感受到类似视频掉帧一样的卡顿现象）。除此之外，过高的系统消耗，甚至会影响到用户对设备的正常使用（比如：过度发烫/操作延时卡顿等）。

在视频通话过程中，有一些参数是可动态调节的。往往不同的视频参数对应着不同的性能消耗。常见的调节参数有视频分辨率、视频帧率，除此之外，还可以调节视频处理特性(比如：超分 / 降噪 / HDR 等)，甚至还可以切换不同编码器及档位，对于 Simulcast 还可以选择切流 (Fallback)。

## 3.1 视频分辨率降级

降级视频分辨率是指**降低视频的发送分辨率**。通常来说，RTC 主要是指编码分辨率。对于一些特殊场景，降低视频分辨率还包括了支持编码分辨率的回调，采集模块收到回调的分辨率后，会主动降低采集模块输出分辨率（但通常不会直接降低 camera 采集分辨率，因为调整采集参数会涉及到摄像头重启，切换过程会出现黑帧，重启摄像头也会增加出错概率）。这种场景特效分辨率也会随之降低，收益最大化。

## 3.2 视频帧率降级

降级视频帧率是指**降低视频的发送帧率**。通常来说，RTC 主要是指编码帧率。降级帧率是最不容易出错，并且收益可观的一种降级手段。对于一些特殊场景，还支持编码帧率回调，采集模块收到回调之后，会主动降低采集模块输出帧率。

## 3.3 编码器降级

降级编码器指，**降级编码器档位，或者****切换****到****性能更好的编码器**。通常，编码压缩率越高的编码器，编码性能消耗越高。因此，当系统负载较高时，可以切换到压缩率相对低的编码器或者编码档位，降低性能消耗。

## 3.4 视频处理特性降级

在各业务场景下，会有一些视频前后处理特性，主要目的是为了提升画质，比如：超分 / 降噪 / HDR 等。在性能足够好，并且负载不高的情况下，可以开启这些视频处理特性，提升用户体验。当系统性能瓶颈时，需要适当降级视频处理特性，甚至是关闭特性来确保正常的视频通话。

**RTC** **视频性能降级方式及优缺点总结：**

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLfPRbmAe7Oa5BN9WlicvXhY8V4zOSUrnwducu1tsLu368xCwDXdcYBAA/640?wx_fmt=png)

RTC 视频性能降级方式及优缺点总结

# 4. 火山引擎 RTC 性能降级策略

## 4.1 性能降级策略概览

火山引擎 RTC 降级策略包括了多种基础能力和策略：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLzEh0NZFMn30aiasH4eoeZbSzSAvLU0dY2GzyC91tXARqVDq5dYsZReg/640?wx_fmt=png)

火山引擎 RTC 视频性能动态降级策略概览

下面具体介绍几种降级策略以及策略中的注意点。

## 4.2 RTC 编码组织方式

火山引擎 RTC Simulcast Encoder 之间采用完全并行的编码方案，每条 Simulcast 流处在不同的 Pipeline 上，线程之间相互不影响。相比 WebRTC Simulcast Encoder 之间串行的编码方案，并行编码方案**效率更高，** 并且编码效率基本不受 Simulcast 流数的影响。

对于性能降级来说，并行编码组织方式，可以选择对单条流进行降级，也可以选择同时对所有流进行降级，降级方式变得更加灵活。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLgzDTNNmeDI0jLDKXY2ANfaabic8YBPfbT9TOuNo704ykeJnR5iaSubOg/640?wx_fmt=png)

## 4.3 RTC Simulcast 流降级方案

因为火山引擎 RTC 编码器采用并行方案，单路 Simulcast 流的编码延时高，降级可以选择同时降级所有流的帧率，也可以选择只降级编码延时较高流的帧率，而不影响其他 Simulcast 流。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLfwHNYK8SmehXhPico344Oce7ibLQkk07Ptvt7naOwSffXrogZcl5FnVQ/640?wx_fmt=png)

火山引擎 RTC 除了降级单条流之外，还支持 Simulcast 流之间联动。性能不足时，支持关闭高分辨率的流（Fallback），性能恢复时，可以重新开启高分辨率的流。当发生 Fallback 时，订阅高分辨率的用户会自动切换为订阅次高分辨率的流，性能恢复时，会重新切换回来。以下图为例，如果 720p 流被关闭，订阅 720p 的用户将会收到最接近 720p 的分辨率的流，所示为 360p。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLDo4xnJEwdTIaANMicvJ1rA9Cw1XEoRpJiahe1AiaTPY7DXSAc4NnJPq0A/640?wx_fmt=png)

火山引擎 RTC 降级偏向于 **画面的流畅度和画质的均衡**（升降级路线可后台配置）。

## 4.4 不同发布流之间的协同降级

在没有流之间(比如：屏幕流/视频流)协同的情况下，会存在不同流之间 **同升同降** 的问题。为了更好的解决这类问题，也为了更好的处理不同流之间的优先级问题，火山引擎 RTC 内部采用一个 **性能集中调控中心**，来处理不同流之间的优先级问题。以会议场景举例来说，我们通常会认为，屏幕共享的优先级比视频流更高，在性能负载较高时，我们选择优先把视频的消耗降低，把资源尽可能让给屏幕流。只有在视频流降级之后，系统负载依旧较高，无法满足性能要求时，才会降级屏幕流。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLcRF7oNHvTlGibLU7QNeUFRic3X9VSicXuSxscvTtiaQYnW4aZYXTFBNsaQ/640?wx_fmt=png)

典型的降级路径

典型的降级路径是：先对视频流降级，再降级屏幕流；升级顺序和降级顺序正好相反。

## 4.5 性能和带宽降级关系处理

性能和带宽是 RTC 系统中最重要的两种资源。随着系统运行，两者会处在不断的变化中。同时有性能以及带宽波动的情况下，可能会出现，性能负载过高，触发降级，但同时带宽回升，又会触发升级。因此，需要有一种机制保证两者之间出现“你升我降”的问题。火山引擎 RTC 把性能和带宽控制两者解耦开来，把性能的输出作为一个最大限制条件。性能升级相当于是上调水位线，降级相当于下调水位线，实际性能/带宽升降级由一个模块统一处理。

除了性能和带宽之外，火山引擎 RTC 还支持**按需发布**能力，发布端结合三者采用如下方案进行综合决策。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLEncxtAHLZM17dHsicrX9gxEouph6JGVMGWFBlehNt8M7MY8LssuXeJw/640?wx_fmt=png)

说明：因为性能原因，720p 流被关闭，订阅 720p 的用户将会收到最接近 720p 的分辨率的流，所示为 360p。

## 4.6 订阅端的性能降级

订阅端性能在某些场景下可能会成为性能瓶颈，比如多人会议，或者高分辨率解码。这种情况下，如果不能有效处理，可能会导致卡顿/延时逐渐拉大等问题；

火山引擎 RTC 引入订阅端性能降级方案，联动上下行，当系统负载较高或者解码器延时较长时，订阅端支持动态性能降级。

1）订阅端可以根据流的优先级，优先选择降级低优先级的流，尽可能保证**高优先级流**的视频体验。

> 火山引擎 RTC 支持 API 方式设置订阅流的优先级。

2）就单条流来说，订阅端也可以灵活的配置，是优先先降级分辨率还是帧率（后台配置）。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbLt2iaQBKDBFnytib1aNtnxYcG29ZSyUicmOWHX0t9PpjgZGribwwftaafOg/640?wx_fmt=png)

上图展示了 Client 用户同时订阅 3 条 720p 30fps 的流，但是流的优先级不同，Stream1 为高优先级流，Stream2 / Stream3 为低优先级流。当客户出现性能问题时，会首先降级低优先级的 Stream2 / Stream3。以上图为例，Stream2 / Stream3 降级到了 180p 8fps。优先级最高的 Stream1 没有降级。直到低优先级的流降无可降，才考虑降级高优先级的流。

## 4.7 基于 CPU 使用率的降级

使用特性处理耗时（比如：编码延时或者视频处理算法耗时）的最主要的问题在于：

1. 仅能监控当前特性自身的负载，如果链路其他消耗较高(并且不在监控范围内)，导致整体负载过高时，依旧无法降级。

2. 系统 CPU 使用率较高时，无法退避，导致设备过烫，甚至用户操作受到严重影响。

火山引擎 RTC 支持性能降级统一调控方案，可以进行上下行联动，也可以对视频/屏幕的性能降级联动等，甚至可以联动音频及网络。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbL6tSG692dduEWBXFncEMViblonzZGYK3iaILibwqRXFrfla2icDibz8ME9ZA/640?wx_fmt=png)

火山引擎 RTC 以流维度拆分成几个 **降级单元**，单元的排列情况，可以表示优先级（优先级可配置）。

```
enum RXPerfUnitType {
    kRXPerfUnitUnknown = 0,
    // 发布视频流
    kRXPerfVideoPubCamera = 1,
    // 发布屏幕流
    kRXPerfVideoPubScreen = 2,
    // 发布投屏
    kRXPerfVideoPubScreenCast = 3,
    // 订阅视频
    kRXPerfVideoSubCamera = 4,
    // 订阅屏幕
    kRXPerfVideoSubScreen = 5,
};
```

**NOTE****:** 一个降级单元表示一种流类型，一条流内部可能有多种降级手段，比如编码和视频处理算法等。

# 5.  总结和展望

## 5.1  总结

我们在会议场景对上述视频性能降级策略进行了验证。上线这些策略后，线上高负载时间比例持续优化，从整体 9‰ 左右优化到 5‰，用户感受高负载情况（设备发烫、界面响应慢、音视频卡顿、甚至程序崩溃或死机等问题）变少。

当前的视频性能降级策略也存在一些可以优化的地方，比如：

**基于 CPU 的性能降级存在误伤**。类似编译场景，在 CPU total usage 占用较高，但 App usage 占用很低的情况下，降级收益很小，但实际中这种场景可能会存在；针对这种场景，应该做区分，不是一味降级，退避是保障在一定的视频质量基础。

**降级最低视频质量配置可以更灵活**。降级至最低档位时，应该还要关联实际的发布订阅情况来执行。比如，用户在订阅 1080p 的流，这时候降级到 180p 可能不是一个很合适的选择；但如果用户本身订阅就是 360p 的流，这时候降级到 180p 可能是一个不错的选择。后续将进一步探索和优化，保证性能满足要求的情况，质量损失最小。

**支持基于** **GPU** **的性能降级**。RTC 场景不光对于 CPU 的消耗大，对于 GPU 的消耗同样也不小。后续基于 GPU 的性能降级也将上线。

## 5.2  展望

未来，火山引擎 RTC 还将支持更多降级策略，比如超分 / 降噪特性的性能降级、编码器降级等；降级方案完整性进一步提升，比如根据用户设备来推荐最佳视频参数；另外，利用火山引擎“数据驱动”优势，量化性能数据，探索性能和带宽深度融合方案。通过这些优化，更好地平衡高级特性的使用和机器性能的矛盾客观存在，为用户带来更好的体验。

# 6.  加入我们

火山引擎 RTC，致力于提供全球互联网范围内高质量、低延时的实时音视频通信能力，帮助开发者快速构建语音通话、视频通话、互动直播、转推直播等丰富场景功能，目前已覆盖互娱、教育、会议、游戏、汽车、金融、IoT 等丰富实时音视频互动场景，服务数亿用户。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiakT6q8VnQ4v4IrMCvNgBbL8RTmVQpg8jjeicqicCSbiaXLnqrjzTERgg0ZJUJ8H6cVVDIH266wFDVvA/640?wx_fmt=png)

🏃 扫描上方二维码，或点击**阅读原文**，赶紧加入我们吧！

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC6RyG...