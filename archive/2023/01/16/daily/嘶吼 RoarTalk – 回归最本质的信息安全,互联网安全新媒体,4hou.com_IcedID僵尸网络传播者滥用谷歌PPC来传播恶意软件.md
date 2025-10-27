---
title: IcedID僵尸网络传播者滥用谷歌PPC来传播恶意软件
url: https://www.4hou.com/posts/N1qv
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-16
fetch_date: 2025-10-04T03:59:12.795582
---

# IcedID僵尸网络传播者滥用谷歌PPC来传播恶意软件

IcedID僵尸网络传播者滥用谷歌PPC来传播恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# IcedID僵尸网络传播者滥用谷歌PPC来传播恶意软件

luochicun
[技术](https://www.4hou.com/category/technology)
2023-01-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)1002014

收藏

导语：本文介绍了IcedID僵尸网络的最新传播方法和它使用的新加载程序的技术细节。

我们分析了IcedID僵尸网络的最新变化，该活动滥用谷歌点击付费(PPC)广告，通过恶意广告攻击传播IcedID。 IcedID 是最早在 2017 年被披露的模块化银行木马，也是近年来最流行的恶意软件家族之一。IcedID 主要针对金融行业发起攻击，还会充当其他恶意软件家族（如 Vatet、Egregor、REvil）的 Dropper。

在密切跟踪IcedID僵尸网络的活动后，我们发现它的传播方法发生了一些重大变化。自2022年12月以来，我们观察到谷歌点击付费(PPC)广告被攻击者滥用，通过恶意广告攻击传播IcedID。趋势科技已将检测到的IcedID变体命名为TrojanSpy.Win64.ICEDID.SMYXCLGZ。

像谷歌广告这样的广告平台，其目的是使企业能够向目标受众展示广告，以提高流量和增加销售。恶意软件发布者滥用同样的功能，使用一种被称为恶意广告的技术，其中选择的关键字被劫持，显示恶意广告，诱使毫无戒心的搜索引擎用户下载恶意软件。

在我们的调查中，攻击者使用恶意广告通过合法组织和知名应用程序的克隆网页传播IcedID恶意软件。最近，美国联邦调查局(FBI)发布了一份关于网络犯罪分子如何滥用搜索引擎广告服务来伪装成合法网站，并通过一些经济诱惑将用户引向恶意网站。

本文介绍了IcedID僵尸网络的最新传播方法和它使用的新加载程序的技术细节。

**技术分析**

有机搜索结果是由Google PageRank算法生成的，而谷歌广告出现在有机搜索结果的上方、旁边、下方或更突出的位置。当这些广告被攻击者通过恶意广告劫持时，它们可以将用户引导到恶意网站。

**劫持搜索结果的关键词**

在调查中，我们发现IcedID传播者劫持了这些品牌和应用程序用来显示广告的关键词：

![？？.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688204606824.png "1672687764228657.png")

这些恶意网站看起来就像合法网站一样。下图显示了一个看起来合法的恶意Slack网页，被IcedID传播者用来引诱受害者下载恶意软件。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688205111375.png "1672687781163128.png")

一个被IcedID传播者使用的看似合法的恶意Slack网页

**感染链**

整个感染流程包括传播初始加载程序，进入设备并最终释放有效负载。有效负载通常是后门。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688206204450.png "1672687796121346.png")

IcedID僵尸网络恶意软件感染链

**通过劫持搜索的广告结果发起攻击**

用户会通过在Google上输入搜索词来搜索应用程序，在这个特定的示例中，用户想要下载AnyDesk应用程序，并在Google搜索栏上输入搜索词“AnyDesk”。被劫持的AnyDesk应用程序的广告会导致恶意网站显示在有机搜索结果上方。

IcedID攻击者滥用合法的Keitaro交通方向系统(TDS)来过滤研究员和沙盒流量，随后受害者被重定向到恶意网站。

一旦用户选择了“下载”按钮，它就会下载用户系统中ZIP文件中的恶意Microsoft软件安装程序（MSI）或Windows安装程序文件。

