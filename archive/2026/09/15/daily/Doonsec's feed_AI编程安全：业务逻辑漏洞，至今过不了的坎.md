---
title: AI编程安全：业务逻辑漏洞，至今过不了的坎
url: https://mp.weixin.qq.com/s/KfQKypZlvpd_mvP94k05Qw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:01:22.701311
---

# AI编程安全：业务逻辑漏洞，至今过不了的坎

# AI编程安全：业务逻辑漏洞，至今过不了的坎

原创

秋风
秋风

北京秋风代码科技有限公司

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

###

### 一、    0.01元下单299元的商品，为什么SAST工具难以发现？

### ![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0J16PL3qL15slWOc9pzGvaTp0ej7eGq1fNMEvHvK6j3p5qRyoeEdvdacOraSax4YOL4CP8hykj9GtomknoXh76u01wM2icSfZCc/640?wx_fmt=png&from=appmsg)

先看两个几乎每个安全工程师都见过的场景。

场景一：订单详情接口/api/orderid=1888，用户登录后把orderid=1888改成1889，则返回了别人的订单、收货地址和手机号。

场景二：下单请求体里带了个price字段，把299元商品抓包改成0.01，299元的商品一分钱购买成功，服务端执行毫无异常。

这两类问题有个共同的名字：业务逻辑漏洞，因为攻击者绕过了系统鉴权、登录状态，所以可使系统业务代码正常执行查询订单、下单购买。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0LiawrLMLabpQHU1kmZOkz19Cwdb0EMatHtoHI6tvOxmtyxicUibvvVh3QbxHiaowWdTRTCGyVGcOvmCiameFqFPpa8F8HVLUsicQPic4/640?wx_fmt=png&from=appmsg)

该类业务逻辑漏洞在近年来，跃居榜单前几名，在CWE Top 25 2025中的榜单，CWE-862缺失授权：从第9名跳到第4名，单年跃升5位。

![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0KG2Uiape2RFtJtRf9czQqsZmzW7JfeBsIyYLJyKge2bddUibMsedvbECZsPxibEjKLicAokbJq6LDqEr8wmDrVIJ2SIJqrmCB7YJg/640?wx_fmt=png&from=appmsg)

但这类业务逻辑漏洞怎么才能才能检测出来？答案有两种方式：

方式1：靠着资深安全测试工程师花几周读代码、理流程、用攻击者的头脑去想不该发生但能发生的操作，虽然有效，但成本高、效率低，当AI让代码产量以十倍速膨胀，这条路正在走到极限。

![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0JDxm2tecexGr1oo3bbBEMNdjzBlRVicsYp0Vy0icGV3VSaEN5OGwDeWeYicR4vxNxiaozPGrG8IQR2XLEVTCffZ1XBtShQre9HETI/640?wx_fmt=png&from=appmsg)

方式2：使用交互式应用安全测试（IAST）工具，在运行起来的WEB应用中放置探针，或者采用流量代理、流量镜像的方式捕获测试人员点击页面产生的交互流量，再还原流量进行污点分析，通过IAST内置的规则库，检测出业务逻辑漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0Jt4ficV3BPUE6qp78ib9txQ7rIjxib0RBg5r0ickibqhXyXTfDb1k0ElFU1EGrLPvN9TK9SEBvgmem6qBxSVRGI0rnoJtqQVhlGcibk/640?wx_fmt=png&from=appmsg)

有些人认为，SAST也能靠着语义理解，去检测业务逻辑漏洞，业务逻辑漏洞（如越权访问、支付金额篡改等）需要理解真实业务，但SAST是基于规则匹配的检测方式，SAST工具往往束手无策。

![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0KuuyBRJf5DiaeVSjibTMOUDqrib8V7C4sbrFCdxclrXSciblbbWZFL80cYyKSjrlWaLvfZQPYm2eecp5gI0cZnNHaMsEOReXTttlw/640?wx_fmt=png&from=appmsg)

