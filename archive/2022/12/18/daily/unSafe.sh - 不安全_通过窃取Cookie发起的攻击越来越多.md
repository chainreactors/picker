---
title: 通过窃取Cookie发起的攻击越来越多
url: https://buaq.net/go-140383.html
source: unSafe.sh - 不安全
date: 2022-12-18
fetch_date: 2025-10-04T01:51:17.113738
---

# 通过窃取Cookie发起的攻击越来越多

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/74708ac203d34bcd3c3ff54794d016e5.jpg)

通过窃取Cookie发起的攻击越来越多

导语：随着越来越多的企业转向使用云服务和多
*2022-12-17 11:44:0
Author: [www.4hou.com(查看原文)](/jump-140383.htm)
阅读量:48
收藏*

---

导语：随着越来越多的企业转向使用云服务和多因素身份验证，与身份和身份验证相关的 cookie 就为攻击者提供了一条新的攻击途径。

![Depositphotos_90753880_L.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832530185073.jpeg "1661832530185073.jpeg")

随着越来越多的企业转向使用云服务和多因素身份验证，与身份和身份验证相关的 cookie 就为攻击者提供了一条新的攻击途径。

凭据窃取恶意软件是各类攻击者经常使用的工具包的一部分。虽然用户帐户名和密码是凭据窃取活动的最明显目标，但越来越多地使用多因素身份验证 (MFA) 来保护基于 Web 的服务已经使该方法不再有效。越来越多的攻击者转向窃取与证书相关的“cookie”来复制当前或最近的web会话，并在此过程中绕过MFA。

最新版的 Emotet 僵尸网络只是针对浏览器存储的 cookie 和其他凭据（例如存储的登录名和在某些情况下支付卡数据）的众多恶意软件家族之一。谷歌的 Chrome 浏览器使用相同的加密方法来存储多因素身份验证 cookie 和信用卡数据——这两个都是Emotet的目标。

针对 cookie 的攻击范围很广，小到信息窃取恶意软件，例如 Raccoon Stealer 恶意软件即服务和 RedLine Stealer 键盘记录器/信息窃取程序，它们都可以通过地下论坛购买，且通常被入门者用来批量盗取cookie和其他证书，并出售给犯罪市场。

 美国艺电公司（Electronic Arts，NASDAQ: ERTS，简称EA）一名员工的 cookie 就出现了明显的泄漏。 黑客组织Lapsus$的成员声称从市场购买了一个被盗的会话 cookie，使他们能够访问 EA 的 Slack 实例；这使他们能够欺骗 EA 员工的现有登录名，并欺骗 EA 的 IT 团队成员为他们提供网络访问权限。这使得 Lapsus$ 能够获取 780 GB 的数据，包括游戏和图形引擎源代码，该企业随后利用这些数据试图勒索 EA。

对于高级攻击者来说，研究人员观察到活跃的攻击者以各种方式获取 cookie。在某些示例中，研究人员已经看到勒索软件运营商使用了与不太复杂的攻击者相同的信息窃取恶意软件的证据。但研究人员也经常看到实际攻击滥用合法的攻击安全工具，例如 Mimikatz、Metasploit Meterpreter 和 Cobalt Strike，以执行 cookie 收集恶意软件或运行从浏览器缓存中获取 cookie 的脚本。

还有一些合法的应用程序和进程可以与浏览器的cookie文件交互。研究人员在 Sophos 的遥测技术中发现了cookie-snooping检测的反恶意软件、审计工具和操作系统助手：例如，Bing 的壁纸更新程序可以访问 cookie来获取新的桌面背景。但是，在筛选出这些良性来源后，我们看到每天有数千次访问浏览器 cookie 的尝试超出了良性软件行为的范围。有时，随着特定活动的启动，这些检测结果会急剧上升。此外，一些使用 cookie 的合法应用程序可能会泄露它们，从而将令牌暴露给攻击者。

**进入存储cookie的文件**

浏览器将 cookie 存储在文件中，对于 Mozilla Firefox、Google Chrome 和 Microsoft Edge，该文件是用户配置文件文件夹中的 SQLite 数据库。类似的SQLite文件存储浏览器历史记录，网站登录和自动填充这些浏览器的信息。其他连接到远程服务的应用程序有自己的cookie存储库，或者在某些情况下可以访问web浏览器的cookie存储库。

数据库中每个 cookie 的内容都是参数和值的列表，一个键值存储，用于标识与远程网站的浏览器会话，在某些情况下，还包括在用户身份验证后由网站传递给浏览器的令牌。其中一个键值对指定cookie的过期时间，即cookie在必须更新之前的有效时间。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832556619762.png "1661832556619762.png")

cookies.sqlite 文件中的一些 cookie

窃取cookie的原因很简单：与web服务身份验证相关的cookie可能被攻击者用于“传递cookie”攻击，试图伪装成最初向其发出cookie的合法用户，并在没有登录挑战的情况下获得对web服务的访问权。这类似于“传递哈希”攻击，它使用本地存储的身份验证哈希来访问网络资源，而无需破解密码。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832565931973.png "1661832565931973.png")

合法的网络服务活动

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832574191996.png "1661832574191996.png")

“传递cookie”攻击是如何发起攻击的

这可能导致对web服务(如AWS或Azure)、软件即服务和协作服务的利用，以进一步暴露或横向移动数据，如商业电子邮件泄露、访问云数据存储，或使用劫持的Slack会话引诱其他受害者下载恶意软件或暴露其他可用于访问的数据。

许多基于web的应用程序执行额外的检查以防止会话欺骗，例如根据发起会话的位置检查请求的IP地址。但是，如果 cookie 被同一网络内的手动键盘攻击者使用，那么这些措施可能不足以阻止攻击。而为桌面和移动结合使用而构建的应用程序可能不会始终如一地使用地理位置。

有些cookie窃取攻击可能完全从目标本身的浏览器中远程发起。HTML注入攻击可以使用插入易受攻击的网页的代码来利用其他服务的 cookie，这允许访问目标在这些服务上的个人信息，并允许更改密码和电子邮件。

**盗取cookie 的成本收益**

通常，恶意软件运营商会使用付费下载服务和其他无针对性的方法，以低成本和不费力的方式收集尽可能多的受害者 cookie 和其他相关凭据。这种类型的窃取器部署非常类似于 Raccoon Stealer 和我们看到的其他恶意软件活动，这些恶意软件活动通过 dropper 来传播。

ISO 或 ZIP 文件中的恶意软件包通过搜索引擎优化提升的恶意网站作为盗版或“破解”商业软件包的安装程序。基于 ISO 的传播包也被广泛用于代替恶意软件垃圾邮件活动中的恶意文档，这主要是因为微软最近屏蔽了来自互联网的Office文件中的宏。

研究人员在一个大学网络上看到的“下载即服务”示例中，窃取的恶意软件包含在一个从网站下载的虚假软件安装程序中，很可能是一个广告盗版商业软件。安装程序通过用户下载的 300 兆 ISO 文件的形式传播，大型 ISO 文件经常被用于阻止恶意软件检测软件的文件扫描。

ISO 包含 BLENDERINSTALLER3.0.EXE，这是一个来自另一个软件包的重新利用的软件安装实用程序。该释放程序使用 PowerShell 命令和使用 AutoIT（一种经常被恶意软件运营商滥用的合法工具）创建的可执行文件安装多个文件，以从 .ISO 中提取恶意软件，并从 Discord 的内容传播网络下载其他恶意软件文件。然后，恶意软件包通过 .NET 进程（使用 .NET 框架中的 jsc.exe）注入一系列命令，以从 Chrome 中获取 cookie 和登录数据。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832583311611.png "1661832583311611.png")

一个虚假的安装程序/信息窃取cookie程序

**高度复杂的攻击过程**

恶意垃圾邮件还与其他伪装附件一起使用，通常针对特定行业或国家的企业。 2021 年 10 月，一名土耳其计算机用户收到了一封电子邮件，其附件是一个 XZ压缩文件。这包含一个伪装的可执行文件，“ürün örnekleri resmi pdf.exe”（翻译为“产品样本图像 pdf.exe”）。该可执行文件是一个使用 Delphi 编程语言（称为“BobSoft Mini Delphi”）构建的自解压恶意软件dropper。

这个dropper依次安装了几个可执行程序。第一个是合法的Microsoft Visual Studio组件(msbuild.exe)。 MSBuild 通常用于编译和执行编码项目，它可以在命令行上传递项目文件或包含脚本的 XML 文件，并启动它们。由于该文件是受信任的 Microsoft 二进制文件，因此可以将其打包到 dropper 中，以掩盖恶意软件的恶意性质。

第二个可执行文件是从 Discord 内容传播网络中检索并解密的，它是 Phoenix 键盘记录器，一个信息窃取者。 QuasarRat 也在某个时候被释放，这是一个用 C# 编写的远程访问工具。

在接下来的一周中，攻击者使用安装的QuasarRAT启动了Phoenix信息窃取程序并通过 MSBuild 执行命令。 MSBuild 构建和执行的命令访问了目标设备上的 cookie 文件。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832592210371.png "1661832592210371.png")

Malspam / Phoenix 窃取的过程

**有针对性的利用**

窃取 cookie 不仅仅是一项自动化活动。在某些情况下，这也是积极的攻击者寻求加深对目标网络渗透的努力的一部分。在这些情况下，攻击者利用网络上的攻击入口来部署利用工具，并使用这些工具来传播他们的访问权限。随着越来越多的有价值的数据从网络转移到云服务中，这些攻击者通过窃取cookie和抓取web登录数据来增加这些服务的横向移动。

研究人员在2022年6月发现了一个这种类型的长期攻击活动，其中窃取cookie是持续数月的 Cobalt Strike 和 Meterpreter 活动的一部分。攻击者专门针对 Microsoft Edge 浏览器中的 cookie。首先，他们能够使用 Impacket 漏洞利用工具包通过 Windows SMB 文件传输从初始入口点传播，将 Cobalt Strike 和 Meterpreter 释放到网络内的目标计算机上。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832602848942.png "1661832602848942.png")

窃取cookie

接下来，攻击者在目标系统上放置了一个合法 Perl 脚本解释器的副本，以及之前基于 Impacket 的攻击中看到的 Perl 脚本文件（名为 c）和批处理文件（execute.exe）。然后他们使用 Meterpreter 传递以下命令字符串：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220830/1661832612138947.png "1661832612138947.png")

Perl脚本访问目标计算机上的cookie文件，并将内容输出到一个名为\_output的临时文件。该批处理文件将 \_output 的内容传回给攻击者并删除了 Perl 脚本。其余的 shell 命令关闭了屏幕输出，删除了批处理文件，并终止了命令 shell。

这三个示例仅代表 cookie 窃取网络犯罪的冰山一角。窃取信息的恶意软件越来越多地将窃取cookie作为其功能的一部分，而低成本高收益使得销售窃取的cookie成为一项可行的业务。但更有针对性的攻击者也以 cookie 为目标，他们的活动可能无法被简单的反恶意软件防御检测到，因为他们滥用了合法的可执行文件，包括已经存在和作为工具带来的合法可执行文件。

如果没有这么多应用程序使用长期访问 cookie，那么 cookie 窃取几乎不会构成威胁。例如，Slack结合使用持久cookie和特定于会话的cookie来检查用户的身份和身份验证。当浏览器关闭时，会话cookie会被清除，但其中一些应用程序(如Slack)在某些环境中仍然无限期地打开。这些cookie过期的速度可能不够快，无法防止被盗时被人利用。如果用户不关闭会话，与一些多因素身份验证相关联的单点登录令牌可能会造成同样的潜在威胁。

定期清除浏览器的cookie和其他认证信息可以减少浏览器配置文件提供的潜在攻击面，企业可以使用一些基于 Web 的平台的管理工具来缩短 cookie 保持有效的允许时间范围。

但强化cookie政策是有代价的。缩短cookie的生命周期意味着用户需要进行更多的重新身份验证。而且，一些利用基于Electron或类似开发平台的客户端的基于web的应用程序可能有它们自己的cookie处理问题。例如，他们可能有自己的 cookie 存储，攻击者可以在 Web 浏览器存储的上下文之外专门针对这些存储。

本文翻译自：https://news.sophos.com/en-us/2022/08/18/cookie-stealing-the-new-perimeter-bypass/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?E6PuUXfT)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/08e17cf73766d5d9a8913812b8d519d8.jpg)

  通过窃取Cookie发起的攻击越来越多](https://www.4hou.com/posts/QLKl)
* [![](https://img.4hou.com/images/9dadd252f33722c337e7129bf20ec03e.jpg)

  Zerobot——新的基于Go语言编写的僵尸网络已大肆活动](https://www.4hou.com/posts/q817)
* [![](https://img.4hou.com/images/WX20221211-193256@2x.png)

  以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（二）](https://www.4hou.com/posts/mX9E)
* [![](https://img.4hou.com/images/37b58172a31e6a47b42384a9adda061e.png)

  MINDSHARE：使用BINARY NINJA分析BSD内核的未初始化内存泄露（下）](https://www.4hou.com/posts/3JPn)
* [![](https://img.4hou.com/images/1660208574132702.jpeg)

  DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（上）](https://www.4hou.com/posts/O9LL)
* [![](https://img.4hou.com/images/微信截图_20221206113239.png)

  MINDSHARE：使用BINARY NINJA分析BSD内核的未初始化内存泄露（上）](https://www.4hou.com/posts/2JQP)

![]()

文章来源: https://www.4hou.com/posts/QLKl
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)