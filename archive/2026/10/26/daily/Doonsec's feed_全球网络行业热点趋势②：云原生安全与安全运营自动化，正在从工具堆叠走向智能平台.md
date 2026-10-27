---
title: 全球网络行业热点趋势②：云原生安全与安全运营自动化，正在从工具堆叠走向智能平台
url: https://mp.weixin.qq.com/s/178lVBmQXWwJ-E2ZwBpjPA
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:02:18.306813
---

# 全球网络行业热点趋势②：云原生安全与安全运营自动化，正在从工具堆叠走向智能平台

# 全球网络行业热点趋势②：云原生安全与安全运营自动化，正在从工具堆叠走向智能平台

原创

天元实验室
天元实验室

权说安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/vzicWlmgHGj0oEo96ibVJm2icuMoabx6OstGVQ75SW9ia9ibBADl9rn0yXykt7RibIKrXtG4cxeBuYu7Sn9owV4QlZqcxK7kr1mcvveZEoiciccIR7U/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU5NjEzNTY4NQ==&mid=2247486363&idx=2&sn=05e68549479c76eec8a66faba77d61c4&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vzicWlmgHGj1A4Vqic0FF9Y9J0ttRhVFv2By5MuAkfJaC7ZDFx7Y6my5zVsicYOPD2uVwBYA8UibylK5hbicsusvt33UAzcib83Efn2sK0gPq3ia54/640?wx_fmt=jpeg&from=appmsg)

║企业今天缺少的往往不是安全工具，而是把分散信号转化为行动的能力。云原生安全解决“看见风险”，安全运营自动化解决“及时处置”，二者正在汇聚成一套新的平台化防线。

过去几年，企业的云环境越来越复杂，安全工具也越来越多。

公有云、私有云、容器、Kubernetes、Serverless和SaaS同时存在；CSPM、CWPP、漏洞扫描、EDR、SIEM、SOAR等产品各自生成告警。工具数量增加了，安全团队却没有因此变得轻松。

问题出在哪里？

一方面，分散工具只能看到局部风险，很难还原完整攻击路径；另一方面，安全运营仍高度依赖人工研判，面对海量告警和机器速度的攻击，响应效率已经接近极限。

因此，2025—2026年全球网络安全行业出现了两条相互汇合的主线：

●云原生安全从单点工具走向统一的CNAPP平台；

●安全运营从静态SOAR走向能够自主推理与执行的Agentic SOC。

这不只是产品名称的变化，而是安全体系从“买工具”转向“建能力”的结构性转折。

**一、为什么纯CSPM正在降温？**

云安全最早关注的是配置问题。

存储桶是否公开、端口是否暴露、权限是否过大、加密是否开启——这些问题催生了云安全态势管理，也就是CSPM。

但随着云原生架构不断深入，仅仅发现配置错误已经不够。

一次真实的云攻击可能同时经过暴露资产、错误配置、过度授权、工作负载漏洞和敏感数据。单点工具可以分别发现其中某个问题，却很难回答真正关键的问题：

攻击者能否把这些风险串联起来，并最终接触到核心数据？

这正是CNAPP兴起的背景。

CNAPP，即云原生应用保护平台，试图将云安全态势管理、工作负载保护、基础设施即代码扫描、身份权限分析、漏洞管理和运行时防护整合到同一平台。

Gartner相关资料预计，2026年CNAPP市场规模将达到87亿美元。与此同时，Forrester 2025年的研究显示，85%的欧洲企业运行在多云环境；Gartner预测，到2029年将有35%的企业应用运行在容器中，而2023年这一比例还不足15%。

多云与容器化程度越高，工具碎片化带来的问题就越突出。

**二、真正的CNAPP，不是把多个模块装进同一个菜单**

平台化不等于简单拼装。

如果一个所谓的CNAPP仍然需要在多个控制台之间跳转、重复部署Agent、手工关联不同模块的告警，它只是换了包装的工具集合。

判断一个CNAPP是否真正统一，可以重点观察三个方面。

**1. 是否拥有统一的图谱数据模型**

安全团队需要看到的不只是“某个主机存在高危漏洞”，而是漏洞所在的工作负载是否暴露在公网、使用了什么身份、能够访问哪些数据，以及攻击者可能沿什么路径继续移动。

图谱的价值，在于把孤立风险还原成具有业务意义的攻击路径。

**2. 是否连接开发、部署和运行阶段**

云原生安全不应等到应用上线后才开始。

基础设施即代码、镜像、开源依赖和权限策略，都应在开发与交付阶段接受检查；应用上线后，则需要持续监测运行时行为。只有打通“代码到云”的全过程，安全才能从事后发现转向前置预防。

**3. 是否真正适配多云环境**

