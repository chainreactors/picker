---
title: 八种常见的云配置错误类型及缓解方案
url: https://www.4hou.com/posts/2JNP
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-24
fetch_date: 2025-10-03T20:42:57.258016
---

# 八种常见的云配置错误类型及缓解方案

八种常见的云配置错误类型及缓解方案 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 八种常见的云配置错误类型及缓解方案

小二郎
[新闻](https://www.4hou.com/category/news)
2022-10-23 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)181060

收藏

导语：盘点常见的云配置错误类型

![微信截图_20221015145548.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666322084115643.png "1665817019549340.png")

云配置错误（Cloud misconfiguration）指的是云环境中可能会对有价值的信息和资产构成风险的任何错误、故障或缺口。当组织没有正确配置基于云的系统时，就会发生这种情况，造成网络暴露、安全漏洞、内部威胁或外部黑客攻击。

这些云配置错误会导致组织未加密或敏感的数据暴露在公共互联网上，造成大规模的数据泄露和宕机情况，进而可能导致组织或政府实体面临无可挽回的声誉和财务损失。

本文将探讨云配置错误的影响、最常见的类型，以及可以采取的缓解措施，以最大限度地保护云环境安全。

**云配置错误对系统安全的影响**

云环境中的错误配置可以使攻击者未经授权地访问系统功能和敏感数据。例如，数据库服务器的错误配置可能使数据通过基本的web搜索访问，这可能会导致重大的数据泄露。云配置错误甚至可能导致系统安全的完全破坏和其他严重后果。虽然，特定配置错误的业务影响取决于错误配置的严重程度，但由此导致的数据泄露可能会使组织损失数百万美元。

**常见的云配置错误类型**

**1. 过于宽松的访问控制**

当启用了太多的云访问权限时，就会出现云环境过于宽松的情况。这可能包括：

**·** 在云主机上启用遗留协议；

**·**暴露面向外部的端口；

**·**在缺乏适当控制措施的情况下暴露敏感的API；

**·**启用私有和公共资源之间的通信模式；

在配置应用程序时，对访问控件的过多权限可能会为攻击者提供在系统内部垂直或横向移动的路径，并增加暴露的攻击面。

**2. 存储访问配置错误**

云错误配置的另一个例子是将存储资产暴露给外部参与者。很多时候，组织会混淆“认证”用户和“授权”用户，从而错误地授予“认证”用户访问权限。这些经过身份验证的“认证”用户可以是任何具有有效凭证的客户端或用户，因为他们通过AWS进行了身份验证，但却并未得到您的组织或应用程序“授权”。一个简单的例子是允许所有AWS用户（而不是应用程序的所有授权用户）访问S3桶。

组织应该只在组织内部授予对存储桶的访问权限。由于这种云配置错误的结果，网络犯罪分子可能会访问存储，并在积极扫描AWS S3存储桶和公共GitHub存储库时找到关键信息，如API密钥、密码和其他凭证。因此，组织在设置存储配置时应该格外谨慎，以确保云存储不被破坏或暴露。安全团队也应该默认为存储桶中的关键数据启用强加密，监视所有标记为公共的存储节点，并消除不必要的权限。

**3. 无限制的入站和出站端口**

所有对互联网开放的入站端口都存在潜在的安全风险。当迁移至多云（multi-cloud）基础设施时，安全团队应该了解开放端口的全部范围，并将它们限制在基本系统中，锁定那些并非十分必要的系统。

当然，不仅入站端口会带来安全问题，当系统受到威胁时，出站端口也会通过数据渗漏、横向移动和内部网络扫描产生漏洞。通过各种模式（如RDP或SSH）从公共网络甚至从您的VPN之外的网络授予对服务器的访问权，是一种常见的云错误配置，它会使您面临数据泄露的风险。应用程序服务器应该将出站流量限制为“只对基本应用程序和服务器有效”。使用最小特权原则，并限制通过SSH对出站端口的访问，因为应用程序服务器很少需要通过SSH与网络中的其他远程服务器通信。

