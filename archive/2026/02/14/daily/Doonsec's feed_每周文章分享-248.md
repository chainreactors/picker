---
title: 每周文章分享-248
url: https://mp.weixin.qq.com/s/cse672EeaGfxLSjTvaoa2w
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:15:51.958774
---

# 每周文章分享-248

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp2m1rrf02iazTZGRfjGkQeMiaktPwdY1fWOgDs55BBgVZmgcEot417uHZ60cT4arHgZa4ORa7FVla0hlZNsiabgjZwUrdnnoJ8Wmc/0?wx_fmt=jpeg)

# 每周文章分享-248

网络与安全实验室

![]()

在小说阅读器中沉浸阅读

每周文章分享

2026.02.09至2026.02.15

**标题:**Intelligent Routing in Directional Ad Hoc Networks Through Predictive Directional Heat Map From Spatio-Temporal Deep Learning

**期刊:**IEEE Transactions on Mobile Computing, vol. 23, no. 4, pp. 2639-2656, April 2024.

**作者:**Zhe Chu, Fei Hu, Elizabeth Bentley, Sunil Kumar.

**分享人:** 河海大学——王凌宇

01  研究背景

传统的路由方案主要追求最短路径，一种典型的方案是发送方会根据网络的拓扑结构运行迪杰斯特拉最短路径算法，通过最短路径传输数据，然而这种方案忽视了网络中的流量分布特征。一些路由方案关注网络的能耗问题，因为无线传感器网络中节点能量有限且不易补充，这些路由协议专门针对能量受限的网络如无线传感器网络进行设计。针对由汽车、飞机等电池续航能力较强的节点构成的移动自组网，更关注服务质量而非电池寿命，因此路由协议设计可在延迟、吞吐量等方面提出更高要求。本文的动机在于构建一种面向QoS的路由协议，通过综合考量时域和空域的全局网络流量分布特征，当在有建立新路由需要时，主动规避网络中的拥塞。

02  关键技术

本文研究了为配备定向天线的移动自组网构建智能主动路由方案，建立了一个高QoS的路由协议，考虑了时间和空间域内的全局网络流量分布，实现在满足时延要求的同时实现高吞吐量。本文构建的方向热力图（DHM），反映了交通密度分布和来自定向天线的方向信号传播，该模型整合了五类网络拓扑图谱：链路拓扑图、队列拓扑图、流量发送方拓扑图、流量接收方拓扑图以及定向天线感知无线信道拓扑图（DAWC）。最后本文使用增强深度学习实现了方向热力图预测。

该方法的创新和贡献如下：

1）本文提出了方向热力图（DHM）的概念，用于描述整个网络的流量密度分布。在路由搜索过程中，新建立的路径会参考当前活跃流量的分布模式，从而选择流量较轻的区域；

2）本文不采用当前瞬时状态的DHM进行路由决策，而是使用增强型时空深度学习模型（st-DL+）对DHM进行一步预测，能够实现更精确的路由决策。

03  算法介绍

如图1所示，是本文的算法框架，共有三个阶段，首先是构建方向热力图（DHM），方向热力图由五幅图组合形成；接着，网络中不同阶段的DHM被管理节点收集起来，用于预测未来在下一个时段的DHM；最后，网络中的节点可以根据预测的DHM快照，避开拥堵，寻找合适的路由路径。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2g8SjVv4EGZwOHUU9q7fsDIrafLxVSOlLGl6QUgsPL4bPnwCLwFiaXw2OqqfWkywvv896beiazq43gPxovQvpEZCpFsmw6flzBI/640?wx_fmt=png&from=appmsg)

图1 基于方向热力图的路由协议框架

**（1）方向热力图模型**

方向热力图（DHM）模型，是由链路图、发送与接收节点信号图、排队图以及定向天线感知无线信号图（DAWC）这五幅图组成的，它将真实世界的网络建模为像素网格中的图像。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2bJ7j2mPl59XahUCDGO9ghiaHtR5ZauvYvDHeQ2jPibAC6LKjzibpm5iakyk9AzC6zQ1s8epoBOonGRTaB0FPYiarcicalCU7MMINr4/640?wx_fmt=png&from=appmsg)

图2 链路图示意

如图2所示，是链路图示例。当两节点之间有合适的信噪比（SNR）时，便可以形成链路。图中越接近红色表示链路中的流量速率越高。本文使用以下公式确定链路图中任一位置的值，其中C代表链路容量，即数据传输速率，d\_lk(x,y)表示点(x,y)到链路k的距离，阈值设置为单个像素框的对角线长度，当该距离小于阈值时，就将链路容量乘容量利用率，并加到该位置的数值上。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3XyBx3E8Fhy1ic72L1UZm6DfZ2De1a4XI4TE7c93PIeFZ8ibtJHqQjzffmmURY5Ck0WhonHoBGqp5fenebGvo1sSkb0ic9KNlwFA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2LibMVW1w7ibOHrUqB8Ct1wSthiaCyQCjicG9kFfKGNRQ6PZVIVnTibOEn4TmTOsDM4icFVEibMyo7oAswHbBciaad03d6crWHGXWSLzM/640?wx_fmt=png&from=appmsg)

图3 发送与接收节点信号图

如图3所示，是发送与接收节点信号图示例，分别表示来自发送节点或接收节点的数据流量速率。如下公式中S\_m与R\_n分别表示单个发送或接收节点的数据流量速率，从公式中可以看出，信号的辐射强度随着距离的平方成反比例下降。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2v6ZslnfuHy86BkMy2hxnic4fSwmThCveicYibBzhOnWauSCUqh4RCcuzyAtK8lGlTwO8TZsGexyAEoflX4iczMOm4oa5gRTy99t8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2Zhcib4JJfia5fOsJmmHZtSZ2dCEGtVicrn3uG3oCnm0w7QHIIHfibkOwkZ9WjcMLKicfJhpNmMy0CMFm5NeCDze5LcaSw7Q6gyuhY/640?wx_fmt=png&from=appmsg)

图4 排队图示例

如图4所示，是排队图示例，表示不同节点缓冲区队列中的数据包等待情况，红色表示节点的队列已满。用如下公式表示，其中B代表缓冲区大小，OB表示已使用的缓冲区大小。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1BgOnNpOAypjmNHHKc3ZRPZrhTfzG4bcficbv8gPhE6jVPOYWcqzwL7CHNnFpDb9Yj9Vk9ecH9v9KoKibZBNxhicjcG5C4XAMHoI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0RWKEjc0pCp5L7DW7n2aJx5yUl5MaNqy9StS3oGVBsk2ticKRZOkt8tpuxVUvtVWQxnHYF0icZewnQyA3iaczYXstLoibPxo3RJuo/640?wx_fmt=png&from=appmsg)

图5 DAWC示例

如图5所示，是定向天线感知无线信号图（DAWC）示例，显示了定向天线的属性，包括波束宽度、方向等，以及无线信道的占用情况，反映特定时间和空间位置上的无线信道拥塞程度。图中红色表示无线信道使用量高，用公式表示如下。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0ee1jreNDQnnKL1GIbvaVFDxDvVaemlu88slzL4amX33EZYCr8fuxTQWlq8aTO8OHjfrx6fuQVCbp4DIZosT0cLPZwKgZiaoj0/640?wx_fmt=png&from=appmsg)

建立DHM图后，需要对数据进行归一化。如图6所示，本文将链路信道的占用情况用5个等级来表示，从而将逐像素的精确值估计问题转化为图像的分割与分类问题，降低建模复杂度。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp13PABUoCl2Ku3G0t1E7c3N0Qg9Ag48DB0R5GtIpuFalgY7icbVCl9dFySIlq36GbLOK2pDzGBldZAAduKWib6anVKINb3iaJPWRc/640?wx_fmt=png&from=appmsg)

图6 DHM归一化示例图

