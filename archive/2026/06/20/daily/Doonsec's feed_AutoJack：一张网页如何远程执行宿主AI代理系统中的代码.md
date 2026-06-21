---
title: AutoJack：一张网页如何远程执行宿主AI代理系统中的代码
url: https://mp.weixin.qq.com/s/ekyU9ZV6IkaqC9zc5mHPsQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:48:13.453315
---

# AutoJack：一张网页如何远程执行宿主AI代理系统中的代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjxDmxHZo4GxeB7459ENs7Iwiac1yEuekuQrd7lykfUosWHVK1CLTP5ouleqiaTPviaIGPA97Kjrh4QxGISKRcHwmGlUnGUTDQ1Pw/0?wx_fmt=jpeg)

# AutoJack：一张网页如何远程执行宿主AI代理系统中的代码

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

我们对AI代理框架安全性的持续研究发现，AutoGen Studio（AutoGen的开源原型UI）中存在一个漏洞利用链。它允许浏览代理渲染的非受信网页内容触及本地的模型上下文协议 (MCP) WebSocket，进而在宿主上启动任意进程。我们将这种技术称为 **AutoJack**：它通过跨越许多开发者工具所依赖的本地主机信任边界，劫持代理成为攻击者的“最后一公里”攻击媒介。

我们将此问题报告给了微软安全响应中心 (MSRC)。接到报告后，维护者在主分支的提交 `b047730` 中加固了上游代码。此问题在开发阶段即被识别和修复。受影响的MCP WebSocket接口从未包含在任何PyPI发布版本中，因此通过PyPI安装AutoGen Studio的用户不会暴露于这条具体攻击链。

但更广泛的教训是具有普遍性的：如果一个代理能够浏览非受信页面，同时又能与有特权的本地服务通信，那么回环地址 (localhost/127.0.0.1) 就可能变成一个攻击面，控制平面必须经过认证、授权和隔离。

## **我们为何关注代理框架**

现代的AI代理不仅是文本生成器。它们能读取文件、浏览网页、调用API、调用外部工具。这正是它们有用的原因，也正是为什么需要投资去发现那些将模型与工具连接起来的框架中存在的*系统性*执行风险。在这个系列的前一篇文章中，我们介绍了 Microsoft Semantic Kernel中的RCE原语。在这篇文章中，我们将目光移向更上层——一个*面向基础设施和开发者*的原型界面，并展示当原型在没有安全防护的情况下运行时，那些使这些工具对实验如此有价值的关键代理能力，是如何变成远程代码执行 (RCE) 的攻击通道的。

关键点不是要避免使用原型工具，而是这个：**当在你的核心服务器或笔记本电脑上运行的代理可以浏览开放的互联网**并且**与有特权的本地服务通信时，localhost就不再是一个信任边界了**。防御者需要为此做好准备，而本文的发现说明了原因。

### **什么是AutoGen Studio**

AutoGen Studio 是建立在 AutoGen（微软研究院的多代理系统框架）之上的一个用户界面 (UI)。它允许开发者组合代理、附加工具（包括MCP服务器）并运行快速实验。其文档明确了其预期用途。换句话说，它是一个研究性质的原型，在开发体验上有所取舍：默认设置倾向于迭代便利性，而不是加固部署。

## **AutoJack攻击链概览**

*以下说明仅为演示目的。该漏洞利用链在当前的构建版本中已失效。将其包含在此是为了让防御者能在其他代理框架中识别出类似模式。*

该利用链结合了AutoGen Studio的MCP WebSocket接口中三个独立的问题：

1. **来源 (Origin) 白名单信任 localhost —— 但本地代理**本身**就是 localhost****(CWE-1385 – WebSockets中缺少来源验证)：** MCP WebSocket只接受来源 (Origin) 为 `http://127.0.0.1` 或 `http://localhost` 的连接。这可以阻止来自 `evil.com` 的浏览器攻击，但**不能**阻止在**同一台机器上由AutoGen代理控制的**无头浏览器所渲染的JavaScript。
2. **认证中间件对MCP路径默认跳过 (CWE-306 – 关键功能缺少认证)：** AutoGen Studio中的认证中间件明确跳过了 `/api/mcp/*`（和 `/api/ws/*`），假设这些路径会自己做检查。但MCP WebSocket处理程序并未实施后续检查。结果是，不论应用的其余部分配置了何种认证模式，MCP WebSocket都接受未经任何认证的连接。
3. **来自URL的 `StdioServerParams` 被直接执行 (CWE-78 – OS命令中特殊元素的不当中和)：** 该端点接受一个 `server_params` 查询参数，将base64编码后的JSON块解码为 `StdioServerParams`，然后将命令和参数交给 `stdio_client(...)`。这里没有白名单机制—— `calc.exe`、`powershell.exe -enc …` 或 `bash -c ‘…’` 都会被当作“MCP服务器”接受。

