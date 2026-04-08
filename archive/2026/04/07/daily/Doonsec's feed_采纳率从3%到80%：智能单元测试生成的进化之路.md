---
title: 采纳率从3%到80%：智能单元测试生成的进化之路
url: https://mp.weixin.qq.com/s/Bxjh9Kj4n_y4E5gJGRhoRA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:32:32.991403
---

# 采纳率从3%到80%：智能单元测试生成的进化之路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1W9wCmVgWH6UfQszWT90NhDWQGUWcQ97PQFohibZoib01iaIlIIibpO7d4wN10LAVibRLMZgWOG4QODwBkzaN39cCqiad4ialZDx3j5ias/0?wx_fmt=jpeg)

# 采纳率从3%到80%：智能单元测试生成的进化之路

原创

快手技术
快手技术

快手技术

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**体系介绍**

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

在[《生成率从8%到60%：快手智能测试用例生成系统的四阶进化》](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247499932&idx=1&sn=fde31ecd487620a992c505214682a277&scene=21#wechat_redirect)中，快手研发效能团队重点分享了在「用例生成」环节的探索与实践，显著提升了测试阶段的自动化与覆盖能力。在此基础上，团队正逐步将智能化的触角从测试环节延伸至代码质量的源头防线——单元测试。业务高速迭代往往伴随着代码质量风险，作为保障快速交付稳定性的基石，单元测试的重要性不言而喻。但在业务高速迭代的背景下，传统人工编写模式长期受困于人力投入产出比失衡、覆盖率与有效性双低、工具辅助有限导致“治标不治本”的三大痛点，严重制约了研发效能的进一步跃升。

尽管AI生成被视为破局关键，但随之而来的“智能单测生成可用性危机”却成为新的拦路虎。面对这一挑战，本文将分享快手研发效能团队如何通过智能单测架构的多次演进升级，成功将采纳率从3%提升至80%的实战之路，进一步探索如何将个人层面的AI提效转化为组织级的交付效能。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VNWiaKWaR3GUuqr8AqOapGk9LZDo6uJTqKlBjjWicoaxI7DVRWF0cEx0iaqicpyPYak8uGI7bzIJW0PgmOhTCIibzv5MFhxokTCU7U/640?wx_fmt=png&from=appmsg)

**一、背景**

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

1.1 效率与质量的博弈：传统编写单测模式的固有痛点

在快手高速迭代的业务场景下，代码质量和交付速度的平衡面临严峻挑战。传统的人工编写单元测试模式存在三大核心痛点，严重制约了研发效率和质量保障能力。

* 人力投入产出比失衡，开发者“苦不堪言”：根据对业内的调研发现，如果想写好单测，其所需时间与编写业务代码相当甚至更长。在快手内部对单测要求严格的团队中，经常出现“半天写业务代码，一天写单测”的极端场景。这种“一行代码，十行单测”的情况严重拖慢了业务交付速度，开发者也普遍对编写单测感到枯燥乏味，缺乏动力。
* 覆盖率与有效性双低，质量保障“形同虚设”：快手单测现状充满挑战，单测接入率仅20%，全量单测覆盖率仅24%，增量单测覆盖率40%。相比业界领先水平存在显著差距。这种低覆盖率意味着大量代码变更缺乏最基本的质量保障，埋下线上隐患。
* 工具辅助能力有限，“治标不治本”：现有单测生成工具（如TestMe等插件）只能提供基础的测试模板，核心的覆盖逻辑、断言设计和复杂对象构建仍需人工完成。这种“半自动化”模式无法从根本上解决单测编写的效率和成本问题。

1.2 AI的引入与新挑战：如何突破“生成可用性”瓶颈

面对传统单测模式的困境，AI生成被视为必然出路。然而，在初期探索过程中，我们遭遇了典型的AI单测生成可用性危机，主要表现为：

