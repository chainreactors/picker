---
title: 藏在屏保与小游戏背后：你的电视可能在帮别人转发网络流量
url: https://mp.weixin.qq.com/s/-kE-t7lu1SR-XOi8_xcvgA
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T05:59:54.024444
---

# 藏在屏保与小游戏背后：你的电视可能在帮别人转发网络流量

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrtSP9aYYfno8OslcyW8RcsEjYibSUQnYEPeibx1Sy0on0iaMovkDt9XWYRODp26D2NUe1fNZ3C4blYbUGb7gtibXAAaGVfKlshiab8/0?wx_fmt=jpeg)

# 藏在屏保与小游戏背后：你的电视可能在帮别人转发网络流量

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

多数人会反复检查手机应用的权限与隐私行为，却很少留意家里智能电视上安装的应用。

安全研究团队 Spur Intelligence Labs 针对 LG 与三星智能电视平台完成了一次大规模扫描，覆盖 6038 款已完成指纹识别的应用，结果显示其中 2058 款应用都嵌入了住宅代理相关 SDK，本质上是在将用户家庭的 IP 地址与网络带宽作为资源对外售卖。

表面上这些应用可能是休闲鱼缸动态壁纸、时钟工具、纸牌游戏或是宠物主题屏保，看起来无害且安静。在后台它们却运行着 residential proxy（住宅代理）程序，能够将第三方的网络流量通过你客厅里的电视设备转发出去，而这类情况已经在智能电视生态中普遍存在。

本次调研覆盖两大主流智能电视系统，分别是 LG 的 webOS 系统与三星的 Tizen 系统，整体代理 SDK 的检出率达到 34.1%。其中 LG webOS 平台共检测 2851 款应用，1213 款包含代理 SDK，占比 42.5%。三星 Tizen 平台共检测 3187 款应用，845 款包含代理 SDK，占比 26.5%。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqYLdXEzicVqxID4mGGP6w7cTOo1icSgX1pQkV8AbPEwLhBNoYP0mYAXs9y6DfJu1woJ0u8wcqyTBdgRDjeVIhmz6bxfWWzHDq7A/640?wx_fmt=jpeg&from=appmsg)

智能电视几乎是最理想的代理宿主设备。它们和其他所有设备处在同一个家庭网络中，却很少被用户当成普通计算机对待，几乎不会有人像检查手机一样去审计电视应用的行为。电视没有电池耗电异常可供察觉，没有手机话费突然暴涨的提醒，也没有应用切换器能展示可疑的后台活动。一台电视可以保持插电、登录账号并持续联网数年，而用户始终只把它看作一件普通家具。

这种认知差也直接改变了授权同意的实际效果。大部分用户对于售卖住宅 IP 地址使用权这件事没有清晰的概念，换到电视场景下认知差距会更大。一次需要用遥控器操作的授权提示很容易淹没在初始设置流程里，而应用会在用户早已忘记同意内容的情况下，长期利用网络连接完成变现。

驱动这一模式的核心是盈利需求。

传统广告变现需要吸引用户注意力，插入广告又会直接降低使用体验。

时钟、动态壁纸这类应用的定位恰恰相反，它们需要保持安静不打扰用户，不适合高频插入广告。嵌入代理 SDK 之后，应用可以维持简洁平静的外观，同时在后台利用电视的网络连接持续产生收益。

目前已确认的代理 SDK 服务商共有三家，分别是 Bright Data、Massive 与 Oxylabs。在 LG webOS 平台的确认样本中，Bright Data 对应 1015 款应用，Massive 对应 135 款，Oxylabs 对应 63 款。在三星 Tizen 平台的确认样本中，Bright Data 对应 619 款应用，Massive 对应 191 款，Oxylabs 对应 35 款。

各 SDK 对授权同意的界定标准，以下是这几家公司对其代理 SDK 有效授权的认定规则。它们仅向用户发起一次授权询问，此后便不再重复提示。

其中最值得关注的是后台运行条款，三家的授权提示均注明，代理服务可在应用关闭后持续运行。用户可以退出应用，代理进程却不会随之终止。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpCpjvJ6rPoq69QYpqs5tn1qrwXUic6Af9ZTkAqLesjV4IIUsyOcLawrT1FbOjzy7bia6nJWfzlLknJrc5DIQ5EnSF8Ja2GfjK9U/640?wx_fmt=png&from=appmsg)

部分应用会将这种权益交换的逻辑展示得更加直白。三星 Tizen 平台上的《吃豆人》将接入 Bright Data 服务设为无广告选项，用户选择拒绝，便可继续游玩带广告的游戏版本，选择同意，应用就有权使用电视的网络连接开展 web indexing（网页索引）。这是一套清晰的变现分叉设计，用户要么观看广告，要么成为代理网络的一部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrWT6OzmGWN94mEpTHcQvMicCJFcjzs7iah9KycU3C293J1eJwzolboEZTI9MJvzrwz5j2XY0SIz17N7dAarBF5WPEGm9rvvk9QU/640?wx_fmt=png&from=appmsg)

##

以搭载 Bright Data SDK 的应用 Galactic Harmony 为例，授权提示会告知用户，想要无广告体验就需要允许 Bright Data 开展 web indexing（网页索引），偶尔调用设备的空闲资源与 IP 地址从互联网下载公开网页数据。提示同时声明 Bright Data 只会将 IP 地址用于经过审批的商业场景，不会进行未经授权的操作，除 IP 地址外不会访问或收集任何个人信息，也不会追踪用户，用户可随时选择退出。