将这些问题与互联网上一张由在同一台机器上运行的AutoGen代理渲染的网页结合起来，就形成了一个远程代码执行 (RCE) 原语。除了让代理渲染攻击者的页面外，不需要任何用户交互。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZhAUtBk1wYLZZLYHQIADfT8ibhEKGDCM8TYcxPicaUqBVPAWia4thelKVNickWXMeZwmX8ZibibfrXlx7NnCv8qSxuP5Qu6RP966E0tM/640?wx_fmt=other&from=appmsg)

图1：端到端的攻击链。一个攻击者页面被本地浏览代理渲染；该页面打开一个到 `ws://localhost:8081/api/mcp/ws/?server_params=` 的WebSocket连接；AutoGen Studio解码有效负载并在开发者的账户下启动攻击者提供的命令。

我们将此技术命名为AutoJack：攻击者*劫持*了浏览代理，将其用作一个“混乱的代理人”，驱使它跨越本地主机边界，进入AutoGen Studio的MCP控制平面。

## **攻击链剖析**

### **问题1：代理自身就能绕过的来源 (Origin) 白名单**

AutoGen Studio的MCP WebSocket依赖于防御浏览器驱动的跨站WebSocket劫持 (CSWSH) 的常规方法：只接受来自 `127.0.0.1` / `localhost` 的同源连接。

```
allowed_origins = ["http://127.0.0.1", "http://localhost"]
```

这对于人类用户打开一个访问 `evil[.]com` 的标签页是正确的控制。浏览器会将来源 (Origin) 头设置为 `https://evil[.]com`，检查会失败，连接会被拒绝。

但对于代理来说，仅靠来源 (Origin) 检查就不是正确的控制方法了。一个配备了内置网页浏览工具的AutoGen代理，例如 `MultimodalWebSurfer`、`fetch_webpage_tool`、任何基于Playwright的浏览器、或者一个能执行 `requests/websockets` 的代码执行工具，它本身就在*工作站上*作为一个进程运行。它加载的任何内容都继承了本地主机的身份。由该无头浏览器执行的任何JavaScript的“来源”就是代理导航到的任何地方——而随后它发起的WebSocket调用所携带的来源 (Origin) 则满足白名单要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZgN7dT2H6wxic96RkXvYspiaiaibsqwOkpHVabdPOib67l46GZEJKYic7tUFSFB0bFzNpH1E4oq6aRKuDwhLa668gGqX3mVoNWJCOKfM/640?wx_fmt=other&from=appmsg)

图2：通过代理绕过来源 (Origin) 检查。AutoJack——工作站上的浏览代理被外部内容操纵，连接到本地的AutoGen Studio MCP控制平面，从而瓦解了回环地址的信任边界。

### **问题2：认证中间件排除了MCP**

AutoGen Studio支持几种认证模式 (`none`， `github`， `msal`， `firebase`)。它们都通过一个在FastAPI路由分发之前运行的 `AuthMiddleware` 连接起来。在PyPI上的版本中，这个中间件包含一个针对WebSocket风格路径的早期返回：

```
# auth excluded for these paths; they were intended to do their own checks
if request.url.path.startswith("/api/ws") or request.url.path.startswith("/api/mcp"):
    return await call_next(request)
```

其意图是合理的：ASGI中间件无法像拦截HTTP请求那样有意义地拦截WebSocket*握手*，因此设计上要求WebSocket处理程序自己在接受连接时强制执行认证。但MCP路由从未承担起这个责任。因此，对于已发布的包，下表成立：

| **认证配置** | **REST API 受保护？** | **`/api/mcp/ws/*` 受保护？** |
| --- | --- | --- |
| type: none | 否 | 否 |
| type: github | 是 | **否** |
| type: msal | 是 | **否** |
| type: firebase | 是 | **否** |

仅仅在 `config.yaml` 中开启认证本身并不能堵上这个漏洞。

### **问题3：来自URL的 `server_params` 就是命令行参数**

开发版本中的MCP WebSocket路由读取一个 `server_params` 查询参数，将其base64解码，JSON解析为 `StdioServerParams`，然后将它传入 `stdio_client(...)`：

```
@router.websocket("/ws/{session_id}")
async def mcp_websocket(websocket: WebSocket, session_id: str):
    encoded = websocket.query_params.get("server_params")
    decoded = base64.b64decode(encoded)
    params = StdioServerParams(**json.loads(decoded))
    await create_mcp_session(bridge, params, session_id)
```

`StdioServerParams.command` 和 `StdioServerParams.args` 被传递给 `stdio_client`，后者用它们来生成一个MCP“服务器”进程。这里没有强制要求可执行文件必须是支持MCP协议的二进制文件的白名单，所以同样的管道可以愉快地生成 `calc.exe`、`powershell.exe -enc …` 或 `bash -c '…'`。

一个最小的有效负载如下：

```
{
  "type": "StdioServerParams",
  "command": "calc.exe",
  "args": [],
  "env": { "pwned": "true" }
}
```

将其base64编码成一个查询字符串，完整的攻击URL是：

```
ws://localhost:8081/api/mcp/ws/<session_id>?server_params=<base64(json)>
```

