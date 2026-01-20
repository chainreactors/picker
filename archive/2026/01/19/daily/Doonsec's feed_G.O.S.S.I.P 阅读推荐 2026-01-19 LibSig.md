---
title: G.O.S.S.I.P 阅读推荐 2026-01-19 LibSig
url: https://mp.weixin.qq.com/s/DEabwHu6q18UkBhhnu5uEg
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:17.353219
---

# G.O.S.S.I.P 阅读推荐 2026-01-19 LibSig

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnicwUzicKwvGOfctPalDtGJbQM7uwpSSSMD6QhBEGPicAenmEJH4kqzwibXg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-01-19 LibSig

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

我们很少会看到巴西研究人员的论文（请纠正这种stereotype），不过今年的CGO会议上有一篇来自巴西的研究论文 *Binary Diffing via Library Signatures* 值得一读（想想当你访问这个PDF的时候它来自地球的另一端），那今天就给大家介绍这个研究工作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnicHOpiaHFKL2sntCJy66icdsvHgQeaCuibhxUxPITBG5Keb9ZHwXibxl5kbQ/640?wx_fmt=png&from=appmsg)

搞二进制代码分析（特别是patch分析）的筒子们都用过BinDiff这个工具吧，在二进制代码层面做diff一直是一个很让人头疼的研究方向，最近几年随着AI的兴起，研究技术也纷纷转向利用机器学习技术辅助的binary diffing，但是这些技术有一个共同的缺陷：如果二进制代码的发布者在编译时故意进行了编译选项的变换，或者使用代码混淆技术实施干扰，那么很多binary diffing工具的准确性就会大大降低。

在本文中，作者引入了一个特殊的概念——Library Signature，那么什么是Library Signature呢？来看一段代码示例：

> 鄙视一下巴西人的C语言老师，main函数的返回值还是void

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnico7MLMia3dhj0y4Xae4DibeAzB5nW85Lhj1aQg6AJzKTRdxM2tymNVlyw/640?wx_fmt=png&from=appmsg)

如果你熟悉二进制代码生成，那么这段C代码编译的结果在哪里你肯定不陌生：它会编译到可执行文件的`.text`段，而作者定义说，`.text`段上的代码执行过程中，对外部函数的调用序列，就被称为Library Signature：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnicib8CDPwIUEsqOHg1B87nP06yCfQqdwUFsJ2zDNMUbLLqyCicClib5rmwg/640?wx_fmt=png&from=appmsg)

听上去有点抽象，我们再看一个例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnicKLUtmBkJhLv3E6D1EctibHRGYmeCicictnFp3V4Gb45uVdfWUaJBlmZsg/640?wx_fmt=png&from=appmsg)

前面那个（写得很烂的）main函数的Library Signature就是对`atoi`、`sqrt`和`printf`的顺序调用（如上图标记）。作者把这种特征当成了代码的特定指纹，用来辅助binary diffing进行定位。

接下来，巴西作者讨论了怎么提取Library Signature，不过他们似乎觉得代码的编译、链接和加载是很值得科普的（看起来他们没读过美国的《Linkers and Loaders》和中国的《程序员的自我修养》），于是就用了一些篇幅来介绍各种外部函数导入的机制：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnicyKlibaPSb7fWhKzH46lHtcdCcaQvmaokh1EjJpA9qbBUMcicUw3zqmWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnicViceBphm20mVPwPk6riawms1TNp3puialMl0hW0gVV7BTNMPo5feic9nrg/640?wx_fmt=png&from=appmsg)

接下来，作者介绍了他们开发的`LibSig`系统，这是一个动态分析系统，有两种实现方式，一种基于Valgrind，而另一种基于RTLD-AUDIT（这个RTLD是Runtime Linker Auditing Interface的缩写）技术（听起来有点陌生，可以理解为监控动态链接库的各种函数加载的一种插桩机制），当然作者表示`LibSig`还可以用`LTRACE`（或许未来他们还会用到eBPF？）

作者表示，用Valgrind的版本能够更好处理那些不使用PLT进行linking的情况（例如用了`dlopen`），当然缺点就是慢。然而作者在Table II里面比较的时候说`LTRACE`的分析粒度更细，因为它能分析外部函数调用的参数和返回值，这就有点让人困惑了，难道你用代码插桩就不行吗（还是说你不会写这种分析代码）？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnicV26Bb7XMR1FDre00fb50uOAic5STNq3pWKSWlxibct9YjjugdAcJtlPA/640?wx_fmt=png&from=appmsg)

这篇论文比较有意思的一点是它的第四章定义了一个binary matching game（当然这个也是基于同一个研究团队在2023年CGO提出的一个Game Framework），用这个game来评估特定的binary diffing工具的有效性。但是感觉也没有什么和以往的测试有什么本质的不同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hy1LPprmGicicwkTQZhTTxnickC2eN5l3bSqKFbWmAsJqt0leCNiaw6dx7gC3uA5wLibxfNmt2FbhBXRA/640?wx_fmt=png&from=appmsg)

作者选择了CoreUtils里面的程序，除了用GCC和Clang编译之外，还使用了OLLVM和KHAOS（中科院计算所研究团队设计的一个工作，可以参考 *Khaos: The Impact of Inter-procedural Code Obfuscation on Binary Diffing Techniques* 这篇论文，ACM图书馆现在都免费访问了哦）两款混淆器。当然评估的结果都不用介绍了，肯定是`LibSig`更好，大家如果有兴趣就看看，没兴趣其实也不用去浪费时间了。

总体来说这篇工作的技术含量不是那么足，这个想法看起来有点老套，如果你不信，可以去看看G.O.S.S.I.P在2016年的论文 *Cross-Architecture Binary Semantics Understanding via Similar Code Comparison* 并对比一下，看起来是不是比`LibSig`的想法和技术更复杂呢？

---

> 论文：https://homepages.dcc.ufmg.br/~fernando/publications/papers/CGO26\_Rimsa.pdf
> 代码：https://github.com/rimsa/LibSIG
> Artifacts：https://zenodo.org/doi/10.5281/zenodo.17082032

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