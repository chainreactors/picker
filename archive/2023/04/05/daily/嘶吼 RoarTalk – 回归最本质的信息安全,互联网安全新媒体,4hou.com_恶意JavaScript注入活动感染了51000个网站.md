---
title: 恶意JavaScript注入活动感染了51000个网站
url: https://www.4hou.com/posts/GKy0
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-05
fetch_date: 2025-10-04T11:29:46.580526
---

# 恶意JavaScript注入活动感染了51000个网站

恶意JavaScript注入活动感染了51000个网站 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 恶意JavaScript注入活动感染了51000个网站

布加迪
[新闻](https://www.4hou.com/category/news)
2023-04-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)141410

收藏

导语：Unit 42的研究人员一直在跟踪一起大范围的恶意JavaScript（JS）注入活动，该活动将受害者重定向到广告软件和欺骗页面等恶意内容。这一威胁在2022年全年都很活跃，并在2023年继续感染众多网站。

Unit 42的研究人员一直在跟踪一起大范围的恶意JavaScript（JS）注入活动，该活动将受害者重定向到广告软件和欺骗页面等恶意内容。这一威胁在2022年全年都很活跃，并在2023年继续感染众多网站。

我们在51000多个网站上检测到了注入的JS代码，包括跻身Tranco前100万个网站排行榜的数百个网站。受影响的网站出现在Tranco中表明，这起活动可能影响了大量的人。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679810981428033.png "1679810981428033.png")

我们还发现，这起活动是多方面的，因为它在重定向到恶意网页之前执行多步注入，并使用混淆和良性附加攻击来绕过检测机制。恶意软件编写者利用这些技术将恶意JS代码样本的多种变体注入到网站中。

我们新颖的对抗性深度学习技术无罪推定（IUPG）检测到了注入的JS代码的多种变体。该模型是我们下一代防火墙产品的高级URL过滤（AUF）订阅服务的一部分。它可以检测恶意JS样本，并可以对来自内联保护和我们离线爬虫的内容进行分类，内联保护可对防火墙上的流量进行实时分析。

**具体活动和用户影响**

我们已经检测到攻击者将恶意JS代码注入到网站的活动的多种形式。这种注入的代码将受害者重定向到各种恶意内容，比如广告软件和骗局。

研究人员去年报道了一起类似的活动。我们在2020年观察到了该活动的第一例。然而，我们将侧重介绍在2022年1月至2023年期间跟踪的这起活动的最新变体。

自2022年初以来，我们在来自51000个主机名的大约170000个URL上检测到了这起活动。如图1所示，该活动在过去一年保持活跃状态，并在2023年继续影响网站。这起活动在2022年5月至8月期间达到了顶峰，当时我们看到平均每天有4000个URL中招。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679810997631256.png "1679810997631256.png")

图1. 该图显示了整个2022年和2023年初的活动，在2022年5月至8月之间达到顶峰

我们怀疑这起活动影响了大量的人，因为在撰写本文时，数百个受感染的网站跻身Tranco的前100万网站排行榜。在2023年1月期间，我们在14773个设备上拦截了来自这些网站的约240000次会话。

**JS注入的例子**

这起恶意JS注入活动使用各种技术来绕过检测机制，比如混淆、向大型良性文件附加代码和多步注入。我们将介绍恶意JS代码的几个例子，活动背后的不法分子对这些代码进行混淆处理，并隐藏在更庞大的JS文件中。我们还将介绍一个例子，其中恶意软件在最终加载恶意载荷之前执行一系列的JS注入。

**混淆**

图2a、b和c显示了活动中经常检测到的JS片段例子。在所有这些例子中，注入的JS代码都经过混淆处理，以隐藏恶意载荷从而绕过检测。具体来说，这种经过混淆处理的代码隐藏了用于加载恶意JS的外部URL。代码还包括向文档对象模型（DOM）动态添加恶意JS的行为。

比如说，下面的前两个JS代码片段（图2a和图b）使用String.fromCharCode隐藏了指向恶意JS的链接，这是一种常见的混淆技术。图2c显示了混淆的另一个例子。经过混淆处理的代码显示在左边，经过去混淆处理的代码显示在右边。通过使用variable \_0xfcc4中的十六进制表示来混淆函数调用的名称（比如fromCharCode）。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679811019374258.png "1679811019374258.png")

图2 a. 使用String.fromCharCode隐藏恶意JS链接的例子

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679811030136099.png "1679811030136099.png")

图2 b. 使用String.fromCharCode隐藏恶意JS链接的例子

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679811047474949.png "1679811047474949.png")

图2 c. 隐藏函数调用名称的例子。图像的左侧显示了如何使用variable \_0xfcc4中的十六进制表示来混淆函数调用。图像的右侧显示了去混淆后的函数调用fromCharCode

**将JS代码附加到大文件中**

我们在一些网站上发现了这些经过混淆处理的JS片段被注入到常见实用程序JS文件（比如jQuery）中的例子。恶意软件编写者经常使用这一招将恶意代码附加到大块的良性代码中，这又叫良性附加攻击。这种技术可以帮助恶意软件编写者逃避安全爬虫的检测机制。

**多步JS注入**

在所有JS代码片段中注入的JS代码（如图2a、b和c所示）通过操纵DOM附加外部恶意JS代码。这使攻击者能够改变恶意载荷。

这起活动最近的一种变体是将恶意JS代码注入到网站。然后它执行一系列中间JS注入，之后加载将受害者重定向到恶意网页的恶意载荷。

在图3显示的例子中，每个注入的JS代码在投放恶意载荷之前依次执行来自另一个网站的JS代码。包含来自不同网站的JS注入的一个原因可能是，攻击者想要不断改变加载最终载荷的URL，以防加载JS的URL被安全爬虫列入黑名单。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679811070508587.png "1679811070508587.png")

图3. 这个例子表明网站上的脚本注入在最终加载重定向到恶意网页的恶意载荷之前执行一系列中间脚本注入

**重定向到恶意内容**

最终的恶意载荷将用户重定向到不同的网站，然后登录到最终的网页，这通常是广告软件或欺骗页面。比如说，访客可能被重定向到一个虚假的通知欺骗页面，如图4a所示。在这个页面上，人们会看到欺骗性内容，引诱他们允许由攻击者控制的网站发送浏览器通知。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679811095915000.png "1679811095915000.png")

图4. 显示虚假的验证码图像，是为了引诱人们允许网站发送通知

在另一个例子中，如图4b所示，最终的恶意网页显示了来自知名视频共享平台的模仿页面的虚假警告这种形式的欺骗性内容。这些欺骗性内容会诱使人们下载虚假浏览器。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230326/1679811113843606.png "1679811113843606.png")

图4 b. 显示了知名视频共享平台的模仿页面以及虚假警告，诱使人们下载虚假浏览器

**JS如何被注入到网站上？**

Unit 42的研究人员怀疑，由于一个或多个易受攻击的内容管理系统（CMS）插件，大量网站可能会遭到攻击。Sucuri公司的研究人员曾报告了一起类似的活动利用CMS插件（详见https://blog.sucuri.net/2022/05/massive-wordpress-javascript-injection-campaign-redirects-to-ads.html）。我们还发现，检测到的网站（共51000个）中估计四分之三使用流行的CMS。

在一半以上被检测到的网站的主页上都包含注入的恶意JS代码。活动攻击者采用的一种常见策略是向经常使用的JS文件名（比如jQuery）注入恶意JS代码，它们可能被包含在中招网站的主页上。这可能帮助攻击者锁定网站的合法用户，因为他们更有可能访问网站的主页。

**利用深度学习检测恶意JS注入**

恶意软件编写者为这起活动设计了恶意JS代码的不同变体，将其注入到网站中。众所周知，深度学习技术在检测同一攻击的不同变体方面功能很强大。因此，深度学习技术可以提高恶意JS注入的检出率。

深度学习技术还可以抵抗来自恶意软件的对抗性逃避活动。这些类型的对抗性逃避的一个具体例子是普遍存在的黑盒对抗性威胁，即良性附加攻击。

**结论**

在2022年至2023年初期间，在51000多个网站上检测到了一起广泛的恶意JavaScript注入活动。我们发现恶意软件编写者对恶意JS进行混淆处理以绕过检测机制，并在重定向到恶意网页之前执行多步注入。

注入的JS代码可能影响了大量互联网用户，因为数百个受感染的网站跻身Tranco前100万网站排行榜。我们建议网站所有者和客户及时更新第三方插件和软件，以保护他们的网站免受这类注入。

这起活动中注入的恶意JS代码是我们在外头看到的附加攻击的一个常见例子。正如我们在IEEE安全和隐私研讨会（SPW）上发表的IUPG模型研究工作中所解释的那样，IUPG模型的训练过程专门旨在识别和隔离良性内容背景中的恶意子模式。

我们的深度学习模型无罪推定（IUPG）检测到了注入恶意JS代码的多种变体。该模型是高级URL过滤云提供的安全服务（可检测恶意JS样本）的检测功能之一。它还可以对来自离线爬虫以及防火墙上流量的内联实时分析的内容进行分类。

使用高级URL过滤和DNS安全订阅的下一代防火墙让客户可以免受本文描述的恶意JS注入活动的已知URL和主机名。我们还提供了已知攻陷指链接（https://github.com/pan-unit42/iocs/blob/master/IOCs\_MaliciousJS.txt），帮助对付本文中讨论的威胁。

本文翻译自：https://unit42.paloaltonetworks.com/malicious-javascript-injection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?c4aGbgsC)

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
...