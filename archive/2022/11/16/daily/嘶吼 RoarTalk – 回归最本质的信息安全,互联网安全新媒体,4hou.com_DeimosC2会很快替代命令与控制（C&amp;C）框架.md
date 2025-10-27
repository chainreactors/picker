---
title: DeimosC2会很快替代命令与控制（C&amp;C）框架
url: https://www.4hou.com/posts/mXmn
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-16
fetch_date: 2025-10-03T22:51:56.904436
---

# DeimosC2会很快替代命令与控制（C&amp;C）框架

DeimosC2会很快替代命令与控制（C&amp;C）框架 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# DeimosC2会很快替代命令与控制（C&C）框架

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-11-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)172901

收藏

导语：本文介绍了攻击者正在使用的几个C&C框架之一，DeimosC2便是其中之一。我们预计这些替代C&C框架的使用会有所增加，攻击者已经开始使用DeimosC2代替Cobalt Strike了。

随着网络防御者对Cobalt Strike的关注度上升，攻击者一直在寻找替代的命令与控制（C&C）框架，DeimosC2就是一个替代工具。

C&C系统对于渗透测试人员和安全人员来说是非常有用的协作工具。它们为所有受害设备提供了一个公共的位置，以便与之联系、进行控制，并允许多个用户与相同的受害设备进行交互。当执行授权测试时，这是非常重要的，因为日志保存在一个单独的地方，以帮助报告。然而，越来越多的这些工具被攻击者利用，包括开源工具和商业工具。它们的易用性和稳定性让它们能够长时间运行而没有任何问题，这也是为什么攻击者也开始转向这些C&C平台而不是建立自己的平台的原因之一。

由于大多数注意力都集中在像Cobalt Strike这样的成熟的商业工具上，攻击者一直在寻找能够提供许多相同功能的其他替代品。对于防御者来说，这意味着随着攻击者转向开源C&C软件，个人和组织都更难抵御网络攻击了。

**开源C&C软件**

与其他一些开源C&C框架(如Ares C2、PoshC2和TrevorC2)一样，DeimosC2提供了经典的C&C框架特性，但也提供了一个感觉和行为非常像Cobalt Strike或Metasploit Pro等商业工具的用户界面。

到目前为止，在地下犯罪组织中，将DeimosC2作为替代方案的讨论还不多，但攻击者可能会在不久的将来将DeimosC2作为首选工具。虽然DeimosC2不是攻击者目前寻找其他C&C平台使用的最受欢迎的选择，但研究DeimosC2，可以更好地了解是什么原因使攻击者想要使用这个平台作为C&C框架？

**什么是DeimosC2？**

DeimosC2是一个开源的C&C框架，于2020年6月发布。它是一个功能齐全的框架，允许多个攻击者访问受害计算机，为其创建有效负载并与之交互。作为一个利用后的C&C框架，DeimosC2将生成需要在计算机服务器上手动执行的有效负载，这些有效负载已经通过其他手段(如社会工程、利用或暴力攻击)被破坏。一旦部署有效负载，攻击者将获得与执行有效负载的用户帐户(管理员或普通用户)相同的系统访问权。注意，DeimosC2不执行任何类型的活动升级或特权升级。

利用后C&C服务器很受安全人员欢迎，因为它们提供了一种方便的方法，可以与多个受害设备交互，收集记录，并存储对每台设备所做的事情的证据。

**DeimosC2的特点**

DeimosC2有两种在系统上安装的选项：一种是不依赖于安装Go的预构建二进制文件，另一种是可以在任何安装了Go的系统上编译和运行的源代码。在这项研究中，使用了Debian虚拟机（VM）中预先构建的二进制文件，因此与使用直接从GitHub项目下载的源代码相比，某些行为可能有所不同。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228029650967.png "1668228029650967.png")

GitHub上的DeimosC2服务器二进制文件

DeimosC2结合了许多与其他c&c软件平台相同的特性。像DeimosC2这样的C&C系统的主要目的之一是帮助安全人员和渗透测试人员整合他们的基础设施，在研究期间通过共享被破坏的主机与他人协作。考虑到这一点，DeimosC2具有多个用户支持，为用户提供两种角色：管理员和用户。下图显示了DeimosC2测试中的两个用户设置。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228039170374.png "1668228039170374.png")

