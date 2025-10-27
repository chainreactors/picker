---
title: Intel CPU漏洞研究，为你深入详解三个史诗级的芯片漏洞
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458489310&idx=2&sn=65be16f07e07cab5d29111dbd406d3ec&chksm=b18ea15486f928428114713f06dc4016836f052e13c456507ecca59f74de756e19f7aa224f80&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-12-26
fetch_date: 2025-10-04T02:31:11.321700
---

# Intel CPU漏洞研究，为你深入详解三个史诗级的芯片漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuZjXpwNEVwXokHzn68uiaNPSia9A5ACyuJgOdGGMNcMTTbIAmxCLRELNQ/0?wx_fmt=jpeg)

# Intel CPU漏洞研究，为你深入详解三个史诗级的芯片漏洞

看雪学苑

![](https://mmbiz.qpic.cn/mmbiz_gif/DzwMlsjkpcr1tUhbc6hg27DORgWJ3KWQkSysibiakq3ia13HCrsNnlymqCZZhiawDqIdmBdib5I8WO7WlcXKT1IAzVg/640?wx_fmt=gif)

安全问题的焦点是随着时代变化而变化的。

二十世纪末二十一世纪初的主流安全问题是栈溢出漏洞，之后在各种新的安全机制的绞杀下，栈溢出已经没有了生存之地。但随之而来的是更加隐蔽、威力更大的通用内存破坏漏洞。

可以预见在不久的将来内存破坏漏洞将逐渐退出一线，新的更加底层硬件漏洞将登上舞台，研究者们的目光也将更多地投向当前安全问题的边界——电路。

在这场新的战争中，CPU将会是厮杀激烈的主战场。

想了解前沿的Intel CPU漏洞，走在时代前端吗？

为此， 看雪推出【Intel CPU漏洞研究】课程！

![](https://mmbiz.qpic.cn/mmbiz_png/GLrZwmh5s7zd2rkPhk5lERFK90yyodHR2RSNUKyDkev7nriamlU8kNfic6yB6DrVXCscnnWM32T2TTl70tcGxkcg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GyNzjWyzA15sFhnpSJn3JQjWcthPeGvPNDzDEsmMe2THQL7jCTBsfYtCtW4SLWiacRTlSWC54WJJQ/640?wx_fmt=png)

课程简介

![](https://mmbiz.qpic.cn/mmbiz_png/lMfKCAD8Y1iaibE6ibLef6Q6k3PN9KkFpIFEJSDz6lWtUgw3yUmUx0e8xicX34VcAj6xPzic0UQEIP759EQbLs4pVeg/640?wx_fmt=png)

课程将介绍2017年爆出的Intel处理器两个安全漏洞**Spectre**和**Meltdown**的研究，以及**Intel处理器缓存侧信道攻击**的研究。在讲清楚原理的同时，详细介绍实际应用方向上的研究。

讲师介绍

![](https://mmbiz.qpic.cn/mmbiz_png/lMfKCAD8Y1iaibE6ibLef6Q6k3PN9KkFpIFEJSDz6lWtUgw3yUmUx0e8xicX34VcAj6xPzic0UQEIP759EQbLs4pVeg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_gif/rrLibLCA8Z36yPibDz9Ia2n8kBpMxpiafEv7kjFicQjM2K5ML6S3KNYzqVa6nL1HQNxbIYzuHMJHBKW66bXh9o3Q1A/640?wx_fmt=gif)

**极目楚天舒**，业余安全研究员、Linux爱好者，擅长漏洞分析/安全开发。**长期跟踪处理器相关漏洞，研究利用方式。**

课程大纲

![](https://mmbiz.qpic.cn/mmbiz_png/lMfKCAD8Y1iaibE6ibLef6Q6k3PN9KkFpIFEJSDz6lWtUgw3yUmUx0e8xicX34VcAj6xPzic0UQEIP759EQbLs4pVeg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_gif/rrLibLCA8Z36yPibDz9Ia2n8kBpMxpiafEv7kjFicQjM2K5ML6S3KNYzqVa6nL1HQNxbIYzuHMJHBKW66bXh9o3Q1A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/DzwMlsjkpcr1tUhbc6hg27DORgWJ3KWQkSysibiakq3ia13HCrsNnlymqCZZhiawDqIdmBdib5I8WO7WlcXKT1IAzVg/640?wx_fmt=gif)

**前言**

* 课程简介

**基于时间探测的缓存侧信道攻击**

* CPU缓存、操作系统以及应用程序层面相关的知识
* 缓存攻击之Prime + Probe
* 攻击场景：信息搜集与传输
* 示例程序的设计
* 基本数据结构、Covert Channel的建立
* Eviction Set的生成算法与遍历策略
* 数据的传递与处理

**Spectre V2漏洞剖析**

* “幽灵”漏洞原理
* 缓存攻击之Flush + Reload
* 攻击场景：跨进程信息泄漏
* 示例程序的设计
* 目标分支的定位与训练
* Covert Channel的建立
* Cache的刷新与访存延迟的测量

**Meltdown漏洞剖析**

* “熔毁”漏洞原理
* 攻击场景：寻找内核随机化基地址，实现任意内核内存dump
* 内核地址随机化在Linux5.0内核x86\_64体系下的实现01
* 内核地址随机化在Linux5.0内核x86\_64体系下的实现02
* 攻击程序性能瓶颈的分析
* 缓解措施：内核页表隔离
* 攻击程序的设计

![](https://mmbiz.qpic.cn/mmbiz_png/GLrZwmh5s7zd2rkPhk5lERFK90yyodHR2RSNUKyDkev7nriamlU8kNfic6yB6DrVXCscnnWM32T2TTl70tcGxkcg/640?wx_fmt=png)

预备知识

![](https://mmbiz.qpic.cn/mmbiz_png/lMfKCAD8Y1iaibE6ibLef6Q6k3PN9KkFpIFEJSDz6lWtUgw3yUmUx0e8xicX34VcAj6xPzic0UQEIP759EQbLs4pVeg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_gif/rrLibLCA8Z36yPibDz9Ia2n8kBpMxpiafEv7kjFicQjM2K5ML6S3KNYzqVa6nL1HQNxbIYzuHMJHBKW66bXh9o3Q1A/640?wx_fmt=gif)

* 计算机体系与结构知识
* 操作系统相关的知识
* c语言、x86汇编语言知识

福利

![](https://mmbiz.qpic.cn/mmbiz_png/lMfKCAD8Y1iaibE6ibLef6Q6k3PN9KkFpIFEJSDz6lWtUgw3yUmUx0e8xicX34VcAj6xPzic0UQEIP759EQbLs4pVeg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_gif/rrLibLCA8Z36yPibDz9Ia2n8kBpMxpiafEv7kjFicQjM2K5ML6S3KNYzqVa6nL1HQNxbIYzuHMJHBKW66bXh9o3Q1A/640?wx_fmt=gif)

1、进群1v1指导

2、作业实战

3、课上自由答疑互动

立即报名

![](https://mmbiz.qpic.cn/mmbiz_png/lMfKCAD8Y1iaibE6ibLef6Q6k3PN9KkFpIFEJSDz6lWtUgw3yUmUx0e8xicX34VcAj6xPzic0UQEIP759EQbLs4pVeg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_gif/rrLibLCA8Z36yPibDz9Ia2n8kBpMxpiafEv7kjFicQjM2K5ML6S3KNYzqVa6nL1HQNxbIYzuHMJHBKW66bXh9o3Q1A/640?wx_fmt=gif)

***398元***

*![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Hc7Jyrv1jFeGTTJcBMI9ZpNgQTqTLKOsgC8uE1nV85qia7XSopwebw7eyWSqqtC7ssPviauoxq2oSA/640?wx_fmt=png)*

扫描二维码立即报名

报名成功后，请添加工作人员微信号：kanxuecom，进入课程群。

讲师为你揭秘安全漏洞“熔断”和“幽灵”原理，

解析处理器缓存侧信道攻击。

通过作业实战和辅导答疑，

让你快速成为CPU漏洞专家！

赶快把握机会，享限时5折优惠！

![](https://mmbiz.qpic.cn/mmbiz_gif/yiaUGfBWPtbQuH5aUviaiay2jOqF78SXDppoz3HyYRn9dxRRh5ibAiaFDx9eFQfuoMu3HicEicpZiabLGOJjiavxkbRibfDg/640?wx_fmt=gif)

**一步一步****积累技能后，你总会无坚不摧的。**

**赶快加入学习吧~**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Hc7Jyrv1jFeGTTJcBMI9ZpNgQTqTLKOsgC8uE1nV85qia7XSopwebw7eyWSqqtC7ssPviauoxq2oSA/640?wx_fmt=png)

*扫描上方二维码立即学习*

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hh3mibRXzvbmBIDfuZTEEtRA8qSdEKVzic3SUEUcebyJAJXob9sZESRxQTA33gqU1N0HraF7DjYb3Q/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458437955&idx=2&sn=73dd2dd34b75abc14bd03c12e0e3fb49&chksm=b18ff9c986f870df59522246f1b8f23240b52806bacb4bda1b45d79d602e3ac931f9cc6dafbb&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iaa8r7PJoyAtlfHAKe8RosE3wYVKBac55p1HPBJHZS42ywnG4yYtD3jo9A9e5kawBZs4IE6R1C4wibw/640?wx_fmt=gif)

- End -

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz/z9433rAGTDd78cwaDvzakb7575ic82NHaKASbJ2j330Auic2Ft9xA6W1fIhzeWib47ju2MNkhofiaumYKD9YltcqTQ/640?wx_fmt=gif)点击**阅读原文**，即可进入《Intel CPU漏洞研究》！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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