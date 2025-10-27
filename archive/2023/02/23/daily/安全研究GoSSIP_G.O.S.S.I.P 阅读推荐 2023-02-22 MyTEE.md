---
title: G.O.S.S.I.P 阅读推荐 2023-02-22 MyTEE
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494225&idx=1&sn=05dce1c66858490c4fa664d6c9c2029e&chksm=c063c488f7144d9e6c6143aad8e4cb9e6e544ad34e98b136765d079b1ba68c542bd2a71a40b4&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-02-23
fetch_date: 2025-10-04T07:52:14.023857
---

# G.O.S.S.I.P 阅读推荐 2023-02-22 MyTEE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibaiciccI0TEPeibvfTQvoVNFialEia4gddXfB64rupC0vhGtkxIsOjQEGDGg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-02-22 MyTEE

原创

G.O.S.S.I.P

安全研究GoSSIP

继续NDSS 2023之旅，今天要从会议论文中给大家推荐的是一篇关于可行执行环境TEE的研究论文 *MyTEE: Own the Trusted Execution Environment on Embedded Devices*，这篇论文的有趣之处在于，作者设计了一套能够在底层硬件不支持的情况下仍然工作的TEE环境——`MyTEE`，听上去好像有点厉害对吧？那就让我们看看论文的细节

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibFw5LamaPXzh3jwvFF228apfvMX6HQhLWysTdPq0xtibZJ6Z8bt3kKBw/640?wx_fmt=png)

这篇论文的作者来自韩国的Chungnam National University（中文有的翻译为“全南大学”，有的则叫做“忠南国立大学”，是有着百年历史的一所大学），论文的第二作者Jinsoo Jang长期研究可信执行环境，发表过大量相关论文，因此这篇论文的质量也得到了保证。在这篇论文中，作者探讨了一个常常困扰低端ARM MCU的问题——由于ARM并未给产品线上所有的MCU提供TrustZone的支持，经典的TEE软件栈是没法部署在全系列的ARM MCU上的。那么，有没有可能给那些缺乏硬件安全机制支持的MCU也带来TEE的安全性呢？

作者在本文中给出了自己的设计——`MyTEE`环境，这个`MyTEE`解决了什么问题呢？主要是为了弥补如下一些硬件安全机制的缺失：在支持ARM TrustZone的硬件中，为了保证内存的隔离和访问控制，需要 TrustZone Address Space Controller (TZASC) 和 TrustZone Memory Adapter (TZMA) 的支持，同时需要 TrustZone Protection Controller (TZPC) 为IO通信建立一个安全的信道。此外，为了抵御恶意的直接内存访问（direct memory access，DMA），也需要 input/output memory management unit (IOMMU) 的支持。下表总结了一些典型的SoC上TrusZone安全机制的缺失情况（注意到本文假设ARM的secure boot机制在所有情况下都生效）：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibCpaU5EJn0nEN6EXbjFhyibHUK2DgDbnbbpQqYLKoR4Dk2e2yLSCnmXQ/640?wx_fmt=png)

作者指出，假如这些硬件机制都没有，那就让我们的`MyTEE`来取而代之吧！`MyTEE`实现了一套软件方式的安全防护（架构如下图所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ib9FRHH8jtMsDUdzMEmTOg2aGF5KCQQOCh9ExkXWuCdQLSh6PkkZB5aQ/640?wx_fmt=png)

其中：

* 为了实现内存的隔离，`MyTEE`和此前的很多防护方案一样，在页表上做文章，利用ARM的stage-2 page table（就是一个和x86上扩展页表extended page table类似的设计，都是用来为虚拟化服务的）机制，在底层实现了一个迷你的hypervisor，作为`MyTEE`中隔离TEE和normal OS的组件。当然，由于hypervisor本身也可能被软件攻击，在这个组件里面，`MyTEE`还需要进一步保证TEE的内存页面一旦加载完毕，hypervisor既不能去管理这些页面，同时这些页面也不允许被修改了。
* 为了防止基于DMA的攻击，`MyTEE`又设计了一个filter，对所有从 memory-mapped IO (MMIO) 到 DMA controller 的请求进行审查。
* 为了实现安全的IO读写（secure IO），`MyTEE`把相关的操作搬到了normal OS里面（！！），然后同样用hypervisor去保护相关的IO buffer，实现了无硬件支持的IO读写。

