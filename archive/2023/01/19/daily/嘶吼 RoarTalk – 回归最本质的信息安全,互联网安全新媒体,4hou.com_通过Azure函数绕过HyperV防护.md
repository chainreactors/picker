---
title: 通过Azure函数绕过HyperV防护
url: https://www.4hou.com/posts/LBqD
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-19
fetch_date: 2025-10-04T04:14:57.999127
---

# 通过Azure函数绕过HyperV防护

通过Azure函数绕过HyperV防护 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 通过Azure函数绕过HyperV防护

luochicun
[技术](https://www.4hou.com/category/technology)
2023-01-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)177326

收藏

导语：Unit 42研究人员调查了Azure的无服务器架构，发现他们能够破坏底层主机的无服务器函数。

Unit 42研究人员调查了Azure的无服务器架构，发现他们能够破坏底层主机的无服务器函数。研究人员还发现，他们的主机实际上是一个HyperV虚拟机，它托管了其他几个无服务器函数。Hyper-V是微软的一款虚拟化产品，是微软第一个采用类似Vmware ESXi和Citrix Xen的基于hypervisor的技术。

Azure serverless functions（通常称为Azure Functions）是一种无服务器解决方案，可以使用户减少代码编写、减少需要维护的基础结构并节省成本。无需担心部署和维护服务器，云基础结构提供保持应用程序运行所需的所有最新资源。你可以专注于使用你认为最高效的语言编写最重要的代码，而 Azure Functions 处理其余代码。作为一个基于触发器的服务，它运行代码以响应各种事件。在本文中，这个事件是一个网页请求。

研究人员发现，对于每个函数，主机都会生成一个新的容器。每个容器将在几分钟后终止并删除，以将无服务器函数与传统的容器即服务区分开来。

问题主机只托管研究的Azure用户有权访问的函数，因此不会造成真正的攻击。很明显，微软竭尽全力阻止人们访问主机，因此可能还有其他问题尚未被发现。虚拟机上可能有不应该显示的重要信息，这些信息可能会被动机充分的攻击者发现。

微软经常使用容器来加强安全性，但由于容器本质上不如虚拟机那样安全，因此通常不会将其视为安全边界。在本文的示例中，他们实现了额外的安全层，这被证明是有效的。

Prisma的无服务器解决方案为大多数云提供商提供了函数发现和漏洞扫描功能。这些功能会作用于无服务器函数上，并在发现这些函数中存在已知漏洞时提醒你。

**什么是无服务器函数**

无服务器函数是无服务器计算（通常简称为“无服务器”）的一个特点，云提供商按需为其客户提供所有计算资源，并管理所有架构，包括云基础设施。

无服务器理想应用程序的一个很好的例子是聊天机器人。例如，Slack使用名为marbot的无服务器应用程序通过Slack向DevOps团队发送通知。

“serverless”这个名字有点误导人。不管它的名字意味着什么，无服务器计算仍然需要物理服务器来执行代码。与传统计算的主要区别在于，无服务器抽象了与代码本身无关的任何东西，从代码运行的操作系统到实际运行代码的设备硬件。

**无服务器函数的内部结构**

你可能会问自己的第一个问题是如何开始研究无服务器平台。任何使用过Azure Serverless Functions的人都知道，可研究的地方不是很多。你可以上传一些代码或更改一些设置，如下图所示，但仅此而已。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543412149303.png "1671543412149303.png")

通过Azure函数提供的所有不同运行时

研究人员决定从一个HTTP请求触发的Linux上的Python函数开始研究，对于某些运行时，Windows也可用。

下一步是在函数中获得一个有效的交互式shell，以更好地理解研究人员正在处理的内容，并获得有关运行代码的设备的一些信息。为了便于使用，研究人员决定使用逆向shell。研究人员还决定使用数据传输工具socat而不是netcat，因为它支持更广泛的协议。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543426170257.png "1671543426170257.png")

研究人员使用的socat二进制文件

研究人员只是将socat二进制文件放在Visual Studio代码中的项目目录中，并将整个文件部署到研究人员之前创建的无服务器函数中。实际启动逆向shell的代码非常简单，因为整个逻辑都在socat应用程序中，如下图所示。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543442424866.png "1671543442424866.png")

连接到逆向shell侦听器的简单函数代码

执行逆向shell后，研究人员进入了一个名为app的用户下的函数目录。研究人员使用

cat/proc/1/cgroup\_last\_cap命令，以SandboxHost开头的设备主机名也暗示了这一点。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543457380494.png "1671543457380494.png")

无服务器函数内部的shell

在研究人员登录的工作目录中没有太有趣的东西。这个目录包括他们上传的所有文件，外加一个额外的lib文件夹，其中包含Python与Azure通信所需的库。

**容器**

这项研究一开始并没有明确的目标，只是为了改善Prisma的无服务器保护。然而，在了解了更多关于架构的知识后，研究人员渴望探索一下容器。

在熟悉了容器及其文件以及用户权限等之后，研究人员决定检查环境变量，因为它们通常包含一些有趣的信息。这一次没有什么不同。在其他有趣的事情中，研究人员注意到环境变量泄露了映像名称。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543474197438.png "1671543474197438.png")

环境变量中的映像名称

在网上搜索这个映像名称，研究人员找到了一个显示映像名称的微软官方目录，该目录指向一个提供所有Microsoft映像(包括我们正在查看的映像)的官方存储库。

研究人员的第一个方法是获取映像“源代码”（如果你使用Docker，则为Dockerfile）。经过一番搜索，研究人员发现有一个叫做Whaler的实用工具，它可以将Docker映像逆向工程到创建它们的Dockerfile中。该过程如下所示。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543491195283.png "1671543491195283.png")

使用Whaler对微软映像进行逆向工程

Whaler有大量的映像，从而产生一个易于使用的单行命令。使用这个方法，研究人员成功地生成了一个足够好的Dockerfile版本，如下图所示。文件中最有趣的部分是最后一行。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543507588046.png "1671543507588046.png")

逆向之后的Dockerfile版本

网格文件夹似乎包含一些有趣的文件，特别是launch.sh脚本，它似乎是容器内执行的第一件事。此时，研究人员只需从映像内部复制整个网格文件夹，以进一步研究它。

还有一些脚本在不同的场景中调用了一些其他脚本，该文件夹中有趣的部分是一个名为init的二进制文件，它在每个Azure无服务器容器的后台运行。对研究人员来说幸运的是，这个二进制文件也包含了符号，所以逆向工程很容易。

在研究了函数和字符串列表之后，有一个函数特别有趣：init\_server\_pkg\_mount\_BindMount。在对其进行逆向工程之后，研究人员发现该函数将容器内的一条路径绑定到另一条路径，该路径也位于容器内。此函数也不要求用户具有特权，但它在root上下文中运行！要将一个文件绑定到任何其他文件，你所需要做的就是在容器中使用正确的参数在正确的端口上执行HTTP查询。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543524230074.png "1671543524230074.png")

init\_server\_pkg\_mount\_BindMount函数签名

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543542206564.png "1671543542206564.png")

init\_server\_pkg\_mount\_BindMount函数解析来自HTTP请求的sourcePath和targetPath

在这部分调查的过程中，研究人员还发现了许多关于Azure无服务器架构如何在幕后工作的信息。虽然这超出了本文的范围，但可以在本文中深入探讨这一问题。

**升级权限**

简而言之，虽然在一个没有特权的用户的容器中研究，但研究人员能够将任何一个文件作为根文件绑定到任何其他文件。此时，研究人员的目标是在容器内将特权升级到根权限。可能有几种方法可以实现这一点，但研究人员选择用生成的文件替换/etc/shadow文件，然后将用户更改为root。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543559114005.png "1671543559114005.png")

使用OpenSSL生成/etc/shadow

为了实现这一点，研究人员执行了以下步骤：

为root用户生成一个密码已知的/etc/shadow文件；

将该文件上传到Function容器的本地目录；

使用正在运行的init服务和BindMount函数通过查询http://localhost:6060将本地阴影文件绑定到实际的/etc/shadow文件；

使用su-root命令将用户更改为root。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543575168667.png "1671543575168667.png")

不断升级权限

**利用root权限规避容器**

可以利用新获得的根访问来规避容器，通过研究，研究人员选择了菲利克斯·威廉姆（Felix Wilhelm）多年前发现的一个旧漏洞。

不过要使用此漏洞也不是一件简单的事情，要使其正常工作，需要满足以下几个要求：

研究人员必须在容器内以root身份运行；

容器需要具有SYS\_ADMIN函数；

容器要么没有AppArmor配置文件，要么允许挂载系统调用；

cgroup v1虚拟文件系统必须在容器内以读写方式安装；

研究人员已经在早些时候实现了第一个需求。令人惊讶的是，其余的需求在我们的容器中也可用。这是令人惊讶的，因为在默认情况下，容器启动时具有一组受限的函数，并且没有启用SYS\_ADMIN函数。此外，Docker通常在默认情况下使用AppArmor策略启动容器，这防止了在容器使用SYS\_ADMIN运行时使用mount sycall。通过在/proc/PID/status下的shell状态文件上运行capsh命令，研究人员确认了所有必要的函数，如下图所示。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221220/1671543654290100.png "1671543654290100.png")

使用capsh和一些sed脚本来打印特权用户函数

关于此漏洞的详细解释已超出了本文范围，我们建议阅读 "Digging into cgroups Escape" 以更好地理解此技术。简而言之，研究人员将通过以下步骤描述该漏洞：

查找或创建对cgroup控制器的访问权限（大多数版本的漏洞利用使用RDMA）；

在该控制器中创建一个新的cgroup；

将该cgroup的notify\_on\_release设置为1；

将发布代理设置为容器和主机都可以访问的文件；

在该cgroup中启动一个快速完成流程，该流程将在终止时触发发布代理的执行。

研究人员决定通过运行ps aux并将其与容器的ps aux进行比较来演示实现主机执行上下文。在本节开头的视频中，你可以看到漏洞的整个利用过程。需要注意的是，托管容器的设备是HyperV虚拟机，而不是物理服务器。

**总结**

不管怎样，Azure的用户都可以访问虚拟机托管的所有资源，因此，这种防御没有什么意义。这是云提供商缓解措施按预期工作的一个示例。在本文的示例中，他们选择不依赖容器作为安全边界，并实现另一种保护，这被证明是一个聪明的举动。

但是，如果在虚拟机本身中发现另一个漏洞，这个漏洞可能会产生巨大的影响。此外，微软在过去已经修复了类似的问题，即使他们本身没有将其称为漏洞。

虚拟机可能包含对无服务器函数用户或可能的攻击者不可见的重要信息或秘密。在与微软分享该调查结果后，他们考虑了以下防御措施，以更好地保护客户：

对绑定装载API进行额外验证，以防止装载过度；

尽可能从二进制文件中删除符号。

本文翻译自：https://unit42.paloaltonetworks.com/azure-serverless-functions-security/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?EWtKE7uu)

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

  攻防速写｜一条微信消息，实现客户端持...