---
title: Drift Protocol遭史诗级攻击
url: https://mp.weixin.qq.com/s/xJwLw26p_EQIm6kVNXti0w
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:40:57.131551
---

# Drift Protocol遭史诗级攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibicDQQkq5lsKWmFunIIQxdBlniaJTuT0icfygYu058B9EU0q5lOz6utTbRibYmRJo3b0lUSRkruCWtLrNB0etfvHg9aKa6JicBAia1nXFl0RYYpgA/0?wx_fmt=jpeg)

# Drift Protocol遭史诗级攻击

原创

ChainSecLabs
ChainSecLabs

ChainSecLabs

![]()

在小说阅读器中沉浸阅读

区块链安全相关的内容

我们将在这里分享一些

Hi，这里是ChainSecLabs！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsJOGhHLQ156HR2cJE1GUMer1UkMGwdQbaF8MicS3yshY8UkPe5XOmiaEWETuHhg5icyyQB5JGjj9iccnStEvNx9LOcdXVWbw88ZM98/640?wx_fmt=png&from=appmsg)

**01**

   从 500 美元假币，到掏空金库：

一场精心策划的 DeFi 攻击

2026 年 4 月 1 日，一起发生在 Solana 生态核心协议上的安全事件，迅速从“异常波动”演变为震动整个加密行业的重大黑客攻击。

作为 Solana 上最重要的衍生品交易协议之一，Drift Protocol 在短短不到一小时的时间里，被攻击者抽走了约 2.7 亿至 2.85 亿美元的资产。这一规模不仅使其成为 2026 年迄今为止最大的 DeFi 安全事件之一，也再次揭示了去中心化金融体系中一个长期被忽视的问题：真正的风险，往往不在代码，而在人和治理结构本身。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsKT8aZBYFD22tWkltX56bAEvia6lyQFPiaqXS5HBWKH5TmgOSzH1tyvc4LFxbQpVfCHRicYib9wf1lR8eg4RNNiaB5Bushdsw1SzlCQ/640?wx_fmt=png&from=appmsg)

**02**

Drift Protocol：

Solana DeFi 的“金融引擎”

在理解这次攻击之前，有必要先明确 Drift 的定位。

     Drift 并不是一个简单的去中心化交易所，它更接近于一个“链上金融系统”。其核心功能是提供永续合约（Perpetual Futures)，同时支持用户使用多种资产作为抵押进行杠杆操作，并通过资金费率、流动性池等机制维持市场运转。

在事件发生之前，Drift 的总锁仓量（TVL）一度超过 5.5 亿美元，并与 Jupiter 等核心协议形成深度集成关系，成为 Solana 生态中重要的流动性枢纽。

换句话说，Drift 并不仅仅服务用户交易，它本身也是其他协议流动性的重要来源。一旦其发生问题，影响将迅速向整个生态扩散。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsJiamd0HNcYeaNbZfPxcy3Iz58AsNydsYCZXGkwegk0yf6AxKaiayuYIwoDhcTqibicZ7387rnVbJXqaPYZicv34a2PMgtMFDj8IicCo/640?wx_fmt=png&from=appmsg)

**03**

攻击并非偶然：

一场持续数周的“预谋行动”

从链上数据复盘来看，这次攻击并非临时起意，而是一个至少持续数周的精密布局。攻击者并没有一开始就直接动手，而是先搭建好整个攻击所需的“舞台”。

最早的异常可以追溯到攻击发生前一到两周。攻击者创建了一种名为 CarbonVote Token（CVT）的代币，并为其设置了一个看似“正常”的市场价格。

但关键在于，这个价格完全是人为制造的。

攻击者在流动性池中仅投入约 500 美元资金，却通过控制交易对，使 CVT 的价格维持在接近 1 美元的水平。由于流动性极低，这个价格并不具备真实市场意义，但对于某些依赖链上数据的系统而言，它却可能被视为“有效价格”。

这一操作的本质，是为后续攻击准备一个“看起来有价值，但实际上几乎没有成本”的抵押资产。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsJVnZqzpEehzbbHyDPlticXsFggZ8qO6kZ2xQe8Vq2DywvwG7zCNrnbCuqDcrkdftNP0I3u8VCQjO4djhx2kQWSVUhIiboicImgKc/640?wx_fmt=png&from=appmsg)

