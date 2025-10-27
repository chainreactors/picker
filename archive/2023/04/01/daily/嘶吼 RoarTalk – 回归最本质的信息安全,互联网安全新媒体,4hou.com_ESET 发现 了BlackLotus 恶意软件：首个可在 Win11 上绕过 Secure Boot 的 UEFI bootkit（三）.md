---
title: ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（三）
url: https://www.4hou.com/posts/RBRq
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-01
fetch_date: 2025-10-04T11:19:42.655091
---

# ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（三）

ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（三） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（三）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-03-31 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)123568

收藏

导语：ESET 的安全研究人员近日发现了一种劫持 UEFI 的恶意软件，并将其命名为 BlackLotus。该恶意软件是首个可以在Win11系统上绕过 Secure Boot 的 UEFI bootkit 恶意软件。

**与HTTP下载器的通信**

内核驱动程序能够通过使用命名的Event和Section与HTTP下载器通信。所使用的命名对象的名称是根据受害者的网络适配器MAC地址（以太网）生成的。如果一个八位字节的值小于16，那么将向其添加16。生成的对象名称的格式可能在不同的示例中有所不同。例如，在我们分析的一个示例中，对于MAC地址00-1c-0b-cd-ef-34，生成的名称为：

\BaseNamedObjects\101c1b：用于命名部分（仅使用MAC的前三个八位字节）；

\BaseNamedObjects\Z01c1b：用于命名事件，与Section相同，但MAC地址的第一个数字被替换为Z；

如果HTTP下载器想要将一些命令传递给内核驱动程序，它只需要创建一个命名的节，在其中写入一个包含相关数据的命令，并通过创建一个指定事件等待驱动程序处理该命令，直到驱动程序触发（或发出信号）该命令。

驱动程序支持以下一目了然的命令：

安装内核驱动程序；

卸载BlackLotus；

细心的读者可能会注意到这里的BlackLotus弱点，即使bootkit保护其组件不被删除，内核驱动程序也可以通过创建上述命名对象并向其发送卸载命令来完全卸载bootkit。

**HTTP下载器**

最后一个组件负责与C&C服务器通信，并执行从其接收的任何C&C命令。我们能够发现的所有有效载荷都包含三个命令。这些命令非常简单，正如部分名称所示，主要是使用各种技术下载和执行额外的有效载荷。

**C&C通信**

为了与其C&C通信，HTTP加载器使用HTTPS协议。通信所需的所有信息都直接嵌入到下载器二进制文件中，包括使用的C&C域和HTTP资源路径。与C&C服务器通信的默认间隔设置为一分钟，但可以根据C&C的数据进行更改。与C&C的每个通信会话都从向其发送信标HTTP POST消息开始。在我们分析的示例中，可以在HTTP POST标头中指定以下HTTP资源路径：

```
/network/API/hpb_gate[.]php
/API/hpb_gate[.]php
/gate[.]php
/hpb_gate[.]php
```

信标消息数据以checkin=字符串开头，包含有关受攻击机器的基本信息，包括自定义设备标识符（称为HWID）、UEFI Secure Boot状态、各种硬件信息以及一个看起来是BlackLotus内部版本号的值。HWID由设备MAC地址（以太网）和系统卷序列号生成。加密前的消息格式如下图所示。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678091492633855.png "1678091492633855.png")

在向C&C发送消息之前，首先使用嵌入的RSA密钥对数据进行加密，然后使用URL安全的base64编码。在分析过程中，我们发现样本中使用了两个不同的RSA密钥。这种HTTP信标请求的示例如下图所示。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678091501115558.png "1678091501115558.png")

信标HTTP POST消息示例（由VirusTotal中的示例生成——具有本地IP而非真实C&C地址的示例）

作为对信标消息的响应，从C&C接收的数据应以两字节魔法值HP开头；否则，不进一步处理响应。如果魔法值正确，则在CBC模式下使用256位AES对魔法值之后的数据进行解密，并使用上述HWID字符串作为密钥。

解密后，该消息类似于信标，一个JSON格式的字符串，并指定命令标识符（称为Type）和各种附加参数，例如：

C&C通信间隔；

执行方法；

有效负载文件名；

基于文件扩展名的负载类型（支持.sys、.exe或.dll）；

应该用于请求下载有效负载数据的身份验证令牌；

用于解密有效负载数据的AES密钥；

下表列出了所有支持的命令及其说明。

表2：C&C命令

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678091513795383.png "1678091513795383.png")

