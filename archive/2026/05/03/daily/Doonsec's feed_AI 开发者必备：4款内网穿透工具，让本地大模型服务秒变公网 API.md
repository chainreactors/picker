---
title: AI 开发者必备：4款内网穿透工具，让本地大模型服务秒变公网 API
url: https://mp.weixin.qq.com/s/BvzX_UFTvxeRhOpgpuiNzg
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:29:13.643550
---

# AI 开发者必备：4款内网穿透工具，让本地大模型服务秒变公网 API

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9laT0icEalUIzNnUqAmwhal80xiaq5y4fKjzaOwhsAkOD83mHMsFjrCfAl8ANYHVX7AHLxGVu1DhpFYEMicnoRdMcSPib7n55BKufUBoUW04TNE/0?wx_fmt=jpeg)

# AI 开发者必备：4款内网穿透工具，让本地大模型服务秒变公网 API

原创

薛小蛮
薛小蛮

AI安全手记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#### 概述

AI 开发中，我们经常需要将本地部署的大模型服务（如 Ollama、vLLM）暴露给外部调用，但本地服务只能通过 localhost 访问，无法提供 API 给前端或第三方。内网穿透工具可以**一条命令将本地 AI 服务暴露到公网**，无需服务器、无需公网IP，极大简化开发调试流程。

本文介绍4款主流内网穿透工具，从零配置到生产级方案，帮你选择最适合的方案。

#### 核心痛点

* **本地大模型服务无法外网调用**：Ollama、vLLM 等本地部署的大模型只能 localhost 访问，无法提供 API 给前端或第三方
* **Webhook 调试困难**：AI 应用的回调接口、第三方 AI 平台联调需要公网地址
* **演示不便**：临时给客户演示 AI 能力需要部署到服务器，流程繁琐
* **成本高昂**：购买 GPU 服务器只为临时测试，资源浪费严重

#### 支持协议

* HTTP/HTTPS：REST API、Web 界面
* WebSocket：实时对话、流式输出
* TCP：数据库、Redis、SSH
* UDP：实时语音、游戏服务器

---

#### 方案一：localhost.run — 最简 SSH 隧道

**官网**：https://localhost.run/

**概念**：基于 SSH 远程端口转发（-R 参数）的纯命令行隧道服务，无需安装任何软件。通过 SSH 协议建立加密隧道，将本地端口映射到公网。

**支持协议**：HTTP、HTTPS、TCP

**国内速度**：

* 延迟：无法连接（测试超时）
* 稳定性：❌ 不稳定
* 说明：服务器在国外，国内访问受限

**使用方法**：

* 1
* 2
* 3
* 4
* 5

```
# 映射本地 AI API 服务ssh -R 80:localhost:11434 localhost.run
# 映射本地数据库ssh -R 3306:localhost:3306 localhost.run
```

**典型 AI 场景**：

* 本地 Ollama 大模型 API 临时分享
* 本地 AI 应用调试
* 本地数据库远程访问

**优点**：

* ✅ 零配置，系统自带 SSH 即可
* ✅ 一条命令搞定
* ✅ 支持 TCP 协议

**缺点**：

* ❌ 国内访问不稳定，延迟高
* ❌ 免费版子域名几小时后变化
* ❌ 速度和带宽有限制

**价格**：

* 免费版：临时子域名
* 付费版：$9/月，支持自定义域名

---

#### 方案二：pinggy.io — 带调试面板的 SSH 隧道

**官网**：https://pinggy.io/

**概念**：基于 SSH 反向隧道，提供终端交互界面，可查看请求日志和带宽统计。适合需要实时查看请求详情的调试场景。

**支持协议**：HTTP、HTTPS、TCP、UDP

**国内速度**：

* 延迟：220-225ms
* 稳定性：✅ 基本稳定
* 说明：延迟较高，但可以正常使用

**使用方法**：

* 1
* 2
* 3
* 4
* 5

```
# 映射本地 AI API 服务ssh -p 443 -R0:localhost:11434 qr@free.pinggy.io
# 映射本地 AI 应用ssh -p 443 -R0:localhost:8000 qr@free.pinggy.io
```

**典型 AI 场景**：

* AI Webhook 回调调试
* 第三方 AI 平台接口联调
* 实时查看 AI 请求日志

**优点**：

* ✅ 零配置，系统自带 SSH 即可
* ✅ 提供调试面板和请求日志
* ✅ 免费版 URL 7 天内有效
* ✅ 支持 UDP 协议

