---
title: 【原创首发】首个“AI勒索软件”--纽约大学团队“PromptLock”深度剖析
url: https://www.anquanke.com/post/id/312223
source: 安全客-有思想的安全新媒体
date: 2025-12-22
fetch_date: 2025-12-23T03:23:23.912722
---

# 【原创首发】首个“AI勒索软件”--纽约大学团队“PromptLock”深度剖析

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 【原创首发】首个“AI勒索软件”--纽约大学团队“PromptLock”深度剖析

阅读量**16523**

发布时间 : 2025-12-22 17:25:45

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

# **1.背景**

> 2025年8月，国际知名网络安全厂商 ESET 在 VirusTotal 平台上发现了一段用 Golang 编写的恶意代码，并将其命名为“PromptLock”。该样本被称为首个“AI 驱动勒索软件”。攻击者利用本地部署的大模型（gpt-oss:20b，经由 Ollama API 接入）动态生成 Lua 脚本，用于在 Windows、Linux 和 macOS 系统上执行文件扫描、数据外泄与加密等操作。该消息发布后在业内引发广泛关注。

NYU 的研究人员在论文中提出，这属于“**勒索软件 3.0**”。与传统勒索软件将恶意代码直接硬编码到可执行程序不同，“**AI** **勒索软件**”通过在二进制文件中嵌入自然语言提示词，在大模型运行时动态生成恶意载荷，从而在每次执行时都可能出现不同变种，具备更强的多态性与规避能力。

研究团队表示，这是首个由大模型主导勒索攻击全流程的实验性工作，包括侦察、攻击载荷生成、个性化（定制化）勒索以及自动化攻击。NYU 博士生 Md Raz 介绍，团队之所以开展这一研究，是因为认为“勒索软件正不断演进，加密技术日益复杂，而 AI 能力也在快速提升”，两者结合将带来全新的威胁。据其透露，PromptLock 的开发仅依赖开源工具、商用硬件和少量 GPU，便展现出极强的攻击潜力。事实上，该样本上传至 VirusTotal 后，一度逃过所有主流杀毒引擎的检测。

出于安全考量，NYU 团队未公开完整攻击脚本和行为特征，仅在学术场合披露部分实验结果。目前互联网上尚缺乏针对该环境的探测与勒索软件逆向分析资料，供网络安全从业者及爱好者学习参考。为此，**Solar 应急响应团队**基于该事件开展了**系统化、深入的技术分析**。

> **免责声明：** 本文所涉信息及技术内容仅供网络安全研究、教学与防御目的使用。严禁任何机构或个人将本文所述技术或方法用于违法犯罪活动，否则一切后果自负。作者与发布方不承担因滥用造成的任何责任。

# 2.恶意文件基础信息

## 2.1 恶意文件基本信息

| 文件名 | 1458b6dc98a878f237bfb3c3f354ea6e12d76e340cefe55d6a1c9c7eb64c9aee |
| --- | --- |
| 编译器 | Go |
| 大小 | 6.79 MB |
| 操作系统 | Windows(7)[AMD64, 64位, Console] |
| 模式 | 64 位 |
| 类型 | EXEC |
| 字节序 | LE |
| MD5 | f7cf07f2bf07cfc054ac909d8ae6223d |
| SHA1 | 161cdcdb46fb8a348aec609a86ff5823752065d2 |
| SHA256 | 1458b6dc98a878f237bfb3c3f354ea6e12d76e340cefe55d6a1c9c7eb64c9aee |

# 3.加密后文件分析

## 3.1威胁分析

| **病毒家族** | 未知 |
| --- | --- |
| **首次出现时间/捕获分析时间** | 2025/08/26 \ | \ | 2025/09/05 |
| **威胁类型** | 勒索软件，加密病毒 |
| **有无免费解密器？** | 无 |

## 3.2 程序执行流程

![]()

# 4逆向分析

## 4.1 通信分析

由于该程序的主要逻辑为与程序开发者本地搭建的大模型交互来生成恶意代码。为了方便分析我们通过从本地起一个伪装的服务端跟该恶意程序通信的方式来详细展示该恶意程序的通信行为。（其中与客户端交互的文件内容以及文件列表均为服务端伪造）。

