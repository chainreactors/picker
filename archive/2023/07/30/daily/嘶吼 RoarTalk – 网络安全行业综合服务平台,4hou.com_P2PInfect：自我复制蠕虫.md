---
title: P2PInfect：自我复制蠕虫
url: https://www.4hou.com/posts/MKWG
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-30
fetch_date: 2025-10-04T11:52:25.066606
---

# P2PInfect：自我复制蠕虫

P2PInfect：自我复制蠕虫 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# P2PInfect：自我复制蠕虫

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-07-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117281

收藏

导语：2023年7月11日，Unit 42研究人员发现了一种新的对等（P2P）蠕虫，研究人员将其称之为P2PInfect。

2023年7月11日，Unit 42研究人员发现了一种新的对等（P2P）蠕虫，研究人员将其称之为P2PInfect。对等网络，即对等计算机网络，是一种在对等者（Peer）之间分配任务和工作负载的分布式应用架构，是对等计算模型在应用层形成的一种组网或网络形式。“Peer”在英语里有“对等者、伙伴、对端”的意义。因此，从字面上，P2P（Peer-to-peer）可以理解为对等计算或对等网络。该蠕虫使用Rust编写，Rust是一种高度可扩展且对云友好的编程语言，能够跨平台攻击，并针对Redis，这是一种在云环境中大量使用的流行开源数据库应用程序。

Redis实例可以在Linux和Windows操作系统上运行。Unit 42的研究人员在过去两周内发现了超过30.7万个公开通信的独特Redis系统，其中934个可能容易受到这种P2P蠕虫变体的攻击。虽然并非所有Redis实例都会受到攻击，但蠕虫仍然会以这些系统为目标并试图进行攻击。

P2PInfect蠕虫通过利用Lua沙盒逃逸漏洞CVE-2022-0543攻击易受攻击的Redis实例。虽然该漏洞于2022年被披露，但目前尚不完全清楚其攻击范围和目标。然而，它的CVSS得分10.0。此外，P2PInfect利用Redis服务器在Linux和Windows操作系统上运行的优势，比其他恶意软件更具可扩展性。Unit 42研究人员观察到的P2P蠕虫是攻击者利用该漏洞进行严重攻击的一个示例。

P2PInfect利用CVE-2022-0543进行初始访问，然后释放建立P2P通信的初始有效负载。一旦建立了P2P连接，蠕虫就会删除其他恶意二进制文件，如操作系统特定的脚本和扫描软件。然后，受攻击的实例加入P2P网络，以向未来受攻击的Redis实例提供对其他有效负载的访问。

以这种方式利用CVE-2022-0543使P2PInfect蠕虫在云容器环境中更有效地运行和传播。Unit 42的研究人员就是在HoneyCloud环境中发现蠕虫的，因为它攻击了HoneyCloud环境中的Redis容器实例，HoneyCloud是一组蜜罐，用来识别和研究跨公共云环境的新型基于云的攻击。研究人员认为，这次P2P攻击活动是利用这种强大的P2P命令和控制(C2)网络的潜在更强大的攻击的第一阶段。P2PInfect的恶意工具包中存在“挖矿”功能。然而，研究人员没有发现任何确切的证据表明曾经发生过挖矿。此外，P2P网络似乎拥有多种C2功能，如“自动更新”，这将允许P2P网络的控制器将新的有效负载推送到网络中，从而改变和增强任何恶意操作的性能。

Unit 42于2023年7月11日使用Palo Alto Networks的HoneyCloud环境发现了第一个已知的P2PInfect实例，这是一组蜜罐。

P2PInfect蠕虫使用P2P网络来支持和促进恶意二进制文件的传输。我们之所以选择这个名称，是因为术语P2PInfect出现在泄露的符号中，反映了恶意软件的结构，如下图所示。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398083153376.png "1690398083153376.png")

Windows版本、名称和Redis模块的建构

所有收集到的P2P蠕虫样本都是用Rust编写的，Rust是一种高度可扩展且对云友好的编程语言。这使得蠕虫能够针对Linux和Windows操作系统上的Redis实例进行跨平台攻击，请注意，Redis不正式支持Windows操作系统。

