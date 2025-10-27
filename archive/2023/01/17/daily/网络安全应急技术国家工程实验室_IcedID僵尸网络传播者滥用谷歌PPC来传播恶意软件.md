---
title: IcedID僵尸网络传播者滥用谷歌PPC来传播恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533904&idx=3&sn=62eb97bcec6b2a8b4a8750293456e055&chksm=fa93f391cde47a8703e8cb8f11f5ba634e918ce06710bd2e8b414452badf6bd2f9c534cc87e0&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-01-17
fetch_date: 2025-10-04T04:04:30.994239
---

# IcedID僵尸网络传播者滥用谷歌PPC来传播恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nOBekQia4yfTqJVf9EMP3CBluS2e5kZY2PATWGNiaZ9wiaYwZY0znedIq8c7eW4gib3GpzVwpxwXSLnA/0?wx_fmt=jpeg)

# IcedID僵尸网络传播者滥用谷歌PPC来传播恶意软件

网络安全应急技术国家工程中心

我们分析了IcedID僵尸网络的最新变化，该活动滥用谷歌点击付费(PPC)广告，通过恶意广告攻击传播IcedID。IcedID 是最早在 2017 年被披露的模块化银行木马，也是近年来最流行的恶意软件家族之一。IcedID 主要针对金融行业发起攻击，还会充当其他恶意软件家族（如 Vatet、Egregor、REvil）的 Dropper。

在密切跟踪IcedID僵尸网络的活动后，我们发现它的传播方法发生了一些重大变化。自2022年12月以来，我们观察到谷歌点击付费(PPC)广告被攻击者滥用，通过恶意广告攻击传播IcedID。趋势科技已将检测到的IcedID变体命名为TrojanSpy.Win64.ICEDID.SMYXCLGZ。

像谷歌广告这样的广告平台，其目的是使企业能够向目标受众展示广告，以提高流量和增加销售。恶意软件发布者滥用同样的功能，使用一种被称为恶意广告的技术，其中选择的关键字被劫持，显示恶意广告，诱使毫无戒心的搜索引擎用户下载恶意软件。

在我们的调查中，攻击者使用恶意广告通过合法组织和知名应用程序的克隆网页传播IcedID恶意软件。最近，美国联邦调查局(FBI)发布了一份关于网络犯罪分子如何滥用搜索引擎广告服务来伪装成合法网站，并通过一些经济诱惑将用户引向恶意网站。

本文介绍了IcedID僵尸网络的最新传播方法和它使用的新加载程序的技术细节。

# **技术分析**

有机搜索结果是由Google PageRank算法生成的，而谷歌广告出现在有机搜索结果的上方、旁边、下方或更突出的位置。当这些广告被攻击者通过恶意广告劫持时，它们可以将用户引导到恶意网站。

# **劫持搜索结果的关键词**

在调查中，我们发现IcedID传播者劫持了这些品牌和应用程序用来显示广告的关键词：

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nOBekQia4yfTqJVf9EMP3CBenkCNeoZWSS5DELqF7kJLmJRk0KHVo4MVs2Cp77my2gWo8agpPVbEQ/640?wx_fmt=jpeg)

这些恶意网站看起来就像合法网站一样。下图显示了一个看起来合法的恶意Slack网页，被IcedID传播者用来引诱受害者下载恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayy5yEQAFyIez80haHFTUM0dT2LmZpTk2aCxjkD6ohYRlVojMYDMcNnFA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

一个被IcedID传播者使用的看似合法的恶意Slack网页

# **感染链**

整个感染流程包括传播初始加载程序，进入设备并最终释放有效负载。有效负载通常是后门。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyiaFcW91WdGB1nwRNdbnqq8cvnrz4BtNLFcOoAQjM5Tm4ibBCW5UaJrvQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

IcedID僵尸网络恶意软件感染链

# **通过劫持搜索的广告结果发起攻击**

用户会通过在Google上输入搜索词来搜索应用程序，在这个特定的示例中，用户想要下载AnyDesk应用程序，并在Google搜索栏上输入搜索词“AnyDesk”。被劫持的AnyDesk应用程序的广告会导致恶意网站显示在有机搜索结果上方。

IcedID攻击者滥用合法的Keitaro交通方向系统(TDS)来过滤研究员和沙盒流量，随后受害者被重定向到恶意网站。

一旦用户选择了“下载”按钮，它就会下载用户系统中ZIP文件中的恶意Microsoft软件安装程序（MSI）或Windows安装程序文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyU4QezkL0XzUiaiccWfuCYr7QYjBumlj1VgulicjTWUaYG2wN7WzFvMOVA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyKctLOeeomgNvkiadeu1KaWMxVAt5JcJj1ibkmqlckklJc4ITqokf1rqw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

