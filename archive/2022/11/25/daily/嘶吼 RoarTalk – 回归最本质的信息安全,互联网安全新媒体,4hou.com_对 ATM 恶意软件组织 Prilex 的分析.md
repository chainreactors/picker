---
title: 对 ATM 恶意软件组织 Prilex 的分析
url: https://www.4hou.com/posts/nJP4
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-25
fetch_date: 2025-10-03T23:43:05.578087
---

# 对 ATM 恶意软件组织 Prilex 的分析

对 ATM 恶意软件组织 Prilex 的分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 对 ATM 恶意软件组织 Prilex 的分析

lucywang
[技术](https://www.4hou.com/category/technology)
2022-11-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)131089

收藏

导语：该恶意软件能够从插入受感染 ATM 的信用卡和借记卡上的磁条中捕获信息。之后，这些有价值的信息可用于克隆银行卡并从银行客户那里窃取更多资金。

![sl-malicious-pos-terminal-payment-transaction-phone-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447425141132.jpeg "1664447425141132.jpeg")

ATM 恶意软件组织 Prilex自 2014 年起就开始活跃，不过在2016 年，该组织决定放弃ATM 业务，将所有注意力集中在 PoS 系统。很快，他们采用了恶意软件即服务模式，并将攻击范围扩大至巴西以外的地方，以模块化的方式创建了一套包括后门、上传程序和窃取程序的工具。

Prilex PoS恶意软件从一个简单的内存抓取器演变为非常先进和复杂的恶意软件，直接处理 PIN pad硬件协议而不是使用更高级别的 API，在目标软件中进行实时修补，挂钩操作系统库，扰乱回复、流量和端口，以及从基于重放的攻击切换到为其 GHOST 交易生成密码，即使是使用 CHIP 和 PIN 技术保护的信用卡。

在 2016 年的狂欢节期间，一家巴西银行意识到他们的 ATM 已被黑客入侵，其中的所有现金都被盗了。根据事后报告，策划此次攻击的攻击者能够在同一起事件中感染属于一家银行的1000多台机器，这使他们得以在巴西复制2.8万张独特的信用卡。

攻击者没有进入ATM的物理权限，但他们能够通过一个包含4G路由器和树莓派的DIY设备访问银行的网络。通过打开后门，他们能够劫持该机构的无线连接，并随意攻击 ATM。在获得初始网络访问权限后，攻击者将运行网络识别过程以查找每个 ATM 的 IP 地址。有了这些信息，攻击者将启动横向移动阶段，使用默认的 Windows 凭据，然后在所需的系统中安装定制的恶意软件。后门将允许攻击者通过启动恶意软件界面并输入攻击者提供的代码来清空 ATM 套接字，每个被黑客攻击的 ATM的代码都是自定义的。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447439100907.png "1664447439100907.png")

感染了 Prilex 的 ATM

攻击中使用的恶意软件名为 Prilex，它是通过使用特权信息和 ATM 网络的高级知识从零开始开发的。该恶意软件能够从插入受感染 ATM 的信用卡和借记卡上的磁条中捕获信息。之后，这些有价值的信息可用于克隆银行卡并从银行客户那里窃取更多资金。

**演变成 PoS 恶意软件的过程**

Prilex 已经从专注于 ATM 的恶意软件演变为针对巴西国内的支付系统的模块化恶意软件，即所谓的 EFT/TEF 软件。它们的 ATM 和 PoS 版本之间有许多相似之处。他们的第一个 PoS 恶意软件于 2016 年 10 月在野外被发现。前两个样本的编译日期为 2010/2011，如下图所示。但是，研究人员认为由于不正确的系统日期和时间设置而设置了无效的编译日期。在后来的版本中，时间戳对应于发现样本的时间。我们还注意到，在 2022 年开发的软件中，开发人员开始使用 Subversion 作为版本控制系统。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447450113117.png "1664447450113117.png")

Prilex PoS 恶意软件的版本：2022 年的 3 个新版本

如上所示，Prilex 在 2020 年非常活跃，但在 2021 年突然消失，并在 2022 年重新出现并发布了三个新变体。

