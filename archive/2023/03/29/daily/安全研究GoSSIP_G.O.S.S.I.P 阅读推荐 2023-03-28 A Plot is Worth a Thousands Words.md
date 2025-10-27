---
title: G.O.S.S.I.P 阅读推荐 2023-03-28 A Plot is Worth a Thousands Words
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494724&idx=1&sn=3c8ac68599272ac39fc002472be655b1&chksm=c063c29df7144b8bd9504dfe429e871db56231478f60e96892b3ac704acd4d1369e847d0ead5&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-29
fetch_date: 2025-10-04T11:01:28.149047
---

# G.O.S.S.I.P 阅读推荐 2023-03-28 A Plot is Worth a Thousands Words

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8OTKRHW9icrvxvCrC2K4LvR5ibcJoBhVCSgJKBmzZ1H5Rv8LJ8qOD8LgQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-28 A Plot is Worth a Thousands Words

Boyang@CISPA

安全研究GoSSIP

今天给大家推荐的是来自德国亥姆霍兹信息安全中心(CISPA)[张阳研究组](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492201&idx=1&sn=5f4c38f8961b3a18c27107062b8c75b2&chksm=c063ccb0f71445a6bd29685dd7375e560322d2dbb1ee567f51f707c348c123986b90dcde1edd&token=1033824400&lang=en_US&scene=21#wechat_redirect)、NetApp的沈韫和[弗吉尼亚大学的王天豪](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492540&idx=1&sn=5c02407afc67d9d6aaea6a4ba9aa999c&chksm=c063cd65f7144473b9d979f26810d4ad0ecc236a75968c2f715d9bacea566d7547abe8f4b642&token=1033824400&lang=en_US&scene=21#wechat_redirect)研究组投稿的关于从科学图表中窃取机器学习模型信息的文章A Plot is Worth a Thousands Words: Model Information Stealing Attacks via Scientific Plots，目前该工作已被USENIX 2023录用。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8HNLZMBfehjDphnVpD3oYGIzUa2EkSA8u5Ih30fAibOM0H2FaxUfhTAg/640?wx_fmt=png)

随着机器学习在各个领域取得了长足的发展，保护模型信息愈加重要。高质量的模型，通常需要多次训练测试不同模型架构以及相对应的超参数（hyperparameters）来找到最优设定。基于训练过程所需的人力物力，这些信息对于模型拥有者来说是非常宝贵的。另外，泄露模型信息可以使得黑盒（black-box）模型变成白盒（white-box）模型，导致模型更容易被其他攻击威胁，比如对抗样本生成（generating adversarial example）和成员推断攻击（membership inference attack）。

以往的研究表明，机器学习模型的确会从预测结果中泄露模型信息。然而，以往的工作依赖于使用预测结果中的信息。模型拥有者可以很容易检测到攻击者的存在并部署相关的防御措施。如果模型拥有者对预测结果的格式以及模型使用量有限制，这些攻击效果通常也会大幅下降。然而，用于展现模型在预测任务上表现的科学图表往往不被认为会泄露敏感信息，在发表的论文以及商业化软件广告中都很常见。因此这些图表可以被攻击者很容易得到。攻击者从已发布的图表中窃取信息不会给原模型拥有者任何提示，从而带来更严重的安全隐患。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr805ibB5XRC3cLCpfdcbnuibr1qHm4CKAaeWqCjmCyVukq3zfxVlPQfExQ/640?wx_fmt=png)

在本文中，作者提出了第一个从展现模型表现的科学图表中窃取模型信息的工作。 本文着重研究两种广泛应用的（如上图所示）t-SNE散点图（t-SNE plot）和损失函数折线图（loss plot）。实验结果表明，两种图表都会泄露原有模型的信息，包括模型类别，架构，以及训练所用的超参数。作者还提出相对应的防御方法。通过在不同阶段像图表加入扰乱可以适量减少攻击的有效性。但对于已知防御手段的攻击者来说可以很容易加入适应性的训练信息导致防御失效， 更加显示此类攻击的威胁性。

## t-SNE散点图攻击

t-SNE散点图是本文着重研究的科学图表。t-SNE（t-Distributed Stochastic Neighbor Embedding）是一种常用的降维方法将机器学习模型学到的高维特征映射到可以绘图的2或3维。这类图表广泛应用于反应数据分类效果上。
攻击者的目标是利用科学图表对目标模型进行模型信息窃取攻击，从而获得训练该模型所需要的信息，进而使攻击者可以用相同参数训练出一个表现和行为相似的模型。作者首先训练出多个不同参数的模型，然后用每个模型随机选择一部分样本来生成科学图表。这些生成的科学图表成为训练数据来训练一个图片分类器作为攻击模型，推测类别便是生成该图表的原本模型信息（如模型类别、架构等）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8wV5gGSlCItahIKgwlWSaMRw433p6Cu0U1fQ6fVBVYp6ddspXbibebXg/640?wx_fmt=png)

