---
title: 攻击者如何在攻击中滥用原生 Linux 工具
url: https://www.4hou.com/posts/PJln
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-16
fetch_date: 2025-10-03T20:01:54.371872
---

# 攻击者如何在攻击中滥用原生 Linux 工具

攻击者如何在攻击中滥用原生 Linux 工具 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者如何在攻击中滥用原生 Linux 工具

lucywang
[技术](https://www.4hou.com/category/technology)
2022-10-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124504

收藏

导语：通过趋势科技的蜜罐和监测技术，研究人员能够观察到攻击者滥用原生 Linux 工具对 Linux 环境发起攻击的实例。

通过趋势科技的蜜罐和监测技术，研究人员能够观察到攻击者滥用原生 Linux 工具对 Linux 环境发起攻击的实例。

采用容器已经成为主流，各类企业的使用率都在上升。根据 CNCF 的一项调查，93% 的受访者目前正在或计划在其运行中使用容器。像Kubernetes这样的容器项目和其他在云和互联网上可用的工具，已经导致了组织运作方式发生变化，从单一架构到创建由微服务组成的分布式系统。

由于使用了容器这些变化也导致了攻击面的扩大，特别是通过在部署中引入的安全错误配置或漏洞。对于使用容器的企业来说，补丁管理常常是一项巨大的任务，这意味着更新并不总是及时地实现，这使得云安全更加复杂。

研究人员已经在面向公众的 Web 应用程序中发现了各种来源的严重漏洞，从易受攻击的开源库（Log4Shell 和 Spring4Shell）到框架（Apache Struts 和 Drupal），甚至是诸如Atlassian Confluence、Oracle WebLogic Server 和 Apache HTTP Server等应用程序。一旦漏洞的概念证明 (POC) 被披露，攻击者就可以利用它们执行恶意任务，从挖掘加密货币到有时部署勒索软件。

从防御者的角度来看，理想的结果是阻止攻击者获得最初的立足点。然而，情况并非总是如此。如果攻击者确实设法进入系统，则防御者的工作就是通过使用纵深防御策略使攻击者更难成功地完成攻击。

通过蜜罐网络和监控分析，研究人员能够观察到大多数成功利用尝试的一些有趣特征，特别是攻击者如何在其例程中使用本机 Linux 工具。

**在 Linux 环境中使用合法实用程序和工具检查攻击**

对基于 Linux 的系统的攻击通常遵循标准的利用链。首先，攻击者利用一个漏洞或一系列漏洞来获得对环境的初始访问权限（我们现在可以将其视为受到攻击）。此时，攻击者可以采取不同的路径进一步进入被破坏的环境：

1.枚举当前环境的上下文（发现）；

2.从环境中泄露敏感数据（泄露、影响）；

3.通过删除应用程序执行拒绝服务攻击（影响）；

4.通过下载挖矿软件来挖掘加密货币（影响）；

5.尝试其他技术（权限升级、横向移动、持久性或凭据访问）；

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708317550031.png "1662708317550031.png")

攻击者如何在受感染的环境中进一步发起攻击

基于真实世界的攻击和蜜罐捕获的样本，研究人员观察到攻击者使用与 Linux 发行版捆绑在一起的各种启用工具，例如 curl、wget、chmod、chattr、ssh、base64、chroot、crontab、ps 和 pkill ，这些工具都可以被攻击者利用。

我们已经看到攻击者在野外滥用这些工具。至少应该考虑这些实用程序的存在，尤其是在容器环境中，因为它们为攻击者提供了额外的途径。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708325102815.png "1662708325102815.png")

使用base64解码有效负载，以便稍后执行

base64 工具是一个 Linux 实用程序，用于解码以 base64 格式编码的字符串。攻击者经常使用 base64 编码来混淆他们的有效载荷和命令以逃避检测 (T1027)，我们在之前的文章《恶意Shell脚本的进化》中详细描述了这种技术。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708335133272.png "1662708335133272.png")

使用“cat”进程查看所有用户的 .bash\_history

.bash 历史文件存储在用户的主目录中，记录用户在其 bash shell 上执行的命令。众所周知，攻击者会从这些文件中提取信息以了解当前环境的上下文，正如我们之前在另一篇文章中所详述的那样，错误配置的 Docker 守护程序 API 端口因 Kinsing 恶意软件活动而受到攻击。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708343138934.png "1662708343138934.png")

使用“cat”进程查看“/etc/passwd”

作为枚举步骤的一部分，攻击者访问 /etc/passwd 文件，该文件包含环境中已注册用户的列表，并显示给定用户是否具有与其登录相关联的 shell（T1003.008）。此信息有助于攻击者了解环境并确定有价值的用户。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708380138019.png "1662708380138019.png")

使用“chattr”` 将 /etc/crontab 文件修改为可变

chattr 实用程序用于更改文件和文件夹属性，以控制文件的删除和修改等突发操作。上图中的示例显示 /etc/crontab 文件的属性已被更改，导致文件不安全。正如《分析TeamTNT 的活动》中所讨论的，该实用程序之前已被观察到被 TeamTNT 滥用。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708389932616.png "1662708389932616.png")

使用“chmod”使文件可执行

chmod工具用于修改文件模式，实现用户/组访问粒度化。它需要执行新下载的可执行文件，在本例中，我们看到/tmp路径上的agettyd文件被设置为可执行位。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708398102315.png "1662708398102315.png")

使用“crontab”删除所有现有的 cron 作业

cron作业是用于调度任务(或作业)的实用工具。众所周知，攻击者滥用cron作业并修改“crontab”来执行执行、持久性，有时还会使用特权升级技术(T1053.003)。上图中的示例显示了对现有cron作业的删除。这种情况很常见，加密货币挖矿软件通过删除其他挖矿软件的痕迹来劫持尽可能多的资源。《Linux 加密货币挖矿软件之战》深入讨论了这些活动。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708407197992.png "1662708407197992.png")

使用“curl”将系统信息泄露给攻击者

curl 或 cURL 实用程序用于跨不同协议传输数据，例如 HTTP、HTTPS 和文件传输协议 (FTP)。上图中的示例显示操作系统版本和发布版本等系统信息作为 POST 请求发送到攻击者的基础设施。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708416205764.png "1662708416205764.png")

使用“curl”从 GitHub 下载 xmrig 二进制文件

在本例中，curl用于从Github下载XMRig 挖矿软件的二进制文件。众所周知，攻击者滥用像Github和Netlify这样的合法平台来服务于加密挖掘工具，正如我们在之前的《通过 GitHub、Netlify 提供的门罗币挖掘恶意软件漏洞》博客中解释的那样。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708426179443.png "1662708426179443.png")

使用“pkill”阻止竞争进程/coinminer

kill 套件实用程序用于向进程发送信号，如上图中的示例所示，它将 SIGKILL 信号发送到名为“kdevtmpfsi”的进程。早在 2020 年，我们就一直在追踪名为 kdevtmpfsi 的加密货币挖矿软件，《分析 Kinsing 恶意软件对 Rootkit 的使用》展示了另一个竞争挖矿软件被终止的例子。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708435125757.png "1662708435125757.png")

使用“ps”查看正在运行的进程

ps 实用程序用于查看进程的状态。上图显示了 ps aux 命令获取有关进程的详细信息，例如系统上当前正在运行的进程、进程 ID 和进程权限。此信息可以帮助攻击者执行与发现相关的技术（T1057 ——进程发现）并获取有关他们所处环境的信息。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708445136638.png "1662708445136638.png")

使用“rm”从 /tmp 目录中删除隐藏文件

在上图中，我们看到 rm 工具用于删除 /tmp 目录下的隐藏文件和文件夹。在文件或文件夹名称之前，攻击者可以通过添加“.”来创建隐藏目录以逃避检测（隐藏工件：隐藏文件和目录 - T1564.001）。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708455104990.png "1662708455104990.png")

使用“ssh”通过 XMR 挖矿软件感染底层主机

ssh 实用程序是用于通过 Secure Shell (SSH) 以类似蠕虫的方式访问系统的远程客户端。在上图中，攻击者尝试下载 Monero 挖矿软件（使用 wget/curl）并感染正在尝试 SSH 的远程计算机（127.0.0.1）。一旦攻击者由于容器的不安全配置（例如，特权容器）而挂载了底层主机的文件系统，他们就会创建新的 SSH 密钥对，使用它来建立“ssh”会话，并用加密货币挖矿软件感染底层主机。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708464163945.png "1662708464163945.png")

使用“wget”、“curl”、“chmod”下载并执行 Mirai 恶意软件

在此示例中，我们看到了不同 Linux 实用程序的组合使用，其中下载了二进制文件，修改了权限，然后再执行。名为“runnable”的可执行文件是在CVE-2021-44228跟踪的Log4shell漏洞被利用后发布的Mirai示例。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708476804918.png "1662708476804918.png")

使用“whoami”查看当前用户上下文

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708486126245.png "1662708486126245.png")

显示攻击者使用“chroot”和“base64”的工作台

使用 Vision One 工作台，我们看到攻击者正在使用 chroot 和 base64 实用程序。请注意，chroot 用于将根更改为提供的目录（在本例中为 /host），其中底层主机的文件系统安装在容器中。在《为什么特权容器很容易被攻击》一文中，我们探讨了此函数在授予容器时所带来的风险。

**保护 Linux 系统免受实用程序滥用的最佳实践**

**使用 distroless 镜像**

通过观察上一节中讨论的技术，我们看到攻击者可以使用一组与完整操作系统捆绑在一起的工具。作为防御者，使用只包含我们需要的工具的容器映像并删除不需要的工具会更安全。

这种安全方法可以在很大程度上帮助降低风险，即使是针对诸如 Log4Shell 之类的关键漏洞也是如此。减少应用程序运行所需的工具数量也减少了由开源库和工具中的依赖漏洞引入的攻击面。这里介绍无发行映像的概念，这些映像被描述为仅包含应用程序及其运行时依赖项的映像，消除了你期望在典型 Linux 发行版中找到的程序，例如包管理器和 shell。

**Cloud One 工作负载安全——应用程序控制**

从防御者的角度来看，重点应该是通过纵深防御策略抵御。虽然对系统进行更改以尽量缓解甚至防止滥用会有所帮助，但利用多种安全措施的多层方法将提供最强的安全级别，理想情况下是将最佳实践与有效的防御技术结合起来。

对于非容器化环境，Cloud One 工作负载安全提供了应用程序控制模块，该模块监控软件更改并根据设置的配置允许或阻止它们。它创建现有应用程序的基线并将规则应用于下载和安装的新应用程序。它基于二进制文件的 SHA256 哈希值工作。

它为用户提供了执行以下操作的选项：

在明确允许之前阻止无法识别的软件；

在明确阻止之前允许无法识别的软件；

我们在 Ubuntu 20.04 长期支持 (LTS) 服务器上使用 wget 从 GitHub 下载 nmap 网络枚举工具的预编译二进制文件。然后，服务器配置了 Cloud One 工作负载安全代理，该代理运行应用程序控制模块，为无法识别的软件设置为“阻止”模式。如下图所示，应用程序控制阻止了执行。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708498574952.png "1662708498574952.png")

使用来自Cloud One Workload Security的Application Control模块防止“nmap”二进制文件的执行

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220909/1662708509193169.png "1662708509193169.png")

在Clou...