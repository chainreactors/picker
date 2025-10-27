---
title: 2024年SOC技术应用调查：“SIEM一切”更为常见，自动化能力仍然不足
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651131201&idx=1&sn=d6ff2fa49fb12819f20f2d2190bf5f44&chksm=bd15bd928a62348494a18c9499f495de9990341f5248a41c69b7c8336411b2664f79c72433f0&scene=58&subscene=0#rd
source: 安全牛
date: 2024-07-23
fetch_date: 2025-10-06T17:43:17.844627
---

# 2024年SOC技术应用调查：“SIEM一切”更为常见，自动化能力仍然不足

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvosICic9tY66aSgBZBhEZdQKKolBml4huEgAnIpEyNiclJobeEvSltUzYg/0?wx_fmt=jpeg)

# 2024年SOC技术应用调查：“SIEM一切”更为常见，自动化能力仍然不足

安全牛

近日，SANS研究所发布了《2024年SOC技术应用调查报告》。调查结果显示，许多组织仍在与困扰他们多年的SOC技术应用问题作斗争，这些问题包括缺乏SOAR等高级功能、人员配置需求高、缺乏熟练的运营分析师以及可见性不足等。以下收集整理了本次报告的一些核心观点和发现：

**01**

**基于云的SOC服务模式成为新的顶层架构**

报告调查认为，目前“基于云”的SOC服务模式现在已经超过了“单一中心”的SOC，成为最常见的SOC技术架构。迁移上云的趋势已经在IT界持续了很多年，现已延伸嵌入到SOC架构中。云混合SOC最终将成为企业首选的SOC。安全将来自于云，服务于云，这是一个重大的改变，将迫使未来安全运营的人员、流程和技术保持一致。

**02**

**“SIEM一切”变得更为常见**

当询问受访者“如何处理SOC的海量数据”的问题时，他们似乎都不太愿意花太多精力去过滤东西，而是把所有东西都倾倒到SOC的日志处理分析系统（SIEM）中（见下图）。这个答案似乎与安全运营的发展要求相违背，但相比在收集数据前花费大量精力去弄清楚实际需要什么，“SIEM一切”的数据处理方式，显然对安全运营团队来说更具成本效益。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvoZctQAquiaVI37NqjS16Iic7IoVBlQCPYicziaMUNeo4efdmFgZqibZcFRSA/640?wx_fmt=png&from=appmsg)

**03**

**集中式架构比例有所增加**

企业组织构建SOC的方法有很多。拥有一个集中式SOC是其中最常见的方法（如下图所示），403名受访者中有242名（60%）受访者如此认为。与2023年的49%和2022年的53%相比有所增加。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvoToUyAuDzF18nubPS2Oc7aq0EcTChNJSH0riaNegbSkPLicIUbCWlu4sg/640?wx_fmt=png&from=appmsg)

**04**

**自动化威胁狩猎应用不断增长**

威胁狩猎的主要目标是寻找还没有被威胁检测系统发现到的漏洞，有一种重要但简单的狩猎方法就是将新发现的指标应用于历史数据存储库。

在询问“威胁狩猎活动是否自动化”时，46.1%的受访者表示他们使用供应商提供的工具实现了部分自动化（如下图所示），同比去年增长了8.1%

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvocapktDIibgIU3XDIgiabKwv4Mn0E36oGxnKsaBOjzeggJYicFmoXmicfTQ/640?wx_fmt=png&from=appmsg)

报告认为，使用更新的威胁指标（IoC）进行追溯分析只是最低限度的猎杀，真正的威胁狩猎需要对以前未被发现的东西进行深思熟虑地探索。建议是，持续深入进行自动化追溯分析，并努力进行复杂的猎杀。

**05**

**AI/ML技术应用满意度仍不容乐观**

去年，SANS首次将AI/ML添加到其技术满意度分析列表中，结果它排在最后一名。今年，情况有所变化，但仍不容乐观。报告发现，从2023年到2024年，计划实施AI/ML的SOC项目比例呈现下降趋势：从2023年20.5%的组织表示计划实施降至2024年的10.6%。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvolK5GKhdXNMuNgMAYtib8YjGA15nslzfY3TScLG0icrQ2BBBBPnOmgCNw/640?wx_fmt=png&from=appmsg)

此外，已经购买这些技术的买家是否存在“后悔情绪”，SANS每年都会提供基于GPA的评分。2023年，AI/ML的GPA为2.17，仅击败了GPA最低的网络数据包分析（2.15）。今年，它再次排在倒数第二，但平均绩点更低，仅为1.99。

