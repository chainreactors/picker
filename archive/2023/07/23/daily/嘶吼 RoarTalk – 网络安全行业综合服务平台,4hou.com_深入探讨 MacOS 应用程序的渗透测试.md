---
title: 深入探讨 MacOS 应用程序的渗透测试
url: https://www.4hou.com/posts/z4Qq
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-23
fetch_date: 2025-10-04T11:51:16.800208
---

# 深入探讨 MacOS 应用程序的渗透测试

深入探讨 MacOS 应用程序的渗透测试 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 深入探讨 MacOS 应用程序的渗透测试

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-07-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102095

收藏

导语：随着macOS及其应用程序的普及，针对它们的攻击越来越多。为了确保这些应用程序的安全性，需要进行渗透测试。

![微信截图_20230717074204.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551866549785.png "1689551866549785.png")

首先，我们将定义什么是macOS应用程序。此外，我们将用Swift编程语言创建一个简单的应用程序，并配置应用程序沙盒功能。它还涵盖了基本的GUI和网络测试，包括Burp Suite的配置以及SIP与此的关系。

**应用程序结构**

让我们从定义什么是macOS应用程序开始，macOS应用程序是为在苹果的macOS操作系统(以前的OS X)上运行而设计的软件，它由一组文件和资源以特定格式捆绑在一起，通常有一个用户界面。一些流行的macOS应用程序包括Safari、Chrome和Word。Swift和Objective-C是创建macOS应用程序最常用的编程语言，但macOS也支持其他语言，如C和c++。

许多应用程序都是从App Store获得的，但用户也可以选择从第三方资源下载和安装应用程序。安装后，应用程序通常位于/Applications或~/Applications路径，但也可以存储在其他位置。例如，系统应用程序是通过/system/applications路径访问的。需要注意的是，macOS应用程序可以通过查找“.app”扩展来区分，并存储为包，也称为应用程序包（Application Bundle）：包（bundle）是一个具有标准化层次结构的目录，通常包含可执行代码和该代码使用的资源。包扮演着许多不同的角色：应用、应用扩展、框架和插件都是包。包也可以包含其他包。

虽然包在Finder中显示为单个文件，但它实际上是一个目录。要查看应用程序的内容，右键单击文件名并选择“显示包内容”。在Content目录中，你可以找到如下所示的几个子目录：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551881463990.png "1689551881463990.png")

应用程序内容

macOS应用程序包的基本结构包括以下内容：

Info.plist：这个文件包含应用程序的配置信息，例如包标识符和包版本；

MacOS：这个目录包含主要的可执行文件；

Resources：该目录包含应用程序的资源，如图像、本地化和接口文件；

你可以在应用程序包中找到的其他目录：

Frameworks：此目录包含由主可执行文件加载的框架和动态库；

Plugins：这个目录包含应用程序扩展和插件，它们是扩展应用程序功能的软件组件。插件通常作为共享库开发，提供特定应用程序定义的API和接口。他们可以为特定的应用程序添加新功能，例如提高残疾人可用性的无障碍插件。另一方面，扩展是一种修改操作系统行为的插件，例如向Spotlight搜索功能添加新功能；

Library: 此目录可能包含各种子目录，包括：

LaunchServices：该目录包含由服务管理框架安装的特权助手工具，这些工具允许应用程序和进程执行需要管理权限的系统级任务。它们在后台运行，使用进程间通信(IPC)机制(如Mach消息或XPC)与主应用程序通信。这些工具通常作为启动守护进程或启动代理实现，负责管理后台进程。应用程序代理在用户登录时启动并继续在后台运行，而应用程序守护进程则从系统启动开始在后台持续运行，它们分别在/Library/LaunchAgents和/Librare/LaunchDaemons中的plist文件中定义。

SystemExtensions：该目录包括系统扩展，允许网络扩展和端点安全解决方案等软件在不需要内核级访问的情况下扩展macOS的功能。如今，这些扩展被用作内核扩展（kext）的替代方案。

XPCServices：该目录包括macOS应用程序中用于实现进程之间通信的XPC服务。XPC服务被实现为一个单独的二进制可执行文件，它在后台运行，可以由多个进程使用。

完整的列表可以在苹果的文档中找到。

**虚假应用程序**

我们搜索了一个包含一些错误配置的虚假应用程序，例如：

网络上未加密的数据；

各种应享权利；

无效的代码签名；

加载可被劫持的dylib；

但是我们找不到一个适合我们需要的，因此，我们决定创建自己的应用程序。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551903257702.png "1689551903257702.png")

虚假应用程序

幸运的是，我们发现了一个有趣的博客，在整个Swift语言应用程序开发过程中为我们提供了有用的指导。

在构建我们的应用程序时，除了一个基本的应用程序外，我们还添加了一些代码，其中包括向服务器发送HTTP请求的功能。

你可以在下面找到“复杂”应用程序的代码（代码片段1）：

![3.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551918198804.png "1689551918198804.png")

![3.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551928980105.png "1689551928980105.png")

代码片段1：虚假应用程序代码

通过在Xcode中创建一个新的macOS应用程序，它将获得应用程序沙盒权限和默认功能集。

为了允许我们的应用程序创建网络请求，我们添加了一个用于输出连接的功能，该功能将com.apple.security.network.client授权添加到我们的应用程序中。

![4.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551946153635.jpg "1689551946153635.jpg")

Xcode中的应用沙盒功能

应用程序沙盒限制访问系统资源和macOS应用程序中的用户数据，可以通过授权进行访问。

