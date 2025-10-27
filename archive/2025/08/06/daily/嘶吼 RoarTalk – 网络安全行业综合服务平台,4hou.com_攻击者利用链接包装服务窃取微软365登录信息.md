---
title: 攻击者利用链接包装服务窃取微软365登录信息
url: https://www.4hou.com/posts/ZgBJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-06
fetch_date: 2025-10-07T00:17:55.814115
---

# 攻击者利用链接包装服务窃取微软365登录信息

攻击者利用链接包装服务窃取微软365登录信息 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者利用链接包装服务窃取微软365登录信息

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-05 11:14:49

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)63090

收藏

导语：滥用合法服务来传递恶意有效负载并不是什么新鲜事，但利用链接包装安全特性是网络钓鱼领域的最新发展。

一个威胁者一直在滥用科技公司的链接包装服务来掩盖恶意链接，这些链接会导致微软365网络钓鱼页面收集登录凭证。

从6月到7月，攻击者利用了网络安全公司Proofpoint和云通信公司Intermedia的URL安全功能。一些电子邮件安全服务包括链接包装功能，该功能将邮件中的url重写为受信任的域，并通过一个扫描服务器进行扫描，以阻止恶意目标。

**使网络钓鱼网址合法化**

Cloudflare的电子邮件安全团队发现，攻击者在入侵Proofpoint和intermedia保护的电子邮件帐户后，将恶意url合法化，并可能利用他们未经授权的访问来分发“清洗”的链接。

研究人员发现，攻击者以各种方式滥用Proofpoint链接包装，包括通过受损帐户使用URL缩短器进行多层重定向滥用。

攻击者添加了一个混淆层，在从受保护的账户发送恶意链接之前，首先缩短恶意链接，然后自动包装链接。攻击者用虚假的语音邮件通知或共享的微软团队文件来引诱受害者。在重定向链的末端是一个收集凭据的Microsoft Office 365钓鱼页面。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250804/1754291628193085.png "1754291345452665.png")

利用链接包装功能分发的微软365钓鱼邮件

在滥用Intermedia服务的活动中，威胁者发送电子邮件，假装是“Zix”安全消息通知，以查看安全文档，或冒充微软团队通知新消息。

据称指向该文件的链接是一个由Intermedia服务包装的URL，并被重定向到一个假页面，该页面来自数字和电子邮件营销平台Constant Contact，该平台托管了该钓鱼页面。点击虚假Teams通知中的回复按钮，就会进入一个收集登录凭证的微软网络钓鱼页面。

Cloudflare的研究人员表示，通过用合法的电子邮件保护url来伪装恶意目的地，威胁者增加了成功攻击的几率。需要注意的是，滥用合法服务来传递恶意有效负载并不是什么新鲜事，但利用链接包装安全特性是网络钓鱼领域的最新发展。

文章翻译自：https://www.bleepingcomputer.com/news/security/attackers-exploit-link-wrapping-services-to-steal-microsoft-365-logins/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?TTe7cBE3)

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