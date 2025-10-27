---
title: DVGA 演练
url: https://www.anquanke.com/post/id/289548
source: 安全客-有思想的安全新媒体
date: 2023-07-06
fetch_date: 2025-10-04T11:52:46.405374
---

# DVGA 演练

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# DVGA 演练

阅读量**958334**

发布时间 : 2023-07-05 10:14:51

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

这篇文章将为您提供每个方法的更详细的解释以及我使用的方法的概述。老实说，这更多的是为了我自己跟踪我在DVGA上所做的事情以供将来参考，但欢迎您继续阅读。😉

#### **安装 DVGA**

要托管您的 DVGA 实例，您需要一个安装了 Docker 的 Linux 系统。与所有故意易受攻击的练习应用程序一样，请确保不要将其安装在面向互联网的服务器、VPS 或虚拟机上。

我通常将目标应用安装在与攻击者系统分开的 VM 上。

如果你想做同样的事情，首先在你最喜欢的虚拟机管理程序软件（我使用VirtualBox）上创建一个新的VM，然后安装一个Ubuntu系统。这将是您的目标系统。

现在安装 Docker（请参阅此处的说明）。

要检查 Docker 引擎是否已正确安装，请通过键入以下内容来运行 hello world 映像：

sudo docker run hello-world

现在安装并运行 DVGA：

sudo docker pull dolevf/dvga

sudo docker run -t -p 5013:5013 -e WEB\_HOST=0.0.0.0 dolevf/dvga

确保您的终端显示以下内容（服务器版本可能不同）：

DVGA Server Version: 2.1.2 Running…

DVGA 应用程序可从以下浏览器本地访问：

http://localhost:5013

可从其他 VM（包括最重要的攻击者 VM）访问该应用：

（这是假设目标 VM 在网络上的地址为 ，因此请相应地进行调整）。

http://192.168.1.26:5013http://192.168.1.26

#### **安装黑客工具**

您还需要在攻击者系统上安装一些工具。

1. Altair
2. graphql-introspection nmap script
3. graphw00f
4. InQL
5. Sqlmap（通常已经随Kali一起安装）
6. 您还需要打嗝套件和邮递员。

#### **检测和指纹识别 GraphQL**

第一步是确定应用是否提供 GraphQL API。

您的第一个赌注是尝试通过将攻击者机器的浏览器指向来访问最常见的 GraphQL 端点：

http://192.168.1.26:5013/graphql

果然，这向我们表明这确实是一个 GraphQL 端点。

但让我们想象一下，事实并非如此。我们需要使用**graphw00f**扫描尝试可能的目标端点列表，同时对 GraphQL 实现进行指纹识别：

![]()

这确认了目标端点，也表明 GraphQL 引擎是**Graphene**，所以我们面对的是用**Python**编写的 GraphQL 实现。

让我们检查攻击面矩阵https://github.com/nicholasaleks/graphql-threat-matrix/blob/master/implementations/graphene.md

这为我们提供了以下信息：

![]()

让我们把它放在手边，以备后用。

现在让我们检查一下是否启用了内省：

![]()

因此，该应用程序确实可以进行内省。这是个好消息。

现在，让我们使用此处提供的内省查询获取架构：

https://github.com/dolevf/Black-Hat-GraphQL/blob/master/queries/introspection\_query.txt

复制查询并在 Altair 中运行它。

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA03.png)

这会导致相当长的响应。与其手动查看，不如让我们使用**GraphQL Voyager**获得图形表示。

转到https://ivangoncharov.github.io/graphql-voyager然后单击（左上角），然后单击选项卡，粘贴我们从 Altair 收到的响应，然后单击 。这让我们很好地了解了架构的工作原理。

CHANGE SCHEMAINTROSPECTIONDISPLAY

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA04.png)

#### **DoS：批量查询攻击**

好吧，让我们继续进攻。DVGA 解决方案页面列出了一系列要运行的 DoS 攻击。

问题语句告诉我们查询是资源密集型的，可用于批量查询攻击。`systemUpdate`

这可以通过将发送到 GraphQL 端点的数组中的一系列命令分组来完成。但是，**Altair**、GraphQL Playground 和**GraphiQL Explorer 等 GraphQL IDE**不支持基于数组的查询。这意味着我们需要从命令行工作。

此外，我们之前检查的**石墨烯**攻击面矩阵提到批处理请求默认处于禁用状态。因此，我们需要首先检查DVGA是否真的如此：

![]()

这表明已启用批处理查询。这对我们来说又是一个好消息。

现在让我们使用资源密集型查询尝试相同的命令，而不是我们可以在数组中运行十次：

systemUpdate

![]()

这会使应用无响应。所以我们的DoS攻击是成功的。

