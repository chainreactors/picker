---
title: 集权系列科普 | Exchange server的“高光”，就在这一篇②
url: https://www.anquanke.com/post/id/300082
source: 安全客-有思想的安全新媒体
date: 2024-10-09
fetch_date: 2025-10-06T18:48:54.166403
---

# 集权系列科普 | Exchange server的“高光”，就在这一篇②

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 集权系列科普 | Exchange server的“高光”，就在这一篇②

阅读量**269613**

|评论**1**

发布时间 : 2024-10-08 13:59:47

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

在现代企业环境中，Microsoft Exchange Server 作为一种广泛使用的电子邮件和日历服务器，承载着大量的企业通信数据。随着数字化转型的推进和电子邮件在商业活动中的核心地位，Exchange服务器的安全性变得尤为重要。然而，正因为其重要性和广泛使用，Exchange服务器也成为了攻击者的重点目标。**本文将深入探讨Exchange的攻击面，包括常见的漏洞利用方式、攻击手段**，旨在帮助企业加强其Exchange环境的安全性。

# **无Exchange凭据攻击面介绍**

如果没有目标Exchange凭据，甚至对Exchange相关信息一无所知，这时候攻击者首先会先收集目标Exchange相关信息。比如通过相关手段找到目标Exchange、Exchange的版本信息以及Exchange所在AD域的域名。为了获取邮箱账户的凭据，攻击者会利用Exchange对外暴露的接口进行暴力破解、用户名枚举。Exchange也存在一些漏洞，它们不需要攻击者提供凭据就能够执行攻击，并且影响很大。像Proxylogon、Proxyshell之类的攻击链危害严重，利用它们往往能起到事半功倍的效果。

## 信息收集

**1、Exchange信息收集**

外网发现Exchange：利用FOFA搜索引擎和特殊域名原理搜索和发现Exchange服务。

版本探测：通过访问特定路径查看源代码或使用Burpsuite抓取包来获取Exchange的版本号。

**2、服务器信息获取**

利用nmap进行HTTP NTLM认证的信息收集，获取系统相关信息。

通过MailSniper脚本获取Exchange服务器的相关信息。

**3、内网定位Exchange**

SPN扫描：使用setspn工具查询域中SPN服务来快速定位Exchange服务器。

LDAP定位：利用ldap过滤规则进行定位。

端口扫描：通过nmap进行端口发现服务，识别服务器上是否安装了Exchange。

## 暴力破解

**1、获取AD域名**

通过上文介绍的获取Exchange服务器信息的方法即可获得AD域名。这里也可以通过MailSniper.ps1来获取AD域名。

Invoke-DomainHarvestOWA -ExchHostname 192.168.60.116

**2、用户名获取**

Exchange 存在基于时间的用户名枚举问题，Exchange 2016 版本的表现为：爆破到真实存在的域用户（无论是否开通邮箱账户）时，其响应开始接收时间会更短（不是完整响应时间）。

**3、密码爆破，密码喷洒**

经过对AD域名的收集，以及用户名的获取，目前已经获取到了正确格式的用户名。为了获得用户对应的密码，接下来利用工具EBurst、ruler等工具对密码进行爆破。如果目标存在多次爆破密码锁定机制，采用密码喷洒技术来绕过锁定机制。

## 漏洞利用

Exchange Server曾爆发过众多的漏洞，一些漏洞威胁等级特别高，如果利用这些漏洞进行攻击，Exchange Server将受到严重影响。比如2021年爆发的Proxylogon和Proxyshell攻击链都能够在没有账户凭据的情况下攻击Exchange Server，最终获取到Exchange Server的system权限，进而对AD域形成重大威胁。

**1、Proxylogon**

ProxyLogon 是 CVE-2021-26855 的正式通用名称，它是 Microsoft Exchange Server 上的一个漏洞，允许攻击者绕过身份验证并冒充管理员。此漏洞与另一个身份验证后任意写入文件漏洞 CVE-2021-27065 相结合，可以造成代码执行攻击。

**2、Proxyshell**

CVE-2021-34473：

Microsoft Exchange 有一项名为 “显式登录 “的功能，通过在 URL 中提供邮箱地址，用户可以在新的浏览器窗口中合法地打开其他用户的邮箱或日历。该功能仅在用户被授予 “完全访问权限 “且目标邮箱或日历被配置为发布的情况下才提供访问权限。Exchange 的设计是将 URL 中指定的邮箱地址规范化，以识别目标。漏洞存在于将 Autodiscover/Autodiscover.json 字符串传递到 URL 中的电子邮件字段。通过传递该字符串，Exchange 没有对地址执行足够的检查，并通过其规范化过程，导致以 NT AUTHORITY/SYSTEM 身份任意访问后端 URL。

CVE-2021-34523：

