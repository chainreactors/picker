---
title: 强网拟态：国际赛事如何促进与国际联队的关系
url: https://mp.weixin.qq.com/s/BBGQvJYkmgvCJSHEsMAB7A
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:44:55.649156
---

# 强网拟态：国际赛事如何促进与国际联队的关系

# 强网拟态：国际赛事如何促进与国际联队的关系

原创

黄豆安全实验室
黄豆安全实验室

黄豆安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

第九届强网拟态在2026.11.1结束，主办方紫金山实验室、（）网安提供平台，作为一个AI时代的国际赛事，本次拟态的平台展现出了前所未有的（）和（），参与此比赛的国际战队，如越南的IRESDTU战队，在开一个容器需要半分钟、一个队伍限制一个容器、且当时所有容器全都502无法打开的严苛环境下，仍然做到了8秒钟提交一个flag，让我们为他们祝贺：

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqurTLiaTVTUlg1EE4xicGwBiblvO9e6JDA3yk4HSpWowszEpKIqTnxegRMMf0icacm4j5zRrtEawNO4HaxFgatRbDKbRD0lGEAzbug/640?wx_fmt=png&from=appmsg)

众所周知，拟态的比赛平台是xxx.com:54443（目前已关停），如果你扫了端口，会发现：

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqtxkG85F796RUhRtZMJkHT4tcEs2mV5iaYtibE6uGYgic53fUrsuSkxPTRudUrHDicxxcdgpNAF2zpiaEJfpbyJwicsnhjsW534Szzic0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWqsibUG6pzZl5ag9lCK4qU4iaVeT0Jub7MwUnWcb0fianELKg29vcKAFc3R2d35ekWPymBz7861IXON6dpC2ficiaHNQmKoX1icIXw0Og/640?wx_fmt=png&from=appmsg)

可见我们的（）网安非常擅长物尽其用，知道在不同端口上同时部署不同服务，来最大程度地节省资源，虽然最后导致平台被打穿，flag被泄露，但还是让我们为他们点赞。

作为一个比赛，第九届强网拟态肯定是要开设选手群，让选手和赛方共同针对比赛中出现的问题进行交流的，让我们来看一下紫金山实验室与选手的交流记录中讨论最多的一个话题（你问我为什么没有某网安的交流记录？这是你该问的？）

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqtichC8Mr9NFPicRZrSial0ABASjb2hstO7jJzIkicWriboZIMh3GU6aDAyXCzzkfjOVCG3ic9vD5BXaEK1iaWqGrNariciasF3DAeedkJo/640?wx_fmt=png&from=appmsg)

与此同时：

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqs36L01Fr0G67hyvticnBqS6bvzIrHLElJ2QClOZFqeLkZSmwlUvXOcZJEQFDTYFAkmAHclafovvlgz6OpjhT1jMsFq4HCL9ye4/640?wx_fmt=png&from=appmsg)

可以看到还是有部分战队顶着无法访问容器的困境去做题的，当然了肯定不是利用什么平台漏洞，（）网安还没说话呢。

众所周知，PWN是CTF中的一个主要方向，本次拟态也下发了许多PWN题目，无一例外，它们都没有附件，其中PWN1、3、4在黑盒的情况下，使用AI可以解出，你问我这是什么类型的黑盒PWN？我很明确地告诉你，这些都是忘了上附件才导致要打黑盒的PWN。在上附件之前，PWN2仅有12解，上附件后解数开始激增，说明大家的AI基本都折在了PWN2，啊当然了这12个解肯定不是攻击平台才拿到的flag，blind pwn隔壁强网不也有吗？正常。希望在不攻击平台的情况下能盲打出来PWN2的战队去把你的WP提交到CVE，到时候我们又可以震惊瘫坐了，啊某某某AI在某某某比赛中独立挖掘出Linux大0day，人类完蛋了，不要拿你的头去顶AI大人的鞋底了，新鞋别搞

杂项（Misc）在拟态中，是以静态附件为主的方向，越南IRESDTU战队在8:27解答完成了一道8:30才上的取证题，这是内幕吗？不是。这是（）网安的工作人员不小心把八点半上的题提前上了，之后光速撤回，但是不影响我们其他人顺利拿到附件并解答，我甚至还保留了Agent拉到这道题的Session会话记录，致敬强网杯伦华不是轮滑先生，你丢掉的session我替你补上了。

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqtNbGzJyL4BPqwDazyhARfSqbLL5iadpKPQtIT6VzaMXPx7Y2VN5bics9Eb7TXrTNpBKib5sbPSNibQLcsPJBIOkejphaB5VWcK3vw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWqsV4lg4k2K5dHoQHqMaIibEwDYUjxfodF9BhtBryAVialWe5XSwJ57IzJT7PM5Y5icCOEUuGmb2RicaACfTolbsKGpZ8wjt2yp4Epo/640?wx_fmt=png&from=appmsg)

