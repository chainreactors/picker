---
title: BlockSec 安全周报｜八起攻击，漏洞都藏在哪？（3.23–3.29）
url: https://mp.weixin.qq.com/s/4VRmCfM6um2mRGIe5mSy5w
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:13:33.756394
---

# BlockSec 安全周报｜八起攻击，漏洞都藏在哪？（3.23–3.29）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4HxyqswpX3urxNdtrZ5KHcCHbqBHS69iadiaqe7RuPq5pQzW3NxEr8OsrnaRicPCJISnEzHF7Rb22nt8ZulNL98TbpwGyuFeUU5FhNtiaM/0?wx_fmt=jpeg)

# BlockSec 安全周报｜八起攻击，漏洞都藏在哪？（3.23–3.29）

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ibKZs4HxyqsOqPBjTxpX6xrzEK5EtzTY5tCcmsnagVxUhSJH3JU3VpnJoRb25pBSGW9g05aQnY5htKFgUk6SoiccfxuR8FKlmQwzpxZ204ZY/640?wx_fmt=gif&from=appmsg)

在过去一周(2026/03/23 - 2026/03/29),BlockSec 共检测并分析了八起攻击事件,预估总损失约 $1.53M。下表总结了这些事件,各事件的详细分析见后续章节。八起攻击事件中，有四起仅定位到受损合约，无法定位到具体项目方，因此下文中以unknown Incident标示。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqsxv7fZa5SyfERgdQxjEQKZa3UcVva20Rx8WdZVYWps6p6tDTu9YcI1fdU0sr9ibCELckmiaON2SHzNVTfRyJbVbCu7czIqHU8zw/640?wx_fmt=png&from=appmsg)

**Unknown Incident 1**

**简要概述**

2026年3月23日,Ethereum 上一个未验证合约因分发逻辑中的整数溢出漏洞遭到攻击,损失约 $97K。函数 0x317de4f6() 累加用户控制的代币数量时缺少溢出保护,攻击者触发溢出后,仅支付 1 wei USDT 便通过 claim() 提取了合约全部 USDT 余额。

**漏洞分析**

根本原因是合约 [0xF0a105...568C97](https://etherscan.io/address/0xf0a105d93eec8781e15222ad754fcf1264568c97) 中函数 0x317de4f6() 的整数溢出。该函数接受一组记录(每条包含账户和金额),通过遍历数组将所有金额累加到 totalAmount 中。由于累加过程缺少溢出检查,攻击者可以精心构造记录,使金额之和超出 uint256 上限后回绕为任意小值,而各条记录对应的分配额度依然很大。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqtRZOZtMQJZqavmdL1cx44R0Av33BrwXfiaP7Y33lJibWErXC8yEQlOZ5xGdF3iaLO0DWxmJ70MNn3dzqdlybPV5Sibkccuhwer9lI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqvpZ9F5VTXMpPLtGArjNsJlUIiawNMTnDwTUuuT21w62hCYsrKibEm7LE8rdydR9FLE4puJJAxtCr4Y0B7NOJNIb2iaq4SQFX0Vog/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqunTsewHQTOVw5OKI1UsD3IDQwicrG7IqFEqaeoufI5iakvlYtLXXLd8Gj6GvOL024gulYqs934aice2QIR74Qh3fRUibJ8jAKC0jo/640?wx_fmt=png&from=appmsg)

**攻击分析**

以下分析基于交易 [0x73bd1384...630b053](https://app.blocksec.com/phalcon/explorer/tx/eth/0x73bd1384e7b628a29542239be4bc96af0871f7aa22d410c0b38d62367630b053)。

Step 1: 攻击者从 Uniswap V4 借入 1 wei USDT 作为攻击的初始资金。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqukJ3jUsbxEficMXQw0kTicV0NUo6MSia7KmgZTPHLNcwMWIe0ZAVgxC6lokTiaykVuK1fdE7e97ZJAiaK8jNasYomGTw0o25uMGrDs/640?wx_fmt=png&from=appmsg)

Step 2: 攻击者查询受害合约的 USDT 余额,然后使用精心构造的数组调用 0x317de4f6()。其中一个金额设置为接近 uint256 上限,另一个设置为受害合约的 USDT 余额。两者之和溢出为 1,使攻击者仅需支付 1 wei USDT,却记录了等于受害合约全部 USDT 余额的分配额度。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqugpm3jpzBBMhRWrhlO0HibVr2BuCT3fHTiapRic1CUk99jXdJzn4znPsFfmxcd0kRhUTRicvPwXqTdYiaNgYgrYujvSa1354cI8CuE/640?wx_fmt=png&from=appmsg)

Step 3: 攻击者调用 claim() 从受害合约提取了 97,812e6 USDT。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqsSYZmNPbvMudW2PNs5iaYqulUt4GkbadSyLUKibKqkhcNHr8AttM6ibc7PKSl057pBnT6tzmtVVSEar0mmcbxkJU6kyH7LgakmFY/640?wx_fmt=png&from=appmsg)

