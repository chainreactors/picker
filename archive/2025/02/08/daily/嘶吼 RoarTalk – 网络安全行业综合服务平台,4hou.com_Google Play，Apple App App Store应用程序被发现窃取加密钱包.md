---
title: Google Play，Apple App App Store应用程序被发现窃取加密钱包
url: https://www.4hou.com/posts/Dxxk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-08
fetch_date: 2025-10-06T20:34:18.254722
---

# Google Play，Apple App App Store应用程序被发现窃取加密钱包

Google Play，Apple App App Store应用程序被发现窃取加密钱包 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Google Play，Apple App App Store应用程序被发现窃取加密钱包

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-02-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)64655

收藏

导语：如果用户在设备上安装了这些应用程序中的任何一个，建议立即卸载它们。

Google Play商店和Apple App Store上的Android和iOS应用程序包含一个恶意软件开发套件（SDK），旨在使用OCR偷窃器窃取加密货币钱包恢复短语。该活动被称为“ SparkCat”，其名称（“ Spark”）是受感染应用程序中恶意SDK组件之一的名称（“ Spark”）。

根据Kaspersky的说法，仅在Google Play上，下载数字就可以公开使用，被感染的应用程序下载了242,000次。

Kaspersky解释说：“我们发现Android和iOS应用程序具有恶意的SDK/框架，这些应用程序嵌入了窃取加密货币钱包恢复短语，其中一些可以在Google Play和App Store上找到。”

从Google Play下载了被感染的应用程序超过242,000次。这是在App Store中找到偷窃器的第一个已知案例。

**Spark SDK窃取用户的加密货币**

被感染的Android应用程序上的恶意SDK利用了称为“ Spark”的恶意Java组件，该组件伪装成分析模块。

它使用GitLab上存储的加密配置文件，该文件提供命令和操作更新。在iOS平台上，该框架具有不同的名称，例如“ gzip”，“ googleappsdk”或“ stat”。另外，它使用一个称为“ IM\_NET\_SYS”的基于锈的网络模块来处理与命令和控制（C2）服务器的通信。

该模块使用Google ML Kit OCR从设备上的图像中提取文本，试图找到可用于在攻击者设备上加载加密货币钱包的恢复短语，而无需知道密码。

它（恶意组件）会根据系统的语言加载不同的OCR模型，以区分图片中的拉丁语，韩语和日本角色。然后，SDK沿路径 / API / E / D / U将有关设备的信息上传到命令服务器，并在响应中接收一个调节恶意软件后续操作的对象。

![SparkCat_08.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250205/1738726485713738.png "1738726394113673.png")

用于连接到命令和控制服务器的URL

该恶意软件通过使用不同语言的特定关键字来搜索包含秘密的图像，而这些关键字是每个区域（欧洲，亚洲等）的变化。虽然某些应用程序显示针对区域，但它们在指定地理区域之外工作的可能性也不能排除在外。

**受感染的应用程序**

据发现，有18个受感染的Android和10个iOS应用程序，其中许多应用程序在各自的应用商店中仍然可用。 Android Chatai应用程序是由卡巴斯基感染的一个应用程序，该应用程序安装了超过50,000次。该应用已不再在Google Play上可用。

![app.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250205/1738726488190044.png "1738726466513217.png")

在Google Play上下载的50000个应用程序

如果用户在设备上安装了这些应用程序中的任何一个，建议立即卸载它们，并使用移动防病毒工具扫描任何残留物。除此之外，用户最好还应考虑重置。

文章翻译自：https://www.bleepingcomputer.com/news/mobile/google-play-apple-app-store-apps-caught-stealing-crypto-wallets/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2kmH5tIX)

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