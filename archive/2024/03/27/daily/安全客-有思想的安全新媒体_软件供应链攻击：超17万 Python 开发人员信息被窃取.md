---
title: 软件供应链攻击：超17万 Python 开发人员信息被窃取
url: https://www.anquanke.com/post/id/294329
source: 安全客-有思想的安全新媒体
date: 2024-03-27
fetch_date: 2025-10-04T12:07:57.860557
---

# 软件供应链攻击：超17万 Python 开发人员信息被窃取

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

# 软件供应链攻击：超17万 Python 开发人员信息被窃取

阅读量**97691**

发布时间 : 2024-03-26 10:29:10

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://checkmarx.com/blog/over-170k-users-affected-by-attack-using-fake-python-infrastructure/>

译文仅供参考，具体内容表达以及含义原文为准。

Checkmarx 研究团队最近发现了一场针对软件供应链的攻击活动，有证据表明成功利用了多个受害者。其中包括 Top.gg GitHub 组织 （拥有超过 17 万用户的社区）和一些个人开发人员。威胁行为者在这次攻击中使用了多个 TTP，包括通过窃取的浏览器 cookie 接管帐户、通过经过验证的提交贡献恶意代码、设置自定义 Python 镜像以及将恶意包发布到 PyPi 注册表。本博客将介绍攻击和攻击者使用的技术。

关键点

* 攻击者组合多个 TTP 发起静默软件供应链攻击，窃取受害者的敏感信息。
* 威胁行为者创建了多个带有点击诱饵描述的恶意开源工具来欺骗受害者，这些工具很可能来自搜索引擎。
* 攻击者分发了托管在虚假 Python 基础设施上的恶意依赖项，将其链接到 GitHub 上的流行项目和合法的 Python 包。 GitHub 帐户被接管，恶意 Python 包被发布，并且威胁行为者还使用了社会工程方案。
* 多阶段、规避性的恶意负载从受感染的系统中收集密码、凭据和更多有价值的数据转储，并将它们渗透到攻击者的基础设施中。
* 在这次攻击中，攻击者部署了一个伪造的 Python 包镜像，该镜像成功地用于部署流行包“colorama”的中毒副本。
* 受害者中还有一名 top.gg 贡献者，他的top.gg社区（17万+成员）的代码存储库受到了攻击的影响。

我刚刚被黑了

*“我今天使用我的笔记本电脑，只是在命令行上经常摆弄 python 和其他东西，直到我在命令行上看到一条奇怪的消息，说 python 上的 colorama 有问题，我并没有太在意，因为我已经习惯了这些东西，所以我跳过了它，几分钟后，我收到了相同的错误消息，但在我使用的不同脚本中。 当我看到这个的时候，我就知道发生了什么事，我被黑了。”*

这个令人毛骨悚然的帐户来自 安全研究人员Mohamed Dief 最近的一篇博客文章，他在克隆存储库“maleduque/Valorant-Checker”时成为复杂恶意软件攻击的受害者。

穆罕默德的故事只是这一恶意软件活动产生深远影响的一个例子。该活动背后的攻击者采用了一种狡猾的策略，通过恶意 GitHub 存储库传播恶意软件。

假蟒蛇镜子

攻击基础设施包括一个看似 Python 包镜像的网站，并在“files[.]pypihosted[.]org”域下注册。

此域选择是官方 Python 镜像“files.pythonhosted.org”的巧妙 Typosquat  ，因为后者是 PyPi 包的官方工件文件通常存储的位置。

![]()

在攻击者的足迹中，我们看到他们利用了 pip（Python 的包管理器）中的一项功能，您可以在其中指定 URL 来获取包依赖项并使用他们的假 Python 镜像来下载包。

![]()*Requirement.txt 文件，假镜像 URL 与合法 URL*

接待有毒的“colorama”

