---
title: 网安利器 | Burp Suite + MCP：让AI参与Web安全测试
url: https://mp.weixin.qq.com/s/ciP5hHiFfSl5aOmOSY1b2Q
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:20.981788
---

# 网安利器 | Burp Suite + MCP：让AI参与Web安全测试

# 网安利器 | Burp Suite + MCP：让AI参与Web安全测试

原创

小安Air
小安Air

小安数记pro

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**前言：新漏洞频发，攻击手段日新月异。这里是小安数记pro。专注网络安全领域，日常更新分享，带你穿透技术迷雾。左上角点击关注，你的支持是小编创作的最大动力。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A4gKXH0hLyBHR4vfqicpmicGbiaZFcT0QXiaia0aUy7F99CjC8feIzeOejCfu5H1BRgbdMyiallrQJkArX03eUb4sQoA/640?wx_fmt=png&from=appmsg)

由于公众号推送机制调整，现在只有**常读和星标**的公众号才会显示大图推送。防止大家找不到，收不到及时咨询，建议大家将小安数记pro按照上面图片设置为星标，之后就可以及时收到咨询！！！

**免责声明**

> 本平台所有内容（包括技术文章、工具及方法）仅供网络安全从业人员在合法授权环境下进行学习与研究，严禁用于任何非法用途。使用者需在自有或完全授权的环境中操作，并对自身行为承担全部责任。因使用本平台内容导致的任何损失，本平台不承担责任。我们保留随时更新本声明的权利，不另行通知，持续使用即视为接受修改内容。请务必遵守法律法规，共同维护健康的网络安全研究环境。本文仅展示本人自己使用推荐和分享感受，并不做任何商业行为。作者只负责分享自己实践过程。

这篇文章不打算把 MCP 讲成一个“万能外挂”。我更想从实际使用角度看看：当Burp Suite接入 MCP 后，AI能够访问哪些Burp能力，怎么连接，什么地方值得用，以及哪些权限一定要谨慎。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkUMc1pE2l1A2Cm5q5WLLY2cibLvsnXib9icFOr33bt2xBCJ3fwfgy2VfJj3Oju7qyYD9xrg7XFCsiaGS5rI6CRZp5M4dOPZU1xTib4s/640?wx_fmt=png&from=appmsg)

# 一、先说结论：MCP到底是什么？

MCP 的全称是 Model Context Protocol。放到 Burp Suite这个场景里，可以把它理解成一座“桥”：Burp负责代理、抓包、重放、历史记录等安全测试工作，AI客户端负责理解自然语言、整理上下文和调用工具，MCP则规定了两边如何以结构化方式通信。

所以，MCP 的价值并不是“给Burp加一个聊天框”，而是让 AI 客户端可以在授权范围内调用 Burp 提供的工具。比如读取和筛选 Proxy 历史、发送HTTP/1.1或HTTP/2请求、创建Repeater标签页、把请求发送到 Intruder，以及使用URL/Base64等编码工具。PortSwigger当前公开的MCP Server扩展也明确列出了这些能力。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkWo6WaiaFZAEFlsiaofdFyokEoXEm1IzrKfxcqDY5PPJe99iaxR75tq6xhamnwXicbN0ETLPE4TakHLicdWwt7EhZ5pvCaCXA6kYumA/640?wx_fmt=png&from=appmsg)

# 二、接入之后，AI究竟能做什么？

从实际工作流看，最有意思的地方不是“AI 会不会聊天”，而是它能不能减少重复操作。MCP 接通以后，AI 可以围绕 Burp 中已有的流量和工具展开工作，而不是让你每次都把一整段 HTTP 请求手动复制过去。

