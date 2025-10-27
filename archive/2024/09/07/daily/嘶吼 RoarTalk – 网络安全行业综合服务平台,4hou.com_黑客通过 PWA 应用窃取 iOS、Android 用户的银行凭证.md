---
title: 黑客通过 PWA 应用窃取 iOS、Android 用户的银行凭证
url: https://www.4hou.com/posts/8g3o
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-07
fetch_date: 2025-10-06T18:20:38.984320
---

# 黑客通过 PWA 应用窃取 iOS、Android 用户的银行凭证

黑客通过 PWA 应用窃取 iOS、Android 用户的银行凭证 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客通过 PWA 应用窃取 iOS、Android 用户的银行凭证

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)84920

收藏

导语：渐进式 Web 应用程序 (PWA) 是跨平台应用程序，可以直接从浏览器安装，并通过推送通知、访问设备硬件和后台数据同步等功能提供类似原生的体验。

近期，安全研究人员发现威胁者开始使用渐进式 Web 应用程序冒充银行应用程序并窃取 Android 和 iOS 用户的凭据。

渐进式 Web 应用程序 (PWA) 是跨平台应用程序，可以直接从浏览器安装，并通过推送通知、访问设备硬件和后台数据同步等功能提供类似原生的体验。

在网络钓鱼活动中使用此类应用程序可以逃避检测，绕过应用程序安装限制，并获得设备上危险权限的访问权限，而无需向用户提供可能引起怀疑的标准提示。

该技术于 2023 年 7 月在波兰首次被发现，而同年 11 月发起的后续活动则针对捷克用户。

网络安全公司 ESET 报告称，它目前正在追踪两个依赖这种技术的不同活动，一个针对匈牙利金融机构 OTP Bank，另一个针对格鲁吉亚的 TBC Bank。

然而，这两起攻击活动似乎是由不同的威胁分子发起的。其中一个组织使用不同的命令和控制 (C2) 基础设施来接收被盗凭证，而另一个组织则通过 Telegram 记录被盗数据。

**感染链**

ESET 表示，这些活动依靠多种方法来接触目标受众，包括自动呼叫、短信（短信网络钓鱼）以及 Facebook 广告活动中精心制作的恶意广告。

在前两种情况下，网络犯罪分子会用虚假消息诱骗用户，称他们的银行应用程序已过时，出于安全原因需要安装最新版本，并提供下载钓鱼 PWA 的 URL。

![infection-flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240822/1724298344157911.png "1724298098149114.png")

PWA 活动感染流程

在社交媒体上发布恶意广告的情况下，威胁分子使用冒充的银行官方吉祥物来诱导合法感，并宣传限时优惠，例如安装所谓关键应用更新即可获得金钱奖励。

![malvertisment.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240822/1724298346160692.png "1724298134889241.png")

网络钓鱼活动中使用的恶意广告之一

根据设备（通过 User-Agent HTTP 标头验证），点击广告会将受害者带到虚假的 Google Play 或 App Store 页面。

![googleplay.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240822/1724298348161389.png "1724298179122953.png")

虚假的 Google Play 安装提示（左）和进度（右）

点击“安装”按钮会提示用户安装一个伪装成银行应用程序的恶意 PWA。在某些情况下，在 Android 上，恶意应用程序以 WebAPK（由 Chrome 浏览器生成的原生 APK）的形式安装。

网络钓鱼应用程序使用官方银行应用程序的标识符（例如，看似合法的登录屏幕徽标），甚至将 Google Play Store 声明为该应用程序的软件来源。

![webapk.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240822/1724298349135470.png "1724298223159642.png")

恶意 WebAPK（左）和钓鱼登录页面（右）

**在移动设备上使用 PWA 的吸引力**

PWAs 旨在跨多个平台运行，因此攻击者可以通过单一网络钓鱼活动和有效载荷瞄准更广泛的受众。

不过，其主要好处在于可以绕过谷歌和苹果对官方应用商店之外的应用安装限制，以及可能提醒受害者注意潜在风险的“从未知来源安装”警告提示。

PWAs 可以紧密模仿原生应用的外观和感觉，尤其是在 WebAPK 的情况下，图标上的浏览器徽标和应用内的浏览器界面都是隐藏的，因此几乎不可能将其与合法应用程序区分开来。

![paw.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240822/1724298350209029.png "1724298305573345.png")

PWA（左）和合法应用程序（右）

WebAPK 难以区分，因为它们的图标中没有 Chrome 徽标。这些 Web 应用可以通过浏览器 API 访问各种设备系统，例如地理位置、摄像头和麦克风，而无需从移动操作系统的权限屏幕请求这些权限。

最终，攻击者可以在无需用户交互的情况下更新或修改 PWA，从而允许动态调整网络钓鱼活动以获得更大的成功。

滥用 PWAs 进行网络钓鱼是一种危险的新兴趋势，随着越来越多的网络犯罪分子意识到其潜力和优势，这种趋势可能会发展到新的程度。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-steal-banking-creds-from-ios-android-users-via-pwa-apps/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?wpmQNKuI)

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