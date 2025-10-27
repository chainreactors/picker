---
title: 字节跳动基于 Ray 的大规模多模态数据处理框架
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247511900&idx=1&sn=00aa033a2e651b06d0a02ce4940d0e11&chksm=e9d364bedea4eda8e5124c4fcca56f35d188dea68d9f5fe578f40fe47d43f8e1d07113b1a53a&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-11-23
fetch_date: 2025-10-06T19:19:17.624113
---

# 字节跳动基于 Ray 的大规模多模态数据处理框架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4WaibEQ8C3klPibo0tUkFb7A0YGS07EuQLSR6XVWNreZiaFianJlTlWHdrg/0?wx_fmt=jpeg)

# 字节跳动基于 Ray 的大规模多模态数据处理框架

原创

王万兴

字节跳动技术团队

Ray Summit是Ray社区一年一度的全球盛会，2024年于9月30日至10月2日在美国旧金山举行，主题是"Where Builders Create the AI Future"，聚焦于构建人工智能的未来，吸引了全球众多AI开发者和行业领袖。今年的Ray Summit不仅是一个技术交流的平台，更是一个展示最新AI技术和趋势的舞台。包括OpenAI、Meta、LangChain、Google、Nvidia、ByteDance在内的多家顶尖科技公司和组织参与了此次盛会，共同探讨和分享了他们在AI领域的最新进展和洞见。

来自ByteDance的Xiaohong Dong、Zhibei Ma、Liguang Xie分享了题为《How Bytedance Builds Large-Scale Data Processing Pipelines for Multimodal Models with Ray》的演讲。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4jvJoD2nARvo6iaia0LB36QDcbnER6LcFSjv0fsiagGNou2ibeK4PRAHAvA/640?wx_fmt=jpeg&from=appmsg)

YouTube视频链接：https://www.youtube.com/watch?v=f67SKoxR9H0&t=152s

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4Iibn1am97YrianzxKwvWabo4BFqvN0dnY0E3MibpXibcRId8PpiaMSjUJVA/640?wx_fmt=png&from=appmsg)

我们来自字节跳动Seed（语音、视觉）和Data Infra团队，致力于构建高性能、可扩展的分布式数据处理平台，通过数据驱动的方法来提高多模态大模型能力。

当前数据处理面临三大挑战：1) 数据呈指数级增长，数据量达到PB量级；2) GPU和CPU资源有限；3) 数据处理任务越来越复杂，有多个步骤和复杂的算法。

我们的目标是在有限的资源下，提高数据处理效率。Ray就是答案，它可以处理大量数据，优化异构资源分配，并具有灵活的编排能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4KP3ibzAXicrTiagpcR8icuZKuO1Lpd4yBZqXEocY0efQeibicUsGA9icwLWLQ/640?wx_fmt=png&from=appmsg)

接下来将介绍在字节跳动，如何**使用****Ray****/RayData构建Audio/Video数据处理Pipeline，以及在大规模不稳定资源上运行RayData所做的优化工作**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4iaauibfJaTyPL896LcyDV9VgG0yzVRe9jULTpyIZNCj9rmG8NxkssHMA/640?wx_fmt=png&from=appmsg)

首先，让我们深入探究 Audio 数据处理平台的细节，了解 Ray 是怎样解决上述提到的在数据处理中颇具挑战性的三个问题的。如图所示，数据处理平台架构可分为三层：第一层为基础设施层，它管理基础的存储资源与计算资源，以及任务调度，确保可用资源的高效利用以及各类任务的顺畅执行。第二层是自主研发的数据处理Pipeline，专门用于处理各种Audio的数据，执行一系列的数据转换与处理。顶层是应用层，处理后的数据被用于各种业务场景，比如音乐生成等。接下来重点介绍数据处理Pipeline。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4OKyB4zvCyHbOT7a7PcsibOBMDCBAE1O30IiaShYdgxFSD3rGxMQwcRaw/640?wx_fmt=png&from=appmsg)

数据处理Pipeline中的第一个概念是node，它通常代表一个特定的任务或算子，例如过滤算子、打标算子、去重算子。node可能需要 CPU资源也可能需要 GPU 资源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4T2UpghibHWRUaEW6xiaibX5Wg7zhqjF0TnZ7IuRmicrYJ0UKUjicUgs3eGQ/640?wx_fmt=png&from=appmsg)

第二个概念是flow，flow被定义为节点之间的数据或控制传输关系，是一种有向连接。一个node可能有多个输入flow或输出flow。最终数据处理Pipeline的DAG由node和flow定义，并通过 YAML 组装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ49Wsedt4uZXg4hz5ia8NkkQVCwZrD4Yovia9XcnlmiamNibOIu5vXCl7FQg/640?wx_fmt=png&from=appmsg)

