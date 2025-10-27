---
title: Menagerie2.0：一个高速迭代的攻击
url: https://www.4hou.com/posts/po7Q
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-11
fetch_date: 2025-10-04T11:51:32.157600
---

# Menagerie2.0：一个高速迭代的攻击

Menagerie2.0：一个高速迭代的攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Menagerie2.0：一个高速迭代的攻击

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-07-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)150277

收藏

导语：此类攻击活动可能对网站所有者或网络托管公司造成负面影响。

![微信截图_20230710001005.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921681110242.png "1688921681110242.png")

Unit 42的研究人员发现，从2020年末到2022年末，发生了一系列针对美国和欧盟几家网络托管和IT提供商的攻击活动，研究人员将其编号为CL-CRI-0021，并认为其幕后攻击者是Menagerie。

攻击者在被劫持的设备上部署挖矿程序，以盗窃受攻击服务器的资源。他们通过大规模部署web shell，来进一步增加持强起持续访问能力，并进一步访问受攻击网站的内部资源。这样一来，攻击者就有可能把被劫持的合法网站（由目标网络托管和IT提供商托管）大规模地变成指挥和控制(C2)服务器，从而影响数千个网页。因此，攻击者可以从具有良好声誉的合法网站运行他们的C2活动，这些网站不一定被安全解决方案标记为恶意。这可能会对被滥用的合法网站产生巨大的影响，在这种情况下，这些网站会在不知情的情况下托管恶意内容和隐藏攻击活动。此类攻击活动可能对网站所有者或网络托管公司造成负面影响。

在受害者的网络中，攻击者尝试了多种技术来逃避各种检测。他们还继续执行有效负载，重新部署和重新运行以前被阻止的工具，或者使用其他类似的工具。总之，攻击者试图不用已知的恶意软件，通过引入定制工具和依赖公开可用的合法工具来躲避检测。

根据研究人员在这次攻击中观察到的战术、技术和程序(TTP)，之前被称为 Menagerie的攻击者实施了上述攻击，因此本文将其称之为“Menagerie2.0”。

据澳大利亚网络安全中心报道，该攻击者至少从2018年就开始活跃，目标是澳大利亚的网络托管公司。

**初始访问和持久化**

“Menagerie2.0”活动是在2020年底首次发现的，目标是美国和欧盟的公司。在此活动中，攻击者通过利用易受攻击的web应用程序和IIS服务器，并在这些受攻击的服务器上部署不同的web shell，获得了对目标设备的访问权限。

在活动的web服务器上部署web shell允许攻击者劫持合法网站。webshell被放置在这些托管网站的C:\[hosted websites on the server path]\wwwroot\example.com\webshell.aspx文件夹中。

这些操作还允许将来从受害者的网络外部公开访问，这可以让这些网站变成攻击者未来的C2服务器。研究人员还观察到同样的web shell,，即xn.aspx，目标是澳大利亚的网络主机公司。

在Manic Menagerie 2.0中部署web shell后，攻击者开始部署挖矿程序。这样做很可能是为了滥用受损服务器强大的计算资源，通过挖矿获取目标的钱财。

2021-2022年期间，在公开披露多个Microsoft Exchange Server漏洞后，攻击者试图在一些目标中利用以下漏洞：

CVE-2021-26855、CVE-2022-41040:（ProxyNotShell）Exchange Server SSRF漏洞；

CVE-2021-34473：ProxyShell漏洞之一，Exchange Server远程代码执行漏洞；

CVE-2021-33766（ProxyToken）：允许攻击者修改任意用户的邮箱配置；

因此，除了IIS服务器中的漏洞和环境中易受攻击的web应用程序之外，前面提到的漏洞还为攻击者提供了另一个渗透和持久性载体。

**侦察功能和权限升级**

从2020年底开始，参与Menagerie 2.0活动的攻击者开始定期尝试执行本地权限升级，以将自己的用户添加到IIS服务器中的管理员组中，以进一步提升他们的攻击能力。当一个工具失败时，他们会尝试用另一个具有类似功能的工具。

