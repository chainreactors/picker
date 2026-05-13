---
title: codex-lb：用负载均衡的思路管理多个 ChatGPT 账号
url: https://blog.einverne.info/post/2026/05/codex-lb-chatgpt-account-load-balancer.html
source: Verne in GitHub
date: 2026-05-12
fetch_date: 2026-05-13T05:45:52.450712
---

# codex-lb：用负载均衡的思路管理多个 ChatGPT 账号

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

# codex-lb：用负载均衡的思路管理多个 ChatGPT 账号 将多个 ChatGPT 账号汇聚成一个统一的 OpenAI 兼容代理

Posted on 05/12/2026
, Last modified on 05/12/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-05-12-codex-lb-chatgpt-account-load-balancer.md)

用 [[Codex]] CLI 做开发的人大概都遇到过这个场景：手头有几个 ChatGPT 账号，分散在不同的订阅计划里，但工具只认一个账号，额度用完了只能手动切换，每次还要重新登录。更头疼的是，当多人共享一个环境，或者想用同一套配置同时跑 Codex CLI 和 OpenCode 时，账号管理很快就变成了一团乱麻。

[codex-lb](https://github.com/Soju06/codex-lb) 用一个很优雅的思路解决了这个问题：把多个 ChatGPT 账号池化，暴露出一个统一的 OpenAI 兼容接口，所有下游客户端只需要指向这个本地代理就行了。它在 2026 年 1 月创建，目前已经积累了 1077 个 Star 和 40 名贡献者，最新版本是 v1.15.0。

![codex-lb 负载均衡示意图](https://pic.einverne.info/images/2026-05-12-15-00-00-codex-lb-load-balancer.png)

## codex-lb 是什么

简单来说，codex-lb 是一个本地运行的反向代理，它接管所有 AI 客户端的请求，然后按照负载均衡策略分发到不同的 ChatGPT 账号上。对下游客户端（Codex CLI、OpenCode、Python SDK）而言，它就是一个普通的 OpenAI 兼容 API 端点；对上游的 ChatGPT 账号而言，请求自然地分散开来，不会压垮某一个账号的 rate limit。

它的核心功能包括：账号池化负载均衡、每账号的 token 和费用追踪（含 28 天趋势）、Dashboard 管理界面（支持密码 + TOTP 双因素认证）、API Key 系统（支持按 token 量/费用/时间窗口设置速率限制），以及自动从上游同步可用模型列表。这个功能集对于需要协作共享或想精细管控 AI 用量的场景来说相当完整。

## 快速部署

[[Docker]] 是官方推荐的方式，一行命令即可启动：

```
docker volume create codex-lb-data
docker run -d --name codex-lb \
  -p 2455:2455 -p 1455:1455 \
  -v codex-lb-data:/var/lib/codex-lb \
  ghcr.io/soju06/codex-lb:latest
```

启动后访问 `http://localhost:2455`，添加 ChatGPT 账号，就算完成了。端口 2455 是代理服务，1455 是内部通信端口（多副本场景用）。

如果不想用 Docker，也可以直接用 [[uvx]] 运行：

```
uvx codex-lb
```

首次远程访问时需要 bootstrap token 来设置初始密码。服务启动后会在日志里打印这个 token：

```
docker logs codex-lb
# ============================================
#   Dashboard bootstrap token (first-run):
#   <token>
# ============================================
```

用这个 token 登录 Dashboard，设置好密码，之后就走正常的密码 + TOTP 流程。如果是本地访问（localhost），则完全跳过这一步，直接进入 Dashboard。

数据默认存储在 Docker volume 里（`/var/lib/codex-lb/`），本地运行则在 `~/.codex-lb/`，定期备份这个目录即可保留账号和配置。

## 配置下游客户端

添加好 ChatGPT 账号之后，就是让各个 AI 工具把请求指向 codex-lb。不同工具的配置方式略有差异。

**Codex CLI** 的配置最受关注，因为 codex-lb 就是从这个场景出发设计的。在 `~/.codex/config.toml` 里添加一个自定义 provider：

```
model = "gpt-5.3-codex"
model_reasoning_effort = "xhigh"
model_provider = "codex-lb"

[model_providers.codex-lb]
name = "OpenAI"
base_url = "http://127.0.0.1:2455/backend-api/codex"
wire_api = "responses"
supports_websockets = true
requires_openai_auth = true
```

`name = "OpenAI"` 这个字段是必填的，它告诉 Codex CLI 按 OpenAI 协议处理 `/responses/compact` 端点，少了这个 remote compact 功能会失效。如果开启了 API Key 认证，还需要加上 `env_key = "CODEX_LB_API_KEY"` 并设置对应的环境变量。

**OpenCode** 的配置稍微特殊，文档特别提醒不要用自定义 provider，而要覆盖内置的 `openai` provider 的 `baseURL`。原因是自定义 provider 走 Chat Completions API，会丢失 reasoning/thinking 内容，内置 openai provider 走 Responses API，才能正确处理 `encrypted_content` 和多轮推理状态：

```
{
  "provider": {
    "openai": {
      "options": {
        "baseURL": "http://127.0.0.1:2455/v1",
        "apiKey": "{env:CODEX_LB_API_KEY}"
      }
    }
  }
}
```

**OpenAI Python SDK** 则只需要指定 `base_url` 就行，门槛最低：

```
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:2455/v1",
    api_key="sk-clb-...",  # 从 Dashboard 获取，未开启认证时填任意非空字符串
)
```

## API Key 与速率限制

codex-lb 自带一套 API Key 管理系统，在多人共享场景下特别有用。Dashboard 里的 “API Keys” 页面可以创建任意数量的 key，每个 key 可以独立设置：过期时间、允许使用的模型列表、速率限制（按 token 数量、费用上限，支持按日/周/月的时间窗口）。

API Key 认证默认是**关闭**的。本地使用时不需要开启，代理路由（`/v1/*`、`/backend-api/codex/*`）默认只接受来自 localhost 的请求。如果需要通过 Docker 网络、局域网或远程访问，才需要在 Dashboard 的 Settings 里打开 API Key Auth，并让客户端在请求头里带上 `Authorization: Bearer sk-clb-...`。

Key 创建时完整值只显示一次，务必记录下来。

## WebSocket 与流式传输

Codex CLI 在流式输出时可以使用 WebSocket 传输，codex-lb 默认采用 `auto` 模式，会根据请求头和模型类型自动选择 WebSocket 或 HTTP。如果需要强制使用 WebSocket（有时候性能更好），可以设置环境变量：

```
export CODEX_LB_UPSTREAM_STREAM_TRANSPORT=websocket
```

也可以在 Dashboard 的 Settings → Routing → Upstream stream transport 里切换。验证 WebSocket 是否正常工作，可以用 debug 模式运行一次：

```
RUST_LOG=debug codex exec "Reply with OK only."
```

正常情况下日志里应该能看到 `connecting to websocket` 和 `successfully connected to websocket`，同时 codex-lb 的日志显示 `WebSocket /backend-api/codex/responses`，而不是降级的 `POST` 请求。如果 codex-lb 跑在反向代理后面，需要确认反向代理正确转发了 WebSocket upgrade 请求。

## 从直连 OpenAI 迁移

如果之前用的是 Codex CLI 直连 OpenAI，切换到 codex-lb 之后，`codex resume` 看不到旧的会话——因为 Codex 按 `model_provider` 字段过滤历史记录。可以用下面的命令把旧会话的 provider 字段改成 `codex-lb`：

```
# JSONL 格式的会话文件
find ~/.codex/sessions -name '*.jsonl' \
  -exec sed -i '' 's/"model_provider":"openai"/"model_provider":"codex-lb"/g' {} +

# SQLite 状态数据库（>= v0.105.0）
sqlite3 ~/.codex/state_5.sqlite \
  "UPDATE threads SET model_provider = 'codex-lb' WHERE model_provider = 'openai';"
```

## Kubernetes 部署

如果需要在 Kubernetes 集群里运行（比如团队共享环境），codex-lb 提供了官方 Helm chart：

```
helm install codex-lb oci://ghcr.io/soju06/charts/codex-lb \
  --set postgresql.auth.password=changeme \
  --set config.databaseMigrateOnStartup=true \
  --set migration.schemaGate.enabled=false
kubectl port-forward svc/codex-lb 2455:2455
```

多副本场景下，Helm chart 默认使用 headless service DNS 来协调各副本之间的 HTTP session owner handoff，保证同一个对话的请求路由到正确的副本。数据库可以从默认的 SQLite 切换到 PostgreSQL（通过 `CODEX_LB_DATABASE_URL` 环境变量），适合高并发或多副本的生产环境。

Dashboard 认证支持三种模式：标准密码 + TOTP、信任反向代理的 `Remote-User` 请求头（适合接入 Authelia 等认证网关）、以及完全禁用认证（仅限内网隔离场景）。

## 最后

codex-lb 本质上是把运维领域”服务网格”的思路搬进了个人 AI 工具的使用场景：通过统一代理层屏蔽上游账号的差异，让客户端只需要面对一个稳定的接口。从功能完整度来看，Dashboard 的用量可视化、API Key 的细粒度速率控制、多客户端兼容性（[[Codex]]、[[OpenCode]]、OpenAI SDK）以及 Kubernetes 支持，这些都是超出”玩具项目”级别的设计。1077 个 Star 和 40 名活跃贡献者也说明它确实在解决真实需求。

对于个人开发者来说，最直接的价值是：多个 ChatGPT 账号的额度可以无缝轮换，不会因为某个账号触达 rate limit 就中断工作流。对于小团队共享账号的场景，API Key 的用量追踪和配额控制进一步降低了”谁用了多少”的管理成本。如果你手头有两个以上的 ChatGPT 订阅，codex-lb 值得花半小时试试。

## Related Posts

* [本地快速切换 Claude Code 和 Codex CLI 账号的几种方案](/post/2026/05/switch-claude-code-codex-accounts.html) - 05/12/2026
* [codex-lb：用负载均衡的思路管理多个 ChatGPT 账号](/post/2026/05/codex-lb-chatgpt-account-load-balancer.html) - 05/12/2026
* [CLIProxyAPI 把 Claude Code、Gemini CLI、Codex 订阅包装成统一 API 的开源神器](/post/2026/04/cliproxyapi-unified-ai-gateway-for-cli-subscriptions.html) - 04/07/2026
* [SyncTrain：让 iPhone 终于能用上 Syncthing 的开源客户端](/post/2026/03/synctrain-syncthing-ios-client.html) - 03/22/2026
* [推荐我使用的 Agent Skills](/post/2026/01/recommended-agent-skills.html) - 01/19/2026
* [CopilotKit：让你的 React 应用 10 分钟拥有上下文感知的 AI Copilot](/post/2025/12/copilotkit-intro.html) - 12/09/2025
* [利用 AI 来完成实盘交易](/post/2025/10/ai-trading.html) - 10/31/2025
* [搭建 Claude Code 中转服务](/post/2025/09/claude-relay-service.html) - 09/20/2025
* [Codex 使用体验](/post/2025/09/codex.html) - 09/19/2025
* [让 AI 来编写 Git 提交变更信息](/post/2025/06/ai-commits.html) - 06/17/2025

---

* [← Previous（前一篇）](/post/2026/05/cc-switch.html "cc-switch：在多个 AI 编码工具之间优雅切换")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2026/05/socat-command-usage.html "socat：比 netcat 更强大的网络瑞士军刀")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/05/codex-lb-chatgpt-account-load-balancer.html)评论。

* [产品体验 230](/categories.html#产品体验)

* [codex 9](/tags.html#codex)
* [chatgpt 24](/tags.html#chatgpt)
* [openai 28](/tags.html#openai)
* [load-balancer 2](/tags.html#load-balancer)
* [proxy 18](/tags.html#proxy)
* [self-hosted 43](/tags.html#self-hosted)
* [ai-tools 8](/tags.html#ai-tools)
* [open-source 54](/tags.html#open-source)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my...