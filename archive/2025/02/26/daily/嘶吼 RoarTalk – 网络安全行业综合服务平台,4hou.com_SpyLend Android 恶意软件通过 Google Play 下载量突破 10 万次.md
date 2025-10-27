---
title: SpyLend Android 恶意软件通过 Google Play 下载量突破 10 万次
url: https://www.4hou.com/posts/LGDD
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-26
fetch_date: 2025-10-06T20:33:24.860352
---

# SpyLend Android 恶意软件通过 Google Play 下载量突破 10 万次

SpyLend Android 恶意软件通过 Google Play 下载量突破 10 万次 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# SpyLend Android 恶意软件通过 Google Play 下载量突破 10 万次

山卡拉
[新闻](https://www.4hou.com/category/news)
2025-02-25 10:32:27

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)83636

收藏

导语：​一款名为 SpyLend 的 Android 恶意软件应用程序已在 Google Play 上被下载超过 10 万次。

一款名为 SpyLend 的 Android 恶意软件应用程序已在 Google Play 上被下载超过 10 万次。该应用伪装成一款金融工具，但实际上是一个针对印度用户的掠夺性贷款应用程序。

该应用程序属于名为 SpyLoan 的恶意 Android 应用程序组，这些应用伪装成合法的金融工具或贷款服务，实际上却窃取设备数据用于掠夺性贷款。这些应用通常承诺提供快速简便的贷款，只需很少的文档，并提供诱人的条款，以此吸引用户。然而，在安装时，它们会请求过多的权限，从而窃取用户的个人数据，包括联系人、通话记录、短信、照片和设备位置等信息。

这些收集到的数据随后被用来骚扰、敲诈和勒索用户，尤其是当用户未能满足应用程序的还款条款时。

**贷款诈骗和敲诈勒索**

网络安全公司 CYFIRMA 发现了一款名为 Finance Simplified 的 Android 应用，该应用自称是一款财务管理工具，在 Google Play 上的下载量已达 10 万次。然而，CYFIRMA 表示，该应用在某些国家（如印度）表现出更多的恶意行为，会窃取用户设备的数据用于掠夺性贷款。研究人员还发现了其他恶意 APK，这些 APK 似乎是同一恶意软件活动的变种，包括 KreditApple、PokketMe 和 StashFur。

尽管该应用现已被从 Google Play 中移除，但它可能仍在后台运行，继续从受感染的设备中收集敏感信息。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250225/1740450720190146.png "1740450635200534.png")

Google Play 上 Finance Simplified 的多条用户评论显示，该应用提供的贷款服务会向未支付高额利息的借款人进行勒索。一位用户评论称：“这款应用程序非常糟糕，他们提供的贷款金额很低，然后勒索要求高额还款，否则就会把照片编辑成裸照进行威胁。”

这些应用程序还声称自己是注册的非银行金融公司（NBFC），但 CYFIRMA 表示这并不属实。

为了逃避 Google Play 的检测，Finance Simplified 加载了一个 WebView，将用户重定向到外部网站，然后从该网站下载托管在 Amazon EC2 服务器上的贷款应用 APK。

CYFIRMA 解释道：“Finance Simplified 应用程序似乎专门针对印度用户，它通过显示和推荐贷款申请、加载显示贷款服务的 WebView 来重定向到外部网站，然后在该网站下载单独的贷款 APK 文件。”

研究人员发现，只有当用户位于印度时，该应用程序才会加载欺骗性界面，这表明该活动具有特定的目标。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250225/1740450722801347.png "1740450658298758.png")

**应用程序窃取敏感数据**

该恶意软件活动更令人担忧的方面是其数据收集行为，其中包括存储在用户设备上的敏感个人信息。以下是该恶意软件窃取的数据摘要：

* **·** 联系人、通话记录、短信和设备详细信息。
* **·** 来自内部和外部存储的照片、视频和文档。
* **·** 实时位置跟踪（每 3 秒更新一次）、历史位置数据和 IP 地址。
* **·** 最后 20 个复制到剪贴板的文本条目。
* **·** 贷款历史和银行短信交易信息。

虽然这些数据主要用于敲诈那些错误申请贷款的受害者，但也可能被用于金融欺诈或转售给网络犯罪分子以牟利。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250225/1740450724168075.png "1740450689203537.png")

**应对措施**

如果您怀疑您的设备被任何上述应用程序或类似应用程序感染，请立即删除它们，重置权限，更改银行账户密码，并执行设备扫描。

本文翻译自：https://www.bleepingcomputer.com/news/security/spylend-android-malware-downloaded-100-000-times-from-google-play/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?JX2kL5D3)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

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

[查看更多](https://www.4hou.com/member/azxO)

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