---
title: Red Pill漏洞影响Coinbase等6款加密货币钱包
url: https://www.4hou.com/posts/pVr6
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-26
fetch_date: 2025-10-04T10:42:28.768803
---

# Red Pill漏洞影响Coinbase等6款加密货币钱包

Red Pill漏洞影响Coinbase等6款加密货币钱包 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Red Pill漏洞影响Coinbase等6款加密货币钱包

ang010ela
[漏洞](https://www.4hou.com/category/vulnerable)
2023-03-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)207908

收藏

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

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679551848380036.png "1679551624870115.png")

截止目前，Coinbase钱包、Rabby 钱包、Blowfish、PocketUniverse和Fire 扩展都修复了该问题。

完整分析参见：https://zengo.com/zengo-uncovers-security-vulnerabilities-in-popular-web3-transaction-simulation-solutions-the-red-pill-attack/

本文翻译自：https://www.bleepingcomputer.com/news/security/coinbase-wallet-red-pill-flaw-allowed-attacks-to-evade-detection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iJ8OMh1v)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/e7OO)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)