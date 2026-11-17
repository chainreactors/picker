---
title: 【工具学习31】katana：从翻页面到扒 JS，把网站里的接口全摸出来
url: https://mp.weixin.qq.com/s/ZA7ppy7BcRB1jBrVzQx-Uw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:53:52.534967
---

# 【工具学习31】katana：从翻页面到扒 JS，把网站里的接口全摸出来

# 【工具学习31】katana：从翻页面到扒 JS，把网站里的接口全摸出来

原创

CabinQ
CabinQ

逆熵寻生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

katana：从翻页面到扒 JS，把网站里的接口全摸出来

做过渗透侦察的人都知道，光扫一堆域名没用，关键得知道**每个站里到底藏了哪些页面和接口**。这活儿有个传统做法——拿字典去硬撞目录，就是 ffuf 干的事。但如今的前端早不是几十年前那种静态 HTML 了，大量内容是**靠 JavaScript 动态渲染**、所有接口都藏在打包后的 JS 文件里。这时候靠字典硬撞，就像在黑灯瞎火的屋子里只数门板，漏掉太多。今天的主角 **katana**，干的就是"主动把整个网站翻个底朝天"的活儿，而且是连 JS 都拆开翻的那种。

它是 ProjectDiscovery 家出品（就是 nuclei、httpx 的老东家）的**下一代爬虫 / 蜘蛛框架**（项目主页：https://github.com/projectdiscovery/katana ），Go 写的、MIT 开源、最新 v1.7.0。定位很明确：不靠猜，靠"顺着链接跑遍全站 + 解析 JS 挖接口"，把目标站点里能爬到的每个角落都清点出来。

快与"能看到"：两种爬取模式

普通的爬虫只有一种玩法——发 HTTP 请求、读返回的 HTML。但这种模式下，只要页面里关键的链接或接口是 JavaScript 动态生成的，它就读不到，等于白爬。katana 把这个问题拆成了两种模式：

**Standard（标准模式）** 用 Go 原生 HTTP 库直接发请求做爬取，速度飞快，没有浏览器开销，适合大多数常规目标。但它和普通爬虫一样，看不到"渲染后"的内容。

**Headless（无头浏览器模式）** 才是 katana 的杀手锏。它内置一个无头 Chrome，在真实浏览器环境里执行页面、跑 JavaScript，把渲染之后才出现的链接和**异步接口调用**全都抓出来。那些用 Vue、React 写的单页应用（SPA），页面一开疯狂向后端发 XHR 请求拉数据，普通爬虫完全抓瞎，katana 用无头模式能把这一层全看透。开它很简单：

katana -u https://example.com -headless

而且无头模式下它发出的 TLS 指纹、User-Agent 都跟真实浏览器一致，不容易被简单的反爬规则识破。

能从 JavaScript 里挖出隐藏接口

这是 katana 最实用的看家本领。现代前端把功能都写在 JS 里，里面藏着一大堆**接口路径、API 端点、甚至硬编码的参数结构**。katana 专门盯着 JS 文件下手：

katana -u https://example.com -jc

`-jc` 会去解析、爬取页面里引用的 JavaScript 文件，把里面出现的接口路径、请求端点全都抠出来。想挖得更深，还有 `-jsl` 开启 jsluice 深度解析，把 JS 里的结构化信息榨得更干净（只是占内存更多）。对渗透来说，这些从 JS 里抠出来的隐藏接口，往往就是测试的重点——很多站点的管理入口、未授权接口，都藏在别人看不进去的 JS 里。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Uhia8L5ia7ha4HuiaLEZahDbvG0Vs5tyKxVf5MvExTqXISKSoHDktu8M29ry8Dwian7bjcjUkllyKH8TYSCia1ZPUpFe9qKYZF6UFRicyQJImMd4s/640?from=appmsg)

连上已登录的浏览器爬

很多目标的后台、会员区是要登录才能访问的。为此 katana 支持**接管一个真实浏览器会话**：你先用 Chrome 开远程调试，登录好目标网站再保持浏览器开着，然后让 katana 连上去爬——它就带着你的登录态去把登录后才能看到的页面全翻出来。

启动带远程调试的 Chrome：

google-chrome --remote -debugging-port=9222

浏览器会返回一串 websocket 地址，再把它交给 katana：

