---
title: CLIProxyAPI 把 Claude Code、Gemini CLI、Codex 订阅包装成统一 API 的开源神器
url: https://blog.einverne.info/post/2026/04/cliproxyapi-unified-ai-gateway-for-cli-subscriptions.html
source: Verne in GitHub
date: 2026-04-07
fetch_date: 2026-04-08T04:30:42.087476
---

# CLIProxyAPI 把 Claude Code、Gemini CLI、Codex 订阅包装成统一 API 的开源神器

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# CLIProxyAPI 把 Claude Code、Gemini CLI、Codex 订阅包装成统一 API 的开源神器 一个代理层，撬动所有 AI CLI 订阅的 API 能力

Posted on 04/07/2026
, Last modified on 04/08/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-04-07-cliproxyapi-unified-ai-gateway-for-cli-subscriptions.md)

最近在折腾自己的 AI 工具链时，我遇到了一个非常现实的痛点。手里同时握着 [[Claude]] Pro、ChatGPT Plus、Gemini Advanced 这几个订阅，每次想在自己的脚本或小工具里调用它们的能力，都只能望洋兴叹——订阅账号给的是网页端或 CLI 工具的使用权，而不是 API Key。如果想走 API 路径，就得额外付一次费，而且 API 的定价往往比订阅贵得多。于是我一直在找一个能把订阅账号的额度转化为 API 调用能力的方案，直到最近发现了 [[CLIProxyAPI]] 这个项目。今天就聊聊这个工具到底解决了什么问题。

