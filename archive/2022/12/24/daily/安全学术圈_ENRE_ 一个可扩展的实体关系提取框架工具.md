---
title: ENRE: 一个可扩展的实体关系提取框架工具
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247488370&idx=1&sn=648a384ab864c89f0d3a95f8cfffab19&chksm=fe2eecf9c95965ef0601fd8d66e7c342fd55e390ecedf2fd70f25a3dcd48d06668d96565370a&scene=58&subscene=0#rd
source: 安全学术圈
date: 2022-12-24
fetch_date: 2025-10-04T02:26:06.825244
---

# ENRE: 一个可扩展的实体关系提取框架工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6Dibw6L070WGj1gfGCIlibAKciaKojJGzBrWNC81l7nVXesXmU4IOJxBrdicARY4A4PFNwuukfCZG9LLTz0yMFVBiag/0?wx_fmt=jpeg)

# ENRE: 一个可扩展的实体关系提取框架工具

原创

senu11

安全学术圈

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFxb2EWWK8Fjz8olK6TTB3bjBjiabwoiacicib08WCLJqibNDMT3ba8YJwSwVolWbjoFQu7icX4m7wE6LwQ/640?wx_fmt=jpeg)

> *原文标题：ENRE: A Tool Framework for Extensible eNtity Relation Extraction*
> *原文作者：Wuxia Jin, Yuanfang Cai, Rick Kazman, et al.*
> *原文链接：https://ieeexplore.ieee.org/abstract/document/8802634*
> *发表会议：2019 IEEE/ACM 41st International Conference on Software Engineering: Companion Proceedings (ICSE-Companion)*
> *笔记作者：senu11@SecQuan*
> *笔记小编：ourren@SecQuan*

# 1.目的

本节通过论文中的插图来引入作者此篇文章解决的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WGj1gfGCIlibAKciaKojJGzBrD5H3iatYmZa2EsYGXEUMz4xSzmzNSV8agWRk1y4zPPfeGtWDsa4NiaUA/640?wx_fmt=png)

如上图所示，函数 train1() 和 train2() 都调用了方法 run()，该方法属于类 FirstAgent 或 SecondAgent，作者使用商业逆向工程工具Understand来提取依赖项，发现它忽略了从 train2() 到 FirstAgent 或 SecondAgent 的关系，因为它无法解析是哪个函数运行的类（只能在运行时动态确定）。也即**静态分析会忽略实体间潜在的关系**。

另外一个问题就是**现有的工具不能支持多种编程语言来提取实体间的依赖关系**。

为此，作者提出了一个框架ENRE，可以从多种语言中提取代码实体之间的依赖关系。目前，该框架可以从Java、python、c++、JS/TS、golang中提取代码实体间的依赖关系。

项目地址：https://github.com/jinwuxia/ENRE

新搬迁至：https://github.com/xjtu-enre

# 2.ENRE框架

本节先介绍作者是如何定义与统一实体关系表示的，然后再介绍框架。

## 2.1.实体关系表示统一

提取实体间的依赖关系，需要首先定义实体、实体间的关系。

1）实体。实体是具有给定名称或标识符的对象。文章中定义了5种基本类型的实体：Package、File、Class、Function、Variable。

2）实体关系。实体关系即实体之间的关系。举个简单的例子：当实体 i 依赖于实体 j 来完成其功能时，实体 i 到实体 j 之间存在关系。文章中定义了 8 种类型的关系：① Import，② Extend (e.g. Implement, Inherit), ③ Call, ④ Set (a function modifies a variable), ⑤ Use (a function reads or uses a variable), ⑥ Parameter Type (a function takes a class type as a parameter), ⑦ Return Type (a function returns a class type), ⑧ Dynamic relation。关系具有如下属性：sourceId、destId、type、weight。

Dynamic relation，即动态关系，动态关系是只能在运行时精确确定的关系。静态关系和动态关系的区别主要表现在调用关系上。在判定调用类型时，文章为调用关系定义了两种动态依赖关系：

