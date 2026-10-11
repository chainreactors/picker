---
title: 用大模型做智能体工具治理(ATG)原型—— 拦截点设计 · 专项Prompt模板 · 投毒检测代码骨架 · 五天实战
url: https://mp.weixin.qq.com/s/5cOfonz_1TQFLIeVLBUofA
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:01:02.296514
---

# 用大模型做智能体工具治理(ATG)原型—— 拦截点设计 · 专项Prompt模板 · 投毒检测代码骨架 · 五天实战

# 用大模型做智能体工具治理(ATG)原型—— 拦截点设计 · 专项Prompt模板 · 投毒检测代码骨架 · 五天实战

原创

H
H

AI安全推进计划

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

导读  这份手册和通用版有什么不同

通用版手册解决的是「怎么用大模型加速原型生产」。这份手册解决的是更具体的问题:当原型对象是「智能体的工具调用」时,该在哪里拦、怎么拦、怎么让客户相信真的拦住了。

|  |
| --- |
| 一句话区别  通用原型检测的是「文本里的攻击」;ATG 原型管控的是「智能体要做的动作」。前者看内容,后者看行为。 |

由此带来三个根本差异:

● 技术前置不同:必须先跑通 MCP 链路(JSON-RPC 通信),否则无从下手

● 拦截对象不同:不是拦文本,而是拦「工具调用参数」与「工具返回内容」

● 演示冲击力不同:客户能直接看到「一个危险调用被当场挡下来」,冲击力远强于检测结果展示

手册围绕这三条差异组织内容:D1–D4 覆盖四项子能力的技术解剖,第 3 章讲拦截点设计,第 4 章给四类专项 Prompt 模板,第 5 章是完整的五天实战,第 6–7 章讲审计与避坑。

重要提示:本手册涉及的 MCP 协议细节以公开协议规范为准;实际实现需结合所用框架版本确认。所有样本与代码为方法示意,不针对任何具体产品。

1  ATG 四子能力与技术解剖

1.1  为什么智能体安全是独立的战场

传统的 AI 安全关注「模型说了什么」——内容是否合规、是否被注入。但智能体改变了风险的本质:它不再只是「说」,而是能「做」——调用工具、读写文件、访问网络、执行命令。

|  |  |  |
| --- | --- | --- |
| 对比维度 | 传统AI安全 | 智能体安全(ATG) |
| 风险载体 | 模型输出的内容 | 智能体的动作与工具调用 |
| 攻击面 | 提示词、上下文内容 | 工具描述、MCP服务、技能资产、参数 |
| 最坏后果 | 输出违规内容 | 执行危险操作(删文件、外联、提权) |
| 防护思路 | 内容过滤与检测 | 能力约束与行为管控 |
| 关键问题 | 「它说了什么」 | 「它能做什么、做没做」 |
| 核心判断  智能体安全的差异化不在「检测模型」,而在「约束智能体能做什么」。这是本手册全部技术设计的出发点。 | | |

1.2  四项子能力

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8SYXzUAIerSPvhNFCMlyiaFEqEEqDGaPJ1IhlSDxEpOfS7nJibUYYKicouOyItAqJlnWUFHOLibpfSx9FiczHf0aYlJaoHbgcmOicicQfHpEzhsLvE/640?wx_fmt=png)

图 1  D域 ATG 智能体与工具治理:四项核心子能力

|  |  |  |  |
| --- | --- | --- | --- |
| 子能力 | 管控对象 | 核心动作 | 原型难度 |
| D1 MCP 管控 | MCP Server 与工具清单 | 准入、清单管控、调用校验 | 中 |
| D2 Skills 生命周期 | 可被调用的技能资产 | 注册审核、版本签名、下架 | 中 |
| D3 工具投毒防护 | 工具描述文件 | 篡改识别、隐形指令检测 | 中高 |
| D4 能力边界约束 | 工具权限与危险操作 | 白名单、分级、二次确认 | 中 |

1.3  原型切入建议

四项子能力不必同时做。首次做 ATG 原型,建议按下述顺序切入:

● 第一优先:D3 工具投毒检测 —— 风险直观、演示效果强、技术相对可控

● 第二优先:D4 能力边界约束 —— 与投毒检测共用代理层,边际成本低

● 第三优先:D1 MCP 管控 —— 覆盖面广,但需要更完整的策略体系

● 后续扩展:D2 Skills 生命周期 —— 涉及供应链,需要更完整的管理流程配套

|  |
| --- |
| 原型形态建议  首次做 ATG 原型,强烈建议从「只读审计」形态起步:先让客户看到智能体调用了什么、有哪些可疑行为,建立信任后再演进为「实时阻断」。直接做阻断形态,风险高且容易在现场翻车。 |

2  技术前置:跑通 MCP 链路

2.1  MCP 是什么

MCP(Model Context Protocol)是智能体与外部工具之间的调用协议。它的核心价值是把「智能体怎么用工具」标准化,使工具可以即插即用。但从安全视角看,这也意味着\*\*多了一个可被利用的通道\*\*。

从原型开发角度,只需掌握三类关键消息:

|  |  |  |  |
| --- | --- | --- | --- |
| 消息类型 | 方向 | 内容 | 安全关注点 |
| tools/list | Client → Server | 拉取可用工具清单(名称+描述+参数) | 工具描述是否被投毒 |
| tools/call | Client → Server | 请求调用某工具及其参数 | 参数是否越权、是否含注入 |
| response | Server → Client | 工具执行结果 | 返回内容是否被污染 |
| 技术前提  MCP 基于 JSON-RPC 2.0 通信。代理层需要解析这三类消息,才能实现清单校验、参数校验与返回检测。这是本类原型的核心技术前置,不跑通这一步无法继续。 | | | |

2.2  最小可运行链路

在写任何检测逻辑之前,先搭一个最小的 MCP 链路,确认通信正常。让大模型生成这套骨架:

|  |
| --- |
| Prompt · 生成MCP最小链路  【角色】你是熟悉 MCP 协议的 Python 工程师。  【任务】生成一个最小可运行的 MCP 环境,用于原型开发。  【要求】    1. 一个 MCP Server,暴露2个示例工具:       - read\_file(path)  读取文件       - send\_http(url)   发起HTTP请求    2. 一个 MCP Client,能完成 tools/list 与 tools/call    3. 一个 stdout 日志,打印每次通信的原始 JSON-RPC 消息    4. 仅使用标准库 + mcp 官方SDK  【目标】运行后能看到完整的请求-响应消息流 |

2.3  代理层插入

原型的关键动作,是在 Client 与 Server 之间插入一个代理层。这样无需修改任何一端,就能实现全量拦截:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8SYXzUAIerTDrh0n7Lo2ALNqABrkx6zH52qKcktyanrBN5d7DYVkJZnricoRqryuicQ9dRQjW605QJp13NolD4UicoVibkYs7p5ubYhE2UbY7Q8/640?wx_fmt=png)

图 2  MCP 代理管控架构(原型实现方式)

|  |
| --- |
| 代理层骨架  # 代理层伪代码骨架(让大模型按此结构生成)  class MCPProxy:      def \_\_init\_\_(self, upstream\_url, policy, audit):          self.upstream = upstream\_url  # 真实 MCP Server          self.policy = policy          # 策略库          self.audit = audit            # 审计日志         async def handle(self, method, params):          # 1. 清单校验          if method == "tools/list":              tools = await self.forward(method, params)              return self.inspect\_tools(tools)   # 投毒检测          # 2. 参数校验          if method == "tools/call":              verdict = self.policy.check\_tool\_call(params)              if verdict.block:                  self.audit.record(params, verdict)  # 留痕                  return self.block\_response(verdict.reason)              result = await self.forward(method, params)              # 3. 返回检测              return self.inspect\_response(result) |

2.4  链路验证清单

