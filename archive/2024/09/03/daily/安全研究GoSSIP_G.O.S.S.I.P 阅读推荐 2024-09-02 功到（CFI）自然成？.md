---
title: G.O.S.S.I.P 阅读推荐 2024-09-02 功到（CFI）自然成？
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498805&idx=1&sn=430a24d97ae0f68bed7e52443d5ba46b&chksm=c063d2ecf7145bfa588072e071af04b1808fc78cf5e7bc1a73d869ef13cf43bde796fbdf90cf&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-09-03
fetch_date: 2025-10-06T18:26:17.458601
---

# G.O.S.S.I.P 阅读推荐 2024-09-02 功到（CFI）自然成？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21F30VOnCMfpUJHFkAqpOp33IHKO01SiaWnYmYK4b9Z1nTr80OzuiaibJRQY4ibI4Orrdibia65iagwGPnsTg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-02 功到（CFI）自然成？

原创

G.O.S.S.I.P

安全研究GoSSIP

现在是2024年，距离Robert Morris利用栈溢出来劫持控制流已经过去了（不止）36年，Aleph One那篇著名的*Smashing the Stack for Fun and Profit*已经发表了28年，而学术界针对此类问题的防护，从1998年开始（第7届USENIX Security会议上的*StackGuard: Automatic Adaptive Detection and Prevention of Buffer-Overflow Attacks*）到2005年CCS会议上正式提出控制流完整性也就是我们今天已经熟知的Control Flow Integrity（CFI），也已经有超过20年的时间了。从卢瑟福开始研究原子模型的1909年到1945年最终实现“三位一体”核爆实验也就36年，我们今天就要看看到底人类有没有利用CFI来征服控制流劫持攻击：在今天推荐的这篇WOOT 2024的SoK论文*On the Effectiveness of Control-Flow
Integrity in Practice*中，作者带我们一起检查了CFI的最新应用现状，并且告诉大家，我们并没有征服控制流劫持攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F30VOnCMfpUJHFkAqpOp332Q2nOrGCliatonHMeUm0hrTfDYWMa3GYcKupBm5mUiaCl2aA7h8iaFbkQ/640?wx_fmt=png&from=appmsg)

作为一个已经发表了超过700篇原创内容的技术公众号，我们真的不可能再去讲述控制流劫持攻击和CFI的背景知识了（再说了AI技术都这么发达了，不懂就学，不会就练）。直接进入主题——本文针对如下一些2024年已经比较成熟或者普及的软硬件CFI方案进行调研：

1. LLVM编译器内置的Clang CFI方案：主要应用于Android和Linux内核防护；
2. Windows Control Flow Guard（WCFG）和它的后继：eXtended Flow Guard（XFG），主要用于Windows平台代码防护（废话）；
3. ARMv8 Pointer Authentication（PA，2016年开始在ARMv8.3-A指令集中增加的硬件辅助的安全防护）以及后续的Branch Target Identification（BTI，2019年于ARMv8.5-A指令集中增加）：这两项硬件级防护技术已经得到了Apple家的操作系统（从A12那一代的CPU开始，然后M1及后续的苹果家芯片都支持，因此iOS和macOS都得到了防护支持）、Android和Windows的使用，而且如果你做点扩展功课，就会发现从2021年开始，更多用于低功耗嵌入式的Cortex-M系列处理器也开始拥有这类特性——从ARMv8.1-M指令集开始也支持PA和BTI了；
4. Intel家的Control-flow Enforcement Technology（CET）：在2017年前后就提出，不过直到2021年11代处理器开始得到Windows和Linux的广泛支持。

当然除了这几个最主流的CFI软硬件防护方案，还有一些其他的方案，作者在论文表格里也简要介绍了一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F30VOnCMfpUJHFkAqpOp33qXT5iaich8WicVjY5LZPv31aib3K70sq1GruPornBIt1SNXpGPgJOEf0sA/640?wx_fmt=png&from=appmsg)

论文的第二章和第三章比较粗略地把CFI的一些设计考虑和已知的攻击都过了一遍，然后就进入到比较关键的第四章——对于目前使用最多的几种CFI方案的核心设计理念的介绍。介绍首先将CFI分为两大类：forward-edge和backward-edge CFI，前者主要防护那些滥用函数指针进行间接跳转的情况，后者主要防护的是利用返回地址实施各种return-oriented attack的情况。

