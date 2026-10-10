---
title: 「AI Agent安全」IronClaw拆解：WASM沙箱+凭证注入怎么防密钥泄露
url: https://mp.weixin.qq.com/s/okUKUN6mLHpiqCTJLm1aEw
source: Doonsec's feed
date: 2026-10-09
fetch_date: 2026-10-10T07:56:02.999494
---

# 「AI Agent安全」IronClaw拆解：WASM沙箱+凭证注入怎么防密钥泄露

# 「AI Agent安全」IronClaw拆解：WASM沙箱+凭证注入怎么防密钥泄露

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一个越来越尖锐的问题

你让 AI 助手帮你读邮件、整理文件、查资料的时候，有没有想过一件事：**它手里握着你的 API key。**

这不是吓人。现在流行的这一类「个人 AI 助手」（OpenClaw 那一挂）本身就是一个常驻进程，能装工具、能联网、能读你本地文件，还能接微信、Slack、Telegram。你给它一个 `ghp_...` 或者 `sk-...`，它就能替你 push 代码、发消息、调接口。

问题在于，这些「工具」很多不是你写的。你从社区装一个、从 MCP 拉一个，它就能读你的工作区、拿你的密钥。这个工具是谁写的、它会拿你的密钥去哪儿，你根本不知道。

今天拆的 IronClaw（`nearai/ironclaw`），就是冲这个问题来的。

## 它是什么

一句话：**NEAR AI 开源的「Agent 操作系统」，用 Rust 把 OpenClaw 重写了一遍，核心卖点是把安全做进架构里。**

它的自我定位是「你的安全个人 AI 助手」。和 OpenClaw 的差别，它在文档里写得很直白：

* OpenClaw 有近 **50 万行代码、53 个配置文件、70+ 个依赖**，安全停在应用层（白名单、配对码），所有东西跑在一个 Node 进程里、共享内存；
* IronClaw 用 Rust 重写，代码量小到「能看懂」，Agent 跑在各自的 Linux 容器里，做的是**文件系统隔离**，而不只是「权限检查」。

截至我核实（2026-10-09），仓库 `nearai/ironclaw` 的数据是：

* **12,645 个 star、1,479 个 fork、1,547 个未关 issue**
* Rust 写的，**MIT OR Apache-2.0** 双协议
* 2026-02-03 建仓，最新版本 **ironclaw-v1.4.1**（2026-09-29 发布）

## 亮点：四层防御纵深

它把安全拆成四层互相独立的防线，数据要一层层过完，才能到 LLM 和外部服务：

1. **WASM 沙箱**——非受信工具跑在 WebAssembly 容器里，权限按「能力」声明；
2. **凭证保护**——密钥永远不交给工具，在「主机边界」注入；
3. **提示注入防御**——输入校验、内容净化、策略引擎、泄漏检测、工具输出包裹，五道；
4. **网络白名单**——工具只能连预先批准的端点。

![IronClaw 安全数据流：四层防御纵深](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4Lfu5jUSk63qAKH98JzYODjp0qZnPiaIRBgPRC2lYKnR1XedBzAJYwicZMt8l09oAo4y3kXp6W4p1xNvUFqib3qfdOZicDTiaDoibm8KJI/640?wx_fmt=png "IronClaw 安全数据流：四层防御纵深")

## WASM 沙箱：工具的能力写在文件里

在 IronClaw 里，非受信工具跑在 **wasmtime** 沙箱里，能力由 `capabilities.json` 一份文件声明——这是唯一的真相源。

拆开看它的沙箱约束：

* **Fuel 计量**：每条 WASM 指令都消耗「燃料」，默认上限 **1 亿条指令**，跑完就被终止，防止死循环把 Agent 拖死；
* **内存上限**：默认 **16 MB** 线性内存，超了直接 trap；
* **限流**：每个工具独立的 `requests_per_minute` / `requests_per_day`，防止被投毒的工具狂调 API；
* **主机函数只有 4 个**：`log`、`now_unix_secs`、`workspace_read`、`workspace_write`。就这些。