**04**

真正的突破口：管理员权限被攻陷

如果说 `CVT` 是“子弹”，那么真正扣动扳机的，是 Drift的权限系统。

在攻击发生前一周，Drift 的多签机制刚刚经历了一次调整。新的多签账户由 5 个签名者组成，阈值为 2/5。这种配置本身并不罕见，但问题在于：

* 没有设置时间锁（Timelock）

* 权限变更缺乏透明公告

* 新签名者的安全性未知

更严重的是，这个多签账户拥有非常关键的系统权限，包括：

* 上架新抵押资产

* 修改风险参数

* 调整提款限制

攻击者正是利用了这一点。一旦获取管理员私钥（或控制足够签名者），就相当于获得了“协议级最高权限”。

在这次事件中，攻击者成功使用这些权限完成了两件关键操作：

第一，将 CVT 上架为可抵押资产；

第二，大幅提高提款限制参数，使原本用于保护资金的风控机制形同虚设。

至此，协议的安全边界已经被彻底突破。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsIobaXjyDBWfVSJlugBz0STqkNw9bXvSfhnghXhianPWI2Gg7D8GdIIWiaFt3T3Vl7LxMic5SkBYicrzRtuo0yeKAARwppeFkFGMNk/640?wx_fmt=png&from=appmsg)

**05**

核心：用“空气资产”换走真实资金

在完成权限控制之后，攻击进入最关键的一步。

攻击者分批向协议中存入约 7.85 亿枚 CVT。由于系统依赖价格预言机，而 CVT 在低流动性池中的价格被人为维持在 1 美元左右，这些代币被系统估值为约 7.85 亿美元。

这意味着，攻击者实际上用几乎可以忽略成本的资产，获得了巨额抵押价值。

接下来发生的事情，就变得“顺理成章”：攻击者以这些 CVT 作为抵押，从协议中借出并提取真实资产，包括：

* 大量稳定币 USDC

* 比特币和以太坊相关资产

* 流动性凭证（如 JLP）

整个过程仅通过十余笔交易完成，总计带走约 2.7 亿美元。

这一步的本质，可以用一句话概括：系统把“假价值”当成了“真实信用”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsLu8JgXicvicG7PUBLEfw9OYKGDX92Op9nia4hnlQGibB1PdZSMmMozpdbkMRww6hBw6fSVY5G1G7vr9ic857KY9BLeLk9PuibpvFHDg/640?wx_fmt=png&from=appmsg)

**06**

资金转移：经典的跨链洗钱路径

在成功提取资产后，攻击者迅速开始转移资金，以降低被追踪和冻结的风险。

其路径大致如下：

* 在 Solana 上通过聚合器完成资产兑换

* 使用跨链桥将资金转移至其他网络

* 在以太坊上将资产进一步转换为 ETH

这一过程完成得非常迅速，其中相当一部分资金被转换为 ETH，使追踪难度进一步增加。

这种“Solana → 跨链 → Ethereum”的路径，已经成为近年来 DeFi 攻击中较为常见的资金处理方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsJjFsKic6jqdMoSVCYVLkMQS0S5thyZz55UnATnPhxELAdSqfToLZ7ztdzhqfWicVFPouqYV9FMQJQNeFkGXtMeicOd34wRDN9jBI/640?wx_fmt=png&from=appmsg)

**07**

市场冲击：信任的崩塌更致命

事件发生后，Drift的总锁仓量迅速从约 5.5 亿美元下降至约 2.5 亿美元，几乎腰斩。同时，协议被迫暂停存取款，用户流动性受到限制。

其平台代币也出现明显下跌，而更重要的是，整个 Solana DeFi 生态的信心受到冲击。部分资金开始向治理更稳健、风控更严格的协议迁移。

在 DeFi 世界中，资金的流动本质上是“信任的投票”。而一旦信任受损，其恢复往往比技术修复更加困难。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsKUgqlPiathZe9Tbl04tRrsluVHJRxuvwzgBJ1wDxPaXDJC6Kn2ia7ia0Zy9gT52TUGhqa4U16ibcG8hw1ibiapjngqDw74dPOvlAvpo/640?wx_fmt=png&from=appmsg)

