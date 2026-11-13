---
title: 为什么拦截率达到90%，黑产攻击仍然不会停止？
url: https://mp.weixin.qq.com/s/VJPbTGuMwhpQyWA7t6KlbA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:00:42.487998
---

# 为什么拦截率达到90%，黑产攻击仍然不会停止？

# 为什么拦截率达到90%，黑产攻击仍然不会停止？

原创

极验
极验

极验

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/8VOiack4f29dIwUZyFYpjZn2acm1AYKiczUk7R9j0L9sc0c5KVCzNo0X20mZSYTFn2S2yxwae4dLJydLqpnQZFAw/640?wx_fmt=gif)

**导语**

一个平台拦截了90%的异常请求，剩下的10%还会不会继续造成风险？

答案是会，过去一年里，从游戏账号工厂、广告分成刷量，到音乐版税欺诈、预售盗刷和设备外挂，黑产不断换场景、换工具和换账号。表面上看，攻击对象各不相同；放到收益模型里观察，它们都有同一个目标：用尽可能低的成本，制造能够进入平台业务结果的成功事件，以此来获得收益

平台统计的是拦截了多少异常请求、封禁了多少风险账号，避免了多少损失；黑产计算的却是最后赚到多少。

拦截率描述了防守过程，但黑产不会因为拦截成功就停止攻击。

只要漏网的 1% 收益能覆盖全部成本，攻击就不会停。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VOiack4f29cjg1STTg9bWovzGduMwouTa4lYN9LTwqB2a50W4mX9ibrf9EkjHFHyO0w9NmTRGgLgTdyTTCfATicg/640?wx_fmt=png&from=appmsg)

# 剩下的10%，为什么仍然值得投入？

假设平台遭遇100万次异常请求，其中90万次被拦截。

从技术报表看，90%的拦截率已经相当可观。在验证码这一环节的拦截率，参照物是进入验证环节的异常请求，而非整个业务链路的风险请求，更不是最终造成的实际损失。

剩余10%通过验证，只意味着它们跨过了这一道验证，并不代表都能完成注册、领券、下单、接口调用或结算。其中一部分仍可能在后续业务风控中被拦截，另一部分即使完成了业务动作，也未必能够最终变现。

这正是验证码的边界：**验证码主要判断当前这次验证交互是人还是机器，不能独立判断账号是否属于批量注册、设备是否被异常复用、操作是否符合活动规则，更不能替平台作出最终的业务和结算决策。所以它不能独立判断在正常设备和环境中，作为人交互的异常。验证通过，不等于业务风险已经消失。**

验证码被突破之后，平台仍有止损机会：

第一道在业务结果发生前，结合账号、设备、行为特征和业务规则，对注册、领券、下单、接口响应等环节继续拦截或二次验证；

第二道在结算变现前，通过订单审核、权益冻结、延迟结算和对账核查，阻止异常收益落地，避免风险进一步转化为实际损失。

如果上述节点未能完成拦截，异常权益已经核销、资金已经结算或提现，或者敏感数据已经返回，损失就已经发生。此时平台只能通过追偿、冻结关联资源、停止后续访问等方式控制进一步损失，难以保证完全挽回。因此，后续处置不能替代前端防护和业务流程中的及时拦截。

![](https://mmbiz.qpic.cn/mmbiz_png/e9GhxSDPqRhkcu3z0lliaxm9DdmkemnUbpXSSniavUicWajdLMicATUtA3POOVTkZOSk6mFlMrdHOmok7YV2X2icrdJzMbDGEOCIMsflCWaYGfIs/640?wx_fmt=png&from=appmsg)

而对于黑产来说，并不要求每一次请求成功，只会关注：

> 成功请求产生的可变现收益，能否覆盖算力、模型、数据、设备、协同、变现成本。

所以，黑产真正计算的不是“有多少请求通过了验证码”，而是其中有多少最终完成目标并成功变现。如果后续业务风控和结算审核能够持续提升黑产对抗成本，10%的验证通过率未必足以覆盖攻击成本；反之，只要优惠券、订单或结算收益仍能持续落地，并足以覆盖攻击成本，对黑产而言，仍有足够“吸引力”

只要成功事件能够低成本复制，有限收益就可以被账号和订单数量持续放大。

所以，90%的拦截率不天然等于风险下降90%。平台还需要继续追问：剩余成功请求转化成了多少有效账号、订单和权益？这些业务结果是否仍然可能给黑产带来持续的正收益？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VOiack4f29cjg1STTg9bWovzGduMwouTibPad0noFibJpF8luQhibJwhib8pJzosW1zVKaEhTUFAhA21hMglVkUh7g/640?wx_fmt=png&from=appmsg)

# 黑产为什么不怕封号？

> 攻击者是理性的经济参与者，只有收益超过成本时，才会投资基础设施、工具和人力。他们的创新，是对那些压低利润的防御措施作出的回应。他们改变策略，不是为了智力挑战，而是为了恢复盈利。

如果只看单次请求，拦截意味着失败；但把观察周期拉长，封号、限IP和验证拦截，有时只是黑产的一次资源消耗。

四川南充一个团伙曾租借7000余个手机号，注册6000余个平台账号，其中5000余个账号成功兑换活动物资。**对这类账号池模式而言，部分账号失效并不影响整体运转，只要补号成本足够低，新的账号就会继续进入业务流程。**

**封禁减少的是存量账号，而下一批存量账号正在以低供给成本补位。**

进一步来说，在一个客户或者业务场景中不能使用的账号，也不会就此作废，由此进入跨平台复用，它们还可能被转用于其他平台、其他活动，或者继续作为账号池中的储备资源。对黑产来说，单个账号更像可以替换的消耗品，而不是必须长期保住的核心资产

