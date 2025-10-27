---
title: Yak 在 AI 浪潮中应该如何存活？
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247527752&idx=1&sn=8f4148b9f96cfd513f38ab1ec5762562&chksm=c2d111ecf5a698fa6b6aae1d1dad7bad45b6e7563889e275191d0c74041eb47391a0a00055b8&scene=58&subscene=0#rd
source: Yak Project
date: 2025-02-28
fetch_date: 2025-10-06T20:39:03.775258
---

# Yak 在 AI 浪潮中应该如何存活？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmovrwwqjsbrdNA8Qq3Q4MSicAFXpnRZTob2j4SII7Azic0iaNRg4hWqZyg/0?wx_fmt=jpeg)

# Yak 在 AI 浪潮中应该如何存活？

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmd0CJRK84NKwtGwNLg2c0kyKw5OdBUYA4l3TBwJFDDlbG552ptAwJ3Q/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmtKn2PAMfSE2IhvVjYIicQclCBTabCxFxzicKHz63w5w9IiaAtk8wMHP1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmmxerSCEvrRGLEZ4v8HpicmpiasPkR2UqItV1n3Bc02xzibBnXAicGWIYibQ/640?wx_fmt=png&from=appmsg)

MCP 是 Claude 发起的一个协议，在2024年10月左右发布，在2025年2月开始逐步有大批量的 AI 应用体开始支持这个协议。这个协议目的是让 AI 同时可以感知有什么工具可以用，如果要调用这些工具的话，应该是用什么样的方式。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmO8NicRMswCKy257DcIG6f9jOLeSMjMeibriap0P8eZM1qxn4uLWFt9Uqg/640?wx_fmt=png&from=appmsg)

这个 MCP 协议会重新塑造一种新的代码交互模式，安全产品的研发的思路需要发生极大的改变：我们不仅仅需要为用户构造可用的产品，还需要**为 AI 构建可用的工具。**

之前我们编写的代码几乎都是人在使用，现在不一定了，我们**需要让代码被 AI 来调用**，来迅速为 AI 补充他没有的能力，或让 AI 来决策。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmDiaib3KUjUtqZrw7WVIGic88APoG83yfGzEMAxsEUW86u9nfJfRsDQrbQ/640?wx_fmt=png&from=appmsg)

在 Yak 对 AI MCP 的支持计划中，会被分为两个阶段，这两个阶段是并行的：

1. 本身**安全能力完全开放给 AI 工具**，我们把现有的一些稳定的能力实现 MCP 接口，在支持 MCP 客户端的地方都可以快速使用；
2. 教会 AI 编写 Yak 代码，如果 AI 想实现的安全能力无法在现有模块中找到，**AI 可以通过编写 Yak 代码来实现他想实现的功能**，当然 Yak 代码是图灵完备的，AI 理论上可以自己写代码达成自己的目标。

截止2024年2月中旬，我们确实已经实现了MCP的初步接入：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDm3ibAZ50e6q08ljiaibLWcpyPKoJjK8hANka92ibs3RJrLKQ1TcPWLff2kg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDm7yUCFXdTHmNRysBlJuJA0sFEMQBumxPceszJsqvtWjMcBaXKRJjhlg/640?wx_fmt=png&from=appmsg)

实际上，大家用 AI 的都懂：Chat 绝对不是终极交互目标，在写代码过程中，Chat 虽然和 Cursor 的交互形式背后的引擎可能是一样的，但是实践性和可用性远远比不上 Cursor 之类的工具。AI 已经发展了有这么久了，然而在我们用户中，Yakit 的操作和基础的流量分析和发包，扫描等功能，实际上是大家花了大量时间在使用的。**AI 如果真的想改造创造生产力，第一个目标应该是改造 AI 生产工具。**

我们一方面需要解决 AI 能力的扩充（使用 Yak 本身的安全能力和库函数），另一方面应该着手去解决安全生产力工具的革新。这个革新绝对不是简单嵌入一个 Chat Tab 可以解决的。核心的 MCP 能力通过 Yak 来接入，符合“认知飞轮”的任务型 AI 交互模式也需要重塑。“认知飞轮”循环控制：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmeeHzqlYhTqD2AguI1soxHjFdgediacEj3DuA2NubY8ibpgN1IzwC8baw/640?wx_fmt=png&from=appmsg)

当然，我们上面讲的是我们如何把 Yak 中已有的功能或者生产工具开放给 AI，这仅仅只是过去的知识的用法；

如果沉迷在过去，技术工具将会止步不前，AI 也会因为没有新的技术和新的能力加入，创造力变的枯竭。因此我们也会**投入大量精力放在“无语料区”**，AI 会极大的帮我们从琐事中抽身，让我们投身在这些“探索性”的工作中，这些工作将在未来的很长一段时间内是竞争力的体现。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmkXOniaBBOaRHPQLFgrcRRS3OL4cGVJAC4t8xxaS8aUDFBTGLwpykm9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmkKwDCCTkqNpEF6TzxBKjLTa0fk2ic6Lp0ficxMdSapKw1icGibMicq4LcZA/640?wx_fmt=png&from=appmsg)

