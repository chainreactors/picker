---
title: 能信安：病毒和恶意代码通告
url: https://mp.weixin.qq.com/s/k0P7NuHQMEXPV1GXcbqgkA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:30:09.941326
---

# 能信安：病毒和恶意代码通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7kDwzldia4nFPHbMsphOncst5Iqk3756PicFwCnQTDSBzWVvJk74W0uCf4mtBqQWiaG2SicSjU61J860pMgFzbtCpmnsG9ayB8yCC7wyxS7paQA/0?wx_fmt=jpeg)

# 能信安：病毒和恶意代码通告

能信安资讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![企业微信截图_17738185598290.png](https://mmbiz.qpic.cn/mmbiz_png/7kDwzldia4nGJb0h3uvjnicSAm8HYg5yNfiajx5jOficQziccQs9cuaPkC7BjIBrm1LLPHWKbXtsI44eib1EypiaiaHwIpiakF7212MyzFn4AChqEWK4/640?wx_fmt=png&from=appmsg)

网络安全预警通报

病毒和恶意代码通告 2026年4月17日

**0****1**

**“BeatBanker”木马程序**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7kDwzldia4nH61ic1yQoDHHL13HuHyvpuGElLvdiavyE4XicndQYjGY33xfKPR9L9RiazusxMqHJevqvX9DlfNT5ymuKjg4niaCStDx6iciclmKmmxU/640?wx_fmt=png&from=appmsg)

**描述：**

2026年3月，针对巴西用户的新型网络钓鱼活动曝光，该活动利用特洛伊化的“Red Alert”火箭预警应用及伪造的社会保障（INSS）服务应用，传播名为BeatBanker的复合型恶意软件。BeatBanker集成了加密货币挖矿模块与银行木马功能，代表了移动威胁领域的一次显著演进。

本文深入剖析了BeatBanker的感染链条、持久化机制及多阶段载荷投递策略。研究发现，该恶意软件通过播放静音音频维持后台进程、利用设备状态（电量、温度、用户活跃度）动态调整挖矿行为以规避检测，并通过覆盖屏幕（Overlay Attacks）技术劫持Binance、Trust Wallet等主流加密应用的交易流程。

文章进一步探讨了此类利用公共安全焦虑与社会工程学相结合的攻击范式，并提出了基于行为分析与运行时监控的防御架构。反网络钓鱼技术专家芦笛指出，面对这种伪装成公共服务工具的深层渗透，传统的静态特征检测已失效，必须构建基于上下文感知的动态防御体系。本文最后提供了针对此类覆盖攻击与异常资源占用的检测代码示例，旨在为移动安全治理提供理论支撑与技术路径。

**安全建议：**

1.安装防病毒软件并及时更新漏洞库，定期实施全盘查杀。

2.避免打开来历不明的邮件、链接和网址附件等，尽量不要在非官方渠道下载非正版的应用软件，发现文件类型与图标不相符时应先使用安全软件对文件进行查杀；

3.定期检测系统漏洞并且及时进行补丁修复。

4.使用强密码，并定期更改密码，以防御黑客进行的暴破攻击。

**0****2**

**“Slopoly ”恶意软件**

