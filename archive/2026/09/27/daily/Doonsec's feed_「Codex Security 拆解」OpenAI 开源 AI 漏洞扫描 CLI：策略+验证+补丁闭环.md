---
title: 「Codex Security 拆解」OpenAI 开源 AI 漏洞扫描 CLI：策略+验证+补丁闭环
url: https://mp.weixin.qq.com/s/-ZFUp0n1_OVSrFfZqNvUdQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:55:31.187152
---

# 「Codex Security 拆解」OpenAI 开源 AI 漏洞扫描 CLI：策略+验证+补丁闭环

# 「Codex Security 拆解」OpenAI 开源 AI 漏洞扫描 CLI：策略+验证+补丁闭环

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

用 AI 扫代码漏洞，最难的不是"扫出来"。是扫出来之后那一堆东西：哪条是真的、谁去修、改完了怎么证明修好了。前两年大家比的是"我的 agent 能找出多少洞"，现在比的是"我能不能为每一条结论给出证据"。

2026 年 7 月 13 日，OpenAI 在 GitHub 上开了 `openai/codex-security`。两个多月过去，它今天已经是 10856 星、817 个 fork。有意思的是，它不是一个"AI 扫洞神器"，而是一套把"怎么审、怎么验、怎么修、怎么复核"写成文件的安全工程流水线。

![Codex Security 仓库标识](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LfuGv4cX9KjNl9RyAJ0m92eUAZIPa3Na1NX9Zpgfywib5RbUcfUC7cyqxVTDR5vcPDUD5Pt3M7bkd1gzkctU5VneLlRY4EkGs41w/640?wx_fmt=png "Codex Security 仓库标识")

## 先核身份

按老规矩，发布前用 GitHub API 当天核实：仓库 `openai/codex-security`，**10856 颗星、817 个 fork、34 个 watcher**；主语言 **TypeScript**，协议 **Apache-2.0**；2026 年 7 月 13 日建仓，最近一次推送就是**今天（2026 年 9 月 27 日）**，当前有 239 个未关闭 issue。npm 包名 `@openai/codex-security`，仓库内版本已到 **0.1.31**；运行要求 Node ≥ 22.13.0、Python ≥ 3.10；容器镜像 `ghcr.io/openai/codex-security`。

看数据就知道它在高频迭代。下面说几个我觉得真正值得抄的设计。

## 它先承认自己是一层薄壳

仓库根目录 `AGENTS.md` 的第一句话很直接：Codex Security 是 Codex 和它的安全插件外面的一层薄壳。也就是说，它没有自研一个"安全大模型"，而是拿 Codex 当引擎（隔离配置里模型是 `gpt-5.6-sol`、推理强度 `xhigh`、多 agent 线程上限 9，也就是 1 个父线程加最多 8 个子线程），外面套了一套安全技能包，再包成 CLI 和 TypeScript SDK 两种入口。

这套技能包是这个仓库里最厚的部分：`plugins/codex-security/skills/` 下有 15 个 `SKILL.md`——仓库扫描、diff 扫描、深度扫描、威胁建模、发现、验证、分诊、修复、修复复核、补丁风险体检、攻击路径分析、加固建议、finding 跟踪、漏洞写作、安全策略定义。`references/` 下还压着 `core-scan.md`、`scan-contract.md`、`finding-detail-fields.md`、`static-finding-assessment.md` 等参考文档。

换句话说：它把"怎么做好一次安全审计"这件事，写成了可读、可版本管理、可被 review 的文档，而不是塞在一段看不见的系统指令里。对做 AI 安全产品的人来说，这一步的价值比多接一个模型高得多。

## 一次扫描落三份规范产物，报告只是投影

它给"封存的扫描"定了一份契约，产物固定三份 JSON：

* `scan-manifest.json`：终态回执，记录终态时间戳、三份规范文档与证据的哈希、目标类型与 `snapshotDigest`；
* `findings.json`：语义化的 finding 记录；
* `coverage.json`：覆盖面，记录 mode、inventoryStrategy、completeness、审查过的 surface。

而平时你看到的 `report.md`，在这套设计里**只是投影**——由封存后的规范化文档确定性生成，不允许手写，SARIF、CSV 同样是下游投影。封存之后不可改，适配器只能读、不能改。

