---
title: Stillepost：或者，如何通过 Chromium 代理你的 C2 HTTP 流量
url: https://mp.weixin.qq.com/s/zeNJEKYTBSLBvSwB87vsRg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:32.186367
---

# Stillepost：或者，如何通过 Chromium 代理你的 C2 HTTP 流量

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nShlzA64pdGVFiauibUsYvfRacfM0ZVOfBhhxFMAoia5Zh4Wq6LzgiaKWXmGFiaobCVetOr24nfuSmKpXV5KbqkgZLdPTBXMK3KaoicHc/0?wx_fmt=jpeg)

# Stillepost：或者，如何通过 Chromium 代理你的 C2 HTTP 流量

x90x90
x90x90

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://x90x90.dev/posts/stillepost/ | x90x90 |

## 引言

我最近在为自己的 C2 项目寻找新模块时，开始接触从不同浏览器中导出 cookies 这一话题。在阅读实现这件事的各种技术时，我发现了像 WhiteChocolateMacademiaNut 这样的工具，它利用了 Chrome DevTools Protocol (简称 CDP)。这种方法之所以让我印象深刻，是因为它不同于其他技术，不需要直接读取文件，也不依赖 hooking，而是借助一个原本就存在、且按预期方式使用的合法功能来达成恶意目的。这让我开始思考：这个 Chrome DevTools Protocol 对攻击者来说，还能在哪些方面派上用场？这也正是这篇博客和工具发布的由来。

在这篇文章里，我会介绍 Chrome DevTools Protocol、我在阅读其文档时受到启发产生的想法，以及如何把这个想法一步步落地成可用实现。读完这篇博客后，你应该能够在自己的项目中使用 stillepost，通过基于 Chromium 的浏览器发送 HTTP 请求。

> 如果你对背后的想法和开发过程不感兴趣 (🥲)，可以直接在这个仓库里查看最终的 C 库和 Python 代码：https://github.com/dis0rder0x00/stillepost

## ✨Chrome DevTools Protocol✨

正如 ChromeDevTools documentation 本身所说：

> **Chrome DevTools Protocol**允许工具对 Chromium、Chrome 以及其他基于 Blink 的浏览器进行插桩、检查、调试和性能分析。许多现有项目 目前都在使用 这一协议。Chrome DevTools 本身也使用该协议，并由其团队维护对应的 API。
>
> 插桩能力被划分为多个 domain (如 DOM、Debugger、Network 等)。每个 domain 都定义了一组它支持的命令，以及它会产生的事件。无论是命令还是事件，都会被序列化为固定结构的 JSON 对象。

要使用 CDP，首先需要通过命令行参数 `--remote-debugging-port=`启动一个 Chrome 实例。如果你把这个参数设为 `0`，Chrome 会随机生成一个端口号，并通过该端口暴露 CDP server。如果你不喜欢随机性，想让生活更可控一点，也可以手动指定任意端口号 (当然，这个端口必须可用)。

在启动浏览器并让它拉起 CDP server 之后，你就可以通过一个 WebSocket URL 连接到它。这个 WebSocket URL 有两种获取方式：

1. 浏览器进程会把这个 URL 打印到 STDERR，可以直接从那里读取。
2. 通过读取 `http://127.0.0.1:<debugPort>/json/list`获取。

如果你选择第二种方式，对这个 endpoint 发起一个 GET 请求后，会得到如下类似响应；你可以从中解析出任意一个 `webSocketDebuggerUrl`:

```
[ {
"description": "",
"devtoolsFrontendUrl": "https://aka.ms/docs[...]",
"id": "FA73A14107D6EF7709C69BFB9BAAB529",
"title": "localhost",
"type": "page",
"url": "http://localhost:4444/json/list",
"webSocketDebuggerUrl": "ws://localhost:4444/devtools/page/FA73A14107D6EF7709C69BFB9BAAB529"
},
[...]
]
```

