---
title: Web3常见钓鱼方式分析与安全防范建议
url: https://www.freebuf.com/articles/web/401745.html
source: FreeBuf网络安全行业门户
date: 2024-05-25
fetch_date: 2025-10-06T17:17:48.271254
---

# Web3常见钓鱼方式分析与安全防范建议

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Web3常见钓鱼方式分析与安全防范建议

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

Web3常见钓鱼方式分析与安全防范建议

2024-05-24 09:47:36

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

Web3钓鱼是一种针对Web3用户的常见攻击手段，通过各种方式窃取用户的授权、签名，或诱导用户进行误操作，目的是盗窃用户钱包中的加密资产。

近年来，Web3钓鱼事件不断出现，且发展出钓鱼即服务的黑色产业链（Drainer as a Service, DaaS）,安全形势严峻。

本文中，SharkTeam将对常见的Web3钓鱼方式进行系统分析并给出安全防范建议，供大家参考，希望能帮助用户更好的识别钓鱼骗局，保护自身的加密资产安全。

## ****一、常见钓鱼手法分析****

### ****1. Permit链下签名钓鱼****

Permit是针对ERC-20标准下授权的一个扩展功能，简单来说就是你可以签名批准其他地址来挪动你的Token。其原理是你通过签名的方式表示被授权的地址可以通过这个签名来使用你的代币，然后被授权的地址拿着你的签名进行链上permit交互后就获取了调用授权并可以转走你的资产。Permit链下签名钓鱼通常分为三步：

