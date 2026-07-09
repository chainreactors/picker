---
title: CISA被曝部署Mythos扫描联邦代码库，已发现大量漏洞
url: https://mp.weixin.qq.com/s/8MJTJS-aCetEZEfJIZ5KIA
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:01:32.772519
---

# CISA被曝部署Mythos扫描联邦代码库，已发现大量漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d3C5oxt0zNW7YCnw3bjmV2p0Hcuf0tibDucPNBiaN7HwvagyCG9oCqJcSLAUwGg1wb6jHu6QO2hc9JSR4icAWfODEaricYSbpW6jCY/0?wx_fmt=jpeg)

# CISA被曝部署Mythos扫描联邦代码库，已发现大量漏洞

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

当地时间2026年7月6日，路透社援引三名知情人士的消息披露，美国网络安全和基础设施安全局（CISA）正在使用Anthropic公司开发的高级AI模型Mythos，对联邦政府代码仓库进行大规模安全审计。这一消息由路透社驻华盛顿记者拉斐尔·萨特率先报道，随后被CybersecurityNews、SecurityWeek、The Next Web等多家科技安全媒体跟进解读，共同印证了美国政府机构对AI自动化漏洞发现能力的强烈需求，也让Anthropic与华盛顿之间既对抗又依赖的复杂关系浮出水面。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d2F5teUEdkpsRx4pJXWr2vnbTCBtwZEOvwUqjjYh8SLWswLba5KKsnibibSU4TIld8YIoXfjpCtQYFxcPWV8MEXibKIeUxOH3vWBs/640?wx_fmt=jpeg&from=appmsg)

#### 审计行动：攻击面评估团队牵头，已发现“大量漏洞”

据路透社报道，此次AI驱动的代码审计工作由CISA下属的“攻击面评估团队”负责执行。该团队在联邦政府范围内专门从事数字安全评估和模拟黑客攻击演练，其核心任务是在外国情报机构和网络犯罪分子之前发现可被利用的安全缺口。SecurityWeek的报道进一步确认，该团队正在利用Mythos“识别复杂编码错误和潜在攻击路径”，并实现规模化运作。

两名消息人士向路透社透露，AI辅助审计已经发现了“大量漏洞”，但拒绝就漏洞的性质或严重程度做进一步说明。路透社明确表示，“无法确认该团队审查了多少政府代码，也无法确定所发现漏洞的性质或严重程度”。The Next Web的报道对此评论称：“扫描范围仍然不明朗。尚无公开信息说明哪些系统已被扫描，如何对发现的漏洞进行分类，以及Mythos发现漏洞后会如何处理。”

CISA与Anthropic双方均对此次行动保持沉默。路透社报道指出，一名CISA代表上月曾表示会查看是否有相关信息可分享，但随后未再回应后续邮件；Anthropic公司同样未对有关该计划的问题作出答复。The Next Web因此将当前所有说法定性为“基于匿名消息来源，而该机构和该公司均拒绝透露具体工作内容”，强调相关信息“仅供参考，尚未定论”。

#### 漫长前奏：从五角大楼“拉黑”到情报机构秘密采用

Mythos最终进入CISA手中之路远非坦途，其过程折射出Anthropic与美国政府间高度戏剧化的关系逆转。

今年2月，双方关系降至冰点。Anthropic当时拒绝移除其AI模型中防止被用于自主武器或国内监控的安全措施。五角大楼随即作出回应，正式将这家总部位于旧金山的公司列入“供应链风险”名单——路透社指出，这一标签此前“几乎专门用于涉嫌协助间谍活动的外国公司”。3月，一名联邦法官叫停了这一前所未有的“拉黑”决定。

转折点出现在Mythos的私下发布。该模型被描述为在发现和利用网络安全漏洞方面“极其强大”。据路透社报道，Axios于今年4月率先披露，尽管存在五角大楼的禁令，美国国家安全局（NSA）早在4月就已在使用Mythos；随后《纽约时报》进一步报道称，NSA分析师已在机密环境中对其进行了测试，并“对其能力印象深刻”。

当Anthropic于6月初推出面向公众的版本Fable——其包含该公司所称的“网络安全防护措施”——白宫突然要求该公司禁止外国人运行该模型。路透社称，此举“引发了全球范围内的模型停用，直到上周才解除”。SecurityWeek补充指出，Fable的全球短暂下线凸显出“围绕强大AI系统的持续政策挑战”。

值得注意的是，Mythos是Anthropic旗下网络安全项目“玻璃之翼计划”的核心产品。The Next Web报道称，Anthropic声称该模型在漏洞发现和利用方面性能异常出色，目前已将使用权扩展至15个国家的150家机构，且该公司已秘密提交了在美国进行首次公开募股的申请。

#### 行业影响与深层矛盾

随着CISA使用Mythos的消息传出，AI驱动的自动化安全审计正从概念迅速走向实战。传统代码审计耗时且资源密集，而像Mythos这样的AI模型能快速分析庞大代码库，自动追踪跨服务的数据流以识别注入点或权限提升路径，标记出可能被忽略的细微逻辑缺陷或不安全配置。CybersecurityNews指出：“随着网络威胁日益复杂，将AI融入漏洞管理工作流程可能成为公共和私营部门的标准做法。”与此同时，该媒体也提醒，“部署如此强大的工具也引发了对监督、滥用以及安全创新与政策控制之间平衡的质疑。”

行业竞争同步升温。据报道，OpenAI已推出自己的网络防御模型作为替代方案。The Next Web评论道：“竞争对手们纷纷效仿……显而易见的是，无论官方文件如何规定，政府将进攻型人工智能应用于防御任务的实验已经展开。”

综合多方信源来看，Mythos进入联邦网络安全防线承载着多重矛盾。一方面，一个负责保护政府网络安全的机构，正在依赖一家曾被五角大楼正式认定为“供应链风险”的公司的私有模型来解读政府自身代码。The Next Web将此称为“务实之举还是权力过度扩张”的问题，答案“可能取决于审计的实际结果”。另一方面，扫描范围与后续处置机制仍然成谜，这种不透明性使外界难以评估AI审计对政府安全态势的实际贡献。

路透社在报道中援引消息人士的评价称，此举是“政府热情采用Anthropic工具的又一迹象，尽管该公司正在应对与白宫的持续僵局”。从NSA的机密测试到CISA的代码审计，一个信号已相当清晰：无论监管争议如何演变，AI驱动的安全审计已在改写美国政府网络安全防护的游戏规则，而这一张力恐将在Mythos的进一步部署中持续发酵。

参考文献

1. Satter, Raphael. “US cyber agency is using Anthropic’s Mythos to audit government code, sources say.” *Reuters*, July 6, 2026. https://www.reuters.com/world/us-cyber-agency-is-using-anthropics-mythos-audit-government-code-sources-say-2026-07-06/
2. Abinaya. “U.S. Cyber Defense Agency Reportedly Using Anthropic’s Mythos to Audit Government Code Repositories.” *CybersecurityNews*, July 7, 2026. https://cybersecuritynews.com/u-s-cyber-defense-agency-using-anthropics-mythos/
3. Lennon, Mike. “CISA Reportedly Using Anthropic’s Mythos to Scan Government Software for Flaws.” *SecurityWeek*, July 7, 2026. https://www.securityweek.com/cisa-reportedly-using-anthropics-mythos-to-scan-government-software-for-flaws/
4. The Next Web. “US cyber agency is using Anthropic’s Mythos to audit government code.” *The Next Web*, July 7, 2026. https://thenextweb.com/news/cisa-anthropic-mythos-government-code-audit

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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