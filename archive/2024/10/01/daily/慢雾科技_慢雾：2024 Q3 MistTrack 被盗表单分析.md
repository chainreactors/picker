---
title: 慢雾：2024 Q3 MistTrack 被盗表单分析
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500472&idx=1&sn=b8af0c6be27c5f779a9886e166ef8287&chksm=fddebc3fcaa93529cd590f829d1219d5594f9662263493dcddda5733842ceb946a95d538dda6&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-10-01
fetch_date: 2025-10-06T18:53:08.463152
---

# 慢雾：2024 Q3 MistTrack 被盗表单分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8bEd1icicibXa8rG8tXbqQq8FicjMEqk7KatB1gOWXovjswicgG6sgzl88nw/0?wx_fmt=jpeg)

# 慢雾：2024 Q3 MistTrack 被盗表单分析

原创

慢雾 AML 团队

慢雾科技

慢雾 SlowMist 每天都会收到大量受害者的求助信息，希望我们提供资金追踪和挽救的帮助，其中不乏丢失上千万美金的大额受害者。基于此，本系列通过对每个季度收到的被盗表单进行统计和分析，旨在以脱敏后的真实案例剖析常见或罕见的作恶手法，帮助行业参与者从中学习并更好地保护自己的资产。

据统计，MistTrack Team 于 2024 年 Q3 季度共收到 313 份被盗表单，包括 228 份国内表单和 85 份海外表单，相对 Q2 季度有所减少，Q2 季度表单情况可查看[慢雾：2024 Q2 MistTrack 被盗表单分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499939&idx=1&sn=9a19ea41c058d225c6ccbb21736f8923&chksm=fddebe24caa93732fab9dc5b29801e718e4a72db379f53db6a5b0532d4f22e957f6221946f2f&scene=21#wechat_redirect)。我们为这些表单做了免费的评估社区服务（Ps. 本文内容仅针对来自表单提交的 Case，不包括通过邮箱或其他渠道联系的 Case。）

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8UeHtnibn6lBYwPGsGMCtf62EPE7qGxFhibXL75OxxK8mZ6hsCjwsKvTg/640?wx_fmt=jpeg&from=appmsg)

其中，MistTrack Team 协助 16 个被盗客户在 16 个平台冻结约 3,439 万美元的资金。

# **被盗原因 Top 3**

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8doibywicRKuwPWPQNfDO8gyP0xJx2bmEqP6Fn4bNH6GbxARMI4gnpvPQ/640?wx_fmt=jpeg&from=appmsg)

2024 年 Q3 最常见的作恶手法如下：

## **私钥泄露**

私钥泄露在 Q3 表单的被盗原因中占据高位。根据整理结果，主要分为以下几类：

### 1. 购买账号导致私钥泄露

拿具体案例来说，用户从不可信渠道购买如 WPS 会员、海外的 AppleID 等，然后将私钥/助记词记录在备忘录或文档上，而卖方通过修改账号密码并检测到私钥，使得用户资产面临被盗的风险。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8cicQqrKiaTFxAXt3hOkov7AUaNeibt1O0ArqdsHDKwvS4lQkQy1X1jExQ/640?wx_fmt=png&from=appmsg)

建议用户始终从知名或可信赖的平台购买账户，同时不要将重要的个人信息保存在可共享的平台上。

### 2. 私钥保存不当

私钥保存不当是私钥泄露最常见的原因，让我们看看 Q3 季度有哪些保存不当的方式：

* 私钥以照片形式保存在手机便签/备忘录/微信收藏
* 助记词以二维码形式保存在邮箱的草稿箱里
* 私钥保存在本地或云文档
* 私钥通过 xlsx、txt 保存
* 将助记词截图存在手机相册里并通过云端传输
* 记在纸上，被熟人偷拍

