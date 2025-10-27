---
title: PyPI中出现了针对Windows用户的6个恶意Python包
url: https://www.4hou.com/posts/vxR8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-27
fetch_date: 2025-10-04T11:51:03.623696
---

# PyPI中出现了针对Windows用户的6个恶意Python包

PyPI中出现了针对Windows用户的6个恶意Python包 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PyPI中出现了针对Windows用户的6个恶意Python包

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-07-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)114037

收藏

导语：今年3月，Unit 42的研究人员在Python Package Index(PyPI)包管理器上发现了6个恶意包。恶意软件包旨在窃取Windows用户的应用程序凭据、个人数据和加密钱包的跟踪信息。

![微信截图_20230716105524.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689476685115639.png "1689476685115639.png")

今年3月，Unit 42的研究人员在Python Package Index(PyPI)包管理器上发现了6个恶意包。恶意软件包旨在窃取Windows用户的应用程序凭据、个人数据和加密钱包的跟踪信息。该攻击试图模仿攻击组织W4SP，该组织此前曾使用恶意软件包发起过几次供应链攻击。

研究人员将讨论攻击者在开源生态系统中使用恶意包传播恶意代码的难易程度，他们观察到的行为并不是由攻击组织策划的有组织的攻击，而很可能是一个模仿者阅读了以前攻击的技术报告来执行他们自己的攻击。

研究人员将描述Palo Alto Networks Prisma Cloud模块使用的指标，这些指标识别了本文讨论的恶意软件包。Palo Alto Networks的客户可以通过Prisma Cloud获得包含恶意代码的开源软件包的保护。

恶意软件包是故意设计用于对计算机系统或其处理的数据造成损害的软件组件。此类软件包可以通过各种方式传播，包括钓鱼电子邮件、被攻击的网站甚至合法的软件存储库。

恶意软件包可能会产生很大的破坏力，包括偷偷窃取敏感数据到导致系统中断，甚至控制整个系统。此外，这些恶意软件包具有传播到其他互联系统的能力。因此，在进行软件下载和安装时，尤其是在源代码不熟悉或不受信任的情况下，务必格外小心。

通过保持警惕和洞察力，用户可以保护他们的系统，并防止攻击者渗透到他们的技术环境。

**在PyPI中发现新的恶意包**

2023年3月，Prisma Cloud研究人员在PyPI软件包管理器上发现了6个针对Windows用户的恶意软件包。恶意软件包旨在窃取应用程序凭据、个人数据和加密货币钱包信息。

研究人员的Prisma Cloud引擎，旨在检测恶意PyPI包，发现几个在短时间内上传的具有可疑属性的包：

这些软件包缺少相关的GitHub存储库，它通常与合法软件包一起使用。这可能表明希望从视图中隐藏代码。另外，再加上有限的下载量，进一步引起了研究人员的怀疑；

在执行时，这些包执行恶意操作，例如收集敏感数据并将其发送到第三方URL；

这些包包含一个恶意代码模式，目前已检测到了它；

因为包的开发者是新创建的，只上传了一个包，并且没有提供支持信息，例如到其他项目或任何存储库的链接，所以他们不被认为是有信誉的；

最后，包开发者的用户名是在几分钟内创建的，遵循一个独特的模式（例如，Anne1337、Richard1337），每个用户名只上传了一个包。

第二阶段的攻击与我们之前看到的W4SP攻击群的攻击相似。该组织专门利用开源生态系统中的漏洞，针对组织和传播恶意软件。他们的主要目标是获得对敏感信息（如用户凭据和财务数据）的未经授权的访问权限。他们经常使用自动化工具来扫描漏洞并试图利用它们。除了传统攻击外，W4SP攻击者还执行供应链攻击。

**检测结果**

Prisma Cloud引擎检测到被标记为可能包含恶意代码的包。每个包都包含一个指向可疑远程URL的链接，试图在单个用户单独上传后下载内容。