* 代码调用信息缺失：AI 基于被测方法获取的信息有限，在对方法进行mock时缺失参数、返回值类型等，导致import部分出现大量幻觉；
* 生成代码质量不稳定：直接使用通用大模型生成的单测代码存在大量语法错误、编译问题和运行时异常，需要开发者花费大量时间调试和修复，反而增加工作量；
* 场景覆盖不全面：AI生成倾向于“安全”的正常场景，对边界条件、异常情况的覆盖不足，难以满足质量保障要求；
* 集成体验割裂：现有AI编码工具多为独立对话式界面，无法无缝融入快手现有的研发流程（流水线、IDE开发环境），使用门槛高；

这些问题导致初期AI单测生成采纳率低，开发者普遍持观望态度，工具价值难以体现。

**二、效果**

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

快手智能单测生成系统从1.0到3.0的演进历程，涵盖从初期的启发式生成，再到场景分组+异常智能修复，最终到知识、规则驱动。目前，该系统在快手内部每日成码10w+行，采纳率可达到80%。

* 单侧代码生成质量

AI生成单测的代码质量取得显著提升，为质量保障提供坚实基础：

+ 采纳率：3%→80%
+ 编译通过率：30%→99%
+ 执行通过率：10%→89%
+ AI生成单测的覆盖率：38.38%→80.12%

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UWA8tJjHYdSe2vw5yD6DSENMmMFJBp9y2JEcicQWMdu8xZgo9VmlCZJfBoGiaYE0rppo6HmeDOM5iahXG1YT8kUtc4GSYDPWXErI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1UlDPMWOdQpSibotibwf4aw1AIthgoGQLsyOuiaJMKaSR3ftG5iaeVLy7lw0nA5bfmJYhT1Ah23gpwuQq3fRxcSXTmiaHh8QZiaeX3DA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UOd4f7ntC8RNiaibmD62ibK7QM7vHiadwtXfhvyibJpqK5DqTecmBowqLh4dQDrpb5MJvaZYvkadQ6vzkStBoITUJ4ySP1SK5HOom4/640?wx_fmt=png&from=appmsg)

* 研发效率大幅提升

通过用户回访显示，单测生成效率相比人工编写提升3～5倍，可将开发者从重复的测试代码编写中解放出来，聚焦于更有价值的业务逻辑和创新工作。

* 规模化落地

周采纳代码行数从2千行增长至35万行，使用量从周均15次增长至300次。这表明工具已从“可用”走向“好用”，广泛获得开发者信任。目前已接入42.5%的研发仓库, 支持日均生成代码10w+行。

**三、实践1：核心技术实现**

**——从简单生成到智能工作流的演进**

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

工具不仅要能生成代码，更要生成可直接使用的、高质量的、符合业务场景的单元测试，实现从生码到入仓无干预——这是在智能单测生成系统的建设过程中，快手始终秉持的核心理念。

整个系统经历了[prompt工程探索] →[多轮异常修复+合并优化] →[知识构建+规则召回]三个阶段，现已基本实现生码到入库无干预的愿景，持续提升生码质量和采纳率，进而推动系统向更高可用性和实用性迈进。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1WkVqgfFKtkSJ6Y8a9txPLR6eAdZ6BYWgtNcX3c76H5mGe5aAG1QAeOBUA4PkIR2s5DdNXOmBFLeWYfHcgRSFLSaLZoAPibz4Ug/640?wx_fmt=png&from=appmsg)

##

## 3.1 智能单测1.0：纯LLM启发式单测生成（探索）

为解决人工编写单测痛点，我们在2025年Q2进行了引入LLM进行单测生成的初步探索，整体架构采用“目标方法识别+场景分析+AST解析+单测生成”的基础流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1WOEZm7LEpGr4oyA80GGYK3ziccmXZQF9OAhn5QlaFQyI4qJb4PO7JNJn9T2AoePNhhpsGrFJ4rVpxWLCnWHOCXCT22jsBjLeAE/640?wx_fmt=png&from=appmsg)

###

### 3.1.1 核心流程

