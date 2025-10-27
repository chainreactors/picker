---
title: 特拉维夫大学 | FlowPic：一种通用的加密流量分类与应用识别表示方法
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491689&idx=1&sn=17687d1be26ab151a1e6d49e00a734e0&chksm=fe2d1fe2c95a96f4eddee949c7d9d669df8708caae70eb5e9a9a18eecf15d90eca0995d9c83a&scene=58&subscene=0#rd
source: 安全学术圈
date: 2025-02-19
fetch_date: 2025-10-06T20:47:33.557279
---

# 特拉维夫大学 | FlowPic：一种通用的加密流量分类与应用识别表示方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZfFD2HD0TZykDDt4l6BjyMzY662eXHYxXibd6jdy3JRqeb4Ewv1wgceA/0?wx_fmt=jpeg)

# 特拉维夫大学 | FlowPic：一种通用的加密流量分类与应用识别表示方法

原创

孙汉林@安全学术

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZlqtoibMlWgOeFiaePfet1700KwM9KoGyicVAMvJvxyousxW8PCssFxGOA/640?wx_fmt=png&from=appmsg)
> *原文标题：FlowPic: A Generic Representation for Encrypted Traffic Classification and Applications Identification*
> *原文作者：Tal Shapira and Yuval Shavitt*
> *原文链接：https://ieeexplore.ieee.org/abstract/document/9395707*
> *发表期刊：IEEE Transactions on Network and Service Management*
> *笔记作者：孙汉林@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、引言

本文提出了一种新颖的加密流量分类和应用识别方法。与传统依赖于手工提取特征的方法不同，该方法通过将流量数据转换为图像（FlowPic），然后使用卷积神经网络（CNN）来识别流量类别（如浏览、聊天、视频等）和应用程序。该方法省去了手工提取特征的繁琐步骤。实验结果表明，即使在没有额外训练的情况下，该方法也能成功识别未参与训练的新应用程序，提高了流量识别的灵活性和扩展性。

### 2、数据集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZUhJXTHKpNIzKuXLTXdCAQUnIn55GtpOezuVP5iceibLK4GjLibq7JEPTQ/640?wx_fmt=png&from=appmsg)

本文使用UNB提供的 ISCX-VPN 和 ISCX-Tor 数据集，以及自建的 TAU 数据集来构建最终数据集。数据集涵盖VoIP、视频、文件传输、聊天和浏览五种类型的流量，包含非VPN、VPN和Tor三种加密方式，并将流量表示为基于5元组（源IP，源端口，目的IP，目的端口，协议）的单向流。

为了增加训练集样本数量并减少过拟合，作者将每个单向流拆分成等长的数据块。在实验中，每个会话被分割为60秒的区块，并采用45秒的重叠窗口（即相邻区块的起点相差15秒），这种方法类似于目标检测中的滑动窗口技术。例如，10分钟的VoIP通话可以被分为10个不重叠区块（600/60=10）或37个重叠区块((600-(60-15))/15=37)，每个区块都略有不同。需要注意的是，数据增强在训练集和测试集划分之后，这样是为了确保同一会话的区块不会同时出现在训练集和测试集中。

### 3、构建FlowPic

FlowPic 的构建过程分两步：

* 从每个流中提取数据，记录每个数据包的 `{IP 包大小, 到达时间}` 对，并将相同流量类别和加密方式的记录合并。
* 构建基于流的二维直方图，将X轴设为数据包到达时间，Y轴设为数据包大小，并限制Y轴范围为 1-1500 字节（去除超过以太网MTU的包）。X轴则通过归一化将 60 秒映射到 0-1500。

将所有归一化的数据点填充到 1500×1500 的直方图中，直方图的每个单元格代表特定的时间间隔和数据包大小。最终，每个直方图作为 FlowPic 存储，并用于模型输入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZRQD5F3lYJFCtOlPICdw3PoAJtBiaVnSNtuU8sgLarIB5Oicro0OGiaheQ/640?wx_fmt=png&from=appmsg)

不同应用的流量行为差异明显，如上图所示，Netflix 的视频流量包大小固定，而 Skype、Facebook 和 Google Hangout 的流量包大小分布较广。此外，视频流不仅包含视频数据，还包含音频流（类似 VoIP）和用于协调控制的小包流量（类似聊天流量），如在Skype上，视频流和音频流之间存在明显的分离情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZ2ZmXQt9FicJZBwGUXkToHqzevZLrkVtXvcwwPWcI1UBqgibOpcEwSKYA/640?wx_fmt=png&from=appmsg)

不同的加密技术也会影响流量特征，如上图所示，普通聊天流量由少量小包组成，而 VPN 会将多个流合并，Tor 则会将所有流量整合为一个大的加密数据包。此外，Tor 采用分组加密，这导致数据包大小呈离散分布，而非 VPN 流量的数据包大小则较为多样，分布更广。

这些特性表明，FlowPic 能够捕捉复杂的流量模式，且适合用于深度学习模型训练，从而提升流量分类的准确性和泛化能力。

### 4、构建卷积神经网络

本文采用 LeNet-5 [1] 风格的架构进行多种互联网流量分类任务，并针对所有子问题保持相同结构。网络包含七层（不含输入层），具体结构如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZNx5xjUHT5sXbR1cYOQNWafO9BwsZhEXt0VjPnGdgjvwibOy64DnVVLQ/640?wx_fmt=png&from=appmsg)

### 5、实验结果

由于原始数据集存在类别不均衡问题，本文使用随机欠采样方法构建平衡数据集，以确保分类器评估的可靠性。分类任务有如下两种：

1. **多分类（Multiclass）**

* 流量分类（Traffic Categorization）：识别网络流量所属的类别（如Web浏览、视频流、VoIP等）。包含三种加密方式（非VPN、VPN、Tor）的流量数据。并且创建了一个合并数据集，用于研究加密方式是否影响流量分类。重点在于流量类别的分类。
* 加密方式分类（Multiclass Encryption Techniques）：区分流量的加密方式，即判断某个流量是非VPN、VPN 还是 Tor。每个加密方式的流量包含所有的互联网流量类别（例如，Web浏览、视频、VoIP等）。重点在于区分加密技术。
* 应用识别（Application Identification）：识别具体的VoIP和视频应用（如Skype、YouTube等）。非VPN情况下，数据集包含10种VoIP和视频应用。VPN和Tor情况下，各包含5种VoIP和视频应用。重点在于区分具体的应用程序。

2. **二分类（Class vs. All）**

* 针对每个流量类别，构建一个数据集，使目标类别与所有其他类别的数据量相等，并保持其他类别间的比例一致。Class vs. All 是一个二分类任务。

具体实验结果如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZaFVy5kR0aKbVHrVnXD3bgLcq3DrrgwAJsqibQbHgNRyLepVYCd8uZicQ/640?wx_fmt=png&from=appmsg)

与其他机器学习方法结果的对比：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEia0hj4qHia82Gjae7flxsyZWNuoF4AMFZob4bLRQibR6xU3FIojaUqklaM4492FKcPC2b3F3QIxFtw/640?wx_fmt=png&from=appmsg)

### References

[1] LeCun, Yann, et al. "Gradient-based learning applied to document recognition." Proceedings of the IEEE 86.11 (1998): 2278-2324.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

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