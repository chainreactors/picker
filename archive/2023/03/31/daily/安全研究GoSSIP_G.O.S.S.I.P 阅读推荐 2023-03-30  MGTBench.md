---
title: G.O.S.S.I.P 阅读推荐 2023-03-30  MGTBench
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494746&idx=1&sn=21017225e821bc78261ba8e6d7bef69b&chksm=c063c283f7144b95bd06dfbdaa6338c1ce94dd6f60b89c542d1353b288cfa6be3e66fe5f14c5&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-31
fetch_date: 2025-10-04T11:15:54.396749
---

# G.O.S.S.I.P 阅读推荐 2023-03-30  MGTBench

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC60XL7eGYomO8mxpz4riaXmJZpdrOjGPHax1UgcSibt8hV8jcGJfflpGaA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-30 MGTBench

MGTBench Group

安全研究GoSSIP

今天给大家推荐的是来自德国亥姆霍兹信息安全中心(CISPA)[张阳研究组](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492201&idx=1&sn=5f4c38f8961b3a18c27107062b8c75b2&chksm=c063ccb0f71445a6bd29685dd7375e560322d2dbb1ee567f51f707c348c123986b90dcde1edd&token=1033824400&lang=en_US&scene=21#wechat_redirect)投稿的关于ChatGPT生成文本检测工具的研究。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC6Yq5RtbPvXibOWfuMXuLGnH9MRJBAicLwWvOzokXLf1xl8hZRiaGo7NqCw/640?wx_fmt=png)

近年来，大型语言模型如T5, PaLM, ChatGPT等在多个科技、教育、金融、服务等多个领域都展示了令人惊叹的效果。在海量模型参数和大量语料的加持下，人们可以轻松使用大型语言模型生成各种各样的文本，比如小说、诗歌、剧本、广告、文案。然而，在技术的快速推进下，这些生成的文本所带来的的安全、隐私、版权等问题仍然没有得到明确定义。

因此，如何识别机器生成的文本（machine-generated text, MGT）就显得至关重要。

为了解决这个问题，研究者们提出了许多检测方法。但是这些检测方法的测试数据集、语言模型、评价指标都不尽相同。这对进一步理解、运用、评估现有的检测方法提出了很大的挑战。

为了解决这一挑战，本文提出了第一个整体评估生成文本检测方法的框架——MGTBench。

目前，MGTBench实现了8种不同的检测方法，包括6种基于指标的算法和2种基于分类模型的算法。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC6PWLLS8Kxp68RLMicqMAgdYBG3ibRgnE9eTyic87wrrPvgud3CHibQrkribg/640?wx_fmt=png)

## 数据集

为了公平衡量这些检测方法的性能，作者使用了多个公开数据集对其进行评估。

具体来说，作者的测试文本包括两部分，人工编写的答案（human-written text, HWT）和机器生成的答案（Machine-generated text, MGT）。其中人工编写的答案来自公开数据集中本身包含的内容，机器生成的答案则来自于当前最先进的ChatGPT语言模型。

本文使用的数据集如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC6A70PsrnUV8p0P5xiaVRRbMOMU0uTAgqtC9GnsNz2tMj3rR5ul7I8Eiag/640?wx_fmt=png)

## 性能分析

MGTBench的结果如下表所示。

作者发现在8种算法中，ChatGPT Detector的表现最好。这可能是因为ChatGPT Detector已经在不同的ChatGPT生成的语料上进行训练, 使其对ChatGPT生成的文本特征有着更强的分辨能力。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC65Y7hSViczeX0wXrqWvBMUicVicW139v9x8rvzibnW6r007mpcbchvc0ib3g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC6GXLldkd7h6UdkDz2vXyklnJzwl35XwUOg2rMwPicKEsEEGEYbLsf3YA/640?wx_fmt=png)

此外，作者还分析了人工回答的文本和ChatGPT生成的文本在长度上的区别，如上图所示。作者发现，ChatGPT生成的文本往往更长，而绝大多数人工回答的文本只有不超过25个词。为了消除长度对检测结果的影响，作者进一步过滤掉所有长度超过25个词的数据，并对剩余数据进行测试，结果如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC616tVibLwBIbf3C7IwgJIcPRhpzmibSXA0cvwksxzAxftwNtmx2r3Ticlg/640?wx_fmt=png)

作者发现，所有检测算法均受到了不同程度的影响，而ChatGPT Detector受到的影响相对较小，这也得益于其在ChatGPT生成的语料上训练过，因此能够更好地检测ChatGPT生成的文本特征。

## 鲁棒性测试

该工作的另一个贡献是对ChatGPT Detector的鲁棒性测试。作者发现，通过对抗样本攻击，即使只用很小的扰动，也能轻松绕过ChatGPT的检查，如下图所示。这也说明现有的检测方法的鲁棒性尚有不足，同时也为未来检测方法的设计提供了思路。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC6jSVdujw5eqvic7Azeaz9kJRkbeFXLNkBsAQlLEtcJg0NCYYIOfzfx9A/640?wx_fmt=png)

下图展示了一些添加扰动的例子：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HjlUibqdujcEXaCTkjWFSC6SeOIh0N2iav7c5IZJ4sLzoWRohWslicylicwJv2a8jSb4sV55szk3icicVg/640?wx_fmt=png)

## 结语

在这篇工作中，作者提出了第一个整体评估生成文本检测方法的框架——MGTBench。

**MGTBench采用模块化设计和开发，覆盖8种检测算法，多个公开数据集，支持开箱即用。**

在未来，MGTBench Group将会涵盖更多的检测方法、实验数据集、分析工具。敬请期待！

论文链接：https://arxiv.org/abs/2303.14822

代码链接：https://github.com/xinleihe/MGTBench

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