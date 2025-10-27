---
title: ATT&CK 2024更新内容简介
url: https://mp.weixin.qq.com/s?__biz=MzUzMDk0MjY2NQ==&mid=2247484263&idx=1&sn=35e7bbdbe5e9a7a5fc253e0c563743bc&chksm=fa4b5cc1cd3cd5d7c3f2bc58cc7ba262a7272f13f706311fe32c1fedf745987d8efede2aa9ca&scene=58&subscene=0#rd
source: 安全喷子
date: 2024-12-25
fetch_date: 2025-10-06T19:38:36.889928
---

# ATT&CK 2024更新内容简介

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcbZn5niaicVw2XrtNnLxr31ubaR3U7Y9hcheH51KbgbtUY7e9kUcHYibtA/0?wx_fmt=jpeg)

# ATT&CK 2024更新内容简介

原创

程度

安全喷子

引言

主要更新内容

ATT&CK继续延续每年更新两个大版本的状态，今年迎来的ATT&CK 的第16个版本。笔者跟踪了这一年的ATT&CK的进展以及刚结束的ATT&CKcon 5.0中各个内容。提炼了主要的更新内容和主要的更新方向。

ATT&CK更新内容

主要更新内容

最新进展(自ATT&CK con4.0以来，ATT&CK v14)：新增44个攻击技术/子技术；新增20个攻击组织；新增13个攻击行动；新增55个攻击软件。更新了267个攻击技术/子技术；更新了96个攻击组织；更新了7个攻击行动；更新了204个攻击软件。每年新增的内容并不是很多，只是两位数的增长。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcEFPZGNx6K3cU1xFSbt68R7eYSO9rrR8xM1Fiag5w2K1OdFEI9viaAaGA/640?wx_fmt=png&from=appmsg)

图1 ATT&CK V16更新内容

1、主要技术范围扩展

* 增加了语音钓鱼等新型攻击方式
* 加入了人工智能相关内容
* 增加了金融盗窃相关内容

（1）语音钓鱼（T1566.004）：攻击者可能会使用语音通信来最终控制访问受害者系统。这种攻击方式与其他形式的鱼叉式网络钓鱼不同，通过电话或其他形式的语音通信来操纵用户提供对系统的访问，例如冒充可信来源（模仿）或为接听者制造紧迫感或警报。在这种情况下，攻击者使用电话来获取受害者的敏感信息。这些方式被称为语音网络钓鱼（或“vishing”），可以由攻击者、雇佣的呼叫中心手动执行，甚至可以通过自动呼叫自动执行。语音网络钓鱼者可能会伪造他们的电话号码，同时冒充受信任的实体，例如业务合作伙伴或技术支持人员。

（2）二维码钓鱼（T1598.003）：攻击者还可能以二维码（QR code）（也称为“quishing”）的形式发送恶意链接。这些链接可能会将受害者引导至凭证网络钓鱼页面。通过使用QR码，URL可能不会在电子邮件中展示，因此可能不会被大多数自动电子邮件安全扫描检测到。这些QR码可能会被用户的移动设备扫描或直接传送到用户的移动设备（即网络钓鱼），这在一些相关方面可能不太安全。例如，由于移动设备尺寸较小，移动用户可能无法注意到真实网站和凭证收集网站之间的细微差别。

（3）人工智能能力（T1588.007）：攻击者可能会获得生成式人工智能工具，例如大型语言模型（LLM），以在渗透过程中帮助使用各种技术。这些工具可用于建议、增强和使能各种恶意任务，包括进行侦察、创建基本脚本、协助社会工程，甚至开发有效负载。

例如，通过利用公开的LLM，攻击者实质上是使用该工具外包或者自动化一些任务。使用人工智能，攻击者可以用各种书面语言起草和生成内容，用于网络钓鱼/网络钓鱼信息活动。也可能会进一步使用漏洞或其他支持开发能力的攻击性研究。人工智能工具还可以通过生成、改造或以其他方式增强（例如模糊文件或信息）恶意脚本和有效负载来自动化攻击任务。