**（2）用于DHM预测的增强型时空深度学习**

本文中，增强型时空深度学习（st-DL+）模型采用长、中、短周期采样，能够捕获系统长期、中期、短期的变化特性，从而能够识别高维数据特征。如图7所示，是信号模型在趋势、周期和接近度方面的示例。从图中可以看出，数据呈线性下降、约20秒周期内的中期振荡以及1秒级别的短期波动。因此，本文的时空深度学习模型模型能够捕捉高维数据的特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3Qll03cSN5o1ibIfKibmEnRssdYO1mEdhicbGlOPPibKTzeh5iafRp6AblCGTbV0UQ6tM6tsanxsemUCsc1jMP4OUV5mdBawic2FvyQ/640?wx_fmt=png&from=appmsg)

图7 趋势、周期与接近度示例

如图8所示，是增强型时空深度学习（st-DL+）模型图。该模型能够预测下一时刻的DHM快照，使路由更适应流量分布的动态变化。模型中添加卷积编码器和解码器扩展了传统的基于ResNet的DNN模型。通过增加卷积编码器和解码器网络（CEDN），从历史快照中提取特征图/矩阵，生成方向热力图。在输入层中，本文使用了三个相同的并行ResNet，分别用来处理长、中、短期的快照。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1Bx6G0yFoRXcDV9BheKHemDbfFmBvRiac3tkQEgT0bMcwco6RuEibicGoYVibvDoTGzhE2icnIuJn2euvNBcZu2tHbsgf6qpxbB5yk/640?wx_fmt=png&from=appmsg)

图8 增强型时空深度学习模型图

ResNet由如图9所示的ResNet单元组成，其中，模块中的层归一化有助于对每个分量图中的模块进行归一化，从而平衡权重。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2y3CAJzU0lVS6EyLNOcxWuRGX8AFaOdGWk2MMmbGYIBWxlSbrqLaxKEmL2ee2J91sm4BbWkQP8yAT0VGxianm9yThka5BazXVc/640?wx_fmt=png&from=appmsg)

图9 ResNet单元

本文根据如下公式中交叉熵损失模型计算损失，并使用Adam优化方案实现损失函数最小化，并实现整个训练过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2IsZCyZVItPQ0sicFEH9oYWLQ9gjIu7bUyVj9zj93jJYpBAiaTVW6CEk11XiaZD1cQQCKFA25FbP2WHHFxaaNVGRKsQSTBlzG5h8/640?wx_fmt=png&from=appmsg)

**（3）路由路径选择**

本文使用全局流量地图生成路径，以满足QoS要求，并且单一数据流在拥堵的情况下仍可分流，从而保证数据流的吞吐量。如图10所示，其中包含了两条端到端路径，分别是路径1从节点11到15，路径2从节点6到14。其中，由于链路2经过拥堵区域的边缘。为了保证整条路径流量均衡，本文路由协议将路径2拆分成两个分支，即图中的红色与绿色线路，一个分支沿拥堵区域边缘，另一个分支与路径1存在重合。通过路径的拆分，能够确保不同的数据流均保持高吞吐量，从而实现绕开拥堵区域的路由方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1cF3DiaoDOibt5evHI2eQDNy9Q8gyIHucHAHMMhwFduJicrCHzHpojib9jRVBtdhtMWu3iaNaibOzHwhdCxNWKPO7ocNHs2xMybmIHs/640?wx_fmt=png&from=appmsg)

图10 路径分割示例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1ojP8cQK2X5jajKQJaoqPcLc92I34QAgbiaNdAdo1W3YNCbJbu0WdrCBaWK8ejTXUeVicv7CiapPJw0C6X2Wk2txc6ibToIEKn684/640?wx_fmt=png&from=appmsg)

图11 定向通信网络建模有向图

如图11所示，本文将定向通信网络建模为一个有向图，用公式表示如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3PtPTnFOduWH2E8ccMreXPr07oEQjj1TcXNzYCZnrblfJLLkJk5PKs5656qGOLebZdyM1or6iaib2sTiaYaswQicvTvAMvkSIiaBe0/640?wx_fmt=png&from=appmsg)