Prilex的PoS版本是用Visual Basic编写的，但本文中描述的窃取模块是用p-code编写的。简而言之，这是Visual Basic 程序中的高级指令与 CPU 执行的低级本机代码之间的中间步骤。 Visual Basic在运行时将p-code语句转换为本机代码。

Prilex 并不是唯一起源于巴西的 PoS 恶意软件，研究人员发现它与原来的 Trojan-Spy.Win32.SPSniffer 存在某种联系，两个家族都能够拦截PIN pad的信号，但使用的方法不同。

PIN pad配备硬件和安全功能，以确保在有人试图篡改设备时擦除安全密钥。事实上，PIN在进入设备时使用各种加密方案和对称密钥进行加密。大多数情况下，这是一个三重DES编码器，使它很难破解PIN。

但是有一个问题：这些设备总是通过 USB 或串行端口连接到计算机，这些端口与 EFT 软件进行流量。原来的 PIN pad设备使用过时和弱加密方案，使得恶意软件很容易安装 USB 或串行端口嗅探器来捕获和解密 PIN pad和受感染系统之间的流量。这就是 SPSniffer 获取信用卡数据的方式。有时流量甚至没有加密。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447459167650.png "1664447459167650.png")

SPSniffer：允许捕获非加密流量的串口嗅探器

Prilex 用于捕获信用卡数据的主要方法是使用 PoS 系统库中的补丁，允许恶意软件收集软件传输的数据。恶意软件将寻找一组特定的可执行文件和库的位置，以便应用补丁，从而覆盖原始代码。安装补丁后，恶意软件会从 TRACK2 收集数据，例如帐号和到期日期，以及执行欺诈交易所需的其他持卡人信息。

**初始感染载体**

Prilex 不是一种广泛传播的恶意软件，因为它不是通过电子邮件垃圾邮件活动传播的。它具有高度针对性，通常通过社会工程传播，例如，目标企业可能会接到自称是“技术人员”的电话，他坚持认为该公司需要更新其PoS软件。假冒技术人员可能会亲自访问目标，或要求受害者安装AnyDesk，并为其提供远程访问权限，以安装恶意软件。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447467965144.png "1664447467965144.png")

PoS 供应商关于 Prilex 社会工程攻击的警告

**使用EMV标准的漏洞发起攻击**

巴西于 1999 年开始使用EMV，如今，该国发行的几乎所有卡都支持芯片。芯片内部有一个基于java的小应用程序，可以很容易地操作以创建一张“金票（golden ticket）”卡，该卡在大多数销售点系统中都有效。这使攻击者能够升级他们的工具集，使他们能够以这种新技术为特色创建自己的卡片。

最初版本的Prilex能够执行重放攻击，在这种攻击中，它们没有破坏EMV协议，而是利用了糟糕的实现。由于支付运营商未能执行 EMV 标准要求的某些验证，攻击者可以利用该过程中的这一漏洞为自己谋取利益。

在这种攻击中，欺诈者通过卡片网络推送常规磁条交易作为EMV购买，因为他们控制着支付终端，并有能力操纵通过该终端进行交易的数据字段。后来他们转而从真正的基于 EMV 的芯片卡交易中获取流量。攻击者可以将被盗的卡数据插入交易流程，同时动态修改商家和收购方的银行账户。

至少从2014年起，巴西网络攻击者已经成功发起重放攻击，比如2019 年对一家德国银行的攻击，该银行损失了 150 万欧元， Prilex团伙声称对此负责。从名称字段和工具的功能来看，他们很可能使用了他们在黑市上销售的软件。

为了使用克隆的信用卡自动进行攻击，Prilex 攻击者使用了 Xiello 等工具，这是研究人员在 2020 年通过遥测技术发现的。该工具允许网络攻击者在进行欺诈性购买时批量使用信用卡。它将购买数据发送给信用卡购买者，然后由他们批准或拒绝交易。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447476206172.png "1664447476206172.png")

Prilex 用于自动化交易的 Xiello 工具

随着支付行业和信用卡发行商修复 EMV 中的漏洞被修复，重放攻击变得过时且无效，这促使 Prilex 团伙采用其他新的信用卡欺诈方式。

**从“Replay”技术到“Ghost”技术的演进**

最新版本的Prilex在攻击方式上与之前的版本有所不同：该组织已从重放攻击转变为使用受害者卡在店内支付过程中生成的密码进行欺诈交易，攻击者将其称为“GHOST 交易”。