你知道的，逆向这种方向被AI抽得最狠了，拟态和强网都不例外，咋办呢？好说，你出个无解逆向，或者少给个附件不就完事了，我们拟态确实是这么做的，后面即使一连串上了4个hint，也改变不了0解的结果。平台已关，给大家看一下我的AI记录：

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqvXEWygfNtFMMsgrdsMJPkhibictiaxHxFHDcCO9JuztHkszcGLyc5pSXiaSLGXPpXX4yiagEebCobp32f04qZ5Elj0ycxkLKAFg0NY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqtBr5M0gAicd03Picav3lk9nNlvlMRpdXdapiaibgZbK5FOK4RC2N2pAI3bGaLac7YxWx1gEcRw28VibDBHF9rc18PZGSibW67Iz7sJs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWquydRXKNcjiaNibP3CLOhYtt0CXvOw0JFaClbib6GAu1OnIfEhQVtoJsmRPRQcnproaqFVxHWjTU1srGhtr030icn6aoxtMNJFAgHk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWqtDxQhr4DVvrIsmYaDHT34r18ml2dcZyJheso0LXXX7haIUibynCFv3BfVK8osrelxPEGcqXVvVNVdUvBqwdYzv5132z8n2S4bY/640?wx_fmt=png&from=appmsg)

请注意我在这道题上使用的模型和额度：

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqufD38C6AUygJGfYTBMZdRZjdiaj1kngNiaqa0liaLRVuyGYWGhSAn9IibzQ7gPybiblJxsVmGwO1jnkqibdVZuZCh7GPHHRictIREF6U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWquJTia42vZZHsu0oxYJfBN4wRbkRzIJSwNCberVUPbmQMezQ6mKxco1YibJgu9OOCe79o59iabhD1DHxcc3vSsrqnVgxGh6AQOUGs/640?wx_fmt=png&from=appmsg)

那么，这道题是什么时候出的呢?

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqvOEHYNCT5FLGJT13olhqJcX4ynRHLcveiaCc43pdJJeFoib5c8qUsibd51IaqSLPDCE1E6wLP3HyuueVqZhg95RvErdSMCs0YFB4/640?wx_fmt=png&from=appmsg)

是在第三轮上题前2h出的，而且出题人一直强调没有上错附件，我也是狠狠期待一手官方wp

我给你了，这逆向我不要了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWqu3nLaIeHUTpTdCC3eibfc98mCrdU8nnicvFEsdtMVHfuSibc79o9j2ayd1mnmy2Bw8pfzQn0lIRGfqy3w8ydoMDvXSmWWvCBx7s0/640?wx_fmt=png&from=appmsg)

赛中因为种种原因，紫金山这边宣布了比赛暂停，抽象的是只要你开了一个海外代理，那么仍然可以正常比赛，（）网安也在几分钟之后宣布了比赛重开，多亏了我们越南大人，不然拟态都没法办了👍👍

可以看到作为主办方，紫金山这边压力还是很大的，但是还是给选手了一个答复，认可了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWqvfFWZa7U9wy6uJ9pY64Xm5S7OT9ic4nYVVjEb5jzQmFqK1rvUv72cLSHLhBF5eZTfqjq9o6AO4Ha3d7ClwY0zS2rvtJQ0ibiaicBI/640?wx_fmt=png&from=appmsg)

比赛最后的结果是什么呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SbtGVeibYWqu7PbHLG2aibmBagoASwGToYiafhGjT2XhYicfBiaTFHXRKHbjheWDIo6DdSha7PffoLw3YFdmmGPqibiaWics3ATribgMSLW8fDtZ4BW4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/SbtGVeibYWqu8Q82cPibRia5icyiatUd4APXiaibZic80ek14LgjAibD5yzcCktC82yJhcs9qbuIicJo9nvS4q5KWxwjgUib4CPx5lBU5gayB7rR1LjuWQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfZGYGTCfkmoZAjWACD8SRcEPz9kMiasJSNMegN4rfJLBZWicE3jfCX2MQK74RNyibxbVFvD7F0nTHoEg/0?wx_fmt=png)

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