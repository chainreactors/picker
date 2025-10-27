---
title: 一种基于网络流量风险数据聚类的APT攻击溯源方法
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247534906&idx=1&sn=f94b394de09372ce2a451479e827b7a8&chksm=fa93fffbcde476edd1af0051ac4762200a42147466e203e0ba9611c0474e122d02fb4f8477c8&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-02-25
fetch_date: 2025-10-04T08:04:54.175436
---

# 一种基于网络流量风险数据聚类的APT攻击溯源方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176moltN6pDACpaVffQkr6gEBTg9E09Qvm44R2dqrnDLjVXHcGCvtoEQQqy5otWDXGsIsvAWLYQXGEw/0?wx_fmt=jpeg)

# 一种基于网络流量风险数据聚类的APT攻击溯源方法

网络安全应急技术国家工程中心

以下文章来源于信息安全与通信保密杂志社
，作者Cismag

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM57SpaEcnib8NMGibzYLk6p0uOuGZThgJsy6XBtuoV6SmKQ/0)

**信息安全与通信保密杂志社**
.

网络强国建设的思想库、安全产业发展的情报站、创新企业腾飞的动力源

**摘要：**当今世界正值百年未有之大变局，网络空间成为继陆、海、空、天之后的第五大疆域，安全威胁也随之延伸至网络空间。没有网络安全就没有国家安全，在新时代网络空间安全已经上升至国家安全的高度。高级持续性威胁(Advanced Persistent Threat，APT)攻击是网络空间中威胁最大的一种攻击，其危害性大、隐蔽性强、持续时间长。考虑到APT攻击的溯源一直是网络空间攻防中极为重要的一环，提出了一种基于网络流量风险数据聚类的APT攻击溯源方法。首先介绍了所提方法的工作流程，其次对流程中的风险数据聚类算法进行了详细介绍，最后通过实验验证了所提方法的有效性。

高级持续性威胁(Advanced Persistent Threat，APT)攻击是指攻击者使用多种先进手段，对特定目标展开的持续的、高威胁性的网络攻击活动，它有3个重要特征：(1)攻击能力强，这体现了APT中的A(既先进性)这一方面；(2)持续时间长，这体现了APT中的P(即持续性)这一方面；(3)目标特定，危害程度大，这体现了APT中T(即威胁性)这一方面。这种攻击活动的发起者往往具有较强的政治背景，攻击活动具有极强的隐蔽性和针对性，而攻击活动的受害者也往往要承受巨大的损失。

根据奇安信发布的《全球高级持续性威胁(APT)2021年度报告》披露的数据，2021年度全球APT攻击的主要目标包括政府、医疗、科技、国防、制造、运输、教育、航空、通信、能源等社会生活的方方面面。攻击手段也有从传统的鱼叉攻击向大量利用0day漏洞发展的趋势。此外，针对基础设施及供应链攻击的事件愈发泛滥，甚至有越来越多的针对网络安全产品的攻击活动，APT攻击的发生频率和威胁程度呈持续扩大的态势。

APT攻击不仅危害性大，而且隐蔽性强。2022年2月23日，奇安盘古实验室发布报告，发现隶属于美国国安局的“方程式”组织利用顶级后门，对中国等45个国家开展了长达十几年的名为“电幕行动”的网络攻击，攻击目标所属的行业涵盖了电信、大学、科研、经济、军事等。

我国是APT攻击的最大受害国之一。长期以来，“海莲花”“蔓灵花”“虎木槿”“方程式”等APT组织对我国进行了持续性的网络攻击，使相关领域遭受了极大的损失。而且，针对政府、国防、能源、金融等重点行业的攻击频率在最近几年都有100%以上的涨幅，个别行业甚至有200%以上的涨幅。

APT攻击的溯源一直都是网络空间攻防中极为重要的一环。做好溯源工作不仅能使相关部门掌握APT攻击的活动规律，做好应对与防范，有效减少损失，还能使我国在面对敌对势力在网络安全问题上的舆论攻击的时候，拿出确凿的证据进行有力的反驳，有效维护国家尊严。

# **1、传统的 APT 攻击溯源方法**

**1.1　基于日志记录的溯源**

在常见的网络攻击活动中，典型的攻击过程如图1所示。攻击者通过多个中间节点(路由器)，连接到受害者的主机，或者把攻击载荷投送到受害者的主机上。在这个过程中，攻击者到受害者之间的每个节点都会留下日志记录。攻击发生后，追踪者根据掌握到的攻击数据包特征，与获取到的各个路由节点的日志记录进行匹配，如果匹配成功，则可断定攻击的数据流经过这一节点。如此一级一级地追踪，直至发现真正的攻击者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77hhlKMQdjXtNiaCrC6hqw4BGDiaZHfniccTT8ZP15Okq3xqqTL8Pf4Dxwg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

这种溯源的方法可以看作对攻击过程的一种逆向追踪，但使用这种方法进行溯源具有如下困难：

(1)需要获取并存储大量中间路由节点的日志数据，而这往往需要使用行政手段得到网络运营商(Internet Service Provider，ISP)的支持，对于一般的企业或单位来说具有较大的难度。

(2)中间环节易中断。跟踪者往往无法获取到境外运营商的路由节点日志数据，对于来自境外的网络攻击，追踪链就会中断。而一旦追踪链中断，往往会导致前期的追踪工作前功尽弃。

(3)如今的网络攻击大量使用僵尸网络，即使费尽周折找到了发起攻击的IP，最终也往往是僵尸网络，还是难以确定攻击者的身份。

综合以上原因，这种溯源的方式在面对有组织的APT攻击的时候成功率会大大降低，而成本则会大大增加。

**1.2　基于包标记技术的溯源**

所谓的包标记是指在网络节点(如路由器)中以特定的概率对通过的数据包进行标记，并将路径信息标记在IP数据包的预留字段中。在受害者接收到数据包后，通过解析其中的标记信息，即可重构数据包的路径。包标记过程如图2所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77Un6nVchct8G8rO9HB0DwbRpSKicMVOWadEnia64ck3VpQM507P7F8ichA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

使用包标记技术进行溯源，无须再存储海量的中间节点产生的日志数据，然而还是需要运营商对中间节点进行特殊的改造和设置。同时，上文所述的基于日志数据的溯源方法中存在的中间环节易中断且无法对使用僵尸网络的攻击者进行溯源的问题依然存在。

**1.3　基于主动感知数据的溯源方法**

为了解决以上两种方法的数据获取难的问题，陈周国等人提出了一种基于主动感知数据的溯源技术框架，其架构如图3所示。在此方法中，网络感知是基础，可以通过拓扑主动发现、网络扫描和渗透等多种主动感知技术进行信息获取。追踪溯源模块则对感知到的数据进行分析处理，重构数据传输路径，并将结果与感知及策略管理模块进行交互，以动态调整系统运行策略和感知内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvZSrdFUBtAic9icDclMDYibcRfqBMAHZKDibcC6wpxaYibTibovdMFyuwZhAaPmamxicHeSiaib6faKzrP7VQ/640?wx_fmt=jpeg)

# **２、基于网络流量风险数据的溯源方法**

**2.1　溯源框架**

在上述溯源方法中，溯源过程需要巨大的人力成本。在面对愈发频繁和复杂的APT攻击的情况下，这种溯源方式的效率日益低下。近几年，基于流量还原的网络空间态势感知技术不断发展，相关产品也已在市场上取得了不错的反响。通过对流量还原数据的分析和挖掘，可以发现网络流量中的攻击行为，并将其作为风险数据存储到单独的风险数据库中。本文基于这些挖掘出的风险数据，提出了一种 APT 攻击溯源的新思路。其整体框架和溯源流程分别如图 4、图 5 所示。

APT攻击溯源的最终目的是定位到发起攻击的组织或个人。APT组织往往都与特定的政治实体有关联，在一段时间内具有较为固定的攻击目标、武器库、漏洞库等，这些特征就可以成为确定一个组织的不同的维度。因此，溯源的过程可以分解成确定这些特征维度的过程。确定了维度之后，再与已有的APT组织情报库进行匹配，就可以定位到某个具体的组织。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77FJwFNzR4rgP5iayPYTlGRCNvU3GRkvvkSH4LzmDpT11LDua6qtMp0Vg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77yhn8fIuyaUooUVtJmJWJ3WMJeBcm7GkykBq2icwvaUGXNPne4KUNCfA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在图5所示的溯源流程中，先基于风险数据进行聚类分析，把具有相似特征的多种类型的风险数据聚合在一起；然后再基于这些聚类的结果进行维度分析，得到APT组织的攻击目标、时区、语言等维度的数据；最后基于分析得到的各个维度的结果，与APT组织情报库中的组织特征进行匹配，确定该组织是否是某个已知的APT组织，或者是一个未知的组织。

本文重点研究在此方法中对风险数据进行聚类的过程。

**2.2　聚类算法模型**

**2.2.1　定义**

定义1：聚类(P)。把一批风险数据划分成不同的数据集的过程。

定义2：线索(C)。一条风险数据就是一个线索，如一封钓鱼邮件、一个木马样本等。

定义3：维度(D)。为方便对数据进行数学表示，而对数据进行拆分描述的不同的侧面。

定义4：元素(E)。从风险数据中提取出来的各个维度的值。

