---
title: 助力MITRE ATT&CK框架应用落地的10种免费工具（资源）
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651120720&idx=1&sn=be431e9ffee4f40661b7d532b0717e63&chksm=bd1454838a63dd95c4c63e458734099fe2c6eee757c1864a5b4ae05354649b5ab7c67cf2a59a&scene=58&subscene=0#rd
source: 安全牛
date: 2022-12-08
fetch_date: 2025-10-04T00:53:49.841509
---

# 助力MITRE ATT&CK框架应用落地的10种免费工具（资源）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RW52SoqaibSCcXbHIYVhXe5aMLe8QOb2FicooBnPYlc37DXEDjBftubtlA/0?wx_fmt=jpeg)

# 助力MITRE ATT&CK框架应用落地的10种免费工具（资源）

安全牛

ATT&CK框架公开发布于2015年，从最初的一个内部人员分享的Excel电子表格工具，到如今已经发展成为威胁活动、技术和模型的全球知识库，成为在企业、政府和安全厂商中广为流行的安全工具。ATT＆CK框架提供了关于在野网络攻击活动最全面及时的社区知识集合，这有助于企业划分安全威胁的优先级，并用于评估安全方法、产品和服务。

不过研究人员发现，ATT＆CK框架的应用潜力目前还没有得到充分挖掘，其应用推广中面临的主要挑战包括：

* 缺乏安全工具支持，难以实现互操作性
* 框架部署的成熟度不够，难以实现自动化

为了帮助使用者应对上述挑战，本文收集整理了一些有助于MITRE ATT&CK知识库应用落地的免费工具和资源。

**01**

Getting Started with ATT&CK

**《ATT&CK实践指南》白皮书**

这本免费的电子书将一系列博客文章中的威胁情报、检测和分析、对手模拟和红队、评估和工程等内容整合到一个单一的、方便的工具集中。这样将有助于安全威胁分析师如何更好地使用ATT&CK。本书收集了大量真实用例的共享内容，并将这些内容分成不同的级别：

* 级别1适用于刚起步但可能没有太多资源的分析师；
* 级别2适用于开始成熟的中级安全团队；
* 级别3则适合更先进的网络安全团队。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWa26N70OTdo8vbspqYfKvcQYicQf9icbMOG81qBrbribGEw0O0iaQJQWiazQ/640?wx_fmt=jpeg)

**传送门**

https://www.mitre.org/sites/default/files/2021-11/getting-started-with-attack-october-2019.pdf

**02**

**CALDERA**

CALDERA是一个由python语言编写的红蓝对抗工具（攻击模拟工具）。它是MITRE公司发起的一个研究项目，该工具的攻击流程是建立在ATT&CK攻击行为模型和知识库之上的，能够较真实地APT攻击行为模式。

通过CALDERA工具，安全红队可以提前手动模拟并设定好攻击流程，并以此进行自动化攻击和事件响应演练。同样，安全蓝队也可以利用该工具，根据相应的威胁开展模拟应对。

该工具主要由两个组件组成：

* 核心系统。由相关存储库中可用的内容组成，主要包括一个带有REST API和web界面的异步命令控制（C2）服务器。
* 插件。这些插件可以扩展核心系统功能，包括代理、报告、TTP集合等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWoFVSDljeF9dk5avmDwohOicPzGx5YbbTc2bxYrj9zMjWHONBFxL4xgA/640?wx_fmt=jpeg)

**传送门**

https://www.mitre.org/sites/default/files/2021-11/getting-started-with-attack-october-2019.pdf

**03**

Best Practices for MITRE ATT&CK Mapping

**《MITRE ATT&CK映射的最佳实践指南》白皮书**

由于ATT&CK框架的应用潜力并没有得到充分挖掘，美国网络与基础设施安全局（CISA）和国土安全系统工程与发展研究所（HSSEDI）共同制定了一份《MITRE ATT&CK映射的最佳实践指南》，旨在帮助网络威胁分析师将攻击者的TTP（技术、工具和程序）映射到相关的ATT&CK技术，以提高防御者主动检测对手行为和共享行为情报的能力。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWXxyd8oKtMibO1mEN5GG7jeg518uKoYTZFT5UNECBEiaM0jBS6NAsTSgQ/640?wx_fmt=jpeg)

**传送门**

https://www.mitre.org/sites/default/files/2021-11/getting-started-with-attack-october-2019.pdf

**04**

**CASCADE**

CASCADE也是MITRE公司发起的一个研究项目，旨在将“安全蓝队”团队执行的大部分调查工作自动化，以确定使用主机数据的网络上存在的可疑行为的范围和恶意程度。

CASCADE原型应用具有处理用户身份验证、运行分析和执行调查的能力，可以对存储在Splunk/ElasticSearch中的数据进行分析，以生成警报。警报会触发一个递归调查过程，其中几个后续查询会收集相关事件。应用会自动生成这些事件的图形，显示它们之间的关系，并用ATT&CK的信息标记该图形。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWOjmgEgD1icqJ1U3764YjnKdiaf2s0kicCKYe8xZIWc9M3cHEtHZWHBT7w/640?wx_fmt=jpeg)

**传送门**

https://www.mitre.org/sites/default/files/2021-11/getting-started-with-attack-october-2019.pdf