WASM 模块**不能** fork 进程、不能执行 shell、不能加载动态库、不能直接碰网络。它的网络出口只有一条路：模块发出的 HTTP 请求先到网络代理，代理校验目标域名在不在 `allowed_hosts` 白名单里，不在就**在建立 TCP 连接之前**拒绝；HTTPS 走 `CONNECT` 隧道，代理先验主机名再放行。

一句话：**一个被投毒的 WASM 工具，也读不到你的密钥，也连不到白名单之外的任何主机。**

## 凭证注入：密钥永远不进容器

这是我觉得最值得抄的一块设计。

在 IronClaw 里，工具**不能**直接访问密钥。工具要做的是，在 `capabilities.json` 里声明「我需要哪个 key」：

```
"credentials": {
  "google_oauth_token": {
    "secret_name": "google_oauth_token",
    "location": { "type": "bearer" },
    "host_patterns": ["gmail.googleapis.com"]
  }
}
```

然后工具正常发一个**不带认证**的 HTTP 请求，网络代理在出站时拦截，把 `Authorization` 头补上再转发。整个过程里，密钥**从没进过 WASM 模块的内存**。

密钥本身用 **AES-256-GCM 加密**存在本地，只有代理层拿得到。官方文档里有一句话很关键：**凭证注入是单向的**——没有任何机制让 WASM 模块读到存储里的密钥，「即使模块被攻破，它也碰不到密钥库」。

这比「把 key 塞进环境变量、让工具自己读」的传统做法高一个层级。因为环境变量对容器内的一切代码都是可见的，工具一旦被投毒，key 就跟着走。

## 提示注入 + 泄漏检测

外部内容（用户输入、工具返回）在进 LLM 之前要过五道：

1. **输入校验**——长度、编码、禁用模式；
2. **净化器**——转义危险内容；
3. **策略引擎**——按严重级别给动作（Block / Warn / Review / Sanitize）；
4. **泄漏检测**——扫 **15+ 种密钥模式**；
5. **工具输出包裹**——用 XML 格式包住、附转义提示，再进 LLM 上下文。

泄漏检测扫的是**所有要发给 LLM 的内容**，不管是用户输入还是工具返回。它用正则加启发式识别密钥形状：

| 模式 | 例子 |
| --- | --- |
| API key | `sk-...` 、`ak-...` |
| Token | `ghp_...` 、`sess-...` |
| 私钥 | `-----BEGIN RSA PRIVATE KEY-----` |
| 连接串 | `postgres://user:pass@...` |
| AWS 凭证 | `AKIA...` |

命令注入也单独查：命令拼接（`cat file; rm -rf /`）、子 shell（`echo $(cat /etc/passwd)`）、路径遍历（`cat ../../../etc/passwd`）都会被拦下来。

## 它整体长什么样

架构是 hub-and-spoke，Web 网关是中心：

* **Channels**：REPL、HTTP webhook、WASM channels（Telegram、Slack）、Web Gateway（SSE + WebSocket）；
* **Agent Loop**：消息处理和任务编排；
* **Scheduler / Routines**：并行任务，加 cron / 事件 / webhook 触发；
* **Orchestrator**：容器生命周期、LLM 代理、按任务发 token，任务跑在 Docker 沙箱容器里；
* **Tool Registry**：内置 + MCP + WASM 工具；
* **Workspace**：全文加向量的混合搜索，做持久记忆；
* **Safety Layer**：提示注入防御和内容净化。

数据本地存储、无遥测，所有工具执行都有审计日志。

## 上手

装它，官方给了一条命令：

```
IRONCLAW_RELEASE_TAG=ironclaw-vX.Y.Z
curl --proto '=https' --tlsv1.2 -LsSf \
  "https://github.com/nearai/ironclaw/releases/download/${IRONCLAW_RELEASE_TAG}/ironclaw-installer.sh" | sh
```

然后跑引导配置：

```
ironclaw onboard
```

