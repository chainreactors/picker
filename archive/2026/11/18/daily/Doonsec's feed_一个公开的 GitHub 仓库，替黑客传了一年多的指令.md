---
title: 一个公开的 GitHub 仓库，替黑客传了一年多的指令
url: https://mp.weixin.qq.com/s/hKZeu4rvMpfCt-S6B_2oyQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:45:21.445767
---

# 一个公开的 GitHub 仓库，替黑客传了一年多的指令

# 一个公开的 GitHub 仓库，替黑客传了一年多的指令

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MNicb9nDjSwFID8A8mEuy9wO4ggJm8OmR7m5nb9KSHMEen9oZ4LyTib1HKWQwicWhIDdIots4PNvyXmBAaH7uKJmkTVewSAiaZpjw/640?from=appmsg)
> **导语**：ShadowCloud 的目标是亚洲和非洲的政府部门。入侵链第一环不是 0day，是机器上早就躺着的合法远程代理，没人知道它什么时候装的。再往后才看清楚：黑客用公开 GitHub 仓库收指令、用 SharePoint 空间存数据，C2 流量长得和日常云调用一模一样。

![GitHub 与 SharePoint 成为 C2 通道](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NcIJzs3ibMt1THgVAoEs8bd13bYmibf5UsDicWIJ80AMpulIPSo3mQoCI8juVEXf8cQyfib4cbp3armBztuohUpZx6ZOaLhmqZJMs/640?from=appmsg "GitHub 与 SharePoint 成为 C2 通道")

## 入口不是 0day，是个人人都装过的远程工具

卡巴斯基在 2026 年初发现这波活动，威胁研究员 Saurabh Sharma 和 Noushin Shabab 在两篇分析里说得很直白：攻击者没用什么 0day，他们挪用的是合法工具 MeshAgent（MeshCentral 的远程管理代理），这东西本来给运维远程控桌面、跑命令行、管文件用的。

MeshAgent 具体怎么装上去的，目前不清楚。卡巴斯基的说法是"复用了网络里早已存在的旧感染"——机器上本来就有个谁都不记得装过的东西。这次明确点名的受害目标是一家台湾机构，身份没披露。

装好之后，MeshAgent 被写死一个 C2 地址：`wss://27.102.66.162:443/agent.ashx`，然后从上面取三个载荷：一个用来做 DLL 侧加载（DLL sideloading）的合法程序（start.exe、pythonw.exe、zoomit.exe）、一个干活的恶意加载器 DLL（jli.dll、SbieDll.dll、python39.dll、WINMM.dll、libcef.dll）、以及一个装着核心后门的加密文件。

加载器分两种。Type 1 先过 RC4 流密码再叠一层 XOR 掩码，Type 2 干脆就一个 XOR。解出来的后门直接注入当前进程内存，不落盘。

![GitHub 与 SharePoint 成为 C2 通道示意图](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Ploia1yxnOosQibEH8z3Zaw3lp8WicLVvyqQtHr8xhAQ69ice3ThmrfZkRfF8hYibF2AjgTQ0kLkg0KicjzgqOpFnTTOleK2bmZyRz4/640?from=appmsg "GitHub 与 SharePoint 成为 C2 通道示意图")

*（图：GitHub 与 SharePoint 被用作 C2 通道示意，来源 The Hacker News）*

## GitDoor：拿 GitHub 仓库当收件箱和回执单

GitDoor 的逻辑简单粗暴：拉指令用一个公开仓库，回传结果用另一个私有仓库，路径都写死了——`/repos/LatonyCharnleyaW/Havo` 负责收，`/repos/LatonyCharnleyaW/Trix` 负责发。

这两个仓库的创建时间说明了一切：最早能追到 2024 年底。也就是说这波行动不是临时起意，准备期至少一年多。

GitDoor 支持 26 条命令，文件管理、键盘记录、起代理、加载 Base64 编码的 COFF 格式二进制、自杀退出都在里面。最值钱的是自定义 shellcode 功能，下载即执行，落地模块包括 APC 注入（异步过程调用注入）、枚举并改写防火墙规则、用 cmd.exe 跑命令、建计划任务、递归读写注册表、往本地组里塞新账户、dump 指定进程的内存、截图、导出 Chrome 和 Edge 的 Cookie（走 CookieKatz 浏览器凭据转储工具）、用 Mimikatz 凭据转储工具从 LSASS 里掏哈希、抠 WhatsApp 的数据库解密密钥、发起 NTLM 认证到攻击者自己的地址。

键盘记录落到 `%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat`——伪装成系统证书缓存目录，正常终端上基本不会有这文件。

## GraphDoor：把 SharePoint 当文件柜

