---
title: 黑产交易风险监测模块：从复杂无序的黑产交易市场中快速定位业务风险
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498232&idx=1&sn=c8730bb42a2c4f02462eb4e6a19e8271&chksm=eb12dfc3dc6556d5d18702da1a6e2a744051b275e65465b24d892c5fd27e46deb45efb766a24&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2024-11-08
fetch_date: 2025-10-06T19:20:36.427237
---

# 黑产交易风险监测模块：从复杂无序的黑产交易市场中快速定位业务风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibjYjqo0KRxu3TY34DXxmu9TLr0Rxsz6N3sjGSx4aI2Rowavo4rqMslw/0?wx_fmt=jpeg)

# 黑产交易风险监测模块：从复杂无序的黑产交易市场中快速定位业务风险

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif)

**黑灰产业链能够持续不断地高效运作****离不开上游资源交易和下游套利变现**，上游黑产通过特定渠道**采购账号、工具、手机号等攻击资源**，下游黑产通过各种渠道将攻击所得的**优惠券、现金券、会员权益、实体商品等进行变现**。

对企业而言，如果能及时获取到黑产的交易信息，如**企业自身有哪些数据及营销资产正在被交易、黑产交易趋势有哪些新变化、自身资产或业务在黑产交易中的价格情况**等等，基于这些情报信息及时发现业务攻击风险并快速调整防御策略。

如，电商企业在**大促期间**可通过**实时监测低价代购和优惠券交易情况**，通过交易量级或价格等异常波动发现业务可能存在的风险，及时调整风控策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibViadxkOXTiac2eAiaE6mv49KeLhlRQXDuiaJjU8mW88iaK5Z5eoSic3COmFg/640?wx_fmt=jpeg&from=appmsg)

对此，威胁猎人业务风险情报平台在2024年7月上线了业内首个**“黑产交易风险监测模块”**，基于对黑灰产上中下游的持续监测，利用大语言模型技术，对黑灰产交易的复杂商品信息进行结构化数据提取和分类归一：

一方面**可****对****黑灰产交易的商品类型及分布量级、商品详情信息、商品交易趋势等进行分类展示；**另一方面将复杂的商品信息归类**聚焦到企业业务场景**，为企业业务构建一个“**黑灰产交易风险全景图**”，全面、及时地感知黑灰产攻击风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibVM2NEhRAku9ICtObQSNGZSxfP6d9GukpU9XwR6nyv8XVwAs58auIVA/640?wx_fmt=png&from=appmsg)

截至目前，威胁猎人“黑产交易风险监测模块”监测的**黑灰产交易平台有534个，覆盖928万商品，日均新增捕获黑产商品数量超10万个**。

***1.*****黑灰产交易商品涉及实物商品、教程工具、会员权益、代下单服务、优惠券等类型**

威胁猎人发现，黑灰产交易的商品**涉及实物商品、教程工具、会员权益、代下单服务、优惠券、账号、刷量服务等**，截至目前，实物商品类数量最多，占比26.09%，以营销活动获取的实物奖励为主，其次是教程工具类和会员权益类。

进一步分析发现，**教程工具类商品**主要包括各种应用辅助脚本，例如挂机脚本、自动抢单工具等，这类商品可为用户**提供违反平台公平参与规则的作弊手段**，吸引了一大波想要快速获利的风险用户；

**会员权益类商品**则涵盖了视听软件的代充值、会员账号共享等，这些权益获取来源并不透明，存在批量薅取官方权益的情况以及低价回收分润，**一些用户通过这些服务可以低于官方价格享受会员权益**，扰乱了平台正常的用户生态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibIEbpRUunUOWVnrXRKtf1E8icuTiaOhVkhnUYXIhoZicaB6UNqoicc1tUzQ/640?wx_fmt=png&from=appmsg)

***2.*****上百种攻击教程及工具，包含脚本工具、游戏辅助、抢单工具、挂机教程等**

相比实物商品交易，**针对业务的精准攻击教程或工具等商品交易风险更大、范围更广**，这些服务通过技术手段吸引更多用户绕过规则以获取非法利益，给企业造成巨大的损失。如，脚本工具可以实现自动化任务，帮助一些违规用户完成自动化操作，在秒杀、热门票务销售等活动中抢占更多资源。

**企业若能获取到有多少黑灰产正在售卖针对企业资产的攻击教程或工具、交易价格趋势等，可快速调整风控策略，避免进一步的攻击风险。**

威胁猎人情报运营人员针对教程工具类商品进一步分析，**脚本工具数量最多，其次是游戏辅助类工具**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibdAyHyWXhZvkibhzbIOvGxSKXlUw258icMcw0MFY4dBU2I7D5wiaPMO7Jg/640?wx_fmt=png&from=appmsg)

***3.*****现成账号、低价会员、优惠券、代金券等直接权益及服务的市场需求旺盛**

威胁猎人情报运营人员针对账号售卖类的商品进一步分析，黑灰产售卖的账号商品包含游戏账号、社交媒体账号、通信娱乐账号为主等。