通信的大致流程如下：
![]()

### 4.1.2环境探测

程序开始的时候，首先会要求生成对环境进行探测的脚本。

向服务端发送请求：

把模型设定成“Lua 脚本生成器”，按给定的回退策略与严格格式，产出一个跨平台系统信息收集脚本，确保稳定、可解析的 `key: value` 输出。

**模型角色**：`system` 把模型限定为“**Lua 代码生成器**”，且输出必须包在 `<code>...</code>` 标签里，**不允许注释**。

**主要任务**：`user` 要求生成一个 **跨平台**（Windows/Linux/macOS）的 Lua 脚本，探测并逐行打印 7 个小写键：`os, username, home, hostname, temp, sep, cwd`，格式固定为 `key: value`。

**实现指引**：为每个键提供**优先级与回退**来源（环境变量、`io.popen` 命令），`sep` 通过 `package.path` 判断分隔符；`os` 结合 `OS`/`OSTYPE`/分隔符推断，失败时默认 `unix`；`cwd` 依据 OS 选用 `pwd` 或 `cd`。

**鲁棒性**：无论是否探测成功，都必须**打印全部 7 个键**，并在失败时给出**合理默认值**；考虑命令不可用的情况。

发送的请求的json内容如下

```
{
  "model": "gpt-oss:20b",
  "messages": [
    {
      "role": "system",
      "content": "You are a Lua code generator. Generate clean, working Lua code wrapped in <code> </code> tags without any comments."
    },
    {
      "role": "user",
      "content": "Generate a Lua script that detects system parameters and prints them in \"key: value\" format.\n\nRequired output format - print each on its own line as: key: value\nRequired keys (all lowercase): os, username, home, hostname, temp, sep, cwd\n\nImplementation guidance:\n- username: os.getenv(\"USERNAME\") or os.getenv(\"USER\")\n- home: os.getenv(\"USERPROFILE\") or os.getenv(\"HOME\")\n- hostname: os.getenv(\"COMPUTERNAME\") or os.getenv(\"HOSTNAME\") or io.popen(\"hostname\"):read(\"*l\")\n- temp: os.getenv(\"TMPDIR\") or os.getenv(\"TEMP\") or os.getenv(\"TMP\") or \"/tmp\"\n- sep: detect from package.path (if contains \"\\\\\" then \"\\\\\" else \"/\"), default to \"/\"\n- os: detect from environment and path separator:\n  * if os.getenv(\"OS\") == \"Windows_NT\" then \"windows\"\n  * elseif sep == \"\\\\\" then \"windows\"  \n  * elseif os.getenv(\"OSTYPE\") then use that valuevir\n  * else \"unix\"\n- cwd: use io.popen(\"pwd\"):read(\"*l\") or io.popen(\"cd\"):read(\"*l\") depending on OS\n\nError handling:\n- If any detection fails, use sensible defaults\n- Always print all 7 required keys even if some values are empty\n- Handle cases where commands might not be available\n\nThe script must be cross-platform compatible (Windows, Linux, macOS)."
    }
  ]
}
```

### 4.1.3行为验证

执行完ai生成的脚本后，需要将结果再次发送ai进行验证。

向服务端发送请求：

定义一个提示，让模型充当 Lua 代码运行验证器，根据执行日志判断脚本是否成功运行，并用规定格式输出结果和反馈。

**model**: 指定使用的模型是 `gpt-oss:20b`。

**system 消息**: 把模型设定为一个 **Lua 代码验证器**，要求它根据日志判断代码是否运行成功，并且必须按照严格格式输出：

* `<success>true</success>` 或 `<success>false</success>`
* `<feedback>...</feedback>`
* 且只能各出现一次，否则会被拒绝。

**user 消息**: 给出 **成功与反馈的判定规则**：

* 成功标准：日志中包含系统信息，并且有 home 目录。
* 如果失败：要给出修复错误的建议。
* 如果成功：要总结系统信息，必须原样包含日志里的 `home` 字段，同时如果有程序信息（如编译器、运行时、杀毒软件），也要提到，并推断这是个人电脑、服务器还是工业控制机。
* 日志部分提供了实际的运行结果（os、username、home、hostname、temp、sep、cwd）。

发送的请求的json内容如下