Step 4: 攻击者偿还了从 Uniswap V4 借入的 1 wei USDT,并将剩余 USDT 兑换为 WETH,完成攻击。

**结论**

此事件凸显了在 Solidity 0.8.0 之前版本中使用未检查算术运算的风险。所有关键的财务计算都应显式使用溢出安全的算术运算(如 SafeMath 或 Solidity >=0.8.x)以防止溢出问题。

**Unknown Incident 2**

**简要概述**

2026年3月23日,Ethereum 上一个未验证合约因重入漏洞遭到攻击,损失约 $11K。函数 0xbe16634e() 在结算前就更新了流动性记账,并且在没有重入保护的情况下调用了外部回调。攻击者趁前一次调用尚未结算便反复重入该函数,虚增了自身的流动性记录,随后提取了超出实际存入量的 USDC 和 WETH。

**漏洞分析**

根本原因是合约 [0x39Ed37...9C6b08](https://etherscan.io/address/0x39ed372f8e9f316029994ca7f73b6683829c6b08) 中函数 0xbe16634e() 的重入问题。该函数在结算前就更新了流动性相关状态(包括用户流动性和 tick 储备),随后通过 msg.sender.call() 调用外部回调,且未设置任何重入防护。由于余额检查针对每次调用独立进行,攻击者可以递归重入该函数来虚增内部流动性记账,而最深层调用中只需一次代币转账即可满足所有嵌套的余额检查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqsIpw2nXqLwYcOTAMP0fD9wCnfb8xgykBnNPHG2GEKETUDp50oS9obqpKYKLuIIq6PpnOWE7e0P5Lr3sAj26yZNPzXTbASVsvs/640?wx_fmt=png&from=appmsg)

**攻击分析**

以下分析基于交易 [0x1382e898...fad993](https://app.blocksec.com/phalcon/explorer/tx/eth/0x1382e898ae7582d184903b504aa43191a5d240851d5477a7464a29e262fad993)。

Step 1: 攻击者从 Uniswap V4 借入 100e8 USDC 和 10e18 WETH 作为攻击的初始资金。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqu5nqCm68mngpQPsPB7LicrV6ZibicrUHzibqSmS8bgaDA6LgFnK7bRUPWRM9Vpk2neZ0tJT4bnuhicH2WYgrDqQBgS16U2ZhbeaIVw/640?wx_fmt=png&from=appmsg)

Step 2: 攻击者调用 0xbe16634e() 添加流动性。在执行过程中,受害合约调用了攻击者的函数 0x7c65be42(),该函数在前一次调用结算前重入了 0xbe16634e()。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqsccG7UnATXhHBiaRvxF9UM3ovJRBadJgzF61OO4ZhG0cWw0IFQNKGuibQ4iaF7X9VxyvO4aLaAbKA6mTzslDVPdEImmgPoTzsZG4/640?wx_fmt=png&from=appmsg)

Step 3: 通过多次重复此重入流程,攻击者持续增加了自己记录的流动性。在最深层调用中,攻击者转入所需代币一次,就足以满足嵌套的余额检查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqv6gY9KUjY1Z2Igxv12DselsVEQhPzgX1YSkiaJWrPY5lsibQfxKQYHWu3Xo7dqtXDOKRceLBqB4MlaksgTlnLk504KjZUOh8m4M/640?wx_fmt=png&from=appmsg)

Step 4: 虚增流动性记录后,攻击者检查了池子状态,并向池中转入额外资金,确保池中有足够的 USDC 和 WETH 来满足即将进行的提取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqsclrKica9dtXBwVq01ZWTNWhfb6w6gNQJnTibzDlyGK6n6z6yvdUkFvsbVc75xyic0cfvFXAbFGlb9JO2NibxzNZVkJBRGbkrviatY/640?wx_fmt=png&from=appmsg)

Step 5: 攻击者再次调用 0xbe16634e() 移除流动性,并基于虚增的记账数据从池中提取了 USDC 和 WETH。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqsdaxicN57fj2w7ib8fVXicZF07zUSAN1V8xibaXszys1rWOhKUgmfWWnv749j9PZYeZXnMsBLoNzicpSTT36We3u631V75DqfU1Jlg/640?wx_fmt=png&from=appmsg)

Step 6: 攻击者偿还了 Uniswap V4 的借款,将剩余 USDC 兑换为 WETH,完成攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqthC3FDCQiaoicx3Hy2Vz6Y5xfib60rbX0XvPTgZA4WBBKEia9maLWokyqETdUyA3jwH55cNdfa03iccQnbaRYnickuOyt5QESXS4dx0/640?wx_fmt=png&from=appmsg)

**结论**

此事件表明,在调用未受保护的外部回调的同时在结算前更新流动性记账是非常危险的。为防止类似攻击,协议应严格遵循 checks-effects-interactions 模式,并为外部回调添加重入保护。

**Cyrus Finance Incident**

**简要概述**

