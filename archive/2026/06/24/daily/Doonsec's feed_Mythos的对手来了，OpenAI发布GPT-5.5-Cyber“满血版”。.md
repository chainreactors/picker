---
title: Mythos的对手来了，OpenAI发布GPT-5.5-Cyber“满血版”。
url: https://mp.weixin.qq.com/s/kne6fkfb6re_wS0F7x9xLg
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:06.491521
---

# Mythos的对手来了，OpenAI发布GPT-5.5-Cyber“满血版”。

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hlXiae3yiayvfZmRuticBsV2YRO2S8drZEK8Tbc3QP8xU9ogx7U5UUibeR3hLORQwHnaEibicdoEK8ADhWWibSjOgp4AaeMVuUVREdaVZGAJ5Wya2E/0?wx_fmt=jpeg)

# Mythos的对手来了，OpenAI发布GPT-5.5-Cyber“满血版”。

老林
老林

安小圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年6月22日，OpenAI宣布扩展其Daybreak网络安全计划，释放出一整套旨在加速漏洞修复而非仅仅发现漏洞的工具与合作伙伴体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hlXiae3yiayvfWCtRNMOKic66ErENNUWjgic098w5GHQcBnTl8yWZGO7jCqswx5KtkrUIaiacbVY2xianbiaVvcEhpGRttUeFHkp0OAWcMMf8w6Eek/640?wx_fmt=jpeg&from=appmsg)

这背后是一个正在发生的瓶颈转移。OpenAI直言：漏洞报告本身并不能保护任何人。长期以来，“发现漏洞”是安全链最大的瓶颈——它需要稀缺的专业技能、大量时间和深入的系统认知。但当前沿AI模型已经能大规模巡视代码库、推理攻击路径、验证假设并挖出隐藏的安全问题时，新的瓶颈已变成“修复”。

用OpenAI的话说：“AI已经改变了网络安全的物理规则。” 前沿AI模型持续加速漏洞发现，但防守方已被海量发现淹没。真正有价值的是验证问题、评估影响、开发测试补丁、协调披露、帮助团队部署修复。

【🚀 GPT-5.5-Cyber“满血版”：专为防御而生】

此次发布的核心是GPT-5.5-Cyber完整版——OpenAI迄今最强大的漏洞发现与修复辅助模型。

数据是硬道理：在CyberGym基准测试中，GPT-5.5-Cyber得分85.6%，超过标准版GPT-5.5的81.8%，也超越了Anthropic Mythos 5的83.8%。在ExploitGym测试中，该模型得分39.5%，而GPT-5.5仅为25.95%。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hlXiae3yiayvfX19gBa9ic8iaQ1kGicibnBhOObpJYibPWicmCD4HF9DTY1akDPqAhfDMmfcpXWMeEYJBYGrz3Hib4wyHNfXnm8jThdTK7ticsA6LK2q4/640?wx_fmt=jpeg&from=appmsg)

该模型能对大型代码库进行持续深入分析——识别安全相关组件、追踪漏洞是否可达、在受控环境中验证问题、开发测试补丁、为人工审查准备证据。目标是帮防守方走完整个修复闭环，而不只是产生更多漏洞发现。

不过，该模型并非公开发布。访问权限仅向通过OpenAI“可信网络安全访问”（Trusted Access for Cyber）计划审核的防御方开放。

【🔧 Codex Security：把“发现”变成“修复”】

OpenAI同步发布了Codex Security插件更新，这是一套能嵌入开发流程的AI安全工具链。

该插件能自动扫描代码、评估严重性、收集验证证据、映射攻击路径、并针对特定代码库生成可供人工审核的补丁。更关键的是，它可以接收来自扫描器、安全公告、漏洞赏金或工单系统的历史报告，批量筛选、验证、排序，并自动生成补丁，导出到现有漏洞管理流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hlXiae3yiayvd9j9BRjZl0rGf7hK9DPtw8y78hM1pL1nR0MegwYwIqJZibibZbiagdF7iaauKdEibbPrz7NfSBWRyVcYn61cs9s0j1FJroeDDWXsiaE/640?wx_fmt=jpeg&from=appmsg)

