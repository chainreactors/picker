---
title: 慢雾：2024 Q2 MistTrack 被盗表单分析
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499939&idx=1&sn=9a19ea41c058d225c6ccbb21736f8923&chksm=fddebe24caa93732fab9dc5b29801e718e4a72db379f53db6a5b0532d4f22e957f6221946f2f&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-07-03
fetch_date: 2025-10-06T17:43:31.427273
---

# 慢雾：2024 Q2 MistTrack 被盗表单分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawypDVcEQpbRojWjG3KjjYV9f7mwQyuC0uRgUc5S3ot8eS4Bch54f8tzg/0?wx_fmt=jpeg)

# 慢雾：2024 Q2 MistTrack 被盗表单分析

原创

慢雾 AML 团队

慢雾科技

随着区块链的快速发展，针对用户的盗币、钓鱼、欺诈等安全事件日益增多，且攻击手法多样。慢雾 SlowMist 每天都会收到大量受害者的求助信息，希望我们提供资金追踪和挽救的帮助，其中不乏丢失上千万美金的大额受害者。基于此，本系列通过对每个季度收到的被盗表单进行统计和分析，旨在以脱敏后的真实案例剖析常见或罕见的作恶手法，帮助用户学习如何更好地保护好自己的资产。

据统计，MistTrack Team 于 2024 年 Q2 季度共收到 467 份被盗表单，包括 146 份海外表单和 321 份国内表单，我们为这些表单做了免费的评估社区服务（Ps. 本文内容仅针对来自表单提交的 Case，不包括通过邮箱或其他渠道联系的 Case）

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawywVqa3icaTPTyvlCd7YcgWgobNJV3rLWamBibibYsLFIr751A8KDlf9z9g/640?wx_fmt=jpeg&from=appmsg)

其中，MistTrack Team 协助 18 位被盗客户在 13 个平台冻结约 2066.41 万美元的资金。

**被盗原因 Top 3**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawyH8iaqGliclVRMPk8aoH9GA5DcAs9ZkmcuBpvicxrVibQdfOq61p7bXic2xg/640?wx_fmt=png&from=appmsg)

2024 年 Q2 表单最常见的作恶手法如下：

**私钥泄露**

据 Q2 表单的统计，不少用户会将私钥/助记词存储在 Google 文档、腾讯文档、百度云盘、石墨文档等云盘之中，有的用户会通过微信等工具将私钥/助记词发送给自己信任的朋友，更有甚者通过微信的图片识字功能，将助记词复制到 WPS 表格中，然后加密这个表格并开启云服务，同时又存在电脑的本地硬盘中。这些看似提高了信息安全的行为实际上都极大地增加了信息被窃取的风险。黑客们常利用“撞库”这种方法，通过收集网络上公开泄露的账号密码数据库，尝试登录这些云存储服务网站。虽然这是碰概率的行为，但只要登录成功，黑客就能轻易地找到并盗取与加密货币相关的信息，这些情况可以被看作是信息被动泄露。另外还存在一些主动泄露的案例，例如受害者被冒充客服的骗子诱导填写助记词，或者在 Discord 等聊天平台上被钓鱼链接欺骗，然后输入私钥信息等。在此，MistTrack Team 强烈提醒大家，任何情况下都不应该把私钥/助记词透露给任何人。

除此之外，假钱包也是导致私钥泄露的重灾区。这部分已经是老生常谈，但依然有大量用户在使用搜索引擎时，无意间点击广告链接，从而下载了假冒的钱包应用。由于网络原因，很多用户会选择从第三方下载站获取相关应用。尽管这些站点声称其应用均源自 Google Play 的镜像下载，但是其真实安全性存疑。此前慢雾安全团队就分析过第三方应用市场 apkcombo 上的钱包应用，结果发现 apkcombo 提供的 imToken 24.9.11 版本，是一个并不存在的版本，且是目前市面上假 imToken 钱包最多的一个版本。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawyrWGjic74XUfQXWpVA16fdGwFBM6kK5B12EpOymIYhLGOtaibOfZSgW7g/640?wx_fmt=png&from=appmsg)

我们还追踪到了一些与假钱包团队有关的后台管理系统，其中包含用户管理、币种管理以及充值管理等复杂数字货币控制功能。这类钓鱼行为具备的高级特性与专业程度都已超出了许多人的想象。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawyZk7tS7yKB8IYSx4Pl4V0C4tWa6H0VwKIJu3auEQ0ZrsuY65icUNKgLQ/640?wx_fmt=png&from=appmsg)