本文将链路成本定义为该链路上热力图像素值的平均值，由此可以得到路由路径选择的目标函数如下。根据网络中的流量平衡条件和信道容量约束，可使用修正单纯型法求解优化问题。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0VicNWnhFKqDzJicjiamqUHqcrlblMY3ibmvmVnm4o2Lia8FGzd5lEQLpT8NGzJzdHldibzEIqVJJEj7CIHiaibZVNO9fzXDTSia13NF6c/640?wx_fmt=png&from=appmsg)

04  实验结果分析

**（1）实验设置**

本文中实验参数设置如下表所示。网络的范围大小是4000乘4000米，平均节点间距离是600米，移速是60米每秒，这是一个类似直升机网络的实验场景。本文将路由方案与已有的协议进行对比，其中OLSR能够识别出网络中跳数最少的路径；传统基于QoS的移动自组网路由协议是属于经典的反应式移动自组网路由协议；仅优化模型是为了研究DHM的作用，本文从协议中移除了DHM预测方案，仅保留基于优化模型的路由方案；基于DHM的优化模型，能够选择避免拥堵区域的较短路径，同时避免了多条路径流的交叉。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0hzictefafHDGpxick0TnZPJBYQTRmhRO7OzXqMZJeK1iaicEMQyJvCQ9kkJhL8Q0PtPK7GfYqGk3gfuJWITO5bpIXfnF3jtWmnqg/640?wx_fmt=png&from=appmsg)

**（2）实验结果与性能分析**

如图12、图13所示，是定向天线夹角固定为30度时接收端数据包投递率和端到端延迟的性能表现。其中红色线是本文所提方案。从图中可以看出本文方案数据包投递率最高、延迟最低，是效果较好的。本文在夹角为60度时进行的实验结果与此类似。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3ps0vQM7DSibQ0KS9t1RA7hpwzuicJXlP1XE2xAEJYY1Ol4BfB2TCpDMEOlh135gcoRNC84ABA8hMmAyibeZhOv3TJe6ToNXzcto/640?wx_fmt=png&from=appmsg)

图12 数据包投递率

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1xnLAsiazXlEzNNQ4ibmibkmXvSr0qK0dywjJTA9DibPXd8vV9wDRJ08tyrPYBqAYxSpMpIzuElEcxLLkJcupXbAAX5vT6sY59L2I/640?wx_fmt=png&from=appmsg)

图13 端到端延迟

如下表所示，是对于预测模型的准确性分析。本文将st-DL+模型分别与具有5个和10个单元的ConvLSTM模型进行对比。ConvLSTM模型是一个基于长短期记忆（LSTM）的循环神经网络（RNN）模型，其目标是克服传统LSTM模型中的数据维度限制问题。st-DL+模型具有超过95%的预测精度，准确性更高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0d7uoXNRBibnu5cCUZ4ZpyZwoch7TBiaOTq81wIxkTZXgoXQ0RC9icMGHcOUfITm59vpHYyvC1B3k0RHicWMxTSVs5upmvRXeOKkM/640?wx_fmt=png&from=appmsg)

本文为了验证定向天线波束宽度对路由协议的影响，如图14、图15所示，分别展示了不同天线宽度下网络的平均吞吐量与延迟表现，其中绿色柱状代表本文所提方案，可以看出，本文方案吞吐量更高、延迟更低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2N4r0FtLwTIcyb2sd3qiaibWUqZ3Ao05SDchic8aNDs9WGZFY1Ud61pricTZddXqXdhndc7SvhKVo5GZL0sd80iaMiaGP28UnzewGWA/640?wx_fmt=png&from=appmsg)

图14 不同天线宽度下网络的平均吞吐量

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0jx1lYkR5dNNdHv9FfkJjBFLSyNbaHWuTEoqlL9xfUBsLVSXwyveG817icqX3...