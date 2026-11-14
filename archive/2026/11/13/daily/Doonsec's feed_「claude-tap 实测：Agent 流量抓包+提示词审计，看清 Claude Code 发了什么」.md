---
title: 「claude-tap 实测：Agent 流量抓包+提示词审计，看清 Claude Code 发了什么」
url: https://mp.weixin.qq.com/s/lx8VnwH8UPAGhPsHuqREIw
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:18:18.721039
---

# 「claude-tap 实测：Agent 流量抓包+提示词审计，看清 Claude Code 发了什么」

# 「claude-tap 实测：Agent 流量抓包+提示词审计，看清 Claude Code 发了什么」

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

你问 Agent 刚才做了什么，它会给你一段总结。你问它读了哪些文件，它会列一个清单。这些话通常都对，但它们都是 Agent 自己写的。

真正发出去的东西在另一层：HTTP 请求体。system prompt 有多长，工具 schema 里写了什么，上下文里塞了哪几段文件，哪一句话被截断，token 花在哪里。这些内容不会出现在终端里，也不会完整出现在会话记录里。

`claude-tap` 就是把这一层翻出来给你看的工具。它是个本地代理加一个 trace 查看器，MIT 协议，11 月 13 日查询时 3336 星、289 个 fork、43 个未关 issue，主语言 Python，2026 年 2 月建仓，最新 PyPI 版本 0.1.146 发布于 10 月 17 日，仓库累计 138 个 release，9 位贡献者。

## 一、它做的事很窄

跑一条命令，它起一个本地代理，把你要观察的客户端拉起来，让客户端的 API 请求先经过自己，再转发到真正的上游。请求和响应成对落盘，退出时生成一个自包含的 HTML 查看器。

支持 16 类客户端：Claude Code、Codex CLI、Codex App、Gemini CLI、Grok Build CLI、DeepSeek Harness、Kimi CLI 与 Kimi Code、MiMo Code、OpenCode、OpenClaw、Pi、Hermes Agent、Cursor CLI、Qoder CLI、Antigravity CLI、CodeBuddy CLI。名单里既有官方 CLI，也有各种兼容网关和本地中转，这一点比只支持一家的抓包工具实用。

两种代理模式：

* **reverse**：改客户端的 base URL，指向本地代理，代理再转发到上游。适用于认 `ANTHROPIC_BASE_URL`、`OPENAI_BASE_URL` 这类变量的客户端。
* **forward**：给子进程注入 `HTTPS_PROXY` 和本地 CA，客户端以为自己在直连。适用于同时连多个厂商的客户端，比如 OpenCode、Pi、Hermes。

还有一个例外：Cursor 是 transcript-only。它只监听 `~/.cursor/projects/*/agent-transcripts/*.jsonl`，不 MITM `api2.cursor.sh`。所以 Cursor 的"抓包"其实是读本地会话文件，不是看真实请求。

## 二、为什么这件事在 AI 安全里重要

Agent 的自述和事实之间，隔着三层东西。

**第一层，模型有没有被换掉。** 请求体里的 `model` 字段、上游地址、响应里的 `model` 字段，三者对不对得上。用第三方中转站的时候，这一层最容易被做手脚。今年已有研究披露过路由层替换模型、伪造转售商的问题。抓一次包，比看十篇测评有用。

**第二层，工具描述里有没有夹带指令。** MCP 服务器的工具描述、参数 schema、`description` 字段，都会原样进入模型上下文。工具投毒的常见做法就是把指令写在这些字段里。会话记录里不一定显示，请求体里一定有。

**第三层，上下文里有没有不该有的东西。**`.env`、私钥、内部地址、客户数据，是不是被 Agent 读进了 prompt。这一层最容易被"它只读了一个文件"这种自述掩盖。

客户端自己的日志由客户端写，可以省略、截断、改写。HTTP 请求体是客户端发出去的原文，除非它同时控制代理，否则改不了。这就是抓包在安全审计里的价值：它不是更详细的日志，它是另一个来源的证据。

## 三、它自己怎么描述风险

仓库的 `SECURITY.md` 写得很直接：trace 文件可能包含 prompts、tool schemas、文件路径、响应体和其他私有上下文，**即使 API key 已经被脱敏**。它列出的安全敏感面包括 API key、auth token、cookie、header 处理、trace 脱敏与导出、正反向代理路由、`--tap-host` 与 `--tap-no-launch` 的远程绑定、生成的 CA 与逐主机证书、生成的 viewer HTML。

一份安全工具的安全声明写到这个程度，说明作者知道这东西的两面性。下面这些结论，是我在 0.1.146 上实测出来的。

