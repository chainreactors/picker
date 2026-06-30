---
title: AI工具调用的三层架构_CLI_Skill与MCP到底怎么分工
url: https://mp.weixin.qq.com/s/pONL3hQDr7QfEb855gdGgg
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:05:44.500328
---

# AI工具调用的三层架构_CLI_Skill与MCP到底怎么分工

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JEth9NwFY4G28c6iaguQxkmzhsz1ibG6z6XMCH1cJwba2ESqhayuWH6uruuIh75oSdwcH4ey31hTwV10XObUNzEdb4opGgF7tQicJhiabhSoibdo/0?wx_fmt=jpeg)

# AI工具调用的三层架构\_CLI\_Skill与MCP到底怎么分工

原创

lidasimida
lidasimida

安全学习之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

执行层、上下文契约层、控制平面：比“谁取代谁”更重要的工程问题

# 目录

一、先给结论：别把执行入口、说明书和协议端点混成一件事

二、第一层：执行层，真正干活的是工具能力

三、第二层：上下文契约，AI 怎么知道有什么、怎么用

四、第三层：控制平面，谁批准、谁记录、谁负责

五、为什么“模型更聪明”解决不了协议问题

六、CLI 路线的深层优势：低耦合、可探索、可组合

七、MCP 路线的深层优势：可发现、可协商、可治理

八、skill、CLI、MCP 的真实关系

九、状态、会话与长任务：MCP 不只是函数调用

十、安全边界：MCP 不是安全本身，而是安全挂点

十一、工程选型矩阵：什么时候用 CLI，什么时候用 MCP

十二、FAQ：8 个容易误判的问题

十三、专业术语注释

十四、参考资料

#

# 一、先给结论：别把执行入口、说明书和协议端点混成一件事

一句话核心观点：CLI 是执行入口，Skill 是给 AI 的操作说明书，MCP 是让 AI 应用标准连接工具和上下文的协议端点。三者不是同一层东西，真正的工程问题也不是“谁取代谁”，而是你的系统缺执行能力、缺上下文契约，还是缺治理边界。

很多团队开始做 Agent 工具接入时，会遇到一个看似简单的问题：既然模型已经能读 help、能写脚本、能根据报错修正命令，为什么还要把工具封装成 MCP？反过来，如果 MCP 已经能暴露 tool 和 schema，CLI 是否就成了低配方案？

这两个问题都把层级混在了一起。一个 AI 工具系统至少有三层：执行层负责真正干活；上下文契约层负责告诉 AI 有什么工具、什么时候用、参数怎么填、结果怎么解释；控制平面负责授权、确认、审计、会话、安全和责任边界。

MCP 官网把 MCP 定义为连接 LLM 应用与外部数据源和工具的开放协议，并说明它提供标准方式来共享上下文、暴露工具能力、构建可组合工作流 [1]。这句话的关键词不是“工具更强”，而是“标准方式”。因此，CLI、Skill、MCP 的关系，应该从三层架构里看，而不是从流行度或新旧程度里看。

|  |
| --- |
| 本文的判断：能力不在 CLI 或 MCP 这两个名字里，能力在底层系统里；CLI/MCP 的差异，是这套能力如何被 AI 发现、约束、授权、执行和审计。 |

#

# 二、第一层：执行层，真正干活的是工具能力

执行层是真正干活的地方：CLI、HTTP API、SDK、数据库、浏览器自动化、本地脚本、云服务、RPA、函数计算，都属于这一层。天气查询、企业数据查询、GitHub 操作、图片处理、代码构建，这些能力本身不天然属于 CLI，也不天然属于 MCP。

一个能力可以被封装成 CLI，也可以被封装成 MCP tool。MCP Tools 规范说，tools 是模型可调用的函数，可以表示查询数据库、调用 API、执行计算等动作 [3]。这说明 MCP tool 的真实能力仍来自被包装的系统。

所以“CLI 做不了复杂任务”“MCP 能做 CLI 做不了的事”这类说法要小心。如果底层系统允许，CLI 完全可以做复杂任务，也可以走认证、计费和服务端风控。GitHub CLI 的 auth login 就是一个成熟例子 [9]。真正的问题不是 CLI 有没有能力，而是这份能力能不能被 AI 稳定理解和安全调用。

