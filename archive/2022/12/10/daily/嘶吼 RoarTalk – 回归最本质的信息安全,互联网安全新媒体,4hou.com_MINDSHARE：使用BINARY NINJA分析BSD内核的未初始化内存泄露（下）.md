---
title: MINDSHARE：使用BINARY NINJA分析BSD内核的未初始化内存泄露（下）
url: https://www.4hou.com/posts/3JPn
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-10
fetch_date: 2025-10-04T01:04:36.720685
---

# MINDSHARE：使用BINARY NINJA分析BSD内核的未初始化内存泄露（下）

MINDSHARE：使用BINARY NINJA分析BSD内核的未初始化内存泄露（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# MINDSHARE：使用BINARY NINJA分析BSD内核的未初始化内存泄露（下）

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-12-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126513

收藏

导语：本文的想法是执行支配流不敏感分析（insensitive analysis），以静态跟踪所有内存存储操作。当跨信任边界复制来自该内存区域的数据时，任何从未写入的内存区域都被标识为未初始化。

**跟踪动态内存分配中的内存存储**

到目前为止，我们的所有分析都集中在堆栈内存作为信息披露的源缓冲区。这在很大程度上是由于堆栈内存泄漏错误的盛行，如KLEAK：实用内核内存泄漏检测（PDF）中所述。其他内存区域（如堆）呢？我们可以对一些堆内存泄漏建模吗？

在查找堆内存泄漏时，思路也是一样的。我们仍在寻找调用具有已知大小值的sink 函数。但源指针不是RegisterValueType.StackFrameOffset，我们检查RegisterValueType.UndeterminedValue。考虑sys\_statfs()的代码：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221010/1665370206843623.png "1665370206843623.png")

sys\_statfs()中的动态内存分配

此时copyout()中的内核指针rdi\_1#2还是不确定，因为Binary Ninja并不知道分配器函数返回什么。然而，通过使用SSA表单，我们可以手动跟踪rdi\_1#2是否保存malloc()的返回值。例如，按上图中突出显示的说明进行操作。变量被分配为rax\_1#1->r15#1->rdi\_1#2。可以使用MLIL get\_ssa\_var\_definition()API通过编程方式获取此信息。一旦获得SSA变量的定义位置，我们就可以使用CALL操作检查变量是否被初始化。

那分析器如何知道分配器函数的定义？我们可以采用与提供静态函数挂钩信息相同的方法（请参阅上面的“静态函数挂钩和内存编写API”一节）。向分析器提供一个带有分配器函数列表和大小参数索引的JSON配置。对于任何具有已知目标(即MLIL\_CONST\_PTR)的CALL指令，获取该符号以检查已知的分配器函数。下面是一个用于分析的JSON配置示例：

一旦我们建立了源指针和分配器调用之间的连接，下一个问题是，将分配什么指针值作为分配器调用的返回值？在Binary Ninja中跟踪为负偏移量的堆栈指针是这样的：为了在堆栈指针和堆指针之间具有一个通用表示，我决定将堆分配器调用的返回值设置为分配大小的负值。对于sys\_statfs()中的malloc()调用，rax\_1#1设置为0x1d8作为起始地址。因此，需要初始化的内存区域的范围从0x1d8到0不等。即使分配大小不确定，起始地址也可以设置为某些任意值，例如0x10000。最重要的是要知道copyout()访问的连续内存区域是否已初始化。

**使用dominator和后dominator过滤内存存储**

下图中的dominator提供了一些基本块的执行顺序信息。虽然我们已经在“处理指针对齐优化”一节中使用了dominator来处理指针对齐的优化，但本节将详细介绍dominator在检测支配流敏感（flow-sensitive）内存存储操作中的使用。

为了分析未初始化的内存泄露，我们使用了两种思路：dominator和后dominator。如果到Y的所有路径都应经过X，则称基本块X支配另一个基本块Y。如果从X到函数的任何返回块的所有路径均应经过Y，则称基础块Y支配基本块X。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221010/1665370217251157.png "1665370217251157.png")

dominator和后dominator的图表

在所提供的图中，节点B支配节点C、D、E和F，因为到这些节点的所有路径都必须经过节点B。根据定义，每个节点都会进行自我支配，因此由节点B支配的所有节点集将是B、C、D，E和F。此外，节点A支配图中的所有节点。因此，节点C、D、E、F的dominator是A和B。

同理，当A为函数入口节点，E和F为出口节点，则节点B为节点A的后dominator。这是因为从A到出口节点的所有路径都必须经过B。

那么，dominator和后dominator如何帮助我们进行分析呢？

我们可以对sink函数的调用者执行dominator分析。其思想是只记录基本块中的内存存储，这些基本块支配调用copyout()的基本块，也就是说，将执行与分支决策无关的基本块，代码如下：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221010/1665370227155441.png "1665370227155441.png")