在这些攻击中，Prilex 样本作为 RAR SFX 可执行文件安装在系统中，将所有必需的文件提取到恶意软件目录并执行安装脚本（VBS 文件）。从已安装的文件中，我们可以突出显示该活动中使用的三个模块：一个后门，在这个版本中除了用于流量的C2服务器外没有改变；一个窃取模块和一个上传模块。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447484292276.png "1664447484292276.png")

维护持久性的Prilex方法

窃取模块负责拦截销售点软件和用于在交易期间读取卡的 PIN pad之间的所有流量。一旦识别出正在运行的交易，恶意软件将拦截并修改交易内容，以便能够捕获卡信息并向受害者的卡请求新的 EMV 密码。这些密码随后用于 GHOST 交易。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447494202766.png "1664447494202766.png")

用于解析发送/接收的密码键盘消息的方法

为了针对一个特定的进程，攻击者将对机器进行初步筛选，以检查它是否是具有足够信用卡交易的有趣目标，并确定他们将针对的流程。

进程被识别后，恶意软件将继续安装拦截交易信息所需的挂钩。由于 PoS 软件和读卡器之间的流量是通过 COM 端口进行的，因此恶意软件会在目标进程内安装许多 Windows API 的挂钩，旨在根据需要监控和更改数据。有趣的是，Prilex 不是为挂钩程序分配内存，而是在模块内存中找到空闲空间，这种技术称为代码洞穴，这使得一些安全解决方案很难检测到受感染系统中的威胁。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447503182590.png "1664447503182590.png")

添加到CloseHandle进程中的挂钩代码

从交易中捕获的所有信息都被保存到一个加密文件中，该文件位于恶意软件配置之前设置的目录中。这些文件随后会被发送到恶意软件C2服务器上，允许网络攻击者通过以虚假公司名义注册的欺诈性 PoS 设备进行交易。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447513702870.png "1664447513702870.png")

捕获的信用卡数据稍后将被发送到运营商服务器

以前的版本监控交易是为了获取原始交易生成的密码，然后使用收集的密码执行重放攻击。在这种情况下，密码具有相同的 ATC（应用程序交易计数器），允许通过重复使用 ATC 以及密码内部的日期与提交日期不匹配的事实来识别欺诈交易，因为欺诈交易是在较晚的时间提交的。

在较新版本的 Prilex 执行的 GHOST 攻击中，它会在捕获交易后请求新的 EMV 密码。然后，这些密码将通过其中一种网络犯罪工具用于欺诈交易，其输出日志如下所示。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447520170378.png "1664447520170378.png")

上表显示了从恶意软件收集的数据。它包含由卡生成的授权请求密码 (ARQC)，现在应该得到发卡机构的批准。剖析响应（80128000AA5EA486052A8886DE06050A03A4B8009000）后，我们得到以下信息。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447529752233.png "1664447529752233.png")

卡上应用了多个应用程序密码，其中交易金额（蓝色）、ATC（绿色）和生成的密码（红色）在每次交易中都会发生变化。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447537276549.png "1664447537276549.png")

简而言之，这是整个 Prilex 方案：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447545875530.png "1664447545875530.png")

Prilex：从感染到套现

**后门模块**

后门有许多命令，除了内存扫描程序常见的内存扫描之外，较老的(ATM) Prilex版本还提供了一个命令，用于调试进程和查看其内存。这很可能被用于了解目标软件行为并对恶意软件或环境进行调整以执行欺诈交易。旧版本的 Prilex 对特定软件库进行了修补，而较新的示例不再依赖特定软件，而是使用Windows api来执行它的工作。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220929/1664447558270991.png "1664447558270991.png")

Prilex 调试器

下面是在ATM版本的Prilex中使用的命令列表，其中包括调试：

```
Reboot, SendKeys, ShowForm, Inject, UnInject, HideForm, Recursos, GetZip, SetStartup, PausaProcesso, LiberaProcesso, Debug, SendSnapShot, GetStartup, CapRegion, CapFerro, KillProcess, Shell, Process, GetModules, GetConfig, StartSendScreen, StopSendScreen, ReLogin, StartScan, GetKey,...