a）Internal Case，即内部调用。

b）External Case，即外部调用。如本文开头的贴图中例子演示，可以将对象作为参数传递而调用。

## 2.2.ENRE框架

ENRE框架如下所示，用户可根据需要自行扩展相关组件。ENRE以源代码作为输入，并输出代码之间的实体依赖关系，输出格式支持JSON、XML、DOT，用户也可以自行扩展输出其它格式。此工具框架基于Pipe-And-Filter模式，其中每个组件都可以被替换掉而不影响其他组件的工作。此工具由三部分组成，下面详细介绍。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WGj1gfGCIlibAKciaKojJGzBryIOBaC3gKnAC4hAapc6bwJ5TO74DAmoOcSJrc151ibIhQONHTtaxYrg/640?wx_fmt=png)

1）**Entity Generator，实体生成器**。此部分将源代码转换为实体树，作为一种中间表示，包括两个部分：

a) Parser，解析器。文章使用 Antlr 作为底层解析器，对源代码进行词法和句法分析。它使用给定语言的语法规则生成解析树。

b) EntityTree Builder，实体树生成器。这部分遍历解析树来构建实体树。实体树中的每个节点都是一个具体实体，扩展了 UERR 中定义的基本实体。每个节点可以有一个父节点和多个子节点。实体树中的节点用关系相关的语句进行注释，如“import”、“function call”。该部分取决于何种语言，分析师需要从对应的语言的解析树中识别和实现具体实体。

2）**Relation Generator，关系生成器**。该组件使用两个组件从实体树中提取和分析关系：

a) PriRelation Extractor。该组件通过分析实体树中的注释来提取实体关系。在处理完所有的注解后，生成所有的Primitive Relations，这些关系是代码中的直接关系。该组件也取决于是何种语言，因为不同的语言在名称范围和解析方面具有不同的语义。

b) HiRelation Analyzer。根据层次范围，该组件处理Primitive Relations并生成层次关系，例如哪些包包含哪些文件，哪些文件包含哪些功能等。

3）**Dependency Exporter，依赖导出器**。这将从前两个组件中提取的关系转换为指定格式，也包括两个组件：a）Formator。该组件定义了数据模型来wrap实体关系。数据模型可以使用流行的数据模型，例如 GraphViz DOT ，亦或者自定义模型。

b) writer。该组件将实体和关系格式化输出为 .CSV、.XML 或 .JSON 等文件。

要为给定的编程语言创建引擎（文章定义从 ENRE 扩展的依赖项提取程序为 ENRE 引擎），用户只需扩展 EntityTree Builder 和 PriRelation Extractor 来适应不同的实体和关系类型。

# 3.实验

由于语言为golang时，找不到可以对比的工具来评估，故作者以语言为python，将ENRE与Understand进行对比；实验以5种实体类型、3种公共关系来对2个 Python 项目开展准确性验证，实验结果如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WGj1gfGCIlibAKciaKojJGzBria0zxcjTNNxESarPO5mdAl9PP4vZQVOtpdzmnicA7vS5TRtfjJBZCLsA/640?wx_fmt=png)

1）关于实体部分，ENRE和Understand在实体为Package、File时结果一样，但是当实体为Function时，ENRE稍胜一筹，作者做了如下两个解释：

a）ENRE只统计最外层的类（或函数），忽略了它们的内部类，而understand将内部和最外部的均统计，因此产生更多的功能。ENRE不统计内部类是因为这些内部类通常是封装了的；

b）ENRE 统计类实例化的 **init** 方法，无论是否显式定义。Understand 只统计显式定义的，因此方法数量比 ENRE 少。

2）关于实体关系部分，当实体关系为Import 和 Extend 时，两者一致；当关系为动态关系时，ENRE更优秀，其中只有当对象变量是self（即被调用者像self.m()）时才解析部分动态内部调用关系，而且 ENRE 提取了外部的动态调用关系。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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