## 四、我实测到的几件事

我在本机装了 0.1.146，用一个本地假上游做实验，不涉及任何真实模型调用。

**第一，代理只在 `--tap-no-launch` 模式下绑 `0.0.0.0`。** 启动日志写的是 `listening on http://0.0.0.0:8899`，`lsof` 也确认 `TCP *:8899 (LISTEN)`。代码里的注释说，这个模式通常是远程使用场景。问题是它不校验 `Proxy-Authorization`，只把这类头当 hop-by-hop 头剥掉。同一网段的人把它当开放代理用，流量会落到你的磁盘上。

**第二，回环目标静默不录。** 我把上游指向 `127.0.0.1:8898`，请求成功转发，返回 200，但 trace 记录是 0 条。仓库里有个未关 issue #465，说的就是 loopback 网关在 reverse 模式下静默不被记录。这个行为我复现了。

**第三，换成局域网地址就录到了。** 上游换成 `192.168.31.161:8896`，同样一条请求，录到 1 条记录。

**第四，记录的 header 只留前 12 位。** 我故意发了一个带 `Bearer` 前缀的长 token，trace 里存下来的长度是 15 个字符，即前 12 位加三个点；`x-api-key` 同样处理；`cookie`、`set-cookie` 直接替换成 `***`。

**第五，请求体一个字都没脱敏。** 我在 body 里放了一个 AWS key 形状的字符串，trace 里原样保留，`body` 长度 233 字符，`system`、`messages`、`tools` 的 `input_schema` 全在。这跟 `SECURITY.md` 的警告一致：header 脱敏不等于 body 脱敏。

**第六，记录落在 SQLite，不在 `--tap-output-dir`。** 0.1.146 的记录写在 `~/.local/share/claude-tap/traces.sqlite3`；我按 README 把 `--tap-output-dir` 指向一个临时目录，会话进行中那个目录是空的。README 里的 `./.traces` 是导出目录的口径，实时记录在数据库里。这一条建议自己跑一遍确认，不同版本可能有差异。

**第七，路径白名单挡掉了非 API 流量。** 我用 `example.com` 走代理，返回 404，没有转发也没有记录。代码里有一份 `ALLOWED_PATH_PREFIXES`，只放行 `/v1/messages`、`/v1/responses`、`/v1/chat/completions`、`/v1beta/models`、`/v1internal` 这类端点。这个设计减少了误录，也意味着自定义端点要显式加进去。

![claude-tap 的 trace 查看器：按模型分组，右侧是请求详情](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J2hBCjr4Lft1PTnBs5awmRMj8vzRbrHIMXpdruwp2HUegaHJ5SmIhTjibJMYl7tNZtnPCJicsKylAxMohLYCPOx06IbFceWl5PRPzY3t7Udak/640?wx_fmt=jpeg "claude-tap 的 trace 查看器：按模型分组，右侧是请求详情")

## 五、查看器里能看到什么

查看器是一个自包含的 HTML 文件，不依赖外部资源。几个实用功能：

* **结构化 diff**：对比相邻两次请求，标出新增/删除的消息、system prompt 的差异，字符级高亮。排查"为什么这一轮行为变了"，这个功能最省时间。
* **路径过滤**：只看 `/v1/messages` 或某个端点。
* **模型分组**：侧栏按模型分组，Claude 系列优先排序。多模型切换时能一眼看出哪一轮用了哪个。
* **token 四段**：input、output、cache read、cache creation 分开列。
* **工具检查器**：展开看工具名、描述、参数 schema。
* **全文搜索**：在消息、工具、prompt、响应里搜。
* **复制 cURL**：一键把某条请求复制成 cURL，方便复现。
* 8 种界面语言，含简体中文。

![相邻请求的结构化 diff，能看出这一轮上下文多了什么](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J2hBCjr4Lfv7QU8b5xYMQbJmeAeXvoogwdeickSic9zkAInuETsiaVePZ2I5NpyVqyZ5JfT2bibEkIh04iaZ4qyIYpfAv8e3NhFktxBW84PQor3I/640?wx_fmt=jpeg "相邻请求的结构化 diff，能看出这一轮上下文多了什么")

导出有两种：`claude-tap export <session-id> -o trace.ctap.json` 生成紧凑包，再把紧凑包渲染成 HTML；或者直接从 JSONL 生成。HTML 可以带 `embed=1&hideHeader=1` 这类参数嵌到别的页面里。

## 六、上手

