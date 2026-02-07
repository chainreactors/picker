---
title: G.O.S.S.I.P 阅读推荐 2026-02-06 修旧如新及其他
url: https://mp.weixin.qq.com/s/uWUDRdMyFX-iHqr8-wW50w
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:02:53.284157
---

# G.O.S.S.I.P 阅读推荐 2026-02-06 修旧如新及其他

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolX2MtF2QicBxZyApNtaVT7QO2PHTclYxlWAiaD5DnC8k8CwAMKQfbuaReAaQkTj4ibc8iah5vaL0XmYJuLh7FGCU6QYgwR9uAjFRHY/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-02-06 修旧如新及其他

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

快要过年了，我们的专栏也要开始休闲阅读啦~ 今天推荐给大家的是一个运营了快30年的blog，在这么一个网路上全是赛博数字人的年代，这种blog本身就很有古旧感，而作者竟然从1999年（那可是上一个1000年哦）开始写作，直到这个月还在更新，那这位作者Dmitry Brant本人也是维基百科基金会的工作人员（白天给Wikipedia的Android APP搞开发），但是他的业余爱好除了写blog就是修电脑：他可不是修现在的电脑，而是修复那些非常古旧的设备（所以他其实也是一位数据取证达人），而且是用了现代的手段哦。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWnnjKRYPU3BbxGMicpXk4ic1JViclEVkrszgVyQiaib7InHwW2Rr5Fw7y8WeAvxHSPEDA4rxFrlq4ttSk04gN0v5XeGFw57l4AOjmo/640?wx_fmt=png&from=appmsg)

在（国内）大家都在喊着“Claude要降维打击网络安全”的时候，Dmitry Brant根本就不care这些，人家一方面沉浸在自己对计算机的热爱之中，另一方面也很积极地拥抱了Claude。下面我们就介绍一下Dmitry Brant和AI在赛博考古方面的一则小故事。

在2025年，Dmitry Brant收到了一盘3M的QIC磁带（问了下AI，这是Quarter-Inch Cartridge的缩写，也就是“四分之一英寸盒式磁带”），这个古老的东西对于我们当代的小年轻网友肯定非常陌生，但是Dmitry Brant之前就研究过了（比如 2019年的blog文章 https://dmitrybrant.com/2019/05/11/more-data-recovery-war-stories-recovering-qic-80-tape-backups 里面他已经写了相关的内容），他有一台古老的工作站，上面运行了CentOS 3.5（2005年发布），同时连接了一个QIC-80磁带驱动器可以读取相关内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolW0YiblQZIY2vj5A2J3WdEiaK3c2VzZibB2VpcFUIt8BqEM6ytW6n3tW03Q2ic63MVl8dLXeRQKOAZNjvE3ibQFtc5S49sVTMiaxkTuc/640?wx_fmt=png&from=appmsg)

这台运行了2005年CentOS的机器上有一个`ftape`驱动，这是目前已知的唯一开源的驱动，能支持QIC-80磁带的读取（当然还有一些闭源的运行在Windows 3.x/9x甚至MS-DOS下的软件也能支持），而我们的Dmitry Brant先生突发奇想，觉得这个`ftape`驱动代码写得太messy了，能不能让不知疲倦的数字工具人帮忙改造一下，顺便让它支持更新版本的Linux呢？

This repository is a Linux kernel driver that communicates with legacy tape drives connected to the floppy controller (FDC) on the motherboard. Unfortunately, this driver hasn’t been maintained for a long time, and can only compile under kernel version 2.4. I’d like to modernize this driver, allowing it to be built with the latest versions of the kernel.

Claude真的是太贴心了，马上回复：*I’ll help you modernize this Linux kernel driver for legacy tape drives. This is a significant task that will require updating the code to work with modern kernel APIs and conventions.*

经过反复几轮迭代（编译出错-把出错信息提供给Claude-继续改写-再编译）后，这个新“driver”就能通过编译了，不过我们的Dmitry Brant先生还不满足，还想要一个kernel module，于是他又继续驱使AI干活（以后能不能有劳动法保护下AI的工作时间）：

Is there a way to compile just this module in-place, instead of copying it into a kernel source tree?

不知疲倦的Claude回答道：*Yes! You can compile kernel modules out-of-tree without copying them into the kernel source. Let me create a proper standalone build system for the ftape driver.*

到了这里，Dmitry Brant先生还是比较谨慎的，他知道在内核里面加载的代码很危险，于是自己介入，一边加载刚刚由AI写好的内核模块进行调试（通过和老电脑上的驱动的dmesg输出进行对比），一边把不太对的地方丢给Claude让它继续修改，而**Claude竟然也能理解“No such device or address" (ENXIO) error”的原因是没有正确设置I/O port base address**，最后这个驱动/内核模块就写好了！！！

> https://github.com/dbrant/ftape

于是Dmitry Brant先生就有了一个可以读取QIC-80磁带的现代Linux操作系统，原来我们从小就被普希金骗了，《渔夫和金鱼的故事》告诉我们：只要敢于提要求，你就能够成为老太婆！

最后给大家看一张照片：不要以为这张照片和前面那张是一样的，前面那张照片里面运行的是CentOS 3.5，而这张照片里的操作系统已经是Xubuntu 24.04了！Bravo！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolVstJfHLuuzC0cmLmP8oXHuomevoGfibUejhaZEE2XNBOibOt0M4B3DwXuSJcIJTd4zJowxWlY70CjJ3z5QQicQ9wzcdlyicgd0fog/640?wx_fmt=png&from=appmsg)

作为一个怀旧的人，Dmitry Brant先生也跟大家说“要积极拥抱新事物啊”：

**Open yourself up to a genuine collaboration with these tools.**

大家可以去作者网站上阅读更多其他有趣的信息哦：

> 原文：https://dmitrybrant.com/2025/09/07/using-claude-code-to-modernize-a-25-year-old-kernel-driver

---

说到这个，再给大家推荐另一个有趣的内容：【修复阿波罗11号登月导航计算机AGC(第一期）】

> https://www.bilibili.com/video/BV1HBypYHE7u/?share\_source=copy\_web&vd\_source=c9a4cd65d0e9b7e7e82e897222f9fabd

这是一群老炮凭借着热爱，修复了阿波罗11号登月导航计算机AGC的视频记录，也非常值得一看！

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