---
title: 半空：LLM 辅助的 Go2Rust 项目迁移
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512796&idx=1&sn=349504697de0c8697e3b70c4e9f40922&chksm=e9d3793edea4f028a460d11f961bf245141a930e98b9bd9337b62798342ea5936552a9007b72&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-01-10
fetch_date: 2025-10-06T20:09:48.182713
---

# 半空：LLM 辅助的 Go2Rust 项目迁移

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0436mqUe6FribUygMk1SQRw2C2cZLoice7aZ31zaqQZbkaCSlriauPJCibA/0?wx_fmt=jpeg)

# 半空：LLM 辅助的 Go2Rust 项目迁移

高文举

字节跳动技术团队

试想一下：将一个 Golang 项目（大象）改写为（装进） Rust（冰箱） 总共需要几步？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0aJ9ZF8LEGuON5I7vicY5gibLKibuQuOE3htmK8l1xB2hSs6hbXNHEc4Ww/640?wx_fmt=other&from=appmsg)“Gopher in 冰箱” by DALLE3

# 背景

当 Rust 语言为我们展示出在「性能」、「安全」、「协作」等方面诱人的特性之后，却因为其陡峭的学习/上手曲线拒人千里之外。是否存在一种科技，能够帮助我们的同学在**语言学习**和**项目迁移**上完美并行，最终真正将 Rust 项目迁移这个看似美好的荆棘之果转变为触手可得的「低垂果实」呢？

为了将美好的愿望转变为实际，我们结合 LLMs 做了一些尝试，利用 LLMs 在编程语言上体现出的「涌现」能力，设计了一套基于 LLMs 的应用开发基座（ABCoder），在这个基座之上进一步演进出了我们本篇的主角：「半空」。

