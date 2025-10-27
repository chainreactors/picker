---
title: 新的网络钓鱼攻击欺骗Microsoft 365身份验证系统
url: https://www.4hou.com/posts/qpD7
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-07
fetch_date: 2025-10-04T11:59:19.553637
---

# 新的网络钓鱼攻击欺骗Microsoft 365身份验证系统

新的网络钓鱼攻击欺骗Microsoft 365身份验证系统 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的网络钓鱼攻击欺骗Microsoft 365身份验证系统

布加迪
[新闻](https://www.4hou.com/category/news)
2023-08-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)155099

收藏

导语：Vade公司近日发布的一份报告详细阐述了最近发现的一起成功欺骗了Microsoft 365身份验证系统的网络钓鱼攻击。

![1688937664565900.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688937664565900.jpg "1688937664565900.jpg")

电子邮件安全和威胁检测服务提供商Vade公司近日发布了一份报告，详细阐述了最近发现的一起网络钓鱼攻击，这起攻击成功欺骗了Microsoft 365身份验证系统。

据Vade的威胁情报和响应中心（TIRC）声称，攻击电子邮件含有一个带有JavaScript代码的有害HTML附件。这段代码的目的在于收集收件人的电子邮件地址，并使用来自回调函数变量的数据篡改页面。

TIRC的研究人员在分析一个恶意域名时解码了使用base64编码的字符串，获得了与Microsoft 365网络钓鱼攻击相关的结果。研究人员特别指出，对网络钓鱼应用程序的请求是向eevilcorponline发出的。

研究人员通过periodic-checkerglitchme发现，其源代码与附件的HTML文件很相似，这表明网络钓鱼者在利用glitch.me来托管恶意的HTML页面。

glitch.me是一个允许用户创建和托管Web应用程序、网站和各种在线项目的平台。遗憾的是，在这种情况下，该平台却被人利用，用于托管涉及这起进行中的Microsoft 365网络钓鱼骗局的域名。

当受害者收到一封含有恶意HTML文件（作为附件）的电子邮件时，攻击就开始了。受害者打开该文件后，一个伪装成Microsoft 365的网络钓鱼页面就会在受害者的互联网浏览器中启动。在这个欺骗性页面上，攻击者提示受害者输入其凭据，攻击者会迅速收集这些凭据用于恶意目的。

由于Microsoft 365在商业界得到广泛采用，被泄露的账户很有可能属于企业用户。因此，如果攻击者获得了对这些凭据的访问权，他们就有可能获得敏感的商业和交易信息。

此外据报告显示，Vade的研究人员还发现了一种涉及使用被欺骗的Adobe版本的网络钓鱼攻击。

![1688937850201873.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691120027214697.jpg "1688937850201873.jpg")

图1. Office 365和Adobe网络钓鱼诈骗的登录页面（图片来源：Vade）

进一步分析后发现，恶意的“eevilcorp”域名返回了一个与Hawkeye应用程序相关的身份验证页面。值得一提的是，包括Talos在内的网络安全专家曾对最初的HawkEye键盘记录器进行了分析，将其归类为2013年出现的恶意软件套件，随后出现了后续版本。

这一发现很重要，因为这解释了为什么TIRC的研究人员无法将身份验证页面与HawkEye键盘记录器直接联系起来。

发现的攻陷指标（IoC）如下：

periodic-checkerglitchme

scan-verifiedglitchme

transfer-withglitchme

air-droppedglitchme

precise-shareglitchme

monthly-payment-invoiceglitchme

monthly-report-checkglitchme

eevilcorponline

ultimotemporeonline

这起攻击之所以引人注目，是由于它利用了恶意域名（eevilcorponline）和HawkEye。作为一种键盘记录器和数据窃取工具，HawkEye可以在黑客论坛上买到。虽然Vade的调查仍在进行中，但是用户有必要保持警惕，并遵循以下这些措施，以防止沦为Microsoft 365网络钓鱼骗局的受害者：

**仔细核对电子邮件发件人：**小心那些声称由Microsoft 365发来、实际上由可疑或不熟悉的电子邮件地址发来的电子邮件。验证发件人的邮件地址，以确保它与微软官方域名匹配。

**留意一般的问候语：**网络钓鱼电子邮件常常使用一般的问候语，比如“亲爱的用户”，而不是直接称呼你的姓名。正规的微软电子邮件通常用你的姓名或用户名来称呼你。

**分析电子邮件内容和格式：**注意拼写和语法错误以及糟糕的格式。网络钓鱼电子邮件常常含有微软的正规邮件不会含有的错误。

**将鼠标悬停在链接上方：**在点击电子邮件中的任何链接之前，将鼠标悬停在链接上方，以查看实际的URL。如果链接的目的地看起来可疑或与微软官方域名不同，请不要点击它。

**警惕紧急请求：**网络钓鱼电子邮件常常给人一种紧迫感，迫使你立即采取行动。小心那些声称你的Microsoft 365账户存在风险或要求紧急验证个人信息的电子邮件。

切记，如果你怀疑一封电子邮件是网络钓鱼骗局，最好谨慎行事。向微软报告任何可疑的电子邮件，并避免提供个人或敏感信息，除非你可以通过官方渠道核实请求的合法性。

本文翻译自：https://www.hackread.com/phishing-attack-microsoft-365-authentication/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fG5Nptvk)

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