我们具体看一下每个部分的细节，首先是内存的隔离，这部分的设计主要考虑如何把不同的组件放在stage-2 page table的不同区域，而stage-2 page table由secure boot保证完整性。注意到在`MyTEE`设计中，OS的kernel被降低了权限（deprivileged），只有那些特定的设备驱动（负责处理相关的secure IO）才被允许获得更高的权限。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibm8xYmb8jAZQNXKdVQ6RhSl3mToJkPA7wU3nU5RnwibOHwo8AoicA9ZDQ/640?wx_fmt=png)

接下来是DMA controller上的安全过滤，作者在本文中假定所有的硬件都是安全的，因此只考虑软件层面上的恶意DMA请求。`MyTEE`监视了所有的DMA controller register，对可能的DMA请求都进行拦截（还是通过stage-2 page table控制data transmission memory的读写）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibGAVaAvibTtrtlc78zQcrMr7dflZ71IQlEBWjLyablXR9vqdcFDrKT1Q/640?wx_fmt=png)

最后是secure IO的实现，这里`MyTEE`只允许 peripheral hardware 和 TA 访问hypervisor中的特定buffer，而不允许操作系统访问。同时，临时地给予特定的设备驱动访问这些buffer的高权限（当secure IO操作发生之时）。这样就实现了一种“软”secure IO读写。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ib61Tzib3rRvx0MribK9O4kcXiblqRbzOFkaSTOk1CLicmqZFtjf2ufiaib3cQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibThpTGibc2ZTFXTOtfTvHTpVuXxTBzBzXrJB0Z5IzIk92PmeEehfPcLA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9iblZsvaCOxpquzEoC2gLoyzLhGnn4GdhoJia2tBUgos5yfpI33KEDw6kw/640?wx_fmt=png)

作者把`MyTEE`部署在了没有TrustZone支持的树莓派3上面，用来保护OP-TEE，而上层支持Raspbian OS（Linux 4.15）运行。整个开发的工作量如下表所示，看起来也不算非常巨大：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibZfML2eL1Pw6lDr6DLPpbIYHmbIuErhqvpstHC0RbRoE0KhyHyN0eyQ/640?wx_fmt=png)

在`MyTEE`的支持下，作者实现了“软安全可信”的TPM、USB键盘IO和可信显示这三个功能。同时评估了性能开销，大部分情况下，benchmark的开销增长都在1%-5%左右，这个在现实应用中是非常不错的！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibLWjvpHTJdHuIBOnEwd9awzzF5MWE1zXHfVVJ77CmdrIpia12bEsU13w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibOm5ntia1Mum2lIEbexttwvkicpafbOSHqujP7u99arT4WfrVrpXWsFjA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibTtQiaib6OF8ebjPWdyGtplSq9lagHTI6jB1r9n6sEcWPdflgXz9vicgbw/640?wx_fmt=png)

即使是对于一些外设的secure IO读写（完全由软件模拟管理，因此可能预期会有较大的性能损耗），实验数据（下面的表格）看起来也还是比较能接受的：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FSdJpo6e9SPF5Wk9405r9ibkOricbz0QNeax0FKSMdmlaA1lLLbwSicMUlScuTvPoFL1R1yMFWTNBibA/640?wx_fmt=png)

---

> 论文：https://www.ndss-symposium.org/wp-content/uploads/2023/02/ndss2023\_s41\_paper.pdf
> 代码：https://github.com/sssecret2019/mytee （目前什么也没有，骗子）

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