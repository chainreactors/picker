---
title: DISTDET：具有成本效益的分布式网络威胁检测系统
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247488312&idx=1&sn=5cb059ab90faccd3ce2aba06433e4f42&chksm=fe2eecb3c95965a52ed87f6e80525b2a848a71cd83e36f9bc10e711a515ef5eea6bae7dea106&scene=58&subscene=0#rd
source: 安全学术圈
date: 2022-12-08
fetch_date: 2025-10-04T00:53:55.983890
---

# DISTDET：具有成本效益的分布式网络威胁检测系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkwQiavDx0dLpT9yJQvYcb2MrOgxwibibKchCYnb4KTqooVFF7Rn6IxIMHTw/0?wx_fmt=jpeg)

# DISTDET：具有成本效益的分布式网络威胁检测系统

原创

mini

安全学术圈

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFxb2EWWK8Fjz8olK6TTB3bjBjiabwoiacicib08WCLJqibNDMT3ba8YJwSwVolWbjoFQu7icX4m7wE6LwQ/640?wx_fmt=jpeg)

> *原文标题：DISTDET: A Cost-Effective Distributed Cyber Threat Detection System*
> *原文作者：Dong F, Wang L, Nie X, Shao F, Wang H Y, Li D, Luo X P, Xiao X S*
> *原文链接：https://www.usenix.org/system/files/sec23summer\_8-dong-prepub.pdf*
> *发表会议：32nd USENIX SECURITY SYMPOSIUM*
> *笔记作者：mini@SecQuan*
> *笔记小编：ourren@SecQuan*

## 1. 介绍

构建考虑软件行为之间因果关系的起源图（provenance graph）可以更好地提供网络攻击的上下文信息，特别是对于APT攻击等高级攻击来说。起源图将系统执行过程表示为有向无环图（DAG），其中节点表示系统实体（如进程、文件和网络连接），边表示系统事件（如创建文件的进程）。使用起源图，检测工具可以通过构建导致异常检测工具所报告的报警事件来获取APT攻击的上下文信息。这类上下文信息可以有效地揭示高级攻击策略（如区分ZIP的良性使用与勒索软件）。使用起源图来执行攻击检测的现有方法存在两个基本的限制。

首先，现有方法采用集中式检测架构，将所有系统审计日志发送到服务器进行处理，导致数据传输、数据存储和计算成本难以承受。其次，研究者要么采用基于规则的检测技术，这种技术无法检测未知威胁；要么采用产生大量误报的异常检测技术，未能在APT检测中实现准确率和召回率的平衡。

作者因此提出DISTDET，一种检测APT攻击的第一个分布式计算、异常检测和误报过滤技术的具有成本效益的检测系统。DISTDET采用了一种新颖的分布式检测架构，通过将部分APT检测转移到客户端，只向服务器传输代表潜在攻击的摘要图，从而最大限度地降低整体计算成本，从而大大降低了数据传输和存储成本。此外，DISTDET结合异常检测和误报过滤来检测未知威胁（提高召回率）和对抗报警疲劳（提高精度）。

作者在大规模工业环境（1130台主机，14天，约16亿事件）和DARPA TC数据集上的实验表明，DISTDET在检测攻击方面与最先进的技术一样有效，同时显著降低了网络带宽（从11.28Mb/s到17.08kb/s，减少了676.5倍），内存使用量从364MB到5.523MB（减少了66倍），存储从 1.47GB 到 130.34MB（减少 11.6 倍）。截至撰写这篇论文时，DISTDET 已部署到 50 多家行业客户和 22,000 多台主机超过 6 个月，并识别了 900 多次真实世界的攻击。

## 2. 贡献

DISTDET开发了三个主要组件：

* 基于主机的异常检测：DISTDET设计了包括分层系统事件树(hierarchical system event tree, HST)和警报摘要图 (Alarm Summary Graphs, ASG)，以最大限度地减少对客户端性能的影响。每个客户端首先根据学习期间收集的日志构建一个HST作为主机模型。基于创建的HST模型，DISTDET将偏离模型的事件检测作为报警，即进行轻量级异常检测。对于每一个报警，都会生成ASG并将之发送给服务器。
* 误报过滤：DISTDET通过三个步骤来实现误报过滤：警报重复数据删除、警报语义聚合和基于上下文事件的警报排名。
* 全局模型推导：DISTDET通过合并客户端定期发送的HST来推导出一个全局模型，以补充学习期间的所缺失的行为。

## 3. DISTDET是如何检测F-lateral攻击的

