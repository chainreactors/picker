---
title: Dark Pink APT组织针对东南亚以及欧洲地区的攻击活动（一）
url: https://www.4hou.com/posts/JX3J
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-13
fetch_date: 2025-10-04T09:23:37.589993
---

# Dark Pink APT组织针对东南亚以及欧洲地区的攻击活动（一）

Dark Pink APT组织针对东南亚以及欧洲地区的攻击活动（一） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Dark Pink APT组织针对东南亚以及欧洲地区的攻击活动（一）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-03-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)158228

收藏

导语：最近网络安全公司Group-IB发现了一波针对东南亚以及欧洲地区的攻击，目前暂将其命名为Dark Pink，截止发文还没有分析出其背后的攻击者，因此极有可能Dark Pink是一个全新的APT组织。

长期以来，亚太地区国家一直是高级持续性威胁(APT)的重灾区。最近网络安全公司Group-IB发现了一波针对东南亚以及欧洲地区的攻击，目前暂将其命名为Dark Pink，截止发文还没有分析出其背后的攻击者，因此极有可能Dark Pink是一个全新的APT组织。为研究方便，本文就将其幕后组织称为Dark Pink APT组织。

有证据表明，“Dark Pink”活动早在2021年年中就开始了，2022年中后期激增。目前已确认的受害者包括菲律宾和马来西亚的两个军事机构，柬埔寨、印度尼西亚和波斯尼亚和黑塞哥维那的政府机构，以及越南的一个宗教组织。

攻击者正在利用一套新的战术、技术和程序，他们利用一个自定义工具包，包括TelePowerBot、KamiKakaBot、Cucky和Ctealer信息窃取器(所有名字都被称为Group-IB)，旨在窃取政府和军事组织网络上的机密文件。特别值得注意的是，Dark Pink甚至有能力攻击连接到受攻击设备的USB设备，甚至访问受攻击设备上的即时通讯工具。此外，Dark Pink组织利用两种核心技术，其中一种是DLL侧加载和执行由文件类型关联触发的恶意内容（事件触发执行：更改默认文件关联）。

**重要发现**

在2022年6月至12月期间，Dark Pink对某个目标发动了七次攻击。

研究人员将Dark Pink的首次活动与攻击者利用的Github账户联系在一起，首次攻击发生在2022年6月。他们的活动在2022年的最后三个月达到顶峰，当时他们发动了四次攻击。

Dark Pink的受害者分布在五个亚太国家(越南、马来西亚、印度尼西亚、柬埔寨、菲律宾)和一个欧洲国家(波黑)。攻击对象包括军事机构、政府和发展机构、宗教组织和一个非营利组织。

Dark Pink APT的主要目标是进行商业间谍活动，窃取文件，从受攻击设备的麦克风中捕获声音，并从即时通讯工具中窃取数据。

Dark Pink最初的核心载体是针对鱼叉式网络钓鱼邮件，攻击者假扮成求职者。有证据表明，“Dark Pink”背后的组织扫描了发布空缺职位的网站，并伪装成求职者发送了电子邮件。

几乎所有工具都是定制，包括TelePowerBot和KamiKakaBot，以及Cucky和Ctealer窃取程序。整个调查过程中，我们只发现了一个公共工具：PowerSploit /Get-MicrophoneAudio。

Dark Pink APT使用了一种称为事件触发执行的罕见技术，通过更改默认文件关联，以确保恶意TelePowerBot恶意软件的启动。这些特殊攻击者利用的另一种技术是DLL侧加载，他们用它来避免在初始访问期间被发现。

攻击者创建了一组PowerShell脚本，用于在受害者和攻击者的基础设施之间进行通信，其目的是横向移动和网络侦察。

受攻击的基础设施和Dark Pink背后的攻击者之间的所有通信都基于Telegram API。

Dark Pink APT组织实施的攻击非常先进。他们利用复杂的自定义工具组合来攻破多个政府和军事组织的防御系统。首次发现是2022年6月在越南的一个宗教组织上注册的攻击。然而，在此之前，他们就一直很活跃，因为Group-IB研究人员发现了这些攻击者使用的Github账户，其活动可以追溯到2021年年中。根据研究，由攻击者初始化的恶意软件可以发出命令，让受攻击的设备从这个特定的Github帐户下载模块。有趣的是，在迄今为止的整个活动期间，攻击者似乎只使用了一个Github账户，这可能表明他们已经能够在很长一段时间内不被发现。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975548202337.png "1673975548202337.png")

上图详细显示2021（上图）和2022年（下图）Dark Pink APT在Github账户上的活动