**缺点**：

* ❌ 国内延迟 220ms 左右
* ❌ 60 分钟超时限制
* ❌ 随机子域名
* ❌ 访问时有品牌页

**价格**：

* 免费版：7 天有效 URL
* 付费版：持久隧道、自定义域名

---

#### 方案三：InstaTunnel — 免费自定义子域名

**官网**：https://instatunnel.my/

**概念**：基于 Node.js 的轻量隧道客户端，免费版即支持自定义子域名。适合需要稳定域名的临时分享场景。

**支持协议**：HTTP、HTTPS、WebSocket

**国内速度**：

* 延迟：230-235ms
* 稳定性：✅ 基本稳定
* 说明：延迟较高，但可以正常使用

**安装使用**：

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8

```
# 安装npm install -g instatunnel
# 映射本地 AI API 服务instatunnel 11434 --subdomain my-ollama
# 映射本地 AI 应用instatunnel 8000 --subdomain my-ai-app
```

**典型 AI 场景**：

* 本地 AI 项目演示给客户
* 前端 AI 应用实时预览
* WebSocket AI 对话测试

**优点**：

* ✅ 免费支持自定义子域名
* ✅ 会话可持续 24 小时以上
* ✅ 支持 3 条同时隧道
* ✅ 支持 WebSocket（适合 AI 流式输出）

**缺点**：

* ❌ 国内延迟 230ms 左右
* ❌ 需要安装 Node.js
* ❌ 无付费版（功能受限）
* ❌ 不支持纯 TCP

**价格**：免费

---

#### 方案四：Cloudflare Tunnel — 生产级内网穿透

**官网**：

Cloudflare Tunnel 文档

