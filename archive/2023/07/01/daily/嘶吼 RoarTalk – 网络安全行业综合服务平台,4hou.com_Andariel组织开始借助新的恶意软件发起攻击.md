---
title: Andariel组织开始借助新的恶意软件发起攻击
url: https://www.4hou.com/posts/7yDB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-01
fetch_date: 2025-10-04T11:53:40.177682
---

# Andariel组织开始借助新的恶意软件发起攻击

Andariel组织开始借助新的恶意软件发起攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Andariel组织开始借助新的恶意软件发起攻击

lucywang
[新闻](https://www.4hou.com/category/news)
2023-06-30 11:43:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)147020

收藏

导语：Andariel是一个和Lazarus 有关的APT组织，以在2022年年中使用DTrack恶意软件和Maui勒索软件而闻名。

![abstract_money_cybercrime-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230630/1688091632121561.jpg "1688011455207036.jpg")

Andariel是一个和Lazarus 有关的APT组织，以在2022年年中使用DTrack恶意软件和Maui勒索软件而闻名。DTrack 是一个模块化后门，具有键盘记录器、屏幕截图捕捉器、浏览器历史记录检索器、运行进程窥探器、IP 地址和网络连接信息捕捉器等。在同一时期，Andariel还在不断利用Talos和Ahnlab报告的Log4j漏洞。自从2021年11月曝光的Log4j漏洞已成为一大“持续性流行漏洞”，将在未来多年引发持续风险，换言之，这种无所不在的软件库的未经修复版本，将在未来十年或更长时间内继续留存在各类系统当中。同时，美国网络安全审查委员会预测，鉴于 Log4j的普遍存在，在未来十年中，易受攻击的版本仍将存在于系统中，Log4j漏洞不仅影响直接使用该库的基于Java的应用程序和服务，还影响许多其他流行的依赖它的Java组件和开发框架，包括但不限于Apache Struts2、Apache Solr、Apache Druid、Apache Flink、ElasticSearch、ApacheKafka。当然Andariel还经常使用几个恶意软件，如YamaBot和MagicRat，但也有更新版本的NukeSped，当然还有DTrack。

卡巴斯基实验室的研究人员最近发现了一个以前未曾发现的恶意软件家族以及Andariel攻击时的TTP策略。

**攻击过程分析**

Andariel通过执行Log4j漏洞来感染计算机，而Log4j漏洞又会从C2服务器下载更多恶意软件。不过，研究人员无法捕捉到他们下载的第一个恶意软件，但分析发现下载的DTrack是Andariel最先使用的后门程序。通过分析攻击者执行的命令，可以发现这些命令是由人类操作员执行的，从错误和打字错误的数量来看，很可能是一个没有经验的操作员。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230630/1688091632360090.png "1688011467246858.png")

注意“Program”是如何错拼成“Prorgam”的。另一个有趣的发现是，攻击者的系统环境使用了葡萄牙语，他们花了大量的时间来学习执行cmd.еxe /c net localgroup命令代码:

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230630/1688091633875573.png "1688011475164501.png")

研究人员还能够识别一组现成的工具Andariel，这些工具在命令执行阶段安装并运行，然后用于进一步利用目标，比如：

**·**Supremo远程桌面；

**·**3Proxy；

**·**Powerline；

**·**Putty；

**·**Dumpert；

**·**NTDSDumpEx；

**·** ForkDum；

**EarlyRat恶意软件**

研究人员在上述Log4j案例中注意到EarlyRat的一个版本，并假设它是通过Log4j下载的。然而，当他们开始寻找更多样本时，发现了最终导致EarlyRat失败的网络钓鱼文档。网络钓鱼文档本身并不像下面所示的那样先进：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230630/1688091633185648.png "1688011483198498.png")

启用宏后，将执行以下命令：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230630/1688091634124181.png "1688011492988678.png")

奇怪的是，VBA代码ping了一个与HolyGhost / Maui勒索软件活动相关的服务器。

EarlyRat和许多其他RAT（远程访问木马）一样，在启动时收集系统信息，并使用以下模板将其发送给C2：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230630/1688091634137812.png "1688011500207548.png")

如上所述，请求中有两个不同的参数：“id”和“query”。除此之外，还支持“rep0”和“page”参数。它们用于以下情况：

**·**id：计算机的唯一id，是解密“query”值的加密密钥；

**·**query：它是Base64编码的，并与“id”字段中指定的密钥进行滚动异或；

**·**rep0：当前目录值；

**·**page：内部状态的值；

就功能而言，EarlyRat非常简单。它能够执行命令，这是它能做的最有趣的事情。EarlyRat和MagicRat之间有很多相似之处。两者都是使用一个框架编写的：QT用于MagicRat，PureBasic用于EarlyRat。此外，两种RAT的功能都非常有限。

**总结**

尽管Lazarus是一个APT组织，但它仅执行某种特定攻击，比如部署勒索软件，这使得分析其攻击过程变得更加复杂。此外，该组织使用各种自定义工具，不断更新现有的和开发新的恶意软件。

本文翻译自：https://securelist.com/lazarus-andariel-mistakes-and-easyrat/110119/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?WXWn4NDf)

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

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/member/eXPv)

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

[查看更多](https://www.4hou.com/member/eXPv)

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