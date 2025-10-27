---
title: 新型Android TapTrap攻击用不可见的UI对用户进行引导性欺骗
url: https://www.4hou.com/posts/pnp2
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-24
fetch_date: 2025-10-06T23:17:02.256379
---

# 新型Android TapTrap攻击用不可见的UI对用户进行引导性欺骗

新型Android TapTrap攻击用不可见的UI对用户进行引导性欺骗 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Android TapTrap攻击用不可见的UI对用户进行引导性欺骗

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-07-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)90058

收藏

导语：研究人员表示，除非用户在开发者选项或可访问性设置中禁用动画，否则最新的Android版本是可以启用动画的，否则会使设备暴露在TapTrap攻击之下。

一种新型的点击劫持技术可以利用用户界面动画绕过Android的权限系统，允许访问敏感数据或欺骗用户执行破坏性操作，例如清除设备。

与传统的基于覆盖的点击劫持不同，TapTrap攻击甚至可以在零权限应用程序上启动无害的透明活动，这种行为在Android 15和16中仍然没有得到缓解。

TapTrap是由维也纳工业大学和拜雷塔大学的安全研究团队开发的，并将在下个月的USENIX安全研讨会上展示。目前，该团队已经发表了一篇技术论文，概述了这次攻击，并建立了一个网站，总结了大部分细节。

**TapTrap如何工作**

TapTrap滥用Android用自定义动画处理活动转换的方式，在用户看到的和设备实际注册的内容之间造成视觉上的不匹配。

一个恶意应用程序在目标设备上安装后，使用‘startActivity()’和自定义低不透明度动画从另一个应用程序启动敏感的系统屏幕（权限提示、系统设置等）。

“TapTrap的关键是使用一种动画，使目标活动几乎不可见，”研究人员在一个解释攻击的网站上说。

这可以通过定义一个自定义动画来实现，将开始和结束的不透明度（alpha）设置为一个低值，比如0.01，从而使恶意或危险的活动几乎完全透明。可选的是，缩放动画可以用于缩放特定的UI元素（例如，权限按钮），使其占据整个屏幕，并增加用户点击它的机会。

![overview.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250709/1752043765576097.jpg "1752031476170734.jpg")

TapTrap概述

虽然启动的提示接收所有触摸事件，但用户看到的只是显示自己UI元素的底层应用，因为在它的顶部是用户实际参与的透明屏幕。

用户认为他们是在与应用程序互动，他们可能会点击屏幕上与危险操作相对应的特定位置，例如在几乎看不见的提示上点击“允许”或“授权”按钮。

**风险暴露**

为了检查TapTrap是否可以与Play Store（官方Android仓库）中的应用程序配合使用，研究人员分析了近100000个应用程序。他们发现76%的应用程序容易受到TapTrap攻击，因为它们包含满足以下条件的屏幕活动：

**·**可以由另一个应用程序启动

**·**在与调用应用程序相同的任务中运行

**·**不覆盖过渡动画

**·**在动画完成之前就对用户输入作出反应

研究人员表示，除非用户在开发者选项或可访问性设置中禁用动画，否则最新的Android版本是可以启用动画的，否则会使设备暴露在TapTrap攻击之下。

在开发攻击时，研究人员使用了当时最新的Android 15，但在Android 16发布后，他们也对其进行了一些测试。

Marco Squarcina表示，他们在运行Android 16的bb0 Pixel 8a上尝试了TapTrap，他们可以确认这个问题仍然没有得到缓解。

专注于隐私和安全的移动操作系统GrapheneOS也证实，最新的Android 16容易受到TapTrap技术的攻击，并宣布他们的下一个版本将包括修复程序。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-android-taptrap-attack-fools-users-with-invisible-ui-trick/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Nn8JEAUA)

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