```
uv tool install claude-tap
pip install claude-tap            # 需要 Python 3.11+

claude-tap                        # 默认 Claude Code，实时查看器默认开
claude-tap --tap-client codex       # Codex CLI
claude-tap --tap-client hermes      # Hermes，forward 模式
claude-tap dashboard               # 只浏览历史记录
```

`--` 之后的参数原样传给客户端，比如 `claude-tap -- --model claude-opus-4-6`。

Hermes 的接入值得单独说一句。它默认走 forward 模式，给子进程注入 `HTTPS_PROXY` 和本地 CA，因为 Hermes 可能连 Nous Portal、OpenRouter、NVIDIA NIM、GLM、Kimi、MiniMax 等多家。如果跑 gateway，要用 `claude-tap --tap-client hermes -- gateway start`，它会自动把 `gateway start` 改写成 `gateway run`，否则 systemd/launchd 拉起的守护进程不继承代理，一条记录也不会有。

Bedrock 有个硬约束：原生 AWS 端点带 SigV4 签名，改 base URL 会破坏签名，所以只能用 `--tap-proxy-mode forward`，不能 reverse。自定义 Bedrock 网关（不带 SigV4）可以 reverse。

![claude-tap 的代理结构：客户端、代理、上游三段](https://mmbiz.qpic.cn/mmbiz_jpg/J2hBCjr4LftMRw3VO0ZfibCNUFwO07FicXyQcfPS5DRXX5C6Afaic6FIKicfh7rCK5SXLlibOia9GjdcXcCHwLUUgnia82ofpicGwV0hPuvr0fQNmlY/640?wx_fmt=jpeg "claude-tap 的代理结构：客户端、代理、上游三段")

## 七、避坑

1. **`--tap-no-launch` 默认绑 `0.0.0.0`，代理没有鉴权。** 在共享网络、云主机、办公网里这样跑，等于开了一个会记录流量的开放代理。要么加防火墙，要么显式 `--tap-host 127.0.0.1`。
2. **本地 CA 有效期 5 年，逐主机证书 1 年，私钥在 `~/.claude-tap`。** 拿到这个私钥的进程可以伪造任意站点的证书。它装进的是当前用户的 login keychain，不用 sudo，也不碰系统钥匙串，但这不代表风险低。
3. **header 脱敏只留前 12 位，body 完全不脱敏。** prompt、工具 schema、文件内容、响应体、路径全是明文。别把 `.traces` 或 `traces.sqlite3` 放进同步盘、共享目录、备份。
4. **导出的 HTML 是自包含的。** 发出去等于把整段上下文发出去。对外分享前先确认里面有没有客户数据、内部地址、密钥形状的字符串。
5. **`--tap-store-stream-events` 会存原始 SSE/WebSocket 事件数组。** 默认关是有原因的：开了之后体积和敏感内容都会上一个量级。
6. **客户端侧有一批静默失败。** #465 回环网关不录、#463 Codex App 自定义 provider 只转发不记录、#455 关闭终端会漏一个孤儿客户端进程、#478 opencode v2 架构变更不兼容、#240 请求体偶发被整体解析成一个字符串。录不到不等于没发生，先确认记录条数。
7. **Cursor 不 MITM。** 它只读 transcript，能看到会话内容，看不到真实请求头、真实模型字段。要验中转站，别用 Cursor 模式。
8. **它不是防护工具。** 只观察，不拦截，不阻断。要拦要在它前面再加一层网关或沙箱。把它当"审计相机"，别当"门禁"。
9. **43 个未关 issue、138 个 release。** 迭代快，边界情况也多。生产用之前先在自己的客户端上跑一遍，确认记录条数对得上。

## 八、适合谁

适合做 Agent 安全审计、事件响应、供应链核查的人：要确认第三方中转有没有换模型、有没有在请求里加料，抓一次包就有答案。

适合 Agent 开发者：调 prompt、调工具 schema、排查上下文漂移，结构化 diff 比读日志快。

适合做采购和安全评估的人：厂商说自己的网关不记录、不改请求，用这个工具看一眼就知道。

不适合把它常开在生产环境，不适合放在多用户共享的机器上，也不适合把 trace 当合规证据——它没有签名链，没有防篡改，只是一个本地记录。

## 九、最后一句

Agent 安全这两年在做一件事：从"信 Agent 说了什么"转向"看协议层发生了什么"。沙箱管它能碰到什么，网关管它能连到哪里，`claude-tap` 管它到底发了什么。三件事各管一段，缺一段都不完整。

它不判断对错，只把原文摆出来。真正难的部分不在工具，在谁来读这些 trace、读完敢不敢承认自己家的 Agent 确实发了那些东西。

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