---
title: Blockchain-dark-forest-selfguard-handbook/README_CN.md at main · slowmist/Blockchain-dark-forest-selfguard-handbook
url: https://buaq.net/go-150228.html
source: unSafe.sh - 不安全
date: 2023-02-21
fetch_date: 2025-10-04T07:35:04.306667
---

# Blockchain-dark-forest-selfguard-handbook/README_CN.md at main · slowmist/Blockchain-dark-forest-selfguard-handbook

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/46dba412b22ab399e67964bded728cd4.jpg)

Blockchain-dark-forest-selfguard-handbook/README\_CN.md at main · slowmist/Blockchain-dark-forest-selfguard-handbook

*2023-2-20 22:49:24
Author: [github.com(查看原文)](/jump-150228.htm)
阅读量:37
收藏*

---

区块链黑暗森林自救手册

🔥Website: <https://darkhandbook.io/>
🇺🇸English：[Blockchain dark forest selfguard handbook](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README.md)
🇯🇵日本語版：[ブロックチェーンのダークフォレストにおける自己防衛のためのハンドブック](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README_JP.md)

Blockchain dark forest selfguard handbook
*Master these, master the security of your cryptocurrency.*

作者：余弦@慢雾安全团队
联系我：Twitter([@evilcos](https://twitter.com/evilcos))、即刻(@余弦.jpg)

[![alt this](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/raw/main/res/this.png)](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/res/this.png)

| 日期 | 更新日志 |
| --- | --- |
| 2023/01/07 | 我在我的个人 GitHub 做扩展阅读更新：<https://github.com/evilcos/darkhandbook> |
| 2022/06/14 | V1 [日文版](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README_JP.md)出现，感谢翻译者们。 |
| 2022/05/17 | V1 [英文版](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README.md)出现，一点小修正，感谢翻译者们。 |
| 2022/04/15 | V1 出现，仅仅修正了点错别字，一些不错的建议，我将在之后的小版本里加入，感谢:) |
| 2022/04/12 | V1 Beta 出现，中文，用碎片时间断断续续写了三周😀 |

*注：选择 GitHub 方便协同及看到历史更新记录。你可以 Watch、Fork 及 Star，当然我更希望你能参与贡献:)*

⚓**目录**