实际成果已显现：自研究预览版上线以来，Codex Security已扫描超3万个代码库中的3000万次代码提交，人工审核员已将超7万条发现标记为已修复，另有超50万条被自动判定已修复。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hlXiae3yiayvfSibiaSBaj9BK88WZMN4SZIjHCMMicCpSib44rEsOicuGmhiaRj3ibsYIoyWUOkhbBXtQEG7Edj7RLZjYjnianHx6QQJa8PChlkKhy3b4/640?wx_fmt=jpeg&from=appmsg)

具体案例更令人印象深刻：研究人员在Chrome的V8引擎中发现5个可利用漏洞，在Safari的WebKit中发现超10个；Firefox案例中，Mozilla在Pwn2Own柏林大赛开幕前两天修复了一个由GPT-5.5发现的WebAssembly漏洞，此后六支Firefox参赛队伍中有五支退出。

【🌍 “Patch the Planet”：救开源项目于水火】

此次扩展的亮点是面向开源生态的“Patch the Planet”（修补地球）计划。该项目由OpenAI与安全研究公司Trail of Bits联合发起，并与HackerOne合作。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hlXiae3yiayvf5FEyDIwD46wtvSNkticYjFKOUcZ9EicjB6xtqHfWoTspK6WNSZpxC24DG4aW2zVtKRMosWh16CpkQ4GxMA3eXEj2r20RpjYoO0/640?wx_fmt=jpeg&from=appmsg)

为什么需要这个计划？开源项目维护者已不堪重负。 OpenAI引用Linux基金会与哈佛大学研究：在被调查的广泛使用项目中，94%的项目仅有不到10名开发者负责了超过90%的代码提交。向如此小规模的团队投入更多AI生成的漏洞报告，只会加剧积压，而非提升安全性。

运作机制：OpenAI资助专业安全研究人员，配备Codex Security和高级模型，直接与开源维护者协作。关键设计在于——每一条发现都由人工安全工程师审核后才提交给维护者，而非丢更多自动化报告。

成果令人振奋：一次为期五天的冲刺中，安全团队在19个项目中发现数百个合法问题，合并了数十个补丁，产出了可供项目持续使用的模糊测试和测试工具。其中一项亮点是用GPT-5.5-Cyber在不到一天内建起完整fuzzing测试环境——这以往由人类专家手动进行通常要两到三周。

首批参与的30+开源项目包括：cURL、Go、Python、Sigstore、pyca/cryptography等广泛使用的项目。

【🤝 Daybreak合作伙伴计划：让生态一起上】

OpenAI还推出了Daybreak网络安全合作伙伴计划，允许安全厂商和集成商将GPT-5.5与可信访问集成到其商业产品中。

首批启动合作伙伴阵容强大：埃森哲、思科、CrowdStrike、IBM、Okta、Palo Alto Networks、Wiz等。IBM将把GPT-5.5-Cyber整合到其安全运营平台中，该平台目前为全球超4000家企业客户提供服务。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hlXiae3yiayvdR4NX8eia6T7XG0H0zx5ibFXicqibD2cuYppXia7r3sz3BEDcBfsoeNJ9h46U6TzD18AcmBKOEXW23euBhic7cdeYhKLu6voQW7pTeA/640?wx_fmt=jpeg&from=appmsg)

同时，OpenAI正与多国政府和机构合作，包括美国、澳大利亚、加拿大、法国、德国、日本、韩国及欧盟ENISA，帮助关键基础设施防御方更快响应。

【💡 核心观点：从“找漏洞”到“修漏洞”】

从这次发布可以清晰看到，OpenAI的战略重心已经转移。正如Daybreak项目所宣称的：“前沿防御能力不应集中在少数人手中。软件触及生活方方面面——从关键基础设施到企业应用和政府网络。随着AI改变漏洞发现的速度，各地的防御者都需要民主化地获取这些模型，在攻击者发现和滥用漏洞之前找到、修复并保护他们的基础设施。”

当找漏洞变得廉价、瓶颈集体移向修补时，竞争与防御的重心正从“谁能找到最多漏洞”转向“谁能更快把修补落地”。OpenAI通过Daybreak与Patch the Planet补上的，正是这条安全链上最被忽视、也最致命的一环。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbNFGhZSttuhIzVnNJAlxXcndiaWI3s9WjaqpgsqpHlQnicYyLjF0hovoEKHxic0cbyVibvXhs7lKv9YNw/0?wx_fmt=png)

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