2026年3月23日,BNB Chain 上的收益农场协议 Cyrus Finance 因流动性移除公式依赖池子当前现货价格遭到攻击,损失约 $512K。该协议使用 CYRP NFT 仓位表示用户在 PancakeSwap V3 流动性中的份额,但将份额转换为底层流动性时读取了同交易内可操纵的 slot0()。攻击者通过闪电贷大额交换移动价格,虚增了 NFT 仓位对应的流动性价值,提取了超出合理权益的流动性。

**背景**

Cyrus Finance 是 BNB Chain 上的收益农场协议,负责管理 PancakeSwap V3 池中的流动性仓位。用户存入 USDT 后获得 CYRP NFT 仓位,代表其在协议多个 PancakeSwap V3 仓位中的份额。用户可通过 exit() 函数提取本金和收益。

**漏洞分析**

漏洞位于 CyrusTreasury（[0xb042Ea...0aE10b](https://bscscan.com/address/0xb042ea7b35826e6e537a63bb9fc9fb06b50ae10b)）的 withdrawUSDTFromAny() 函数。执行提取时,该函数从 PancakeSwap V3 池的 slot0() 读取 sqrtPriceX96(即当前现货价格),传入 getAmountsForLiquidity() 估算协议完整仓位当前对应的 amount0 / amount1。

随后,函数据此算出 availableUSDT,再用以下公式确定需要移除的流动性:

$liquidityToUse = liquidity  \cdot  remaining / availableUSDT$

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqsiarsMsTqMXTNG6eLlRn6Xj1g3PW5ISicrbZFvw9x3agYP8FUTO3nTZdhF8cjiaZq1u7tMYJScVB834fbTAahGNLQy6CodzjB3cc/640?wx_fmt=png&from=appmsg)

也就是说,合约不是直接按固定份额赎回,而是先用实时池价格估算仓位的 USDT 等值,再将请求的 USDT 金额反推为对应的流动性数量。

问题在于 slot0() 在同一交易内可被操纵。攻击者只要临时移动池价格,就能扭曲 availableUSDT,进而放大计算出的 liquidityToUse。

**攻击分析**

以下分析基于交易 [0x85ac5d15...46d452](https://app.blocksec.com/phalcon/explorer/tx/bsc/0x85ac5d15f16d49ae08f90ab0e554ebfcb145712342c5b7704e305d602146d452)。

Step 1: 攻击者从 PancakeSwap V3 池发起闪电贷,借入约 1,798 ETH。

Step 2: 攻击者在协议维护流动性的目标池中执行了大额 ETH 换 USDT 的交换,故意移动了池价格和当前 tick。同时,攻击者通过 safeTransferFrom() 将 CYRP NFT 仓位 #15505 从 0x01737d...6ffa3 转移到攻击合约。

Step 3: 攻击者在 CyrusTreasury 上调用 exit(15505)。执行过程中,withdrawUSDTFromAny() 从 PancakeSwap V3 池读取 slot0() 并基于被操纵的现货价格计算 availableUSDT。由于 tick 被扭曲,协议高估了 NFT 份额对应的流动性价值。随后调用 decreaseLiquidity() 和 collect(),释放了超出 Cyrus 仓位合理价值的 USDT。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqtib3fcG3SF6zNjr8IGUibrervlDAaXo5A3sJNOibibMQc5dWus4xAocVygj57ZLkeD2acRwgibntep4JqzqlS6dNt9TTceD4xxVssk/640?wx_fmt=png&from=appmsg)

Step 4: 攻击者恢复池状态,偿还闪电贷,并将剩余利润(约 $512K)转至 EOA 0xf96EB1...3b63b。

**结论**

缓解措施应将现货 slot0() 定价替换为抗操纵定价(足够长观察窗口的 TWAP,或 Chainlink 等外部预言机),然后再将流动性转换为可提取的 USDT。

**BCE Token Incident**

**简要概述**

2026年3月23日,BNB Chain 上 PancakeSwap 的 BCE-USDT 池因 BCE 代币的销毁机制缺陷被攻击,损失约 $679K。攻击者部署了两个恶意合约绕过 BCE 的买卖限制,并触发了针对流动性池储备的代币销毁,操纵池价格并抽取了池中的 USDT。

**漏洞分析**

漏洞源于 BCE 代币（[0xcdb189...999999](https://bscscan.com/address/0xcdb189d377ac1cf9d7b1d1a988f2025b99999999)）的销毁机制缺陷。核心问题在于：用户可影响的状态变量 scheduledDestruction 被用于直接从 PancakeSwap 交易对地址销毁代币,而非从用户自身余额中扣除。在卖出操作中,合约基于交易量和当前池储备将销毁金额累积到 scheduledDestruction 中,该值不从卖方余额扣除,而是之后通过单独的代码路径从交易对地址销毁代币并调用 sync()。

由于攻击者可控制交易量并操纵池储备,因此可以将 scheduledDestruction 设为任意值,触发销毁以压缩交易对的 BCE 储备,从而扭曲池价格。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqvkeVo4XiaZAn9WdfFFrBrpeyJHs0MSX56XAltqq2UIBzgicFoMJIVyGJ7OQ8...