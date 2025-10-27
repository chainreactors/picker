---
title: WiFi 协议漏洞可用于劫持网络流量
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516076&idx=2&sn=7aa0709e9df4a0d8c797ce6c54547971&chksm=ea948ec6dde307d069669905324ed5495a07a93a3b8b7382f3bd7a98c0ca31d2a53d56e329c5&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-30
fetch_date: 2025-10-04T11:07:53.824279
---

# WiFi 协议漏洞可用于劫持网络流量

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQUh334wvWDKcC86ibud5PEDsTndS1UZpH4ojxNtKKobuD6En68ktdkUomIzAssBsT5iaqfpu5rWnCQ/0?wx_fmt=jpeg)

# WiFi 协议漏洞可用于劫持网络流量

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全公司的研究员在 IEEE 802.11 WiFi 协议标准中发现一个根本性漏洞，可导致攻击者诱骗访问点以明文形式泄漏网络框架。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQUh334wvWDKcC86ibud5PEDRmIvO4YY2Mp4jSAFCE9QqJXus13wYJTaDgiaicTVTgO8fq8SJHEnDBaQ/640?wx_fmt=gif)

WiFi 框架是由表头、数据payload 和封装尾组成的数据容器，包括的信息有源和目的MAC地址、控制和管理数据。这些框架排序并以受控形式传输以阻止碰撞，并通过监控接收点的闲忙状态将数据交换性能最大化。

研究人员发现，排列/缓冲框架无法防御攻击者，后者可操纵数据传输、客户端欺骗、框架重定向和捕获。

研究人员在技术分析报告中指出，“由于影响多种设备和操作系统（Linux、FreeBSD、iOS 和安卓），以及这些漏洞可用于劫持TCP连接或拦截客户端和 web 流量，因此攻击的影响范围广泛。”

**0****1**

节电缺陷

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQUh334wvWDKcC86ibud5PEDFicYC8uesdFX0ibaPOZ7du21Zz3HVaGosLxG4ibhvC1s66451foAdfDmA/640?wx_fmt=gif)

IEEE 802.11标准包括节电机制，可允许WiFi 设备通过缓冲或排列睡眠设备的框架保省电。当客户端站（接收设备）进入睡眠模式时，则会向接入点发送带有包含节能位的标头的框架，因此所有框架都排队。然而，该标准并未提供关于管理这些排队框架安全性的明确指南，而且并未设限，如这些框架可以保持这种状态的时长。一旦客户端站唤醒，接入点就会取消缓冲框架的排队，应用加密并将其传输到目的地。

攻击者可欺骗网络上设备的 MAC 地址并将节能框架发送到接入点，强制它们对目标框架排队。之后攻击者传输唤醒框架以检索框架栈。这些传输的框架一般通过组结合的加密密钥（在所有WiFi 网络中的设备中共享）或者成对加密密钥（每台设备是唯一的，用于加密两台设备之间交换的框架）进行加密。

然而，攻击者可通过向接入点发送认证和关联框架的方式更改这些框架的安全上下文，从而强制接入点以明文形式传输框架或者以攻击者提供的密钥进行加密。

研究人员可通过自创的自定义工具 MacStealer 实施该攻击。该工具可测试 WiFi 网络中是否存在客户端隔离绕过并拦截 MAC 层其它客户端的流量。研究人员指出，源自Lancom、Aruba、思科、华硕和D-Link 的网络设备模型受这些攻击影响。

研究人员提醒称，这些攻击可用于注入恶意内容如将 JavaScript 注入 TCP 数据包中。他们指出，“攻击者可通过受骗的发送者IP地址注入偏离路径的 TCP 数据包，利用自身的联网服务器将数据注入 TCP 连接中。例如，这可被滥用于将恶意 JavaScript 以明文HTTP 连接形式发送给受害者，目的是利用客户端浏览器中的漏洞。”

虽然该攻击也可用于窥探流量，但由于多数 web 流量通过 TLS 加密，因此影响有限。

**0****2**

思科证实漏洞存在

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQUh334wvWDKcC86ibud5PEDFicYC8uesdFX0ibaPOZ7du21Zz3HVaGosLxG4ibhvC1s66451foAdfDmA/640?wx_fmt=gif)

思科是首个证实该 WiFi 漏洞影响的厂商。该公司表示论文中所提到的攻击可能适用于 Cisco Wireless Access Point 产品和具有无线能力的 Cisco Meraki 产品。

然而，思科认为被检索的框架可能无法危害保护得当的网络。然而，该公司仍然建议应用多种缓解措施如使用策略执行机制 Cisco Identity Services Engine (ISE)，通过执行思科 TrustSec 或 Software Defined Access (SDA) 技术限制网络访问权限等。

思科在安全公告中指出，“思科还建议执行传输层安全性，在尽可能的情况下加密数据，因为它将使攻击者无法使用所获得的数据。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[Realtek WiFi SDK 被曝多个漏洞，影响供应链上至少65家厂商近百万台IoT设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507215&idx=1&sn=7c95fd8598c4f33e573e12e6f92c9808&chksm=ea94ec65dde36573649c4936289838a96ef4d81fe5a5b17b6c5f3603897fa056588850c946ae&scene=21#wechat_redirect)

[这个 bug 可劫持同一 WiFi 网络上所有的安卓版火狐移动浏览器](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247495106&idx=2&sn=1b0fe939237e5dcc8a2b5feede9e847c&chksm=ea94dca8dde355be1b3c2aadca4eff191b6d902d17d4aebf96e0d9617638d26f6f6b07c21288&scene=21#wechat_redirect)

[1997年起至今的所有 WiFi 设备均易遭 Frag 攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247504175&idx=1&sn=689f4e5d274d77b5ef431ec903a71f42&chksm=ea94e045dde369539a7b23a9be1aa8f664932e46267a239563c4976c60aab38e25d1fbe13ed0&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/wifi-protocol-flaw-allows-attackers-to-hijack-network-traffic/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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