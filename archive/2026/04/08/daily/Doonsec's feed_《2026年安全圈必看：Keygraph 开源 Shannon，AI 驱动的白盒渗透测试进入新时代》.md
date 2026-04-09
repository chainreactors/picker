---
title: 《2026年安全圈必看：Keygraph 开源 Shannon，AI 驱动的白盒渗透测试进入新时代》
url: https://mp.weixin.qq.com/s/qI6jN_6esu3yc5whu3ebTw
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:26:23.805119
---

# 《2026年安全圈必看：Keygraph 开源 Shannon，AI 驱动的白盒渗透测试进入新时代》

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4T1PVwJicwkibxjVU2c5iaiahia2vEr5rY9s85O4NLqadCibyVzYa3q8icpUsafEeFduqk1FGjVOU2IpHg3MpZ3qkwMkc6ag5icfW9BveKAjm1XUDL4/0?wx_fmt=jpeg)

# 《2026年安全圈必看：Keygraph 开源 Shannon，AI 驱动的白盒渗透测试进入新时代》

原创

KeygraphHQ
KeygraphHQ

泷羽Sec-Norsea

![]()

在小说阅读器中沉浸阅读

## Shannon是什么

Shannon是由Keygraph开发的AI渗透测试工具。它结合源代码分析和实时漏洞利用，对Web应用程序及其底层API执行白盒安全测试。

`Shannon` 会分析您的 Web 应用程序源代码，识别潜在的攻击途径，然后使用浏览器自动化和命令行工具对正在运行的应用程序及其 API 执行实际的漏洞利用（注入攻击、身份验证绕过、SSRF、XSS）。

最终报告仅包含具有可验证概念的漏洞。

地址见文末

## Shannon存在的意义

借助 Claude Code 和 Cursor 等工具，团队可以持续不断地发布代码。

但是，渗透测试呢？一年才进行一次。这造成了*巨大的*安全漏洞。

在剩下的 364 天里，可能在不知不觉中将漏洞部署到生产环境中。

`Shannon`通过提供按需自动化渗透测试来弥补这一差距，该测试可以针对每个构建或版本运行。

## 案例

`Shannon` 在 `OWASP Juice Shop` 中发现了 20 多个漏洞，包括身份验证绕过和数据库数据窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkicpPpC1MMVVjwrjjjPcb7XLLjadRpUoV5icKeeAGLn8lvIRfVicNy8HnicJN6qBibsxEiaq2UiccNW5CIsrGp7bbPB54XktaDybe8XUM/640?wx_fmt=png&from=appmsg)

**特点**

* **完全自主运行**：只需一条命令即可启动完整的渗透测试。`Shannon` 可自动处理双因素`身份验证/TOTP` 登录（包括单点登录）、浏览器导航、漏洞利用和报告生成，无需人工干预。
* **可复现的概念验证漏洞利用**：最终报告仅包含已证实可利用的漏洞，并提供可直接复制粘贴的概念验证代码。无法利用的漏洞将不予报告。
* **OWASP 漏洞覆盖范围**：识别和验证注入、XSS、SSRF 和身份验证/授权失效等漏洞，其他类别正在开发中。
* **代码感知动态测试**：分析源代码以指导攻击策略，然后使用实时浏览器和基于 CLI 的漏洞利用程序对正在运行的应用程序进行验证。
* **集成安全工具**：在侦察和发现阶段利用 Nmap、Subfinder、WhatWeb 和 Schemathesis。
* **并行处理**：漏洞分析和利用阶段在所有攻击类别中同时运行。

## 安装和使用说明

### 安装条件

* **Docker** - 容器运行时（安装 Docker）
* **Node.js 18+** - 使用需要`npx`（安装 Node.js）
* **pnpm** - 克隆和构建模式所需（安装 pnpm）
* AI提供商资质

+ **Anthropic API 密钥（推荐） - 从**Anthropic 控制台获取
+ **Claude Code OAuth 令牌**
+ **AWS Bedrock** - 使用 AWS 凭证通过 Amazon Bedrock 进行路由
+ **Google Vertex AI** - 通过 Google Cloud Vertex AI 进行路由（
+ **【实验性 - 不支持】通过路由器模式提供的替代提供商**- OpenAI 或 Google Gemini

### 快速入门（推荐：npx）