部分应用会把交易逻辑展示得更加直白。三星 Tizen 平台上的吃豆人游戏会将接入 Bright Data 作为无广告选项，用户选择拒绝就继续游玩带广告的版本，选择同意则应用可以使用电视的网络连接开展网页索引。这是非常清晰的变现分叉，用户要么看广告，要么让自己的设备成为代理网络的一部分。

搭载 Massive SDK 的应用提示逻辑类似，想要免费使用应用，就需要允许 Massive 调用设备空闲资源与 IP 地址下载公开网页数据，同样声明不会追踪用户，可随时在设置中关闭。提示也会明确说明 Massive 会在应用关闭后继续在后台运行。

这并不只是代理公司说服普通开发者嵌入 SDK 这么简单。在大量案例中，代理公司本身或是挂着相关名义的主体，就是应用的发布方。

数据显示 Bright Data、Bright Data Ltd 与 Bright SDK 相关主体，在数据集中共有 367 款被标记为包含代理的应用。Oxylabs 的子公司 Honeygain UAB 也作为发布方出现在 16 款应用中。

这让问题的性质发生了变化。其中一部分应用并不是正常功能应用碰巧加入了代理 SDK，它们更像是代理服务商的第一方库存。批量上线的低质小游戏、屏保程序与简易工具壳子，本质上只是为代理 SDK 提供运行环境的载体。应用只是外包装，住宅 IP 资源才是真正售卖的产品。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqSptYsZUIzU40W0GNaWobpbeOVAQuFb8ZMKx7QpIQujZWVVPAy7iaibiawE1qlwpN1Xw6vMgS6DyZCs6JuBgIzH2oUB6fjDtia3Gw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoLYaoDf6Lmc9uWeVPS7weZDUeciaokLzt6vkpULGYA7sJahu8qtlKTBcGIjx0yycVDT2GCic6ImAzelb9pjJ3AagIaq4m8cZBeQ/640?wx_fmt=png&from=appmsg)

在三星 Tizen 平台，代理应用数量最多的发行方是 Desoline，共有 239 款，其次是 Bright Data Ltd 的 140 款，其余头部发行方也大多以批量生产轻量应用为主。

其他智能电视平台早已对此类行为划出红线。

亚马逊在其设备与系统滥用政策中明确规定，禁止应用为第三方提供代理服务。据媒体报道 Roku 也已经关闭了相关入口，有报道指出 Roku 禁止开发者使用 Bright SDK 及同类代理服务，在平台方介入后，使用该 SDK 的 Roku 应用已全部下架。

LG 与三星尚未公开出台对等的限制政策，这正是这类应用能够大规模存在的空间。同样的商业模式，在亚马逊被明令禁止，在 Roku 被平台封禁，却能在 webOS 与 Tizen 生态中规模化运行。

电视应用具备代理能力之后，风险远不止公共 IP 地址被第三方借用这么简单。这类代理应用运行在家庭网络内部，如果代理提供商允许请求访问私有或本地地址，或是流量过滤机制出现失效，这台电视就会成为入侵跳板，能够接触到所有原本不该暴露在公网的内网设备，包括路由器管理后台、NAS 存储设备、打印机、家用摄像头、开发主机，以及所有监听本地端口的服务与应用。

这并非理论上的风险。

2026 年 1 月，KrebsOnSecurity 曾报道过 Kimwolf 僵尸网络事件，该僵尸网络滥用住宅代理网络建立隧道，反向接入代理节点背后的本地网络。攻击者不仅通过代理访问公网流量，还会触达代理节点同一局域网内的设备，并以此为基础进一步横向扩散。

从 SDK 的技术实现中也能看到对应的边界设计。Bright Data 的样本内置了明确的私有与本地地址黑名单，覆盖网段包括 127.0.0.0/8、10.0.0.0/8、172.16.0.0/12、169.254.0.0/16、192.168.0.0/16 以及 255.255.255.255。这项设计值得肯定，但也恰好印证了核心问题，电视本身具备建立内网连接的能力，访问边界只由 SDK 的策略代码决定。

Massive 的样本中，代理会话会解析服务器下发的 host:port 参数，并建立对应的 net.Socket 网络连接。Honeygain 也就是 Oxylabs 的样本中，服务器会下发 messageType 为 connect 的消息，携带 address.host 与 address.port 参数，后续通过分片消息向该连接写入数据。在本次分析的 Massive 与 Honeygain/Oxylabs 样本中，研究团队没有找到与 Bright Data 对等的私有网段黑名单。

这意味着真正的访问边界取决于服务商的政策与执行力度，而非不可突破的技术限制。边界的保障来自代理公司的客户审核、流量过滤、内部规则，以及 LG 或三星应用审核环节的约束。代理服务商可以声称流量仅用于经过审批的公网场景，但设备所有者没有任何可行的方式从电视端验证这一点。一旦边界规则变更、出现故障或是被恶意利用，原本被包装成网页索引的 SDK，就可能变成网络犯罪分子接入家庭网络的专属通道。

本次研究没有依赖应用商店描述或是权限提示文本，而是直接下载了 LG webOS 与三星 Tizen 的应用安装包，解包后对内部文件进行扫描。

研究人员通过特征指纹识别确认 SDK 组件，包括 Bright Data 的 brd\_api.js 文件与 brd\_sdk 服务、Massive 客户端与.massivesdk 服务、Honeygain/Oxylabs 的 SDK 文件与服务名称，以及相关的令牌或包名。所有被统计的应用都具备明确的代理 SDK 特征指纹。

黑鸟：自查。

相关：[智能电视正在成为全球AI数据爬虫的住宅代理节点](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186970&idx=1&sn=5a9a38c2019f2ad8e62d38d1e0c46bbe&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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