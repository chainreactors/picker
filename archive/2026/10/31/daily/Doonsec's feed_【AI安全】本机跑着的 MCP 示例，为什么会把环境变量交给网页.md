---
title: 【AI安全】本机跑着的 MCP 示例，为什么会把环境变量交给网页
url: https://mp.weixin.qq.com/s/gbCIvRqBjCKoNKVOIJpqXA
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:19:07.507270
---

# 【AI安全】本机跑着的 MCP 示例，为什么会把环境变量交给网页

# 【AI安全】本机跑着的 MCP 示例，为什么会把环境变量交给网页

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 一、浏览器里的陌生页面，碰到了本机的测试服务

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRfXjn7mlVAsUoKuTGMxdYvvniaFTLVl83nlb9v8aw8WAsltZFh7yQn17eSSezP2f3QLXMHgicdWmOPZ9tav38xymhe2eCTibqRjQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzU2NDgxNQ==&mid=2247488841&idx=1&sn=6980ae43228319cdcdb598f74cffedda&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

🧪 想象一个开发场景：你在电脑上试用 MCP 工具，终端里保留着项目的 API 密钥，浏览器同时开着查资料的页面。MCP 是让 AI 客户端调用外部工具的一套协议；示例服务器则像工具演示台，方便观察这些调用怎样工作。

这里最容易漏掉的角色，是浏览器页面。开发者知道自己启动了什么程序，却未必会把“刚打开的网页”也算进这个程序的潜在调用者。只要演示台另外开出了 HTTP 网络入口，就需要重新回答：谁能连进来，谁能读结果？

10 月 25 日，MCP 官方 servers 仓库发布 GHSA-mvf5-2qqv-rg3c：`server-everything` 的受影响 HTTP 传输缺少鉴权、使用宽松跨源配置，`get-env` 工具会返回进程环境变量。公告将其评为中危，修复版本是 **2.0.1**。

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHQLuUhddE1f6RrBl3aVvwzQZfkPH7wIv995Wlmc18XXtJYDEhmXkticicMQbLtmib4ko4EF7XiaQmCvKycLHhP09nNF7PEc4FyN4to/640?wx_fmt=png&from=appmsg)

**问题发生在工具服务器的访问边界，不需要先说服模型违背提示词。** 进程环境变量，就是程序启动时获得的一组配置值。它们可能包含访问第三方服务的凭据；演示工具读到什么，取决于该进程实际继承了什么。

🔍 可以用办公室里的打印机理解这个差别：你允许它读取某份文档，不代表经过办公室的任何人都有权向它索取文档。对 MCP 工具也一样，调用格式正确只能说明双方会说同一种协议，不能证明调用者有资格拿到数据。

先把三种经常混淆的判断拆开：

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | 你已经确认的事 | 还需要回答的问题 | | --- | --- | | 程序在自己的电脑上运行 | 是否对网络开放，页面能否访问？ | | 已经完成 MCP 握手 | 服务端是否验证调用者身份？ | | 工具是调试用途 | 返回内容是否包含不该出进程的数据？ | |

> ⚠️
>
> 公告明确区分了传输方式：默认 **stdio 不受本次 HTTP 暴露链影响**。stdio 是客户端通过子进程的标准输入输出交换消息。不能仅凭“装过 everything”就认定已经泄密。

今天第一步应是查启动配置，而非搜集所有密钥的值：确认是否真的启动了 SSE 或 Streamable HTTP，记录实际软件包版本、监听地址和进程身份。不要把生产环境变量完整打印进工单，排查本身也不应制造新的秘密副本。

# 二、四个小边界，怎样连成一次越界读取

🌐 跨源，指网页与它请求的服务不属于同一个来源；来源由协议、主机和端口共同决定。浏览器的 CORS 规则决定跨源页面能否读取响应，服务端鉴权则决定谁有权使用服务，两者承担不同任务。

把这次风险拆成四个连续动作，就容易看见缺口。下面是根据公告整理的机制解释，**本次未独立运行攻击代码，也没有扫描任何真实部署**。

1. **有一条到达服务的路。**

   HTTP 入口让独立客户端能够连接；监听范围决定网络上的哪些位置可能够得着它。
2. **页面获准读取跨源响应。**

   过宽的 CORS 配置让本该隔开的网页获得读取工具结果的机会，具体浏览器行为还受其网络安全策略约束。
3. **请求到达敏感工具。**

   若缺少身份和权限检查，完成协议初始化就可能继续调用工具；会话编号不能自动充当授权凭证。
4. **返回值越过数据边界。**

   工具若直接交出环境配置，调用者拿到的就不只是“测试成功”，而可能是程序赖以访问其他系统的秘密。

**阻断点应放在数据交出之前。** 给模型补一句“不要泄密”，不能替代网络服务拒绝无权调用者；模型甚至可能根本没有参与这条调用链。

🔒 MCP 的传输规范要求 Streamable HTTP 服务验证 `Origin`，建议本地服务只绑定回环地址并配置鉴权。`Origin` 表示请求来自哪个网页来源；回环地址则只在本机网络栈内使用。

这几层防护要分别检查。收紧监听可减少局域网暴露，却不能独自解决本机浏览器发起的请求。限制页面来源可以拒绝不受信网页，但直接发 HTTP 请求的程序不会因为浏览器 CORS 规则而自动失去能力。身份校验回答“你是谁”，工具权限还要继续回答“你能读哪些数据”。

🛠️ 对自己维护的工具，可以先在隔离环境设计一个安全的反向检查：不放真实凭据，用专门的假配置，确认无身份请求在执行工具之前被拒绝、非允许页面来源不能读取结果。检查要记录“在哪层拒绝”，只看到页面报错不足以证明敏感工具没有运行。

到这里，读者应能复述完整关系：陌生网页是潜在调用者，HTTP 服务提供通路，过宽读取规则与缺失授权共同扩大权限，而环境变量工具决定可能流出的数据。是否真实造成损失，还必须结合传输方式、进程配置、可达路径和访问证据判断。

# 三、版本号变小了，升级动作却不能省略

🎯**核心问题：依赖文件已经写入 2.0.1，正在监听的进程却可能还用着旧代码。**

📦 从日期版本迁移时，为什么不能只等常规升级提醒？怎样沿着启动入口找到实际运行的那份安装？

🔒 除了收紧网络入口，调试启动器该传入哪些配置，才能让环境变量工具失去可泄露的真实秘密？

完整稿在 Oxo AI Security 知识星球继续拆解运行态验收和演示凭据管理，把“依赖改了”落实为“当前服务的边界已确认”。

📚**AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛**AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡**AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠**AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHTyDcYibjzbUGJL327LZoTO0Zyq6bdUMbpn91SghUOtXJRd4F3vicV15o2ppct8BIEoUd4BIlXLkhNibn78SrCjoibAXt0bHzXDUAc/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRy2nZH6S7gzEkSbJnlJu1zIywWiaNFSlmNhnylG29ETiatRN7MkD64QPQGpxIiaR9xbVOr7Zhn1TdziaC6KjJnBDHPibFfkJ5OAMGs/0?wx_fmt=png)

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