### 二、    为什么传统SAST工具无法识别业务逻辑漏洞

要解答这个问题，要看SAST的工作原理，传统SAST的检测逻辑是三步：1、解析代码，生成AST语法树；2、构造控制流图和数据流图；3、定义检测规则，根据检测规则去看控制流和数据流所经过的点是否违背该条规则。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0JwFlWd5Rcux8RPbWcyJYXpSicwVsbAWSFY7T3hcfa9ECYMAn6PkbicmE9sQTicF8pu5rNG3UJfQibftRtMkDjo6TIXnWDv6mLRvuQ/640?wx_fmt=png&from=appmsg)

但问题是：业务逻辑漏洞在任何SAST检测规则和引擎中都是完全OK的，例如这行代码：get\_user\_order(orderid)，根据orderid去查询用户购买的订单。虽然看起来没问题，但在前面缺失了一行逻辑判断：if order\_id !=current\_user.id: abort(403)，如果订单不是当前这个人的，则返回403错误，从而限定用户ID和订单是一一对应的。

这种缺失的业务逻辑代码，必须要在WEB程序运行起来后，操作者在浏览器访问后做异常操作才能发现。因此让SAST工具在没有运行起来的WEB代码中找出没有业务逻辑判断的代码，比找有错误的东西难一个数量级，因为SAST并不知道这个代码在运行时的不正常操作会有哪些问题。

### 三、    被寄予厚望的 IAST，为什么AI编程时代反而更难了

很多人对交互式应用安全测试（IAST）寄予厚望，它曾被Gartner列为网络安全重点技术之一，同时也是测试WEB业务逻辑漏洞的常用工具。但IAST的优劣势也非常明显：

![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0IsT4uPObOmGKKPC720icELw9hNXRPsib68Xo8yjjjymEAiax6yfEuQsAKKzD7A5dxy0JzLScFGF9icyZW357GdciayrWQEfrYic49fE/640?wx_fmt=png&from=appmsg)

优势：比SAST强的地方是可以通过捕获WEB应用的交互流量，能看见WEB页面操作的前后台是否绕过了验证码、是否批量注册、越权等，探针在真实请求的流量里看得一清二楚，还可还原调用过程与代码片段，所以误报率低、定位准。

劣势：虽然IAST有着误报低的优势，但它也有自己的短板，他的Agent要随语言、容器、框架分别适配，插桩通常带来3%～5%的服务器运行时性能开销，还存在部分组件不兼容的问题。IAST能发现哪些业务逻辑漏洞，取决于内置的规则库，以及IAST对WEB页面的覆盖度，还有安全测试人员的水平，即使有些厂商的规则库中有些业务逻辑漏洞，但如果某条水平越权、负数金额的规则没有考虑周全，或者IAST的某些关键页面没有覆盖到，或者操作者的异常操作没有考虑到，IAST也无法从还原的流量中检测出来。

但对于AI编程时代，一天生成的代码、接口等抵过去一周甚至一个月的代码量，而AI最擅长生成的代码，恰是订单、支付、审批这类业务逻辑，同时IAST也会因为自身的劣势，无法覆盖到更多的页面，导致一些业务逻辑漏洞无法被检测出来。因此，逻辑漏洞这块最硬的骨头，也就留给了下一代AI编程安全检测技术，“业务逻辑理解与操作异常检测技术”。

![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0KibsicP4YamMQK2a0iad1fQKouh2UDMmm4kPGvZ8IoZNVKANmqP1HbogDXz6iaIYcZdSPImpP3EwsJU35FnOOp43Rlmyh5ibSaHyz0/640?wx_fmt=png&from=appmsg)

### 四、    为什么AI编程安全可以让业务逻辑漏洞有解？

