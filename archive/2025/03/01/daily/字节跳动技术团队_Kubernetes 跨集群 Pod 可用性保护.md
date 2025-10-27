---
title: Kubernetes 跨集群 Pod 可用性保护
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247513617&idx=1&sn=2181e97c2240f8cee3b8b3eb372fba43&chksm=e9d37df3dea4f4e54d081807dd0f107267df6698236ef89f6f41522b191602137d0fa2546fbd&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-03-01
fetch_date: 2025-10-06T21:59:37.844707
---

# Kubernetes 跨集群 Pod 可用性保护

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjq5IlQFl6ojIuw0l7BKjg7mhI3oYs6zE73VoId58a5IV0lp1hZRRwia9FhnwshqoR69hUM2ZrNVdA/0?wx_fmt=jpeg)

# Kubernetes 跨集群 Pod 可用性保护

字节跳动技术团队

多集群部署微服务带来了可扩展性和容灾性等优势，但也引入了全局层面的脆弱性——中心控制平面的任何问题都会级联影响所有被管理集群，造成灾难性后果。其中最严重的场景之一是由于Pod删除导致的服务容量丢失。这在Kubernetes复杂的事件链中可能由多种原因引发，例如：

* 意外删除所有Deployment的owner资源类型的CRD
* 集群拓扑配置错误，导致用其他集群的spec覆盖当前集群
* 多集群滚动更新实现缺陷，同时在所有集群触发更新
* 联邦主集群的etcd磁盘损坏，导致Deployment对象从索引中移除
* 多个集群同时独立进行Pod驱逐操作，并发度不受控

虽然这些问题均可单独解决，但成因多样且在持续变化的基础设施中难以穷举。更便捷的方式是采用端到端处理：只要全局要求未满足就阻止Pod删除。因此我们开发了Podseidon项目——当跨集群的最小可用性要求不满足时，拒绝删除请求的准入webhook。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n81xxQ54j1awfA8lfreecdr2UpBb8iazWOyLcDQiaL3Bqgh2kfia53tUO1jQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**0****1**

**整体设计**

#

Podseidon引入PodProtector CRD，其spec与原生PodDisruptionBudget相近：

```
apiVersion: podseidon.kubewharf.io/v1alpha1kind: PodProtectorspec:selector:matchLabels: {app: www}minAvailable: 8minReadySeconds: 30
```

为与现有工作负载集成，Podseidon提供可定制插件的控制器 podseidon-generator，用于从Deployment等根属主工作负载自动生成并同步PodProtector。部署在每个集群的podseidon-aggregator控制器将集群内Pod当前状态聚合写入PodProtector的status字段，而各集群并配置了准入验证 webhook podseidon-webhook，在可用性底线未能满足时拒绝Pod的删除请求。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n81UPwo3095qA5FoDXQdyoLs57nrAPR3YBnBL9jV4nJViboSTobyk2VxMw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**同步路径 vs 最终一致性**

Pod删除事件有两种数据源：list-watch与准入webhook，各有优劣：

|  |  |  |
| --- | --- | --- |
|  | List-watch | 准入 webhook |
| 及时性 | 异步，通常滞后~100ms | 同步，UpdateStatus成功时相对其他 webhook 实例具备原子性 |
| 准确性 | 代表过去某时刻的真实快照 | 可能包含被其他原因拒绝的删除事件 |
| 相对实际状态 | ≤ 实际删除数，可能遗漏最新事件 | ≥ 实际删除数，可能误计被拒事件 |

举个图表化的例子：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Jn4sedy3xuGNpZdcKpKHOgxm9ZxhLkiaO4nHxicbXOuBjfSic8JhZxUSwMLPYdgvibRgscGU5kWa3oX3JF5EGl238A/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

（实际的pod删除过程涉及多个步骤，但为了讨论简单起见，我们假设在成功执行DELETE请求并设置deletionTimestamp后，pod 会立即被删除）

list-watch 低于实际值，这意味着突然大量删除事件会被错误地允许爆发，所以这并非一个安全的选择。但是使用来自webhook的事件计数也不可行，因为它会无限制地偏离实际状态。

相反，我们结合了两个数据源：webhook 存储已批准的 pod 删除的历史记录，aggregator将其视图时间之前的历史记录压缩为最终正确的状态。PodProtector 对象同时包含来自aggregator最后观察到的状态以及其后来自 webhook 的增量历史，后者作为临时缓冲等待aggregator进行权威聚合。当删除突发过大，无法在单个 PodProtector 对象内存储（因为可能包含上万副本Deployment的每个副本的条目）时，最早的Pod删除事件将被压缩到某个时间范围内，避免超大PodProtector对象影响存储集群性能。

示例时间线：

