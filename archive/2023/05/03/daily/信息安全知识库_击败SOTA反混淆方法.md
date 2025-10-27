---
title: 击败SOTA反混淆方法
url: https://vipread.com/library/topic/3916
source: 信息安全知识库
date: 2023-05-03
fetch_date: 2025-10-04T11:38:19.129891
---

# 击败SOTA反混淆方法

[![logo](/static/logo_light.png)
![logo-dark](/static/logo_light.png)](/)

[VIPREAD 导航](/)

* [主页](/index)
* [书架](/library/category)
* [议题](/library/datas)
* [附件](/library/attachment)
* [成员](/library/authors)
* [搜索](/library/search)
* [**打赏**](/donate)
* [我要分享](/share/submit)

* [登录](/auth/login)
* [Dark](/setmode/black)

##### [主页](/) / [KCon 2022 黑客大会](/library/cid/442) / 击败SOTA反混淆方法

![](https://archive1.vipread.com/covers/2023/05/topic/migration_3916_1682976913_efd3b878.jpg)

* 标题

  [击败SOTA反混淆方法](/library/topic/3916)
* 作者

  程瑞, 黄泳龙, 徐辉, 范铭
* 标签

  [代码混淆](/library/tags/%E4%BB%A3%E7%A0%81%E6%B7%B7%E6%B7%86)
  [SOTA](/library/tags/SOTA)
  [安全加固](/library/tags/%E5%AE%89%E5%85%A8%E5%8A%A0%E5%9B%BA)
  [软件安全](/library/tags/%E8%BD%AF%E4%BB%B6%E5%AE%89%E5%85%A8)
  [安全研究](/library/tags/%E5%AE%89%E5%85%A8%E7%A0%94%E7%A9%B6)
* 简介

  代码混淆是一种被广泛应用的软件保护技术。目前，有许多基于符号执
  行、污点分析、切片等软件分析方法的自动化反混淆方法被提出，传统代码
  混淆方法正面临极大的挑战。同时，也有许多针对符号执行的混淆方法被提
  出。这些混淆方法大部分是利用路径爆炸这一挑战性问题提出的，然而许多
  反混淆方法并不会使用符号执行工具去覆盖程序的所有可能执行路径，而
  仅仅是尝试覆盖所有基本块，以重建控制流图。还有一些路径合并策略（如
  veritesting）能有效缓解动态符号执行中存在的路径爆炸问题，而研究者们
  都没有验证他们提出的混淆方法能否有效抵抗这些策略。基于这些，我们合
  理地提出第 1 个问题：已提出的反符号执行的代码混淆方法真的能有效抵
  抗自动化的反混淆方法吗？部分混淆方法是通过调用系统 API 实现的，但
  是，为符号执行工具编写扩展，处理 API 语义并不是复杂的工作。基于这
  些，我们提出第 2 个问题：是否为符号执行工具编写简单的扩展就能导致这
  些混淆方法失效？为了回答这两个问题，我们深入研究了已有的反符号执行
  混淆对自动化反混淆方法的抵抗性。结果显示，现有的反符号执行混淆方法
  可以分为 3 类：(1) 对自动化反混淆方法并没有明显的抵抗性；(2) 对自动
  化反混淆方法有明显的抵抗性，但通过为符号执行工具编写简单的扩展，自
  动化反混淆方法就可以处理它们；(3) 有明显的抵抗性，并且很难通过扩展
  符号执行工具处理它们。我们深入研究了第 3 类混淆，提出了构造这一类
  混淆的框架。基于我们提出的框架，软件开发者们可以简单地构造出高强度
  的混淆方法。实验显示，基于我们的框架构造出的混淆方法具有更小的时间
  开销。我们还提出了一种引入过污染问题的混淆构造框架，它也能让切片工
  具错误地选择不相关代码。我们基于 LLVM 编译工具链实现了一个混淆编
  译器，它能自动化输出被混淆过的可执行文件。本文的所有实验与工具的源
  代码已开源至 Github: <https://github.com/DrShabulaji/Paper_Obfs>.
* 援引

  https://github.com/knownsec/KCon/tree/master/2022
* 提示

  本站仅做资料的整理和索引,转载引用请注明出处

###### 相关推荐

* [![](https://archive1.vipread.com/covers/2020/10/topic/migration_3204_1603931451_7ca630f1.jpg)](/library/topic/3204)

  [邮件钓鱼之macro](/library/topic/3204)

  2020-10-29 08:30:51.788211
* [![](https://archive1.vipread.com/covers/2023/05/topic/migration_3907_1682918837_a205213b.jpg)](/library/topic/3907)

  [基于硬件虚拟化技术的新一代](/library/topic/3907)

  2023-05-01 13:27:17.344267
* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1g523mx9inwj312q0m9jvc.jpg)](/library/topic/2306)

  [微软威胁防护的机器学习进展](/library/topic/2306)

  2019-07-16 07:20:46
* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1fyeleka282j30960cftaw.jpg)](/library/topic/1875)

  [《信息安全研究》2018年](/library/topic/1875)

  2018-09-06 08:56:28

[![](https://archive1.vipread.com/images/ad/flag_3.gif)](https://www.flagify.com/?ref=https://vipread.com)

###### 附件下载

* ![](/static/images/icons/file-pdf.svg)

  ###### 击败SOTA反混淆方法.pdf

  时间:  2023-05-02T05:35:17Z

  大小:
  0.35 M

  下载:  19

  [登录下载](/auth/login)

##### 附件下载

![validate_code](#)

输入验证码
刷新验证码？

提交

错误信息

###### R2直链下载:

点击下载

###### 百度网盘:提取码(svip)

正在同步,稍等片刻

###### 蓝奏云盘:

正在同步,稍等片刻

关闭

错误信息

**分享文档请发送到 [[email protected]](/cdn-cgi/l/email-protection) ,感谢支持**

© 2014-2024 [信息安全知识库](//vipread.com)
[吉ICP备15005112号-2](https://beian.miit.gov.cn/)

* [**打赏支持**](/donate)
* [友情链接](/friends)
* [服务条款](/terms)
* [RSS](/rss)
* QQ交流群: 825629062