可以使用 停止该命令，但还需要在目标 VM 上重新启动 DVGA（除非要等到十个命令完成，这可能需要一段时间）。

curlCtrl-CsystemUpdate

#### **DoS：深度递归查询攻击**

这一次，我们希望通过构建一个循环查询来利用递归，该查询使用两个相互交叉引用的对象类型。让我们首先检查一下我们在 GraphQL Voyager 中拥有的模式的可视化表示。

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA04.png)

在这里，我们可以看到 和 对象类型相互交叉引用，所以让我们使用它。

PasteObjectOwnerObject

作为旁注，我们还可以使用 InQL 自动检测架构中的循环关系：

![]()

现在让我们检查结果：

![]()

这证实了我们在 GraphQL Voyager 中发现的内容。

让我们使用 and 字段构建一个深度递归查询：

pastesowner

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA4_5.png)

此查询的深度为 30 行。它返回 1400 行响应。但是，这还不足以使应用程序崩溃。

我们可以使用一个类似的查询，它有 2003 行长，你可以在这里下载：

https://github.com/dolevf/Black-Hat-GraphQL/blob/master/ch05/unsafe-circular-query.graphql

在 Altair 中运行它，您将看到它使应用程序无响应：

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA-05bis.png)

所以我们有一个成功的攻击。

您可以再次重新启动 DVGA 实例。

#### **DoS：资源密集型查询攻击**

这不是我们需要完成的任务，而是提醒我们一些 GraphQL 服务器实现了查询成本分析。此系统根据 GraphQL 服务器需要处理的资源量为架构中的字段分配值。

这允许服务器设置一个阈值来确定它将接受哪些查询以及它将拒绝哪些查询，以保持合理的 GraphQL 服务器工作负载。

这意味着如果这样的系统到位，DoS攻击可能不那么容易进行。

另外提醒一下，我们之前检查的攻击面矩阵表明，Graphene不支持开箱即用的查询成本分析。这意味着想要设置成本分析器的开发人员将需要自定义其设置。

在现实生活中，您可能会遇到忽略这一点的 GraphQL 服务器。

#### **DoS：字段重复攻击**

尝试针对 GraphQL 服务器的 DoS 攻击的一种简单方法是简单地复制查询中的字段：

![]()

但是，除非选择资源密集型查询，否则需要多次复制所选字段才能产生任何效果。

一个更快的选择是使用 Python 漏洞来自动执行大规模字段重复攻击。您可以在此处下载漏洞利用：

https://github.com/dolevf/Black-Hat-GraphQL/blob/master/ch05/exploit\_threaded\_field\_dup.py

现在针对目标 DVGA 应用程序运行漏洞：

python3 exploit\_threaded\_field\_dup.py http://192.168.1.26:5013/graphql

这会使应用无响应。你可以插入脚本以恢复你的外壳。您还需要在目标 VM 上重新启动 DVGA。`CTRL-C`

请注意，如果 GraphQL 服务器实现了查询成本分析，如上所述，这种攻击将不那么容易执行。此外，某些服务器可能会实现字段重复数据消除中间件，该中间件将从查询中清除重复的字段。

#### **DoS：基于别名的攻击**

GraphQL 不喜欢处理相同的响应键，如果一个查询包含两次给定的字段名称，并且您为每个查询传递具有不同值的参数，通常会抱怨。

这就是为什么使用别名将允许 GraphQL 服务器返回响应，而无需为两个字段处理相同的响应键。

不确定这意味着什么？没关系。。。目前，只需尝试使用别名发送包含多个字段实例的查询：`systemUpdate`

![]()

这使得应用程序没有时间。所以我们的DoS攻击是成功的。

为了清楚起见，让我们提一下上面的示例类似于DVGA解决方案页面上给出的解决方案。但是，由于不会产生相同的响应键冲突，因此以下内容也将起作用：

systemUpdate

![]()

不同之处在于，使用别名有时会更有效，尤其是在实施了现场重复数据消除中间件的情况下。请注意，GraphQL 服务器上需要一个特定的查询中间件来检测别名的使用。

综上所述，我最喜欢的执行基于别名的攻击的方法是使用 python 单行代码来生成攻击：

python3 -c ‘for i in range(0, 1000): print(“q”+str(i)+”:”+”systemUpdate”)’

这将生成一个包含 1000 个别名的列表：

q0:systemUpdate

q1:systemUpdate

q2:systemUpdate

q3:systemUpdate

q4:systemUpdate

q5:systemUpdate

q6:systemUpdate

q7:systemUpdate

q8:systemUpdate

q9:systemUpdate

…

将列表粘贴到 Altair 中的查询中，您的 DVGA 实例就像死了一样，可以重新启动了。

#### **DoS：圆形片段**

