---
title: 通过DeathNote活动发现的Lazarus组织的最新攻击趋势
url: https://www.4hou.com/posts/NKxL
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-19
fetch_date: 2025-10-04T11:32:39.861944
---

# 通过DeathNote活动发现的Lazarus组织的最新攻击趋势

通过DeathNote活动发现的Lazarus组织的最新攻击趋势 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 通过DeathNote活动发现的Lazarus组织的最新攻击趋势

xiaohui
[趋势](https://www.4hou.com/category/observation)
2023-04-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)179943

收藏

导语：研究人员将在本文中重点介绍一个研究人员称之为DeathNote的活动。

Lazarus又名APT38，是一个知名的朝鲜语APT组织。主要负责以获得外汇为目的的攻击。自从2007年第一次出现后，该组织就非常活跃。早期主要是针对美国、韩国进行政治攻击，后续攻击目标渐渐扩大到印度、菲律宾、越南、孟加拉等亚洲及欧洲国家。2007年攻击韩国政府网站；2014年攻击Sony公司网站；2016年入侵Bangladeshi银行，等等，不过真正让Lazarus“一球成名”还是2014年的索尼影业入侵事件，至此之后，Lazarus逐渐衍变成了一个全球性的黑客组织，先后导演了入侵孟加拉国央行账号、使用WannaCry大范围勒索、攻击5大数字货币交易所、破坏印度KNPP核电站的重大安全事件，甚至他们发布发布的一些黑客工具也随着流行起来。

研究人员将在本文中重点介绍一个研究人员称之为DeathNote的活动，这是因为负责下载额外有效负载的恶意软件名为Dn.dll或Dn64.dll，该活动也被称为“Dream Job”或”NukeSped”。在过去的几年里，研究人员一直在密切监测DeathNote集群的活动，观察到他们目标的转变，以及他们工具、技术和程序的发展和改进。DeathNote是Lazarus使用的一个复杂的恶意软件集群，在2019年出现。集群（cluster）是一种较新的技术，通过集群技术，可以在付出较低成本的示例下获得在性能、可靠性、灵活性方面的相对较高的收益，其任务调度则是集群系统中的核心技术。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464726623285.png "1681464726623285.png")

DeathNote集群演变的时间线

接下来，研究人员将从技术和战略方面介绍该集群中发生的重大修改。

**持续分析DeathNote**

臭名昭著的攻击组织Lazarus长期以来一直以加密货币相关的企业为目标。在分析攻击者的活动时，研究人员注意到在一个特定的示例中，他们使用了一个经过显著修改的恶意软件。2019年10月中旬，研究人员发现了一份上传到VirusTotal的可疑文件。经过进一步调查，研究人员发现这份文件的幕后黑手自2018年10月以来一直在使用类似的恶意Word文件。恶意软件开发者使用了与加密货币业务相关的诱饵文件，如关于购买特定加密货币的问卷调查，特定加密货币的介绍，以及比特币挖矿公司的介绍。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464736531059.png "1681464736531059.png")

虚假文件

一旦受害者打开文档并启用宏，恶意的Visual Basic脚本就会提取嵌入的下载恶意软件，并使用特定参数加载。在最初的发现中，攻击者使用了两种类型的第二阶段有效负载。第一种是包含恶意后门的被操纵软件，而第二种是带有多阶段二进制感染进程的典型后门。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464746996951.png "1681464746996951.png")

感染进程

第二阶段中使用的木马应用程序伪装成真正的UltraVNC查看器。如果在没有任何命令行参数的示例下执行，它将显示一个合法的UltraVNC查看器窗口。然而，当它使用“-s {F9BK1K0A-KQ9B-2PVH-5YKV-IY2JLT37QQCJ}”参数生成时，它会执行恶意例程。另一种感染方法执行安装程序，它在Windows服务中创建并注册注入程序和后门。最后，后门被注入到一个合法进程（svchost.exe）中，并启动命令和控制（C2）操作。在这次感染中，注入合法进程的最后一个有效负载是Manuscrypt。在这一发现之前，Lazarus组织的主要目标是加密货币业务。

