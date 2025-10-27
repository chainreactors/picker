---
title: XRP库xrpl.js 遭黑客攻击，导致钱包被盗
url: https://www.4hou.com/posts/mkg9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-28
fetch_date: 2025-10-06T22:04:22.830191
---

# XRP库xrpl.js 遭黑客攻击，导致钱包被盗

XRP库xrpl.js 遭黑客攻击，导致钱包被盗 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# XRP库xrpl.js 遭黑客攻击，导致钱包被盗

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)77696

收藏

导语：恶意代码似乎是由与Ripple组织相关的开发人员帐户添加的，可能是通过受损的凭证添加的。恶意提交没有出现在公共GitHub存储库中，这表明攻击可能发生在NPM发布过程中。

近期，Ripple推荐加密货币NPM JavaScript库名为“xrpl.js”，被入侵窃取Ripple钱包种子和私钥，并将其转移到攻击者控制的服务器上，允许威胁者窃取存储在钱包中的所有资金。

恶意代码被添加到xrpl NPM包的2.14.2、4.2.1、4.2.2、4.2.3和4.2.4版本中，并于下午时间4:46到5:49之间发布到NPM注册表中。这些被破坏的版本已经被删除，现在有一个干净的4.2.5版本，所有用户都应该立即升级到这个版本。

xrpl.js库由Ripple币账本基金会（XRPLF）维护，是Ripple币通过JavaScript与Ripple币区块链交互的推荐库。它支持钱包操作、XRP转账和其他分类账功能。由于它是与XRP区块链交互的推荐库，它已经被广泛采用，在过去的一周内下载量超过14万次。

NPM库通过可疑方法进行了修改，名为CheckValitysofdeed将附加到折衷版本中的“

```
/src/index.ts
```

”文件的末尾进行了修改。此功能接受字符串作为参数，然后通过http Post请求转发给https：// 0x9c [。] xyz/xcm，威胁者可以在其中收集它。该代码试图通过使用“ AD-REFFERAL”用户代理使其看起来像网络流量监视系统的广告请求，从而试图变得隐秘。

![xrpl-compromise.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745402755127401.png "1745402608211521.png")

恶意代码插入到xrpl.js NPM库中

根据开发安全公司Aikido的说法，checkValidityOfSeed（）函数在各种函数中被调用，用于窃取XRP钱包的种子、私钥和助记符。

![calling-checkvalidityofseed-function.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745402756912654.png "1745402647214463.png")

通过checkValidityOfSeed函数窃取数据

威胁者可以利用这些信息在自己的设备上导入被盗的XRP钱包，以提取其中的任何资金。

目前已经确定，受感染的版本是在不同时间上传的，总共有452次下载。虽然总下载量并不大，但这个库可能被用来管理和连接更多的XRP钱包。

恶意代码似乎是由与Ripple组织相关的开发人员帐户添加的，可能是通过受损的凭证添加的。恶意提交没有出现在公共GitHub存储库中，这表明攻击可能发生在NPM发布过程中。

如果用户使用其中一个版本，请立即停止并旋转与受影响系统的任何私钥或秘密。XRP Ledger支持钥匙旋转：https：//xrpl.org/docs/tutorials/how-tos/how-tos/manage-manage-acccount-account-settings/assign-a-a-a-regular-regular-key-pair-，如果任何帐户的主密钥可能被妥协，则应将其禁用：https：//xrpl.org/docs/tutorials/how-tos/manage-manage-account-settings/disable-master-key-pair。”

开发人员称，XRP账本代码库或GitHub存储库没有受到影响。“澄清一下：这个漏洞存在于xrpl.js中，这是一个用于与XRP账本交互的JavaScript库。它不会影响XRP账本代码库或Github存储库本身。使用xrpl.js的项目应该立即升级到v4.2.5，”XRP账本基金会在X上发布。

开发商还证实，Xaman钱包、XRPScan、First Ledger和Gen3 Games项目没有受到供应链攻击的影响。这种供应链攻击类似于之前以太坊和索拉纳npm用于窃取钱包种子和私钥的攻击。

文章翻译自：https://www.bleepingcomputer.com/news/security/ripples-recommended-xrp-library-xrpljs-hacked-to-steal-wallets/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?wJiHxa3C)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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