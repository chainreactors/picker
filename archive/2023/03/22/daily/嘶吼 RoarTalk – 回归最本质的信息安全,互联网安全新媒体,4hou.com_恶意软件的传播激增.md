---
title: 恶意软件的传播激增
url: https://www.4hou.com/posts/kMJ5
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-22
fetch_date: 2025-10-04T10:13:55.277739
---

# 恶意软件的传播激增

恶意软件的传播激增 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 恶意软件的传播激增

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-03-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125515

收藏

导语：本文将介绍恶意广告是如何运作的，针对它的一些防御措施，以及最近如何利用它来分发恶意软件的例子。

许多入侵和攻击都是从终端被恶意软件感染开始的。恶意软件的传播通常以诱骗某人打开一个可执行文件为手段，这些诱骗文件是良性的，例如一个常见的软件实用程序，但实际上是恶意的。传播恶意软件最常见的方法之一是通过垃圾邮件，但还有其他方法，比如，一种长期使用的将恶意软件植入系统的技术在去年年末重新出现。

“Malvertising” 是恶意软件和广告的合成词，其技术包括购买搜索引擎广告，并在这些广告中放置指向恶意网站的链接。自从与搜索相关的点击付费(PPC)广告出现以来，这种技术就一直被攻击者使用，但最近不知出于什么原因，这种技术被使用的频率和数量出乎意料。接下来，我们将介绍恶意广告是如何运作的，针对它的一些防御措施，以及最近如何利用它来分发恶意软件的例子。

**PPC的工作原理**

谷歌的PPC广告平台是攻击者用来传播恶意软件的主要媒介。Intel 471 曾详细介绍过建立Google Ads活动的内容。这些文章介绍了很多关于这些攻击者如何开展活动的信息，以及他们如何为自己的广告获得顶级搜索结果的一些理论。

谷歌的PPC广告管理面板具有一个相当直观的设计，允许用户一目了然地查看他们的广告活动统计数据。用户可以查看他们当前的广告、关键字、推荐、统计数据和每次优惠的总成本。用户必须提供一个URL来创建广告，显示URL的路径，提供优惠的描述，并为广告制作一些标题。描述、标题和网站都被被纳入谷歌用来计算广告排名的公式中。

一旦创建了广告，用户可以设置广告在PPC上花费的最大金额。广告位的销售采用了一种盲拍卖机制，广告客户可以出价高于竞争对手，但无法看到其他人对广告位的出价。谷歌以前的广告排名算法考虑的是广告商为广告植入排名的出价，然而，新系统综合考虑了广告出价、描述、标题和网站检查。

一旦用户创建了广告并设定了投标价格，他们就可以开始使用Google Ads平台上的多种工具。通过设备定位，广告商可以为只在平板电脑或手机等特定类型的设备上播放的广告定价。

客户可以在Google Ads面板的“受众”选项卡中使用额外的目标定位。用户可以监控点击广告的人的人口统计数据，创建有针对性的广告，或排除某些人口统计数据，并针对特定类型的人，如在金融服务或酒店业工作的人。该平台还允许广告商根据地理位置和受众跟踪，或包括城市、州和邮政编码在内的各种因素来定位客户。

![1.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678702275508612.jpeg "1678702275508612.jpeg")

2023年1月26日谷歌PPC广告平台的广告客户目标选项的截图

**BokBot**

BokBot，也被称为IcedID，是一种银行木马，也可以下载其他恶意软件。BokBot的开发人员与Conti勒索软件组织和Trickbot(另一种用于传播勒索软件的银行恶意软件和僵尸网络)一直有关联。在过去的一年中，最初的访问代理（IAB）越来越多地使用BokBot作为网关恶意软件进行攻击，以取代现已失效的BazarLoader或Trickbot家族。2022年12月和2023年1月，BokBot运营商开始尝试使用谷歌PPC广告平台进行分发。

这些BokBot活动的流量分配系统（TDS）在谷歌搜索广告引擎指向的登录页面上使用受害者和木马过滤。此过滤确保连接客户端不是来自虚拟专用网络（VPN）IP地址，使用户代理检查并遵循超文本传输协议(HTTP)"GET"标头条件。如果连接不符合条件，用户不会被重定向到BokBot恶意登陆页面，而是停留在广告网站上，而广告网站可能与目标应用程序或品牌无关。该网站通常与活动无关。符合目标标准的连接将被重定向到BokBot恶意登陆页面，并且永远不会看到广告站点。

最近的BokBot活动伪装成操作系统虚拟化平台Docker的广告。恶意广告包含拼写错误的域名，并且似乎高于Docker的合法报价。一旦用户点击广告链接，BokBot的第一个URL劫持域就会执行一些基本的木马过滤，以确定广告的观看者是否是目标的合法受害者，而不是研究人员。如果基于用户代理、用户代理客户端提示或地理位置的检查失败，Docker活动的登录页面将引导查看者进入一个关于如何设置和使用Docker的虚假教程。

![2.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678702285695292.jpeg "1678702285695292.jpeg")