步骤1：目标方法识别

* 目的：快速识别目标方法，降低用户负担
* 做法：

+ 基于git diff分析识别待测分支和基线分支的差异，提取新增/修改的方法
+ 解析jacoco文件，进一步筛选目标方法

步骤2：AST解析

* 解析目标方法调用的下游方法，获取下游方法的全限定名，用于作为import
* 提取同类的私有调用方法

步骤3：场景分析

* 理解逻辑: LLM理解目标方法+私有调用方法代码逻辑
* 任务规划：基于AI理解代码逻辑，分析不同测试场景（正常、边界、异常），生成测试用例规划

步骤4：单测生成

* 基于标准模板生成测试方法
* 生成基础的Mock对象和断言语句
* 将生成的测试代码合并到现有测试文件中, 处理简单的代码冲突

###

### 3.1.2 核心问题

* 生成代码稳定性差

+ 频繁出现语法错误、编译失败等基础问题，代码可用性低，大量语法错误需要人工修复
+ 未考虑编译错误、运行时异常等问题的自动修复
+ 无法解决多个case的合并冲突

* 上下文缺失

+ 没有获取代码信息的工具，所有信息来源只有AST解析和被测方法内容
+ 三方包中的代码信息无法获取
+ 对于非同类的方法调用，无脑mock
+ 无法适配kconf、kswitch等私域中间件的mock
+ 给模型的指令缺乏Know-how，过于依赖模型自主理解

* 能力缺失

+ 无法支持私有方法、抽象类方法等特殊场景的单测生成

###

### 3.1.3 阶段总结

* 数据表现：单测代码采纳率3%，生成的代码出现大量无法编译的情况，编译通过率不足40%。
* 技术验证：证明了 AI 生成单测的技术可行性，但暴露了简单串联流程的严重不足。
* 演进方向：

+ 重构整体流程，加入代码异常修复机制，提升代码质量；

+ 引入代码和jar包的查看工具，补充上下文；

+ 引入智能分组策略+工程解决，用于提升代码合并效果。

##

## 3.2 智能单测2.0：场景分组+多轮异常修复

针对V1.0阶段单测质量不稳定、编译错误多、执行失败率高的问题，我们进行了系统性重构，引入“单测场景分组+多轮异常修复”的创新架构。多轮异常修复用于提升单个case的质量，场景分组则有效地避免了大量的合并冲突。两者的互补大幅度提升了单测代码的质量，实现了从可生成到信任使用的跨越。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1W4iazlwkbwhD32bcvkd1kvDoK7BRd3CYqJuyuRNgH5nasTFWUVXYO3d17vbiaNNlwgY6aJ9NkKmSO18tic1zqjQuTP84WpLaa3c8/640?wx_fmt=png&from=appmsg)

###

### 3.2.1 单测合并

合并单测的难点：

* 多个被测方法属于同一个类文件，每个被测方法都会生成大量的单测
* 合并时要包含已有单测，必须保留用户早期单测
* 单测生成阶段除了生成大量的单测方法，还会有单测的前置和后置方法
* 如果代码中有长json，经过模型处理后会出现json文件被修改而无法反序列化的问题
* 将以上内容合并为一个文件，并且有逻辑和语法冲突

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1WgtibXLEnHUAUyia0Pib6RfEdleNhHnykENXxicm9QBzFq0P9ngTof3icyttAdt6hn2EQwzxXhahbJh6Xjsic6JwiaqvTVycubo5V2MM/640?wx_fmt=png&from=appmsg)

在V1.0版本中，将属于同文件的所有内容全部交给大模型，让大模型通过stop key分几次将合并结果返回，但生成质量不高，且LLM会引入新的错误；所以在V2.0版本中，核心思想是工程能力优先。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VG2j3U4NsaGVdID86Y8wwfLyaKSFgunBxFXtiaYFib7VH2eV4JEJL24L9qHGdK849qBtQsN6HvauHpRy6lsia2dHL0KULrg9H9mo/640?wx_fmt=png&from=appmsg)

