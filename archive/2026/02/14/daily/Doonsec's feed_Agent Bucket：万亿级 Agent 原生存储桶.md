---
title: Agent Bucket：万亿级 Agent 原生存储桶
url: https://mp.weixin.qq.com/s/A6sUm-s44MwM7ZvIzqs_Eg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:11.087186
---

# Agent Bucket：万亿级 Agent 原生存储桶

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FefzIDjvI90XKKqmFEj0ltXuaHTpJM2crVhpZZ857bJzKicxcoWGkRegaK87mBVibmlt3XaLGp08QoZO1iahHFcPWeNSyERJicFRdZ4/0?wx_fmt=jpeg)

# Agent Bucket：万亿级 Agent 原生存储桶

原创

火山引擎存储
火山引擎存储

字节跳动技术团队

![]()

在小说阅读器中沉浸阅读

AI Agent 如雨后春笋般涌现的今天，开发者们正以前所未有的速度构建着充满想象力的智能应用。从能帮你编写代码的编程助手，到一句话生成一部电影的创作工具，再到时刻待命的个人智能助理，Agent 正在重塑我们与数字世界的交互方式。这股浪潮背后，一个共识日益清晰：借助 Serverless 架构（如 Lambda）、大语言模型（LLM）和云存储（如 S3、TOS），结合 Vibe Coding，任何人都能在 30 分钟内快速搭建一个属于自己的 AI Agent。

从“能用”到“好用”，Agent 开发者在从“玩具”向“生产级应用” 依然需要跨越难题。随着业务迈向海量用户，开发者不得不面对一个极其复杂的挑战：如何在对象存储上为海量终端用户构建完备的存储方案 ？对于大多数开发者而言，这不仅是技术门槛，更是阻碍 Agent 规模化分发的鸿沟。Agent Bucket 旨在通过 AI 原生的存储设计，彻底简化多租户系统的构建流程，提供更友好的 Agent 能力。

**当亿万用户涌入，传统对象存储“不够用了”**

想象一下，你开发了一款爆火的 AIGC 应用。每个用户都会生成并存储大量的图片、视频和临时文件。作为开发者，你自然会选择像 S3 和 TOS 这样成熟、可扩展的对象存储服务。但问题来了：如何为海量用户管理数据？

2022 年 S3 的博客 《Partitioning and Isolating Multi-Tenant SaaS Data with Amazon S3》中阐述两种方式， “每个租户使用独立的 S3 桶” 以及 “基于前缀隔离的共享 S3 桶 ”：

1. **为每个用户创建一个独立的“桶” （Bucket）：**这在用户量少时可行，但当用户增长到数万、数百万时，桶的数量会迅速爆炸，管理成本和资源限制都让人难以承受。S3 提供全 region 合计 10000 的桶配额，但面向火热的 AI 能力，1 万还远远不够。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedNATgUQIT4JVxH30sT755LjicGu4WBc7Hic59YgC1icTDNwc0NqD2vWrVNnnEOnykawJox0uM5DUTvjLNkCe884OccYibaqtymbt0/640?wx_fmt=png&from=appmsg)

AWS S3：Bucket-Per-Tenant Model