状态有四个值：`completed`、`failed`、`canceled`、`interrupted`。规矩只有一条：**只有 `completed` 才支持"完成结论"**。其余三种属于停下来的扫描，保留的 finding 和 coverage 必须被当成不确定，不能把"没发现问题"说成"没问题"。这一条把安全工具里最常见的自我欺骗直接堵死了。

## finding 的身份怎么保持稳定

这是我最喜欢的一段设计。每条 finding 有几个必须稳定的字段：

* `ruleId` 是**漏洞家族**，格式 `<类别>.<稳定控制家族>`，比如 `path-traversal.archive-extraction`、`authorization-bypass.object-update`。不是单次发现的编号。
* `identity.anchor` 是语义上的根控点，**明确禁止放行号**；同级但可独立攻击的兄弟问题用 `identity.instance` 区分。
* 指纹由 targetId、ruleId、anchor、instance 派生；`findingId` 由指纹派生，`occurrenceId` 由 scanId 加指纹派生。

它自己加了一句提醒：指纹匹配只是**对账信号，不是等价证明**，有歧义就当未解决处理。

仓库自带的示例产物正好能说明这套字段长什么样：一条 CWE-22 路径穿越，`ruleId` 是 `path-traversal.archive-extraction`，语义锚点是 `archive-entry-write-without-containment`，CVSS 3.1 打 8.1，严重度 high、置信度 high，受影响位置是 `src/extract.py` 的第 41 到 44 行，角色标为 sink，修复建议是"归一化目标路径，拒绝逃出解压根的条目"。

![仓库自带示例 finding](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LfuHJHbp91Xicaz6BMvwXEMedgadubUQcQ8R4MmHmIk7vvic2YmjWfSDuXE3jpLohUsJZcE07nibcpNkVcpfADB0R48fb5eEegA7nM/640?wx_fmt=png "仓库自带示例 finding")

行号一动、文件一改名，历史对账就全废——做过扫描平台的人都知道这个坑有多深。它选择把"稳定"放在语义层，而不是坐标层。

## 先让 AI 读你的规矩：策略即代码

`npx @openai/codex-security policy .` 会生成一份 `SECURITY.md` 草案，草案存在仓库外面，**不会自动装进仓库**，也不触发扫描；你要自己 review 那份 diff 再拷进去。做组件级策略可以加 `--path services/api --knowledge-base architecture.md`。

嵌套策略从根到叶组合，越靠近代码的优先级越高。它附带了两句提醒：别把 `.github/SECURITY.md`、`docs/SECURITY.md` 当成仓库级扫描规矩，也别在写根策略时把这两个覆盖掉。

更值得抄的是它的信任姿势：策略文件、源码、测试、finding 全部按**不可信证据**处理。它们可以影响范围判断和严重度口径，但**不能授权执行命令、改代码、对外披露或者扩大范围**。

## 深度扫描与成本上限

扫描分 standard 和 deep。deep 模式下：`--workers` 控制发现并发，`--subagents` 是每个 worker 的子代理数，`--stop-after-no-new` 是连续多少轮没新发现就停，`--max-discovery-runs` 封顶轮数，`--max-time-hours` 封顶时长（上限 96 小时，允许小数）。到点就停发现，把已完成的 finding 合并返回。

成本这块它写得很细，也很诚实：`--max-cost USD` 超了就停，但**在途请求可能跑超**；到 80% 时交互式面板会问你加不加预算，而 CI、JSON、headless 模式**不给加**。成本输出的是区间 `estimatedUsdRange`：下限按短上下文价格算，上限按长上下文价格算，上下文标为 `unknown`——原因很朴素：运行时无法知道哪一次请求走了长上下文定价。旧记录也不会被按现价重算。

## 发现 → 验证 → 修复 → 复核，四步都不许含糊

* `validate`：评估候选，可以喂自定义动态验证指令，要求任务报告验证证据，或者明说哪些检查没跑起来，**才允许**声称修好了。
* `patch`：改并验证；`--assess-patch-risk` 在补丁完成后跑一次补丁风险体检（只读、不改变补丁和合并状态）；`--create-pr` 走 `gh`/`glab` 开草稿 PR/MR，自建 GitLab 要设 `GITLAB_HOST`。
* 它的诚实边界：patch 结果里的 `applied`、`filesChanged`、`files`**只说明文件改了，不说明安全问题修好了**；已保存的 finding 还需要 patch 任务给出 `verified` 结果。
* `verify-fix`：在只读沙箱里复核，结论是 `fixed`、`still_vulnerable`、`inconclusive`，退出码 0/1/2；并且明说关闭的工单、无关的通过测试、以及"新扫描没报出来"**都不算修复证据**。