Exchange PowerShell Remoting 功能原生内置在 Microsoft Exchange 中，旨在通过命令行协助管理活动。先前的漏洞允许攻击者NT AUTHORITY/SYSTEM 身份访问任意后端URL，但由于该用户没有邮箱，攻击者无法以该权限级别直接访问PowerShell后端 (/Powershell)。PowerShell后端会检查传入请求中的 X-CommonAccessToken 标头。如不存在，则使用另一种方法获取 CommonAccessToken。该方法会检查传入请求中的 X-Rps-CAT 参数，如存在，则将其反序列化为有效的 CommonAccessToken。有了先前收集的目标邮箱信息或内置邮箱的默认信息，传递有效的 X-Rps-CAT 值就变得轻而易举了。通过将此值与先前成功的访问令牌一起传递到 PowerShell 后端，攻击者就可以将 NT AUTHORITY/SYSTEM 账户降级为目标用户。该用户必须拥有本地管理权限，才能执行任意 Exchange PowerShell 命令。

CVE-2021-31207：

一旦前两个漏洞被成功利用，CVE-2021-31207 漏洞就会允许攻击者写入文件。只要攻击者能够执行任意的 PowerShell 命令，并将所需的 “Mail Import Export”角色分配给被伪造的用户（可通过执行 New-ManagementRoleAssignment来实现），就可以使用New-MailboxExportRequest 将用户的邮箱导出到特定的所需路径。

**3、CVE-2021-41349**

这是一个XSS漏洞，远程攻击者可通过注入有效载荷执行反射型XSS攻击。

# **有Exchange凭据攻击面介绍**

## 权限提升

CVE-2018-8581：

由于 Exchange 本身机制问题，在内网中，使用 CVE-2018-8581 漏洞，将管理员的 NTLM hash 中继到域控服务器上，就可以获得域管权限，实现域内提权。

CVE-2020-0688：

这个漏洞是由于Exchange服务器在安装时没有正确地创建唯一的加密密钥所造成的。具体来说，与正常软件安装每次都会产生随机密钥不同，所有Exchange Server在安装后的web.config文件中都拥有相同的validationKey和decryptionKey。这些密钥用于保证ViewState的安全性。而ViewState是ASP.NET Web应用以序列化格式存储在客户机上的服务端数据。客户端通过\_\_VIEWSTATE请求参数将这些数据返回给服务器。当攻击者通过各种手段获得一个可以访问Exchange Control Panel （ECP）组件的用户账号密码时。攻击者可以在被攻击的exchange上执行任意代码，直接获取服务器权限。

ProxyNotShell：CVE-2022-41040 和 CVE-2022-41082

一旦攻击者获得了服务器访问权，他们就会安装 webshell 以获得对网络的持久访问权。GTSC 向 Zero-day Initiative (ZDI) 报告了该漏洞，该漏洞被命名为 CVE-2022-41040 和 CVE-2022-41082，严重程度分别为关键和重要。CVE-2022-41040是服务器端请求伪造（SSRF）漏洞，CVE-2022-41082是允许在攻击者访问 Exchange PowerShell 时执行远程代码（RCE）。

CVE-2020-16875：

由于对cmdlet参数的验证不正确，Microsoft Exchange服务器中存在一个远程执行代码漏洞。成功利用此漏洞的攻击者可以在系统用户的上下文中运行任意代码。利用此漏洞需要拥有以某个Exchange角色进行身份验证的用户权限。

CVE-2020-17144：

由于程序未正确校验cmdlet参数引起。经过身份验证的攻击者利用该漏洞可实现远程代码执行。该漏洞和 CVE-2020-0688 类似，也需要登录后才能利用，不过在利用时无需明文密码，只要具备 NTHash 即可。除了常规邮件服务与 OWA外，EWS接口也提供了利用所需的方法。漏洞的功能点本身还具备持久化功能。

CVE-2023-21529：

这是一个远程代码执行漏洞。该漏洞的攻击者可针对服务器账户执行任意远程代码。攻击者利用已通过身份验证的用户，尝试通过在服务器账户上下文中触发恶意代码。

CVE-2021-24085：

此漏洞允许远程攻击者在受影响的 Microsoft Exchange Server 程序上提升权限。利用此漏洞需要进行身份验证和用户交互，因为目标必须访问恶意页面。具体漏洞存在于 Canary15 类内的 HasValidCanary 函数中。该问题导致不安全地生成可用于安装 Office-addins 的跨站点请求伪造令牌。攻击者可利用此漏洞将权限提升到管理权限。

CVE-2020-17083：

该漏洞是由于边界错误而存在的。远程用户可以在目标系统上执行任意代码。经过 Internet 身份验证的远程用户可以利用此漏洞。

ProxyToken：

VNPT ISC 的研究人员 Le Xuan Tuyen 于 2021 年 3 月向 Zero Day Initiative报告了该漏洞，微软在 2021 年 7 月的 Exchange 累积更新中修补了该漏洞。该漏洞的标识符为 CVE-2021-33766 和 ZDI-CAN-13477。利用此漏洞，未经身份验证的攻击者可对属于任意用户的邮箱执行配置操作。

## 功能滥用

**1、邮箱委托**