（4）金融盗窃（T1657）：攻击者可能会通过勒索、社会工程、技术盗窃或其他旨在获取经济利益的方法从目标窃取货币。金融盗窃是多种流行活动类型的最终目标，包括勒索软件勒索、商业电子邮件泄露(BEC)和欺诈、“杀猪盘”、银行黑客攻击和利用加密货币网络。

攻击者可能会破坏账户以进行未经授权的资金转移。在商业电子邮件泄露或电子邮件欺诈的情况下，攻击者可能会利用冒充可信实体的方式。一旦社会工程成功，受害者可能会被欺骗，将钱汇入攻击者控制的金融账户。

由于金融盗窃可能对业务产生巨大影响，对手可能会滥用金融盗窃的可能性并寻求金钱利益，以转移对其真正目标（例如数据破坏和业务中断）的注意力。

2、检测增强功能

更新了数百种技术和子技术；描述检测细节的来龙去脉；以更直接可用的格式开发了100多种分析能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcSQJqWBDvvc4x7xvUcpWBUQvesAUKwFumbQfj0BWUKpayZVhxiaU5qgA/640?wx_fmt=png&from=appmsg)

图2  检测能力增强

（1）工控领域（ICS）增加了资产（Assets）的分类

资产代表工业控制系统环境中常见的设备和系统。每个资产对象都包括技术关系的映射，这些技术关系表示攻击者可能根据设备的能力和功能针对设备的操作。

这些设备通常具有不同的名称或行业特定术语。为了更准确地跟踪这些差异，使用“相关资产”字段，该字段根据相似的功能、架构位置和相似对手技术的暴露情况将这些术语关联起来。每个相关资产都包括名称、可选的扇区标识符以及为资产页面定义提供细微差别的描述。

尽管资产最初在ATT&CK中表示为平台字段，但资产与平台明显有区别。平台通常描述操作系统或应用程序（即Microsoft Windows），而资产代表设备，包括硬件、软件、架构和预期功能的考虑因素。资产可以利用平台来描述设备的常见操作系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcTRjzXdicbSSgNK7WB5uP9QqYJcdU4COEbq26TaCv7jqgDlY0OelUX0Q/640?wx_fmt=png&from=appmsg)

图3 工控资产的列表

（2）移动平台(Mobile)的两个主要更新内容

（i）结构化检测（Structured detections）

图中展示了一个检测表格示例，包含ID、数据源、数据组件和检测内容等字段具体展示了两个检测条目：

* lDS0041:关于应用程序审核(Application Vetting)的权限请求检测
* lDS0042:关于用户界面(User Interface)的权限请求和系统设置检测

这些检测需要设备管理员权限的请求和管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcKicWb3emGcwW8dOhdreMERdutUpKBcDrB3hYYFsGQfhAa79iakEyya8A/640?wx_fmt=png&from=appmsg)

图4 移动平台的检测

（ii）跨平台攻击者

图中展示了一个具体案例C0033，这是一个PROMETHIUM组织的攻击活动，他们使用StrongPity工具针对Android用户进行攻击，特别之处在于这是PROMETHIUM组织首次被公开记录的移动平台攻击活动（该组织此前主要针对Windows系统）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zc19xhoiaiaHmiaF12VJxtGkhtmk4trzvU3BxLib5M3Cy7AcJ9EmOpmocMpg/640?wx_fmt=png&from=appmsg)

图5 C0033介绍

Enterprise 框架内容更新

1、云平台相关的重要更新

考虑到身份即服务平台不止一个，还有Okta、Ping Identity、JumpCloud、Onelogin等等。Office365跟Google Workspace重复度较高。重组了云平台的分类结构，包括：

