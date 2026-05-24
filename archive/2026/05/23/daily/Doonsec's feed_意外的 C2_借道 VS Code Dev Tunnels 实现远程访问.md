---
title: 意外的 C2:借道 VS Code Dev Tunnels 实现远程访问
url: https://mp.weixin.qq.com/s/dDg75NqJIuIv4FHQd_nwKA
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:28.664235
---

# 意外的 C2:借道 VS Code Dev Tunnels 实现远程访问

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSiayqLgoqV7RTQ4BcBXC1xGm2Ij1hNQ3Y3iboO7ssk6mXPiaMo5N19cPMJWnV4H68F2haZdiaOC1x3qVLdicKz4a87zWc2vPyrNzEYg/0?wx_fmt=jpeg)

# 意外的 C2:借道 VS Code Dev Tunnels 实现远程访问

Adam Chester
Adam Chester

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://blog.xpnsec.com/accidental-c2/ | XPN / Adam Chester |

我是在从曼彻斯特飞往 JFK 的航班上开始写这篇博客文章的。每当我出行时，我通常会从研究待办清单中挑出一个小项目，戴上耳机，把世界隔绝在外，直到飞机降落。这趟旅程也不例外，给了我大约 7 小时的时间专注于一个困扰我已久的话题 —— Visual Studio Code Dev Tunnels。

其他人已经尝试过用 dev tunnels 来代理 C2 流量，但 VS Code 本身可以执行远程 shell 命令并搬运文件。所以底层一定有某些东西在红队评估中是有用的。

通常我不会尝试在跨大西洋航班上启动这样的项目，主要是因为 dev tunnels 严重依赖稳定的网络连接 (而大多数时候，£25 的机上 Wi-Fi 连接感觉就像 IPoAC)。但这次，我有一个新的依靠来应对这种不稳定性。

## 放飞 Bishop

"Bishop"(以《异形》中的机器人科学官命名) 是我新搭建的 LLM 工作机。它是一台基础款的 M4 Mac mini，唯一的任务就是远程处理长时间运行的 Claude Code、Codex 和 OpenCode 会话。

我的想法是，通过远程启动新任务来缓解不稳定的 Wi-Fi 问题，让 LLM 在后台埋头工作，等网络恢复时再拉回一份精炼的报告。

于是我从一个简单的 prompt 开始：

