---
title: 天津大学 | 基于操作依赖分析的MLIR编译器基础设施模糊测试
url: https://mp.weixin.qq.com/s/3gMCod0GCb6ZO29NtWnJcQ
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:50.723197
---

# 天津大学 | 基于操作依赖分析的MLIR编译器基础设施模糊测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEkpibswMXJXnqApQUUIpYSQMGKWm5ib74hVKl78XN7Y6s3JAUZvJSwj7tcS78et5IMZyowwAJricUww/0?wx_fmt=jpeg)

# 天津大学 | 基于操作依赖分析的MLIR编译器基础设施模糊测试

原创

马硕
马硕

安全学术圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEkpibswMXJXnqApQUUIpYSQB3RTibRmWgK7TShe2bh8bDnrLuUEA7tOyaVABR4UDSHSlVC2iaJDkWwQ/640?wx_fmt=png&from=appmsg)

> **论文题目：Fuzzing MLIR Compiler Infrastructure via Operation Dependency Analysis**
> **论文作者：Chenyao Suo, Junjie Chen, Shuang Liu, Jiajun Jiang, Yingquan Zhao, Jianrong Wang**
> **发表会议：ISSTA**
> **主题类型：漏洞检测**
> **笔记作者：马硕@Web攻击检测与追踪**
> **主编：黄诚@安全学术圈**

# 研究概述

MLIR是由LLVM项目推出的一种中间表示框架，旨在通过统一的基础设施支持不同层次和领域的中间表示（IR）。核心理念是通过方言（Dialect）机制来处理多层次IR，从而适应多样化的计算需求和优化要求。现有的模糊测试技术无法直接应用于MLIR，其原因有三：

1. 首先是测试对象的不同，传统模糊测试技术直接生成高级源代码作为测试用例，而MLIR编译器需要生成和测试中间表示而不是源代码；
2. 数据结构和语义上的差异，传统的模糊测试技术不适配MLIR中的操作、属性和类型的复杂语义，生成的操作序列往往不符合Dialect规则，导致无效或非法输入；
3. 测试效果较差，传统方法生成的高级源代码经过前端转化为MLIR，作为测试样例的多样性较差，样本的覆盖率和语义多样性不足。

本文提出了MLIRod，使用操作依赖图和其相关的操作依赖覆盖率来指导fuzz，并设计了一系列的突变规则以获得尽可能高的覆盖率。![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEkpibswMXJXnqApQUUIpYSQSgxQSQm942DAqO4ibibnPP100f1n6xG4UfTXmibuictruLM4g9D7LnXeFA/640?wx_fmt=png&from=appmsg)

上图显示了MLIRod的概述，具体而言，MLIRod为每个MLIR程序构建一个操作依赖图（ODG），然后基于该图测量相应的操作依赖覆盖率，模糊测试过程被驱动向增加操作依赖覆盖率的方向发展。同时，为了生成促进操作依赖覆盖率增加的MLIR程序，MLIRod精心设计了一套变异规则，其重点在于建立新的依赖关系或修改操作之间的现有依赖关系。

MLIR编译器中，某些类型的优化只会在特定操作组合的情况下发生，因此需要利用操作依赖提高测试样例生成的效率（实现尽可能高的操作依赖覆盖率）。**操作依赖图**（ODG）中包含了数据依赖和控制依赖。操作由其名称、操作数和结果组成，将操作简单地认为是某个名称下的操作数和结果的抽象单元是粗粒度的，难以触发某些bug；将操作的名称和特定的值和结果认为是一个抽象单元实现了细粒度，但会导致ODG空间过大，效率降低。因此本文将一个操作及其操作数和结果的类型作为一个基本单元，称为操作实例。

**操作依赖覆盖率**则是测试集中所有程序的操作依赖模式，在所有可能的操作依赖模式空间中所占的比例，其公式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEkpibswMXJXnqApQUUIpYSQiaNDicm45yUiafBhpjbgrjHFn10XhYe1U46AAjxNuDibfGFXSyRTwLqP8A/640?wx_fmt=png&from=appmsg)

本文中仅使用操作依赖覆盖率指导输入空间的探索，并非测试充分性评估，因此直接采用分子值表示操作依赖覆盖率。

* **突变规则**，旨在创建新的依赖或者修改已有操作之间的依赖，从操作依赖图的角度来看，只需要修改图中的节点和边即可实现，因此作者主要设计了以下四种突变规则：
* **节点插入：**向操作依赖图中插入随机节点，然后根据插入的节点类型引入依赖边。在插入新节点时，倾向于将节点放在能够被某个已存在的操作实例控制的位置，从而引入一条新的控制以来边。
* **节点删除：**随即删除操作依赖图中存在的节点，并更新由于节点删除造成的依赖边更新。
* **数据依赖修改：**随机挑选一个节点，将该节点数据依赖的节点替换为图中其他类型兼容的节点。
* **控制依赖修改：**更新MLIR程序的操作依赖图中随机节点的控制依赖，同时保证所有数据依赖不变，具体操作就是将一个操作实例从一个内层条件块转移到外部，从而修改控制依赖。为保证被移动到外层的操作节点数据依赖不变，将其数据数据依赖的节点也移动到外层（使节点的相对顺序不变）。

**最终的整体模糊测试流程即为：**

1. 种子池的初始化，利用MLIRSmith中的种子生成技术（随机生成）构建种子池，然后计算种子程序的操作依赖覆盖率；
2. 突变程序的生成，在每次fuzz迭代过程中，从种子池中随机选择种子程序和突变规则，创建新的MLIR程序；
3. 基于MLIR-Pass的模糊测试，从MLIR官方文档说明的pass中随机选取k个，并随机决定顺序，对输入的MLIR程序进行IR转换、优化。如果发生了崩溃现象，认为该测试程序检测到编译器中的bug。同时收集所有经过IR转化、优化而产生的新MLIR程序，用于维护种子池；
4. 基于操作依赖覆盖率的种子池维护，如果通过变异生成的MLIR程序使操作依赖覆盖率增加，则将该MLIR程序放入种子池，在fuzz过程中每个MLIR pass转化后也会检查转化后的程序是否提高了操作依赖覆盖率，如果有所提高也会放入种子池。

# 贡献分析

* 贡献点1：论文针对现有MLIR模糊测试工具（如MLIRSmith）采用随机生成策略，导致输入空间探索受限的问题，提出了一种全新的、基于操作依赖性的覆盖率度量方法（OD coverage）。该方法通过构建操作依赖图（ODG）来捕捉MLIR程序中操作间的数据和控制依赖关系，从而更精确地衡量测试用例的多样性；
* 贡献点2：论文基于新的覆盖率度量标准，提出了一种名为MLIRod的新型模糊测试技术。该技术不依赖于随机生成，而是以提升操作依赖覆盖率（OD coverage）为导向，通过一套精心设计的、针对依赖关系进行变异的规则（如节点插入/删除、数据/控制依赖修改）来高效地生成能够触发深层错误的测试用例；

# 代码分析

代码链接：https://github.com/tju-chenyaosuo/MLIRod

关于代码使用的类库，MLIRod是作者在其原有工作MLIRSmith的基础上进一步完成的，所以使用了MLIRSmith中的一些功能模块以及LLVM中MLIR相关的部分；关于主要fuzz过程，MLIRod实现了自己的一个运行脚本用以调用，包含其在论文中提到的种子生成模块、种子池、突变器以及覆盖率等等，最终脚本中代码行数共561行，实现难度相对简单。其后端所使用的用于突变和覆盖率收集的部分实现难度相对较高，突变部分需要对MLIR的语法规则有完整的了解，保证突变后的MLIR程序仍然正确；覆盖率收集没有采用传统的插桩，而是在运行结束后正确地构建MLIR程序的操作依赖图并静态分析其中的操作依赖，所需要的工作量相对较大。

# 论文点评

1. **bug判断规则的局限性：**MLIRod与MLIRSmith一样，主要依赖“程序崩溃”（Crash）作为发现bug的唯一标准。这意味着它无法检测到不会导致崩溃、但会生成错误代码的bug。论文也承认，由于生成的程序可能包含未定义行为，导致采用差分测试等更复杂的预言机时容易产生误报。因此未来的工作可以专注于增强程序生成模块，通过引入机制来识别和避免未定义行为。这将使得集成更高级的测试预言机（如差分测试，即比较不同优化等级下的编译结果）成为可能，从而能够捕获更广泛类型的编译器缺陷。
2. **对初始种子池质量的依赖性：**作为一种基于变异的Fuzzer，MLIRod的最终效果可能受到初始种子池质量的影响。实验中使用了50个随机生成的MLIR程序作为初始种子，但没有讨论不同来源或规模的初始种子对结果的影响。因此需要更全面的种子选择策略研究，比较MLIRod在使用不同的种子集时的表现，评估该工具的鲁棒性及对初始条件的敏感度。
3. **突变规则的丰富度：**文中设计了四种核心的变异规则。尽管实验已经证明了它们的有效性，但可能还存在其他更复杂的、能够构建更特殊依赖关系的变异策略未被探索。未来可以基于对已发现bug的根源分析，设计更多样化、更具有针对性地变异规则。例如，可以设计专门用于构造特定方言组合或罕见操作序列的规则，以探索MLIR编译器更复杂的状态。
4. **结合大模型：**在测试用例的生成和突变上可以利用LLM的知识，避免随机生成以及突变规则的限制，同时，在MLIR pass的选择上，也可以利用LLM来读取文档，判断适用的优化序列，避免由于优化序列的错误选择造成模糊测试效率的降低。

# 论文文献

1. Suo C, Chen J, Liu S, et al. Fuzzing MLIR Compiler Infrastructure via Operation Dependency Analysis[C]//Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis. 2024: 1287-1299.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

---

**专题最新征文**

* [期刊征文 | 暗网抑制前沿进展](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491610&idx=1&sn=8b6c9caf92435cbd9b76b77686619972&scene=21#wechat_redirect) (中文核心)
* [期刊征文 | 网络攻击分析与研判](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491661&idx=1&sn=ab0a97741cdf854757ef3024b03f1d44&scene=21#wechat_redirect) (CCF T2)
* [期刊征文 | 域名安全评估与风险预警](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491703&idx=1&sn=7f351031fc81e1b63d5215ddb8dc91b5&scene=21#wechat_redirect) (CCF T2)

---

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