* Infrastructure as a Service (基础设施即服务)
* Software as a Service (软件即服务)
* Identity Provider (身份提供商)
* Office Suite (办公套件)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcykf2yo2u7lQvxfbCx3qosmyI4zIyIz8PGOXphDOeYJjN1Hj2Oeuekg/640?wx_fmt=png&from=appmsg)

图6 云平台分类更新

2、添加了事件触发执行的新子技术：设备文件管理（Udev Rules T1546.017）

攻击者可以通过执行使用udev规则触发的恶意内容来保持持久性。Udev是Linux内核设备管理器，它动态管理设备节点，处理对/dev目录中伪设备文件的访问，并响应硬件事件，例如插入或移除硬盘或键盘等外部设备时。

攻击者可能通过在udev规则文件中添加或修改规则来滥用udev子系统来执行恶意内容。例如，攻击者可以配置规则，以便在每次应用程序访问伪设备文件（例如/dev/random）时执行其二进制文件。尽管udev仅限于运行短任务，并且受到systemd-udevd沙箱的限制（阻止网络和文件系统访问），但攻击者可以使用操作符下的脚本命令来分离并在后台运行恶意内容的进程，以绕过这些控制。

3、资源劫持技术

* Compute Hijacking （利用计算资源来挖掘加密货币）
* Bandwidth Hijacking （劫持代理网络出售网络带宽）
* SMS Pumping （产生短信流量以获取利润）
* Cloud Service Hijacking （滥用基于云的消息服务发送大量垃圾邮件）

威胁情报内容更新

1、威胁情报的整体目标

* 及时捕获相关的威胁态势
* 改进对其他地区和网络犯罪活动者的覆盖
* 利用Campaign对象更准确地反映活动随时间的变化

2、威胁组织(Group)优先事项

* APT组织：

   （1）持续捕获新兴的国家支持的威胁

   （2）确保保持最新的信息

* 网络犯罪组织：

* （1）继续扩展对犯罪实体的表示
* （2）努力区分组织、软件和活动

3、攻击软件(Software)优先事项

* 恶意软件：确保捕获重要且独特的恶意软件
* 勒索软件：提高对勒索软件家族的覆盖
* 工具和实用程序：捕获入侵中使用的非恶意工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcmejRrpjictbBianEbezdHDoG6g9LewGGeIicKRZnKJsvAMYK6nK3Aic7Qw/640?wx_fmt=png&from=appmsg)

图7 攻击软件的优先事项

4、攻击活动(Campaign)优先事项

* 目前在ATT&CK中Campaign对象使用不足，将进行改变
* 解决长期运行的组织看似使用"所有技术"的问题
* 网络犯罪行动中多个行为者之间的关系模糊，使Campaign表示比明确的组织更适用

未来发展方向：改进数据模型；增强活动分类和表示；完善对新兴威胁的覆盖；加强对非传统区域和威胁的支持。

防御内容更新

1、防御增强

* 新的和更新的缓解措施
* 事件ID到数据源的映射
* 将伪代码转换为SPL分析规则

2、分析能力提升

* 目前有360个分析规则
* 计划填补缺失的战术分析
* 符合Sigma标准
* 增加多事件分析能力

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcpmNHA50raicqTcAukKicp1ibqn6pdsFo1xEyb5eSgu5ppNbL3h0Uaqopw/640?wx_fmt=png&from=appmsg)

图8 分析能力战术分类

3、数据源重构

* 重新定义数据源概念
* 细化实际日志源分类
* 采用"通用源:具体日志通道"的格式
* 涵盖多种平台和服务的日志

分行业攻击分析

Red Canary公司制作的一份关于行业与网络安全威胁关系的分析报告。其核心观点包括以下几个方面：

* 主要论点：一个组织所属的行业并不是决定其面临网络威胁类型的关键因素。数据显示，不同行业面临的攻击技术和威胁类型存在很大的相似性。

* 数据支持：

* （1）报告分析了2023年和2024年初的威胁检测数据
* （2）使用NAICS(北美行业分类系统)对不同行业进行分类
* （3）通过Jaccard相似度指数等方法比较不同行业间的威胁技术异同