![CLIProxyAPI 统一 AI 网关示意图](https://pic.einverne.info/images/cliproxyapi-unified-gateway.png)

## CLIProxyAPI 是什么

简单来说，CLIProxyAPI 是一个代理服务器，它可以把 Gemini CLI、Claude Code、OpenAI Codex、Qwen Code、iFlow、Antigravity 等官方 CLI 工具的 OAuth 登录态包装成 OpenAI、Gemini、Claude、Codex 兼容的 API 接口。听起来有点绕，我换个角度解释一下：当你在本地用 `gemini` 命令或者 `claude` 命令登录官方 CLI 之后，系统会在本地缓存一份 OAuth token，这份 token 的使用额度是走你的订阅账号的。CLIProxyAPI 做的事情，就是在这份 token 上架一个 HTTP 服务，对外暴露标准的 API 接口，让任何支持 OpenAI SDK、Anthropic SDK 或 Google GenAI SDK 的客户端都可以通过这个代理来调用模型。

这个项目由 router-for-me 团队维护，仓库地址是 `github.com/router-for-me/CLIProxyAPI`，使用 Go 语言编写。从 Star 数和 Fork 数来看，这个项目在国内外开发者社区中的关注度相当高，围绕它衍生出的第三方工具已经有十几个，包括 macOS 菜单栏应用 vibeproxy、Claude Code 多账号切换工具 CCS、跨平台管理面板 ProxyPal 等等，形成了一个小而精的生态圈。

## 核心能力

CLIProxyAPI 最核心的能力是协议转换。无论你上游绑定的是哪个家族的 AI 服务，对外暴露的接口都可以是 OpenAI 的 `/v1/chat/completions`、Anthropic 的 `/v1/messages`、Google 的 `/v1beta/models/...` 或者 Codex 的 `/v1/responses` 格式。这意味着你可以用 OpenAI 的 SDK 去调用 Claude Sonnet 4.5，也可以用 Anthropic 的 SDK 去调用 Gemini 3 Pro，协议层由代理自动翻译。对于那些希望在不同模型之间做 A/B 测试、或者希望把多家模型聚合进同一个应用的开发者来说，这个特性非常实用。

多账号轮询和负载均衡是另一个让人眼前一亮的功能。项目支持为 Gemini、OpenAI、Claude、Qwen 和 iFlow 配置多个 OAuth 账号，代理会以 round-robin 的方式自动在多个账号之间分配请求。对于免费额度有限的场景，多账号聚合可以有效拉高整体的可用配额；对于有多台订阅的企业用户或团队来说，这个功能直接解决了账号管理的头疼问题。特别是 Gemini CLI 的免费额度相当慷慨，绑定几个 Google 账号就能获得相当可观的 Gemini 2.5 Pro 免费调用量。

在模型支持方面，CLIProxyAPI 目前覆盖的列表相当全面。[[Gemini]] 系列包括 gemini-3-pro-preview、gemini-3-pro-image-preview、gemini-2.5-pro、gemini-2.5-flash 等多个版本，甚至支持 gemini-2.5-flash-image 这类多模态图像生成模型。[[OpenAI]] 这边覆盖了 gpt-5 和 gpt-5-codex。[[Anthropic]] 的 Claude 系列从 claude-opus-4-1、claude-sonnet-4-5 到 claude-haiku-4-5 都在支持范围内。此外还包括阿里的 qwen3-coder-plus、qwen3-max 系列，DeepSeek 的 deepseek-v3.2 和 deepseek-r1，Moonshot 的 kimi-k2，智谱的 glm-4.6 等国产大模型，甚至还能接入 OpenAI 兼容的上游服务商比如 [[OpenRouter]]。这个列表几乎涵盖了当下所有主流的闭源大模型。

OAuth 认证流程是这个项目的灵魂所在。当你在命令行运行认证命令时，CLIProxyAPI 会启动一个本地 HTTP 服务器接收 OAuth 回调，整个流程跟官方 CLI 工具的登录体验几乎一模一样。认证完成后，token 会被加密保存在本地配置目录中，之后所有的 API 调用都会自动使用这份 token。对于 Gemini 还支持传统的 Generative Language API Key 方式，如果你有 AI Studio 的 Key 也可以直接配置进去。

其他值得一提的能力包括流式响应和非流式响应两种模式、Function Calling/Tools 支持、多模态输入（文本+图像）、以及对 Amp CLI 和 IDE 扩展的原生适配。流式响应对于构建聊天界面来说是刚需，而 Tools 支持则让你可以在本地跑起像 [[Agent]] 这样的复杂工作流。

## 实际使用场景

从我这几天的体验来看，CLIProxyAPI 最直接的应用场景是让订阅账号释放出更多价值。举个例子，我平时订阅了 ChatGPT Plus 和 Claude Pro，这两个订阅加起来每月大约 40 美元。在没有 CLIProxyAPI 之前，我只能在官方客户端里使用这些模型；有了它之后，我可以把这两个订阅的额度打通给本地的开发工具链，比如在自己写的知识库摘要脚本里调用 Claude Sonnet 4.5，在自动化翻译流水线里调用 GPT-5，完全不需要额外的 API Key。虽然官方的订阅额度也有限，但对于个人项目和日常自动化任务来说，这些额度已经相当够用了。

另一个让我觉得非常实用的场景是与本地 AI 工具的集成。像 [[Cline]]、Roo Code、[[Cursor]] 这些 AI 编程助手都支持配置自定义的 OpenAI 兼容端点，我只要把 CLIProxyAPI 的地址填进去，就可以在这些工具里无缝使用自己订阅的 Claude Code 或 GPT-5 额度。这种组合方式彻底改变了我的开发流程，因为我不再需要为每一个 AI 工具都单独购买 API 额度，所有的 AI 能力都可以汇集到一个统一的代理入口。

对于国内开发者来说，CLIProxyAPI 还有一个隐性的好处，就是它可以作为网络层的统一出口。你只需要保证 CLIProxyAPI 所在的服务器能够稳定访问 OpenAI、Anthropic、Google 这些上游服务，本地客户端只要能连接到 CLIProxyAPI 就行。这种部署方式对于那些在网络受限环境下工作的团队来说非常友好。

团队共享账号也是一个值得讨论的场景。如果你所在的小团队有一个共享的 Claude Max 或 ChatGPT Team 订阅，通过 CLIProxyAPI 部署一个内部服务，大家就可以通过 API 的方式共享使用这个订阅，配合多账号轮询还可以进一步扩大可用配额。当然，这里需要注意订阅服务商的使用协议，避免违反相关条款。

## 部署与配置经验

这篇文章最早写出来的时候，我对安装部分写得还是太“概念型”了，像是在告诉你“它不难装”，而不是告诉你“到底怎么装”。我重新看了一遍 CLIProxyAPI 官方 quick start 之后，发现最稳的上手方式其实非常清晰：先准备一份最小配置，再选一种安装路径，完成 OAuth 登录，最后把下游工具指向这个代理。你只要按这个顺序走，第一次跑通不会太费劲。

我自己的建议是，第一次不要同时折腾 Claude、Gemini、Codex 三家账号，也不要一上来就配管理面板、模型别名、多账号轮询。先让单账号、单 provider 跑通，再慢慢往上加。CLIProxyAPI 的功能面很宽，但它真正容易让人卡住的，其实是第一次“配置、登录、启动、验证”这四步没串起来。

### 先准备一份最小配置

不管你用 [[Homebrew]]、[[Docker]] 还是源码编译，最终都要落回一个 `config.yaml`。官方 `config.example.yaml` 很长，第一次看容易有点吓人，但本地自用其实只需要一份极简配置就能启动：

```
host: "127.0.0.1"
port: 8317

remote-management:
  allow-remote: false
  secret-key: "change-this-management-key"

auth-dir: "~/.cli-proxy-api"

api-keys:
  - "local-dev-key"

debug: false
```

这份配置里，`host: "127.0.0.1"` 的意义非常大，它会把服务限制在本机监听，避免你在没做好鉴权之前就把代理直接暴露到局域网甚至公网。`auth-dir` 是 OAuth 凭证保存目录，Gemini、Claude、Codex 这些登录态最后都会落到这里。`api-keys` 则是你给下游客户端使用的访问令牌；比如 [[Claude Code]]、[[Codex]]、[[Gemini CLI]] 或者你自己的脚本在访问 CLIProxyAPI 时，就可以用这个 key 做最基本的请求鉴权。至于 `remote-management.secret-key`，如果你希望开启管理 API 和管理面板，这个值就不要留空；官方文档说它在启动时会自动哈希回写，所以填明文即可。

### 安装方式其实有好几种

从官方 quick start 来看，CLIProxyAPI 目前把主流安装路径都准备好了。

如果你在 macOS 上，最轻松的方式就是直接用 [[Homebrew]]：

```
brew install cliproxyapi
brew services start cliproxyapi
```

这里有一个官方文档里提到但很多人第一次会忽略的细节：如果你是通过 `brew services` 跑服务，默认配置文件路径不是 `~/.cli-proxy-api/config.yaml`，而是 `$(brew --prefix)/etc/cliproxyapi.conf`。如果你更喜欢把所有配置和登录态都统一放在 `~/.cli-proxy-api/` 目录里，官方给的做法是把默认路径软链接过去：

```
brew services stop cliproxyapi
mv "$(brew --prefix)/etc/cliproxyapi.conf" "$(brew --prefix)/etc/cliproxyapi.conf.bak"
ln -s ~/.cli-proxy-api/config.yaml "$(brew --prefix)/etc/cliproxyapi.conf"
brew services start cliproxyapi
```

如果你在 Linux 上，官方 quick start 给了一个一键安装脚本：

```
curl -fsSL https://raw.githubusercontent.com/brokechubb/cliproxyapi-installer/refs/heads/master/cliproxyapi-installer | bash
```

如果你用的是 Arch，也可以直接从 AUR 安装，然后交给 [[systemd]] 用户服务管理：

```
yay -S cli-proxy-api-bin

mkdir -p ~/.cli-proxy-api
cp /usr/share/doc/cli-proxy-api-bin/config.example.yaml ~/.cli-proxy-api/config.yaml
systemctl --user start cli-proxy-api
systemctl --user enable cli-proxy-api
```

如果你喜欢容器化部署，官方提供的 [[Docker]] 路径也很直接，而且很适合把服务放到一台单独的机器上长期运行。最基本的启动命令就是：

```
docker run --rm -p 8317:8317 \
  -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml \
  -v /path/to/your/auth-dir:/root/.cli-proxy-api \
  eceasy/cli-proxy-api:latest
```

最后一种就是源码编译。官方 quick start 给出的命令也非常朴素：

```
git clone https://github.com/router-for-me/CLIProxyAPI.git
cd CLIProxyAPI
go build -o cli-proxy-api ./cmd/server
```

如果你走这条路，后面的登录命令和启动命令里，把 `cliproxyapi` 替换成你自己的可执行文件路径就行，比如 `./cli-proxy-api`。

如果你在 Windows 上，官方 quick start 给的路径更直接：下载最新 release 二进制或者桌面 GUI 应用，直接运行即可。对不想自己维护服务进程和配置文件路径的人来说，GUI 包装版反而会更省事。

### OAuth 登录要分 provider 单独做

CLIProxyAPI 不会替你自动“继承”本机已经登录好的官方 CLI 状态，它有自己的一套 OAuth 登录流程，会把拿到的凭证保存到 `auth-dir`。这一步其实就是整个安装流程里最关键的一步。

官方 provider 文档里给的命令很明确。Gemini CLI 的 OAuth 登录用：

```
cliproxyapi --login
```

如果你是已经在用 Gemini Code 的老用户，官方还建议必要时显式带上 `--project_id`：

```
cliproxyapi --login --project_id <your_project_id>
```

Gemini 的本地 OAuth 回调默认走 `8085` 端口。Codex 的登录命令是：

```
cliproxyapi --codex-login
```

它的本地回调端口是 `1455`。[[Claude Code]] 的登录命令则是：

```
cliproxyapi --claude-login
```

它的本地回调端口是 `54545`。这几个登录命令都支持 `--no-browser` 参数，也就是不自动拉起浏览器，而是直接把登录 URL 打印出来。如果你是在远程服务器、SSH、或者没有图形界面的环境里部署，这个参数会很有用。

如果你用 Docker 跑登录，官方文档也给了对应写法。比如 Gemini OAuth：

```
docker run --rm -p 8085:8085 \
  -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml \
  -v /path/to/your/auth-dir:/root/.cli-proxy-api \
  eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --login
```

Codex 和 Claude 也是同一个思路，只是把端口和参数换成 `1455 + --codex-login`、`54545 + --claude-login`。如果你计划长期用 Docker 部署，这里一定要把 `auth-dir` 做成持久化挂载，不然容器删掉之后登录态也会一起没掉。

### 启动服务之后，先做一次最小验证

很多人卡在这里，是因为登录做完了，但并没有立刻验证“代理是否真的已经在工作”。我的建议是，启动服务之后，先不要急着接 [[Cline]]、[[Cursor]]、Roo Code 这些复杂客户端，而是先用最简单的方式验证...