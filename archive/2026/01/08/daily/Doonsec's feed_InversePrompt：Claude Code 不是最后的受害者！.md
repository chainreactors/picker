---
title: InversePrompt：Claude Code 不是最后的受害者！
url: https://mp.weixin.qq.com/s/RFl7dn1Gr3sYcWllkYiNFw
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:27:17.424231
---

# InversePrompt：Claude Code 不是最后的受害者！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkh6ibgic9WmUFBbMxOX4fUicWnpCen8mlUfGNtbolZt5dWUjwfm8Oy0rImQ/0?wx_fmt=jpeg)

# InversePrompt：Claude Code 不是最后的受害者！

原创

一个不正经的黑客

一个不正经的黑客

![]()

在小说阅读器中沉浸阅读

点击上方卡片“一个不正经的黑客”关注公众号

大家好，我是一个不正经的黑客，一个驰骋网络安全领域十年的安全牛马。

今天，我们来学习一个“船新”的黑客技术，探讨在如今AI应用盛行的年代，在安全领域，到底笼罩了一颗什么样的“乌云”？

## **引言：当 AI 帮你“黑”AI**

随着 Anthropic 推出的 **Claude Code** 逐渐被开发者接受，并成为一款强大的 **AI 编程助手（AI coding assistant）**，它被设计为一种**安全、可控**的方式，帮助开发者使用 Claude 的能力进行开发。

但问题来了：**如果这个原本用来“限制你”的助手，反而无意中教会你如何绕过这些限制，会发生什么？**

在 Anthropic 的 **Research Preview（研究预览）阶段**，我在 Claude Code 中发现了 **两个高危漏洞（high-severity vulnerabilities）**，并第一时间向官方反馈，相关问题也很快被团队修复。

这两个漏洞让我能够**突破系统原本设计的限制（escape its intended restrictions）**，并在 **Claude 自身的协助下**执行未经授权的操作。

通过“以工具攻工具”的方式，我开始深入研究 Claude Code 是**如何解析（interpret）和校验（validate）用户输入**的，最终发现了一些关键缺陷，直接导致了以下问题：

* • **路径限制绕过（Path restriction bypass）**
* • **通过命令注入实现代码执行（Code execution via command injection）**

更值得警惕的是：

**这两个漏洞都可以仅通过精心构造的 Prompt 进行利用（simple prompt crafting）**，并不需要复杂的攻击技巧。

这些发现再次提醒我们：在使用 **基于大语言模型（LLM-powered）的开发者工具**时，**盲目信任是极其危险的**。

因为在某些情况下，**负责“制定规则”的系统，本身也可能成为“打破规则”的工具。**

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkhVSzxibEUFGgPhEzPARLu58SPpQ01RRhAnFNlAmrba6Yz3icyQKH0JhRA/640?wx_fmt=jpeg&from=appmsg)

img

## **什么是 Claude Code？**

**Claude Code** 是 Anthropic 推出的一款 **AI 驱动的编程助手（AI-powered coding assistant）**，通过**自然语言 Prompt** 帮助开发者编写、分析和运行代码。

它是 **Claude 生态** 的一部分，专注于软件开发相关任务，例如：**函数生成、代码调试、以及与开发者本地机器上的文件进行交互**。

从设计上来看，Claude Code **以当前用户的权限运行**。在获得用户授权、并受用户配置限制的前提下，它几乎可以执行**用户本身能够执行的大多数操作**。

通常情况下，它的活动范围被限定在当前工作目录（Current Working Directory, CWD）内；当它尝试访问陌生文件，或执行不在预定义范围内的命令时，会主动向用户请求确认。

在这一模型下，Claude Code 具备以下能力：

• **读取或写入文件**

• **列出目录内容**

• **执行特定被允许的命令）**

• **在获得明确用户许可的情况下，与本地开发环境交互**

为了在 AI 助手与底层系统之间建立清晰的安全边界，Claude Code 在以下场景中会要求用户授权：

**访问 CWD 之外的陌生文件或路径，或执行不在预先批准命令列表中的指令。**

但正如接下来你将看到的那样，**这些边界并非牢不可破**。

有时，**仅凭一个精心构造的 Prompt，就足以跨越它们。**

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkhCEA7A41AF5XWZqFu69tOdGI2zwiab8BhAR9ibdXtG418ibhQAoZyO5nJg/640?wx_fmt=jpeg&from=appmsg)

img

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkh5rZgegBgXtabTshY8j3LVII4CaF42tAoSct9Fl2FicFicEM5I8uicibh4g/640?wx_fmt=jpeg&from=appmsg)

img

## **Claude Code 是如何工作的？**

Claude Code 通过一个安全的本地接口**运行，将 Claude 语言模型与你的**本地开发环境连接起来。

它的设计目标非常明确：**给 AI “刚刚好”的权限，让它足够有用；但除非用户明确允许，否则系统的其他部分一律不可触碰。**

在这套安全模型中，有 **两个核心控制机制**：

### CWD 限制（Current Working Directory）