例如，Q2 有一个较为罕见的案例：某用户在搜索引擎中搜索“Twitter”，不慎下载了一个假冒版的 Twitter 应用。当用户打开这个应用时，系统弹出了一个提示，声称由于地区限制，需要使用 VPN，并引导用户下载该应用自带的虚假 VPN，结果导致该用户的私钥/助记词被窃取。这样的案例再次警示我们，对于任何在线应用和服务，都应进行仔细审查和验证，确保其合法性与安全性。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawySVycFAyUSWqsl6Zn93OBFeoZyQZRmYbYAKVoMU8zkPX0ffzIStrY5g/640?wx_fmt=png&from=appmsg)

**钓鱼**

根据分析，Q2 多起被盗求助事件的被钓鱼原因都是：用户点击了发布在知名项目推特下的钓鱼链接评论。此前慢雾安全团队做了针对性的分析统计：约有 80% 的知名项目方在发布推特后，评论区的第一条留言会被诈骗钓鱼账号占据。我们还发现 Telegram 上有大量售卖 Twitter 账号的群组，这些账号的粉丝数量和发帖数量不一，注册时间也各不相同，这让潜在的买家可以根据他们的需求选择购买。历史记录显示，大多数出售的账号都与加密货币行业或网络红人有所关联。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawyFIr4Qlp4Ub49lFwqRicT3ehrOZ2INf64x4ShjU9wbdp9Gb1aLbN8sWw/640?wx_fmt=png&from=appmsg)

除此之外，还存在一些专门售卖 Twitter 账号的网站，这些网站销售各年份的 Twitter 账号，甚至支持购买高度相似的账号。例如，假冒账号 Optimlzm 和真实账号 Optimism 外观相似程度极高。购买了这种高度相似的账号后，钓鱼团伙就会采用推广工具提升账号的互动和粉丝量，以此提高账号的可信度。这些推广工具不仅接受加密货币支付，还销售包括点赞、转发、增粉等在内的多种社交平台服务。利用这些工具，钓鱼团伙可以得到一个具有大量粉丝和帖子的 Twitter 账号，并模仿项目方的信息发布动态。由于与真实项目方的账号具有高度的相似性，使得许多用户难以分辨真假，从而进一步增加了钓鱼团伙的成功率。随后，钓鱼团伙实施钓鱼行动，比如使用自动化机器人来关注知名项目的动态。当项目方发布推文后，机器人会自动回复以抢占第一条评论，从而吸引更多浏览量。鉴于钓鱼团伙伪装过的账号与项目方账号极其相似，一旦用户疏忽，点击假账号上的钓鱼链接，然后进行授权、签名，便可能导致资产损失。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawypEovhznUxrqmya7ibfyxibpkHol8DicgiaAcpaZektXkMTNAppXJaPydTg/640?wx_fmt=png&from=appmsg)

总的来说，纵观区块链行业的钓鱼攻击，对个人用户来说，风险主要在“域名、签名”两个核心点。为了实现全面的安全防护，我们一直主张采取双重防护策略，即人员安全意识防御 + 技术手段防御。技术手段防御是指借助各种硬软件工具，如钓鱼风险阻断插件 Scam Sniffer 来确保资产和信息安全，用户在打开可疑的钓鱼页面时，工具会及时弹出风险提示，从而在风险形成的第一步就将其阻断。在人员安全意识防御方面，我们强烈建议大家深度阅读并逐步掌握《区块链黑暗森林自救手册》（https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README\_CN.md）。只有通过这两种防护策略的相互配合，才能有效对抗不断变化、升级的钓鱼攻击手段，守护资产安全。

**诈骗**

诈骗手法有很多，Q2 最为常见的诈骗手法是貔貅盘。在传说中，貔貅被视为一种神奇的生物，据说它可以吞噬所有事物而不排泄出来，寓言所说的黄金和珠宝等财宝一经吞入，便无法从其体内取出。因此，貔貅盘被用来比喻一旦购买就无法再卖出的数字货币。

某位受害者描述了自己的经历：“我当时在 Telegram 群组提了一个问题，有个人热心回答了我很多问题，也教了我很多东西，在我们私聊了两天之后，我觉得他人挺不错的。于是他提议带我去一级市场购买新代币，并在 PancakeSwap 上给我提供了一个币种的合约地址。我购买之后，这个币一直在猛涨，他告诉我这是半年一遇的黄金机会，建议我立即加大投资。我感觉事情没这么简单就没采纳他的建议，他就一直催我，一催我意识到可能被欺骗了，我便请群里的其他人帮忙查询，结果发现这确实是貔貅币，我也试过了只能买不能卖。当骗子发现我不再加仓时，他也将我拉黑。”

这位受害者的经历实际上反映了貔貅盘诈骗的典型模式：

1. 诈骗者部署设置了陷阱的智能合约，并抛出承诺高利润的诱饵；

