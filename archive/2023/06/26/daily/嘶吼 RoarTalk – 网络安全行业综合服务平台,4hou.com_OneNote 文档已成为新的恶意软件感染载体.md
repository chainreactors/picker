---
title: OneNote 文档已成为新的恶意软件感染载体
url: https://www.4hou.com/posts/GXRr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-26
fetch_date: 2025-10-04T11:45:05.573978
---

# OneNote 文档已成为新的恶意软件感染载体

OneNote 文档已成为新的恶意软件感染载体 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# OneNote 文档已成为新的恶意软件感染载体

丝绸之路
[新闻](https://www.4hou.com/category/news)
2023-06-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)205767

收藏

导语：OneNote 文档已成为一种新的感染媒介，其中包含在与文档交互时执行的恶意代码。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660412645626.png "1684241596141077.png")

随着越来越多的人提高了安全意识并实施强大的安全措施，并且安全软件变得更加复杂，传播恶意软件会变得比以往更加困难。正因为如此，黑客一直在寻找新的技术来欺骗受害者。

微软 Office 文件曾经是恶意软件的流行载体，但最近变得不那么有效了，部分原因是默认情况下 Office  软件不再启用宏。2022 年 2 月，微软禁用了文档中的VBA 宏，因为它们经常被用作恶意软件分发方法。此举促使恶意软件作者寻找新的方法来分发其有效负载，从而导致其他感染媒介的使用增加，例如密码加密的 zip 文件和 ISO 文件。黑客的最新选择是使用微软 OneNote 文件。

OneNote 文档已成为一种新的感染媒介，其中包含在与文档交互时执行的恶意代码。Emotet 和 Qakbot 以及其他高端窃取器和加密器是使用 OneNote 附件的已知恶意软件威胁。目前已观察到使用 OneNote 进行恶意软件传递的电子邮件活动具有相似的特征。尽管消息主题和发送者各不相同，但几乎所有的活动都使用独特的消息传递恶意软件，并且通常不使用线程劫持。消息通常包含 OneNote 文件附件，主题包括发票、汇款、财产和季节性主题(如圣诞节奖金)等。2023年1月中旬，安全研究人员观察到演员使用 URL 投递 OneNote 附件，这些附件使用相同的 TTP 执行恶意软件。这包括2023年1月31日观察到的 TA577 活动。

研究人员目前正在开发新的工具和分析策略来检测和防止这些 OneNote 附件被用作感染工具。本文重点介绍了这一新发展，并讨论了恶意行为者用来破坏系统的技术，以及为什么微软 OneNote 文件被用来传播恶意软件和您应该如何保护自己？

**为什么 OneNote 被用来传播恶意软件？**

OneNote 是微软开发的一款流行的笔记应用程序。它旨在提供一种快速记笔记的简单方法，并且包括对图像、文档和其他可执行代码的支持。

该软件功能丰富，因此也是黑客的理想选择。

2022 年，Microsoft 禁用了 Office 文件中的宏。除此之外，再加上大多数企业已经在努力防范 Office 文件，这意味着黑客现在正在寻找其他文件格式。

OneNote 是一个流行的应用程序，但更重要的是，它默认安装在所有 Windows 计算机上。这意味着即使潜在的受害者没有主动使用 OneNote，如果他们单击该文件，该文件仍会在他们的计算机上运行。

OneNote 是 Microsoft 应用程序，因此 OneNote 文件看起来值得信赖。这很重要，因为除非人们实际点击该文件，否则恶意软件不会传播。它还与其他 Microsoft Office 文件兼容，并且可以嵌入其中。

该软件允许嵌入许多不同类型的内容。这让黑客可以使用各种技术来启动恶意软件下载。OneNote 以前没有被用来分发大量恶意软件。正因为如此，大多数人不会怀疑此类文件，企业也不一定具备防御使用它们的攻击的能力。

**谁是目标？**

涉及 OneNote 文件的攻击主要针对企业。OneNote 文件附加到电子邮件中，然后批量发送给员工。这些文件通常附加到旨在窃取信息的网络钓鱼电子邮件中，但可以附加到任何类型的电子邮件中。

虽然企业员工是最有利可图的目标，但个人也是潜在的受害者。对个人的成功攻击将减少获利，但可能更容易实施。因此，每个人都应该提防不可靠的 OneNote 附件。