表 1：同一底层能力可以有多种外壳

|  |  |  |  |
| --- | --- | --- | --- |
| 底层能力 | CLI 外壳 | MCP 外壳 | 关键差异 |
| GitHub 仓库操作 | gh issue、gh pr、gh auth | GitHub MCP server 暴露 tools | MCP 更利于 host 发现工具和约束参数；CLI 更利于脚本与本地开发 |
| 企业数据查询 | 官方 CLI 或内部脚本调用 API | query\_company、get\_report 等 MCP tool | MCP 更适合跨 host 分发和审计；CLI 更适合内部自动化 |
| 图片/音视频处理 | FFmpeg、ImageMagick、本地脚本 | 封装成 edit\_image、transcode\_video tool | MCP 提供工具说明和 schema；CLI 提供底层可组合能力 |
| 运维和构建 | kubectl、docker、npm、pytest | 封装为 deploy、run\_tests、inspect\_logs tool | 高风险动作需要控制平面，不只是执行入口 |

#

# 三、第二层：上下文契约，AI 怎么知道有什么、怎么用

AI 工具调用最难的不是“执行命令”，而是“让模型知道有哪个工具、该在什么时候用、参数怎么填、结果怎么解释”。这就是上下文契约层。

CLI 的上下文契约通常来自 help、README、示例、错误信息、man page、skill.md 或开发者提示。它的优势是灵活：模型可以按需读取 help，可以试错，可以根据报错修正。它的问题也明显：help 格式不统一，参数约束不统一，输出结构不统一，host 很难做统一治理。

MCP 的上下文契约更标准。Architecture 页面说明 MCP primitives 支持 list 方法，client 可先列出可用 tools，再执行它们；Tools 规范规定 tool 有 name、description、inputSchema、outputSchema、annotations 等字段 [2][3]。这让工具从“人类读说明书”变成“host 和模型可发现、可校验、可更新的协议对象”。