![](https://mmbiz.qpic.cn/mmbiz_png/7kDwzldia4nFXom0tEjIqch4E81kyMNO18aGjpJ4OF3TniaOFtibRIMBko5FhL4DHqTVQYu0icEb46TkgdQkrOsFKgx8iaich4ibyjKtWhcGsmX7X8/640?wx_fmt=png&from=appmsg)

**描述：**

网络安全研究人员披露了一款疑似由人工智能（AI）生成的恶意软件的详细信息，该软件代号为 Slopoly，由以经济利益为动机的威胁行为者 Hive0163 使用。

IBM X-Force 研究员 Golo Mühr 在提前提供给 The Hacker News 的报告中表示：“尽管 Slopoly 这类 AI 生成的恶意软件目前仍相对普通，但它表明威胁行为者可以多么轻松地利用 AI 来开发新的恶意软件框架，所需时间仅为过去的一小部分。”

Hive0163 的活动以大规模数据窃取和勒索软件勒索为驱动。该电子犯罪团伙主要与一系列恶意工具相关联，包括 NodeSnake、Interlock RAT、JunkFiction loader 和 Interlock ransomware。

在该公司2026 年初观察到的一起勒索软件攻击中，威胁行为者在漏洞利用后阶段部署了 Slopoly，以便在受感染服务器上维持超过一周的持久访问权限。

Slopoly 的发现可追溯至一个很可能通过构建器部署的 PowerShell 脚本，该脚本还通过名为 “Runtime Broker” 的计划任务建立了持久访问权限。

有迹象表明，该恶意软件是在一个尚未确定的大语言模型（LLM）的帮助下开发的。这些迹象包括存在大量注释、日志记录、错误处理和命名准确的变量。注释还将该脚本描述为 “Polymorphic C2 Persistence Client”，表明它是一个命令与控制（C2）框架的一部分。

Mühr 指出：“不过，该脚本不具备任何高级技术，几乎不能被视为多态的，因为它无法在执行过程中修改自身代码。但构建器可能会生成具有不同随机配置值和函数名的新客户端，这在恶意软件构建器中是标准做法。”

该PowerShell 脚本充当一个功能完整的后门，每 30 秒向 C2 服务器发送一次包含系统信息的心跳消息，每 50 秒轮询一次新命令，通过 “cmd.exe” 执行该命令，并将结果传回服务器。目前尚不清楚在受感染网络上运行的命令的具体性质。

据称，此次攻击本身利用了ClickFix 社会工程策略，诱骗受害者运行一个 PowerShell 命令，该命令随后下载了 NodeSnake—— 一款被归因于 Hive0163 的已知恶意软件。

为第一阶段组件，NodeSnake 旨在运行 shell 命令、建立持久访问权限，并检索和启动一个更广泛的恶意软件框架，即 Interlock RAT。

Hive0163 有使用 ClickFix 和恶意广告进行初始访问的记录。该威胁行为者用来建立立足点的另一种方法是依赖初始访问代理，例如 TA569（又名 SocGholish）和 TAG-124（又名 KongTuke 和 LandUpdate808）。

该框架在PowerShell、PHP、C/C++、Java 和 JavaScript 中有多种实现，以同时支持 Windows 和 Linux。与 NodeSnake 一样，它也与远程服务器通信以获取命令，这些命令允许它启动 SOCKS5 代理隧道、在受感染机器上生成反向 shell，并交付更多载荷，例如 Interlock ransomware 和 Slopoly。

Slopoly 的出现进一步扩大了 AI 辅助恶意软件的名单，该名单还包括 VoidLink 和 PromptSpy，凸显了不良行为者如何利用该技术加速恶意软件开发并扩大其活动规模。

IBM X-Force 表示：“从技术角度来看，AI 生成的恶意软件的引入并不构成新的或复杂的威胁。它通过减少操作者开发和执行攻击所需的时间，极大地增强了威胁行为者的能力。”

**安全建议：**

1.安装防病毒软件并及时更新漏洞库，定期实施全盘查杀。

2.避免打开来历不明的邮件、链接和网址附件等，尽量不要在非官方渠道下载非正版的应用软件，发现文件类型与图标不相符时应先使用安全软件对文件进行查杀；

3.定期检测系统漏洞并且及时进行补丁修复。

4.使用强密码，并定期更改密码，以防御黑客进行的暴破攻击。

▼

**能信安——新一代网络安全领先企业！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7EgONBwTicyukySMu6FXUXWDAkWwribspgqezQeNT68WySw9CozfOicqxGnISiaB0GFYXp3qXHmpmHzays0SBTSibQ/640?wx_fmt=jpeg "bde0f1f294be1789aa279651ce5123d5.jpg")

**公司简介**

深圳市能信安科技股份有限公司，是以安全、移动、泛在和大数据为主要方向的专业技术公司，致力于移动互联安全、车联网安全、物联网安全、大数据安全和人工智能安全技术。

公司是公安部、工信部网络安全技术支撑单位，国家网络安全威胁和漏洞信息共享平台技术支撑单位，是深圳大运会、党的十八大、2020年全国两会、2021年联合国生物多样性大会网络安全技术支撑单位。公司是国家级专精特新“小巨人”企业，中国移动安全十强企业，全国网络安全百强企业，具有良好的品牌影响力。

公司为中国新一代网络安全领先企业。在移动安全领域，公司可提供业界最先进、完整的技术、产品与解决方案，引领移动互联安全的技术潮流。主要产品及服务包括移动应用安全防火墙、无线安全检测及防御系统、移动应用安全检测及加固技术等。在数据安全领域，提供业界领先的数据安全治理、数据安全合格产品与服务。

公司依托于多年网络安全领域的技术经验及专业资质，向各类政府机关及企事业单位提供等级（分级）保护顾问咨询、关基保护顾问咨询、数据安全治理、密码改造顾问咨询、信息系统风险评估、安全体系建设咨询、修复加固服务、渗透测试服务、应急响应服务、安全运维保障服务。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7EgONBwTicwJbtXPMDMSMHxOK5ibqcf4XC5icFVAVsNF8fiaHuTFeRINsEs3tESvq6aNNTywQlVga3LibzRqNXoPiaA/0?wx_fmt=png)

能信安资讯

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7EgONBwTicwJbtXPMDMSMHxOK5ibqcf4XC5icFVAVsNF8fiaHuTFeRINsEs3tESvq6aNNTywQlVga3LibzRqNXoPiaA/0?wx_fmt=png)

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