> ABCoder 是字节内部一个编程向 LLMs 应用开发基座，包含自研的 LLMs 原生解析器、工具（Tools）以及工作流（Workflows），对编程项目本身进行深度解析、理解和压缩，并将其制作为源码知识库（Source code as Knowledge），之后利用这类知识库实现对 LLMs 推理过程中所需上下文进行补齐，从而构建出高质量、低幻觉、稳定的编程类 LLMs 应用。有关 ABCoder 更多的介绍可以参考[这里](https://mp.weixin.qq.com/s?__biz=Mzg2MTc0Mjg2Mw==&mid=2247494657&idx=1&sn=cb6f847324d6d1a09b9d4518bd927c62&scene=21#wechat_redirect)。

# 半空

按照 ABCoder 的设想，让 LLMs 理解编程项目的入口就是结合对项目的解析、理解、压缩后的知识关联和构建，这对于一个轻量化的应用来说可能足够（ABCoder 当前已经能够实现将一个标准 Hertz 项目“转述”为一个 Volo-HTTP 项目），但对应到实际场景中的业务项目来说（增加大量业务属性且复杂度更高），要想真正让 LLMs 完整理解整个项目，并且在有需要的时候让 LLMs 完整的将整个项目“转述”为另外一个语言的项目时我们就需要对我们的**解析、理解、压缩、应用**流程进行更加细粒度的设计和优化了。

「半空」主要讨论的就是对于**复杂项目的理解提升**和**辅助** **LLMs** **渐进式多轮迭代**构建出一个复杂项目的可行性。核心需要解决的是因为项目规模提升所带来的复杂度以及上下文规模提升和 ABCoder 所制作的对应知识库知识密度跟不上的矛盾。

## 内核简述

罗马不是一日建成的，参考软件工程标准的项目迭代方式，迭代一个越庞大的项目，引入的标准作业流程和所花费的迭代周期和人力就越多。ABCoder 要想深刻的解析并理解一个大型项目，一口永远吃不成一个胖子。

好消息是构建一个复杂项目的过程是有迹可循的的，ABCoder 需要做的其实就是逆着项目构建的路径，反向解析出项目构建过程中涉及到的不同粒度的知识库。

之后将这些知识库输入 LLMs 驱动的 Workflows，通过构建渐进式的多轮迭代流，将原来的项目以任意编程语言又输出出来，基于对知识库的持续构建，甚至实现为其他语言的项目：**语言翻译**。

### 意译 or 直译？

相较于给 LLMs 一段代码，让他直接翻译为另外一个语言（直译），「半空」所做的类比下来更像是：帮助 LLMs 理解代码，之后经过抽象和设计结合我们希望它采纳的知识，重写出另外一个语言实现的版本（意译）。

### 理解和设计

按照 ABCoder 的通用处理流，一个任意庞大的项目我们几乎都可以通过解析、级联压缩的方式构建函数、方法、结构体、变量的语义化映射。但仅仅通过这些散落的信息 LLMs 是没有办法高效的建立一个对这个项目系统深刻的理解。因此我们在做 LLMs 辅助的项目文档梳理应用的时候，就已经开始下意识的做一些单元聚合工作了：通过将某个包（文件/模块）中的函数、方法、结构体、变量语义化含义进一步抽象，得到关于这个包（文件/模块）的语言和框架无关的高层次语义化抽象，按照这个思路，我们可以自底向上抽象，到最终项目维度。

举个直观的例子，对于 Hertz 的项目，任意一个 Hertz 项目在项目维度都能够抽象为形如：**这个项目是一个基于 HTTP 应用框架的应用，它或许注册了/a/b/c** **路由** **（Route）的 GET 方法（Method），关联了某个对应的逻辑（Handler）** 。

仔细分析这个抽象，尝试对其中蕴含的细节进行总结：

1. 一个基于 Hertz 的 Golang 项目，在经过某个维度的抽象之后，丢掉了大量细节，留下了一些在当前维度的关键信息。在上述例子中，我们得到的抽象已经不关心这个项目具体采用的语言实现和具体涉及到的应用框架了，仅仅需要关注的是 HTTP 框架应用以及 HTTP 应用必备的信息：注册了某个路由，处理了某个业务逻辑。
2. 通过这层抽象，我们可以将任意一个复杂项目映射出了一个最简单的迭代入口：启动一个 HTTP 应用框架，并注册处理某个 URL 的某个逻辑函数。
3. 对整个复杂项目的理解过程被我们巧妙的转换为对一个项目自底向上的逐层抽象的过程，如果我们能将这个抽象过程做的足够清晰和准确，对于一个完成抽象的项目来说，我们反过来也得到了一个支持我们至顶向下层层细化的项目构建流。
4. 理论上通过增加、减少、优化各层级抽象，我们就能不断提升对这个项目深度理解的效果。

多轮的抽象和迭代的本质是项目在不同维度上多语言实现和 ABCoder 抽象语义的不断对齐：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0BaEqLtpuiac0txUwCYQOwpFjqCKwaFEoibS0voju9GWGRHiaasLZEXsibA/640?wx_fmt=other&from=appmsg)

配合语言对应的知识库建设，按照标准抽象块（已归一化逻辑）进行知识检索，分层分模块持续迭代，填充核心逻辑，辅助业务完成项目构建。

### 实施和测试

当我们通过上述解析和抽象，得到了关于一个项目完整的理解知识，之后就可以至顶向下辅助 LLMs 逐层实现项目的渐进式迭代了。同样，接着上一小结里提到例子来说，我们在这层抽象上做的事情就是：

1. 根据「**HTTP 应用框架**」匹配目标语言对应的知识，比如检索出 Volo-HTTP 库的知识（如果我们的目标是将这个应用实现为一个 Rust 项目），之后结合 Volo-HTTP 提供的框架初始化逻辑，拉起一个 Volo-HTTP 的项目
2. 之后按照本层抽象剩下的描述信息，完成**「/a/b/c路由和对应处理函数」**的注册
3. 由于本层抽象并不具备这个处理函数的详细描述信息，因此仅仅需要生成一个空实现的桩函数即可
4. 之后我们所做的所有变成，二次确认完成了具体实现和对应语义化抽象的对齐

以上即是对一轮迭代核心流程的描述，完成本轮迭代之后即可开启下一层抽象的对齐。之后按照这个流程持续的迭代这个项目。