Claude Code 的活动范围被限制在一个特定目录中，也就是**当前工作目录（Current Working Directory, CWD）**。

这意味着，所有与文件相关的操作——包括**读写文件、列出目录内容、遍历子目录**——都只能发生在这个明确划定的范围内。

一旦尝试访问 **CWD 之外的文件**，Claude 通常会采取以下两种处理方式之一：

• **通过系统提示请求用户的明确授权**

• **直接拒绝该请求**

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkhFSVK7Z67LeQpADJjga3j3aoYu5GBQJncqiafjpSWu8K3ncKeIzh1riaw/640?wx_fmt=jpeg&from=appmsg)

img

这一机制的设计初衷，是为了**防止未经授权的文件访问**，以及**敏感数据的泄露**。

### **预批准命令机制**

Claude Code **可以执行 Bash 命令**，但前提是：

这些命令必须来自一个**严格定义的预批准列表（whitelist）**。

通常，这个列表只包含一些**相对安全、面向开发场景的操作**，例如：

• ls

• cat

• touch

• mkdir

• echo

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkhTx926RdRPwajybJ7UEovia6YcibG6W6GT5UCc4egyVVWknIpAlXluwjQ/640?wx_fmt=jpeg&from=appmsg)

img

而那些**潜在风险更高的命令**（例如 rm、curl、dd），要么被直接拦截，要么需要用户进行**额外的显式确认**才能执行。

至少在设计层面，这样的机制被认为可以为系统提供一层防护，用来抵御：

• **命令注入（command injection）**

• **权限提升（privilege escalation）**

——**至少，理论上是这样。**

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkhOSicSWedG51mE35v215muHflagCEcWf9HwZyDQRnOGDeXxV8eQjKPTg/640?wx_fmt=jpeg&from=appmsg)

img

## **底层是怎么跑的？**

在内部实现上，**Claude Code** 是通过 **API** 调用 Anthropic 的 **Claude 大语言模型（Claude LLM）** 来工作的。

根据你的具体环境配置，这个工具可以连接到**不同的模型服务提供方（provider）**，包括：

• **Anthropic API**

• **AWS Bedrock**

• **GCP Vertex AI**

不同的平台，提供的 **Claude 模型版本** 也不尽相同，例如：

• **Opus**

• **Sonnet**

• **Haiku**

用户可以在初始化配置阶段，自行选择要使用的模型版本。

在连接过程中，Claude Code 会使用所选平台对应的 **API Key** 进行身份认证，随后将**所有发送给大模型的 Prompt**，统一转发到对应的后端服务进行处理。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkhiayetk3gAkUHAO4Mcg7pficcwicXjeodBciaXB0x4sEdGLPEYjbvDN4yoA/640?wx_fmt=jpeg&from=appmsg)

img

当你输入这样一个 Prompt：

**“List all files in the CWD（列出当前工作目录下的所有文件）”**

![img](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMobCJ9ZGKHRWHibyibnPbIDkhBm5RkwHgVQ9TmzeIwrD1icIdADYv1wicwGqM5oI1taiaFP8KfbwYUXn7Q/640?wx_fmt=jpeg&from=appmsg)

img

Claude Code 会先对这条 Prompt 进行**语义解析（interpret）**，然后将其映射到一条已被列入白名单的命令（例如 ls -la），并在 **CWD** 范围内执行。

按设计来说，**所有交互都会被记录（logged）并受到严格约束（constrained）**——

**至少，官方是这么设想的。**

## **逆向 Claude Code：我是如何开始“拆解”它的**

和许多 **LLM 开发者工具** 不同，**Claude Code 并不是开源项目（not open source）**，这也让漏洞研究变得更加棘手。

我的探索之旅，始于一个看似简单的问题：

> **在源码不可见的情况下，我还能搞清楚它“背后”是怎么运作的吗？**

一开始，我尝试寻找是否存在 **Claude Code 的公开版本或反混淆（deobfuscated）版本**。

这个过程把我引向了 **Geoffrey Huntley** 的一篇高质量博客文章。他的分析对 Claude Code 的运行方式、以及它如何与底层系统交互，提供了非常有价值的洞察。

更重要的是，他还公开了一个 **GitHub 上的反混淆项目**，其中包含了 **Claude Code 前端逻辑的可读快照**。

不过，我并没有直接依赖那份代码，而是决定**亲自动手**。

我选择在 **Cursor 编辑器**中使用**内置的 Claude**，一边观察应用的真实行为，一边逐步理解它的内部结构。

在 Claude 的“协助”下，我开始拆解那些被混淆过的 **JavaScript bundle**，不断向它提问：

• Webpack 的内部结构是怎样的？

• 常见的反混淆（deobfuscation）思路有哪些？

• 该如何一步步理清整个代码结构？

最终，我找到了一个非常强力的工具：**WebCrack**。

它让我能够**自动化完成反混淆过程**，并成功还原出一份**干净、可读的代码结构**——也就是 Claude Code 界面背后真正运行的逻辑。

