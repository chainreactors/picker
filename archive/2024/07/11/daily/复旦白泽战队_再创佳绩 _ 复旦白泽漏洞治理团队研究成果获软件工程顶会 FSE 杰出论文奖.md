---
title: 再创佳绩 | 复旦白泽漏洞治理团队研究成果获软件工程顶会 FSE 杰出论文奖
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247490471&idx=1&sn=38e35f75e2df8edc5a0121c237c6f5d0&chksm=fdeb9fd9ca9c16cfcc1b23b909b88f9ffbddc46a130ea27a5d5df4feb56be9c6114e0e9b1a74&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2024-07-11
fetch_date: 2025-10-06T17:45:35.481698
---

# 再创佳绩 | 复旦白泽漏洞治理团队研究成果获软件工程顶会 FSE 杰出论文奖

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW87fx03Jws9or3gsOA26EFQBxOOdC6T6C5cI1LIPECDXJ3dOUP8fS99mTG0TV1BVafxddAKT5OCwzA/0?wx_fmt=jpeg)

# 再创佳绩 | 复旦白泽漏洞治理团队研究成果获软件工程顶会 FSE 杰出论文奖

原创

复旦白泽战队

复旦白泽战队

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBzpyarOEj25ibWIeNjN5icY8lP3xCuUnJkBZjgXS9Y7AFzYrYicxzsR6jA/640?wx_fmt=png&from=appmsg)

**1. Distinguished Paper Award**

**成果介绍**

2024年7月15日至19日，软件工程领域最具有影响力，历史最悠久的国际旗舰学术会议之一 FSE（CCF A类）将在巴西召开。复旦大学系统软件与安全实验室在移动安全领域的最新研究成果“Component Security Ten Years Later: An Empirical Study of Cross-Layer Threats in Real-World Mobile Applications”荣获**2024年度FSE杰出论文奖（ACM SIGSOFT Distinguished Paper Award）**。

   这是本团队在[2022年获得网络安全领域顶尖学术会议USENIX Security杰出论文奖](https://mp.weixin.qq.com/s?__biz=MzA4NDA0MjY2Mw==&mid=2650734587&idx=1&sn=e5c7086737cccd1229435bc8e1529821&scene=21#wechat_redirect)之后，再次获得的CCF A类国际顶尖学术会议杰出论文奖，也使得本团队成为了**国内首个跨界同时获得网络安全领域和软件工程领域顶级会议杰出论文荣誉的研究团队**。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBxKicALsRQ7ZWfb23SRCy2FHLNhYk6PvLxHz79bAad24X1sfrpBMKrUw/640?wx_fmt=png&from=appmsg)

安卓应用安全领域经过多年的深入研究和不断创新，已经积累了丰富的漏洞类型和成熟的解决方案。总体而言，现有研究主要集中在应用内敏感功能和数据暴露问题上。由于安卓应用主要使用内存安全语言Java作为开发语言，其内存安全问题往往被研究者所忽视。**本文首次从内存安全角度出发，研究攻击者对于安卓应用内存可用性和完整性的攻击方法，丰富了Java内存安全研究的内涵。**

    具体而言，开发者习惯性采用统一规范式的数据存储机制来管理不同来源的数据，使得低可信数据与敏感数据存储在一起。更糟糕的是，开发者在加载和使用这些内部存储的数据时，出于对操作系统应用隔离机制的信任，往往天然信任这些数据，缺少对加载数据大小和语义的检查。利用数据存储机制的管理缺陷，攻击者可以注入大量垃圾数据或篡改敏感数据。当应用程序运行时使用了这些数据，会导致安卓应用内存的可用性和完整性被破坏，从而间接操纵应用内部敏感功能。

    针对**现有安全解决方案难以细粒度的识别数据存储中数据来源**的局限性，本团队提出了一种数据存储感知的数据流分析方法，能够追踪数据存储中同一数据项的读取和写入，并识别滥用后果。通过对近1.5万个流行应用的实证研究，我们发现并验证了大量可实际利用的安全漏洞，能够造成如任意代码执行、点击劫持、UI诱导欺骗、持久性拒绝服务等严重安全后果。本研究在盲审期间得到了审稿人的一致认可：“**该研究不仅识别了新的安全风险，还为改进Android组件安全性提供了重要的缓解措施和技术方法，对提升移动应用的整体安全性具有重要意义。**”

***Q***

**移动安全研究已有十余年发展，如何在传统研究方向上实现“老树开新花”？**

***A***

**廉轲轲（博士生）：**

    刚开始确定这个研究课题时，我其实是持怀疑态度的，因为安卓应用组件安全已经是一个非常成熟的研究领域，容易想到的问题都被研究过了。因此，我们必须从非传统角度重新进行剖析。之所以选择Java内存安全角度，灵感源自我们在S&P 2022上发表的关于安卓系统服务内存资源耗尽的研究。通过分析可能的攻击手段并对大量流行应用进行逆向分析，我们发现了安卓应用中存在的数据存储管理机制缺陷。更进一步的，我们发现现有的安全检测方案在分析粒度上无法有效的应对数据存储读写操作，于是，我们针对性提出了数据存储感知的细粒度数据流分析方法。

    这项研究前后持续了将近两年的时间，中间遭受了数次拒稿，一度让我对这项工作的意义产生怀疑，但幸运的是，实验室的几位指导老师们始终认可对这项工作的价值，并给予了我很多鼓励和帮助，使我能够坚持到最终取得成果的这天。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBzpyarOEj25ibWIeNjN5icY8lP3xCuUnJkBZjgXS9Y7AFzYrYicxzsR6jA/640?wx_fmt=png&from=appmsg)

