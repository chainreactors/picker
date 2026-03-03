---
title: 论文研读与思考|用于机器人检测的多属性异构图卷积网络
url: https://mp.weixin.qq.com/s/Ck6AouqrT5zlSnPzGhEt8A
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:06:37.381062
---

# 论文研读与思考|用于机器人检测的多属性异构图卷积网络

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIzKE7Fkdun5icjesvEDJFnGjv1It1E1t5adSezTc2V6ZrRS74ScRrNaLibcuvKWeGDG25JjXia3nGK7vPjjNyMrjBNJctnVS3KibQU/0?wx_fmt=jpeg)

# 论文研读与思考|用于机器人检测的多属性异构图卷积网络

Yuan
Yuan

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

**原文标题：Multi-Attributed Heterogeneous Graph Convolutional Network for Bot Detection**

原文作者：Jun Zhao, Xudong Liu, Qiben Yan, Bo Li, Minglai Shao, Hao Peng

期刊：Information Sciences

DOI：https://doi.org/10.1016/j.ins.2020.03.113

# **一、主要研究问题、目标和方法**

## **1.1****核心研究问题和研究动机**

僵尸网络（Botnet）是当前网络空间安全领域最具破坏力的攻击形式之一，传统依赖流特征或静态规则的检测系统逐渐失效。

机器人检测是追踪和减轻互联网网络威胁的一项关键任务。论文旨在解决当前机器人检测系统的两个主要局限性：

Flow-based 方法的局限：只分析单条网络流（source IP、destination IP、port 等），忽略僵尸节点之间的结构依赖，无法捕获全局行为模式且对未知攻击泛化能力差。本质问题将“群体行为”的攻击问题，转化为“孤立样本分类问题”处理。

Graph-based 方法的局限：多为同质图（只有 IP 作为节点），依赖特定社区结构或子图模式，无法表达多类型实体之间的语义关系，规则依赖严重，适应性差。本质问题缺乏对细粒度异构交互行为的建模能力。

核心研究问题：

1.如何构建能够表达细粒度网络对象及其交互行为的图模型？

2.如何度量不同主机在复杂语义路径下的相似性？

3.如何在标注样本有限的情况下实现高精度检测？

这三个问题分别对应图建模、相似性计算与半监督学习三个技术层面。

## **1.2****论文提出的关键方法、模型或理论框架**

1.问题定义：基于AHGCN的僵尸检测（Bot Detection Based on AHGCN）

给定一个多属性异构信息网络（AHIN）G = {V ,E,A}，以及元路径集合MP = (P1,⋯,Pi)和元图集合MG = (M1,⋯,Mj)

基于AHGCN的僵尸检测任务包括以下四个步骤：

①主机相似度建模：将图中每一个源 IP 视为一个主机（host）。

基于元路径（MP）和元图（MG）度量任意两个主机之间的相似度，从而分别构建两个主机之间的加权同构图：基于元路径得到的加权邻接矩阵AM和基于元图得到的加权邻接矩阵AG

②主机特征矩阵构建

将主机的属性信息映射到潜在向量空间，构建主机的特征矩阵X，这里，X表示主机属性的表示矩阵（文中称为主机属性的邻接矩阵），用于后续图卷积操作。

③图卷积特征提取

分别在两个加权图上执行图卷积操作：GCN(AM,X) 和GCN(AG,X)

通过图卷积传播结构与属性信息，学习更加具有判别力的僵尸行为特征表示。

④前馈神经网络分类

将图卷积得到的嵌入特征输入前馈神经网络（forward network），训练分类模型，实现僵尸主机检测。

其中：V，E，A分别表示异构图中的节点集合、边集合和属性集合；

X为主机属性特征矩阵；AM，AG分别为基于元路径和元图构建的主机加权邻接矩阵；GCN（·）表示图卷积操作；Pi表示一个具体的元路径实例；Mj表示一个具体的元图实例。

2.AHIN 构建思路