* [引子](#%E5%BC%95%E5%AD%90)
* [一张图](#%E4%B8%80%E5%BC%A0%E5%9B%BE)
  + [创建钱包](#%E5%88%9B%E5%BB%BA%E9%92%B1%E5%8C%85)
    - [Download](#download)
    - [Mnemonic Phrase](#mnemonic-phrase)
    - [Keyless](#keyless)
  + [备份钱包](#%E5%A4%87%E4%BB%BD%E9%92%B1%E5%8C%85)
    - [助记词/私钥类型](#%E5%8A%A9%E8%AE%B0%E8%AF%8D%E7%A7%81%E9%92%A5%E7%B1%BB%E5%9E%8B)
    - [Encryption](#encryption)
  + [使用钱包](#%E4%BD%BF%E7%94%A8%E9%92%B1%E5%8C%85)
    - [AML](#aml)
    - [Cold Wallet](#cold-wallet)
    - [Hot Wallet](#hot-wallet)
    - [DeFi 安全到底是什么](#defi-%E5%AE%89%E5%85%A8%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88)
    - [NFT 安全](#nft-%E5%AE%89%E5%85%A8)
    - [小心签名！](#%E5%B0%8F%E5%BF%83%E7%AD%BE%E5%90%8D)
    - [小心反常识签名！](#%E5%B0%8F%E5%BF%83%E5%8F%8D%E5%B8%B8%E8%AF%86%E7%AD%BE%E5%90%8D)
    - [一些高级攻击方式](#%E4%B8%80%E4%BA%9B%E9%AB%98%E7%BA%A7%E6%94%BB%E5%87%BB%E6%96%B9%E5%BC%8F)
  + [传统隐私保护](#%E4%BC%A0%E7%BB%9F%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4)
    - [操作系统](#%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F)
    - [手机](#%E6%89%8B%E6%9C%BA)
    - [网络](#%E7%BD%91%E7%BB%9C)
    - [浏览器](#%E6%B5%8F%E8%A7%88%E5%99%A8)
    - [密码管理器](#%E5%AF%86%E7%A0%81%E7%AE%A1%E7%90%86%E5%99%A8)
    - [双因素认证](#%E5%8F%8C%E5%9B%A0%E7%B4%A0%E8%AE%A4%E8%AF%81)
    - [科学上网](#%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91)
    - [邮箱](#%E9%82%AE%E7%AE%B1)
    - [SIM 卡](#sim-%E5%8D%A1)
    - [GPG](#gpg)
    - [隔离环境](#%E9%9A%94%E7%A6%BB%E7%8E%AF%E5%A2%83)
  + [人性安全](#%E4%BA%BA%E6%80%A7%E5%AE%89%E5%85%A8)
    - [Telegram](#telegram)
    - [Discord](#discord)
    - [来自“官方”的钓鱼](#%E6%9D%A5%E8%87%AA%E5%AE%98%E6%96%B9%E7%9A%84%E9%92%93%E9%B1%BC)
    - [Web3 隐私问题](#web3-%E9%9A%90%E7%A7%81%E9%97%AE%E9%A2%98)
* [区块链作恶方式](#%E5%8C%BA%E5%9D%97%E9%93%BE%E4%BD%9C%E6%81%B6%E6%96%B9%E5%BC%8F)
* [被盗了怎么办](#%E8%A2%AB%E7%9B%97%E4%BA%86%E6%80%8E%E4%B9%88%E5%8A%9E)
  + [止损第一](#%E6%AD%A2%E6%8D%9F%E7%AC%AC%E4%B8%80)
  + [保护好现场](#%E4%BF%9D%E6%8A%A4%E5%A5%BD%E7%8E%B0%E5%9C%BA)
  + [分析原因](#%E5%88%86%E6%9E%90%E5%8E%9F%E5%9B%A0)
  + [追踪溯源](#%E8%BF%BD%E8%B8%AA%E6%BA%AF%E6%BA%90)
  + [结案](#%E7%BB%93%E6%A1%88)
* [误区](#%E8%AF%AF%E5%8C%BA)
  + [Code Is Law](#code-is-law)
  + [Not Your Keys, Not Your Coins](#not-your-keys-not-your-coins)
  + [In Blockchain We Trust](#in-blockchain-we-trust)
  + [密码学安全就是安全](#%E5%AF%86%E7%A0%81%E5%AD%A6%E5%AE%89%E5%85%A8%E5%B0%B1%E6%98%AF%E5%AE%89%E5%85%A8)
  + [被黑很丢人](#%E8%A2%AB%E9%BB%91%E5%BE%88%E4%B8%A2%E4%BA%BA)
  + [立即更新](#%E7%AB%8B%E5%8D%B3%E6%9B%B4%E6%96%B0)
* [总结](#%E6%80%BB%E7%BB%93)
* [附](#%E9%99%84)
  + [安全法则及原则](#%E5%AE%89%E5%85%A8%E6%B3%95%E5%88%99%E5%8F%8A%E5%8E%9F%E5%88%99)
  + [贡献者](#%E8%B4%A1%E7%8C%AE%E8%80%85)
  + [那些官网](#%E9%82%A3%E4%BA%9B%E5%AE%98%E7%BD%91)

首先，需要先恭喜你的是：你看到了这本手册。我不清楚你是谁，但如果你持有加密货币或对这个世界有兴趣，未来可能会持有加密货币，那么这本手册值得你反复阅读并谨慎实践。

其次，需要有心理准备的是：本手册的阅读需要一定的知识背景，我尽量照顾初学者，但很难。我希望初学者不必恐惧这些知识壁垒，因为其中大量是可以“玩”出来的。如果你遇到不懂的知识点，需要扩展了解的话，建议你用好 Google。并强烈建议你掌握一个安全原则：网络上的知识，凡事都参考至少两个来源的信息，彼此佐证，始终保持怀疑。

是的，始终保持怀疑！包括本手册提到的任何知识点:)

区块链是个伟大的发明，它带来了某些生产关系的变革，让“信任”这种宝贵的东西得以部分解决。这已经很难得了，不需要中心化、不需要第三方角色，有些“信任”基于区块链就可以得到很好解决，不可篡改、按约定执行、防止抵赖。但，现实是残酷的，人们对区块链的理解会存在许多误区。这些误区导致了坏人轻易钻了空子，频繁将黑手伸进了人们的钱包，造成了大量的资金损失。这早已是黑暗森林。

在区块链黑暗森林世界里，首先牢记下面这两大安全法则：

1. 零信任。简单来说就是保持怀疑，而且是始终保持怀疑。
2. 持续验证。你要相信，你就必须有能力去验证你怀疑的点，并把这种能力养成习惯。

*注：本手册中，安全法则就这两大，其他都可以认为是这两大推论出来的安全原则。*

好，引子部分就到这。下面我们从一张图开始，进入到这个黑暗森林，看看我们都会遇到哪些风险及我们应该如何应对。

[![](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/raw/main/res/web3_hacking_map.jpg)](https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/res/web3_hacking_map.jpg)

在仔细看后文之前，你可以先粗略过下这张图。这张图是你在这个世界（无论你如何称呼这个世界，区块链、加密货币还是 Web3 都行）里关键活动有关的内容，从流程上包括三大部分：创建钱包、备份钱包及使用钱包。

我们顺着这三大流程，将涉及到的每个关键点展开分析。

## 创建钱包

钱包最最最核心的就是那个私钥（或助记词）。

私钥长这样：

> 0xa164d4767469de4faf09793ceea07d5a2f5d3cef7f6a9658916c581829ff5584

助记词长这样：

> cruel weekend spike point innocent dizzy alien use evoke shed adjust wrong

*注：用以太坊举例，关于私钥/助记词的基础知识请自行扩展。*

私钥即身份，如果私钥丢了或被盗了，那么这个身份也就不是你的了。钱包应用其实很多，知名的也不少，我并不打算也不可能一一介绍。不过该手册确实会提到一些具体的钱包，请注意，能被提到的必然是我有基本信任的，但我不担保你在使用过程中可能出现的安全问题或目标钱包可能出现并不在我预期内的安全风险（后文我不会再不断去废话这些，引子里提到的两大安全法则希望你牢记心中）。

钱包从应用分类来说主要包括几种：PC 钱包、浏览器扩展钱包、移动端钱包、硬件钱包及网页钱包等。从触网与否来说主要可以分为冷钱包和热钱包。当我们要进入这个世界，首先要思考将拥有的钱包的用途，用途决定了你将用哪个钱包，同时用途也决定了你会如何对待这个钱包。

无论你选择什么钱包，但至少有一点可以肯定的：在这个世界玩久了后，你不可能只有一个钱包。

于是这里我们又需要记住一个安全原则：做好隔离，也就是鸡蛋不要放在一个篮子里。一般来说使用越频繁的钱包，自然也加大了出问题的风险。时刻牢记：面对一个新事物时，先准备个单独的钱包，用单独的小资金去玩一段时间。除非你已经如我这般，经历无数，对许多事物都了然于心。但，常在河边走，哪有不湿鞋呢？

### Download

单这么简单的一点，其实也不简单，原因：

1. 许多人（真是许多人）找不到正确的官网，正确的应用市场，于是安装了假钱包。
2. 许多许多人对下载了的应用不知道如何确认是否被篡改过。

于是，出师未捷身先死。还没来得及进入这个世界，就已经钱包空空了。

针对上面的第 1 点，找到正确的官网是有技巧的，比如：

* Google
* 行业知名收录，如 CoinMarketCap
* 多问一些比较信任的人

好，上面这几点得到的信息可以全部结合起来参考，互相佐证，最终真相只有一个:)恭喜你，找到了正确的官网。

接着，你要下载安装应用了，**如果是 PC 钱包**，根据官网提供的下载链接，下载后需要自己去安装。但在安装之前，建议做下是否篡改的校验工作，虽然这个做法并无法防止源头就被完全篡改的情况（比如官方自己内部作恶、内部被黑、官网被入侵替换了相关信息等等），但可以防止如：源头被部分篡改、被中间人劫持篡改等这些情况。

是否篡改的校验，实际上就是文件一致性校验。常见的方式有两种：

* 一种是哈希校验，比如 MD5、SHA256 等，MD5 绝大多数情况下够用，但存在被哈希碰撞的极小风险，所以业内一般选择 SHA256，够用且够安全。
* 另一种是 GPG 签名校验，这个其实也很流行，强烈建议掌握 GPG 工具、命令、方法，虽然对于新人来说有那么些费力，但上手后，相信我，你会很快乐的。

话虽至此，其实业内这样做的项目方并不多，所以一旦遇到，真是难能可贵，弥足珍惜，比如一款比特币钱包 Sparrow Wallet，下载页面的“Verifying the Release”简直良心了，提到的两种方式都有清晰指南，可以直接参考学习：

> <https://sparrowwallet.com/download/>

这个页面提到的 GPG 工具有两个：

* GPG Suite，macOS 下运行的。
* Gpg4win，Windows 下运行的。

如果你细心观察，你会发现这两个 GPG 工具的下载相关页面其实都有给出两种方法的一致性校验说明，但不好意思的是，并没手把手教你如何校验。估计吧，都是认为你会是聪明人，该补上的知识你已经补上了:)

**如果是浏览器扩展钱包**，比如这世界家喻户晓的 MetaMask，你唯一有机会注意的就是目标扩展下载页面里的用户数多不多、评分情况如何，比如 MetaMask 在 Chrome 网上应用店里，用户数可是超过一千万的，同时有两千多用户评分的，虽然最终评分并不高。有人要说这不可以刷出来吗？这位朋友，是这样的，刷，我相信，不过刷的量如此之巨大，当各方是傻子呢。

**如果是移动端钱包**，判断方式类似扩展钱包，不过需要注意的是，iPhone 的 App Store 是分区的，加密货币在中国大陆被驱赶得不行，所以如果你用 App Store 中国区账号下载到了钱包，建议只有一个：别用，换成如美区的 App Store 账号下载吧。另外，通过正确的官网也能引导到正确的下载位置（比如全球知名的 imToken、Trust Wallet 等，官网安全一定要做好，官网都被黑了，那这安全责任就真大了）。

**如果是硬件钱包**，简单来说，可以从官网源头的引导下购买，不要直接去在线商城，到手后也需要留意是否存在被异动手脚的情况，当然有些针对硬件包装的异动是很高明的，不一定都能看得出。此时建议：无论如何，使用时，先连续至少三次从头开始的创建，记录下生成的助记词、相关钱包地址，不会重复就行。

**如果是网页钱包**，非常不建议使用这种在线的钱包，除非你不得已，那么识别好是官方的后，速战速决吧，千万别有任何感情依赖。

### Mnemonic Phrase

一般来说，我们创建了钱包后，直接打交道的关键信息是助记词（而不是私钥），毕竟助记词是方便人类记忆的。助记词是有标准约定的（如
BIP39），这就对助记词提了要求，比如一般 12 个英文单词，也可以是其他数量（3 的倍数），不过不会超过 24 个单词，要不然太复杂也就不助记了，数量少于 12 的话，安全性也...