---
title: Sub2API：把 Claude/Gemini/GPT 订阅变成 API
url: https://mp.weixin.qq.com/s/TljNV8GKqz356HtHfBJQ7A
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:05.113424
---

# Sub2API：把 Claude/Gemini/GPT 订阅变成 API

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp03lNgAfWQgibfOlecsy1InueOPKnXngfDAREomeicwCKbO9VjNB4EP9tq7wnuW9IZXOGJc4b4mtTxt3ibF9Y5C47JypjE1lD9lPic8/0?wx_fmt=jpeg)

# Sub2API：把 Claude/Gemini/GPT 订阅变成 API

原创

攻防路
攻防路

攻防录

![]()

在小说阅读器中沉浸阅读

项目地址：https://github.com/Wei-Shaw/sub2api

在线体验：https://demo.sub2api.org/

---

订了 Claude Pro，只有自己用有点浪费；几个人一起用，又没法共享账号。这是很多人碰到的问题。

Sub2API 的思路是把这件事从账号层解决——上游是你的订阅账号，下游是标准 API Key。你把 API Key 分发给需要的人，每个人用自己的 Key 调用，平台在中间处理鉴权、计费和请求转发。本质上是把订阅的配额通过网关的方式分发出去。

截至 2026 年 3 月，项目在 GitHub 已有超过 9.5k Star，累计发布 94 个版本，最新版本 v0.1.106 于 2026 年 3 月 30 日发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp022kqepJldMS0tL0YkfwTL4JXnuXjgKsUDmoK8M1cGLIN46OOibZRlO1JDwNfoicNCNlic4JYOrAVSgmktFGbicibjfPdaFy7lteZy8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp00zSel7A17E3Woe6iaDLudZAiaicoXfrTL0IqnANrLl9gcUiagOicTIrCqFBfElXG3RMhLibkrIRa16JO5DsUzK52mfzaKc1DU7zVIr8/640?wx_fmt=png&from=appmsg)

Sub2API Logo

## 网关怎么工作

Sub2API 的核心是一个 AI API 网关，支持 Claude、OpenAI、Gemini、Antigravity 这几类上游。

整个流程是这样的：管理员在后台录入上游账号（支持 OAuth 和 API Key 两种接入方式），平台生成多个 API Key 分发给用户。用户拿着 Key 发请求，平台接到之后选一个可用的上游账号转发出去，响应原路返回。

中间层做了这些事：

**Token 级计费**：不是按次数算，是真正解析响应里的 Token 数量，按实际消耗计费。对管理员来说，能比较准确地知道每个用户用了多少。

**粘性会话（Sticky Session）**：同一个对话，会尽量路由到同一个上游账号。这对 Claude 这类有多账号时上下文不互通的情况很关键，不然同一段对话被路由到不同账号，Claude 会失忆。

**细粒度并发控制**：支持每个用户设并发上限，也支持每个上游账号设并发上限，防止单个账号被打爆或某个用户占满资源。

**分组隔离**：同一平台上可以建多个账号分组。比如把 Anthropic 订阅和 Antigravity 账号分开放，避免调度时混用（Claude 的不同来源上下文不互通，混用会出问题）。

各模式对比：

| 使用方式 | 多人共享 | 计费追踪 | 原生工具支持 | 管理成本 |
| --- | --- | --- | --- | --- |
| 直接共享账号密码 | ✅ | ❌ | ✅ | 高（账号安全风险大） |
| 三方中转服务 | ✅ | 部分 | 部分 | 低（但依赖第三方） |
| Sub2API 自建 | ✅ | ✅ Token 级 | ✅ | 中（需维护服务器） |

---

## Antigravity 接入

Sub2API 支持 Antigravity 账号接入，授权后可用专用端点访问：

* `/antigravity/v1/messages`：Claude 模型
* `/antigravity/v1beta/`：Gemini 模型

配合 Claude Code 使用时，设两个环境变量就行：

```
export ANTHROPIC_BASE_URL="http://localhost:8080/antigravity"
export ANTHROPIC_AUTH_TOKEN="sk-xxx"
```

