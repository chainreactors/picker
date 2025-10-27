---
title: WordPress广告欺诈插件每天产生14亿个广告请求
url: https://www.4hou.com/posts/l0Ng
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-29
fetch_date: 2025-10-06T22:04:33.224087
---

# WordPress广告欺诈插件每天产生14亿个广告请求

WordPress广告欺诈插件每天产生14亿个广告请求 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# WordPress广告欺诈插件每天产生14亿个广告请求

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)91977

收藏

导语：Scallywag是一个围绕四个WordPress插件建立的欺诈即服务运营，帮助网络罪犯从高风险和低质量的网站中赚钱。

最新发现，一个名为“Scallywag”的大规模广告欺诈操作，通过精心制作的WordPress插件，每天产生数十亿的欺诈请求，从盗版和URL缩短网站中获利。

Scallywag是由机器人和欺诈检测公司HUMAN发现的，该公司绘制了一个由407个域名组成的网络，支持该操作，最高时每天有14亿个欺诈性广告请求。

HUMAN阻止和报告Scallywag流量的行为导致其减少了95%，尽管威胁者通过轮换域名和转向其他货币化模式显示出了弹性。

**围绕WordPress广告欺诈插件构建**

由于法律风险、品牌安全问题、广告欺诈和缺乏高质量的内容，合法的广告提供商会避免盗版和网址缩短网站。

Scallywag是一个围绕四个WordPress插件建立的欺诈即服务运营，帮助网络罪犯从高风险和低质量的网站中赚钱。

该操作创建的WordPress插件是Soralink（2016年发布），Yu Idea（2017年），WPSafeLink（2020年）和Droplink（2022年）。

Human表示，多个独立的威胁者购买并使用这些WordPress插件来建立自己的广告欺诈计划，有些人甚至在YouTube上发布教程，详细说明如何做到这一点。

这些扩展降低了潜在威胁者的进入门槛，他们想要从通常无法通过广告获利的内容中获利；事实上，一些威胁者已经发布了视频来指导其他人建立自己的计划。

Droplink是这种销售模式的唯一例外，因为它可以通过为卖家执行各种赚钱步骤而免费获得。

访问盗版目录网站查找电影或高级软件的用户点击嵌入的url缩短链接，并通过该操作的现金支付基础设施被重定向。

不能直接投放广告的盗版目录网站不一定是由Scallywag运营的。相反，它们的运营商与广告欺诈者结成了“灰色伙伴关系”，将盈利外包出去。

![pirate-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745398040553067.png "1745397272833221.png")

盗版网站（左）链接到Scallywag网站（右）

重定向过程将访问者带过中间的大量广告页面，这些页面会给Scallywag运营商带来欺诈性印象，并最终进入一个包含承诺内容（软件或电影）的页面。

中间站点是运行Scallywag插件的WordPress站点。这些处理重定向逻辑，广告加载，验证码，计时器和隐形机制，它显示一个干净的博客在广告平台检查。

![diagram.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745398041617760.png "1745397306106789.png")

Scallywag的操作概述

**破坏Scallywag**

HUMAN通过分析其合作伙伴网络中的流量模式来检测Scallywag活动，例如来自看似良性的WordPress博客的高广告印象量，伪装行为，以及在重定向之前强制等待时间或CAPTCHA交互。

![cloaking.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745398043962640.png "1745397409310489.png")

直接访问（左）和通过url缩短器访问（右）的同一站点

随后，它将Scallywag列为欺诈网络，与广告提供商合作，停止对广告请求的竞标，并削减了Scallywag的收入来源。

作为回应，Scallywag的参与者试图通过使用新的现金支付域名和打开重定向链来隐藏真正的推荐者来逃避检测，但HUMAN表示他们也检测并阻止了这些。

![block.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745398044140615.png "1745397570937144.png")

Scallywag请求随时间的推移

结果，Scallywag的每日广告欺诈流量从14亿急剧下降到几乎为零，许多分支机构放弃了这种方法，转而采用其他骗局。

尽管Scallywag生态系统在经济上已经崩溃，但它的运营商很可能会继续试图逃避缓解措施，重新盈利。

文章翻译自：https://www.bleepingcomputer.com/news/security/scallywag-ad-fraud-operation-generated-14-billion-ad-requests-per-day/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?28r14Qnj)

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