结合问题1和2，攻击者所需要做的就是让代理渲染一个能打开这个URL的页面。

## **组合起来：一个现实的场景**

为了验证端到端的攻击链，我们编写了两个小型的验证程序：

**`malicious_web_server.py`**：一个运行在 `http://attacker[.]example/websocket-interactive` 的网页。其唯一有意义的內容是一个 `<script>`，它会用一个base64编码的、用于运行 `calc.exe` 的有效负载打开上述WebSocket。

**`web_summarizer_app.py`**：一个包装在Flask UI中的小型“网页内容摘要”*AutoGen代理*应用。该应用从用户那里获取一个URL，并将其交给一个 `MultimodalWebSurfer` 代理，提示为\*“浏览此URL并总结其内容。”\* 换句话说，这是一个任何人都可以在框架之上构建的完整AutoGen代理——Flask页面只是其界面。

端到端的流程如下：

> 开发者构建了一个运行在与AutoGen Studio相同机器上的AutoGen代理，例如网页摘要工具，或任何具有浏览能力的代理。
>
> 攻击者在一个合法的新闻网站上植入恶意评论，或者用户要求摘要代理总结一个攻击者控制的URL。
>
> 这可以通过直接的提示、先前内容中的提示注入，或应用中的URL字段发生。

> 代理的浏览工具（在我们的例子中是MultimodalWebSurfer）将无头浏览器导航到攻击者的页面。
>
> 页面的JavaScript打开 ws://localhost:8081/api/mcp/ws/<id>?server\_params=<base64> 连接。因为浏览器在同一台机器上，来源 (Origin) 是可接受的；又因为认证中间件跳过了 /api/mcp/\*，所以不需要令牌。
>
> AutoGen Studio解码有效负载，并在开发者账户下运行 calc.exe（或任何其他命令）。

> *注意，我们将演示打包为一个受控的本地概念验证*，详见端到端演示。

下面的截图展示了在单台工作站上的完整攻击链：开发者在 `localhost:8081`（默认端口）启动AutoGen Studio，打开网页内容摘要应用，并提交一个攻击者控制的URL。在 `MultimodalWebSurfer` 渲染页面的几秒钟内，`calc.exe` 计算器程序就会出现在开发者的桌面上，由AutoGen Studio进程启动，而不是由浏览器或代理的无头Chrome启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZg5ZNVXdCBbrqh48Jh9SEZ3D0yCMbnybnB3tbUf5CRpnxFgOBibqekIY67MnuDoMI2MbKb6nhzlmdIPAia85hzHC5E1y9whnso44/640?wx_fmt=other&from=appmsg)*Autogen Studio*

![](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZjFrAQa8ABbXibsxuiclpOln3dTuAxqcBopKauKB80soicdZYcveMzJ3HVaDARkblmcQ4dkCXricQEWRiafnfLtvu6JXbgtqTrVuqRg/640?wx_fmt=other&from=appmsg)*我们构建的AutoGen浏览器代理按设计检索并总结网站内容。*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjlTNUQk7nwPGjMXTn71LKQmvs4eoHm1OWuAw6EHqsCGzF0cCHP1yb4Fq3BgMiboh03QH1L9auWOaMo9OTRgNTGvIMmUZMEHkPM/640?wx_fmt=other&from=appmsg)*AutoJack实战：浏览代理渲染攻击者页面；页面的JavaScript打开指向 `ws://localhost:8081/api/mcp/ws/…?server_params=` 的WebSocket；AutoGen Studio解码有效负载并启动calc.exe。在真实世界的部署中，同样的原语可被用来在任何运行AutoGen Studio的宿主上执行攻击者选择的其他命令，具体取决于该进程的权限。*

### **已应用的修复和加固措施**

在微软安全响应中心的协助下，此问题得到了修复。维护者实施了必要的加固措施，在全面发布和更广泛采用之前帮助保护用户：

**服务器端参数绑定。** 在主分支上，WebSocket处理程序不再从URL读取 `server_params`。一个单独的 `POST /api/mcp/ws/connect` 路由将参数以UUID为键，存储在服务器端的 `pending_session_params` 中。WebSocket处理程序通过会话ID弹出该条目，并对未知的ID返回关闭码4004拒绝连接。代码注释明确指出：*“这防止攻击者通过WebSocket查询字符串注入任意的server\_params。”*

**更严格的认证跳过列表。** 主分支上的中间件跳过列表不再包含 `/api/mcp`。它现在只包含 `/api/ws` 和 `/api/maker`。MCP路由现在会经过正常的认证路径。

这些更改自提交 b047730 起已存在于AutoGen的主分支中，主分支的 `pyproject.toml` 版本为 0.7.2。

**关键的是，这个问题是在任何PyPI版本发布之前被识别和修复的，因此受影响的代码从未在任何已发布的包中发布。** 暴露范围仅限于在MCP插件合并到主分支到上述加固提交之间的时间段内，从GitHub主分支构建Aut...