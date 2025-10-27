---
title: DataCon2024 | 开源软件包暗藏恶意代码，如何实现高效精准检测？
url: https://mp.weixin.qq.com/s?__biz=MzU5Njg1NzMyNw==&mid=2247488753&idx=1&sn=d82c194ca07fc3cfbe8f3626cdccd13e&chksm=fe5d0c71c92a8567872cc3ba374731c438df29cd94a80dc56a17182390945606332692124935&scene=58&subscene=0#rd
source: DataCon大数据安全分析竞赛
date: 2024-12-04
fetch_date: 2025-10-06T19:38:49.775662
---

# DataCon2024 | 开源软件包暗藏恶意代码，如何实现高效精准检测？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RicNZQMn3FU6ehsgeStma6o8icSSS0gplZjYlPwic5dq968OC9OMwJWefZ0dOdUF1IW01UdnJlXxKibHbSE3gWFubQ/0?wx_fmt=jpeg)

# DataCon2024 | 开源软件包暗藏恶意代码，如何实现高效精准检测？

DataCon大数据安全分析竞赛

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarR4k6dFYU4ia1491dUkgSYwZjs7JI5vnibyX6BVYbVqXl1BtmchhibKnnJa7ibJ65wfTKnfbLicAq2LvQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

11月28日，由清华大学网络科学与网络空间研究院联合奇安信集团、蚂蚁集团、广东联通、百度安全、赛尔网络、北京航空航天大学国家卓越工程师学院共同主办的DataCon2024大数据安全分析竞赛圆满落幕，五大赛道冠军均已揭晓。其中，“软件供应链安全”议题聚焦考察参赛者对恶意代码、恶意软件包的识别和检测水平。最终**来自中国科学院软件研究所的“SecureNexusLab供应链安全”战队脱颖而出，荣获该赛道冠军**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarR4k6dFYU4ia1491dUkgSYwwHHo3ddZ3p4QUdF6ro5eZkXsreTRpj62xCJcyrmBWbQoUzoy9UXLlQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**开源项目遭遇投毒？高效精准检测是关键**

01

软件安全是历届DataCon大数据安全分析竞赛的重点关注议题，从2021年至2023年，大赛不仅持续聚焦软件供应链安全，还逐步扩展到物联网安全、恶意软件自动化分析等领域。软件供应链安全已成为当今软件行业面临的一项重大挑战。随着软件开发过程中对开源组件依赖性的不断增加，这为攻击者提供了新的入侵途径。攻击者可以通过向开源项目注入恶意代码或篡改现有组件的方式，对软件供应链实施攻击。这种攻击往往隐蔽性强、波及范围广,已经成为高级持续性威胁(APT)的重要手段之一。

本次赛题要求选手从NPM软件包、PyPI软件包中精准检测出包含恶意行为的软件包。“要准确检测出这些恶意的开源组件并不容易,需要综合运用多种技术手段，如静态分析、动态分析，以及当前较为热门的大模型。这就要求选手有一个较为广泛的技术能力，并且可以处理大量的数据。其核心难点在于如何平衡检测中的误报率和漏报率。”大赛评审委员会专家讲解赛题难点时指出。

过高的误报率会导致大量安全告警无法被及时有效处理，而高漏报率则可能使真正的高危威胁被忽视。“我们面临的主要挑战是在缺乏先验知识的情况下难以准确地开展恶意软件包检测”SecureNexusLab战队成员表示，“此外，在初步筛选后的样本数据集中，存在明显的漏报与误报问题。”

为应对这些难题，该团队开发了一种基于聚类分析的自研检测技术，并结合其他静态分析方法，以便在没有预设信息的前提下快速完成初步筛查。他们构建了一个迭代优化框架：首先使用大型模型对潜在恶意代码进行评分和定位，以有效降低误报率；然后，根据大模型识别出的新规则重新扫描整个数据集，进一步减少漏报情况的发生。该方案在降低误报率、提高查全率等方面取得了显著突破。

**赛事搭台促合作 科研成果走向实战应用**

02

竞赛所探索出的高效、精准的恶意代码检测方法，不仅能够提升开源社区软件供应链的安全治理水平，还可以被整合到企业的开发工具链中，为一线开发者提供更加可靠的安全保障，增强整个软件行业的安全基础设施。DataCon竞赛研究成果已被广泛应用于实际场景，成功识别并防御了多起潜在的安全威胁，展现了极高的实用价值。