**4. 无限制地访问非HTTP/HTTPS端口**

识别和检查所有开放端口非常重要，因为系统操作依赖于这些潜在的、易受攻击的开放端口。组织应该开启那些绝对需要的端口，并屏蔽那些并不必要的端口。如果这些端口配置不当，攻击者就很容易利用或强行使用身份验证。如果这些端口需要对互联网开放，请确保通信是加密的，并且流量只限制在特定的地址。

**5. 禁用或未配置监控和日志记录**

即使是完善的组织有时也会缺乏严格且强大的监控和日志记录机制。对云平台上的活动进行日志记录和定期监控至关重要。

这些日志可以用于:

**·**识别可疑行为和安全盲点；

**·**注意到员工未经授权的行为；

**·**定期报告；

**·**确认任何其他错误或配置错误；

但是，只有在为了采取适当的操作而持续监视日志时，日志才会发挥作用。因此，请确保您对每个可能导致安全漏洞的活动都有足够的日志记录和监控。此外，基于这些日志实现自动化和有针对性的警报，以便在任何可疑活动导致破坏之前识别和处理它。

**6. 系统的默认凭据**

许多开发团队会为身份验证创建默认凭据，以简化开发过程。例如，许多团队对于云实例、数据库和其他服务都有一些默认凭据。这些默认凭据通常很容易被猜出和/或被太多人知道。因此，这些凭据或配置绝对不应该在生产环境中使用。

组织应该根据开发环境拥有不同的配置文件。实现一个防止默认凭据传播到生产环境的过程是关键，审计每个版本以确保该过程正在有效运行也是关键。

**7. 生产环境中的开发设置**

另一个常见的配置错误是在生产环境中使用开发设置。在大多数情况下，适合于开发环境的设置和配置并不适合于生产环境，原因有很多。例如，允许从任何服务器以任何速率传入请求在开发中似乎并没问题，但在生产环境中却可能会导致重大问题。这还包括应用程序中的隐藏代码。例如，在控制台中打印敏感的调试信息可能很容易被忽略，但在生产环境中却会导致严重的安全漏洞。因此，在部署到生产环境之前，组织需要仔细检查这些代码设置并正确设置它们。

**8. 不遵循第三方组件的“安全”配置**

在整个开发过程中，我们会使用各种第三方库、组件和应用程序。虽然在为各种组件选择供应商时，进行全面的分析是至关重要的，但确保遵循第三方规定的最佳实践和配置也同样重要。

大多数软件供应商——无论是商业的还是开源的——都将规定最佳实践或推荐的安全实施标准，这些配置通常都已在其端进行过安全测试。正确地实现这些最佳实践不仅可以降低安全漏洞的风险，而且在漏洞确实发生的情况下也能增加这些供应商的责任。

**结语**

配置错误是云环境中安全漏洞的最常见原因之一。即使您在开发过程中遵循了所有的最佳实践，一个简单的配置错误——如果忽略了——也可能危及整个系统的安全性。虽然采取必要的预防措施来防止这种情况发生是至关重要的，但创建一个100%安全的系统是非常困难的。尽管如此，通过识别并消除本文所述的云安全漏洞，将有助于最大限度地降低安全风险。

与所有的网络风险一样，云安全工作应该围绕优先处理和减轻与您业务最相关的威胁，将您的资源用于最需要的地方，并开展团队合作，以有效降低真正的网络风险。

本文翻译自：https://cloudsecurityalliance.org/blog/2022/09/27/8-common-cloud-misconfiguration-types-and-how-to-avoid-them/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mgZCQ5QU)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/9381c342641778c32b6b.jpeg)

# [小二郎](https://www.4hou.com/member/enxl)

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

[查看更多](https://www.4hou.com/member/enxl)

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