功能和授权是决定应用程序权限和访问级别的两种机制。功能定义了应用程序需要使用的功能，比如摄像头或互联网。同时，授权授予应用程序与操作系统和其他应用程序交互的访问权限。

对于某些操作，我们需要添加特定的功能，例如：

为了访问互联网，我们添加了传入/传出连接的功能，这将自动为应用程序提供com.apple.security.network.\*权限。

为了访问硬件，例如内置摄像头，我们添加了特定硬件的功能，该功能为应用程序提供了com.apple.security.device.\*权限。

为了访问文件，我们添加了特定文件和权限的功能，为应用程序提供了com.apple.security.files.\*权限。

默认情况下，在macOS 10.15或更高版本中，所有Mac应用程序必须经过苹果的“公证”才能启动。请参阅苹果文档公证macOS软件之前发布的更多细节。如果我们必须通过App Store传播应用程序，则需要通过额外的安全检查进行公证。

我们可以通过以下步骤查看虚假应用的应用包：

点击Xcode菜单中的“Product”；

选择“Archive.”；

右键单击并从上下文菜单中选择“在Finder中显示”；

**GUI测试**

与Windows和Linux客户端一样，第一步将是识别常见的用户输入界面，并测试它们的安全漏洞，例如SQL注入或跨站点脚本。

此外，了解应用程序的行为和功能也是必不可少的。这包括了解应用程序如何处理用户输入，它存储和收集什么数据，以及它如何与外部系统交互。

**网络测试**

分析应用程序和服务器之间的网络通信对于渗透测试至关重要。我们可以通过检查网络流量来检测未经加密或通过不安全通道传输的敏感信息。

然而，在macOS中，我们默认启用SIP。首先，让我们了解SIP是什么。

**系统完整性保护**

SIP（系统完整性保护）是一种安全功能，可防止恶意软件修改Mac系统上受保护的文件和文件夹。它限制了root用户帐户，并限制了root用户可以在操作系统的受保护部分执行的操作。

系统完整性保护包括几种机制，包括：

文件系统保护：防止对/System、/sbin、/bin和/usr目录以及某些系统文件和文件夹进行任何修改。

运行时保护：SIP限制了附加调试器和防止代码注入的能力。

内核扩展保护：将内核扩展（kext）的安装限制为仅限苹果批准和签署的内核扩展。

macOS中的SIP机制阻止我们监控网络活动，因此禁用SIP对于我们的需求是必要的。我们不建议禁用SIP，但我们将禁用它进行测试。

要禁用SIP，请遵循以下步骤，在恢复模式下从实用程序菜单中启动终端，运行命令csrutil disable并重新启动macOS。使用用户身份登录后，打开终端并执行命令csrutil status，查看SIP是否成功关闭。

重要的是要记住，禁用SIP可能会使你的系统容易受到恶意攻击，因此请确保在完成研究后重新启用它。你可以按照上面提到的相同步骤启用SIP，但不是运行csrutil disable，而是运行csrutil enable。

既然SIP已被禁用，我们就可以继续配置代理来拦截和分析虚假应用程序的网络活动。

为此，我们将使用BurpSuite工具，它将允许我们拦截、操纵和分析web应用程序与其服务器之间的HTTP和HTTPS流量。

下面是在macOS系统上配置代理的步骤：

1.下载并安装BurpSuite：你可以从PortSwigger网站下载该工具，安装很简单；

2.配置BurpSuite代理：为此，我们将导航到“Proxy”选项卡并选择“Options”选项卡。在这里我们将设置一些选项，例如代理侦听器和端口。在下一步中，我们应该以.der格式导出Burp证书，并将其保存在某个本地文件夹中。

![5.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551965831622.jpg "1689551965831622.jpg")

导出Burp证书

3. 安装导出的证书并允许系统使用它：

![6.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689551984110948.jpg "1689551984110948.jpg")

将证书安装到系统

4. 配置macOS网络设置：

要执行此操作，请导航到“系统首选项”菜单并选择“网络”。此时，我们将选择网络适配器并单击“高级”按钮。在“高级”菜单中，我们将选择“代理”选项卡并配置代理设置。我们将代理类型设置为“HTTP”，代理服务器设置为“127.0.0.1”，我们还将端口设置为“8080”。

![7.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689552001124109.jpg "1689552001124109.jpg")

代理配置

5. 验证代理配置：我们可以启动一个网络浏览器并导航到一个随机的网站来验证一切是否正常。然后，我们将返回到BurpSuite工具，并验证网络活动是否已被捕获。

**Wireshark**

此外，还可以使用Wireshark进行网络流量分析。

Wireshark是一种网络协议分析器，可以捕获和分析网络流量。我们可以使用它来检测网络通信中的安全弱点，例如明文密码、不安全的协议和敏感信息。

![8.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689552020194213.jpg "1689552020194213.jpg")

Wireshark未加密的流量

**总结**

我们了解了macOS应用程序及其结构，并演示了如何构建虚假应用程序。我们还讨论了SIP以及如何配置常用的网络拦截工具。

在下一部分，我们将深入研究文件和二进制分析，包括代码签名机制、强化的运行时异常和授权。此外，我们还将介绍一些用于这些目的的几种工具和技术。

本文翻译自：https://www.cyberark.com/resources/all-blog-posts/a-deep-dive-into-penetration-testing-of-macos-applications-part-1如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?cyWzJPXp)

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

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https:/...