IcedID僵尸网络恶意广告感染链

# **新的IcedID僵尸网络加载程序**

在这个攻击活动中，加载程序通过MSI文件被释放，这并不是IcedID的常规操作。

安装程序会释放几个文件，并通过rundll32.exe调用“init”导出函数，然后执行恶意加载程序例程。

这个“加载程序”DLL具有以下特征:

开发者使用了一个合法的DLL，并在最后一个序数处使用“init”导出函数名将一个合法函数替换为恶意加载程序函数；

IcedID加载程序中每个合法导出函数的第一个字符都替换为字母“h”；

对恶意函数的引用是一个经过修复的合法函数；

生成的恶意文件几乎与合法版本完全相同。这对机器学习(ML)检测解决方案来说是一个挑战。

从表面上看，恶意的IcedID和合法的sqlite3.dll文件几乎完全相同。下图显示了使用由安全研究员Karsten Hahn开发的PortEx Analyzer工具对这些文件进行的并排比较。该工具允许我们快速地可视化可移植可执行(PE)文件的结构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyOQhF87ILVuxtGhD75N1dfksbfFzDick25PHQ4ia5gkJdLrmC18icdPPFg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

恶意IcedID(左)和合法PE(右)文件的可视化表示(使用Karsten Hahn的PortEx Analyzer工具)

因此，我们假设这是针对两种类型的恶意软件检测技术的攻击：

机器学习检测引擎；

白名单系统；

# **充当IcedID加载程序的篡改DLL文件**

我们已经观察到，一些被修改为充当IcedID加载程序的文件是众所周知且广泛使用的库。

已被修改为IcedID加载程序的文件如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayy68EYAyn54uLXhZjjKJ2ZuZjqkXIn8z4tnglzIvKtjdW1N6WtUHFheA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在sqlite3.dll中，我们观察到在序号270处的函数“sqlite3\_win32\_write\_debug”已被IcedID加载程序中的恶意“init”函数替换。

上面列出的修改后的DLL文件就是这种情况，最后一个序号的导出函数被恶意的“init”函数替换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyVOuOyxq1gRlq0kLpLGYsLJbXa8fOW84aQ35NuBIj1tTkJrJJaict6ug/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

IcedID修改（左）和正常（右）文件的比较，其中前者在最后一个序号的导出函数被恶意的“init”函数替换

进一步调查表明，该文件的结构是相同的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayy0I9NTeKgCNyVeDpicK2G11iaMm8zCFWEnLP1TUFpic9XnFFElnhBYeicdA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

IcedID修改文件和普通文件的比较，其中两个文件显示相同的结构

# **执行**

“MsiExec.exe”执行（父进程）(MITRE ID T1218.007 - System Binary Proxy Execution: msiexec)；

生成“rundll32.exe” (MITRE ID T1218.011 - System Binary Proxy Execution: rundll32.exe)；

“rundll32.exe”通过 “zzzzInvokeManagedCustomActionOutOfProc” (MITRE ID T1218.011 - System Binary Proxy Execution: rundll32.exe)运行自定义操作“Z3z1Z”；

自定义操作生成第二个“rundll32.exe”以运行带有“init”导出函数 (MITRE IDs T1027.009 - Embedded Payloads and T1218.011 - System Binary Proxy Execution: rundll32.exe)的IcedID加载程序 “MSI3480c3c1.msi”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyA59bCianibJAtQ17x7ib4Q5ic5eC3SqT5419kBchzuUTff7e1FQv1M6Azw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

IcedID加载程序执行链

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyvGnI9TvNmbDlseuVDqhN9hAUj43FHS5BEVZ7eYwWYR6We7nffqdqqw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

MSI自定义操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibOjeta899JiaUL8ibzvr4ayyFSichAcUX6HagIkRlfjY700luZVQxvzLJfAGAO0Af5icdTnWwLDN20QA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

包含自定义操作的MSI结构

# **总结**

IcedID是一个值得注意的恶意软件家族，能够传播其他有效负载，包括Cobalt Strike和其他恶意软件。IcedID使攻击者能够执行具有高度影响力的后续攻击，从而导致整个系统被破坏，例如窃取数据和使用勒索攻击瘫痪整个系统。恶意广告和规避加载程序的使用都在提醒我们部署分层安全解决方案的重要性，包括自定义沙箱、预测性机器学习、行为监控以及文件和网络声誉检测功能。终端用户还可以考虑使用广告拦截器来阻止恶意攻击。

**参考及来源：**

https://www.trendmicro.com/en\_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过