---
title: G.O.S.S.I.P 阅读推荐 2025-02-13 征帆何处客，相见还相隔
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499717&idx=1&sn=3f9fc817ce266fb8581850e82bdd86b9&chksm=c063d11cf714580ae367bd7457a3a9b316077f9e3c7300fc2b4de301539b490fffe764186b8f&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-14
fetch_date: 2025-10-06T20:37:24.220033
---

# G.O.S.S.I.P 阅读推荐 2025-02-13 征帆何处客，相见还相隔

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTjibWUC7WEeBcNLicr609nSI5537yYDIkU04GxfZECiaAL8YMAOMGibTWIA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-13 征帆何处客，相见还相隔

G.O.S.S.I.P

安全研究GoSSIP

图片来源：ARM官网
![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTsUtMA9azlN44whicoOMSJp63p8Eyd32Afu3MrGKnvQGpyItZC3vcknw/640?wx_fmt=png&from=appmsg)

（西方）情人节就要到了，热恋之人最怕的恐怕便是不能相见，可是我们搞安全防护，每天都要考虑isolation，去年我们推送了好几篇关于隔离防护的文章，今天我们也要预热一把“死死团”，再来介绍一篇关于硬件隔离机制的综述性论文、来自USENIX ATC 2024的*Limitations and Opportunities of Modern Hardware Isolation Mechanisms*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTuHWJgSlWW16SkN3l4LAD2kkNgY9ibxhd1vnYNFUenRYVaS7HUTf5ttA/640?wx_fmt=png&from=appmsg)

这篇研究工作由来自犹他大学的研究人员完成，详细评估了 **Intel MPK、ARM MTE、ARM PAC、ARM Morello** 这四大硬件隔离机制的全面测评~ 想要知道到底各家隔离机制有什么优缺点吗？那就跟着我们进入到今天的阅读推荐详细内容吧！

首先要强调的是，虽然作者测评了四个不同的硬件隔离机制，但是并不是要去直接比较它们，因为它们其实并不完全是同类型的技术（请大家去找AI帮忙学习或者复习技术细节）。Intel MPK和ARM MTE关注的是对内存的区域隔离，而ARM PAC则是对指针（其实也就是内存地址这种特定的数据）的完整性保护，至于ARM Morello，它是ARM基于实验性的Capability Hardware Enhanced RISC Instructions安全架构来构建的安全平台，我们差不多是在整整两年前介绍过，参见【[G.O.S.S.I.P 阅读推荐 2023-02-08 CHERI](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494070&idx=1&sn=261aa305049086909f930224247c32bc&scene=21#wechat_redirect)】。

既然不是为了~~拿自家的孩子和别人家的孩子~~比来比去，作者在论文的第三章着重讨论了隔离防护需要重点满足的特性和挑战，包括：

1. 硬件内生的隔离机制：像基于内存段（segment）和页（page）的隔离，天然不需要程序代码本身去做什么检查，而是由CPU在访存时触发特定的访问异常，这种就属于硬件内生的隔离检查；如果需要软件代码额外做一些检查，那么基本上肯定是会有运行时开销过大的问题；
2. 隔离区域（domain）的快速切换机制：这个在很多论文和技术报告里面都讨论了无数次，硬件辅助的隔离机制里面最重要的一点就是要在不同的权限级别之间能够快速切换，如果切换的开销太高，那么又要回到“太慢不用”的老问题上；
3. 跨隔离区域的数据传递问题：嘿嘿这个问题其实在隐私计算领域更受到关心对不对？大家都在关心哪些数据能够“出域”，而在体系结构安全领域，数据传递主要关注的是不同的I/O子系统之间的数据如何共享，最好能做到zero-copy（而不是每次传递都要复制和检查一遍），但是这种共享又牵涉到不同子系统的权限问题，很难做好；
4. 权限的动态调整：在实际运行中，另一个让人头疼的问题是对不同的区域和其绑定的实体，其权限不可能一成不变，而如果发生了权限的调整（或者因为数据传递而导致敏感数据进入了访问权限不同的区域），那就意味着需要持续跟踪数据的流动（也就是要插桩监控整个程序），想想这个复杂度就很可怕。。。

作者在论文第四章里面，通过结合Intel MPK、ARM MTE、ARM PAC、ARM Morello，分别开发了一系列的隔离原型系统，来讨论这些硬件隔离机制是如何各有千秋。由于这些原型系统基本上都只是按照相关硬件隔离机制的特点来实现的，并没有像很多论文一样对其进行扩展（例如libmpk这种对MPK机制的扩展），因此论文的重点便是后面的测试部分。作者首先测试的是在不同硬件隔离原语加持的情况下，性能的开销情况。由于MPK是x86/64架构而其他三项技术是ARM独有，因此作者分开进行性能的测试，下面的三幅图给出了开销数据。注意到由于MPK、MTE和PAC本身并没有去进行control flow的检查，因此作者不仅测试了naive的情况（单纯只用这些硬件原语实施隔离），同时还在部署了Google Native Client（NaCl）这个沙盒（以前用在浏览器里面提供对优化生成的native code的隔离，后来被弃用，转到WASM方向）的情况下进行了性能测试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTr8vm1Nx8Dmb1NdibKVuGPauppuKEEm7MCgQ7bChXevz5q1muzNkZbFA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTNIZzOaCah5WtYy35bmAKASgTZH9r2YKEYMXN40PpG84FZq2LQSmEhg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTTkrS6pHBTuTHurCPbTibicIgHGFcianuedV0YcusbZQqdBhBibORsQROMQ/640?wx_fmt=png&from=appmsg)

