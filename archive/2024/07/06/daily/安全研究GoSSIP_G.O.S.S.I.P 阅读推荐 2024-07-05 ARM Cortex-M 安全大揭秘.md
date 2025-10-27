---
title: G.O.S.S.I.P 阅读推荐 2024-07-05 ARM Cortex-M 安全大揭秘
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498376&idx=1&sn=52b537d37227fa870feedeeee3e85b4f&chksm=c063d451f7145d476dcb8ddf2b636f34c9ffd01f5931b5ef6bd9bb7ed53e2b7a215bcc45e31a&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-06
fetch_date: 2025-10-06T17:43:53.235589
---

# G.O.S.S.I.P 阅读推荐 2024-07-05 ARM Cortex-M 安全大揭秘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgYDVr8qTIwuTwYQeOCPqXwDkyxmKeenjZVfkCvic2xMA5sRcmCKBuoYA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-07-05 ARM Cortex-M 安全大揭秘

原创

G.O.S.S.I.P

安全研究GoSSIP

先来预告一下，今年[Let’s GoSSIP暑期学校](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498364&idx=1&sn=cb274a5852cd36c892b7f5af30882e25&chksm=c063d4a5f7145db3f55ce28d903b8fd7cc67453fb0265b375053ec72230abed9fa8d7d2a51e4&scene=21#wechat_redirect)一上来就会给大家一个“下马威”——来自南方科技大学张锋巍老师的lab，会让大家在树莓派上去亲手测试ARM芯片的安全特性和安全问题，由于需要准备实验器材，希望大家积极踊跃[报名](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498364&idx=1&sn=cb274a5852cd36c892b7f5af30882e25&chksm=c063d4a5f7145db3f55ce28d903b8fd7cc67453fb0265b375053ec72230abed9fa8d7d2a51e4&scene=21#wechat_redirect)，我们好提前准备，不然到时候没有实验设备了哦。

为了配合暑期学校的内容，我们今天介绍的论文也跟ARM安全密切相关，这篇SoK论文*SoK: Where’s the “up”?! A Comprehensive (bottom-up) Study on the Security of Arm Cortex-M Systems*将会在2024年的WOOT会议上和大家见面，今天让我们先睹为快。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgQfvlyhMt7RiaRHmYicJcA2EnKePWLDhQHv1xZL3KiaGgaCADMiaJNJiafpQ/640?wx_fmt=png&from=appmsg)

这篇论文关注的是ARM Cortex-M系列处理器的安全特性和安全问题，Cortex-M系列处理器是ARM专门为比较低功耗、低性能的运算环境（例如单片机）设计的处理器，由于需要考虑减小处理器的开销，所以在安全功能上相比起更高端的Cortex-A系列和Cortex-R系列处理器会有很多的裁剪。针对于此，论文首先把整个要讨论的内容用了一幅图来展示，这个很赞，可以看到作者在第三章关注了Cortex-M系列处理器的安全局限性，在第四章讨论了相关的软件系统安全设计思路在适配Cortex-M系列处理器上的问题，在第五章则是关注软件代码在Cortex-M系列处理器上运行时的实现安全问题，最后在第六和第七章总结了研究现状和未来的研究方向。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgHiazvZTTnBwicIdLZ2fF7GBAibWcLrAGGm6a0ia6W2Vx5EABL3NNC0TZUQ/640?wx_fmt=png&from=appmsg)

在介绍后面的研究内容之前，先说说论文的研究准备工作：作者首先收集了现实世界中的1797个Cortex-M系列处理器相关的固件，涉及689款设备，作者认为只有这样才能像田野调查（field research）一样，对真实的情况进行分析。作者还从CVE数据库里面收集了超过500个和Cortex-M系列处理器有关的bug报告（2017年到2023年期间），同时也整理了30多篇最近发表在各个顶会上、和Cortex-M系列处理器安全相关的研究论文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgn91x3UIznLannUk7XTH3VxEKQGrEuqQuFjYN6PnSUF6tusU8p5hroQ/640?wx_fmt=png&from=appmsg)

