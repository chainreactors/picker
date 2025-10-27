---
title: ZKP 系列之 Circom 验证合约输入假名漏洞复现
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497028&idx=1&sn=79d9c0773c1a16a5e94d32294b7ca75c&chksm=fdde8bc3caa902d5ac89af5b6c59233bcffe37ce7cce8aa4fe8eb6aa9cd388a4065ab92a5bfa&scene=58&subscene=0#rd
source: 慢雾科技
date: 2023-02-21
fetch_date: 2025-10-04T07:37:48.755743
---

# ZKP 系列之 Circom 验证合约输入假名漏洞复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFibFvriaZgUPVgmLSMpPicGyyGOIjyNRc1kZxU9Cv8a8fKHviaAtSTFB0tQ/0?wx_fmt=jpeg)

# ZKP 系列之 Circom 验证合约输入假名漏洞复现

原创

慢雾安全团队

慢雾科技

By: Victory

**概述**

此前，俄罗斯开发者 poma 在 Semaphore 上发现了一个零知识证明验证合约存在双花漏洞（详见 https://github.com/semaphore-protocol/semaphore/issues/16）。出于兴趣，想先尝试复现一下该漏洞的 PoC，但由于漏洞代码是很久以前的代码，且该项目相对复杂，因此决定自己编写一个简单的 PoC 来复现漏洞。

##

## **前置介绍**

零知识证明（ZKP）技术的核心是一个叫做「证明系统」的算法。该算法通过对消息进行一系列的计算，生成一个证明，用于证明消息的真实性。接收者无需拥有其它信息，只需验证证明，即可确认消息的真实性。

ZKP 的实现有许多种实现方案，我们在之前的文章[《盘点 ZKP 主流实现方案技术特点》](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497003&idx=1&sn=21a449f322652cd26b739fbf87f17d78&chksm=fdde8baccaa902ba0956dfbb2f747451ed7ef543fbe33e4e062d88dbc4b5a50106266c8e8145&scene=21#wechat_redirect)里为大家介绍了各种证明系统及编程平台，本次实验中使用的正是其中的 Circom 平台。

Circom 使用 Groth16 和 PlonK 作为其证明系统，在开发过程中我们可以任选其一，开发框架可以在不需要改变电路的情况下自动为开发者生成证明参数和验证合约。

简单来说，Circom 通过在客户端生成见证数据和证明数据，将这些数据提交到合约。verifier.sol 合约负责对提交的数据进行校验，以验证证明是否是在规定的规则下生成的。这种方法可以实现快速、高效和安全的验证，无需暴露消息的具体内容，保护消息的隐私性。

## **漏洞解析**

1、话不多说，我们直接上问题代码，请看下图的 verifyHash 函数。图中红框内的代码是记录某次见证数据是否有使用过，这种用法在防止双花上是比较常见的。但是此次漏洞的出现就是出现在这个见证数据 hash1 上。按照正常的理解一组 proof 数据应该只能匹配一组 hash1 进行验证。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFm3tzsMTWyvLqgWek23jUKxbU2mbu3Y2cXM2zia9xrUw45FMehIG0ALg/640?wx_fmt=png)

2、在 verifier.sol 合约中，函数 verify(uint[] memory input, Proof memory proof) 的作用是对传入的数值进行椭圆曲线计算校验。该函数利用名为 scalar\_mul() 的函数实现了椭圆曲线上的标量乘法。具体地，它会使用输入的参数对椭圆曲线进行计算，并比较计算结果与给定证明中的值是否相等，以确定输入值是否有效。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFMaOvXbxGricx4RSxadvx9ZDXONSVNCb8DVPxrIlaR0t1T43licdGqXIA/640?wx_fmt=png)

3、在 Solidity 智能合约中，需要使用 uint256 类型来编码 Fq。但是，由于 uint256 类型的最大值大于 q 值，可能会出现多个不同的整数在进行 mod 运算后会对应到同一个 Fq 值的情况。例如，s 和 s+q 实际上表示同一个点，即第 s 个点。同样的，s+2q 等等也都对应到点 s。这种现象被称为「Input Aliasing」，也就是这些数互为假名。

