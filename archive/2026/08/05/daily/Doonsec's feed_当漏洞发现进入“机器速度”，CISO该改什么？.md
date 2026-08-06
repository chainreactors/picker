---
title: 当漏洞发现进入“机器速度”，CISO该改什么？
url: https://mp.weixin.qq.com/s/u3tTS7PBrRbwCe3kBKrpRA
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T04:59:57.737248
---

# 当漏洞发现进入“机器速度”，CISO该改什么？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dJ6206EMFEjtwJRpHjcZFS3gBK05rwicr98XCtGOibFiatgjgcvuEssrXgg9nia3ELeY8rFcNIicPJ4YxfaNz7KxDxiaxMUGmoBDnSiayUEJHrgdfE/0?wx_fmt=jpeg)

# 当漏洞发现进入“机器速度”，CISO该改什么？

国际云安全联盟CSA上海代表处

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一支安全团队刚把季度渗透测试报告送进修复流程，另一套AI扫描系统可能已经生成了下一批问题。新增告警越来越快，真正能够完成验证、排序和修复的问题却没有同比增加。安全工作的节奏差，就出现在这里。

CSA发布的**《AI Security Through the CISO Lens: Insights from the AI Storm Summit Series》**，汇总了2026年5月至6月三场AI Storm Summit的讨论。旧金山站更多关注AI驱动的安全运营，纽约站聚焦治理、组织和董事会沟通，华盛顿站则深入到攻击自动化、OT/ICS环境和智能体架构。参与者来自不同规模和行业的组织。报告遵循“**查塔姆宫规则**”**（Chatham House Rule）**，属于实践者经验的定性综合，并非统计意义上的行业调查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEgmicSRKDa0iaHgiaq79AlLDibk2RZ0Qy9y1nuNF7plCq8iawKkohDut9RicjQ6YMicFjF33ic4s1mL6TkfdnSzzDWgGLxv20zIKcz6ft8/640?wx_fmt=png&from=appmsg)

这一点很重要。报告记录的是一批安全负责人的现场判断和早期实践，不足以证明整个行业已经进入同样阶段。把它当成风险雷达，比当成趋势宣言更合适。

**漏洞越找越快，**

**修复能力却没有同步扩容**

三场讨论反复提到，**AI正在缩短漏洞发现和利用的时间**。一些走在前面的团队已经把代码扫描、可利用性验证和高优先级处置压缩到数小时。与此相比，按季度测试、按天计算严重漏洞修复时限的流程显得迟缓。

问题在于，发现速度并不等于安全水平。AI可以低成本地产生大量线索，但每条线索是否真实、在本企业环境中是否可达、能否与其他弱点形成攻击链，仍需要验证。未经筛选的结果直接进入研发工单，只会把原来的告警疲劳搬到修复团队。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEiaWBKMWRmRsF5j6ZyaJWDCetVyciaR3shujhRwMuDyDdpg5VgrYlJhGD2ib0HT4riabqNIibzRYjoxXGib47MUtfDvIUDNicnupN06kU/640?wx_fmt=png&from=appmsg)

示意图：发现规模扩大后，验证、排序和修复能力成为新的瓶颈。

报告提出了一个值得采用的指标——“**吸收率**”，即一段时间内解决的问题与新增问题之比。这个指标虽然简单，却比“本月发现多少漏洞”更接近安全团队的实际压力。如果新增问题长期快于关闭速度，再漂亮的扫描覆盖率也只是积压的另一种表达。

CVE、CVSS和KEV在这里并非毫无价值，只是无法单独完成优先级判断。通用评分需要与企业自己的上下文合并：**资产是否暴露、漏洞是否可达、攻击能否串联、业务影响有多大、是否存在补偿性控制**。EPSS等利用可能性数据可以作为输入，但最后仍要落到本地攻击路径和处置成本上。

**别把智能体当作另一个员工账号**