DeimosC2中的用户配置截图

因为DeimosC2也是针对安全研究人员的，所以它支持多因素身份验证(MFA)、API、备份和恢复特性，以及将系统标记为开发系统或生产系统的能力。

设置了用户之后，下一步是设置侦听器，侦听器是受害设备将接触到的套接字和协议。DeimosC2有五种类型的侦听器，用户可以为其有效负载配置这些侦听器，到目前为止我们看到的最常见的是HTTPS和TCP。我们预计，随着这些工具的普及，我们很可能会看到攻击者使用DNS over HTTPS DNS over HTTPS (DoH)选项。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228047124517.png "1668228047124517.png")

显示侦听器设置类型的截图

一旦做出选择(在本例中是HTTPS)，就会通过输入强制设置和某些可选设置所需的数据来配置侦听器。用户需要设置域名和IP地址，而密钥和大多数高级设置是可选的。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228057165701.png "1668228057165701.png")

显示HTTPS侦听器设置的截图

在高级设置中，有一些C&C服务器工作方式的可配置选项。在这里，你可以找到更改受害者将通过HTTP POST使用到C&C服务器的默认路径的设置。默认情况下，这些路径是/login、/index、/settings和/profile，但可以在创建侦听器期间更改这些路径。它们也可以在以后更改。然而，需要创建新的二进制文件。

配置完所有设置后，将根据设置的“编译选项”部分中的选项创建二进制文件。这些设置决定了要创建哪些二进制文件以及是否应该对它们进行模糊处理。

创建二进制文件后，通过从侦听器选项中选择“interactive”，即可通过界面下载它们。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228066112620.png "1668228066112620.png")

为HTTPS侦听器创建的侦听器的截图

一旦下载，这些软件就可以部署到通过其他方式（如网络钓鱼或漏洞攻击）受到威胁的设备上。易于使用，为C&C通信创建开发后二进制文件。

**DeimosC2代理分析**

虽然许多DeimosC2示例都使用了gobfuscate(一种用于混淆Go语言编写的程序的开源工具)，但我们也发现了未混淆的示例。这使我们能够识别出DeimosC2包的名称，我们发现这是一个开源的后开发C2框架。也可以手动消除gobfuscate等工具实现的更改的模糊化，但这太耗时。

在DeimosC2术语中，用于感染受害者的客户机二进制文件称为代理。DeimosC2利用Go语言的多平台特性为不同的体系结构(如Windows、Linux、macOS和Android)编译代理。

代理很简单：当执行时，它会立即尝试联系硬编码C&C域或IP地址中的侦听器，除非设置了执行时间范围。

DeimosC2代理使用三个不同的秘钥与侦听器交换消息。

**代理秘钥**

这是标识代理的唯一秘钥。秘钥最初被设置为"000000000000000000000000000000000000"，但是来自侦听器的第一个响应将它更新为一个新版本，4 UUID。

**AES密钥**

这个256位AES密钥是每次代理与C&C侦听器对话时随机生成的，这用于加密与C&C侦听器交换的消息。

**RSA密钥**

除了AES加密之外，DeimosC2还使用RSA-2048对代理和前面解释的AES密钥进行加密。代理使用硬编码的公钥加密其他密钥，而C&C侦听器使用其私钥解密数据。

下图从代理的角度说明了加密过程。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228076170848.png "1668228076170848.png")

DeimosC2代理加密方案

发送到C&C侦听器的第一条消息以JSON格式包含有关受感染设备的信息，如下图所示。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228086123159.png "1668228086123159.png")

首次发送到C&C侦听器的JSON数据示例

发送的数据包括有关操作系统、已安装的防病毒产品、主机名、登录的用户名、内部IP地址、文件系统上的代理路径、可用的shell程序、进程ID (PID)和用户特权的信息。

**命令**

C2侦听器响应可以包括一个或多个命令(在DeimosC2术语中称为“jobs”)。

DeimosC2命令及其描述如下：

Shell：执行shell命令；

下载：将文件下载到C&C服务器；

上传：将文件上传到受感染的计算机；

选项：抖动和延迟选项设置C&C通信的休眠时间。eol(我们假设它意味着生命结束)选项设置代理退出的日期，而hours选项配置通信的时间范围；

文件浏览器：要求代理列出给定路径上的所有文件和目录；