这里的 q 值是指循环群的阶数，也就是可以输入多个大整数会对应到同一个 Fq 中的值的数量。简单来说，即使将 hash 加上一个 q 值，仍然可以通过验证。在 uint256 类型的范围内，最多有 uint256\_max/q 个不同的整数可以表示同一个点。这意味着一组证明最多可以有 5 个匹配的 hash1 能够通过合约的验证。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFR5lYVZeQQZ88oeLj9ApzMjUs2ge6wwKwdCWiarGh5owwxRbpyEOc27g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfF4yr1gsAYVZypZCB4HEVRga26IJcJ5x1rwcq64j5ED0cJFz8Q1GrUMQ/640?wx_fmt=png)

## **漏洞复现**

1、实现一个简单的电路输入 2 个数据返回一个见证数据，就是在合约里面用到的 hash1。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFru30vPuNgicYNSJaiaxPTBzDH0B4A8W9u29RtJWia3lkbsx8ibUlQpmHmQ/640?wx_fmt=png)

2、对电路进行编译生成 circuit\_final.zkey, circuit.wasm 和 verifier.sol。接着生成一组 proof，一个正常的 hash，一个攻击 hash。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfF7QHlsWWjhwwwuWUlOxO1K08V4kPz2jtcge0ILIM6Y1lvib1UT3rtbXg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFG1sjDfMJcnDfZTF9pric1GwI8YvicTupXtqa2P9VOFPNuxEib4jEgx3Aw/640?wx_fmt=png)

3、随后部署合约，使用前面生成的 checkHash 进行一次验证，验证通过。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfF0ZRcJs6Thqr9xFVleib8v3bRsyvmTmcKxlNZcPxoLO7gwf4FdtsgTYg/640?wx_fmt=png)

4、接下来在使用相同的见证数据与前面生成的 attackHash，发现验证一样是通过的。这说明了一组 proof 可以有多个匹配的 hash 能通过合约的校验。至此 Circom 验证合约输入假名漏洞复现成功。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFicOhnsg2KxKVibwJ9zNJsljNJwqoelR3Kg7OGOkUgSOaDtvDGnnh8u2w/640?wx_fmt=png)

**漏洞的解决方案**

此次漏洞是由于一组证明可以有最多 5 个匹配的 hash 能在合约上通过验证。所以漏洞修复也很简单，就是限制所有输入的 hash 都要小于 q 值。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZKoNicjYeib9tqmbnG6owKfFDLZHWpvQofFDnjPjmSAo86GnIZo9c5ibWhI7a5kqib9yeQ6Hj3WHhlMQ/640?wx_fmt=png)

##

## **总结**

输入假名漏洞在零知识证明及密码学实现里是一个比较通用的漏洞，本质原因是数值在有限域内取余相同，开发者在进行密码学开发时需要注意验证群的阶数。

**参****考链接：**

*[1]. https://github.com/kobigurk/semaphore/issues/16*

**往期回顾**

[慢雾：盘点 ZKP 主流实现方案技术特点](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497003&idx=1&sn=21a449f322652cd26b739fbf87f17d78&chksm=fdde8baccaa902ba0956dfbb2f747451ed7ef543fbe33e4e062d88dbc4b5a50106266c8e8145&scene=21#wechat_redirect)

[慢雾：“揭开” 数千万美金大盗团伙 Monkey Drainer 的神秘面纱](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496989&idx=1&sn=b1129d682fb132b08aa44e380c741c66&chksm=fdde8b9acaa9028c6d506e974a2a038b28834cf26d036aab0ac1d96342a1b64dbbe0a3844212&scene=21#wechat_redirect)

[暗度陈仓 —— Orion Protocol 被黑分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496929&idx=1&sn=67eefeea3c1161bbf2ea6e1de92d5093&chksm=fdde8a66caa90370fe7b27060e3c23d11cc830c61a7c760d5fb9a9e03bee46b680e23123bc2a&scene=21#wechat_redirect)

[瞒天过海 —— BonqDAO 被黑分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496912&idx=1&sn=51626c406874ef0c3367bf1fbd55f75a&chksm=fdde8a57caa9034158cd1fcb92dc9ffcfc08371da28f1a0d647c9b9c980d658aa92dafd599c5&scene=21#wechat_redirect)

[喜迎五周年 | 慢而有为，雾释冰融（文末有惊喜）](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496889&idx=1&sn=82e7a4703406a90cc51205c1f47a2eee&chksm=fdde8a3ecaa90328101608c67378fc1267915fbeb732fc1efe4a6c143e0c640b77eac6dd4f93&scene=21#wechat_redirect)

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