因为抽象本身会丢掉本层部分细节，而丢掉的这部分细节其实还是保留在抽象前的层级中的，对应迭代路径来说，上一层丢掉的细节**一定**会在下一层迭代中被补充回来。因此，通过多轮的迭代构建出来的项目，理论上也并不会丢失具体的实现细节。

每一层迭代后都会有一次**人工介入时机** —— 即可以及时人工介入修改代码并反馈到后续的翻译轮次中，这也是「半空」的核心能力之一 —— 在这个切面上能够按需的扩展任意的软件测试解决方案，包括时下流行的：LLMs 辅助 UT 生成等技术。等到所有的修改和测试通过之后，即可开启下一层的迭代或者选择直接退出手动接管剩余的翻译工作。

## 交付内容

作为用户最为关心的部分，「半空」究竟在项目 Go2Rust 转换（存量 Golang 项目改写为 Rust）上帮助我们做到哪些事情呢？其实非常简单，好比将大象装进冰箱，「半空」辅助下的 Go2Rust 自动化迁移也是**三个核心**步骤：

1. **打开冰箱门**：基于 ABCoder 对存量 Go 项目完成系统解析，产出**函数粒度的项目理解原料**
2. **把大象放进去**：基于项目理解原料产出将该项目改写为**Rust** **对应的项目设计文档**
3. **关上冰箱门**：基于设计文档中指引的迭代顺序，全自动可控地，产出**各层迭代代码**

实际上，结合简介中的描述，聪明的小伙伴也许已经发现：「半空」作为一套通用框架，应用面其实并不仅仅局限在 Go2Rust 上，对于任意语言之间的相互转换逻辑上都是完全一致的，区别在于对语言特异性处理和特定语言的知识库构建。「半空」一期重点针对 Go2Rust 场景完成内场的适配和持续打磨，后续如果有对更多语言栈（Python2Go/Java2Go/...）的切换诉求也非常欢迎勾搭~

# 项目实战举例

> 一个使用「半空」做 Go2Rust 项目转换的示例

## 项目介绍

Easy\_note 是 CloudWeGo 社区对外提供的一个基于 Hertz 和 KiteX 的实现复杂、功能覆盖度高的业务实战示例项目；其使用 Hertz 提供了若干 API 接口，并在接口实现中通过 KiteX client 发起对下游 KiteX Server RPC 接口的调用。

本次使用「半空」翻译的是其 API 模块，其主要功能列表如下：

* 用户管理

+ 用户注册 (HTTP 接口 -> RPC 调用)
+ 用户登录 (HTTP 接口 -> RPC 调用)

* 笔记管理

+ 创建笔记 (HTTP 接口 -> RPC 调用)
+ 查询笔记 (HTTP 接口 -> RPC 调用)
+ 更新笔记 (HTTP 接口 -> RPC 调用)
+ 删除笔记 (HTTP 接口 -> RPC 调用)

涉及到的 Hertz/KiteX 框架相关的核心能力如下：

* 初始化 Hertz Server
* 注册 Hertz 路由和 handler
* 实现 Hertz 自定义中间件(JWT、服务发现)
* 实现 Hertz 的 handler 逻辑
* 使用 KiteX Client 调用下游接口

## 流程说明

从输入原始项目产出 ABCoder 理解知识原料开始，「半空」会结合函数粒度知识原料，自底向上完成整个项目的逐层抽象和理解，之后至顶向下完成重构设计的制定，同时确定项目渐进式构建顺序：从**粗粒度****知识映射**到**细粒度****知识映射**到最后**逐个 Package 的实现**，最终完成 Golang 项目到 Rust 项目的渐进式构建（意译）。这个过程中项目构建进度完全由用户掌控，结合人工修改反馈辅助协同，推动项目完成 Go2Rust 迁移落地。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0oKHWX9PWImfIARfiaicQ2VUDqr25yeqIiaiaQrAGFFyjRmejhkzVSTUZYw/640?wx_fmt=other&from=appmsg)

上图提到的 Golang AST / Rust AST 是 ABCoder 在分析仓库代码，将**函数、方法、结构体、变量**等定义以树形关联出来的数据结构体集合，是一个能够与项目一比一映射的 **LLMs原生****抽象语法树**。