2. 诈骗者极力吸引目标购入代币，受害者购买后常会看到该代币快速升值，于是，受害者通常会决定等到代币的涨幅足够大了再尝试兑换，结果发现无法卖出已购的代币；

3. 最后，诈骗者提取受害者投资的资金。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawyNiaFRCjNZickCSh2FE98ob35t7bvUjdLBUY6arJcsJxqr60vK9yTxLBw/640?wx_fmt=png&from=appmsg)

值得一提的是，Q2 表单所提到的貔貅币都发生在 BSC 上，下图中可以看到貔貅币有很多交易，骗子还把持有的代币发送给钱包和交易所，造成有很多人参与的假象。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYMXfFPmibNwtK6OtYwqhiawymQnf4SicFPmzOdXDWQDWQicD82FLc4GjJ6QIB9nq9OTicPA3UfMGAT3fQ/640?wx_fmt=png&from=appmsg)

由于貔貅盘的本质具有一定隐蔽性，即便经验丰富的投资者也可能很难看清真相。如今 Meme 风盛行，各类型的“土狗币”对市场造成一定的影响。由于貔貅盘的价格会迅速上涨，人们常常冲动地跟风购买，许多未明真相的市场参与者苦苦追逐这波“土狗热”，却无意中步入貔貅盘的陷阱，购买后再也无法将其出售。

因此，MistTrack Team 建议广大用户进行交易前，采取以下措施来避免因参与貔貅盘导致资金受损：

* 使用 MistTrack 查看相关地址的风险情况，或通过 GoPlus 的 Token 安全检测工具识别貔貅币并进行交易决策；
* 在 Etherscan、BscScan 上检查代码是否经过了审计和验证，或阅读相关评论，因为有些受害者会在诈骗代币评论选项卡上发出警告；
* 了解相关的虚拟货币信息并考量项目方背景，提高自我防范意识。警惕提供超高回报的虚拟货币，超高的回报通常意味着更大的风险。

**写在最后**

如果您的加密货币不幸被盗，我们将免费提供案件评估的社区协助服务，仅需要您按照分类指引（资金被盗/遭遇诈骗/遭遇勒索）提交表单即可。同时，您提交的黑客地址也将同步至慢雾 InMist Lab 威胁情报合作网络进行风控。（注：中文表单提交至 https://aml.slowmist.com/cn/recovery-funds.html，英文表单提交至 https://aml.slowmist.com/recovery-funds.html）

慢雾(SlowMist) 在加密货币反洗钱领域深耕多年，形成了一套完整且高效的解决方案，涵盖了合规、调查与审计三个方面，积极助力构建加密货币健康生态环境，也为 Web3 行业、金融机构、监管单位以及合规部门提供专业服务。其中，MistTrack 是一个提供钱包地址分析、资金监控、追踪溯源的合规调查平台，目前已积累三亿多个地址标签，一千多个地址实体，50 万 + 威胁情报数据，9000 万 + 风险地址，这些都为确保数字资产的安全性、打击洗钱犯罪提供有力的保护。

**往期回顾**

[慢雾出品 | 2024 上半年区块链安全与反洗钱报告](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499923&idx=1&sn=e075b86887cefa622b8a8318be269d49&chksm=fddebe14caa937024e5926e5524ace12fd4413510f51c8d8bdab1b01db4f16239b2cf8735a73&scene=21#wechat_redirect)

[「区块链黑暗森林自救手册」阿拉伯文版正式发布](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499898&idx=1&sn=e69f4409d60a42166cdfabae8a778436&chksm=fddebefdcaa937eb36e93c2d5fc126c5c9be7d0650cf108710b858941ad8fdf68912cd2a5b19&scene=21#wechat_redirect)

[慢雾：UwU Lend 被黑分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499891&idx=1&sn=25f3885531c260de8c37ec6212fd5480&chksm=fddebef4caa937e2bcdcba85424fed82bfd9ba3165ab07cd2efc01d117712bdb0d9dc8b74bb1&scene=21#wechat_redirect)

[劈波斩浪，安全出“粽”。祝大家端午安康！](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499874&idx=1&sn=cd8c475477c3a3b0a56d70ddbd87481b&chksm=fddebee5caa937f33723b1440326e8c084341b4e96a48e2bebae8438daebcec18ebe69c22b23&scene=21#wechat_redirect)

[慢雾：Chrome 恶意扩展盗取百万美金解惑](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499862&idx=1&sn=b84bd2706da7a6cc4d6ef5c738bf88d3&chksm=fddebed1caa937c757bde772a0a7eb6448a4099f0f113e2af53eca2e17567042407863bf8a24&scene=21#wechat_redirect)

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