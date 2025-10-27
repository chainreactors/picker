---
title: 慢雾：2024 Q4 MistTrack 被盗表单分析
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500805&idx=2&sn=be253330d0da176f82c8c2db7821ea12&chksm=fddeba82caa933941c30351bfa9a34776e0c8413939a57714795dedb6661c8ba9973f1309914&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-01-04
fetch_date: 2025-10-06T20:11:07.621730
---

# 慢雾：2024 Q4 MistTrack 被盗表单分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1rJ1O4FlzKOF61d3eyadoncf71b2o7EufwZlexugt2ejJQ7QBbja4W6A/0?wx_fmt=jpeg)

# 慢雾：2024 Q4 MistTrack 被盗表单分析

原创

慢雾 AML 团队

慢雾科技

自慢雾(SlowMist) 上线 MistTrack 被盗表单提交功能以来，我们每天都会收到大量受害者的求助信息，希望我们提供资金追踪和挽救的帮助，其中不乏丢失上千万美金的大额受害者。基于此，本系列通过对每个季度收到的被盗表单进行统计和分析，旨在以脱敏后的真实案例剖析常见或罕见的作恶手法，帮助行业参与者从中学习并更好地保护自己的资产。

据统计，MistTrack Team 于 2024 年 Q4 季度共收到 2,077 份被盗表单，包括 335 份国内表单和 151 份海外表单，其中 1,591 份表单来自 DEXX 事件，我们为这些表单做了免费的评估社区服务。（Ps. 本文内容仅针对来自表单提交的 Case，不包括通过邮箱或其他渠道联系的 Case）

本季度，MistTrack Team 协助 25 个被盗客户在 18 个平台冻结约 5,352.12 万美元的资金。

#

# **被盗原因**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1r3pqooSLxWy3W8iag82BTT27R0R2w5LyU1PRzGOkR1rHMmMaJ4F2Dozw/640?wx_fmt=png&from=appmsg)

2024 年 Q4 的作恶手法中，诈骗成为被盗原因 Top1。除了老生常谈的手法，Q4 还出现了一些新的骗局手法，我们一起来看下。

### **1. 恶意交易机器人**

多位用户报告在使用交易机器人时，频道顶部出现了一个新的机器人，以为是官方新推出的，于是点进新机器人导入私钥绑定钱包，结果被盗。仔细一看，这个机器人前面有个 Ad（advertisement）字眼，这是 Telegram 自带的广告提示，由于这个广告出现在官方频道，用户很容易下意识认为是官方发布的机器人，请大家仔细甄别。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1rVkiaHA4wP5T5Q520Dq7sRHLaGHYe58lWn1QsFvhb3RVxhrYUGPardjg/640?wx_fmt=png&from=appmsg)

有的用户在电报里搜索知名度较高的交易机器人，在搜索结果中选择了排在最前面的机器人（恶意），然后将私钥粘贴至机器人，结果钱包里的资产在 1 分钟左右被盗走。我们建议用户在使用交易机器人时，如果遇到需要直接输入私钥的情况，多一份怀疑，选择信誉良好的交易机器人，定期检查交易机器人平台的安全性，确保使用的是最新版本，同时增强私钥管理的能力。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1rMYpL3pWtDsLoBxXicjiaUq4yeVGIYLdI6cCbHLpfvQxmSn2Ev9ROq1Ow/640?wx_fmt=png&from=appmsg)

### **2. 质押返利**

2024 年，用户依然面临着假冒官方群组进行质押返利的骗局。质押返利是一个非常经典的诈骗手法，通常以“官方返利活动”的名义，声称只要参与质押就能获得高额回报。诱人的回报率吸引了不少用户加入，但实际上这些“官方”并非真实的项目方。用户往合约地址打款后，收到了返利，便想投入更多的资金以获得更多的收益，此举正中骗子的圈套，最后用户投入的资金都被骗子卷走。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1rAYv8Wp9PasiaqQicRNLM0etMqQANibLFFohOfuGL4lIibZZzrAPribjNE3Q/640?wx_fmt=png&from=appmsg)

更可恶的是，还有些骗子在给用户返利时，返回的甚至是假币，不明所以的新用户以为真的收到了返利，直到尝试交易返利的币时才发现这是假币，毫无价值。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1rCb7TvHFBnZ9hRjUrPibLrwOLub0x53aOrpwEoybG2v0GqqVL2dVKcsA/640?wx_fmt=png&from=appmsg)

用户应特别小心，避免盲目相信“高收益”诱惑，始终通过官方渠道确认项目信息。

### **3. 会议木马**

