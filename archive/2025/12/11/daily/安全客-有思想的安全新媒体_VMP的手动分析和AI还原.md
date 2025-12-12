---
title: VMP的手动分析和AI还原
url: https://www.anquanke.com/post/id/313690
source: 安全客-有思想的安全新媒体
date: 2025-12-11
fetch_date: 2025-12-12T03:20:44.343738
---

# VMP的手动分析和AI还原

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

# VMP的手动分析和AI还原

阅读量**17769**

发布时间 : 2025-12-11 15:15:32

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## VMP的手动分析和AI还原

> 作者：uiop[@360SRC](https://github.com/360SRC "@360SRC")

### 前言

DEX-VMP：主要保护Android应用中的Java/Kotlin方法。它会将Dex文件中的ART字节码转换为自定义字节码，并将原方法标记为native方法。

### 一、DEX-VMP实现原理

根据art虚拟机解释模式可以模仿实现自定义操作码进行取值、译码、执行
以下是简易实现

```
 1. // 一个简化的解释器核心循环
 2. while (true) {
 3.     // 1. 取值 (Fetch)
 4.     unsigned char opcode = *vip++; // 从指令流中读取操作码
 5.
 6.     // 2. 译码 (Decode) 并 3. 执行 (Execute)
 7.     switch (opcode) { // 根据自定义操作码跳转到对应的处理函数
 8.         case OP_ADD:  // 如果是加法指令
 9.             // ... 执行加法的具体代码 ...
10.             break;
11.         case OP_MOV:  // 如果是移动数据指令
12.             // ... 执行移动数据的具体代码 ...
13.             break;
14.         // ... 其他成百上千的指令处理分支 ...
15.     }
16. }
```

### 二、手动分析流程

分析流程根据实现思路，可以围绕取值阶段来还原自定义操作码；

* 1、首先看看静态分析能否获取到信息

  通过hook registernative获取到MainActivity.onCreate的地址在0x7401b38088
  查看maps内存空间可以定位注册在以下标记的一段匿名可执行内存空间中

  ![]()

  将上边内存空间dump出来，可以看到这段代码为跳板函数会跳转到0x7362fb934执行函数

  ![]()

  0x7362f对应在下边内存，通过以前对壳的分析，这段匿名内存是通过壳进行加载并匿名的实际逻辑实现

  ![]()

  对正在执行oncreate函数的内存进行Dump并完成修复，会发现函数存在大量br跳转，手动简单修复br跳转后查看oncreate函数（未完全修复完毕），需结合动态半自动修复

  可以查看大体函数执行逻辑

  ![]()

  修复后的cfg，可以看出很多跳转缺失，纯靠静态分析是非常困难，需要结合动态调试来下一步分析

  ![]()

* 2、定位取值阶段

  分为有无源码对比，可使用两种突破方式,

  1. 通过 JNITRACE分析函数大致执行逻辑，使用指令级 Trace，通过指令块循环次数结合函数指令大小，从而实现突破。
  2. 利用有源码的函数开头的稳定特征，监控读取操作精准命中，实现突破。

  通过指令大小并结合trace进行快速定位代码块进行分析：通过分析oncreate函数开头以及指令大小定位内存加密后的oncreate函数指令位置，此 oncreate函数存在58条指令
  源码开头：

  ![]()

  在dump的dex中查找指令开头位置再0x63f77c

  ![]()

  通过trace的log分析后，发现以下代码块出现了58次正好结合58条指令，猜测并标记地址为取指令行为

  ![]()

  知道取指令地址后下监控断点验证查看确实在0x167608处取出指令

  ![]()

  跳转过去分析取值后跳到0x16766c

  ![]()

  分析0x16766c取指后操作进行字节码解密处理

  ![]()

  通过以上分析可以发现完全和trace的猜测一样。

  继续通过修复oncreate函数追踪分析13353c发现存在jni映射

  ![]()

  修改结构体顺序还原自定义jni映射

  ![]()

  向下追踪找到执行实际函数操作

  ![]()

  通过回调向上分析

  ![]()

  结合trace验证，确定为分发指令到0x15af88里边执行

  ![]()

Hook该解密函数获取所有opcode

![]()

接下来就是通过dex索引查找函数一步步进行字节还原，需要手工对照一点点还原比较耗时；能否取巧结合ai方式进行还原，可以进一步实践；

### 三、基于AI还原

dex vmp的基础支撑其实是jni函数，通过追踪jni调用，人工分析基本代码流程，筛选后的tracelog再结合强大的ai能力进行还原能节省很多人工分析流程时间，以下为ai还原对照，可以看到对于简单的函数可以进行完美还原，缺点是对于复杂函数涉及的log非常大的话需要多次拼接进行分析，造成的结果可能不是特别准确，但是基本逻辑不会出现问题可以进行正常的逆向分析

* Ai还原代码：

  ![]()
* 源dex反编译代码：

  ![]()

### 四、VMP保护更安全的展望

针对以上分析过程使用的突破方式，可以采用的防护手段

* JNItrace防护
  1、通过jnienv计算所有jni函数偏移量来通过函数指针形式进行调用隐藏所有jni的调用过程
  2、通过jnienv获取jni接口地址，检测jni接口函数是否在libart范围内，以及jni函数开头是否改变，防护Jnitrace、frida-trace、xposed实现的jnitrace。
* 指令trace防护
  1、采用 DexVM 与并对解密算法 VM 进行嵌套，将核心逻辑与算法执行流完全虚拟化，从而提升代码混淆强度并抵抗传统指令级分析,类似如下实现即可防护通过指令数量来快速定位代码块的方法
  ![]()

### 参考

<https://bbs.kanxue.com/thread-288731.htm>
<https://bbs.kanxue.com/thread-270799.htm>
<https://bbs.kanxue.com/thread-285212.htm>
<https://github.com/NiTianErXing666/SmallVmp>
<https://www.cnblogs.com/theseventhson/p/14933920.html>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**360安全应急响应中心**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313690](/post/id/313690)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [逆向分析](/tag/%E9%80%86%E5%90%91%E5%88%86%E6%9E%90)
* [脱壳反混淆](/tag/%E8%84%B1%E5%A3%B3%E5%8F%8D%E6%B7%B7%E6%B7%86)

**+1**0赞

收藏

![](https://p1.ssl.qhmsg.com/dm/200_200_100/t01b5d8fecc4d01072b.jpg)360安全应急响应中心

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhmsg.com/dm/200_200_100/t01b5d8fecc4d01072b.jpg)](/member.html?memberId=122586)

