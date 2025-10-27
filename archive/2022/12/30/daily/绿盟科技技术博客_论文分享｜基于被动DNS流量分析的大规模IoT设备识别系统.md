---
title: 论文分享｜基于被动DNS流量分析的大规模IoT设备识别系统
url: http://blog.nsfocus.net/dns/
source: 绿盟科技技术博客
date: 2022-12-30
fetch_date: 2025-10-04T02:44:50.843913
---

# 论文分享｜基于被动DNS流量分析的大规模IoT设备识别系统

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 论文分享｜基于被动DNS流量分析的大规模IoT设备识别系统

### 论文分享｜基于被动DNS流量分析的大规模IoT设备识别系统

[2022-12-29](https://blog.nsfocus.net/dns/ "论文分享｜基于被动DNS流量分析的大规模IoT设备识别系统")[杨双镇](https://blog.nsfocus.net/author/yangshuangzhen/ "View all posts by 杨双镇")[IoT](https://blog.nsfocus.net/tag/iot/), [被动流量识别](https://blog.nsfocus.net/tag/%E8%A2%AB%E5%8A%A8%E6%B5%81%E9%87%8F%E8%AF%86%E5%88%AB/)

阅读： 1,088

## ****一、引言****

随着智能家居的普及，物联网设备的数量也在增加。但是，由于物联网设备的开发商和供应商往往会忽略基本的安全机制，导致越来越多大规模网络攻击事件都与物联网设备有关。这不仅危及用户的安全，也给互联网带来了极大的安全威胁。目前，网络空间测绘系统使用主动探测技术来扫描整个IPv4空间，并通过获取banner或其他指纹来识别网络服务和暴露的物联网设备。然而，这种主动探测技术无法识别隐藏在NAT防火墙设备之后的IoT设备，同时，当IoT设备被分配到IPv6地址时，主动探测也面临挑战。

本文介绍一篇来自IEEE European Symposium on Security and Privacy（EuroS&P）的会议论文《IoTFinder: Efficient Large-Scale Identification of IoT Devices via Passive DNS Traffic Analysis》，该论文解决了上述问题，作者设计了一种用于可大规模被动识别设备的IoTFinder系统，通过对分布式被动DNS进行数据收集，可识别位于NAT（或其他中间设备，如防火墙）之后或分配IPv6地址的IoT设备。接着，使用基于机器学习的系统准确识别各种各样的IoT设备类型及其设备型号。

## ****二、IoTFinder系统设计****

**2.1 系统概述**

如图1，作者设计了一个大型物联网实验室，包括多个语音助手、摄像头、体温计等53个来自不同厂商的活跃物联网设备。通过收集智能设备的DNS流量，包括每个设备发送和接收的所有流量作为数据集。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_98a96681-db66-4825-b9f5-c0c0b65ae221-300x188.png)

图1 IoT流量收集设置

如图2所示，表示24小时内的部分IoT设备查询域名情况，横轴为时间，纵轴表示每个IoT设备查询的域名，圆点表示DNS查询的次数。可以看出，不同于单一域名，物联网设备发出的DNS查询的域名组合和相关频率往往会有特定的频率。基于该发现，作者建立一组可区分行为指纹，该指纹可以识别不同的物联网设备型号，且与客户端的DNS行为匹配时不太可能触发大量误报。因此，利用上述发现构建了可以自动学习的基于DNS的IoT指纹的系统，而不需要对设备可能查询的域名格式进行转换来生成过滤规则，从而减少误报。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_42ab37c4-552f-48db-b9d3-1af45ddce0a7-300x276.png)

图2 24小时内的IoT设备的域名查询情况

IoTFinder系统如图3所示，作者提出了一种将IoT设备识别与文档检索相似的方法，即将IoT设备的DNS行为转换为TF-IDF特征向量表示，然后计算IoT设备与普通设备之间的相似性（例如余弦相似度）。通过这种方法，可以检索出与已知设备相似的IoT设备。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_4736cf9b-6394-420b-8144-b7c451a30cad-300x92.png)

图3 基于DNS请求日志的IoT指纹学习与匹配技术

