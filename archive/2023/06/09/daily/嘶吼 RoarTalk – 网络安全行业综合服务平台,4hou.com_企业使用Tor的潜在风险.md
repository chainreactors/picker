---
title: 企业使用Tor的潜在风险
url: https://www.4hou.com/posts/7Jyj
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-09
fetch_date: 2025-10-04T11:46:50.798632
---

# 企业使用Tor的潜在风险

企业使用Tor的潜在风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 企业使用Tor的潜在风险

luochicun
[技术](https://www.4hou.com/category/technology)
2023-06-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)160681

收藏

导语：攻击者以各种方式利用Tor进行勒索软件攻击。

下图可以帮我们了解Tor匿名过程。

首先，我们假设使用者已经构建了一个 Tor路径，这意味着计算机已经选择了三个Tor节点（运行Tor软件的服务器）来中继消息并获得了每个节点的共享密钥。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230608/1686192111147865.png "1661930648129012.png")

计算机首先对私有数据进行三层加密（上图中的步骤 1），这也是洋葱名称的由来。之后，使用者的计算机以相反的顺序加密数据：首先使用最后一个退出节点的密钥 (Kn3)，然后使用中间中继节点的密钥 (Kn2)，最后使用保护节点的密钥 (Kn1)。保护节点接收到数据后，使用 Kn1 去除最外层的加密，并将解密的消息发送到中继节点。中间节点使用 Kn2 删除下一层，并将其中继到退出节点。最后，退出节点使用 Kn3 解密消息并将原始数据发送到 Web 服务器（在本例中是peel-the-orange[.]com）。分层加密实现了保密性，并限制了参与通信的人员，因为只有知道密钥的节点才能解密消息。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230608/1686192111364650.png "1661930658192624.png")

上图汇总了哪些节点知道哪些其他节点。守卫节点（guard node）知道使用者是谁以及下一个接收使用者消息的节点，即中间中继节点。但是，守卫节点不知道最后的退出节点和使用者的最终目标地，因为只用Kn1解密，此时入口节点的消息仍然是乱码。中继节点知道的最少。它不知道谁是原始发送者或最终目标地，只知道入口和退出节点。退出节点知道中间中继节点和目标服务器，而目标服务器只知道退出节点。

返回使用者的消息以类似的方式传回，每个节点使用与使用者共享的密钥添加一层加密。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230608/1686192112177432.png "1661930668718461.png")

上图是全球Tor网络中，使用者和监控者的示意图。Emilia代表使用者，Lemonheads代表监控者。当使用者使用Tor时，监控者只能观察到使用者与入口节点的连接。即使他们对所传递的消息有完全的全局可见性，他们也很难跟踪使用者的消息，因为它们混入了所有Tor用户的流量，而且每次消息传递到另一个节点时，加密层都会发生变化。如前所述，如果使用者使用单一的 VPN 提供商，它将知道使用者访问的网站。此外，监控者可以观察来自 VPN 服务器的传入和传出消息，并可能确定使用者正在访问哪些网站。

一个奇怪的问题是：使用者如何在不暴露身份的情况下与Tor节点共享密钥？要解决这个问题需要分两步。

