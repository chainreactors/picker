---
title: KICS for Networks 5.0中的MLEP：机器学习如何助力追踪工控设备的网络行为
url: https://mp.weixin.qq.com/s/vbxMVkHsfudJ23hGeKB3Gw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:04:05.631167
---

# KICS for Networks 5.0中的MLEP：机器学习如何助力追踪工控设备的网络行为

# KICS for Networks 5.0中的MLEP：机器学习如何助力追踪工控设备的网络行为

卡巴斯基
卡巴斯基

卡巴斯基威胁情报

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXCtic0I4v7y9svolwVGyJouJfuyu3ePW9SDmtYwNsVRPlbE4Cs1A5Ayvqz5t7BI0jSAejccXGwAbibIHxMfe9muVIeUprkwq18Sg/640?wx_fmt=png&from=appmsg)

在工业网络中，恶意活动很难和设备之间的正常数据交互区分开。恶意攻击者常会利用合法工具以及“就地取材”（Living-off-the-Land）技术实施攻击，因此单条网络连接可能不会呈现任何已知攻击特征：设备使用常见协议，传输的也是普通数据。异常行为会隐藏在细微之处：对于某台特定设备而言，数据来源、访问时间或者传输数据量可能是非典型的。但要检测这类异常，就需要清楚连接两端设备的作用，并且掌握它们正常的网络行为模式。

然而企业的资产台账数据往往并不完整，这就增加了及时发现未授权连接的难度。假设监控系统发现一台主机持续和可编程逻辑控制器（PLC）进行数据交互。它的IP地址是已知的，但资产台账没有标注它的用途：它是工程工作站、过程数据服务器，还是外包厂商的设备？这台主机也有可能早已接入工业网络，在网络升级之后，对应的台账信息就已经过时。

在美国网络安全与基础设施安全局（CISA）及其合作方2025年联合发布的运营技术（OT）资产清点指南中，设备清点以及按用途对设备分类，属于运营技术资产管理的组成部分。对企业来说，这是重中之重：根据SANS 2025年工业控制系统（ICS）安全调研，50%的受访者在过去12个月内部署或大幅扩充了工业控制系统资产清点与可视性工具，54%的受访者将这类工具列为未来12至24个月的重点投入方向。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5DBHibIELyXAxCN6A5TCCJWahmTce11ovzERh7nypmRNqwvrkgd1ib48SbTqqrG5glBqxcN5zUH9sFtmT2M4R6ehFicPXNDFMcmJw91WiajqksI/640?wx_fmt=jpeg&from=appmsg)

**卡巴斯基工业网络安全软件中的设备清单**

在卡巴斯基工业网络安全软件中，资产发现技术是资产可视性的基础。被动网络流量分析能够检测设备及其交互行为，而识别规则有助于判定设备类型，并提取设备相关可用信息，例如厂商、型号或软件版本。系统具体可以获取哪些属性，取决于所监测的协议与流量。我们在卡巴斯基工业网络安全大会上对此进行了更为详细的讲解。

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXCsgQsiadGrjRKLV4QIENImghAErt6aAPJG2FvJhWFiaF3IILsHtQONVe9jjy30KvZibzvyt5qbCVS1kDibA7Uh19n9STct2wYYzGA/640?wx_fmt=png&from=appmsg)

**设备卡片中的硬件与软件信息**

该产品还支持主动轮询模块（APM）：在允许轮询的场景下，这些模块可向设备请求额外的配置信息与固件版本详情。这类资产清单远比IP地址列表详实得多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXDELnFy68mvSZibHOhHODk8IWI0I8KebHic5MhzGAicbG10oDicLpAiaMjcibV4qq3gKwTI2jZLt5OrlRfABJrg4s8E6q8KcvCeVtsZA/640?wx_fmt=png&from=appmsg)

**已安装模块及其在PLC机架中的布置**

然而，即便硬件信息准确，也未必总能说明一台主机在特定工业设施中承担何种功能。信息缺口的出现有多种原因：部分设备仅在启动或配置阶段发送标识信息，还有一些设备极少进行通信；专有协议并非总能被解析，加密传输可能仅留下连接元数据可供分析；如果监控系统无法接收工业网络每个网段的流量，部分网络活动就无法被监测；主动轮询也并不适用于所有设备或全部运行工况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXBJ8s7IHWgKdd3xvicUg5EibR1GGTBibib8WQbfZJKS0HEwE4xL8FGDToZu9qbrLP1EYmQEf4x6DTWgfD7r1gKMgdD48CwZsPIGEw4/640?wx_fmt=png&from=appmsg)