以上都是 Q3 季度提交表单的用户常用的私钥保存方式，这些看似提高了信息安全的行为实际上都极大地增加了风险，容易被黑客或恶意软件攻破，甚至被身边人惦记。曾有这样一个案例，受害者资金被盗后请求 MistTrack Team 协助，MistTrack Team 刚评估出追踪结果就发现资金已被转回到受害者的地址，后面得知是受害者的朋友一时起了贪念转走了资金，但始终惶恐不安，便在心理压力下返还了资金并向受害者坦白道歉。因此，请不要将你的私钥/助记词分享给任何人，并通过安全合理的方式进行保存，例如抄写在纸上，然后存放在一个安全的物理位置或者使用硬件钱包，如果必须使用电子存储手段，请确保文件已经过强加密，并存储在离线设备上。

### 3. 下载假 App

假钱包 App 导致的资产被盗案例已经是老生常谈，而这里的假 App 不只是指假钱包 App。

* 案例一：下载恶意 App

受害者下载骗子给的恶意 App，导致权限被修改，TRON 地址被多签。关于钱包被恶意多签的知识可阅读[Web3 安全入门避坑指南｜钱包被恶意多签风险](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500038&idx=1&sn=00ff98cee22c817942d2e1bce4f8db46&chksm=fddebf81caa93697ba13a1ad0f8eb3baab0c739926912e671c3ac4d81b18467feee1bffae095&scene=21#wechat_redirect)。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8iblFVrfXJMuhQ8XFo86Yov0r77gl7GeJbdn9AHWficJcw2ITJ8dlltKQ/640?wx_fmt=png&from=appmsg)

受害者下载了假的 Telegram，朋友发送的钱包收款地址被篡改为黑客的地址，导致转账到错误的地址。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8ViaZTB1AlzYiaQTjJ4sxciabFGD8ldXt07v0MN5iaUldCbRxdXQ3KSlXDA/640?wx_fmt=png&from=appmsg)

* 案例二：木马病毒

根据表单的情况，大部分受害者都是在骗子的诱导下，下载恶意应用程序中了木马病毒导致数据和权限被盗。

例如，骗子私信用户，以提供工作机会的名义让用户下载一款假冒 PartyChaos 的游戏，据我们了解，该骗局已被多名用户在 X 上披露：

官方：partychaos[.]fun

骗子：partychaos[.]space

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8Y13IwfgshyTMlyOPpCtKE22icj79btG52FO7aeylM6AicGH2NoxlWhCw/640?wx_fmt=png&from=appmsg)

其中一名受害者猜测这可能是有风险的程序就没有立刻下载，但后来不小心误触了，导致其所有资产的访问权限被盗取。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt85878lBdV93RyMDLgCJgVWyHmeBxtbQqfsicfHrBB3wFyicSuWIfFXxBQ/640?wx_fmt=png&from=appmsg)

还有受害者在 X 被诈骗，下载了带有病毒的 vbs 脚本导致被盗的案例：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt81q4IibggUCsc4onhiauCxu42bAH8oHfcODuiaYkamekoCibFicOZtekQdicQ/640?wx_fmt=png&from=appmsg)

更为常见的是骗子冒充 VC 或者记者，私信诱导受害者下载恶意的视频会议应用程序。例如，我们收到的表单中的一个案例是，骗子冒充 VC 或者记者私信受害者，并通过 Telegram 进行交流。接着，骗子诱导受害者在视频会议应用程序 WasperAI 上进行视频通话。由于受害者没有该应用，骗子发送了一个链接(wasper[.]app)，称是该应用的官方下载链接，实际上却是个钓鱼链接，从而窃取了受害者电脑的数据，包括私钥。

我们发现该钓鱼站点制作精美，并且还有对应的 GitHub 开源项目。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt83wxn9xf8qkVgLKRYtJxiap4ARIk5orz87cFho5YmFfpXw9GibQNyVcxg/640?wx_fmt=png&from=appmsg)

骗子为了让虚假项目更具备可信度，甚至还对开源项目的 Watch, Fork, Star 进行设计。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8sXjZckSuicSoKK0eY5qicGZMawwLqwG4ms5qHoibicdAWTlZibM1j2Ayd5w/640?wx_fmt=png&from=appmsg)