首先，两个节点如何在任何人都可以读取所有通信的公共网络上合作创建一个只有他们知道的密钥？答案是 Diffie-Hellman key Exchange (DHE) 协议。首先，双方需要各自生成他们自己的私有秘密，并将其组合成只有他们两个人可以计算的共享秘密(Kn1。在实际应用中，基于椭圆密码学的认证ECDHE来解决vanilla DHE 的问题。

此时，使用者可以访问每个Tor节点，并分别与它们建立一个密钥，但这会让每个节点都知道使用者的身份。问题的第二部分是使用DHE建立密钥。使用者的计算机并没有直接与所有三个节点通信，而是在与入口节点建立密钥后，用 Kn1 对所有消息进行加密，并通过入口节点将消息发送到中继节点。这意味着中继节点只知道入口节点而不知道使用者。同样，使用者的计算机用 Kn2 和 Kn1 加密 DHE 消息，并将它们通过守卫节点和中继节点发送到退出节点。

不幸的是，在使用者了解Tor并开始使用它之后，监控者开始审查与公开宣传的Tor节点 IP 的连接。为了安全，开发者开始运行秘密的Tor网桥（私下替换公开宣传的入口节点），并一次只向少数用户提供小批量的服务。

对使用者来说，更糟糕的是，研究人员发现他们可以通过扫描整个IPv4空间来发现Tor网桥。

总之，对于使用者来说，这是一场持续的猫捉老鼠游戏。

**Tor 的恶意和良性示例**

使用Tor的用户可以可能是坏人也可能是好人。不管怎样，人们可能会使用Tor访问受地理限制的内容或规避政府的审查或机构的内容封锁。例如，如果Tor流量没有被阻止，高级URL过滤的客户无法阻止使用Tor的员工规避基于分类的过滤。

Tor 还以其洋葱服务而闻名。例如，Tor 有助于隐藏多个举报人网站，用户可以在这些网站上举报其组织中的非法和不道德活动，而不必担心遭到报复。洋葱服务通过允许用户仅使用Tor进行连接来保护其 IP 地址的秘密。这个想法是，用户和洋葱服务都通过Tor连接，它们在中间的一个集合点（一个Tor节点）相遇。虽然这些洋葱服务的目的不一定是为了使非法活动成为可能，但过去的研究发现，Tor用户建立了很大一部分或大部分用于非法目的的隐藏服务。然而，只有 6.7% 的Tor用户连接到隐藏服务。与洋葱服务相比，绝大多数用户访问不太可能是非法的那些网站。例如，超过 100 万人使用Tor查看 Facebook 的隐藏服务，该服务允许来自政府审查的地区的访问。

攻击者也可以利用Tor进行他们的活动。攻击通常从侦察开始，攻击者探索目标的基础设施并搜索潜在漏洞，例如，通过扫描开放的端口和运行的服务。通过使用Tor，攻击者可以隐藏他们的位置，并将他们的活动分布到多个退出节点。

同样，攻击者可以使用Tor进行攻击的后续步骤，例如利用侦察期间发现的漏洞、更新目标设备上的恶意代码、命令和控制通信以及数据泄露。Tor的其他恶意用途包括 DoS 攻击、虚假帐户创建、垃圾邮件和网络钓鱼。

攻击者以各种方式利用Tor进行勒索软件攻击。在 Ryuk 和 Egregor 勒索软件的示例中，名为 SystemBC 的初始远程访问木马 (RAT)使用Tor隐藏服务作为命令和控制通信的后门。在构建木马攻击时，使用Tor隐藏服务进行命令和控制非常有用，因为这使得命令和控制难以取消并保持其可访问性，除非使用各种安全产品阻止与Tor的连接。Gold Waterfall 攻击组织在安装 DarkSide 勒索软件时也使用Tor进行后门通信。Tor隐藏的基于服务的泄漏网站也被用来托管与 DarkSide 和Ranzy locker相关的被盗数据。此外，DoppelPaymer还利用Tor支付网站收取赎金。 Unit 42 最近发表了关于 Cuba勒索软件和BlueSky Ransomware勒索软件的研究，前者使用基于Tor隐藏服务的泄漏网站，后者发送勒索通知，指示目标下载Tor浏览器，作为获取文件访问权的一部分。

Tor 的使用并不特定于针对服务器和个人计算机的恶意软件。一种Android恶意软件还使用Tor隐藏服务作为命令和控制服务器，使攻击变得困难。

此外，研究人员发现Tor被用来发送各种恶意垃圾邮件，通常以评论和约会垃圾邮件的形式出现。研究人员还发现，通过Tor发送的电子邮件可能包含严重的威胁，包括 AgentTesla RAT 的传播、以 Adobe 为主题的网络钓鱼电子邮件和 Covid-19 贷款诈骗。

**使用Tor的攻击者是如何被抓住的？**

虽然Tor提供了比许多其他解决方案更好的匿名性，但它并不完美。

2013 年，一名哈佛学生试图通过发送炸弹攻击来逃避他的期末考试。他通过Tor连接到一个匿名电子邮件提供商以隐藏他的身份。然后他使用这个电子邮件提供商发送炸弹攻击。虽然他正确使用了 Tor，但当他从哈佛的 wifi 网络连接到Tor时，他犯了一个大错误。该生的错误是Tor只隐藏了使用者所做的事情，而不隐藏使用Tor的事实。学校管理者从电子邮件的标题中发现有人使用Tor发送电子邮件。他们从那个位置检查了网络日志，看看是否有学生在学校收到邮件的时间内连接到 Tor。

臭名昭著的洋葱服务“丝绸之路”(Silk Road)的创始人罗斯·乌布里希(Ross Ulbricht)也正确使用了洋葱网络，但他在操作上犯了另一个错误，导致他被捕。丝绸之路是当时最著名的暗网市场，卖家提供毒品、假钞、伪造身份证件和枪支等商品。美国联邦调查局(FBI)发现，早些时候，有人用“薄荷糖”(Altoid)这个笔名四处推销丝绸之路。8个月后，Ulbricht用这个笔名发布了招聘广告，联系人是rossulbricht@gmail[.]com ，以聘请一名 IT 专家，来帮助“一家由风投支持的比特币创业公司”。据报道，联邦调查局随后能够访问Ulbricht使用的 VPN 服务器的日志和谷歌访问他的 Gmail 地址的日志。这两项记录都指向了旧金山的一家网吧，并导致了他的被捕。

攻击者可以通过其他方法对Tor用户进行去匿名化，例如，通过使用 JavaScript 或设置非法Tor节点（现在可能正在现实世界中发生）。关键是，虽然Tor确实提供了一定程度的匿名性，但用户可以通过操作错误泄露他们的身份，或者如果追查者确定并拥有资源，他们可以被识别。

**如何阻止攻击者利用Tor**

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230608/1686192112131611.png "1661930681771089.png")