* 查看和筛选 Proxy 历史：可以按条件检索 HTTP / WebSocket 历史，辅助快速定位某类请求。
* 发起和修改请求：在支持的安全控制下，由 AI 调用 Burp 发送 HTTP/1.1、HTTP/2 请求。
* 联动 Repeater / Intruder：AI 可以创建 Repeater 标签页，也可以把请求送到 Intruder，方便继续人工测试。
* 使用 Burp 的辅助能力：例如 URL、Base64 编解码以及随机字符串生成。
* 处理 Burp 工作流：还可以和 Organizer 等功能配合，让“发现请求—整理—继续验证”变得更连贯。

Professional 用户还会涉及 Collaborator 等能力。官方说明里明确标注了部分功能是 Professional only，所以实际能调用什么，要看你当前 Burp 版本、授权和具体工具权限。

# 三、AI负责“找”，Burp负责“做”

对于安全测试来说，一个比较实际的分工是：AI 负责从大量信息里整理重点、提出下一步操作；Burp 继续承担真实的流量处理和测试执行。这样做比“让 AI 全自动跑一遍”更容易观察每一步，也更方便人工确认。

举个简单例子：你已经通过浏览器访问了一个授权测试站点，Proxy 历史里积累了几十到上百条请求。传统做法是人工翻历史、找接口、复制参数，再放进 Repeater。接入 MCP 后，可以让 AI 先根据路径、方法、参数特征帮你筛出一组值得继续看的请求，然后由你决定哪些请求进入后续验证。

这里的重点不是让 AI 替代安全人员，而是把“检索、整理、转发、格式转换”这些机械步骤压缩掉，把时间留给真正需要判断的部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/v7ntTxZACkUKpw8hvd21j3iaK0icmgX9LicOoia10CX2bibcAU379z9ibFH5fFp8IcQAOaXhfsNaianDc3TIj6kYUU41XtB15OWQgIX6wHpibrzWRME/640?wx_fmt=jpeg)

# 四、怎么部署？先把最简单的方式跑通

## 1.安装 MCP server

## 方法1：在 Burp 中安装MCP Server

当前官方App页面显示，MCP Server可以直接从Burp的App Store 安装。安装后，在Burp的MCP标签页中启用服务，并根据需要调整安全设置。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkVibAJZJn2wKZoLIIZibgSc4ERLs5NqUHiaKrHicoVbXB6UlXLxRPsVQm51nMrbOUpwe3lNxibU8WshFGeWCIhrYo9YFcMVA0Sf5vicU/640?wx_fmt=png&from=appmsg)

方法2:源码编译安装(商店搜不到时)

```
1.Clone the Repository: Obtain the source code for the MCP Server Extension. 克隆仓库：获取 MCP 服务器扩展的源代码。
```

```
git clone https://github.com/PortSwigger/mcp-server.git
```

```
2.Navigate to the Project Directory: Move into the project's root directory. 进入项目目录：请移动到项目的根目录。
```

```
cd mcp-serverBuild the JAR File
```

```
3.Build the JAR File: Use Gradle to build the extension. 构建 JAR 文件：使用 Gradle 来构建该扩展模块。

```
```
./gradlew embedProxyJar
```
```

This command compiles the source code and packages it into a JAR file located in build/libs/burp-mcp-all.jar. 该命令会编译源代码，并将编译后的文件打包成一个 JAR 文件，该文件位于 build/libs/burp-mcp-all.jar 路径下。

最直接的方式就是下载已经编译好的：https://github.com/PortSwigger/mcp-server/releases/tag/v1.3.0
```

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkX2CjWdiaMhRhtPkZSzGbsOmN5YzoFSiazHUib6P8XHyru8NXibHibIRhm6OlMV4rfVqicibzUn6N8SQeBwRGia4kWibZq7uEE10BLwGicDM/640?wx_fmt=png&from=appmsg)

Loading the Extension into Burp Suite 将扩展模块加载到 Burp Suite 中，这里不过多赘述。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkUp8MHOvGJ0nbbNia7ey5NCD0r0oVjjLjue80ydMHFnyyBPntYnibxbKyjT0NGriaFrQ4ZswHO3lgCFOqUDOF9ZsaryLDRTYDbsy4/640?wx_fmt=png&from=appmsg)