在2022年6月的攻击之后，Group-IB研究人员无法将任何其他恶意活动归因于Dark Pink。然而，这个APT组织在夏末突然活跃起来，当时Group-IB注意到2022年8月越南一家非营利组织遭受的攻击具有6月攻击的所有特征。这样，Group-IB就能够将9月份的一次攻击、10月份的两次攻击(一次成功，一次失败)、11月份的两次攻击和12月份的一次攻击统一在一起。2022年12月8日，印度尼西亚政府组织就被攻击了一次。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975563164849.png "1673975563164849.png")

Dark Pink APT时间线和攻击目标

**攻击链**

Dark Pink攻击的复杂性体现在它执行了多个不同攻击链。攻击者能够用几种编程语言制作工具，这使他们在试图破坏防御基础设施并在受害者的网络上获得持久性时提供了很大的灵活性。因此，我们将讨论这些过程的不同步骤和阶段，但需要注意的是，大部分攻击都基于PowerShell脚本或命令，旨在启动受攻击网络和攻击者基础设施之间的通信。

最初的访问是通过成功的鱼叉式网络钓鱼邮件实现的，这些信息包含一个短链接，引导受害者下载恶意ISO映像，在一个示例中，Group-IB发现该映像存储在公共免费共享服务MediaFire上。一旦受害者下载了ISO映像，攻击者就可以使用三个不同的攻击链，我们将在下面详细介绍。

首先引起我们注意的是，攻击者和受害者设备之间的所有通信都是基于Telegram API的。由TelePowerBot和KamiKakaBot创建的自定义模块旨在通过攻击者控制的Telegram木马读取和执行命令。有趣的是，这些模块是用不同的编程语言开发的。TelePowerBot是用PowerShell脚本表示的，而KamiKakaBot则是在.NET上开发的，其中包含了窃取功能。自2021年9月以来，攻击者一直使用相同的Telegram木马程序。

此外，Dark Pink APT利用自定义Ctealer和Cucky从网络浏览器中窃取受害者的凭据。

**首次访问**

Dark Pink的成功很大程度上要归功于用于获得初始访问权限的鱼叉式网络钓鱼邮件。在一个示例中，Group-IB能够找到攻击者发送的原始电子邮件。在这个示例中，攻击者假扮成一名申请公关和传播实习生职位的求职者。在邮件中，攻击者提到他们在求职网站上发现了这个空缺，这可能表明攻击者扫描了求职板，并使用这些信息创建了高度相关的钓鱼电子邮件。

这些电子邮件包含一个链接到免费使用的文件共享网站的短URL，受害者可以从中选择下载一个ISO映像，其中包含攻击受害者网络所需的所有文件。在调查过程中，研究人员发现攻击者利用了几个不同的ISO映像，我们还注意到这些ISO映像中包含的文件因情况而异。根据目前掌握的信息，我们坚信攻击者会向每个受害者发送独特的电子邮件，我们认为攻击者可以通过电子邮件将恶意ISO镜像作为直接附件发送给受害者。

Dark Pink APT发送的原始鱼叉式钓鱼邮件截图，其中记录了文件共享网站上ISO映像的存储情况

鱼叉式网络钓鱼邮件中发送的ISO映像包含不同数量的文件。目前，在攻击者发送的所有ISO映像中发现了三种类型的文件：已签名的可执行文件、非恶意的诱饵文档(例如.doc、.pdf或.jpg)和恶意DLL文件。鉴于这封电子邮件与一个职位空缺有关，我们可以假设受害者首先会寻找所谓的申请人的简历，简历通常以MS Word文档的形式发送。然而，在Dark Pink攻击中，攻击者在ISO镜像中包含一个模仿MS Word文件的.exe文件。该文件在文件名中包含“.doc”，并包含MS Word图标，以此来迷惑受害者并认为该文件可以安全打开。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975605412146.png "1673975605412146.png")

Group-IB发现一个ISO图像中包含的五个文件的屏幕截图。请注意，.doc和.dll文件位于隐藏视图中

如果受害者首先执行.exe文件，与.exe文件位于同一文件夹中的恶意DLL文件将自动运行。这是一种被称为DLL侧加载的攻击者使用的技术。DLL执行的主要功能是确保攻击者的核心恶意软件TelePowerBot获得持久性。在文件执行完成之前，诱饵文件(如信件、简历)会显示在受害者的屏幕上。

**木马执行和持久性**

目前Group-IB研究人员已完整了解了TelePowerBot或KamiKakaBot在受害者设备上启动的过程。如上所述，包含这两个恶意软件之一的恶意DLL文件可以位于鱼叉式网络钓鱼活动期间发送的ISO映像中。在Group-IB分析的一个案例中，攻击者使用了一系列MS Office文档并利用了模板注入(Template Injection)，即攻击者在初始文档中插入指向包含恶意宏代码的模板文档的链接。在Group-IB研究人员检查的另外两个案例中，Dark Pink背后的攻击者通过DLL侧加载技术启动了他们的恶意软件。总的来说，我们发现了攻击者利用的三个不同的攻击链，我们将在下面详细介绍它们。