报告的另一项担忧来自企业智能体。它们已经开始读取数据、调用工具、执行代码，有些还会创建子智能体或直接连接生产系统。传统IAM通常围绕人类用户和相对稳定的应用账户设计，很难自然覆盖这种持续运行、权限可变、能够自主组合工具的工作负载。

企业至少要先回答几个朴素的问题：**现在有多少智能体？谁创建、谁负责？它们使用哪些模型和工具？能读什么数据，能改什么系统？授权何时到期，出现异常后怎样停用？**如果这些问题没有统一答案，后续谈最小权限和审计都会缺少基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEgBciatUYcngl4bdaticicJfoWibEHJs0GbsrReEWQw7XWibjwKogm3ff33MUqMibuzgXeEn0p0tsxzicTXVibObOTF7kYhHgbhFVtTEuI/640?wx_fmt=png&from=appmsg)

示意图：智能体治理需要同时覆盖身份、授权、

隔离验证、行为监测和回滚。

SPIFFE、SPIRE等工作负载身份机制，可以帮助企业给智能体签发可验证的身份，但身份只是起点。系统还要记录它在什么任务下获得了什么权限，调用过哪些工具，依据什么证据采取行动，以及后果由谁承担。识别出“它是谁”，不代表已经解释清楚“它为什么这样做”。

报告多次使用“**harness**”一词，**指围绕模型建立的提示、规则、工具、编排和验证机制**。这个概念比单纯比较模型排名更接近工程实际。同一个模型，放在不同的任务边界、验证流程和反馈机制中，可靠性可能相差很大。对安全团队而言，模型只是其中一个组件，harness才决定结果能否进入生产流程。

**自动化处置：**

**该快的地方快，该停的地方停**

如果每一个动作都等待人工逐项审批，安全响应很难追上自动化攻击；如果智能体可以直接修改生产环境，又会引入新的操作风险。三场讨论都没有给出统一边界，但“按后果分层”是一条可落地的思路。

资产发现、日志关联和处置建议可以高度自动化。漏洞利用验证应放在隔离环境中。限流、短时封禁、终端隔离等可逆动作，可以在证据和阈值满足预设条件时自动执行。涉及生产数据删除、关键配置修改或业务中断的操作，则应保留人工确认。