**OneNote 是如何被诈骗者利用的**？

恶意的 OneNote 文档包含嵌入式文件，通常隐藏在一个看起来像按钮的图形后面。当用户双击嵌入的文件时，系统会提示他们一个警告。如果用户继续单击，文件将执行。该文件可能是不同类型的可执行文件、快捷方式(LNK)文件或脚本文件，如 HTML 应用程序(HTA)或 Windows 脚本文件(WSF)。

**恶意 OneNote 文档概述**

将 OneNote 文档武器化的网络钓鱼活动的整体视图如下面的图2所示。恶意文件以 zip 文件或 ISO 映像形式通过钓鱼电子邮件传递给目标。我们已经观察到，大多数恶意文档要么有调用 Powershell 在系统上删除恶意软件的 Windows 批处理脚本，要么有执行相同操作的 VisualBasic 脚本。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660413283061.png "1684241613126065.png")

恶意 OneNote 文件会在电子邮件中分发，讨论发票和晋升、薪资等常见主题。它们还包括收件人需要下载文件的看似合理的理由。

某些电子邮件包含恶意 OneNote 文件作为附件。其他消息将用户引导至恶意网站，然后鼓励他们下载 OneNote 文件。

打开它后，受害者将被要求点击某种类型的图形。执行此操作后，将执行嵌入文件。嵌入式文件通常用于执行从远程服务器下载恶意软件的 PowerShell 命令。

**攻击链**

随着 VBA 宏的禁用，威胁参与者已转向使用 OneNote 附件作为在端点上安装恶意软件的新方法。OneNote 附件可以包含嵌入式文件格式，例如 HTML、ISO 和 JScripts，这些格式可以被恶意行为者利用。OneNote 附件对攻击者特别有吸引力，因为它们是交互式的，并且设计用于添加和交互，而不仅仅是查看。这使得恶意行为者更容易包含可能导致感染的诱人消息和可点击按钮。因此，用户在与 OneNote 附件交互时应谨慎行事，即使它们看起来无害。使用更新的安全软件并了解与交互式文件相关的潜在风险至关重要。

**恶意程序的文件头示例**

为了理解数据是如何在文件中布局的，我们需要在字节级别检查它。仔细观察OneNote文档，我们会发现一个有趣的现象，因为它的头文件的神奇字节并不是一个微不足道的字节。下图显示了文档二进制文件的前16个字节。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660414922766.png "1684241650154725.png")

前16个字节需要解释为 GUID 值{7B5C52E4-D88C-4DA7-AEB1-5378D02996D3}。我们可以使用 OneNote 规范的官方文档来理解所有字节及其结构。下图显示了来自 OneNote 规范文档的头信息。

