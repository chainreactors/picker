---
title: ghostsurf：从 NTLM 中继到浏览器会话劫持
url: https://mp.weixin.qq.com/s/fZK821MJLl2YsJYk6N-wpQ
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:50:59.161906
---

# ghostsurf：从 NTLM 中继到浏览器会话劫持

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSgGBAdgPmABBoiaUobwUFVpxej9NCR9yP2IHiaEKsSPYkWzrKia9ibdGKg9pSxVOf9fM7Dng6VRwS2Rn6aQhSCdCzHbLnBicPhw8ono/0?wx_fmt=jpeg)

# ghostsurf：从 NTLM 中继到浏览器会话劫持

Allen DeMoura
Allen DeMoura

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://specterops.io/blog/2026/04/02/ghostsurf-from-ntlm-relay-to-browser-session-hijacking/ | Allen DeMoura |

***TL;DR：**`ntlmrelayx`的 SOCKS 代理在 SMB 和 MSSQL 上表现出色，但一旦尝试通过它访问 Web 应用就会失效。我追查了原因，发现了它在 HTTP 处理上的几个根本性缺陷，并写了 `ghostsurf`来解决这些问题。在此过程中，我还发现并绕过了一些未公开的 Windows 内核认证机制。`ghostsurf`允许你以中继用户的身份，通过 SOCKS5 代理访问支持 NTLM 认证的 Web 应用（比如企业密码保险柜！），即便 Cookie 窃取根本不是一个可行选项，这套方案依然有效。*

**工具：**https://github.com/senderend/ghostsurf

## 事情的起点

最近在一次渗透测试评估中，目标环境部署了 CyberArk Privileged Access Manager。无论是普通用户还是管理员，日常流程都是打开内部托管的 Web 界面，借助 Windows 登录会话自动完成认证，然后直接从浏览器里复制密码使用。我们拿下了一个中继位置，成功捕获了某个特权域账户的 NTLM 认证凭据（无法暴力破解）。只要能以这个用户的身份访问 CyberArk，该账户下被分配的所有机密信息便唾手可得，我们还可以借助大量可用的服务作为跳板，向环境更深处横向渗透。

Impacket 套件中的 `ntlmrelayx`恰好为这类场景提供了 SOCKS 代理功能。完成 NTLM 认证中继后，它会启动一个 SOCKS5 代理，让你通过已认证的会话来路由流量。这套方案在 SMB 和 MSSQL 等协议上效果不错——把 smbclient 或 mssqlclient 指向代理，就能以交互方式对目标展开攻击。然而，当我们把浏览器的 SOCKS 代理指向它并导航到 CyberArk 的 Web 界面时，麻烦接踵而来：弹出基本认证对话框、连接无响应挂起、收到的部分响应内容已损坏、页面始终无法完整渲染……大量搜索和与同事交流之后，虽然有几人曾遭遇过同样的问题，却没有人找到过解决方案。

我花时间排查了代理配置、换过不同的浏览器、调整了连接时序，一概无济于事。于是我开始翻阅 `ntlmrelayx`HTTP SOCKS 插件的源代码，想搞清楚网络层面到底发生了什么——事情也就从这里开始变得有意思了。在深入实现细节之前，先来了解一些必要的背景知识。

## `ntlmrelayx`HTTP 浏览器 SOCKS 的现状

`ntlmrelayx`是一款经久不衰的工具，几乎所有做网络渗透测试的人都用过，而且往往效果不俗。不过，它的设计初衷是配合命令行工具使用的。那么，把浏览器接上去会发生什么？我们来走一遍这段略带讽刺意味的"探索之旅"，看看实际情况到底如何。

首先，带上合适的参数和目标，启动 `ntlmrelayx`——这操作我们都做过不知道多少遍了：

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgjAIkwfVFtG7MrkC8pOd6qfVTCRGpIaska0EZoibcKONxOsiaJZ1N6Ountq0eDiarVPxt2Ec3JesyqOt0ODnpF0B93PFOrzFTSPA/640?wx_fmt=png&from=appmsg)

