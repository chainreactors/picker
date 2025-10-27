---
title: 欧洲航天局官方网上商店遭黑客攻击
url: https://www.4hou.com/posts/9jXY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-28
fetch_date: 2025-10-06T19:37:01.345159
---

# 欧洲航天局官方网上商店遭黑客攻击

欧洲航天局官方网上商店遭黑客攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 欧洲航天局官方网上商店遭黑客攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-12-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)106050

收藏

导语：网店不再提供虚假的 Stripe 支付页面，但恶意脚本仍然在该网站的源代码中可见。

本周，欧洲航天局 (ESA) 官方网上商店遭到黑客攻击，该商店出现一段 JavaScript 代码，该代码在结账时会生成虚假的 Stripe 支付页面。

欧洲航天局的预算超过 100 亿欧元，主要通过培训宇航员、建造火箭和卫星来探索宇宙的奥秘，从而扩大太空活动的极限。获得销售欧空局商品许可的网络商店目前无法使用，并显示“暂时无法使用”。

该恶意脚本本周出现在该机构的网站上，并收集客户信息，包括在购买最后阶段提供的支付卡数据。电子商务安全公司 Sansec 注意到了该恶意脚本，并提醒该商店似乎与 ESA 系统集成，可能会给该机构员工带来风险。

![Sansec_ESA_store.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241227/1735266841118682.png "1735201984181287.png")

Sansec 表示 ESA 商店遭到入侵

Sansec 发现用于泄露信息的域名与销售 ESA 商品的合法商店使用的域名相同，但具有不同的顶级域名 (TLD)。虽然欧洲机构的官方商店在 .com TLD 中使用“esaspaceshop”，但黑客在 .pics TLD 中使用相同的名称（即 esaspaceshop[.]pics），如 ESA 商店的源代码所示：

![MageCart_script_ESA.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241227/1735266844157684.png "1735202039397822.png")

ESA 网络商店中注入恶意 JavaScript

该脚本包含来自 Stripe SDK 的模糊 HTML 代码，当客户尝试完成购买时，该代码会加载虚假的 Stripe 支付页面。值得注意的是，假冒的 Stripe 页面看起来并不可疑，特别是当看到它是由 ESA 官方网上商店提供时。

![FakeStripe_ESA.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241227/1735266845190498.png "1735202085473862.png")

ESA 的网上商店加载虚假的 Stripe 支付页面

有网络应用安全公司也证实了 Sansec 的调查结果，并捕获了 ESA 官方网络商店上加载的虚假 Stripe 支付页面，目前该网店不再提供虚假的 Stripe 支付页面，但恶意脚本仍然在该网站的源代码中可见。

欧空局表示，该商店并未托管在其基础设施上，也不管理其上的数据，因为该机构不管理这些数据，它不拥有这些数据。这可以通过简单的 whois 查找来确认，该查找显示了 ESA 域名 (esa.int) 及其网络商店的完整详细信息，其中联系数据经过编辑以保护隐私。

文章翻译自：https://www.bleepingcomputer.com/news/security/european-space-agencys-official-store-hacked-to-steal-payment-cards/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?sc9y73BK)

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