katana -headless-u https://example.com -cwu ws://127.0.0.1:9222/devtools/browser/xxx

这个能力对测"需要认证"的站点特别实用——不用去破解，直接借真实的登录态把后台、会员页面的范围摸清楚。

爬哪儿、不爬哪儿，自己定

爬虫最怕漫无目的地乱跑，把自己钻进别人的 scope 里。katana 给了精细的范围控制和过滤：

🔹 **`-cs` 限定 in-scope**：只跟随匹配某个正则的链接，比如只爬 `shop.example.com`；

🔹 **`-fs` 字段级范围**：默认 `rdn`（根域名），保证不跑出目标站点；想跨子域就用 `-fs fqdn`；

🔹 **`-ef` 过滤扩展名**：把 `png,css` 这类无关资源滤掉，只看要的；

🔹 **`-em` 只挑某种扩展名**：比如只要 `js,jsp,json`。

它还能用表达式做更聪明的筛选，比如"只留下状态码 200 的接口"：

katana -u https://example.com -mdc'status\_code == 200'

甚至能判断技术栈再过滤，比如把跑在 Cloudflare 后面的端点挑出去。这种把"要什么、不要什么"写进命令的能力，让它在自动化链路里特别好用。

别把自己爬成攻击对象

爬得快是本事，爬得太猛会惹麻烦。katana 内置了完整的限速机制，避免把目标网站激怒、给自己招来封禁：

katana -u https://example.com -delay2-rate-limit 50

`-delay 2` 是每个请求之间隔 2 秒，`-rate-limit 50` 是每秒最多发 50 个请求，还有 per-host 的 `-hrl` 按域名单独限速、遇到 429/503 自动退避。做渗透侦察，尤其测别人的资产时，这些克制是专业性的体现——慢慢爬，才能爬得久。

它在渗透链路里的位置

对渗透来说，katana 填的是"内容发现"里最关键的一环：它把目标网站**能访问到的页面、能调用的接口**成体系地清点出来，直接喂给后面的漏洞验证。一条非常典型的自动化管道是：

cat domains | httpx | katana -jc | nuclei

httpx 先探出哪些域名活着，katana 顺着爬出所有页面和从 JS 里挖出的接口，nuclei 再逐一对这些接口打模板找漏洞。三段各司其职，一气呵成。而 katana 的输出支持 JSON/JSONL 格式，喂给 Hermes 这种自动化渗透系统做下游判定也毫无压力——它收集的 endpoint、参数、技术栈信息，正好是编排下一步打哪里的依据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uhia8L5ia7ha4RnyyERnStmgbOkumkoVvvGT8W7icCczuddhZBEbXJPGL1RmytGUkdQFDVIgWiaTaWv3fJV207T6YrwjibIGJEj2bO06s1WQryXo/640?from=appmsg)

**蓝队视角反过来看。** 凡是 katana 能顺着 JS 挖出来的接口、能爬到的隐藏页面，攻击者一样能。所以做防护时，敏感接口不要硬编码在公开的 JS 里、加权限校验而不是依赖"接口隐蔽"、对无头浏览器爬取做限流和识别，都是对自己暴露面负责的做法。接口藏得再深，也挡不住一个会拆 JS 的爬虫。

写在最后

katana 的厉害，在于把"爬网站"从机械的翻页面升级成了"带着眼睛理解页面、拆 JS 找接口"的体系化侦察。它快、能看渲染后的内容、能挖 JS、能接管登录会话，还能精准控制爬哪儿不爬哪儿。在一众 GET 请求爬虫里，它更像是那个走遍全场、还专门蹲在墙角拆线索的侦察兵。

最后照例说规矩：爬取目标必须是你有权测试的对象——自己的资产、授权的项目、CTF 靶场。对他人系统做未授权爬取和内容发现，不管用什么工具，都是越线。侦察的本事越强，越该先分清哪条线能动、哪条线不能碰。

🎯 关注我，持续不断地成长！

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Uhia8L5ia7ha5Irp0ovtXmib2AMCGUXM4EIRkkSia1Djn1tVnApSbg3RvIOzgVG7YxAFIpyh4rvxNDEEjvMpdZrJUpTtYMsLuykkFg6JKgVn5Lk/0?wx_fmt=png)

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