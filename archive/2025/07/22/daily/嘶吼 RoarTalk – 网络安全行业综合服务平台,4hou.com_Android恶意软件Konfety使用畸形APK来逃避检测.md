---
title: Android恶意软件Konfety使用畸形APK来逃避检测
url: https://www.4hou.com/posts/LGOw
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-22
fetch_date: 2025-10-06T23:26:13.985844
---

# Android恶意软件Konfety使用畸形APK来逃避检测

Android恶意软件Konfety使用畸形APK来逃避检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Android恶意软件Konfety使用畸形APK来逃避检测

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-07-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105855

收藏

导语：Konfety自称是一款合法的应用程序，模仿谷歌Play上的无害产品，但没有任何承诺的功能。恶意软件的功能包括将用户重定向到恶意网站，推送不需要的应用程序安装，以及虚假的浏览器通知。

一种新的Konfety安卓恶意软件变种出现，带有畸形的ZIP结构和其他混淆方法，使其能够逃避分析和检测。

据悉，Konfety自称是一款合法的应用程序，模仿谷歌Play上的无害产品，但没有任何承诺的功能。恶意软件的功能包括将用户重定向到恶意网站，推送不需要的应用程序安装，以及虚假的浏览器通知。

相反，它使用CaramelAds SDK获取并呈现隐藏的广告，并泄露安装的应用程序、网络配置和系统信息等信息。

![redirects.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250716/1752648722762255.jpg "1752648362140249.jpg")

虽然Konfety不是间谍软件或RAT工具，但它在APK中包含一个加密的二级DEX文件，该文件在运行时被解密和加载，包含在AndroidManifest文件中声明的隐藏服务。这为动态安装额外的模块敞开了大门，从而允许在当前感染中提供更危险的功能。

**逃避策略**

移动安全平台Zimperium的研究人员发现并分析了最新的Konfety变种，报告称该恶意软件使用几种方法来混淆其真实性质和活动。

Konfety通过复制谷歌Play上可用的合法应用程序的名称和品牌，并通过第三方商店分发，从而诱骗受害者安装它——Human的研究人员将这种策略称为“诱饵双胞胎”。

恶意软件的运营商正在第三方应用商店中推广它。

这些市场通常是用户寻找“免费”的高级应用版本的地方，因为他们想避免被Google跟踪，或者他们的安卓设备不再受支持，或者他们无法使用Google服务。

动态代码加载（恶意逻辑隐藏在运行时加载的加密DEX文件中）是Konfety采用的另一种有效的混淆和逃避机制。

Konfety中另一个不常见的反分析策略是以一种混淆或破坏静态分析和逆向工程工具的方式操纵APK文件。

首先，APK将通用位标志设置为“0位”，表示文件已加密，即使它没有加密。当试图检查文件时，这会触发错误的密码提示，阻止或延迟对APK内容的访问。

其次，APK中的关键文件是使用BZIP压缩（0x000C）声明的，而APKTool和JADX等分析工具不支持这种压缩，从而导致解析失败。

![crash.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250716/1752648723195662.jpg "1752648439353632.jpg")

同时，Android忽略声明的方法，退回到默认处理以保持稳定性，允许恶意应用在设备上毫无问题地安装和运行。安装后，Konfety会隐藏其应用程序图标和名称，并使用地理围栏根据受害者所在地区改变行为。

在过去的Android恶意软件中也观察到基于压缩的混淆，正如卡巴斯基在2024年4月关于SoumniBot恶意软件的报告中所强调的那样。在这种情况下，SoumniBot在AndroidManifest.xml中声明了一个无效的压缩方法，声明了一个虚假的文件大小和数据覆盖，并用非常大的命名空间字符串混淆了分析工具。

通常建议人们避免安装第三方Android应用商店的APK文件，只信任你知道的发行商的软件。

文章翻译自：https://www.bleepingcomputer.com/news/security/android-malware-konfety-uses-malformed-apks-to-evade-detection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?v94kPZZV)

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