GraphDoor 更绕一层。它开一个命名管道，在应用数据目录下建一个叫 `Intel_Log` 的文件夹，收集系统信息。跟 C2 通信时，它用一个恶意应用去 `login.microsoftonline.com:443` 认证，拿 access token 之后直接调 Microsoft Graph API，把偷来的数据暂存进 SharePoint 空间。

它还会从服务端拉三个插件并行跑：截图、列进程、记键盘。

GraphDoor 的插件清单也值得抄下来：`kl.ts` 记键盘（同样写 logs.dat）、`pr.ts` 列进程、`scr.ts` 按进程 ID 截图存 JPEG、`moveDir.ts` 把合法程序、加载器 DLL 和加密后门挪到指定路径、`channel.ts` 起代理、`abchannel.ts` 用 Ably（云消息服务）代理流量、`ab2channel.ts` 则是藏在 Ably 的 Pusher 兼容 WebSocket 里的 SOCKS5 代理。

换句话说，这两个后门都不只是"能上线"，它们各自还带一条把流量转出去的地道。卡巴斯基提到，被改动过的 Erfrp 客户端和基于 Ably 消息服务的插件都被用来做流量代理。

![GitDoor 与 GraphDoor 的 C2 路径与检测着眼点](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6P4Pc9FxP1MkjvYRaBsPSzCibcVBXQGQgKOib5rMiavopxL1QSyCXv8u4ZArVIaPTyuKGsLM3mVT0ZsGVU9sEnibWb79bKr2lxyk40/640?from=appmsg "GitDoor 与 GraphDoor 的 C2 路径与检测着眼点")

*（图：GitDoor 与 GraphDoor 的 C2 路径与检测着眼点，来源 Kaspersky / The Hacker News）*

## "信任流量"成了新的藏身处

卡巴斯基对这个手法的评价挺狠：调用 Graph、GitHub、Ably 的云 API 流量和企业正常用法没法区分，大量基于网络的检测直接失效。

更麻烦的是动态载荷。插件和 shellcode 都按需从云上仓库取，想换功能不用改主机上的文件，防守方连一个可疑的 PE 都未必看得到。

至于背后是谁，卡巴斯基没给结论，只说战术层面和 Sophos 追踪的 China-nexus 活动 Bronze Sandcastle 有重叠，也和 FamousSparrow、CopperTurtle（BlackTech）过去的行动有相似之处——好几台受害主机上，这些团伙和 GitDoor 用了同一个暂存目录，植入时间只差一天。这不能证明同源，但说明背后很可能是个中文母语的团伙在开发或者使用这两把后门。

## 防守方该盯的六件事

我们的判断：这种打法，封域名基本白费。GitHub、SharePoint、Ably 是企业天天在用的服务，没人会拦。真正能抓到的是这些：

* 出口流量里出现 `27.102.66.162:443`，或者 wss 协议连向 `/agent.ashx`
* 机器上跑着 MeshCentral / meshagent 进程，但 IT 说不出是谁、什么时候装的
* `%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat` 和 `Intel_Log` 目录——正常终端不会有
* 非浏览器进程（pythonw.exe、zoomit.exe 这类）在请求 Graph API 或 SharePoint，服务器上没有开发任务却持续出站
* 微软 Entra（统一身份管理）应用注册里冒出来没见过的应用在申请 Graph 令牌
* GitHub 侧出现 `LatonyCharnleyaW/Havo`、`LatonyCharnleyaW/Trix` 两个仓库的访问，或者账号有异常的仓库读写

一句话：盯"哪个进程在跟它说话"，别只盯"它在跟谁说话"。域名黑名单在这条链上等于一张废纸。

## 参考来源

* The Hacker News：New GitDoor and GraphDoor Backdoors Turn GitHub and SharePoint Into Covert C2 Channels
* 卡巴斯基 Operation ShadowCloud 两篇分析报告

**版权声明**：本文由华盟网原创发布，保留所有权利。文中图片来源于 The Hacker News 及 Kaspersky。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NkJv7siciaq2l56JKLJibWSVHW9yO0uRk2ibPk3zTTQdZFR5gpyjuzsAkKTl7P1R0MrjkyrQIo8tLovOicfwB4w2MonbotBGm6FCyo/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PibJKIf8X0IiaGgIk7bwCcHSxghjPaZL033fJNxE9bMEaIQc8crn99mw0goiaY4uyhdkKicPEh2AQ2wqRtnicptRPsere4CK6wx6aU/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PDTF2XWEzjy7UDIuQ0n92BdYiceCR6ZFAe4DyvBxRczyH1ubQ9xzd9CIWQTiakGvm8ibOMicyzsHXoGIrJOeKoPL36icvAI73joJjg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Mmrh2qn8LqpcQOKSU8rT09h8E6978peB20EveBLCZcODPBmqgtibPTBib37kMgGyo2MTib57cGFWbWKrKD1dpicEp2mibvnoUdDbo8/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过