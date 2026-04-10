---
title: 用 AI Agent 自动化 JavaScript 加密逆向分析
url: https://mp.weixin.qq.com/s/ESavpqR8av08_t2qtVrbAA
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:41:40.239632
---

# 用 AI Agent 自动化 JavaScript 加密逆向分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/unnlWdxxboMM8c32759TdGKxbubzCwTs34cmpayhT6zTsad7hj2Oq3icS4F4oWYzlCoEKmnAqYuxicxiav92qliae1kCY3NMaqzpvWOKcrm37Vc/0?wx_fmt=jpeg)

# 用 AI Agent 自动化 JavaScript 加密逆向分析

原创

牧之
牧之

从黑客到保安

![]()

在小说阅读器中沉浸阅读

# 一种基于 Claude Code Agent + 双工具架构的 JS 加密参数逆向方法论

# 背景

前端加密逆向是安全研究中的常见需求：分析网页 JavaScript 中的加密逻辑，理解加密参数的生成流程，并用 Python 等语言复现。

传统做法是人工在 Chrome DevTools 中设断点、单步跟踪、记录变量值，再手动编写还原代码。这个过程繁琐、容易遗漏，且面对混淆代码和 JSVMP 保护时效率极低。

核心思路：将这个过程封装为一个 Claude Code Agent，让 AI 自主完成「代码收集 → 关键词定位 → 断点调试 → 算法识别 → Python 复现 → 交叉验证」的完整链路。

# 架构设计

# 为什么需要双工具？

JS 逆向分析需要两类截然不同的操作：

|
|  |

|
|  |

| 操作类型 | 特点 | 举例 |
| --- | --- | --- |
| **静态分析** | 一次性、无状态 | 搜索关键词、收集代码、AI 反混淆、加密算法检测 |
| **运行时调试** | 多步、有状态 | 设断点 → 触发 → 查看调用栈 → 单步进入 → 求值变量 |

关键发现：CLI 工具无法支持多步调试。

CLI 工具（如通过 node skill.js 调用）的生命周期是：启动进程 → 连接浏览器 → 执行命令 → 断开连接 → 退出进程。每次命令都是独立进程，无法在「设断点」和「查看断点命中后的变量」之间保持 CDP 连接。

```
CLI 架构（单次进程）:  命令1: connect → set_breakpoint → disconnect → exit  命令2: connect → ??? 断点状态已丢失
MCP 架构（持久进程）:  tool1: set_breakpoint     ← CDP 连接保持  tool2: (等待断点命中)      ← 同一连接  tool3: get_paused_info    ← 断点状态仍在  tool4: evaluate_on_callframe ← 可访问暂停时的作用域
```

# 双工具架构

最终方案是两套工具互补：

```
┌─────────────────────────────────────────────────┐│                  Claude Code Agent               ││                  (js-reverser.md)                ││                                                  ││  ┌──────────────────┐  ┌──────────────────────┐ ││  │  工具集 A: CLI    │  │  工具集 B: MCP Server │ ││  │  (Skill 命令)     │  │  (持久 CDP 连接)      │ ││  │                  │  │                      │ ││  │  - 浏览器启动     │  │  - 断点管理           │ ││  │  - 反检测注入     │  │  - 执行控制 (单步)     │ ││  │  - 代码收集       │  │  - 调用帧求值         │ ││  │  - 关键词搜索     │  │  - Hook 函数          │ ││  │  - AI 反混淆      │  │  - 变量查看           │ ││  │  - AI 语义理解    │  │  - 网络请求监控        │ ││  │  - 加密算法检测   │  │  - XHR 断点           │ ││  │  - 页面控制       │  │  - 对象属性展开        │ ││  │  - DOM 检查       │  │  - Storage 读取        │ ││  └──────────────────┘  └──────────────────────┘ ││                                                  ││  选择规则:                                        ││  - 需要跨步骤保持状态 → MCP                        ││  - 一次性操作 → CLI                               │└─────────────────────────────────────────────────┘
```

# 7 阶段逆向方法论

# Phase 1: 环境准备与代码收集 [CLI]

启动浏览器，注入反检测脚本，导航到目标页面，按优先级收集 JS 代码。

```
browser launchstealth inject-preset mac-chromepage navigate <target_url>collect <url> --smart-mode=priority --priorities=encrypt,sign,token
```

要点：使用 --smart-mode=priority 按关键词优先级收集，避免收集全量代码导致 Token 溢出。

# Phase 2: 快速侦查 [CLI + MCP]

用关键词搜索缩小范围，定位加密相关的代码区域。

```
# CLI: 关键词搜索search "encrypt"search "AES"search "<目标参数名>"search "<API路径片段>"
# CLI: AI 快速检测detect-crypto <可疑代码片段>summarize collected
# MCP: 跨脚本搜索search_in_sources("CryptoJS")
```