威胁行为者获取了 Colorama  （一种非常流行的工具，每月下载量超过 1.5 亿次），对其进行复制并插入恶意代码。然后，他们使用空格填充将有害的有效负载隐藏在 Colorama 中，并将这个修改后的版本托管在他们的误植域名假镜像上。这种策略使得用肉眼识别该包的有害性质变得更加困难，因为它最初似乎是合法的依赖项。

GitHub 帐户接管

攻击者的影响范围超出了通过自己的帐户创建恶意存储库的范围。他们成功劫持了具有较高声誉的 GitHub 帐户，并利用这些帐户下的资源进行恶意提交。

其中一名受害者是 GitHub 帐户 editor-syntax  ，他也是 Top.gg  GitHub 组织的维护者，拥有 Top.gg git 存储库的写入权限。

通过控制这个受信任的帐户，攻击者 使用窃取的editor-syntax 的 GitHub 身份  对 top-gg/python-sdk存储库进行了恶意提交。他们在requirements.txt中添加了从假Python镜像下载中毒版本colorama的指令。

他们还使用该帐户对多个恶意 GitHub 存储库加注星标，以提高其可见性和可信度。

通过被盗 Cookie 接管帐户

“editor-syntax”的 GitHub 帐户很可能是通过被盗的 cookie 被劫持的。攻击者获得了对帐户会话 cookie 的访问权限，从而允许他们绕过身份验证并使用 GitHub UI 执行恶意活动。这种帐户接管方法尤其令人担忧，因为它不需要攻击者知道帐户的密码。

![]()

Top.gg 社区（拥有超过 17 万成员）也是此次攻击的受害者。

![]()

2024 年3 月 3日，用户在社区的 Discord 聊天中向 “editor-syntax”发出了 关于源自其帐户的恶意活动的警报。  至少可以说，“editor-syntax”非常震惊，因为他通过 GitHub 帐户意识到发生了什么事。很明显，该恶意软件已经危害了多人，凸显了攻击的规模和影响。

![]()

有趣的是，攻击者的域名抢注技术是如此令人信服，甚至 GitHub 上的用户也成为了受害者，而没有意识到自己受到了攻击。当恶意域名“piphosted[.]org”宕机时，用户在其中一个恶意存储库上提出了一个问题，对此进行了抱怨，但没有意识到它是恶意负载的主机。

![]()

大海捞针

为了进一步隐藏他们的恶意意图，攻击者在对许多恶意存储库进行更改时采用了一种策略方法。他们会同时提交多个文件，包括包含恶意链接的要求文件以及其他合法文件。这一经过深思熟虑的举措旨在最大限度地减少检测的机会，因为恶意链接会与合法的依赖项混合在一起，从而降低用户在粗略审查已提交的更改时发现异常的可能性。

![]()*攻击者在多个文件的提交中隐藏虚假镜像 URL 的示例*

深入研究恶意包

除了通过恶意 GitHub 存储库传播恶意软件外，攻击者还利用名为“yocolor”的恶意 Python 包进一步分发包含恶意软件的“colorama”包。他们采用了相同的误植技术，将恶意包托管在“ files[.]pypihosted[.]org ”域上，并使用与合法“colorama”包相同的名称。

通过操纵包安装过程并利用用户在 Python 包生态系统中的信任，攻击者确保只要在项目要求中指定恶意依赖项，就会安装恶意“colorama”包。这种策略使攻击者能够绕过怀疑并渗透到依赖 Python 打包系统完整性的毫无戒心的开发人员的系统中。

![]()

阶段1

第一阶段是毫无戒心的用户从误植域“files[.]pypihosted.org”下载包含恶意依赖项“colorama”的恶意存储库或软件包 。

![]()*ycolor 包中恶意代码的示例*

第二阶段

恶意“colorama”包包含与合法包相同的代码，除了一小段额外的恶意代码。最初，该代码位于 “colorama/tests/\_\_init\_\_.py”文件中， 但攻击者后来将其移至 “colorama/init.py”， 可能是为了确保恶意代码更可靠地执行。该代码为攻击的后续阶段奠定了基础。

