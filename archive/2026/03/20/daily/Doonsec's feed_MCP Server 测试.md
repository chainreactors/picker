---
title: MCP Server 测试
url: https://mp.weixin.qq.com/s/cPNNAwoxDHFExqbiwS1U_Q
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T03:59:07.585154
---

# MCP Server 测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0UKPAuBeu7n0Vyia6iaeicAOqicZ4xUcBUxRgXKv3Jx7YvJDtrW0P4wr19dUfjVibbV86IhjyeCkXM7jD7icYRCXQPdUYTWnxPWeQuiaJdOEmBBpNg/0?wx_fmt=jpeg)

# MCP Server 测试

原创

何以解忧
何以解忧

联想全球安全实验室

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/INRb4MCKe9bhnicMvBELYsSpnCErDzKAEMfaFkUPEN5zdqq6T1H2VuZl7uUT2XeTCpxVNFx82btNIubBLNtI6Ig/640?wx_fmt=png)

**一**

**什么是MCP**

![](https://mmbiz.qpic.cn/mmbiz_gif/BBRxEeqtefiasDDcyfCQljnDRl7m4lTHtCtYNRibqYCjL7iaicc5wNoUCFxBumIrwulmjAOsyJpGkYxeLXaI07D4RA/640?wx_fmt=gif)

MCP（Model Context Protocol，模型上下文协议）是一套开放的标准协议，用来让大模型应用（Host，如 Claude Desktop、IDE 插件等）以一种统一、可扩展、可组合的方式连接外部能力，从而把模型 “上下文” 和 “可用工具” 安全、结构化地接入进来。

MCP 所解决的问题是：不同工具/数据源（本地文件、数据库、SaaS、内部系统等）各自有不同的接入方式，集成成本高且难复用。MCP提供统一接口，让一次实现可在多个Host里复用。

模型上下文协议（MCP）遵循  Client-Host-Server 架构，每个主机可以运行多个客户端实例，下图为 MCP 核心组成部分示例图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7nL2W5eAKMKRHTYudeEogrnYot1FXtuvQ5asJslW9BcfSWU8UIesBVrvPP4GHwQD8OHsiaYRwbC5olT4ukcjbLicoO7HibowRvVeE/640?wx_fmt=png)

MCP 各核心组成部分：

**MCP Host**：协调和管理一个或多个 MCP Client 的 AI 应用，如 Claude Desktop、Cursor、IDE 等，即实现了通过 MCP 协议和 MCP Server 通信、调用 MCP Server 所提供能力的 AI 应用。

**MCP Client**：负责维护与 MCP Server 的连接，并从该 MCP Server 获取上下文供 MCP Host 使用， 即一个实现了 MCP 协议、可与 MCP Server 进行通信的 Client。

**MCP Server**：提供上下文与能力的服务端程序，对外暴露 tools/resources/prompts 等能力，并接收客户端调用请求返回结果

**二**

**如何测试MCP Server**

![](https://mmbiz.qpic.cn/mmbiz_gif/BBRxEeqtefiasDDcyfCQljnDRl7m4lTHtCtYNRibqYCjL7iaicc5wNoUCFxBumIrwulmjAOsyJpGkYxeLXaI07D4RA/640?wx_fmt=gif)

对于 MCP Server 的测试，可以根据 MCP Server 暴露位置的不同，采取不同的方式进行测试。

常见的业务场景中，MCP Server 的部署位置一般有以下两种：

1. MCP Server 部署于 Agent Server 一侧，只提供给内部 Agent Server 使用，外部无法直接访问，需要通过 Agent Client 进行调用。对于一些提供了如订阅、查询/创建订单、工单操作等能力的 AI Agent，为了保护 MCP Server 中可能使用到的 API 接口、凭据等信息，MCP Server 一般选择这种部署方式。

以 [Agent Zero](https://github.com/agent0ai/agent-zero) 项目架构为例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7n3y66IIwaSpGXHgnicDSicIChFIPw7rTErCpoL7FgmOM8LFChibpjnNzgvl5kyvqJNq4dRAdQbZbFttjX5XqibKdLe8xYia3XdzpZ0/640?wx_fmt=png)

对于部署于 Agent Server 一侧的 MCP Server，在测试时，通过提示词获取当前 Agent 所具有的能力，可以调用的工具及需要提供的参数。

如下图示例，可以看到通过提示词可以获取到当前 Agent 加载的 MCP tool及其参数信息。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7lwUX7uGOHXK7hDywtbVwNnEHkNKJUbbjWoZRa26yLaG7Ntql5HMT1rD3f7y8cicCq84nDVicd1PtD0Ovibicv9cpIiax3fmudVV3FY/640?wx_fmt=png)

2. MCP Server 部署于用户可以直接访问的位置，如通过 http 服务直接暴露给用户，或用户可以通过下载执行文件在本地运行的 MCP Server。常见的，用户通过 IDE、Claude 等工具配置的加载的自定义 MCP Server 均属于这种部署方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7lRF3WQk8rHeQQMCG9HDdbqsMVWrohT2gibPfOCrLrRAdO9EbJ67rzOY03vdribKU79SJXial10yDYOpougE6HcnS3vTHGnHlZqxs/640?wx_fmt=png)

对于部署于用户可以直接访问位置的 MCP Server，可以通过官方提供的 MCP SDK 编写 MCP Client 对 MCP Server 进行调用测试，同时官方也提供了 MCP Server的调试工具 [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) ，通过 MCP Inspector 可以方便的对 MCP Server 进行测试，直接获取和调用 MCP Server 提供的 tools/resources/prompts，这样做的好处是，在测试MCP Server时，不需要加载调用大模型服务，不需要消耗 token，只需要按照正常的 web 接口测试即可。

**三**

**MCP Inspector的使用**

![](https://mmbiz.qpic.cn/mmbiz_gif/BBRxEeqtefiasDDcyfCQljnDRl7m4lTHtCtYNRibqYCjL7iaicc5wNoUCFxBumIrwulmjAOsyJpGkYxeLXaI07D4RA/640?wx_fmt=gif)

1. 下载安装 node

2. 运行 MCP Inspector

```
```shell下载 MCP Inspector 到当前目录npm install @modelcontextprotocol/inspector运行 MCP Inspectornpx @modelcontextprotocol/inspector```
```

如下图为运行成功，通过浏览器访问即可打开MCP Inspector，如有对 MCP Client 和 MCP Server 通信进行抓包的需求，可以使用 Proxies 将 node 进程的请求代理到 BurpSuite，为解决 node 证书验证问题，可以设置环境变量 NODE\_TLS\_REJECT\_UNAUTHORIZED="0"，此处使用windows powershell 进行配置环境变量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7mC7ame8FibibIywtaIesVs5vibx8U8ickWvuxQDIDmSuibjXmkHW1dEhTNzUKaf7R5Ia5tqEWMg8pz5UufyHJFia3ITGp85crFa4zIQ/640?wx_fmt=png)

如下图所示，Transport Type 是 SSE 或者 Streamable HTTP，只需要填写对应的 URL 即可，当前使用的测试环境（[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server/tree/main)），连接 MCP Server 后即可通过右侧的工具，列出该 MCP Server 提供的所有 tools/resources/prompts，此处通过调用获取 resource，可以看到当前 MCP Server resources 中暴露了系统凭据信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7nPlBsaibcZdRxHiczeYnETQaC7ia4licfzvSib0ufqCdibqkDAgfichXU6g4vjeFWpJCzkdlhwz2gXGzOSAa3ib5ZzXg5Ed1mkpSFKrY0/640?wx_fmt=png)

当 Transport Type 为 stdio 时，根据 MCP Server Config 中的启动命令进行配置 Command 和环境变量即可。

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7k6z4NRo8jnaBZJzfS6ibkxTAbkWBiaCRskpREW7JUVsk5LiaO5l5BsSMaibYnhjm1dn8unBCmoLWpuuoZGfk91szsAQFaPVNiacs48/640?wx_fmt=png)

如使用 [Amap Maps MCP Server](https://mcp.so/server/amap-maps/amap?tab=content)，根据其提供的 MCP Server Config 在 MCP Inspector 设置 Command 即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7k47iaY98LXCbgYdGXEuXDDxZO7RiaQb4icG7gN8mFEnPNcibaO6PbCiblA9mAxhdRxxjJnMjqRTFiaj8fq7TibCEmjwQaf99UmMiaQHxU/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7mXmmp59jqxewpybGr7wCbiakiaZoCC64kbngn47Jl9fA1qaB49Oib22mOJuicJ42sXSfoaURO6JGhvMW9m6vIsScOfkphib8rDc4zY/640?wx_fmt=png)

如上图，对于 Stdio 方式的 MCP Server，若为 nodejs、python等类型，可以容易获得 MCP Server 的到源码 ，除了通过 MCP Insecptor 进行测试，还可以对其进行源码审计，下载对应的 MCP Server 包即可。除了 nodejs、python 类型，有些 MCP Server 是 exe 等二进制程序，同理的，为了更直接的获取其提供的 tools/resources/prompts 并测试，直接在 MCP Insecptor Command 中指定可执行程序 exe 的绝对路径即可。

**参考链接**

![](https://mmbiz.qpic.cn/mmbiz_gif/BBRxEeqtefiasDDcyfCQljnDRl7m4lTHtCtYNRibqYCjL7iaicc5wNoUCFxBumIrwulmjAOsyJpGkYxeLXaI07D4RA/640?wx_fmt=gif)

https://modelcontextprotocol.io/docs/learn/architecture

https://modelcontextprotocol.io/docs/tools/inspector

https://github.com/harishsg993010/damn-vulnerable-MCP-server/tree/main

**往期精彩合集**

●[跨层残差绕过LLM内生安全](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493556&idx=1&sn=f8237130ba8216d7d3b398272c28b6a5&scene=21#wechat_redirect)

●[模块化机房建设踩坑纪实](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493543&idx=1&sn=444f0e8922c8968fc3447dc38f154215&scene=21#wechat_redirect)

●[App 接口安全：被低估的系统安全边界](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493510&idx=1&sn=5cac29cd413f33b84d74e7e0946ff37d&scene=21#wechat_redirect)

●[在智子的监视下，如何好好的聊天？Signal协议简介](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493450&idx=1&sn=c1dee7b3dabf3a5ef88eb5001d065595&scene=21#wechat_redirect)

●[小心你的路由器 —— UPnP 协议分析](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493424&idx=1&sn=199b5933ea6cd2bd29dde05e3419f7ca&scene=21#wechat_redirect)

**长**

**按**

**关**

**注**

联想GIC全球安全实验室（中国）

chinaseclab@lenovo.com

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0UKPAuBeu7nvDILy1MnoDiakNIBOeEwc1Cds2qGQXbqqlHbc9dSTPic1Gybk2HibNtvBbgQV9CB0I6ib4Mv2GKxERwKe1E6RYkDk2XfeSbLung0/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

联想全球安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

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