（1）规划阶段：在待测方法和场景类型（正常场景、边界场景、异常场景等）层面上进行分组

* 场景类型分组

+ 正常场景组：验证基本业务逻辑
+ 边界场景组：测试参数边界条件和极端情况
+ 异常场景组：验证异常抛出和错误处理

* 逻辑相似性分组

+ 共享相同Mock对象的用例归为一组
+ 使用相似断言模式的用例归为一组
+ 需要相似数据准备逻辑的用例归为一组

优势：

* 相近逻辑批量处理：相近方法（例如某个方法的多个边界用例）有着相近的代码逻辑（Mock逻辑、断言方法等），也容易出现类似的问题（例如某个类Mock错误）。分组策略让这些相近方法生成和修复都在一起，实现通用逻辑的抽取以及批量修复问题。
* 减少重复工作：相似场景共享setup/teardown逻辑，避免重复代码生成
* 代码结构清晰

+ 组织清晰：不同方法和不同场景的笛卡尔积会让单测方法数量很大，也难以维护和理解；分组策略按逻辑组织测试代码，结构清晰易懂。
+ 可维护性增强：每个分组独立，修改和调试时影响范围明确。

（2）生成阶段：按照规划阶段对每个分组进行生成，一个分组对应一个nested class，组内的单测方法共享前置后置方法。

（3）合并阶段：会通过语法树对已有单测和新生成的大量单测文件进行合并。

* 使用JavaParser解析现有单测文件和新生成的单测文件

* 将多个类通过nested class的方式合并在一个语法树中，nested class内的前置后置方法共享，对外互不影响（方法合并→内部类合并)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1VLPWxIfF6ibiak5tWhlKon9ich2vDBpfUg3wuLroU5yFYOKSrIdV96RtPORvC6o4aiakMqn3F7Chv1eqX2V55ouClNfcmZSQticFfE/640?wx_fmt=png&from=appmsg)

* 收集所有的import块，并对其进行去重、排序，然后注入到语法树中
* 编译检测，如果发现问题，通过模型优化

优势

* 用户代码零修改：AST操作确保手写代码完整性
* 结构正确性：语法树操作避免大括号等结构错误
* 内容保护：长文本保护机制防止AI幻觉破坏

###

### 3.2.2 多轮异常修复

在生成单测的过程中，上下文信息缺失和模型幻觉往往导致代码出现语法错误或编译失败等基础问题，这导致代码可用性低，且人工修复成本高昂。鉴于覆盖率是评估单测效果的核心指标，而该指标的获取严格依赖于代码的可编译性与可执行性，这就要求我们必须生成“零错误”的代码。既然依赖模型一次性生成完美代码并不现实，我们便转而采用多轮次修复的方式，通过反复迭代来打磨代码质量。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VzHj1dIFhpsScyIxydGckWLrOHY5yM4jFuyfsOhWDNNgX4tLKEUejIYfTWt2peSmMQAWMn1umJsfdicQeZRHhh8gjc5sicPv3mY/640?from=appmsg)

（1）编译修复阶段

* 建立“执行-反馈-优化”的持续迭代机制
* 采用javac进行单文件编译
* 对错误类型分组，每轮只修复特定类型问题

+ 多个位置暴露同类问题，更有利于定位原因、修复
+ 避免上下文过载
+ 可批量修复

* 成功修复的方法不再参与后续轮次
* 达到质量阈值或最大轮次时自动终止
* 编译错误大多是类型不匹配、方法不存在、import缺失，可通过调用代码查看工具快速解决

（2）执行修复阶段

* 同样采用“执行-反馈-优化”的持续迭代机制
* 执行过程为了避免影响线上业务，采用沙箱环境执行（staging)
* 执行错误大多是mock造成的，在本阶段没有达成很好的效果，会在V3.0阶段基于规则和知识解决

###

### 3.2.3 并发生成

由于多轮修复大幅度拉...