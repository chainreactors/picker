---
title: Codex CLI + MoonBridge + FreeLLMAP+I+cc switch：一套零成本的 AI 编程助手搭建方案
url: https://mp.weixin.qq.com/s/CTNtwv4P8XzyGmzae2TLOQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:57:19.677829
---

# Codex CLI + MoonBridge + FreeLLMAP+I+cc switch：一套零成本的 AI 编程助手搭建方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BowImrBK4tKhDgM6iawoh7BxpRPWlRdiazoAsqqkrjicYQvBf5CjQMS3ZLkTeXagXQ0RxcdehtP6Lfpic2GKjIOj2t3BI0fX4KmnSicCicpdKBPpI/0?wx_fmt=jpeg)

# Codex CLI + MoonBridge + FreeLLMAP+I+cc switch：一套零成本的 AI 编程助手搭建方案

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 上次简单介绍了下FreeLLMAPI，今天用codex+MoonBridge+FreeLLMAPI，实现了免费智能AI助手的搭建，几亿的token可以用在codex上面了,在配合cc switch简直是对收费的降维打击

## 先说一下，为什么需要自己搭

很多人觉得 AI 编程助手很贵。Cursor 每月 20 美元，GitHub Copilot 每月 10 美元，Claude Pro 又是 20 美元。一个月下来小几百块就没了。

但如果你想白嫖，又不想用盗版，确实有一条路：**开源组件 + 免费 API 的零成本方案。**

Codex CLI（OpenAI 开源的终端编程助手）+ MoonBridge（协议转换代理）+ FreeLLMAPI（免费 LLM 聚合），这三件套搭起来，编程、写脚本、跑实验，基本够用了。

我们来拆解一下。

---

## 一、Codex CLI：OpenAI 的终端编程助手

Codex CLI 是 OpenAI 开源的一个 AI 编程工具，运行在终端里。84.7k star，Rust 写的，Apache-2.0 协议。

它能干嘛？

* • 读文件、写代码、执行命令
* • Git 操作、搜索网络、MCP 集成
* • 直接在终端里跟你对话，像 Claude Code 那样

之前它一直用 OpenAI 的 Chat Completions API。但 2026 年 2 月起，OpenAI 彻底停掉了老接口，**新版本的 Codex CLI 只支持 Responses API（/v1/responses）**。

这就带来了一个问题：Chat Completions 接口的模型用不了。

但 Codex CLI 的配置文件中可以自定义 `base_url`（`~/.codex/config.toml`），也就是说，你可以把它指向一个兼容 Responses API 的代理服务。

对于它的配置可以使用CC，参考如下：

```
model = "moonbridge"
model_provider = "ccx"
model_context_window = 1000000
model_max_output_tokens = 384000

[model_providers.ccx]
name = "Moon Bridge free"
base_url = "http://127.0.0.1:38440/v1"
wire_api = "responses"

[mcp_servers.deepwiki]
url = "https://mcp.deepwiki.com/mcp"
startup_timeout_sec = 3600
tool_timeout_sec = 3600
```

这就引出了第二个组件——

---

## 二、MoonBridge：协议转换，搞定 Responses API

MoonBridge 是一个开源的协议转换代理，GitHub 上叫 `ZhiYi-R/moon-bridge`，Go 语言写的，GPL v3。

它的核心功能是：

**对外暴露**`/v1/responses`**接口，对内把请求转成其他格式。**

具体来说，它支持三种工作模式：

1. 1. **Transform 模式**— 接收 Responses API 请求，转换为 Chat Completions 请求转发给下游
2. 2. **CaptureAnthropic 模式**— 转成 Anthropic Messages API 格式
3. 3. **CaptureResponse 模式**— 直接转发给另一个 Responses API 端点

为什么要这个东西？

因为现在大多数免费 LLM 提供商只支持 Chat Completions 接口，根本不支持 Responses API。MoonBridge 就是那个「翻译官」——你没 Responses API，我帮你转。