Exchange 邮件服务存在一种机制，可以设置权限将邮箱委托给指定用户管理使用。这种委托可以是全局的委托，可以通过后台修改；也可以是对单独文件夹进行委托，用户自行对文件夹设置。因此，当 ecp 可登录且拥有管理员权限时，就可以通过添加邮箱委托的方式，实现邮箱控制。在默认情况下，某些管理员在配置时，组用户会默认拥有对组内用户的委托管理权限。

**2、转发规则**

在获得目标邮箱的密码情况下，可登录 ecp 后台，添加全局规则持续获得此用户收件箱邮件。例如新建规则，目标用户一旦接收到邮件，都会将此邮件转发一份到配置的另一个用户。

**3、获取邮箱用户**

在获得一个有效账户后，为了长期控制，或者更全面的控制，一般会选择获取邮箱全部邮件地址列表，即全局通讯录。Exchange GlobalAddressList(全局地址列表)包含 Exchange 组织中所有邮箱用户的邮件地址，只要获得 Exchange 组织内任一邮箱用户的凭据，就能够通过GlobalAddressList导出其他邮箱用户的邮件地址。

**4、Exchange的邮件导出和邮件搜索**

在渗透测试中，如果我们获得了Exchange服务器的管理权限，下一步就需要对Exchange服务器的邮件进行搜索和导出。

● 直接在Exchange服务器上执行管理邮件的命令

● 导出邮件

● 邮件搜索

**5、TransportAgent后门安装**

ESET研究发现了一个专门针对Microsoft Exchange的恶意软件LightNeuron，使用一种从未见过的持久性技术：Transport Agent，能够实现以下功能：

● 阅读和修改通过邮件服务器的任何电子邮件

● 撰写并发送新电子邮件

● 阻止任何电子邮件：原始收件人将不会收到电子邮件

可以用来扩展和修改Exchange的传输行为，以自定义消息的接受，拒绝，路由和传递，以及在各种类型的内容之间进行转换。Transport Agents作为Exchange的插件，能够对Exchange的传输行为进行扩展和修改，例如读取、修改和删除传输的每一份邮件。

**6、攻击域管**

在 Exchange 安装完后，域内会添加一个名为 Microsoft Exchange Security Groups 的 OU，其包括两个特殊的组：Exchange Windows Permissions 和 Exchange Trusted Subsystem，后者隶属于前者。所有的 Exchange 服务器都会加入 Exchange Trusted Subsystem 组，也就是 Exchange 服务器都继承了 Exchange Windows Permissions 组的权限，而该组拥有对域分区的 WriteDacl 权限，且可以继承。因此，在拿下 Exchange 服务器后，可以利用 Exchange 机器账户对域分区添加任意 ACL 进行提权，比如添加 Dcsync 权限导出域内所有 Hash。

# **攻击案例一**

2023年攻防演练期间，攻击者通过OA系统信息泄漏漏洞获得企业所有员工的用户名，随后攻击者把用户名制作成不同格式的用户名字典，对Exchange服务器进行密码喷洒，结果获取一个普通账户的凭据。基于已获得的普通权限凭据，利用CVE-2023-21529漏洞攻击Exchange服务器，获取Exchange服务器的控制权。由于有了Exchange机器对域对象具有WriteDACL权限，所以利用了ACL攻击，获取了域管权限。最后利用邮件委派获取其他人的联系方式等敏感信息。

![]()

# **攻击案例二**

2022年攻防演练期间，攻击者首先通过钓鱼攻击，获得了一台域内终端的控制权。以此为跳板，利用CVE-2018-8581漏洞触发Exchange带上Exchange机器账户的凭据回连跳板机，然后跳板机将此凭据中继到域控的LDAP，给指定用户添加DCSync权限。之后拿着研发的凭据登录登录研发服务器，获取到重要资料。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**御守实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300082](/post/id/300082)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Exchange server](/tag/Exchange%20server)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t015bd9ae31452d2c73.png)御守实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t015bd9ae31452d2c73.png)](/member.html?memberId=159343)

[御守实验室](/member.html?memberId=159343)

网星安全御守实验室（Amulab）是隶属于网星安全（中安网星）的纯技术研究团队。主要职能包括横向移动研究、AD域安全研究、Windows安全研究等前瞻攻防技术预研、工具孵化，为产品输出安全能力。

* 文章
* **21**

* 粉丝
* **42**

### TA的文章

* ##### [网星安全AWS攻防方案，重磅发布！](/post/id/300331)

  2024-10-08 14:03:06
* ##### [集权系列科普 | Exchange server的“高光”，就在这一篇②](/post/id/300082)

  2024-10-08 13:59:47
* ##### [集权系列科普 | 想了解AD&攻击面？独家干货放送（上）](/post/id/299747)

  2024-09-03 16:06:22
* ##### [集权攻击避实击虚- AD域安全解析](/post/id/287523)

  2023-03-21 16:30:16
* ##### [Kubernetes攻击频发，如何避免集群“裸奔”](/post/id/287522)

  2023-03-18 16:30:36

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### ...