**2.2 基于DNS的IoT指纹学习**

通过分析某一段时间内IoT设备的DNS查询来对设备进行识别。为了对IoT设备进行建模，将T(l)划分为长度为w的不重叠的时间窗口，则时间窗口个数N(w)表示为

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_df699d09-5ce6-4839-adfa-44d7d9e8d076-300x98.png)

IoT设备在T(l)时间内查询m(k)个不同域名q(kj)的查询次数Q(k)表示为

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_21379c5a-b86a-40d7-8859-be8b6d628f60-300x61.png)

IoT设备Q(k)查询的域名q(kj)在任意长度w的时间窗口内至少查询一次的概率p(kj)表示为：

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_bc9ac978-181b-4321-bfa0-eff1320a6920-300x127.png)

那么，IoT设备Q(k)的统计指纹则可以表示为：

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_62bbf8e5-1c93-443e-9a32-299a08e64b41-300x65.png)

时间离散化过程是一种将时间划分为离散间隔或“窗口”的方法，用来解决IoT设备之间查询频率的变化。这一点很重要，因为物联网设备的查询频率可能会受到其位置或所连接的网络基础设施等因素的影响。通过将时间划分为窗口，可以比较不同物联网设备的查询频率，更好地近似它们的真实行为。

IoT设备查询的每个域名的逆文档频率(IDF)用于评估每个域名在全球DNS查询中“流行度”，定义如下：

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_8d9322c9-0d83-490b-94a8-bb58d66abf6a-300x35.png)

其中，N(c)表示在T(p)时间内至少查询一个IoT域名的总的客户端数量。IDF越高，说明域名在所有客户端中越不常见，其特异性就越高，表示更有机会匹配到一个IoT设备，可用于提高物联网指纹匹配的准确性。

最后，在学习阶段可获得IoT的统计指纹如下：IoT域名查询频率、用于计算P(k)的时间窗口w，每个域名的IDF以及每个设备的最大容忍误报率φ计算的检测阈值θ。

**2.3 基于DNS的IoT指纹匹配**

作者通过IoT设备的统计指纹P(k)与客户端C(i)在时间窗T(t)中收集的DNS流量进行匹

配，进而实现基于DNS流量的IoT指纹匹配，分为以下3个步骤。

1. 计算指纹在时间T(k)内IoT设备Q(k)的TF-IDF向量ψ(k)，公式如下

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_b8304983-dc98-4bb5-949b-d5efc3577f82-300x47.png)

2. 计算客户端C(i)的TF-IDF向量。假定C(i)在T(t)时间内查询不同域名d(ij)及其发生频率f(ij)，则客户端C(i)的TF-IDF向量表示为

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_6bf1fa44-44f9-46f9-985a-4b847fb42f53-300x51.png)

3. 计算IoT设备的TF-IDF与客户端C(i)之间的相似性s(ψ(k),Γ(i))，这里使用余弦相似度，表示为

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_08d8881a-305d-4f8a-a8e5-7235286db5c1-300x50.png)

其中，Γ(i)为C(i)映射到ψ(k)的向量空间得到新的TF-IDF向量，计算如下

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_7b5eb50e-f3c0-4902-81e8-d73f933d427a-300x52.png)

在得到两个跨度相同的向量空间ψ(k)和Γ(i)，如果匹配值s(ψ(k),Γ(i))大于等于阈值θ(k)，则C(i)的DNS数据行为与IoT设备Q(k)匹配。

## ****三、IoTFinder系统评估****

**3.1 数据集介绍**

实验用了4个不同的数据集，包括IoTDNS、PDNS、LDNS和PIoTDNS，数据集在不同

时间收集，用于训练和测试统计物联网指纹，简要介绍如下：