由于钓鱼网站，虚假项目，X 账号之间的信息相互呼应，这看起来就像是一个正常的项目，不仔细辨别很容易掉入陷阱。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8Tt0XuaIiaLJXH97dibASSkdm8HHxmM3uVRnuMXvqNeakicFnJGC1jUFkw/640?wx_fmt=png&from=appmsg)

我们发现这是一个有组织，操作行为批量化，具备专业技术且精通社会工程学的黑客团伙。有时他们会伪装成项目方，创建精美的项目官网、社交媒体账号、项目开源仓库，并且刷了 follower 数量，撰写项目白皮书，看起来和正常的项目高度相似，导致很多受害者认为这是真实的项目，因此被攻击。

慢雾 SlowMist 建议广大用户提高警惕，在点击网站链接前要保留一份怀疑；安装知名杀毒软件，如卡巴斯基、AVG 等提高设备安全性，如果不幸中招，请第一时间转移钱包资金，并对个人电脑进行全面的杀毒排查。

### 4. “主动”输入私钥

此类泄露方式主要是指受害者在放松警惕、不明所以的情况下自己输入私钥导致被盗，主要分为三类：

* 在绑定钱包机器人的时候，未仔细甄别，导致将私钥泄露给假冒的机器人。
* 参与项目时，骗子提供脚本，用户提供资金，骗子通过私钥直接盗走产出及收益。
* 用户在 Discord 和 X 询问问题，被假冒的官方人员私信，诱导访问钓鱼链接并输入私钥。

还是那句话，任何时候都不要泄露自己的私钥。遇到问题时，应直接通过官网提供的正规客服渠道寻求帮助，不要轻信第三方机器人或客服。

## **钓鱼**

根据分析，Q3 多起被盗求助事件的被钓鱼原因都是：点击了发布在知名项目推文下的钓鱼链接评论。此前，慢雾安全团队做了针对性的分析统计：约有 80% 的知名项目方在发布推文后，评论区的第一条留言会被诈骗钓鱼账号所占据。我们还发现还存在一些专门售卖 X 账号的网站，这些网站销售各年份的 X 账号，甚至支持购买高度相似的账号。由于与真实项目方的账号具有高度的相似性，使得许多用户难以分辨真假，从而进一步增加了钓鱼团伙的成功率。随后，钓鱼团伙实施钓鱼行动，比如使用自动化机器人来关注知名项目的动态。当项目方发布推文后，机器人会自动回复以抢占第一条评论，从而吸引更多浏览量。鉴于钓鱼团伙伪装过的账号与项目方账号极其相似，一旦用户疏忽，点击假账号上的钓鱼链接，然后进行授权、签名，便可能导致资产损失。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8SrOl6j3UrCj7ib7kVb9AROic0Lm8P4Fvo1b6rticzg8gmuw23Q9PYPPog/640?wx_fmt=png&from=appmsg)

其次，点击搜索引擎中的广告位的钓鱼网站导致被盗的案例也很多。例如，在Google 搜索 Rabby Wallet，从 Google 搜索关键字情况来看，排在前两位的搜索结果都为钓鱼广告，然而第一条广告的链接却很反常，它显示的是 Rabby Wallet 的官方网站地址。通过跟踪发现，钓鱼广告有时会跳转到真正官方地址 rabby.io，而在多次更换代理到不同地区后，则会跳转到钓鱼地址 rebby[.]io，并且该钓鱼地址会更新改变。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8pqiaKzVtrDm4wicuhiaia2vSRtXg72mK7mlDBGsGpNSjNzdqG0miazYCl0g/640?wx_fmt=png&from=appmsg)

总结来说，不要相信任何搜索结果显示出来的广告投放地址！建议用户安装钓鱼风险阻断插件 Scam Sniffer 来确保资产和信息安全，用户在打开可疑的钓鱼页面时，工具会及时弹出风险提示，同时建议大家深度阅读并逐步掌握《区块链黑暗森林自救手册》：https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/。