**攻击链1：全包式ISO**

攻击链的第一个变体导致ISO映像通过鱼叉式网络钓鱼邮件发送给受害者。此ISO映像包含一个恶意DLL文件，其中包含TelePowerDropper(名称是Group-IB定义的)。此DLL文件的主要目标是在受攻击设备的注册表中获得TelePowerBot的持久性。在某些情况下，DLL文件还可以启动攻击者的专有窃取程序，它会解析来自受害者设备上浏览器的数据，并将其存储在本地文件夹中。在初始访问期间，攻击者可以启动任何类型的窃取程序。Dark Pink可以在攻击的所有阶段发送特殊命令来下载和启动窃取程序。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975622108606.png "1673975622108606.png")

攻击链1的完整示意图

需要注意的是，在此阶段DLL文件已打包。当文件启动时，它对自己进行解密，并将控制权传递给自己的解压缩版本。此外，一旦DLL文件启动，就会创建一个互斥锁。其中一个例子是gwgXSznM-Jz92k33A-uRcCCksA-9XAU93r5。完成此步骤后，启动TelePowerBot的命令将添加到自动运行中。这意味着每次用户登录系统时，TelePowerBot都会被启动。这可以通过通过路径HKCU\Environment\UserInitMprLogonScript创建注册表项来实现。新建的密钥值如下:

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975644242305.png "1673975644242305.png")

上面的代码显示，该命令启动了一个标准实用程序whoami，它显示有关该设备当前用户的信息。输出被重定向到文件并完成执行。

此时还不知道TelePowerBot如何开始，答案的关键是文件扩展名.abcd。简而言之，攻击者使用此扩展名创建一个文件，作为名为“事件触发执行：更改默认文件关联”的技术的一部分。其思想是添加一个处理程序来处理注册表项树中无法识别的文件扩展名。这在下面的截图中有详细说明。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975660162232.png "1673975660162232.png")

创建扩展名为.abcd的文件时运行的详细命令截图

上面的屏幕截图详细介绍了在创建具有特定扩展名.abcd的文件时触发的PowerShell命令的一部分。PowerShell命令存储在base64视图中，并且高度模糊。这些命令的结果相对简单：读取注册表项、解密并启动TelePowerBot。

**攻击链2：Github宏**

攻击链的第二个变异与前一个几乎完全相同。唯一不同的是初始阶段使用的文件。在我们的分析过程中，我们发现攻击者使用命令在打开初始ISO文件中包含的.doc时自动从Github下载包含TelePowerBot的恶意模板文档。写入此模板文档的宏代码可以确保恶意软件的持久性。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975680167283.png "1673975680167283.png")

攻击链2的完整示意图

在本例中，发送给受害者的ISO映像包含一个MS Word文档，导致从Github自动下载包含TelePowerBot的恶意模板文档。为了在初始访问期间避开检测，宏代码被写入模板文档。这种技术被称为模板注入。宏包含多个带有字段的表单，在执行过程中，这些表单字段的值将被读取并作为注册表项中的值建立。

这个技巧可以帮助恶意软件躲避检测，因为文档本身不包含任何恶意功能或代码。编码的文档包含带有几个参数的表单，这些文件中包含的宏可以读取这些值，并确保TelePowerBot在受害者的设备上具有持久性。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975709136721.png "1673975709136721.png")

截图详细显示了两个包含预定义密钥和值的表单，这些密钥和值是由恶意宏代码写入到注册表中发送给受害者的MS Word文件中。

**攻击链3：X(ML)标记点**

我们将详细介绍的第三种也是最后一种攻击链变体是Group-IB分析的最近一次Dark Pink攻击中使用的一个，在2022年12月8日，攻击者破坏了印度尼西亚政府机构的网络。通过鱼叉式网络钓鱼电子邮件发送给受害者的ISO映像包含诱饵文档、已签名的合法MS Word文件和名为KamiKakaDropper的恶意DLL。此攻击载体的主要目标是在受攻击的设备上持久化KamiKakaBot。在这个攻击链中，XML文件位于加密视图中诱饵文档的末尾。与攻击链 1一样，恶意DLL文件是由DLL侧加载技术启动的。一旦DLL文件启动，启动下一阶段攻击链的XML文件将从诱饵文档中解密并保存在受攻击的设备中。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1673975733354271.png "1673975733354271...