在对forward-edge CFI方案的讨论中，首先是对于LLVM CFI和Windows平台的WCFG和XFG的介绍，对于这两种纯软件实现方案而言，最关键的设计在于你不能在静态分析阶段就把间接跳转（indirect call）的所有可能性都算出来，否则其实算是完美解决了指针分析，那么要给定一个什么样的“许可”策略才能够既保证运行时效率同时又尽可能避免攻击者绕过呢？两家CFI都不约而同考虑了一种type-based policy，也就是首先要求间接跳转必须要跳转到已知的函数入口，同时根据编译期信息，分析这个间接跳转的指针类型和跳转地址的函数类型是不是属于同一类，如果违反了这个策略，就视为安全攻击。而基于硬件特性的CFI防护，由于硬件本身不可能提供太多的存储资源，因此所设计的policy不太可能很细粒度（当然像PA这种每个指针里面拿了一部分冗余的地址来做辅助标记的除外），但是硬件的好处就是快啊，很多时候大家觉得CFI部署上去性能损失太多，这时候硬件加速的优势就体现出来了（虽然防护没那么全面，挡住一部分也行）。而且最近几年太多的研究论文在基于原来很简单的硬件防护原语的基础上，进行了一系列的扩展，把防护玩出花来了的情况也挺多的（特别是在体系结构的会议论文中）。

对于backward-edge CFI方案，大家的思路基本上就是考虑用shadow stack（不管是软件还是硬件实现），在ARM和在x64平台上，不管是用PA还是用CET来作为原语，对return address是否被篡改进行校验，都是高效而且比较容易理解的方法。

论文最有价值的部分，应该是第五章——对于各个平台上部署CFI情况的实际分析。作者首先分析了Android平台的情况：由于AOSP已经全面使用LLVM来进行编译，因此其实就是对LLVM CFI的实施情况的调研。作者分析了33个不同的Android固件包，除了Pixel 7的AOSP官方固件包（Generic System Images、GSI）以外，还有Samsung Galaxy S22、Xiaomi 13、Vivo V25、Oppo Reno 8 5G（看起来国产手机已经基本上走向世界了，记得2017年去美国的时候，商店里面除了三星就只有LG和SONY的机子）的固件包，当然作者还把号称支持隐私保护做得很好的GrapheneOS为Pixel手机定制的固件包拿来一起分析了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F30VOnCMfpUJHFkAqpOp33STwm7EVBfdDlwMYAkv1j6zTQU44ANjFIcmsS5ibQnZE50bgxYdXpCIg/640?wx_fmt=png&from=appmsg)

经过上图的分析流程之后，作者发现，在Android固件里面还有很大比例的二进制代码并没有被CFI保护，下面的表格展示了各个类型的可执行文件中使用CFI保护的情况，看起来做得最好的是小米13的系统，而OV两家似乎就很糟糕，当然Pixel 7自己家也不怎么样，至少比不过三星。而且这里面有一个很大的问题是对库文件缺少CFI保护，特别是shadow stack的使用上，几乎所有的库文件都默认忽略了这一项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F30VOnCMfpUJHFkAqpOp33SnKvT8SG4fQ9Hg0ytNI835I4icEoLTwRIhWxxus6iaJHuFKiaiboBuCEhg/640?wx_fmt=png&from=appmsg)

接下来看看历史的进程，随着Android系统的演进，GSI里面的可执行文件使用各种防护机制的比例也在逐渐增长：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F30VOnCMfpUJHFkAqpOp335Sp4PEx3iaMdkTpOvKSaAiaFuNkRUu9icuHh7bVqNA5Z4CJ00JP61ygcQ/640?wx_fmt=png&from=appmsg)

研究完了Android，作者接下去要看看Linux和Windows平台的情况，作者首先看了一下Linux几大发行版，发现它们的内核（截至2023年9月）并没有开启（CET支持的）shadow stack和`CONFIG_CFI_CLANG`编译选项，倒是用户侧的各种程序的默认编译选项开启了Indirect Branch Tracking（IBT）和shadow stack支持，然后作者说算了吧那我们就不看Linux了……

至于Windows平台，没有碎片化了倒是好分析（当然现在不再是Wintel时代了，Windows支持x86也同时支持ARM），于是作者对于Windows 11 Insider Preview developer build 23440这个版本进行了分析，主要就是看WCFG和XFG的使用情况。从下表看来，大公司的统一管理还是不错的，没有应用CFI防护的二进制代码的比例已经低于3%了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F30VOnCMfpUJHFkAqpOp3387dyRib4ouYRcicJS0zMohaVxCF5csBT5gFgSTfDUIib2dHsdWWGN8g8A/640?wx_fmt=png&from=appmsg)

最后作者把他们的测试代码都放在了GitHub上，欢迎大家试用：

> https://github.com/seemoo-lab/woot24\_cfi\_coverage\_tools/

---

> 论文：https://www.usenix.org/system/files/woot24-becker.pdf

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