---
title: 「AI Agent安全+提示注入+开源SDK」Superagent拆解：给大模型应用装安全护栏
url: https://mp.weixin.qq.com/s/v9rom7uDgCPJlwZCKbUWaQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:37.168319
---

# 「AI Agent安全+提示注入+开源SDK」Superagent拆解：给大模型应用装安全护栏

# 「AI Agent安全+提示注入+开源SDK」Superagent拆解：给大模型应用装安全护栏

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一个聊天机器人，用户上传了一张照片。照片里有人举着一块牌子，上面写着一行字。模型读完这张图，就乖乖照做了——把画面里举牌的那个人从描述里「删掉」了。用户没有输入任何指令，攻击就藏在图片的像素里。

这类攻击叫视觉提示注入（visual prompt injection），它只是提示注入（prompt injection）的一种。AI 应用和传统软件不一样：它会读数据、听指令、调工具、再输出，失败的方式也不一样——提示注入、数据泄露、工具被诱导执行危险动作、工作流被带偏。`superagent-ai/superagent` 就是冲着这些问题来的：一个开源的 AI Agent 安全 SDK，把「护栏」直接嵌进你的应用。

![视觉提示注入的真实例子：右边的人举着一块牌子，上面写着让 AI 忽略自己的指令（仓库 docs/public 原图）](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4LfsDDQUAJrwFXVSepxNhvtrHZ1YUjogpMYy55n3OVEMeXDuPAPpScOianFibfmpmlQK3SlicdbUBzMWjoYYanJjLwxR2cmGpWNKD5g/640?wx_fmt=png "视觉提示注入的真实例子：右边的人举着一块牌子，上面写着让 AI 忽略自己的指令（仓库 docs/public 原图）")

## 先核身份

发布前用 GitHub API 当天核实：仓库 `superagent-ai/superagent`，**6763 颗星、963 个 fork、19 个未关闭 issue**，主语言 **TypeScript**，协议 **MIT**，2023 年 5 月 10 日建仓，最近一次提交在 **2026 年 8 月 25 日**。仓库 topics 直接写着 `prompt-injection`、`guardrails`、`llm`、`security`、`ai`、`anthropic`、`openai`，官网 superagent.sh，背后是 Y Combinator 支持的项目。它把自己定位成「Make your AI apps safe」——一个给 AI Agent 做安全的开源 SDK。

## 它要解决什么问题

传统软件的安全边界是确定的：输入校验、权限、SQL 参数化，都是静态规则。但 AI 应用多了一层「自然语言」这个不可信输入面。用户的一句话、一张图、一个 PDF、甚至仓库里一段被投毒的注释，都可能变成攻击载荷。

Superagent 的思路是：在 AI 应用的关键节点上，插入四个可编程的方法——`guard()`、`redact()`、`scan()`、`test()`。你可以把它们放在输入上、输出上，或者任意中间步骤上，而且它不绑定模型，OpenAI、Anthropic、Google、Groq、Bedrock、Fireworks、OpenRouter 都能接。

## 四个核心方法

**Guard（护栏）** 是核心。它把输入内容分类成 `pass` 或 `block`，检测提示注入、恶意指令和安全威胁。返回值里有 `classification`（pass/block）、`reasoning`（为什么这么判）、`violation_types`（违规类型，比如 `prompt_injection`、`visual_prompt_injection`）、`cwe_codes`（关联的 CWE 编号，比如 CWE-77）、`usage`（token 用量）。默认模型是 `superagent/guard-1.7b`，**开箱即用不需要任何 API key**。还可以传 `systemPrompt` 定制判断标准，用 `chunkSize`（默认 8000 字符，设 0 关闭分块）控制长文本切分。

**Redact（脱敏）** 负责把敏感数据从文本里拿掉。默认实体覆盖 SSN、驾照、护照号、API key、密钥、密码、姓名、地址、电话、邮箱、信用卡号；也可以传 `entities` 只脱敏你关心的类型，或者用 `rewrite: true` 做上下文改写而不是占位符替换——把「我的邮箱是 john@example.com」改成「我的邮箱已存档」，而不是留一串 `<EMAIL_REDACTED>`。

**Scan（扫描）** 面向仓库。它会把仓库 clone 进 Daytona 沙箱，用 OpenCode 去检测针对 AI Agent 的攻击，比如 repo poisoning（仓库投毒）、提示注入、恶意指令。默认分析模型是 `anthropic/claude-sonnet-4-5`，返回一份安全报告和本次扫描的 token 与美元成本。注意 scan 需要 `DAYTONA_API_KEY` 和至少一个模型 key。