**2. 白泽长期关注移动安全**

过去十五年是移动互联网飞速发展的阶段，复旦白泽团队在这个过程中也不断发展，围绕移动安全领域取得了一系列研究成果。

    如下图展示，自2009年移动互联网浪潮开启，团队在杨珉老师的带领下布局安卓系统安全和隐私研究，带着“十年磨一剑”的坚定决心和顽强意志，埋头苦干，攻坚克难。2013年，棱镜门事件为中国移动互联网安全与隐私保护敲响警钟，也是这一年，团队首次在网络安全顶会CCS上发表2篇研究成果，突破了欧美高校和研究机构的垄断。随后几年，团队在移动安全领域实现多方面突破，在2020年实现网络安全领域Top-4顶尖学术会议大满贯并获得**CCS杰出论文提名奖**，到2022年成为**国内首个**荣获网络安全顶尖学术会议**USENIX Security杰出论文奖**荣誉的团队，并且在2024年荣获软件工程领域顶尖学术会议**FSE杰出论文奖**。如今，复旦白泽团队的研究成果数量已经在**全球****“**[**安全天梯排行榜**](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497022&idx=1&sn=3a8f02204a1521cdde2d90fe1a330da5&scene=21#wechat_redirect)**”中名列前茅**。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBx3V404IOX8wgMmIKR6TcZOHpiaGicUwHlKTCvNLibkODict1rlhzqtwcSg/640?wx_fmt=png&from=appmsg)

***Q***

**白泽团队近年来快速发展，取得了多项重大突破，您认为最关键的因素是什么？**

***A***

**杨珉教授：**

    我觉得最关键的主要有三个方面：

    首先是**研究方向的选择**。要坚持长期主义，选择难度高的方向，可以形成技术壁垒，同时要顺应技术和时代发展趋势，确保研究价值。当初我们团队选择移动安全作为转型方向就是基于这样的考量，如今我们在开源软件漏洞治理上的大量投入，也是考虑到其存在的技术难题和在国家安全层面的重要意义。

    其次是**技术的积累**。我们的社会在不断发展和进步，会给有准备的人提供机会，尽管窗口可能会很窄。能否抓住这些重大机会，取决于你在所选领域的积累。当初移动安全对我们虽然陌生，但我们在操作系统和编译技术领域的多年积累，为转型奠定了坚实基础。如今团队在无人驾驶安全，AI安全等方向取得的成果，也源自在相关领域的持续积累。

    最后是**学生的培养**。“人才”是第一资源，如何吸纳优秀学生和培养学生能力对于科研团队的发展至关重要。白泽CTF战队就是我们积极探索的学生培养方式之一，通过“以赛代练”，不仅帮助学生积累了实践经验，还获得多项国际和国内顶尖赛事的冠军，吸引了许多优秀的校内外学生加入实验室。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBzpyarOEj25ibWIeNjN5icY8lP3xCuUnJkBZjgXS9Y7AFzYrYicxzsR6jA/640?wx_fmt=png&from=appmsg)

**3. 新的征程：开源软件漏洞治理**

我国正积极推动信创产业发展，通过自主研发和国产化替代，实现关键核心技术的自主可控，保障国家信息安全和技术独立。**开源代码的广泛使用使得其安全性直接影响国家关键基础设施和系统的安全**。因此，提升开源代码漏洞治理能力不仅有助于预防潜在网络攻击，更能够强化技术自主控制力，推动科技的创新和可控发展。