企业选择多云通常是业务、成本和合规共同作用的结果。安全平台如果深度绑定单一云厂商，可能无法提供一致的风险视图。

Wiz的快速增长，很大程度上来自无代理扫描和多云中立性。它成立仅6年，年化营收便突破10亿美元，客户覆盖超过一半的《财富》100强企业。Google最终以320亿美元收购Wiz，也说明CNAPP已成为云平台竞争中的战略能力，而不是边缘安全工具。

**三、安全运营的下一站：从SOAR到Agentic SOC**

如果说CNAPP解决的是“看见云上的风险”，那么安全运营自动化解决的就是“发现之后如何行动”。

传统SOAR通过预先编写的Playbook执行告警查询、工单流转和封禁等动作，在规则明确、流程固定的场景中非常有效。

但它也存在明显局限：静态Playbook通常只能覆盖约30%—40%的告警类型，一旦遇到新的攻击手法、缺失的上下文或未预设的变量，流程仍会回到人工分析。

Agentic SOC的变化在于，AI Agent不再只负责总结告警，而是开始承担完整任务：

1. 理解告警和调查目标；

2. 主动调用多个安全工具补充证据；

3. 基于上下文判断攻击链和影响范围；

4. 生成或选择处置方案；

5. 在授权范围内执行响应；

6. 记录过程，并把高风险决策交由人工确认。

这让自动化从“按照剧本执行”升级为“理解目标后动态完成任务”。

Palo Alto Networks的XSIAM客户报告显示，其平均告警关闭时间不到18分钟，而传统SIEM/SOAR配置的行业平均值超过4小时。Cortex AgentiX则基于大量真实Playbook执行经验训练，厂商声称可将平均响应时间缩短98%。

CrowdStrike推出Charlotte AI AgentWorks，让客户以无代码方式构建安全代理；Google Security Operations将确定性自动化与Gemini驱动的AI Agent结合，用后者处理流程中未预设的变量；Torq则专注于Agentic安全自动化，并在2025年完成7000万美元融资。

一个明显趋势是：传统SIEM负责集中日志、SOAR负责执行流程、AI助手负责提供建议的界限，正在被AI原生安全运营平台逐渐打破。

**四、云安全与自动化为什么一定会走到一起？**

云环境天然是动态的。

资源可以在几分钟内创建或销毁，容器不断扩缩容，权限与API调用关系持续变化。仅靠周期性扫描，很容易在两次检查之间错过风险；仅靠人工处置，也难以跟上基础设施变化的速度。

CNAPP与Agentic SOC结合后，可以形成一个更完整的闭环：

持续发现资产 → 识别配置、漏洞和权限风险 → 还原攻击路径 → 结合业务影响确定优先级 → 自动调查与响应 → 将处置结果反馈给开发和运营团队。

这条闭环的价值，不只是“自动关掉更多告警”，而是减少安全团队在不同平台之间复制信息、重复判断和手工协作的成本。

头部厂商的战略也在验证这一方向。Palo Alto Networks通过Cortex Cloud、XSIAM和AgentiX连接云安全与自治运营；Microsoft利用覆盖身份、端点、云和数据的遥测构建统一防御；Google收购Wiz后，则有机会把CNAPP能力与其云平台及安全运营产品进一步整合。

行业竞争的焦点，正在从单个功能的优劣，转向谁能提供更完整的数据、上下文和响应闭环。

**五、中国市场：技术升级背后，更现实的是交付效率**

在国内，安全运营自动化的价值不仅体现为响应速度，也直接关系到安全服务能否规模化交付。

调研数据显示，2025年国内MDR收入达到312.05亿元，同比增长41.2%，成为增长最快的安全子赛道；MSSP市场也保持高速增长。越来越多客户希望购买的不是一套系统，而是7×24小时持续运营和明确的安全结果。

然而，传统托管运营严重依赖分析师人力。如果每增加一个客户都要同比增加人员，服务规模越大，成本压力也越高。

亚信安全在2026年发布AI XDR 2026，将十大智能体嵌入威胁检测、分析和响应链条，厂商声称可降低15%—30%的运营成本、提高50%—70%的事件响应效率。奇安信也在推进AISOC与智能体运营指挥体系。

对国内厂商而言，Agentic SOC最直接的商业价值或许不是创造一个更炫的AI入口，而是把分析师经验沉淀为可复制的运营能力，让MDR与MSSP摆脱纯人力扩张模式。

**六、企业选型时，建议先问这六个问题**

面对越来越多“AI原生”“一体化”“自动运营”产品，企业需要避免被概念带着走。

**1. 平台能否形成统一资产和风险视图？**

确认它能否关联云资源、身份、漏洞、配置、工作负载与数据，而不只是展示多个独立模块。

**2. 能否解释风险优先级？**

高危漏洞不一定意味着最高业务风险。平台应能够结合公网暴露、可利用性、身份权限和数据敏感度，说明为什么某个问题需要优先处理。

**3. AI Agent到底能执行什么？**

区分“生成一段调查摘要”和“真正完成跨工具调查及处置”。同时确认Agent的权限范围、审批机制、失败回滚和审计记录。

**4. 自动化效果能否量化？**

关注平均检测时间、平均响应时间、告警压缩率、自动处置覆盖率和误操作率，而不是只看演示中的问答效果。

**5. 能否融入开发与运维流程？**

如果风险只能留在安全控制台中，开发团队无法及时收到可执行的修复建议，平台仍然难以形成闭环。

**6. 数据与责任边界是否清晰？**

确认哪些日志和业务数据会被模型处理，模型在哪里运行，操作如何追溯，以及发生错误时由谁负责。

**结语：未来的安全平台，竞争的是闭环速度**

云原生安全的本质，是在高度动态的基础设施中持续看见风险；安全运营自动化的本质，是把风险及时转化为行动。

当两者结合，企业安全体系便不再只是告警、工单和工具的集合，而成为一个能够持续感知、判断、处置并学习的系统。

因此，未来真正有竞争力的平台，不一定是功能列表最长的平台，而是能够用最完整的上下文回答三个问题的平台：

风险在哪里？哪一个最重要？现在应该采取什么行动？

谁能更快、更准确、更可控地完成这条闭环，谁就更接近下一代安全运营的核心位置。

参考资料

1. [Gartner：Top Cybersecurity Trends for 2026](https://www.gartner.com/en/newsroom/press-releases/2026-02-05-gartner-identifies-the-top-cybersecurity-trends-for-2026)

2. [CNAPP市场与选型趋势](https://cybernoz.com/dissecting-gartners-cnapp-market-guide-key-takeaways/)

3. [CNAPP及身份安全市场数据](https://www.orizon.one/blog/cybersecurity-trends-2026)

4. [Google收购Wiz及全球网安并购数据](https://m.eeworld.com.cn/ic\_article/468/734267.html)

5. [AI原生网络安全平台与XSIAM运营数据](https://researchintelo.com/report/ai-native-cybersecurity-platform-market)

6. [亚信安全发布AI XDR 2026](http://www.news.cn/tech/20260420/290e4ed750fb486686ef8b8bf50eae8a/c.html)

注：本文依据公开资料及《2025—2026年网络安全行业热点趋势深度调研报告》整理，数据截至2026年9月。文中厂商数据包含企业公开口径，仅用于趋势分析，不构成采购或投资建议。

推荐阅读

[全球网络行业热点趋势①：AI安全与身份安全，正在成为行业绝对焦点

2026-10-12

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vzicWlmgHGj0F3ugHdJq1MWfIiaibMnoQDdRWzkzly5cNNnOqbQhHMNx8pWvF2PscE1meSKvrHRVFfjx6S2YuhQQibTRn2kwVu9EJOxmINwvnzY/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU5NjEzNTY4NQ==&mid=2247486430&idx=1&sn=53b368f294e0a1313a649671fcb6e380&scene=21#wechat_redirect)[从策略堆叠到智能决策：AI 如何让零信任真正动态起来

2026-09-21

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vzicWlmgHGj0pXJQ74YMicrTK5zsjY0s5Go7Wueyic6iaE9HQzA83JiclnRRBTVAv6jjkaicxuvsKiayBHR3G1cY2v5XUXWcuBgbHqpXNpMHagaFX0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU5NjEzNTY4NQ==&mid=2247486415&idx=1&sn=57734d46604840a0618e1e8d454a50fd&scene=21#wechat_redirect)[当智能体拿到生产权限：OWASP 2026 智能体安全十大风险解读与零信任应对

2026-09-07

![](https://mmbiz.qpic.cn/mmbiz_jpg/vzicWlmgHGj21ElSxIsCUfJF4yH7O0pq4eylzoiaSrCPe68IrYBqOEGQqoicMR5IybLkkUyB2bRBLot2XhBclwdibV8HK1ee4vGpiasicXmjDlwWI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU5NjEzNTY4NQ==&mid=2247486400&idx=1&sn=4a526501548d1790a4ed6835f2418150&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8QxXQzRARZladuBovosTjIcKTHeW20XYkoDSIsf9UBwmfVCFjmsSiaSJP8icE2AkMZue9bW5viaOpAUOOX1JOhelw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8QxXQzRARZmz1YjZRNibbgPicM5K0KicUyO8orTibSpIqGRqibyPTWdxp324uWR4XAort9GiaX4fb2lq4CNCjoohpdEA/0?wx_fmt=png)

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