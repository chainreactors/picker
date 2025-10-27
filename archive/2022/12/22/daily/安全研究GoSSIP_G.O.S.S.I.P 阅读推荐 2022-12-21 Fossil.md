---
title: G.O.S.S.I.P 阅读推荐 2022-12-21 Fossil
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493664&idx=1&sn=1789b03ad045b5d718e30d2c154d181f&chksm=c063c6f9f7144fef0a09595fcb3ebf09e66d22618eeff78a583a4c95e40f93dee2711905d066&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-12-22
fetch_date: 2025-10-04T02:14:32.261237
---

# G.O.S.S.I.P 阅读推荐 2022-12-21 Fossil

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21FkGjXukPere5gwFib21C9cwxTPdV0q1q4FQUyuTIe2p4hVz6icNLnz9a4mFSUGv1vUK3JxIFC7sFZg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-12-21 Fossil

原创

G.O.S.S.I.P

安全研究GoSSIP

今天为大家送上的是2023年NDSS会议录用的论文–*An OS-agnostic Approach to Memory Forensics*，这是一篇关于数字取证（forensics）相关的研究论文（说到取证，这里就要强行插入一条软广：G.O.S.S.I.P在2011年移动安全刚刚兴起的时期，就曾经拿到过一项国际数字取证竞赛的奖项，感兴趣的读者可以访问 https://www.honeynet.org/challenges/forensic-challenge-9-mobile-malware 了解细节），在这篇论文中，作者讨论了一个非常重要的研究主题——如何在不知道设备运行的操作系统的情况下，直接分析raw memory dump来获取更多运行时信息？

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FkGjXukPere5gwFib21C9cwmHIT4NmdlXMkJLSNAkzUabmPtb3MoQG9Hj93F4OAaouoxUHLrgcUNw/640?wx_fmt=png)

我们知道，由于操作系统的管理，直接去读取物理内存并分析是很困难的，我们还需要还原物理内存到虚拟内存的映射关系才能得到“可读的”内存数据。然而在很多场景下，分析人员需要直接对物理内存中的数据进行取证分析，而且随着现代操作系统的多元化（同时还要考虑到越来越多的虚拟化场景），有时候你甚至都无法确定待分析的数据究竟运行在什么样的系统上，这个时候我们就需要开展所谓的OS-agnostic Memory Forensics，即操作系统不可知情况下的内存取证。

作者援引了他们自己刚刚发表的一篇论文 *In the Land of MMUs: Multiarchitecture OS-Agnostic Virtual Memory Forensics* 中的结论 (https://dl.acm.org/doi/10.1145/3528102)，认为“*for most CPU architecture it is possible to reconstruct the kernel address space in an OS-agnostic way by
using only information derived from the hardware configuration of the machine. It is by using this information that we reconstruct in-memory kernel data structures like linked lists and trees*” 此外，在内存取证分析中，有一项非常标准的技术——memory carving可以利用。也就是说，像字符串信息这种在内存中不管怎么放都很容易识别出来的数据，可以被当成是基础的index（在本文中作者将此类信息定义为seeds），以它们做定位符来驱动其它的指针类型数据的识别（是不是很像小孩玩拼图~）

更进一步，作者带大家复习了一下计算机系大一的《数据结构》课，对OS内核里面常用的数据结构（诸如双向链表、树以及更多的复合结构）常用的指针指向特点进行了总结（Fig 1），然后使用了名为欧米伽函数（Ω function）的扫描算法来判定内存中某个数值是否为一个指针（即指向了一个合法的虚拟内存地址）。这个Ω function的具体实现在论文的第五章有所描述。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FkGjXukPere5gwFib21C9cwgayQntSUxJ1MCickRzMIqmm2hvRSo9Mv1PX5p7pXSXezP8iaIjk9GPvA/640?wx_fmt=png)

在具体操作中，首先使用Ω function对内存数据镜像进行分析，找到各种指针（下图的step 1）；然后再把各种指针之间的关系进行恢复（下图的step 2），具体细节见Section IV-A；有了指针的信息还不够，进一步的静态分析会把数据分析扩展到指针所在的struct的其它数据（下图的step 3）。最后，利用汇总的信息进行cross-references分析，完成拼图（下图的step 4）！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FkGjXukPere5gwFib21C9cwaA4SDSZKcQSYficXQiaZqo9vxZZIKcQrsAvaooXwA9MPugUe2pia1AZyg/640?wx_fmt=png)

注意到这种分析肯定会存在一些误差（通常是把数据当成指针），作者也承认Ω function存在一些过估计，如下图所示。这时候可以利用seed信息来辅助，将分析结果精细化。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FkGjXukPere5gwFib21C9cwv8ZQFVQIdd1iansCUVsW13dhZyeN08DSicMzfMtncWsz9cj0Hlc18P4A/640?wx_fmt=png)

作者还提出了更为大胆的想法，即使不考虑内存中的一些seed信息，是否也可以开展类似的分析（即论文中讨论的seed-less analysis）。作者在后续实验中也验证了可行性。

论文中，作者设计了名为`Fossil`的原型系统，对14个不同的OS进行了实验。首先测试的是对指针信息的恢复：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FkGjXukPere5gwFib21C9cwqLHLGuhpjvhWURHJtmiatbKA2jMBUEKicozZKNqbY8nZaye1eoP6acHA/640?wx_fmt=png)

在对内存镜像中的数据结构的恢复实验中，`Fossil`几乎可以识别不同操作系统的各类数据结构：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FkGjXukPere5gwFib21C9cwkaBRtdciac1dgFVs4ArUKwTzgat53trBratqeOpa9VcnKKoTsHodYgw/640?wx_fmt=png)

作者还把`Fossil`同取证行业常用的Volatility进行了比较，Volatility大部分的分析都是基于人工编写的规则，因此在分析时只要知道了底层操作系统的细节，应该可以算成是ground truth（或者说接近ground truth）。而`Fossil`在不知晓底层OS的情况下，还能做到Volatility的69%的效果，而且在一些特定的数据结构（例如内核中的双向链表）恢复上，表现甚至超过了Volatility手写插件。

最后，作者对seed-less analysis的分析结果（下表）表明，即使不知道seed信息，作者的方法和`Fossil`系统还是能够为分析者提供很大的帮助！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FkGjXukPere5gwFib21C9cwHOibUzjYOCayryoPNEgf19Csibjoj8fJ2DJOkssDm6nFoUpUSgqiao2GA/640?wx_fmt=png)

---

> 论文PDF：https://s3.eurecom.fr/docs/ndss23\_oliveri.pdf
> 项目代码：https://github.com/eurecom-s3/fossil （无情地鄙视这种虚假开源的项目！）

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