为刻画更细粒度的网络流对象以及僵尸网络之间的行为交互关系，作者构建了一个包含多种对象类型与关系类型的异构信息网络。核心节点类型包括：Source IP（源 IP）Destination IP（目的 IP）Protocol（协议）Port（端口）Request（请求）Response（响应），围绕这些对象，论文定义了 10 类关系，用邻接矩阵形式表示：

①以Source IP为核心的关系（R1–R6）

R1：Source IP – Destination IP

构建源IP与目的IP的邻接矩阵M。若Mi,j=1，表示源IP i访问了目的IP j。

R2：Source IP – Protocol

构建源IP与协议之间的关系矩阵R。若Ri,j=1，表示源IP i使用了协议j。

R3：Source IP – Port

定义源IP与端口之间的矩阵S。若Si,j=1，表示源IP i使用了端口j。

R4：Source IP – Request

构建源IP与请求之间的矩阵C。若Ci,j=1，表示源IP i 发送了请求j。

R5：Source IP – Response

构建源IP与响应之间的矩阵M。若Mi,j=1，表示源IP i接收了响应j。

R6：Protocol – Port

构建协议与端口之间的邻接矩阵P。若Pi,j=1，表示协议i使用端口j进行通信。

②以 Destination IP 为核心的关系（R7–R10）

类似于 R2–R5 的建模方式，作者进一步构建了目的IP 与以下对象之间的语义关系：

Destination IP – Protocol；Destination IP – Port；Destination IP – Request；Destination IP – Response；这四类关系记为 R7–R10。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIwoSncUyRzH99uWRxgHKEKShgCdc89ZqeUUj8nUPgfIAZ7ZbW95LBzKT1grzw4av4jtLSz2WMhu10geWBI801fdPHficGk6Gc4M/640?wx_fmt=jpeg&from=appmsg)

3.基于权重学习的相似度嵌入对于机器人检测任务

目标是通过分析构建的 AHIN 中所有主机（每个单独的源 IP 被视为一个主机）的恶意机器人在属性和行为模式方面的相似性。整体思路分为两部分：1）基于元路径的相似度建模；2）基于元图的高阶语义相似度建模。

①基于元路径的主机相似度嵌入

如果两个主机通过大量“重要的”元路径实例相连，则它们更可能属于同一类别（同为恶意或同为正常）。则相似度由两部分决定：语义重叠程度（共享元路径数量）；语义广度（各自的总路径数量，用于归一化）

给定对称元路径集合：![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIyHbN3m4ELSOyX4F0UGdHrXWmnvoeCpXa2AndbyYtthcsNshhuz59BxMIUODfEZDAiccSmJoBpMQtYpYTh1YVpYOpQLJY3icMxV8/640?wx_fmt=jpeg&from=appmsg)

任意两个主机的元路径相似度定义为：

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzBSS3Zyu24RCYorhDCF5TO7MmbWOgv45IVt6cGw7Cd5KV2rHR7BKlCwFWPD3YtBesvdCAR0r8A4ibVhaUOGFxrp0QSPLxibWLqc/640?wx_fmt=png&from=appmsg)

其中：分子：两个主机之间的元路径实例数量（语义重叠）

分母：两者自身路径数量之和（语义广度归一化）

Wm：元路径权重（可训练参数）

M‘：元路径数量

4.成对随机游走

给定一个对称元路径p，若该路径可以分解为两个长度相同的子路径：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIz2VTIZV8apIB5yPrthszdFaFJnHImdtHibYZdQZGyOdbia32oyYZcRNlyGVAtwUA1eZzjbA2Cqc2q7a1OyrHlqBRApY5LWLMs1U/640?wx_fmt=png&from=appmsg)

则定义成对随机游走概率![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxicnaXrItWgnDHbXVkqghdQSqtRMrunomcSYShS8xS2hCWZgibia1R2GyyqEV6JLO2gRAMg2ah8DYrChOlekricaBDrWoPWibNbRN4/640?wx_fmt=png&from=appmsg)

从节点x和节点y同时出发，沿着对应的子路径随机游走，并最终到达同一连接节点的概率。

