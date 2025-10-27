---
title: PyPI中新出现了一类新型混淆攻击
url: https://www.4hou.com/posts/4Kjk
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-24
fetch_date: 2025-10-03T23:36:49.478227
---

# PyPI中新出现了一类新型混淆攻击

PyPI中新出现了一类新型混淆攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PyPI中新出现了一类新型混淆攻击

xiaohui
[新闻](https://www.4hou.com/category/news)
2022-11-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)150504

收藏

导语：针对恶意包的新型混淆技术可以在图像中隐藏代码。

针对恶意包的新型混淆技术可以在图像中隐藏代码。

Check Point 研究团队最近在PyPI上检测到一个新的、从未见过的恶意包，PyPI是Python编程语言的软件库。恶意包被设计用来隐藏图像中的代码(基于图像的代码混淆——隐写术)，并通过Github上的开源项目感染PyPI用户。这些发现反映了攻击者严密的攻击计划，证明了PyPi上的混淆技术已经进化。

**常见恶意软件包结构**

开源域上的恶意软件包通常包括3个主要组件：

恶意代码：负责下载和运行病毒可执行文件，向攻击者打开远程shell，或者只是收集并发布它能找到的所有PII。

运营商代码：负责注入恶意代码。通常，它将是一个合法的包，其中包含作为安装代码一部分的恶意代码段（如PyPI中的setup.py或NPM中的安装后脚本）。运营商代码通过混淆处理被隐藏，或者可以在安装过程中从诸如pastebin.com之类的源动态下载。

感染软件包：首先吸引受害者安装恶意软件包，一种常见的技巧是与普通合法名称相似的包名。

攻击者通常会仔细命名包名称。选择过于普通的包名可能会导致恶意应用程序被快速检测到(对PyPI用户具有很高的可见性)。选择一个小众名称可导致包的下载量较少，这将降低成功感染的潜在数量，需要开发商通过积极与潜在用户接触，让他们安装受感染的包来填补这一空白。在大多数情况下，攻击者似乎喜欢规模化攻击，即模仿常见的包名，假设高下载量将保证至少发生一些感染，即使潜在的软件包寿命更短。有些情况包括更独特和更重要的恶意代码设计选择。Apicolor似乎使用的就是该方法，它有一个小众且不受欢迎的软件包，但会积极尝试让GitHub用户安装该应用程序。

**Apicolor**

Check Point 研究团队检测到的恶意包名为“apicolor”。乍一看，它似乎是PyPI上许多开发包中的一个。它是相当新的，最初发布于今年10月31号，有一个大致的描述和一个混淆的标题，说明这是一个“REST API的核心库”。普通恶意包的观察者几乎不会注意到这些。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050467834445.png "1668050467834445.png")

在深入研究了包安装脚本之后，研究人员注意到开头有一个奇怪的、重要的代码部分。它首先手动安装额外的需求(不是通过更常见的需求部分)，然后从web下载一张图片，使用新安装的包处理图片，并使用exec命令触发处理生成的输出。代码片段与我们通常在一般setup.py安装脚本中看到的代码片段有很大不同。

![2.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050482160914.jpeg "1668050482160914.jpeg")

手动安装的两个包是request(API使用中非常流行的帮助包)和judyb。judib包的细节最初看起来像一个“正在进行中”的包，有一个空的描述和一个混淆的标头，说明这是“一个纯Python judyb模块”。深入研究发现，judyb与apicolor首次发布的时间大致相同。

![3.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050491850639.jpeg "1668050491850639.jpeg")

judyb代码原来是一个隐写术模块，负责隐藏和揭示隐藏在图片中的信息。研究人员怀疑在apicolor安装过程中下载的图像可能包含其内部的隐藏部分。

![4.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050504214520.jpeg "1668050504214520.jpeg")

![4.2.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050513173961.jpeg "1668050513173961.jpeg")

![4.3.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050522491245.jpeg "1668050522491245.jpeg")

现在回到apicolor安装代码，第一步是观察从网上下载的图片。这似乎是合法的，没有什么异常。

将judyb的“揭示”方法应用于这张图片，显示了一条隐藏的信息，从该图像中发现。该消息似乎包含一个base64混淆的Python代码，这是恶意软件包隐藏其恶意代码的常用做法。

![6.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050542972835.jpeg "1668050542972835.jpeg")

使用base64对该代码段进行去混淆处理揭示了我们非常熟悉的常见恶意代码模式；从web下载恶意exe并在本地运行。

![7.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050552117897.jpeg "1668050552117897.jpeg")

在发现apicolor软件包的恶意和载体部分后，接下来就应该介绍如何安装这些软件包以及这些感染是如何被引发的？

**主动感染**

研究人员搜索使用这些包的代码项目，使团队能够进一步了解它们的感染技术及进程。通过这一搜索，很明显apicolor和judib非常小众，在GitHub项目上有少量使用。

![8.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050562907951.jpeg "1668050562907951.jpeg")

只有三个GitHub用户似乎在他们的代码中包含了这些包。将它们作为(超级冗余的)需求添加到其公开可访问的GitHub项目中。不出所料，这三个用户都是GitHub的新用户。

![9.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050574210856.jpeg "1668050574210856.jpeg")

![9.2.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050582102189.jpeg "1668050582102189.jpeg")

![9.3.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050596309358.jpeg "1668050596309358.jpeg")

**隐性感染**

感染过程如下：

当用户在网上搜索合法的项目时，会遇到这些GitHub开源项目，并在本地安装它们，他们并不知道其中含有恶意的包。需要注意的是，代码似乎有效。在某些情况下，存在空的恶意包。从安装程序的角度来看，他们正在尝试一个来自GitHub的开源项目，并不知道其中隐藏了恶意木马程序部分。

![10.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050609369053.jpeg "1668050609369053.jpeg")

细心的用户只会考虑热门的开源项目，而上述项目似乎符合这一标准。

![11.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050621592463.jpeg "1668050621592463.jpeg")

![11.2.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221110/1668050634164207.jpeg "1668050634164207.jpeg")

**向PyPI披露**

一旦这些包被识别出来，Check Point Research就会提醒PyPI它们的存在，之后PyPI就会进行删除。

供应链攻击 旨在利用组织和外部方之间的信任关系。这些关系可能包括合作伙伴关系、供应商关系或使用第三方软件。攻击者会破坏一个组织，然后向供应链的上游移动，利用这些受信任的关系来访问其他组织的环境。近年来，这类攻击越来越频繁，影响也越来越大，因此开发人员必须确保自己的操作安全，反复检查正在使用的每个软件成分，特别是从不同存储库下载的软件，尤其是那些不是自己创建的软件。

研究人员发现了一种新型的有组织的攻击，他们不仅会模仿一个常见的包，隐藏其恶意代码，还会直接针对特定类型的用户组织发起攻击，将感染阶段从高度关注的PyPI平台转移到GitHub，这使得检测此类恶意包变得更加困难。

本文翻译自：https://research.checkpoint.com/2022/check-point-cloudguard-spectral-exposes-new-obfuscation-techniques-for-malicious-packages-on-pypi/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?dg53maev)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

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

[查看更多](https://www.4hou.com/member/bo2j)

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

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6...