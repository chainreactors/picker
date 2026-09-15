---
title: 「AI安全红队技能库Claude-Red实测：78个SKILL.md覆盖提示词注入+越狱+RAG投毒，GitHub 4146星」
url: https://mp.weixin.qq.com/s/tY2BA7FO_V4HavWo10M-pg
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T07:00:31.950338
---

# 「AI安全红队技能库Claude-Red实测：78个SKILL.md覆盖提示词注入+越狱+RAG投毒，GitHub 4146星」

# 「AI安全红队技能库Claude-Red实测：78个SKILL.md覆盖提示词注入+越狱+RAG投毒，GitHub 4146星」

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

想给红队整把手，不用自己撸一套扫描器或恶意脚本，直接把一批写好的攻击方法论"塞进"Claude 里，让它碰到某个攻击面就自动变成对应领域的专家。这不是科幻，就是今天句芒深挖的 **Claude-Red**——一个正在 GitHub 趋势榜上溜达的进攻性安全技能库。

## 它是什么：给 Claude 准备的攻击技能包

Claude-Red（`SnailSploit/Claude-Red`）是面向 Claude Skills 系统整理的开源攻击性安全技能库，Python 实现，MIT 许可。2026-03 创建，2026-09-14 用 GitHub API 核实 **4146 颗星、592 个 fork**，仍在活跃维护。

它的形态很朴素：仓库里是一批**结构化的 `SKILL.md` 文件**，每个文件把 Claude 在某个攻击面"升级"成领域专家——从 SQL 注入到 shellcode，从 EDR 逃避到 ADCS 滥用。目前 **78 个技能、23 个分类**，覆盖 Web（16）、无线（14）、基础设施与进攻性红队（7）、exploit 开发（6）、模糊测试、容器/K8s、CI/CD、密码学、供应链、社工、以及安全方向越来越火的 **AI 安全**。

![Claude-Red 仓库官方 banner（README 首图）](https://mmbiz.qpic.cn/mmbiz_jpg/J2hBCjr4LfvhsFlQbRHJMCquuXv24MJcibEectqf5KNhGjCC1NYbPibZyicVW6GQAjVOfR5g4UAeVmI6xxVoOnzOXwyXiczcXygaclnGAeuBEo8/640?wx_fmt=jpeg "Claude-Red 仓库官方 banner（README 首图）")

## 亮点：按需加载，不白烧上下文

和那种往系统提示里塞一整页"我无所不能"的提示词不同，Claude-Red 的设计核心是**按需加载、节省上下文**。技能通过对话里的触发词自动匹配——你把库扔进 `~/.claude/skills`，聊到 SQL 注入，它自动把 `offensive-sqli` 调进来；没用到的技能完全不占你的 token 窗口。每份 SKILL.md 也不是一句 prompt 带过，而是带元数据、触发词、完整方法论、检查清单、攻击链、修复建议的"作战手册"。

装法有三条路，任选：

```
# 方式1：装进 Claude Skills 系统（对话触发词自动激活）
git clone https://github.com/SnailSploit/Claude-Red ~/.claude/skills/claude-red

# 方式2：Claude Code，临时把某个技能灌成 system
cat Skills/ai/offensive-ai-security/SKILL.md | claude --system-file -

# 方式3：只拉某几个分类，别全量（sparse checkout）
git clone --filter=blob:none --sparse https://github.com/SnailSploit/Claude-Red
cd Claude-Red && git sparse-checkout set Skills/ai
```

仓库还带 `install.sh`，支持分类安装和指定目标目录。

## 从 AI 安全角度深挖：技能里到底写了什么

AI 安全分类下目前是 **`offensive-ai-security`** 一个技能，但厚度惊人——把整份 AI/LLM 攻击方法论列成了可执行清单。它先讲透脆弱性的**底层机制**：指令跟随与歧义（模型分不清指令和数据）、数据依赖（训练数据投毒 + 间接提示词注入）、黑盒不透明、过度代理权（插件）、不安全输出处理、资源消耗（DoS）、供应链、过度依赖。再往下连 2025-2026 的新打法都收进去了：

* **策略层冲突**——layer 的 provider/厂商/应用规则互相打架，留出隐性绕过窗口
* **稀疏微调漂移**——轻量 adapter 训练常常直接把基座模型的安全对齐磨掉
* **多模态通道**——视觉/语音模型继承文本漏洞，还多出隐写攻击面
* **工具链级联提权**——Agent A 委托 B、B 再够到特权 C，绕过单跳限制
* **记忆投毒**——往 AutoGPT、CrewAI、LangChain Memory 里注入持久恶意指令
* **分词器漏洞**——零宽字符、Unicode 归一化在清洗器和模型分词器之间不一致

攻击链它也帮你串好了。最典型的一条：**提示词注入（LLM01）→ 控制 LLM → 插件滥用/过度代理权（LLM08）→ SSRF 或 API 滥用 → 内网探测、数据外带**。还有间接注入吞外部文档、注入 + 不安全输出处理连成 XSS、恶意文档被内部 LLM 摘要时借插件外带数据……每条链都标注了终止在哪个 OWASP LLM 编号、能升级成什么后果。

工具清单也顺手点名了一串咱号反复用过的：garak、LLMFuzzer、promptfoo、PyRIT、ART、NeMo Guardrails。等于这份技能把打 AI 应用的主流武器都编排成了一本翻着就能用的手册。

防守侧它也没少写——**角色严格分离、工具/域名白名单（deny 不够要 allow）、JSON Schema 强校验 tool 参数、RAG 检索内容打"仅当数据"标签、外带代理域名白名单挡 SSRF、金丝雀 token 探测外带、fail-closed 控制**。攻防两边的清单都在同一个文件里，红蓝都能拿它当参照系。

## 上手与避坑

装完、在对话里点一句"prompt injection"或"AI 红队"，技能触发后你就获得了一整套打 AI 系统的步骤：先侦察理解目标（模型、工具、数据流、权限边界），再按 OWASP Top10 for LLM 逐项投注，手动构造注入话术（DAN 人格、Base64/同形字/零宽字编码、虚拟化攻击、语法破坏绕过人类过滤），最后把单个漏洞串成攻击链。技能里甚至给了一批**现成的注入样本**可以直接改着用。

四条坑必须说清：

* **只打授权环境。** 这是进攻性技能库。
* **SKILL.md 是方法论，不是自动外挂。** 它告诉你"该测什么、怎么测、怎么串"，动手搭环境、喂工具还是你自己来，别指望一句话让 Claude 全自动打穿。
* **技能本身有门槛。** 无线、exploit、EDR 这些分类很专，没有对应基础的人读了也跑不动。按需只装自己会的分类，别全量塞进去。
* **触发词匹配有边界。** 聊得不够准时技能不激活，关键场合直接 `--system-file -` 显式指定更稳。

## 适合谁

给自家 AI Agent / LLM 应用做授权红队的安全研究员；想系统摸清提示词注入、越狱、RAG 投毒攻击面、但手里缺一份结构化清单的工程师；以及做 CTF、赏金、agent 安全评估的团队。仓库 GitHub 搜 `SnailSploit/Claude-Red`，要装哪些技能、怎么配你自己的 Claude 环境、哪些 SKILL.md 的细节需要对着源码核，自己进仓库各技能目录翻，别图省事把整库无脑克隆到生产环境。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hHXiayYmia1LqLl6UmtMH3DtucaIaicr9HY5ffO5ckGVia3LvuCPCDNRNAX9fEmhicdmtRshennOyOqtPic6GTeASRNg/0?wx_fmt=png)

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