---
title: 我们如何为邮件安全构建高速威胁狩猎
url: https://mp.weixin.qq.com/s/R1OnZnMtMUTGCICYiYw8Ng
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:59.078637
---

# 我们如何为邮件安全构建高速威胁狩猎

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcQW2Vg2bcPlRv8IkmT1RqE4RbWpHU3kxXXUXcMoAqAO3IgBJA0iamjwBuoiaecpVTt3pibjme26McerEe4AH4ib1Slx4yO1OTRCgs/0?wx_fmt=jpeg)

# 我们如何为邮件安全构建高速威胁狩猎

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Sublime Security 的工程师分享他们如何让威胁狩猎和检测回溯测试变得飞快。秘诀在于将查询拆分为“候选选择”和“评估”两阶段，并用上数据分片、列式存储、智能并行化等一系列巧妙的设计和优化。

对安全团队来说，快速分析历史数据是硬需求。

SOC（安全运营中心）、事件响应和情报团队需要狩猎威胁，调查攻击和失陷事件。检测工程师则通过回溯测试来验证检测规则的效果。在这些场景里，查询慢一秒，攻击就可能多蔓延一步。

Sublime Security 是少数同时提供历史威胁狩猎和检测规则回溯测试的邮件安全平台之一。能做到这一点，是因为它建立在专为查询邮件数据设计的领域特定语言 MQL（邮件查询语言）之上。作为服务一些超大型企业的邮件安全解决方案，速度和规模缺一不可。

在这篇文章里，我们聊聊 Sublime 是如何能在不影响产品体验的前提下，及时处理数百万封邮件的。

## 开始前的准备知识

首先要明确的是，在后台，Sublime 把“狩猎”和“回溯测试”视为一回事，只是展示层不同。所以下文我们会统一用“狩猎”来指代两者。

其次，Sublime 将邮件数据拆分存储于热存储和冷存储。轻量级的元数据放在热存储（通常是数据库），而庞大的数据（如原始邮件内容、附件、HTML等）则存放在冷存储（如对象存储）。为了保持速度，我们先在热存储中查询，以减少最终需要访问冷存储的请求量。为了让冷存储操作也更快，我们尽可能地进行并行处理。

好了，背景说完，咱们切入正题。

## 狩猎操作化：候选与评估

并非所有 MQL 操作的成本都一样。有些操作相对廉价（比如一些基础查询），有些则比较昂贵（比如各种数据富化操作）。本着效率优先的原则，我们先跑廉价操作，只对廉价操作筛选出的消息子集运行昂贵操作。

我们通过将狩猎分为两个阶段来实现：候选选择阶段和评估阶段。

在候选选择阶段，我们通过查询一个存储了每封邮件部分数据的数据库，来找到相关的邮件。这些候选邮件随后被传递到评估阶段进行检索和深度处理。实际上，这两个阶段是并发进行的，由许多工作进程并行处理。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf9cicnKAbPEAqmj6iabpUqicPf2IrQfuRnSRohiaIE3sHZa162KUpNexQsxdxZXERg1oiabkqjayIFakmzickqerOe8bhwwSXl90Jes/640?wx_fmt=jpeg&from=appmsg)

## 邮件摄取：行与块

邮件被处理后，会在 Sublime 平台保存长达30天，以供后续狩猎。这意味着我们不仅要安全地保存完整邮件以备深度分析，还得有办法快速定位到相关邮件。

我们的做法是：将部分MDM数据存入数据库（求快），将完整的邮件存入块存储（求全）。对于块存储，我们首先将原始的EML文件解析成一种易查询的格式，叫做MDM（邮件数据模型）文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibe4gk9d9RT7ubReicnxHFj6icJnLePmwV4Hke1R6TRO740D33GSEDFHw2atYFmE5YpIhneupZdC4h1reiap4mueJCYVRXT2aOqh7U/640?wx_fmt=jpeg&from=appmsg)

MDM 文件以 FlatBuffers 格式保存，这允许在评估阶段进行部分反序列化，这个后面会细说。

## 候选选择：理论与案例

为了解释狩猎如何工作，我们看个例子。假设你想调查2025年10月所有来自非应邀发件人的、含有PayPal发票的邮件。

你可能会写这样一个狩猎查询：

type.inbound
and not profile.by\_sender().solicited
and any(attachments,
        .file\_type == "pdf"
        and any(ml.logo\_detect(.).brands,
                .name == "PayPal" and .confidence == "high"
        )
)

当你点击“狩猎”时，Sublime 会把这个 MQL 查询在后台转换成几个步骤，然后返回结果。

### SQL生成：把MQL变成数据库能懂的语言

MQL被解析和验证后，会变成一种中间表示。编译器知道其中标亮的部分（比如type.inbound，附件类型是pdf）可以在数据库里找到。这意味着我们可以将这部分IR编译成SQL，直接在数据库里筛选出符合条件的邮件ID，而不是傻乎乎地去处理时间范围内的每一封邮件。

这利用了“谓词下推”技术，这是大多数数据库索引扫描的核心。要记住，这只是候选选择阶段的IR，它只需要返回一个没有假阴性的候选集。出现假阳性没问题，评估阶段会过滤掉它们。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcgXMwZxQn0icdabbT6XJJTEUUgt4zW82jNL8tibC4iaGmSJXoTFRSPsdq4xiaVHupWEia6ibIUvMeQ8DputGqPsicRhwHqgHJBax8SEs/640?wx_fmt=jpeg&from=appmsg)

最终生成的SQL大概长这样：

SELECT id, received\_at
FROM mdms
WHERE received\_at >= '2025-10-31'
 AND received\_at < '2025-11-01'
 AND "type.inbound"
 AND 'pdf' = ANY(attachment\_file\_types)
 AND NOT EXISTS (
 SELECT 1
 FROM sender\_history
 WHERE sender\_history.email = mdms.sender\_email
 -- 我们只关心收到邮件之前的历史
 AND sender\_history.received\_at < mdms.received\_at
 AND sender\_history.solicited
 )

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf7Ria2ZvDd0QE52STzR4AunYoibogxa9D8x8DlwUiciaAhSmOia7sOguuZmMj7QFYgqqkjrmD1eXaQGNYibbIgLfdo1XyXrnneRbTas/640?wx_fmt=jpeg&from=appmsg)

### 周期分块：化整为零，并行处理

注意到上面的查询只看了十月里的一天，而不是整月吗？这是因为我们把狩猎时间范围拆分成了一个个称为“周期”的块。

通过分块，我们可以更早、并行地处理候选邮件，以便更快地将结果呈现给用户。这意味着我们不用等所有候选邮件都选出来，评估阶段就可以开始了。

分块按时间倒序进行（从新到旧），因为我们想尽快展示最近的邮件，以便处理紧急事件。理论依据是：昨天的问题邮件通常比一个月前的要重要得多（比如恶意链接的有效期往往撑不过30天）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeHTu0ewmKd1L2JX3iaEylUFeCMfFKHXTO3c7xU4Ac2aq4ZUwGoSw048sLatanGqjrZeBN9fNtLrdSvlCxG3vH2zibiaraOB74TuM/640?wx_fmt=jpeg&from=appmsg)

例子中周期是一天，但实际上我们使用查询执行时间的指数加权移动平均值来动态调整周期大小。主要原因是：

* 邮件活动有波峰波谷（比如周一早上和周末），我们需要调整周期大小以在整个狩猎时间内保持性能稳定。
* 当数据库负载高时，狩猎需要自我限流；当数据库资源更充裕时，则可以加速。
* 查询是否易于索引也会影响周期大小。需要O(n)行为的查询可以用较小的批次，而能利用索引的查询则可以高效地搜索更大的时间范围。

我们通过将目标查询时长设定在5-15秒内，并在移动平均中赋予较新的查询执行时间更高权重来实现快速响应数据库负载。我们甚至设定了最大增长率来平滑周期大小的调整过程。

## 评估阶段：去伪存真

当候选消息从队列中被取出后，我们用Go语言对完整的MDM数据执行剩余的MQL查询，以消除任何假阳性候选。这确保了在这个最终阶段之后，只有完全符合狩猎条件的MDM才会作为结果流式传输给用户。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibe4jA3Diae5EEfmXNBxMXgAkXEu3yPqR6YYWJvI236icv6hGtLyug73Hy6mm16dWibQrUVUZOAajxdHUutiaMa7ltVc0VkNq1MoicjY/640?wx_fmt=jpeg&from=appmsg)

看看这个评估阶段的IR是如何提升效率和速度的。

首先，你会注意到我们再次检查了`.file_type`。这是为了保证正确性，避免对非PDF附件运行`ml.logo_detect`。

其次，一个简化版的IR意味着我们能确切知道需要反序列化哪些字段。在我们的例子中，我们只需要MDM中的`.file_type`和`attachments`原始字节，其他都可以忽略。这为我们处理的每一封邮件都节省了大量的CPU和内存。

接着，我们从块存储中获取MDM（以FlatBuffers格式存储），并根据评估阶段IR生成的字段掩码进行反序列化。这一切意味着我们只对相关的PDF应用`ml.logo_detect`，并将结果写入数据库。

