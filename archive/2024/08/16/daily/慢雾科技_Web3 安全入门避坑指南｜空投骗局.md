---
title: Web3 安全入门避坑指南｜空投骗局
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500174&idx=1&sn=e3cb8f76396b64e8dd23bbcdc1a24bcd&chksm=fddebf09caa9361fef844c27d8b8b4360cac62f2fb5f3b8b9fe83f1cfa44de95311a62915f8d&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-08-16
fetch_date: 2025-10-06T18:04:21.540332
---

# Web3 安全入门避坑指南｜空投骗局

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLbvj3oCz0IX8VSAAcxrDv6EYicJiahdap0XUjdbguFdtXySwaOV6FDRrb0ibKNYLW9NI3rSSA9M8UBzw/0?wx_fmt=jpeg)

# Web3 安全入门避坑指南｜空投骗局

原创

慢雾安全团队

慢雾科技

[#Web3 安全入门避坑指南](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU4ODQ3NTM2OA==&action=getalbum&album_id=3398201563809300482#wechat_redirect)

**背景**

在上一期 [Web3 安全入门避坑指南](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500038&idx=1&sn=00ff98cee22c817942d2e1bce4f8db46&chksm=fddebf81caa93697ba13a1ad0f8eb3baab0c739926912e671c3ac4d81b18467feee1bffae095&scene=21#wechat_redirect)中，我们主要讲解了多签钓鱼的相关知识，包括多签机制、造成多签的原因及如何避免钱包被恶意多签等内容。本期我们要讲解的是一种无论在传统行业还是加密领域，都被视为有效的营销手段 —— 空投。

空投能够在短时间内将项目从默默无闻推向大众视野，迅速积累用户基础，提升市场影响力。用户在参与 Web3 项目时，需要点击相关链接、与项目方交互以获取空投代币，然而从高仿网站到带后门的工具，黑客早已在用户领空投过程的上下游布满了陷阱。因此，本期我们将通过分析一些典型的空投骗局来讲解相关风险，帮助大家避坑。

#

# **什么是空投**

Web3 项目方为了增加项目的知名度和实现初期用户的积累，常常会免费向特定钱包地址分发代币，这一行为被称为“空投”。对项目方而言，这是获得用户最直接的方式。根据获取空投的方式，空投通常可以分为以下几类：

* 任务型：完成项目方指定的任务，如转发、点赞等。
* 交互型：完成兑换代币、发/收代币、跨链等操作。
* 持有型：持有项目方指定的代币以获得空投代币。
* 质押型：通过单币或双币质押、提供流动性或进行长期锁仓来获得空投代币。

#

# **领空投时的风险**

**假空投骗局**

此类骗局又可以细分为以下几种：

1. 黑客盗取项目方的官方账号发布假空投的消息。我们经常可以在资讯平台上看到“某项目的 X 账号或者 Discord 账号被黑，请广大用户不要点击黑客发布的钓鱼链接”的安全提醒。据慢雾 2024 上半年区块链安全与反洗钱报告的数据，仅 2024 上半年，项目方账号被黑事件就有 27 件。用户基于对官方账号的信任而点击这些链接，进而被引导至伪装成空投的钓鱼网站。一旦在钓鱼网站上输入了私钥/助记词或授权了相关权限，黑客就能盗走用户的资产。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKvDYW9xTvgynX9hKYmA222vPPEb1UAop9ibWsgicXpdMp5LAlnA9AXf0Sg/640?wx_fmt=png&from=appmsg)

2. 黑客使用高仿的项目方账号在项目方官方真实账号的评论区刷留言，发布领取空投的消息，诱导用户点击钓鱼链接。此前慢雾安全团队分析过这类手法并提出了应对建议，见[真假项目方 | 警惕评论区高仿号钓鱼](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499326&idx=1&sn=513d9d58b559f95f98d34e8d2e991064&chksm=fdde80b9caa909af2245149db21e916834aae08c538d4e8017c6a770990ffb0e65e3856bf6b5&scene=21#wechat_redirect)；此外，在真项目方发布空投的消息后，黑客也会紧随其后，在社交平台上使用高仿账号大量发布包含钓鱼链接的动态，许多用户因未仔细辨别而安装了虚假 APP 或打开钓鱼网站进行了签名授权的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKvMkMCsqXoLvjy6tm8sKJwwwic2IR0xqbluB9vPWibVicA2yvljvoHHLgOw/640?wx_fmt=png&from=appmsg)

(https://x.com/im23pds/status/1765577919819362702)

3. 第三种诈骗套路更可恶，妥妥的骗子，他们潜伏在 Web3 项目的群组里，挑选目标用户进行社会工程攻击，有时以空投为诱饵，“教”用户按照要求转移代币以获取空投。请广大用户提高警惕，不要轻易相信主动联系你的“官方客服”或是“教”你如何操作的网友，这些人大概率是骗子，你只是想领个空投，结果却损失惨重。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKv9dUKbE4icZqVApbEHEDuEiaKqw4axYSgkcDGLRh0eqpb36EejrkpnL9A/640?wx_fmt=png&from=appmsg)

**“白给”的空投代币**

开篇提到，用户往往需要完成某种任务才能获取空投，我们接下来看看“白给“用户代币的情况。黑客会向用户的钱包空投没有实际价值的代币，用户看到这些代币，可能会尝试与之交互，例如转移、查看或在去中心化交易所上进行交易。然而我们逆向分析一个 Scam NFT 的智能合约发现，当尝试挂单或转移这个 Scam NFT 时会失败，然后出现错误提示“Visit website to unlock your item”，诱导用户访问钓鱼网站。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKvNMB9d2a5cZ1DwVgSx6ibznyxlZy8fV7as1bPuxtR1vDrlbX7bwiaYWeQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKvYYcR2MmibiaMsol5tDGlvRw6dHlPdibIZHic86Nic4eszw1ibT8OiaafyPP7A/640?wx_fmt=png&from=appmsg)

如果用户访问了 Scam NFT 引导的钓鱼网站，黑客便可能进行以下操作：

* 批量“零元购”有价值的 NFT，见[“零元购” NFT 钓鱼分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496261&idx=1&sn=9c657f56128df327e27c49fc49d4cc02&chksm=fdde8cc2caa905d4a9cd709c44888b54ccf4071301056052f0bc800b6d5d487873d3bafd124a&scene=21#wechat_redirect)
* 拿走高价值 Token 的 Approve 授权或 Permit 签名
* 拿走原生资产

接下来我们再看看黑客如何通过一个精心设计的恶意合约窃取用户的 Gas 费。

首先，黑客在 BSC 上创建了一个名为 GPT 的恶意合约 (0x513C285CD76884acC377a63DC63A4e83D7D21fb5)，通过空投代币吸引用户进行交互。

用户与该恶意合约交互时，出现了需要批准该合约使用钱包中代币的请求。如果用户批准了这个请求，恶意合约会根据用户钱包中的余额，自动提高 Gas 限额，这使得后续的交易消耗更多的 Gas 费。

利用用户提供的高 Gas 限额，恶意合约使用多余的 Gas 来铸造 CHI 代币（CHI 代币可以用于 Gas 补偿）。恶意合约积累了大量的 CHI 代币后，黑客可以通过燃烧 CHI 代币，获得合约销毁时返还的 Gas 补偿。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKvoibwRDU3SIGoCas2uStTSibgUgTP9XvqaXusFrTO6icY3y7V2jQLVrTRw/640?wx_fmt=png&from=appmsg)

(https://x.com/SlowMist\_Team/status/1640614440294035456)

通过这种方式，黑客巧妙地利用用户的 Gas 费为自己牟利，而用户可能并未察觉到他们已经支付了额外的 Gas 费。用户本以为可以通过出售空投代币获利，结果却被盗取了原生资产。

**带后门的工具**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKvwtvhRrKNFbJWpkSDPibo1WraxHLwNmiaWLAC7nQFpm9ib5WcBZw2QKVmg/640?wx_fmt=png&from=appmsg)

 (https://x.com/evilcos/status/1593525621992599552)

领空投的过程中，一些用户需要下载翻译或查询代币稀有度之类的插件，这些插件的安全性存疑，且有的用户下载插件时没有从官方渠道下载，这就使得下载到带有后门的插件的可能性大大增加。

此外，我们还注意到网上有出售领空投脚本的服务，声称可以通过运行脚本完成自动批量交互，听起来挺高效的，但是请注意，下载未经审查和验证的脚本存在极大的风险，因为你无法确定脚本的来源和它的真实功能。脚本可能包含恶意代码，潜在的威胁包括盗取私钥/助记词或者执行其他未授权的操作。而且，一些用户在执行相关类型的风险操作时，未安装或是关闭了杀毒软件，导致未能及时发现设备中了木马，进而受损。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYhTcZsa6ULfJaQRMEnRgKvdglr7tnicgAoSia3vicqh2EckNajjzLZZcb4NibZrhFJApGxrBYbC3pvJg/640?wx_fmt=png&from=appmsg)

# **总结**

在本期指南中，我们主要通过分析骗局的方式为大家讲解领空时会有哪些风险，现在许多项目都把空投作为营销手段，用户可以通过以下措施减少在领空投过程中资产受损的可能性：

* 多方验证，访问空投网站时，请仔细检查网址，可以通过项目的官方账号或公告渠道确认，还可以安装钓鱼风险阻断插件（如 Scam Sniffer），协助识别钓鱼网站。
* 钱包分级，用于领空投的钱包存放小额资金，把大额资金放在冷钱包。
* 对于从未知来源收到的空投代币要保持警惕，不要轻易执行授权/签名操作。
* 注意检查交易的 Gas 限额是否异常高。
* 使用知名杀毒软件，如卡巴斯基、AVG 等，保持实时防护开启，并随时更新最新病毒库。

**往期回顾**

[初识 TON：账号、Token、交易与资产安全](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500158&idx=1&sn=7496a1dcfa1326533a145348078bb996&chksm=fddebff9caa936ef22ef30829b17a5e573b4961808b7ea5b1858a014f3058215b02d85485031&scene=21#wechat_redirect)

[「区块链黑暗森林自救手册」印尼文版正式发布](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500140&idx=1&sn=88f5db074ebd46d5ef0debb09aeb90a7&chksm=fddebfebcaa936fdecb584664a7c668adde29124f69886d189ca16aa1e42470e5ad89ea74511&scene=21#wechat_redirect)

[每月动态 | Web3 安全事件总损失约 2.79 亿美元](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500129&idx=1&sn=05f509600c933d84fa6d74e45bc084ae&chksm=fddebfe6caa936f03df20aeee4a9ee6ebfac12f299b7e202b461a942554694233e6452c80f3d&scene=21#wechat_redirect)

[慢雾：X 账号安全排查加固指南](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500113&idx=1&sn=565d07ddee32d31b1e5d3271281e7c3f&chksm=fddebfd6caa936c02a5600ff8c266caf7d4798b41c4d1600aea03ce5c6b9433c3e107bd9c041&scene=21#wechat_redirect)

[TonConnect SDK 的 Origin 伪造风险分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500083&idx=1&sn=236a3bc7285c68e9636e231d5704a629&chksm=fddebfb4caa936a27719caf94d384e21d77b40ed876748f218ae8568504632200abe713c15e9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togv4VUdq4r7iak19Hta2pfbzPrGohPNR71WxPKrBoK9nyibPVL7ssCuW3yA/640?wx_fmt=png)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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