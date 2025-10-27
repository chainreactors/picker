---
title: G.O.S.S.I.P 阅读推荐 2024-08-12 影子写手
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498643&idx=1&sn=96fa8a0cba660f82c56fb2f78d5cdc0f&chksm=c063d54af7145c5c38816878b9bd8ae7d59039fe34e7ef5f80be68342b797efa5d90afc0bebd&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-13
fetch_date: 2025-10-06T18:06:47.851259
---

# G.O.S.S.I.P 阅读推荐 2024-08-12 影子写手

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDibkEAfQFHNX8QASdAuGic4mzpFwAiciaRhK6kflzucy1pykGG40VhmjKRg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-08-12 影子写手

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDg9pLWHUZSiaqazrCShSWprwabYgHn8hHJGfurRAWVzOkUSXBRe0feoA/640?wx_fmt=png&from=appmsg)

2012年有一部很吸引眼球的电影上映，那就是由两大型男——“007”皮尔斯·布鲁斯南和“欧比旺”伊万·麦克格雷格联袂出演的《影子写手》（英文片名叫做The Ghost Writer），这是一部现实主义风格的虚构电影，里面小有一点阴谋论，非常好看，如果你没有看过可以去找来看看（当然你也可以因为这部电影的导演是罗曼·波兰斯基而杯葛它）。这部电影和我们今天要介绍的内容有什么关系呢？我们今天要给大家介绍的Black Hat 2024上的论文*RISCVuzz: Discovering Architectural CPU Vulnerabilities via Differential Hardware Fuzzing*中，作者发现了一个影响RISC-V处理器的超高危漏洞，就把它命名为了“GhostWrite”，也许是在向天行者的老师致敬？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDQBEv73JzUhGuOu2cdmUGX6OBAwLUCroFaETkHGrYzc6d3sXxMiaUxlA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDRoIickxzR4XgdJSvbyKUWuVtd6NVKYzADv7n8ibZSrS5o1P0Fib2hQ22g/640?wx_fmt=png&from=appmsg)

这篇论文讲了什么呢？简单的说就是用差分测试技术（differential testing）来对不同的RISC-V处理器（真正硬件实现了的产品，不是纸面上的）进行测试，让它们执行相同的指令，比较大家运行结果的差异。这种测试技术除了用来测试CPU，也广泛应用在各种各样的软件产品测试上（只要是大家都喜欢重复造轮子的地方都可以用）。关于特定硬件指令集的执行差异这个问题，你甚至可以去稍微考一下古，从2009年的ISSTA和2012年的ASPLOS这两次学术会议上就能找到相关的研究论文（*Testing CPU Emulators* @ ISSTA和*Path-Exploration Lifting: Hi-Fi Tests for Lo-Fi Emulators* @ ASPLOS），拿模拟器来和真实的CPU进行对比测试。

时间快进到了2024年，拿着锤子到处找钉子的研究人员，终于等到新的硬件架构了：RISC-V热闹了这么多年，现在总算有一些厂商开发出来商用处理器，于是本文的研究人员把平头哥的玄铁处理器（C906/C908/C910三款）和SiFive的U54/U74处理器拿出来进行了测试，当然也不忘致敬一下前面提到的ISSTA和ASPLOS论文，顺便也测试了QEMU的4个不同的版本（6.2.0，7.2.0，8.2.2和9.0.0）。至于测试的工具，就是论文里面介绍的`RISCVuzz`这个工具，不过我们并不打算多介绍工具，因为本文或者说这项研究工作的重点是作者发现的一个很有意思的漏洞——GhostWrite漏洞，我们直接快进到这部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDVg1vvgP0FbumLjibX15AcZzdlo7WKbfCMOP5LmMjbc9TTRtwbkydtiaQ/640?wx_fmt=png&from=appmsg)

先看一下如下的视频：

怎么样？看起来是不是小有一点震撼？或者说完全看不懂。我们先提一个问题，如果你突然有了任意物理内存地址写的能力，你能做什么？

乍一看，这个好像有点奇怪，现在已经是2024年了，又不是1984年人人都在用DOS的年代，现代计算机系统里面哪里还有物理内存这种概念容身之处，除了上OS课程以外，平时你用10000个小时的计算机是不是都看不到一个物理内存地址？可事实上，能够破坏计算机世界的“物理定律”，就必然有办法成为那个宇宙中的超人，再来看下面的一段视频：

上面所有的这些演示，实际上全部出自一个微小的问题——在特定的RISC-V处理器（说的就是你，玄铁C906/C908/C910处理器）中不知道出于什么原因，莫名其妙地有这么一条指令`vse128.v`，它不会把操作数当成虚拟内存地址处理（不作任何翻译），而是直接把这个地址当成物理内存地址来用，于是通过它就可以实现任意物理内存地址写，并且不需要任何特权。于是乎，一个普通的用户态程序就可以从这里出发，直到最后获取整个系统权限。至于这个exploit到底怎么做的，**我们后续会出一个特别版的解释**，欢迎大家关注~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDgGUjWyPvicDQKUwYibfZMXssZH4ectJCmKyJECGw43Xx5ibPib1FvHmh7w/640?wx_fmt=png&from=appmsg)

至于作者是怎么发现这个问题，实际上就是给CPU提供各种奇奇怪怪的opcode，然后去看哪些undocumented opcode能“悄悄”产生效果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDxIdAfpXiavlpevYia1tHftTQYjVMp4PC4lDkmUYw9uXUj16UPXKiczn5w/640?wx_fmt=png&from=appmsg)

最后作者还吐槽了一下“你们这些号称开源的处理器也不够透明啊”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GZ6Y8VbYY2uOicXPyzr0UqDRyu20Eic0ibxxRQYxtnSae3w1tAMCpmKtukHdCpibtIZfAYPu8UqRGPvQ/640?wx_fmt=png&from=appmsg)

作者提供了GhostWrite的PoC exploit代码，大家可以去研究一下：

> https://github.com/cispa/ghostwrite

---

> 论文：https://ghostwriteattack.com/riscvuzz.pdf
> 网站：https://ghostwriteattack.com/

预览时标签不可点

修改于

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