**配置文件可以交给hermes来写，提示词：安装了moonbridge，路径在～/tools/moon-bridge，检查下config配置，需要使用FreeLLMAPI的免费API**

---

## 三、FreeLLMAPI：免费模型的聚合入口

FreeLLMAPI 是一个聚合了十几个免费 LLM 提供商的 API 网关。

它有两种形态：

**开源版（tashfeenahmed/freellmapi）**— Node.js 写的，聚合了大约 14 个免费提供商，每个月能提供约 13 亿 tokens 的免费额度。对外暴露 `/v1/chat/completions`，支持智能路由和故障转移，还带一个 Web 管理界面。

**托管版（apifreellm.com）**— 用 Google 账号登录就能拿到一个永久的免费 API Key，不用自己部署。

它背后绑的免费提供商包括：Google Gemini 的免费层、Groq 的免费额度、Hugging Face Inference API 等。你只需要在这些平台上注册账号，拿到各自的 API Key，配置到 FreeLLMAPI 里就行。

**注意：**FreeLLMAPI 只提供 Chat Completions 接口，不提供 Responses API。所以它必须通过 MoonBridge 做协议转换才能接到 Codex CLI。

---

## 四、三件套组合：架构链路和配置方法

完整的链路长这样：

```
Codex CLI  ⟶  MoonBridge  ⟶  FreeLLMAPI  ⟶ 14+ 免费 LLM 提供商
   ↑               ↑               ↑
Responses API   协议转换       Chat Completions
```

**配置一共三步：**

### 第一步：启动 FreeLLMAPI

部署开源版，或者直接用托管版 apifreellm.com。拿到 API Key 后，把各个免费提供商的 Key 配置进去。FreeLLMAPI 默认暴露在 `localhost:3001/v1/chat/completions`。

### 第二步：启动 MoonBridge

MoonBridge 的上游指向 FreeLLMAPI，对外暴露 `localhost:8080/v1/responses`。

```
# 伪代码，实际以项目文档为准
moonbridge --upstream http://localhost:3001/v1/chat/completions --port 8080
```

### 第三步：配置 Codex CLI

修改 `~/.codex/config.toml`，把 base\_url 指向 MoonBridge：

```
[openai]
base_url = "http://localhost:8080"
```

然后启动 Codex CLI：

```
codex
```

搞定。

---

## 五、能用吗？优缺点坦白说

**能用的场景：**

* • 学习 AI 编程工具的原理
* • 写简单的脚本、自动化任务
* • 实验不同的模型组合
* • 低成本跑个人项目

**别指望它能取代 Cursor 或 Copilot 的场景：**

* • 大型项目代码审查
* • 需要深度理解上下文的复杂重构
* • 对延迟敏感的生产环境

**几个硬伤，不打马虎眼：**

1. 1. **模型不是顶级的**— 免费模型里没有 GPT-5、Claude Opus 这个级别的，指望写出生产级代码有点勉强
2. 2. **延迟叠加**— Codex CLI → MoonBridge → FreeLLMAPI → 免费提供商，三层代理，延迟肉眼可见
3. 3. **工具兼容性问题**— Responses API 和 Chat Completions 的工具调用转换不完美，部分模型可能翻车
4. 4. **免费额度有上限**— 13 亿 tokens 听起来多，但每个提供商各有独立的 Rate Limit

---

## 六、我的看法

这套方案的价值不在「替代付费产品」，而是 **让学习 AI 编程的入门门槛降到零**。

你能用它理解 Codex CLI 怎么工作，理解 Responses API 和 Chat Completions 有什么区别，理解协议转换的难点在哪。这些东西，光读文档是读不出来的。

另外，MoonBridge 这个项目本身很有启发。它揭示了一个趋势：**AI 工具的协议层正在走向统一，但过程会很痛苦。**Responses API 的出现让 OpenAI 可以塞更多功能（比如内置的 web\_search），但也让兼容性问题从「换个 base\_url 就行」变成「还要一个中间件做协议转换」。

如果你对这套方案感兴趣，建议周末花两小时搭一下。踩坑的过程本身，就是最好的学习方式。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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