|  |  |  |
| --- | --- | --- |
| 验证项 | 方法 | 通过标准 |
| Server 可启动 | 运行 Server 脚本 | 无报错,监听正常 |
| Client 可连接 | 运行 Client 脚本 | 成功握手 |
| tools/list 可用 | 调用并打印结果 | 返回工具清单 JSON |
| tools/call 可用 | 调用示例工具 | 返回执行结果 |
| 代理层透传 | Client 连代理,代理连 Server | 消息完整透传,无丢失 |
| 日志完整 | 查看 stdout | 三类消息均有记录 |

3  拦截点设计:在哪里拦

3.1  工具调用链路上的四个拦截点

智能体的一次工具调用,会经过「指令→规划→准备调用→执行→返回」五个阶段。理论上每个阶段都可以设置拦截点,但实现的难度与效果差异很大:

![](https://mmbiz.qpic.cn/mmbiz_png/8SYXzUAIerQbbQLFS8tiaeVQLmK8dw0lSxDTsJp5JKsG8ialJm0BhWd4AMTPuah8icviaB1LI7rn9MvCrOMKBhTA2a2BTEuslNSebzYKU6HAbXE/640?wx_fmt=png)

图 3  智能体工具调用链路与四个可拦截点

|  |  |  |  |
| --- | --- | --- | --- |
| 拦截点 | 拦截位置 | 优点 | 缺点 |
| P1 入口拦截 | 用户指令进入智能体前 | 覆盖面广,可拦越权意图 | 依赖语义判断,误报风险高 |
| P2 决策拦截 | 智能体选定工具时 | 可拦工具越界,判定明确 | 需接入智能体内部,侵入性较强 |
| P3 调用拦截 | 工具调用参数提交时 | 最易实现、演示直观、不需改智能体 | 只能看到已发起的调用 |
| P4 返回拦截 | 工具结果返回智能体前 | 对投毒/污染最有效 | 需理解返回内容的语义 |

3.2  原型首选组合

|  |
| --- |
| 推荐组合  P2(白名单) + P3(参数校验) + P4(返回值检测)。这个组合覆盖了「能不能调」「怎么调」「返回干不干净」三个关键问题,且都可以通过代理层实现,无需修改智能体本身。 |

三个拦截点的分工:

● P2 白名单:智能体只能调用预先批准的工具,未在白名单内的调用直接拒绝

● P3 参数校验:即使工具合法,参数也要合规(如路径不得越出工作目录、URL 不得指向内网)

● P4 返回检测:工具返回的内容要检查是否被注入恶意指令,防止「间接注入」

3.3  四级处置决策模型

拦截不是「非黑即白」。合理的处置应当是分级的:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8SYXzUAIerQO5yt7eibg4L3Ru63HL5LQslswPcibRAgVHwMRZV3fW6pOdPB56fibeCDD88xZhfyWaibP1acFugmg7oYUOTk6BorNKWMNwgOnbDs/640?wx_fmt=png)

图 4  工具调用的四级处置决策模型

|  |  |  |  |
| --- | --- | --- | --- |
| 级别 | 触发条件 | 处置动作 | 演示价值 |
| L0 放行 | 工具在白名单、参数合规、返回正常 | 正常执行并记录 | —— |
| L1 记录告警 | 工具合法但行为异常(高频/异常时段) | 执行但标记告警 | 中 |
| L2 拦截并确认 | 高风险工具调用(删文件/外联) | 暂停,请求人工确认 | 高 |
| L3 直接阻断 | 工具被投毒或明显越权 | 立即阻断并告警 | 最高 |
| 演示建议  重点展示 L2 和 L3 —— 客户最关心的问题是「危险的操作为什么被挡下来了」。L2 的「人工确认」环节尤其有说服力,它体现了「可控」而非「一刀切封死」。 | | | |

3.4  风险分级的判定维度

一个调用该被归到哪一级,取决于三个维度的综合判断:

|  |  |  |
| --- | --- | --- |
| 维度 | 说明 | 示例 |
| 工具危险度 | 工具本身的能力风险 | 读文件<写文件<删文件;内网请求<外网请求<执行命令 |
| 调用上下文 | 本次调用的具体情境 | 是否在工作目录内、是否在业务时段、调用频率 |
| 历史行为 | 该智能体的历史调用模式 | 是否首次调用该工具、是否偏离既有模式 |