![3.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688207115502.png "1672687813165010.png")

![3.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688208946704.png "1672687826194650.png")

IcedID僵尸网络恶意广告感染链

**新的IcedID僵尸网络加载程序**

在这个攻击活动中，加载程序通过MSI文件被释放，这并不是IcedID的常规操作。

安装程序会释放几个文件，并通过rundll32.exe调用“init”导出函数，然后执行恶意加载程序例程。

这个“加载程序”DLL具有以下特征:

开发者使用了一个合法的DLL，并在最后一个序数处使用“init”导出函数名将一个合法函数替换为恶意加载程序函数；

IcedID加载程序中每个合法导出函数的第一个字符都替换为字母“h”；

对恶意函数的引用是一个经过修复的合法函数；

生成的恶意文件几乎与合法版本完全相同。这对机器学习(ML)检测解决方案来说是一个挑战。

从表面上看，恶意的IcedID和合法的sqlite3.dll文件几乎完全相同。下图显示了使用由安全研究员Karsten Hahn开发的PortEx Analyzer工具对这些文件进行的并排比较。该工具允许我们快速地可视化可移植可执行(PE)文件的结构。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688209616444.png "1672687955173697.png")

恶意IcedID(左)和合法PE(右)文件的可视化表示(使用Karsten Hahn的PortEx Analyzer工具)

因此，我们假设这是针对两种类型的恶意软件检测技术的攻击：

机器学习检测引擎；

白名单系统；

**充当IcedID加载程序的篡改DLL文件**

我们已经观察到，一些被修改为充当IcedID加载程序的文件是众所周知且广泛使用的库。

已被修改为IcedID加载程序的文件如下所示：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688210195560.png "1672687972924241.png")

在sqlite3.dll中，我们观察到在序号270处的函数“sqlite3\_win32\_write\_debug”已被IcedID加载程序中的恶意“init”函数替换。

上面列出的修改后的DLL文件就是这种情况，最后一个序号的导出函数被恶意的“init”函数替换。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688211588007.png "1672687988132268.png")

IcedID修改（左）和正常（右）文件的比较，其中前者在最后一个序号的导出函数被恶意的“init”函数替换

进一步调查表明，该文件的结构是相同的。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688212201618.png "1672688005125079.png")

IcedID修改文件和普通文件的比较，其中两个文件显示相同的结构

**执行**

“MsiExec.exe”执行（父进程）(MITRE ID T1218.007 - System Binary Proxy Execution: msiexec)；

生成“rundll32.exe” (MITRE ID T1218.011 - System Binary Proxy Execution: rundll32.exe)；

“rundll32.exe”通过 “zzzzInvokeManagedCustomActionOutOfProc” (MITRE ID T1218.011 - System Binary Proxy Execution: rundll32.exe)运行自定义操作“Z3z1Z”；

自定义操作生成第二个“rundll32.exe”以运行带有“init”导出函数 (MITRE IDs T1027.009 - Embedded Payloads and T1218.011 - System Binary Proxy Execution: rundll32.exe)的IcedID加载程序 “MSI3480c3c1.msi”。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688213928019.png "1672688020127951.png")

IcedID加载程序执行链

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688214198076.png "1672688034716371.png")

MSI自定义操作

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672688214194852.png "1672688049191556.png")

包含自定义操作的MSI结构

**总结**

IcedID是一个值得注意的恶意软件家族，能够传播其他有效负载，包括Cobalt Strike和其他恶意软件。IcedID使攻击者能够执行具有高度影响力的后续攻击，从而导致整个系统被破坏，例如窃取数据和使用勒索攻击瘫痪整个系统。恶意广告和规避加载程序的使用都在提醒我们部署分层安全解决方案的重要性，包括自定义沙箱、预测性机器学习、行为监控以及文件和网络声誉检测功能。终端用户还可以考虑使用广告拦截器来阻止恶意攻击。

本文翻译自：https://www.trendmicro.com/en\_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4fWbC95b)

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

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

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

[查看更多](https://www.4hou.com/member/aOZG)

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
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4...