## 它自己写明的安全边界

这部分最有句芒味，我几乎原文照抄它的态度。

它运行在**你的操作系统权限**下，扫描与工作台子进程**可以继承你的环境变量**——仓库的 `.mcp.json` 里那份转发白名单长得很实在：`OPENAI_API_KEY`、`AWS_ACCESS_KEY_ID`、`AWS_SECRET_ACCESS_KEY`、`AWS_SESSION_TOKEN`、`AWS_ROLE_ARN`，还有 `HTTP_PROXY`、`HTTPS_PROXY`、`NODE_EXTRA_CA_CERTS` 之类。仓库原话是：扫描和工作台子进程可以继承你的环境，**包括无关的 API token 和云凭据**。所以它的建议是：只给扫描它需要的凭据。

![仓库自带 .mcp.json 的 env_vars 白名单](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4Lfu77gyHfV292EA0W4gicQeicWXwwQ9Xvmp5ibZ7coUDAEdFky4836iaYWfk6tof3zOHeP7DWB3do1Dh7wSIjQUjTCQ5ZLNyOjESNdg/640?wx_fmt=png "仓库自带 .mcp.json 的 env_vars 白名单")

deep 扫描的 worker 用只读执行来防止并发写工作区，但它马上补一句：**这不构成隔离环境，也不禁用继承来的 MCP server**；worker 必须留在父会话的权限范围内。它还专门区分了两种情况：使用继承工具的既有权限本身不算绕过安全边界，但被强制实施在那个工具或操作上的限制依然算数。

它的 `SECURITY.md` 说得更直白：**提示注入、或者模型滥用它本来就拥有的访问权限，本身不构成漏洞报告条件**，即使它泄露了数据或者做了不该做的事——必须证明存在一个**被强制实施的安全控制被绕过**。模型行为类的问题走单独的 Safety Bug Bounty；漏报、误报、扫描结果错误、性能问题都算普通 bug，不算安全问题。

对做 AI Agent 的人来说，这段文字等于一份现成的"边界声明模板"：先说清哪些不算漏洞，再谈哪些算。

## 两个很实用的小模式

**mock 模式**：`--mock` 不调模型、不需要认证，几秒内造出 12 条 finding——8 条在同一仓库重复扫描中稳定复现，4 条每次身份都变，另有两对是同一根因、不同标题、不同身份，专门拿来测去重。它自己声明这些是合成数据、路径和代码片段是虚构的、并且永远不会写进仓库。

**import 模式**：把已有 CSV/JSON 导进本地历史，原始标识保留在 `extensions.import`，原文件封存进 `artifacts/import/`，覆盖率标为 `unknown`，报告里**明说没有做安全分析**。这条思路很值得抄：导入的数据不是审计结论。

## 工程纪律也写在仓库里

`AGENTS.md` 里还有两条，我觉得比功能列表值钱得多：**保持简单**；**不要做投机性防御**——不要为假设中的问题加脱敏、校验、兜底逻辑，要说清它修的是哪个具体失败；并且明确禁止"先发明一个限制，然后写测试去满足这个限制"。另外公开 CLI 的变更按公共 API 对待，不许顺手加 flag。

## 适合谁，不适合谁

**适合**：有代码仓库、想把安全体检接进 CI 的团队；需要用自有策略统一严重度口径的团队；要把 finding 按流程发到 Linear 或云端的团队；对成本敏感、需要设上限的团队。

**不适合**：指望它替代人工审计的——它自己说漏报误报算普通 bug；扫你没权限的仓库——它以你本机权限运行；想一键"证明修好了"的——要 `verify-fix` 给出 `fixed` 才算。

想试的话，我建议的顺序是：先在一个小仓库跑 `--mock` 把链路跑通，再用 `policy .` 生成一份策略草案人工过一遍，然后拿一个真实仓库正式扫一次并设 `--max-cost`，最后再谈接 CI——配置放仓库外面。

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