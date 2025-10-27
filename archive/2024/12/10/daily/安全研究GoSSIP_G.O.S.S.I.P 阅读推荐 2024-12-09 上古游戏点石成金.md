---
title: G.O.S.S.I.P 阅读推荐 2024-12-09 上古游戏点石成金
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499372&idx=1&sn=b723d2be54a413cae106a3d24c6d624c&chksm=c063d0b5f71459a3bed08a8fe5f4ee555991a8fda0e2b97214d7402b01e1b6f5844677df8135&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-12-10
fetch_date: 2025-10-06T19:40:27.601431
---

# G.O.S.S.I.P 阅读推荐 2024-12-09 上古游戏点石成金

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSsQbmvKTW7SiaZf8fxofOuIeXwa9dNMM7KsuybtRoxMaST8kkH6qsRKA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-12-09 上古游戏点石成金

原创

G.O.S.S.I.P

安全研究GoSSIP

有多少游戏陪伴你度过了一个美好的童年？对于生活在前互联网时代的人来说，单机游戏往往伴随着许多珍贵的回忆。所以在今天的互联网上，你会看到还有很多人沉迷于一些“古老”的游戏，今天我们要介绍的这篇非常有趣的文章，就是一个粉丝利用了自己的逆向工程知识，来让老游戏重获新生的故事。

首先声明一下，就算是编辑部可能也觉得有点不可思议，这个叫做《特技岛》（Stunt Island）的模拟飞行游戏是1992年发行的一个DOS游戏，可是今天在steam上竟然还敢卖42块钱的价格？？！！要知道宇宙级的《微软飞行模拟2024》现在标准版售卖价格也就是498港币。而且你看看下面这个巨粗糙的图像质量，是梁静茹给了开发者勇气？（哦不对，这个游戏是Disney代理的，懂了）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSOSRibOA1eVYmsQgWZxeEOCN9XeH3Sp7dHANaX2dD61RhfM12h8WzJOg/640?wx_fmt=png&from=appmsg)

反正我们的博客文章作者就是这么一个爱好者，还专门写了一篇文章《一首挽歌送给特技岛》去介绍怎么缅怀这个图像质量粗糙得可怕的游戏：

> https://fe9aefb4.annali-af6.pages.dev/2024/11/15/stunt-island-elegy
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSYzLvDcTw5LvCE8u0FJicGccTAevlGobCPibmPI6lM3Yo1nlTBTq6sPRg/640?wx_fmt=png&from=appmsg)

不过真爱确实是人类最强的动力之一，作者虽然在《挽歌》里面表达了希望能够有高清重制版的愿望，但可能是实在受不了也等不了了，终于决定自己动手来拯救它。于是就有了今天的文章——*800% Detail: Tweaking Stunt Island’s 30-year-old 3D Engine*：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSfE8uR6aC47JLemLm8hVTSRic6jnxic7WDVicnG520Hf2YfsicGLKrvRuWQ/640?wx_fmt=png&from=appmsg)

简单总结一下，作者拿出了逆向工程神技，把下图改造成了下下图的质量（注意下下图的远景细节）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSUvaXicD51S48ZCjccXy5Auhjicsm0Libicic0ITVlVAeRxsdCk9zP4Cc9Cg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSSLc7o2aexd3QDOTnicSP08GvkDiaG5Fprx2AvkMvjVV3tVmEh8sRbEGA/640?wx_fmt=png&from=appmsg)

好，接下来进入技术解读，作者首先觉得自己只要拿出反编译器就搞定了，于是拿出来Ghidra就有

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSu8BYo3pdFOBWyAnjbubO7JfiaJERNnHw9TSicAYPbgFCSDicdBgRVsRSw/640?wx_fmt=png&from=appmsg)

一看，代码分析结果很糟糕，然后查了一下，发现中了packer，还是程序员之神Fabrice Bellard写的一个LZ91 Packer，当然也有对应的脱壳器UNLZEXE，之后Ghidra就可以做一些事情了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSLkQssjFwVbgazTJaibQg0xIEibaZg8rOaZntfDbfiaPslRmUklKO8dnLg/640?wx_fmt=png&from=appmsg)

不过很搞笑的是，作者现在看不懂了，看来静态逆向能力还得练。

于是作者祭出来了动态调试大法，或者说游戏修改器大法：DosBox的调试功能启动！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSdnhBeP7XY1wekW6HTNAHR6kHibl9Zkx8UxAticlHpzeiaLpfsr3z97myQ/640?wx_fmt=png&from=appmsg)

这边作者展示出了很多技巧性的调试能力，比如怎么去设置断点，这个还是很考验对系统的理解的，建议大家去仔细阅读。核心在于想办法能够让游戏在“调整图像细节”这个操作上中断暂停（下图）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSajsIOibicdzdGh8tf6ZeZJHPHGOtbMjmHRjHOudNLtqsgN9Tle2b4Dsg/640?wx_fmt=png&from=appmsg)

接下来就是考验数据分析能力的时刻了：作者利用中断的上下文观察到的一些特殊的值，开始在Ghidra里面去搜索（就是赌一把这些值是statically保存的），还真的找到了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSFazKkB2mXGfNfjydkiaaibAdicXqrg5jjiaPrQRtoKRTpP4TNeMrHgg1Zw/640?wx_fmt=png&from=appmsg)

接下来是调试中经常做的一件事，就是修改某些值，观察程序的变化，作者在这里做了个实验，在某个点把`DX`寄存器的值清空，然后观察游戏画面，所有细节都消失了！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSx9eJd5ojWTXAe07KZcWpJynb7HtYv1l0dUeBVvsFmf0rtOkvrIVGCQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnSTRGSB7PpOlXyAvibLgSL0qmNcZbTIBAzbJiclHwbkukdzoic6BKQJagcg/640?wx_fmt=png&from=appmsg)

这说明`DX`寄存器的值很可能是控制分辨率细节的，那么修改一下，是不是能看到细节呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EPELJQLTZvRoQNlnCOFhnS5VDfDjevhTMag2pzicnicibzbScw5MrWEqe0Y8aCy97ib93kVecQ46QrbA/640?wx_fmt=png&from=appmsg)

成功！有视频为证

最后一步就是写patch去让修改一劳永逸，这部分就不多说了，因为**我们并没有42块钱去买游戏来玩****，所以作者提供的patch也用不上**，如果我们的读者愿意支援我们，非常欢迎！！！

---

> 博客原文：https://fe9aefb4.annali-af6.pages.dev/2024/11/20/tweaking-stunt-island
> Patch：https://fe9aefb4.annali-af6.pages.dev/assets/2024-11-20--tweaking-stunt-island/si-8x.7z

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