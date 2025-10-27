---
title: Agenda勒索软件的Rust变体针对医疗等行业发起攻击
url: https://www.4hou.com/posts/QLyG
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-05
fetch_date: 2025-10-04T03:03:41.825945
---

# Agenda勒索软件的Rust变体针对医疗等行业发起攻击

Agenda勒索软件的Rust变体针对医疗等行业发起攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Agenda勒索软件的Rust变体针对医疗等行业发起攻击

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-01-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117452

收藏

导语：在这篇文章中，我们介绍了另一个已经开始使用这种语言的勒索软件组织Agenda(也称为Qilin)。

今年，各种勒索软件即服务组织相继在Rust中开发了他们的勒索软件版本，这其中就包括Agenda。Agenda的Rust变体瞄准了一些重要行业。我们将在本文中介绍Rust变体的工作原理。今年，BlackCat、Hive和RansomExx等勒索软件即服务（RaaS）组织开发了Rust版本的勒索软件，Rust是一种跨平台语言，可以更容易地为Windows和Linux等不同的操作系统定制恶意软件。在这篇文章中，我们介绍了另一个已经开始使用这种语言的勒索软件组织Agenda(也称为Qilin)。

根据我们在过去一个月的观察，Agenda勒索软件的活动包括在其泄露网站上发布许多公司的信息。攻击者不仅声称他们能够侵入这些公司的服务器，还威胁要公布他们的文件。勒索软件组织在其泄漏网站上发布的公司位于不同的国家，主要属于制造业和IT行业，总收入超过5.5亿美元。

最近，我们发现了一个用Rust语言编写的Agenda勒索软件样本，检测结果为Ransom.Win32.Agenda.THIAFBB。值得注意的是，同样的勒索软件最初是用Go语言编写的，以针对泰国和印度尼西亚等国家的医疗和教育部门而闻名。攻击者通过使用泄露的账户和唯一的公司ID等机密信息作为附加的文件扩展名，为目标受害者自定义了之前的勒索软件二进制文件。Rust变体还使用了间歇性加密，这是当今攻击者用于更快加密和逃避检测的新兴策略之一。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624927112534.png "1671624594212492.png")

VirusTotal中二进制文件的提交详细信息，包括提交日期和上传地区

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624934207820.png "1671624606105377.png")

BinText上显示二进制文件使用的Rust模块/函数的字符串

**技术分析**

执行时，Rust二进制文件会提示以下错误，要求将密码作为参数传递。这个命令行特性类似于用Golang编写的Agenda勒索软件二进制文件。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624935116124.png "1671624615170149.png")

执行示例时的错误提示

在以“-password”作为参数并结合虚拟密码“agenda apass”执行示例时，勒索软件示例将从终止各种进程和服务开始运行其恶意例程。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624936151079.png "1671624628127288.png")

终止应用程序和服务

针对我们分析的样本，勒索软件将扩展名“MmXReVIxLV”附加到加密文件中。它还在命令提示符上显示活动日志，包括已加密的文件和运行时间。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624937110483.png "1671624638139275.png")

加密文件示例

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624938536348.png "1671624648888478.png")

加密文件中的日志

然后，勒索软件将继续在其加密的每个目录上释放其勒索通知。正如其勒索说明中所观察到的，用于执行勒索软件的密码也将用作登录勒索软件组支持聊天网站的密码。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624939265803.png "1671624658528672.png")

勒索通知

**勒索软件分析**

不同于Agenda的Golang变体，它接受10个参数，Rust变体只接受3个参数：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624939918542.png "1671624667122426.png")

Agenda勒索软件Rust变体使用的参数

Rust变体在二进制文件中也包含硬编码配置，就像以前在Golang中编译的示例一样。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624940662136.png "1671624676106280.png")

包含配置的二进制文件内的函数

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624942599413.png "1671624685315822.png")

包含配置的字符串

它还在其配置中添加了-n、-p、fast、skip和step标志，这些标志在Golang变体配置中不存在，仅通过命令行参数使用。经过进一步分析，我们了解到这些标志用于间歇性加密。这种策略使勒索软件能够根据标志的值对文件进行部分加密，从而更快地加密受害者的文件。这种策略在勒索软件攻击者中越来越流行，因为它可以让他们更快地加密，并避免严重依赖于读/写文件操作的检测。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624943427122.png "1671624696471085.png")

用于间歇加密的标志

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624944135100.png "1671624705165868.png")

用于间歇加密的标志

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624945207252.png "1671624715208177.png")

Agenda勒索软件Golang变体接受的命令行参数

我们试图使用其配置中的一些标志来模拟其加密行为。对于这个模拟，我们使用一个填充“a”作为内容的虚拟文件。

对于快速模式：

值：1

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624946128301.png "1671624724190373.png")

快速标志设置为1

加密字节：1\*0x200000h，其中1是快速标志中设置的值

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624947148355.png "1671624735591383.png")

0x200000h字节加密

对于N-P模式：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624948212461.png "1671624746152588.png")

标志设置为 n = 1; p = 1

总大小=88082336字节，加密的字节数= 1 \* 0x200000,h，其中1是n标志中设置的值，跳过的字节数= 880818字节(整个文件的1%)，其中1是p标志中设置的值。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624950276952.png "1671624759384475.png")

加密字节的0x200000h

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624951141790.png "1671624769599709.png")

880818字节（相当于文件的1%）加密

除了用于不同加密模式的附加标志之外，Rust变体还将AppInfo包括在要终止的服务列表中。它禁用了用户帐户控制（UAC），这是一项Windows功能，有助于防止恶意软件以管理权限执行，从而导致无法以管理权限运行其他应用程序。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624952156663.png "1671624784606564.png")

使用与service\_CONTROL\_stop等效的参数0x01停止服务的函数

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624953474655.png "1671624794767890.png")

用于使用等同于SERVICE\_DISABLED的参数0x04禁用服务的函数

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624953157676.png "1671624804115795.png")

禁用AppInfo服务后，无法运行具有管理权限的应用程序

众所周知，Agenda勒索软件还可以为每个受害者部署自定义的勒索软件，我们已经看到，它的Rust变体有一个分配的空间，用于在其配置中添加帐户，主要用于权限升级。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624954102968.png "1671624814983938.png")

在Agenda勒索软件的Rust变体配置中分配的帐户

要附加在加密文件上的文件扩展名在其配置中是硬编码的。

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624955117818.png "1671624823573707.png")

要附加的文件扩展名

然而，与之前的Golang变体不同，攻击者在Rust变体的配置中不包括受害者的凭据。后者的这一特性不仅可以阻止其他研究人员访问勒索软件的聊天支持网站，还可以在外部提供样本时访问攻击者的对话。它还可以防止来自受害者之外的其他人的主动信息。

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221221/1671624955156516.png "1671624901154383.png")

Agenda勒索软件聊天支持网站

**总结**

Agenda是一个新兴的勒索软件家族，最近一直针对医疗保健和教育行业等关键部门。目前，它的攻击者似乎正在将他们的勒索软件代码迁移到Rust，因为最近的样本仍然缺乏在用Golang变体编写的原始二进制文件中看到的一些特征。Rust语言在攻击者中越来越受欢迎，因为它更难分析，而且反病毒引擎的检测率较低。

本文翻译自：https://www.trendmicro.com/en\_us/research/22/l/agenda-ransomware-uses-rust-to-target-more-vital-industries.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?B6ZpYdio)

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

![](https://img.4hou.com/FpAB1n2wt6I0zw18n_Sz-3Nj9Ctg)

# [gejigeji](https://www.4hou.com/member/mqy0)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4h...