![图片](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n81DaC4jWlqDFfoSwCicicJcHzPxvmx5KUm0v9U5E0YCWlIKo0T3MszdUTQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

因此，分歧的 webhook 线会定期校准到实际线。考虑之前的示例，其中aggregator每秒报告一秒前的状态，校准后的线与实际线更接近：

![图片](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n81ENd8f82FDnjweiaSzM7nQ7XGuQHqhdvMkskLwRPvV1Jje5pYnGK4pCw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

除了压缩删除历史之外，aggregator还会将扩缩容、数据面等非删除事件导致的可用性变化同步到基线值。由于 Podseidon 仅旨在防止控制平面导致的不可用，这些状态变化的延迟相对可以接受。使用此双数据源方案，可以平衡正确性和及时性的要求。

**Aggregator 快照时间推断**

为准确截断准入历史并保留当前快照后的增量删除事件，需从aggregator的pod list-watch事件中获取事件时间戳，然而Kubernetes原生未提供该功能。

最理想的方案本应使webhook与aggregator共用同一时钟，但由于删除请求无法通过mutating webhook修改对象字段，这个想法并不可行。故此，我们需通过其他不可靠渠道推断快照时间戳，包括：

* clock：使用aggregator系统时间
* status：使用Pod字段（creationTimestamp、deletionTimestamp、conditions等）

这些方法均存在偏差：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n81qD0qWM45uILbHApHmSVQGc3aEzibYhW0zJQXeicS7kjReXwFau2aYOCg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* 受webhook响应延迟和watch延迟影响，aggregator系统时间会晚于准入webhook录入PodProtector准入历史的时间
* Pod字段时间数据源不一致，部分早于、部分晚于webhook响应，但无watch延迟问题。尤其当status.conditions推断的快照时间早于webhook准入时间时，可能导致快照无法清除引发自身触发删除事件的准入记录。此外，部署于不同机器的组件间可能存在系统时钟偏差。

在字节跳动的实践中，我们部署的定制版kube-apiserver会在etcd存储的GuaranteedUpdate调用中添加annotation。

其值为当前apiserver系统时间戳（功能上就是个lastUpdateTimestamp）。这使得准入历史时间戳与推断的快照时间之间的延迟更可预测，在生产环境中验证该方案，余下的竞态问题机率较小可忽略。对于标准Kubernetes，推荐采用aggregator系统时间方案 (clock)，至少避免了快照无法清除自身触发事件的问题。

不过理论上，即使忽略时钟偏差，当watch延迟过高时，clock仍可能导致假阴性（错误允许pod删除）：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n81A6jJwGGicjFnJOQazcyn2JoXJBA240NTwtXc5wEhCdhILbgQW8XTwTA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在00:01之后，pod X和pod Y被允许删除，此时PodProtector状态中包含两个准入历史记录条目{X: 00:00}及{Y: 00:01}。在00:02时，aggregator收到pod X 删除的watch事件(延迟了2秒）。通过其informer中的新缓存状态，它观察到00:02时的快照包含pod Y而不包含pod X，因此PodProtector状态中的两个准入历史条目都被清除了。实际上这是预期的行为，因为这符合我们的假设：如果在00:02发生事件而前面没有收到pod Y的删除事件，则意味着pod Y实际上并未被删除；但事实上，该请求仍在处理中，只是时间参照系不一致导致误判。虽然aggregator最终会在00:04更新，正确地排除X和Y影响的pod数，但如果webhook在00:03收到另一个其他pod的删除请求（下称pod Z），则会被错误允许准入，因为系统假定只有pod X被删除而pod Y未被删除，从而导致最后一个不可用配额同时被 pod Y 和 pod Z 重复使用。

在灾难性事件中，大量 pod 在短时间内被删除时，这个问题尤其显著。假设有个控制器在同一个Deployment下，在 10 毫秒内并发100个删除不同pod的请求：由于webhook推送了100次准入历史，临时不可用配额下降了 100；但如果aggregator在观察到首个删除事件后、观察到后续事件之前过快进行对账，其中99个会立即被撤销。如果前面的控制器再对其他pod激增99个删除请求，不可用约束便会突破近双倍了。

为缓解此问题，Podseidon 提供了两个配置项，可全局配置或针对单个PodProtector进行覆盖：

* maxConcurrentLag限制限制单个PodProtector中准入历史的最大条目数。当该值小于maxUnavailable阈值时，可以确保aggregator单次最多清除maxConcurrentLag个条目。然而，将其设置得过小会导致PodProtector缓冲挤拥，引致更多假阳性（误拒绝）返回值，从而可能损害发布、缩容等操作的效率，尤其是当频繁失败触发控制器退避逻辑的更长间隔时尤其显著。
* aggregationRateMillis为aggregator添加从接收pod事件到执行聚合的延迟，限制同一PodProtector的聚合频率。如果一个PodProtector最近没有新的 pod 事件，收到第一个事件后会先等待aggregationRateMillis，以容许更多激增性事件进入informer，然后再执行聚合；每次聚合后至少aggregationRateMillis内不会对同一PodProtector进行重聚合。虽然聚合触发有所延迟，但聚合过程使用的是最新的快照，而非事件接收时的快照。这有助于缓解由上述相同对象突然大量删除引起的竞态条件问题（除非我们不幸接收到在第一个事件后正好过了aggregationRateMillis毫秒才开始发生删除激增）。然而，将该值设置得过高可能会导致更多由于控制器响应变慢帶來的误拒绝，例如在正常的滚动更新过程中，当新版本的pod X状态切成可用，可以把旧版本的pod Y下线时：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n8111nn7sCXSInkQT9OYPC2Zyz08PTDn357zPtibIBjGKsykNXZQdata8Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

虽然这可能会导致偶尔的误判拒绝，但replicaset controller或GC controller的重试退避通常能够在第二次尝试时成功删除。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n81IzrusLIibOM7WAue9WibBNDltX8BvnxHicUSpmk7icLo3E9ftv7ofaVtvA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

一个生产机房内的实际pod删除准入率。在有开启Podseidon保护的pod删除中，拒绝率

甚低，基本对用户无影响。

**触发最终压缩**

Kubernetes 的一个重要特性是系统必须具备自愈能力，状态最终趋向spec的要求。然而，上述算法单独使用时无法实现这一目标：当webhook插入了错误的删除事件时，aggregator不会主动将其移除，而需等待kube-apiserver发送新的pod事件才能清除该记录。这可能会在低副本场景中导致死锁——pod删除请求被webhook拦截，webhook正在等待aggregator清除先前无效的删除事件以释放不可用配额，而aggregator则在等待apiserver发送事件，但由于pod删除被阻塞，apiserver根本没有事件可发送。

为解决这一问题，我们利用了单list-watch流中pod事件的强序特性：每个快照都是一个原子视图，涵盖了快照之前所有由list-watch选择器覆盖对象的所有事件。换句话说，如果我们在t₀收到一个pod X的事件，在t₀到t₁之间没有其他事件，然后在t₁收到pod Y的事件，我们就可以确认自t₀事件以来，pod X 没有发生新变化。因此，aggregator可以维护一个待处理池，追踪所有尚未完全压缩准入历史的PodProtector对象，并在收到list-watch流任意pod事件时尝试对这些对象进行对账。即使这些事件来自于未被 PodProtector 选择器选中的 pod，更新了的全局快照时间也能触发更多准入历史压缩。

这问题在大规模集群中便解决了，在这些集群中，每秒可能会有数百或数千次由真正的pod生命周期或数据面事件自然触发pod 更新。然而，对于每秒不到一 pod事件的小型集群，更新事件频率过低，可能数分钟才自然触发一遍对帐，对用户造成可见的影响，如滚动或缩容操作明显减慢。为解决此问题，可能会想到几种方案：

* 为准入历史增设到期时间——这实际上违背了Podseidon的设计目的。在一些极端灾难事件中，watch请求很可能会中断并触发relist，从而在此期间引起非常高的watch时延（在大规模集群中relist可能需要长达数分钟），甚至无法重新建立新的一致性快照。增设到期时间在这种情况下实际上会使Podseidon webhook失去原来的作用。
* 如果一段时间内没有事件则进行relist——但这样的时间周期该设多长？relist过程本身也会导致长时间没有事件，可能会使情况更糟。而且pod list是個很重的操作，频繁的relist可能冲击kube-apiserver的性能。
* 在一个dummy pod上触发事件——这听起来可能不太优雅，但这是我们找到最切实可行的方案。通过循环更新一个会在list-watch流中发送的dummy pod（例如切换pod注解），我们可以确保watch流的最小理论事件率，从而在正常情况下将无效准入历史条目的存续时间限制在这一时间下。

因此，只有第三种方案是可行的。podseidon-aggregator中嵌入了一个循环组件来执行该方案，可以通过 CLI 选项启用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuHSbZdJl10ZdWgjLt2D3n819ufyQiamTpZOO11lmib3IUD9lI1p0Bbg1mS3Yg8oaSbDDRm69Xm2UJ2w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

根据直方图指标推算出某机房中不同大小的集群发送watch事件前后间的最大时间间隔

这个强一致性要求意味着，每个list-watch流的准入历史和聚合状态必须独立存储（我们称之为“cell”）。在aggregator需要使用多个reflector（如多个命名空间、独立标签选择算符等）场景中，它们必须在不同的aggregator实例中执行，且webhook必须配置以识别每个准入请求所对应的cell。

**PodProtector批量更新**

由于每个删除请求都需要在托管PodProtector对象的集群（"core集群"）中预留不可用配额，每次准入都会对core集群进行一个独立的compare-and-swap更新。这种设计在架构上并不合理，因为拆分多集群本来的目标就是将apiserver负载从O(mn)（m为部署数量，n为每个部署的副本数）降低到core集群O(m)。况且，对同一PodProtector对象进行多次并发更新很可能导致冲突退避，在最坏情况下会给apiserver带来O(mn²)的负载压力。

通过RetryBatch机制，对同一对象的请求进行缓冲和批量处理，可缓...