---
title: 新型Mallox勒索软件通过招募加盟组织来快速扩张
url: https://www.4hou.com/posts/kjX6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-31
fetch_date: 2025-10-04T11:51:05.867610
---

# 新型Mallox勒索软件通过招募加盟组织来快速扩张

新型Mallox勒索软件通过招募加盟组织来快速扩张 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Mallox勒索软件通过招募加盟组织来快速扩张

lucywang
[技术](https://www.4hou.com/category/technology)
2023-07-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125188

收藏

导语：最近，Unit 42的研究人员观察到与去年相比，利用MS-SQL服务器传播勒索软件的Mallox勒索软件活动增加了近174%。

Mallox（又名TargetCompany、FARGO和Tohnichi）是一种针对Windows系统的勒索软件。自2021年6月出现以来就一直很活跃，并以利用不安全的MS-SQL服务器作为攻击手段来攻击受害者的网络而闻名。

最近，Unit 42的研究人员观察到与去年相比，利用MS-SQL服务器传播勒索软件的Mallox勒索软件活动增加了近174%。研究人员观察到，Mallox勒索软件使用暴力破解、数据泄露和网络扫描仪等工具。此外，有迹象表明，该组织正在扩大其业务，并在黑客论坛上招募成员。

**Mallox勒索软件概述**

与许多其他勒索软件一样，Mallox勒索软件使用了双重勒索方法：在加密组织文件之前窃取数据，然后威胁将窃取的数据发布在泄露网站上，增加勒索筹码。

下图显示了Tor浏览器上的Mallox勒索软件网站。尽管这些组织的名称和标识已经被涂黑，但这就是该组织展示其目标泄露数据的方式。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690130978189057.png "1690130978189057.png")

Tor浏览器上的Mallox网站

每个受害者都有一把私钥，可以与该组织互动并协商条款和付款。下图展示了用于交流的工具。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690130996545452.png "1690130996545452.png")

Tor浏览器上的Mallox私人聊天

Mallox勒索软件幕后组织声称有数百名受害者被攻击。虽然受害者的实际人数尚不清楚，但分析显示，全球有潜在受害者已经很多，涉及多个行业，包括制造业、法律服务、批发和零售业。

自2023年初以来，Mallox的活动一直在不断增加。根据研究人员追踪分析和从公开威胁情报来源收集的数据，与2022年下半年相比，2023年Mallox攻击增加了约174%。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131024359941.png "1690131024359941.png")

从2022年下半年到2023年上半年的Mallox攻击尝试

**初始访问**

自2021年出现以来，Mallox组织一直采用相同的方法获得初始访问权限，该组织以不安全的MS-SQL服务器为目标渗透到网络中。这些攻击从字典暴力攻击开始，尝试针对MS-SQL服务器的已知或常用密码列表。在获得访问权限后，攻击者使用命令行和PowerShell从远程服务器下载Mallox勒索软件负载。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131045848813.png "1690131045848813.png")

响应由Cortex XDR和XSIAM引发的Mallox勒索软件字典暴力攻击而引发的警报示例

Mallox勒索软件感染的命令行示例：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131063213540.png "1690131063213540.png")

该命令行执行以下操作：

从hxxp://80.66.75[.]36/aRX.exe下载勒索软件有效负载，并保存为tzt.exe；

运行名为updt.ps1的PowerShell脚本；

接下来，有效负载继续执行以下操作（未在上面显示的命令行脚本中显示）：

下载另一个名为system.bat的文件，并将其保存为tzt.bat；

“tzt.bat”文件用于创建名为“SystemHelp”的用户，并启用RDP协议；

使用Windows管理工具（WMI）执行勒索软件有效负载tzt.exe；

下图显示了Cortex XDR和XSIAM如何检测SQL服务器利用的第一阶段。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131089179330.png "1690131089179330.png")

SQL服务器利用过程（仅限于测试目）

**勒索软件执行**

在进行任何加密之前，勒索软件有效负载会尝试多种操作以确保勒索软件成功执行，例如：

尝试使用sc.exe和net.exe停止和删除sql相关的服务。这样，勒索软件就可以访问并加密受害者的文件数据。

试图删除卷影，使文件加密后更难被恢复。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131107114411.png "1690131107114411.png")

删除卷影副本的警报，由Cortex XDR和XSIAM引发

试图使用微软的wevtutil命令行工具清除应用程序、安全、设置和系统事件日志，以阻止检测和取证分析工作；

