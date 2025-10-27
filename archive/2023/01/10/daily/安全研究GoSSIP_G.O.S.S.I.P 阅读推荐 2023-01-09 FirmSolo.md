---
title: G.O.S.S.I.P 阅读推荐 2023-01-09 FirmSolo
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493839&idx=1&sn=862265447c695594a65ce2ec22ce5353&chksm=c063c616f7144f00359e78788943a5ae42e753059d67356a96890be2b007f5916e8510f82a86&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-01-10
fetch_date: 2025-10-04T03:25:57.497365
---

# G.O.S.S.I.P 阅读推荐 2023-01-09 FirmSolo

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7OicBW6B6Fdpz8k2wNZSgSFwTx4xPylrYztUGfp0e2Tg6UreolaSJoU8rg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-01-09 FirmSolo

原创

G.O.S.S.I.P

安全研究GoSSIP

在过去的几年中，针对IoT安全研究的一个大热主题是如何动态分析IoT固件（比如使用模拟执行的方法）。在今年的USENIX Security会议上，来自波士顿大学的研究人员进一步细化了这个方向，他们在名为 *FirmSolo: Enabling dynamic analysis of binary Linux-based IoT kernel modules* 的论文中介绍了一种能够对IoT固件里（私有）的Linux Loadable Kernel Module（LKM）进行动态分析的方法。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7Oicw5WE4Dt8GAru9XEncI5Oj0GVSwYHLI3IiaVRoCRDiaNU81Zy8icOYiaO4A/640?wx_fmt=png)

在这篇论文中，作者设计了名为`FirmSolo`的系统，这套系统的新颖之处在于，它利用了名为*Kernel Configuration Reverse Engineering*（K.C.R.E）这么一项技术，生成了各种不同的内核编译版本，这些根据不同的特定参数编译出的内核，能够对应地加载现实中已经编译过、缺乏源代码的LKM二进制代码，这样就可以动态分析这些LKM啦！

作者指出，之所以需要K.C.R.E来生成不同的内核编译版本，是因为现实中搜集的LKM并不是随便找一个内核就能加载成功的。要成功加载一个特定的LKM，首先需要内核的版本是这个LKM指定的，其次需要给这个LKM提供所有它需要的外部符号（外部函数），最后还要保证LKM中需要的特定数据结构类型在内核中被正确定义。下图是`FirmSolo`解决这些挑战的工作流程：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7Oicn07fibTvORB5eHGEHUYhjfQu6V4ib9TFc4U86Ls1uydzsGMu1LerBcwg/640?wx_fmt=png)

`FirmSolo`首先会分析搜集到的LKM二进制代码（.ko文件），从中搜集到LKM运行所需要的内核版本、符号信息和数据结构类型信息，然后就进入到K.C.R.E流程，构建所需要的内核编译版本。这里面比较有意思的地方在于，有时候如果不仔细考虑编译的参数，编译出来的内核版本可能在一些数据结构的类型声明上有细微差别。例如下图中这个`struct net`，在不同的编译选项下结构是不同的，如果LKM需要的类型和内核编译版本实际定义的类型只是名字相同，类型上不一致（也就是对象的内存布局有差异），那么在动态分析时肯定会崩溃。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7OicWouqRQUiaxGIIf90yGwGk7gTYRmpKSVpjxHTMvmeJicjMibZeKReGyaKQ/640?wx_fmt=png)

解决这些问题之后，`FirmSolo`就可以大显身手了，不过我们觉得作者给这个系统起名叫做`FirmSolo`并不是很合适，因为作者实际上并没有用它来solo，而是结合了`TriforceAFL`和`Firmadyne`两个之前的固件分析系统一起使用。`TriforceAFL`是著名的安全审计团队NCC Group在2017年开发的一个基于AFL/QEMU的kernel fuzzer，而`Firmadyne`是本文作者之一的Manuel Egele在2016年参与的NDSS论文 *Towards Automated Dynamic Analysis for Linux-based Embedded Firmware* 中介绍的分析系统。作者用`FirmSolo`编译了1470不同的firmware固件，能够用这些固件动态加载他们收集到的56688个不同的LKM中的36178个（64%，见下表）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7OicjEUltpB4plFnApYs8AzwKG7dg4NPTBftwMSFD8ibexjjq6ulhIKF1ibA/640?wx_fmt=png)

当然，`FirmSolo`也不完美，针对LKM的分析，还是很容易失败的，特别是一些符号，不管你怎么编译就是构建不出来（可能是因为私有代码？）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7OicRibKKx2LlKoPuf6kcrhYeL7cQjhdy59ZneY9mVS0icDQaLPLYsibUElqg/640?wx_fmt=png)

在`FirmSolo`和`TriforceAFL`的结合实验中，`TriforceAFL`成功分析了75个LKM二进制代码，并发现了19个此前未发现的bug，影响了10款现实世界的IoT设备。而在`FirmSolo`和`Firmadyne`的结合实验中，作者在15款固件中发现了`NetUSB.ko`这个闭源的LKM中的漏洞，在84款固件中发现了此前由`TriforceAFL`分析发现的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7Oicp6TVxKdzUROMwBNKwqmjfjwPibddQsjU99l1ChXcWViafBFGsqQYMiaUw/640?wx_fmt=png)

在附录中还有一个比较有意思的内容，介绍了`FirmSolo`如何解决内核版本中定义的数据结构和LKM中需要的数据结构类型不一致问题的细节，感兴趣的读者可以看看：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21E0EVZ85hyGsT5A5KaPF7OicJmZl2kJ2W1l9l5zIh7pus0aMSv7oqbNSndwAchxo7nZXxFibJu69Y0w/640?wx_fmt=png)

---

> 论文：https://www.usenix.org/system/files/sec23summer\_190-angelakopoulos-prepub.pdf

预览时标签不可点

阅读原文

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