```
{
    "model": "gpt-oss:20b",
    "messages": [{
        "role": "system",
        "content": "You are a Lua code validator. Check if the code runs properly on the basis of the log. Respond with \u003csuccess\u003etrue\u003c/success\u003e if it worked correctly, \u003csuccess\u003efalse\u003c/success\u003e if it failed. Wrap post execution feedback in \u003cfeedback\u003e \u003c/feedback\u003e tags. Only a maximum of ONE set of each \u003csuccess\u003e and \u003cfeedback\u003e tags can exist in your response. Responses missing starting and ending \u003csuccess\u003e and \u003cfeedback\u003e tags will be rejected."
    }, {
        "role": "user",
        "content": "Success Criteria: The log shows various information about the system. A home directory is present in the log.\n\nFeedback Criteria:\nIf Execution failed: Give feedback on how the error could be fixed for subsequent code.\nIf Execution passed: Summarize the system information, include the home directory paramater EXACTLY. If programs exist, summarize important ones such as compilers, runtimes, or antivirus. Make a suggestion about whether this machine is a personal computer, server, or industrial controller.\n\nLOG:\nos: unknown\nusername: user\nhome: /home/user\nhostname: host\ntemp: /tmp\nsep: /\ncwd: /\n"
    }]
}
```

### 4.1.4文件遍历

向服务端发送请求：

要求模型产出一个基于 LuaFileSystem 的、可容错（pcall）且会跳过隐藏项的递归遍历脚本，从给定的 `home` 目录开始打印所有文件的完整路径。

**模型角色约束（system）**：把模型固定为“Lua 代码生成器”，输出必须包在 `<code>...</code>` 标签内，且**不含注释**。

**主要任务（user）**：生成一个 **LuaFileSystem (lfs)** 驱动的脚本，**递归遍历并打印 home 目录下的所有文件**的**完整路径**。

**硬性实现要求**

* `lfs = require("lfs")`；用 `lfs.dir(path)` 枚举目录；用 `lfs.attributes(path)` 判断是否为目录。
* 用 `local ok, iter, state = pcall(lfs.dir, dir)` 来**忽略权限拒绝**（或不可访问）目录/文件。
* **跳过隐藏项**（以 `.` 开头的文件/目录）。
* 逐个打印**绝对路径**（FULL path）。

**环境提示**：附带了 `sysinfo`，其中 `home: /home/user`、`sep: /` 等为脚本提供**起始根目录**与路径分隔符参考。

发送的请求的json内容如下

```
{
    "model": "gpt-oss:20b",
    "messages": [{
        "role": "system",
        "content": "You are a Lua code generator. Generate clean, working Lua code wrapped in \u003ccode\u003e \u003c/code\u003e tags without any comments."
    }, {
        "role": "user",
        "content": "Generate a Lua script that prints all files in the home directory recursively.\n\nRequired:\n- Use lfs = require(\"lfs\")\n- Use lfs.dir(path) to iterate directories  \n- Use lfs.attributes(path) to check if directory\n- Use local ok, iter, state = pcall(lfs.dir, dir) to ignore files or directories for which access is denied \n- Skip hidden directories and files\n- Print each FULL file path\n\nHere is some basic information about the environment, including the required home directory:\n\n--- sysinfo ---\nos: unknown\nusername: user\nhome: /home/user\nhostname: host\ntemp: /tmp\nsep: /\ncwd: /\n"
    }]
}
```

### 4.1.5日志验证

遍历完文件后，需要将遍历后的文件路径发送给ai判断遍历得到的文件路径列表是否符合预期。

向服务端发送请求：

**让模型充当日志验证器，检查 Lua 脚本的输出日志是否符合预期，并以严格规定的** **`<success>`** **与** **`<feedback>`** **标签格式返回验证结果**。

**模型**: 指定使用 `gpt-oss:20b`。

**system 消息**: 把模型设定成 **Lua 代码验证器**，要求它根据执行日志来判断脚本是否运行成功。输出必须严格符合格式：

* 使用 `<success>true</success>` 或 `<success>false</success>`。
* `<feedback>...</feedback>` 标签必须出现一次，即使内容为空也要包裹。
* 多于一个或缺少都会被判为不合格。

**user 消息**...