**未知类别的设备**

当缺少设备的足够直接信息时，可通过分析其反复出现的网络交互模式来细化设备类别。对这些交互行为进行分析，是机器学习事件处理器（MLEP）的功能，该组件是卡巴斯基工业网络安全5.0内置的一项服务。这款基于机器学习的事件处理器既可以细化设备类别，也能够检测设备网络行为中的异常情况。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5DBHibIELyXCj36s9ibJLwT9BbBUnsMwzUgwJsIU1RMHCdRGa5jFC0O3PExJnD6bI0G8hHERkfmx5M5QkwMJqIEKpd1hATWUg7ASWsPtPiaEqM/640?wx_fmt=jpeg&from=appmsg)

**MLEP分析哪些数据？**

为对比设备行为，无需将每个数据包作为独立观测项（数据对象）存入机器学习模型。MLEP将网络会话表示为一系列时长15秒的短片段。针对每个片段，MLEP存储端点信息（IP地址、MAC地址、端口）、数据交互方向、协议类型，以及传输数据包的数量与大小。这些信息共同构成一个事件，并附上时间戳。如此一来，流量就转化为一串事件序列，能够体现一台设备与哪些主机通信、通信发生的时间，以及通信强度的变化情况。

将数据聚合为事件，同时也带来了该方法的局限性。聚合后的片段无法还原单个数据包的准确顺序，也无法还原指令内容。只有当KICS的另一项技术已经识别出某一新协议时，MLEP才能针对该协议得出分析结论。尽管如此，对比稳定的网络连接以及交互流量的变化，并不需要留存每一个数据包的详细记录。这类观测结果构成了设备的行为历史。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5DBHibIELyXAXnsJom34ibrloaguvr3m5E6dnEH4LYJ3GP5XcWzib56gmicWZu5UIjibau2U75Mf7GNHWvVtiap8EQsv9ibK0tg7Mp2iaBhYepicibTAg/640?wx_fmt=jpeg&from=appmsg)

**从观测结果到MLEP输出**

每个对象都有自身独有的行为历史，一个对象的历史记录无法套用在其他对象上。但行为分析的原理以及部分通用规则，可适用于各类不同对象。

      下面我们来看在基于脉冲神经语义网络（NSN）搭建的MLEP中，这套机制是如何运行的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5DBHibIELyXCnG51AL1eT1SKB2gl6qc9c36OHo9JQCTl0iaduwU21bbbIRh6KsHaxcAz1KV7HkYTiatPHHFou7ucAkF5OFv3QO2KibxVFQg7ZFs/640?wx_fmt=jpeg&from=appmsg)

**事件识别**

神经语义网络将信息构造成多层有序图结构，每一层的数据都基于上一层的数据构建。该图的节点，也就是每一层中的信息单元，起到神经元的作用。神经语义网络会创建专用通道，用来处理不同的事件参数（端口、IP地址等）。每个通道独有的参数值以神经元形式存储在第0层。由一组参数值构成的事件本身，作为神经元存储在网络的第1层。如果某个事件首次出现，神经生成机制会新建一个神经元，并建立指向对应参数神经元的输入连接。这使得网络能够一边学习事件流，一边对事件流进行处理。如果该事件之前已经出现过，网络就会激活该事件首次出现时创建的同一个神经元。通过这种方式，网络可以精准识别每一个事件。每个对应事件的神经元还会收集基础统计信息：上次激活时间以及激活总次数。

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXAjVNUibUW2dicIerNUTS4EHepP5CdRFGnjswhZ7aYwSosGt6yd9dMfZ3adGJOj8tdseW18dUW7ia4IbuKoOAR6ubkY96LlBIJ6QE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5DBHibIELyXBWe8BY6yFf1wAbqZ6DHKicbIeicvcG9egf5iayoWqPyRTy3Glr2UWZCiap9k5x86zkIf8CIEbN71frZZworOxdPuratQS7mRSBjFY/640?wx_fmt=jpeg&from=appmsg)

**事件历史**

