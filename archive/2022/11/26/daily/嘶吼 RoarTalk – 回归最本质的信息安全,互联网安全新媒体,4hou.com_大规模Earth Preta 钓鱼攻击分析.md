---
title: 大规模Earth Preta 钓鱼攻击分析
url: https://www.4hou.com/posts/xjEP
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-26
fetch_date: 2025-10-03T23:48:26.974257
---

# 大规模Earth Preta 钓鱼攻击分析

大规模Earth Preta 钓鱼攻击分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 大规模Earth Preta 钓鱼攻击分析

luochicun
[技术](https://www.4hou.com/category/technology)
2022-11-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)141794

收藏

导语：在这篇文章中，我们讨论了Earth Preta的活动及其策略、技术和程序（TTP），包括新的安装程序和后门。

Earth Preta组织从3月开始就在全球肆虐，其开发的恶意软件家族包括TONEINS、TONESHELL和PUBLOAD。Earth Preta又名Mustang Panda或Bronze President。该组织的攻击对象包括但不限于缅甸、澳大利亚、菲律宾、日本等国家。

趋势科技的研究人员最近发现Earth Preta滥用虚假谷歌账户，通过鱼叉式网络钓鱼电子邮件传播恶意软件，这些电子邮件最初存储在一个存档文件（如rar/zip/jar）中，并通过Google Drive链接传播。然后诱骗用户下载并触发恶意软件执行TONEINS、TONESHELL和PUBLOAD。PUBLOAD之前已被报道，我们会在本文将其与TONEINS和TONESHELL联系起来，后者是该组织在其活动中新使用的恶意软件家族。

此外，攻击者利用不同的技术来逃避检测和分析，如代码混淆和自定义异常处理程序。我们还发现，鱼叉式网络钓鱼邮件的发件人和Google Drive链接的所有者是相同的。根据用于诱骗受害者的样本文件，我们还认为，攻击者能够对目标组织进行研究，并可能事先对其进行破坏，从而使其变得熟悉，这在之前被泄露的账户名称的缩写中有所显示。

在这篇文章中，我们讨论了Earth Preta的活动及其策略、技术和程序（TTP），包括新的安装程序和后门。

**受害目标分析**

根据我们对这一威胁的监测，诱饵文件是用缅甸文写成的，内容是“仅限内部”。文件中的大多数主题都是国家间有争议的问题，包含“机密”或“机密”等词 ，这可能表明，攻击者将缅甸政府作为他们的第一个立足点。这也可能意味着，攻击者在攻击之前就已经对特定的政治对象进行了破坏，Talos研究人员此前也注意到了这一点。

攻击者利用窃取的文件作为诱饵，诱骗与缅甸政府机构有合作关系的目标组织下载并执行恶意文件。受害者涵盖了世界范围内广泛的组织和垂直领域，其中亚太地区的受害者集中度更高。除了在缅甸开展合作的政府办事处外，随后的受害者还包括教育和研究行业等。除了以涉及特定组织的正在进行的国际事件为诱饵之外，攻击者还用与色情材料有关的标题引诱个人用户下载。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175753177784.png "1669175753177784.png")

Earth Preta的目标行业分布

**攻击进程**

Earth Preta使用鱼叉式网络钓鱼邮件作为攻击的第一步。如前所述，一些邮件的主题和内容讨论地缘政治话题，而其他邮件可能包含耸人听闻的主题。我们观察到，我们分析的所有电子邮件中都嵌入了Google Drive链接，这表明用户可能会被诱骗下载恶意文件。文件类型包括压缩文件，例如.rar、.zip和.jar。访问链接后，我们了解到文件包含恶意软件TONEINS、TONESHELL和PUBLOAD。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175761214618.png "1669175761214618.png")

有关会议记录的电子邮件文档，可能是从先前的攻击中窃取的

**鱼叉式网络钓鱼电子邮件**

通过分析电子邮件的内容，发现Google Drive链接被用来诱骗受害者。电子邮件的主题可能为空，或者可能与恶意文件同名。攻击者没有将受害者的地址添加到电子邮件的“收件人”标题中，而是使用了假电子邮件。同时，真实受害者的地址被写在“CC”标题中，可能会逃避安全分析，延缓调查。使用开源情报(OSINT)工具GHunt来探测“收件人”部分中的那些Gmail地址，我们发现了这些虚假账户，其中几乎没有信息。

此外，我们观察到一些发件人可能是来自特定组织的电子邮件帐户。受害者可能会相信这些邮件是由可信的合作伙伴发送的，这增加了收件人选择恶意链接的机会。

**虚假文件**

我们还发现了一些与缅甸政府对象相关或与之合作的组织有关的虚假文件。其中包含了缅甸和中国大使馆之间的粗略会面时间表。另一份文件与日本科学促进协会（JSPS）有关，该协会为研究人员提供在日本进行研究交流的机会。值得注意的是，压缩文件附件中主要是图片。用于下一层侧加载的恶意DLL和可执行文件也包含在其中。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175770377480.png "1669175770377480.png")

有关政府会议(左)及海外研究交流(右)的虚假文件样本

此外，还有其他内容主题多样的诱饵文件，包括地区事务和色情内容。但是，当受害者打开这个文件夹中的假文档文件时，没有相应的内容出现。

**其他攻击途径**

我们观察到至少三种类型的攻击途径，包括通过Google Drive链接、Dropbox链接或其他托管文件的IP地址分布在世界各地的30多个诱饵文件。在我们收集的大多数样本中，都有合法的可执行文件，以及侧加载的DLL。诱饵文件的名称在每个案例中都有所不同。在接下来的部分中，我们将以其中一些为例，介绍每一个的TTP。

**DLL侧加载**

在该示例中，有三个文件：“~”， Increasingly confident US is baiting China.exe和libcef.dll。值得注意的是，诱饵文件和可执行文件的名称可能不同，详细信息将在下一节中介绍。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175778255783.png "1669175778255783.png")

诱饵文件

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175785321453.png "1669175785321453.png")

PUBLOAD文件中的诱饵文件

可以看出“~”文件是一个诱饵文件。Increasingly confident US is baiting China.exe是一个合法的可执行文件（最初名为adobe\_licensing\_wf\_helper.exe，即adobe licensing wf helper）。这个可执行文件将侧载恶意的libeff .dll并触发导出函数cef\_api\_hash。

首次执行时，可执行文件尝试通过复制.exe文件和移动libcef.dll（趋势科技将其命名为Trojan.W32.PUBLOAD）。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175797495403.png "1669175797495403.png")

恶意活动

**快捷链接**

恶意文件包含三个文件:New Word Document.lnk、putty.exe和CefBrowser.dll。特别是，DLL和可执行文件被放置在名为“\_”的多层文件夹中。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175806149724.png "1669175806149724.png")

攻击者利用.lnk文件通过使用WinRAR解压缩文件来安装恶意文件。完整的命令行如下所示。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175813134522.png "1669175813134522.png")

Pputty.exe伪装成一个正常的可执行文件，其原始文件名为AppXUpdate.exe。当它被执行时，它会加载CefBrowser.dll，并在它的导出函数CCefInterface::SubProcessMain中执行主例程。它还滥用schtask来实现持久性。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175820122203.png "1669175820122203.png")

**恶意软件**

在这次活动中，研究人员识别出使用了以下恶意软件，即PUBLOAD、TONEINS和TONESHELL。

**Trojan.Win32.PUBLOAD**

PUBLOAD是一个可以从其指挥控制(C&C)服务器下载下一级有效负载的stager。该恶意软件于2022年5月由Cisco Talos首次披露。

一旦.dll被执行，它首先通过调用OpenEventA来检查相同的进程是否已经在运行。根据Barberousse发布的推文，一些值得注意的事件名称被识别为Twitter上其他网络安全研究人员的用户名，如“moto\_sato”、“xaacrazyman\_armyCIAx”和“JohnHammondTeam”。值得注意的是，这些研究人员与PUBLOAD没有任何关系，只是被二进制文件中的攻击者有意提及。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175828201689.png "1669175828201689.png")

PUBLOAD中特殊事件名称的示例

**持久性分析**

PUBLOAD在

1. 添加注册表运行项

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175837180290.png "1669175837180290.png")

2. 创建计划任务

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175846277890.png "1669175846277890.png")

**反分析技术：带有回调的API**

PUBLOAD恶意软件在内存中的AES算法中解密shellcode。shellcode是通过创建线程或使用不同的API调用的。API可以接受回调函数的参数，作为触发shellcode的替代方法。我们观察到一些利用API的情况，包括GrayStringW、EnumDateFormatsA和LineDDA，可以将其视为绕过反病毒监视和检测的技术。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175854118108.png "1669175854118108.png")

PUBLOAD中的shellcode回调示例

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175862199640.png "1669175862199640.png")

接受回调函数的API

**C&C协议**

解密的PUBLOAD shell代码收集计算机名和用户名作为第一个信标的有效负载。有效负载将使用预定义的RC4 (Rivest Cipher 4)密钥进行加密。在撰写本文时，到目前为止我们看到的所有阶段都共享相同的密钥。

加密后，stager使用特定的字节序列作为其数据包的标头。它在加密数据之前加上神奇的字节“17 03 03”和有效负载大小。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175871633409.png "1669175871633409.png")

PUBLOAD恶意软件中使用的RC4密钥（顶部）和数据包主体（底部）

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175880533390.png "1669175880533390.png")

PUBLOAD中的请求数据包格式

stager还检查响应包是否具有相同的魔术标头“17 03 03”。在内存中下载的有效负载将被视为一段shellcode，并将直接执行。

**值得注意的调试字符串**

在2022年初，我们发现了一些嵌入调试字符串的PUBLOAD示例。它们被用来分散分析人员对主要感染程序的注意力。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175889104470.png "1669175889104470.png")

PUBLOAD中分散注意力的调试字符串

**Trojan.Win32.TONEINS**

Trojan.Win32.TONEINS是TONESHELL后门的安装程序。安装程序将TONESHELL恶意软件放入%PUBLIC%文件夹，并为其建立持久性。TONEINS恶意软件通常出现在诱饵文件中，在大多数情况下，TONEINS DLL的名称是libcef.DLL。恶意例程通过调用其导出函数cef\_api\_hash来触发。

TONEINS恶意软件被混淆，可能会减慢恶意软件分析的速度。它的控制流中包含大量垃圾代码，并且有大量无用的XOR指令，似乎暗示这些指令用于解码字符串。经过检查，我们发现这些混淆的代码是从开源存储库中重用的。

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175898107109.png "1669175898107109.png")

TONEINS中的代码混淆

安装程序通过使用以下schtasks命令建立TONESHELL后门的持久性：

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221123/1669175907110007.png "1669175907110007.png")

被释放的TONESHELL恶意软件的文件名大小写不同，计划任务的名称也不同。建立持久性后，TONESHELL将合法的可执行文件和恶意的DLL复制到%PUBLIC%文件夹，其中两个文件的名称在诱饵存档中都以“~”开头。在本示例中，~$220220817.docx是用于DLL侧加载的合法可执行文件...