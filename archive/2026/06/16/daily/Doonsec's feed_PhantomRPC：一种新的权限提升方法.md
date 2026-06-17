---
title: PhantomRPC：一种新的权限提升方法
url: https://mp.weixin.qq.com/s/Qm3OattHX5a7kqg1GkLO-A
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:01:33.518837
---

# PhantomRPC：一种新的权限提升方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HCYvjoz7ibx0AsTtocsyvWKfDHTPpCOia9qDsleUpveOVDfrgLibRQSBDjdrKa9Jva4UxrTnNTRcskFuQc3zDZBcpU7C66KIia0mQ/0?wx_fmt=jpeg)

# PhantomRPC：一种新的权限提升方法

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Gh5cAG33vnStCpiaGpcSMkXa0WQDuxlTu1pqTxUzg8CtDGrKg74ZuOAagkxmN2cfTeic6KJsyJhT15q1OEwgHzhockGEp48J1YM/640?wx_fmt=jpeg&from=appmsg)

Windows 架构带来了一个新的惊喜，或者更确切地说，是在一项旧技术中带来了一个新的攻击面。

Windows 系统中的进程间通信依赖于RPC（远程过程调用），这是一个复杂的机制，多年来不断有漏洞被发现。我们的专家 Khaydar Kabibo 长期研究 RPC 安全，他发现了一种新的本地权限提升架构途径，并将其命名为 PhantomRPC。

* 该技术的本质是：攻击者设置一个伪造的 RPC 服务器，该服务器使用与合法服务器相同的 UUID/端点响应客户端请求，然后它调用RpcImpersonateClient，这使得服务器线程能够模拟调用客户端的安全上下文，直至 SYSTEM。
* 关键条件：攻击者的进程必须拥有权限SeImpersonatePrivilege（通常适用于网络服务或本地服务帐户）。在这种情况下，如果合法的 RPC 服务器不可用（例如，当相应的服务被禁用时），则有可能提升到 SYSTEM 或管理员级别。

这并非特定服务（例如 Potato 系列服务）的漏洞，而是由于 RPC 运行时未验证 RPC 服务器的合法性，导致其他进程将同一端点注册为合法服务器。在某些情况下，还需要满足额外的环境条件（例如，存在特定的 GPO 配置）。

所有描述的提权路径均已在安装了当时最新更新的 Windows Server 2022 和 Windows Server 2025 上进行了测试。作者指出，由于这是一个架构问题，因此该漏洞也可能被其他版本的 Windows 系统利用。

在补丁发布之前可以做些什么：

— 尽量减少SeImpersonatePrivilege非标准/自定义流程（如果不需要则删除）；

— 如果可能，启用基于 RPC 的合法服务，以便其 RPC 端点由合法服务器占用；

— 启用 ETW 对 RPC 事件的监控，并跟踪RPC\_S\_SERVER\_UNAVAILABLE来自高权限客户端的错误，以便在实际执行之前检测到冒充尝试。

因此，PhantomRPC 在 Windows RPC 中开辟了一个新的攻击面，需要使用此协议的管理员和应用程序开发人员持续关注。

更多详细信息，包括代码示例和利用方案，请参阅文章“ PhantomRPC：Windows RPC 中的一种新的权限提升技术”。https://securelist.com/phantomrpc-rpc-vulnerability/119428/

> 该报告也被列入今天在新加坡举行的Black Hat Asia 2026大会的议程中。
>
> https://blackhat.com/asia-26/briefings/schedule/#phantomrpc-a-new-privilege-escalation-flaw-in-windows-rpc-50806

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0G9JUDE6Y4vZuWia1uMvVYEB4HA6a59m7SJw8FE8g7ulfozVvZiblKiaI1VT9QOx7yFT7OTyTeNZF57OPRib75TsjeUBmtShKdpLyQ/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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