上述测试的基本结论大体上可以概括成两点：

1. 单纯只用硬件隔离原语是非常高效的（几乎不到1%的额外性能开销），但也缺少了很多高级的功能，特别是很多时候大家写论文都会假定CFI之类的安全检查和基于硬件的安全隔离是正交的（也就是做完了硬件级的隔离防护，再做软件级的安全检查），而一旦引入了软件检查，即使是充分利用到硬件原语，开销都至少超过17%，像PAC这种遇到指针就检查的，overhead更是直接飙升到差不多100%；
2. CHERI架构（也就是Morello开发板）加持的防护，基本上和不开防护的性能差不多，这个既可以解读为好消息（CHERI架构可以安心用上防护，把拔麻蚂再也不用担心内存安全问题啦），也可以解读为坏消息（CHERI架构原生性能就一塌糊涂，在各类测试项上，同为2022年出货的Pixel 7搭载的ARM芯片相比Morello开发板，性能优势达到了1.1倍至2.5倍不等）。

作为一篇USENIX ATC论文（更加偏向体系结构），作者必然需要深入去探究一下到底上述的结论中的第一点，于是他们去详细分解了使用软件插桩进行各种检查时，原子级别的操作的开销，如下列各图所示。其中最大的开销来自于**插桩代码获取访存操作涉及的地址信息**这一步骤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTypicibyFlYhX3uGNw4uqJqEaYXMP3lZQGuHTmuW3GJtnHvxTPhsDwlGw/640?wx_fmt=png&from=appmsg)

接下来，作者还比较了不同的硬件原语在切换子系统的时候的开销（和理想情况——也就是只花一条指令就能完成权限域的切换——相比），目前的所有硬件原语都还有比较大的overhead（不过那个理想情况也过于理想了。。。）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTV6WpLN1eM2W7cmZMZLNIr71GeumS4BhPfjPXtSRZa2EOozic1iaIOc6Q/640?wx_fmt=png&from=appmsg)

对于不同隔离区域之间的数据传输，不同硬件原语能够提供的便利性完全不同：MTE这种需要对内存地址的标签进行全面更新的操作，基本上就和重新复制一份（memcpy）是一个性能级别（开销随着数据规模的增长而线性增长），而其他的原语就可以提供常量时间的开销：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTjUU3iax8jUyMZbIxO6CLe0esVxYaLpwuwGgmwhkmvD20nPAHWLanOUA/640?wx_fmt=png&from=appmsg)

最后，作者还找了一个2022年的新SFI系统——Segue来和NaCl对比（估计审稿人要求？只针对x86平台），针对FFMpeg这种真实的应用进行了性能测试，这个比较似乎最突出的特征就是证明了这个Segue方案还蛮厉害的……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E1H2rGLACwib1FWqiafryHWTkz32Yr22micmWkatYsnKELMyevTbMC1JBcXibsqyMlMA4fpTaz8pzeFg/640?wx_fmt=png&from=appmsg)

好了，祝大家在即将到来的情人节幸福美满，甜甜蜜蜜 ~~当然要选择好最优的隔离防护方案~~！由于今天这篇论文偏系统向，从安全研究的角度，我们的G.O.S.S.I.P 阅读推荐指数为：

> Weak accept

---

> 论文：https://mars-research.github.io/doc/2024-atc-hw-isolation.pdf

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