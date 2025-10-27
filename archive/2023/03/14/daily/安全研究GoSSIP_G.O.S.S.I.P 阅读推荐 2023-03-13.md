---
title: G.O.S.S.I.P 阅读推荐 2023-03-13
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494501&idx=1&sn=1090af900d62d1b9c48f2a72ef5e8966&chksm=c063c5bcf7144caad892cb1530ea7a7b6c868a252bdc3ca1f0174b30f0e0c2ee054380034633&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-14
fetch_date: 2025-10-04T09:31:02.389804
---

# G.O.S.S.I.P 阅读推荐 2023-03-13

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66w9tvquxwhFibpO5gJP76fDCwDiaScq4fxj5ZnFL7IlH4A4sP6QUcHzcg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-13

原创

G.O.S.S.I.P

安全研究GoSSIP

今天推荐的这篇论文 *Reassembly is Hard: A Reflection on Challenges and Strategies* 来自USENIX Security 2023，是一项讨论二进制代码重编译（Reassembly，或者应该叫做重汇编？）的研究工作

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR6652o49k1CSBTdL4OdESc12vWtZE8RTAE0M5w6fDicwicx3AicmVc4yIia4w/640?wx_fmt=png)

在这篇论文中，作者主要关注的reassembly技术，特指完全基于静态分析，将已有的汇编代码先进行符号化（Symbolization，就是分析代码中所有的reference引用变量，并将这些reference转成符号的过程）之后再重新生成二进制代码的技术（见下图示例）。我们常说的binary code rewriting这一大类技术中，reassembly是其中的一个特定类别，而像binary code lifting这种技术则不能叫做reassembly，因为它在将二进制代码翻译为中间语言的过程中，并不会进行symbolization处理。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR668SEp5JGyDde4B8Brxw3oE0jticnTI60ho2lkn5WCxWG0En4HSR2r4xA/640?wx_fmt=png)

在汇编表示中，引入符号的重要作用之一是保证代码能够加载到任意内存地址，也就是所谓的Position Independent Executables (PIE) ——地址无关的可执行文件。在地址无关的二进制代码中，下面一些类型的地址信息都应该用可重定位的表达式（relocatable expression）来表示：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66Src4jM9k4f343iaUiaeHTaDHnBCAbw5pSgmJnqiaWOEhmkE3HoF8S0Eng/640?wx_fmt=png)

如果上面的表格让你觉得太抽象，那可以看看下面这个代码示例。在图中左下部分，像`msg`和`LBB0_1`这种标签在实际反汇编结果中都变成了具体的地址，同时像`putchar`这种外部导入函数在没有分析GOT表的情况下，也会显示为一个地址信息。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66WMB2eNnoo6ptIvQ1CzOPQCAP1NqOP6IaarosiaicuW7EspJyG6kwynQA/640?wx_fmt=png)

由于指令层面的反汇编基本不会有太多错误，所以整个reassembly的难点就集中在对于可重定位地址的符号化的精确度上。为了系统评估这一问题，作者设计了一个叫做`REASSESSOR`的系统，把reassembler生成的结果与编译器生成的准确结果相比较（流程见下图），这也是最近10年来很多研究工作的一个基本方法（即研究逆向工程的结果和正向编译结果的符合度）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66gNib4YuFGPczWYR2GLo3SebRTq0W0VJBge98oKB02HtzcuNdCpfVk7w/640?wx_fmt=png)

本文的一大特色是对reassembler准确度进行了分类的评估，下表是作者关心的8种符号化错误，在附录中有更为细节的描述，这里就不再展开了，感兴趣的读者可以去看看论文原文。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66ZqUrOhHicUYCVLiaXafohUibqDRPA0XhuicFph9ibxDGOBqlSviaon8QQPiaA/640?wx_fmt=png)

在实验中，作者使用了153个程序来测试`Ramblr`、`RetroWrite`和`Ddisasm`这三个reassembler工具。

* GNU coreutils (v8.30): 107 executable programs
* GNU binutils (v2.31.1): 15 executable programs
* SPEC CPU 2006 (v1.1): 31 executable programs

在生成二进制代码时，选择的编译选项包括：

* ISA: x86 and x86-64 (= 2)
* Compilers: GCC v7.5.0 and Clang v12.0 (= 2)
* Linkers: GNU ld v2.30 and GNU gold v1.15 (= 2)
* PIE/non-PIE: produce a PIE or a non-PIE (= 2)
* Optimization: O0, O1, O2, O3, Os, and Ofast (= 6)

特别地，作者指出，很多reassembler觉得一旦处理对象是x86-64 PIE，编译器就会自动把那些需要重定位的地址信息进行处理，然而实际上在作者生成的3672个二进制可执行文件中，所有的可重定位地址中有6.9%是label-relative类型的，也就是和原始汇编代码中的label（编译后就消失了）相关的地址偏移。作者指出，如果需要精确恢复这种类型的信息，就需要做好控制流图分析，这是为什么呢？

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66DoTVpxkIybhWWhm5Bj4tEZzNhuGuNllVt1eGueFpMibZH79G3RtxUmQ/640?wx_fmt=png)

要回答上面的问题，我们来看一个具体的例子，在下面的C代码中，由于使用了switch语句，汇编代码中会有一个跳转表（jump table），同时由于里面的操作也涉及到一个数组，所以实际上跳转表数据和数组数据并排存放在从0x830地址开始的数据段中。然而一旦编译完成，在分析过程很难区分出来0x830-0x83f是第一个表，而0x840-0x84f是第二个表，这时候就必须要根据代码中控制流的信息来确定跳转表的边界，而实际上作者发现，所有的reassembler都没法很好处理这种类型的代码（不过上面那个代码的风格也很奇怪，吐槽一下）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR667LHic96oHo9m67PyKKkXHaJGbMoebIVSAsUbhO315Osd3fVjWoVqElQ/640?wx_fmt=png)

总体来说，`Ramblr`、`RetroWrite`和`Ddisasm`这三个工具能够对大部分测试的对象执行reassembly操作，总体成功率都超过了90%（在处理GCC编译的binutils时候表现相对差一些）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66ib6Mo10OPbfr1XicdECB3kMz6vRvhWhBg9qHYaFJNXK2EfCavFYc5g5g/640?wx_fmt=png)

能重编译并不代表结果就是靠谱的，通过作者的分析系统一通测试，我们发现其实重编译的准确率实际上非常低（见下表，三个工具都没能突破10%的准确率）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66DvPTTHwliag1pnhKNfSV3iaTOGibIf8eAFfESDjh16icqdHbSAerjo1UEQ/640?wx_fmt=png)

当然，作者在测试中也对已有的工具进行了一些改进，比如他们给`RetroWrite`提交了一个patch，能够把针对E7类型的地址符号化的false negative大幅度降低（从280个降低到4个）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FQ0MD4aRVWicPDTo17tJR66GPYIQInlR31V8qzjHxPVjkA3TkbgJHHsHX4bVpdqKjsu1UKMPhzyibw/640?wx_fmt=png)

---

> 论文：https://www.usenix.org/system/files/sec23summer\_439-kim\_hyungseok-prepub.pdf
> 开源代码：https://github.com/SoftSec-KAIST/Reassessor

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