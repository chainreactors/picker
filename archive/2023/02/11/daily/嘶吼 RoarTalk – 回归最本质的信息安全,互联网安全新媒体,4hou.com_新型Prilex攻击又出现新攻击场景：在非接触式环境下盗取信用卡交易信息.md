---
title: 新型Prilex攻击又出现新攻击场景：在非接触式环境下盗取信用卡交易信息
url: https://www.4hou.com/posts/MByO
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-11
fetch_date: 2025-10-04T06:18:45.479530
---

# 新型Prilex攻击又出现新攻击场景：在非接触式环境下盗取信用卡交易信息

新型Prilex攻击又出现新攻击场景：在非接触式环境下盗取信用卡交易信息 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Prilex攻击又出现新攻击场景：在非接触式环境下盗取信用卡交易信息

xiaohui
[趋势](https://www.4hou.com/category/observation)
2023-02-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)165818

收藏

导语：本文介绍了最近Prilex修改的NFC相关功能。

![sl-pos-terminal-nfc-error-resized-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230203/1675381322125732.jpeg "1675381322125732.jpeg")

Prilex自从2017年被发现以来，就是一直旨在瞄准银行进行针对性攻击，窃取用户的敏感信息。一开始旨在瞄准巴西银行进行针对性攻击、窃取 ATM 用户的信息。现在，它已经从以ATM为中心的恶意软件演变为具有独特的模块化PoS恶意软件，它是我们迄今为止看到的最先进的PoS攻击，它的技术迭代非常快。这是一种高度先进的恶意软件，采用独特的加密方案，可以在目标软件中实现实时修复，强制协议降级，操纵密码，进行GHOST交易，甚至在使用所谓不可破解的CHIP和PIN技术保护的信用卡环境中也可以实现信用卡欺诈。

关于这一攻击，一个经常被问到的问题是Prilex是否能够从支持NFC的信用卡中盗取数据。在最近针对一位被Prilex攻击的客户的事件响应中，安全研究人员发现了三种新的Prilex版本，能够阻止非接触式支付交易。

本文介绍了最近Prilex修改的NFC相关功能。

**“轻触支付”（Tap to Pay）**

过去几年，苹果一直在支付领域进行创新，2014年推出Apple Pay以来，iPhone就已经支持非接触式支付。通常来说，如果需要使用NFC信用卡付款，那么商家需要申请一台刷卡机。在今年1月彭博社报道称苹果正在开发一项新的支付服务，将允许直接在iPhone设备上使用支付。

去年，苹果就在iPhone上推出新的“轻触支付”（Tap to Pay），无论是商家还是消费者，都可以通过iPhone接受Apple Pay、非接触式信用卡、借记卡以及其他数字钱包的付款。

非接触式支付系统由信用卡和借记卡、密钥卡、智能卡或其他设备组成，包括使用射频识别（RFID）或近场通信（NFC，在三星支付、苹果支付、谷歌支付、Fitbit支付或任何支持非接触式的银行移动应用程序中实现）进行安全支付的智能手机和其他移动设备。

嵌入式集成电路芯片和天线使消费者能够通过在销售点终端的读取器上挥动他们的卡、遥控卡或手持设备来支付。与使用广域蜂窝或WiFi网络的其他类型的移动支付不同，非接触式支付是在物理距离很近的地方进行的，并且不需要物理接触。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230203/1675381339144645.jpeg "1675381339144645.jpeg")

不同的支付方式但使用了一种技术：NFC

以下是它们的工作原理：

使用非接触式信用卡支付时，持卡人只需将卡靠近非接触式支付终端(通常在几英寸内)：

终端向卡发送射频(RF)信号，激活嵌入卡中的RFID芯片；

卡片中的RFID芯片向终端发送唯一的识别号码(ID)和交易信息。交易数据是不可重用的，因此即使被攻击者窃取，他们也无法通过使用这些数据来窃取资金。他们也不能访问RFID芯片来篡改数据生成过程；

终端将交易信息发送到发卡机构的处理网络以进行授权；