## **诈骗**

在 Q3 用户提交的表单中，因假矿池骗局而受损的用户数量显著增加。根据多位受害者的描述，骗子在 Telegram 上冒充知名交易所建立诈骗群组，这种诈骗群的组员动辄几千上万人，很容易让人放松警惕。不少用户在 Telegram 上搜索官方账号时会把群人数当作辨别账号真伪的因素之一。官方群的人数会比较多是没错，但是这个逻辑倒推回来就不一定对了。难以想象，骗子建立一个有上万人的群竟是为了骗几只“羊”，甚至里面的“闲聊”都是诱饵。值得注意的是，一个有五万多人的群，在线人数却不足一百人。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8pI974xubXI7BT0goQibUt0ficGc6Eskkr2gFDdAIIUHFN65G4H2SQ9eQ/640?wx_fmt=png&from=appmsg)

还有一种骗局是骗子先将用户引导至诈骗平台，并通过操控平台数据制造出用户“盈利”的假象。然而，这些盈利只存在于平台的显示上，并不代表实际的资产增加。在这一阶段，用户已经被骗子“高超”的投资能力所迷惑。接下来，骗子进一步邀请用户参与矿池活动，并规定用户每天需要向充币账户充值总资产的 5% 或 8% 的 USDT 以激活矿池。为了获得分红，并在“如果不继续充值就无法赎回本金”的压力下，用户不断向骗子提供的账户充值。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8Uia1G5dWJZVia2WiaSN5rEfUJJRklF4HjLUkO5qR0Q6lm8EmuDltvu2lw/640?wx_fmt=png&from=appmsg)

其次，场外 OTC 被骗的案例数也在增加。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbXGYdEWEyepRlypHDKgJt8cWctrNscaiaBLl42RzftzDIL8N0SQnRPHnBaPLY6N5xnPFvib30ZeySA/640?wx_fmt=png&from=appmsg)

# **写在最后**

如果您的加密货币不幸被盗，我们将免费提供案件评估的社区协助服务，仅需要您按照分类指引（资金被盗/遭遇诈骗/遭遇勒索）提交表单即可。同时，您提交的黑客地址也将同步至慢雾 InMist Lab 威胁情报合作网络进行风控。（注：中文表单提交至 https://aml.slowmist.com/cn/recovery-funds.html，英文表单提交至 https://aml.slowmist.com/recovery-funds.html）

慢雾(SlowMist) 在加密货币反洗钱领域深耕多年，形成了一套完整且高效的解决方案，涵盖了合规、调查与审计三个方面，积极助力构建加密货币健康生态环境，也为 Web3 行业、金融机构、监管单位以及合规部门提供专业服务。其中，MistTrack 是一个提供钱包地址分析、资金监控、追踪溯源的合规调查平台，目前已积累三亿多个地址标签，一千多个地址实体，50 万 + 威胁情报数据，9000 万 + 风险地址，这些都为确保数字资产的安全性、打击洗钱犯罪提供有力的保护。

作者 | Lisa

编辑 | Liz

**往期回顾**

[慢雾：Uniswap v3 协议分析与审计要点](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500440&idx=1&sn=e447aeff528fb5a5c96a3d88f2d31531&chksm=fddebc1fcaa9350964866990b32e3a928e3a6b76a9c39eabe7e8755c4bb47a03a15e48da678a&scene=21#wechat_redirect)

[慢雾：Sui - Move 合约审计入门](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500411&idx=1&sn=a9bd3a971824eb5bdb342a54e6da1782&chksm=fddebcfccaa935ea03d21c459875d19309c50a4822337c62f7285e0c9136698c750ee2584eb2&scene=21#wechat_redirect)

[报告解读｜FBI 发布 2023 年加密货币欺诈报告](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500371&idx=1&sn=0ca64fc5fb738f708f356eb36d0a2552&chksm=fddebcd4caa935c2e13981ab96...