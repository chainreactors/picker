---
title: G.O.S.S.I.P 阅读推荐 2024-09-25 PeTAL和访问控制完整性
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498917&idx=1&sn=235eaa4c23a4c37180c0428057c5f9df&chksm=c063d27cf7145b6a833ab21d0dfbf5c517f169ed94a8a0b1e4f7b37e3dfee39cdd87106bc479&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-09-26
fetch_date: 2025-10-06T18:29:40.277435
---

# G.O.S.S.I.P 阅读推荐 2024-09-25 PeTAL和访问控制完整性

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZNsM5zYiaHQMyDnVPrC56YMZHIWiaHaRYj5Psauia6e5mIWic9UZz9GTPgA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-25 PeTAL和访问控制完整性

原创

G.O.S.S.I.P

安全研究GoSSIP

今天分享的论文*PeTAL: Ensuring Access Control Integrity against Data-only
Attacks on Linux*来自CCS 2024，是一项针对data-only attack安全防护的研究工作。更具体一点来说，本文研究了如何保护操作系统中的访问控制子系统的安全，并把这个需求定义为“访问控制完整性（access control integrity）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZtvXYKksKgR7kiau9NxGtDYTCEo4l231QQRuoEPHqalNY7jIjuHERW5A/640?wx_fmt=png&from=appmsg)

在本文中，作者充分利用ARM近年来在硬件层面上引入的两大辅助特性Memory Tagging Extension（MTE）和Pointer Authentication Code（PAC），对操作系统内核（主要是Android系统内核）中的访问控制子系统关键数据进行保护，对抗data-only attack，而且还开发了一套静态分析方法来标记那些需要保护的数据。特别注意到这篇论文的作者包括来自首尔国立大学和三星研究院的研究人员，仔细观察论文也会发现，里面的研究成果得到了实际的应用——在三星的S22手机上进行了实验，作者还在footnote里面略带show off地指出：“*虽然零售版的S22并不支持本文设计所需要的ARM硬件特性之一的MTE，但是我们是三星研究院啊，我们找公司弄来了一台支持MTE的设备用来进行性能测试~*”

言归正传，在本文中，作者设计了一套专门用来保护访问控制系统（access control system）的数据流完整性（Data Flow Integrity，DFI）防护系统`PeTAL`，对抗现有的data-only attack的威胁。先看下图，目前的data-only attack其实主要就是针对系统的访问控制系统，想办法篡改用户权限相关的数据，让攻击者能够获得更多的资源访问能力，因此`PeTAL`就只聚焦在针对访问控制系统的防护上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZeCzFJQ5XqPI7YGgib3zcUNp2HQaRTMwpNNAmpUiaWn6cN0otX2Iwus0w/640?wx_fmt=png&from=appmsg)

既然目标已经很明确了，接下来就是这种内存安全防护方案的标准套路：

1. 打开冰箱门；
2. 放入大象；
3. 关上冰箱门。

1. 标记出需要保护的对象；
2. 利用各种软硬件特性改善因为实施内存安全防护而产生的性能开销；
3. 测试并证明所提出的方案能够对抗各类攻击。

这个套路看起来很容易理解，但是每一步都涉及到许多复杂的细节，比如第一步里面，你怎么知道哪些对象是需要保护的？很多研究往往都会“挂一漏万”，只关注一些核心的数据，却忽略了很多外围同样需要保护的内容。因此在它的工作流程（如下图所示）中，`PeTAL`首先开展了静态分析，标记出来所有需要保护的（内核）对象。这里要注意的是，下图里面那个序号标错了，大概是作者后面修改论文的时候把Threat Model单独拎出来作为Section 4，所以整个设计全部挪到第5章了，大家看图配合读论文的时候不要搞错哦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZkPO4Rw0n7lAw9faVJ274ib41Em7Y7bljibt1VcBsdfqdlxZUdkqFdJMA/640?wx_fmt=png&from=appmsg)

`PeTAL`的保护对象主要包括了内核中的访问控制的策略数据，为了防止恶意的修改，`PeTAL`必须要保证只有那些得到许可的指令才能去修改策略数据，而其余指令对策略数据进行修改就破坏了“访问控制完整性”。`PeTAL`在这里的设计很有意思，如上图所示，实施访问控制完整性包含两类防护：对privileged object（可以粗略地认为是存储了access control policy的对象，以及一些敏感的资源文件）的保护，以及对privileged pointer（存储了privileged object的内存地址）的防护；前者的实施借助的是MTE，而后者很自然是用PAC来实施。

更细节一点，对于privileged object，作者认为有三种访问的情况（如下图）：

1. non-privileged access：某条访存指令只会访问和access control无关的内存数据；
2. privileged access：某条访存指令只会访问和access control相关的内存数据；
3. mixed access：某条访存指令既会访问和access control相关的内存数据，也可能访问和access control无关的内存数据。

很显然，对前面两种情况都容易处理，而第三种情况是比较麻烦的，而且`PeTAL`的静态分析采取的策略是path-insensitive（但是 inter-procedural、context-sensitive、field-sensitive），在这种情况下，就需要关注的是访问数据的pointer的特点了，这就是接下来要讨论的privileged pointer防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZpicwlAgsgGJIgQ5yr04EbKVpzttmHL66ztNJVmDHdVaCRN80EyRP3Bw/640?wx_fmt=png&from=appmsg)

对于指针的访问，`PeTAL`在PAC的基础上（也就是给指针初始化和赋值的时候同时生成一个tag，在使用指针的时候再检查这个tag是否和当初生成的时候一致），还要进行一次额外的检查，就是看这个指针对应的tag在生成的时候，所对应的上下文（context）是不是和access control相关，如果这个tag确实是在和access control相关的情景下生成的，那么这个指针就允许访问privileged object，作者的这个设计也算是一种context sensitive的安全防护吧？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZWGJwchQB3ibMeQMdTCRvf5d3h9diaua2oDJeTzPNTF9d6FAh8jxyYmww/640?wx_fmt=png&from=appmsg)

`PeTAL`的具体实现中，利用了以前的一些基础工作，比如使用wllvm（Whole Program LLVM，https://github.com/travitch/whole-program-llvm 一看名字就知道什么意思）把内核编译成一个完整的bitcode文件然后再做静态分析，然后用PeX（USENIX Security 2019的工作）来进行间接调用的分析。经过分析，`PeTAL`在Linux Kernel v5.10.136中标记了507个kernel struct type、449个stack object、350个global object和140个global pointer（把它们标记为privileged object）。在对这些对象进行保护（同时也关联了相关的指针防护）之后，性能开销也很不错（特别是跟NDSS 2016的data flow integrity防护系统Kenali对比）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZNziccprJMuZRumdXBlIwRXPOwOnT95cQCaoiaeNxHzEz2bKMkqsjPQmw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVZDH2rGiapE1mHpvWh8JjZ9VFOtqbgpsMMmcTSiaWwWjSswNog996oh2NYZFicibCpVkEOl9T97BINg/640?wx_fmt=png&from=appmsg)

当然，从论文的实验来看，`PeTAL`也能对抗各种已知的data only attack，不过论文里面肯定不会去搞一个自相矛盾的结论的，对于这个防护的效果，我们只要认为它能够提高攻击者的门槛即可。

---

> 论文：https://www.cs.ucr.edu/~csong/ccs24-petal.pdf
> 项目：https://github.com/compsec-snu/petal （确实能用！）

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