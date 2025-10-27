---
title: G.O.S.S.I.P 资源推荐 2024-11-19 办公软件宇宙
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499229&idx=1&sn=425357d6ef4181bd6492c1bb710895de&chksm=c063d304f7145a12115a632c0b50b752f3142c61d5ddce189b258a9ec791f8393273c6c0e553&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-11-20
fetch_date: 2025-10-06T19:18:58.115372
---

# G.O.S.S.I.P 资源推荐 2024-11-19 办公软件宇宙

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HAIIJK56IY2GJu6rAIY7yhJ5Hdehmo9D08iaAHvichsPEVS6JJ8ibELWiaEzv2W0naetVuSGZ7BeEibjQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 资源推荐 2024-11-19 办公软件宇宙

G.O.S.S.I.P

安全研究GoSSIP

计算机世界的奇妙之处在于万物皆可模拟，当然可能Apple的产品例外（参考最近的新闻“基于M4芯片的新款Mac 无法运行macOS Ventura 13.4之前的旧版macOS虚拟机”）。我们以前都习惯于虚拟机软件或者模拟器的使用，但是你有没有想过，那些办公软件同样可以创造属于自己的宇宙？今天我们轻松一下，带大家去看看最常用的两大软件——Microsoft Office套件和LaTex排版系统中的神奇世界。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HAIIJK56IY2GJu6rAIY7yh5UMxDxnULIyJtx432NgpCBxBb3Zd2M5wibcichbGsNbvzHE9eichibw33w/640?wx_fmt=png&from=appmsg)

首先出场的是办公软件中可能最受欢迎的Execl，今天我们要介绍的是用它来制作一款CPU！对的，你没有看错，只需要一个`RISC-CPU.xlsx`文件就可以实现一款8-bit的RISC 指令集的CPU，此外还有一个python脚本可以帮你把相关的汇编指令也编译成xlsx文件，作为这个虚拟CPU的输入。虽然这个CPU只支持10条指令跟一个寄存器（有人留言吐槽说只有CISC架构才会这么抠门，RISC起码要给16个寄存器），但是不妨碍它可以实现图灵完备的运算（当然实现图灵完备很多情况下都用不到这么多指令就够了），当然你在这个CPU上肯定是没有办法运行《黑神话·悟空》的对不对。更多的细节，可以参考下面的视频（搬运自YouTube）：

工程的细节代码可以从GitHub上获取：

> https://github.com/InkboxSoftware/excelRISC-CPU

---

既然Excel能行，那么作为宇宙第一排版系统的LaTex当然不遑多让，你Excel能实现一个超级简单的RISC CPU，那我LaTex自然要实现一个更复杂的CPU。于是就有了下面这个工程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HAIIJK56IY2GJu6rAIY7yhhzriaL13aCNcAjrbulEdVqxZHf6mXcTWO7JPuhvghWIJWgX0kFco4uQ/640?wx_fmt=png&from=appmsg)

在这个叫做`avremu`的完全用LaTex实现的模拟器中，作者实现了一个支持16位内存寻址的8位AVR指令架构的CPU，并且可以几乎完美支持`AVR-GCC`编译出来的二进制代码（除了MULS, MULSU, FMUL,
FMULS, FMULSU这五条机器指令不支持，但是`AVR-GCC`似乎并不会用到）。

作者表示，这个模拟器的运行主频达到了惊人的2.5 KHz，而且考虑到这是10年前的一个项目，那么经过制作工艺的飞升，今天你完全可以去购买一块9800x3D这样的神U，然后说不定可以把`avremu`超频到25 KHz甚至更高，还不快去试试？

> https://gitlab.brokenpipe.de/stettberger/avremu

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