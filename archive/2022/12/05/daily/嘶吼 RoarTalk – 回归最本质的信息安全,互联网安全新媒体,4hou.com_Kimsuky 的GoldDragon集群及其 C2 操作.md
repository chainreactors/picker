---
title: Kimsuky 的GoldDragon集群及其 C2 操作
url: https://www.4hou.com/posts/4KK1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-05
fetch_date: 2025-10-04T00:30:40.164920
---

# Kimsuky 的GoldDragon集群及其 C2 操作

Kimsuky 的GoldDragon集群及其 C2 操作 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Kimsuky 的GoldDragon集群及其 C2 操作

gejigeji
[趋势](https://www.4hou.com/category/observation)
2022-12-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)265416

收藏

导语：尽管获取服务器端对象很困难，但如果研究人员从受害者端分析攻击者的服务器和恶意软件，研究人员可以全面了解黑客组织如何操作他们的基础设施以及他们采用了什么样的技术。

![kimsuky-gold-dragon_featured-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401475254289.jpeg "1661401475254289.jpeg")

Kimsuky（也称为 Thallium、Black Banshee 和 Velvet Chollima）是一个多产且活跃的黑客组织，Kimsuky被认为是由朝鲜政府支持的组织，它与APT37和Lazarus存在一定关联，其攻击目标为韩国，但也包括美国、日本、俄罗斯等国家。

Kimsuky攻击的行业根据国家不同而有所区别，对韩国主要为政府部门、军队、智库机构、教育单位、学术团体、特定记者团队、人权组织等群体；对美国主要为智库等设施；而对俄罗斯等东欧国家则主要为军事和国防等部门。

Kimsuky最早由卡巴斯基实验室在2013年披露，而美国CERT则认为Kimsuky活动始于2012年。与大多数攻击组织一样，该组织也频繁迭代其工具。 2022 年初，卡巴斯基实验室的研究人员就观察到该组织正在攻击韩国的媒体和智囊团。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401483123686.png "1661401483123686.png")

Kimsuky的GoldDragon集群感染程序

在其新的攻击中，攻击者启动了感染链，发送了一个包含宏嵌入 Word 文件的鱼叉式网络钓鱼电子邮件。在已发现的各种不同 Word 文件的示例中，每个示例都显示了与朝鲜半岛地缘政治问题相关的不同诱饵内容。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401490697371.png "1661401490697371.png")

诱饵内容

攻击者利用 HTML 应用程序文件格式感染受害者，并偶尔使用韩文诱饵文件。在最初的感染进程启动后，一个 Visual Basic 脚本被发送给受害者。在此过程中，攻击者滥用合法的博客服务来托管具有编码格式的恶意脚本。植入的 VBS 文件能够报告有关受感染设备的信息并下载具有编码格式的其他有效负载。最后一个阶段是一个 Windows 可执行类型的恶意软件，它能够从受害者那里窃取信息，例如文件列表、用户击键和存储的 Web 浏览器登录凭据。

在研究 Kimsuky 的新型感染链（被归类为GoldDragon 集群）时，研究人员面临着几个限制：

1.在多阶段感染的分析过程中，获取下一阶段的有效负载并不容易；

2.即使研究人员连接到 C2 服务器获取有效负载，也很难获得相关的响应；

3.要弄清楚每个对象之间的联系并不容易。

然而，在跟踪 Kimsuky 组织频繁的活动时，研究人员发现了与上述感染链相关的服务器端脚本。基于这一发现再加上他们的遥测数据，研究人员能够重建该组织的整个操作方法。 Kimsuky 组织配置了多级命令和控制服务器，以及遍布全球的各种商业托管服务。可以将整个 C2 操作总结如下：

1.该攻击者向潜在受害者发送鱼叉式网络钓鱼电子邮件以下载其他文件。

2.如果受害者点击该链接，则会连接到第一阶段的 C2 服务器，并使用电子邮件地址作为参数。

3.第一阶段 C2 服务器验证传入的电子邮件地址参数是预期的，如果它在目标列表中，则发送恶意文件。第一阶段脚本还将受害者的 IP 地址转发到下一阶段服务器。

4.打开获取的文件时，它会连接到第二个 C2 服务器。

5.第二个 C2 服务器上的相应脚本检查从第一阶段服务器转发的 IP 地址，以检查它是来自同一受害者的预期请求。使用此 IP 验证方案，攻击者可以验证传入请求是否来自受害者。

6.最重要的是，攻击者依赖其他几个过程来发送下一个有效负载，例如检查操作系统类型和预定义的用户代理字符串。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401498196612.png "1661401498196612.png")

C2服务器结构

**用于恶意文件发送的 C2 脚本 (download.php)**

1.通过分析发送的恶意文件的服务器端脚本，研究人员弄清楚了该攻击者如何验证来自客户端的请求并最大限度地减少其负载的暴露。该脚本使用来自受害者的特定参数名称，因此研究人员怀疑攻击者通过电子邮件或使用其他类型的有效负载发送请求向受害者提供下载链接。

它检查受害者的 who GET 参数，who 参数包含没有域名的电子邮件地址。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401506415471.png "1661401506415471.png")

2.如果传入的请求包含一个预期的电子邮件地址，它将日期、IP地址和用户代理保存到[who]\_downhistory.txt文件。

3.如果用户代理包含 Windows，这意味着受害者是一台Windows 设备，则将进入下一步。否则，它会向受害者提供一份良性文件。

4.接下来，脚本通过检查 [who].txt 文件的存在来检查来自受害者的连接是否是第一个请求。

5.如果 [who].txt 文件不存在，则表示该文件是受害者的第一个请求，因此脚本将 IP 地址转发到另一台服务器（VBS 服务器），发送恶意文件，将受害者的信息保存到 [ who].txt文件中，包括日期、IP 地址和用户代理。

请注意，该脚本会将受害者的 IP 地址发送到另一台服务器，开发者将其命名为“VBS 服务器”。如果受害者使用适当的电子邮件地址进行连接，并且这是一个初始连接，则 C2 脚本会使用 /index.php?ip= GET 请求将该 IP 地址转发到特定服务器。将适当的受害者 IP 地址发送到远程服务器对于该攻击者的操作安全来说是一个非常重要的过程。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401514139006.png "1661401514139006.png")

查看上述 IP 发送 GET 请求的相应脚本（index.php），它是如何工作的。一旦此脚本在 HTTP 请求的 ip 参数中接收到 IP 地址，它就会从 ip 参数中提取受害者的 IP 地址并将其保存到 allow.txt 文件中。否则，它将客户端信息保存到 error.txt 文件，并将客户端重定向到mail.google.com。此外，开发者还利用naver.com、kisa.or.kr等各种合法网站和热门的电子邮件服务进行了重定向。包含适当受害者 IP 地址的 allow.txt 文件由另一个 C2 脚本引用，以验证传入请求是否有效，从而验证是否发送下一阶段的有效负载。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401521133609.png "1661401521133609.png")

此外，研究人员还发现该脚本正在发送恶意和良性文件。攻击者维护两个文件，一个是良性的（un.doc），另一个是恶意的（v.doc），并根据受害者验证步骤的结果提供适当的文件。诱饵文件的内容包括“2022年亚洲领导人会议”的议程、一种形式的酬金申请、一名澳大利亚外交官的简历等多种主题，正如我们所看到的，攻击者使用了受害者可能感兴趣的内容，例如近期将要举行的活动、特定的请求表单和知名人士的简历。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401529106507.png "1661401529106507.png")

诱饵文件

**恶意文件和发送下一阶段有效负载的方法**

发送给受害者的恶意文件包含一个用于获取下一阶段有效负载的宏，这个宏有一个简单的功能，有趣的是，它产生了几个子 Windows 命令 shell，可能是为了逃避基于行为的分析。最终，宏使用 mshta.exe 进程执行获取的有效负载，该进程旨在执行 Microsoft HTML 应用程序。以下 scriptlet 是文件中恶意宏的一部分。它包含一个远程服务器地址以获取下一阶段的有效负载。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401537177199.png "1661401537177199.png")

幸运的是，研究人员从分析中发现了相应的 C2 脚本 (h.php)。此脚本将传入流量信息保存到 log.txt 文件中，包括日期、IP 地址、用户代理和 IP MD5 哈希的最右边 20 个字符，内部称为“TID”（可能是“Target ID”的缩写）。接下来，它会检查包含已验证受害者 IP 地址的 allow.txt 文件是否存在。仅当客户端的 IP 地址存在于 allow.txt 中时，才会发送下一阶段的有效负载 h.txt。否则，该脚本会提供一个简短的 Visual Basic 脚本来终止 mshta.exe 进程。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401545156102.png "1661401545156102.png")

来自 VBS 服务器的 VBS 脚本

允许运行恶意Word文件中的宏会导致受害者获取并执行 HTML Application (.HTA) 有效负载。获取的 HTA 文件有两个主要目标：向 C2 服务器报告受害者信息和创建自动执行的计划任务。 Kimsuky 组织倾向于在各种脚本中大量重用他们的代码。例如，Visual Basic宏应用程序、Visual Basic脚本和HTML应用程序。

发送的数据包含 ProgramFiles 文件夹路径、防病毒名称、最近打开的文件列表、用户名、操作系统名称、操作系统版本、Microsoft Office 版本、.NET 框架版本、桌面文件夹中的文件列表以及用户固定的列表任务栏项目。当脚本将收集到的信息发送到 C2 服务器时，它使用 /info.php?ki87ujhy= 格式，这是 Kimsuky 组织用于指纹识别的常用 URL 格式。值得注意的是，它使用了硬编码的用户代理，包括故意拼错的单词 Chnome。在查看了服务器端脚本之后，研究人员明白了他们为什么使用 Chnome 而不是 Chrome。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401554222290.png "1661401554222290.png")

除了报告功能之外，获取的脚本还会下载了一个额外的有效负载并将其注册到持久性机制中。此代码在其他 Kimsuky 脚本中也大量使用，并通过 s.php 获取有效负载，将其保存到 defs.ini 文件，将该文件注册为Windows调度文件，在本例中名为“OneDrive Clean”。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401563111705.png "1661401563111705.png")

在本研究过程中，研究人员发现了一个相应的 C2 脚本 (s.php)，用于发送自动执行的有效负载。发送的 VBS 有效负载的主要目标是连接到合法博客，解析后，最后获得下一阶段有效载荷。有趣的是，这个 C2 脚本会根据受害者的 IP 地址生成一个博客地址。在计算受害者IP地址的MD5哈希值后，它将最后20个字符截去，并将其转换为一个博客地址。开发者的目的是为每个受害者运营一个专用的虚假博客，从而减少他们的恶意软件和基础设施的暴露。此外，该脚本会检查用户代理是否具有一个不常见的字符串 chnome。如上所述，Visual Basic 脚本使用硬编码的 chnome 用户代理名称连接到此 C2 脚本，并且该脚本检查拼写错误的用户代理以验证它是来自真实受害者的预期请求。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401571199950.png "1661401571199950.png")

根据上面的发现和分析，研究人员列出了攻击者隐藏其基础设施并使安全研究人员和自动分析系统更难获取有效负载的技巧：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401580110980.png "1661401580110980.png")

来自C2脚本的技巧

**受害者**

根据诱饵文件的内容，研究人员假设此次活动的目标是与政治或外交活动相关的人员或实体。此外，从历史上看，政治家、外交官、记者、教授一直是 Kimsuky 组织的主要目标。基于来自 C2 脚本的电子邮件地址名称，可以进一步巩固上述假设。 C2 脚本只有部分电子邮件地址，因此研究人员试图从外交和学术领域推断完整的电子邮件地址和真正的所有者。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220825/1661401588231242.png "1661401588231242.png")

**总结**

Kimsuky 是朝鲜半岛上最多产和最活跃的黑客组织之一，拥有多个集群，而 GoldDragon 是最常用的集群之一。研究人员已经看到，Kimsuky 组织不断改进其恶意软件感染方案，并采用新技术来阻碍分析。追踪这个组织的主要困难是很难获得完整的感染链。正如研究人员从这项研究中看到的那样，攻击者最近在其命令和控制服务器中采用了受害者验证方法。尽管获取服务器端对象很困难，但如果研究人员从受害者端分析攻击者的服务器和恶意软件，研究人员可以全面了解黑客组织如何操作他们的基础设施以及他们采用了什么样的技术。

本文翻译自：https://securelist.com/kimsukys-golddragon-cluster-and-its-c2-op...