基于上述设计，框架定义了很多常见的数据处理Pipeline，通过重新组合这些常见的Pipeline，可以满足用户模型训练的数据处理要求。这种方法极大地提高了整体数据处理的工作效率，并为数据处理和模型训练提供了更灵活的解决方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4NibYNFql7cjtT3xqX0iaNicWfoSbG9wZqrm0TKbCWQfpCHKPhHOOoFyqw/640?wx_fmt=png&from=appmsg)

在构建数据处理Pipeline的初始阶段，遇到了一些问题：1）可扩展性不够，很难从单个节点拓展至多个节点，不能充分利用资源；2）任务调度与负载均衡问题，需要手动管理任务分配，复杂度很高且任务分配不合理；3）高可用性和容错性，缺乏任务重试和节点故障检测的自动化机制，在节点中断时，可能会有任务失败和数据丢失的情况；4）数据传输与共享，需要手动完成任务和节点之间高效的数据传输和同步。

在调研了Ray的基础能力之后，开始尝试使用RayCore构建Pipeline。因为Ray对Python生态非常友好，使得用户能够更高效地进行开发以及和现存方案进行集成，原有方案得以快速迁移到了Ray上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4UxMkoVyml9RQIONgjxuibtLibgo4aNpcibpHovSyfye2pRP08xQQsnekQ/640?wx_fmt=png&from=appmsg)

RayCore 提供了强大的分布式计算能力，比如Actor、Task，使用RayCore可以方便的开发分布式应用程序，构建数据处理pipeline。但是RayCore提供的是low level的API，直接使用它进行开发需要自行处理很多问题，包括不限于：1) 数据切片和分片管理，需要手动管理数据分片和分布，这无疑增加了复杂性；2）数据读取和加载效率低的问题，缺乏高效的自动化数据读取和加载机制，会影响整体效率；3）缺乏高级数据操作功能，需要手动实现常见的数据操作，开发成本高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4M9ljHsBYCt47SJqGPkKWNSvXQiabhSLVQck7Iwiaxsj0xFAQTLvWzLNw/640?wx_fmt=png&from=appmsg)

所以我们开始在Pipeline中使用RayData，它提供了一系列开箱即用的算子，和丰富的多模态数据DataSource支持，自动管理数据分片能力，同时具有自动扩缩容的能力，极大的减少了开发成本。

同时在Pipeline中也使用到了RayServe进行高效的模型部署和服务，RayServe 提供了易于使用的 API，使模型能够快速转化为可访问的服务。另一方面，在高可用性和容错性方面。RayServe 具有内置的高可用性和容错机制，可以自动检测和从故障节点恢复，以确保服务的稳定性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4Lug6KaKyyOCyJvpp4o3kc7IdWzibOlPYEvqQlA0NPzYOyCzwAeicSciaQ/640?wx_fmt=png&from=appmsg)

在构建Audio数据处理Pipeline中，我们看到Ray的优势有：

1. 良好的可扩展性，从单机到大型集群的轻松无缝扩展
2. 灵活的 API，易于编写和管理复杂的数据处理任务
3. 完善的数据生态，为各种数据处理需求提供全面的解决方案
4. 高性能，高效地分布式计算、数据传输
5. 兼容性好，RayData 与现有的数据处理库和框架（如 Pandas 和 Spark）兼容，可以轻松集成到现有工作流程中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4ll38IIYXKTvL6xziapXPvrkibPaM7Q7WxqZY1F3FbD05TjCzng5aJ65Q/640?wx_fmt=png&from=appmsg)

接下来介绍如何使用Ray来增强Video数据处理Pipeline。大量高质量的视频数据是视频生成基础模型训练的关键，然而与文本图像和音频相比，视频数据量庞大，而且与其他数据格式相比，处理视频数据需要更多的计算资源和时间。比如，对于视频数据经常需要使用 ffmpeg 进行视频编码和解码，这需要很多计算资源和计算时间。因此，高效处理大量视频数据并实现高吞吐量和可扩展性是一个关键挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4uZoLgYnq9YAricmsBSLtevCn8RVLZibR7pVZKyEpARVY5QzwkWPQuu3w/640?wx_fmt=png&from=appmsg)

视频数据处理流程一般有如下步骤：流程需要处理一系列的原始视频，时长可以从几秒到几小时不等。使用视频分割算法，将视频分割成不同的片段，每个片段的时长可以从几秒到 1 分钟左右。然后，下一个步骤是视频处理算法。首先裁剪视频，以便只选择需要的视频，同时还会对视频进行评分。在这个过程中，需要将元数据存储到数据库中，并将片段上传到对象存储中以备将来使用。下一步称为打包，我们使用Ray构建了打包过程，选择需要的视频片段，将来自对象存储和元数据的所有片段放入一个 Parquet 文件中，打包后的Parquet文件将被用于接下来的训练。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4Fv4vbd9TYncXMnyAM5rQpeXmlJDDicasBGA5XHMZfw1iaLdmEe1iatzIA/640?wx_fmt=png&from=appmsg)