5.元图Meta-graph

下图定义了七类对称元图：M1~M7，这些元图从高阶语义角度刻画主机之间的交互行为模式。

例M1表达的语义是：两个主机同时共用相同协议，并且发送相同请求。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIxzD0Exsh3qEHp8yfEFib11sPACY4aCgIgwemWPJw6sc3tOwBsuvLlBkO8jve71340KGgfKcOxu3zUvuPEuQRqLpCtFgibNB7BQg/640?wx_fmt=jpeg&from=appmsg)

元图S是一个有向无环图，具有单个源节点ns和单个目标节点nt，定义在具有模式TG = (A,R)的AHIN G = (V,E,A)上。形式上，元图定义为MG=(VS,ES,AS,ns,nt)，

这比单一元路径表达能力更强，能够揭示僵尸网络中常见的协同行为模式，例如：统一使用特定协议；发送相同类型的控制指令；体现集中控制特征。因此元图特别适合刻画僵尸网络中的群体协同攻击模式。

6.CouMG

CouMG：给定AHIN G = {V,E,A}，以及元图集MG = (M1,M2,⋯,ML+1)，CouMG 是一个计数函数，用于记录满足CouMGM(vi,vj) = CMG 的元图实例的数量其中

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIxv7IEIEZZqTOp7qNZGxwDVo3Qk7ZLsRNQ8mCQlDynQZic4o0Yp7KXbdqPhEJVFoQJasO0pjIFO4n0PqAoSVt2utoalZ1XGLAHU/640?wx_fmt=jpeg&from=appmsg)并且
是元图M下类型Ak和Ak+1之间的邻接矩阵。

7.基于元图的主机相似性嵌入

给定元图集合![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIz0KnR1oHxAa7ic2j4AhHgLoLL7W7gt1sCRibcuRuUbfDp4hnPr3iauhl4adRPdND5bfgCOcPDkQF8q28YFpUzs9xSqqopVxlOnas/640?wx_fmt=jpeg&from=appmsg)

任意两个主机ℎi和ℎj之间的基于元图的相似度可以定义为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxq6IuYIHRACUsxfHRK8ko6Q1EjJHAWOYZZDOLZgoXhSY3k3nra2k9AEp0Nfsf48IpUSakJbI4vcjia9qXFNgKnwrd3MI5qG8Ss/640?wx_fmt=png&from=appmsg)

对于元路径，若路径为![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIy36TX8iaAYCY1ra2Pe7lqtw3FicHWdicUNmEahUQtVJwo8p57Z2h2XOCrsBVn6d60icX18hgnf2y73gKxE6Hl0yicuicEal8OibQPJ4Y/640?wx_fmt=png&from=appmsg)交换矩阵Cp = WA1A2⋅ WA2A3 ,⋯,WAlAl+1

引入Hadamard积捕捉联通元路径之间的高阶语义，以下算法展示了上图中元图M5的交换矩阵的计算原理

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIxFXbI3R4upQb0Vic6y3JIHrmfXFwf5plCLoUMhuWJib6jQg4Uc2ShXSXrR0JiaDIScZ0gOZlfVNIMZibfu0AeqibXQ6J0nBsFxlYTY/640?wx_fmt=jpeg&from=appmsg)

8.基于图卷积网络（GCN）的僵尸网络检测

现有僵尸网络检测方法存在两个问题：1.强依赖大量标注数据 —— 现实中僵尸流量样本有限；2.忽略图结构本质 —— 僵尸网络本质上是图结构组织的控制网络。

因此：1.将网络流建模为多属性异构图；2.将僵尸检测转化为图上的半监督节点分类问题；3.仅需少量标注样本即可训练模型。

元路径相似图AM，![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzLDb7GNyfMNZIPyOu0Q3ibTPhSzevw1sjvfEhbFc23LicuagQD5fiaOKtxgiaNgB1a403fhdWcSibuqu52UAUOskTW0dwL9J02nMAA/640?wx_fmt=png&from=appmsg)表示基于元路径的主机相似度。