攻击者采用了一种巧妙的技术将恶意负载隐藏在代码中。他们使用大量空白将恶意代码推离屏幕，要求检查包的人在发现隐藏的恶意内容之前水平滚动很长一段时间。该技术旨在使恶意代码在快速查看包的源文件时不那么引人注目。

此代码从“hxxps[:]//pypihosted[.]org/version”获取并执行另一段 Python 代码，该代码安装必要的库并使用“fernet”库解密硬编码数据。然后，解密的代码会搜索有效的 Python 解释器，并执行保存在临时文件中的另一个混淆的代码片段。

[](https://checkmarx.com/wp-content/uploads/2024/03/white-space.mp4)

第三阶段

恶意软件进一步发展，从另一个外部链接获取额外的混淆Python代码：hxxp[:]//162[.]248[.]100[.]217/inj，并使用“exec”执行它。

![]()

第四阶段

经过分析，很明显，攻击者已经对他们的代码进行了混淆。使用中文和日文字符串、zlib 压缩和误导性变量名称等技术只是使代码分析和理解复杂化的一些技术。

简化的代码检查受感染主机的操作系统，并选择随机文件夹和文件名来托管最终的恶意Python代码，该代码从“hxxp[:]//162[.]248[.]100.217[:]80/”中检索grb。”

恶意软件还采用持久化机制，通过修改Windows注册表创建新的运行键，确保每次系统重新启动时都会执行恶意Python代码。这使得恶意软件即使在重新启动后也能在受感染的系统上保持存在。

![]()

第五阶段——没有人掉队

从远程服务器检索到的恶意软件的最后阶段揭示了其数据窃取能力的真实程度。它针对各种流行的软件应用程序并窃取敏感信息，其中一些信息包括：

浏览器数据：该恶意软件针对多种网络浏览器，包括 Opera、Chrome、Brave、Vivaldi、Yandex 和 Edge。它搜索与每个浏览器关联的特定目录，并尝试窃取敏感数据，例如 cookie、自动填充信息、浏览历史记录、书签、信用卡和登录凭据。

Discord 数据：该代码通过搜索与 Discord 相关的目录和文件来专门针对 Discord。它尝试定位并解密 Discord 令牌，这些令牌可用于未经授权访问受害者的 Discord 帐户。

加密货币钱包：该恶意软件包含一系列旨在从受害者系统中窃取的加密货币钱包。它搜索与每个钱包关联的特定目录并尝试窃取与钱包相关的文件。然后，被盗的钱包数据被压缩成 ZIP 文件并上传到攻击者的服务器。

Telegram 会话：恶意软件还尝试窃取 Telegram 会话数据。它搜索与 Telegram 相关的目录和文件，旨在捕获受害者的会话信息。通过访问 Telegram 会话，攻击者可能会未经授权访问受害者的 Telegram 帐户和通信。

计算机文件：该恶意软件包含一个文件窃取程序组件，可搜索名称或扩展名中包含特定关键字的文件。它的目标目录包括桌面、下载、文档和最近使用的文件。

Instagram 数据：恶意软件尝试利用 Instagram 会话令牌从受害者的 Instagram 个人资料中窃取敏感信息。该恶意软件使用窃取的会话令牌向 Instagram API 发送请求，以检索各种帐户详细信息。

对最终有效负载的进一步分析表明，该恶意软件还包含键盘记录组件。它捕获受害者的击键并将其保存到文件中，然后将其上传到攻击者的服务器。此功能允许攻击者监视和记录受害者的键入输入，从而可能暴露密码、个人消息和财务详细信息等敏感信息。

使用各种技术将被盗数据泄露到攻击者的服务器。该代码包含将文件上传到匿名文件共享服务（例如 GoFile 和 Anonfiles）的功能。它还使用 HTTP 请求将窃取的信息以及硬件 ID 或 IP 地址等唯一标识符发送到攻击者的服务器，以跟踪受害者。

结论

该活动是恶意行为者采用复杂策略通过 PyPI 和 GitHub 等可信平台分发恶意软件的一个典型例子。

这一事件凸显了在安装软件包和存储库时保持警惕的重要性，即使是来自可信来源的软件包和存储库。彻底审查依赖关系、监控可疑网络活动并维护强大的安全实践以降低成为此类攻击受害者的风险至关重要。

随着网络安全社区不断发现和分析这些威胁，协作和信息共享对于持续打击软件供应链中的恶意行为者仍然至关重要。

我们向 Cloudflare 报告了被滥用的域名，它们已被删除。

作为 Checkmarx 供应链安全解决方案的一部分，我们的研究团队持续监控开源软件生态系统中的可疑活动。我们跟踪并标记可能表明不法行为的“信号”，并及时提醒我们的客户以帮助保护他们。

共同努力维护开源生态系统的安全。

时间线

* 2022 年 11 月：  Pypi 用户“felpes”向 Python 包索引 (PyPI) 添加了三个包，其中包含各种形式的恶意代码。
* 2024 年 2 月 1 日： 攻击者注册了域名 pypihosted[.]org。
* 2024 年 3 月 4 日：  top.gg 贡献者的 GitHub 帐户遭到泄露，攻击者利用该帐户向组织的存储库提交恶意代码。
* 2024 年 3 月 13 日： 攻击者注册了域名 pythanhosted.org，进一步扩展了他们的域名仿冒基础设施。
* 2024 年 3 月 5 日：  “felpes”在 PyPI 上发布了恶意包“yocolor”，充当恶意软件的传递机制。

Packages

|  |  |  |  |
| --- | --- | --- | --- |
| Package Name | Version | Username | Date Released |
| jzyrljroxlca | 0.3.2 | pypi/xotifol394 | 21-Jul-23 |
| wkqubsxekbxn | 0.3.2 | pypi/xotifol394 | 21-Jul-23 |
| eoerbisjxqyv | 0.3.2 | pypi/xotifol394 | 21-Jul-23 |
| lyfamdorksgb | 0.3.2 | pypi/xotifol394 | 21-Jul-23 |
| hnuhfyzumkmo | 0.3.2 | pypi/xotifol394 | 21-Jul-23 |
| hbcxuypphrnk | 0.3.2 | pypi/xotifol394 | 20-Jul-23 |
| dcrywkqddo | 0.4.3 | pypi/xotifol394 | 20-Jul-23 |
| mjpoytwngddh | 0.3.2 | pypi/poyon95014 | 21-Jul-23 |
| eeajhjmclakf | 0.3.2 | pypi/tiles77583 | 21-Jul-23 |
| yocolor | 0.4.6 | pypi/felpes | 05-Mar-24 |
| coloriv | 3.2 | pypi/felpes | 22-Nov-22 |
| colors-it | 2.1.3 | pypi/felpes | 17-Nov-22 |
| pylo-color | 1.0.3 | pypi/felpes | 15-Nov-22 |
| type-color | 0.4 | felipefelpes | 01-Nov-22 |

IOC

* hxxps[:]//files[.]pythanhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.5.tar.gz
* hxxps[:]//files[.]pypihosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz
* hxxps://files[.]pypihosted[.]org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.3.tar.gz
* 162[.]248.101.215
* pypihosted.org/version
* 162[.]248.100.217
* 162.248.100.117
* 0C1873196DBD88280F4D5CF409B7B53674B3ED85F8A1A28ECE9CAF2F98A71207
* 35AC61C83B85F6DDCF8EC8747F44400399CE3A9986D355834B68630270E669FB
* C53B93BE72E700F7E0C8D5333ACD68F9DC5505FB5B71773CA9A8668B98A17BA8

本文翻译自 [原文链接](https://checkmarx.com/blog/over-170k-users-affected-by-attack-using-fake-python-infrastructure/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294329](/post/id/294329)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://checkmarx.com/blog/over-170k-users-affected-by-attack-using-fake-python-infrastructure/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb...