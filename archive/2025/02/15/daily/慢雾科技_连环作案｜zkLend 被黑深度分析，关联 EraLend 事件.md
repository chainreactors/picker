---
title: 连环作案｜zkLend 被黑深度分析，关联 EraLend 事件
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501146&idx=1&sn=90497fe1fb951860c7927052f13be74d&chksm=fddebbddcaa932cb45b0cb9cc1af6a57876edb35e4e73bd3cf0bd151c488702d455e1748c84b&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-02-15
fetch_date: 2025-10-06T20:37:27.392630
---

# 连环作案｜zkLend 被黑深度分析，关联 EraLend 事件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FMyGzrRTiaQfibvUccsGnLGq7VgZRuBiaBMeN6pNTINwia7METegYPS28Sg/0?wx_fmt=jpeg)

# 连环作案｜zkLend 被黑深度分析，关联 EraLend 事件

原创

慢雾安全团队

慢雾科技

**背景**

根据慢雾安全团队情报，2025 年 2 月 12 日，Starknet 链上的头部借贷平台 zkLend 遭到攻击，损失了价值近千万美元的资产。慢雾安全团队对该事件展开分析并将结果分享如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9Ft2y1fZFzpxKxRFYf6oqZ5R4L7tDiacrJ0noThs9lPHkmR6R9Of3xAog/640?wx_fmt=png&from=appmsg)

(https://x.com/SlowMist\_Team/status/1889659563517026772)

## **相关信息**

**攻击者地址：**https://starkscan.co/contract/0x04d7191dc8eac499bac710dd368706e3ce76c9945da52535de770d06ce7d3b26

**存在漏洞的市场合约地址：**https://starkscan.co/contract/0x04c0a5193d58f74fbace4b74dcf65481e734ed1714121bdc571da345540efa05

**攻击交易之一：**https://starkscan.co/tx/0x0160a5841b3e99679691294d1f18904c557b28f7d5fe61577e75c8931f34a16f

##

## **根本原因**

本次被黑事件的核心原因在于空市场中累加器的值可以通过闪电贷中的独特机制来操控放大，并且市场合约采用的 SafeMath 库在进行除法计算时使用直接相除的形式，导致攻击者可以利用放大后的累加器造成向下舍入漏洞来获利。

##

## **攻击步骤分析**

###

### **攻击前置准备**

1. 首先攻击者调用市场合约的 deposit 函数往合约中存入数量为 1 wei 的 wstETH 代币。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FZFIMSibtm9NW4ModzMcR8ywFqeRuxWU0BxjyAE2qPh8icWdErz7xGEwg/640?wx_fmt=png&from=appmsg)

我们可以看到 wstETH 代币的市场是处于一个空市场的状态，市场合约中拥有的 wstETH 代币的数量与铸造的 zwstETH 的数量在该笔存款之前均为 0，这让攻击者可以用极低的成本进行下一步中的操纵。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FADr1ia7Kmd87Opz4ch5R0jBl1tOAAa0UyNh6eagHoUX47h7FHhSpnTQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FZfKAxopuCicAwGwdPT2eA4bJ6XpX62vibNaptgy9vRjRuRsrPXrPKJ6w/640?wx_fmt=png&from=appmsg)

此时 wstETH 市场中的 lending\_accumulator 的值为 1e27。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FRicv5S3wuyjS2z7rNicSJ1cXAA3kAYdBxTibnwbbYTUQ8h9VGC39hfeDQ/640?wx_fmt=png&from=appmsg)

交易哈希：https://voyager.online/tx/0x039b6587b9d545cfde7c0f6646085ab0c39cc34e15c665613c30f148b569687

2. 接着攻击者调用了市场合约的 flash\_loan 函数进行闪电贷操作，借出了 1 wei 的 wstETH，而归还了数量为 1000 wei 的 wstETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FueEAHB55SIIdw77R807jSCCCNLyRE9tmcdyBBibgYcl29zibcribPL3Xg/640?wx_fmt=png&from=appmsg)

可以看到，在闪电贷之后，wstETH 市场中的 lending\_accumulator 的值为 8.51e29, 与之前的值相比，竟然放大了 851 倍。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FvicZBZh0Fsz8G6GMNDELXC0aamKUwLvxAIpjib9DFaDaoekhVa1fz2FA/640?wx_fmt=png&from=appmsg)

