---
title: 新瓶装旧酒｜套利 MEV 机器人骗局
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500549&idx=1&sn=f56cdda53356f44d0a6fb4539e324ef6&chksm=fddebd82caa93494fe315e4ae661cdc1bf115edec17a0d63cbe57c182cac4f3c4d6250ac1d15&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-10-13
fetch_date: 2025-10-06T18:51:44.012115
---

# 新瓶装旧酒｜套利 MEV 机器人骗局

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7AROiaIKgxKKsRfMhjdq6UeCXuPEvk855rQaiaDvhKIRl5g4sgWj6V4gMxicA/0?wx_fmt=jpeg)

# 新瓶装旧酒｜套利 MEV 机器人骗局

原创

慢雾安全团队

慢雾科技

**背景**

今年初，慢雾创始人 Cos 在 X 上提醒用户注意套利 MEV 机器人骗局，如今黑客团伙也是紧跟热点，骗局的名字也从“简单易用的 Uniswap 套利 MEV 机器人”变成了“ChatGPT 套利 MEV 机器人：如何使用滑点机器人每天完全被动地赚取 2000 美元”。慢雾安全团队注意到，近期因这类骗局受损的用户数量有所增加，因此，本文将讲解该骗局的套路和分析骗子的资金转移模式，帮助用户避免落入此类骗局。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7AROuCPraQaZNdr13bRuJr2Rwc9w2ibCUpf1JtoYLUPWSBr4rRicIxXKIPLA/640?wx_fmt=png&from=appmsg)

(https://x.com/evilcos/status/1745728599171457120)

#

# **套利反被骗**

AI 已经成为越来越多人提升生产力的工具，骗子也深谙这一点，给自己的骗局带上了 ChatGPT 这个标签，既吸引注意力，又显得靠谱高级。然而，ChatGPT 只在骗子的视频教程里短暂出现过：骗子声称套利机器人的代码是他利用 ChatGPT 生成的，顺带打消了一部分用户对代码作恶的怀疑。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7AROSX7qwoCQ5V4Yyk7vmELgJMLR0DLy3eDG6x2teApibLz3Omb3pxPJ47g/640?wx_fmt=png&from=appmsg)

 (https://www.youtube.com/watch?v=Z32hH3eLK-c)

实际上，仔细看骗子在 YouTube 制作的视频，不难发现音画不同步，历史视频是凑数的，账号大概率是买的。种种迹象表明这个 YouTuber 不可信，尽管评论区几乎被好评和感谢的话占领，但往下翻就能发现一些受害者的提醒和警告。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7AROZZBPcgjtWic9aE9oLJ05Ep44icmF7Q7LMzVibEIMdHClh8wL8uFEI83hQ/640?wx_fmt=png&from=appmsg)

骗子声称，他的这个机器人可以监控 Ethereum 上的新代币和大的价格变化，寻找套利机会，用户只需要坐等收钱就行。而用户首先得有个 MetaMask 钱包，然后打开教程中提供的 Remix 链接（假 Remix）。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7AROga014GdweiaGlKM2JOtboyE0d3o8wWadZaoxkDPcviclMbGCSLUic0F6g/640?wx_fmt=png&from=appmsg)

接着，用户需要粘贴骗子提供的代码、编译机器人和部署智能合约。到了这一步，骗子表示用户得为合约提供初始资金，且往合约里存越多的 ETH，就能获得越多的利润。而在用户按上述流程操作并点击了“start”后，钱就“消失”了，打入的套利本金都进入骗子钱包地址，因为代码有后门。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7ARO4MrjpdQoVWHyIvphgLkESDT1fnvqFsygssX9ibVroibXcgV9hrcOOqibQ/640?wx_fmt=png&from=appmsg)

我们以 Web3 反诈骗平台 Scam Sniffer 报道过的下述诈骗事件为例，分析此类骗子的资金转移模式。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7ARO7RQ1vDibAvItkbdiaEOuRcOsFGZqFgAY15nAPC7l57IA6lB5ctTQ4pJw/640?wx_fmt=png&from=appmsg)

