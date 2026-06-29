---
title: 当 AI 学会逆向工程 — IDA Pro MCP × CodeBuddy 逆向分析全流程实战
url: https://mp.weixin.qq.com/s/cYbgT_Cxv6CmvoRQPcUyDg
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:31:43.042654
---

# 当 AI 学会逆向工程 — IDA Pro MCP × CodeBuddy 逆向分析全流程实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/y3xArqr5PZlmicA5VAv2WxrW28OfWPbpSzMTsPfNC6rx6jSAetia5eYewiaO4OKFvR4xjzDugQehMQxBZUljKPuynDBpv4NLSxIbtQvIFYBxvA/0?wx_fmt=jpeg)

# 当 AI 学会逆向工程 — IDA Pro MCP × CodeBuddy 逆向分析全流程实战

原创

黄鹂儿
黄鹂儿

一路狂飚的蜗牛

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

用一句自然语言，完成对 crackme.exe 的全自动逆向分析。

---

## 一、前言

逆向工程一直是安全研究领域的核心技能之一。传统的逆向分析流程，通常需要研究人员坐在电脑前，手动操作 IDA Pro、Ghidra 等工具，逐函数、逐指令地分析目标程序。

但如果我告诉你，现在你可以**像和同事聊天一样，让 AI 帮你完成逆向分析**呢？

> "帮我打开这个 crackme.exe，反编译 main 函数，找到 Flag。"

这句话听起来像是科幻电影里的情节。但在今天，借助 **MCP（Model Context Protocol）** 协议，这已经成为现实。

本文将带你亲历一次完整的实战过程：配置 IDA Pro MCP 服务器、让 CodeBuddy 连接它、并用一条自然语言指令完成对 crackme.exe 的全自动逆向分析。

准备好了吗？让我们一起看看，**AI 是如何学会逆向工程的**。

---

## 二、什么是 MCP？

MCP（Model Context Protocol）是由 Anthropic 提出的一种开放协议，它定义了一套标准化的接口，让 AI 模型能够与外部工具、数据源进行交互。

简单来说，MCP 就像是给 AI 装上了"手脚"。以前 AI 只能靠自己的知识库回答问题，现在它可以通过 MCP 协议调用外部工具、读写文件、甚至操控 IDA Pro 进行逆向分析。

**MCP 的核心架构：**

```
┌───────────────┐    HTTP/stdio      ┌───────────────┐      API     ┌────────────┐│ MCP Client    │ ◄────────────────► │ MCP Server    │ ◄──────────► │  IDA Pro   ││ (CodeBuddy)   │                    │ (idalib-mcp)  │              │  (idalib)  │└───────────────┘                    └───────────────┘              └────────────┘
```

* **MCP Client：嵌入在 AI IDE 中（如 CodeBuddy），负责向用户提供对话界面**
* **MCP Server：独立运行的服务进程，暴露一组 Tools（工具函数）供 AI 调用**
* **通信协议：支持 stdio 和 HTTP（streamable-http）两种模式**

以本次实战为例，我们使用的是 streamable-http 模式：CodeBuddy 作为 MCP Client，通过 HTTP 请求调用 WSL 中运行的 idalib-mcp 服务，后者再通过 idalib（IDA Pro 的无界面库）操作二进制文件。

---

## 三、认识 IDA Pro MCP

IDA Pro MCP 是一个开源项目（github.com/mrexodia/ida-pro-mcp），它把 IDA Pro 的强大分析能力封装成了 MCP Server，让 AI 可以通过标准化的接口来操控 IDA。

### 两种运行模式

| 模式 | 说明 | 适用场景 |
| --- | --- | --- |
| **Plugin 模式** | 作为 IDA Pro 插件运行，需要 GUI | 桌面交互分析 |
| **Headless/idalib 模式** | 无界面运行，通过 idalib 在后台分析 | 服务器/CI/CD/自动化 |

本次实战使用的是 **Headless 模式**。它暴露了 20+ 个工具（Tools），涵盖逆向分析的方方面面：

| 工具名 | 类别 | 功能说明 |
| --- | --- | --- |
| `idb_list` | 会话管理 | 获取当前分析会话 |
| `server_health` | 状态检查 | 检查 IDA 运行状态 |
| `survey_binary` | 概览 | 获取二进制文件全局概览 |
| `lookup_funcs` | 函数查找 | 按名称查找函数地址 |
| `decompile` | 反编译 | Hex-Rays 反编译器，生成 C 伪代码 |
| `disasm` | 反汇编 | 生成汇编代码 |
| `find` / `find_regex` | 搜索 | 搜索字符串、立即数、交叉引用 |
| `xrefs_to` | 引用分析 | 查找对某地址的所有交叉引用 |
| `callees` / `callers` | 调用关系 | 分析函数调用关系 |
| `imports` | 导入表 | 列出所有导入的 API |
| `analyze_function` | 综合分析 | 对函数进行综合分析 |

---

## 四、环境搭建

## 4.1 环境信息