![](https://mmbiz.qpic.cn/mmbiz_png/dJ6206EMFEjfgBjuMXMf7yeiafVkZO8hoBCJMn2ZWnQiacKxGAm58ALHGicyqFBkxpSeyvRutMkhDiahk3j8Qgo4ibPLJBkzg36cnEWXTwdDAWo4/640?wx_fmt=png&from=appmsg)

示意图：越接近不可逆的生产变更，证据门槛、

授权强度和人工复核要求越高。

这种安排不是简单地决定“人要不要在环”，而是把治理写进执行过程：事前确定授权范围和触发条件，执行时保存证据，异常时能够停止和回滚，事后有人复核。**人的价值也不再是反复点击批准，而是设置边界、处理例外并承担高后果决策的责任。**

对CISO来说，真正费时的部分往往不在模型部署，而在周边机制。变更流程是否允许预授权处置？供应商SLA能否配合小时级响应？研发团队是否接受带有利用证据的自动工单？法务和采购是否明确了模型变更、数据留存、服务限流及退出安排？这些问题不解决，所谓“机器速度”只能停在演示环境。

**安全能力差距，**

**可能被进一步拉大**

报告不止讨论大型科技公司，教育、医疗、中小金融机构、公用事业以及OT/ICS运营方也出现在讨论中。这些组织面对同样快速的漏洞发现和攻击自动化，却未必拥有足够算力、人才和测试环境。工业设备还受到停机窗口、认证要求和设备寿命限制，很难按照互联网软件的节奏打补丁。

在这些场景中，要求所有组织“更快修复”并不现实。更有效的做法可能是先减少暴露面，强化网络分区和访问路径控制，部署监测与欺骗机制，再通过行业平台共享验证能力和处置经验。CSA在报告中提到的**分层指南和共享harness资源**，也应优先考虑弱资源组织能否实际使用，而不是只为成熟团队提供更复杂的工具。

第三方风险同样需要重新检查。年度问卷和供应商自我声明很难持续反映模型版本、数据处理方式和上游依赖。合同中需要**明确模型变更通知、零数据留存、服务连续性、数字主权和退出机制**；技术上还应演练与关键AI服务断开后的最低业务能力，以及重新接入时如何确认系统状态可信。

**从几个边界清楚的场景开始**

这份报告没有提供大规模数据来证明自动化防御已经普遍成熟，也没有给出替代CVE、CVSS或统一治理智能体的完整方案。报告关于“短期更有利于攻击者、长期可能转向防守者”的判断，目前仍然是一种趋势研判。企业不宜据此仓促开放生产权限，更不能把采购更强模型当作安全转型的完成标志。

现阶段可以先选**少数可逆、可度量的场景**：清点智能体及其责任人，找出高权限工具调用，建立隔离验证环境，给自动处置设定证据门槛，同时验证停止和回滚是否真的有效。指标也应从扫描数量转向吸收率、经验证可利用问题占比、确认到遏制的时间，以及高风险暴露面是否持续缩小。

对CISO而言，眼下最重要的不是追赶每一次模型升级，而是建立一套能跟上新速度、又不会丢掉证据和责任的工作方式。**漏洞可以由机器更快地发现，处置权仍需要被认真设计。**

致谢

文章作者：卜宋博，CSA大中华区研究分析师

关注公众号，回复关键词“CISO”

获取报告完整版

---

**大会预告**

2026 CSA大中华区大会暨AI+安全大会将于9月11日在北京清华大学举办。大会由云安全联盟大中华区（CSA GCR）与清华大学联合主办，以“智序·本体：以可信智能时代筑基”为主题，聚焦AI安全、人工智能治理、产业应用及人才培养等核心方向，汇聚政产学研各界力量，共同探索可信智能时代的发展路径，推动人工智能安全生态建设。

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEjVWDRHMNBefBhK1YHw5KHD4dibZqjgRBaUU0b0U4D6icBqUU9VgKavZ9G6r3V7KYtsbsaSA61fXG0kWsmmIeb0GSwctyIjLJeco/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkwMTM5MDUxMA==&mid=2247512370&idx=1&sn=d98015e98bf5097c699f966824649b10&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/dJ6206EMFEiaYnoBlDc4fuz5lqic5BfvONUibcHQxvnfvSowz2zK7n6umaD07INQE75FSQqQ9QQ1tMqgnbNhXTR4xrxVYsFzm57jybqv9BTcE8/640?wx_fmt=png&from=appmsg)

扫码报名CSA GCR大会

**阅读推荐**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/dJ6206EMFEj9BEke7ctAU9VXaxmlicln7V143S20ys1yYCGcESRqA4BuGq75ulbsAgaOBQhqbUpglSVicXxIoSRvHhTDtOKRc4tJ8bNV8u2bE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwMTM5MDUxMA==&mid=2247512270&idx=1&sn=e273f6cf2c0ca5789a5dd5319889a421&scene=21#wechat_redirect)

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEgwiaCTQEgpbCxsTljLdu8BC4S768Vp76ghzuEq3wibWGe5lucc3IW6Uh14ynA4myMTsymxPlibTqBBKpFDEqTG8pgV1UhPGLrubw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEjm8GNOgWlKVibFnUGjukZVkDRNLK9xcmic3uTnNWclqT7a48VyNWFpJbwSLBcjeKg7wXeaMPdJ1xUpRtndLmTGxAVDtsLLwkdPo/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Atw1J8F68p5KiaFqiav31cr04yNib3LYJQr8icP8AOhorLFK4A5FQxavZVN0a03shJMibfe1uo0kicXia3XOmJ1S384VQ/0?wx_fmt=png)

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