## 2. 打开 MCP 服务并检查监听地址

MCP客户端:Codex、cherryClaude-Desktop、Cherry-Studio、 Cursor、 Trae、Claude-Code CLI等任选其一。

官方项目文档给出的默认监听地址是127.0.0.1:9876。启用服务后，AI客户端就可以通过该MCP服务与本机Burp通信。这个默认方案有一个很重要的特点：服务默认绑定在回环地址，适合本机客户端连接。

```
http://127.0.0.1:9876
```

打开 MCP 标签页：

```
1.✅勾选 Enabled，启动MCP服务；Output面板输出：Started MCP server on 127.0.0.1:98762.Host默认：127.0.0.1，端口默认 9876，不要改成0.0.0.0，避免外部访问风险3.可选配置：  Enable tools that can edit your config : 允许AI修改Burp配置，本地测试可开，生产环境关闭  Extract server proxy jar : 导出 mcp-proxy.jar，用于stdio模式客户端(Claude-Desktop)4.保持Burp全程运行，不要关闭。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkVKqBiauUKQFPzr1shm6p6DTS9pbMEjRnj9N1sY7g3E06Yl1tUqnVRGfqaFgFBoBtXQlD1PSib7X1qIQbdlPeckdt8f47rTTnLxM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkX6oHibZxXCnxiaPUJeWw0t3sKxgh03GuyRcoylJPJ2QBg6A6zavjyYJj4WDTL6aa7FkPAUoRk0ceDdwesYASjQiaBNg4DRSJ8eb4/640?wx_fmt=png&from=appmsg)

## 3. 连接 AI 客户端

PortSwigger的扩展提供了面向Claude Desktop的自动安装方式。如果使用其他兼容MCP的客户端，也可以按客户端要求配置Burp的MCP endpoint。项目仓库同时提供了SSE服务和一个stdio proxy的思路，以兼容只接受stdio MCP Server的客户端。

示例1：Cherry-Studio（SSE模式，最简单）

```
设置 → MCP服务器 → 添加服务器服务器类型：SSE（服务器发送事件）SSE URL：http://127.0.0.1:9876/mcp请求头（部分环境必须加，否则握手失败）Referer:http://127.0.0.1:9876User-Agent:Cherry-Studio
```

示例2：Claude-Desktop（Stdio代理模式）

```
1.在Burp MCP标签页点击 Extract server proxy jar，保存 mcp-proxy.jar，复制完整绝对路径。2.打开Claude-Desktop配置文件：  Windows：%APPDATA%\Claude\claude_desktop_config.json  Mac：~/Library/Application Support/Claude/claude_desktop_config.json3.写入配置，jar路径改为你本地真实路径：{  "mcpServers": {    "burp": {      "command": "java",      "args": [        "-jar",        "/完整路径/mcp-proxy.jar",        "--sse-url",        "http://127.0.0.1:9876/mcp"      ]    }  }}4.重启Claude-Desktop；日志无报错即可识别Burp工具集。
```

示例3:Claude-Code CLI

```
claude mcp add --transpont http burp http://127.0.0.1:9876/mcp
```

执行后即可在claude code对话中调用burp工具。

# 五、第一次使用，可以这样问AI

不建议一上来就让 AI “帮我找漏洞”。更适合从可控、可观察的小任务开始，例如：

* “列出最近抓到的请求，并按 URL 路径帮我归类。”
* “从 Proxy 历史里找出 POST /api/ 开头的请求，整理出方法、路径和状态码。”
* ·“把这条请求放到 Repeater，方便我继续人工验证。”
* “帮我分析这个响应里哪些字段值得进一步检查，但不要主动发送额外请求。”

这样的提示词有两个好处：一是范围清楚，二是每一步都能在Burp里看到结果。等你熟悉工具调用和权限控制以后，再逐步增加自动化程度。

# 六、MCP最值得注意的，其实是“权限”

BurpMCP并不只是“读数据”。官方扩展已经支持发送请求、修改部分配置、控制部分Burp行为等能力。因此，MCP一旦连接成功，就应该把它当作一个具有实际操作能力的自动化接口来管理。

* 目标审批：先理解哪些目标可以被自动调用，再决定是否启用自动批准。
* 配置编辑：官方提供了“允许编辑配置”的选项。没有明确需求时，不必为了追求自动化而全部打开。
* 本地监听：除非有明确的网络架构需求，否则优先保持 127.0.0.1，不要无必要地把服务暴露到非本机接口。
* 数据外发：Burp官方特别提醒，发送给外部工具的数据要遵循相应的数据处理政策。因此，测试数据、账号信息、Cookie、Authorization 头等敏感内容都要提前评估。

还有一个最基本的原则：只对自己有权限测试的目标使用 Burp 和 MCP。Burp 官方文档也明确提醒，安全测试可能对目标系统造成影响，应在获得授权并接受风险的前提下进行。

# 七、使用体验：它更像一个会操作Burp的助手”

如果把 MCP 想象成一个完全自动化的渗透测试按钮，期待值很容易过高。实际使用中，它更像是在 Burp 和 AI 之间增加了一层标准化的工具接口。AI 的优势在于理解自然语言、归纳大量文本和快速组织下一步动作；Burp 的优势仍然是专业的 HTTP 流量处理和测试工具链。

所以我更倾向于把它用于三类事情：流量整理、重复操作、测试过程中的辅助分析。对于真正需要经验判断的漏洞验证，仍然建议自己盯住请求和响应，不要把结果直接当成最终结论。

# 九、最后总结

Burp Suite 接入MCP之后，真正发生变化的是“操作方式”：原本需要你在Burp里一步步寻找和转发的信息，现在可以通过自然语言让 AI 来调用对应工具完成。

它目前更适合作为一个效率工具，而不是一个替代安全人员的“全自动神器”。对于日常 Web 安全学习、授权测试、漏洞复现和流量分析，MCP 提供了一种值得尝试的人机协作方式。

如果第一次体验，建议从本机、单个授权目标、小范围历史检索开始，先把“连接—调用—确认”整个闭环跑通，再慢慢扩大使用范围。

# 十、资料来源与延伸阅读

PortSwigger BApp Store：MCP Server

```
https://portswigger.net/bappstore/9952290f04ed4f628e624d0aa9dccebc
```

PortSwigger 官方 GitHub：MCP Server for Burp

```
https://github.com/PortSwigger/mcp-server
```

PortSwigger：Burp Suite DAST - Connecting your AI client to the MCP server

```
https://portswigger.net/burp/documentation/dast/user-guide/using-ai/mcp-server
```

PortSwigger：Burp Suite 使用与文档

```
https://portswigger.net/burp/documentation
```

  再次强调，能力越大，责任越大。希望我们都能用技术去守护，而不是破坏。记得给小编点个“**赞”留个关注！！！**

> ⚠️ 郑重声明：所有内容均用于合法安全研究，请务必在授权环境下进行测试。做个白帽子，很酷。
> 📮 欢迎交流讨论评论。如果觉得有用，不妨点个“关注”和 “赞”支持一下。

每一次技术解读、每一篇实战记录，都源于大量时间的测试、验证与梳理。如果这份指南为您打开了新的思路，或为您节省了宝贵的时间，不妨给小编进行简单的打赏，支持更多深度内容的诞生。您的每一次点赞、在看、分享，都是我们持续分享的动力；而直接的赞赏，则是对原创内容最温暖的鼓励。

让我们一起，用技术观察世界，用分享传递价值。

感谢您的阅读与支持！

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz...