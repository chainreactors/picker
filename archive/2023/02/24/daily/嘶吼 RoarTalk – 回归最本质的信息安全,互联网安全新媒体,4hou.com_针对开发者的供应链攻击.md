---
title: 针对开发者的供应链攻击
url: https://www.4hou.com/posts/03Jy
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-24
fetch_date: 2025-10-04T07:56:25.369284
---

# 针对开发者的供应链攻击

针对开发者的供应链攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 针对开发者的供应链攻击

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-02-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)180522

收藏

导语：在本文中，我们将关注供应链的一个特定部分——开发者本身。要找到针对开发者的合适攻击模型，我们必须首先了解谁是开发者、他们的工作流程和日常工具。我们还将重点放在开发者和他们各自的工具如何被滥用来破坏供应链。

最近，趋势科技的研究人员分析了几种可被滥用来攻击供应链的攻击载体的概念证明，其中一种便是针对开发者的供应链攻击，该证明重点关注了本地集成开发环境（IDE），考虑当项目或生成被错误地“信任”时，通过注入命令执行恶意生成脚本的情况。

在本文中，我们将关注供应链的一个特定部分——开发者本身。要找到针对开发者的合适攻击模型，我们必须首先了解谁是开发者、他们的工作流程和日常工具。我们还将重点放在开发者和他们各自的工具如何被滥用来破坏供应链。

**谁是“开发者”?**

按照字面理解，将开发者定义为开发计算机软件的人。在安全研究人员的理解中，则是写代码的人。这包括流行的编程或脚本语言，如Java、JavaScript、TypeScript、Go、Python、C/ c++和许多其他语言，包括基础设施或容器部署定义，如Dockerfile、Kubernetes、Terraform HCL等。仅从这个描述来看，该定义就涵盖了IT行业的各个部分，包括编写代码的每个人、安全研究人员等等。

尽管工作流本身可能因开发者和公司的不同而有所不同，但根据开发者如何使用集成开发者环境(IDE)，它很可能属于以下类别之一：
1.本地IDE：开发者在自己的设备上本地安装了IDE。在这种情况下，开发者有两个选择：
1.1将代码拉入或推送到远程存储库，并在本地执行生成和调试；
1.2将更改提交到远程存储库，触发持续集成/持续交付（CI/CD）事件，并导致质量保证（QA）评估，甚至部署到生产环境中。
2.云IDE：开发者使用云服务托管的IDE，如AWS Cloud9、Visual Studio Online、GitHub代码空间和许多其他当今可用的平台。在这种情况下，开发者设备就像网关一样工作，通常通过浏览器访问IDE，主要的代码执行是在云服务提供者内部的云IDE的远程主机中执行的。

由于开发者涵盖多个职业，一些工作流可能会从列表中排除一些项目。例如，本文的概念证明很可能不会建立一个完整的CI/CD管道。然而，大多数工作流将包括使用IDE进行开发。在这篇文章中，我们将重点放在本地IDE上。

**本地IDE的示例**

当使用本地IDE时，其中一个示例是开发者将代码拉到本地计算机上。该代码被进一步编译为二进制格式，以便执行。对以前的贡献者编写的代码有一种隐含的信任，因为大多数开发者认为代码库可能不会被污染，因为它可以按预期工作。这种信任不仅存在于源代码本身中，还存在于生成脚本、库、依赖项和其他项目文件中。这就引出了第一个攻击场景：将恶意操作注入到项目文件或生成脚本中。

作为开发者，在执行远程代码之前，是否有必要在拉入远程代码之后阅读生成脚本？

研究人员通过向生成脚本或项目文件注入恶意生成命令(如果适用的话)来测试各种流行的IDE和编程语言。以下是测试的IDE版本的结果：

```
Eclipse 2022-09Apache NetBeans 16PyCharm 2022.2.4IntelliJ IDEA 2022.03Visual Studio 2022Visual Studio Code 1.73.1
```

当我们考虑通用攻击模型时，还必须包括每个非受控输入。这包括源代码及其文件，并包括生成前和生成后脚本和IDE扩展(如果适用的话)。我们之前在2020年的一篇文章中写过可能存在恶意IDE扩展的危险。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877319125318.png "1674877319125318.png")

IDE攻击模型

我们为每个IDE定义了以下场景，以验证可能的攻击模型：
开发者在线从不受信任的存储库中拉入代码；
开发者在IDE中打开一个项目；
开发者试图编译或生成项目；

**使用Visual Studio代码**

从Visual Studio Code 1.57版(2021年5月发布)开始，代码编辑器引入了Workspace Trust的概念。此功能通过防止代码从不受信任的文件和存储库执行，帮助开发者安全地浏览和编辑代码，而不考虑源代码或作者。这可能是由于当时第三方扩展漏洞的数量不断增加，当被滥用时，在打开不受信任的文件时，可能会允许远程代码执行（RCE）。这个概念很简单：除非工作区是可信的，否则它不允许任何（生成/调试）任务或某些扩展功能运行。这就可以将责任转移到开发者身上，并提示他们是否要信任下载的代码。

这里要强调的是，不要盲目地信任每一个工作区。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877338101832.png "1674877338101832.png")

Visual Studio代码工作区信任对话框

开发者应该寻找和考虑哪些代码不应该被信任的可疑迹象？在其他示例中，应该引起开发者警惕的迹象包括：

较低的下载量；

论坛上共享的项目；

灰色区域；

一般未经证实的来源；

未知的人；

在执行IDE任务之前，应通过审计项目目录中的文件以查找可疑或恶意命令来验证.vscode/tasks.json文件，尤其是从未知源下载时。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877354196735.png "1674877354196735.png")

恶意生成任务的示例

恶意命令可以隐藏在tasks.json文件下并伪装成生成命令。当开发者试图生成之前盲目信任的项目时，开发者设备将执行远程代码，这可能是恶意的。攻击者还可以通过在常规生成命令之间隐藏恶意命令，使有效负载更为隐蔽，这将减少开发者的怀疑。

在模拟中，我们通过Pastebin在远程服务器上放置了一个脚本。这是一种被一些攻击者滥用的方法，将其恶意有效载荷发送到受感染的设备中。这项技术对攻击者的好处是可以远程更改有效载荷。例如，在成功感染后，可以将有效负载更改为无害的内容。

**使用Visual Studio**

Visual Studio是Microsoft用于.NET和C++开发的专有IDE，它没有工作区信任功能。因此，开发者在加载不受信任的项目文件和执行生成时应该格外小心。恶意的生成前或生成后任务可能会被注入到文件中，从而导致从生成开始就执行不必要的执行。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877371266501.png "1674877371266501.png")

Visual Studio项目文件预生成任务命令示例

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877387157575.png "1674877387157575.png")

嵌入预生成PowerShell执行的概念验证示例

**使用其他IDE**

在Eclipse IDE中，仍然可以注入生成命令。因此，文件是不同的。首先，ExternalToolBuilder的生成命令必须在.project文件中指定，参考在. externaltoolbuilders文件夹中定义实际执行命令的另一个文件。通过将多个生成命令链接在一起，我们可以实现与Visual Studio Code中相同的多个命令执行。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877403830944.png "1674877403830944.png")

.project文件节链接生成执行规范的示例

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877420153755.png "1674877420153755.png")

生成事件外部命令规范

由于使用外部生成工具的项目文件注入适用于基本IDE的范围，因此它仅适用于实际代码编译为二进制文件的语言。这包括Java和C/ c++，但不包括像PHP这样的语言，因为不执行生成。

NetBeans IDE主要用于Java开发，尽管它还通过第三方扩展支持PHP、HTML5、JavaScript或C/C++开发。Java开发项目可以利用Maven、Gradle或Ant作为其依赖关系管理和生成自动化工具。因此，项目和生成定义可能不同。然而，所有这些工具都支持将第三方流程作为生成前或生成后操作来执行。在这种情况下，攻击者可以注入恶意代码，并希望开发者不会注意到并不情愿地执行。