![image (1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660415162672.png "1684241663981118.png")

**电子邮件 – 社会工程学**

与大多数恶意软件作者一样，攻击者通常使用电子邮件作为与受害者的第一联系方式。他们使用社会工程技术说服受害者打开程序并在他们的工作站上执行代码。

![download_image.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660415169639.jpeg "1684241677246859.jpeg")

在最近的网络钓鱼尝试中，攻击者发送了一封看似来自可靠来源的电子邮件，并要求收件人下载 OneNote 附件。但是，打开附件后，代码并未按预期自动更新。相反，受害者会收到一个潜在危险的提示。

![download_image (1).jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660416560600.jpeg "1684241691129984.jpeg")

在这种情况下，与许多 OneNote 附件一样，恶意行为者打算让用户单击文档中显示的“打开”按钮，从而执行代码。传统的安全工具无法有效检测此类威胁。

一种可用于分析 Microsoft Office 文档（包括 OneNote 附件）的工具是 Oletools。该套件包括命令行可执行文件 olevba，它有助于检测和分析恶意代码。

![download_image (2).jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660416480423.jpeg "1684241705211528.jpeg")

尝试在 OneNote 附件上执行该工具时，发生错误。因此，分析的重点转向动态方法。通过将文档放在沙箱中，我们发现了一系列脚本，这些脚本被执行以下载和运行可执行文件或 DLL 文件，从而导致更严重的感染，如勒索软件、窃取程序和文件擦除器。

![download_image (3).jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660417110309.jpeg "1684241718105576.jpeg")

**战术和技术**

这个特定的活动使用编码的 JScript 数据来隐藏他们的代码，利用 Windows 工具 screnc.exe。虽然采用编码形式，但 Open.jse 文件不可读。解码 JScript 文件后，发现了一个 .bat 文件的释放器。执行时，.bat 文件会启动一个 PowerShell 实例，该实例会联系 IP 地址 198[.]44[.]140[.]32。

![download_image (5).jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230625/1687660418263635.jpeg "1684241742987881.jpeg")

**利用 OneNote  可以安装什么恶意软件？**

OneNote 文件被攻击者以各种不同的方法使用。因此，涉及许多不同类型的恶意软件，包括勒索软件、特洛伊木马和信息窃取程序。

**勒索软件**

勒索软件专为勒索目的而设计。一旦安装，系统上的所有文件都会被加密，如果没有需要从攻击者那里购买的解密密钥，就无法访问。

**远程访问木马**

远程访问木马 (RAT)是一种允许攻击者远程控制设备的恶意软件。安装后，攻击者可以向机器发出命令并安装其他类型的恶意软件。

**信息窃取者**

信息窃取程序是一种用于窃取私人数据的木马。信息窃取程序通常用于窃取登录凭据，例如密码以及财务信息。一旦在您的计算机上安装了信息窃取程序，黑客就可以访问您的私人帐户。

**如何防范恶意 OneNote 文件**

幸运的是，针对恶意 OneNote 文件的攻击并不难防御。他们依赖于人们的粗心大意，因此您可以通过采取一些基本的安全预防措施来保护自己。

**不要下载电子邮件附件**

恶意 OneNote 文件只有在下载后才会执行。除非您确定知道发件人是谁，否则切勿下载电子邮件附件。

**备份文件**

尽量备份所有重要文件并将备份保存在单独的位置，即不使用外接存储设备插入您的计算机（因为勒索软件也会对其进行加密），则勒索软件的威胁较小。值得注意的是，以这种方式防御勒索软件并不能阻止黑客访问数据并威胁要发布数据。

**使用双因素身份验证**

远程访问木马可用于窃取密码。为了防止这种情况，您应该为所有帐户添加双因素身份验证。双因素身份验证可防止任何人登录您的帐户，除非他们还提供第二条信息，例如发送到您设备的代码。激活后，您的密码可能会被盗，小偷仍然无法访问您的帐户。

**使用杀毒软件**

如果您有防病毒套件，许多类型的勒索软件和远程访问木马将被阻止运行。但是，不应将防病毒软件作为唯一的防线，因为许多恶意 OneNote 文件专门设计用于绕过它。

**企业应提供员工培训**

所有企业都应就此威胁对员工进行教育。员工需要知道网络钓鱼电子邮件的样子，并且不应允许他们下载附件。

**OneNote 文件是黑客的理想选择**

OneNote 文件是传播恶意软件的理想选择。它们是能够在大多数人的计算机上运行的可信文件。它们也与恶意软件无关，因此许多企业没有能力抵御它们。

任何执行恶意 OneNote 文件的人都可能对其数据进行加密或窃取其个人信息。前者需要支付赎金，而后者可能导致账户被盗和财务欺诈。

企业和个人都应该意识到这种威胁，并可以通过遵循基本的安全措施来防范它。

**结论**

为了有效应对不断变化的威胁形势，对安全分析师来说，必须及时了解恶意软件作者使用的最新攻击策略。如果系统没有适当配置以防止此类附件绕过适当的清理和检查，这些方法可以规避检测。因此，分析师必须熟悉分析这些附件的技术。目前，建议进行动态分析，因为将样本放在沙箱中可以提供有关恶意软件的关键信息，包括它连接到的 C2 服务器、进程链信息以及数据写入磁盘然后执行的位置。为了进行更深入的分析，分析师还应该熟悉通常与 OneNote 附件关联和嵌入其中的各种文件格式，

需要注意的是，只有当接收方使用附件时(特别是通过单击嵌入的文件并忽略 OneNote 显示的警告消息) ，攻击才会成功。然而，最好的防御永远是预防。因此，安全团队必须更新他们的系统以检测这些类型的附件，并教育员工下载未知和不受信任的附件的危险。

本文翻译自：https://cybersecurity.att.com/blogs/security-essentials/onenote-documents-have-emerged-as-a-new-malware-infection-vector如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?a5I76GLQ)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/post...