假设中继顺利，它会处理 NTLM 握手，存储中继会话，然后尽职尽责地通过每 30 秒一次的 keepAlive 请求维持认证后的 TCP 连接存活，同时为你开启 SOCKS 代理，方便你接入并使用这些会话。输出里可以看到中继成功的提示：

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiamsZctc1UniaEHIXWIDicEfibMOt85DmdBSm6ASprX7qvicFt6R4xKDq2E2MJo3pbEX35obD9jx1BZqxr8AVY7woDI82YpQLhSHoM/640?wx_fmt=png&from=appmsg)

是时候来"享受"这个全新会话了！用 FoxyProxy 扩展把 Firefox 指向 `ntlmrelayx`在本机默认的代理端口 \_1080/TCP\_，打开目标应用，接受 Impacket 的自签名证书，然后……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShufLUQ8HFfXXibwrH6icfPD5aqnZaOVMqSaVTuaiaeHpxmhjm8gSKUAjlrAQzPxR51KSXqU1aO2Hgcm2upgiaLkViaKgccYzHVyEm0/640?wx_fmt=png&from=appmsg)

……映入眼帘的是一个基础认证弹窗。"享受感"开始打折了。这个弹窗和你在未认证、不走 SOCKS、没有中继的情况下直接访问目标应用时看到的一模一样。大多数时间有限的测试人员走到这一步，往往会断定攻击失败，转战下一个目标——我们当时也是这么干的。

为什么会出现这个基础认证弹窗，后面再细说。现在先假设你锲而不舍，继续在我的实验室里死磕。这是我自己的测试环境，所有凭据我都心里有数，不如就试着输入一个有效的 `domain\user:password`组合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSia4cNhxptMOR1KO8rFicZLny0mOYNVhoe6DQ38PMXKN4ohAcEHz4cGkwcwcWhlwmuOgYnklthj4xNRd4eshI2aJ3EQS6bZ1asZM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjNsYbNYT9H1Y5vUqkX5EibEy9gbv0Dorac5WrxvXPlhz6GgtHGbXjOYjjZ69g8xt8aLMiaJPibDOOyeSufQYBLJRiadibmKNyic2TdM/640?wx_fmt=png&from=appmsg)

[COOL]

好，我们中继了用户，连上了 socks，结果看起来反而倒退了一步——连有效凭据都登不进去？那再来一个骚操作，就当发挥创意。在 domain 和用户名之间改用\_正\_斜杠，哪怕应用程序的基础认证弹窗用这种格式即便凭据完全正确也会**拒绝**。反正试试又不亏，对吧？

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShs7sibKKMYUVQBM5J0l66UpicibgPwR9SibtQArWoZy1hES0AfGHicBruwW2DOTT3eXB5XEJMKlRkbibRnvKiabP67icfGiafoLJzVMENQ/640?wx_fmt=png&from=appmsg)

难以置信，居然成了！进去了！速速打开那香喷喷的 Web 界面，开始掏秘密吧！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgLmWLgjjVicOcHmtZhYibjUibGDS53BOmVibVHmZIHccbFsw0nQibmicfEJe0tibzjUJJrDyibctBAsgXOzktXXUo3nib3gRlf2HZlibN3o/640?wx_fmt=png&from=appmsg)

这一团乱麻，绝对不是 Web 设计师们的本意！没点几下，会话就崩掉了，中继上下文随之丢失，我们的"快乐兜风"就此宣告结束。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaMp9407eev4ZEdTC7oMJ2cns55LzF253KaI2JfeYpez2TvITfVzBLuafRgib7LIeS9X6KN7qvI9YibdWqIkq32iabsFtehtK8Ekg/640?wx_fmt=png&from=appmsg)

到了这里，我的好奇心实在按捺不住了。这到底是怎么一回事？

"为什么会这样"的技术分析放在后面展开，不过我先给个预告和摘要：\_ntlmrelayx 从来就不是为让浏览器通过它运行而设计的。\_ 那些让它在命令行下运行良好的设计决策，恰好阴差阳错地让它在这一场景下与浏览器配合时变得滑稽混乱、完全无法正常使用。

## 浏览器代理为何失效？

根本原因在于：`ntlmrelayx`是为那些在单个连接上**顺序**发起请求的工具设计的，而浏览器根本不是这种工作方式。

与大多数（无状态）HTTP 协议——先完成认证握手、再把 cookie 交出去——不同，Windows NTLM HTTP 认证是绑定在 TCP 连接上的（有状态！）。这意味着：cookie 窃取这条路行不通（详见下方"注意事项"部分）。在 IIS 对 TCP 连接完成身份验证之前，应用层根本看不到你的请求，更别提头部（包括 cookie）了。

