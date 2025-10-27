---
title: 奇妙的化学反应：Euler Finance 被黑分析
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497145&idx=1&sn=d1286caa8e0013713976683385e4c328&chksm=fdde8b3ecaa90228c676e1353d78366e8172aee92034dc91bbfc28715bad5dd2171f0af22f55&scene=58&subscene=0#rd
source: 慢雾科技
date: 2023-03-15
fetch_date: 2025-10-04T09:36:30.539761
---

# 奇妙的化学反应：Euler Finance 被黑分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLWrdGBsrhiaIMXYJplkyzH6mQFmfGd97HWhbVaKHPRCy9h0K4Thm7mXw/0?wx_fmt=jpeg)

# 奇妙的化学反应：Euler Finance 被黑分析

原创

慢雾安全团队

慢雾科技

By: 九九 & Zero

据慢雾安全团队情报，2023 年 3 月 13 日，Ethereum 链上的借贷项目 Euler Finance 遭到攻击，攻击者获利约 2 亿美元。慢雾安全团队第一时间介入分析，并将结果分享如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLVfL57oTs3RJR32wZntEbSrI29jYiaQaaSqPEhNhlF4xsGtrn1VGS6Vw/640?wx_fmt=png)

##

## **相关信息**

Euler Finance 是以太坊上的一个非托管的无许可借贷协议，帮助用户为他们的加密货币资产赚取利息或对冲波动的市场。

当用户在 Euler Finance 上进行存款抵押时会收到对应的 EToken 作为凭证，后续赎回抵押品和进行借贷时都是通过 EToken。EToken 的设计使用户可以通过铸造 EToken 并直接使用新的 EToken 作为抵押品来借出更多的资产并增加债务，即以叠加杠杆的方式进行自我借贷(self borrow)。

Euler 的软清算机制是允许清算人灵活的帮被清算人偿还其债务，而不是只能按照固定的系数进行清算。

以下是本次攻击涉及的相关地址：

攻击者 EOA 地址：

0x5f259d0b76665c337c6104145894f4d1d2758b8c（下称攻击者 EOA 地址 1）

0xb2698c2d99ad2c302a95a8db26b08d17a77cedd4（下称攻击者 EOA 地址 2）

攻击合约地址：

https://etherscan.io/address/0xeBC29199C817Dc47BA12E3F86102564D640CBf99

https://etherscan.io/address/0x036cec1a199234fC02f72d29e596a09440825f1C

https://etherscan.io/address/0x036cec1a199234fC02f72d29e596a09440825f1C

攻击交易：

https://etherscan.io/tx/0xc310a0affe2169d1f6feec1c63dbc7f7c62a887fa48795d327d4d2da2d6b111d

https://etherscan.io/tx/0x71a908be0bef6174bccc3d493becdfd28395d78898e355d451cb52f7bac38617

https://etherscan.io/tx/0x62bd3d31a7b75c098ccf28bc4d4af8c4a191b4b9e451fab4232258079e8b18c4

https://etherscan.io/tx/0x465a6780145f1efe3ab52f94c006065575712d2003d83d85481f3d110ed131d9

https://etherscan.io/tx/0x3097830e9921e4063d334acb82f6a79374f76f0b1a8f857e89b89bc58df1f311

https://etherscan.io/tx/0x47ac3527d02e6b9631c77fad1cdee7bfa77a8a7bfd4880dccbda5146ace4088f

## **攻击核心点**

此次攻击的主要原因有两点：

1. 将资金捐赠给储备地址后没有检查自身是否处于爆仓状态，导致能直接触发软清算的机制。

2. 由于高倍杠杆触发软清算逻辑时，被清算者的健康系数会降低到 1 以下，导致清算者的清算获利可以完全覆盖其负债。因此由于清算后获得的抵押资金的价值是大于负债的价值，所以清算者无需进行额外的超额抵押即可成功通过自身的健康系数检查(checkLiquidity) 而提取获得的资金。

## **具体细节分析**

这里以攻击交易 0xc310a0af 进行分析，其他攻击的手法均一致：

1. 攻击者首先从 Aave 中闪电贷出 30,000,000 枚 DAI，并创建了两个子攻击合约(0x583c21) 和(0xA0b3ee)，为后续攻击做准备。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLz6Bv9YlwEm6jq2CuMgoaDvTHwRyHJ8rNp0GENzmMPex3LQp6y1bZAw/640?wx_fmt=png)

2. 其次将 20,000,000 枚 DAI 通过 deposit 函数存入 Euler 中，获得了 19,568,124.3 枚抵押物凭证代币 eDAI。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLIjGkIfu18XeqJ2Y0WkZ9B0VGiavMC2x82qjbMLDt2oicbpIvyQicf6xdA/640?wx_fmt=png)