Antigravity 账号还支持混合调度：开启后，普通端点 `/v1/messages` 也会把请求路由到 Antigravity 账号，当 Anthropic 原生账号不够用时自动补位。但要注意，Anthropic Claude 和 Antigravity Claude 的上下文不能混用，需要通过分组做好隔离，否则同一段对话会乱。

另外有个已知问题：在 Claude Code 里用 Antigravity 账号时，Plan Mode 完成后不会自动弹出确认选项。解决办法是手动按 Shift + Tab 退出 Plan Mode，再告诉 Claude Code 同意或拒绝。

---

## 三种部署方式

### 脚本一键安装（Linux）

需要事先装好 PostgreSQL 15+ 和 Redis 7+，然后一行命令：

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

脚本会自动检测架构（amd64/arm64）、下载二进制、注册 systemd 服务。装完之后打开 `http://服务器IP:8080` 跑一遍设置向导配数据库和管理员账号就行。

升级不用手动操作，管理后台左上角有「检测更新」按钮，点一下自动拉最新版。

### Docker Compose（推荐）

不想手动装数据库，Docker Compose 版本把 PostgreSQL 和 Redis 都打包进来了：

```
mkdir -p sub2api-deploy && cd sub2api-deploy
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
docker compose up -d
```

部署脚本会自动生成 JWT\_SECRET、TOTP\_ENCRYPTION\_KEY、POSTGRES\_PASSWORD 这几个安全凭证，创建好本地数据目录。推荐用 `docker-compose.local.yml` 版本——数据放本地目录，备份和迁移直接打包整个目录就行。

迁移到新服务器也很简单：

```
# 旧服务器
docker compose -f docker-compose.local.yml down
tar czf sub2api-complete.tar.gz sub2api-deploy/
scp sub2api-complete.tar.gz user@new-server:/path/

# 新服务器
tar xzf sub2api-complete.tar.gz
cd sub2api-deploy/
docker compose -f docker-compose.local.yml up -d
```

### 源码编译

Go 1.21+、Node.js 18+ 的环境，编译也不复杂。前端用 pnpm 构建，后端加 `-tags embed` 把前端打进二进制：

```
cd frontend && pnpm install && pnpm run build
cd ../backend && go build -tags embed -o sub2api ./cmd/server
```

注意一个细节：如果 Nginx 反向代理后接 Codex CLI，需要在 Nginx 的 `http` 块里加一行：

```
underscores_in_headers on;
```

Nginx 默认会丢弃带下划线的请求头，`session_id` 就是这类，丢了就没有粘性会话了。

---

## 简易模式

项目有个「简易模式」，设环境变量 `RUN_MODE=simple` 启动，会把 SaaS 相关的功能（计费、用户管理等）隐藏掉，适合个人或内部小团队快速用，不想搭一整套计费体系的场景。

生产环境要同时设 `SIMPLE_MODE_CONFIRM=true` 才能启动，防止误用。

---

## 技术栈

| 组件 | 技术 |
| --- | --- |
| 后端 | Go 1.25.7，Gin，Ent |
| 前端 | Vue 3.4+，Vite 5+，TailwindCSS |
| 数据库 | PostgreSQL 15+ |
| 缓存/队列 | Redis 7+ |

Go 做网关性能够用，Ent 做 ORM 类型安全，Vue 3 + TailwindCSS 出来的管理界面比较干净。

---

## 生态

围绕 Sub2API 社区已经有了两个扩展项目：

**Sub2ApiPay**（https://github.com/touwaeriol/sub2apipay）：做自助充值的，兼容易支付协议、微信支付、支付宝、Stripe，支持 iframe 嵌进管理后台。

**sub2api-mobile**（https://github.com/ckken/sub2api-mobile）：跨平台移动端控制台，iOS/Android/Web 都能用，基于 Expo + React Native，支持用户管理、监控看板、多后端切换。

---

免责声明：使用本项目可能涉及 Anthropic 等平台服务条款，使用前请自行评估合规风险。

欢迎关注“攻防录”✨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

攻防录

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

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