让我们通过使用两个相互交叉引用的片段来引发无限循环。

在这里，我们在名为 和 的对象样式上创建两个片段，它们相互调用：

PasteObjectStartEnd

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA06.png)

这会立即使 DVGA 崩溃，并在查询响应中报告错误。

现在，尽管我喜欢这种攻击的有效性，但要知道 GraphQL 规范表明不应允许片段形成任何循环。因此，在使用正确设计的 GraphQL 引擎的真实目标上，这种攻击应该不起作用。

无论如何，请记住这一点，并在测试真实目标时尝试一下。你永远不知道，你可能会很幸运。

####

#### **信息披露：GraphQL 内省**

内省查询是探索架构和寻找敏感数据的一些无意泄露的好方法，我们可以利用这些数据来发挥自己的优势。

“解决方案”页中为此任务提供的解决方案是一个非常基本的内省查询，不提供太多信息：

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA07_1.png)

下面是一个稍微详细的版本，其中列出了架构中所有可用查询、突变和订阅的名称：

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA07_2.png)

但是，通过使用我们在侦察阶段生成的 GraphQL Voyager 表示，您将获得更好的视图。界面底部的菜单可让您在查询、变更和订阅之间切换，还允许您专注于特定的对象类型：

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA07_3.png)

现在，熟悉模式和了解可用不同字段的最有效方法是使用 Postman 的 GraphQL 客户端（您需要 Postman v.10.10 或更高版本）。

在 Postman 中，选择“新建”，然后选择**“**GraphQL 请求”以访问**GraphQL**客户端。

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA07_8.png)

架构资源管理器（位于左侧）列出了每种操作类型（查询、更改或订阅）的所有可用字段，并指示可用或必需的参数及其标量类型的相应值。您需要做的就是单击您的方式，Postman 会为您构建查询。

####

#### **信息披露：GraphQL 接口**

解决方案页面告诉我们DVGA提供了一个GraphiQL IDE。因此，让我们尝试找到它（默认的 GraphiQL 端点是 ，但假设 IDE 可能使用非常规端点）。

/graphiql

让我们首先创建一个可能的 GraphQL 端点列表。然后让我们用这个单词列表来模糊 URL：

![]()

我们得到两次点击：一次用于我们已经知道的端点（），一次用于 IDE （）。

/graphql/graphiql

让我们检查一下我们的新端点：

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA07_5.png)

果然，我们找到了IDE。

####

#### **信息披露：GraphQL 字段建议**

GraphQL 支持字段建议。这意味着您可以发送具有故意不正确或不完整的字段名称的查询，并获得包含具有相似名称的有效字段建议的响应。有趣的是，无论是否启用内省，这都有效。因此，现场建议有助于阐明不可用的架构。

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA07_6.png)

我们还会在键入查询时获取字段信息：

![]()

#### **信息泄露：服务器端请求伪造 （SSRF）**

让我们寻找一些带有参数的操作，这些操作可以让我们传递一个 URL。在DVGA主页上，单击导入**粘贴**。“**导入粘贴”**页面有一个接受 URL 的字段。甚至还有一个建议的**Pastebin**页面的 URL。

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA08_1.png)

键入此 URL 并在**Burp Suite**中截获请求。

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA08_2.png)

您可以看到此请求使用了突变，它接受四个参数：、、 和 。这些参数的值构成了用于从**Pastebin**获取粘贴的 URL。

ImportPastehostportpathscheme

导入的粘贴的正文将显示在字段中的响应中。您还可以查看DVGA上的**“专用**粘贴”页面，以查看粘贴确实已导入。

result

我们可以使用它来访问 DVGA 本地网络上的其他 URL。

让我们切换回Postman的GraphQL客户端，看看我们可以用这个突变做什么。

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA08_3.png)

在这里，我们尝试从此 URL 导入粘贴：。

http://localhost:8080/paste.txt

这将返回一个空结果（端口 8080 实际上未在 DVGA 上打开）。但无论如何，我们确实得到了回应。

现在，我们可以尝试在开放端口上探测确实存在的服务。为此，我们需要通过在目标系统的终端中运行以下 Docker 命令，在 DVGA 容器中打开一个**netcat**侦听器来模拟这样的服务：

sudo docker exec -it dvga nc -lvp 7773

listening on [::]:7773 …

接下来，返回到攻击者计算机并从 Postman 发送以下突变：

[![]()](https://zerodayhacker.com/wp-content/uploads/2023/02/DVGA08_4.png)

这一次，请求挂起，我们看不到响应。

切换回目标系统，您应该在终端中看到以下内容：

connect to [::ffff:127.0.0.1]:7773 from localhost:56738 ([::ffff:127.0.0.1]:56738)

GET ...