| 组件 | 配置 |
| --- | --- |
| 操作系统 | Windows 11 + WSL Ubuntu |
| IDA Pro | IDA Professional 9.4 + idalib (Headless) |
| MCP Server | ida-pro-mcp (idalib-mcp) |
| MCP Client | CodeBuddy IDE (streamable-http) |
| Python | 3.11+ + uv 包管理器 |

### 4.2 配置 CodeBuddy MCP

在项目根目录下创建 `.codebuddy/mcp.json` 文件：

```
{ ”mcpServers”: { ”ida-pro-mcp”: { ”type”: ”streamableHttp”, ”url”: ”http://127.0.0.1:8745/mcp”, ”description”: ”IDA Pro MCP - Headless reverse engineering analysis” } }}
```

### 4.3 启动 IDA Pro MCP 服务

在 WSL Ubuntu 中执行：

```
cd /mnt/c/study/Workspace/python_workspace/ida-pro-mcpuv run idalib-mcp --host 0.0.0.0 --port 8745 crackme.exe.i64
```

### 4.4 生成 .i64 数据库（重要！）

在实践中我们发现，idalib **无法直接打开 .exe 文件**，需要先用 `idat` 生成分析数据库：

```
idat -A -B -P+ crackme.exe # 生成 crackme.exe.i64
```

这个命令会自动分析二进制文件，生成包含函数、段、字符串等信息的 .i64 数据库文件（约 39MB）。

---

## 五、踩坑记录：open\_database 返回值 Bug

在环境搭建过程中，我们遇到了一个典型的坑，这也是本次实战中最有价值的发现之一。

### 现象

MCP 服务启动后一直报错：

```
RuntimeError: Failed to open database: /path/to/crackme.exe.i64
```

### 排查

问题出在 `idalib_session_manager.py` 的 `_activate_database_path` 方法中：

```
# 修复前的代码（有 Bug）db_id = idapro.open_database(input_path, run_auto_analysis=True)if db_id is None or db_id == 0: raise RuntimeError(f”Failed to open database: {input_path}”)
```

经过调试发现，`idapro.open_database` 的返回值并不稳定：

| 文件类型 | 返回值 | 实际结果 |
| --- | --- | --- |
| crackme.exe | 0 | 确实失败（无法直接打开） |
| crackme.exe.i64 | **-1 或 0** | **返回值不稳定，但实际均加载成功！** |

### 根因

对于预分析过的 .i64 数据库，`open_database` 可能返回 `0` 但实际加载成功。不能依赖返回值来判断成功与否。

### 修复

不依赖返回值，而是通过函数数量来验证：

```
# 修复后的代码idapro.open_database(input_path, run_auto_analysis=True)# 返回值可能为 0，但实际可能成功，用函数数量验证import ida_funcsif ida_funcs.get_func_qty() == 0: raise RuntimeError(f”Failed to open database (0 functions): {input_path}”)
```

> 💡 **经验**：这个 Bug 的修复很好地体现了"不要盲目信任文档"的原则——当实际行为与预期不符时，深入调试比猜测更有效。

---

## 六、分析实战：一句话拿下 crackme.exe

一切准备就绪后，我们在 CodeBuddy 中输入一条自然语言指令：

> "把这个 MCP Server 配置到 CodeBuddy 中，并使用 crackme.exe 做示例进行分析，给出报告。"

AI 开始自动执行以下分析流程：

### 6.1 获取二进制概览

AI 调用 `survey_binary` 和 `server_health` 工具，获取了文件的基本信息：

| 属性 | 值 |
| --- | --- |
| 文件名 | crackme.exe |
| 编程语言 | **Go (Golang)** |
| 架构 | AMD64 (x86-64) |
| Image Base | 0x140000000 |
| 总函数数 | 2,062 (已命名 1,715) |
| 字符串数 | 7,279 |
| SHA256 | a9054e68834be057b24443dd89b25389dc2f991be84883814cd0561339ac0431 |

### 6.2 定位关键函数

AI 使用 `lookup_funcs` 查找 `main.main` 函数，并通过 `find_regex` 搜索关键字符串：

```
main.main @ 0x1400B1640 (size: 0x3D4 / 980 bytes)”[+] Flag” @ 0x1400E0B30 # 直接找到了 Flag！”woniu” @ 0x1400E0B47 # 用户名”password” @ 0x1400DBDAC # 密码关键字
```

### 6.3 Hex-Rays 反编译

最关键的一步：AI 调用 `decompile` 工具，对 `main.main` 函数进行 Hex-Rays 反编译，得到了清晰的 C 伪代码：

