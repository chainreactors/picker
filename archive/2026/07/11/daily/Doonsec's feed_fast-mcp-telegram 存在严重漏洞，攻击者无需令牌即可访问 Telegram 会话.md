---
title: fast-mcp-telegram 存在严重漏洞，攻击者无需令牌即可访问 Telegram 会话
url: https://mp.weixin.qq.com/s/4zi8UhOhBHv4BVXTOsCvQQ
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:11:00.744645
---

# fast-mcp-telegram 存在严重漏洞，攻击者无需令牌即可访问 Telegram 会话

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zdwoicOrrJb0bu0tWkorgRtSMYQBrB443RQwyEaiauiaJxDR5CsWEBxJICYYjCK84vWaQZ0hfibdmfnANmp6cE0fgOSjVjqltljnrf9aHjUMF2A/0?wx_fmt=jpeg)

# fast-mcp-telegram 存在严重漏洞，攻击者无需令牌即可访问 Telegram 会话

原创

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

fast-mcp-telegram 中的一个严重漏洞（CVE-2026-52830，GHSA-rxw2-pc8j-vxwm）允许攻击者利用磁盘上会话文件解析方式中的路径遍历缺陷，在没有有效持有者令牌的情况下，通过 HTTP 访问 Telegram MCP 会话。

ast-mcp-telegram 是一个 Telegram MCP 服务器，它通过基于会话的身份验证模型将 Telegram 帐户与 AI 助手和 HTTP 客户端连接起来。

在受影响的版本（≤ 0.19.0）中，持有者令牌的验证方式是将原始令牌字符串与会话目录直接连接起来，构建 \*.session 路径，然后检查该文件是否存在。

验证器会去除空格并拒绝保留名称，例如 telegram（文档中将其列为默认的 session\_name）。但是，它不会规范化路径，也不会拒绝路径分隔符和遍历序列。因此，持有者令牌实际上被视为文件系统相对路径，而不是不透明的标识符。

SessionFileTokenVerifier.verify\_token() 中的易受攻击逻辑首先会拒绝小写值出现在保留名称列表中的令牌，包括“telegram”。然后，它会构建会话路径为 session\_dir/f”{token}.session”，如果该路径指向一个现有文件，则接受该令牌。

在 src/client/connection.py 中构建客户端路径时也使用了相同的模式，其中 SESSION\_DIR / f”{token}.session” 被传递给 Telegram 客户端构建器。

至关重要的是，没有任何步骤强制要求解析后的会话路径保持在配置的会话目录中，也没有任何检查拒绝令牌字符串中的 /、\\、.、..、绝对路径或其他遍历结构。

在典型的部署中，MCP 服务器的默认或旧版 Telegram 会话存储在 ~/.config/fast-mcp-telegram/telegram.session 中，并且文档明确保留了 telegram 这个名称，以避免与 stdio 和 HTTP 无身份验证会话发生冲突。

虽然保留名称保护机制正确地拒绝了确切的令牌 telegram，但攻击者可以在 HTTP Authorization: Bearer 标头中提供遍历别名，例如 ../fast-mcp-telegram/telegram。

当与会话目录结合时，此令牌解析为 ~/.config/fast-mcp-telegram/../fast-mcp-telegram/telegram.session，一旦文件系统处理完毕，它就会折叠成相同的默认 telegram.session 文件……因为代码只检查未规范化路径的 is\_file()，所以遍历别名被接受，服务器将攻击者验证为默认的 Telegram 帐户。

这种行为超出了预期的身份验证边界。生产环境中的 HTTP 身份验证部署要求每个客户端提供一个难以猜测、高熵的持有者令牌，该令牌映射到一个唯一的会话文件。此外，保留名称会被屏蔽，以防止 Telegram 等常用令牌与共享会话或旧版会话发生冲突。

路径遍历别名有效地将持有者令牌命名空间转换回文件系统命名空间，允许未经身份验证的客户端通过简单地选择精心构造的相对路径而不是猜测密钥来选择特权默认会话。

一旦通过身份验证成为该帐户，攻击者就可以读取和发送 Telegram 消息、发出 MTProto API 调用，并调用为该会话配置的任何暴露工具和附件表面。

根据账户对工具进行前缀标记的中间件运行在身份验证之后，因此无法修复损坏的边界。一旦遍历令牌被接受为有效的访问令牌，默认账户的带前缀工具就会被列出，并且可以被调用。

同时，未添加前缀的呼叫仍然会被正确拒绝。这证实了该漏洞存在于会话选择和身份验证中，而不是工具前缀强制执行中。

该漏洞影响 fast-mcp-telegram 版本 0.19.0 及更早版本；版本 0.19.1 引入了更严格的验证，将 bearer token 视为不透明标识符，DavidCarliez 在 Gitbub 中报告了此问题。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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