---
title: Rhysida勒索软件活动分析及其与VICE SOCIETY的联系
url: https://www.4hou.com/posts/PKG1
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-12
fetch_date: 2025-10-04T11:59:52.542409
---

# Rhysida勒索软件活动分析及其与VICE SOCIETY的联系

Rhysida勒索软件活动分析及其与VICE SOCIETY的联系 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Rhysida勒索软件活动分析及其与VICE SOCIETY的联系

lucywang
[技术](https://www.4hou.com/category/technology)
2023-08-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)152963

收藏

导语：Rhysida勒索软件组织于今年5月首次被披露。最近，该组织还与针对Prospect Medical Holdings的攻击有关，影响了美国的17家医院和166家诊所。

![微信截图_20230810151646.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230810/1691652290129150.png "1691652067145951.png")

Rhysida勒索软件组织于今年5月首次被披露，自那时起，它就与几起影响巨大的攻击事件有关，其中包括对智利军队的攻击。最近，该组织还与针对Prospect Medical Holdings的攻击有关，影响了美国的17家医院和166家诊所。在这次攻击之后，美国卫生与公众服务部将Rhysida定义为对医疗保健行业的重大威胁。

在分析最近一起针对教育机构的Rhysida勒索软件事件时，Check Point事件响应小组（CPRT）与Check Point Research（CPR）合作，观察到了一套独特的技术、战术和工具（TTP）。在分析中，研究人员发现了它与另一个勒索软件组织Vice Society的TTP有显著相似之处。Vice Society是自2021年以来最活跃、最具攻击性的勒索软件组织之一，主要针对教育和医疗保健行业。

例如，在 2022 年期间，该组织袭击了 33 个教育机构，超过 LockBit、BlackCat、BianLian 和 Hive 等其它勒索软件组织。自 2021 年 5 月开始活跃以来，Vice Society 与其它勒索软件组织主要区别在于其不使用自己的勒索软件变体，而是依赖于地下论坛上出售的 HelloKitty 和 Zeppelin 等预先存在的勒索程序二进制文件。微软曾以 DEV-0832 的名义追踪过该组织活动轨迹，发现在某些情况下，Vice Society 尽量避免部署勒索软件直接勒索，而是利用窃取的数据进行勒索。

鉴于Vice Society与Rhysida之间存在联系，有必要找到这种联系的技术证据。分析显示，这两个组织在技术上层面存在相似性，以及Rhysida的出现和Vice Society的消失之间存在明显关联。此外，这两个组织共同关注的目标都是教育和医疗保健行业。

据观察，Vice Society部署了各种商用勒索软件有效负载，所以Rhysida并不等同于Vice Society，但至少表明Vice Society运营商现在正在使用Rhysida勒索软件。

**战术、技术和程序**

由于之前对Rhysida勒索软件有效负载进行了彻底的分析，我们将重点关注导致其部署的TTP，特别是横向移动、凭证访问、防御规避、指挥和控制以及影响。

根据我们掌握的证据，使用Rhysida勒索软件的攻击者的赎金时间(TTR)相对较低。从最初出现横向移动的迹象到勒索软件的广泛部署，只有8天时间。

**横向活动**

攻击者使用多种工具进行横向活动，包括：

1.远程桌面协议（Remote Desktop Protocol ）——在整个攻击过程中，攻击者启动了RDP连接，并采取额外步骤故意删除相关的日志和注册表项，以避免被检测到，加强研究人员的分析工作。RDP仍然是在环境中进行横向移动的有效方法。

2.远程PowerShell会话（WinRM）——当通过RDP远程连接时，可以发现攻击者正在启动与环境中服务器的远程PowerShell连接。这种情况发生在部署勒索软件负载之前的几天。

3.PsExec——勒索软件有效负载本身是使用PsExec从环境中的服务器部署的。部署分两个阶段进行。

3.1 使用命令PsExec.exe -d \\VICTIM\_MACHINE -u "DOMAIN\ADMIN" -p "Password" -s cmd /c COPY "\\path\_to\_ransomware\payload.exe" "C:\windows\temp"复制恶意负载；

3.2 使用命令PsExec.exe -d \\VICTIM\_MACHINE -u "DOMAIN\ADMIN"" -p "Password" -s cmd /c c:\windows\temp\payload.exe执行恶意负载。

**凭据访问**

最值得注意的是，攻击者使用ntdsutil.exe来创建NTDS的备份。将其放入名为temp\_l0gs的文件夹中。此路径被攻击者多次使用。除此之外，攻击者还列举了域管理员帐户，并试图使用其中一些帐户登录。

**指挥与控制**

攻击者利用了几个后门和工具来实现持久性攻击，包括：

1.SystemBC：在一个成功的PowerShell会话中，攻击者执行一个SystemBC PowerShell植入，它通过安装一个名为socks的注册表运行项来在启动时执行脚本以维护持久性。植入程序的域为5.255.103[.]7。此外，攻击者设置了名为Windows Update的防火墙规则，以允许向另一台服务器5.226.141[.]196发送流量。