调用copyout()的基本块的dominator

调用copyout()的基本块是

在跨函数(inter-procedure)分析期间，对被调用函数进行后dominator分析。它的目的是在初始化它应该返回的内存区域之前，找到被调用者可能返回的漏洞。被调用者函数do\_sys\_waitid()如下所示：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221010/1665370237160832.png "1665370237160832.png")

do\_sys\_waitid()中函数输入块的后dominator

**函数入口块**

基于dominator和后dominator的分析试图填补分析器执行的支配流不敏感分析中的空白。其假设是，在执行进一步的操作之前，内存被初始化或清除，因此支配其他基本块。然而，这种假设并不总是正确的。例如，在某些情况下，单个代码路径可以执行与支配器中相同的操作。此外，当被调用者由于任何错误条件返回时，调用者可以在调用copyout()之前验证返回值。因此，在此情况下基于dominator的分析容易出现大量误报。

**检查未初始化的内存泄露**

一旦所有的内存存储操作都被静态地记录了关于写的偏移量和大小的信息，就可以使用copyout()对复制到用户空间的内存区域进行评估，以进行未初始化的内存公开。copyout()调用是这样的：源指针为0x398，复制的大小为0x330字节。因此，分析器必须验证内存范围从 -0x398到(-0x398 + 0x330)的所有字节是否都已初始化，如果没有，则将其标记为错误。

**误报和限制**

编写分析器的目的是查找在任何可能的代码路径中从未写入过的内存区域。如果无法跟踪内存存储操作，则会出现误报。以下是一些常见的误报情况和限制情况：

1.分析仪不模拟分支指令。因此，在涉及支配流决策的代码构造中会出现误报。考虑一个内存区域，例如在循环操作中初始化的数组。在这种情况下，存储操作将只检测一次，因为分析器只访问循环体一次，而不是像执行期间那样在循环中访问。

2.间接调用不会被静态解析，因此，在间接调用期间执行的任何内存存储都不会被跟踪。

3.优化可能会使跟踪内存存储更加困难。在“处理x86 REP优化”和“处理指针对齐优化”部分中处理了一些常见的优化。

4.Binary Ninja可能会错误地检测用于静态挂钩或copyout()等接收器函数的类型信息。由于我们的分析依赖于RegisterValueType信息，任何未能准确检测函数原型的情况都可能导致错误的结果。在分析和更新之前验证类型信息。

5.分析器仅查找内存源函数和sink函数位于同一函数中的代码模式。在本地函数范围之外，没有对内存源的跟踪。

6.dominator分析是实验性的。你应该仅将其用作执行代码审查的指导原则。

当可以访问源代码时，可以通过更改优化标志或展开循环来减少分支决策，从而解决其中一些误报。

**分析结果**

在Binary Ninja中加载目标内核可执行文件，生成BNDB分析数据库。然后用分析器对数据库进行分析，以便进行更快的分析。有两个脚本：一个用于分析堆栈内存泄漏，另一个用于分析具有已知大小和未知源指针的sink函数。因为源指针可以来自堆分配器，所以提供一个带有分配器函数列表的JSON配置作为参数。dominator分析是实验性的。需要时，请使用可选参数启用它。

**总结**

这些脚本在Binary Ninja版本2.4.2846上针对FreeBSD 11.4、NetBSD 9.2和OpenBSD 6.9内核进行了测试。在结果中，评估了非特权用户可能访问的代码路径。OpenBSD漏洞在与IPv4和IPv6组播路由相关的系统中被发现，分别被命名为ZDI-22-073和ZDI-22-012。

在NetBSD中发现的4个漏洞（ZDI-22-075、ZDI-22-1036、ZDI22-1037和ZDI-21-1067）与支持旧版NetBSD向后兼容的系统调用有关的ZDI-22-2075和ZDI22-11036分别是NetBSD 3.0和NetBSD 5.0的VFS系统调用中的信息泄露。另外，ZDI-22-1037是NetBSD 4.3的getkerneinfo系统调用中的一个信息泄漏。目前，此漏洞已修复，但还存在许多其他潜在问题。

在版本11.4中发现的FreeBSD漏洞也与兼容性有关，在本例中，兼容性用于支持32位二进制文件。然而，在对64位inode进行较大更改期间，该漏洞被修复，但没有被公开。作为64位inode项目的一部分，在copy\_stat函数中清除了未初始化的结构字段。虽然此承诺是在2017年5月，但它被标记为12.0及以上版本。因此，该漏洞在11.4版中一直未被修复，直到2021年9月才被处理。

总而言之，大多数漏洞都是在BSD的兼容层中发现的。此外，所有这些漏洞都是堆栈内存泄漏。

本文翻译自：https://www.zerodayinitiative.com/blog/2022/9/19/mindshare-analyzing-bsd-kernels-with-binary-ninja如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OAZ6oWOr)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bo2j)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png...