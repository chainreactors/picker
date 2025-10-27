---
title: 黑客发起供应链攻击 向周下载量达20亿次的NPM包植入恶意软件
url: https://www.4hou.com/posts/42O6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-12
fetch_date: 2025-10-02T20:01:21.425570
---

# 黑客发起供应链攻击 向周下载量达20亿次的NPM包植入恶意软件

黑客发起供应链攻击 向周下载量达20亿次的NPM包植入恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客发起供应链攻击 向周下载量达20亿次的NPM包植入恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)44466

收藏

导语：此次钓鱼攻击与植入的恶意软件均表明，网页浏览器已成为窃取凭据、篡改流量及入侵网络的巨大攻击面。

在一场供应链攻击中，攻击者通过钓鱼攻击攻陷一名维护者的账户后，向周下载量合计超26亿次的多个NPM包植入了恶意软件。

此次供应链攻击中账户遭劫持的软件包维护者Josh Junon已于今日早些时候确认了该事件。他表示钓鱼邮件来自“support [at] npmjs [dot] help”邮箱——该邮箱对应的域名搭建了仿冒正规npmjs.com的网站。

钓鱼邮件中，攻击者以“2025年9月10日锁定账户”相威胁，通过恐吓手段诱使目标点击链接进入钓鱼网站。邮件内容称：“为维护您账户的安全与完整，请您尽快完成更新。请注意，自2025年9月10日起，使用过期2FA凭证的账户将被临时锁定，以防止未授权访问。”

![phishing-email.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250909/1757385781627581.jpg "1757385574701801.jpg")

网络钓鱼电子邮件

据收到钓鱼邮件的人士透露，攻击者使用相同邮件针对其他包维护者及开发者发起了攻击。安全研究人员发现，npmjs[.]help网站上包含一个登录表单，用户输入的凭据会被窃取并发送至以下URL：

https://websocket-api2[.]publicvm.com/images/jpg-to-png.php?name=[name]&pass=[password]

事件发现后，NPM团队已移除攻击者发布的部分恶意版本包，其中包括周下载量达3.576亿次的“debug”包。

**供应链攻击细节**

安全公司Aikido Security对此次攻击进行分析后指出，攻击者接管账户后对相关包进行了更新，在index.js文件中植入了基于浏览器的拦截型恶意代码。该代码可劫持网络流量与应用程序接口（API）。

恶意代码仅影响通过网页访问受感染应用的用户：它会监控加密货币地址及交易，将其重定向至攻击者控制的钱包地址，导致交易被攻击者劫持，而非发送至预期地址。

这款恶意软件的工作原理是：注入用户的网页浏览器后，监控以太坊、比特币、索拉纳、波场、莱特币及比特币现金的钱包地址与转账行为；一旦检测到包含加密货币交易的网络响应，便将收款地址替换为攻击者控制的地址，在交易签名前完成劫持。

Aikido表示，恶意代码通过挂钩（hooking）JavaScript函数实现上述操作，涉及fetch、XMLHttpRequest以及钱包API（如window.ethereum、Solana相关API等）。

截至目前，遭劫持的包及其周下载量如下：

**·**backslash：26万次

**·**chalk-template：390万次

**·**supports-hyperlinks：1920万次

**·**has-ansi：1210万次

**·**simple-swizzle：2626万次

**·**color-string：2748万次

**·**error-ex：4717万次

**·**color-name：1.9171亿次

**·**is-arrayish：7380万次

**·**slice-ansi：5980万次

**·**color-convert：1.935亿次

**·**wrap-ansi：1.9799亿次

**·**ansi-regex：2.4364亿次

**·**supports-color：2.871亿次

**·**strip-ansi：2.6117亿次

**·**chalk：2.9999亿次

**·**debug：3.576亿次

**·**ansi-styles：3.7141亿次

Aikido Security研究员表示：“这些软件包被更新后植入了一段代码，该代码会在网站客户端执行，暗中拦截浏览器中的加密货币及Web3活动，操纵钱包交互，并篡改支付目的地——使得资金与授权被重定向至攻击者控制的账户，而用户毫无察觉。”其危险性在于多层面运作：既修改网站显示内容，又篡改API调用，还操纵用户应用程序对签名内容的认知。

**攻击影响范围与背景**

尽管这是一场供应链攻击，但应用程序受影响需满足特定条件，大幅降低了攻击的实际影响。具体条件包括：

1. 在软件包遭篡改时段进行了全新安装；

2. 在此期间生成了package-lock.json文件；

3. 直接或间接依赖了受漏洞影响的包。

近几个月来，已有多起类似攻击针对知名JavaScript库的开发者。例如，7月时，周下载量超3000万次的“eslint-config-prettier”包遭攻陷；3月时，另有10个广泛使用的NPM库被劫持并改造成信息窃取工具。

此次钓鱼攻击与植入的恶意软件均表明，网页浏览器已成为窃取凭据、篡改流量及入侵网络的巨大攻击面。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-hijack-npm-packages-with-2-billion-weekly-downloads-in-supply-chain-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5ijkokFc)

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