元图相似图AG，![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzWxxicK179Njk6HXScrTic1EkvQLldk98aiaAx2FSE3VE2lLtJj3Qt7Ng7A1IibVhj2FphbV05YR2EsXFCoeuKkY3HJYXGhlQicliaY/640?wx_fmt=png&from=appmsg)表示基于元图的高阶语义相似度。

AM 捕捉局部行为相似性；AG 捕捉复杂群体交互模式；

为了融合节点属性信息，使用Word2Vec训练主机特征表示：![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIy3jib1j1J096DLaFq9SHATwCZCBaQNmjg3ZV0IzvDwTiahTloo09XrSTIGiavpxicbeLEa0ylrCJdx9c84to7wiatvzib67aicEyHicaw/640?wx_fmt=png&from=appmsg)

N：主机数量；d：特征维度

GCN层级传播规则

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIyEursbQBAG0nfoiaaJDqVDwibcU42mkPrjRMogLYibUa96vjhNPc4lRR7pw8wmqPqxgSPQdCKneL1ujoAdm7suLYzWyraP1E5jts/640?wx_fmt=png&from=appmsg)

基于AM的GCN，该步骤学习基于一阶语义的特征表示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIziajtMfGmic48W5EmoKC0bMwzhtMa6XVkulLy3x6Yv1weqaTAfYtNgaeGPJlzKYSQABZ0sb3r34pDJ1w4gzT5xVPmW4rQvg49ibw/640?wx_fmt=png&from=appmsg)

基于AG的GCN，该步骤学习高阶语义行为特征。![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzkpeDSjicxQ5CGd3qw983LqtXnlMVuNV53c2MJ7SuR6lFDXe87dXlHSkjJDttZ4EmYvPIBAanP7ia0qFlZJOOyKBN6QbcSkhzgk/640?wx_fmt=png&from=appmsg)

最终预测：![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIwibibkkOvtpO2S20Oicc6ia4U67fAWibV7FNvG2AyB6F9BFDqxvHicHRa50VbhnhtuYXvU3R0K09CwOoXwsA6SiaG0bp43WLobxoppH0/640?wx_fmt=jpeg&from=appmsg)，α为可训练系数

损失函数采用交叉熵损失函数：![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIwnDkfIhNQ9NxZpAgIU9Ua899riawHlu8wIFHSZBLicAf09BKgYANJcic0QFnWMtRjfTvzC0UcIVMicY77d1jgZvXFU8wxVlKGWGn8/640?wx_fmt=jpeg&from=appmsg)

Bot-AHGCN 的完整流程闭环为：

AHIN构建→相似度嵌入（AM / AG）→双GCN学习→融合预测→端到端优化。

## **1.3****这些方法如何解决研究问题。**

AHIN的构建解决了无法建模多类型实体的问题，原路径可以表达高阶语义，半监督GCN和将网络流建模为多属性异构图解决了样本有限和泛化能力不足的问题。

# **二、论文的主要发现、结论及创新点是什么？**

## **2.1****论文的核心结果与主要发现**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIyhic8xMf4Ymuk8iam2YicibUAFQWTMJkGPaZgibJPpcL8OdGtM0KFoWia9LGQmKl9F9Tl08IhwVjY0qAeuGicD996xeYcjpCYsicKP3NI/640?wx_fmt=jpeg&from=appmsg)

不同元路径与元图在Precision与Micro-F1指标上表现差异明显，元图整体优于元路径且权重大于元路径，包含Request和Protocol的结构权重更高。

在 CTU-13 与 Honeypot 数据集上：

Bot-AHGCN 达到：Precision：99%+；Micro-F1：98%+

相比基线方法提升：相比 Bot-SVM 提升 13%；相比 Graph-ML 提升 5%；相比 HAN 提升 5%，其meta-graph M6 表现最佳。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIzpswricHnXeXTh83BZNc485QHEYn4VlnS4AKQbywqbEYnpfCsQ5ZapWWPzIlI1DXOs8z7Z4FicJcttzDZOnqOy...