当 `ntlmrelayx`将认证中继到 HTTP 目标时，认证后的会话就绑定在那个特定 relay socket 上——你想以该用户身份发出的每一个请求，都必须经过这个 relay socket。对 SMB 或 MSSQL 来说没问题；这些协议天生是面向连接的：打开连接，完成认证，持续使用。

HTTP 则完全不同。浏览器会**并行**打开多个 TCP 连接，用于加载页面资源、预取内容以及处理多标签页的并发请求，并同时向所有连接发送请求。而 `ntlmrelayx`每个会话只有一个认证后的中继套接字，HTTP SOCKS 插件对其访问也没有任何协调机制。当两个浏览器连接试图同时发送请求时，它们就会互相踩踏：一个正在写入请求，另一个没等第一个响应回来就抢着写入，整个数据流在页面加载完成之前就已彻底损坏。

`ntlmrelayx`的 SOCKS 架构还使用了一个从有状态协议插件继承下来的 `inUse`标志。某个连接在使用会话时，这个标志会阻断其他所有连接。对 SMB 而言，这是防止冲突的必要机制；对 HTTP 而言，这意味着浏览器一次打开六个并行连接，其中五个会被当场拒绝。

### 令人困惑的 Basic Auth 提示

为什么通过已中继且经过认证的 HTTP SOCKS 会话访问时，我们还会收到身份验证提示？

`ntlmrelayx`支持为多个用户同时中继并存储会话，但需要一种机制让用户在通过 SOCKS 代理连接时指定使用哪个会话。HTTP SOCKS 插件要求提供 Basic Auth 头部来完成这一指定——对像 `curl`这样的命令行工具来说足够直观，因为加个调试或冗余输出标志就能看到响应头。

问题在于，这会导致浏览器通过已认证的 `ntlmrelayx`SOCKS 代理访问 web 应用时，弹出一个 Basic Auth 提示框——其外观与未认证用户访问受 Windows NTLM HTTP 身份验证保护的页面时看到的**完全一样**。浏览器用户很难意识到，这个 Basic Auth 提示实际上来自 `ntlmrelayx`，而非目标 Web 应用本身。它并不是真的在要求你向应用进行认证，而是 `ntlmrelayx`用来询问我们\_想用哪个会话\_的特殊方式。这个不幸的巧合，正是本文开头那段令人困惑场景的根源。我们实际上已经通过中继完成了对 web 应用的认证，只是 `ntlmrelayx`要求我们先指定会话，才会把请求通过 relay socket 转发出去。

更烦人的是，`ntlmrelayx`要求你提供这些 Basic Auth 头部，\_即便你只有一个中继会话也不例外\_；它不会自动帮你选。再加一层：你还必须以 `domain/user`格式，也就是***正斜杠***来指定用户名，以适配命令行的解析规则和转义字符。这在浏览器弹出框里尤其令人困惑——因为来自 web 应用本身的那个外观相同的 Basic Auth 提示要求的是 Windows 标准的 `domain\user`格式（***反斜杠***），而且会直接\_拒绝\_ `ntlmrelayx`正斜杠格式的用户名。这个会话选择"认证"提示里的密码字段只是个占位符，填空或随便填点字符都行——`ntlmrelayx`会直接丢弃它，只使用 domain/user 部分。

## 解决方案：`ghostsurf`

`ghostsurf`是 `ntlmrelayx`中继与 SOCKS 基础设施的一个 fork，专为基于浏览器的使用场景重新构建。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjyWyes0icMzX9ibRXNoiaKTVw9kAkx2Vf8JHgHtMdhIclicPXa6kOlcyfbhNT9Sib8cXFxUuPJRxjZ3Dic6lRNAA0ICXohHnxHgLjg4/640?wx_fmt=png&from=appmsg)

首先需要解决的问题是对中继 socket 的并发访问。`ghostsurf`不再使用 `inUse`标志，而是用 mutex 风格的线程锁来包装中继 socket。当浏览器连接需要发送请求时，它会先获取锁，通过中继 socket 发送请求，读取完整的 HTTP 响应以确保中继 socket 在下一次请求前处于干净状态，然后释放锁。其他连接则排队等待轮次。这实现了对所有传入请求的整洁序列化。浏览器可以打开任意多的并行连接而不会破坏中继流，所有请求都会被汇入我们唯一的已认证 relay socket（略有简化；更多细节请参阅下文的内核模式认证章节）。在我的实验室网络中，延迟可以忽略不计。速度更可能受限于你的实际操作网络配置，而非在请求序列化这一层面形成瓶颈。