**05**

**Metta**

Metta是一款对抗性模拟工具，它是由多个内部项目产生的。Metta使用Redis/Celery、python和VirtualBox进行攻击行为模拟，这样用户就可以测试基于主机的安全系统。另外用户还能测试其他基于网络的安全检测和控制，具体过程取决于使用者的设置方式。Metta能够在Microsoft Windows、MacOS和Linux等多个操作系统终端上运行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWKDy265p1dKvaQvD2tjKy7pYCX1g6WqQ5PMpSJdGpmw9MXVUddnK0OA/640?wx_fmt=jpeg)

**传送门**

https://github.com/uber-common/metta

**06**

**Sandbox Scryer**

Sandbox Scryer是一款功能强大的开源威胁情报工具，该工具可以根据公开的沙箱输出信息生成威胁搜索和情报数据，并允许安全研究人员将海量威胁样本发送给沙箱，以构建可以跟MITRE ATT&CK Framework一起使用的技术文档。Sandbox Scryer提供了大规模用例解决方案，该工具适用于对利用沙盒输出威胁情报感兴趣的威胁分析人员。

值得一提的是，当前版本的Sandbox Scryer使用了多种恶意软件分析服务的数据信息，可以帮助分析人员加快和提升威胁搜索的能力。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RW7IVwoorKb6BPB4gvYpeApib4pOvmXvRXRTGTgDjljL5x2tejIZhLU5Q/640?wx_fmt=jpeg)

**传送门**

https://github.com/PayloadSecurity/Sandbox\_Scryer

**07**

Finding Cyber Threats with ATT&CK-Based Analytics

**《使用基于ATT&CK的分析发现网络威胁》白皮书**

该白皮书提出了一种使用MITRE ATT&CK框架的新方法——通过基于行为的威胁模型来识别相关的防御传感器（defensive sensor），并使用攻击仿真来构建、测试和改进基于行为的分析检测能力。该方法可以通过防御差距分析、端点安全性评估、针对特定环境优化行为分析，以及使用红队模拟等多种手段，增强企业的网络安全性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWx6xBm7pGDrlwO7KjqhgKmYqibAibboN7vdKxx2ia5R6lZuAmVFx0hhD0g/640?wx_fmt=jpeg)

**传送门**

https://www.mitre.org/sites/default/files/2021-11/16-3713-finding-cyber-threats-with-attack-based-analytics.pdf

**08**

**Atomic Red Team**

Atomic Red Team是一个由Red Canary主导的开源项目，它提供了和ATT&CK一致的红队测试内容，可以用来测试现有的威胁分析方法。安全团队可以使用Atomic Red Team快速、可移植和可重复地测试他们的系统应用环境。用户可以直接通过命令行执行测试，无需安装运行软件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWYKoUGDE59xqIsDIXoBNRYItl1solAyBbcRTyx6eNs3NINPYQV6NgYQ/640?wx_fmt=jpeg)

**传送门**

https://github.com/redcanaryco/atomic-red-team

**09**

**Red Team Automation（RTA）**

Red Team Automation是一组有38个脚本支持的可执行文件，可生成与ATT＆CK框架中的技术相对应的安全组件，旨在允许安全蓝队测试他们对恶意间谍技术的检测能力。截至目前，Red Team Automation提供50多种由ATT＆CK技术支持的组件，这个数量将来还会进一步增加。Red Team Automation支持Microsoft Windows操作系统，并且使用python进行编码，另外它还可以执行反取证操作，进行恶意传播、绕过UAC等模拟攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWnJ9Cd6b1pFQy8ec9Yjfr1u60UIRYY5LVv5Icfs7rbQEOQmhcKR9Kag/640?wx_fmt=jpeg)

**传送门**

https://github.com/endgameinc/RTA

**10**

**Mapping CVEs to MITRE ATT&CK网站**

这是一个由Vulcan Cyber的研究团队创建的网站，用于展示一个正在进行的攻击研究项目，可以将记录的CVE映射到MITRE ATT&CK矩阵中的相关战术和技术。目前，该网站还处于测试阶段，将会不断更新，以纳入并记录更多的新CVE。用户可以根据特定的技术需要搜索CVE，也可以通过特定的CVE搜索与之匹配的ATT&CK战术和技术。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RWa4pJca5JxMpyHJb0wc2ZhQVdzYDG44Pt5R4s1nhhpCpTecemALAicjA/640?wx_fmt=jpeg)

**传送门**

https://mitremapper.voyager18.io/

**参考链接：**

https://www.helpnetsecurity.com/2022/12/05/top-10-free-mitre-attack-tools-resources/

相关阅读

[企业部署MITRE ATT&CK框架面临挑战](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651108397&idx=3&sn=53cf88d56c2f96c49c331b89887dffd0&chksm=bd1404fe8a638de82cd259c29973fd6326f3aaadd4f4d351002c5ff2b02d992073ea41f232cd&scene=21#wechat_redirect)

[MITRE推出ATT&CK workbench共享工具](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651102907&idx=3&sn=cc688b0eec3333699866d12745fc8185&chksm=bd142e688a63a77e51d4ebdeef0b4af60006cedc85ed7119205e177ce21ccf1ae89bbf391a30&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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