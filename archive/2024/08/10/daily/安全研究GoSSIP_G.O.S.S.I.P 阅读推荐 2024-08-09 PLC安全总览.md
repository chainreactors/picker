---
title: G.O.S.S.I.P 阅读推荐 2024-08-09 PLC安全总览
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498624&idx=1&sn=990fd6dec102a7d80e2be55bf2f2e601&chksm=c063d559f7145c4f5eccf3f4e31315ac556fcd10675b78c5c1777555a2fbdb9571fa78a0d6bc&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-10
fetch_date: 2025-10-06T18:05:41.021874
---

# G.O.S.S.I.P 阅读推荐 2024-08-09 PLC安全总览

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GxxBHxB1Hv16jhOYNdibvMnMtGuLTD6PiaQUEGciaTwg8wC5cUibLI8cDMicRL1gMqU8K37FMOZmkJYhw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-08-09 PLC安全总览

原创

G.O.S.S.I.P

安全研究GoSSIP

关于可编程逻辑控制器也就是Programmable Logic Controller（PLC）这个名字，可能很多人就是从当年引爆了安全新闻圈的伊朗核电站Stuxnet攻击事件中第一次听到的。实际上，在工业控制领域，在互联网还没那么发达的上个世纪，PLC已经是一个成熟的产业了（冷知识：世界上第一个PLC——Modicon 084是在1968年发布的，而Unix系统是在一年之后发布的），像西门子之类的公司早就深耕这个行业多年。最近随着国产化替代的兴起，PLC的国产化也被越来越多的提上议事日程，所以今天我们就要介绍一篇USENIX Security 2024上关于PLC安全的SoK论文*Security of Programmable Logic Controllers*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxxBHxB1Hv16jhOYNdibvMnOYZcnb1Xf41BZ47TvLfhibI3f7YFxw6Xic5FWldQ1iatcl8k5VN2icmPgg/640?wx_fmt=png&from=appmsg)

首先要了解一下PLC的基本知识。其实从硬件上，你完全可以把它看作是一个嵌入式系统，无非就是多了一些来自外部的输入和输出——通常都是连接需要控制的工业设备（例如电梯、空调这种）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxxBHxB1Hv16jhOYNdibvMnUSWECqTOFv4M3RusSwBD0QkRXAkNUjFHOsl56GOggHAw7yLt3Qe5xA/640?wx_fmt=png&from=appmsg)

实际上，PLC最大的特点是它的编程规范。在1993年，PLC有了自己的国际标准——IEC 61131-3 standard，这个规范定义了PLC支持的几种不同的编程语言，例如下面图中展示的这种，你看起来好像是个什么示意图，实际上它也是一种代码，叫做梯形图，是一种可视化编程语言。看到这里大家有没有想到现在特别流行的幼儿编程语言Scratch，哈哈，我们并不是说梯形图比较朴素，只是说这个是特定历史年代下为了让一些不懂计算机的工程师（特别是电气领域）能够开发出来相关的程序而设计的产物，当然现在让我们大声喊出来“PythonPHP是世界上最好的语言。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxxBHxB1Hv16jhOYNdibvMnKRs4wExIacKBVBI92Rr0tgzQpanQvbtDzSSn4j3icuzErVibZBTHBBjg/640?wx_fmt=png&from=appmsg)

在这个标准的定义下，PLC变成了有点像Java的感觉：上层都是通用的开发语言，但是底层的执行引擎（runtime）却完全不透明，厂商可以自己去设计特定的软硬件来实现对上层的PLC编程代码的（解释）执行。随着时代的发展，PLC内部逐渐开始使用RTOS作为核心，同时也引入了联网功能，支持使用串行总线协议Fieldbus或者是基于IEEE 802.3以太网通信规范之上开发的一些私有通信协议来进行PLC设备之间的数据交换。

从上面的介绍，你可以把PLC想象为一个相对比较落后于主流计算机（嵌入式设备）发展的“半原始社会”，既接受了一些主流计算机领域的先进设计，在大部分实现上都还非常简陋。针对这种发展现状，本文作者调研了最近10多年来和PLC领域相关的133篇安全研究相关论文（2007-2023年期间发表），提炼了其中涉及到的119种攻击方法和70种防御措施，同时总结了一套PLC相关的安全威胁分类学（感觉这已经是套路了），形成了本文的主要研究内容。下图是作者的研究方法的示意图（现在连怎么做研究都要画图了，走上了大公司PPT的套路）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxxBHxB1Hv16jhOYNdibvMnQTb8njEwAx1pDIRrCoUBCuDTYiasX58ic83TydbKONKst96lqIJh6soQ/640?wx_fmt=png&from=appmsg)

论文的核心干货是作者总结的两张表——Table 1和Table 2，这两张表涉及的内容太多，要怎么去解读，显然把涉及到的133篇论文都讲一遍是不现实的（事实上有时我们都应该质疑一下这种Survey或者SoK论文到底有没有必要去强调自己调研的论文的数量，反正你最后也不可能全部都用上这里面的内容），所以作者先对攻击（防御）分类，然后每个类别里面挑了两篇引用最高的，简单介绍了一下这两篇论文的highlight，实际上看完你就会发现，PLC这个生态就是个大型的缺乏防护的“安全金矿”，下面这个图里面各个环节，都不像主流互联网一样各种安全防护（例如加密、认证、访问控制）层层部署，甚至基本上都在裸奔，安全攻击者一旦进入到这个领域简直不要太开心了~~~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxxBHxB1Hv16jhOYNdibvMn91xUPTh6NJUmferrk9dk4sO5icOT7fkeefCYIRyvf6V1iaHxGe5UpvUA/640?wx_fmt=png&from=appmsg)

作者针对这些研究，进行了一些总结，要点包括：

1. 大部分的攻击甚至都不需要去了解PLC生态的特点，完全就是把计算机安全的技术平移过去就可以了，实际上这种问题应该是在几乎所有领域都存在的，计算机安全考研热可能还会延续一段时间。
2. 安全研究实际上很多都只是在实验室而不是生产环境里面开展的，因此要么没有覆盖到主流的产品和环境，要么压根就没去对主流的产品进行调查，比如说下面的图中，三菱（Mitsubishi）的PLC基本上就没人研究，但是它家的市场份额还是蛮高的（特别是国内很多使用）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxxBHxB1Hv16jhOYNdibvMnK98oD1BdQ5ejoTU6KsFpZx6fyRPzibaBSNdrXnpciamng4PRIV1qTeBA/640?wx_fmt=png&from=appmsg)

在我们的介绍里面，基本上忽略了作者提出的那个威胁矩阵，感觉这种东西好像有点套路，感兴趣的读者可以去作者的repo里面看看：

> https://github.com/efrenlopezm/ics2matrix

当然，作者也没忘记把所调查的论文的数据集开源出来：

> 数据集：https://github.com/efrenlopezm/plc-sok-dataset

这篇论文还有一个extended version，和USENIX Security的版本相比主要是附录里面多了很多东西，大家如果喜欢可以去读一读，比如在Appendix F里面介绍了包括Stuxnet在内的四个有名的Real-World PLC攻击案例。

> https://arxiv.org/pdf/2403.00280

---

> 论文：https://www.usenix.org/system/files/sec24summer-prepub-483-lopez-morales.pdf

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