* 关键发现：

* （1）大多数攻击者是机会主义的，他们更关注可利用的漏洞而非特定行业
* （2） 一些技术(如PowerShell、Cloud Accounts等)在所有行业中都很普遍
* （3）行业差异主要体现在其IT基础设施和配置上，而非针对性攻击手段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U3rZGBkRogrVtkQGN4lqIRyRvxicr55zcXkdwdVujrXEsGibYQkzd03FLL4hPXRoibibEj8Nnk5ZyAE0StLyxM0Upg/640?wx_fmt=png&from=appmsg)图9  跨部门攻击技术滥用（前10名）

* 特定行业攻击特点：

* （1）教育行业：约55%的检测是电子邮件相关威胁，主要是邮件转发（T1114.003）和邮件隐藏（T1564.008），这与其开放性网络特征相关
* （2）制造业：可移动媒体攻击（T1091）较多，可能与其特殊的设备需求有关
* （3）医疗行业：医疗环境中Linux系统的使用比预期要普遍，检测到大量Cron (T1053.003)和Unix Shell     (T1059.004)的使用，医疗机构的IT架构比表面看起来要复杂得多
* （4）金融行业：更严格的安全控制会推动攻击者采用更复杂和隐蔽的技术。主要侧重于独特攻击技术包括：HTML Smuggling（T1027.006），一种高级的文件传递技术，能够绕过传统的网关扫描；Distributed Component Object Model（分布式组件对象模型T1559.001），利用合法的Windows系统组件进行攻击，这些技术在其他行业的前10名攻击技术中较少出现。

报告也揭示了一些有趣的行业安全模式：

* 信息行业模式:

* （1）特点是拥有大量大型客户，且检测到的威胁数量也很多
* （2）显示出规模与威胁检测量之间的正相关性
* （3）这可能反映了大型科技公司拥有更复杂的IT环境和更多的攻击面，同时也可能拥有更先进的检测能力

* 零售行业情况:

* （1）尽管没有太多大客户，但检测到的威胁数量却很高
* （2）这种不符合一般规律的现象值得关注
* （3）可能反映了该行业特殊的风险因素，如供应链复杂性、系统互联性高等特点

* 金融行业特征:

* （1）虽然有很多大客户，但威胁检测量相对较低
* （2）这种现象的主要原因是严格的合规要求和监管控制
* （3）表明强有力的监管和合规要求确实能有效降低安全风险

整体分析表明，行业特征、公司规模、监管环境等因素共同影响着威胁检测模式。特别值得注意的是，严格的监管似乎确实能有效降低安全风险，而不仅仅是形式上的要求。这为其他行业的安全治理提供了有益的参考。

总结

近年的ATT&CK更新可以看出来更加贴近实际情况与时俱进，更新的内容更加符合行业的趋势。比如二维码和语音钓鱼的情况在国内也很普遍，最核心的Enterprise框架云安全部分也做了很大的调整，工控框架增加了资产内容，移动框架增了一些检测能力。为了让ATT&CK看起来不那么“全面”，后续要更新攻击活动（Campaign）的内容，防御内容这次更新的内容非常丰富，以后的分析思路都可以参考官方的思路。

按照各个行业的ATT&CK的攻击思路可以看出来，相同的地方大于不同的地方，攻击者大部分都是机会主义者，行业攻击不同的地方的分析也很有意思。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/U3rZGBkRogoic5KAloGC6icVFCyxvxMjSWCDMlgwQNoDaZXNrmpdgliaq0aFibojHw2tx7zqzRHgC5Q2iaDXwXSEgZw/0?wx_fmt=png)

安全喷子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/U3rZGBkRogoic5KAloGC6icVFCyxvxMjSWCDMlgwQNoDaZXNrmpdgliaq0aFibojHw2tx7zqzRHgC5Q2iaDXwXSEgZw/0?wx_fmt=png)

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