那么什么是视频数据打包呢？正如刚才提到的，视频数据打包就是将一组视频剪辑存储在 Parquet 文件中，以方便高效的数据管理和访问。这样做的目的是避免在训练阶段加载大量小文件，预先将多个小的视频文件放入一个 Parquet 文件中，然后在训练阶段训练进程直接加载parquet以提高加载效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4AjDdNdC7YU6dNuibibPEZcekqvuD57b51IRia9qTkTJsnugHlaUqu4GTA/640?wx_fmt=png&from=appmsg)

首先调研直接使用RayData构建打包流程。第一步是利用 RayData 从数据库中读取数据，依据不同条件进行过滤操作筛选视频，随后把数据集重新划分成不同的partition，以利于后续进行并行处理。接着是视频处理，从对象存储中下载数据，借助 ffmpeg 等框架处理视频。再将数据打包到 Parquet 并上传。在实验中我们发现这个方案有两个问题，1) 二进制对象的序列化和反序列化，尤其对于大对象会非常耗时；2) 一旦 ObjectStore 满，Ray就会把 Object Spill 到磁盘上，从而影响整体性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4G3Lfib4E8cCKDug6g4SHeLvMJEH3SMZOtEyb4zsBC8gWF1dmchQWnwg/640?wx_fmt=png&from=appmsg)

所以，打包过程中将视频数据像存储在 objectstore中，特别是在大容量的情况下，效率不高。尝试使用另一个解决方案，将所有操作融合到单个 actor 中，以避免 actor 之间的数据传输。如上图所示，actor内部启动多个线程一起运行，在每个线程中下载视频并运行视频处理操作，然后写入 Parquet 文件并上传到外部存储。这个解决方案效果很好，可以实现高吞吐量，并且具有良好的线性扩展性，增加更多的 CPU 资源，带宽也会相应地增加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4TjmtgABv3eegQj835v55TpiaNScaVsMkWQrDSWmDV4vib9yIJIwgkyvg/640?wx_fmt=png&from=appmsg)

接下来分享一些使用Ray的经验以及Ray的优势：

1）Ray具有可扩展性和灵活性，可以轻松地从本地 Python 脚本扩展到大规模集群，在数千个工作节点的规模下也能运行良好；

2）对Python友好，ML场景中大量使用 Python，Ray对python非常友好，非常方便进行开发调试，与现有ML生态也结合的比较好；

3）Ray Dashboard提供作业相关的Restful API，可以非常方便地将这些API集成到业务平台中，包括提交和监控Ray作业的运行状态；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4iaZuOcrXk33bbh8RD0ev52rH1Zbbj1hnQ8JXhhmd3tN57Fc4yoTwlnA/640?wx_fmt=png&from=appmsg)

接下来介绍Ray相关的底层基础设施。在字节跳动，Ray被应用在很多业务场景中，包括但不限于Audio/Video数据处理、RLHF等。Ray支持非常灵活的编排和异构资源（CPU/GPU）的调度能力，帮助用户进行灵活的多角色 DAG 编排和异构计算，构建大规模高性能的 ML 基础设施。但是，像许多其他大规模分布式系统一样，生产环境中使用Ray也面临着巨大的挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4zS4taxYTpSHR3dqpsniauIrO9iaQwp5pZFXjAibzicTTAr2SNEA5qPmzTg/640?wx_fmt=png&from=appmsg)

LLMs的数据处理任务通常需要巨大的资源需求和相对较长的处理时间，一般做为离线处理任务。为了降低成本，会使用大量不稳定的Kubernetes Pod来运行这些数据处理任务，这些Pod可以随时被抢占，也可能随时重新添加进来。我们希望Worker节点被抢占不会导致数据处理任务失败或中断。比如，如果一个Ray任务在 100 个 GPU 上运行，其中 40 个GPU被抢占，期望剩余的 60 个 GPU 能够继续高效运行，这是一个非常大的挑战。虽然 RayCore 提供了强大的 Actor 和 Task 恢复机制，但在当前的 RayData 设计中，当一个 Actor 异常退出，必须等待 Actor 重新启动才能继续执行 task，如果资源不足，Actor将处于Pending状态，因此RayData任务也会hang住，直到资源恢复。为了解决这些问题，我们设计并开发了RayData增强方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjPpvkzgibb5Hzx3WphBaAJ4ElGWRuqJfMc54pxdDT0mDMP1Afoy0OrHHgHThkKibgg04ibZVH5lVQdg/640?wx_fmt=png&from=appmsg)

第一个增强是在RayData调度器重中进行任务重新分配。简单来说就是将RayData Actor Pool中失败的task分派给Actor Pool中其他的actor运行。具体做法是，将Actor Pool中actor的max\_restarts设置为0，也就是完全由RayData掌控actor的生命周期，这样在actor挂掉后RayCore不会再重启它。当RayData调度器检测到actor异常退出时，原先分配给它的未完成的task，会被重新分配给其他actor。RayData调度器重新创建一个map actor，如果没有资源，actor处在pending状态，但是这不会阻碍RayData任务的正常运行。一旦新的资源加入，actor就会变为running，重新加入到actor pool中。

![](https://mm...