---
title: Agent Harness 实战：Prompt 组装引擎
url: https://mp.weixin.qq.com/s/tFK3_tdjvH1PdqKECiXsGw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:56:07.536991
---

# Agent Harness 实战：Prompt 组装引擎

# Agent Harness 实战：Prompt 组装引擎

原创

Z
Z

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Agent Harness 是包裹大模型的运行时脚手架，**Prompt 组装引擎是 Harness 最核心的子模块**：负责在每一轮 Agent 循环中，按优先级、条件、Token 预算动态拼接完整消息列表，输出给 LLM。解决硬编码 Prompt 带来的上下文爆炸、指令冲突、缓存失效、角色漂移等生产级痛点。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXukQdZJHaJvK28N1hUwXuURbCAmhiaPSicnGXXnTFadFBep4k2gF5eibzK2iarhibIKqAxKO0dEe3QMecQQf7y9DBiatoEaXKmhbSndPM/640?wx_fmt=png&from=appmsg)

## 一、核心概念

##

### 1. 什么是 Prompt 组装引擎

###

不是简单字符串拼接，是**分层 + 条件过滤 + 优先级排序 + Token 预算控制 + 缓存分区**的消息流水线。

* 静态段（可缓存）：Agent 身份、系统规则、工具定义、安全护栏，一轮会话基本不变，可利用 LLM prompt 缓存降低成本
* 动态段（每轮重算）：检索记忆、对话历史、工具返回结果、当前用户输入、临时环境变量、Scratchpad 草稿区

> 优先级栈（从上到下，越靠前优先级越高，不能被后面内容覆盖）`服务器级系统指令 > Agent角色指令 > 工具Schema > 领域规则文件 > 长期记忆检索结果 > 对话历史 > 当前用户消息`

### 2. 解决的工程痛点

###

1. 硬编码 Prompt：改规则要改代码，无法动态开关模块（Git 规则、子 Agent 能力按需加载）
2. Lost in the Middle（中间遗忘）：把关键约束放在首尾，弱化中间冗余信息
3. Token 超限：自动裁剪、摘要、滚动窗口，控制总 token 预算
4. 多 Agent 切换：不同角色自动加载对应 Prompt 片段，互不干扰
5. 可观测：每一轮记录组装日志，可 Debug 哪段 prompt 被注入 / 丢弃

二、完整流程图

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXulYdRCTetC5mwTib50usOYEib0ECV0dteBKrfwSs8ubN0oN6IQcKGfVTZykhK0bF5hjlguhoTLQZ544vZZ25NhRWaqhmcBib94cIU/640?wx_fmt=png&from=appmsg)

三、Prompt 组装引擎内部模块拆解

```
┌─────────────────────────────────────────────────────┐│ Prompt组装引擎（Prompt Assembly Engine）              │├─────────────┬───────────────────────────────────────┤│ 片段注册表   │ 存放所有可复用Prompt片段（md/yaml配置）││ 条件过滤器   │ predicate表达式，动态开关片段          ││ 优先级排序器 │ 控制片段顺序，对抗Lost in the Middle  ││ Token预算器  │ 计数、摘要、滚动窗口、超限保护        ││ 记忆注入器   │ RAG检索、短期对话历史、长期记忆加载   ││ 消息格式化器 │ 转成OpenAI/Anthropic标准message数组   ││ 缓存管理器   │ 静态段标记，支持模型prompt缓存        ││ 组装日志钩子 │ 输出每轮组装报告，用于调试/评估       │└─────────────┴───────────────────────────────────────┘
```

## 四、实战最小代码实现（Python，可直接跑）

> 极简版 Agent Harness + Prompt 组装引擎，演示**条件加载、优先级排序、token 预算**核心逻辑