![](https://mmbiz.qpic.cn/mmbiz_png/JEth9NwFY4GFKX2fT9mhQTLXnm6BeibYibTRDOcia2ZyyTHvV5uEkcURzqX9iciaTuB6JBtPE4tExS6JYmPTt5nSZPvvrS9N50sibYHuOHp8XC3Yk/640?wx_fmt=png)

图 1：AI 工具调用的三层结构：执行层、上下文契约层、控制平面。

#

# 四、第三层：控制平面，谁批准、谁记录、谁负责

控制平面负责回答更现实的问题：谁能调用这个工具？调用前用户看见了什么？token scope 多大？操作有没有确认？日志在哪里？失败后谁回滚？

MCP 规范在安全与信任部分明确强调 user consent、data privacy、tool safety：用户必须明确同意并理解数据访问和操作，host 在调用任何 tool 前应取得用户明确同意，tool 描述和 annotations 除非来自可信 server，否则应视为不可信 [1][3]。

这就是 MCP 的深层价值。它并不自动让工具安全，但提供了安全挂点：host-client-server 的责任边界、capability negotiation、transport authorization、tool schema、session、progress、cancellation、logging。这些东西靠裸 CLI 也能做，但通常需要你自己额外设计一整套控制面。

表 2：三层架构分别解决什么问题

|  |  |  |  |
| --- | --- | --- | --- |
| 层级 | 核心问题 | CLI 常见形态 | MCP 常见形态 |
| 执行层 | 怎么真正完成动作 | 命令、脚本、官方 CLI、本地程序 | MCP server 内部调用 API、SDK、CLI 或数据库 |
| 上下文契约层 | AI 怎么知道有什么、怎么用 | help、README、skill、prompt、示例 | tools/list、description、inputSchema、outputSchema、resources/prompts |
| 控制平面 | 谁批准、谁记录、谁负责 | shell 权限、命令白名单、日志、人工确认 | consent、capabilities、session、transport auth、audit、tool safety |

#

# 五、为什么“模型更聪明”解决不了协议问题

模型能力提升，确实会让 CLI 路线更强。模型能读 help，能写脚本，能修正错误，能把多条命令串成流程。对内部研发、本地自动化、一次性任务来说，这是巨大的生产力提升。

但模型更聪明，不等于协议不需要。因为协议解决的是机器之间的稳定协作，而不只是模型理解能力。MCP Lifecycle 要求初始化阶段完成协议版本和能力协商，operation 阶段只使用协商过的能力 [4]。这是为了让 client 和 server 在版本、能力、身份上有明确边界。

换句话说，模型能推理出“也许该用这个命令”，但协议能告诉 host“这个 server 明确声明了这个 tool，这个 tool 的输入字段是这些，输出结构是这些，工具列表变化时会通知”。这不是同一种能力。

|  |
| --- |
| 模型智力解决“我能不能想到怎么做”；协议解决“系统能不能稳定、可验证、可治理地做”。 |

#

# 六、CLI 路线的深层优势：低耦合、可探索、可组合

CLI 的第一优势是低耦合。一个命令只要能在环境里执行，就可以被人、脚本、CI/CD、Agent 复用。它不要求 host 支持某个新协议，不要求工具作者学习 MCP SDK，也不要求用户先进入某个 AI 应用生态。

第二优势是可探索。AI 可以运行 command --help，可以读取示例，可以试错，可以根据 stderr 修正参数。对于简单工具，这种探索成本低于写一个完整 MCP server。

第三优势是组合性。CLI 天然适合管道、文件、脚本和批处理。很多工程自动化不是一次 RPC，而是一组命令、文件、中间产物、检查点和回滚脚本。CLI 在这种场景里仍然非常强。

但这些优势成立有前提：权限边界清楚、执行环境可控、失败可回滚、日志可追踪。否则模型越会用 CLI，事故也越容易被放大。

#

# 七、MCP 路线的深层优势：可发现、可协商、可治理

MCP 的第一优势是可发现。client 可以通过 tools/list、resources/list、prompts/list 等机制知道 server 提供什么 [2][3]。这比让模型猜全局命令更稳定。

第二优势是可协商。MCP 是 stateful protocol，初始化时会协商协议版本、capabilities、实现信息 [2][4]。这能避免 client 和 server 对能力理解不一致。

第三优势是可治理。MCP transport layer 负责通信通道；Authorization 规范则说明 HTTP-based transport 可使用 OAuth 2.1 进行授权，并要求 token audience validation 等约束 [5][6]。Security Best Practices 也明确要求避免 token passthrough、保护 session、限制本地 server 权限 [7]。

第四优势是跨 host 复用。一个 MCP server 理论上可以被多个 host 接入，而不是为每个 AI 应用写一套插件。这也是 MCP 像 LSP 的地方：不是更聪明，而是更标准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JEth9NwFY4F7yxG8DKtGPicpficSSlDHV2qh5Qj58IGgTQy8tcDgbgpFqvl56fWeEsYUgN3Anuz8PfLawzyLhOpy6bkBpibxvkYZOPsIQzIbOs/640?wx_fmt=png)

图 2：工程选择树：越偏本地、低风险、探索性，CLI 越自然；越偏跨 host、高风险、可治理，MCP 越值得做。

#

# 八、skill、CLI、MCP 的真实关系

做 AI 工具接入时，最容易混淆的是 skill、CLI、MCP 的层级。更清楚的拆法是：skill 是指令集，CLI 是执行入口，MCP 是协议端点。

MCP 官网把 Agent Skills 定义为 portable instruction sets，用来把领域知识、工具使用模式、auth 和交互流程编码成可移植指令 [8]。它不是协议端点，也不是可执行工具本身。

CLI 是可执行入口，可以被 skill 指导使用，也可以被 MCP server 包装。MCP server 则是 host 可以连接的协议端点，暴露 tools/resources/prompts，并参与 lifecycle、capability negotiation 和 transport。

因此，严格说不是“skill 对 MCP”或“CLI 对 MCP”，而是：一个工具系统可以同时提供 CLI 给开发者、skill 给 agent 学习、MCP server 给 AI host 标准接入。

表 3：skill、CLI、MCP 的层级关系

|  |  |  |
| --- | --- | --- |
| 对象 | 它是什么 | 它最适合解决的问题 |
| skill | 可移植指令集和任务知识 | 告诉 agent 如何判断、如何调用、如何复核 |
| CLI | 可执行命令入口 | 执行本地或远程能力，适合脚本、探索、自动化 |
| MCP server | 协议端点 | 让 host 标准发现、调用、约束和治理工具 |
| MCP config | 连接 server 的配置 | 告诉 host 如何启动或连接某个 server |