该蠕虫使用CVE-2022-0543攻击Redis。针对该特定漏洞的首次攻击于2022年3月被发现，导致受攻击的Redis实例可能与Muhstik僵尸网络有关。然而，P2PInfect蠕虫似乎与另一个恶意网络有关，目前还不知道与Muhstik僵尸网络是否有关。

通过利用Lua漏洞进行初始攻击后，执行初始有效负载，该初始有效负载建立与更大的C2僵尸网络的P2P通信，该僵尸网络充当P2P网络，用于向未来攻击的Redis实例传播其他有效负载。一旦建立了P2P连接，蠕虫就会传播额外的有效负载，例如扫描仪。然后，新攻击的实例加入P2P网络的行列，为未来受攻击的Redis实例提供扫描有效负载。

P2PInfect利用CVE-2022-0543在云容器环境中实施攻击。容器的功能减少了，例如，取消了“cron”服务。许多利用Redis的蠕虫使用cron服务实现远程代码执行（RCE）。P2PInfect结合了CVE-2022-0543的漏洞，旨在覆盖尽可能多的易受攻击场景，包括云容器环境。

由于P2PInfect蠕虫是新发现的，我们在这里重点进行样本分析及其支持的P2P架构。

**利用CVE-2022-0543**

P2PInfect目前利用Lua沙盒逃逸漏洞CVE-2022-0543进行初始访问。此漏洞已在Muhstik和Redigo等以前的攻击中被使用，这两种攻击都导致受攻击的Redis实例参与针对其他系统的拒绝服务（DoS）、Flooding攻击和暴力攻击。

这种利用向量遵循与之前所看到的类似的模式。然而，P2PInfect的漏洞利用后操作与以前使用该漏洞的操作有很大不同。需要注意的是，此漏洞不是Redis应用程序漏洞，而是Lua沙盒漏洞。

虽然这个活动确实针对易受攻击的Redis实例并执行类似蠕虫的操作，但与其他已知的以Redis为目标并部署蠕虫的组织没有已知的联系，例如Automated Libra(又名PurpleUrchin)， Adept Libra(又名TeamTNT)， Thief Libra(又名WatchDog)， Money Libra(又名Kinsing)， Aged Libra(又名Rocke)或Returned Libra(又名8220)。

**P2PInfect如何利用CVE-2022-0543攻击易受攻击的Redis实例**

P2PInfect蠕虫的初始攻击媒介就是通过CVE-2022-0543利用Redis，这在已知的以Redis实例为目标的其他以加密劫持为任务的蠕虫中并不常见，例如Adept Libra（又名TeamTnT）、Thief Libra（别名WatchDog）、Money Libra（又称Kinsing）。

CVE-2022-0543是Lua库中的一个漏洞，与Debian Linux包管理打包和传播Redis的方式有关。因此，它只影响使用Debian的Redis用户。由于专注于操作系统并利用Redis的一个子组件进行攻击，P2PInfect的攻击因此很复杂。下图是捕获的CVE-2022-0543漏洞的一个示例。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398398190061.png "1690398398190061.png")

Debian操作系统上的P2PInfect漏洞利用示例

如上图所示，可以看到漏洞是如何被攻击者利用的。通过/dev/tcp使用网络请求，如第四行所示，攻击者通过端口60100连接到一个C2 IP地址，写入IP cnc。端口60100是P2PInfect用于维护C2通信的P2P通信端口之一。第四行中的初始有效负载将GET请求设置到目录/linux，该目录是维护P2PInfect蠕虫核心功能的主要滴管。其他二进制文件分布在P2P网络中。

**网络通信行为**

P2PInfect使用其P2P网络向新攻击的系统或云传播后续恶意软件。当系统首次受到攻击时，它将建立到P2P网络的连接，并下载要使用的自定义协议的样本。如下图所示，命令GET/linux之后是核心P2PInfect功能的映像下载。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398412193240.png "1690398412193240.png")

显示P2PInfect下载的网络通信协议

Linux和Windows操作系统P2PInfect示例以相同的方式进行通信。linux、miner、winminer和windows以明文形式从P2P网络下载。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398428121880.png "1690398428121880.png")

