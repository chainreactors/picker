---
title: G.O.S.S.I.P 阅读推荐 2023-03-27 Syscall Integrity
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494700&idx=1&sn=30371fd804f3e69c40cf8c10a77e8694&chksm=c063c2f5f7144be3967be40a566378e46dcd71c4f98fb36c3b459e316c11bf6d2aeceeffe5b1&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-28
fetch_date: 2025-10-04T10:53:23.363412
---

# G.O.S.S.I.P 阅读推荐 2023-03-27 Syscall Integrity

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3Gt8B2puZX55G917WM9lnhEfBPQ3ibUNaSSicb4cSAXzBAWHBXiadiaB43cQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-27 Syscall Integrity

原创

G.O.S.S.I.P

安全研究GoSSIP

安全研究社区早在20年前就提出了control flow integrity（CFI）的防护概念，但是这么多年下来CFI叫好不叫座，因为程序里面实在是太多复杂的执行情况没法提前预测。今天我们要带大家去到本周即将在加拿大温哥华（这里吐槽一下当年潘爱民老师翻译的《计算机网络》那本书里面把温哥华翻译成“范库弗峰”，因为那时候的金山词霸不知道为什么就是把Vancouver解释为这个名字）召开的ASPLOS，在security session中的一篇论文 *Protect the System Call, Protect (Most of) the World with BASTION* 提出的`System Call Integrity`（SCI）的概念

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GunVuwMWhYKr7CYrQMWIFicxVbMGAFBllEy4hIknpjsG6FIxn1nicvOUQ/640?wx_fmt=png)

我们知道，很多时候安全防护都希望做到尽善尽美，但是理想很丰满，现实很骨感，实践中往往只能退而求其次。本文作者认为，我们既然做不到精确控制所有执行路径，那么可以针对安全攻击的关键步骤——system call调用进行安全审查。作者对system call调用的上下文（context）提出了更为严格的约束和检查，具体关心如下三类context：

1. Call Type: which system call is called and how it is invoked
2. Control Flow: how a system call is reached
3. Argument Integrity: arguments are not corrupted

当然，上面这些约束太泛泛而谈了，先看看作者设计的`Bastion`系统——包含了编译期增强和运行时动态检测功能、能够实现SCI的一套系统。首先，类似容器中对system call调用的约束，`Bastion`系统也会首先阻止所有非必要的system call调用；同时作者还观察到，system call很少被间接调用，大部分情况下都是显式地直接调用，因此`Bastion`系统对indirect system call invoking也会严格审查。其次，在运行期，`Bastion`系统会动态检查system call调用的control flow和参数这两项内容，确保调用依照的是合法的逻辑，且数据未被篡改（例如可能有参数注入的危险）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GvgpcOSJM2onTtggSlxosqtjQeOtgq02xE8lbAIo4vqAQUfmQEicc0Qg/640?wx_fmt=png)

作者举了两个Nginx中的实际代码示例来说明现实世界的软件中，一些关键功能往往需要用到比较敏感的system call（例如下面代码中的`execve`和`mprotect`）。而因为这部分代码是必需品，基于code debloating的防护肯定是没用的，所以必须要严格控制，否则危害巨大

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GOXwAxY3gWmWUmibcNpeJvKq7wmyESPBL6kUibV88C6rIfEyj4eiaia4NWw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3G9a6lcnI1hS82I9akRvN7DXgVyBFJrZicd7mibayYbUcOBNUYszdw5YXg/640?wx_fmt=png)

实际上，system call这种特殊的函数调用相当于主动给程序开了一个后门，作者也总结了安全攸关的一些syscall，`Bastion`系统会对它们进行重点的“照顾”：在静态编译分析期，分析总结出call type和control flow的合法范围，然后在运行时，利用`seccomp`来监控所有的system call调用，并在调用发生时去分析call stack，检查CFG是否合法。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GgjJezib2FVpZPOou5JBRGg2gZiaqgYIDibZ1EXO9ryAsJMOwrfoXBfClQ/640?wx_fmt=png)

针对syscall调用参数的完整性，`Bastion`系统首先通过静态分析，在编译期把所有和敏感参数生成相关的内存操作（通过def-use analysis，如下图所示）都进行了标记，然后额外给程序进行了插桩——任何和敏感参数生成相关的内存操作被执行时，`Bastion`系统同时维护的一个shadow memory区域也会进行更新，直到最后调用时，`Bastion`系统的运行时检查就会核对真实参数和shadow memory里面同步维护的数值是否一致，如果不一致就说明参数是被攻击者恶意操控的。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3G1y895BHfo1ZmwuOIhtFibyibx7XUV8XfCsuVFicTnYYbJFKyiaUcMNthIw/640?wx_fmt=png)

---

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GslgOG4yR4XeRoTQsRdMHsGNM4V5JxJG5pqWVIftictuDRbqlhlLOGIg/640?wx_fmt=png)

在实验部分，作者用`nginx`，`SQLite`和`vsftpd`三个有名的服务器应用程序进行了测试，在性能测试方面，作者把自己的系统和LLVM CFI进行了对比，如下图所示。这里比较令人不解的是，实验中针对`Bastion`系统的call type、control flow和argument integrity的测试全部都加上了Intel CET（也就是Intel的Control Flow Enforcement Technology）的选项，在前文中却并没有看到`Bastion`系统哪里必须要依赖Intel CET？

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GEfDJZ32uw3GLAsJYiabzK1LZPRiaNibKEyyzKaLNiaa7RxCVK1MHruc7sg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GgZVAmic9SV3xFuvgmhApE2dmRiaoBJ6hFc2OLibewibTjGPGqj659Uxymw/640?wx_fmt=png)

总之，从实际部署效果来看，SCI（还要加上CET）的性能开销基本上对生产环境没有特别的影响——作者统计认为，`Bastion`系统平均只会带来3%的额外开销。

在安全防护的效果方面，其实我们都知道这部分是很难写的，因为你很难去“证明”一个防护系统能抵挡住全部的攻击，编辑部觉得本文的第10章是一个很好的范例——如果我们审稿看到这样比较全面的比较，一般就不会去给作者挑刺了。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GFV88AOU5uvNj7DnX2wq3GfVDfOnEqxOhibY0H9VPjG69c6o9JEZPRWuiaklwfGkDyibC980rAV5ckA/640?wx_fmt=png)

最后，本文美中不足的一点是没有提供开源代码，这套系统按照作者在第8章的描述是一个中等规模（超过1万行C代码）的工程，如果能让大家一起用起来就更好了~

---

论文：https://dl.acm.org/doi/10.1145/3582016.3582066

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