如何使用不同的方法来阻止攻击者利用 Tor。标记为 Part 1\* 和 2\* 的单元格表示需要同时使用这两种解决方案来保护企业。

要阻止进出Tor网络的流量，我们可以阻止公开发布的Tor IP，或者识别和阻止Tor应用程序流量。上图总结了每种阻止机制的示例。首先，我们可以使用已知退出节点 IP 列表来阻止来自Tor的攻击，例如侦察、利用、命令和控制通信、数据泄露和 DoS 攻击。使用已知保护节点 IP 列表，我们可以阻止我们的用户及其设备向Tor发送流量，并防止数据泄露、命令和控制通信、规避地理限制和内容阻止以及访问 .onion 网站。

由于Tor网桥节点列表未知，基于保护节点 IP 的阻止只是部分解决方案。相反，我们可以使用 Palo Alto Networks 流量分类系统 App-ID 直接检测和阻止Tor流量。除了使用可用的保护和桥接节点 IP，App-ID 还会查看连接的特征，例如使用的密码套件或数据包的大小来识别Tor流量。

此外，攻击者可以从Tor网络或受感染的设备发起数据泄露以及命令和控制通信。因此，要阻止这些攻击，最好同时使用基于退出 IP 和基于流量分析的阻止。

Palo Alto Networks 收集所有公开宣传的Tor退出 IP，并利用它们建立一个电路来测试它们是否有效。已知且有效的Tor退出列表构成了Palo Alto Networks 预定义的Tor退出 IP 外部动态列表。

使用Tor退出 IP 外部动态列表和 App-ID，研究人员观察到企业使用Tor很常见，因为我们在一个月内确定了 204 个客户网络中 691 台设备上的 6617473 个会话。

除了阻止Tor流量外，企业还可以利用 Cortex XDR 等端点保护来覆盖基于Tor的攻击。 Cortex XDR 基于用户和实体行为分析 (UEBA)、端点检测和响应 (EDR)、网络检测和响应 (NDR) 以及云审计日志来检测以下活动：

与Tor中继服务器的可能网络连接；

来自Tor的成功 VPN 连接；

从Tor成功登录；

来自Tor退出节点的可疑 API 调用；

来自Tor的 SSO 成功登录。

**总结**

Tor 为其用户提供匿名性，不过匿名性经常被不法分子利用，一方面，Tor 可以帮助人们改善隐私和保护举报人。另一方面，Tor 可用于各种恶意活动，包括匿名侦察、数据盗窃、逃避地理限制、规避内容阻止以及在暗网上运行非法市场。

由于网络犯罪分子经常将Tor用于恶意目标，因此建议在企业环境中禁止使用Tor。根据调查，企业使用Tor很常见，研究人员在一个月内发现了 204 个客户网络上的 691 台设备的 6617473 个会话。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230608/1686192112297638.png "1661930694854037.png")

Palo Alto Networks 提供了两种用于阻止Tor流量的解决方案，作为攻击预防的一部分，最好一起使用。他们向客户提供经过验证的内置Tor退出 IP 外部动态列表，他们可以使用该列表来阻止与Tor退出节点的连接。此外，可以使用 Palo Alto Networks 流量分类系统 App-ID 阻止企业网络中的Tor流量。此外，客户可以利用 Cortex XDR 来提醒和响应端点设备、网络或云中的Tor相关活动。

本文翻译自：https://unit42.paloaltonetworks.com/tor-traffic-enterprise-networks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OO3iwouo)

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

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

这个家伙很懒,什么也没说!

#### 最新文章
...