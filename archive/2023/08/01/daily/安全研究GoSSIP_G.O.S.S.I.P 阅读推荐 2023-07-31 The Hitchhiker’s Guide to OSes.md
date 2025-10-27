---
title: G.O.S.S.I.P 阅读推荐 2023-07-31 The Hitchhiker’s Guide to OSes
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247495945&idx=1&sn=fde823e46d184d89255bfbcf35706a28&chksm=c063dfd0f71456c6fde4e2fa30c9767204dfd21efa11082569ebcd3d011472ca1cba578e1f5f&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-08-01
fetch_date: 2025-10-06T17:02:33.584831
---

# G.O.S.S.I.P 阅读推荐 2023-07-31 The Hitchhiker’s Guide to OSes

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTN2vqKTdXnLedO2Wg2OATF5en1m8BmCPbSYHcqw73QvOrjA9lwLga2Q/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-07-31 The Hitchhiker’s Guide to OSes

G.O.S.S.I.P

安全研究GoSSIP

本来最近过度疲劳，不想再写阅读推荐，但是迫于看到的这个太好笑了，必须要写一下。今天给大家介绍的是南京大学的B站网红操作系统课程主讲人蒋炎岩老师。他在B站的ID叫做“绿导师原谅你了”，这个名字实在是太搞笑了吧哈哈哈哈哈哈哈笑到停不下来，为什么会有这么可爱的老师哈哈哈哈哈哈哈哈！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTOicsJbM14HGko7VJDH29INoLMicncUGiaelmiaVObYjjwcvd0e7u9KnXAw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTzbbHqkaAOV75vARUicR0iaIzTeVTRu5pxX0j2kXLxEz29FwKrdY8tCfg/640?wx_fmt=png)

可爱的蒋老师今年在USENIX ATC上有一篇solo的论文——*The Hitchhiker’s Guide to Operating Systems*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqT7kyVgibKaug3hosbEcMSdicpIlTSz8NM0mQA5ZyDBjhBfzDOnIgwdcyA/640?wx_fmt=png)

为什么会有这么一篇论文呢，首先我们发现，蒋老师在南大开设的《操作系统》课程非常难受欢迎，引用一下网友评述：

> 这门课的讲授思路也非常有趣，蒋老师先从“程序就是状态机”这一视角入手，为“万恶之源”并发程序建立了状态机的转化模型，并在此基础上讲授了并发控制的常见手段以及并发 bug 的应对方法。接着蒋老师将操作系统看作一系列对象（进程/线程、地址空间、文件、设备等等）以及操作它们的 API （系统调用）并结合丰富的实际例子介绍了操作系统是如何利用这系列对象虚拟化硬件资源并给应用软件提供各类服务的。最后的可持久化部分，蒋老师从 1-bit 的存储介质讲起，一步步构建起各类存储设备，并通过设备驱动抽象出一组接口来方便地设计与实现文件系统。我之前虽然上过许多门操作系统的课程，但这种讲法确实独此一家，让我收获了很多独到的视角来看待系统软件。
> https://csdiy.wiki/操作系统/NJUOS/

大概蒋老师看到这个评论，觉得值得把“程序就是状态机”这个概念推向全世界，于是就有了USENIX ATC的论文。在论文的Intro部分，作者直言不讳：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqT6ncZ4OdYfYicgsr4IBNl8iaEBrZN1rEBsRkN2ibvto9UNlFWvDF7ltEsA/640?wx_fmt=png)

不管你在B站上有没有一键三连过蒋老师的课程，先让我们进入这篇论文，看看里面的细节吧。在这篇论文中，蒋老师把state machine的概念和OS的各种状态切换相融合，由于state machine这个概念相对传统的操作系统来说既精简，定义又比较严谨，因此可能更适合用来刻画OS，而且经典的system call（如下表）大概都可以被视作某种“状态转换”的操作方式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTibX04tdicYdFiboibAOIQe6sorfmBSibLjtYpF3TPI2jZcWb0529fC6sq1A/640?wx_fmt=png)

在这个哲学理念的支持下，我们学习OS可以不再遵循传统的理解思路，而是把系统当成是一个对不同state进行管理的“管家”（state machine manager），而那些针对程序的debugging、tracing或者profiling行为，都可以视作对程序执行过程中不同的state的观察：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTPCD5vibvHYZ8duv30uQoN24F2dpxias6picAxrIEGPtj35MK5qDJE30yw/640?wx_fmt=png)

本文另一个很有意思的内容，是用Python来开发了一个模拟执行的模型——Executable Operating System Model，这个建模的具体过程，大家可以到蒋老师的网站上去看看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTR85ezuO1r7fibjzibFNKNkyWjBy12hdCYwLg3VUDTeLibFdRSrHSiaTkicQ/640?wx_fmt=png)

> http://jyywiki.cn/OS/2023/build/lect4.ipynb

而且蒋老师还设计了一个叫做MOSAIC的model checker，你不仅可以在前面的那个模拟执行模型上编写各种系统相关代码，还可以用MOSAIC去检查你这个代码的状态转移，甚至发现各种问题（例如TOCTTOU安全问题）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTibMXxqkhBQw1zSia4LZ9WUoQ8Zog5B954c1kdqfukDLgurdp3an4vMiaQ/640?wx_fmt=png)

> https://github.com/jiangyy/mosaic

在蒋老师的整个课程中，我们看到了如下图所示的概念理解架构，看到这里，编辑部都想重新回炉去学习下OS，年轻一代的计算机学子真是很幸福。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H5NPl75LF6Hn51uIAhwFqTZvuqgEyOIbvtW86NE0mxhj92fUjPoRDkcpMUjQZvibBPpOOZ0iaiafTIw/640?wx_fmt=png)

最后的最后，要小小吐槽一下，作为一个世界级的网红研究人员，居然不知道给网站用上HTTPS，差评！

> http://jyywiki.cn/

---

> 论文：https://www.usenix.org/system/files/atc23-jiang-yanyan.pdf

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