连上 WebSocket 之后，Chrome DevTools Protocol 主要通过 JSONRPC 请求下发不同命令。每个命令请求都由一个 JavaScript struct 组成，其中包含 `id`、`method`和 `params`，而 `params`中则放入你希望或需要传给该方法的参数。

下面是一个对当前页面截图的命令示例：

```
{
"id": 1,
"method": "Page.captureScreenshot",
"params": {
"format": "jpeg"
    }
}
```

我强烈建议你亲自查看 Chrome DevTools Protocol Documentation，那里列出了所有可用的 domain、它们的方法、属性以及使用方式。

既然核心技术基础已经讲清楚了，接下来我们就看看该如何“滥用”它。

## 现在怎么办 ¯\_(ツ)\_/¯? 核心思路

CDP 让我们能够访问浏览器的基础功能。例如，我们可以：

* 打开页面
* 读写已打开标签页的 DOM
* 获取宿主机信息
* 访问浏览器存储
* 以及更多功能……

但我问了自己一个问题：既然我们已经能访问浏览器这么多功能，那么浏览器具备、而恶意 implant 可能缺少的东西是什么？

我首先想到的是：对各种网站和 endpoint 发起“看起来合理”的网络流量。

如果我们落地到一台用户工作站上，通常可以预期公司会允许员工通过浏览器访问 Web。这意味着浏览器应该已经配置好了正确的代理设置 (或者直接使用系统代理配置)，具备对 443 端口所需的防火墙白名单，而且来自 Chrome、Edge 或其他浏览器的流量本身也应当是正常可预期的。

在我看来，这非常适合这样一种场景：钓鱼载荷通过 side-loading 的方式，让你的 implant 运行在某个任意的已签名二进制文件中。如果 implant 能把流量代理到用户的浏览器里发出，你就可以避免由这个 side-loaded 二进制直接产生异常的对外连接流量 (除了本地 localhost 连接以外)，同时也不必操心让 implant 自己具备代理感知能力。并且，既然这是钓鱼活动的一部分，就可以假设它落在一台用户每天都会实际使用的机器上，这意味着浏览器大概率已经完成配置并且可正常使用。

那么，是否存在一种方式，能让我们通过 Chrome DevTools Protocol 触发任意请求？简短回答当然是：有。否则这篇博客大概也就没什么写的必要了……

我最初想到的是利用 `Network`domain，但在查看它的描述和可用函数后，我发现它似乎并不合适，因为乍一看它并没有提供那种可以让我们把任意数据发送到任意 URL 的函数：

![landscape](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjpjbWXF5b5VrGa0hh6L3HrDcj1hQ8QHXkhR5icLVLFMLP0viaXpticxQdI7iaThIhq0dcRXh0E6QOkIf8mO1c2J3kEGbRkwzQKMng/640?wx_fmt=png&from=appmsg)

landscape

我的下一个想法就稍微“hacky”一点了。如果我们能控制已打开页面的 DOM，那是不是可以往里面注入任意 JavaScript 代码，并由它触发一个 XHR 请求？这样一来，我们就能控制目标 URL、数据，甚至部分请求头。但是，这种方法很可能会受到目标页面 CSP 的限制，从而影响内联 JavaScript 的执行。

于是我又在文档里继续翻了一阵，找到了一个替代方案，而且在我看来更好：`Runtime`domain 及其 `evaluate`方法:

![landscape](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjYicyx0LzAUZCI4XfwDqrrCvQzz9fBXsZ4o5JIeAySANGkHoA3J6x345FgBpqXvG1Oia6OjhGb3pkeXww15vvy3k2zPyKFSJViaw/640?wx_fmt=png&from=appmsg)

landscape

这个方法允许我们直接 `eval`任意 JavaScript 代码，并把它的返回值作为响应拿回来。