(https://x.com/realScamSniffer/status/1828364436241031669)

使用链上追踪和反洗钱平台 MistTrack 查询骗子的地址(0xAEF35f154C318c87744913f38A6d357691258122)，可以看到从八月底至今，仅骗子的这个地址就已获利约 30 ETH，受害者超过百人。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7ARONfOcY0zV9008qfqlibOXZdD4hvoMFyS4DqaX0dlzlSwSAzy9OZbjHGw/640?wx_fmt=png&from=appmsg)

该地址的资金转入模式单一，均为受害者根据上述骗局的流程操作，将 ETH 转入合约，随后被骗子盗走。转出模式呈现直接转入交易所；或是转移至用于暂存资金的地址（如：0xea06b983e144432919779b236ba28ece28b74ec6），然后再转入交易所。

下图中的 0x442a4960c783affe2b6d9884f32d7cf2683a408b 和 0x44d63ce270637553f89f3c2706869d98d1248da3 也是骗子用来直接收集受害者资金的地址，这两个地址创建于八月底，至今已盗走约 20 ETH，受害者约 93 名。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7AROU6RLFZFl70LicsnB2LKfCKd2ak4Q8YADrjRC8n1Egc3vAzibqN9mUqfg/640?wx_fmt=png&from=appmsg)

由于骗子采取广撒网，积小利的模式，因此虽然受害者众多，但因损失相对较少，花费精力去追究不太现实，这类骗子也因此能够长期逍遥法外，给骗局换个“皮”便可继续进行类似的欺诈活动。Remix 已在其网站提醒用户们注意此类骗局，在其发布在 Medium 上的骗局分析文章的评论区发现，从两年前到近期都有受害者发布被骗的留言，还有不少用户提供了相关诈骗视频的链接，提醒大家注意安全，可见这类骗局的泛滥程度。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYbsD8EhU1bQ18ssy2G7AROdQQTzx2Mkezrgrs4pwsLMZ11GZnpkcspQHTdMpCjwjGZALZv5t3RXw/640?wx_fmt=png&from=appmsg)

#

# **总结**

慢雾安全团队提醒广大用户，切勿点击不明链接或运行不明代码。既然骗子声称代码是由 ChatGPT 生成的，那我们至少可以将代码再发给 ChatGPT、Claude 等工具检查下，看看是否包含恶意行为。许多用户原本只是希望赚取被动收益，也愿意付出本金，但跟着骗子一通操作，没想到最后本金也没了，倒是骗子靠着这些“教程”忽悠了一个个受害者往他的钱包里转钱，实现“被动收益”。因此，请用户们保持警惕，操作前多确认下是天降馅饼还是陷阱，避免资金受损。

作者 | Liz

编辑 | Liz

**往期回顾**

[慢雾：貔貅盘防范指南](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500535&idx=1&sn=a6e577d22478824f9350add2437ebcda&chksm=fddebc70caa935669bfb2afaf0edcce673b3e2097d3ee6b98763e68010011304adc34233c44c&scene=21#wechat_redirect)

[报告解读｜UNODC 发布东南亚跨国有组织犯罪的欺诈报告](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500520&idx=1&sn=177c686cd500748da4808fb23b569614&chksm=fddebc6fcaa935795482f708ed51d8f48083edee058b5100d37870eaa7f60c0706ae120b9f40&scene=21#wechat_redirect)

[慢雾：2024 Q3 MistTrack 被盗表单分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500472&idx=1&sn=b8af0c6be27c5f779a9886e166ef8287&chksm=fddebc3fcaa93529cd590f829d1219d5594f9662263493dcddda5733842ceb946a95d538dda6&scene=21#wechat_redirect)

[每月动态 | Web3 安全事件总损失约 1.7 亿美元](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500472&idx=2&sn=cbc8fb3fc309128cb863b0539d28d5f0&chksm=fddebc3fcaa9352943aa2777205c0b4790d1f2b4d27af2e56821981d458ff073fec926fe11a9&scene=21#wechat_redirect)

[慢雾：Uniswap v3 协议分析与审计要点](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500440&idx=1&sn=e447aeff528fb5a5c96a3d88f2d31531&chksm=fddebc1fcaa9350964866990b32e3a928e3a6b76a9c39eabe7e8755c4bb47a03a15e48da678a&scene=21#wechat_redirect)

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