**国防工业成了新的重点攻击目标**

在追踪这场活动的同时，研究人员发现了2020年4月攻击目标的重大转变以及最新的感染载体。研究表明，DeathNote集群被用于针对东欧的汽车和学术部门，这两个部门都与国防工业有关。这样，攻击者把所有的诱饵文件都换成了与国防承包商和外交服务相关的工作描述。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464755154041.png "1681464755154041.png")

虚假文件

此外，攻击者还改进了感染链，在武器化文档中使用远程模板注入技术，以及使用木马化的开源PDF查看器软件。这两种感染方法都会产生相同的恶意软件(DeathNote下载程序)，该恶意软件负责上传受害者的信息，并根据C2的判断检索下一阶段的有效负载。最后，在内存中执行COPPERHEDGE变体。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464765408763.png "1681464765408763.png")

感染链

值得注意的是，一个基于开源软件的木马化PDF阅读器使用了一种有趣的技术来启动其恶意例程。它首先检索打开的PDF文件的MD5哈希，并使用检索到的MD5值对65字节的嵌入数据执行异或操作。接下来，它验证被异或的数据的第一个WORD值是否为0x4682，并检查MD5哈希值是否与被异或的数据的最后16个字节匹配。如果这两个条件都满足，则剩余的47字节值将被用作下一阶段感染的解密密钥。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464774164327.png "1681464774164327.png")

木马化的PDF阅读器的验证进程

最后，这个木马化的PDF查看器用一个诱饵PDF文件覆盖原始打开的文件，并在实现恶意软件有效负载时打开它来欺骗受害者。有效负载使用命令行参数执行，并且在Startup文件夹中创建一个快捷方式文件以确保持久性。这种感染机制证明了攻击者传递有效负载时的谨慎和精确。

**扩大目标并采用新的感染载体**

2021年5月，研究人员观察到欧洲一家提供监控网络设备和服务器解决方案的IT公司被同一集群攻击。据信，Lazarus组织对该公司广泛使用的软件或其供应链有兴趣。

此外，2021年6月初，Lazarus组织开始针对韩国的目标使用新的感染机制。值得注意的是，恶意软件的初始阶段是由在韩国广泛使用的合法安全软件执行的。据悉，该恶意软件是通过这款在韩国广泛使用的软件中的漏洞传播的。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464783187320.png "1681464783187320.png")

感染链

与之前的示例类似，最初的感染载体创建了下载恶意软件。一旦连接到C2服务器，下载程序就会根据操作员的命令检索额外的有效负载，并在内存中执行。在此期间，BLINDINGCAN恶意软件被用作内存驻留后门。虽然BLINDINGCAN恶意软件有足够的能力控制受害者，但攻击者可以手动植入额外的恶意软件，该组织可能旨在创造一种额外方法来控制受害者。检索到的加载程序的导出函数（CMS\_ContentInfo）是使用命令行参数启动的，这对于解密嵌入的下一阶段有效负载和配置至关重要。只有当参数的长度为38时，此进程才会继续。最后，在受害者身上执行该集群以前使用的COPPERHEDGE恶意软件。

大约一年后的2022年3月，研究人员发现同一个安全程序被利用，攻击者向韩国的几名受害者传播类似的下载恶意软件。不过传播的有效负载是不同的。C2操作员手动植入了一个后门两次，虽然无法获得最初植入的后门，但研究人员认为它与下一阶段的后门相同。新植入的后门能够通过命名管道通信执行检索的有效负载。此外，攻击者利用侧加载来执行Mimikatz，并使用窃取恶意软件来收集用户的击键和剪贴板数据。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464792192046.png "1681464792192046.png")

感染链

大约在同一时间，研究人员发现了拉丁美洲的一家国防承包商也被同样的后门攻破的证据。最初的感染载体与研究人员在其他国防工业目标中看到的类似，涉及使用带有精心制作的PDF文件的木马化PDF阅读器。然而，在该示例中，攻击者采用了一种侧加载技术来执行最终的有效负载。当恶意PDF文件被木马化的PDF阅读器打开时，受害者会看到上面提到的相同的恶意软件，它负责收集和报告受害者的信息，检索命令并使用管道通信机制执行它们。行动者使用此恶意软件植入额外的有效负载，包括用于侧加载目的的合法文件。

合法文件：%APPDATA%\USOShared\CameraSettingsUIHost.exe；

恶意文件：%APPDATA%\USOShared\dui70.dll；

配置文件：%APPDATA%\USOShared\4800-84dc-063a6a41c5c；

命令行：%APPDATA%\USOShared\CameraSettingsUIHost.exe uTYNkfKxHiZrx3KJ；

**对一家国防承包商的持续攻击**

2022年7月，研究人员观察到Lazarus组织成功攻击了非洲的一家国防承包商。最初的感染是通过Skype即时通讯软件发送的一个可疑的PDF应用程序。执行PDF阅读器后，它在同一目录中创建了一个合法文件（CameraSettingsUIHost.exe）和恶意文件（DUI70.dll）。这种攻击严重依赖于研究人员在前一个案例中观察到的相同的DLL侧加载技术。最初由PDF阅读器植入和执行的有效负载负责收集和报告受害者的信息，以及从名为LPEClient的远程服务器检索额外的有效负载。Lazarus组织在各种活动中多次使用这种恶意软件。他们还利用同样的DLL侧加载技术植入额外的恶意软件，能够通过后门操作。为了在系统之间横向移动，攻击者使用了一种名为ServiceMove的有趣技术。此技术利用Windows Perception Simulation Service加载任意DLL文件。根据开发者的解释：“每次启动Windows Perception Simulation Service时，都会加载一个不存在的DLL文件”。通过在C:\Windows\System32\PerceptionSimulation\目录下创建任意DLL并远程启动服务，攻击者能够在远程系统上以NT AUTHORITY\SYSTEM的身份实现代码执行。攻击者在PerceptionSimulation文件夹中创建了一个devobj.dll文件，并远程执行PerceptionSimulation服务。在启动devobj.dll文件时，它从同一文件夹解密了加密的后门文件PercepXml.dat，并在内存中执行它。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464803118240.png "1681464803118240.png")

感染链

**Post-exploitation**

在调查中，研究人员对Lazarus组织的Post-exploitation战略有了一个深入的了解。在初始感染后，攻击者执行了许多Windows命令来收集基本的系统信息，并试图找到有攻击价值的计算机，如Active Directory服务器。在横向移动之前，Lazarus组织使用众所周知的方法获得了Windows凭据，并使用了ServiceMove等公共技术。当该组织完成任务并开始窃取数据时，他们主要使用WinRAR实用程序压缩文件并通过C2通信通道传输它们。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464814142446.png "1681464814142446.png")

**总结**

在追踪了DeathNote集群及其起源后，研究人员已经确定Lazarus组织就是其幕后组织。此外，研究人员分析了通过DeathNote恶意软件向受害者发送Windows命令的示例，发现在格林尼治标准时间00:00至07:00之间执行了大量命令。根据研究人员对正常工作时间的了解，研究人员可以推断攻击者位于GMT+08或GMT+09时区。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464824144803.png "1681464824144803.png")

Windows命令的时间点变化

此外，该攻击者还在C2脚本中留下了韩语评论“정상호출”，翻译过来是“正常调用”。这进一步支持了“Lazarus是朝鲜语地区”的假设。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230414/1681464833742665.png "1681464833742665.png")

C2脚本中的朝鲜语注释

总之，Lazarus组织是一个臭名昭著、技术高超的攻击组织。研究人员对DeathNote集群的分析揭示了多年来其战术、技术和程序的快速演变。

本文翻译自：https://securelist.com/the-lazarus-group-deathnote-campaign/109490/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YMn6FGbj)

#### 你可能感兴趣的

* [![]()

  AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
* [![]()

  2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
* [![]()

  【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://...