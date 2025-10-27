---
title: 慢雾：警惕 TransferFrom 零转账骗局
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496770&idx=1&sn=f95df1020b2319e3a1c9469829686c13&chksm=fdde8ac5caa903d3f873fed02a107b0be4ba5343256d5882e4540480cbae1adeb8e6759a6f65&scene=58&subscene=0#rd
source: 慢雾科技
date: 2022-11-27
fetch_date: 2025-10-03T23:53:25.346751
---

# 慢雾：警惕 TransferFrom 零转账骗局

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYdBB5ibXSIK9FicapZU87LPibF6ic9eEeyXGKaoh8OWibQZ0AeyibUbqbyU15lpNvg16VsQUW8ECptf80Q/0?wx_fmt=jpeg)

# 慢雾：警惕 TransferFrom 零转账骗局

原创

慢雾 AML 团队

慢雾科技

By: Lisa

距上次披露 “[相同尾号空投骗局”](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496658&idx=1&sn=86b93a4b30854c5002e04007f4531fc0&chksm=fdde8d55caa90443fd0353f54991a26fa7fceb03dbc4a8268cd09e311322018bb1314aef7081&scene=21#wechat_redirect) 没多久，近日，我们又在用户的反馈下捕捉到一种很相似的手法。

根据多名用户的反馈，用户在 TRON 上的地址转账记录中不断出现陌生地址转账 0 USDT，而这笔交易均是通过调用 TransferFrom 函数完成的。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbaUR6yN6c3XM8SMG2tVZjWC2wUJP5o1wIjWSHkEIuibicpMaeEaurKO90crw7F8uNAScbsGxibRrEHw/640?wx_fmt=png)

（图 1）

随意点进一笔交易查看详情，如图 1 红框第一笔 tx 为 701e7 的交易：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbaUR6yN6c3XM8SMG2tVZjWH5HewPPrcTRbqX8ia1xFdL7sYD11ndrQHt0WmE7b8N2ckS2O81LLnaA/640?wx_fmt=png)

（图 2）

这笔交易是 TCwd 开头的地址调用 TransferFrom，将 0 USDT 从以 TAk5 开头的地址转到以 TMfh 开头的地址。

也就是说，罪魁祸首是以 TCwd 开头的地址，我们去看下这个地址的情况：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbaUR6yN6c3XM8SMG2tVZjWASJAC8FCMzMpgvGxkWcibZ7fZ1UUF4FfMGibz0RT95t5ue5PCQ8ZtCpA/640?wx_fmt=png)

（图 3）

可以看到，这个地址在疯狂地批量调用 TransferFrom。

接着，我们看看此地址在 USDT 的转账情况。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbaUR6yN6c3XM8SMG2tVZjWoxgGNrehLjZwYicW7I0meY2NxeCMLUnhgZ5auEouBIVfAAtB78iaGPwQ/640?wx_fmt=png)

（图 4）

几乎全是转出 0.001 数额的记录。这让我想起了尾数相同空投骗局也曾出现过类似的情况。也就是说，这个以 TCwd 开头的地址可能是作为主地址之一，将 0.001 分发到不同的地址，而这些不同的地址都有可能是攻击者用来空投的地址。我们选择地址 TMQy...6ZRMK 进行验证：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbaUR6yN6c3XM8SMG2tVZjWYlmF7uZvA4JMGJZjxEklkTuP41GNsGOic2b94MuRSoEITEzl5dWsVxQ/640?wx_fmt=png)

（图 5）

USDT 接收地址都是 TADXT...Lhbuo，再往下追溯：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbaUR6yN6c3XM8SMG2tVZjWdJQhsqibibsKS9GpjbI0oOpoTO7hzBKvZEmZkaZSnsr9hSLKbLUibgQUw/640?wx_fmt=png)

（图 6）

从图 6 其实可以发现，地址 TADXT...Lhbuo 曾经与 TMQ...QZRMK 地址有过 2 笔正常转账，而攻击者利用尾号 ZRMK 相同不断空投小额 USDT。也就是说，这个用户不仅遭受尾号相同的空投骚扰，也遭受着本文提到的 0 转账骚扰。那也可以认为，这两种相似手法的背后是同一个团伙。

经过对该手法的分析，究其原因主要是代币合约的 TransferFrom 函数未强制要求授权转账数额必须大于 0，因此可以从任意用户账户向未授权的账户发起转账 0 的交易而不会失败。恶意攻击者利用此条件不断地对链上活跃用户发起 TransferFrom 操作，以触发转账事件。

我们不禁猜想，除了 TRON 上，在以太坊上会出现同样的情况吗？

于是我们在以太坊上进行了一个小小的测试。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbaUR6yN6c3XM8SMG2tVZjWpANbgnnvlq4lwpz1FNMEV8jMbcwwhfZfJv0zx3faNVz9qheGNuvTFQ/640?wx_fmt=png)

（图 7）

测试调用成功，在以太坊上这个规则同样适用。

不免想象到，如果用户发现了非自己转账的记录，可能会因此产生自己钱包是不是被盗的恐慌情绪，当用户去尝试更换钱包或者重新下载钱包，会有被骗被盗的风险；另一方面，用户的转账记录被攻击者“霸屏”，可能会因为复制错误转账地址而导致资产丢失。

慢雾在此提醒，由于区块链技术是不可篡改的，链上操作是不可逆的，所以在进行任何操作前，请务必仔细核对地址，同时，如果发现地址出现异常转账情况，请务必警惕并冷静检查，如有需要可以联系我们。

*Ps. 感谢 imToken 安全团队的协助。*

*相关代码链接：*

*https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7#code*

*https://tronscan.org/#/token20/TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t/code*

**往期回顾**

[引介｜EVM 深入探讨 Part 3](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496759&idx=1&sn=b2ed9ce466803dbee59b390ab9d0b1f4&chksm=fdde8ab0caa903a6e48cb7da529c6a1f8271fb39d89382f3114bccf3c11f24fbdd01150abdaf&scene=21#wechat_redirect)

[智能合约安全审计入门篇 —— Phishing with tx.origin](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496742&idx=1&sn=ce5f542b5bd108483592250598b0daff&chksm=fdde8aa1caa903b73640f8464542eed5d6b809a4815cb11332de1872a8b00c96e4327b3d1c63&scene=21#wechat_redirect)

[慢雾 | 智能合约安全审计服务全面增加 Move 安全审计项](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496735&idx=1&sn=2dc98e009904eacdefad22c27b2c40a1&chksm=fdde8a98caa9038eec3625138f078fe85c61e65df1fda35308f4200866e6bab729118fa0d4fa&scene=21#wechat_redirect)

[MistTrack 案例一 | TornadoCash 提款分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496723&idx=1&sn=0ea66570db1fd0c09694506287a46bcf&chksm=fdde8a94caa9038271a690faa41c1f941083f8f5a671fa33df373bc201cfa2066ad61367dcce&scene=21#wechat_redirect)

[慢雾严正声明](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496710&idx=1&sn=8251b764cd551cddbb5c9cc2b5584d0b&chksm=fdde8a81caa90397596db950faf203404d792b594aa3824dac23cc2f08756b2cf04e50b610b2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYfUh8nP24R9XPyrycKa2v1iblTkmpe7hZONa2pqg4b1X1fhtNokuzIj44aaBuGRYo1cybA8pqB1fg/640?wx_fmt=jpeg)

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