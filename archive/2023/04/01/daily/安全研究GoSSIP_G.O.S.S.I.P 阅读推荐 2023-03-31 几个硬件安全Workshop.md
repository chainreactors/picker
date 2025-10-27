---
title: G.O.S.S.I.P 阅读推荐 2023-03-31 几个硬件安全Workshop
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494761&idx=1&sn=0cbc0f16803fbd47edf71005525aa9bc&chksm=c063c2b0f7144ba6eaaa9eb5c58020b00b346c63afeb5f96154f297d7c28adbf1587bcdf0428&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-04-01
fetch_date: 2025-10-04T11:22:50.844110
---

# G.O.S.S.I.P 阅读推荐 2023-03-31 几个硬件安全Workshop

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoeq5icOicBw3wjkEqR7e2K8ywFoRPgYdDBvtvXCreqKMicR7m6DVJ6CsEKw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-31 几个硬件安全Workshop

原创

G.O.S.S.I.P

安全研究GoSSIP

2023年的第一季度就要过完了，不知道你是否充分享受到了今年的明媚春光呢？接下来是更美丽的四月，我们今天就休闲阅读，来看看几个有趣的workshop，放松放松~

首先要为大家介绍的是HASP workshop【https://www.haspworkshop.org】，也就是 *Hardware and Architectural Support for Security and Privacy* 这个workshop，在2022年和体系结构四大会议之一的MICRO一起举办。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoesUlZTLoF0bibyop37fDgsr8vq85swH2hSjUwTX9mQhuIia07kEMoxemw/640?wx_fmt=png)

从名字就可以看出来，HASP的研究论文关注在硬件层面上为系统安全提供新的设计，其实很多最近几年的顶会论文中的一些思想火花也会来源于此，比如我们在本周一推荐的Syscall Integrity论文中介绍的Intel CET技术，研究人员早在2019年就在HASP上发表论文 *Security Analysis of Processor Instruction Set Architecture for Enforcing Control-Flow Integrity* 对它进行了安全分析，而在2022年的HASP上，也有一篇和Syscall Integrity研究类似的论文 *SFP: Providing System Call Flow Protection against Software and Fault Attacks*

> https://arxiv.org/pdf/2301.02915.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoeSmn9qL9JW6v4xpgFfoJjGCfd8S357eIp5LRiaBBGzs2QPmOILZGkQfg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoe08iat2tGStwoCjictxru2kyBVEGZ7k2VNdUdIBzgSLtcBmrNLLPdCWng/640?wx_fmt=png)

另一篇防御Rowhammer攻击的论文 *ALARM: Active LeArning of Rowhammer Mitigations* 非常幽默，论文里面有很多很多的“锤子”符号，但是编辑部现在也不知道这个unicode怎么打出来~ 这篇论文还有华为英国的研究人员参与，也算是“扬我国威”了^\_^

> https://arxiv.org/ftp/arxiv/papers/2211/2211.16942.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoezdhFPSLNzKeDkE2BKTmmpia9jicbQp3iar0M7SubHWQdCTvcJtQe4HJsg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoeSWUuJ8e62TLvSXarpLwKYTSKxJz1kwCOzJqADwNm2GV6rAbCCbQORg/640?wx_fmt=png)

---

另一个今天要推荐的workshop——AIHWS是一个抓住了AI热点的workshop，关注的是人工智能在硬件安全中的应用，是由荷兰Delft大学的AISyLab（人工智能与安全实验室）长期主办、和ACNS一起召开的一个会议。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoe6gCS4w5nxH9lyia5pe2r91RyoJcAhmDoHAn0o1ycDUZI8K4Jonn3iaaQ/640?wx_fmt=png)

AIHWS主要关注的是AI对硬件级别的physical side channel analysis的帮助。由于物理层面上的side channel analysis经常会被噪声干扰，因此人工智能技术对特定模式的识别能力往往能够在这时候发挥重要作用。我们今天要给大家主推的是一篇利用side channel analysis来实现逆向分析的工作 *A side-channel based disassembler for the ARM-Cortex M0*

> https://eprint.iacr.org/2022/523

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoeefDRVQwfOiby1YvIBIic7Vyq9hYeB7HxzVAa9g6FrwibdtjZHiaaTcullw/640?wx_fmt=png)

首先回顾一下历史，（可能是）最早的利用physical side channel information来分析处理器上究竟执行了什么指令的研究工作发表于2002年，在那时候就已经开始使用神经网络了（时尚时尚最时尚！）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoeQO2Yyk4JYSqs4C4WvHh34y46iaf5lQsZTlxn9A84VUnwuuR4VPyU5Fw/640?wx_fmt=png)

到了2008年，在硬件和软件安全综合研究方面的牛校——德国波鸿鲁尔大学的研究人员Martin Goldack在他的毕业论文中详细讨论了用physical side channel information来开展针对microcontroller的逆向工程的可行性

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoezVa2V4V7Rh25LTY6qU1xRzoKXp8Cg48lB5TH7VriaiaPgMgbgrZaCfuw/640?wx_fmt=png)

到了2010年，波鸿鲁尔大学的研究人员进一步提出了利用收集到的physical side channel information来实现一个反汇编工具的技术

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoejQ4bJsA37EpUrmxdkM6p7kDsvpA8T7bWPWqGzOkCjuPQOvczuQOtqg/640?wx_fmt=png)

在本文中，作者针对ARM Cortex M0的CPU上执行的代码进行了功耗分析，并且发现，在实际分析中，其实并不需要特别高深的机器学习方法，也可以（针对作者的实验设计数据）实现88.2%的反汇编（指令区分）准确率

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21H1WslSiaU4Z6PhVthOjMHoe9JHdfRibAy34ZDTPRYa1Zn65ogibrccj3MPCgCYJtzydWibiciaBFtuJscA/640?wx_fmt=png)

好了，今天就让我们划划水，明天就是愚人节了，希望大家都能做到 “人生识字忧患始，脑残儿童欢乐多”！

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