DISTDET首先构建HST作为主机模型，并将其传输到服务器以导出全局模型，这有助于解决局部偏差。DISTDET利用派生的全局模型将未观察到的行为检测为警报，并为每个警报生成ASG。在生成ASG之前，首先使用滑动时间窗口来去除重复的报警，并将重复报警的数量记为边的属性。ASG发送到服务器端后，DISTDET将与告警事件关联的命令解析成句法树，并聚合具有相似命令的ASG。聚合后，剩下 29 个 ASG 用于检测 F-Lateral 攻击，DISTDET 根据我们的 ASG Ranking 算法进一步计算它们的异常分数。在这 29 个 ASG 中，有 23 个 ASG（包括 2 个误报 ASG）的异常分数高于阈值 τd，被 DISTDET 报告为攻击 ASG。由于仅遗漏了 2 个 ground truth ASG，因此 DISTDET 可以非常有效地检测 F-Lateral 攻击的攻击步骤（精度为 91%，召回率为 91%）。![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkw719DTeP4D1O3gibBAOQIaoOliczWavDbN85vu2Y3G1fwP4fOQ3X0FUnw/640?wx_fmt=png)

## 4. 细节

### 4.1 Host-based Anomaly Detection

这个组件有两种模式：训练模式和检测模式。在训练模式中，它从系统事件流中为每个客户端训练一个主机模型；在检测模式中，将偏离模型的事件检测为报警，并根据报警生成ASG。

#### 4.1.1 Host Model Training

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkw6GlNCxA3xzfzAgrJ9cqmDxQqF9oTOcuYpRAib6GpIwcibs73jRovfpmg/640?wx_fmt=png)

host model

HST模型由四层节点组成：Event type、Oprtation、Process和Attribute，其中每一层都是关于事件的一组特定的属性。对于一个系统事件，HST在每一层中找到一个匹配的节点来表示事件的相应属性值，或者如果找不到值则会创建一个新节点。

当新创建的节点比例连续两天小于0.1%时，该模型被认为是收敛的。实验结果显示，大多数服务器在3天内达到收敛。

#### 4.1.2 Host Model Detection

在客户端的HST收敛后，DISTDET会切换到检测模式。给出一个检测的系统事件，DISTDET搜索HST，找出是否与该事件属性相匹配的节点。如果没有找到，就会报告为一个报警。DISTDET会认为在学习期间没有观察到的事件会被认为是异常事件。

#### 4.1.3 ASG Generation

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkw305C0u0NkBkxzZWBof4QwLUibpV0MwWCbzV9xjXqaHsy0cVlicllZr1Q/640?wx_fmt=png)

ASG Generation

对于警报，DISTDET会生成一个ASG，其中包含异常事件和其上下文事件。由于一些进程会产生子进程，共同完成某些系统任务，如文件压缩和网络下载。为了去捕捉这种关键信息，对于报警事件中的主体进程p（称为报警进程），DISTDET首先会建立一个p的进程血缘树（process lineage tree），并确定它X代内的祖先和Y代内的子孙。然后DISTDET就把这些被识别的节点（即它们所发起的事件）的每种类型（进程、文件和网络）的前N条出边，以形成一个ASG。

### 4.2 False Alarm Filtering

DISTDET采取三个组件来克服误报事件

#### 4.2.1 Alarm Deduplication

报警去重基于一种观点：相当数量的误报代表相同的行为。为了消除重复的报警，DISTDET为每个报警维护一个时间窗口，所有后续相同的报警事件将被丢弃。在时间窗口结束时，重复报警事件的频率也会被记录到该重复事件所生成的ASG中。根据作者的研究，作者将时间窗口设为24小时。

#### 4.2.2 ASG Semantic Aggregation

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkwxbmDDZvibFAkv60KYSXv4KPXMwTpUpAh1tDFML0qMS7DqtI4YvuNxAw/640?wx_fmt=png)

Semantic Appregation

除了相同行为的重复报警外，作者还观察到大量误报与所执行的类型命令有关，它们仅在某些参数或操作对象上有所不同。因此DISTDET通过使用聚合相似语义的报警来进一步地减少报警事件数量。

DISTDET通过标记命令中的单词来构建命令的句法树，如上图所示。然后计算两个命令树之间的相似度，如果两个命令的相似度超过阙值，则会认为它们是相似的。DISTDET将报警事件相似的ASG进行聚合，并记录聚合后的ASG出现的频率。

#### 4.2.3 ASG Ranking

最后一步是通过考虑警报的稀有度（频率）以及它们的上下文事件（ASG中的祖先进程和子孙进程）是否也异常来确定报警的优先级。作者设计一种排名算法，该算法考虑报警事件及其祖先/后代的异常分数。

### 4.3 Global Model Derivation

在服务器中构建全局模型可以作为每个客户端中构建的主机模型的补充。DISTDET可以通过导出全局模型并分发全局模型来更新主机模型，从而解决局部偏差问题。

这个过程包含以下四个步骤：

