---
title: Off-by-One Conference 2024议题：经典目标中被遗忘的宝藏
url: https://mp.weixin.qq.com/s?__biz=Mzg4MDcxNTc2NA==&mid=2247486222&idx=1&sn=84ee657bdd47567f0be2ed63382bbed0&chksm=cf71b995f80630838bfeb750a6549e27618267d528636a28c0576ff99e9eb075a3e3a9319ada&scene=58&subscene=0#rd
source: Numen Cyber Labs
date: 2024-07-04
fetch_date: 2025-10-06T17:44:34.655973
---

# Off-by-One Conference 2024议题：经典目标中被遗忘的宝藏

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYFFn5qfcZRjqoUFv2ZpjYYutbfQVX33mTTLu6tzNgZPcIRXDJicNMlmibw/0?wx_fmt=jpeg)

# Off-by-One Conference 2024议题：经典目标中被遗忘的宝藏

原创

Numen labs

Numen Cyber Labs

## **0x00 背景**

在2024年6月26日，OFF-BY-ONE Conference在新加坡举行，我们有幸发表了题目为“经典目标中被遗忘的宝藏”的演讲。

整体来讲，这个演讲主要是讲述我们我们尝试在对一些传统的目标进行 Fuzz 的时候，由于目标已经被大量的进行了 Fuzz，我们无法很好的发现新的可利用的漏洞。所以我们改变方案，重新阅读和分析源码，寻找新的攻击面，并且尝试通过手动的代码审计来挖掘漏洞。最后我们反思我们的fuzz策略和直接代码审计时有什么不同，然后改进了我们的 Fuzz 工具，进一步发现了许多新的漏洞。

这个演讲主要由三大部分组成，分别是被遗忘的宝藏、 审计目标和增强 Fuzzers。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYFNuhBaL6GK5sibFoeBDjHrZ4gibXpTyVTouOJuXqVqkDh7fEZal6EU2qQ/640?wx_fmt=jpeg&from=appmsg)

##

## **0x01 被遗忘的宝藏**

我们都知道，在 web3 项目中，出现一个漏洞，往往会带来巨大的经济损失，所以，web3 的项目往往要求尽可能找出项目中的所有漏洞。但是传统的 web2 项目往往拥有比 web3 项目大得多的规模，所以那些被多次审计或者 Fuzz 过的代码，往往会被忽略或者说默认为安全。

所以，在这个部分中，我们主要回顾了以下一些有趣的漏洞。

* CVE-2020-15999

  图像解析 freetype 的漏洞，被多个项目使用，比如 chrome 和 android。在处理嵌入到字体的 PNG 图像时，由于把获取的32位图像宽高进行截断为16位再进行存储，并且使用16位的数据进行内存申请操作，导致后续出现堆溢出操作。
* CVE-2023-4863、CVE-2023-41064

  webp/libwebpd 的漏洞，被 Android, chrome, ios/masos 等使用。规范霍夫曼编码算法中有越界写漏洞。
* CVE-2023-0461

  Linux内核的 TCP\_ULP 模块漏洞。TCP\_ULP 没有判断协议是否实现某些虚函数，导致在使用特定的协议进行多次三次报文握手时，会出现 double free 的漏洞。

## **0x02 审计目标**

这部分讲述了我们 Fuzz 失败然后进行 Code Review 的过程，这部分由两个部分组成，第一部分是 Linux kernel 相关的，第二部分是 Android 相关的，这部分我们将只阐述其中关于 Linux 相关的内容。

在 Linux Kernel 部分，如果我们想要进行 Linux Kernel Fuzz，我们首先必须确定攻击面。我们首先介绍了 Linux Kernel 近些年常见的攻击面，分别是 ebpf、io\_uring 和 Netfilter。ebpf 由于 Ubuntu 的权限设置，普通用户无法访问，所以该攻击面不可用。io\_uring 和 Netfilter 虽然都是很棒的攻击面，同时有着普通用户可以访问以及足够复杂且多变的代码，但是由于过多人关注这两个攻击面，我们也不选择。经过多方对比，我们最后的选择是，network packet scheduler，这个模块代码可以被普通用户访问到而且足够复杂，最重要的是关注的人不多，但是同时他的缺点也明显，就是 Fuzz 时的通用性差，而且需要创建新的 Namespace。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYF6jaaOYIgUouOFiboKKd2oQE0SmMN17QrmrW5gYeC5zr1DRXmGBvTYGQ/640?wx_fmt=png&from=appmsg)

紧接着，我们介绍了 Network Packet Scheduler 的基本架构，如上图所示，在得到基本架构后，我们可以轻易的使用 Fuzz 工具比如 syzkaller 来进行 Fuzz。但是我们并没有 Fuzz 出什么有效的内容，所以我们转向了直接的代码审计。

然后我们发现了CVE-2023-35788，这个漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYFzL4WJMicLkyzlIpU7mj2jxXshEtxmgxSjwxpy6dGhPWpQMBas49iaPEw/640?wx_fmt=png&from=appmsg)

在`fl_set_geneve_opt`中，`key->enc->opts.len`被用在data数组中，而且在这之前没有进行校验，如果我们构造合适的长度，可以把后续的了`opt`的 `length`, `r1`, `r2`和`r3`字段的0写入`opts.len`中，从而构造一个 off-by-one 的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYF4MqOgccnfcMbI7Eq3wmkeBibOLE4L6qEZYVpoH5VdJl9iccK9W0frKgg/640?wx_fmt=png&from=appmsg)

这可以绕过后续的对于`fl_set_geneve_opt`的校验操作，进而进一步导致结构体内越界写。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYFmoib7jeCicsWZW1Tn4v48co6eLJESzibuB8r6NF7CnGQbKoUKHaUswdhA/640?wx_fmt=png&from=appmsg)

但是由于宏定义的限制，我们最多只能溢出128字节。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYFwApwo6TeetbAjXiafObCa2zH2zibDLQHOb4Nn9YYTib5Jk74icgVrvhckw/640?wx_fmt=png&from=appmsg)

至于越界读取，`cls_flower`本身就提供了读取我们之前传入的内容的功能，而且依赖于`len` 字段。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYFhqwdEq6gLLlxTL3yQsh4IDqRiagyOvlEWB5E8CTuTh6sDuljASa72XQ/640?wx_fmt=png&from=appmsg)

如果我们在触发结构体溢出后，继续在这个数组中填入数据，由于我们的len被修改了，我们会重新开始写这个数据的内容，经过布局，我们可以在修改部分原有的 opt 的 len，同时，在数组的末尾伪造一个虚假的 opt 结构体，那么内核会错误的以为，后续还有我们传入的数据，从而实现越界结构体内读取，泄漏之前说的函数指针。最后我们利用这个越界写入完成了对 Ubuntu 的提权。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYF64M3uq7oB84b7mNxaEZZkudhsAh9zDtiaDhfFEUNC5uQ3EOtjzx8CZw/640?wx_fmt=png&from=appmsg)

在我们发现了这些漏洞后，我们决定去增强我们的 Fuzz，来找到更多的漏洞。

## **0x03 增强Fuzzers**

我们在这部分首先介绍了失败的原因。

第一种情况是该漏洞的模型构建困难。例如，一些内存破坏性漏洞可能不会产生崩溃等直观影响。当他们写越界时，是每隔一些内存单元进行的，并且在一定概率下修改的值是不会出现错误的。

第二种情况通常在一些闭源 Fuzz 中更为常见。因为在某些情况下，代码的触发路径较多且复杂，很难在短时间内确定所有的关键处理模块。因此，大多数情况下，我们可能会更加关注早期的处理模块。

还有第三种情况的漏洞，通常是最难发现的。当多个条件同时满足时才会触发。在很多情况下，我们可能并没有真正理解解析函数所涉及的关键点。同时，在封闭式 Fuzz中，我们通常更关注早期接口参数的适配以及代码覆盖率的提升。这导致我们的 Fuzz 很难挖掘到这些多条件漏洞。

所以我们通过以下方式改进。首先是对于多层嵌套结构，我们关注Fuzz到达特定指令的效率，即我们关注我们 Fuzz 的深度而不是广度。其次我们更关注关键指令位置的路径测试，对于相同的路径，我们多次使用不同的特殊值来进行测试。总的来说，这是一种引导式 Fuzz 策略，可以更好挖掘一些被遗忘的漏洞。

最后，我们集中介绍了CVE-2024-36978。

![](https://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0dZY7rcHTOQpvgwib5IIraYF5DNf11JXGIziaTHEzsDq2FHfUfS4icOS3v0Nh2ibcFqbFJKF2dNyYVbAA/640?wx_fmt=png&from=appmsg)

漏洞发生在`sch_multiq`模块。我们可以看到在位置一，`qopt->bands`被赋值。然后在位置二，removed被申请，通过`q->max_bands`减去`q->bands`。在位置三，`q->bands`被`qopt->bands`赋值。在位置四，我们把一些多余的 qdisc 对象放入 removed 数组，然后在位置五释放。为什么位置二要使用老的 `q->bands` 申请 removed 大小，但是后面的 for 循环中却用了新的`q->bands`。这看起来很奇怪。如果 max\_bands 减去新的 bands 大于 max\_bands 减去老的 bands 的两倍，for 循环就可能越界写入一个马上会释放的堆指针。

利用这个漏洞，我们可以轻易完成 Linux kernel 的提权。

## **0x04 参考链接**

https://medium.com/@numencyberlabs/the-forgotten-treasure-in-classic-targets-94b0a71a5ec7

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0fuMDh4FsqY2dPoxib9NMic0STUiajhkIEKv0s6iaAysfnxcgpEeOiafljac3C6qx9ewaOhAoaiclpibPW6g/0?wx_fmt=png)

Numen Cyber Labs

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vlekRjgqic0fuMDh4FsqY2dPoxib9NMic0STUiajhkIEKv0s6iaAysfnxcgpEeOiafljac3C6qx9ewaOhAoaiclpibPW6g/0?wx_fmt=png)

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