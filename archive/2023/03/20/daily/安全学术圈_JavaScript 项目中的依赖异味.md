---
title: JavaScript 项目中的依赖异味
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247488570&idx=1&sn=34b6a78605f6ba25d32b91c0bc658e3d&chksm=fe2eebb1c95962a775b5b1e44a87f024a9d92c7ed671957e9e4848319a79ec976fdeca902abb&scene=58&subscene=0#rd
source: 安全学术圈
date: 2023-03-20
fetch_date: 2025-10-04T10:05:37.558627
---

# JavaScript 项目中的依赖异味

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6Dibw6L070WEgYT5v0FD943vRPBAp20zic3kse66ctd2Ft2VyvZVcdWm0JT8Jyc7YdOQOWOOicwYhdRicogyIQtf4g/0?wx_fmt=jpeg)

# JavaScript 项目中的依赖异味

原创

NING

安全学术圈

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFxb2EWWK8Fjz8olK6TTB3bjBjiabwoiacicib08WCLJqibNDMT3ba8YJwSwVolWbjoFQu7icX4m7wE6LwQ/640?wx_fmt=jpeg)

> *原文标题：Dependency Smells in JavaScript Projects*
> *原文作者：Abbas Javan Jafari, Diego Elias Costa, Rabe Abdalkareem, Emad Shihab, Nikolaos Tsantalis, et al*
> *原文链接：https://ieeexplore.ieee.org/abstract/document/9519532*
> *发表会议：TSE'20*
> *笔记作者：NING@SecQuan*
> *笔记小编：ourren@SecQuan*

## 1 研究介绍

现代软件开发中的依赖关系管理给希望保持最新功能和修复同时确保向后兼容性的开发人员带来了许多挑战。项目维护者往往选择自己最熟悉的方式进行依赖版本的管理，这种不合适方法可能会引入依赖错误和漏洞。因此依赖管理问题被放大，本文主要研究当下反复出现的依赖管理问题，并且和从业者进行深入交流来探讨依赖管理问题的成因以及发展趋势。

* **RQ1：JavaScript 依赖异味有多普遍**
* **RQ2：从业人员如何看待依赖异味及其影响**
* **RQ3：为什么 JavaScript 当中会引入这些依赖异味**

## 2 概念简介

### 2.1 JavaScript 依赖管理

JavaScript 项目的依赖管理主要依靠 Package.json 文件，里面会定义项目的元数据和依赖项。而依赖项常见有三种类型：运行依赖（默认 Dependencies）、开发依赖（devDependencies）、可选依赖（optionalDependencies）。

### 2.2 版本控制语法（SemVer）

SemVer 是当下许多软件生态系统（npm、PyPI 等）的版本控制标准，定义为 (例如版本 3.2.10)。

## 3 依赖异味

与代码异味（Code Smell）相似，它指代的依赖管理中的分类目录，而本文在对 12 名专业开发人员的调查总结后，归纳出了 7 种依赖异味，如下图所示：（具体每一项的成因及出现后果在原文种有详细解释）

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WEgYT5v0FD943vRPBAp20zicPyF70DRbnrLHM2OBzLmmq2b7ggOyhUNge32lnFicfZB8QKqiaPW9Qsaw/640?wx_fmt=png)

## 4 实验调查及结果

这里本文选择在 github 收集开源项目，经筛选后共 1146 个。并对其进行了 7 种异味的检测。

* **RQ1：JavaScript 依赖异味有多普遍**

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WEgYT5v0FD943vRPBAp20zicSxYnzhPXRz3GNpkGBCSBibP5qY7hDKZw8f8SLf3X6epx96sGydxSaVQ/640?wx_fmt=png)

图 2 依赖普遍性

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WEgYT5v0FD943vRPBAp20zic6UEvbd5z9J3licqbEibsD8govevW8bhys4cV2sQftFXtDEnE2oiaRUjEw/640?wx_fmt=png)

图 3 包含不同异味的项目数量

如图 2 所示，这里显示了每种依赖异味项目在总项目数的百分比。总的来说依赖异味现象非常普遍，而其中项目未使用项尤其高（这一点可以与 Java 领域提出的 Bloated Dependency-臃肿依赖进行类别）。除此之外，我们还能看到各项占比之和是远大于 100% 的，于是作者也对项目包含的依赖异味数目进行了统计，结果如图 3 所示。

* **RQ2：从业人员如何看待依赖异味及其影响**

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WEgYT5v0FD943vRPBAp20ziccgl4O4lmgkfw7vpG6JqAppicMibZR4JW2Gvoe9icmcrM3YDL8GT71HVeQ/640?wx_fmt=png)

图 4 调研结果

如图 4 所示，显示了每个依赖异味、相关陈述及态度分布堆叠条形图。我们将“两者都不是”上的条居中对齐。因此，大部分绿色条向右倾斜的陈述表明 41 名参与者更多地达成一致。相反，条形图向左（橙色）的陈述表明受访者更多地不同意该陈述。这里每个语句要么是使用依赖异味/方法的基本用意（标有'+'）或使用异味/方法的缺点（标有'−')。

总体而言，图 4 第三列所示的结果表示开发人员基本同意 21 项陈述中的 15 项。开发人员大多同意所有与使用 SemVer 的好处相关的陈述，以及未使用和缺少依赖项可能导致的问题。除此之外，我们还看到了关于使用依赖气味的缺点的更普遍的共识。例如，与固定依赖相关的三个高度一致的陈述都与固定依赖的缺点有关：随着时间的推移增加错误和漏洞，增加安装大小并为维护人员带来额外的开销。我们在高度同意的许可约束和 URL 依赖声明中观察到类似的情况，表明开发人员倾向于同意使用依赖气味的缺点。

* **RQ3：为什么 JavaScript 当中会引入这些依赖异味**

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WEgYT5v0FD943vRPBAp20zicTdgN9feRW5dfOBtyLtxy5M4tN8ZWmw2FAbiatric0VSet1S7h9m1Mic7A/640?wx_fmt=png)

图 5 原因分析

在对 100 名开发人员调研后，共收到 28 封回复，之所以只对四项异味进行调研，是因为后面是属于管理不善。最后总结出如图 5 的 10 条原因。（而具体原因分析原文中也有做解释，这里不多赘述）

最后研究者还从时间发展的角度研究了前四种异味的变化，发现增加数目大于修正数目，这也是为什么尽管有修正，但总数也是不断上升的原因。曲线如图 6 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WEgYT5v0FD943vRPBAp20zicUHVnqSeNh4NQ7nAHXkG1YJkGClqIS3kl1BOLCIc378H9wQu5WgicF3w/640?wx_fmt=png)

图 6 随着时间的推移，依赖气味的积累

## 5 个人思考

* NodeJS 的无用依赖很多，在文中也有所体现，这个可以类比 Java Maven 生态系统中正在做的去臃肿依赖（Bloated Dependency）问题进行下一步研究
* 真正缓解该领域依赖管理的前四个问题还是需要指定统一标准比较重要，大部分是开发人员的职业习惯或者和对 SemVer 的不熟悉有关

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