从P2P网络中提取的恶意软件样本的列表

一旦核心P2PInfect样本完成执行，有效负载将开始扫描其他主机以进行攻击。扫描的重点是暴露的Redis主机。然而，研究人员还发现，受攻击的Redis实例也会在端口22 SSH上执行扫描尝试。由于P2PInfect没有已知的攻击SSH的企图，目前还不清楚为什么会发生这种扫描操作，但端口22在被其他已知蠕虫攻击后被扫描并不罕见。

**节点通信**

主滴管使用TLS 1.3与当前已配置节点列表上的任何其他侦听P2P成员进行通信。当受攻击节点向P2P网络发送具有所有已知节点的json请求时，C2基础设施被更新。C2基础设施的更新将自动下载。节点更新的示例如下图所示。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398443195092.png "1690398443195092.png")

P2P节点更新

带有x.x.x.x的值是当前节点IP或新学习的节点。

**扫描行为**

下图展示了受攻击主机扫描暴露SSH实例的网络扫描过程。这些扫描操作发生在P2PInfect功能选择的随机网络范围内。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398458344282.png "1690398458344282.png")

扫描SSH实例

下图是对暴露的Redis实例的P2PInfect扫描操作。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398474171242.png "1690398474171242.png")

扫描Redis实例

**P2PInfect的其他观察结果**

一些发送到被攻击系统的初始有效负载p2p样本包含UPX，而第二阶段的恶意软件样本miner和winminer没有包含UPX。

在第一个滴管运行后，它开始解密从命令行接收的配置，以及关于P2P网络中其他节点的信息。我们发现P2P端口是可变的，这有利于攻击者发起攻击。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398489102255.png "1690398489102255.png")

P2PInfect的可变端口示例

Unit 42研究人员发现的所有样本都是用Rust编写的，有些样本内部有“泄露的符号”，这可以显示恶意软件开发者的项目结构。例如，windows示例主执行线程泄露了项目的名称以及攻击者的文件目录使用情况。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398506772143.png "1690398506772143.png")

从核心Windows P2PInfect样本中提取的分析

研究人员还发现了一个PowerShell脚本，用于在受感染的主机和P2P网络之间建立和维护通信。PowerShell脚本利用encode命令来混淆通信启动。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398526176278.png "1690398526176278.png")

混淆PowerShell命令建立P2P网络连接

PowerShell命令执行的第一个操作之一是配置本地系统防火墙，以阻止对受攻击Redis应用程序的合法访问（见下图的第五行）。然后（从图11中的第17行开始），脚本打开一个通信端口，供攻击者访问受攻击实例。这是持久性攻击的一种形式，允许攻击者保持对受感染主机的访问并保持其可操作性。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398543135651.png "1690398543135651.png")

修改被攻击Windows实例的网络流量规则

从解码的PowerShell中可以看出防火墙配置设置如下：

对等端口为60102，此端口是可变的，因为并非所有节点都使用相同的端口；

Redis端口6379只允许连接已知的C2 IP；

防火墙规则名为Microsoft Sync；

**监控进程**

在Windows操作系统中运行时，初始P2PInfect负载的另一个有趣功能是一个名为Monitor的进程。Monitor进程的作用是维护受攻击主机上运行的P2PInfect进程的功能。Monitor被转储到C:\Users\username\AppData\Local\Temp\cmd.exe，Monitor (cmd.exe)枚举系统运行进程的示例如下所示：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398566135174.png "1690398566135174.png")

P2PInfect监控器示例cmd.exe进程树

启动Monitor（cmd.exe）后，初始P2PInfect负载从P2P网络下载其自身的新版本，并将它们以随机名称保存到相同原始文件夹中，然后释放加密配置（.conf）。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398582150739.png "1690398582150739.png")

随机文件名的示例

执行新的P2PInfect下载版本，并启动扫描操作以查找其他易受攻击的Redis实例。初始P2PInfect滴管将尝试删除自己。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690398598415630.png "1690398598415630.png")

删除核心P2PInfect有效负载

**总结**

P2PInfect蠕虫...