产出：目标 JS 文件的 URL/scriptId，加密代码的大致行号范围。

# Phase 3: 加密入口定位 [MCP]

这是双工具架构的核心价值所在 —— 通过 XHR 断点精确定位加密函数入口。

策略 A — XHR 断点法（推荐）：

```
MCP: break_on_xhr("*/api/target*")       ← 设 XHR 断点MCP: navigate_page("https://target.com") ← 触发请求     ... 等待断点命中 ...MCP: get_paused_info()                   ← 查看调用栈MCP: evaluate_on_callframe(expr, frameId) ← 在断点上下文求值
```

调用栈会展示从 XMLHttpRequest.send() 到加密函数的完整调用链。从底往上找到第一个处理数据变换的帧，就是加密入口。

策略 B — Hook 法：

```
MCP: hook_function("CryptoJS.AES.encrypt")MCP: hook_function("JSON.stringify")     ... 触发请求 ...MCP: list_hooks()    ← 查看捕获的调用参数和返回值
```

策略 C — 代码文本断点：

```
MCP: set_breakpoint_on_text(".encrypt(")  ← 按代码内容自动定位行号
```

# Phase 4: 加密链路追踪 [MCP]

从加密入口开始，单步跟踪每一步数据变换。

```
MCP: set_breakpoint(scriptUrl, lineNumber)     ... 断点命中 ...MCP: get_paused_info()          ← 调用栈 + 当前作用域MCP: evaluate_on_callframe(     ← 检查变量值       "JSON.stringify(inputData)"     )MCP: step_into()                ← 进入函数调用MCP: evaluate_on_callframe(     ← 查看函数内部状态       "key.toString()"     )MCP: step_over()                ← 跳过当前行MCP: evaluate_on_callframe(     ← 检查输出       "result.toString()"     )
```

记录清单（每步必须记录）：

| 记录项 | 示例 |
| --- | --- |
| 输入数据 | `{"userId": "123", ...}` |
| 算法 | AES-128 / MD5 / zlib / Custom Base64 |
| 密钥及来源 | `"abc123..."` — JSVMP 动态生成 |
| 模式/填充 | ECB + PKCS7 |
| 输出数据 | `"U2FsdGVkX1..."` |

# Phase 5: 算法识别与参数提取 [CLI + MCP]

CLI 负责 AI 分析：

```
detect-crypto <加密代码片段>     ← 自动识别算法类型deobfuscate <混淆代码>          ← AI 反混淆understand <代码> --focus=security ← AI 语义理解
```

MCP 负责运行时验证：

```
# 在加密调用处断点，验证实际参数evaluate_on_callframe("mode.toString()")        → "ECB"evaluate_on_callframe("key.toString()")          → 实际密钥值evaluate_on_callframe("padding.toString()")      → "Pkcs7"
```

原则：AI 分析结果仅作参考，关键参数必须通过断点求值验证。

# Phase 6: Python 还原代码生成

基于验证后的算法参数，生成可独立运行的 Python 代码。

```
# 代码结构模板"""目标: [参数名], 端点: [API路径]"""
# ============ 常量（注明来源和验证方式）============AES_KEY = "..."       # [运行时验证] 断点捕获CUSTOM_B64 = "..."    # [运行时验证] evaluate_script 确认
# ============ 子函数（按加密链路顺序）============def step1_serialize(data): ...def step2_compress(data): ...def step3_encrypt(data, key): ...def step4_encode(data): ...
# ============ 主入口 ============def encrypt(plaintext): ...
# ============ 自测试（用浏览器捕获的真实数据）============if __name__ == '__main__': ...
```

# Phase 7: 交叉验证 [CLI + MCP]

```
# 浏览器中执行 JS 加密MCP: evaluate_script("encrypt('test_input')")
# 本地执行 Python 加密$ python encryption.py
# 对比输出
```

# 逐步验证：不只验证最终结果，对每个子函数单独验证。差异常见原因：编码（UTF-8 vs Latin1）、填充方式、压缩参数、随机性。

# 核心策略

# 处理闭包变量

前端 JS 经过打包后，加密库通常在闭包内，全局作用域不可达：

```
// webpack 打包后(function(modules) {  var CryptoJS = modules['crypto-js'];  // 闭包内，window.CryptoJS 不存在  function encrypt(data) {    return CryptoJS.AES.encrypt(data, key);  }})([...]);
```

错误做法：evaluate\_script("window.CryptoJS") → undefined

正确做法：在 encrypt 函数内部设断点，断点命中后用 evaluate\_on\_callframe 直接读取闭包变量 CryptoJS。

# 处理 JSVMP（JS 虚拟机保护）

