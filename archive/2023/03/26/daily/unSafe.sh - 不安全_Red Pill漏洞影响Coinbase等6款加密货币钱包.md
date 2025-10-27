---
title: Red Pill漏洞影响Coinbase等6款加密货币钱包
url: https://buaq.net/go-155206.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:25.809251
---

# Red Pill漏洞影响Coinbase等6款加密货币钱包

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

![](https://8aqnet.cdn.bcebos.com/0e6a1de679f5541b236d43b0de267421.jpg)

Red Pill漏洞影响Coinbase等6款加密货币钱包

导语：​Coinbase等6款加密货币钱包
*2023-3-25 12:0:0
Author: [www.4hou.com(查看原文)](/jump-155206.htm)
阅读量:27
收藏*

---

导语：​Coinbase等6款加密货币钱包被爆'Red Pill'漏洞，攻击者可以绕过合约安全检测。

Coinbase等6款加密货币钱包被爆'Red Pill'漏洞，攻击者可以绕过合约安全检测。

Coinbase是全球领先的加密货币交易所，用户利用其提供的APP可以保存、管理数字资产，并与其他数字资产进行交互，比如比特币、以太坊、ERC-20 token。ZenGo安全研究人员发现Coinbase钱包和其他去中心化加密货币APP易受到red pill攻击。

**Red pill：攻击智能合约模拟**

Red pill攻击一种可以在交易模拟过程中隐藏恶意智能合约行为以绕过安全检测的方法，该攻击使得用户相信交易是安全的，然后允许该交易执行，交易执行后会发现智能合约会窃取用户加密货币资产。

Web3智能合约可以自动执行程序，允许开发者对网站和加密货币资产进行更大范围内的处理。比如，智能合约可以在用户支付后自动向支付用户发送NFT，根据交易自动向网站写入内容。任何可编程的内容都可以被智能合约自动执行。

同样地，攻击者也可以利用智能合约进行恶意目的，比如使用他们来窃取发送的加密货币或从钱包中窃取加密货币。这些恶意合约签名请求与合法请求很难区分，使得加密货币持有者面临巨大威胁。

为应对此类攻击，去中心化应用开发者引入了模拟交易解决方案来对在用户同意交易前对该交易进行模拟签名，然后预测签名后的结果。模拟的结果会展示给用户，用户可以看到签名后的结果，然后决定是否允许该交易继续执行。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679551847123555.png "1679551652993471.png")

图 交易执行的安全模拟

ZenGo安全研究人员指出，部分恶意执行合约可以检测到其是否被模拟，并展示出看似无害的行为，以绕过web3模拟安全检测。

攻击者可以在恶意合约中实现red pill以在被模拟时改变行为，而在用户同意该交易时窃取用户数字资产。具体实现上是由智能合约中的填充变量来完成的，即模拟时填入安全数据，而在真实执行时用恶意数据来替换。使得模拟时显示智能合约是安全的，而在真实执行时会窃取用户加密货币。

比如，“COINBASE”中包含当前区块矿工的地址。而在模拟时是没有真实的区块，因此也就没有矿工，部分模拟实现就会将其填充为全0地址。因此，恶意智能合约可以武器化“COINBASE” red pill：要求用户发送加密货币到合约，如果COINBASE为0的话，合约就会返回用户加密货币，因此在钱包模拟时对用户是安全的。但用户在链上真实发送交易时，COINBASE是当前矿工地址而非全0地址，因此合约就会窃取用户的加密货币。

PoC视频参见：https://youtu.be/Krp8qtVpGpQThe

在PoC模拟中可以看到，通过模拟可以发现用户如果同意该交易请求可以得到0 0.016 WETH（约30美元）。但用户同意该交易后，并未得到任何回报。

**漏洞（攻击）影响**

ZenGo安全研究人员进一步探索了red pill的攻击场景，发现有6款加密货币钱包dapp都受到该攻击的影响，包括Coinbase钱包、Rabby 钱包、Blowfish、PocketUniverse、Fire 扩展和另外一款尚未修复的扩展。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679551848380036.png "1679551624870115.png") 图 受影响的dAPP应用

截止目前，Coinbase钱包、Rabby 钱包、Blowfish、PocketUniverse和Fire 扩展都修复了该问题。

完整分析参见：https://zengo.com/zengo-uncovers-security-vulnerabilities-in-popular-web3-transaction-simulation-solutions-the-red-pill-attack/

本文翻译自：https://www.bleepingcomputer.com/news/security/coinbase-wallet-red-pill-flaw-allowed-attacks-to-evade-detection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?CIT5m34a)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/微信截图_20230324142907.png)

  Red Pill漏洞影响Coinbase等6款加密货币钱包](https://www.4hou.com/posts/pVr6)
* [![](https://img.4hou.com/images/57a0314b89156f341bbd624eff42b69d.jpg)

  CVE-2023-23397：Outlook漏洞PoC](https://www.4hou.com/posts/MBY3)
* [![](https://img.4hou.com/images/29c47a276430705ad01d018f4a601f63.jpg)

  CVE-2023-21716：Word远程代码执行漏洞PoC公布](https://www.4hou.com/posts/pVG2)
* [![](https://img.4hou.com/images/微信图片_20230310163647.jpg)

  记一次反序列化漏洞的利用之路](https://www.4hou.com/posts/XV3W)
* [![](https://img.4hou.com/images/微信截图_20230308092705.png)

  CVE-2022-25365在内的多个 Docker漏洞，通过攻击命名管道实现权限升级](https://www.4hou.com/posts/ZX3J)
* [![](https://img.4hou.com/images/微信截图_20230222101942.png)

  TouchEn nxKey键盘加密应用程序出现的许多漏洞很容易使其被黑化](https://www.4hou.com/posts/ZXPw)

![]()

文章来源: https://www.4hou.com/posts/pVr6
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)