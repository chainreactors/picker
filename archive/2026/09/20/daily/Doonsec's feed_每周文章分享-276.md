---
title: 每周文章分享-276
url: https://mp.weixin.qq.com/s/SPjH4fK4sCGGifzf6POuiA
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:24:04.101248
---

# 每周文章分享-276

# 每周文章分享-276

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.09.14至2026.09.20

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**MTRF: Multidomain Transformation Representation for Network Flows in Network Intrusion Detection

**期刊:**IEEE Transactions on Dependable and Secure Computing, Vol. 23, No. 3, May/June 2026

**作者:**Weili Wu.Xinlei Wang, Mingshu He, Xiaojuan Wang and Shize Guo

**分享人:**河海大学——龚子忱

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

随着移物联网设备持续增长，使网络攻击面不断扩大。传统入侵检测系统通常依赖云端部署和大规模标注数据：一方面，将网络流量上传至云端会带来检测时延与隐私泄露风险；另一方面，真实网络中的攻击样本稀缺且类别分布高度不平衡，深度模型容易过拟合，轻量机器学习模型又依赖人工特征工程，难以适应新的攻击模式。

雾计算将检测能力下沉至靠近终端的网络边缘，可降低通信时延并减少原始数据外传。然而，雾节点资源有限，需要一种既能利用少量标注样本、又能为终端侧轻量分类器提供高质量特征的表征模型。网络传输中的丢包、延迟、重传和乱序还会在时域引入噪声，而相对稳定的频域特征能够反映流量的周期性与稳定模式。如何联合利用两类信息，同时避免跨域特征相互干扰，是本文关注的核心问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文提出网络流多域变换表征模型 MTRF，将表征学习与下游分类任务解耦。模型以原始数据包头为输入，不依赖明文载荷和手工特征选择；训练阶段在云端利用少量网络流学习通用编码器，推理阶段将编码器部署于雾节点，对流量进行低维表征，再将结果交给 IoT 设备上的 ET、RF、DT 或 XGBoost 等轻量分类器完成检测。

该方法的创新和贡献如下：

1）多域解耦表征：分别学习网络流的时域趋势/短期波动与频域周期/稳定模式，降低时域传输噪声对频域表征的干扰。

2）面向网络环境的数据增强：模拟丢包、重传、延迟与乱序等网络诱导现象，将训练样本扩充为原来的 8 倍，提高模型对不同网络条件的鲁棒性。

3）双分支对比学习：时域分支采用基于动量编码器和动态队列的自监督对比学习；频域分支引入傅里叶变换、监督对比学习和硬间隔惩罚，增强少数类的类间可分性。

4）少样本与跨数据集泛化：设计五类由易到难的平衡/不平衡、多分类/二分类任务，并验证已训练模型对未知类别及未知数据集的迁移能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

**（1）框架设计**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp09LQAibVdDssYmxYwONscOYxrPsdJUlA5387B6mq7eqGr2wNNibCCCCVVlyaTY63sk4M5dibZIibxoKPaTjCUxQSUQ0e7BwfzGxDs/640?wx_fmt=png&from=appmsg)

传统网络入侵检测方法通常直接将网络流量输入分类模型进行攻击识别，但这种端到端学习方式容易受到网络环境变化以及数据噪声的影响。同时，在物联网（IoT）场景下，由于隐私保护要求，大规模标注网络流量数据往往难以获取，导致模型在少样本、类别不平衡场景下面临泛化能力不足的问题。

针对上述挑战，论文提出了一种多域转换表示学习框架（Multidomain Transformation Representation for Network Flows, MTRF）。该方法的核心思想是：

先学习网络流量中具有泛化能力的特征表示，再利用轻量级分类器完成入侵检测。