交易哈希：

https://voyager.online/tx/0x039b6587b9d545cfde7c0f6646085ab0c39cc34e15c665613c30f148b569687c

那么是什么原因导致 lending\_accumulator 的值能被操控放大这么多呢？让我们跟进到市场合约的 flash\_loan 函数中：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9Fy8wVIuPPloEI7Eq5zoebxymu6KUV42RHV7AVjDkjwzS36gkhtkygOw/640?wx_fmt=png&from=appmsg)

可以看到在用户归还闪电贷之后，调用了一个名为 settle\_extra\_reserve\_balance 的函数。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9Ft6mCJVwuECKmuJRnvr90mGwicj8JKy1EE4icddPCjQhPENHSUluic8JFA/640?wx_fmt=png&from=appmsg)

该函数的作用主要是将合约中多余的资金分配给存款人，而分配的方式是用合约中多余的资金计算出一个新的 lending\_accumulator，并更新保存到对应资产代币的市场数据中。计算公式可以简化为如下：

```
(reserve_balance + totaldebt - amount_to_treasury) * 1e27 / ztoken_supply
```

由于市场在之前是处于一个空市场的状态，所以其中 reserve\_balance 为用户还款的闪电贷的数量，即 1000 wei，totaldebt 为 0，amount\_to\_treasury 计算出来为 149 wei，zwstETH 的供应量为上一步先前存款操作时铸造的 1 wei，最终计算出来新更新的 lending\_accumulator 为 8.51e29。

从历史交易记录中可以发现攻击者进行了多次相同的闪电贷操作，通过每次都还款更多代币的方法来迅速操控 wstETH 市场中 lending\_accumulator 的值。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FCib0hicJKf5NeGOhf5oicVPvFgGgmy6pU5Hqj91SwTAmQtXwVv9ZIGl1g/640?wx_fmt=png&from=appmsg)

最终 lending\_accumulator 被放大到了一个非常大的数值 4.069e45（4069297906051644020000000000000000000000000000）：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FOqcdUC7fN6QygdCGeYbeRdCZ4aM8YosibYAlovELRjgraibyAk9xo2hQ/640?wx_fmt=png&from=appmsg)

### **正式攻击**

交易哈希：https://voyager.online/tx/0x0160a5841b3e99679691294d1f18904c557b28f7d5fe61577e75c8931f34a16f

1. 当有其他用户往 wstETH 市场存款后，攻击者开始正式的攻击操作。首先攻击者调用了市场合约的 deposit 函数，向合约中存入约 4.069 枚 wstETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9F6Go8OtHEUr2temADRiaUibdia7U7fE9Fia10jaaJ0Zk09ASfgl2gaiccccw/640?wx_fmt=png&from=appmsg)

2. 接着调用 withdraw 函数，提取约 6.1039 枚 wstETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FQyuUYAvbHtWLdibeS35OqDoSIWI9lxPsJfCWgnmbRzlo5rt59BbV8Fg/640?wx_fmt=png&from=appmsg)

3. 通过重复上面两步操作，攻击者从市场中最终窃取了约 61 枚 wstETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9F0wibHYmajjMwTuou3nGkicN88Xf4cPwgLLuJZRuU41XvXegOHzDHSmSA/640?wx_fmt=png&from=appmsg)

那么为什么攻击者只存入了 4.069 枚 wstETH，却可以提款出 6.103 枚 wstETH 呢？

跟进到 deposit 函数中，当用户转入资产代币 wstETH 后，会外部调用 zToken 合约来为用户铸造对应数量的 zwstETH 代币。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9F6ZND9bTZC9mowbxjeEP0bxLnhSWzHnasJodRZ9WicYa3CDt5hyWe19A/640?wx_fmt=png&from=appmsg)

用户实际获得的 zwstETH 数量是由传入的资产代币的数量与市场的 lending\_accumulator 计算：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9F1qIb7JDfvakzNm0H6uM96MWENZDzQr50IewflIumYjYuSwyQVvGe3A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FA9acWWBCNh9pfiaTiaqhpTZveQBsOEPN7z6v6Ydsy3BIJz5pKvRQ6TaA/640?wx_fmt=png&from=appmsg)