不再需要折腾基本认证头。如果你只有单个中继会话，`ghostsurf`会自动为你选择，浏览器即可透明地以被中继用户的身份进行 proxy。当你中继了多个用户时，`ghostsurf`会在页面加载前进行拦截，并在浏览器中呈现一个 HTML 选择页面。点击想要的用户，目标页面将以该用户的身份加载。底层实现上，这会设置一个 cookie，将后续所有浏览器请求绑定到该中继会话。当你准备切换用户上下文时，关闭浏览器即可清除 cookie，选择页面将再次出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaxr40CwybVyTyUvoTOEibJvNIpgqAV5TndH5yQvKF1paeJLYqEMh8k82Sf8GG67QiaMrZ9libD50rDFJOdWqk60o1DhWiabRULvzg/640?wx_fmt=png&from=appmsg)

`ghostsurf`还会在中继过程中保留浏览器头部。原始的 `ntlmrelayx`HTTP 插件在转发到目标前会剥离大部分头部。`ghostsurf`则保留了 User-Agent、cookie（仅剥除自身的会话跟踪 cookie）以及目标应用程序可能依赖的、用于状态和会话跟踪的其他头部。

## 内核模式认证研究

我最初的测试和开发是在一个运行于 IIS 上、启用了 Windows 身份验证的单页随手搭建的测试 Web 应用上进行的。上述改造实施完毕后，一切运行顺畅，但当我尝试针对真实企业软件进行测试时，情况变得复杂起来。我获取了 Passwordstate 密码管理器的试用版并在实验室中部署，对其发起中继攻击，随后调试工作变得棘手。

中继攻击成功，初始页面加载正常；然而，点击第一个导航链接时，我被再次要求进行基本认证。随后的每次点击都会弹出一个新的基本认证浏览器提示，此后所有请求均告失败。

我首先怀疑的是 IIS 的认证持久化设置。`authPersistSingleRequest`会指示 IIS 对每个请求重新发起认证质询，但其默认值为 `false`，我确认 Passwordstate 的这一设置及所有 IIS 默认值均未改变。不过，即便将其设为 `true`，也无法解释我所观察到的现象：30 到 50 个经过认证的请求成功返回 200，随后突然收到 HTTP 401 响应。`AuthPersistNonNTLM`同样与此无关，因为它仅适用于 Kerberos。

在深入研究 IIS 设置及其默认配置数天后，我注意到，与我手动安装的测试应用不同，Passwordstate 使用 IIS 默认配置安装，其中包含内核模式认证设置。该设置将认证逻辑从 IIS 用户模式执行层移至 *HTTP.sys*监听器的内核层。Windows 在请求到达 IIS 或应用层之前便完成认证决策。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjJRKaWNXAyu6zubdv9w1zy3MqFBEEJibuibIA2iaDbYHp0AaibSkh4k5Uqa1WWrRvlhmemmtYM7eE2U7TPqtNOwQ07AicsLp8ibBwGI/640?wx_fmt=png&from=appmsg)

经过数天对请求日志的仔细梳理，我发现了一个规律：每次 401 重新认证质询总是出现在对某些特定端点的成功请求之后。仔细观察后发现，尽管 Web 根目录要求 Windows 身份验证，但用于静态内容 (CSS 文件、JavaScript、图片、字体等) 的虚拟目录和 URL 路径被设置为匿名认证。这在 Web 应用中很常见：浏览器需要获取这些资源来渲染页面，而它们不包含敏感数据。

此时，规律如下：

1. 对已认证资源的多次成功请求
2. 对未认证 (匿名) 资源的一次或多次成功请求
3. 对已认证资源的请求失败 (收到 401 认证质询响应)

我开始形成一个假设：也许某些机制重置了某种认证缓存。在用户模式认证下，IIS 似乎能够跨越对已认证和未认证资源的任意请求序列"记住"我的认证上下文。然而，在内核模式下 (内存和执行约束更为严格)，认证缓存似乎表现为一个非此...