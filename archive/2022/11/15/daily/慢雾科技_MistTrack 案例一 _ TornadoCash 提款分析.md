---
title: MistTrack 案例一 | TornadoCash 提款分析
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496723&idx=1&sn=0ea66570db1fd0c09694506287a46bcf&chksm=fdde8a94caa9038271a690faa41c1f941083f8f5a671fa33df373bc201cfa2066ad61367dcce&scene=58&subscene=0#rd
source: 慢雾科技
date: 2022-11-15
fetch_date: 2025-10-03T22:46:06.700761
---

# MistTrack 案例一 | TornadoCash 提款分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYsxibg30mjEPYPgcKPYfIIeVhhFzkRSC2xJdAzwnOUKbdtHaNiciceZ5cZLMU2LM4z0BOVg44lkjfWQ/0?wx_fmt=jpeg)

# MistTrack 案例一 | TornadoCash 提款分析

原创

慢雾 AML 团队

慢雾科技

By: Zero

本系列为 MistTrack 追踪分析案例分享。

**概览**

某项目被黑，被盗资金被黑客全部转移到 TornadoCash，项目方找到 MistTrack (https://misttrack.io/) 进行协助。MistTrack 针对 TornadoCash 做提款分析，协助项目方重新捕获被 TornadoCash 混淆后的被盗资金。几天后，等待黑客开始将资金转移到某交易所后，MistTrack 在建议项目方联系执法机构的同时，向黑客 TornadoCash 提款地址发送链上消息。最终在项目方发送链上消息 9 小时后，黑客将大部分被盗资金退还到项目方地址。

MistTrack 主要通过以下步骤起到关键性推进作用：

1. 和项目方相互的信任感；

2. 被盗资金追踪；

3. 黑客痕迹分析；

4. TornadoCash 提款分析；

5. 被盗资金监控；

6. 与黑客展开链上沟通博弈；

7. 必要情况下执法机构的介入支持。

下文将对案例一的 MistTrack 分析过程做详细阐述。

**被盗资金追踪**

收到项目方的协助请求后，MistTrack 立即开展了调查分析工作 。

在被盗资金追踪过程中，我们得出结论：被盗资金全部转入 Tornado.Cash。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYsxibg30mjEPYPgcKPYfIIeBBSKE7tOicgZjse2HL7TiaEr6yrHFxY4o78WchUSDtAXHtzlk1M0S6pQ/640?wx_fmt=png)

**被盗资金追踪**

接着，MistTrack 按照调查工作流，对黑客地址进一步开展分析。

* 手续费溯源
* 使用工具
* 黑客操作时间线
* 黑客画像
* 攻击前痕迹
* ...

黑客手续费来源是 TornadoCash，这里也可以向上进行溯源分析，在此处不做进一步展开。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYsxibg30mjEPYPgcKPYfIIeXwVQSLuLJungibiaicLiatlNiagvOvicTqetbcOURwcAr49WGibvbkvC75StQ/640?wx_fmt=png)

在资金兑换、跨链和洗钱的过程中，黑客使用到多种工具，例如 xxSwap 等，这将给后续 TornadoCash 提款分析埋下伏笔。

**TornadoCash 提款分析**

根据上述初步情况，MistTrack 评估案例一的突破点在 TornadoCash 提款部分，于是就此点展开深入分析。

下图是提款分析过程中使用的工具 (https://dune.com/awesome/Tornado-withdraw-analysis)，用于过滤符合筛选特征的 TornadoCash 提款地址。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYsxibg30mjEPYPgcKPYfIIeibU8aicGxFcW8lWlmia7YPEict6xINic2QmMuMEuXWn3sybOicmZOjRsicuWA/640?wx_fmt=png)

获取到提款地址列表后，通过以下指标对提款地址进行分类：

* 发送存款/取款当天的时间
* Gas 价格分布
* 与相同的服务进行交互
* 提款地址行为
* 提款数额分布

在其中一个提款地址分类中，我们发现了它命中了以下特征：

* 同样使用了上文的 xxSwap
* 与黑客地址的常用操作时间重合
* 与黑客存款到 TornadoCash 的数量一致

更为重要的是，其中一个提款地址还发现了与原黑客地址相关联的痕迹。于是我们便分析出了 TornadoCash 提款地址列表。

**被盗资金监控**

MistTrack 分析出黑客的 TornadoCash 提款地址列表后立即同步给了项目方，并使用 MistTrack 监控模块对 TornadoCash 提款地址进行监控。项目方对 MistTrack 的推进成果表示出极大的认可。

**链上沟通博弈**

在监控后的几天后，MistTrack 和项目方都收到了黑客经过多层转移后转移到某交易所的邮件。MistTrack 迅速与项目方进行语音会议探讨方案。在语音会议上，MistTrack 建议项目方积极的联系执法机构获取相关支持，并引导项目方向转移到交易所的黑客地址发送链上消息：“呼吁黑客在 48 小时内退款，并保留部分资金作为漏洞赏金，否则将继续推进调查并寻求执法帮助”。MistTrack 在积极筹备跟进执法流程的同时，也继续监控着黑客地址的异动。

**结果**

最终在项目方发送链上消息 9 小时后，黑客将大部分被盗资金退还到项目方地址。

**往期回顾**

[慢雾严正声明](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496710&idx=1&sn=8251b764cd551cddbb5c9cc2b5584d0b&chksm=fdde8a81caa90397596db950faf203404d792b594aa3824dac23cc2f08756b2cf04e50b610b2&scene=21#wechat_redirect)

[李逵还是李鬼？假币安 APP 钓鱼分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496694&idx=1&sn=e78bdca342520910385e1a04a7f5f084&chksm=fdde8d71caa9046722f7bc4e383db9a84963ccb418869816fb9502f7702555583dd7a1017006&scene=21#wechat_redirect)

[慢雾：pGALA 事件根本原因系私钥明文在 GitHub 泄露](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496669&idx=1&sn=afc4ca790ea79c62f09d21b1aafaa3cc&chksm=fdde8d5acaa9044c346e1e72aaca4c73db33a83b6a2b982c207a8778187a418cc0bf02db73b1&scene=21#wechat_redirect)

[慢雾：警惕相同尾号空投骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496658&idx=1&sn=86b93a4b30854c5002e04007f4531fc0&chksm=fdde8d55caa90443fd0353f54991a26fa7fceb03dbc4a8268cd09e311322018bb1314aef7081&scene=21#wechat_redirect)

[复盘 | Team Finance 被黑简要分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496624&idx=1&sn=9f7d0180bbfe3c017c4f279b3b25b3e4&chksm=fdde8d37caa904210d1f49e720c9193405aff8176b4b2ab2d3bdd898d89881b7b317ae8aa6c8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZicqJ95dics4nWpHGjsRUpeSdzvpiaECO7GGibicwsEdGNhIyh558P1ibickrNer98kLGRe1ezNiceGzKFcw/640?wx_fmt=png)

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

阅读原文

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