3. 之后调用 mint 函数(self borrow) 进行借款，借出了 195,681,243 枚 eDAI 和 200,000,000 枚债务代币 dDAI。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLfmLYiagdrJpIvzvTl1KOnQmKe6MjHGeic0WNKSXaygiaU3XVzt1BUF9VA/640?wx_fmt=png)

4. 紧接着调用 repay 函数用剩余的 10,000,000 枚 DAI 进行还款，其目的是为了减轻债务并增加抵押物价值，以便再次进行借贷。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLcKpFHnQO1eQpaMicIWqhtC8ZAnHOvAiaiaibNkU4zOWyjCIm4Bhpfq6agw/640?wx_fmt=png)

5. 再次调用 mint 函数(self borrow) 进行第二次借款，借出了 195,681,243 枚 eDAI 和 200,000,000 枚 dDAI，此时该账户中大约 410,930,612 枚 eDAI 与 390,000,000 枚 dDAI。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcL8a0Rhq7s56NgRkamuqhC7uNnqYUQzcgz1xHMyXzAA2YicWzwUfrLBaQ/640?wx_fmt=png)

6. 然后调用 donateToReserves 函数将 100,000,000 枚 eDAI 捐赠给储备地址，此时账户中的 eDAI 剩下 310,930,612 枚，而债务代币 dDAI 有 390,000,000 枚，此刻账户处于爆仓状态，但 donateToReserves 函数并没有检查账户的健康系数。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLZlrtHGJjVr9ictkQejMXjX1aMEzOyM0doDhmV4TfQhZOibKlUvTy0ibJw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLD0a76MIcuiaicuicQdAktww5ACZnOkAVic4bvL27hIncP0xxL56ABArribw/640?wx_fmt=png)

7. 通过另一个子攻击合约 0xA0b3ee 调用清算函数去清算上一步中处于可被清算状态下的账户 0x583c21。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLmvYLf5tM2SDo5ztDW2csLuRU7hdb8w6uUQCEXdway5cSsxR17CYXyg/640?wx_fmt=png)

清算过程中将 0x583c21 账户的 259,319,058 枚 dDAI 的负债转移到 0xA0b3ee 上，并获取了该账户的 310,930,612 枚 eDAI。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLhaucGwm84WBzqiaU8M9eBicMAniasMmia88bS4eRWzQWsKlLVlAMkvcERg/640?wx_fmt=png)

可以看出清算人仅承担较少的债务却可以获得绝大部分的抵押品，这是因为 Euler 的软清算机制：当清算人开始进行清算时，将会根据债务人的健康系数计算折扣。根据这个特性当健康系数越低时，折扣越大，所能转移抵押品越多，最终只要能覆盖本身的债务既可完成获利。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLwXMxr76cPmvibOEjpUnibzR4iaGbExbPyI4Eg1SJhUL7cIJfV9wZtNs9A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcL8icO9ELT4hTIOsBqiaRv8Bqo3HdEKne7Kic9SWKV6TS4BPR19oOEhg29A/640?wx_fmt=png)

由于清算后 0xA0b3ee 账户获得的抵押品是超过债务数量的，所以能成功通过清算检查。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcL94kKVusHs8rovVicnD7gcAZHH3AHX9pyyFDuP9EzTZBsPmNAGcTeImw/640?wx_fmt=png)

8. 最后通过调用 withdraw 函数进行提款上一步清算中得到的资金，并归还闪电贷获利。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLYZRwAlrrMqzXywmSmDRicxHcZ1Qsycib289LQf7XfNwicZRaJSRpaiaiboQ/640?wx_fmt=png)

## **MistTrack 链上追踪**

截止发文时间，100 ETH 已经被黑客转移到 Tornado Cash。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLvqxbKia3XOaepic9bHnxlHGF3jnpticyYE8MFicjmcUZ5wfEbg1ILPkViag/640?wx_fmt=png)

剩余资金作为余额保留在黑客地址，以下为详情：（备注：价格取 2023-03-14 10:00 UTC）

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLI1KHIbJld54sAdW8CkJEYicfJbjRA9qRhhIqftOwcbiaaSazQqafmdog/640?wx_fmt=png)

值得注意的是，此次攻击事件共有 6 笔攻击交易，除了第一笔攻击交易为攻击者 EOA 地址 1 发起的外，其他的攻击交易发起人均为攻击者 EOA 地址 2。