```
npx @keygraph/shannon setup # 配置凭证

export ANTHROPIC_API_KEY=your-api-key # 直接导出环境变量

npx @keygraph/shannon start -u https://your-app.com -r /path/to/your-repo # 开始渗透测试
```

Shannon 将从 Docker Hub 拉取工作进程镜像，启动基础设施，并启动一个用于扫描的临时工作进程容器。

### 克隆和构建

如果你想从本地克隆运行 Shannon、修改 Shannon 本身或保持本地构建的工作镜像，请使用此功能。

```
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon

cat > .env << 'EOF'
ANTHROPIC_API_KEY=your-api-key
CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
EOF

export ANTHROPIC_API_KEY="your-api-key"
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000

pnpm install
pnpm build

./shannon start -u https://your-app.com -r /path/to/your-repo
```

Shannon 将在本地构建工作进程镜像，启动基础设施，并启动一个用于扫描的临时工作进程容器。

### 准备存储库

Shannon 可以扫描您机器上的任何存储库。传递绝对路径或相对路径`-r`。

例如：

```
npx @keygraph/shannon start -u https://example.com -r /path/to/repo
```

克隆和构建命令等效项

```
./shannon start -u https://example.com -r ./relative/path
```

### 常用命令

#### 监测进度

```
npx @keygraph/shannon logs <workspace>
npx @keygraph/shannon status
```

打开 Temporal Web UI 以进行详细监控：

```
open http://localhost:8233
```

#### 停止Shannon

```
npx @keygraph/shannon stop
npx @keygraph/shannon stop --clean
npx @keygraph/shannon uninstall
```

#### 使用示例

```
npx @keygraph/shannon start -u https://example.com -r /path/to/repo

npx @keygraph/shannon start -u https://example.com -r /path/to/repo -c /path/to/my-config.yaml

npx @keygraph/shannon start -u https://example.com -r /path/to/repo -o ./my-reports

npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w q1-audit

npx @keygraph/shannon workspaces
```

### 工作区和恢复

Shannon 支持**工作区**，允许您恢复中断或失败的运行，而无需重新运行已完成的代理。

**工作原理：**

* 每次运行都会创建一个工作区（默认情况下会自动命名，例如`example-com_shannon-1771007534808`）。
* `./workspaces/`工作区以本地模式或`~/.shannon/workspaces/`npx 模式存储。
* 使用`-w` 可以为你的运行添加自定义名称，以便于引用
* 要恢复任何运行，请通过以下方式传递其工作区名称`-w`——Shannon 会检测哪些代理已成功完成，并从中断处继续运行。
* 每个代理的进度都通过 Git 提交进行检查点保存，因此恢复运行会从一个干净、经过验证的状态开始。

```
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w my-audit

npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w my-audit

npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w example-com_shannon-1771007534808

npx @keygraph/shannon workspaces
```

### 凭据和配置

#### 证书优先权

**本地模式**解析凭据的方式如下：

1. **环境变量**-`export ANTHROPIC_API_KEY=...`
2. **`.env`文件**-`./.env`

**npx 模式**使用 TOML 而不是`.env`：

1. **环境变量**-`export ANTHROPIC_API_KEY=...`
2. **`~/.shannon/config.toml`**- 由`npx @keygraph/shannon setup`

环境变量始终优先，因此无需编辑文件即可覆盖单个会话的已保存配置。

#### 配置（可选）

虽然可以不带配置文件运行程序，但创建配置文件可以启用身份验证测试和自定义分析。可以使用 `.` 传递任何配置文件路径`-c`。

##### 创建配置文件

复制并修改示例配置：

```
cp configs/example-config.yaml ./my-app-config.yaml
```

运行方式：

```
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -c ./my-app-config.yaml
```

项目地址：

```
https://github.com/KeygraphHQ/shannon
```

## 学习交流群

刚加入网络安全行业的小白，可以加入学习交流群，大家一起互相学习，互相进步，不会的难题大家一起学习，一起攻克。

想要进学习交流群的师傅们，可以扫描下方二维码添加好友，我再拉你进群（Ps：防止广告进群）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9dEclFnKnAAurt1AlnO1HBLiaRymULG1ibJJhXlNjMH1rd1SgQQWIyFBVTRMteWWfiby3FCWfpB7n2oA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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