准备工作结束，作者首先调查的是Cortex-M系列处理器的硬件安全特性及其缺陷（第三章），在这部分中，作者总结了Cortex-M系列处理器的一些典型的不足之处，其中关键在于缺少了一些硬件内存管理部件，例如由于没有内存管理单元（memory management unit，MMU）导致不支持虚拟内存（直接使用物理内存寻址，相当于所有代码共享内存了），同时处理器的内存隔离能力和更高端的系列相比更弱，例如不支持按memory page的粒度去给不同的内存区域划分权限，只能把整个内存划分为少数几个不同的region来分开管理。更重要的是，Cortex-M系列处理器的TrustZone可以说是一个“阉割版”的TrustZone。因此，针对Cortex-M系列处理器，常见的硬件侧信道攻击不管是功耗分析还是计时攻击抑或是故障攻击，同时还包括我们此前介绍过的SRAM老化攻击【[G.O.S.S.I.P 阅读推荐 2023-10-23 UnTrustZone（续）](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247496523&idx=1&sn=b20128c665183038eb911639494a137c&chksm=c063dd92f7145484862a95026cbc5919387dd4d33453b740ec6b13a57bbd32e927da913d8def&scene=21#wechat_redirect)】都是有效的。当然，还有一些攻击是我们今年的暑期学校实践课程里面也会涉及的，大家想了解就赶紧来上海围观哦！

在政治课上，有一句经典的论断——经济基础决定上层建筑。在计算机世界中，我们可以说，硬件基础决定软件上层建筑，特别是上层的安全设计。下面的图中展示了作者收集的1797个固件分别采用了什么样的操作系统设计，但是这幅图并没有展示这些不同的设计在1797个固件中的分布。实际上，图中的（a）也就是bare-metal or unikernel这种设计是所有1797个固件中的99.44%的设计选择，也就是说，这些固件里面的代码都是运行在相同的特权级别，只有0.56%的固件采取了桌面计算机和服务器的设计，把应用代码和内核代码分别运行在不同的权限级别中。至于其他的一些类别的设计（图中的（c）到（e）的设计），目前只能在一些研究项目中看到，在真实世界的固件中并没有发现有使用的迹象。由于权限划分和隔离都没有做好，很多运行在Cortex-M系列处理器上的系统彷佛处在上个世纪，对经典的软件安全漏洞例如stack overflow都没法很好的防御（没有canary，甚至允许stack上的数据被当成代码执行）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgVj6A00FXwLtu2YVvbdBwJjGQkt8GY6R5jhqM7AhzqLutibyVcjIrGPw/640?wx_fmt=png&from=appmsg)

在系统层面，和Cortex-M系列处理器相关的代码已经缺乏很好的安全防护机制，那么在应用代码层面，安全现状又怎么样呢？作者把2017年到2023年间各种和Cortex-M系列处理器软硬件相关的CVE都整理在下表中，可以看到除了vendor和OS相关的问题，很大一部分问题出在了TLS库（实际上就是专门针对嵌入式的Mbed TLS和WolfSSL这两个）里面。当然，我们相信肯定还有很多第三方库的问题被引入到固件里面，只不过可能是因为它们并不是专门针对嵌入式或者Cortex-M系列处理器设计的，所以可能没有统计进来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgBQ0fJx07C3OltFxXUxsFK7FoaOXDyF1Qe2tfaZW6sWaLTK0jHJ9zNw/640?wx_fmt=png&from=appmsg)

针对这些CVE，作者也调查了它们涉及的代码缺陷的类别，这里面很大一部分是Validation类型的问题，也就是对输入输出数据没有进行严格的检查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgRT88kAOLZuoibVEtZEPKwz4ZjWg5IL38BHPoxt0ENSEcxKvmVIaeNMA/640?wx_fmt=png&from=appmsg)

最后，作者把Cortex-M系列处理器的安全设计的不足之处和现阶段各类研究工作进行了关联（下图是high level的示意图），具体涉及到的各项研究工作（特别是一些防护性的研究）都在论文第六章进行了详细的讨论。大家感兴趣可以去看看原文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgSRNFsFF9RmE7ich3wuhfKZHEZAsOY0Mw1Qdg0C5WoicfRWOX1icx5bu5Q/640?wx_fmt=png&from=appmsg)

本文调查的此前一些涉及Cortex-M系列处理器安全的顶会论文也在论文的Table 5中进行了罗列，这个表格对想要了解这个领域研究工作的同学来说是一个非常好的guideline！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hx2XIicf9E3BQicSHTS1CDLgdkupZHNFjITUUl7AphcdoVT1lACDM4tAFVdxAbQxOxSbPHAGice0BEw/640?wx_fmt=png&from=appmsg)

---

> 论文：https://arxiv.org/pdf/2401.15289
> Artifact：https://github.com/CactiLab/SoK-Cortex-M

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