近期，伪装成 Zoom 会议链接的钓鱼攻击频发。攻击者使用形如官方的域名伪装成正常 Zoom 会议链接，页面与官方 Zoom 会议高度相似，攻击者会伪装成投资人、知名记者等向潜在受害者发起聊天并提供恶意链接，诱使用户点击。当用户点击“启动会议”按钮，便会触发下载恶意安装包，受害者的设备会被感染恶意软件，攻击者能够远程控制设备、窃取敏感信息，甚至盗取加密货币钱包中的资产，详情见[眼见不为实｜假 Zoom 会议钓鱼分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500726&idx=1&sn=6910bca0976da7f6078662bd95f0bc68&scene=21#wechat_redirect)。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1r62tUianarWgicNiamuH7OAoWot1hsRMytrAeqmkPvTUMNS5c7U5MIbGQg/640?wx_fmt=png&from=appmsg)

建议广大用户提高警惕，在点击网站链接前要保留一份怀疑；安装知名杀毒软件，如卡巴斯基、AVG 等提高设备安全性，如果不幸中招，请第一时间转移钱包资金，并对个人电脑进行全面的杀毒排查。

### **4. 貔貅币**

根据表单的统计，一种常见的情况是用户被骗子的花言巧语所诱惑，继而投资了貔貅盘。具体来说，攻击者创建一个完全没有实际应用场景的代币（如貔貅币），并通过夸大其未来潜力吸引投资者。投资者被诱导在未经审查的交易平台或钱包中购买这种币种。一旦投资者购买了这些“貔貅币”，骗子会将资金直接转移至自己的钱包地址，由于貔貅币本身没有实际的市场流通，投资者无法出售或者兑换。在一些情况下，骗子会通过庞氏骗局的方式，使用新投资者的资金来支付给早期投资者，制造币种上涨的假象，从而吸引更多的投资。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1rE4DY1EH8X4d9RXqtPHDvQLVUsEP4AIF4CEKoBRDYdrazYxvFGW5QUQ/640?wx_fmt=png&from=appmsg)

建议用户在参与投资前使用 Token 检测工具如 Goplus 对相关代币进行核查，最好查阅相关项目的白皮书、团队背景等信息，避免投资任何未经充分验证的 ICO 或新兴币种。

### **5. 在小红书上受骗**

近期，MistTrack Team 注意到有些用户是在小红书上遭遇的诈骗，且损失金额较大，达上百万美元。我们在小红书上搜索“加密货币”、“比特币”、“交易所”等关键词，可以看到许多用户在上面分享自己盈利/亏损的情况，比如“一天翻了 X 倍”、“勇闯币圈”、“百 U 战神”等帖子，评论区里有不少用户“求带”，在骗子眼里，这就是一大片“鱼塘”。骗子在评论区钓鱼，自称提供交易所安装服务，接下来的套路相信大家可以猜到了，用户进入 Web3 的第一步便中了骗子的圈套，下载了假的交易所，资金受损。有的骗子冒充所谓的“行业专家”或“投资达人”，向用户展示虚假的投资成功案例，建立“可信度”。接着私信向用户发送所谓的加密货币投资机会，声称有内部消息可以带领用户“稳赚不赔”，同时将沟通渠道转移到其他平台，继续行骗。请广大用户提高警惕，不要轻信他人，避免出现你想赚利息，而对方盯上本金的情况。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1r7dEZN3xZ31N1bBaOEIykjtBA8R4SMDpTzGvaIzHSGRV81QHelBdU9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYgcj5NFAz17icNLhibJjVr1rHmuDJjt99AJcD77P3YBgYBUp67jKQRTCQibgaGfVMGbtDIKJVJFm0mQ/640?wx_fmt=png&from=appmsg)

# **写在最后**

如果您的加密货币不幸被盗，我们将免费提供案件评估的社区协助服务，仅需要您按照分类指引（资金被盗/遭遇诈骗/遭遇勒索）提交表单即可。同时，您提交的黑客地址也将同步至慢雾 InMist Lab 威胁情报合作网络进行风控。（注：中文表单提交至 https://aml.slowmist.com/cn/recovery-funds.html，英文表单提交至 https://aml.slowmist.com/recovery-funds.html）

慢雾(SlowMist) 在加密货币反洗钱领域深耕多年，形成了一套完整且高效的解决方案，涵盖了合规、调查与审计三个方面，积极助力构建加密货币健康生态环境，也为 Web3 行业、金融机构、监管单位以及合规部门提供专业服务。其中，MistTrack 是一个提供钱包地址分析、资金监控、追踪溯源的合规调查平台，目前已积累三亿多个地址标签，一千多个地址实体，50 万 + 威胁情报数据，9000 万 + 风险地址，这些都为确保数字资产的安全性、打击洗钱犯罪提供有力的保护。

**往期回顾：**

[慢雾：2024 Q3 MistTrack 被盗表单分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500472&idx=1&sn=b8af0c6be27c5f779a9886e166ef8287&scene=21#wechat_redirect)

[慢雾：2024 Q2 MistTrack 被盗表单分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499939&idx=1&sn=9a19ea41c058d225c6ccbb21736f8923&scene=21#wechat_redirect)

作者 | Lisa

编辑 | Liz

**往期回顾**

[慢雾(SlowMist) 荣获 ISO/IEC 27001:2022 信息安全管理体系认证证书](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500738&idx=1&sn=f6b41633e284c83cefc943cbed001870&scene=21#wechat_redirect)

[眼见不为实｜假 Zoom 会议钓鱼分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500726&idx=1&sn=6910bca0976da7f6078662bd95f0bc68&scene=21#wechat_redirect)

[慢雾科技通过厦门市 2024 年专精特新中小企业认定](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500689&idx=1&sn=4edcb09fb8b3f3c92edad1d7a6edcb05&scene=21#wechat_redirect)

[Keyblock Solutions 宣布与 MistTrack 达成战略合作](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500674&idx=1&sn=ae109f56fa8b688eebce6f48366d1a3f&scene=21#wechat_redirect)

[每月动态 | Web3 安全事件总损失约 8,624 万美元](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500662&idx=1&sn=7ae9f27e00bd9f6751cdc900e42566c9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaa3Th7YiamUUBwq1Iiby9N9lWh3tKP2MVjM6L3UxtTnuUy6iaegsOP2IrqZYsIBM2v3XgC5O2JTbY5g/640?wx_fmt=png&from=appmsg)

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