MTRF 不直接进行攻击分类，而是通过时间域（Temporal Domain）和频率域（Frequency Domain）两个不同视角对网络流量进行特征建模，分别捕获流量变化趋势以及周期性规律，从而获得更加稳定、鲁棒的网络流量表示。论文提出该框架主要用于部署在雾节点（Fog Node）上的轻量化入侵检测场景，将复杂的特征提取过程放在计算资源较强的节点完成，再将低维表示传输给 IoT 设备进行快速检测。

整个框架可以概括为以下几个重要部分：

1)网络流量预处理与表示转换：每轮在输入模型之前，MTRF 首先对原始网络流量进行结构化处理。论文从 pcap 文件中提取具有相同五元组（源 IP、目的 IP、源端口、目的端口、协议）的网络流，作为一个完整 Flow。假设一个 Flow 包含 N 个数据包，每个数据包提取前 M 个字节，则该网络流可以表示为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp245mDyZGkmnJeBtaibVETA7Q1vj7lPaWLlRiaAWRNwgRBH67QnY4p8B4XkhKrOFtDgJNIAVIl4D3CXkubZBib8hnF4R81e7U9R1I/640?wx_fmt=png&from=appmsg)

2)网络环境扰动增强机制：在真实网络环境中，网络流量往往会受到复杂网络条件的影响，例如数据包丢失、重复传输、传输顺序变化等情况。这些网络环境因素会导致同一种攻击行为产生不同形式的流量表现，使模型难以学习到真正具有区分性的攻击特征。为了提升模型对于复杂网络环境的适应能力，MTRF 引入了网络环境扰动增强机制（Network-induced Transformation）。该方法通过模拟真实网络中的常见传输异常，对原始网络流量进行多样化变换，使模型能够在训练过程中接触不同环境下的流量变化，从而学习更加稳定、鲁棒的网络流量表示。

3)时间域表示学习模块： 网络流量本质上是一种具有时间变化特征的数据，例如数据包的发送顺序、传输间隔以及流量变化趋势等，都包含攻击行为的重要信息。然而，在真实网络环境中，数据包可能受到延迟、丢失、重传等因素影响，使时间序列特征容易受到噪声干扰。针对这一问题，MTRF 设计了时间域表示学习模块（TGCN），主要用于捕获网络流量在时间维度上的动态变化规律。该模块采用基于 Momentum Contrast（MoCo） 的对比学习方法，通过构造同一网络流量在不同网络扰动环境下的样本作为正样本，使模型学习到在不同传输条件下仍保持稳定的流量特征。同时，通过引入负样本约束，使不同类型流量在特征空间中保持更明显的区分。

4)频率域表示学习模块： 除了时间变化规律外，网络流量中还存在一些周期性和稳定性特征，例如某些扫描攻击、异常通信行为可能会表现出固定的数据传输频率。为了进一步挖掘这些隐藏规律，MTRF 引入了频率域表示学习模块（GFCN）。该模块通过傅里叶变换（Fourier Transform）将网络流量从时间空间转换到频率空间，分析不同频率成分中包含的信息，从而提取网络流量中的周期模式和稳定特征。

**（2）Hard Margin监督对比学习**

在网络入侵检测任务中，一个重要挑战是类别不平衡问题（Class Imbalance）。例如，在真实 IoT 网络环境中：正常流量可能占绝大多数； 某些攻击类型样本数量较少； 少数攻击类别往往更加难以被模型识别。 传统监督对比学习（Supervised Contrastive Learning）虽然能够利用类别标签信息，将同类别样本拉近、不同类别样本推远，但它通常默认：不同类别样本之间应该保持相同程度的分离距离。然而在实际网络流量中，不同攻击类别之间的难度并不相同。某些攻击类型之间特征差异明显，而另一些攻击类型可能具有非常相似的通信模式，导致它们在特征空间中距离较近，容易出现误分类问题。因此，MTRF 在频率域表示学习模块（GFCN）中引入了 Hard Margin监督对比学习（Hard Margin Supervised Contrastive Learning），通过增加类别边界约束，使模型重点关注那些难以区分的负样本，提高少数类别攻击的表示能力。相应的损失函数如下：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3WWfvm0lpMXpNoiavGku3Am6P7tTMmFALVVj0ic3fDdpBpmyrtgE9Iia3C2ribCicpzKu5qYfs8eEpliaGlqBue0DPhY4HfAJiaIib8ibk/640?wx_fmt=png&from=appmsg)