2.AnyDesk：通过远程管理工具AnyDesk观察到该攻击者。

**逃避检测**

在整个活动过程中，攻击者始终在其活动之后删除日志和取证工件。这包括：

1.删除最近使用的文件和文件夹的历史记录；

2.删除最近执行的程序列表；

3.删除文件资源管理器中最近输入的路径的历史记录；

4.删除PowerShell控制台历史文件；

5.删除当前用户临时文件夹中的所有文件和文件夹；

6.在RDP会话之后，攻击者还通过以下方式删除了RDP特定的日志：

7.在Windows注册表中的“HKCU:\Software\Microsoft\Terminal Server Client”下搜索所有子项，并删除每个子项的“UsernameHint”值（如果存在）；

8.删除用户Documents文件夹中的Default.rdp；

**影响**

在勒索软件部署当天，攻击者会利用AnyDesk提供的访问权限，使用PsExec在环境中广泛部署的勒索软件有效负载：

1.删除帐户访问权限（Account Access Removal）——攻击者启动了对域中数万个帐户的密码更改，以加强修复工作；

2.禁止系统恢复（Inhibit System Recovery）：在部署勒索软件负载之前，攻击者试图部署具有多种功能的PowerShell脚本，包括：

2.1 将所有本地密码更改为预定义密码；

2.2 阻止与数据库系统、备份软件、安全产品相关的业务；

2.3 禁用Windows Defender并阻止其运行；

2.4 使用wmic.exe和vssadmin.exe删除卷影副本；

2.5 将默认RDP端口更改为4000并为其创建防火墙规则；

2.6 删除所有Windows事件日志和PowerShell历史记录。

3.数据加密：如上所述，攻击者最终使用PsExec部署了Rhysida勒索软件有效负载。

**与Vice Society的关系**

在研究人员对Rhysida勒索软件TTP和基础设施的分析中，发现了与另一个臭名昭著的勒索软件组织Vice Society的几个相似之处，并且观察到随着时间的推移勒索软件有效负载的变化。有人提出Vice Society和Rhysida之间可能存在联系。接下来，我们将提供支持这一说法的其他证据。

**技术、工具和基础设施**

上面描述的许多技术与之前由微软和Intrinsec描述的Vice Society攻击高度相关。其中一些可能对勒索软件运营商来说很通用，但却以非常具体的方式被利用，包括不常见的特定路径：

1.使用NTDSUtil创建一个NTDS.dit备份到一个名为temp\_l0gs的文件夹。据观察，Vice Society也使用了同样的路径。

2.使用名为Windows Update的New-NetFirewallRule创建本地防火墙规则，以便于使用恶意软件SystemBC进行流量中继。SystemBC是通过存储在值socks下的注册表Run项执行的。

3.在部署勒索软件有效负载之前，启动整个域的密码更改过程；

4.对与Rhysida事件相关的基础设施的分析发现了一组PortStarter样本，其中一些之前被认为是Vice Society的。尽管PortStarter经常被描述为一种独立的恶意软件，但它的使用几乎完全与Vice Society联系在一起。

**受害者研究**

除了技术上的相似性之外，Rhysida的出现与Vice Society活动的显著下降也存在相关性。根据Rhysida和Vice Society泄漏网站的信息，研究人员构建了一个时间线。

自从Rhysida第一次出现以来，Vice Society只公布了两名受害者。这些很可能是在早些时候进行的，直到6月份才被公开。自2023年6月21日起Vice Society的攻击者就停止在他们的泄漏网站上发布信息。

![微信截图_20230810152210.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230810/1691652290152829.png "1691652142162170.png")

Rhysida和Vice Society受害者随时间的分布

此外，研究人员还注意到，受这两个组织影响的目标行业有相似之处，这两个组织以教育和医疗保健行业为目标而闻名。在整个勒索软件生态系统中，教育行业的受害者比例很高，这对这两个组织来说都是独一无二的：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230810/1691652291137130.png "1691652095614081.png")

Rhysida受害者在每个行业分布情况

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230810/1691652291138139.png "1691652104107325.png")

Vice Society受害者分布情况

**总结**

研究人员对Rhysida勒索软件攻击的分析揭示了该组织与臭名昭著的Vice Society之间的明确联系，但它也揭示了一个残酷的事实，大量勒索软件攻击者的TTP基本保持不变。目前观察到的大部分活动均已被任何勒索软件组织用于部署任何勒索软件有效负载。

上述分析表明，安全人员不仅要了解勒索软件有效负载的操作，还要了解导致其部署的整个过程的重要性。

本文翻译自：https://research.checkpoint.com/2023/the-rhysida-ransomware-activity-analysis-and-ties-to-vice-society/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Nl3C5ZlV)

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
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/abou...