在 2025 年，Yakit 遇到第一个挑战性需求是：**本地 TCP 劫持。**

这是一个听起来非常离谱的需求。我们的目标是，不侵入操作系统内核的情况下，仅通过安全的网络配置劫持本地 TCP，以达到类似替代 proxifier（内核设置代理）的目的。在这个过程中，脱离操作系统内核会让这个行为变成一个纯用户行为，并且可移植性被认为是“非常好”。

这种新的劫持技术会重新改造大家对 Yakit 或者基于代理的习惯。同时也可实现之前几乎无法实现的功能：**如果一个 HTTP 应用无法设置 HTTP 代理或者 Socks 代理，那应该如何劫持 HTTP 协议？**

我们实际上知道，VPN 理论上是可以拿到很多流量的，但是一般 VPN 不做 MITM 的支持，这是为什么？

1. TCP 以数据帧的形式在 VPN 隧道中传输；
2. 即使 TCP 数据帧被重组了后，TCP 传输内容被修改了，仍然需要重新切割数据帧保证 ID 都是连续对应的。

很多时候，我们知道数据帧重组这个事情本身是一个操作系统干的事儿（当然在一些高级产品或者应用中也有实现，比如 Wireshark 或 Yakit 的抓包系统算法中）。

如果我们能控制 TCP 数据帧重组（PDU重组）和拆分过程，那么理论上来说，VPN 的实现方式完全可以被改造为 TCP MITM。我们梳理了整个过程，并完成了一个最小原型验证 VPN 方式进行 TCP 劫持的可行性：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDm0NLvz1wv0H1UdfEE9ylfzhLBibS9pGicB8zVPx5tu498LRJ4OPuQ1p4g/640?wx_fmt=png&from=appmsg)

届此功能实现在 Yakit 与大家见面的时候，Yakit 应该是首个实现 VPN 级别 MITM 劫持的工具和产品。在这种方案的帮助下，理论上用户应该不再需要 Proxifier 之类的内核修改代理等方案定向劫持了。

值得一提的是，我们利用 gVisor 已实现了网络虚拟机的构建，可以替代任何主机与本地客户端进行握手，同时也有很多办法可以绕过系统路由表的“环路”限制。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmDsXjNZJsHSUjxWm5tTolIKlVf2IZgeQdMnronlg6gwphziaMHHZRzvw/640?wx_fmt=png&from=appmsg)

在这个重要的产品 PoC 实现过程中，我们发现这个需求的实现几乎完全没有语料，现有的很多语料和散落的知识对这个 PoC 几乎不适用。在这个系统构建过程中，AI 的帮助几乎都是反作用：

1. gVisor 在大版本更新后，AI 无法准确了解它里面 AI 的具体含义，你想实现的功能几乎无法使用 AI 来实现。
2. AI 幻觉非常严重，一些不存在的 AI 会让你反复确认原生库中是否真的有这个代码，浪费大量时间
3. gVisor 本身仓库的构建使用 bazel 工具，主仓库无法直接使用 go get 之类的命令直接安装，需要做一些小小的额外参数，虽然改动不大，但是操作员没有深入的基础知识的情况下，AI 无法自己修复整个工具链的报错。

虽然在解决这个 PoC 过程中，Cursor 等 AI 工具仍然帮助了业务基础代码和一些小代码的生成，但是总体来说，核心时间和调试代码的工具链还是依赖于大量的“传统”并且“精准”的工具链。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmZeWzSCJLXicLd6GKXGaXlrCndMlfrt0dNaicOG8ZyxfW4Bt35vSKibbeQ/640?wx_fmt=png&from=appmsg)

我们在 Yak 开源的时候，就一直在反复提“安全能力融合”的概念。早些日子我们只能实现一些“攻击性”的安全能力，随着 Yak 项目和基础设施的逐步完善和发展，我们今年实现了除了攻击扫描类之外的安全基础设施：流量安全基础设施：兼容型流量安全规则分析引擎，流量生成器，网络虚拟机引擎；编译级静态代码分析引擎；

这些算法和引擎的代码实现在 AI 的发展下，并没有丧失他们原本的光辉，在 AI 全面改造安全技术发展过程中，会逐步发挥他们更大的威力。同样的，我们之前通过 Yaklang 这个图灵完备容器实现的“融合”效果也只会在 AI 的浪潮中变的更快更强更具有实践性。

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcWCfWBbAaIicJnoe8NG8SDmgAPh116KFDIz2YsLB1YasTiaxiciaR6BZwSdrWb3CglHXibFGIezuIvngA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

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