跟进到计算时用到的 safe\_decimal\_math 库中：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FbTy6auWibOibUw9RXOoMCAwWibFh0CTQVvptuuTUhjicSmg8KBdVymJ7LA/640?wx_fmt=png&from=appmsg)

所以可以得出实际获得的 zwstETH 数量的计算公式为：

```
zToken_amount = amount * 1e27 / lending_accumulator
```

其中 amount 的值为：4069297906051644021，lending\_accumulator 为攻击者操纵之后的值：4069297906051644020000000000000000000000000000。最终计算出来获得的 zwstETH 的数量为 1。

当用户调用 withdraw 函数提取 6.103 枚 wstETH 时，会调用 zToken 合约的 burn 函数来燃烧先前存款获得的 zwstETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9F5iak4bsd4zK5URtoKOJQHFNH3tqtichYll8W1tzpap4XnL8IfL39WXeQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FAQoICxqPlsWaMnRnnAazsG7eiahdOKzM30o71d1ZrQLgCzz4Mk7WOwA/640?wx_fmt=png&from=appmsg)

在 zToken 合约的 burn 函数中，我们可以发现实际所需要燃烧的 zwstETH 数量的计算方式与铸造时一样：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FnCian7S0lujzrvROpSNJyjgj9jx9jkDBeqiaXJKOuGvsSTo3k5x82icnQ/640?wx_fmt=png&from=appmsg)

其中 amount 传入的数量为 6103946859077466029，但是由于所使用的 safe\_math 库中的 div 函数在进行除法时是直接相除的形式，所以会截断结果中的小数部分。并且因为 lending\_accumulator 被攻击者在之前的操作中放大，最后计算出来实际应该燃烧的 zwstETH 代币的数量会因为向下舍入取整的问题也等于 1，刚好满足用户存款时实际获得的 zwstETH 数量。

```
6103946859077466029 * 1e27 / 4069297906051644020000000000000000000000000000 = 1
```

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FKna8w2F1jibBJWcwuyK6mtrl1YK0NW7vpS4BmAOib7AsKibicZH32MLoKA/640?wx_fmt=png&from=appmsg)

所以提款时燃烧 zwstETH 代币的逻辑可以正常通过，这也就是为什么攻击者可以只存入 4.069 枚 wstETH，却可以成功提款出 6.103 枚 wstETH 的根本原因。

而在正常的市场情况下，lending\_accumulator 的值应该是精度为 1e27 的数，相除时由于分子远大于分母好几个数量级，所以并不会受到影响。

## **MistTrack 分析**

据链上追踪工具 MistTrack 的分析，攻击者从 zkLend 盗取了约 950 万美元。随后将获利代币兑换为 ETH 后使用 LayerSwap, Orbiter Bridge, Rhino.fi, StarkGate ETH Bridge 等跨链桥跨链到各种网络，大部分资金被跨链到以下以太坊地址：

* 0xcd1c290198e12c4c1809271e683572fbf977bb63
* 0x0b7d061d91018aab823a755020e625ffe8b93074
* 0x645c77833833A6654F7EdaA977eBEaBc680a9109

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FoEoicJj9gk4xJcnzJ55kzbGia8AUia4Xiapaibkywz4SXtHzgRJUplxorMw/640?wx_fmt=jpeg&from=appmsg)

其中，地址 0x645c77833833A6654F7EdaA977eBEaBc680a9109 有很多历史交易，首笔交易出现在 2024 年 6 月 22 日。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9F1g9cQJN2WibbRIwciakxC5qr89L1sTpmns61fbxdlNnjJFw0Te6h8Hag/640?wx_fmt=png&from=appmsg)

该地址在以太坊、BSC 和 Base 网络上都有与 Binance 交互的记录，也可能是嵌套 Binance 账号接口的第三方交易平台。该地址在以太坊网络上还存在与 ChangeNOW 和 Hitbtc 交互的痕迹。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaXEcA3kWjDkZJy7HMbPc9FOiboafTP3zccLZHkovKYK30rRBDcOW8eA6FPNMSV8RP4PP6BQm1YLEQ/640?wx_fmt=png&from=appmsg)

进一步分析黑客在 Starknet 上的相关地址：0x04d7191dc8eac499bac710dd368706e3ce76c9945da52535de770d06ce7d3b26，发现该地址在攻击前与以下 L1 地址存在强关联：

...