---
title: 引发DoS攻击的电动汽车充电站劫持事件
url: https://www.4hou.com/posts/YX1M
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-08
fetch_date: 2025-10-04T05:56:22.461711
---

# 引发DoS攻击的电动汽车充电站劫持事件

引发DoS攻击的电动汽车充电站劫持事件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 引发DoS攻击的电动汽车充电站劫持事件

布加迪
[新闻](https://www.4hou.com/category/news)
2023-02-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)169937

收藏

导语：几种电动汽车充电系统近日曝出两个新的安全漏洞，这两个漏洞一旦被人利用，可用来远程关闭充电站，甚至使充电站面临数据和能源被盗的风险。

**简单概述**

SaiFlow研究团队近日发现，网络攻击者可以利用某些版本的使用WebSocket通信机制的开放充电站协议（OCPP），导致电动汽车充电站无法使用，并导致服务中断。发现的这种攻击方法结合了OCPP标准存在的两个新漏洞：

I）对多个充电器的连接处理不当

II）薄弱的身份验证策略

OCPP标准没有规定如何同时处理单个充电站的多条连接。网络攻击者可以代表充电站打开一条额外的“新”连接连到充电系统管理服务（CSMS），从而破坏充电站与CSMS之间的原始连接，并将原始连接暴露在各种威胁的面前，包括潜在的拒绝服务（DOS）攻击、从电动汽车供应设备（EVSE）网络窃取数据和能源。将新连接的处理不当与薄弱的OCPP身份验证和充电器身份策略结合起来，可能导致针对EVSE网络的大规模分布式DoS（DDoS）攻击。

这种攻击最近大多家CSMS提供商的身上进行了演示和测试。接受测试的每家CSMS提供商都以不同的方式处理拥有相同充电站ID的多条连接，结果发现大多数CSMS提供商都容易受到攻击，它们有两种类型的反应：

1. 一些CSMS提供商会关闭原始充电站连接，使实际充电站断开连接。

2. 其他提供商会保持原始连接处于打开的状态，但不会与之通信。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675596180140766.png "1675595889126471.png")

这两种情况都容易受到分布式拒绝服务（DDoS）攻击，最后一种情况最严重，因为CSMS和充电站都不会通知充电站运营商（CPO）某个地方出了岔子。

此外在攻击过程中（攻击者的连接连到CSMS），敏感的个人信息暴露给了攻击者，这可能使攻击者得以进一步攻击CSMS或窃取客户的身份。

新漏洞是在OCPP 1.6J版本中发现的，这是目前市面上的主要版本。更新颖的OCPP版本（2.0.1）尚未得到大规模部署，如果没有适当地采取所需的身份验证防范措施，同样容易受到这种攻击。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675596181881694.png "1675595943115973.png")

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675596182116074.png "1675595963195376.png")

**利用电动汽车充电器的漏洞**

这种攻击方法结合了OCPP标准中的两个漏洞：I）对多条充电站连接处理不当和II）OCPP标准中薄弱的身份验证策略。可以利用这两个漏洞对EVSE网络执行拒绝服务（DoS）攻击，或造成大得多的影响，引发分布式拒绝服务（DDoS）。

**I）对多条充电器连接处理不当**

标准的OCPP协议没有定义当充电站接受一条“新”连接、原始连接仍在使用时会有的预期行为。充电站期望与CSMS建立连接，以支持诸如收费授权、支付、折扣和计费报告之类的功能。如果充电站无法授权电动汽车充电，充电操作可能不被接受，电动汽车将无法充电。DoS可能会对CPO造成经济和声誉上的损害。此外，在最糟糕的情况下，如果一家公司拥有对其业务至关重要的电动汽车车队，可能会受到网络攻击者的破坏或被索要赎金。

Saiflow的研究团队发现，CSMS提供商以不同的方式处理多条连接，所有这些方式都可以被攻击者利用。市面上的一些CSMS提供商在“新”连接建立起来后，断开充电站WebSocket连接。这种行为让网络攻击者得以通过原始充电器的连接，阻止真正的充电站与CSMS进行联系，从而引发DoS。其他CSMS提供商开始使用“新的”恶意连接，允许攻击者接收敏感信息，比如驾驶员的个人信息、信用卡资料，甚至CSMS用于固件无线更新的文件服务器凭据。

**II）OCPP标准中薄弱的身份验证策略**

按照OCPP协议标准及其1.6J版本的安全扩展，CSMS提供商可以使用以下三种方法之一来验证充电站的身份：1）单独的充电站身份；2）充电站身份和凭据；3）充电站身份和客户端证书。使用第一种方法可能会让网络攻击者得以从有效的充电站劫持连接，并代表该连接搞破坏。

在大多数情况下，CSMS提供商已经过配置，以执行上述第一种薄弱的身份验证方法。

当充电站使用WebSocket通道创建连到CSMS的OCPP连接时，充电站使用URL端点中的参数提供其身份。攻击者可以通过蛮力破解充电站身份并冒充充电站，破坏和攻击连接到同一CSMS的许多充电站。除此之外，虽然通常建议密码每30天更改一次，但充电站标识符在充电站的整个生命周期中都应该是一样的。

**缓解建议**

由于我们描述两个不同的漏洞，因此应该实施相应的缓解措施：

**I）对多条充电站连接处理不当**

当CSMS有来自单单一个充电站的多个连接时，两个连接都应该由CSMS管理，除非它通过主动发送WebSocket ping或OCPP心跳请求来确定和识别实际的“正确”连接。如果其中一条连接没有响应，CSMS应该会终止它。如果两条连接都有响应，运营商应该能够直接终止恶意连接，或通过与CSMS集成的网络安全模块来终止恶意连接。

值得一提的是，在一些情况下，由于蜂窝网络接收问题、重新连接后断电、关闭所有已连接的充电站等原因，单单一个充电站可能同时拥有多条连接。

**II）OCPP标准中薄弱的身份验证策略**

CPO应该设置一个更强大的安全配置文件，至少有基本的身份验证措施，设置一个定制的密码，不使用出厂默认密码。执行这一策略将使网络攻击者更难利用上述漏洞。

展望未来，OCPP 2.0.1版本及其安全扩展将要求充电站凭据作为最基本的强制性安全配置文件，这可能会使上述建议变得多余。然而，版本2.0.1是新版本，仍处于采用的早期阶段。我们将密切关注这些漏洞方面的新动向。

鉴于充电站标识符是敏感内容，通常应该使用与普通密码类似的策略来保护它，比如使用Web应用防火墙限制来自同一个IP地址的失效OCPP连接的数量（限制一段时间），或者使用威胁情报源阻止来自Tor网络、可疑VPS和VPN提供商的连接。

SaiFlow的网络监控产品可以检测到EVSE网络中的异常，并预防和实时警报企图利用上述漏洞攻击充电站的活动。SaiFlow还有助于针对充电站、EVSE和分布式能源（DER）网络管理安全策略，并提供可见性和风险管理功能，允许CPO决定强制执行身份验证策略、默认凭据及其他重要的网络安全标准。

本文翻译自：https://www.saiflow.com/hijacking-chargers-identifier-to-cause-dos/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8ggHmGGA)

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