过去的SAST检测引擎，是通过代码分析和规则匹配去做的，而不会做代码业务逻辑理解。但直到大模型出现后，出现了转机。但原因不是模型很聪明，而是大模型的代码业务理解能力。业务逻辑漏洞的本质，是实现与意图的偏离，要检测业务逻辑漏洞，前提大模型能理解代码业务逻辑、这个模块想干什么，再对照实现找落差。举一个AI检测订单越权业务逻辑漏洞的例子：

1、模型读完代码后，理解这是订单对象，它只属于某个用户，这个接口从请求参数取了订单ID，却只校验了登录状态，但没有校验订单ID是不是属于这个用户的，因为登录状态和订单是某个用户的业务逻辑是两回事。

2、水平越权这类过去只能靠双账号互换测试的问题，通过AI时代的源码理解，业务逻辑漏洞在源码层第一次有了可被检出的可能。

3、虽然AI能发现业务逻辑漏洞，但也别高兴太早，AI能理解代码业务，和能把它做成可检测业务逻辑漏洞可交付的产品，中间隔着两道技术壁垒：

（1）AI幻觉，大模型会一本正经地报出不存在的漏洞，这是所有AI模型的弊端，而成熟做法不是让模型直接给结论，而是在让模型检测之前，先用自己的引擎把流水线做好，再把目标函数、调用图、数据模型、甚至需求一起给模型，再让模型生成业务操作假设，列出在业务操作过程中，哪些操作会导致不正确的事情发生。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0IR12Km5Wy1gre9ENjLowZ4axk7dUicP9mVOOOC6x4OaQJiaHg1P8B4xAEXXjLaBKrJKickIiajR7WGM3Y8ic7zvlWBtdP2JpRRezDQ/640?wx_fmt=png&from=appmsg)

（2）上下文长度，业务逻辑的代码存在于百万行代码或数十个模块中，不可能把整个系统塞进提示词，所以如何切分代码、如何识别整个操作链、如何把业务需求和业务逻辑代码对齐，这是一整套非常复杂的代码业务理解工程。

![](https://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0KvHV1Iwo2hYIeg5Kz8zHx1NB03FZTwRMhCBKgASic9YiaVnFI3ma4ofqY4adhFVjSdDicicUgJKejat6icF3bicXicJI3R1TBZQFHILo/640?wx_fmt=png&from=appmsg)

所以，这就是为什么下一代AI编程安全必须突破传统SAST、IAST的技术路径，不依赖探针和流量镜像，变成理解代码业务逻辑，再验证业务逻辑偏离的技术。

### 五、    AI编程安全如何重新定义业务逻辑漏洞检测？

回看整篇文章，代码类漏洞教会了SAST检测引擎如何识别坏代码，SAST规则引擎扫了二十年，虽然有误漏报，但成效显著；而业务逻辑漏洞要求大模型先懂业务逻辑，再判断代码有没有坏了的规矩，这是两种完全不同的能力。过去二十年，业务逻辑这类漏洞只能靠资深安全测试工程师兜底，贵、慢、不可复制。虽然IAST曾经可以发现WEB运行时漏洞，但它依赖探针、依赖测试人员水平、依赖测试流量、依赖厂商预置规则等，但在AI编程时代，代码产出十倍速增长，订单、支付、审批这类逻辑最密集的功能恰恰是AI写得最多的，IAST能检测出来的比例反而在缩小。

真正的转机，是大模型带来的语义理解能力，AI能够读懂一段代码在业务里扮演什么角色、一条流程应该遵守哪些操作逻辑，再把业务需求和业务逻辑代码对齐，再分析用户操作过程中的一些异常行为会不会产生不正确的结果。

上一代SAST审计工具回答的问题是：这段代码，是否存在漏洞？

下一代AI编程安全要回答的问题是：这段代码在跑起来以后，能不能防止别人恶意操作？

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kMicrkibFtl0IVTCvMZ32NUia9DzEI8InMz2NPAmptMK3LFGbJUxgd3x7Znw2JibrKylBNYpguBxe3Taia2HDx4aXf47icXn8astrnAAOIP5SncAk/0?wx_fmt=png)

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