选 LLM provider、输 API key（隐藏输入）、接受默认模型。它会自动建本地配置、加密密钥库、WebUI 登录 token，并起后台服务。

![IronClaw 引导配置向导](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4LftmClOtPflsU1gLL4Co6wlkiamTH9EfxAFyZNTQAPP0L3UxGBI1IHyoz7Wkv8qyibGHb6vbC2X6vwAQv4A68o7SPib7Ikd19ZgN1s/640?wx_fmt=png "IronClaw 引导配置向导")

之后：

```
ironclaw status          # 看服务状态、打印登录链接
ironclaw repl            # 开一个交互终端会话
ironclaw run --message "hello"   # 跑一轮
```

装 WASM 工具：

```
ironclaw extension search          # 列出运行时能看到的包
ironclaw extension search my-tool   # 找一个包
ironclaw extension install my-tool  # 按 id 装
```

注意：`extension install` 只认 **id**，传文件路径或 `https://` URL 都会失败。

## 避坑

第一，**项目还在快速演进**。1,547 个未关 issue 说明它很活跃，也说明接口和目录结构还会变。今天能跑的命令，下个版本可能就换了。生产用之前盯紧版本。

第二，**装第三方 WASM 工具前，必须先读它的 `capabilities.json`**。这份文件决定了这个工具能连哪些域名、读哪些路径、注入哪些凭证。官方文档专门加了一条警告：装不受信来源的 WASM 工具前先审能力文件。这不是可选项。

第三，**WASM 沙箱只覆盖「非受信工具」**。内置的 Rust 工具是受信的，跑在正常进程里，不受 WASM 那套约束。它的模型是「把不信任的东西关进沙箱」，不是「把一切关进沙箱」。

第四，**它是单用户系统**。文档里明确写了 single-user——实例所有者范围（owner scope）贯穿持久任务、密钥、job、设置、扩展、工作区记忆。它面向「一个人一个助手」，不是多租户平台。

第五，**它是 Agent OS，不是安全扫描器**。这点得分清楚：它的定位是「安全优先的操作系统」，安全是它的设计约束，不是你外挂的护栏。它不会替你去扫别人写的代码，也不会替你审第三方仓库。你要找「审仓库」的工具，那得另找（比如 MEDUSA 那一类）。

第六，**OpenClaw 的很多功能它还没对齐**。官方自己维护了一份 `FEATURE_PARITY.md`，Discord、WhatsApp、iMessage 这些渠道，语音、OTel/Prometheus 等还是没实现。想直接从 OpenClaw 迁过来的人，先看这份矩阵。

## 适合谁

* **自建个人 AI 助手、又担心密钥安全的人**：想给助手读邮件、文件、聊天记录，但不想让 API key 裸奔在容器里的；
* **给团队搭 Agent 平台的人**：想看一套「默认隔离 + 凭证不进沙箱」的参考架构的；
* **写 AI Agent 工具的开发者**：想知道「一个工具到底该声明哪些能力」的，`capabilities.json` 是个不错的范本；
* **研究 AI Agent 安全的人**：想拆一套把 WASM 沙箱、凭证注入、提示注入防御、网络白名单叠在一起的完整实现的。

**不适合谁**：想找一个「一键扫代码」的安全工具的人——它是操作系统，不是扫描器。

## 最后

回到开头那个问题：**要不要把 API key 交给一个能读你全部邮件、文件和聊天的助手。**

IronClaw 给的是一个工程答案：**密钥可以不进容器，工具可以只能连白名单域名，非受信代码可以关进 WASM 沙箱。** 这些不是「建议你小心一点」，是架构层面的强制约束。

这两年 AI Agent 铺开之后，安全的重点在悄悄挪位置。以前你担心的是模型会不会说错话，现在你更该担心的是**模型周围那一圈工具，和它们手里的凭证**。当每个 Agent 都能装工具、能联网、能读你的数据的时候，**「把密钥和不可信代码隔开」这件事，就得在架构里做，而不是靠自觉。**

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