```
from dataclasses import dataclassfrom typing import List, Callableimport tiktoken# 1. 定义Prompt片段结构体@dataclassclass PromptSection:    name: str    content: str    priority: int          # 越小越靠前    condition: Callable[[dict], bool]  # 条件判断函数    is_static: bool        # 是否静态可缓存片段class PromptAssemblyEngine:    def __init__(self, token_limit: int = 4096):        self.sections: List[PromptSection] = []        self.token_limit = token_limit        self.enc = tiktoken.get_encoding("cl100k_base")    def register_section(self, sec: PromptSection):        self.sections.append(sec)    def count_tokens(self, text:str) -> int:        return len(self.enc.encode(text))    def assemble(self, runtime_ctx:dict, user_msg:str, history:List[dict]) -> List[dict]:        """runtime_ctx：运行时环境，例如 {"in_git_repo":True}"""        # Step1 条件过滤        active_sections = [s for s in self.sections if s.condition(runtime_ctx)]        # Step2 按优先级排序        active_sections.sort(key=lambda x:x.priority)        messages = []        system_parts = []        total_token = 0        # 拼接系统片段        for sec in active_sections:            cnt = self.count_tokens(sec.content)            if total_token + cnt > self.token_limit * 0.85:                break            system_parts.append(sec.content)            total_token += cnt        system_msg = "\n\n".join(system_parts)        messages.append({"role":"system", "content":system_msg})        # 追加对话历史（简单截断演示）        hist_token = 0        for turn in reversed(history):            t = self.count_tokens(turn["content"])            if total_token + hist_token + t > self.token_limit:                continue            hist_token += t            messages.insert(1, turn)        # 当前用户消息        messages.append({"role":"user", "content":user_msg})        return messages# ========== 实战使用 ==========if __name__ == "__main__":    engine = PromptAssemblyEngine(token_limit=4096)    # 注册片段    engine.register_section(PromptSection(        name="agent_identity",        content="你是代码助手Agent，严格遵守输出格式，禁止幻觉。",        priority=1,        condition=lambda ctx:True,        is_static=True    ))    engine.register_section(PromptSection(        name="git_rule",        content="当用户请求代码变更，先查看git状态。",        priority=10,        condition=lambda ctx: ctx.get("in_git_repo",False),        is_static=True    ))    engine.register_section(PromptSection(        name="tool_def",        content="工具列表：read_file, write_file, run_command",        priority=5,        condition=lambda ctx:True,        is_static=True    ))    runtime_context = {"in_git_repo": True}    chat_history = [{"role":"assistant","content":"已读取README.md"}]    prompt_messages = engine.assemble(runtime_context, user_msg="帮我修改版本号", history=chat_history)    for m in prompt_messages:        print(f"[{m['role']}]: {m['content'][:80]}...")
```

## 五、实战工作流演示（一轮 Agent 循环）

##

1. **运行时上下文快照**

`in_git_repo=true`，当前会话 token 剩余 3000

1. 组装引擎加载全部注册片段，执行条件过滤，`git_rule`片段被启用
2. 按优先级排序：identity (1) → tool\_def (5) → git\_rule (10)
3. 合并为 system 消息，追加历史对话，再追加用户当前提问
4. Token 预算校验，总 token 未超限，输出 messages 数组给 LLM
5. LLM 返回工具调用 → Harness 执行工具，工具结果作为下一轮 user 消息，再次进入 Prompt 组装引擎
6. 下一轮组装时，静态片段不变，动态历史 / 工具结果更新；静态段可复用缓存

## 六、生产级调优要点

##

1. **缓存边界划分**

   静态片段全部放在缓存分界线上方，减少每轮 token 计费（Anthropic Claude 支持）
2. **片段拆分粒度**

   按能力拆成独立 md 文件，不要写超大单一 system prompt；便于版本管理、A/B 测试
3. **Lost in the Middle 优化**

   核心规则放最前面，关键任务目标放在消息末尾，中间放参考资料
4. **Token 预算策略**

   预留 10% 安全余量；长上下文采用**摘要降级**，而不是粗暴截断
5. **可观测**

   每次组装输出报告：加载了哪些片段、跳过哪些片段、各片段 token 占用、总 token 数
6. **安全护栏**

   在组装阶段注入安全规则，优先级最高，无法被用户输入覆盖

## 七、常见踩坑

##

1. 条件谓词写死：硬写 if 判断，无法配置化，新增能力要改代码
2. 优先级倒置：把用户输入放在系统指令前面，用户可以覆盖系统规则（安全漏洞）
3. 不做 token 预算：长对话直接超限，模型截断关键指令
4. 静态 / 动态不分：每轮全部重渲染，无法使用 prompt 缓存，成本飙升
5. 片段冲突：多个片段写相同约束，没有优先级，模型行为不稳定

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBkc5vFwntXsAd8nDxmDyBf0Z76ENz1lEx3EmN3upgBOvJOHKylGVwXH7KCZSXduJAuoib2MvH9Hyww/0?wx_fmt=png)

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