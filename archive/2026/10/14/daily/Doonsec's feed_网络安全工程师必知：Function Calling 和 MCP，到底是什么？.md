---
title: 网络安全工程师必知：Function Calling 和 MCP，到底是什么？
url: https://mp.weixin.qq.com/s/_PNbelDzpFYFT-bhZhdapw
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:15.742146
---

# 网络安全工程师必知：Function Calling 和 MCP，到底是什么？

# 网络安全工程师必知：Function Calling 和 MCP，到底是什么？

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 过去，我们使用 AI，主要是让它回答问题、分析日志、编写代码。但现在，AI 不仅能思考和回答，还能调用工具、查询数据库、执行命令，甚至串联多个系统完成任务。

例如，让 AI 分析一段 Web 访问日志，它可以进一步调用日志平台查询数据、使用威胁情报接口核验 IP，再生成安全分析报告。

**AI 从“会回答”走向“能干活”，背后有两个值得网络安全工程师重点关注的技术：Function Calling 和 MCP。**

## 一、Function Calling：让 AI 学会调用工具

Function Calling，通常翻译为“函数调用”或“工具调用”，是让大模型能够按照约定的格式，提出调用外部函数或工具的请求。

需要注意：**大模型通常负责决定调用什么工具、传递什么参数，真正执行函数的是外部程序，而不是模型本身。**

以安全运营为例，工程师希望 AI 查询某个 IP 的威胁情报。系统可以预先定义一个查询函数，要求输入 IP 地址并返回查询结果。

典型流程如下：

1. 用户提出问题：“帮我查询这个 IP 是否存在恶意行为。”
2. 大模型判断需要调用威胁情报查询函数。
3. 模型按照约定的参数格式输出调用请求。
4. 应用程序校验参数和权限，执行查询。
5. 查询结果返回给大模型，由模型分析并生成结论。

Function Calling 解决的核心问题是：**如何让大模型按照结构化约定，调用外部能力。**

在网络安全领域，它可以用于日志查询、漏洞信息检索、资产查询、告警分析、工单创建，以及调用自动化响应接口等场景。

## 二、MCP：让 AI 更方便地连接外部工具

如果说 Function Calling 解决了模型如何提出工具调用请求，那么 MCP（Model Context Protocol，模型上下文协议）关注的是：**AI 应用如何以统一的协议连接外部工具、数据和上下文资源。**

MCP 由 Anthropic 于2024年推出，采用客户端—服务器架构。一个 MCP Server 可以向 AI 应用提供三类主要能力：

* **Tools（工具）**：执行操作，例如查询漏洞、检索日志。
* **Resources（资源）**：提供数据，例如安全知识库、配置文件。
* **Prompts（提示模板）**：提供可复用的提示模板。

举个例子，一家企业有多个安全系统：SIEM、安全资产管理平台、漏洞扫描平台和工单系统。过去，开发者可能需要为不同 AI 应用分别编写各系统的对接代码。

通过 MCP，可以为这些系统提供标准化接口，让支持 MCP 的 AI 应用更方便地发现和使用相应能力，减少重复集成工作。

但要注意，MCP 并不意味着所有系统接入后就能自动互通。实际使用仍然需要开发或部署 MCP Server，并处理身份认证、权限控制、数据格式和兼容性等问题。

## 三、Function Calling 和 MCP 有什么区别？

两者并不是竞争关系，而是解决不同层面的问题。

| 对比维度 | Function Calling | MCP |
| --- | --- | --- |
| 核心作用 | 让模型提出工具调用请求 | 标准化 AI 应用与外部能力的连接 |
| 关注重点 | 调用什么、传递什么参数 | 如何发现、连接和使用工具及资源 |
| 主要参与者 | 模型、应用程序、函数或工具 | MCP Host、MCP Client、MCP Server |
| 典型用途 | 让 AI 查询 IP 威胁情报 | 让 AI 应用通过统一协议连接威胁情报服务 |
| 两者关系 | 可以作为工具调用机制的一部分 | 可以承载工具定义与调用交互 |

需要特别说明：MCP 并不等于 Function Calling，也不取代大模型自身的工具调用能力。MCP 负责协议层面的连接与交互，而模型如何选择工具、如何生成调用请求，仍取决于 AI 应用和模型的具体实现。

## 四、网络安全工程师必须关注的三个风险

当 AI 可以调用工具，它就不再只是一个聊天窗口，而可能成为能够访问企业数据、执行操作的智能体。新的能力也意味着新的攻击面。

**第一，工具权限过大。**

如果 AI 能直接执行系统命令、修改防火墙策略或删除数据，一旦模型判断错误，或者被恶意指令诱导，就可能造成真实损失。

建议遵循最小权限原则，对高风险操作设置审批、隔离和审计机制。

**第二，提示词注入与工具滥用。**

攻击者可能在网页、邮件或文档中植入恶意指令，诱导 AI 调用不该调用的工具，尝试读取敏感数据或执行越权操作。

不能因为请求来自 AI，就默认它是可信的。所有工具调用都必须在服务端进行权限校验。

**第三，MCP Server 和工具供应链风险。**

恶意或存在漏洞的 MCP Server，可能成为数据泄露、凭据窃取和越权操作的入口。

企业应核验服务来源，审查工具实现，保护 API 密钥，限制网络访问，并持续监控工具调用行为。

## 五、未来：安全工程师要学会构建“可控的 AI”

Function Calling 让 AI 能够调用工具，MCP 则让外部工具和数据能够通过更标准化的方式接入 AI 应用。两者共同推动 AI 从内容生成走向任务执行。

对于网络安全工程师而言，这不仅意味着可以利用 AI 提升安全运营、漏洞分析和应急响应效率，也意味着必须重新审视传统安全边界。

过去，我们重点保护 API、数据库、服务器和业务系统；现在，还需要关注 AI 能调用什么工具、能够访问哪些数据、如何获得授权，以及每一次操作是否可追溯。

**AI 时代，安全的关键不只是让模型更聪明，而是让它在正确的权限下，执行正确的操作，并且始终处于可控、可审计的边界之内。**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/buQYO9JqQcqHibMSbuUlH1q4N0BqiaJT4A81RZWbGMibEU57wlC7W6ryRDOF3vnn8UEfjlTdxeyEovsOzIibw7B11Xp7353IVMKgugHfLB4YWic4/640?from=appmsg)

END

**推荐阅读**

[网络安全人士必知的AI Agent网络攻防能力基准测试框架BountyBench](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494039&idx=1&sn=87bb44dc7cad9b7270a3aee5bb2f4c92&scene=21#wechat_redirect)

2026-10-13

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQV9j1RxNqeu0QtdesoVViaEick0eicEzR5nUibZ40uz7L4jRjPRZ6QRWVKxibnB3UctczGjiaelxC8MrEGiaFfV5kOCU2TRwyLvGic6tc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494039&idx=1&sn=87bb44dc7cad9b7270a3aee5bb2f4c92&scene=21#wechat_redirect)

[一文讲透 SCA 与 SBOM：软件供应链安全，为什么两者缺一不可？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494031&idx=1&sn=6eeaf68397e78efa5250f925ca23c698&scene=21#wechat_redirect)

2026-10-12

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQ1S4zvgwqIews6QfiaVXorP1JFekx0ib6vbiakv88zWouskj0vUlSTcRFV5fswkWTaMZvS6Xd21QibV3neY6iabWzYdicEDlT6f5Q04/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494031&idx=1&sn=6eeaf68397e78efa5250f925ca23c698&scene=21#wechat_redirect)

[Anthropic 免费开放 AI 漏洞扫描：开源软件安全，正在进入 AI 自动化时代](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494024&idx=1&sn=2cc3ebdedd571e5e963dbe7e61c3233c&scene=21#wechat_redirect)

2026-10-11

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTDwWee5lMdACwkY16N28MRa5Q9gQQQWOk4ic94YWzmVCH7SExe9G6aT649GGQbr5jcusibhnbO5KAGg4JiaxOPVpSB0A9xt4j4KE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494024&idx=1&sn=2cc3ebdedd571e5e963dbe7e61c3233c&scene=21#wechat_redirect)

[网安人必看！REA 开源工具，让 AI 直接参与软件逆向分析](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494018&idx=1&sn=32fd85c8956a1d070d22eb90b66171be&scene=21#wechat_redirect)

2026-10-10

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQq3NnVDV3e4nF7icgiaZicFRssngqyx9r41neD5JEqmKXlrQzg7iahUyxg6w2utKiaCJicnkMVWpGib1iap4zR3uWZ0cDzJEmy3wic1XbA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494018&idx=1&sn=32fd85c8956a1d070d22eb90b66171be&scene=21#wechat_redirect)

[湖南网信办约谈4家大模型企业：安全不是上线后的补丁](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494013&idx=1&sn=34051aafe36f02b173ed5f1c317a7381&scene=21#wechat_redirect)

2026-10-09

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibRqBo8t8I3wv8MxfAMJnbXO7hG3zW70LI80HLTxYBoclSKjI6J6PCuTJuabibpNDUxibSVHff0y0WMtCpaiaJYtibsl0YhBUM3qcJo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494013&idx=1&sn=34051aafe36f02b173ed5f1c317a7381&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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