因此，只要我们写一个 JavaScript 函数，让它接收 URL、一些数据以及一组请求头，然后通过 XHR 发起请求，从理论上讲，我们就能返回一个包含响应内容的对象。做到这一步，整个项目的核心目标也就实现了。那就开始吧。

## 搭建整体框架

基于目前掌握的信息，这个 PoC 的基本工作流程应当如下：

1. 准备环境
2. 使用必要的参数启动一个 Chromium 浏览器
3. 解析 JavaScript 模板并填入所需信息 (method、目标 URL、data、headers)
4. 获取 WebSocket URL 并连接过去
5. 携带该 JS 模板发出 `Runtime.Evaluate`命令
6. 取回响应

> 如果这能帮助你更好理解这个思路，我也公开了自己最初的 Python PoC: https://github.com/dis0rder0x00/stillepost/blob/main/python\_code/stillepost\_poc.py

### 环境准备

在启动浏览器之前，我们需要先明确并准备一些变量，包括：

1. 要启动哪个浏览器
2. 浏览器应当使用哪个 user-profile
3. CDP server 监听哪个 debug port

在 stillepost 库中，这些内容都作为对外暴露函数 `stillepost_init`的一部分来实现，其函数签名如下：

```
BOOL stillepost_init(LPSTR lpBrowserPath, DWORD dwDebugPort, LPSTR lpProfilePath)
```

第一个参数 `lpBrowserPath`的用途应该很直观，它表示基于 Chromium 的浏览器可执行文件路径。如果这个参数被设置为 `NULL`，则会使用 Edge 的默认路径 (`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`)。

理论上你也可以使用其他基于 Chromium 的浏览器，例如：

* Chrome
* Opera
* Brave
* Vivaldi
* Chromium (谁能想到呢)

第二个参数 `dwDebugPort`是 CDP server 监听的 debug port。如果它被设为 `0`，代码就会模拟浏览器自身的行为，随机生成一个端口。

第三个参数 `lpProfilePath`表示浏览器实例将使用的 profile。你既可以传入 profile 文件夹路径，也可以传入 profile 名称。如果把这个参数设为 `NULL`，stillepost 会生成并创建一个临时目录，并在后续由 stillepost 的 cleanup 函数将其删除。

我更倾向于让这个工具在每次运行时都从一个干净环境开始，因此默认行为是新建一个临时 profile (也就是传入 `NULL`)。我认为 XHR 请求大概率不会出现在用户 profile 的历史记录里，但与其冒着污染现有用户 profile 的风险，我还是更愿意创建一个临时目录，并在之后删除它。如果你了解使用现有 profile 可能带来的影响，欢迎告诉我。

当浏览器参数和环境都准备好后，函数接下来就会真正启动浏览器。

### 启动浏览器

真正启动这个进程并没有多复杂，本质上就是调用 `CreateProcessA`并带上相应命令行参数。

```
HRESULT hr = StringCchPrintfA(
    lpDebugCmd,
sizeof(lpDebugCmd),
"\"%s\" --remote-debugging-port=%d --headless --user-data-dir=\"%s\" --log-level=3 --disable-logging",
    g_lpChromePath,
    g_dwDebugPort,
    g_lpProfileFolder
);

if (!CreateProcessA(
NULL,
    lpDebugCmd,
NULL,
NULL,
FALSE,
    CREATE_SUSPENDED | DETACHED_PROCESS,
NULL,
NULL,
    &si,
    &pi))
return;

g_piBrowser = pi;
```

> 作者注：在开发这个技术时，我曾在这个阶段加入过一个小型规避机制，用来增加检测难度，这个思路来自我在一些类似技术检测规则中见过的模式 (如果能在不带初始参数的情况下触发进程创建就更好了……)。我最终没有把这部分代码放进公开版本。我认为，不包含它也足以说明核心概念；而公开“规避性”实现，在我看来，只会降低缺乏经验的使用者上手门槛。我原本打算在这里简要描述一下这个机制，所以才把“启动浏览器”单独写成了一节，但结果也导致这一节显得有点空。抱歉。