攻击者使用了一个名为RunasCs的runas.exe.NET封装器。此公开可用的工具启用了原始runas.exe实用程序所缺乏的扩展功能，例如通过使用用户凭据明文执行进程。

观察到攻击者试图通过在易受攻击的web应用程序下运行，在受攻击的环境中执行进一步的网络侦察。然后，他们试图通过运行au.exe来添加自己的用户，au.exe是“add user”的缩写。该文件必须由已提升的用户运行。然后，他们通过运行net命令来确保他们的用户名存在。

他们对用户名iis\_user和iis\_users的使用是值得注意的，因为后者最初可能看起来是一个拼写错误。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921695830621.png "1688921695830621.png")

au.exe创建iis\_user用户并为其生成密码

前面提到的au.exe是一个攻击者试图多次运行的工具，它与不同的PoC本地权限提升工具链接在一起，如下图所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921711378108.png "1688921711378108.png")

试图在易受攻击的web应用程序下执行RunasCs和其他命令

可以看到攻击者使用多个工具来实现相同的权限升级，如上图所示，64位版本的PrintSpoofer就是其中一个工具。这个公共工具被攻击者用来提升au.exe，否则它就不会添加它想要添加的用户。

**fork炸弹（fork bomb）和更多本地权限升级**

据观察，攻击者利用以下漏洞，试图使用多个公开可用的工具升级本地权限（LPE）：

CVE-2018-8120

CVE-2019-0623

CVE-2019-0803

CVE-2019-1458

研究人员在Menagerie 2.0中观察到的另一个有趣的执行是svchost.exe fork炸弹。ACSC关于Menagerie活动的报告也提到了这种类型的拒绝服务(DoS)工具的存在。

这个fork炸弹的代码非常简单，因为它在一个无限循环中运行，会打开越来越多程序，直到设备耗尽内存。此活动旨在使设备崩溃并强制重新启动。这允许需要重新启动才能开始的可执行文件的持久性机制。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921728131983.png "1688921728131983.png")

fork炸弹二进制文件中的无限循环代码片段

**dllnc.dll：运行有效负载和添加用户工具**

研究人员在 Menagerie 2.0活动中观察到的另一个名为dllnc的工具有两个主要功能。一个是加载攻击者的一些可执行文件和批处理文件，另一个是作为另一个工具，用于将攻击者的用户添加到管理员组。

它包含一个指示PDB路径：F:\upfile\3389\opents\dlladduser\x64\Release\dllnc.pdb，截至2023年5月中旬，其在VirusTotal中没有产生任何其他结果。这表明，这是针对特定目标的自定义工具。

加载程序代码段试图加载一些它认为已经在攻击者路径中的工具(如图4所示)，因为没有检查它们是否实际存在。在这样做的同时，它考虑了几种可能的硬编码路径，其中大多数都出现在这次攻击活动中。

![4.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921743112463.png "1688921743112463.png")

![4.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921754162496.png "1688921754162496.png")

攻击者工具的硬编码路径，如dllnc.dll中所示

然后，该工具删除当前的iis\_user用户，然后重新添加它，这次是使用硬编码的密码。同样，这种行为与ACSC关于原始疯狂Menagerie运动的报告有关。该报告中也提到了相对ID（RID）劫持工具的一个旧变体（如图5所示），类似于这种行为。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921773109596.png "1688921773109596.png")

RID劫持工具

这两种变体中的密码有着明显的、非常相似的地方，因为它们都使用xman前缀和类似的后缀。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921802203168.png "1688921802203168.png")

用户iis\_user及其硬编码密码

**PCHunter**

PCHunter是被观察到的另一个被Menagerie 2.0活动使用的工具，它让人想起GMER和Rootkit Unhooker等老工具。它是一个合法的和强大的工具包，用于浏览和修改不同的Windows内部组件。下图显示了试图执行被阻止的PCHunter。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921815206453.png "1688921815206453.png")

下图显示了“Epoolsoft Corporation”的PCHunter数字签名。中文评论提供了该工具的快速描述。这被翻译为“Yipmin是一个Windows系统信息查看工具（安全类别）。”

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921838124918.png "1688921838124918.png")

PCHunter签名者信息

**大规模后门：将已知的Web Shell部署到多个目的地**

在Menagerie 2.0活动中观察到的第二波明显的攻击主要是在托管网站大规模部署web shell。这使得攻击者能够通过允许他们未来的公共访问来加强他们的攻击立足点，并将他们的web shell隐藏在嵌套文件夹深处。这些合法被劫持的网站将来可能会被用作C2服务器，例如，作为僵尸网络基础设施的一部分。

攻击者的部署尝试可以追溯到2022年初，当时他们在多个托管网站上部署了名为ASPXSpy的已知web shell，他们观察到这个web shell被写入了数百个不同的路径，如下图所示。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921854208407.png "1688921854208407.png")

ASPXSpy web shell被写入不同的托管网站路径

**GoIIS**

攻击者还运行了一个名为IIS1.asp或GoIIS.exe的工具，该工具于2017年编译。该工具是用Golang编写的，用于遍历服务器的文件夹以检索服务器的配置信息。这使攻击者能够获得有关被攻击服务器的宝贵信息。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921872118060.png "1688921872118060.png")

IIS工具

**Sh.exe：自定义Web Shell部署工具**

2022年末，攻击者部署了一个名为sh.exe的自定义工具，作为Menagerie 2.0活动的一部分，其执行情况如下图所示。该工具的作用是根据共享相同公共IP地址的服务器上预先配置的路径和合法被劫持网站的列表，在托管网站大规模编写web shell。

为了方便使用此工具，攻击者使用了caclcs.exe的自定义封装器，攻击者将其命名为mycacls.com，这是一个用于管理访问控制列表（ACL）的命令行工具。该工具使他们能够批量更改web服务器的ACL权限，并降低IIS安全设置。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921889955320.png "1688921889955320.png")

尝试与其他工具和命令一起执行sh.exe，但被Cortex XDR阻止

传递给sh.exe的参数包含共享相同公共IP的相关网站列表。在执行时，sh.exe工具生成各种看起来合法的子文件夹，例如图像和css，以进一步隐藏它们的活动。这可能是为了让攻击者将来能够从互联网访问受害者的设备，并可能在将来大规模地使用该基础设施作为C2服务器。

sh.exe使用 "Fujian identical investment co.,Ltd."颁发的无效证书签名，如下图所示。这与ACSC报告在活动中描述的用于签署另一个工具的名称相同。

在观察到的样本中，sh.exe是在2022年11月3日编译的。其证书于2022年12月6日签署。签署后不久，就可以看到攻击者在其中一个受攻击的环境中执行sh.exe。无效证书的编译时间戳和日期范围可能表明该工具是专门为此特定活动制作的。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921933295548.png "1688921933295548.png")

Sh.exe无效签名

虽然攻击者删除了大部分文件，但研究人员发现sh.exe和它释放的文件之间存在无法恢复的连接。调查发现了攻击者使用的三个不同的已编译.NET DLL。

一旦“原始”ASPX文件第一次被访问，这些dll将由IIS服务器编译。在对代码进行反编译后，基于在两个文件中发现的指示字符串，在web shell和sh.exe之间发现了有趣的相似之处。

浏览其中一个被web shell释放的网站，页面上的内容是字符串ONEPIECE，如下图所示。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688921951157414.png "1688921951157414.png")

浏览其中一个被劫持网站的web shell资源

浏览其中一个web shell的代码并查看负责显示HTML内容的代码，可以看到该字符串以及其他指示字符串，如x\_best\_911。

![14.png](https://img.4hou.com/...