```
I am creating a research-project into VS Code Dev Tunnels. Primarily the goals of this research will be:

1. Create a standalone tool which will allow me to list/add/interact with existing dev-tunnels
2. Interact with existing authentication tokens (Azure/GitHub) to view existing tunnels and interact with them

First I need to understand how they work under the hood. This will be imperative to understanding how my research will go.

The repo is at: https://github.com/microsoft/vscode.git

First take a clone of this and start exploring, looking for answers to the above.

Other resources which may be useful:

* https://github.com/microsoft/dev-tunnels.git - Dev Tunnels source
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSglh9cZI4IeZsWibj257GGjfaspYia2Kjwc81UyFE5qMl9siaSd4BXGUDLT5j7gqC10kvuD2MK2S6uVQ12owIwoLo5EWVv64xRrCw/640?wx_fmt=other&from=appmsg)

令人惊讶的是，在调用 `GPT-5.4-Cyber`模型后，几分钟内就返回了一份初始报告，让我对 Dev Tunnels 协议的工作原理以及相关代码段的位置有了一个良好的概览。

如果你感兴趣，可以在这里查看初始报告。

随后又生成了进一步的迭代和代码示例，这同样意味着在我专注于研究的同时，其他 agent 正在后台对任务进行迭代。

## VS Code Dev Tunnels 的分层结构

Dev Tunnels 在 VS Code 中已经存在一段时间了。你通常会在侧边栏的 Remote Explorer 中看到它们：

![](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSia7BjDFW5HLmAEC961yj7eStJaiciavNGu8rHI5hmDsvPqjJlQrsXJJQUzgXdNxiaq8pPRm5gHzoP5xaM16yic4wk64h1pvLuWicnNo/640?wx_fmt=other&from=appmsg)

你或许会以为这项功能的底层实现相当简单。毕竟，你本质上是在两台主机之间建立一条 HTTP 隧道，而我们知道 Microsoft 有好几款用于隧道传输的产品，这能有多难呢？

遗憾的是，Microsoft 的 dev tunnels 实际上是多层次、而且相当不标准的，这意味着为了理解这一切是如何运作的，我不得不与 Bishop 一起逐层剖析。

我发现最简单的处理方式是从客户端到服务器的连接流程开始，逐层重建。所以让我们从 VS Code 如何搜索现有隧道开始，逐层深入，直到我们抵达代码执行环节。

## Layer 0 - REST 管理

当连接到现有的 dev-tunnel 时，VS Code 需要了解有哪些现有的服务器可用。这是通过向一个标准的 JSON REST 端点发送 GET 请求来完成的：

```
GET /tunnels?includePorts=true&labels=vscode-server-launcher&allLabels=true&global=true&api-version=2023-09-27-preview HTTP/1.1
Host: global.rel.tunnels.api.visualstudio.com
Authorization: github gho_GITHUB_TOKEN_HERE
User-Agent: vscode.dev.remote-server Dev-Tunnels-Service-TypeScript-SDK/1.2.1
```

响应随后提供了我们可用的隧道范围的信息：

```
HTTP/1.1 200 OK
...
{
"value": [{
"regionName": "UkSouth",
"value": [{
"clusterId": "uks1",
"tunnelId": "wild-fog-s1alk0t",
"name": "",
"description": "",
"labels": ["prometheus", "protocolv4", "vscode-server-launcher", "_flag3"],
"options": {
"isGloballyAvailable": true
            },
"status": {
"hostConnectionCount": 0,
"lastHostConnectionTime": "2026-04-08T16:16:57Z",
"clientConnectionCount": {
"current": 0,
"limit": 20
                },
"lastClientConnectionTime": "2026-03-31T23:11:04Z",
"clientConnectionRate": {
"current": 0
                },
"uploadRate": {
"periodSeconds": 1,
"resetTime": 0,
"current": 0,
"limit": 20971520
                },
"downloadRate": {
"periodSeconds": 1,
"resetTime": 0,
"current": 0,
"limit": 20971520
                },
"uploadTotal": 45013860,
"downloadTotal": 19000550,
"apiReadRate": {
"current": 0
                },
"apiUpdateRate": {
"current": 0
                }
            },
"endpoints": [{
"hostRelayUri": "wss://uks1-data.rel.tunnels.api.visualstudio.com/api/v1/Host/Connect/wild-fog-s1alk0t",
"clientRelayUri": "wss://uks1-data.rel.tunnels.api.visualstudio.com/api/v1/Client/Connect/wild-fog-s1alk0t",
"id": "45e5e54c-1acf-41f3-96d4-c2085c0dfe35-relay",
"connectionMode": "TunnelRelay",
"hostId": "45e5e54c-1acf-41f3-96d4-c2085c0dfe35",
"portUriFormat": "https://a5n51h3l-{port}.uks1.devtunnels.ms/",
"tunnelUri": "https://a5n51h3l.uks1.devtunnels.ms/",
"portSshCommandFormat": "ssh a5n51h3l-{port}@ssh.uks1.devtunnels.ms",
"tunnelSshCommand": "ssh a5n51h3l@ssh.uks1.devtunnels.ms"
            }],
"ports": [{
"clusterId": "uks1",
"tunnelId": "wild-fog-s1alk0t",
"portNumber": 31545,
"protocol": "auto",
"options": {
"isGloballyAvailable": true
                },
"status": {},
"portForwardingUris": ["https://a5n51h3l-31545.uks1.devtunnels.ms/"],
"inspectionUri": "https://a5n51h3l-31545-inspect.uks1.devtunnels.ms/"
            }],
"created": "2025-11-03T11:20:51.376614Z",
"expiration": "2026-05-08T16:17:03Z"
        },
        ...
```

为了连接到一个正在运行的隧道服务器，我们接下来需要生成一个访问令牌。但在此之前，我们需要从上面的响应中获取几项信息：

* `clusterId`

  - 目标隧道所分配到的中继集群。
* `tunnelId`

  - 这是隧道创建时随机生成的名称，看起来类似于 `cheeky-sausage-a123456b7`

有了这些信息后，我们就可以通过以下方式请求一个新的访问令牌：

```
GET /tunnels/wild-fog-s1alk0t?includePorts=true&tokenScopes=connect&api-version=2023-09-27-preview HTTP/1.1
Host: CLUSTERID.rel.tunnels.api.visualstudio.com
Authorization: github gho_GITHUB_TOKEN_HERE
User-Agent: vscode.dev.remote-server Dev-Tunnels-Service-TypeScript-SDK/1.2.1
```

从 URL 参数中我们可以看到，我们正在请求一个 connect 范围的令牌，并在响应中收到它：

```
HTTP/1.1 200 OK
...
{
"clusterId": "uks1",
"tunnelId": "wild-fog-s1alk0t",
"name": "",
"description": "",
"labels": ["prometheus", "protocolv4", "vscode-server-launcher", "_flag8"],
"accessTokens": {
"connect": "eyJhbGci[REDACTED]FxfRpNXiNGjcw"
    },
"accessControl": {
"entries": []
    },
"options": {
"isGloballyAvailable": true
    },
"status": {
"hostConnectionCount": 0,
"lastHostConnectionTime": "2026-04-13T16:05:29Z",
"clientConnectionCount": {
"current": 0,
"limit": 20
        },
"lastClientConnectionTime": "2026-04-13T15:46:16Z",
"clientConnectionRate": {
"current": 0
        },
"uploadRate": {
"periodSeconds": 1,
"resetTime": 0,
"current": 0,
"limit": 20971520
        },
"downloadRate": {
"periodSeconds": 1,
"resetTime": 0,
"current": 0,
"limit": 20971520
        },
"uploadTotal": 6366,
"downloadTotal": 15840,
"apiReadRate": {
"current": 0
        },
"apiUpdateRate": {
"current": 0
        }
    },
"endpoints": [{
"hostRelayUri": "wss://uks1-data.rel.tunnels.api.visualstudio.com/api/v1/Host/Connect/wild-fog-s1alk0t",
"clientRelayUri": "wss://uks1-data.rel.tunnels.api.visualstudio.com/api/v1/Client/Connect/wild-fog-s1alk0t",
"id": "45e5e54c-1acf-41f3-96d4-c2085c0dfe35-relay",
"connectionMode": "TunnelRelay",
"hostId": "45e5e54c-1acf-41f3-96d4-c2085c0dfe35",
"portUriFormat": "https://a5n51h3l-{port}.uks1.devtunnels.ms/",
"tunnelUri": "https://a5n51h3l.uks1.devtunnels.ms/",
"portSshCommandFormat": "ssh a5n51h3l-{port}@ssh.uks1.devtunnels.ms",
"tunnelSshCommand": "ssh a5n51h3l@ssh.uks1.devtunnels.ms"
     }],
    ...
```

同样，从这个响应中我们需要在继续之前提取几项内容：

* `connectToken`

  - 连接到中继服务器所需的 JWT 访问令牌
* `clientRelayUri`

  - 我们需要连接的客户端 WebSocket URI

生成访问令牌后，我们可以进入下一层。但在此之前，让我们稍微绕个弯，讨论一下初始身份验证。

## 使用 GitHub 进行身份验证

你可能已经从上面的 `Authorization`标头中注意到，在向 REST 服务器发出请求时使用了 GitHub token。

该 token 是当你首次使用 GitHub 账户设置 dev tunnels 时，由 VS Code 发起的 OAuth2 流程生成的 (使用 GitHub OAuth2 Client ID `01ab8ac9400c4e429b23`以及 `read:org`和 `user:email`这两个 scope)。

该 Client ID 也已获准用于 Device Code 流程，这意味着 Device Code Phishing 是获取 dev tunnels 身份验证所需 GitHub token 的一种可行方法：

```
POST /login/device/code HTTP/1.1
Host: github.com

client_id=01ab8ac9400c4e429b23&scope=read:org,user:email
```

OAuth2 流程完成后，GitHub 会返回一个 token:

```
HTTP/1.1 200 OK
...

{
"access_token": "gho_[REDACTED]",
"token_type": "bearer",
"scope": "read:org,user:email"
}
```

正是这个 `access_token`值会被用于最初的 API REST 调用中，通过 `Authorization: github TOKENHERE`标头来生成 connect token。

## 使用 Azure 进行身份验证

如果你选择使用 Entra ID 作为 SSO 提供商，那...