2023年1月26日，出现在合法Docker搜索结果和广告之前的恶意Docker广告截图

**BatLoader和EugenLoader/FakeBat**

恶意软件加载器，也称为“下载器（滴管）”，是系统上的初始感染，然后被攻击者用来下载其他恶意代码。BatLoader于2022年2月被发现，是一种利用微软软件安装程序(.msi)和PowerShell的加载器。

Intel 471最近发现，两个不同的攻击者正在通过不同的命令和控制(C2)基础设施分发BatLoader。Mandiant在2022年确定为BatLoader的活动涉及.MSI在安装期间执行.BAT文件。然而，第二个活动不涉及.BAT文件的执行。相反，该恶意软件有一个内嵌的PowerShell脚本，它会代替.BAT文件执行。由于这些差异，Intel 471分析师决定将第二次活动更名为EugenLoader，它也被称为FakeBat。

由于之前的报告混合了EugenLoader和BatLoader，因此很难确定EugenLoaders何时首次出现。但它可能会在2022年11月或12月运行。在对EugenLoader的调查中，我们发现一个域名似乎被用作新活动的下载目的地。域的根目录被错误地打开并显示了EugenLoader活动的.MSI文件。如下图所示，EugenLoader恶意软件已被重命名为模拟已知软件，如FileZilla、uTorrent和WinRAR等。

![3.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678702296474218.jpeg "1678702296474218.jpeg")

可疑EugenLoader活动的域的根目录处于打开状态

在分发活动中，EugenLoader建立了一些域名，声称提供合法的流行软件，但其实这是恶意软件。

EugenLoader最活跃的恶意广告活动之一是伪装成WinRAR，这是一种用于压缩和提取文件的流行软件实用程序。虽然其他广告活动似乎间歇性地将其广告放在搜索结果的顶部，但WinRAR广告活动没有这样的限制，这使得攻击者能够欺骗受害者不断安装EugenLoader。

EugenLoader还通过欺骗7-Zip(另一种流行的文件归档软件)的恶意广告活动进行分发。使用精心制作的谷歌搜索广告，该活动能够将其下载链接放置在7-Zip官方下载页面之前，如下图所示。

![4.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678702305347256.jpeg "1678702305347256.jpeg")

有两个PPC广告提供7-Zip，但域名与官方项目无关

直到最近，恶意广告还不是攻击者首选的攻击手段，与电子邮件垃圾邮件等传统手段相比，它很少被使用。然而，EugenLoader背后的运营商能够购买始终出现在谷歌第一搜索结果位置的广告。恶意广告技术有可能挑战恶意软件垃圾邮件(malspam)作为攻击者首选载体的位置。

恶意软件开发者投放恶意广告有利有弊。首先，攻击者可以通过广告吸引寻找下载工具的用户，出现在第一个搜索结果中意味着很有可能有人在没有仔细查看域名的情况下点击。随后的登录页面看起来与合法登录页面完全相同，人们很可能会下载并安装该工具。

这与垃圾邮件相比具有优势，垃圾邮件可能会被安全工具捕获并隔离，或者被发送到垃圾邮件文件夹，永远不会被潜在受害者注意到。如果目标确实下载了它，攻击者必须诱骗其打开，例如打开发票、点击链接或运行可执行文件。但恶意广告抓住了那些想下载并立即运行的人。

然而，恶意广告的成本并不便宜。每次点击点击付费广告的成本可能高达2至3美元。由于攻击者不断竞标广告位，这些行动也提高了合法广告商的成本。有可能是恶意商家用偷来的信用卡信息来支付广告费用。另外，攻击者是如何为这些广告买单的，这将是另一个值得研究的课题，它可能会挖掘出这些活动背后的团体。

在某些情况下，活动的成功与否可以衡量。一些恶意广告将受害者引导到Bitbucket上的网站，这可能会显示下载数量。其中一项活动的下载量超过3000次。按每次点击2美元计算，投放广告的人可能已经支付了多达6000美元，这表明攻击者有经济实力。在这些活动中发现的其他类型的恶意软件包括RedLine等信息窃取软件。恶意软件经常阻碍VirusTotal提交。文件大小高达700 MB，这与滴管或加载器的典型大小相比非常大。VirusTotal的文件大小限制为32 MB(最多可提交200 MB的文件)，这意味着由分发的恶意文件不一定会有分析示例。

**总结**

恶意广告激增，对谷歌影响最大，在2023年1月中旬达到顶峰，此后有所下降。安全社区已经就其调查结果与谷歌取得联系。几位研究人员制作了一份电子表格，用于跟踪恶意广告活动和被假冒的品牌。在2023年1月19日至2023年2月22日期间，该电子表格包含了584起恶意广告活动的示例。此外，研究人员还开发了一些工具，比如Randy McEoin开发的这个工具，它可以搜索恶意广告，Michael McDonnell开发的这个工具也可以对活动截图留证。

本文翻译自：https://intel471.com/blog/malvertising-surges-to-distribute-malware如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vfZjY5hJ)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bo2j)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方...