游戏账号通常包含了虚拟货币、装备和其他有价值的游戏内物品，对于购买者而言，通过非官方渠道打折购买高等级、好装备的游戏账号性价比更好；

**社交媒体账号通常被黑灰产用于引流、传播虚假信息**；通信娱乐账号主要指没流涕视频服务、音乐平台、在线书籍和漫画等平台的会员账号，**用户还可以低价的“共享”方式享受会员服务**。

在会员权益类、优惠券类等商品中，**会员账号、VIP会员、超级会员、优惠券、代金券、无条件减免、红包等直接权益大受欢迎**。这些会员账号或VIP权益通常以共享或租赁的形式出售，为一些用户提供了低门槛的内容访问渠道，而优惠券、代金券等福利原本是平台为了拉客、促活等目的给特定用户的福利，却给**黑产薅了羊毛**，**不仅达不到原先的营销目的，还给平台造成巨大的经济损失**。

**通过“黑产交易风险监测模块”快速定位风险业务，及时调整风控策略**

面对种种业务欺诈风险挑战，威胁猎人“**黑产交易风险监测模块**”自上线以来陆续帮助电商、短视频、出行服务、社交、在线票务等行业客户在错乱复杂的黑灰产交易市场中，**及时定位被攻击的业务资产、黑产攻击成本监测、识别企业自身未知却被黑产利用的业务漏洞等等**。

**应用场景一**

**关注黑产交易商品动态，快速定位核心业务风险**

企业可根据平台捕获及呈现的黑产交易商品量级和增长趋势，并根据商品描述**快速定位到相关业务场景**；此外，可通过对新增商品类型的持续观察，如近期黑产交易市场有新增哪些商品类型或具体商品，再关联到自身业务场景，**提前判断潜在的风险趋势，有效调整风控策略**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibuG70ufibGdibvict6kQ2ekoufsEKTKMia2NeaYpI8bxlRpfeq8KGrfM51g/640?wx_fmt=png&from=appmsg)

如，**电商企业**在**大促期间**可通过**实时监测低价代购和优惠券交易情况**，通过交易量级或价格等异常波动发现业务可能存在的风险，及时调整风控策略。

**应用场景二**

**洞察指定商品交易趋势**

**快速识别新的攻击方式或业务漏洞**

通过持续观测黑产交易商品数量波动情况，识别新的攻击方式或与自身业务相关的漏洞。

如，某商品的**交易数量或者价格短时间内出现较大的下降**，企业需要引起重视，关联业务是否出现了**新的业务漏洞**，或者黑产针对该业务攻击开发了**新的自动化工具**？

企业可以根据商品描述等相关信息以及威胁猎人其他情报数据，快速定位风险并及时调整风控策略，避免更大的损失。

**应用场景三**

**攻击成本及收益监测，实时评估自身风控效果**

在“黑产交易风险监测模块”可看到每个商品的价格，通过对商品价格的持续监测和统计分析，了解黑产针对相关业务的攻击成本及收益情况，**一方面能对判断潜在攻击风险，另一方面可评估自身风控效果**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibgIKyoIwoxgxVGTysUuLZs3VdCHFBKOwGb5U0vJOo6aPkazd9Breurw/640?wx_fmt=png&from=appmsg)

如，企业可观察市面上的代理服务价格价格有较大下降，企业需要引起重视，可能会出现新一轮的攻击风险，同时也要复盘自身的风控是否有做不到位的地方。

了解您的业务资产是否正在被交易

有哪些数据或营销资产正在被交易

**欢迎扫码咨询**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFG0eNBwBQgVutgHMGIG9Vib35yLgOzLu4yLjEaDFMDjKzEHeJu5rWWibEPA9XVuiaLjjc7lG0a05EjQ/640?wx_fmt=png&from=appmsg)

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibUzVdibpibjrEwniaWZ604NSf4TyIFDfREylrOM6DMu1wFdroE8v3qaZ2g/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498207&idx=1&sn=995239022e4341f0172fdebe3906d768&chksm=eb12dfe4dc6556f28a945fdd01dee4d3b4d513321256ab379499055f63c481da3443e5ab5396&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqFG0eNBwBQgVutgHMGIG9VibE9yiamC2jt1WG5lNLPqadSPB3BKIIia0A5t0d11m2MO1dUbylJFOFVTQ/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498178&idx=1&sn=cea1e2823de9287b8abf9112aa7e373e&chksm=eb12dff9dc6556efdca100fbc186e08f9b803504596bbc9908bc254b1512d9e0ba6350d63136&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqEsfSYoHcZjWvPtUIYg21stiayCHxKZ34vjvwSOZIRjicpKaWG5oG4e2Dh7JAWiaBgKgOv8FTVzLXq1A/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498201&idx=1&sn=f309cbe307dc9bb5cf02c4b672873bd7&chksm=eb12dfe2dc6556f489e7e3e3f5478907728bad46bbc343ba3c7805d7708fe528953aa868b591&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

威胁猎人Threat Hunter

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

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