[https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/

**概念**：Cloudflare 企业级隧道服务，自动提供 HTTPS 和 DDoS 防护。通过 cloudflared 客户端在本地服务与 Cloudflare 全球边缘网络之间建立加密的出站连接。

**支持协议**：HTTP、HTTPS、WebSocket、TCP、UDP、SSH、RDP

**国内速度**：

* 延迟：175-180ms
* 稳定性：✅ 稳定（有丢包风险）
* 说明：延迟最低，但偶有丢包，适合生产环境

**安装方法**：

macOS：

* 1
* 2
* 3
* 4
* 5
* 6

```
# 使用 Homebrew 安装（推荐）brew install cloudflared
# 或者下载安装包curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz | tar xzsudo mv cloudflared /usr/local/bin/
```

Linux (Ubuntu/Debian)：

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8

```
# 添加 Cloudflare GPG 密钥wget -q https://packages.cloudflare.com/cloudflare-main.gpg -O- | sudo tee /usr/share/keyrings/cloudflare-main.gpg
# 添加软件源echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://packages.cloudflare.com/debian stable main" | sudo tee /etc/apt/sources.list.d/cloudflare.list
# 安装sudo apt update && sudo apt install cloudflared
```

Linux (CentOS/RHEL)：

* 1
* 2
* 3

```
# 添加 Cloudflare 仓库curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-x64.rpm -o cloudflared.rpmsudo rpm -i cloudflared.rpm
```

Windows：

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10

```
# 使用 winget 安装（推荐）winget install Cloudflare.cloudflared
# 或者使用 Chocolateychoco install cloudflared
# 或者手动下载# 访问 https://github.com/cloudflare/cloudflared/releases/latest# 下载 cloudflared-windows-amd64.exe 并重命名为 cloudflared.exe# 将其放入 PATH 目录中
```

**验证安装**：

* 1

```
cloudflared --version
```

**使用方法**：

方式一：快速临时分享（无需账号）

* 1
* 2
* 3
* 4
* 5

```
# 将本地 AI API 映射到公网cloudflared tunnel --url http://localhost:11434
# 执行后会生成临时地址，如：# https://random-words.trycloudflare.com
```

方式二：正式使用（需 Cloudflare 账号和自有域名）

第一步：登录认证

* 1
* 2

```
cloudflared tunnel login# 浏览器会打开授权页面，选择要使用的域名
```

第二步：创建隧道

* 1
* 2

```
cloudflared tunnel create my-ai-tunnel# 记录返回的隧道 ID
```

第三步：配置路由

创建配置文件 `~/.cloudflared/config.yml`：

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9

```
tunnel: <隧道ID>credentials-file: /home/用户名/.cloudflared/<隧道ID>.json
ingress:  - hostname: api.你的域名.com    service: http://localhost:11434  - hostname: app.你的域名.com    service: http://localhost:8000  - service: http_status:404
```

第四步：启动隧道

* 1

```
cloudflared tunnel run my-ai-tunnel
```

第五步：配置 DNS

* 1

```
cloudflared tunnel route dns my-ai-tunnel api.你的域名.com
```

**典型 AI 场景**：

* 生产环境 AI API 服务暴露
* 远程访问内网 GPU 服务器
* 企业级 AI 应用部署

**优点**：

* ✅ 国内延迟最低（175ms）
* ✅ 自动 HTTPS 和 DDoS 防护
* ✅ 无需公网 IP
* ✅ 适合生产环境
* ✅ 免费版功能强大
* ✅ 支持所有协议（包括 WebSocket 流式输出）

**缺点**：

* ❌ 需要安装客户端
* ❌ 需要自有域名（托管在 Cloudflare）
* ❌ 配置相对复杂
* ❌ 偶有丢包

**价格**：

* 免费版：适合开发和小型生产
* 企业版：更高性能、优先支持

---

#### 国内速度实测对比

| 服务 | 延迟 | 稳定性 | 是否可用 | 推荐指数 |
| --- | --- | --- | --- | --- |
| localhost.run | 无法连接 | ❌ 不稳定 | ❌ 不可用 | ⭐ |
| pinggy.io | 220-225ms | ✅ 基本稳定 | ✅ 可用 | ⭐⭐⭐ |
| InstaTunnel | 230-235ms | ✅ 基本稳定 | ✅ 可用 | ⭐⭐⭐ |
| Cloudflare Tunnel | 175-180ms | ✅ 稳定 | ✅ 可用 | ⭐⭐⭐⭐⭐ |

> 测试环境：国内服务器，测试时间：2026-05-02
> 说明：延迟数据仅供参考，实际速度可能因网络环境而异

---

#### 总结对比

| 服务 | 安装需求 | 支持协议 | 域名支持 | 免费版限制 | 适合场景 |
| --- | --- | --- | --- | --- | --- |
| localhost.run | 无需安装 | HTTP/HTTPS/TCP | 临时子域名（几小时） | 域名临时、速度限制 | 不推荐国内使用 |
| pinggy.io | 无需安装 | HTTP/HTTPS/TCP/UDP | 7 天内有效 | 60 分钟超时、品牌页 | 调试面板测试 |
| InstaTunnel | 需 Node.js | HTTP/HTTPS/WebSocket | 自定义子域名 | 3 条隧道、24h+ 会话 | 稳定子域名分享 |
| Cloudflare Tunnel | 需 cloudflared | 全协议 | 自定义域名 | 需自有域名 | 生产级 AI 服务 |

---

#### AI 开发者选择建议

| 场景 | 推荐服务 | 理由 |
| --- | --- | --- |
| 临时调试 AI API | pinggy.io | 零配置，有调试面板 |
| AI 项目演示 | InstaTunnel | 免费自定义子域名，支持 WebSocket |
| 生产级 AI 服务 | Cloudflare Tunnel | 延迟最低，支持全协议，适合流式输出 |
| 大模型 API 暴露 | Cloudflare Tunnel | 稳定性最好，支持高并发 |
| WebSocket AI 对话 | Cloudflare Tunnel 或 InstaTunnel | 原生支持 WebSocket |

---

#### 注意事项

* ⚠️ localhost.run 国内无法访问，不推荐使用
* ⚠️ 免费服务都有时长/带宽限制，仅适合临时测试
* ⚠️ 生产环境推荐 Cloudflare Tunnel
* ⚠️ 敏感数据传输建议使用 HTTPS 加密
* ⚠️ AI 流式输出建议使用 WebSocket 协议

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LRFSic7veEzMqVJNmcur1bB6X9yRWib4MgN6I5hxOuibaS7NI9TK9ibt9CdoXIGeeujdFG5W76AEbibO8MhqWzibRP6A/0?wx_fmt=png)

AI安全手记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LRFSic7veEzMqVJNmcur1bB6X9yRWib4MgN6I5hxOuibaS7NI9TK9ibt9CdoXIGeeujdFG5W76AEbibO8MhqWzibRP6A/0?wx_fmt=png)

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