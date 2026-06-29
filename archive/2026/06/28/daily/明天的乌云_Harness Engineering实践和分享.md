---
title: Harness Engineering实践和分享
url: https://blog.xlab.app/p/c3ac2cfd/
source: 明天的乌云
date: 2026-06-28
fetch_date: 2026-06-29T06:34:21.140953
---

# Harness Engineering实践和分享

[明天的乌云](/)

透明人博客

* [首页](/)
* [分类](/categories/)
* [归档](/archives/)
* [日报专栏](https://daily.xlab.app/)
* [我的推荐](/links/)
* [友情链接](/friends/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [1. Harness Engineering](#Harness-Engineering)
2. [2. 文档工程](#%E6%96%87%E6%A1%A3%E5%B7%A5%E7%A8%8B)
   1. [2.1. 更好的模型和更轻的SDD](#%E6%9B%B4%E5%A5%BD%E7%9A%84%E6%A8%A1%E5%9E%8B%E5%92%8C%E6%9B%B4%E8%BD%BB%E7%9A%84SDD)
3. [3. 项目质量保障](#%E9%A1%B9%E7%9B%AE%E8%B4%A8%E9%87%8F%E4%BF%9D%E9%9A%9C)
   1. [3.1. 独立review反馈](#%E7%8B%AC%E7%AB%8Breview%E5%8F%8D%E9%A6%88)
   2. [3.2. 完善的测试和环境](#%E5%AE%8C%E5%96%84%E7%9A%84%E6%B5%8B%E8%AF%95%E5%92%8C%E7%8E%AF%E5%A2%83)
   3. [3.3. 人类决策和把关](#%E4%BA%BA%E7%B1%BB%E5%86%B3%E7%AD%96%E5%92%8C%E6%8A%8A%E5%85%B3)
4. [4. Agent并发和管理](#Agent%E5%B9%B6%E5%8F%91%E5%92%8C%E7%AE%A1%E7%90%86)
5. [5. Harness本身的迭代](#Harness%E6%9C%AC%E8%BA%AB%E7%9A%84%E8%BF%AD%E4%BB%A3)
6. [6. 人还需要做什么](#%E4%BA%BA%E8%BF%98%E9%9C%80%E8%A6%81%E5%81%9A%E4%BB%80%E4%B9%88)

![透明人](/images/logo.png)

透明人

Tmr Blog

[203
日志](/archives/)

[33
分类](/categories/)

[161
标签](/tags/)

0%

链接

* [透明日报](https://daily.xlab.app/ "https://daily.xlab.app")

# Harness Engineering实践和分享

发表于
2026-06-28

分类于

[AI](/categories/AI/)

阅读次数：

本文字数：
5.4k

阅读时长 ≈
5 分钟

没有复杂的Claude/Codex Harness，极致简单朴素的Harness Engineering实践

项目人工智能成分100%，本文能工智人成分100%

内部版本 [bytetech](https://bytetech.info/articles/7656642643368034319)

## Harness Engineering

2026年2月，OpenAI发布了一篇[Harness Engineering](https://openai.com/zh-Hans-CN/index/harness-engineering/)文章

> 构建并交付一款软件产品，**其中没有一行代码是人工编写的**
>
> **人类掌舵，智能体执行**
>
> 五个月后，该代码仓库已经拥有约一百万行代码，从应用逻辑、基础设施、工具、文档到内部开发者工具应有尽有

3月开始我做一个阅读产品的side project，计划实践一下Harness Engineering

三个月过去，同样没有一行代码是人写的，项目已经完全由Agent接管

**接管的不只是开发，而是包含设计、开发、测试、运维等全流程**

> 3个月是因为这是side project，另外就是纯token有限

整个的技术栈非常简单透明，同时证明了**Harness Engineering可以非常朴素**

> 这8个里面有3个是我写的（广告）

* 模型：GPT-5.5 / DeepSeek-V4-Pro
  + GPT-5.5绝对主力，DS在没token的时候顶一下
* Agent：[Pi Agent](https://pi.dev/)
  + 除了极早期使用了Claude Code，中途换成了Codex一小段时间，绝大部分的主要工作都是用Pi Agent完成的
* 上下文管理：[pi-context](https://github.com/ttttmr/pi-context)
  + 最早切换到pi其实是为了迭代这个插件，进过多轮迭代已经完全重写到2.0版本非常好用了，让模型长期保持低占用高智力工作
* 任务管理：[pi-tmux-task](https://github.com/ttttmr/pi-tmux-task)
  + Pi没有后台任务功能，对于长耗时异步任务（比如subagent调度/开发服务运维等），后台任务能力是必要的，但没必要过度设计tool，让agent用tmux管理就好了
* 联网搜索：[pi-web-search](https://github.com/ttttmr/pi-web-search)
  + 搜文档查资料必备
* Sub Agent：[Paseo](https://github.com/getpaseo/paseo)
  + Pi没有sub-agent功能，理论上也可以用pi cli实现，但paseo封装好了，还有ui方便观察
* 通用Skill: [waza](https://github.com/tw93/waza)
  + think和hunt非常好用
* IDE: [Zed](https://zed.dev/)
  + 代码变成了只看不写之后，VS Code甚至都太重了，Zed更轻量同时很方便的切换worktree变得很好用，但VS Code的Git功能比Zed好用太多了

整个项目是monorepo组织的，包含前后端，为了简单保持全栈Nodejs（早期后端是go写的，未来也可能切换到go，毕竟内存占用低）

整体是Spec-Driven Development（SDD）模式，目前人和Agent都会提需求（issue），然后进入开发流程，人只决策做什么？怎么做？以及验收有没有做好

统计了一下代码整体30+万行，大部分都是文档，生产代码和测试代码各占一半

| 语言 | 类型 | 文件 | 行数 |
| --- | --- | --- | --- |
| Markdown | 任务类（SDD） | 800+ | 17w+ |
| - | 说明类 | 100+ | 1w+ |
| - | 合计 | 900+ | 18w+ |
| TypeScript/TSX | 生产代码 | 400+ | 7w+ |
| - | 测试代码 | 200+ | 7w+ |
| - | 合计 | 600+ | 14w+ |

> 统计才发现它们似乎都有着合理的文件行数，平均200-300行

## 文档工程

Harness最重要的可能就是文档了，毕竟文档是上下文的重要组成，不仅仅是开发文档，还应该包含

* 产品：功能设计，思考，决策权衡和预期等
* 开发：架构，算法流程，数据关系等
* 设计：设计风格品味等
* 测试：测试文档和各种bug case记录
* 运维：环境运维手册
* …

一切需要被知道的知识都应该被文档化，只要有文档Agent就能干

### 更好的模型和更轻的SDD

早期用的是[superpower](https://github.com/obra/superpowers)，后来发现这个流程实在太重了

随着模型能力提升，在文档中塞太多内容/代码已经没有太大必要，于是我迁移到一个更轻量的自定义SDD上

所有任务只有两个文件，**要做什么**和**要怎么做**

1. issue.md：简要描述任务目标，比如要实现什么功能、设计方向、解决什么bug等
2. plan.md：记录解决方案、思考决策、实现步骤拆分等等（类似于superpower里spec和plan的融合压缩版）

因为项目是纯本地的，没有任何外部系统依赖，也没有GitHub issue

统一使用文件夹+markdown metadata语法管理，**所有的内容都在本地**

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` - docs   - issues/     - readme.md     - open/       - 2026-06-26-xxxx.md     - close/       - 2026-06-26-xxxx.md   - plans     - readme.md     - open/       - 2026-06-26-xxxx.md     - close/       - 2026-06-26-xxxx.md ``` |

readme记录一些说明、规范和模板，比如目前的issue模板，利用metadata语法建立文档/代码之间的关联关系

> 模板其实都是Agent自己设计慢慢迭代出来的

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` title: "Short issue title" status: open kind: bug | feature | ux | performance | accessibility | security | security-hardening | hardening | tech-debt | docs | test priority: urgent | high | medium | low | very-low | parked triage: actionable | planned | needs-plan | needs-design | needs-decision | needs-profile | blocked | parked | wontfix created: "YYYY-MM-DD" updated: "YYYY-MM-DD" areas:   - web   - reader resolution_plan: "docs/plans/open/example.md" # optional depends_on:                              # optional   - "docs/issues/open/example.md" follow_ups:                              # optional   - "docs/issues/open/example.md" related:                                 # optional   - "apps/web/src/example.tsx" ``` |

除此之外，要保持文档更新，像维护项目代码一样维护文档，每个plan里都会要求更新相关文档

像OpenAI一样通过外部定时任务检查和更新文档也是一个好办法，但我发现在plan中**加入自动更新文档机制，并且让文档们链接起来**，模型在更新文档的时候就不容易遗漏，定时任务能发现的内容就比较有限了

## 项目质量保障

issue和plan驱动开发本身很简单，但要做好的工程还很远，模型很容易犯错

> 人也一样，不仅会犯错甚至还会偷懒，Agent有时候比我靠谱

### 独立review反馈

目前每个plan写完和开发完都都有一个独立的review，去检查plan是否完善，去检查实现是否完善

这两个Agent其实站在不同视角，这能很大程度上提高准确性和稳定性

### 完善的测试和环境

众所周知测试是很重要的质量保障工作，所有的plan都需要补充相关的测试，以及后续每个bug case都需要对应有测试补全，来持续保持质量

另外除了常规的单元测试和e2e测试来保障质量之外，我还补充了一个意图测试，像真实用户一样把产品功能都使用一遍，利用模型的“直觉”来发现问题

> 这里必须有视觉模型，像真实用户一样就要求多截图去看，文本模型这块只能猜效果很差

首先独立建立整个产品的功能梳理，对齐当前产品预期（需要同步更新文档）

相比e2e测试，文档在全不在细，需要列清楚预期的功能，但不需要写细节，比如只需要写在xx处有添加入口，支持输入文本和链接

同时还要生成对应的测试环境数据，并且为支持并行测试（在一个意图测试环境中可以并行多个测试agent，比如一个跑首页，一个跑设置页），还需要对所有不可逆的测试项（比如删除某个配置）设计独立的测试数据

另外这里callback回文档中的areas字段，是为了标识任务的改动范围，在plan完成后就只需要跑对应的测试来节省时间

### 人类决策和把关

项目早期我还会看spec和plan文档，甚至有code review，但随着项目变得复杂（有些看不懂），任务变多（看不过来）

现在流程里，人只做两件事

1. 确认Plan
2. 确认代码合并

但不再看各种文件或者代码本身，而是查看摘要，查看结果，以及对话询问去检查（有点像面试）

* 所有的plan都要提供任务解释和关键决策等信息
* 所有涉及ui的plan都提供设计图或者html交互预览
* 所有代码合并都提供关键改动说明，并提供项目的预览地址

以此做到**即使不写一行代码，也对项目的所有关键逻辑和流程都有清晰和准确的认知**

**确保做决策的人对这件事有足够的认知，才能做出正确的决策**

## Agent并发和管理

当第一次建设并跑完整个意图测试之后，Agent一次写了20多个issue，我就知道这个人是看不过来的

于是尝试让Agent自己管理去解决这些任务，就有了多agent架构

所谓：人只需要和一个主Agent交流，这个Agent会管理好其他所有Agent干活

由于许多任务都是异步的，比如可以开5个线程去研究issue，再开3个线程去开发已经批准通过的plan，只要有线程空着，就可以自动找一个任务分配去做

此时就会发现这个主Agent的上下文会由各种不太相关的任务交织在一起，这对模型的要求非常高，尤其是指令遵循能力，要能做多任务切换，讨论产品设计，讨论技术方案，还要做任务编排，包括优先级定义，任务冲突分析等等工作，类似一个项目经理+技术Leader的角色吧

以至于目前只有GPT-5.5能干，而且干的也不是很好，GPT-5.4/DeepSeek直接没法用，Gemini更是不靠谱

> 看来暂时只有人类能做好这种八爪鱼的工作

比如目前Agent在和用户讨论一个plan的设计，此时有一个agent开发完了，要用来批准合并，理想情况下Agent在和用户讨论完之后，就应该把合并的事情拿出来了给用户看了

问题之一是丢任务（低概率），Agent有时候会直接忘记不管这个事情（说我以为这是干扰通知）

问题之二是主动性不够（高概率），Agent在和用户讨论完之后不会主动的把这个事情拿出来给用户，一定得要用户问“看看下一个任务”

丢任务的问题harness能解决，但主动性迭代了很多轮都没有显著提升，可能得靠模型迭代了

不过目前除了能力问题，当并发多了之后会明显感觉主agent成为新的瓶颈了，收到sub-agent消息要去处理，这时候没空和用户对话了，可能也和subagent调度有关系，比如拆分面向用户和后台任务的两个线程，但改动就比较大了，目前还是开多个tab跑主agent来解决

另外一个方向就是把主动性的问题交给程序，比如看板流程驱动（类似[multica](https://github.com/multica-ai/multica)的产品）

> Harness怎么在团队中落地和协作可能和并发问题类似
> 允许多个用户去创建issue，应该由一个带并发的agent来处理这件/些事，云端agent可以直接共享一个数据源
> 本地agent和云端agent协同可能得靠类似git或者其他的同步机制了

## Harness本身的迭代

Harness仍然是围绕上下文的工作，只是上下文变成的项目文档，Agent的上下文从人类组织，到人类提供Agent组织

**Harness不是一次建成的，而是文档和工作流的自然迭代**

Harness去迭代项目，也需要有另一个外部循环去迭代Harness，优化现有的工作流（某种意义上来说也是一种项目级别的自我迭代）

最简单就是如果发现当前对话执行得不是很好，就可以再开一个Agent，让它去检查当前对话有什么可以优化的地方，进而优化整个工作流

当然也可以做成定时任务，定期回顾对话去迭代Harness

**Harness也不是标准答案，更像是对这个项目的量体裁衣**

不同的项目可能会有不同的Harness，但可以有预制的版型，再辅助一些定制化改动，而且不止是软件工程领域，还会有各种领域的Harness

有了各种领域的Harness，也会有做Harness模板套用工作的Meta Harness

> 突然也理解为什么FDE（Forward Deployed Engineer前沿部署工程师）会火了

## 人还需要做什么

Harness Engineering无疑在软件开发上带来巨大变革，但仍然是**人类掌舵，智能体执行**

短期看，一方面是需要阻止Agent在项目里堆屎山，积极的引导AI重构，另一方面是验收测试，模型视觉能力还是比较弱的，很难发现交互体验和UI上的问题，比如某些交互体验是连续动画，仅靠代码/截图也很难发现问题

长期看人只需要做产品和技术的关键决策，Agent可以提供各种的产品/技术方案让人来选

只要产品是给人用的，就需要人来对齐，想要什么样的产品，来提需求和砍需求

关于技术决策可能存疑，为什么人能做出更好、更对的决策呢？为什么Agent做不出来？（难道你比模型聪明？）

我觉得Agent做不出来不会是模型能力问题，而是缺少上下文，因为人会对这个产品有一个虚拟的未来预期，也就是这个产品未来会变成什么样子，但是这个预期没有变成上下文写在文档里，或者说它甚至很难变成一个文档，就像乔布斯说的“很多时候，人们在看到产品之前，并不知道自己真正想要什么”

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/at...