2. **在同一个桶内用“前缀”区分用户：**这成了主流方案。比如，用户 A 的文件都以 ***user-a/*** 开头，用户 B 的则以 ***user-b/*** 开头，就像在电脑上用文件夹管理文件一样。不过对象存储中不存在原生的文件夹，这个方案是在 “K-V” 的存储系统中通过“公共前缀”（Prefix）区分多租户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedugNStANN6Hq0AycRSc1In3UdEVls7fuy85YtO8YHj8AqaLBI8ecGgegG7Og70FiaclSqWfddwwEWDazNsAeA4xkJ8CJ0Y2RCw/640?wx_fmt=png&from=appmsg)

AWS S3：Object Key Prefix-Per-Tenant Model

这种基于“桶”或“前缀”的方案，过去十年里一直被广泛采用。“一用户一桶”的方案由于 S3 协议上要求 Bucket Name 全球唯一，天然有更强的限制，导致扩展性不佳。“单桶多前缀”方案作为当下事实标准，但对象存储服务的高级特性只基于 bucket 或者少量 prefix 提供，例如权限、生命周期、性能、可靠性、容量与计量等，无法支持数十万以上的用户量级业务，给开发者带来沉重的系统复杂度负担，也容易引发“扰邻现象”，导致性能失控。存储层面需要有更合理的方案提供给 Agent 开发者，让开发者能最高效、快速的构建平台化能力：

* **多租隔离：**所有用户的数据混杂在同一个桶里，一个用户的异常高频访问，就可能影响到其他所有用户，产生“邻居效应”。性能隔离、故障隔离都无从谈起。
* **权限管控：**复杂的权限策略（IAM Policy）难以维护，很容易出现配置失误，导致用户数据被意外访问，尤其是在需要与其他云服务交互时，风险敞口更大。
* **成本清晰：**你很难精确地知道每个用户到底消耗了多少存储空间、产生了多少流量费用。当你想根据用量向付费用户收费时，计费和计量就成了一笔糊涂账。

为什么这些看似基础的需求，Agent 开发者们在对象存储上实现有些“重”？深究其原因，是因为在当下的云原生架构中，S3 这种“对象存储”与传统“文件系统（FileSystem）”之间存在着一片巨大的真空地带。对象存储（S3/TOS）的本质是“扁平化”，设计初衷是海量数据的简单存放，像是一个巨大的仓库，虽然容量近乎无限，但在逻辑结构上极其简单。它缺乏原生的高级目录管理、细粒度的元数据控制以及真正的租户感知。当开发者试图在“扁平”的 S3 上，通过硬编码前缀的方式去模拟一个“立体”的多租户文件系统时，我们实际上是在用一种“静态的 KV 存储”，去承载一个“目录语义、强隔离的” Agent 应用的文件访问方式。也就是说 Agent 需要**额外消耗 token** 来管理文件，并控制解决多租户权限与隔离。这些额外消耗的 token 都在表明  S3 定义的简单存储服务（Simple Storage Service ） 对 Agent 不够简单（Simple）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecJKOz876Qrc3suoQiaic9SVX5uuCJaicicGodlryU6NjwMZaL34Aj7qU9oxiaE23gRmy0hIGrxia4ibGdGCWY6ibQMrQ3117x80QstcOk/640?wx_fmt=png&from=appmsg)

S3 Access Points Illustration – providing fine grained policy per team

2025 年 S3 博客 《Design patterns for multi-tenant access control on Amazon S3》 中进一步阐述了 S3 Access Point。这意味着可以创建多个虚拟网络接入点，并为每个接入点配置一个定制的接入点策略，在网络调度层面对于多租户场景有了一些方案。网络调度可以解决权限和访问策略的问题，Agent Bucket 中也涵盖了这一关键设计，并进一步阐述“两把锁”的安全隔离模式（详见 技术设计 章节）。不过 Agent 在 Access Point 基础上，还需要进一步的能力，让我们来一步步分析 **AI Agent 友好的存储产品设计。**

**Agent Wonderland**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedRceibAibmicibysLtWXts2DjDeYuV9UvibsQDASRGXjEyLgkHz757fQYfXcxxKJyoqEsNQtjCHBnbwmmicyz50EgUS0u9FEFZlU11w/640?wx_fmt=png&from=appmsg)

一个理想中的 Agent 开发者在开发 AI Agent 时，可以基于 “Agent SDK + 存储 + MaaS 服务” 构建一个完全 serverless 化的 Agent：

* Agent 可以完全 serverless 运行

* 可以通过 Vibe Coding 的方式，组合现有的产品能力构建出 Agent
* 只需要维护 “ADK” 的 python 脚本
* 存储 使用 对象存储
* AI 能力 使用 豆包
* 理论上无 ECS 或 其他实例型产品

* Agent 可以有一种 object 语义的存储（保存文件），提供多租户接入能力，百万级起步，可扩展到 亿级别
* Agent 可以为每个用户提供独立的空间（多业务之间，业务或者 uid 都可能会重名）
* Agent 可以直接配置每个 user 的带宽，配置 user object 总大小上限
* Agent 可以根据 user 出账、监控、观察
* Agent 可以为每个 user 的文件配置 访问策略

**Agent Bucket：为 AI Agent 注入“多租户原生”基因**

为了从根本上解决这一难题，我们提出了一种全新的对象存储范式——**Agent Bucket**。它的核心创新，是在传统的“桶（Bucket）”和“对象（Object）”之间，引入了一个新的原生资源层级：**对象集合 （ObjectSet）**。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeccvRRlHtdb6BLBPZ3xZjMBN7OV2n58AicO3FeTyWzzfP6y3Y6WIfyURuibDf5VhlyicLRFY9Q9gbOnWVSfOjUZFKGS6ps8hNd7lQ/640?wx_fmt=png&from=appmsg)

这个设计的核心思想极其简洁：**为你的每一个终端用户，都匹配一个专属的 ObjectSet。**你可以把 ObjectSet 想象成一个专为每个用户打造的**“数据保险箱”**或**“云端个人空间”**。它在逻辑上属于你（开发者）的 Bucket，但在物理和管理上，它拥有自己独立的“个性”和“生命周期”。

**Agent Bucket 每个桶支持 1 亿个 ObjectSet**，这意味着你可以从容地为上亿规模的终端用户提供服务，仿佛每一位终端用户“生活”各自独立的存储空间中，而无需再为多租户存储管理焦头烂额。

**ObjectSet 设计——面向 Agent 友好的能力**

Agent Bucket 中 ObjectSet 不仅仅是增加了一个层级，更是将多租户场景下最棘手的需求，都变成了开箱即用的原生能力。当数据归属权在 ObjectSet 这一层被明确下来后，一系列过去难以实现的能力便水到渠成。

1. **原生隔离：**在 ObjectSet 层面，你可以为每个用户设置独立的 **QPS、带宽限制和容量配额。**付费用户的体验可以得到保障，免费用户的异常行为也不会波及他人。这是真正的**故障域隔离**，让“邻居”不再相互干扰。
2. **原生权限：**每个 ObjectSet 都可以拥有一个**独立域名。**这意味着你可以给用户 A 一个 ***user-a.yourapp.com*** 的专属访问地址，而不再是暴露整个存储桶的域名。更巧妙的是**“两把锁”**设计：第一把锁是云服务商颁发的临时访问凭证 （STS），控制应用层面的访问权限；第二把锁则是 ObjectSet 的独立域名，从网络层面就将访问请求锁定在用户自己的数据空间内。这极大地提升了数据安全性。
3. **原生监控：**在监控仪表盘上，你不再只能看到整个桶的总览数据。你可以 **by-ObjectSet** 分解监控图表，清晰地洞察是哪个终端用户在进行大量的访问，从而做出精准的运营和优化决策。
4. **原生能力下沉：**过去只能在桶级别设置的策略，现在都可以下沉到每个用户。你可以为不同等级的用户设置不同的**数据生命周期 （Lifecycle）**，或者为每个 ObjectSet 使用**不同的加密密钥**，实现更精细化、更安全的数据管理。
5. **原生计量：**想知道每个用户占用了多少存储空间？想把存储成本精确分摊到每个用户头上？现在变得轻而易举。Agent Bucket 会自动为你统计每个 ObjectSet 的容量和使用情况，让你的**计费与分账**清晰明了。
6. **原生计费：**开发者可以轻松实现成本分摊，将存储产生的费用精准反推到每个终端用户身上。例如，根据 A、B、C 不同用户实际产生的成本比例进行差异化收费，为 Agent 的商业化提供数据支持 。
7. **原生容量上限：**为了控制 Agent 的运营成本，你可以为每个 ObjectSet 设置 Quota（容量上限）。一旦达到预设值，系统将限制该用户继续产生新文件，从根源上避免多租户场景下的资源滥用。
8. **原生智能：**Agent Bucket 让 Agent 跳出传统文件简单“存取”的局限，给 Object 赋予原生智能，更高效的支持 Agent 一站式开发。ObjectSet 可一键开启智能索引，为 Agent 提供原生友好的多模态问答能力，替代传统 Object CRUD 的机械操作；甚至支持一键开启 **Agentself** 模式，串联向量、知识、模型与 prompt，直接透出场景化的子 Agent 功能，让上层 Agent 开发者专注于主体业务工作流创造，充分释放智能变现效率。

**应用规模井喷带来的技术挑战**

Agent Bucket 通过引入 **ObjectSet**这一原生概念，为应用开发者提供了一种优雅、高效的方式来管理亿万级别的终端用户数据。每个用户的数字资产被安全地存放在其专属的 ObjectSet 中，天然实现了隔离、计费与配额管理。

随着应用规模的急剧扩张，海量 Set 的管理复杂度、隔离难度、物理瓶颈都同时显现出来：

1. **海量用户分级管理问题：**应用在差异化管理大量不同等级用户的资源和特性时，需要自行设计实现用户的分级元数据，并关联对象存储特性开关，在 Set 的原生概念上帮助开发者优雅的管理用户分级是加速应用落地的重要。
2. **单集群容量瓶颈：**尽管 Agent Bucket 在逻辑上可以无限扩展，但其元数据默认存储在单个物理集群中。当桶内对象总数达到千亿甚至万亿级别时，单个集群的物理容量就成了无法逾越的上限。
3. **接入点共享问题：**Agent 的业务多样性和海量 user 对接入点本身带来了更大的安全风险和爆炸半径，如何根据大量不同业务和用户的差异性来做动态调度，实现差异化的安全、隔离和加速能力成为一个难点。

**Set Tagging： 标签化管理用户分级**

ObjectSet 提供原生的标签化管理方式，让 Agent 开发者可以简单的使用 set tagging 能力，完成用户的分级治理；开发者可以为每一个定义出来的用户级别对应为一个 tag，并对每一个 tag 开启不同的配额和特性，所有被打上这个 tag 的 ObjectSet 都会应用对应的配额和特性。以 V1、V2、V3 三个级别举例说明：

* V1：默认级别，免费用户，所有的 ObjectSet 的缺省 tag，可配置最多存储 1GiB 数据，公网分发不可超过 100mbps 带宽，单流下载速度控制为 1mbps；
* V2：入门级收费会员，配置最多存储 10GiB 数据，公网分发不可超过 10gbps 带宽，单流下载速度控制为 10mbps；
* V3：高级收费会员，除了提供更大的存量和公网分发配额以外，还支持配置开启额外的公网弱网加速和高性能介质加速能力；

Agent 开发者可以面向不同 user 的不同发展周期，灵活的使用 V1/V2/V3 tagging 来管理这些用户可以使用的资源和增值特性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedBZcrlFgAQXXm7nXJAzrXZh8msBbkevqibyIY3dQWuaCaup8RPkkWDVCRXibPgot3S3lKbMcQhwicFmtyc8MfTF9ojcj0YBBAH0M/640?wx_fmt=png&from=appmsg)

**Set Slice：海量用户数据原生隔离**

当一个 Agent Bucket 内的 Set 达到亿级，对象数量达到千亿、万亿级别时，**“单 Bucket 所有元数据集中在一个 KV 集群”** 这一事实本身，会带来容量和性能的双重风险。

Set Slice 提供了一种**“逻辑不拆、物理拆分”**的思路：

* 从逻辑上看，你仍然只管理一个 Agent Bucket。
* 在物理上，根据 Set 以及 Set 内对象名的范围，将元数据划分成多个**Slice（切片）**，每个 Slice 可以存放在不同的  集群上，多 Set 天然隔离，单 Set 横向扩展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fefib7fzuv1LZZMf2LZwNMYSbl8eV8JMPE8AJia1KYFfFgkMhKp6epS0kBWdau0G2ibgRic4cCCWYsDiaV8sVKAl3OVJVHqM0WLTGhMM/640?wx_fmt=png&from=appmsg)

Set Slice 是对 ObjectSet 能力的进一步延伸与保障，它在底层解决了物理容量的无限扩展问题，同时确保了上层 ObjectSet 管理模型的稳定性与一致性。

* **管理边界稳定：**即使一个 Agent Bucket 的数据横跨了多个物理集群，**ObjectSet 依然是权限、配额、计费和监控的唯一基本单位。**开发者面向 ObjectSet 配置的策略（如访问控制、容量上限）会自动在所有相关的 Slices 上生效，无需关心底层数据的分布。
* **单 Set 可线性扩展：**当某个 ObjectSet 数据量高速增长时，其数据会自然地分布到多个 Slices 中。随着整体集群的扩容，该 ObjectSet 的容量也随之**无缝、线性地增长**，开发者无需对该 ObjectSet 本身进行任何拆分或迁移等破坏性操作。
* **跨 Set 资源隔离：**通过将不同范围的对象分布在不同的物理集群上，SetSlice 实现了更高维度的资源隔离。结合 ObjectSet 的配额管理，可以有效**防止某个“超级大户” ObjectSet 的数据增长挤占单一集群的全部资源，**从而影响到其他 ObjectSet 的稳定性，让整体容量风险变得可控。
* **逻辑统一与兼容：**对于业务和开发者而言，无论底层有多少个 Slice，他们面对的始终是一个逻辑统一的 Agent Bucket。所有针对桶、ObjectSet ...