如果交易被批准，终端将向持卡人发送确认消息，并处理付款。

**疫情让NFC支付变得流行起来**

根据GrandView Research的统计数据，2021全球非接触式支付市场规模估计为345.5亿美元，预计2022年至2030年间将以每年19.1%的复合增长率继续增长。2021，零售市场占全球非接触式收入的59.0%以上。近年来，零售即插即用交易的数量有所增加：零售商可以清楚地看到无接触支付的好处，这可以缩短交易时间，增加收入，提高运营效率。正如涵盖2020年的万事达卡全球研究中所述，74%的零售商表示打算在疫情之后继续使用非接触式支付。

根据美国支付论坛（US Payments Forum）的数据，Visa报告称，在美国，轻触支付占所有面对面交易的28%，是疫情前的五倍，而万事达卡表示，本国82%的刷卡交易发生在无接触的地点。在澳大利亚，非接触式支付甚至在大流行之前就已经越来越流行，2019年，五分之四的销售点购买都是非接触式的。未来几年，这种支付方式在世界各地的普及率预计会更高。

非接触式信用卡提供了一种方便、安全的付款方式，无需实际插入或刷卡。但是，如果攻击者可以在计算机上运行的EFT软件中禁用这些支付，并迫使你将卡插入密码读取器，会发生什么？

**插入即被盗（Insert-to-get-robbed）**

研究人员在野外观察到了三个新的Prilex版本，并设法获得了最新版本（版本06.03.8080）。其他两个版本分别为06.03.8070和06.03.8072。

所获得的版本于2022年11月被发现，与研究人员当年年初发现的其他版本相比，似乎源自不同的代码库。Prilex现在实现了一个基于规则的文件，该文件指定是否盗取信用卡信息以及阻止一个基于NFC的交易的选项。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230203/1675381358432336.png "1675381358432336.png")

引用NFC阻止的Prilex规则文件示例

这是因为基于NFC的交易通常会生成仅对一笔交易有效的唯一ID或卡号。如果Prilex检测到基于NFC的交易并阻止它，EFT软件将在PIN键盘上显示以下消息：

![3.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230203/1675381374297845.jpeg "1675381374297845.jpeg")

PIN板读卡器上显示Prilex发出的虚假错误提示，显示“非接触错误，插入您的卡”

当然，这里的目标是通过将受害者的物理卡插入PIN读卡器来强制受害者使用其物理卡，因此恶意软件将能够通过使用我们之前的文章中描述的所有技术来盗取来自交易的数据，例如操纵密码和执行GHOST攻击。最新的Prilex示例中添加的另一个有趣的新功能是，可以根据细分市场过滤信用卡，并为每个细分市场创建不同的规则。例如，这些规则只有当卡是黑色/无限、公司或其他具有高交易限额的级别时才能阻止NFC并捕获卡数据，这比低余额/限额的标准信用卡更具吸引力。

**攻击趋势分析**

随着非接触式卡的数量不断增加，全世界采用这种方式的人数也在增加，使用这种方式的支付数量已经大幅增加，预计在未来几年还会进一步增加。对于攻击者来说，非接触式支付过程中产生的交易数据是无用的，因此Prilex需要强制受害者将卡插入受感染的PoS终端是可以理解的。

本文翻译自：https://securelist.com/prilex-modification-now-targeting-contactless-credit-card-transactions/108569/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?K7o4co7H)

#### 你可能感兴趣的

* [![]()

  AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
* [![]()

  2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
* [![]()

  【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
* [![]()

  随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
* [![]()

  关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)
* [![]()

  2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
  2025-09-30 12:00:00
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
  2025-09-02 12:00:00
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
  2025-06-06 16:28:40
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
  2025-05-09 12:00:00

[查看更多](https://www.4hou.com/member/bo2j)

# 相关热文

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)

  胡金鱼
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)

  胡金鱼
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)

  梆梆安全
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)

  胡金鱼
* [关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)

  胡金鱼
* [2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

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