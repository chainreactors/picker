---
title: AI Agent最危险的地方，不是说错话，而是做错事
url: https://mp.weixin.qq.com/s/X1EOoBbVwWAMTCP6PKC0aw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:57:55.640462
---

# AI Agent最危险的地方，不是说错话，而是做错事

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNiak2LLz90HjRQJOGibMzzfARSfQUz6fqj9Seiccs1MZeoGwhTXEG1esIfbN4icKIX0dCaXtpJq6waJFsAWHn4h3HrlE2baicNdrOiaM/0?wx_fmt=jpeg)

# AI Agent最危险的地方，不是说错话，而是做错事

原创

千里
千里

东方隐侠安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/4vJq7gSyjeia7BjPKK3mwLUFW9iauJgBLr2UwKe5VPaaGic57aQUXgEIQjInsYaDANfjhibss8V9XfAy1BwhTGBO4mzsOWSkXG5Vws7XVZFiac4I/640?from=appmsg)

hi，少侠们，我是千里。

如果你这段时间关注 AI Agent 和MCP 相关的安全资讯，应该会发现一个很有意思的变化。前两年大家聊 AI 安全，重点经常放在 Prompt Injection、越狱、模型会不会乱回答、会不会把敏感信息说出来。但最近观察国内外的安全资讯，我反而觉得真正要盯紧的地方，已经慢慢从“模型怎么回答”转到了“Agent 到底替你做了什么”。

前面我们聊过 Composer 的例子，composer install以前就是开发者自己敲的一条命令，到了 AI 编程助手这里，就可能变成 Agent 在一个带着 GitHub token、SSH key、云凭据、内部包仓库权限的环境里自动执行的一条命令。那篇文章讲的是依赖安装这个入口，这次 MCP、工具调用、OpenAPI schema、环境变量、云 CLI 这些资料放在一起看，其实是在把同一个问题往外扩：当 Agent 接上工具以后，配置、文档、插件、远程端点、命令参数，都可能变成执行链的一部分。

![Robot hands typing on a laptop with three code windows.](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNghSgZkXFzIPibHBNPpMG63YVGt71puOsqgk5YMRvmTQp7PRPMdnefk9b4sUv9DzZjb6E1VZhElkODlmKrA7sTZNr2zYqr1sfuo/640?wx_fmt=jpeg)

所以这篇文章不是要说“MCP 都不能用”，也不是要把所有 AI 工具都讲成洪水猛兽。恰恰相反，Agent 真正有用的地方，本来就是它能替人做事：读仓库、跑命令、查接口、接系统、调工具、修 bug、出报告。问题在于，一旦它开始做事，我们就不能再用“聊天框”的眼光去管理它，而要把它当成一个有执行能力、有身份、有网络、有文件系统访问能力的工程角色来看。

风险其实一直都在，只是我们缺少的是捕捉风险的嗅觉和意识。

01

![](https://mmbiz.qpic.cn/mmbiz_gif/ynvNmx6iaYulNXplOC3b49IP9XvkxTT5MkVOd6yKQER9WKm4fpbCp7jMgZYAjK5EOGy8icKWEcym3pyvmfRIBO7nwmUMHK5ekNCYGn2upwXgs/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/9H1ro59kcPliaTF8vFaiayibdHWWoqAxh5YPOnT5icv0K6j3iccE6uFozv4sCzsBZmGaC2e6Uy9WEnDdy7gtlibdGpHkOOY5fqtCkrMSv1gqiazSjk/640?from=appmsg)

总结一下最近我观察到的安全资讯，主要围绕MCPstdio、PraisonAI、FrontMCP、nginx-ui、aws-mcp-server，还有一些 GitHub Copilot / VS Code / cloud agent 相关的治理信息。单独看每一条，好像都是某个产品、某个组件、某个配置点的问题。但如果把它们放在一起，其实在讲一件事情，Agent 接工具以后，风险不再只来自模型输出，而来自“输入如何一路走到真实动作”。

援引THN的这篇文章：https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bDXeDicPJYksw9TK8uDejxLmhP53XrWA1fhM18VKaKcdHAmiba0zsaVjD1Yaryfe0PiaFibXxlKqebNo4HRNLaRNUtf6ujkiaFWo5HiczFZpRklqA/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibWAX0Xtd3AZKU6S2CfXaqQfV29ibK3RcCRupDM2xia8w8lnh3IYMF81ia40YdFBaeWmBBeIjicCXYicZqY6RWdEbFtKcCDicN8xjt1TEpvl0agmQg/640?from=appmsg)

This flaw enables Arbitrary Command Execution (RCE) on any system running a vulnerable MCP implementation, granting attackers direct access to sensitive user data, internal databases, API keys, and chat histories; OX Security researchers Moshe Siman Tov Bustan, Mustafa Naamnih, Nir Zadok, and Roni Bar said in an analysis published last week.

OX安全研究人员Moshe Siman Tov Bustan、Mustafa Naamnih、Nir Zadok 和 Roni Bar在上周发布的一份分析报告中表示：“该缺陷可以在任何运行易受攻击的 MCP 实现的系统上执行任意命令执行 (RCE)，从而使攻击者能够直接访问敏感用户数据、内部数据库、API 密钥和聊天历史记录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J1BCKLh6tPjibhb1jFkNAiafWbL7CickTQWc4C2kIR3eicUMNicnnIb5y8OlxiajAFYpCm7jicxy6G8ou9dMWHI2adbhLx4icjAmXdc6AQwyQ28k8mk/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2IBT24MaWRvK78ycQKVLHicjwiczWP1ibm1sqdlpaH9m4icQSYKoBPSo0LrIASV3dUnCV4DDVDmbP9HUTxN0xAlNuLRPZvtmH2cSNq2gAW2IdIc/640?from=appmsg)

比如MCP stdio这件事，如果不用安全术语说，它其实很简单。所谓stdioserver，本质上就是配置里写了要启动哪个本地程序、带哪些参数，然后 Agent 通过标准输入输出和这个程序通信。正常情况下，这就是一种工具连接方式；但如果这段配置来自仓库、插件市场、用户输入，或者能被第三方内容影响，它就不能只被当成“连接配置”看了，因为配置里那行command和args最后真的会变成本机进程。

过去开发者自己接工具，至少会瞄一眼启动命令是什么、要不要跑、会不会带奇怪参数。Agent 工作流里，这个动作经常被包装成“自动发现工具”、“自动接入能力”、“帮我把这个项目跑起来”。从效率上看，这当然很顺手；从安全上看，这就是把“配置”放进了“执行”前面，中间如果缺少校验、隔离和确认，就很容易出问题。

PraisonAI 这类环境变量继承问题也是一样。

```
# src/praisonai-agents/praisonaiagents/mcp/mcp.py
env = kwargs.get('env', {})
if not env:
    env = os.environ.copy()
```

很多运行时启动子进程时，会默认把父进程的环境变量传下去；在普通脚本里，这个行为大家习以为常，但放到 MCP server 或 Agent 工具里，它就变成了一个很现实的凭据边界问题。父进程里可能有OPENAI*API*KEY、GitHub token、数据库连接串、云厂商临时凭据、内部服务地址，结果你只是想给 Agent 加一个工具，却顺手把这一串身份材料也带给了新启动的 server。

这类问题未必需要传统意义上的 RCE 才危险。攻击者如果能影响你接入的 MCP server，或者让 Agent 在不该启动工具的环境里启动工具，那么它不一定要先“打穿主机”，只要拿到进程继承下来的环境变量，就可能已经拿到了足够有价值的东西。很多时候，攻击者想要的也不是一台机器的控制权，而是这台机器上已经存在的身份。

FrontMCP 的OpenAPI $ref 也可以在这里一起讨论。参考https://github.com/agentfront/frontmcp/security/advisories/GHSA-v6ph-xcq9-qxxj。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bDXeDicPJYksw9TK8uDejxLmhP53XrWA1fhM18VKaKcdHAmiba0zsaVjD1Yaryfe0PiaFibXxlKqebNo4HRNLaRNUtf6ujkiaFWo5HiczFZpRklqA/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibWAX0Xtd3AZKU6S2CfXaqQfV29ibK3RcCRupDM2xia8w8lnh3IYMF81ia40YdFBaeWmBBeIjicCXYicZqY6RWdEbFtKcCDicN8xjt1TEpvl0agmQg/640?from=appmsg)

The `mcp-from-openapi` library uses `@apidevtools/json-schema-ref-parser` to dereference `$ref` pointers in OpenAPI specifications without configuring any URL restrictions or custom resolvers.A malicious OpenAPI specification containing `$ref` values pointing to internal network addresses, cloud metadata endpoints, or local files will cause the library to fetch those resources during the `initialize()` call. This enables Server-Side Request Forgery (SSRF) and local file read attacks when processing untrusted OpenAPI specifications.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J1BCKLh6tPjibhb1jFkNAiafWbL7CickTQWc4C2kIR3eicUMNicnnIb5y8OlxiajAFYpCm7jicxy6G8ou9dMWHI2adbhLx4icjAmXdc6AQwyQ28k8mk/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2IBT24MaWRvK78ycQKVLHicjwiczWP1ibm1sqdlpaH9m4icQSYKoBPSo0LrIASV3dUnCV4DDVDmbP9HUTxN0xAlNuLRPZvtmH2cSNq2gAW2IdIc/640?from=appmsg)

很多团队会把 OpenAPI schema 当成接口说明书，觉得它只是文档，用来生成 MCP 工具很自然。但 $ref 这类外部引用如果默认被解析器递归处理，事情就不只是“读文档”了。攻击者控制一份 schema，就可能让服务器去访问内网地址、云 metadata endpoint，甚至本地文件路径；表面上是工具生成流程，实际上已经触发了网络请求和文件读取。

再看 nginx-ui 和 aws-mcp-server，问题就更直观明了了。MCP HTTP 端点如果认证和白名单逻辑没站住，后面连着的可能就是 Nginx 配置读写、服务重载甚至反代规则修改；另一个是 cloud-tool MCP server 把 Agent 参数送进 AWS CLI，一旦参数处理出问题，风险就不只是“某个小工具命令注入”，而是把不可信输入带进云账号、profile、临时凭据和基础设施权限附近。

这些案例虽然不属于同一类漏洞，也不能简单粗暴地说它们影响范围一样，但它们共同提醒我们：AI Agent 的输入不只有 prompt，像工具配置、schema、manifest、远程端点、仓库文件、依赖元数据、CLI 参数这些我们熟悉的使用对象，都会成为输入。同样，AI Agent 的输出也不只有回答，启动进程、发请求、读文件、改配置、调云 CLI、重载服务，也都会成为输出。

那么，本文的重点就来了。

02

![](https://mmbiz.qpic.cn/mmbiz_gif/ynvNmx6iaYulNXplOC3b49IP9XvkxTT5MkVOd6yKQER9WKm4fpbCp7jMgZYAjK5EOGy8icKWEcym3pyvmfRIBO7nwmUMHK5ekNCYGn2upwXgs/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/9H1ro59kcPliaTF8vFaiayibdHWWoqAxh5YPOnT5icv0K6j3iccE6uFozv4sCzsBZmGaC2e6Uy9WEnDdy7gtlibdGpHkOOY5fqtCkrMSv1gqiazSjk/640?from=appmsg)

攻击者不会只盯着模型怎么回答

如果我是攻击者，今天看一个 Agent 系统，未必会先研究怎么把模型骗到胡说八道。模型越狱当然有价值，但如果这个 Agent 已经能启动本地工具、解析外部 schema、访问内网、读取工作目录、继承环境变量、调用云 CLI，那更现实的路径是：我能不能影响它接下来的动作。

这也是我觉得很多团队容易低估的地方。大家会很认真地讨论系统提示怎么写、模型输出怎么审核、敏感词怎么过滤，但对“Agent 最后执行了什么”反而没有同样重视。攻击者不一定要让模型说出“我要泄露秘密”这种明显违规的话，他可以让一切看起来都像正常工作：这个项目依赖有问题，你装一下；这个接口文档导不进去，你解析一下；这个 MCP 工具接不上，你按这个配置启动一下；这个云资源查不到，你用 AWS CLI 看一眼。

这些话都不像攻击语句，反而像日常研发协作里的正常需求。Agent 一旦照着做，后面接触到的就不是一句回复，而是文件、网络、凭据、内网、云资源和管理面。过去开发者看到一个陌生仓库、陌生配置或者陌生工具，多少会有一点直觉上的犹豫。但是Agent 如果没有被设计成在关键转折点停下来，它会把这些动作当成完成任务的一部分。

所以我现在看Agent安全，会先问几个很土但很有用的问题：谁能影响它的工具配置？它启动工具时带了哪些环境变量？它解析外部文档时能不能访问内网？它调用 CLI 时用的是什么身份？它运行在一次性沙箱里，还是运行在开发者真实工作目录里？它能不能任意出网？执行日志能不能还原它到底做过什么？

这些问题听起来没有“模型攻防”那么新鲜，但更接近真实风险。因为模型说错一句话，最多生成一段烂代码；Agent 带着真实权限做错一个动作，后面可能就是把token、云账号、服务配置和生产环境置于险地。

03

![](https://mmbiz.qpic.cn/mmbiz_gif/ynvNmx6iaYulNXplOC3b49IP9XvkxTT5MkVOd6yKQER9WKm4fpbCp7jMgZYAjK5EOGy8icKWEcym3pyvmfRIBO7nwmUMHK5ekNCYGn2upwXgs/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/9H1ro59kcPliaTF8vFaiayibdHWWoqAxh5YPOnT5icv0K6j3iccE6uFozv4sCzsBZmGaC2e6Uy9WEnDdy7gtlibdGpHkOOY5fqtCkrMSv1gqiazSjk/640?from=appmsg)

Prompt难道没用吗？

当然，我肯定不是说 Prompt 没用。

你当然应该告诉 Agent 不要泄露秘密、不要随便执行危险命令、遇到敏感文件要停下来确认，也应该让它在不确定的时候先解释风险再动手。但这些东西更像提醒，不像护栏，这是软边界，不是硬边界。在我看来，真到了执行链路里，能不能兜住风险，主要还是看环境隔离有没有收住。

我看到很多少侠在使用AI Agent时有个很典型的误区，他们把 Agent 的安全策略写得很漂亮，但执行环境却非常宽松。Agent 运行在工程师真实目录里，里面充斥着.env、SSH key、Git credential、云 CLI 登录态、私有包仓库 token、Docker 登录态、kubeconfig。

在这种条件下，Agent可以随便访问公网，也能访问内网，还能启动本地进程、解析外部 schema、接第三方 MCP server。

作为攻击者来说，哪怕你的系统提示写了十遍“不要泄露秘密”，他只要找到一条能影响工具执行的路径，风险仍然会发生到这些真实资产上。

因此更稳的做法，应该是先把 Agent 的执行环境当成一个小型工程系统来设计。陌生仓库和外部 PR 默认进一次性沙箱；依赖安装和工具启动默认不带生产凭据；OpenAPI schema、MCP 配置、manifest、插件包都按不可信输入处理；网络出口默认最小化，能访问包源不等于能访问任意公网，能访问公网也不等于...