在这些命令中，C&C可以指定是在执行负载之前先将其放到磁盘上，还是直接在内存中执行。在将文件放到磁盘的情况下，操作系统卷上的ProgramData文件夹将用作目标文件夹，文件名和扩展名由C&C服务器指定。在直接在内存中执行文件的情况下，svchost.exe用作注入目标。当C&C发送需要内核驱动程序协作的命令时，或者操作员希望以内核模式执行代码时，将使用与HTTP下载器通信部分中描述的机制。

**反分析技巧**

为了更难检测和分析这一恶意软件，其开发者试图将标准文件工件（如文本字符串、导入或其他未加密的嵌入数据）的可见性限制在最低限度。以下是所用技术的摘要。

**字符串和数据加密：**

示例中使用的所有字符串都使用简单的密码进行加密；

所有嵌入的文件都在CBC模式下使用256位AES加密；

各文件的加密密钥可能因样本而异；

除AES加密之外，一些文件还使用LZMS进行压缩。

**Runtime-only API解析：**

在所有示例中（如果适用），Windows API总是在运行时进行排他解析，并且使用函数哈希而不是函数名来查找内存中所需的API函数地址；

在某些情况下，直接syscall 指令调用用于调用所需的系统函数；

**网络通信：**

使用HTTPS通信；

HTTP下载器发送到C&C的所有消息都使用嵌入的RSA公钥进行加密；

从C&C发送到HTTP下载器的所有消息都使用来自受害者设备环境的密钥或C&C提供的AES密钥进行加密；

**反调试和反VM技巧：**

如果使用该方法，通常放在入口点的开头，仅使用临时沙盒或调试器检测技巧。

**缓解措施和补救措施**

首先，必须保持所使用的系统及其安全产品是最新的；

然后，要防止使用已知的易受攻击UEFI二进制文件绕过UEFI Secure Boot，需要采取的关键步骤是在UEFI取消数据库（dbx）中取消这些二进制文件，在Windows系统上，应使用Windows Update传播dbx更新。

问题是，广泛使用的Windows UEFI二进制文件的取消可能会导致数千个过时的系统、恢复映像或备份无法启动，因此，取消通常需要很长时间。

请注意，BlackLotus使用的Windows应用程序的取消将阻止启动工具包的安装，但由于安装程序将用已取消的启动加载器替换受害者的启动加载器，这可能会使系统无法启动。要在这种情况下进行恢复，重新安装操作系统或仅进行ESP恢复即可解决问题。

如果在设置BlackLotus持久性之后发生取消，则bootkit将保持正常运行，因为它使用具有自定义MOK密钥的合法填充程序进行持久性。在这种情况下，最安全的缓解方案是重新安装Windows，并使用mokutil实用程序删除攻击者注册的MOK密钥（由于在启动过程中需要用户与MOK管理器进行必要的交互，因此执行此操作需要实体存在）。

**总结**

在过去几年中，已经发现了许多影响UEFI系统安全的关键漏洞。不幸的是，由于整个UEFI生态系统的复杂性和相关的供应链问题，即使在漏洞修复后很长一段时间，或者至少在用户被告知它们已修复后，这些漏洞中的许多漏洞仍会使许多系统处于易受攻击状态。下面是一些去年允许UEFI Secure Boot绕过的修复或取消失败的示例：

首先，当然是CVE-2022-21894，这是一个被BlackLotus利用的漏洞。在修复该漏洞一年后，易受攻击的UEFI二进制文件仍然没有被取消，这使得BlackLotus等攻击可以在启用了UEFI Secure Boot的系统上秘密运行。

早在2022年，研究人员就披露了几个允许禁用UEFI Secure Boot的UEFI漏洞。许多受影响的设备不再受到OEM的支持，但在联想消费级笔记本电脑中发现高影响的UEFI漏洞。

在2022年晚些时候，研究人员发现了其他一些UEFI漏洞，这些漏洞也允许攻击者很容易地禁用UEFI Secure Boot。正如Binarly的研究人员指出的那样，在警告发布几个月后，警告中列出的几个设备都没有被修复，或者没有正确地被修复，这使得这些设备容易受到攻击。与前面的情况类似，一些设备将永远处于易受攻击状态，因为它们已经无法更新。在不远的将来，有攻击者会滥用这些漏洞，创建一个能够在启用UEFI Secure Boot的系统上运行的UEFI bootkit。

本文翻译自：https://www.welivesecurity.com/2023/03/01/blacklotus-uefi-bootkit-myth-confirmed/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ZDPadYZl)

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

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/aOZG)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务...