使用Windows内置的takeown.exe命令修改文件权限，拒绝访问cmd.exe和其他关键系统进程；

防止系统管理员使用bcdedit.exe手动加载系统映像恢复功能；

试图使用taskkill.exe终止与安全相关的进程和服务，以逃避检测；

试图绕过检测反勒索软件产品，如果存在，通过删除其注册表项。下图是整个过程的一个示例。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131125331897.png "1690131125331897.png")

删除检测注册表项

如下图所示，勒索软件的流程树中显示了上述一些活动：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131141188535.png "1690131141188535.png")

攻击的完整进程树，如Cortex XDR和XSIAM所示（仅为检测模式）

这个调查的Mallox勒索软件示例使用ChaCha20加密算法对文件进行加密，并为加密的文件添加.malox扩展名。除了使用受害者的名字作为扩展名之外，观察到的其他文件扩展名还有：.FARGO3、.colouse、.avast、.bitenc和.xollam。有关Cortex XDR中加密文件的示例如下图所示。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131161193123.png "1690131161193123.png")

Cortex XDR检测到的Mallox勒索软件加密的文件示例（仅为检测模式）

Mallox在受害者驱动器的每个目录中都留下了一张勒索信，其中解释了感染情况并提供了联系信息，如下图所示。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131183163192.png "1690131183163192.png")

Mallox勒索信示例

执行后，恶意软件会自行删除。

根据其一名成员的说法，Mallox是一个相对较小且封闭的组织。然而，该组织似乎正在通过招募附属公司来扩大业务。

在这次采访几天后，一位名叫Mallex的用户在黑客论坛RAMP上发帖称，Mallox勒索软件组织正在为一个新的Mallox软件即服务（RaaS）分支计划招募分支机构，如下图所示。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131201203645.png "1690131201203645.png")

用户Mallx在RAMP上的帖子

早在2022年5月，一位名叫RansomR的用户在著名的黑客论坛上发帖称，Mallox组织正在寻找加入该组织的附属公司。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131230132056.png "1690131230132056.png")

RansomR在null上的帖子

如果他们的计划取得成功，Mallox组织可能会扩大其覆盖范围，以攻击更多的组织。

**总结**

Mallox勒索软件组织在过去几个月里更加活跃，如果招募附属机构成功，他们最近的招募工作可能使他们能够攻击更多的组织。

组织应该时刻保持高度警惕，并准备好防御勒索软件的持续威胁。这不仅适用于Mallox勒索软件，也适用于其他勒索软件。

建议确保所有面向互联网的应用程序都配置正确，所有系统都打了补丁并尽可能更新。这些措施将有助于减少攻击面，从而限制攻击。

部署XDR/EDR解决方案来执行内存检查和检测进程注入技术。执行攻击搜索，寻找与安全产品防御逃避、服务帐户横向移动和域管理员相关的用户行为相关的异常行为的迹象。

**缓解措施**

Palo Alto Networks Cortex XDR检测并阻止Mallox勒索软件执行的文件操作和其他活动。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131281106439.png "1690131281106439.png")

阻止Mallox执行的终端用户通知

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131314252977.png "1690131314252977.png")

由Cortex XDR和XSIAM引发的可疑文件修改警报（仅为检测模式）

SmartScore是一个独特的机器学习驱动的评分引擎，它将安全调查方法及其相关数据转换为混合评分系统，对涉及Mallox勒索软件的事件进行了100分的评分。这种类型的评分可以帮助分析人员确定哪些事件更紧急，并提供评估原因，帮助确定优先级。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230724/1690131330188140.png "1690131330188140.png")

关于Mallox勒索软件事件的SmartScore信息

针对Mallox勒索软件的安全产品要具有以下功能，才能起到有效保护：

识别已知的恶意样本；

高级URL过滤和DNS安全将与该组织关联的域识别为恶意；

通过分析来自多个数据源（包括终端、网络防火墙、Active Directory、身份和访问管理解决方案以及云工作负载）的用户活动来检测基于用户和凭据的威胁。另外，还可以通过机器学习建立用户活动的行为概况。通过将新活动与过去的活动和预期行为进行比较，检测到攻击的异常活动。

本文翻译自：https://unit42.paloaltonetworks.com/mallox-ransomware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8c72DTHh)

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

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/member/eXPv)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/eXPv)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https...