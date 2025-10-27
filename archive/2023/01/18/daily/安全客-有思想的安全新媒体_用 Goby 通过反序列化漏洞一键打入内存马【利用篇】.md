---
title: 用 Goby 通过反序列化漏洞一键打入内存马【利用篇】
url: https://www.anquanke.com/post/id/285539
source: 安全客-有思想的安全新媒体
date: 2023-01-18
fetch_date: 2025-10-04T04:06:18.808666
---

# 用 Goby 通过反序列化漏洞一键打入内存马【利用篇】

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 用 Goby 通过反序列化漏洞一键打入内存马【利用篇】

阅读量**378255**

发布时间 : 2023-01-17 15:30:43

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 0×01 前言

在上一篇[《Shell中的幽灵王者—JAVAWEB 内存马 【认知篇】》](https://mp.weixin.qq.com/s/44vf7fZv-O0yGMA6sVezKA)中，我从概念上介绍了很多内存马的东西，并给出了我的观点：“大势所趋下，内存马技术将会像 SQL 注入、文件上传一样，是以后每位安全研究员都必须掌握的安全技术”。

内存马技术很好，很棒，大人小孩都爱用，但实际上，一个不可避免的问题是，能熟练修改、调试、使用内存马的技术门槛，相对较高，除了漏洞利用所需要的安全知识，还需要对框架、中间件的设计模式、源码实现相当了解，并且面对不同版本、不同环境、不同 JDK 等情况进行多种兼容，仅针对一个目标进行攻击，可能需要大量的研究与调试，编写代码，这对项目通常时间比较紧的大多数漏洞利用者来讲，不是性价比最高的方式。

试想一下，如果遇到一个反序列化漏洞，你需要测试 Gadget，生成反序列化 payload，原版的 ysoserial 提供的 payload 一般就执行命令，而命令执行后也无法看到结果，在环境不出网的情况下更加无法知道怎么继续利用。在情况允许的情况下，攻击者可以打入内存马，但是面对中间件的版本不同，内核使用的技术可能不同，如果没有提前准备或根据指定环境调试相关的代码，很难一次利用成功。

那该怎么解决呢？我认为，针对某种漏洞类型，能提供一个通用的利用框架，可以覆盖绝大多数的情况，**让攻击者可以无视中间的技术，直接能够使用**，才是最好的办法，如果针对每个漏洞，还能够**提供最佳实践，让使用者点点点就可以了**，岂不美哉？

所以，请观看如下视频：

[【用 Goby 通过反序列化漏洞一键打入内存马【利用篇】](https://www.bilibili.com/video/BV1vR4y1Y7G8/?share_source=copy_web&vd_source=4784d8435f8ee3b6f6fa5b032a0ba2ea)

**感受到“点点点”的快乐了吗？我是脚本小子，我爱点点点，我喂自己袋盐**。接下来简单介绍一下插件的使用。

## 0×02 介绍

反序列化漏洞是什么、ysoserial 项目是什么在这里就不在赘述了，这里主要介绍的是这次融合在 Goby 中的插件的使用方式。

### 2.1 Gadget

说到反序列化漏洞，最重要的就是 Gadget，目标环境中，必须包含带有漏洞利用链的依赖，但是即使有了依赖，还可能因为依赖不全、版本不同等等各种原因，导致利用失败。

Goby 通过动态修改类字节码、反序列化流等手段，提供了不同依赖版本、不同利用方式等共计 65 条反序列化 Gadget，可以覆盖绝大多数的漏洞利用场景。

使用者可以按需选择自己想使用的 Gadget。

![]()

### 2.2 内存马

本插件的重头戏，也是本篇文章想跟大家介绍的，其实是在对内存马的一键打入和利用上。

在反序列化利用中，有相当一部分利用链最终使用了 TemplatesImpl 实例化类字节码进行利用，在原版的 ysoserial 中，仅使用了 `Runtime.getRuntime().exec()` 执行系统命令，功能过于单一，在实战利用中，我们还可以利用其执行很多功能，比如命令执行回显、隧道类、执行任意自定义代码等。

当然也可以打入内存马，**Goby 目前支持了 Spring、Tomcat、Resin、Jetty、Jboss、Websphere 等共计 20 种不同类型的内存马，也可以覆盖大多数的环境**。

![]()

内存马类型目前默认支持冰蝎、哥斯拉 raw、哥斯拉、以及 cmd 命令回显。

![]()

选定了内存马类型后，可以为内存马设置地址、密码及用来校验的 Referer。

![]()

除了 TemplatesImpl，最常见的利用 Gadget 还有 CC 中的 Transformer[] 数组，这是一条链式的反射调用，一般情况也是利用其进行调用 `Runtime.getRuntime().exec()`，那在这种利用方式是否能打入内存马呢？

答案是肯定的，除了可以使用远程类加载、bcel 等方式进行内存马的打入，Goby 还通过使用 ScriptEngineManager 执行类加载 JS 脚本的方式默认支持了内存马的打入，其实还可以通过 `org.mozilla.javascript.DefiningClassLoader` 进行类加载等诸多方式进行内存马的打入，但是考虑到实际环境不一定存在指定的依赖，因此相关的技术还需要进一步的打磨。

### 2.3 扩展选项

此外，本项目还提供了一些扩展选项进行额外的配置。

**Inherit**：对于 TemplatesImpl 方式触发的反序列化利用方式，恶意类是否需要继承 AbstractTranslet；
**Obscure**：提供一些反射调用 navtive 方法、unsafe 之类的混淆绕过方式；
**Jboss**：使用 JBossObjectOutputStream 格式输出；
**Dirty-type**：提供了三种在流量层面对反序列化 payload 进行混淆的方式；
**Dirty-length**：混淆的数据长度；

![]()

使用者可以按需使用这些配置，默认状态下，可以无需进行配置。

### 2.4 总结

在全部配置完成后，点击生成，就可以将生成的反序列化 payload 进行保存了。

关于 Gadget、利用方式等相关信息的更多介绍，可以查看我开源项目的 ReadMe 或源代码。

项目地址：<https://github.com/su18/ysoserial>

## 0×03 使用

使用其实非常简单，例如，我想使用 CC6 反序列化链生成一个 Tomcat Filter 类型的冰蝎内存马，内存马地址为 “/bg.jpg”，密码为 “test”，内存马校验 Referer 地址为 `https://google.com/`，就可以进行如下配置：

![]()

点击 Generate 生成即可。

## 0×04 结合

说了这么多，只是用插件生成反序列化数据，好像没什么意思？我用命令行工具不行吗？之所以封装成为插件，主要有以下两点原因：

**·** 命令行参数过于繁琐，用户体验较差，大家还是使用图形化页面更舒服点；
**·** 考虑到实际漏洞利用环境可能没有 Java 环境，要生成反序列化 payload 还需要进行安装，过于繁琐，这里我们将 payload 的动态生成放在 GodServer 端，Goby 端无需存在 Java 环境。

第二个问题是，有了反序列化 payload，怎么使用？

当然，你可以把生成的 payload 数据复制粘贴在漏洞利用工具或者脚本中进行利用，或者使用 curl 直接对目标进行发包，但既然是在 Goby 中，为什么不跟 PoC 进行融合呢？

所以说，之前三章全是废话，一款好的产品真正要做的，是让使用者可以无需知道细节，也能无碍使用；但如果使用者想进行配置，也可以提供精细化、高级功能的配置。

**所以这里我跟 Goby 同学将中间的细节全部打通，并写了一批可以与 Goby 插件联动使用的 PoC，将一些有代表性的反序列化漏洞、Shiro 系列的漏洞等进行编写，可以直接打入内存马，在这些 PoC 中，我事先内置了确保可以利用的若干参数，Goby 使用者无需任何配置，就可以一键打入内存马。**

也就是文章开篇的视频。视频中联动了 Goby 的 ShellHub 插件，可以直接在 Goby 中对内存马进行管理，可以提供命令执行、文件管理、获取基础信息的功能，如果只是想简单获取一些信息，执行一些命令，那你根本没必要打开其他的 Webshell 管理软件，从资产探测、漏洞扫描、打入内存马到管理 Webshell，都可以直接由 Goby 完成。

当然，如果你对相关技术较为熟练，可以自行修改参数，进行定制化的利用。

由于时间问题，这批 PoC 我准备了 25 个，其中包括的是 Shiro 框架、产品如 Apache OFBiz、Apereo CAS、FineReport、Liferay Portal、ZOHO ManageEngine OpManager、ForgeRock AM 等。一般提供两种利用方式，一种是**命令执行回显（这里用到了各种回显的技术）**，另一种是**内存马的打入**。这一批 PoC 将会作为试点给大家用来体验插件的功能，但并不局限，反序列化作为 Java 安全近几年讨论最多的漏洞利用类型，可以直接打内存马的漏洞数不胜数。

## 0×05 汇总

以上基本上就是本篇文章的内容了，由于这篇主要是对 Goby 插件的介绍，很多技术上的细节没有覆盖完全，感兴趣的师傅可以私下交流。

除去反序列化漏洞，Java 还有诸多漏洞类型可以直接打入内存马，如 JNDI、Fastjson 等等，这些能力可能会逐渐集合在 Goby 上（我猜的），除去 Java，php / .NET 也都有内存马的利用手段，未来也可能会逐渐支持，大家可以期待一下。

目前，如果想使用这个插件生成的 PoC 进行内存马的打入，并联动 ShellHub 进行管理，需要按照指定格式编写 PoC，关于这个格式，后续将会详细更新在 Goby 的录入手册中，大家可以按照手册进行编写和利用。

本次 Goby 插件提供的能力，仅仅是开源项目中提供的一些能力，还有一些有趣的沉淀和成果没有完全提供出来，后续将会逐渐进行分享，帮助大家在内存马的利用上更加顺畅、门槛更低。

**关于本文中涉及的所有技术及效果，将在 Goby 的下个版本进行发布，敬请期待**。

## 0×06 End

**最新 Goby 使用技巧分享**：

[Shell中的幽灵王者-JAVAWEB内存马【认知篇】](https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247521497&idx=1&sn=50e062aa20930102e6b787711d0e214a&chksm=eb847f79dcf3f66f1ac0d14065fdef2576393e9142f36c5add4e738eebbf3b71410a79e759ef&scene=21#wechat_redirect)

[Corp0ra1 | 记一次不停的自我追问式学习(下)](https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247505258&idx=1&sn=7ff14823c497fb2734d14435ee5caeb9&chksm=eb843ecadcf3b7dc718e2bdb11fba1415582d7410c12d990931d0d8358a924e5363df4135590&scene=21#wechat_redirect)

[mesosaur | IP库？信息？资产？拿来吧你！](https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247509617&idx=1&sn=3e3e7df89231add9c55eb051b5a8c8ea&chksm=eb844dd1dcf3c4c797b2b3c78588a269fec6fba092be86c6661b77d0487aca35f5ba32b2ad81&scene=21#wechat_redirect)

[ybdt | 还在手动收集资产？你比别人慢了一步](https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247509945&idx=1&sn=6a9a013fc8ff29dce7ff46c8ce0c8244&chksm=eb844c19dcf3c50f66cd66e484ceeb989a4c08118b71d50a849bda0ba51e33eb30b30eeaf8ef&scene=21#wechat_redirect)

[mybad | 上线利器-ShellHub 插件初体验](https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247510124&idx=1&sn=de3aef91a47b6472d987c2fb7e6f3f6e&chksm=eb8443ccdcf3cadaa4c0ceb1905e14a9d7f3f01bf44f272bd0821c7359db0a847d8533c7abe2&scene=21#wechat_redirect)

**更多 >> 插件分享**

Goby 欢迎表哥/表姐们加入我们的社区大家庭，一起交流技术、生活趣事、奇闻八卦，结交无数白帽好友。

也欢迎投稿到 Goby（Goby 介绍/扫描/口令爆破/漏洞利用/插件开发/ PoC 编写/ IP 库使用场景/ Webshell 等文章均可），审核通过后可加 5000-10000 社区积分哦，我们在积分商城准备了好礼，快来加入微信群体验吧~~~

微信群：公众号发暗号“加群”，参与积分商城、抽奖等众多有趣的活动

红队版付费渠道：<https://gobysec.net/sale>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Goby**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285539](/post/id/285539)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全工具](/tag/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7)
* [Goby](/tag/Goby)

**+1**5赞

收藏

![](https://p2.ssl.qhimg.com/t0122d5645812f2bb92.png)Goby

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t0122d5645812f2bb92.png)](/member.html?memberId=148515)

[Goby](/member.html?memberId=148515)

Attack surface mapping 新一代网络安全测试工具

* 文章
* **35**

* 粉丝
* **20**

### TA的文章

* ##### [Goby 征文大擂台，超值盲盒等你来！](/post/id/286958)

  2023-03-03 17:30:10
* ##### [用 Goby 通过反序列化漏洞一键打入内存马【利用篇】](/post/id/285539)

  2023-01-17 15:30:43
* ##### [Shell中的幽灵王者—JAVAWEB 内存马 【认知篇】](/post/id/284235)

  2023-01-04 12:00:34
* ##### [来检测带外（Out-of-Band）流量的Ceye](/post/id/270611)

  2022-03-23 16:30:47
* ##### [上线利器 - ShellHub 插件初体验](/post/id/262626)

  2021-12-13 17:30:21

### 相关文章

* ##### [SiCat：漏洞检测新工具](/post/id/293257)

  2024-02-18 16:36:45
* ##### [使用 gopacket 从网络捕获及重组数据包](/post/id/288460)

  2023-06-12 15:58:16
* ##### [负载测试框架 Locust](/post/id/288620)

  2023-06-12 15:46:47
* ##### [UI 和 API 自动化测试神器 - Playwright](/post/id/286627)

  2023-02-23 10:30:37
* ##### [基于蜻蜓打造在线SQL注入检测系统](/post/id/286061)

  2023-02-07 12:00:32
* ##### [高效率开发Web安全扫描器之路（一）](/post/id/283900)

  2023-01-06 14:00:19
* ##### [源海拾贝 | DarkAngel - 全自动白帽漏洞扫描器](/post/id/284346)

  2023-01-05 12:00:37

### 热门推荐

文章目录

* [0×01 前言](#h2-0)
* [0×02 介绍](#h2-1)
  + [2.1 Gadget](#h3-2)
  + [2.2 内存马](#h3-3)
  + [2.3 扩展选项](#h3-4)
  + [2.4 总结](#h3-5)
* [0×03 使用](#h2-6)
* [0×04 结合](#h2...