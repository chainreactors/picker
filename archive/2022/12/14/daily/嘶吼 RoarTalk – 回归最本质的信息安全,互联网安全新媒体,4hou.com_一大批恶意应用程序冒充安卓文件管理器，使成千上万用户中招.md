---
title: 一大批恶意应用程序冒充安卓文件管理器，使成千上万用户中招
url: https://www.4hou.com/posts/O9BE
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-14
fetch_date: 2025-10-04T01:22:54.574846
---

# 一大批恶意应用程序冒充安卓文件管理器，使成千上万用户中招

一大批恶意应用程序冒充安卓文件管理器，使成千上万用户中招 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 一大批恶意应用程序冒充安卓文件管理器，使成千上万用户中招

布加迪
[新闻](https://www.4hou.com/category/news)
2022-12-13 11:50:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)159150

收藏

导语：一批新的恶意安卓应用程序冒充无害的文件管理器，渗入到了官方的Google Play应用程序商店中，用Sharkbot银行木马感染众多用户。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669341253174967.png "1669341253174967.png")

一批新的恶意安卓应用程序冒充无害的文件管理器，渗入到了官方的Google Play应用程序商店中，用Sharkbot银行木马感染众多用户。

这些应用程序在安装时并不携带恶意攻击载荷，以便在Google Play上提交时躲避检测，而是之后从远程资源获取攻击载荷。

由于这批木马应用程序是文件管理器，请求危险的权限以加载Sharkbot恶意软件时，不太可能引起怀疑。

**虚假的文件管理器感染安卓**

Sharkbot是一种危险的恶意软件，通过在银行应用程序的合法登录提示中显示虚假的登录表单，企图窃取网上银行账户。当用户试图使用这些虚假表单登录银行时，登录信息就被窃取，并发送给威胁分子。

这种恶意软件一直在进化，以种种形式出现在Play Store上，或者从木马应用程序加载。

在安全公司比特梵德的一份新报告中，分析师们发现了新的安卓木马应用程序伪装成文件管理器，并向谷歌报告了这些木马应用程序。所有这些恶意应用程序此后已从Google Play Store中删除。

然而，许多以前下载了木马应用程序的用户可能仍然在手机上装有它们，或者仍然遭受未被发现的残留恶意软件感染。

第一个恶意应用程序是Victor Soft Ice LLC开发的“X-File Manager”，在谷歌最终将其删除之前，它通过Google Play已被下载了10000次。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669341267241303.png "1669341267241303.png")

图1. Google Play上的X-File Manager（来源：比特梵德）

这款应用程序执行反模拟检查以逃避检测，并只会在英国或意大利的SIM卡中加载Sharkbot，所以它是一起针对性的攻击活动的一部分。

被该恶意软件盯上的移动银行应用程序列表如下所示，不过比特梵德特别指出，威胁分子可以随时远程更新这份列表。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669341279556548.png "1669341279556548.png")

图2. 被这起Sharkbot活动盯上的银行（来源：比特梵德）

比特梵德的遥测数据表明了这起活动的攻击范围很窄，因为这起Sharkbot攻击浪潮的大多数受害者都在英国，其次是在意大利、伊朗和德国。

恶意应用程序请求用户授予有风险的权限，比如读写外部存储、安装新软件包、访问帐户详细信息和删除软件包（以清除痕迹）等。

然而，这些权限在文件管理应用程序中看起来很正常，也属意料之中，因此用户不太可能谨慎地对待请求。

Sharkbot作为虚假的程序更新被获取，X-File Manager在安装前提示用户批准。

第二个安装银行木马的恶意应用程序是Julia Soft Io LLC开发的“FileVoyager”，通过Google Play下载了5000次。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221125/1669341294513933.png "1669341294513933.png")

图3. Google Play上的FileVoyager（来源：比特梵德）

FileVoyager具有与X-File Manager相同的运作模式，针对意大利和英国的同一批金融机构。

比特梵德发现的另一个Sharkbot加载应用程序是LiteCleaner M，该应用程序在被发觉、从Play Store下架之前已累计下载了1000次。

目前，该应用程序只通过APKSOS等第三方应用程序商店才能获得。同一个第三方应用程序商店上有第四个名为“Phone AID, Cleaner, Booster 2.6”的Sharkbot加载程序。

如果安装了这些应用程序，安卓用户应该立即删除它们，并更改他们使用的任何网上银行账户的密码。

由于威胁分子直接从Google Play分发这些应用程序，保护自己的最佳方法是启用Play Protect服务，以便在检测到恶意应用程序后删除它们。

此外，安卓移动安全杀毒应用程序将有助于检测恶意流量和应用程序，甚至在它们被报告到Google Play之前就能检测出来。

本文翻译自：https://www.bleepingcomputer.com/news/security/android-file-manager-apps-infect-thousands-with-sharkbot-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?K6lphAQn)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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