[360安全应急响应中心](/member.html?memberId=122586)

360安全应急响应中心（360 Security Response Center，简称360SRC）是360公司致力于保障产品及业务安全，促进白帽专家合作与交流的平台。诚邀白帽专家向我们反馈360产品安全漏洞、威胁情报，共筑数字安全基石，保障数亿用户业务和产品的安全。

* 文章
* **70**

* 粉丝
* **15**

### TA的文章

* ##### [VMP的手动分析和AI还原](/post/id/313690)

  2025-12-11 15:15:32
* ##### [浅谈SQL注入手工测试思路](/post/id/313692)

  2025-12-11 15:14:59
* ##### [360SRC年终冲榜丨敢AI，就请上场！](/post/id/313386)

  2025-11-26 12:32:59
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [诚邀莅临|三六零天御·亚马逊云科技安全合规沙龙](/post/id/308420)

  2025-06-13 14:18:45

### 相关文章

* ##### [静态搜索iOS动态链接函数的调用位置](/post/id/291737)

  2023-12-07 17:47:04
* ##### [Hook\_IAT实现调包Win32API函数](/post/id/260057)

  2021-11-25 10:00:40
* ##### [实现简单全局键盘、鼠标记录器](/post/id/257129)

  2021-11-01 10:30:29
* ##### [记ctf中利用IDA构建结构体解VM虚拟机（含源码）](/post/id/252573)

  2021-09-08 10:00:57
* ##### [Windows内核回调实现原理与逆向调试分析](/post/id/230073)

  2021-02-03 10:30:31
* ##### [撕开编译器给throw套上的那层皮——代码还原](/post/id/208939)

  2020-06-22 10:30:03
* ##### [深入分析sLoad Downloader：面向英国和意大利传播Ramnit银行木马](/post/id/162642)

  2018-10-25 14:30:57

### 热门推荐

文章目录

* [VMP的手动分析和AI还原](#h2-0)
  + [前言](#h3-1)
  + [一、DEX-VMP实现原理](#h3-2)
  + [二、手动分析流程](#h3-3)
  + [三、基于AI还原](#h3-4)
  + [四、VMP保护更安全的展望](#h3-5)
  + [参考](#h3-6)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)