每个上传包的用户的用户名都是在上传前创建的，之前没有任何上传包的历史记录。每个包都有数百次下载，直到研究人员的研究团队报告了滥用行为，PyPI才将它们和上传它们的欺诈性用户帐户删除。

研究人员分析了代码并试图找到开发者。研究人员在每个包开发者的用户名中发现了一个模式，他们使用“1337”作为后缀，这表明某些自动过程创建了这些用户，下图1显示了其中一个用户名的开发者页面。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689476704449999.png "1689476704449999.png")

恶意包

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689476719751178.png "1689476719751178.png")

PyPI的开发者页面

**自定义包入口点**

这次攻击类似于研究人员之前看到的W4SP攻击组织的攻击，此文详细介绍了这一攻击。这些相似之处让研究人员相信这是一次模仿。

但此次攻击没有真正的W4SP攻击那么复杂，例如：

没有针对任何组织；

恶意软件包没有像W4SP攻击所预期的那样，使用常见流行软件包的输入错误；

第二阶段的攻击没有加密，在来自W4SP的真正攻击中，这个阶段是加密的，这使得检测更加困难；

W4SP在以前的攻击中使用的大部分代码已经可以下载，因此可以很容易地访问和重新利用；

在之前的攻击中，W4SP 窃取程序作为从免费文件托管服务下载的第二阶段有效载荷传播，这使得攻击者可以避免在包存储库中进行检测。

这些包没有包含明显的恶意代码，而是精心设计的，以具有在安装或执行过程中触发的特定入口点。通过利用免费文件托管服务和自定义入口点，攻击者的目标是不被发现，这对负责检测和防御此类攻击的安全专业人员和研究人员构成了重大挑战。

这些攻击很容易实现，并且可以在几乎没有安全专业知识的情况下发起。但是，它们可能非常有效，因为安装过程会自动执行攻击，而不是在使用导入模块时需要攻击者发起攻击。

当软件开发人员想要使用Python包时，他们必须执行两个操作。第一个步是安装包，第二个步是在代码中导入或声明以使用它。正如接下来讨论的那样，攻击代码实际上是从安装文件(setup.py)中开始的，这意味着在安装包期间已经执行了攻击。

在研究人员调查的示例中，攻击者称自己为@EVIL$窃取程序。然而，该名称随着每次攻击而改变。以下是代码签名中的名称集合：

ANGEL窃取程序

Celestial窃取程序

Fade窃取程序

Leaf $tealer

PURE窃取程序

Satan窃取程序

@skid 窃取程序

**恶意代码**

setup.py文件在所有包中都是相同的，并且包含以下代码片段，用于在执行之前从远程URL下载内容：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689476746541754.png "1689476746541754.png")

Setup.py（第一阶段）恶意代码

上图显示了以下活动：

1.攻击者使用\_ffile对象创建临时文件，并使用write方法写入文件的内容，使用带有NamedTemporaryFile函数的临时文件是一种众所周知的技术，可以隐藏恶意代码，使其不被杀毒软件或其他安全措施检测到；

2.文件的内容是通过使用urlopen函数从urllib下载URL的内容获得的。请求模块，然后使用exec函数执行文件的内容；

3.在写完临时文件的内容后，将关闭该文件，并尝试在系统shell中使用start命令执行它。如果成功，将调用setup函数来创建包。然后攻击者使用start命令启动Python引擎的可执行文件(pythonw.exe)，之后这个可执行文件将执行作为参数传递的脚本文件。由于该恶意软件包针对Windows用户，如果脚本文件未签名，则不会受到SmartScreen (Windows安全功能，用于检测和防止潜在恶意文件的执行)或签名检查的影响。这意味着它将在目标计算机上执行恶意代码，即使目标计算机启用了SmartScreen和签名检查。

**第二阶段：W4SP窃取程序**

