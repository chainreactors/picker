---
title: LastPass 发现虚假支持中心试图窃取客户数据
url: https://www.4hou.com/posts/kg6Y
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-21
fetch_date: 2025-10-06T19:13:48.313151
---

# LastPass 发现虚假支持中心试图窃取客户数据

LastPass 发现虚假支持中心试图窃取客户数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# LastPass 发现虚假支持中心试图窃取客户数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-11-20 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)98330

收藏

导语：这些虚假的号码不仅会发布到 Chrome 扩展程序评论中，还会发布到允许任何人创建内容的网站上。

LastPass 发现，诈骗者正在为其 Chrome 扩展程序撰写评论，以宣传虚假的客户支持电话号码。

其实电话号码背后是更大的阴谋，旨在诱骗呼叫者让诈骗者可以远程访问他们的计算机。

LastPass 是一款流行的密码管理器，它利用 LastPass Chrome 扩展来生成、保存、管理和自动填充网站密码。威胁者试图通过使用虚假的 LastPass 客户支持号码留下 5 星级评论来瞄准该公司的大量用户群。

这些评论敦促遇到任何应用程序问题的用户拨打相关热线以联系 LastPass 在线客户服务，该服务与供应商无关。

![reviews.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730709056102681.png "1730708825145453.png")

Chrome 网上应用店中的欺诈性评论

相反，接听电话的骗子会冒充 LastPass 并将个人引导至“dghelp[.]top”网站，他们必须在其中输入代码才能下载远程支持程序。

![fake-lastpass-support-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730709057137828.png "1730708873118351.png")

虚假支持网站

拨打虚假支持号码的人会有人询问他们遇到的问题，然后询问他们是否试图通过计算机或移动设备访问 LastPass 以及他们使用的操作系统等一系列问题。然后，他们将被引导至 dghelp[.]top 网站，而威胁者仍保持在线状态，并试图让潜在受害者与该网站互动，从而暴露他们的数据。

研究人员发现，在此页面上输入代码将下载 ConnectWise ScreenConnect 代理 [VirusTotal]，该代理将使诈骗者能够完全访问某人的计算机。

![screenconnect-properties.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730709058413904.png "1730708954646909.png")

由 ConnectWise 签署的支持代理

从那里，一名威胁者可以让呼叫者继续提问。与此同时，另一个诈骗者利用ScreenConnect在后台安装其他程序进行无人值守的远程访问、窃取数据，或者窃取计算机中的数据。ScreenConnect 客户端将通过 molatorimax[.]icu 和 n9back366[.]stream 与攻击者控制的服务器建立连接。

在隐藏在 Cloudflare 后面之前，这两个网站之前都曾与乌克兰的 IP 地址相关联。提醒 LastPass 用户切勿与任何人（甚至合法的客户支持人员）共享其主密码，因为这将导致对 LastPass 保管库中存储的所有密码和数据的私人访问。

**与更大的诈骗活动相关**

与虚假 LastPass 支持中心相关的电话号码其实与一场规模大得多的活动有关。该电话号码 805-206-2892 也被发现被宣传为许多其他公司的支持号码，包括 Amazon、Adobe、Facebook、Hulu、YouTube TV、Peakcock TV、Verizon、Netflix、Roku、PayPal、Squarespace、Grammarly、 iCloud、Ticketmaster 和第一资本。

![extension-reviews.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730709059135773.png "1730709038205971.png")

作为 PayPal 和 iCloud 支持号码进行推广

这些虚假的支持号码不仅会发布到 Chrome 扩展程序评论中，还会发布到允许任何人创建内容的网站上，例如公司论坛和 Reddit。虽然其中许多帖子在创建后就被删除了，但其他帖子仍然可用，并且全天都会创建新帖子。

文章翻译自：https://www.bleepingcomputer.com/news/security/lastpass-warns-of-fake-support-centers-trying-to-steal-customer-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YsalNBXv)

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