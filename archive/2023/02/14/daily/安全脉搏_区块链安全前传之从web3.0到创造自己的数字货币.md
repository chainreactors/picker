---
title: 区块链安全前传之从web3.0到创造自己的数字货币
url: https://www.secpulse.com/archives/195769.html
source: 安全脉搏
date: 2023-02-14
fetch_date: 2025-10-04T06:30:37.046594
---

# 区块链安全前传之从web3.0到创造自己的数字货币

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 区块链安全前传之从web3.0到创造自己的数字货币

[区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-13

18,652

互联网发展的三个阶段

### web1.0

静态页面，内容只能供用户去阅读，类似于在网络上读报纸或者看书。

### web2.0

动态互联网，实现用户之间的互动，比如等。

web2.0中厂商用免费或极低的成本吸引用户，通过获取到用户的信息来推流广告从而获得利润。

打个比方就是 厂商在一片地上种了很多草，吸引羊来吃，趁着羊吃草的功夫把羊身上的毛薅下来拿去卖钱，而羊自己并不在意这些毛，可以说是一种双向互利的方式。

### web3.0

web3.0是一个很模糊的概念，随着区块链技术的发展，基于区块链的web3.0诞生。

接着用上面的例子来说，随着web2.0的发展壮大，稀缺的不再是草，而是羊毛，也就是用户身上的数据。那么羊毛的重要性愈加突出，所以提出web3.0的概念，也就是拥有自己的一片空间，别人无论如何都无法修改，也就是将羊毛（数据）存放在了一个非常安全的地方中，相比于web2.0，不但实现了动态的交互，也实现了数据的“拥有”。

web3的概念非常模糊，可以说是一个大方向，按照我个人的理解可以说是在互联网创造了一个虚拟的世界，这个虚拟的世界拥有和现实世界一样的货币交易系统以及其他体系，能够自主维持运转的这样一个“虚拟生态系统”，而这个生态系统的生存法则就是“去中心化”。

**什么是去中心化？**

比如现在市面上的app都由一个厂家负责，厂商可以随意删除控制用户数据，形成了以厂商为中心的服务体系，去中心化就是没有中心厂商作为核心，而是所有用户形成一个能够自力更生的体系。

## 密码货币

随着web2.0发展，数字货币使用越来越多，而在区块链技术的支持下，数字货币也出现了全新的存在形式，去中心化的密码货币，世界上第一种密码货币就是比特币。像纸币有防伪印一样，密码货币通过密码学的散列计算出的hash值并且和智能合约进行绑定，密码货币基于去中心化的机制，与依赖中心监管体系的银行金融系统相对。之后出现的数种密码货币被创造，它们通常被称为altcoins。

## 区块链

程序员来讲讲什么是区块链 | 小白也能听懂的通俗解释 | 区块链原理 | 比特币 | 数字货币\_哔哩哔哩\_bilibili

**区块链的防篡改机制** 一个区块中储存了三样东西：数据，前一个区块的hash值，自身的hash值（由数据和前一区块的哈希值共同决定），如果要更改某一区块的内容，那么该区块（a区块）的hash值就会改变，下一区块（b区块）储存的a区块的hash值无法对应a区块当前哈希值，那么这两个区块间的链接就会断开。

如果想要篡改某一区块的数据，我们就要将这一区块以及后续所有区块的hash值进行重算，比如一条区块链里面有abcde五个区块，当我们篡改了b区块的数据，那么我们就要带着b区块的新hash值和c区块的数据重新计算出c区块的新hash值，然后再带着c区块的新hash值和d区块的数据重新计算d区块的新hash值，再带着d区块的新hash值和e区块的数据重新计算e区块的hash值…………………..其实在重新计算某一区块的hash值的过程也就相当于创造了一个新的区块，因此篡改一个区块以及后续区块所需的时间取决于创造一个区块所需要的时间。

这个看起来对算力要求似乎非常庞大，但是现代计算机其实是可以做到这一点的，如果我们有一台超大算力的计算机，那么是不是轻松就可以改变区块链的内容了？为了防止这种情况的出现，区块链加入了工作量证明机制（proof of work）简称 pow

我们用游戏举例说明一下pow，我们刚才说到用超大算力计算机来篡改区块链，这就好比你拿着满级神装在新手村乱杀，区块链是不允许这种情况出现的，因此它会上调怪物属性，也就是会增加创造一个区块所需的难度，使每一新区块被创造时都保持在十分钟左右（当然这个时间是可以更改的），因此即使是一台超高算力的计算机想要篡改一个区块所需的时间仍然是是

`创造一个区块的时间✖️n min`。

那我们所说的挖矿是什么呢？上面提到的情况是想要篡改区块中的数据，那么我没有恶意，我只是单纯的创造区块去给自己或者他人使用，这个创造区块的过程牺牲了我电脑的算力和一些其他资源，所以作为补偿，创建区块的人会得到密码货币的奖励，这就是我们所说的挖矿。

**区块链的点对点网络结构**

在传统的web服务中，传统的链接对象基本都是客户端和服务端，众多客户端访问一个服务端来进行交互，而在区块链的点对点网络结构（peer to peer）中，不再有客户端与服务端的概念，每一个节点间相互平等，并且包含完整的区块链数据存储，也就是说每一个节点中都储存了整个区块链网络中的所有信息，这样即使一个节点出现故障，其他所有节点也在帮他记录信息，这些记录了所有节点区块链的节点叫做全节点，当然也有只储存了自己信息的轻节点，比如区块链用来储存转账记录，那么每一节点都储存了所有节点之间的转账记录，每一节点储存的内容也是相同的，如果某一节点与其他节点出现差异，那么该节点或许就有被篡改过的可能了，但是被篡改几乎是不可能发生的，原因看下面。

点对点网络结构下的所有节点拥有判断区块是否被篡改的能力，当一个新区块想要加入某一节点的区块链时，该节点会向其他所有节点进行广播，所有的节点进行判断，如果50%以上的节点都认为该区块没有被篡改，那么这个区块就可以成功的加入区块链当中，反言之如果想要篡改某一区块的数据，你首先要将这一区块后的所有哈希重新计算，并且还要更改超过百分之五十节点的这一区块后的所有区块的哈希，那么就要拥有超过全网50%以上的算力才可以，这付出的代价是相当高的，这就是区块链网络系统的少数服从多数原则。

## DAPP

### **Dapp 是什么？**

APP (Application) 指的是手机里的应用程序，像是微信、微博、抖音…等都是日常生活中常会使用到的 App。

而 Dapp 的全名为去中心化应用程序（Decentralized Application），是建立在区块链系统网络上，所提供的服务都具有公开透明、不可篡改的特性。

以下是 Dapp 所具有的要素：

* • 代码开源：程序代码皆公开透明，任何人都可以查阅及审核，避免项目方说到没做到。
* • 分布式帐本：降低数据遗失的风险，且没有任何其他第三方有权能够窜改数据。
* • 数据所有权：除本人（私钥持有者）外，任何人皆无法动用该帐号的数据。

### **为什么 Dapp 会崛起?**

事实上，App 都是中心化的应用服务，用户所使用的数据都会存储在单一服务器系统里，代表公司能掌控用户的所有数据，但相关问题也随之浮出水面。

### **数据所有权归属问题**

用户在 App 上的个人资料、搜索浏览纪录等信息都会存储在中心化系统的服务器里，这也意味着软件公司能够借由这些数据来营利。

也导致像是微博、抖音等企业，能透过搜集的用户数据来投放广告，并借此获利。等于企业能用你的信息来赚钱，但你却分不到任何好处，甚至还可能受到影响（例如被疯狂投放广告、或个人资料被平台外泄）。

另外，传统手游的游戏道具、帐号数据也都属于公司所有，一旦宣布停止营运，这些资产也会随着官方服务器关闭而消失。

但在 Dapp 中，你的游戏道具、帐号都会以 NFT 形式储存在链上，因此只要区块链不倒，你就能持续拥有这些资产。换句话说，Dapp 能够让数据的所有权回归到用户身上。额外提醒，虽然你仍拥有这些资产，但可能会因为游戏已经关闭，导致这些资产的现值趋近于零，你能保有的仍以回忆居多。

### **过度中心化**

App 是由中心化服务器来进行管理，因此企业有时可以专断独行，但用户却没有任何反制的手段：例如可以随意植入广告，或是删除用户的内容、帐号。

而 Dapp 的数据都存在区块链上，因此项目方没办法任意删除用户资料，目前也没有任何广告植入的问题（但不确定未来是否会有项目开始植入广告）。

由于上述几点原因，也让许多人开始对传统的 App 感到不满，于是就有人打算通过区块链“去中心化”的特性来研发能解决上述问题的 App，于是 Dapp 就此诞生。

不过同时也要注意，不是每个 Dapp 都一定符合公开、去中心化的规范，例如 Opensea 就能下架用户的 NFT 和限制用户登陆。

### **Dapp 与 App 的差异**

App 的应用服务是使用中心化服务器，代表软件公司必须要承担存储用户的数据量的营运成本，否则将无法持续地运行。

例如抖音服务器的成本就百万以上，因此必须想办法创造各种营收管道来支持各项支出，像是通过大数据将广告推广到潜在用户面前，借此吸引更多广告商进驻。

而 Dapp 是建立在区块链上，用户在链上进行交易、换币等行为时，是需要自行负担手续费（Gas 费）的，也就代表开发商的运营成本会比传统 App 来得更低（不过有些开发商为了吸引用户，会帮用户负担使用时的手续费）。

|  | Dapp | App |
| --- | --- | --- |
| 服务器 | 去中心化 | 中心化 |
| 隐私性 | 有（区块链匿名性） | 无（还可能被外泄） |
| 营运成本 | 用户共同负担（或开发商负担） | 开发商负担 |
| 平台获利来源 | 智能合约（链上手续费） | 广告商或用户消费 |
| 数据所有权 | 用户 | 开发商 |
| 平台控制权 | 开发商或是 DAO 治理 | 开发商 |
| 系统 | 区块链 | Android、iOS |
| 代码是否开源 | 代码皆公开，可供人参考 | 代码为公司机密，擅用者可能会吃上官司 |

## 智能合约

智能合约，是一段写在区块链上的代码，一旦某个事件触发合约中的条款，代码即自动执行。也就是说，满足条件就执行，不需要人为操控，类似于传统web的后端代码。

# 简单区块链实现

我们用Javascript来手写一个建议的区块链出来，其实和写一个链表很像：

```
const sha256 = require('crypto-js/sha256')
Date = new Date()

class block{
    constructor(data,time,previousHash) {
        this.data = data
        this.time = time
        this.previousHash = previousHash
        this.myHash = this.currHash()
    }
    currHash() {
        return sha256(this.data + this.time + this.previousHash).toString()
    }
}

class blockCahin{
    constructor()
    {
        this.chain = [this.createBlockchain()];
    }
    createBlockchain()
    {
        return new block("Genesisblock",Date.toLocaleString(),0o0000000)
    }
    getLatestblock()
    {
        return this.chain[this.chain.length - 1]
    }
    addBlock(newBlock)
    {
        newBlock.previousHash = this.getLatestblock().myHash
        newBlock.myHash = newBlock.currHash()
        this.chain.push(newBlock)
    }
}

BlockChain = new blockCahin()
BlockChain.addBlock(new block("this is a test",Date.toLocaleDateString(),"anything"))
console.log(BlockChain)
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195769-1676258587.png)

接下来我们用代码实现一下简易的POW：

```
const sha256 = require("crypto-js/sha256")
function proofOfwork(){
    let seed = "y1zh3e7"
    let x = 1               // x为自增变量
    while (true){
        if(sha256(seed + x).toString().substring(0,4) != "0000") // 定义难度，比如我现在要求通过不断自增x去计算seed+x的哈希值
        {                                    ...