```
void main_main(){ string *username; string *password;  // 打印 Banner fmt_Fprintln(stdout, ” CrackMe - Level 1”);  // 读取用户名和密码 fmt_Fprint(stdout, ”Enter username: ”); username = runtime_newobject(&RTYPE_string); fmt_Fscanf(stdin, ”%s”, username);  fmt_Fprint(stdout, ”Enter password: ”); password = runtime_newobject(&RTYPE_string); fmt_Fscanf(stdin, ”%s”, password);  // 用户名验证 (XOR 0x7F) if (username->len == stored_len) { for (i = 0; i < stored_len; i++) if (username->str[i] != (encrypted_user[i] ^ 0x7F)) goto INVALID_USER; } else {INVALID_USER: fmt_Fprintln(stdout, ”Invalid username!”); os_Exit(1); }  // 密码验证 (XOR 0x7F) if (password->len == stored_len) { for (j = 0; j < stored_len; j++) if (password->str[j] != (encrypted_pass[j] ^ 0x7F)) goto INVALID_PASS; } else {INVALID_PASS: fmt_Fprintln(stdout, ”Invalid password!”); os_Exit(1); }  // 验证成功！ fmt_Fprintln(stdout, ”[+] Congratulations! You cracked it!”); fmt_Fprintln(stdout, ”[+] Flag: FLAG{crackme_woniu_2026}”);}
```

---

## 七、分析结果

整个分析过程全自动完成，AI 从加载文件到生成报告一气呵成。最终结果如下：

| 项目 | 结果 |
| --- | --- |
| 用户名 | `woniu` |
| 密码 | `woniu_test` |
| Flag | `FLAG{crackme_woniu_2026}` |
| XOR Key | `0x7F` |
| 难度 | ★☆☆☆☆（入门级） |

### 验证逻辑分析

通过反编译代码可以清晰地看到，该程序的安全机制非常简单：

1. 用户名和密码以 XOR 0x7F 混淆形式存储在数据段
2. 输入后逐字符与存储的加密值进行 XOR 比较
3. 验证通过后直接显示 Flag
4. **Flag 以明文形式存储在 .rdata 段，可直接通过字符串搜索发现**

### 与 C 源码的对比

有趣的是，二进制文件是由 **Go** 编译的，而原始源代码是 C 语言。反编译结果与源代码高度一致，但有些微小差异：

| 特征 | C 源码 | Go 二进制 |
| --- | --- | --- |
| XOR Key | `0x37` | `0x7F` |
| 验证函数 | 独立 `check_password()` | 内联到 `main.main` |
| 失败处理 | `return 1` | `os.Exit(1)` |
| 反调试 | 长度检查 | 未使用 |

---

## 八、技术亮点与思考

## 8.1 Headless 模式的优势

idalib-mcp 的 Headless 模式是本次实战的核心亮点。相比传统的插件模式，它有以下优势：

1. **无需 GUI：可以在服务器、Docker 容器、WSL 等无头环境中运行**
2. **自动化友好：完全通过 API 调用，适合 CI/CD 流水线集成**
3. **多会话支持：同时分析多个二进制文件，会话隔离**
4. **MCP 协议标准化：任何支持 MCP 的 AI IDE 都可以直接使用**

### 8.2 AI 辅助逆向的未来

这次实战展示了一个很有意思的趋势：**逆向工程正在从"手动操作"向"自然语言驱动"转变**。

你不再需要记住 IDA Pro 的每个快捷键，也不需要精通 IDAPython API。你只需要告诉 AI：

> "找到验证函数，反编译它，然后告诉我正确的密码是什么。"

这对于安全研究人员来说，意味着效率的巨大提升。但同时也带来了新的思考：当逆向分析变得这么容易时，我们如何保护自己的软件？

### 8.3 关键经验总结

**1. 用 .i64 而不是 .exe**

idalib 无法直接打开 PE 文件，需要先用 `idat -A -B` 生成分析数据库。这是 headless 模式的已知限制。

**2. 不要盲目信任返回值**

`idapro.open_database` 的返回值不稳定，应通过函数数量等实际指标来验证加载是否成功。

**3. 了解工具参数格式**

MCP 工具的参数格式可能与直觉不同，建议先通过 `mcp_get_tool_description` 查看每个工具的参数 schema。

---

## 九、总结

通过这次实战，我们完成了以下几件事：

1. ✅ 配置了 IDA Pro MCP Server，并与 CodeBuddy IDE 集成
2. ✅ 发现并修复了 `open_database` 返回值判断的 Bug
3. ✅ 用**一句自然语言指令**完成了对 crackme.exe 的完整逆向分析
4. ✅ 生成了包含反编译代码、验证逻辑、破解方案的详细分析报告

MCP 协议的出现，让 AI 不再只是一个聊天机器人，而是一个真正能够"做事"的智能体。它可以调用 IDA Pro 分析二进制文件，可以操控浏览器进行 Web 测试，可以读写数据库——它的能力边界只取决于有多少 MCP Server 与之连接。

**当 AI 学会了逆向工程，下一步，它还会学会什么？**

这是一个值得每个技术人思考的问题。

---

> **相关链接**
>
> * IDA Pro MCP 项目：github.com/mrexodia/ida-pro-mcp
> * MCP 协议：modelcontextprotocol.io
> * CodeBuddy：codebuddy.ai

---

*本文基于 2026 年 6 月 28 日实战记录由CodeBuddy撰写！*

--------------------------...