**06**

**运营分析师的平均任期增加**

专业人员配备一直是SOC应用中最受关注的问题。只有通过熟练的分析师，SOC系统才能在真实安全运营场景下表现良好。所以分析师的留存率是SOC系统应用的一个长期挑战。本次调研结果显示，具备3到5年任期经验的人员比例，略高于1到3年任期，这对组织来说是一个积极的趋势。

那么，究竟是什么因素促使SOC分析师留下来？调查结果显示，工作成就感对员工的意义愈发突出，已成为首要驱动因素。如今，组织对一级诊断和分析的自动化程度不断提高，这使得SOC分析师能够专注于更具战略性和智力刺激的活动，例如威胁猎杀和高级事件响应，进而缓解分析师的职业倦怠问题。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvoCI5TSYeore80h3SUNoLsNzicdznTyiaBpVq8zxYibJYr7tqW8iah5q7MGQ/640?wx_fmt=png&from=appmsg)

**07**

**SOC技术满意度分析**

本次报告对SOC系统中广泛涉及的47种技术进行了调研。如下图所示是对处于已部署状态的各种技术的满意度评分，结果表明，满意度更高的是EDR/XDR、VPN、SWG/SEG、SIEM、NGF、MPS、IDS/IPS、持续监控和评估、DoS/DDoS防护、端点OS监测与日志分析、恶意软件防护、DNS防火墙、网络流量监控等。

满意度较低的技术包括：AI和ML、欺骗技术（如蜜罐）、网络连接分析、全包捕获、网络流量分析。此外，受访者对SOAR、威胁情报平台（TIP）、威胁猎杀、数据丢失防护、SSL/TLS流量检测等技术的应用满意度也不太高。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4Njvo7G4et3m6kvL0Yoia52ibiaV3JUeKcN3tUFL1HwRt2gFfW3ib6BSMbdOSww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvoTq5sozCryEIZtX6YTdNhblH1nskJN9Zib5sBHAD2SbmibTwQqOnHSz3w/640?wx_fmt=png&from=appmsg)

值得一提的是，尽管本底调查显示GPT技术应用的满意度较低，只获得了51个肯定回复。但报告分析师认为，GPT可以成为未来SOC应用优化的推动者，以优化沟通并提升分析师对信息理解，但它还不能取代分析师。

**08**

**SOC系统应用面临的挑战**

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvoTgvIanjZDOchUMXbuJH8y9p6soMJMOVLLesp35xyByYMkHCNqdnMQg/640?wx_fmt=png&from=appmsg)

在被问及“组织在应用SOC时目前面临的最大障碍是什么？”时，18.3%受访者回答了“缺乏自动化响应和编排”功能，紧随其后的两个答案是直接相关的——“高员工需求”（14.4%）和“缺乏熟练员工”（14.2%）。第四个常见的挑战则是缺乏企业级的可见性，占比12.9%。其他挑战还包括安全、应急响应和运营人员间的孤岛思维，缺乏管理支持，太多工具未能实现集成，缺乏上下文关联，警报疲劳，缺乏操作流程和指南以及合规要求等。

**09**

**SOC应用性能的度量指标**

报告认为，SOC的使用性能需要通过指标来评估。其中，外包项目（渗透测试、取证、威胁情报和警报分类）最常见的衡量指标是处理的事件数量。紧随其后的指标还包括根除的彻底性（没有复发的原始或类似妥协）、从发现到遏制再到根除的时间、由于已知/未知漏洞而发生的事件等等。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAd3ykpyIEU6S5mOtw4NjvoGQM4Aj6Ss15z5XhJPibphlib0dnLVv33CBWOrVxSKwC26OHZG4Iiaib1AA/640?wx_fmt=png&from=appmsg)

原文链接：

https://torq.io/resources/sans-soc-survey/

相关阅读

[简析自主SOC战略的关键流程与应用实例](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651130070&idx=1&sn=e0e15f6a58caf7dae867cd36ad91f186&chksm=bd15b8058a6231131eb5816a86c9b40edf4c35222480fcd9bbec7c9933f1ed5a48c46f4e1896&scene=21#wechat_redirect)

[SANS研究所：企业在实施零信任时常犯6种错误](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651131170&idx=2&sn=5e7429557ebb69a7f420929fbc68f7ab&chksm=bd15bdf18a6234e7a49d2ed54fa4c14918d48e88bdce7bc145590f99fc5239cb3c7983361cfc&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=wxpic)

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