**08**

结语：技术很强，但人薄弱

Drift Protocol 本身在技术架构上并不落后，但这次事件证明，即使是设计先进的系统，也无法抵御治理和权限层面的失误。

这不是一次简单的黑客攻击，而是一场由多重机制漏洞叠加引发的系统性崩塌。

在 DeFi 这个仍在快速发展的领域中，类似事件可能不会是最后一次。但每一次重大事故，都会推动行业在安全、治理和透明度上向前迈进一步。

对于每一个参与者而言，最重要的或许不是追求最高收益，而是在复杂系统中，始终保持对风险的敬畏。

作者：何圆

编辑：Keats

审核：Chloe

\_\_\_\_\_\_\_\_\_\_\_\_END\_\_\_\_\_\_\_\_\_\_\_\_

---

**往期推荐**

[Layer2的身份幻觉](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485039&idx=1&sn=bcb57bfb4e4f593912e2757d8db28e4a&scene=21#wechat_redirect)

本文讨论了以太坊 Layer2 中地址别名的相关内容，包括其概念、安全背景、易踩的坑以及总结建议等，旨在让开发者重视地址别名以保障跨链协议安全。

[授权方式的更迭: 从 ERC20 到 Permit2](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247484939&idx=1&sn=8bbf8350d1217502f66261fe3e1add5d&scene=21#wechat_redirect)

本文将讨论 DeFi 领域代币授权方式从 ERC20 到 Permit2 的更迭过程及相关特点。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibicDQQkq5lsJtG89ic0SHrUt6Ou8LdpmwBHD8ibdtlul2T6dJAmSpD8Wu1zS9Lk7cFDH61iankYXACDFzrrrTZ4lEHmoFugjSztNyu6zhWqmicVc/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

[主流跨链协议攻击面](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247484876&idx=1&sn=18652e40780696b7f2411de3b3299f7b&scene=21#wechat_redirect)

本文将深入分析当前较具代表性的三种跨链通信协议--LayerZero、deBridge和Wormhole(虫洞)的底层机制。

[风起于青萍之末](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247484849&idx=1&sn=3907bb1b87676b1b4dd9472962553d5f&scene=21#wechat_redirect)

本文将剖析Router设计、通缩代币等魔改协议引发的安全陷阱，进而警示开发者在借鉴或修改成熟协议时需极度审慎。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibicDQQkq5lsIXPoXQBaXZYibe0FZH8rKicrpia4nDWUrlUtyPWKAibHg7FOe22jbOUl3sO1JfW3rHDC7d6ykznH1x7HEMd9QTibeGUwemcCGvBnd8/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

---

---

***搜索公众号  关注我们***

**「ChainSecLabs」**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/hlJuicHobAgAkYmYg8k9LKNWSibARYtAfX4VX0d6Q0HvQyKjdGKnkBRHYD9WGpQbtfD4W2ldGxKRBeBP2iaNFTFFg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

免责声明

      本文章旨在分享安全技术相关知识与经验，内容仅供学习与研究参考。文中所提及的技术手段、工具或操作流程，均基于公开资料与作者个人理解，不代表任何官方立场，也不构成对读者的具体操作建议。

      请勿将本文所述技术用于任何非法用途，否则后果自负。作者严禁并坚决反对一切网络攻击、非法入侵、数据窃取等违法行为，且不承担因读者不当使用文章内容而引发的任何直接或间接责任。

      若文章中引用了第三方工具或资料，版权归原作者所有，若有侵权或不妥之处，请及时联系，我们将第一时间予以处理。

      网络安全关乎法律与伦理，请读者在合法合规的前提下，自主学习、合理应用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hlJuicHobAgDplSpg2SBicqBEmlAlkxzR1vgnpCD7JMrKzoohqQrwYTgPu4oFYhVLwibVPOPjSjOpeX1E0BNibN3hg/0?wx_fmt=png)

ChainSecLabs

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hlJuicHobAgDplSpg2SBicqBEmlAlkxzR1vgnpCD7JMrKzoohqQrwYTgPu4oFYhVLwibVPOPjSjOpeX1E0BNibN3hg/0?wx_fmt=png)

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