1. IoTDNS（IoTLab Trace Dataset）：IoTDNS数据集包含由53个不同的活跃物联网设备生成的DNS流量，如图1所示。
2. PDNS（Passive DNS Traces）:PDNS数据集包含了从一个美国的大型互联网服务提供商（ISP）获取的匿名的被动DNS跟踪数据，该数据集能够查看散布在美国地区超过4000万台互联网连接设备（包括物联网设备）每天发出的域名查询。该数据集用于野外通用设备中的查询频率（IDF计算），并估计每个学习到的统计指纹的物联网设备的总体。
3. LDNS（Labeled DNS Traces）：LDNS数据集包含了从一个美国的大型大学校园网络中获取的带标签的被动DNS跟踪数据，包含了超过54000台通用非物联网设备的日常数据，平均计数分布如表1所示。

表1 非物联网设备每日平均计数

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_2eed3b88-f592-4aea-96a0-254a3d3555c9-300x37.png)

4. TPIoTDNS（Third-Party IoT Device Traffic）：TPIoTDNS数据集包含由第三方实体收集的网络跟踪数据。

**3.2 设备指纹学习评估**

作者通过分析DNS查询来学习IoT设备的特征指纹，并评估了每个设备指纹在识别未来的流量时的性能。如图4所示，通过计算和分析每个设备分类器的ROC曲线下面积，来表示每个设备指纹的性能，图中给出20个不同训练集和测试集的pAUC分布，蓝色方块为pAUC中位数，该方法的平均pAUC达到了99.9%，远高于其他方法的平均水平，这表明该方法在识别IoT设备方面更加准确。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_e214e247-5c18-42d9-a83d-437c6120a124-300x118.png)

图4 设备指纹准确性评估

**3.3 NAT环境中IoT设备的指纹检测评估**

实验评估了当IoT设备的流量与来自其他设备的混合流量时，学习得到设备指纹检测 IoT设备的能力。通过模拟一个有NAT的网络环境，其中有100多台设备共享同一个IP地址。然后，将经过训练的物联网指纹与该模拟流量进行匹配，并测量正确检测到的设备数量以及误报和漏报的数量。结果表明，即使在这种具有挑战性的情况下，对于52台物联网设备，指纹能够检测出中的多达40台，并且没有误报。这证明了该方法在真实网络环境中检测物联网设备的有效性。

**3.4 第三方IoT设备的检测评估**

针对第三方数据集TPIoTDNS数据集，实验用IoTFinder检测第三方数据集中的物联网

设备，通过对比实验数据，研究人员发现除了一个苹果电视盒，IoTFinder准确地检测到了其他所有的IoT设备。研究人员进一步调查了这个问题，发现在混合的IoT和非IoT流量中，有些设备更难检测到，这可能是模型没有匹配到苹果电视盒的原因。实验结果表明，IoTFinder在检测IoT设备方面表现出色，除了在混合流量中检测到某些设备困难的情况。

**3.5 IoTFinder检测效率评估**

图5展示了在某个美国大型互联网服务提供商的DNS流量上部署IoTFinder工具后匹配模型的前20个最受欢迎的设备的分布。实验结果表明，使用基于Apache Spark的实现可以提高IoTFinder的效率，并能够快速匹配IoT指纹。通过这种设置，指纹在超过4000万ISP客户的DNS流量上部署需要大约72分钟。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/企业微信截图_564b8694-b331-4960-80e6-5a2f5ceb2471-300x216.png)

图5 某个美国ISP网络上的IoT设备分布（Top 20）

## ****四、总结****

本文介绍了IoTFinde系统，一个用于大规模被动识别IoT设备的高效检测系统。它利用分布式被动DNS数据收集和基于机器学习的方法，能够准确识别大量不同类型的IoT设备。但是，由于DNS的缓存效果可能会压缩设备的查询频率，所以IoTFinder系统无法识别一个域名系统后有多少相同的设备，而对于主动探测来说，往往很容易得到。因此，在越来越多的IoT设备暴露下，主被动探测结合往往是资产探测的更好 的方式。

### 参考文献

[1] Perdisci R, Papastergiou T, Alrawi O, et al. Iotfinder: Efficient large-scale identification of iot devices via passive dns traffic analysis[C]//2020 IEEE European Symposium on Security and Privacy (EuroS&P). IEEE Computer Society, 2020: 474-489.

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/aptconfuciuspakistanibo/)

[Next](https://blog.nsfocus.net/spade/)

### Meet The Author

杨双镇

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)