当下开源软件漏洞治理**自动化程度低**，面临**关键信息缺失，依赖专家经验**等问题，导致漏洞治理不及时。大模型技术的兴起为传统漏洞治理带来了新的机遇。**白泽漏洞治理团队**聚焦开源软件安全，致力于通过一系列关键技术研发解决开源软件漏洞治理生命周期中的痛点问题。

    目前，团队围绕**大模型赋能传统安全分析技术**和**安全知识增强大模型**两个角度，正在积极开展大模型与传统安全分析技术相结合的研究。一方面，团队利用大模型能力，通过大模型安全能力测量研究，大模型辅助程序分析和模糊测试等研究，重塑安全技术底座。同时，团队将大模型应用于漏洞治理过程中的关键安全任务优化，研究基于大模型的漏洞信息增强技术，自动化PoC生成技术，自动化补丁生成技术等。另一方面，团队致力于利用多年研究积累的安全知识，如漏洞特征，安全规约等，对通用大模型进行微调和增强，构建更加适用于特定安全场景的垂直领域大模型。目前团队相关研究成果已在中国电信，中远海运等多个行业头部厂商中进行落地应用，获得了广泛的认可。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBtSIAiaVicCElibVRoibkyTicqeaHrZKXenby8aUibSRpY5PdxTpXOLRWic8wQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBibDyFFOSexiaOBQk0xyBlTDDqU7sHfqnS2cicvRabHEWbtxEmibEK3BBVA/640?wx_fmt=png&from=appmsg)

欢迎对我们研究方向感兴趣的学弟学妹带上简历联系我们 :)

***Q***

**大模型为漏洞治理带来了哪些机遇与挑战？**

***A***

**张磊助理研究员：**

    大模型具备强大的模式识别和语言理解能力（包括自然语言和程序语言），能够在漏洞报告分析、代码安全审计和修复建议生成等关键漏洞治理任务中提供有效支持。引入大模型技术能有效提高漏洞治理的效率，减少对人工审查的依赖，大幅缩短漏洞暴露时间。

    然而，大模型本身仍存在一些能力短板，例如，上下文长度限制使其难以直接应用于真实世界代码仓库分析，在处理复杂任务时存在注意力分散问题，并且其性能依赖于提示词和训练数据质量。此外，在特定应用场景下，大模型“黑箱”的内部工作机制，以及训练和推理过程中需要大量计算资源等局限性，也使得开发者在信任和采用大模型建议时有所顾虑。

    我们团队目前开展的一系列研究，正是致力于优化和解决大模型与传统安全技术“能力互补”过程中的一些关键问题。通过这些研究，我们希望能够充分发挥大模型的优势，同时克服其局限性，以实现更加高效和可靠的漏洞治理。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBzpyarOEj25ibWIeNjN5icY8lP3xCuUnJkBZjgXS9Y7AFzYrYicxzsR6jA/640?wx_fmt=png&from=appmsg)

**4. 杰出论文获奖团队介绍**

![](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW87fx03Jws9or3gsOA26EFQBq7pic2mnaOBiaPIRZwt6p8Ghv2HXu2VqDEv0zlKxszMrYDs4p6ibk32vQ/640?wx_fmt=jpeg&from=appmsg)

**第一作者：**廉轲轲，复旦大学系统软件与安全实验室博士生，研究方向包括移动安全，开源软件安全，漏洞自动化检测等。在科学研究方面，已在网络安全顶会IEEE S&P和软件工程顶会FSE上发表4篇论文，并获FSE 2024杰出论文奖。在漏洞发现方面，识别并确认 150+ 0Day漏洞（70+ CVE ID），获得来自包括谷歌，华为，vivo，Apache，Eclipse，Red Hat，VMware，Oracle 等知名企业和组织的致谢。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87fx03Jws9or3gsOA26EFQBORs4Sek3MBmFZibp3pM5sicfxzb2zby0bbHbfwdTgicq571Q1ic3PCtMIA/640?wx_fmt=png&from=appmsg)

**指导教师：**张磊，复旦大学计算机科学技术学院助理研究员，硕导，主要研究漏洞挖掘与治理，主持国家重点研发计划子课题、国自科青年基金、上海市人民政府决策咨询项目等，已在IEEE S&P、ACM CCS等网络安全顶会上发表10余篇论文，并获上海市计算机协会科学技术一等奖、ACM SIGSAC 中国优博奖和ACM 中国优博提名奖，FSE 2024杰出论文奖，USENIX Security 2022 杰出论文奖(国内首篇)。研究成果目前在中国电信、中远海运、支付宝、vivo、OPPO等多个行业头部厂商落地应用。

**邮箱：**zxl@fudan.edu.cn

素材：廉轲轲、邓朋

供稿：复旦白泽漏洞治理团队

排版：复旦白泽漏洞治理团队

审核：张琬琪、洪赓、邬梦莹

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、知乎、微博搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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