![](https://mmbiz.qpic.cn/sz_mmbiz_png/e9GhxSDPqRgNkC7xr4g9k5N1Rt0mr8b0cDDXvTdVppoLObtPiaIDFWE3EaWpuAc4ic59pSq2fqfRgiaxiaScGaEeDDC7InwUsR0wJt51grP36wE/640?wx_fmt=png&from=appmsg)

因此，平台重视的应该是封禁之后，黑产需要多久、花多少钱才能恢复原有攻击能力。如果只需重新注册或低价补入一批账号，黑产承担的仍然只是较低的补号成本；

如果需要重新采购手机号和设备、花费数日养号，并重新调试攻击工具，才会真正增加其资源成本、时间成本和维护成本。

封禁只有持续推高这些成本，才可能从清理风险账号，变成削弱黑产持续投入的能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8VOiack4f29cjg1STTg9bWovzGduMwouTqFVK2yEgJcTBX3E9cQL7eXkSPHuuTBGbz4MmnSrHHtvDIG4B0g6Lhw/640?wx_fmt=png&from=appmsg)

# 规则不断升级，为什么攻击仍能适应？

黑产能够持续投入，根本原因在于投入后仍然有利润，同样也会投入成本进行规则更新

平台限制IP，它可能更换代理网络；平台封禁账号，它可能补充账号池；平台升级验证，它可能调整脚本和工具。

在游戏“账号工厂”场景中，团伙将代理IP和自动滑块验证接入注册机，批量完成账号注册。验证不再只是一个独立关卡，而可能被拆解成注册流水线中的自动化组件。

宗某算力套利案则展示了更完整的调整过程：平台增加IP注册限制和电子签名校验后，攻击者又借助AI工具修改脚本、伪造签名，继续调用平台接口。

![](https://mmbiz.qpic.cn/mmbiz_png/e9GhxSDPqRhHpicDSV50BureQzylMSOR83Q4QfticV9bP2oYgy9wGyh7lcaQMh8FibEL9ZYm07zlE5EDia1Ba7lf6Z8XicB4M1AvFzGDD1WTLPyI/640?wx_fmt=png&from=appmsg)

两个案例共同说明，防守规则生效，不代表攻击能力就此消失。黑产会研究验证方式、请求参数和失败反馈，再调整账号、环境或工具。

AI Agent等工具的普及，还可能进一步降低这种调整成本。过去需要人工分析和反复测试的工作，现在可以更快完成。平台升级一次规则所换来的安全窗口，也可能因此缩短。

因此，“规则上线、短期有效、黑产调整、攻击恢复”并不意味着防守回到了原点，平台本来就处在这种持续博弈之中。规则升级的价值，不是一次性终结攻击，而是迫使黑产不断重新投入时间和资源，让攻击变得更贵、更慢、更难恢复。

如果一次规则升级，让黑产从修改几个参数，变成重新采购资源、改造工具并反复测试，它就已经抬高了攻击成本、压缩了收益窗口。平台需要评估的，也不只是“这次有没有拦住”，而是每一次防守让黑产多付出了多少成本、花费了多长时间，以及这些成本能否持续压缩其利润。

# **END**

![](https://mmbiz.qpic.cn/mmbiz_png/e9GhxSDPqRgJzRDBNj2TGI0Ph2CjlIrdX6NAa7kURqvM1b9RS9s6AbC1woiarIs1eyKW5vanmxfucCuQCEicHwZ31wFy5jicsncrvDKsZ0RntE/640?wx_fmt=png&from=appmsg)

真正有效的防守，是让黑产发现：成功越来越难，账号越来越短命，资源越来越难以复用，工具维护越来越昂贵，最终收益又越来越难以兑现。

当继续投入已经无法覆盖作案成本，攻击才会真正失去持续性。拦截率只是这道经济题的起点，让黑产算不过账，才是业务安全更接近终点的答案。

【上一期结果公布】

看看幸运儿是不是你！ 非常感谢各位朋友的留言互动，本期抽奖中奖名单来啦🥳

👉中奖用户：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/e9GhxSDPqRgO93EbYE03sjCyAVAsa7JIVc7breHjaia25pMAmMwFmbxbNQjrwD2yIibicbMgLBnXXM4t5NjzKKOuQfiaZwYe1QNDuEQV2kJ1yVY/640?wx_fmt=jpeg)

🎁领奖提醒： 麻烦中奖的小伙伴尽快私信公众号后台，发送「中奖 + 你的收件信息」，截止时间 11 月 17 日 23：59 ，超时就视作放弃资格。 礼品会统一安排寄送，静候收货就好。

更多干货 + 福利正在路上，记得多多关注～

**关注科技与安全的朋友也在关注极验**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/e9GhxSDPqRiaaQtI8YsLfLmvriaTXibD90YecpZCV4oXXaMBvtZPsVqs16nELaIPYlSic0Z6IINVpu4K3XDicEac6KAUqzELjib5iagYxWCCdnfqno/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8VOiack4f29dibCUWr49Ya5END7RbP3D04rtFNpjhjtrAibMWQo3PhxdqC7mE307jVnNqwmhiadvXVQfkH9J4KnmXg/640?wx_fmt=jpeg&from=appmsg)

#极验#黑产对抗

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8VOiack4f29cpanIK3jdf5Bic4pNF2C2cMwJeibjlw4JHVtqKuJCEiaOic2MlVXnL6xbIib4ljvHLjKsicde4vT9iaPpyg/0?wx_fmt=png)

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