作者首先在不同数据集对不同攻击目标的表现进行了评估（如上图所示）。作者发现，从t-SNE plot中攻击者可以有效提取原模型信息，包括模型类别 （model family），架构 （type），优化器 （optimizer），以及批尺寸 （batch size）。在固定目标的设定下（只有目标信息未知，其余超参数等已知）攻击效果更为显著。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8AFqzaVmTXWfTTun8EjZAjzuH5pCic6SSx2SjYz77AhunMYk1pVorC6A/640?wx_fmt=png)

为了进一步研究t-SNE散点图泄露原模型信息的程度，作者用多个自定义模型来研究更多更具体的模型架构信息从图表中泄露信息的程度（具体参数参考上图）。与上面常用模型结构相比，这些模型之间的差距更小，在对于人眼极微难分辨也可以看出其相似度。但是作者发现攻击依然可以相对准确得预测多个重要模型结构设定。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8icxdhGHfVAW1QBjIpN4LdbGRoHFic11GSKVQosuhZaY5qFRlMaaJ4ETA/640?wx_fmt=png)

和图表攻击相对比，作者发现以往依赖于预测结果的攻击的确在同等实验设定下效果更好，但这是基于有充足的预测结果以及提供完整预测可能性分布的前提下。当预测结果只有类别标签的时候，图表攻击反而更加有效（如上图所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr83TBbaHib7o1LGDDlwYMyPYEgysbbKtkvuAia83c64Tt0m1WqVDLlOhXg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8WIicsHgTFnI2JcRAhlntQRgrQDAA7wiaEgymicFByXuHSMk9d1xibpuVfA/640?wx_fmt=png)

为了防御此类攻击，作者提出多种以轻微扰乱图表中信息为主思路的防御方式。有效的防御需要做到两点： 1）图表反应的模型表现相关信息应该保持不变；2）防御应降低攻击准确度。部分防御方式可以同时实现两点要求（如上图所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8P7V0LM1H6UjTojOuJ7RG5Liaek0h8YuZJbYSq1GvXbUSuH7C6CPsiaGw/640?wx_fmt=png)

作者进一步研究在攻击者知晓防御方法后采取适应性攻击（adaptive attack） 的有效程度。适应性攻击使得之前的防御措施再次失效，并且攻击者不需要确定防御具体设定。对于同类别不同设定的防御适应性攻击依然有效。

## 损失函数图 （loss plot） 攻击

在本文中，作者还研究了从另外一种常用的损失函数图表中推测原模型信息的效果。这类图表可以直观反应训练过程中多种模型表现，包括回归速度和过拟合程度等。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8zUGDRQM5eh9ae2X4briaLQI23YKdM1I9iakfFkqOXcUlhOPv4PAVBRJQ/640?wx_fmt=png)

实验结果表明，损失函数图相对于上面的t-SNE散点图更容易泄露模型信息。攻击者从曲线趋势就能以高准确度推测原模型的类别，优化器以及批尺寸设定。如果能获得坐标信息，攻击效果将进一步提升。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8sMYIQqOJl9iczT6iaRCUIDBogiaaktBx4O1Y7rzVbmQVBfUceLr6dGHng/640?wx_fmt=png)

和t-SNE散点图类似的思路，作者提出了3种扰乱图表信息的防御措施（如上图所示）。在保证图表展示的结果的特征不变的前提下，用滑动窗口平滑曲线可以降低攻击表现。但是同样在适应性攻击下防御措施再次失效。

## Grad-CAM分析

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HElTpD3pib8R3X2Itt1OLr8wPyX3pIahm8NyGW8m5e2kXibBsibR8MMWwzPD7h85NaLE23uAnu1sRkg/640?wx_fmt=png)

为了更好理解科学图表泄露模型信息的方式，作者用Grad-CAM来展示此攻击推断原模型信息的依据。在模型类别上，攻击模型的确能从t-SNE散点图中找到一些各个模型信息对应的特征，但是并没有很明显的规律。在损失函数图表上作者发现加入坐标信息后攻击模型会有效利用加入的额外信息来推测之前没有坐标时较难的类别，从而提升整体攻击有效性。

最后，作者讨论了当前工作的一些局限性以及通过在结构图神经网络（graph neural network）上的实验来展示此类攻击不仅适用于图片数据和视觉模型。

论文链接：https://arxiv.org/abs/2302.11982.pdf
代码链接：https://github.com/boz083/Plot\_Steal

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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