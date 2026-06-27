---
title: Minecraft恶意软件加载器使用RSA签名的智能合约更新来实现持久的C2通信
url: https://mp.weixin.qq.com/s/XAHtWvoDEug-deWh1w_szQ
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:46:20.311238
---

# Minecraft恶意软件加载器使用RSA签名的智能合约更新来实现持久的C2通信

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NjJJvP1VsUJlvYZiaBM5waHELSBn8R91mcGP0lJhFKj6DiaRm9iawpkj6Xg0JC6cjOgUm3VsrGvVLhLdiaaHjcRh4XV13vd010gOk/0?wx_fmt=jpeg)

# Minecraft恶意软件加载器使用RSA签名的智能合约更新来实现持久的C2通信

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一种新型且高度复杂的恶意软件加载器被发现隐藏在一个看似无害的 Minecraft 模组中。

研究人员发现了一项结合区块链技术和社会工程的攻击活动，旨在窃取玩家凭证并植入其他恶意载荷。

自 2026 年 1 月该活动开始以来，损失已经相当严重，已有超过 116,000 个独立系统遭到破坏。

这款名为 LoaderClient 的恶意软件伪装成 Minecraft Fabric 模组进行传播。一旦安装，它会立即窃取玩家的会话数据，包括显示名称、账户 UUID 和有效的 Microsoft OAuth 访问令牌。

被盗的令牌尤其危险，因为它无需密码或绕过双因素身份验证即可接管受害者的账户。

DarkAtlas 的分析师在一份与网络安全新闻 (CSN) 分享的报告中识别并详细描述了该恶意软件。

他们的调查结果显示，LoaderClient 是名为 WeedHack 的更广泛攻击活动的第一阶段有效载荷，WeedHack 是一个恶意软件即服务平台，可以免费使用，也可以每月支付 5 美元使用。

截至 2026 年 6 月，该行动已生成超过 3,820 个独特的恶意文件，并且每天记录 2,000 到 3,000 例新的感染。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PEmF0flszB2R594XZYyoY3z9XIRcS0uEjLlVicP9pSLS83M2XHicySuLTLPMSRRyOZgVKwoJfibg658vpAdQcNtiburiaDbB8rKCB0/640?wx_fmt=png&from=appmsg)

这种威胁最令人担忧之处在于它的传播方式。操作者会上传精心制作的YouTube视频，展示热门的MOD，并在视频描述中隐藏恶意下载链接。

他们还运营虚假门户网站，冒充合法的模组网站，并通过搜索引擎优化（SEO）来获取高排名。由于玩家习惯性地将杀毒软件的警告视为误报而置之不理，许多人因此关闭了杀毒软件的防御功能，在不知情的情况下运行了恶意软件。

该活动在 Telegram 上发展了一个拥有 850 多名注册用户的社区，其中许多是青少年，他们利用这些工具进行同伴骚扰、访问网络摄像头和劫持社交媒体。

这种转变反映出低成本恶意软件越来越多地被用于个人纠纷，而不仅仅是金融犯罪。

## **Minecraft恶意软件加载器使用RSA签名的智能合约更新**

LoaderClient 的独特之处在于其命令与控制架构。该恶意软件并非将服务器地址嵌入代码中，而是通过一种名为 EtherHiding 的技术查询以太坊智能合约来获取其活动的 C2 URL。

这使得通过域名查封或托管服务提供商的行动来破坏基础设施几乎不可能。

智能合约会返回一个带有 RSA 数字签名的 URL。恶意软件随后会使用该签名与硬编码的 2048 位 RSA 公钥进行比对，验证通过后才会信任该地址。

只有操作员的私钥才能生成有效的签名，因此即使篡改合约也会被拒绝，使得黑洞攻击毫无用处。

C2 URL 验证通过后，LoaderClient 会将第二阶段有效载荷完全下载到内存中，而不会将任何文件写入磁盘。该有效载荷使用 JNIC v3.7.0 编译，并将所有逻辑隐藏在加密的 Windows 原生 DLL 中。

它通过同一个以太坊合约独立地重新解析C2地址，并使用DNS over HTTPS来规避企业网络监控。以太坊合约地址是此次攻击活动最持久的标识，永久保存在区块链上。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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