shellInject：在代理进程中注入并运行自定义shell代码；

模块：执行一个模块；

Reinit：重新连接代理，这会使代理获得一个新的代理密钥；

pivotTCP：启动受感染设备中的TCP服务器，以便其他代理可以将其用作侦听器，用于感染无法访问互联网的设备；

pivotJob：处理数据透视作业；

pivotKill：重置透视侦听器列表；

Kill：卸载代理；

**模块**

DeimosC2通过可以在受害者的设备中执行的模块扩展其功能， DeimosC2信息如下：

Screengrab：在受感染的设备上截屏；

Minidump：生成给定进程的用户模式小型转储；

Lsadump：下载SECURITY和SYSTEM注册表配置单元以窃取凭据；

Ntdsdump：下载Ntds.dit并且SYSTEM文件用于凭证窃取；

Samdump；下载SECURITY、SYSTEM和SAM注册表配置单元以窃取凭据；

Shadowdump：从Linux设备下载/etc/shadow文件；

DeimosC2的模块接口允许C&C侦听器推送新模块并从磁盘或内存(使用代码注入)执行它们。

**网络分析**

正如我们前面提到的，在使用DeimosC2时，用户可以选择几种侦听器类型，包括HTTPS、TCP和DoH。这些可能是最常见的选项，因为它们在其他C&C平台上很受欢迎。由于DeimosC2的开源特性，我们能够详细研究这些侦听器是如何工作的。

**HTTPS侦听器**

当监听器运行HTTPS时，我们发现有一个默认的网页被配置。通过查看GitHub页面，我们确认它是Apache的默认Ubuntu页面。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228097227072.png "1668228097227072.png")

显示标题的默认Apache Ubuntu页面的Nmap结果

根据安装过程中侦听器的配置，我们知道该工具使用了一些路径。查看代理源代码的.go版本，我们可以看到已经设置并正在使用的进程。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228107107525.png "1668228107107525.png")

代理使用的路径的Go变量

变量“firsttime”用于与服务器的初始通信。从那时起，变量“checkin”将被使用。

基于此，我们可以对C&C服务器是否为默认配置以及是否启用了HTTPS检测进行指纹识别。代理将向/login发送HTTP POST，然后定期向/index发送。HTTPS侦听器使用的默认端口为4443。但是，在任何其他端口上创建侦听器时，都可以轻松更改此端口。在/profile上，变量“moduleloc”用于将数据从代理发送回服务器。最后，使用“piviotloc”变量通过当前受害者传递数据，作为前面描述的代理piviotloc功能的一部分。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228116866077.png "1668228116866077.png")

HTTPS\_agent中的sendMsg函数

下图显示了由配置为使用HTTPS侦听器的代理发送的加密POST请求。默认情况下，它使用/login发送第一条消息，之后，代理默认情况下向/checkin发送请求。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228126163944.png "1668228126163944.png")

由配置为使用HTTPS侦听器的代理发送的加密POST请求

**TCP侦听器**

TCP侦听器利用Go语言函数创建数据包并将其发送到已创建的套接字。加密流程的工作原理与HTTPS加密相同。在这种情况下，唯一的区别是，整个消息的长度有助于数据的解密。为了实现这一点，它在加密数据的前面加上已加密和要发送的数据的长度。这将发送到套接字，然后发送到C&C服务器。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228137524624.png "1668228137524624.png")

来自TCP侦听器Go代码的sendMsg函数

根据我们对从TCP代理发送到侦听器的数据包的分析，这部分具有可预测的行为。由于uint64调用，创建的长度将是64位或8字节长的无符号整数。分组的数据部分的开始将有8个字节，用于随后的分组长度。我们在与C&C服务器的通信中观察到的大多数信息都是这样。每个数据包总共350字节，包含296字节的数据。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221112/1668228147826118.png "1668228147826118.png")

与C&C服务器通信的TCP代理的数据包的数据部分（突出显示部分）

由于我们知道数据包的数据部分前面有数据包大小，并且它是一个8字节的无符号整数，因此我们可以得出结论，数据的前8字节是处理数据包时将遵循的大小。

在本例中，有一个296字节的数据字段，如果我们去掉长度字段的8个字节，就会为来自C&C服务器的命令留下288个字节。如...