定义5：线索集(S)。一批风险数据的集合。线索与元素的关系如图6所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77YjsCa95sToQ5NAY598icxQDwwn7JxG7giaLmpibicmWpiaQEN8UMaT2dxTw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**2.2.2　数学模型**

根据以上定义，整个聚类的过程如图7所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77gwChic1sI5s3u8azpedhMkfz6ia52NnaJkJAiaN2vYwdOIs83cGVg2HVg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在图7中，![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77RkTAbCkXNHXAFz9W2jYib2NJFclV0eJqCpT0QXaVAsRaAa1MfvWRvDQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)表示风险数据库中的一批线索的集合，![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77bUQ3KO6F2qGdziczSpBD8CicAMUBdrphFRpx16uMmL8q0YwadEAl9wibg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)表示聚类的过程，![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77KMLONbf8mMxaBKeCRibTBl9QIOGTD0wlP3JSBpYu1oI0460KARNWAibg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)表示聚类得到的线索集，其中，![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77QHWUYw1pzHTgdGHUc4duicG3WMhsAicn2Kg6QVZeFS02IQt1UTWKzWicw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)。

**2.2.3　聚类算法**

在本算法中，前置条件是需要有一批可以进行维度拆分的网络流量风险数据。首先对数据的各个维度进行特征提取，然后转换得到每个维度的元素值与线索集的映射。若用![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77ibkuLHEdH7DjwxGInoenXyTpQ6ReT4B3YcBTFj60VoLnb3lcSkIm0IA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)表示此映射中任意一个键值对的key，![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77U6sqsMLLZtzyp5Lwfsj7XsgS7nAxVHPj6Qj3xuMlTWKdX5N9yEM5PQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)表示映射中任意一个键值对的value，则此键值对的含义就是![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77jwxjQ3kuUGs3OntkweZ8GoeCSic88SlbTd9l8YFNiaVIstYl0WuLte3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)中的每一条线索都可以在维度![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77V0BpZoV6ExNew4mp10hZk7IwbtQae2AloHODSqe4DN9nIg3LribD6Wg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)上提取出相同的元素值![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77ibkuLHEdH7DjwxGInoenXyTpQ6ReT4B3YcBTFj60VoLnb3lcSkIm0IA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)。

得到以上映射之后，把映射中所有键值对中的值两两之间取交集，得到多个新的线索集。这些新的线索集中的线索，彼此之间都有至少2个维度的元素值是相同的。然后在这些取交集得到的结果线索集中，过滤出线索数量超过阈值的线索集，作为后续聚类操作的聚类中心。

对每一个聚类中心的线索进行特征提取，然后针对原始线索集中不在任何一个聚类中心的线索，分别计算其与每一个聚类中心的归属度。归属度的具体算法：聚类中心在每个维度上的所有元素值都与线索对应维度的元素值计算相似度，如果有多个值，就对计算出来的相似度求和，即得到在此维度上的分数；然后把各个纬度的分数按照对应维度的权重计算加权平均值，得到一个线索归属于某个聚类中心的归属度。得到任意一个不在聚类中心的线索归属于任意一个聚类中心的归属度后，把线索加入到归属度超过阈值且分数最高的聚类中心。在此过程中，每个聚类中心又吸收到了与之归属度超过阈值且分数最高的线索。

最后计算不同的聚类中心两两之间的相似度。相似度的具体算法：首先，对两个聚类中心在同一维度的元素值计算彼此之间的相似度，如果有多个值，就把多个值求和，得到的结果即为在此维度上的分数；其次，把各个纬度的分数按照对应维度的权重计算加权平均值，就得到两个聚类中心的相似度。求得所有聚类中心两两之间的相似度之后，把相似度分数超过阈值的两个聚类中心进行合并，从而得到最终的聚类结果。

上述聚类算法的过程可以用如下的数学方法进行描述：

步骤1：如图8所示，遍历线索集![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77JHfuvgkqK3ib6RxLibBNNzYTev9wVX8hYfA0sFmBD133M2ugibKFycGibA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)，对于每一条线索![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM770HTwJbJSHWnorNwDaufANQeiafMfcMlR9y5M7jgta0uhd0JDvxbSWZg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)，提取维度特征![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77a1VH35QbDlcp15yPYicE6JFEWZh7kemfDpwwLgaeoPUDZVnXrdL6GJg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)，得到线索对应特征向量的映射![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77IdANPbltXucMkvSOTibH9WQbL8niaFx9hw4equoCMqicxqicjv3ktodsXg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77ib6mNzMSiascmtSOYaAWXQuWJFxgLIEB1lsMI9456ricTGGyIVl6CZxFA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

步骤2：如图9所示，转换映射![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBx81WkcffD14mKZicVicYjM77IdANPbltXucMkvSOTibH9WQbL8niaFx9hw...