根据研究人员的研究，在第二阶段，攻击者使用了配置版本的W4SP窃取程序 1.1.6。这个版本类似于以前的版本，其中代码导入了几个库，包括 requests, Crypto.Cipher, json和sqlite3。然后，它使用各种技术提取和解密存储的浏览器凭据，包括密码和cookie，并将这些信息发送到Discord webhook。

代码的主体定义了一个类DATA\_BLOB，用于存储CryptUnprotectData函数的数据。此函数用于解密受Windows数据保护API（DPAPI）保护的值，该值用于存储密码和API密钥等敏感数据。代码尝试使用CryptUnprotectData和DecryptValue函数解密一个值，然后通过Discord webhook将其发送到远程服务器，如下图所示。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689476794110054.png "1689476794110054.png")

尝试解密Windows数据保护API（DPAPI）保护的值

下图显示了攻击者试图收集受害者信息的几个恶意代码示例。如下图所示，攻击者试图收集受害者的信息，包括IP地址、用户名、国家/地区代码。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689477155171330.png "1689477155171330.png")

检索有关用户IP地址、位置和用户名等信息的代码

在下图中，攻击者与Discord API交互，以检索用户的好友列表并提取有关他们自己的标识信息。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689477172135651.png "1689477172135651.png")

用于在Discord上检索用户好友列表的代码

在稍后的代码中，他们尝试使用事先准备好的Discord webhook，然后尝试通过HTTP请求将受害者信息发送到相关的Discord通道。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689477194494723.png "1689477194494723.png")

Discord webhook

最后，如下图所示，攻击者试图验证受害者的设备是否适合执行攻击。如果确定该设备是合适的，则DETECTED变量将被设置为true，并且来自受害者设备的信息将被发送到远程服务器。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230716/1689477213771873.png "1689477213771873.png")

搜索Cookie的代码

**PyPI作为一个上传恶意软件包的便捷平台**

PyPI是一个备受信赖且广受欢迎的存储库，拥有数量惊人的Python包，在PyPI领域内，出现了一个令人担忧的现实。该存储库无与伦比的受欢迎程度无意中成了攻击者使用的对象，他们试图通过秘密传播恶意软件包来利用其庞大的用户群。

这种令人不安的趋势对安全提出了一个重大挑战，因为PyPI的去中心化性质使监测和检测这些恶意对象成为一项艰巨的工作。成为此类恶意软件包受害者的后果会对毫无戒心的用户和企业造成严重后果，例如数据、凭证或加密被盗。因此，加强PyPI包的安全性是至关重要的。

PyPI于2023年5月20日宣布，由于平台上恶意活动，恶意用户和项目的增加，他们暂时停止注册和上传新软件包。

冻结新用户和项目注册的决定反映了像PyPI这样的软件注册中心面临的安全挑战，因为它们已经成为寻求篡改软件供应链攻击者的目标。

**总结**

开源软件的兴起和普及以及包管理器的激增，使攻击者比以往任何时候都更容易将这些危险的包植入用户的系统。随着软件在我们日常生活中越来越普遍，恶意软件包的威胁变得更加严重。攻击者可以将这些软件包伪装成合法软件，并利用毫无戒心的系统中的漏洞，造成数据盗窃、系统关闭和网络控制等重大损害。

为了防御这种威胁，软件开发人员和组织必须在开发过程中优先考虑软件安全性。增加了安全措施，例如代码审查、自动化测试和渗透测试，可以帮助在部署之前识别和修复漏洞。此外，保持最新的安全补丁和更新可以防止攻击者利用已知的漏洞。

除了技术措施外，提高对软件安全的认识和教育也有助于防御恶意软件包的风险。为开发人员、IT人员和最终用户提供关于最佳安全实践的定期培训很有必要。安全专业人员、开发人员和用户共同努力以确保识别并防止恶意软件包对系统和网络造成损害。

本文翻译自：https://unit42.paloaltonetworks.com/malicious-packages-in-pypi/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?9YAINKx2)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过...