**Test（红队测试）** 是跑红队场景，对生产 Agent 做 `prompt_injection`、`data_exfiltration` 这类攻击，返回发现的漏洞。目前文档标注为 coming soon。

![用 Superagent 护栏搭的 n8n 邮件分诊工作流示例（仓库 docs/public 原图）](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LfstQooKyAEibCMqLhu2fKXDlyicoopoCKBrY2ET2yMGMHiaOn0M75GVicHONfYAxWICvJF5tS2icwpGvQsoBQ2D1JFJoJlt94IFNXp8/640?wx_fmt=png "用 Superagent 护栏搭的 n8n 邮件分诊工作流示例（仓库 docs/public 原图）")

## 开源权重模型

Superagent 把 Guard 模型开源到了 HuggingFace，可以完全跑在自己的基础设施上，**不走任何 API 调用、数据不出本地环境**，CPU 或 GPU 上 50–100ms 延迟。提供 `superagent-guard-0.6b`、`1.7b`、`4b` 三个尺寸（Safetensors），以及对应的 GGUF 量化版本给 llama.cpp 用。

另有一个 20B 的 `SuperagentLM Guard 20B`：基于 GPT-OSS 20B 的 MoE 架构，131k token 滑动注意力上下文，20.9B 参数，导出成 Q8\_0 GGUF（约 19.5 GiB）。它自己放出的内部评测里，Superagent-LM 检测准确率 98%，对比 Gemini 2.5 Pro 97%、GPT-5 94.5%，而 Sonnet-4 只有 37%、Opus 4.1 只有 24.5%。这组数字的语境是「漏掉的攻击载荷越少越好」——它同时提醒一件事：通用大模型不等于安全模型。

## 多语言集成

SDK 覆盖 TypeScript 和 Python（`npm install safety-agent` / `uv add safety-agent`），还有一个 CLI：`superagent guard "..."` 直接输出 JSON，字段含 `rejected`、`decision.status`、`violation_types`、`cwe_codes`、`reasoning`，支持 `--system-prompt` 和 `--entities` 定制。此外还有 MCP Server，给 Claude Code / Claude Desktop 用，提供三个工具：`superagent_guard`（检测注入/越狱/数据外泄）、`superagent_redact`（脱敏 PII/PHI）、`superagent_verify`（对着源材料做事实核验）。

SDK 还内置了容错：`enableFallback`（默认开）、`fallbackTimeoutMs`（默认 5000ms）、`fallbackUrl`，应对主模型的冷启动；以及 `fallbackModel`，当主模型返回 429/500/502/503 时自动改投备份模型，备份模型可以来自完全不同的厂商，且只给一次机会、不做递归回退。

## 上手

```
npm install safety-agent
export SUPERAGENT_API_KEY=your-key
```

```
import { createClient } from "safety-agent";
const client = createClient();

const result = await client.guard({ input: userMessage });
if (result.classification === "block") {
  console.log("Blocked:", result.violation_types);
}
```

Guard 支持多种输入：纯文本、URL（自动抓取分析）、Blob/File（按 MIME 处理）、PDF（逐页并行分析、OR 逻辑、任一处违规即拦截，但扫描版 PDF 不做 OCR）、图片（需要 vision 模型，OpenAI/Anthropic/Google 支持，其余厂商当前只支持纯文本）。

## 避坑

* **它默认是云端调用。** guard/redact/scan 默认走 Superagent 的托管模型，需要 API key；只有自托管开源权重模型才完全不出网。要数据不出本地，就自己跑 GGUF。
* **Scan 的成本不低。** 它把仓库 clone 进沙箱再让模型分析，按 token 计费，大仓库成本会明显上升，先在小分支上试。
* **PDF 不做 OCR。** 扫描版 PDF 提取不到文字，等于没分析；图片必须用 vision 模型，纯文本模型看不到图里的注入。
* **它是 SDK，不是网关。** 它给你的是可编程的判断能力，拦截动作要你在自己的应用里执行；它不替你判断模型本身是否安全。
* **用途要合规。** 红队测试和仓库扫描只应在自有或获书面授权的目标上跑。

## 适合谁

如果你在做 AI 应用的工程落地，Superagent 值得看的不是「它有几个方法」，而是它把「AI 应用安全」这件事做成了能嵌进代码的四步：guard 判输入输出、redact 去敏感数据、scan 查仓库投毒、test 跑红队。开箱即用的 guard 模型不需要 key，开源权重模型又能让你把数据留在本地。

它的边界也很清楚：判断由模型给出、拦截由你执行，最后那道「到底拦不拦」的门，仍然得由人来守。

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