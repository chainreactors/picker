---
title: 不可避免的内存安全（Memory Safety）之路
url: https://www.solidot.org/story?sid=81250
source: 奇客Solidot–传递最新科技情报
date: 2025-05-10
fetch_date: 2025-10-06T22:29:56.297336
---

# 不可避免的内存安全（Memory Safety）之路

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251005)
  [往日投票](/polllist)
* 皮肤

  [蓝色](/?theme=blue)
  [橙色](/?theme=yellow)
  [绿色](/?theme=green)
  [浅绿色](/?theme=clightgreen)

* 分类:
* [首页](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [科学](//science.solidot.org/)
* [科技](//technology.solidot.org/)
* [移动](//mobile.solidot.org/)
* [苹果](//apple.solidot.org/)
* [硬件](//hardware.solidot.org/)
* [软件](//software.solidot.org/)
* [安全](//security.solidot.org/)
* [游戏](//games.solidot.org/)
* [书籍](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [云计算](//cloud.solidot.org/)
* [高飞的电子替身](//story.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](/QA)查看。

## 消息

**本文已被查看 6101 次**

## 不可避免的内存安全（Memory Safety）之路

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年05月09日 19时20分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81250&appkey=1370085986&title=%E4%B8%8D%E5%8F%AF%E9%81%BF%E5%85%8D%E7%9A%84%E5%86%85%E5%AD%98%E5%AE%89%E5%85%A8%EF%BC%88Memory%20Safety%EF%BC%89%E4%B9%8B%E8%B7%AF "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自光明之子**

Shawn the R0ck 写道：*“Memory safety 近年来成为热门话题。但在讨论“memory safety”时，我们需要先明确究竟在探讨什么、追求什么目标。你是在关注通过编译器完成静态分析（如 Clang Static Analyzer、rustc 等）来在编译阶段捕获潜在问题，还是更信任编译器让代码顺利编译，通过运行时机制（比如 Go 或 Java 中的垃圾回收）来解决所有问题？或者，你仅仅关注于安全加固的最终目标——即防止系统遭受攻击？内存安全问题的复杂性正反映了安全领域的本质：安全是一门交叉学科，融合了计算机科学和复杂性理论，这使得要完全掌控其复杂性变得异常困难。因此，企图通过单一或者几种 “memory-safe language” 重写现有软件，从而彻底杜绝所有安全隐患，并非现实可行的方案。

一门编程语言在设计时可能就倾向于提供内存安全机制，例如自动垃圾回收、数组边界检查等，这些机制在规范层面上勾画了一个理想状态。但在现实中，不同的实现者会出于需求和性能指标的考虑采取不同的策略。例如，虽然 Lisp 通常配备垃圾回收机制、支持灵活的数据操作和动态类型系统，但这并不意味着所有 Lisp 解释器都能完全消除内存安全问题。如果由于特定需求或追求性能而对部分安全检查作出妥协，那么内存越界或非法指针访问等安全隐患依然有可能出现。

同样，C/C++ 被长期视为“不安全”的语言，因为它允许程序员直接操作内存和执行指针运算。然而，通过严谨的工程化手段（如静态分析工具、严格的代码审查、运行时检测机制等），使得 C/C++ 在特定环境下无限接近无 Bug 状态也是可能的。本文将以 HardenedLinux 过去数十年中在对抗系统复杂性、提升内存安全方面的一些做法为背景进行探讨。总体来看，内存安全不仅关乎编译器或运行时单一环节的责任，而是需要在语言设计、工具支持、工程实践等多方面协同努力，以实现最终“系统不被攻陷”的安全目标。本文不涉足强制访问控制，沙箱，Linux内核加固等议题。”*
hardenedlinux.github.io/system-security/2025/05/07/path-to-memory-safety-inevitable.html

﻿

发现可能性的界限的唯一办法就是越过这个界限，到不可能中去。--阿瑟·克拉克

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251005)
* [过去的投票](/polllist)
* [编辑介绍](/authors)
* [隐私政策](/privacy)
* [使用条款](/terms)
* [网站介绍](/introd)
* [RSS](/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205　涉未成年人举报专线：010-62641208 举报邮箱：jubao@zhiding.cn　网上有害信息举报专区：<https://www.12377.cn>