（1）攻击者伪造钓鱼链接或钓鱼网站，诱导用户通过钱包进行签名（无合约交互，不上链）。![20240523171919611image.png](https://image.3001.net/images/20240524/1716515257_664ff1b9167bae8033f38.png!small)

签名对象：DAI/USDC/WETH等ERC20代币（这里是DAI）

holder://签名地址

spender://钓鱼者地址

nonce:0

expiry:1988064000 //过期时间

allowed:true

如果签名了，钓鱼者就从受害者这边获得了用于盗出DAI/USDC/WETH等ERC20代币（这里是DAI）的签名（一段r, s, v 值，钓鱼者与permit函数交互时需要用到）。

（2）攻击者调用permit函数，完成授权。![20240523171926463image.png](https://image.3001.net/images/20240524/1716515258_664ff1bac4e04290f177b.png!small)![20240523171931077image.png](https://image.3001.net/images/20240524/1716515259_664ff1bbca168fb14d3fb.png!small)

<https://etherscan.io/tx/0x1fe75ad73f19cc4c3b658889dae552bb90cf5cef402789d256ff7c3e091bb662>

（3）攻击者调用transferFrom函数，将受害者资产转出，完成攻击。

在这里先说明一下transfer和transferFrom的区别，当我们直接进行ERC20转账的时候，通常是调用ERC20合约中的transfer函数，而transferFrom通常是在授权第三方将我们钱包内的ERC20转移给其他地址时使用。![20240523171938437image.png](https://image.3001.net/images/20240524/1716515260_664ff1bcd884631f27830.png!small)

<https://etherscan.io/tx/0x9c02340896e238fc667c1d84fec78af99b1642c986fe3a81602903af498eb938>

补充说明：这种签名是一个无Gas的链下签名，攻击者拿到后会执行permit和transferFrom链上交互，所以在受害人地址的链上记录中看不到授权记录，在攻击者地址中可以看到。一般来说这种签名是一次性的，不会重复或持续产生钓鱼风险。

### ****2. Permit2链下签名钓鱼****

Permit2是Uniswap为了方便用户使用，在2022年底推出的一个智能合约，它是一个代币审批合约，允许代币授权在不同的DApp中共享和管理，未来随着越来越多的项目与Permit2 集成，Permit2合约可以在DApp生态系统中实现更加统一的授权管理体验，并且节约用户交易成本。

Permit2出现之前，在Uniswap上进行代币兑换需要先授权（Approve）再兑换（Swap），需要操作两次，也需要花费两笔交易的Gas费。在Permit2推出后，用户一次性把额度全部授权给Uniswap的Permit2合约，之后的每次兑换只需要进行链下签名即可。

Permit2虽然提高了用户的体验，但随之而来是针对Permit2签名的钓鱼攻击。和Permit链下签名钓鱼类似，Permit2也是链下签名钓鱼，此种攻击主要分为四步：

（1）前提条件是用户的钱包在被钓鱼之前已使用过Uniswap并将代币额度授权给了Uniswap的Permit2合约（Permit2默认会让用户授权该代币的全部余额的额度）。![20240523171945515image.png](https://image.3001.net/images/20240524/1716515261_664ff1bddcf29877683bc.png!small)![20240523171950446image.png](https://image.3001.net/images/20240524/1716515262_664ff1bed0726769d2428.png!small)

<https://etherscan.io/tx/0xd8f0333b9e0db7175c38c37e490379bde5c83a916bdaa2b9d46ee6bff4412e8f>

（2）攻击者伪造钓鱼链接或钓鱼页面，诱导用户进行签名，钓鱼攻击者获取所需的签名信息，和Permit链下签名钓鱼类似。![20240523171955025image.png](https://image.3001.net/images/20240524/1716515266_664ff1c2c22f502b1eb49.png!small)

（3）攻击者调用Permit2合约的permit函数，完成授权。![20240523172002755image.png](https://image.3001.net/images/20240524/1716515268_664ff1c41bf81c6297bdb.png!small)

<https://etherscan.io/tx/0xd8c3f55dfbc8b368134e6236b296563f506827bd5dc4d6c0df39851fd219d658>

（4）攻击者调用Permit2合约的transferFrom函数，将受害者资产转出，完成攻击。![20240523172009400image.png](https://image.3001.net/images/20240524/1716515269_664ff1c5172dd40e5f9db.png!small)

<https://etherscan.io/tx/0xf6461e003a55f8ecbe919a47b3c0dc6d0f068e48a941658329e35dc703138486>

补充说明：这里攻击者接收资产的地址通常有多个，通常其中一个金额最大的接收者是实施钓鱼的攻击者，另外的则是提供钓鱼即服务的黑产地址（钓鱼即服务DaaS的供应商地址，例如PinkDrainer、InfernoDrainer、AngelDrainer等）。

### ****3. eth\_sign 链上盲签钓鱼****

eth\_sign是一种开放式签名方法，可以对任意哈希进行签名，攻击者只需构造出任意恶意需签名数据（如：代币转账，合约调用、获取授权等）并诱导用户通过 eth\_sign 进行签名即可完成攻击。

MetaMask在进行eth\_sign签名时会有风险提示，imToken、OneKey等Web3钱包均已禁用此函数或提供风险提示，建议所有钱包厂商禁用此方法，防止用户因缺乏安全意识或必要的技术积累被攻击。![20240523172017558image.png](https://image.3001.net/images/20240524/1716515270_664ff1c6a636f1bcd4b20.png!small)![20240523172021360image.png](https://image.3001.net/images/20240524/1716515271_664ff1c7c433f785f27d6.png!small)

### ****4. personal\_sign/signTypedData 链上签名钓鱼****

![20240523172031020image.png](https://image.3001.net/images/20240524/1716515272_664ff1c8d0e24cb5cf10b.png!small)personal\_sign、signTypedData是常用的签名方式，通常用户需要仔细核对发起者、域名、签名内容等是否安全，如果是有风险的，要格外警惕。![20240523172036421image.png](https://image.3001.net/images/20240524/1716515274_664ff1ca06dc79d2e06de.png!small)

此外，如果像上面这种情况personal\_sign、signTypedData被用成“盲签”，用户看不到明文，容易被钓鱼团伙利用，也会增加钓鱼风险。

### ****5. 授权钓鱼****

攻击者通过伪造恶意网站，或者在项目官网上挂马，诱导用户对setApprovalForAll、Approve、Increase Approval、Increase Allowance等操作进行确认，获取用户的资产操作授权并实施盗窃。

****（1）setApprovalForAll****

以PREMINT挂马钓鱼事件为例，项目方网站上的一个js文件（https://s3-redwood-labs.premint.xyz/theme/js/boomerang.min.js）被注入了恶意代码，执行后会动态创建注入恶意js文件（https://s3-redwood-labs-premint-xyz.com/cdn.min.js?v=1658050292559）。攻击由这个恶意脚本发起。![20240523172044473image.png](https://image.3001.net/images/20240524/1716515275_664ff1cb0422d8ef50208.png!small)![20240523172048507image.png](https://image.3001.net/images/20240524/1716515276_664ff1cc10aee54e15a3e.png!small)

用户因未及时发现风险，对setApprovalForAll操作进行了确认，无意间泄漏了对资产的操作授权，导致资产被盗。![20240523172057857image.png](https://image.3001.net/images/20240524/1716515278_664ff1ce2242f783da0ea.png!small)

****（2）Approve****

与setApprovalForAll类似，用户对Approve操作进行了确认，泄漏了对资产的操作授权，导致资产被盗。

Approve误授权：

<https://etherscan.io/tx/0x4b0655a5b75a9c078653939101fffc1d08ff7e5c89b0695ca6db5998214353fa>

![20240523172107079image.png](https://image.3001.net/images/20240524/1716515279_664ff1cf1a4420fdaa496.png!small)攻击者通过transferFrom转移资产：

<https://etherscan.io/tx/0x0dedf25777ff5483bf71e70e031aacbaf50124f7ebb6804beb17aee2c15c33e8>

![20240523172119092image.png](https://image.3001.net/images/20240524/1716515280_664ff1d0a1d4f4cba48dd.png!small)Increase Approval和Increase Allowance函数攻击原理也与此类似，默认状态下攻击者对受害者地址代币的操作上限额度为0，但经过这两个函数的授权之后，攻击者提高了对受害者代币的操作上限，随后就能将该额度的代币转移。

****（3）Increase Approval****

Increase Approval误授权：

<https://etherscan.io/tx/0x7ae694080e2ad007fd6fa25f9a22ca0bbbff4358b9bc84cc0a5ba7872118a223>

![20240523172127537image.png](https://image.3001.net/images/20240524/1716515281_664ff1d1d528bda09de09.png!small)攻击者通过transferFrom转移资产：

<https://etherscan.io/tx/0x15bc5516ed7490041904f1a4c594c33740060e0f0271cb89fe9ed43c974a7a69>

****![20240523172136463image.png](https://image.3001.net/images/20240524/1716515282_664ff1d2e8f0112a38874.png!small)（4）Increase Allowance****

Increase Allowance误授权：

<https://etherscan.io/tx/0xbb4fe89c03d8321c5bfed612fb76f0756ac7e99c1efaf7c4d99d99f850d4de53>

![20240523172142435image.png](https://image.3001.net/images/20240524/1716515283_664ff1d3efb20bdc45caa.png!small)攻击者通过transferFrom转移资产：

[https://etherscan.io/tx/0xb91d7b1440745aa07409be36666bc291ecc661e424b21b855698d488949b920f![20240523172151571image.png](https://image.3001.net/images/20240524/1716515285_664ff1d57856549b86f72.png!small)](https://etherscan.io/tx/0xb91d7b1440745aa07409be36666bc291ecc661e424b21b855698d488949b920f)

### ****6. 地址污染钓鱼****

地址污染钓鱼也是近期猖獗的钓鱼手段之一，攻击者监控链上交易，之后根据目标用户历史交易中的对手地址进行恶意地址伪造，通常前4～6位和后4～6位与正确的对手方地址方相同，然后用这些恶意伪造地址向目标用户地址进行小额转账或无价值代币转账。

如果目标用户在后续交易中，因个人习惯从历史交易订单中复制对手地址进行转账，则极有可能因为大意将资产误转到恶意地址上。

2024年5月3日就因为此地址污染钓鱼手法被钓鱼1155WBTC，价值超过7千万美元。

正确地址：0xd9A1b0B1e1aE382DbDc898Ea68012FfcB2853a91

恶意地址：0xd9A1C3788D81257612E2581A6ea0aDa244853a91

正常交易：

<https:/...