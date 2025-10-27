---
title: G.O.S.S.I.P 阅读推荐 2023-03-29 Hardware-assisted Fault Isolation
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494734&idx=1&sn=c32a573a4da65a44a94e6aedbd3b9660&chksm=c063c297f7144b81a1a7fe4962cc9fe387c1f17d10d42101c415596732495afc83d8bc61f5d2&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-30
fetch_date: 2025-10-04T11:08:00.383214
---

# G.O.S.S.I.P 阅读推荐 2023-03-29 Hardware-assisted Fault Isolation

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21Fd4xO6zhphzQEfibJicYxeeqqKlgibMfKpxgeeIIRDBEvwqxoHaCIMda6ITTrRGiaY4icpC8lYN3KwDFw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-29 Hardware-assisted Fault Isolation

G.O.S.S.I.P

安全研究GoSSIP

今天介绍这篇ASPLOS论文 *Going beyond the Limits of SFI: Flexible and Secure Hardware-Assisted In-Process Isolation with HFI* 的同时，顺便要提一下论文第二作者Tal Garfinkel，他作为一名从2003年开始就在虚拟化和安全隔离领域开展研究的低调技术人员（Stanford博士，VMWare初创的核心技术成员，个人网站 http://xenon.stanford.edu/~talg/ 却非常简朴），发表过的许多论文都是编辑部反复阅读的经典，例如在USENIX Security 2004上发表的论文 *Understanding Data Lifetime via Whole System Simulation*，个人认为这篇比NDSS 2005上发表的那篇 *Dynamic Taint Analysis for Automatic Detection, Analysis, and Signature Generation of Exploits on Commodity Software* 更早引领了Taint Analysis技术在随后几年的研究热潮。

20年过去了，目前身在UC San Diego的Tal Garfinkel和其他作者（包括Intel的技术人员）一起，提出了一种硬件辅助的进程内隔离（In-process Isolation）方法。由于去年G.O.S.S.I.P在CryotoMPK研究工作上的投入，导致我们格外关注此类研究。本文的风格和此前的一些研究（包括我们的研究）很不一样，它一方面将研究对象聚焦在WebAssembly（WASM）的in-process isolation上，另一方面从更加“硬核”的角度来探讨怎么实现隔离——作者从指令集（ISA）的角度设计了一套扩展指令，用来补充现有处理器在安全隔离上的不足。那就让我们来看看这套hardware-assisted fault isolation（HFI） 方案有何过人之处。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fd4xO6zhphzQEfibJicYxeeqKHdopHWROIGF5nzhZSpdhJ07LaMicIUqRrK6gVPrNOicSAYapXC9xaLw/640?wx_fmt=png)

在HFI方案中，作者有几个关键的设计考虑，第一是HFI完全在用户态开展隔离，这样方便易用；第二是HFI隔离不需要MMU的支持，直接在硬件层面上引入了名为`region`的概念，用来实现内存区域的隔离（不管是粗粒度还是细粒度都可以支持）；第三是HFI只维护了当前正在运行的sandbox的状态，而不用关心其他不活跃的sandbox，这样就可以支持任意多个不同的sandbox而不用担心状态维护的开销。

这篇论文的一个毛病是很不直观，对HFI的设计与实现用了整段整段的文字描述（作者就不能请ChatGPT帮忙画一个HFI的架构图吗）。简单来说，HFI设计允许同一个CPU上不同的核拥有自己的*HFI state*，也就是说每个CPU核上执行的代码在*HFI state*开启后就进入到了HFI的sandbox中。在指令集上，作者设计了`hfi_enter`和`hfi_exit`两条指令来进入/退出HFI sadnbox状态，在进入sandbox状态后，一系列特定的register用来控制内存访问（也就是前面提到的对不同region的访问控制）。

说到region，HFI对region的访问控制让人一下子想到DOS时代——利用段寄存器和分段机制来管理内存访问。HFI允许用户设定一个region的base address和范围，并且给整个内存设置read、write和execution属性。当用户需要新建一个sandbox时，可以按照如下步骤：

1. 为sandbox分配region：利用`hfi_set_region`指令对需要使用的region的各种属性进行设置
2. 选择不同的sandbox类型：如果是untrusted code，HFI启动的是native sandbox，限制各种系统调用的同时，也对各种region register设置只读属性；如果是trusted code，则启动hybrid sandbox，允许代码操作region register
3. 保存进入sandbox之前的context
4. （可选）设置exit handler：允许native sandbox在退出时候调用一个特定的exit handler函数来检查执行状态是否正常

如果sandbox在执行过程中正常使用`hfi_exit`退出，或者执行system call时候触发了sandbox退出机制，HFI机制都没啥问题。但是如果sandbox中的代码在运行时遇到代码异常错误，处理器硬件机制会把错误信息用model specific register（MSR）记录下来，同时产生特定的错误信号，让OS和HFI runtime负责捕捉错误。

作者在这篇论文中显然更重视实际的实现，给出了在x86架构下如何把HFI组件加入到执行流水线的细节。下图中的绿色部分就是HFI增加的内容：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fd4xO6zhphzQEfibJicYxeeqUl4ODt6dnAAONymVFtQgPCRoRT6iacJlvp4ia0CHPo0BLuicWdUpFZMHQ/640?wx_fmt=png)

从软件层面上，完整的HFI扩展接口如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fd4xO6zhphzQEfibJicYxeeqiaGGMrcibV3dFMVHRQhUXv7LywjPIoI4ps99t8HLrjkJ4JPuaxxotJbw/640?wx_fmt=png)

由于本文发表的会议ASPLOS更关注的是体系结构，所以论文中使用了在系统结构研究领域很常用的`gem5`仿真器（simulator）来评估性能开销：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fd4xO6zhphzQEfibJicYxeeqiciaIMJD7IqUMMXArxl119MvF3tSicKhF6GUe5ndmJrhZwiamnwOSKrDIw/640?wx_fmt=png)

当然也少不了经典的SPEC测试套件：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fd4xO6zhphzQEfibJicYxeeqfHN1xNGcknLuonicNtLWeMbk3tiaf5Two6nJfHFjHLwTZyU7C0OWkkAw/640?wx_fmt=png)

值得注意的是，作者将HFI和MPK进行了对比，并指出由于HFI sandbox需要将region相关的metadata数据从内存读入到region register，所以开销会稍微增加（但是HFI可以支持更多数量的sandbox，而MPK的domain数量有限）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fd4xO6zhphzQEfibJicYxeeqde3l7uuRG26ZObXvZ5Y55VUue6S8D0uGyicA6uSyRUGd7iatjel4uYsg/640?wx_fmt=png)

如果对这篇论文的安全评估进行评价，那肯定是达不到安全研究社区的及格线，对HFI如何抵御各种安全攻击并没有详细的讨论。不过，论文作者里面有sandbox开发社区的多年老兵，也具体参与了FireFox的WASM安全隔离的设计，肯定深知不管怎么做，defense永远不可能完全防御各种各样奇怪的攻击，且看后续有什么研究成果来破解HFI吧~~~

---

> 论文：https://dl.acm.org/doi/10.1145/3582016.3582023
> 代码：https://github.com/PLSysSec/hfi-root （然而404找不到！）

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