JSVMP 将关键逻辑编译为自定义字节码或 AST，在 JS VM 解释器中执行。

识别特征：

| 类型 | 特征 |
| --- | --- |
| 字节码解释器 | `e.b[u++]^c`、`switch(opcode)` 大循环 |
| AST 解释器 | `decodeURIComponent` + `JSON.parse` → AST 对象、eval5/sval |
| 通用信号 | 创建时缓存 `Date`/`Math`/`parseInt` 到局部变量 |

分析策略 — 黑盒优先：

```
不要试图理解 VM 内部的字节码/AST 执行逻辑        ↓在 VM 入口和出口设断点        ↓观察输入参数和返回值        ↓  返回值是 16 字符字符串？ → 可能是密钥生成  返回值是长串密文？ → 可能是主加密函数  返回值是 boolean？ → 可能是校验函数        ↓确认后，追踪返回值的使用位置（是否被当作 AES key）
```

# 处理反调试

常见反调试手段及应对：

| 反调试手段 | 应对方法 |
| --- | --- |
| `debugger` 语句 | Hook 或条件断点跳过 |
| 定时器检测（`setInterval` 检查执行时间差） | Hook `setInterval` / 覆盖检测函数 |
| JSVMP 内时间差检测 | 在 VM 内部设断点而非外部单步 |
| `console.log` 重写检测 | 在 Hook 前保存原始引用 |
| 栈深度检测 | 通过 CDP 直接操作，不增加栈帧 |

# 结论溯源标注

每项结论必须标注验证方式，让报告的可信度一目了然：

| 标注 | 含义 |
| --- | --- |
| `[运行时验证]` | 通过断点 + evaluate\_on\_callframe 在运行时确认 |
| `[静态分析]` | 通过代码阅读 / AI 分析确认，未经运行时验证 |
| `[未验证/推测]` | 无法通过工具验证，仅为推测 |

Agent 定义

Agent 以 Markdown 文件定义（如 .claude/agents/js-reverser.md），包含：

```
# JS 逆向工程 Agent
## 核心原则1. 双工具架构 — 明确哪些操作用 CLI、哪些用 MCP2. 运行时验证 — 禁止仅凭静态代码推断关键参数3. 结论溯源 — 每项结论标注数据来源
## 工具集 A — CLI (Skill 命令)[列出所有 CLI 命令及用途]
## 工具集 B — MCP Server[列出所有 MCP 工具及用途]
## 7 阶段方法论[Phase 1-7，标注每阶段使用哪套工具]
## 通用策略[闭包处理、JSVMP、动态密钥、反调试等]
```

# MCP Server 注册

在项目根目录 .mcp.json 中注册 MCP Server：

```
{  "mcpServers": {    "js-reverse": {      "command": "node",      "args": ["path/to/js-reverse-mcp/build/src/index.js"]    }  }}
```

MCP Server 在 Claude Code 会话期间保持运行，CDP 连接跨工具调用持久保持。

# 实战效果

由于版权问题，我就不具体公布分析的样本了，agent中关于jsvmp分析的流程我也删除了一些。后续等版本更新了，考虑开源出来。最终效果完成了某厂的设备指纹的加密分析，包含了其中的jsvmp逻辑。

# 局限性与改进方向

# 当前局限

1.JSVMP 内部断点困难 — 反调试时间差检测限制了在 VM 内部单步调试，部分参数只能通过 AST 解码获取而非运行时验证

2.随机性参数验证 — 涉及 Math.random() 的加密步骤（如 Custom Base64 偏移），每次结果不同，只能验证格式正确性

3.动态加载脚本 — 通过 eval() 或 new Function() 动态加载的代码可能在收集时遗漏

# 改进方向

1.CDP Fetch Domain 拦截 — 在网络层拦截并修改响应，注入反反调试代码

2.AST 级别自动化 — 对 JSVMP AST 进行自动化解码和分析，减少人工介入

3.差异化验证 — 对随机性步骤，执行 N 次加密并验证统计特征（长度分布、字符集等）

4.多 Agent 协作 — 静态分析 Agent 和动态调试 Agent 并行工作，结果合并

# 总结

这套方法论的核心思想是：

1.工具分层 — 静态分析用 CLI（轻量、快速），运行时调试用 MCP（持久连接、有状态）

2.7 阶段流水线 — 从环境准备到交叉验证，每阶段有明确的输入/输出/工具选择

3.运行时验证优先 — 不信任静态代码中的字符串常量，关键参数必须断点捕获

4.结论溯源 — 每项结论标注来源和验证方式，区分确认/推测

将这些经验编码为 Agent 定义（Markdown prompt），使得 AI 可以在新目标上复用同一套分析方法论，显著降低 JS 逆向的人工成本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](htt...