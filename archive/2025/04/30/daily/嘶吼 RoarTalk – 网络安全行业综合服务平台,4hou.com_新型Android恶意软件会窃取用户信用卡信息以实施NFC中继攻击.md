---
title: 新型Android恶意软件会窃取用户信用卡信息以实施NFC中继攻击
url: https://www.4hou.com/posts/kgN6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-30
fetch_date: 2025-10-06T22:03:18.160358
---

# 新型Android恶意软件会窃取用户信用卡信息以实施NFC中继攻击

新型Android恶意软件会窃取用户信用卡信息以实施NFC中继攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Android恶意软件会窃取用户信用卡信息以实施NFC中继攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)88366

收藏

导语：诈骗者指示受害者将他们的支付卡轻敲到他们的手机上以验证他们的卡，允许恶意软件读取卡芯片数据并将其发送给攻击者。

一种名为“SuperCard X”的新型恶意软件即服务（MaaS）平台已经出现，该平台通过NFC中继攻击安卓设备，使销售点和ATM交易能够使用受损的支付卡数据。

SuperCard X是由移动安全公司Cleafy发现的，该公司报告称，在意大利发现了利用这种安卓恶意软件的攻击。这些攻击涉及多个具有细微差异的样本，表明分支机构可以根据区域或其他特定需求定制构建。

**SuperCard X攻击是如何展开的**

攻击开始时，受害者会收到一条假冒银行的假短信或WhatsApp消息，声称他们需要拨打一个号码来解决可疑交易引起的问题。

接电话的是一名冒充银行客服人员的骗子，他利用社会工程学欺骗受害者“确认”他们的卡号和密码。然后，他们试图说服用户通过他们的银行应用取消消费限制。

最后，威胁者说服用户安装一个伪装成安全或验证工具的恶意应用程序（Reader），其中包含SuperCard X恶意软件。

安装后，Reader app只需要很少的权限，主要是NFC模块的访问权限，这就足够进行数据窃取了。

诈骗者指示受害者将他们的支付卡轻敲到他们的手机上以验证他们的卡，允许恶意软件读取卡芯片数据并将其发送给攻击者。

攻击者在他们的安卓设备上接收这些数据，该设备运行另一个名为Tapper的应用程序，该应用程序使用被盗数据模拟受害者的卡片。

![apps.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219942148071.png "1745219799789753.png")

这两款应用和设备参与了此次攻击

这些“模拟”卡允许攻击者在商店和自动取款机上进行非接触式支付，但金额有限制。由于这些小额交易是即时的，对银行来说似乎是合法的，因此它们更难被标记和逆转。

![attack.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219944126525.png "1745219848167165.png")

SuperCard X攻击概述

**规避恶意软件**

Cleafy指出，SuperCard X目前没有被VirusTotal上的任何防病毒引擎标记，并且没有危险的权限请求和侵略性攻击功能，如屏幕覆盖，确保它不受启发式扫描的影响。

该卡的仿真是基于atr （Answer to Reset）的，这使得该卡在支付终端看来是合法的，显示了技术的成熟度和对智能卡协议的理解。

另一个值得注意的技术方面是使用互TLS （mTLS）进行基于证书的客户机/服务器身份验证，保护C2通信免受研究人员或执法部门的拦截和分析。

![coms.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219946464638.png "1745219893210186.png")

保密通信系统

根据目前的检测，谷歌Play上没有发现包含此恶意软件的应用程序。Android用户将自动受到谷歌Play Protect的保护，该保护在带有谷歌Play Services的Android设备上默认是开启的。谷歌Play Protect可以提醒用户或阻止已知表现出恶意行为的应用，即使这些应用是来自Play之外的来源。

文章翻译自：https://www.bleepingcomputer.com/news/security/supercard-x-android-malware-use-stolen-cards-in-nfc-relay-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?LowWh3Qi)

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