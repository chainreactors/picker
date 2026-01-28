---
title: 新型“Stanley”黑产 MaaS 遭曝光，可令钓鱼扩展通过谷歌 Chrome 商店审核
url: https://mp.weixin.qq.com/s/2O0yrPj6Z5H7QN6EyqKxsw
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:33:24.020264
---

# 新型“Stanley”黑产 MaaS 遭曝光，可令钓鱼扩展通过谷歌 Chrome 商店审核

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UZ1NGUYLEFg3fnZWLw328RutErm4YmY9ueNW9JY1UUh1ibhB2SiauaM5vsYI7wFX0DJXxgZX2cnhnVhBnIsT0bhQ/0?wx_fmt=jpeg)

# 新型“Stanley”黑产 MaaS 遭曝光，可令钓鱼扩展通过谷歌 Chrome 商店审核

安世加
安世加

安世加

![]()

在小说阅读器中沉浸阅读

**新闻**

*News Today*

1 月 27 日消息，数据安全公司 Varonis 的安全研究人员发现了一种名为“Stanley”（取自卖家的化名）的新型恶意软件即服务（MaaS），宣称能够制作并发布通过 Google 审核的恶意 Chrome 浏览器扩展，并成功上架至 Chrome 应用商店。

根据研究人员的描述，Stanley 主打功能是 —— 通过拦截用户浏览行为，在网页上覆盖一个全屏 iframe，从而在不改变浏览器地址栏显示地址的情况下，向用户展示指定的钓鱼内容。

Varonis 表示，该 MaaS 提供的恶意扩展可在 Chrome、Edge 和 Brave 浏览器中运行，并支持所谓的“静默自动安装”。此外，其服务还允许客户进行一定程度的定制，以适配不同的攻击场景。

Stanley 采用订阅制收费模式，其中价格最高的“Luxe Plan”包含一个管理面板，并承诺提供将恶意扩展发布到 Chrome 应用商店的全流程支持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UZ1NGUYLEFg3fnZWLw328RutErm4YmY9ugZf7oxHMe4eoQW8dibnYiacINjmQaXInk1jcnd5h2QrF8YibFiaRRrvZA/640?wx_fmt=png&from=appmsg)

从技术实现上看，Stanley 的核心攻击方式是利用全屏 iframe 覆盖真实网页内容，使受害者在看到合法域名的情况下，实际与钓鱼页面进行交互。研究人员指出，这种方式可以降低用户的警惕性，从而提高攻击成功率。

此外，攻击者可通过 Stanley 的控制面板随时启用或关闭页面劫持规则，并能直接向受害者浏览器推送通知，引导其访问特定页面，以加快钓鱼流程。该服务还支持基于 IP 的受害者识别功能，可进行地理位置定向，并在不同会话和设备之间进行关联分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UZ1NGUYLEFg3fnZWLw328RutErm4YmY9iaqfXwSKJibIgq9aGkguEfq29rYbHbbQzUDFJc8T6mcbgrJUhbbbPNbA/640?wx_fmt=png&from=appmsg)

在通信机制方面，备用域名轮换能力，以提高在遭遇封禁或下线行动时的存活性。

研究人员同时指出，从纯技术角度来看，Stanley 并不包含复杂或前沿的攻击手段，而是采用了较为直接的方式组合多种已知技术。其代码质量被描述为较为粗糙，存在俄文注释、空的异常捕获块以及不一致的错误处理逻辑。

Varonis 认为，Stanley 真正引人关注之处在于其分发模式，尤其是其宣称能够通过 Chrome 应用商店审核并将恶意扩展发布到主流平台。此前，赛门铁克（Symantec）和 LayerX 的独立报告也曾指出，恶意扩展仍可能绕过官方审查机制进入用户环境。

研究人员提醒用户，应尽量减少安装不必要的浏览器扩展，在安装前仔细查看用户评价，并核实扩展发布者的可信度，以降低潜在风险。

本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！

文章转自：IT之家

安世加为出海企业提供SOC 2、ISO27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UZ1NGUYLEFgcA7bggpA95iaqhjhPnOKQj3Fm4IIBNGywCNJLkfrXvUj1EFZKblGnOwCqZrdYAK9yG8dz5o9bRkw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

安世加

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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