除了 debug port 和 profile 这类环境信息外，我们还指定浏览器以 headless mode 启动。这样浏览器就不会创建可见窗口。这显然是必须的，否则用户会直接看到有东西在运行。不过这样做也有个副作用：浏览器会尝试附加到我们自己进程的控制台上。理论上你也许可以规避这一点，但我认为对这个 PoC 来说不值得花这个精力，所以我选择把日志限制到最低，这也就是浏览器剩余那些命令行参数存在的原因。

### 获取 WebSocket URL

在启动浏览器之后，我们还需要拿到 WebSocket URL，这样才能向它发送命令。

如果你还记得前面内容，我当时提到了两种获取方式。在这个项目里，我选择实现第二种，也就是向 `http://127.0.0.1:<debugPort>/json/list`发起一个 `GET`请求，并解析它的响应。

这部分代码位于 `get_websocket_debugger_url`函数中，它由 `stillepost_init`在内部调用。利用 WinHTTP 和 cJSON 实现起来相当直接，所以这里我就不展开讲太深了。

发出这个 `GET`请求后，借助 cJSON 库，响应解析大致就像下面这样简单：

```
cJSON *cjsonRoot = cJSON_Parse(lpResponse);
if (!cjsonRoot)
goto cleanup;

if (!cJSON_IsArray(cjsonRoot)) {
cJSON_Delete(cjsonRoot);
goto cleanup;
}

cJSON *cjsonFirstElem = cJSON_GetArrayItem(cjsonRoot, 0);
if (!cjsonFirstElem || !cJSON_IsObject(cjsonFirstElem)) {
cJSON_Delete(cjsonRoot);
goto cleanup;
}

cJSON *cjsonWsItem = cJSON_GetObjectItemCaseSensitive(cjsonFirstElem, "webSocketDebuggerUrl");
if (!cjsonWsItem || !cJSON_IsString(cjsonWsItem) || !cjsonWsItem->valuestring) {
cJSON_Delete(cjsonRoot);
goto cleanup;
}

lpWsUrl = _strdup(cjsonWsItem->valuestring);
cJSON_Delete(cjsonRoot);
```

知道该通过哪个 WebSocket URL 去连接 CDP server 当然很好，但截至目前，我们还不知道连上去之后到底要执行什么。下面就来解决这个问题。

### JavaScript 模板

我得坦白说……我真的不喜欢 JavaScript。也正因为如此，我写它写得非常烂 (除了写一些基础的 XSS PoC，用来拿个 CSRF-token，或者以目标用户身份执行某些操作之外)。所以，我们这里用来实际触发到远端 endpoint 的 XHR 请求的那个 JavaScript 模板，基本上是 AI 生成的。拜托别举着火把和草叉来找我。

于是我让 ChatGPT 帮我写了一个 JavaScript 函数，用来触发 XHR 请求，并返回一个包含响应状态码、全部响应头以及响应体的 JSON 对象。在说明这个函数应当接受哪些参数、并对结果做了一些修改之后，我得到了下面这段代码：

```
functionsendRequest(method, url, headersJson, dataJson) {
returnnewPromise(function(resolve) {
varxhr=newXMLHttpRequest();

xhr.onreadystatechange=function() {
if (xhr.readyState===4) {
varallHeaders=xhr.getAllResponseHeaders() ||"";
varheaderLines=allHeaders.trim().split(/\\r?\\n/);
varhdrObj= {};
for (vari=0; i<headerLines.length; i++) {
varline=headerLines[i];
varidx=line.indexOf(":");
if (idx>-1) {
vark=line.substring(0, idx).trim();
varv=line.substring(idx+1).trim();
hdrObj[k] =v;
                    }
                }

varresultObj= {
status:xhr.stat...