![](https://mmbiz.qpic.cn/mmbiz_png/nicUAzFsiaL3ZwzCbUfmX2NqMicEptqcJTNibWibfwX5hrOEqdGMYgOyArZ2w0lNqMs94JbAbBBkcpLF8aqf1SuXGoA/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other)

“在2022年的软件安全赛道中，PowerShell反混淆的赛题吸引了428支队伍参赛。由东南大学和复旦大学组成的dddd联队，他们工具的反混淆效果远超其他参赛者，而且解题思路极其新颖。”评审委员会专家回忆称。

赛后，奇安信技术研究院星图实验室与该战队的两位成员进行了深入合作。经过近两年的持续交流与协作，双方成功将DataCon竞赛期间开发的原型工具，拓展成为效果远超现有解决方案的动态反混淆工具——PowerPeeler。目前该工具已在天穹沙箱中得到广泛应用。

此外，这项研究成果还形成了一篇高质量的学术论文，并被国际网络安全领域的顶级会议CCS 2024接受，展现出世界领先的研究水平。

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarR4k6dFYU4ia1491dUkgSYwR6QvLXTJtSsLACXV6EuIFSMaqPmc0ZmTs9ZqqxYddm0lZvMhjPIIYw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

奇安信技术研究院成员在美国盐城湖市CCS 2024会场，介绍Powershell反混淆工作

**奇安信构建全线供应链安全支撑能力**

03

Gartner预测，到2025年全球45%的企业机构将遭遇软件供应链的攻击。供应链安全公司ReversingLabs在2024年报告《软件供应链安全状况》中指出“过去三年中，源自开源软件包存储库的威胁增加了1,300%以上。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarR4k6dFYU4ia1491dUkgSYwh6ZsEZicCVLvvMXtlq82jvQIicKiaQ1MiaibpAjwgqXYvxj9zZgibjOgNC8A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

软件供应链风险存在于应用系统的全生命周期，包括设计、生产、交付、部署、使用及运营、停止等阶段。奇安信认为，需要用系统工程方法体系化、全局性治理，来确保各个阶段的安全性和可靠性。企业的软件供应链安全的技术能力建设离不开四项关键能力，即开发安全能力、开源安全能力、安全部署运行能力、自动化渗透测试能力。

为此，奇安信提供了**奇安信代码卫士，**帮助企业以最小代价建立代码安全保障体系并落地实施；**奇安信开源卫士，**实现开源软件资产识别、开源软件安全风险分析、开源软件漏洞告警及开源软件安全管理等功能，保障企业交付更安全的软件；**奇安信天问软件供应链安全分析系统**，为高危漏洞影响范围评估、终端软件安全管控、后门植入事件主动发现、信创软件安全性测评等一系列软件供应链安全分析工作提供支撑，等等。

同时，奇安信构建了一套全面的软件供应链安全治理框架，帮助用户建立以软件供应链安全检测为核心，集软件供应链安全咨询、软件供应链应急响应处置、软件供应链安全教育与培训为一体的安全体系，整体提升软件供应链安全技术防护和管理水平。

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarR4k6dFYU4ia1491dUkgSYwf8QXsrTlef5HDmSiboCVD9JdW0u8Y9UVa5GoibuvoMsqrUK2944icLK3g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

早在2021年，为了进一步强化全国范围内的软件供应链安全保障，深入源代码安全技术研究、产品研发和市场服务，奇安信与重庆市璧山区政府联合承建了“软件供应链安全检测中心”，成为全国首个软件供应链安全专业检测机构，已经在全国20余家合资公司设立检测机构分中心。

▼

从学术科研的前沿探索，安全竞赛的实战演练，到产品开发的精益求精、治理框架的系统构建，奇安信始终走在行业发展的最前沿。奇安信不仅着眼软件供应链的起始环节，更致力于从源头强化安全理念，推动数字技术底座的内生安全能力建设。唯有确保软件供应链中的每一环节都安全可控，才能为数字经济的蓬勃发展提供最为坚实可靠的支撑。

**![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU6ialicOYa6NNX3XP398lFDzGWzB6PUVLLVrB1P74v8KttVZWrOYSQCbnpQDu94tsCFGw9yAykbIibiaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)**感谢合作伙伴的助力 让我们走得更高更远****

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU4hm1Q9ribADDO7RNGuhGoaK6TGiacLYicPyX2PZw0dic30n8cWY2cWJed3agEib9Re36dmOJhWvoCVvDw/0?wx_fmt=png)

DataCon大数据安全分析竞赛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU4hm1Q9ribADDO7RNGuhGoaK6TGiacLYicPyX2PZw0dic30n8cWY2cWJed3agEib9Re36dmOJhWvoCVvDw/0?wx_fmt=png)

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