到这一步，我已经拥有了一个**完整的代码轮廓**，以及一个**极其适合挖漏洞的环境（target rich environment）**。

接下来发生的事情，多少有点“魔幻”。

在用 WebCrack 生成反混淆文件之后，我只是**不断向 Claude 提问**——

想到什么就问什么。

而它的表现，**堪称完美**。

**Claude，真的在“协助”我逆向 Claude Code 本身。**

比如下面这段代码，就来自反混淆后的版本，展示了 **Claude Code 可以执行的一部分命令**，以及这些命令各自对应的 **正则限制（regex limitations）**。

```
var In5 = new Set([/^date\b[^<>()$`]*$/
 /^cal\b[^<>()$`]*$/
 /^uptime\b[^<>()$`]*$/
 /^echo\s+(?:'[^']*'|"[^"$<>]*"|[^|;&`$(){}><#\\\s!]+?)*$/
 /^claude -h$/
 /^claude --help$/
 /^git diff(?!\s+.*--ext-diff)(?!\s+.*--extcmd)[^<>()$`]*$/
 /^git log[^<>()$`]*$/
 /^git show[^<>()$`]*$/
 /^git status[^<>()$`]*$/
 /^git blame[^<>()$`]*$/
 /^git reflog[^<>()$`]*$/
 /^git stash list[^<>()$`]*$/
 /^git ls-files[^<>()$`]*$/
 /^git ls-remote[^<>()$`]*$/
 /^git config --get[^<>()$`]*$/
 /^git remote -v$/
 /^git remote show[^<>()$`]*$/
 /^git tag$/
 /^git tag -l[^<>()$`]*$/
 /^git branch$/
 /^git branch (?:-v|-vv|--verbose)$/
 /^git branch (?:-a|--all)$/
 /^git branch (?:-r|--remotes)$/
 /^git branch (?:-l|--list)(?:\s+"[^"]*"|'[^']*')?$/
 /^git branch (?:--color|--no-color|--column|--no-column)$/
 /^git branch --sort=\S+$/
 /^git branch --show-current$/
 /^git branch (?:--contains|--no-contains)\s+\S+$/
 /^git branch (?:--merged|--no-merged)(?:\s+\S+)?$/
 /^head[^<>()$`]*$/
 /^tail[^<>()$`]*$/
 /^wc[^<>()$`]*$/
 /^stat[^<>()$`]*$/
 /^file[^<>()$`]*$/
 /^strings[^<>()$`]*$/
 /^hexdump[^<>()$`]*$/
 /^sort(?!\s+.*-o\b)(?!\s+.*--output)[^<>()$`]*$/
 /^grep\s+(-[a-zA-Z]+\s+)*(?:'[^']*'|"[^"]*"|\S+)\s*$/
 /^pwd$/
 /^whoami$/
 /^id[^<>()$`]*$/
 /^uname[^<>()$`]*$/
 /^free[^<>()$`]*$/
 /^df[^<>()$`]*$/
 /^du[^<>()$`]*$/
 /^ps(?!\s+.*-o)[^<>()$`]*$/
 /^locale[^<>()$`]*$/
 /^node -v$/
 /^npm -v$/
 /^npm list[^<>()$`]*$/
 /^python --version$/
 /^python3 --version$/
 /^pip list[^<>()$`]*$/
 /^docker ps[^<>()$`]*$/
 /^docker images[^<>()$`]*$/
 /^ping\s+(?:-c\s+\d+\s+)[^<>()$`]*$/
 /^host[^<>()$`]*$/
 /^nslookup[^<>()$`]*$/
 /^dig[^<>()$`]*$/
 /^netstat(?!\s+.*-p)[^<>()$`]*$/
 /^ip addr[^<>()$`]*$/
 /^ifconfig[^<>()$`]*$/
 /^man(?!\s+.*-P)(?!\s+.*--pager)[^<>()$`]*$/
 /^info[^<>()$`]*$/
 /^help[^<>()$`]*$/
 /^sleep[^<>()$`]*$/
 /^tree$/
 /^which[^<>()$`]*$/
 /^type[^<>()$`]*$/
 /^history(?!\s+-c)[^<>()$`]*$/
 /^alias$/
 /^compgen[^<>()$`]*$/
 /^yes$/]);
```

## **CVE-2025-54794：路径限制绕过，逃离作用域（CVSS 评分 7.7）**

**Claude Code** 的设计初衷，是将所有文件操作严格限制在预先定义的当前工作目录（Current Working Directory, CWD）内。

这套**目录隔离（containment）模型**的目标很明确：

**除非获得明确授权，否则 AI 助手不应访问其作用范围之外的任何文件。**

而我做的第一件事，就是验证一个问题：

**Claude Code 是否也存在我之前在 Anthropic 的 Filesystem MCP Server 中发现过的那类漏洞？**

这些漏洞曾在博客中详细分析过：

> **CVE-2025-53109 & CVE-2025-53110 – EscapeRoute：突破 Anthropic 的...