* DISTDET从每个主机模型中提取出特定服务的进程列表：主机模型中的 进程节点分为两类，即系统进程和特定服务进程。系统进程在所有同类型操作系统上都是一样的。与之相反的是，特定服务进程是软件应用程序的进程，这些进程可以表示主机所提供的服务类型。通过汇总不同操作系统的系统进程可以得到系统进程列表，然后每个模型都可以通过排除系统进程来导出特定服务进程的列表
* 对于所提取到的特定服务进程，DISTDET计算所提取的进程名称的词嵌入（word embeddings）。DISTDET使用word2vec（一种主流的预训练词嵌入模型），来计算每个进程名称的嵌入。
* DISTDET使用k-means算法根据模型的嵌入向量来对模型聚类。这样，提供相同类型服务的主机会被分组到一个相同的集群中。k的值是根据不同企业设置的，在作者的评估实验中被设置为146。
* DISTDET之后合并相同集群中的公共进程。如下图所示，Model-1、Model-2、Model-7在同一个集群中，它们共享进程p1和p2。DISTDET将这三个模型中p1，p2的行为合并，得到p'1和p'2，然后用p'1和p'2替换局部模型中的p1和p2，得到全局模型。然后将全局模型分发到每个主机以更新本地模型。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkweAZMRsCz3OiaebxTlyFTNiam41deAlXW4C0qAZKLbI5cRD0YDl4icy3Aw/640?wx_fmt=png)

Global Model Derivation

## 5. 评估

### 5.1 DISTDET降低的成本

作者在Industry Arena数据集上比较了DISTDET和Unicorn（最具代表性的集中式架构之一）的成本。

DISTDET 将存储成本从 1.47GB/host（1.63TB/1130）降低到 130.34MB/host（143.83GB/1130），减少了 11.6 倍。

与 UNICORN 相比，DISTDET 将带宽从平均 11.28Mb/s 降低到 17.08Kb/s（减少 676.5 倍）。

DISTDET 将平均计算成本从 364MB/host 降低到 5.523MB/host（客户端为 5.52MB，服务器端为 3KB，即减少了 66 倍）。

DISTDET 将主机成本（保护单个主机的费用）从 3.4 美元降低到 0.061 美元（减少 56 倍）。因此，为了保护 1,130 台主机的整个集群，DISTDET 的成本仅为 68.93 美元，而集中式系统的成本为 3,842 美元。此外，所花的钱只是可以量化的成本，还有业务受损、技术壁垒等其他隐性成本。例如，在采用集中式系统时，使用11.28Mb/s的网络带宽进行安全检测会严重影响其他日常业务。另一方面，由于服务器端需要401GB的内存来实时检测APT攻击，因此需要额外搭建一个如此规模的集群。这些障碍极大地限制了现有集中式方法在现实世界中的使用。

### 5.2 DISTDET的有效性

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkwyzyu8AWa6qaQSXBxNwL22Af6A4suBTwtLppxVOgRd3HlFLedNWeg0w/640?wx_fmt=png)

Detection Results

DISTDET 报告了 11K 个 ASG 中的 141 个攻击 ASG，其中 2 个是误报 (FP)。由于有 139 个标记的攻击 ASG，DISTDET 没有遗漏任何真正的攻击，实现了 100% 的召回率和 99% 的准确率。并且作者发现，那两个误报是由于下面两个原因所引起：(1). 罕见的良性行为。Windows Explorer.EXE 启动了意外的主题更新，导致创建了 \Local\Microsoft\Windows\ActionCenterCache\xx.png 文件。相关事件在模型中以低频率记录，导致误报；(2). 日志的缺失。由于缺少日志，计划任务apt-daily.service 被标记为攻击，这是一项定期刷新Ubuntu服务器中可用包列表的服务。

### 5.3 误报过滤

#### 5.3.1 全局模型的有效性

对于不同的集群，全局模型平均可以减少70%左右的误报。并且作者选择了企业中最具代表性的服务：MongoDB、Redis和Kubernetes集群作为案例研究来展示全局模型的有效性。如下图所示，全局模型（虚线）产生的误报数量远少于局部模型（实线）。当仅依靠局部模型进行检测时，每个主机产生的平均误报数为 240，而全局模型报告的平均误报数为 39。这表明全局模型可以有效地补充主机模型以消除局部偏差。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WE7rfGNxvYhGOoQlvFHhBkwcgwibfXltW77HTaDEI5oI8m7DXBrTmGgPicVPlaTvEvXoMjKpPQU0U4A/640?wx_fmt=png)

False alarms

#### 5.3.2 报警去重的有效性

在为期两周的实验中，1,130 台主机总共发出了约 100 万条警报，平均每台主机每天发出 69 条警报。使用 24 小时的滑动时间窗口进行重复数据删除后，警报数量减少到 76,000（4.8 个警报/主机/天）。这表明DISTDET以较小的开销减少了客户端93.03%的重复告警，节省了大量的网络带宽。

#### 5.3.3 报警语义聚合的有效性

语义聚合后，从76,000 个ASG中最终保留下来了 11,242 个ASG。这说明语义聚合可以进一步消除85.21%的报警

## 6. 局限

当训练期间发生攻击行为是，攻击噪声可能会导致主机模型受到污染

泛化能力差：在客户端的HST模型计算效率较高，但对其他类型的良性行为的泛化能力很有限

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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