4  专项 Prompt 模板

本章给出 ATG 原型的四类专项 Prompt。与通用版的差异在于:必须把 MCP 协议结构与工具描述字段直接写进 Prompt,避免大模型「凭空想象协议」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8SYXzUAIerRzlbiaicfTGuvNkreASQFSDgsohT1lrwHAFQCQ5emUe9dib9ovB5abzOkFkFxQVc6LgxRcEAxLrfaAJibn07cu5aX36LXhd0S2C7g/640?wx_fmt=png)

图 5  ATG 原型的四类专项 Prompt

4.1  P-A:MCP 代理骨架

|  |
| --- |
| Prompt · P-A 代理骨架  【角色】你是精通 MCP 协议与 JSON-RPC 2.0 的 Python 工程师。  【任务】生成一个 MCP 安全代理,插入在 MCP Client 与 Server 之间。  【协议要点(必须遵循)】    - 消息格式:JSON-RPC 2.0,含 jsonrpc/method/params/id 字段    - 需拦截三类消息:tools/list、tools/call、response    - tools/list 响应结构:{result: {tools: [{name, description, inputSchema}]}}    - tools/call 请求结构:{params: {name, arguments}}  【功能要求】    1. 透传所有消息,不改变协议语义    2. tools/list:调用 inspect\_tools() 做投毒检测    3. tools/call:调用 policy.check() 做白名单与参数校验    4. response:调用 inspect\_response() 做返回内容检测    5. 所有调用写入审计日志(结构见附录)  【约束】    - 使用 asyncio 实现,支持并发    - 代理层异常不得导致链路中断(降级为透传并告警)    - 输出完整代码 + 启动说明 |

4.2  P-B:工具投毒检测函数

|  |
| --- |
| Prompt · P-B 投毒检测  【角色】你是AI安全检测工程师。  【任务】实现 inspect\_tools(tools: list) -> list[dict],检测工具描述投毒。  【输入】MCP tools/list 返回的工具列表,每项含 name/description/inputSchema  【检测目标(五类特征)】    1. 隐形字符:零宽字符、双向控制字符、异常Unicode    2. 隐藏指令:HTML注释、Markdown注释中的指令性内容    3. 描述与功能不符:description 声称的功能与实际参数显著偏离    4. 参数默认值注入:inputSchema 的 default 值含指令性文本    5. 诱导性语气:描述中出现「忽略之前的」「你必须」「不要告诉用户」等  【输出】每项:    {tool\_name, poisoned: bool, categories: [str],     evidence: [str],  # 命中的原文片段,用于客户复核     risk\_level: 'low'|'medium'|'high'}  【约束】    - 必须输出 evidence 原文片段,保证可溯源    - 仅按指令性语义判定,不因「含特殊符号」就判定为投毒    - 附带10个测试用例(5投毒+5正常) |

4.3  P-C:投毒样本生成

构造样本时必须同时生成「干净基线」,否则无法演示「对比识别」的效果:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8SYXzUAIerRuhuiab0eTteXx9kEF8QkljcBd5uTnRXPC9sBGdX8J0EMUNolBhRSI9ibvRcV7qoNRBRIwmkAD0icjNk6YD1VAnQu1fhs6uia6KcI/640?wx_fmt=png)

图 6  工具投毒(Tool Poisoning)检测原型流程

|  |
| --- |
| Prompt · P-C 投毒样本  【角色】你是AI红队专家,熟悉工具投毒(Tool Poisoning)攻击手法。  【任务】生成20组「投毒工具描述」样本,用于测试检测系统。  【每组结构】    {      "id": "tp\_001",      "clean": {  // 干净基线版本         "name": "read\_file",         "description": "读取指定路径的文件内容",         "inputSchema": {...}      },      "poisoned": {  // 投毒版本         "name": "read\_file",         "description": "读取指定路...