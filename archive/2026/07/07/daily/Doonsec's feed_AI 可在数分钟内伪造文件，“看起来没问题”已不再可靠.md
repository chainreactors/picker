---
title: AI 可在数分钟内伪造文件，“看起来没问题”已不再可靠
url: https://mp.weixin.qq.com/s/UswxFz40l-raOyo-cHP0qg
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:02:18.096804
---

# AI 可在数分钟内伪造文件，“看起来没问题”已不再可靠

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3md097pJ19liawc4X9DVHic9sxT3m62yFGKcibfv0tcuShqZYdooCjYPHkU6zUiclibLq3tfurAzI8kxEPdbDJriaT3Y79G9bbowcsQ/0?wx_fmt=jpeg)

# AI 可在数分钟内伪造文件，“看起来没问题”已不再可靠

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX03hO4KnqvZIS8icpVlYhxb5WuGCbw6hpx5rGOClcZLCqP8cpVLm5RNhHYKicOU8uIw5bawqiaic6ePHn8GoqH2Zf50zo1iabQZytVM/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3CswQhEcxqaZ7DC2Uy2bx1pg32nS9Qtjt8En1d8lNnxoKAc9Qia5pAPjF1Kfzicf1F2xnmralHLus3aBIoZr4UR33R9LqSdictHo/640?wx_fmt=png&from=appmsg)

Part01

生成式AI颠覆传统防伪手段

多年来，识别伪造文件主要依靠寻找破绽：错误的字体、模糊的标识或与声称日期不符的元数据。生成式AI彻底改变了这一局面——传统识别特征已失效，伪造者不再需要专业技能，任何拥有聊天机器人工具的人都能在几分钟内完成伪造。

数据显示这并非渐进趋势而是质的飞跃。Sumsub报告显示，2025年合成身份文件欺诈激增300%以上，北美地区较2024年第一季度增长311%，深度伪造欺诈尝试更是呈数量级增长。研究人员使用GPT-4o在五分钟内生成的合成护照，肉眼已无法与真实证件区分。目前超过10%的企业遭遇过深度伪造或AI生成文件的欺诈尝试，约5%的身份验证失败案例涉及深度伪造技术。

Part02

指数级增长的安全威胁

安全团队最应警惕的是增长曲线。身份欺诈分析师报告显示，AI生成的欺诈尝试年增长率达数百个百分点——iProov记录2024年数字注入攻击暴增783%，Jumio数据显示2025年又增长88%。这种增长并非线性，生成模型的每次迭代都降低了伪造成本并提升了质量，导致欺诈尝试持续激增而非趋于平稳。

德勤预估，到2027年生成式AI可能使美国相关欺诈损失从2023年的23亿美元飙升至400亿美元。四年三倍增长的背后并非欺诈者数量增加，而是个体作案效率的飞跃。当制作逼真伪造品的工具免费且快捷时，欺诈的限制因素已从技术门槛转为作案意图。

Part03

监管响应与验证范式转变

监管机构已开始量化风险：美国金融犯罪执法网络（FinCEN）2024年底就金融欺诈中的深度伪造媒体发布警报；FBI互联网犯罪投诉中心2025年记录超过2.2万起涉及AI的投诉，损失超8.93亿美元；仅2025年上半年，监管机构就开出超23亿美元与管控薄弱相关的罚单。"文件看起来没问题"的说辞已不能作为受监管机构的免责理由。

PDF签名验证正从视觉检查转向密码学验证。安全团队需要回答的不再是"文件能否正常打开显示验证标记"，而是"能否证明这是声称日期由指定方签署的原始文件"。可靠的验证意味着证据不能仅存在于发送方副本或单一供应商软件中，而需与签署事件本身绑定并支持多方独立验证。

Part04

溯源验证成为防御核心

当前反欺诈面临结构性困境：越来越多被识破的伪造文件使用主流生成工具制作，检测器始终基于历史伪造样本训练，而生成器每月都在升级。这是一场防御方永远落后的军备竞赛——当伪造品专为通过检测而设计时，更细致的检查也无济于事。

攻击方式已发生本质变化：攻击者无需修改现有文件留下痕迹，可直接生成包含目标内容的新文件并添加签名，或篡改已签署文件。元数据这个曾经的"铁证"现在最易伪造或剥离。每季度文件检查的有效性都在降低，唯有绑定原始签署事件的证据始终有效。

因此验证的关键节点应是入口而非事后。KYC流程、供应商准入、贷款申请和合同执行等文件从外部转入内部的环节，正是伪造文件造成破坏的突破口。在入口自动核查来源，可将验证从损失后的调查转变为损失前的闸门。

Part05

确定性验证的实践价值

以开户申请为例：自拍照片、身份证件和地址证明均可合成——深度伪造的面部、生成模型制作的证件、模板秒改的账单。每个伪造品都能通过目视检查，但攻击者无法伪造连接文件与合法签发方的完整监管链。这正是防御必须从判断文件本身转向验证其来源的原因。

溯源验证的优势在于确定性而非概率性：检测器给出的置信度会随伪造技术提升而降低，而可验证的签署记录只给出是与否的结论——无论伪造多么完美，重新生成的文件绝不会与原始签署文件的哈希值匹配。这种特性不会因模型迭代而失效，正是军备竞赛中所需的防御机制。

Part06

开放验证的实践必要性

选择支持多方独立验证的方案具有现实意义：局限于单一平台的验证仅适用于该平台用户，而银行核查客户文件、监管机构审查档案或交易方验证合同时，各方都需能独立确认。基于开放公共记录的溯源验证无需账户、许可或技术支持即可完成。在文件频繁跨机构流转的欺诈环境中，止步于企业边界的验证正是攻击者寻找的突破口。

新时代的安全标准不再是"检查是否仔细"，而是"能否不依赖提供方自证，随时由任何人验证文件完整性"。对于KYC、供应商准入和合同审核团队，当务之急是停止将呈现的签名视为证据。防御方的应对之策是在文件进入业务环节时（而非损失发生后），应用机器可验证且法庭认可的溯源机制。

在逼真伪造品唾手可得的时代，"看起来没问题"已不是有效控制。真正的控制力在于第三方能够不依赖任何人的说辞，独立证明文件在签署后未被篡改。值得注意的是，这对真实文件并非负担——合法签署的文件自带证明可即时通过验证，只有再生或篡改的文件会失败。在入口添加溯源验证不会拖慢诚实申请者或真实供应商的流程，也无需审核员练就识别超越人眼极限的伪造品的火眼金睛。

参考来源：

AI Can Forge Documents in Minutes – "Looks Right" Is No Longer Enough

https://hackread.com/ai-forge-documents-minutes-looks-right-not-enough/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0ctiaj5Z87Tg1RMJbr06lrE2fqlFoKFB0d4hx9AsKnZwJlVP4C7SBicZtVYotXf2IOL9UhETZBwFP2Q5D9A7vpdzWjR2M6r7abc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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