其中，L\_f为频率域对比学习损失，N\_neg为负样本数，N\_f为负样本之间的相似度矩阵γ为Hard Margin控制参数γ为调整因子。这个公式的核心作用在于当不同类别样本之间相似度过高时，提高损失权重，迫使模型进一步拉开它们之间的距离。为了避免模型对所有负样本进行过度惩罚，论文设计了一个松弛函数：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0prVVocpQziavxPwt8PfVPy7oibIPEmYiczBynnGibCowSeVj4rbVq9CAv3z7zYvMiccIcSsNFnDAxxibc8tLdm7icrzib1Pqwicwej1ib4/640?wx_fmt=png&from=appmsg)

因此 Hard Margin监督对比学习帮助 MTRF：提升少样本攻击类别的特征表达能力； 减少相似攻击类型之间的混淆； 提高模型在类别不平衡网络环境中的检测性能。 最终，MTRF 在频率域中通过 Fourier Transform 提取稳定周期特征，再利用 Hard Margin 监督对比学习优化类别边界，使网络流表示具有更强的判别能力。

**（3）基于表示学习的最终分类检测**

经过时间域表示学习模块（TGCN）和频率域表示学习模块（GFCN）的训练后，MTRF 并不会直接使用深度网络完成最终攻击分类，而是将两个分支学习到的特征进行融合，生成更加稳定、更具判别能力的网络流量表示。

传统网络入侵检测方法通常采用端到端训练方式：原始流量->深度学习模型->攻击类别这种方式虽然能够自动学习特征，但是存在两个问题：容易受到网络噪声影响网络流量中包含大量非攻击相关因素，如果直接进行分类，模型可能学习到这些不稳定因素，而不是攻击行为本身。第二个问题是计算成本较高IoT设备通常计算资源有限：内存较小； CPU能力有限； 不适合部署大型深度神经网络。 因此 MTRF 采用了一种非端到端检测框架：

由资源较强的云端或雾节点负责复杂的表示学习，再将低维特征交给轻量级模型完成检测。论文提出该框架就是为了支持资源受限 IoT 场景，将 MTRF 部署在雾节点中生成流量表示，再由 IoT 设备根据自身资源选择合适的检测模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文在MQTT-IoT-IDS2020，UNSW-NB15，USTC-TFC2016，CIC-DDoS2019和TON-IoT数据集上验证所提出的算法，这些数据集涵盖了多样化的应用场景从模拟的物联网网络到真实的网络测试平台并涉及多种攻击类型，例如 DDoS 攻击以及基于内容的攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3hoibwJmM7YDdSYpb5ECyicMK0q84sxpxiaiaA1sT36MTnGaG5iacnOfQHicxhB3aUuPPvvCLZUNGpNbwtq6yI7hxpzTgh5dErYvvbw/640?wx_fmt=png&from=appmsg)

**(1)数据包载荷异常检测结果**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3WToHvXzFlr0XQvwbfYa6Tgf7cvqbqRcx7xyIHq5wWicqkcjfqXm6rDVB5Niac1ibibhPHEfXshTGmkeRLQ89UzxqVG6eBRqeH0yE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3v0IcYxm3rW3zfV7GeU895yEvwEDDhSKnhO5GQr1VEY74nXiaT1ibIiaLCWWSSS0vTm395BiaicUWS1kYYyk7mz3KEF82Ap8DBdDOw/640?wx_fmt=png&from=appmsg)

实验结果表明，MT...