#

# 九、状态、会话与长任务：MCP 不只是函数调用

如果把 MCP 只理解成“函数调用格式”，会低估它。Architecture 页面明确说 MCP 是 stateful protocol，需要 lifecycle management；还提供 notifications、progress tracking、cancellation、logging 等 utility features [2]。

2025-11-25 规范里还出现了 experimental tasks，用于 durable execution wrappers，支持延迟获取结果、状态跟踪、昂贵计算、workflow automation、batch processing、multi-step operations 等场景 [2]。

这意味着 MCP 的位置不只是“把一个函数暴露给模型”。它更像 AI 应用和工具服务之间的会话协议。CLI 当然也能做长任务和状态管理，但通常要靠进程、文件、数据库、任务队列或自定义日志来补；MCP 则把一部分模式收进协议语义里。

#

# 十、安全边界：MCP 不是安全本身，而是安全挂点

MCP 不是安全魔法。官方安全文档反而提醒，MCP 会带来本地 server 风险、token passthrough、session hijacking、SSRF、恶意启动命令等问题 [7]。

这点非常重要：MCP 只是让安全边界更容易被表达和检查，不等于自动安全。一个恶意本地 MCP server 仍然可能读取文件、发网络请求、执行代码。一个设计很差的 MCP tool 仍然可能暴露过宽权限。

CLI 也不是天然不安全。如果它调用远程服务，服务端可以做认证、计费、审计和风控；如果它在沙箱里执行，也可以被限制文件系统和网络访问。真正的安全来自边界设计：最小权限、用户确认、日志、回滚、scope、session、沙箱和 owner。

|  |
| --- |
| 不要问 CLI 安全还是 MCP 安全。要问：执行在哪？权限多大？谁确认？日志在哪？失败怎么撤回？ |

#

# 十一、工程选型矩阵：什么时候用 CLI，什么时候用 MCP

更成熟的工程判断不是二选一，而是分层交付。

底层保留 CLI 或 SDK，服务开发者、脚本、CI/CD 和内部运维。中层提供 skill 或文档，告诉 agent 怎么使用工具、怎么判断失败、怎么复核结果。上层提供 MCP server，给 AI host 一个标准、可治理、可复用的工具入口。

表 4：CLI / skill / MCP 选型矩阵

|  |  |  |  |
| --- | --- | --- | --- |
| 问题 | 优先 CLI | 优先 skill | 优先 MCP |
| 使用者是谁 | 开发者、内部自动化、CI/CD | agent 需要学习一套流程 | 多个 AI host 或外部客户 |
| 任务风险 | 只读、低风险、可回滚 | 中等风险，需要判断步骤 | 高风险写入、付费、生产变更 |
| 工具稳定性 | 频繁变化、探索中 | 流程稳定但实现可变 | 接口稳定、长期维护 |
| 上下文需求 | 人知道怎么用，模型可按需读 help | 需要把经验写成步骤 | 需要工具发现、schema、动态更新 |
| 治理要求 | 简单日志和人工看护即可 | 需要复核点和失败处理 | 需要 consent、scope、session、audit |

·低风险内部自动化：CLI + 简短 skill 通常够用。

·复杂但私有的团队流程：CLI/SDK + skill 更灵活。

·跨 host、跨团队、外部客户可用的工具：MCP 值得优先设计。

·敏感动作：无论 CLI 还是 MCP，都要加控制平面。

·成熟产品：CLI、SDK、skill、MCP 并存不是浪费，而是服务不同使用面。

#

# 十二、FAQ：8 个容易误判的问题

Q1：CLI 会被 MCP 取代吗？

A：不会。CLI 是执行层的长期资产，MCP 是 AI host 接入工具的协议层。二者会长期叠加。

Q2：MCP 会被更强模型取代吗？

A：不会简单取代。模型变强会让 CLI 更好用，但协议、授权、审计、跨 host 复用仍然需要工程结构。

Q3：CLI help 能替代 MCP schema 吗？

A：不能完全替代。help 更适合人和模型阅读，schema ...