以下是 6 笔攻击交易的时间线：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLENWJrNrPTDj1RoAiaVG8eqPDIQPyVpT3ZNemzp9wvwE2cwxDtRaO8oQ/640?wx_fmt=png)

2023-03-13 11:38:11 UTC，攻击者 EOA 地址 1 将获利的 8,877,507.34 DAI 提款到攻击者 EOA 地址 2 的获利地址。

2023-03-13 12:08:35 UTC，攻击者 EOA 地址 1 发起链上喊话交易，喊话内容为：攻击者 EOA 地址 1 自称为 MEV 机器人，抢跑了攻击者 EOA 地址 2 的第一笔攻击交易，尝试抢跑其他的攻击交易但失败。更不幸的是，它创建的攻击合约只能提款到攻击者 EOA 地址 2 的获利地址。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLU7nVYTGZbZXmfzIKicfCv1zeVePAqbU2KIibdx54GicjgFGxKPvYjG7Qw/640?wx_fmt=png)

根据 MistTrack 链上分析团队分析，攻击者 EOA 地址 1 的手续费来源地址是 30 天前在 BSC 链采用闪电贷攻击手法攻击 EPMAX 项目的黑客地址，攻击获利 346,399.28 USDT。

攻击获利后，EPMAX 黑客地址通过 cBridge 跨链到 ETH 链后将获利资金转移到 Tornado Cash。EPMAX 黑客使用到的平台工具有 Multichain, FixedFloat, cBridge, 1inch 和 KyberSwap。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLeMClWV5kV5rIaWdb8Uicge6VXMT2jA5pqJ58s3tAdZ9smnmJd2WJWxw/640?wx_fmt=png)

攻击者 EOA 地址 2 的手续费来源是 Tornado Cash。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZmb3Q2IepB8rBcQje9CEcLapGuOAxZ7efIzIFGqibXu6JqeTwUYUtmhfDXzVY5RhUS7Zxy7r1mtGQ/640?wx_fmt=png)

## **总结**

综上所述，我们可以发现其实单独看 donate 操作，不检查捐赠用户的流动性是没有问题的。当用户捐赠后处于爆仓状态时，自然会有套利机器人进行清算。而单独看软清算的特性反而可以减轻过度清算以及清算不足的情况，正常清算的情况下是要求清算者需要有一定的抵押物，以避免完成清算后无法通过流动性检查。

但当捐赠操作与软清算相结合时就发生了奇妙的化学反应，攻击者通过杠杆(self borrow) 与捐赠特性将本身的健康系数降低到 1 以下，这就直接导致了清算者在完成清算后的获利可以覆盖其负债。

此次攻击事件的根本原因在于涉及用户资金的关键函数缺少流动性检查，并与动态更新折扣的清算机制构成了套利空间，导致攻击者无需抵押或偿还债务即可套取大量的抵押品。慢雾安全团队建议借贷类型的协议在涉及用户资金的函数需要做好必要的健康检查，并且需要考虑到不同模块组合后会形成的安全风险，设计安全的经济模型与业务模型。

**往期回顾**

[ZKP 系列之 Groth16 证明延展性攻击原理及实现](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497116&idx=1&sn=9122e84ffd7d66b96695e20c3940ce7a&chksm=fdde8b1bcaa9020d95404c2f302e90afb42398b6512fa054ca22954664f163e3979e6c04644b&scene=21#wechat_redirect)

[引介｜EVM 深入探讨 Part 5](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497104&idx=1&sn=85f08352d0abb5730fed8f6857b4e75e&chksm=fdde8b17caa902012781c59751443160c13bd75e88f54c6ddeb5f2ae3b4d22aadc3534ba6e74&scene=21#wechat_redirect)

[最流行的以太坊客户端 —— Prysm 已通过慢雾安全审计](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497093&idx=1&sn=c96c09970099c484242a758938b57bd7&chksm=fdde8b02caa90214a34aa116c0f7bd3c1116dbadce29636882a0caebc24559c91903ba253876&scene=21#wechat_redirect)

[NFT 防钓鱼指北：如何选择一款防钓鱼插件](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497080&idx=1&sn=7d238035ebad68267044085f503976da&chksm=fdde8bffcaa902e98dd964116386ad6674e305411faf7aec99b5996601298115ad21267d0486&scene=21#wechat_redirect)

[ZKP 系列之 Circom 验证合约输入假名漏洞复现](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497028&idx=1&sn=79d9c0773c1a16a5e94d32294b7ca75c&chksm=fdde8bc3caa902d5ac89af5b6c59233bcffe37ce7cce8aa4fe8eb6aa9cd388a4065ab92a5bfa...