对于Ant，注入可以在nbproject/build-impl.xml文件中完成，方法是将以下代码片段添加到一个合适的目标标记中：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877436865442.png "1674877436865442.png")

Ant的注入点和触发生成时的命令执行示例

当开发者使用Maven作为生成工具时，可以通过更改项目文件夹中的pom.xml来实现相同的目标。这一次，在生成标记中使用了org.codehaus.mojo插件。所使用的语法类似于Ant所使用的语法。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877450141726.png "1674877450141726.png")

Maven第三方执行示例

对于Gradle，Groovy语言脚本用于位于app/build.gradle内部的生成定义，并且对所选任务内的字符串调用execute()函数将触发代码执行。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877465106134.png "1674877465106134.png")

Gradle第三方执行示例

尽管“打开项目”对话框有一个“信任项目生成脚本”选项，但其功能仅对Gradle项目有效。如果未选中，它将阻止Gradle脚本启动，因此，当加载项目作为CVE-2020-11986修复时，代码执行是可能的。尽管如此，当用户决定手动执行生成时，不会显示进一步的对话框，并且生成被认为是可信的。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877480875090.png "1674877480875090.png")

NetBeans中的“信任项目生成脚本”复选框

IntelliJ IDEA是另一个用于Java、Kotlin、Groovy和其他基于Java虚拟机(JVM)的语言开发的IDE。它还支持Ant生成脚本。加载包含Ant生成脚本的项目会触发一个对话框警告，提示它可能会执行潜在的恶意代码，如果它不是来自可信的源，建议使用安全模式。当开发者试图在安全模式下执行生成时，IDE会警告用户该操作只能在可信模式下完成。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877497343137.png "1674877497343137.png")

IntelliJ IDEA显示潜在恶意生成脚本的警告

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877520198240.png "1674877520198240.png")

IntelliJ IDEA生成安全模式生成警告

PyCharm是用于Python开发的IDE。Python脚本通常不会在执行之前编译。然而，开发者仍然可以指定自定义运行/调试配置，允许在实际脚本执行之前执行第三方二进制文件。这可能用于脚本数据输入准备。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877537645186.png "1674877537645186.png")

运行执行前的外部工具

该操作在项目内部被参考。但是，实际的可执行规范存储在不同的位置，更具体地说，存储在 ~/.config/JetBrains/PyCharmXXXX/tools/External Tools.xml。正如我们所看到的，该文件存储在用户主目录中，保护它不受攻击模型场景的影响，因为它需要修改本地文件系统。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877551423662.png "1674877551423662.png")

运行前任务参考

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230128/1674877568170426.png "1674877568170426.png")

运行前任务定义

**总结**

研究人员使用执行恶意生成脚本的攻击场景评估了所有已识别的IDE，向这些生成脚本中注入恶意命令是可能的。如上所述，一些IDE明确警告开发者恶意操作的可能性，除非项目配置将其标记为明确可信，否则不允许执行任务。另一方面，一些IDE使用这样的假设，即当开发者打开一个项目或将其复制到他的工作区时，它会自动被信任，并且不需要任何进一步的操作。

无论我们使用什么IDE，总会权衡安全性和可用性。开发者不应该盲目地相信互联网上的每一个开源项目。在执行任何生成操作之前，开发者至少应该知道他们有可能成为目标并审查生成脚本。

我们还想强调，上述攻击场景不仅限于本地IDE，而且安全重要性在于所使用的工作流和工作区信任本身，无论开发者在容器或支持在线IDE的VM中执行实际生成/编译的情况如何。一旦工作区被标记为可信，并且生成脚本被修改，它可能会在环境中触发不需要的代码执行，并导致IDE具有访问权限。以下是开发者可以记住的一些最佳安全实践：

使用安全配置的CI/CD平台，在具有适当的基于角色的访问控制（RBAC）的外部设备或服务上执行生成，只有授权人员才能更改生成脚本；

在集成到项目之前，检查外部源代码和生成脚本；

避免在审计之前盲目使用开箱即用的解决方...