更重要的是，为了在评估像`ml.logo_detect`这样的富化操作时不至于压垮下游服务或无限缓存，我们采用了两层缓存系统。Redis作为短寿命、高吞吐量的主缓存，块存储作为长寿命的二级缓存，用于在必要时重新预热主缓存。如果真的发生完全缓存缺失，我们还设置了并发限制，防止请求“惊群”。

虽然我们略过了缓存策略的许多细节，但这一切都说明，为了最大化狩猎速度，我们下了很大功夫。

## 踩过的坑和填平的洞

在构建候选选择阶段时，我们遇到了一些障碍，必须解决它们才能达到“快速狩猎”的目标。这里分享几个。

### 问题一：在“死元组”周围查询

候选选择阶段的处理器通过一个持久化的、基于数据库的队列来协调工作。我们选择利用数据库来实现严格的顺序和持久化队列，无需进行大的架构改动——这也是同时运营SaaS和本地部署方案带来的挑战之一。

数据库带来的一个大问题是：在PostgreSQL中，从队列中“弹出”一条待处理消息，只会将对应的元组标记为“死亡”，但在执行VACUUM清理之前，它仍然存在。这个表上的流量太高了，数据库几乎没机会执行VACUUM，因此所有查询都不得不跳过这些“死元组”去找“活元组”。最终，这导致出队操作变成了全表扫描，尽管你预期只是读取一行。我们是通过追踪查询的CPU使用率并结合查询计划发现这个问题的。

**解决方案：**我们保存了一个已知的最后一条活跃消息ID的游标（这个ID有索引），这样我们总能跳过任何尚未被清理的、之前的死元组。这个游标在每个实例的内存中缓存，并在后台定期从数据库刷新。我们指定第一个处理器（根据分配的ID）来更新数据库中的游标，以避免重复工作。

### 问题二：统计信息泛滥

另一个类似的问题出现在处理器频繁将统计信息写入数据库时。根据狩猎任务的不同，处理器可能快速处理大量消息并随之高频率地更新数据库中的统计行。每个处理器只有一行用于更新统计信息，但在PostgreSQL内部，由于多版本并发控制（MVCC），更新操作会被当作删除旧行并插入新行来处理。这意味着单看一行数据，内部可能存储了一系列死元组，最后才是一个活元组。数据库会消耗额外的CPU，像顺序扫描一样遍历这些死元组来寻找活的那一个。

**解决方案：**我们增加了一个新的、加了索引的`updated_at`列，这样我们可以使用该行最新的`updated_at`来找到活元组，即使只是一行数据，这依然有用。索引让我们可以完全跳过那些尚未被VACUUM的旧版本行。

### 问题三：过于“天真”的处理器

最初，每个处理器都会“天真地”查询数据库来刷新狩猎状态，以决定是否需要继续处理。随着每次狩猎的处理器数量增加，我们遇到了极高的数据库负载和争用。

**解决方案：**与更新游标类似，我们指定第一个处理器来聚合统计信息，并将其提供给其他处理器（通过Redis或预聚合表）。处理器ID是按可用ID的升序分配的，因此我们总能知道哪个是“第一个”处理器。这使得我们可以在不增加状态查询负载的情况下，扩展处理器数量。

## 未来方向：更快，更智能

我们的狩猎已经很快了，但总有改进空间。

举个例子，在热存储中放入太多数据可能会耗尽RAM，进而导致缓存缺失和数据库颠簸。为了防止这种情况在候选选择阶段发生，我们正在研究使用有损数据结构（如布隆过滤器）来进行高效检查，同时不过多牺牲存储或性能。既然评估阶段最终会处理任何假阳性，我们在候选选择阶段就有一些用精度换取性能的操作空间。

此外，目前每次狩猎都固定分配了一定数量的阶段处理器，但每次狩猎的需求和瓶颈各不相同。未来，我们将根据每次狩猎的瓶颈动态调整处理器数量，同时尽量减少对其他并发狩猎的影响。例如，在数据库使用率较低的时段，我们可以利用更多数据库连接来增加候选选择阶段的处理器数量，在负载高峰时再缩减回来。

## 速度即正义

总的来说，我们通过将狩猎过程拆分为候选选择和评估两个阶段并使其并行处理，最大化地提升了狩猎和回溯测试的速度。这种架构让我们能够扩展算力以满足企业级需求，同时不降低平台性能。通过深挖瓶颈，我们在这个架构内添加了大量优化，而且还会继续增加。我们的目标是让狩猎变得更好、更快，让安全从业者获得他们所需的大规模处理速度。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过