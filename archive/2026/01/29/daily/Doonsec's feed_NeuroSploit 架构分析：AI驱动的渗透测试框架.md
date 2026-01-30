---
title: NeuroSploit 架构分析：AI驱动的渗透测试框架
url: https://mp.weixin.qq.com/s/RIemvieVgKLhMl2JU1oS7A
source: Doonsec's feed
date: 2026-01-29
fetch_date: 2026-01-30T04:01:59.488997
---

# NeuroSploit 架构分析：AI驱动的渗透测试框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vRBYx9F4Zf6mzPibrlVdTbGJZy1icILRUlbXbzY6q5QIAyRBvOUa6zjVSDDiaE5kn7NTiaokaC72wF5bybibiacyicxnw/0?wx_fmt=jpeg)

# NeuroSploit 架构分析：AI驱动的渗透测试框架

原创

丘迟
丘迟

极客零零七

![]()

在小说阅读器中沉浸阅读

**NeuroSploit**是一个**AI 驱动的自适应渗透测试框架，**旨在通过大语言模型（LLM）的智能决策能力，实现类似专业渗透测试人员的自主安全评估。它利用大型语言模型（LLMs）进行动态和上下文感知的漏洞分析。上一篇[NeuroSploitv2: 一款AI驱动的渗透测试工具（试用版）](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247486029&idx=1&sn=a6cf7cb00e1cfa23983da3acb46d9959&scene=21#wechat_redirect)中我们对该工具进行了简单的测试，本文我们从项目出发了解AI如何在渗透测试中发挥作用。

整体架构

![](https://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6mzPibrlVdTbGJZy1icILRUlO9oL3iaKbe6zgW3icn2SmLJVP0LAcQiaPYnX2wJibz01uanQLdh4jB0uog/640?wx_fmt=png&from=appmsg)![]()

该框架的核心特色是其现代化的Web界面（使用React构建）和由FastAPI驱动的强大后端，两者通过容器化技术（Docker）实现了一致的、可轻松部署的运行环境。核心特性：

* **AI自主决策**：不依赖预设规则，由LLM动态分析和适应
* **适应性测试**：根据发现结果自动调整测试策略
* **多工具集成**：支持Nmap、Sqlmap、Burp等传统安全工具
* **上下文感知**：预收集的侦察数据指导AI决策
* **模块化设计**：易于扩展不同的测试代理和工具

---

核心模块

1. LLMManager-统一的大模型管理器

**文件**: `core/llm_manager.py`，主要功能：

* 支持多个LLM供应商的透明切换
* 加载和管理提示词库
* 实现幻觉检测和防护栏
* 提供统一的`generate()`接口

关键组件

![](https://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6mzPibrlVdTbGJZy1icILRUlEKt51qnej8R7r6V16WsWrkiaglj7Xr4OQfZYYNI7mszAicgjPowkCYTw/640?wx_fmt=png&from=appmsg)

![]()

核心方法：

| 方法 | 功能 | 使用场景 |
| --- | --- | --- |
| `generate()` | 调用LLM生成响应 | 所有AI决策步骤 |
| `_load_all_prompts()` | 从JSON和MD加载提示词 | 初始化时加载 |
| `_mitigate_hallucination()` | 检测和修正幻觉 | 关键分析时 |
| `_apply_guardrails()` | 应用安全防护栏 | 生成敏感内容前 |

提示词管理系统：提示词存储在两个位置，包含多个内置的提示词，如blue\_team\_agen、pentest、red\_team\_agent、owasp\_expert等。

![](https://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6mzPibrlVdTbGJZy1icILRUl2mibv1mmqEROwEbm0XH0tVkSiagvjYtGFneFUNF1Y1PCKRLXVupYlt4Q/640?wx_fmt=png&from=appmsg)![]()

渗透测试Markdown提示词：

```
# Penetration Test Prompt## User PromptAs a Penetration Tester, perform a comprehensive security assessment based on the provided scope and initial information. Identify vulnerabilities, assess risks, and provide actionable recommendations.**Scope of Work:**{scope_json}**Initial Information:**{initial_info_json}**Instructions:**1.  Outline a detailed penetration testing plan (reconnaissance, scanning, enumeration, exploitation, post-exploitation).2.  Identify potential attack vectors.3.  Suggest tools and techniques for each phase.4.  Provide a risk assessment for identified vulnerabilities.5.  Formulate remediation strategies.## System PromptYou are a highly skilled and ethical Penetration Tester. Your goal is to systematically identify security weaknesses, assess their exploitability, and provide clear, practical advice to improve the security posture of the target system. Adhere strictly to the defined scope and ethical guidelines.
```

2. **BaseAgent** - 自主安全测试代理

**文件**: `agents/base_agent.py，`核心设计理念是模拟真实渗透测试人员的工作流程：

* 发现攻击面（动态发现）
* 智能分析响应（用LLM）
* 自适应测试策略（根据发现调整）
* 重点深入（发现有趣的发现时）
* 生成文档化的PoC

**执行模式 A：直接模式（无预收集数据）**

```
用户输入 → 提取目标 → 发现阶段 → AI分析 → 工具执行 → 最终报告
```

**执行模式 B：自适应模式**（使用预收集的侦察数据）

```
用户输入 → 加载侦察上下文↓[PHASE 1] 分析上下文充分性↓[PHASE 2] 如需要则运行工具填补空白↓[PHASE 3] AI最终分析↓生成报告
```

**关键AI调用点1:  上下文充分性分析**

![](https://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6mzPibrlVdTbGJZy1icILRUlbbSGJCGclXCxjXucgHKcUFDMdxvvCibUpI7kVAMeqSQK3YjqwCsMCZw/640?wx_fmt=png&from=appmsg)![]()

**AI决策点**：判断是否需要运行额外工具、识别缺失的关键数据、推荐特定的测试类型（XSS、SQLi、SSRF等）

**关键AI调用点2: 测试生成**

```
def _ai_analyze_context(self, target: str, context: Dict, user_input: str) -> str:    """AI analyzes the recon context and creates targeted attack plan."""    # 1. 提取侦察上下文数据    urls_with_params = data.get('urls', {}).get('with_params', [])[:30]    technologies = data.get('technologies', [])    api_endpoints = data.get('api_endpoints', [])[:20]    # 2. 构建提示词，指示 AI 生成测试    analysis_prompt = f"""You are an elite penetration tester...    [TEST] curl -s -k "[URL_WITH_PAYLOAD]"    """    # 3. 调用 LLM 生成测试命令    response = self.llm_manager.generate(analysis_prompt, system)    # 4. 解析响应并执行测试    tests = re.findall(r'\[TEST\]\s*(.+?)(?=\[TEST\]|\Z)', response, re.DOTALL)    for test in tests[:30]:        if test.startswith('curl'):            self.run_command("curl", args)
```

AI决策点：选择哪些URL进行测试、为特定应用设计有效载荷、确定测试优先级。

**关键AI调用点3: 利用策略规划**

```
def _context_based_exploitation(self, target: str, context: Dict, attack_plan: str):    """AI-driven exploitation using context data."""    for iteration in range(8):        print(f"\n  [*] AI Exploitation Iteration {iteration + 1}")        recent_results = self.tool_history[-15:]
        # AI 分析最近的测试结果        exploitation_prompt = f"""You are actively exploiting {target}.
        [RECENT TEST RESULTS]        {results_context}
        Look at the results. Identify:        1. SQL errors = SQLi CONFIRMED        2. XSS reflection = XSS CONFIRMED        3. File contents = LFI CONFIRMED
        Output your next tests as:        [EXEC] curl: [arguments]        """
        response = self.llm_manager.generate(exploitation_prompt, system)
        if "[DONE]" in response:            break
        commands = self._parse_ai_commands(response)
        for tool, args in commands[:10]:            result = self.run_command(tool, args, timeout=60)            self._check_vuln_indicators(result)
```

**AI决策点**：制定后续利用策略、生成具体的命令序列、评估风险和影响

**关键AI调用点4: 最终分析和报告生成**

```
def _final_analysis(self, user_input: str, context_text: str, target: str) -> str:    """AI生成专业的渗透测试报告"""    report_prompt = f"""    从这些真实的扫描结果生成专业的渗透测试报告:
    用户请求: {user_input}    目标: {target}    扫描结果: {context_text}
    报告应包含:    1. 执行摘要    2. 发现的漏洞（按严重性）    3. 业务影响    4. 修复建议    5. PoC代码    """
    return self.llm_manager.generate(report_prompt, system_prompt)
```

**AI决策点**：解释漏洞的业务影响、提供修复建议、撰写专业报告

3. **PromptParser**-提示词解析器

**文件**: backend/core/prompt\_engine/parser.py。

关键特性：不使用LLM，而是用正则表达式和关键字匹配。从用户的自然语言提示中提取结构化的测试指令。

![](https://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6mzPibrlVdTbGJZy1icILRUlCNnAiafRWKFwDSL3JZ7NFZLAAu7fD98qEQLQ03sxTkHvAaKrdtoibFFA/640?wx_fmt=png&from=appmsg)![]()

支持的漏洞类型（180+关键字）

| 类别 | 类型 | 关键字示例 |
| --- | --- | --- |
| 注入 | XSS (3种) | "xss", "cross-site scripting", "script injection" |
| 注入 | SQLi (4种) | "sql injection", "union-based", "blind sql" |
| 注入 | 命令注入 | "rce", "command injection", "remote code execution" |
| 文件访问 | LFI | "local file inclusion", "path traversal", "../" |
| 文件访问 | XXE | "xml external entity", "xml injection" |
| 请求伪造 | SSRF | "server-side request forgery", "metadata service" |
| 认证 | 认证绕过 | "authentication bypass", "login bypass" |
| API安全 | 速率限制 | "rate limit", "throttling" |

输入示例：

```
"Test the target for XSS and SQLi vulnerabilities.  Focus on the login and search parameters.  Only run quick tests, don't do thorough scanning.  Show critical findings only."
```

**输出示例**:

```
{  "vulnerabilities_to_test": [    {"type": "xss_reflected", "category": "injection", "confidence": 0.9},    {"type": "xss_stored", "category": "injection", "confidence": 0.9},    {"type": "sqli_error", "category": "injection", "confidence": 0.9}  ],  "testing_scope": {    "depth": "quick",    "include_recon": true,    "time_limit_minutes": null,    "max_requests_per_endpoint": null  },  "special_instructions": [    "Focus on the login parameter",    "Focus on the search parameter"  ],  "target_filters": {    "focus_on_parameters": ["login", "search"]  },  "output_preferences": {    "severity_threshold": "critical",    "include_poc": true,    "include_remediation": true  }}
```

AI/LLM 集成方案

1）多层次的AI决策系统

项目中 AI 并不是简单的"提示 → 响应"，而是在多个决策点深度集成：

**第1层：发现策略决策, 用户请求→AI分析→决定是否需要工具→选择运行哪些工具。LLM调用**`_analyze_context_gaps()`

**第2层：测试生成决策。已发现的端点和参数→AI生成测试→创建有效载荷→执行测试。LLM调用**`_generate_ai_tests()`

**第3层：利用规划决策。发现漏洞→AI规划利用→生成命令→执行深度测试。**LLM调用`_plan_exploitation()`

**第4层：报告生成决策。所有扫描结果→AI分析→生成专业报告→提供修复建议。LLM调用：**`_final_analysis()` 和 `_generate_final_report()`

2）LLM 提示词工程

系统提示词 (System Prompt) 的作用：为 LLM 定义角色和行为准则。示例系统提示词（来自 md\_library）：

```
## System Prompt你是一位资深渗透测试专家，具有15年的安全测试经验。你的职责是：1. 分析安全扫描结果2. 识别真实漏洞和误报3. 评估业务影响4. 提供实用的修复建议在分析时始终：- 考虑实际攻击可能性- 提供可复现的PoC- 提醒管理员优...