## 设计阶段：Package 翻译顺序

根据 ABCoder 解析后的项目原料，「半空」自动化根据 Package 的**依赖关系**完成了使用 Rust 重构这个项目所需的设计文档的编写，**自顶向下**得到如下迭代顺序：

1. "github.com/cloudwego/biz-demo/easy\_note/cmd/api"：项目的二进制入口和基础框架搭建
2. "github.com/cloudwego/biz-demo/easy\_note/cmd/api/hertz\_handler"：HTTP 通用 handler 的实现
3. "github.com/cloudwego/biz-demo/easy\_note/cmd/api/hertz\_router"：HTTP 通用 router 的注册
4. "github.com/cloudwego/biz-demo/easy\_note/cmd/api/hertz\_router/demoapi"：HTTP 业务 router 的注册
5. "github.com/cloudwego/biz-demo/easy\_note/cmd/api/hertz\_handler/demoapi"：HTTP 业务 handler 的实现
6. "github.com/cloudwego/biz-demo/easy\_note/cmd/api/rpc"：请求下游的 RPC 封装
7. "github.com/cloudwego/biz-demo/easy\_note/cmd/api/mw"：通用/业务中间件具体实现

## 实施阶段：根据设计文档顺序逐步展开

1. **"** **easy\_note/cmd/api** **"**

> 对应 MR: https://github.com/cloudwego/biz-demo/pull/83

main package，主要实现了 HTTP server 的初始化、路由注册调用等能力

| Golang 原始实现 | 「半空」意译效果 |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0TQ25Kk8uTvutKEFOHIiavN4mWwnliaxHdc7FJpqHFn03NBwevDEib7SQA/640?wx_fmt=other&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0Xk0icMIUfoTYTYjia5wRpw8Q3hMytQuOvfxd4iboia32mxGLgmvJBHcCRw/640?wx_fmt=other&from=appmsg) main() |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0qe6Zib3SunM2xR7HkmOCt4Vmco4ibppx99yBubWLezJKykic4hY18JYwg/640?wx_fmt=other&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E042Cqk6gx7JiaIyibv91Hw5pFyRneiaPbAiaAxx5rgNAo9F5k4W9QJJvWfQ/640?wx_fmt=other&from=appmsg) |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0WSibib4TpBTLIRGnNJDO7vS0M585jzHPuKLXawOemYJKHhnx7bhUDiaRA/640?wx_fmt=other&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0ia1YVqb0V8YyaTKLNLwtBGACjOWlgZahtibiaTceFVcn17FPrzz0gO8ZQ/640?wx_fmt=other&from=appmsg) 常量定义[mock实现] |

* **结果评估**

+ 目录：所有 `main` package 的内容，都生成到 Rust 项目的 `/src/bin/main.rs`下；后续支持细粒度的文件模块映射
+ 内容：翻译的函数内容、逻辑正确；辅助生成的注释清晰体现核心步骤
+ 错误：存在 Opentelemetry 使用上的报错；原因：目前还没有注入相关知识，后续通过知识库飞轮进行持续补充，其他缺少三方知识的问题类似，结合知识库飞轮会持续收敛
+ Mock：Main package 会依赖其他包的内容，因此会将其他 package 下的内容进行 mock，确保可以正确编译

* **数据统计**

+ > 生成节点完备率=无需改造的节点/生成节点总数
  >
  > 可编译度=1-修改的代码行数/生成的代码总行数
+ 生成节点完备率: 50%
+ 生成代码可编译度：73%

2. **"** **easy\_note/cmd/api/hertz\_handler** **"**

> 对应 MR: https://github.com/cloudwego/biz-demo/pull/84

hertz\_handler package 主要实现了一个 ping handler，用于处理 ping-pong 请求

| Golang 原始实现 | Rust 意译效果 |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E0SwVnSrHjtfsBcmUt0UDRrHL7TwibEGciaa2gkFibUySvKRSvvcRShJmRw/640?wx_fmt=other&from=appmsg) Ping() | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgX9BvELaF5pcHuYFau55E014k1wFdRDP3tSZuZaOoWY6EMXGMzCicGn7qdDAVRK...