在基于NSN的事件处理中，第2层及以上层级会按时间存储事件序列：包括重复出现的模式与完整历史记录。不过，分类与统计异常检测并不需要存储完整报文序列或是每一条网络事件的详细时间线。正如前文所述，事件本身已是聚合结果，这意味着网络报文的先后顺序已经做了平均化处理。因此MLEP仅在每个片段内临时保存历史（默认30000条聚合事件），以此节约计算资源。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5DBHibIELyXAzQibicQTJdUXiaZdoW5EWeTzh4OlPUfPvQgDxx0IhPTRrPiaGhrFicic33iaxwGgvbKpib7ny0sYWbmw4JPn89g2vGudZaAOHiaYBmBFs/640?wx_fmt=jpeg&from=appmsg)

**MLEP的统计处理**

MLEP主要依靠网络-1层（负一层）上专用的监听神经元完成统计处理，注意力头与监控器均构建在这类神经元之上。

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXBFgwRjx28ib8PITtEbiaGTDeicTNrQibbdKuXblgDvN6TY0kFImALz5KAtyADrUPOqxmMuwlhicp1ClicfnaAB7FTY0xciaT6yicPsUzM/640?wx_fmt=png&from=appmsg)

**国家物资编号的主要组成部分**

当事件到来时，对应的神经元会被激活，网络能够立刻识别该神经元是新增的还是此前已经创建的。每个注意力头订阅自身所需的事件或事件特征，仅接收匹配神经元的激活信号。如果某个事件首次出现，所有注意力头都会收到通知，随后自行决定是否订阅（建立与相关神经元的连接），并从该时刻起接收这类神经元的激活信息。

它被称为脉冲网络，原因在于激活信息是脉冲信号，而非数值。该脉冲信号用于告知注意力头：它所关注的事件已经发生。

注意力头根据场景进行配置，场景指的是MLEP需要发出告警的各类情形。注意力头配置的核心是查询语句，它用来过滤流入信息，同时作为订阅判定标准。和常规数据库查询不同，该查询在数据流上持续运行，因此可以对事件做出即时响应。

注意力头的工作逻辑和人类日常语言的语义十分相似。一条查询包含关注主体（一个或多个语法主语）以及条件（句子的其余成分）。在工业企业的基础设施中，主体就是网络内的设备，条件则是网络通信的各类属性，例如端口、协议、平均数据包大小。如果一个注意力头包含多个关注主体（例如它需要关注工业网络里的全部设备），就会进行分支展开：为关注主体的每一个取值，也就是每一台设备，分别生成一个子注意力头。子注意力头负责监控指定设备，并向父注意力头上报信息。

注意力头不会累积数据，也不做统计运算，仅对事件流进行过滤。当注意力头收到匹配的事件时就会激活，并向订阅该注意力头的监控器发送脉冲信号。

而监控器配有堆栈，用于累积和处理事件，监控器也可以配置独立的查询语句，对来自注意力头的信息做二次过滤。例如，监控器可以只挑选经过注意力头过滤后的新增事件。

**监控分为以下几种类型：**

。

统计监控：跟踪特定事件（例如设备活动）在其典型时间间隔内的平均计数变化，或是数值型事件参数的平均值变化（例如设备流量的变动）。

。

基于单事件触发的监控：仅依靠事件本身判断，当事件在指定时间区间内达到指定发生次数，或是首次发生时触发告警。

。

相似行为监控：依托可对事件做泛化处理的检测模块，也就是仅提取少量参数，这些参数的组合能够在大量事件中实现共用（泛化匹配）。

**MLEP使用这些监控类型来实现设备分类以及异常行为检测场景：**

1. 分类方面，MLEP借助注意力头与监控器识别不同资产间的共性行为，并据此对设备分组。随后MLEP从资产发现模块获取部分资产的已知分类信息，并将这些分类拓展至同一分组内的其他资产。由于一台设备可能呈现多种不同活动行为，因此它可能被归入多个分组。MLEP会综合所有相关分组开展加权评估。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXCAIyz3Hbtp6e2NFAr7xgEiariaicxwzobBzhvIxDtkLurozW2LE7RibTkTficric3lcx54zIQSgF1zg99wIGegibbIEpaFvSiaho6hFVc/640?wx_fmt=png&from=appmsg)

**网络行为相似的设备组**

在最后阶段，系统会验证将该类别分配给资产是允许的。这项操作同样由系统启动时加载至NSN中的专用规则监视器执行。这些规则依赖资产发现模块与APM提供的资产元数据。

2.MLEP采用类似的方式进行异常检测：由注意力头和监视器定义一个异常场景，通常定义较为宽泛。当监视器在该场景下触发时，MLEP会生成异常行为告警。

当前版本的MLEP自带预配置的注意力头与监视器。

下方的功能动态示意图展示了工业网络中设备产生的事件是如何被处理的。

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXAudwzeC18gPaHC6YMhX4zGHhLrMOUo3mqXvj1FXho9tunIZod1icuptWibAS2RXvHwHWtkqvy1yiaJR65EkwHSk62YjHHGOgwNmI/640?wx_fmt=png&from=appmsg)

**事件处理流程（点击播放）**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5DBHibIELyXAm12KMwWpr2gSPcv5IkrKiaMZcLiawKxL8WJuwxFaPicykYGhZWwV1ETGGSLuIJYHVBNt83DxcXeyjK37Jv2gesLeWriakcPsggCY/640?wx_fmt=jpeg&from=appmsg)

**MLEP实践应用：依托行为特征完善资产清单**

在拥有多条相似产线的厂区内，不同产线的设备信息完整度可能存在差异。某条产线上的设备可识别为PLC（可编程逻辑控制器），而另一条产线完成升级后，部分主机仅能识别出地址：现有流量数据不足以判定其设备类型。但这些设备会和同类人机界面（HMI）、过程数据采集服务器通信，通信方向、通信频次与数据流量大小也相近。

这正是MLEP的作用所在。它利用已知资产的类型信息，将已知资产网络行为的重复特征，和未分类设备的行为特征进行比对。当观测到的交互行为特征相似时，MLEP就可以在资产清单中为该主机补充设备类型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXC9PZUial48656RgrClaLjFTFTd3QQqqdjDwVC9nY9IrKdzsuenqvT7CnKeC2HJTnenJMOYVg9hNymwHmPps8ayKd95gjyCgz6g/640?wx_fmt=png&from=appmsg)

**MLEP建议的设备类别**

一旦类别完成细化，工业网络图能够提供更多关于网络内设备的背景信息。在分析网络活动时，分析人员可以直接看到设备的推荐类别，无需在设计图纸中逐一查询每个IP地址。这种方式在设备更新速度快于文档更新速度的场景下尤为实用。

系统还会对照现有设备信息和预设约束条件校验推荐类别，以此筛除部分相互矛盾的选项，但预测效果依旧取决于可观测流量的多少，当设备通信频次很低时，该影响会更加明显。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXCicMBYeo87Fhria7R4uYHiaQ8z7SF8w20p5xcPzaKZZ0y5tQnxXic5wXb6G6bxEpzz73bYq9cxZkxhMevX9OFfaufdhcKNyhJQRtk/640?wx_fmt=png&from=appmsg)

**异常活动与流传输统计数据**

对真实攻击事件的调查表明，攻击者会主动使用标准工具以及合规协议。要识别潜在恶意活动，并非总是需要预先掌握攻击者的具体技术。基于特征的检测能够发现已知攻击标识，但无法评估观测到的交互行为对于某台特定设备而言是否属于常态。MLEP会将当前活动与该设备的常规网络基线进行比对：包括它通信的主机、使用的协议、数据传输的时间与传输量、平均数据包大小等。它所检测到的异常变化能够为调查工作指明方向。将这些变化与其他事件以及运行环境信息关联分析，有助于判断其背后是否存在恶意行为。在调查已发现的安全事件时，异常信息可以帮助还原攻击行为序列。

**MLEP 的首个版本内置了六项预配置监控项，分别对应设备网络基线的六类异常偏离情况：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXBB77s8uiclMPdKTYicEmjzatd1MicKCHHQqUtwBj4SPN4ffIyc8bhfhYWicraJssicbIUicVEaAkKibmtnD6juKNduSLoBkLWwa8rRbw/640?wx_fmt=png&from=appmsg)

在调查过程中，异常信息有助于还原变化序列：特定主机何时建立新连接、切换协议、增大数据传输量，或是改变运行时段。按照设备和时间匹配事件，能够让分析人员看清已检测到的安全事件周边活动的发展过程。

当攻击者的部分操作不在监控范围内，或是没有触发其他KICS技术时，该方法尤为实用。将这些变化与设备角色、协议分析数据以及其他技术上报的事件关联起来，分析人员就能得到更完整的时间线。行为异常...