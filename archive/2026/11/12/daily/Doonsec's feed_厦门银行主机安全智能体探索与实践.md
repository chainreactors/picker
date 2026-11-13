---
title: 厦门银行主机安全智能体探索与实践
url: https://mp.weixin.qq.com/s/nczKm1Bih0cVjZjC5PhuZw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:18.790447
---

# 厦门银行主机安全智能体探索与实践

# 厦门银行主机安全智能体探索与实践

青藤云安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于中国金融电脑，作者厦门银行

**作者**

厦门银行汤姿平劳模工作室

厦门银行信息技术部 黄于秦

![](https://mmecoa.qpic.cn/mmecoa_png/iaDf0iaGn69rmgI8WT00FVyVicqerpf3tGNS5C3JCRjrBFIcqx29xicz8Ziab1ibRbyrDqwr9lMT7EWyZmFPTDkuKnC59ax6iaIQDVqImZqhc3tHFI/640?wx_fmt=png&from=appmsg)

**一、主机安全运营挑战**

随着AI 技术加速普及，网络攻击正变得更快、更自动化、成本更低，攻击主体也从“人”扩展为"人+智能体"，这使得防守方面临的压力显著加大。主机作为承载核心业务的关键资产，一直是攻击者的重点目标。在网络攻击全面提速的背景下，传统以人工流程为主的主机安全运营模式难以跟上攻击节奏。具体来看，主机安全运营面临四方面突出挑战：

一是告警研判面临瓶颈，规则建设依赖人工。主机安全告警研判需结合日志、进程、文件、网络连接及业务背景逐项核查，复杂应用场景还需理解程序调用与业务运行逻辑，较为依赖人员经验；已确认的正常业务行为也需持续维护白名单等规则，重复排查与规则建设占用较多人力。

二是情报核查效率低。情报核查需跨系统关联资产、组件版本、端口暴露、配置与运行状态，并进一步核验利用条件，效率较低；面对“两高一弱”专项或多条情报集中核查任务，人工查询、逐项比对工作量较大，难以兼顾时效与核查深度。

三是人工调查难以规模化。深度调查需围绕进程、文件、账号和网络行为关联多类线索，并根据新发现持续扩展调查范围。人工方式耗时较长、依赖专家经验，难以对大量疑似线索维持同等调查深度。

四是未知威胁识别仍有盲区，人工盯防难以常态化。既有规则、特征及行为检测模型对未知漏洞利用、合法工具滥用等未被当前检测逻辑覆盖的行为，仍可能存在识别盲区，而未触发明确告警的异常线索难以依靠人工实现大范围、常态化持续盯防。

为应对上述挑战，厦门银行在既有主机安全平台基础上搭建主机安全智能体体系，探索"以 AI 防护 AI"的主机安全运营新模式。

![](https://mmecoa.qpic.cn/mmecoa_png/iaDf0iaGn69rlhnOKsPiaqM5W2A2ga1XMkFBxKYIGoJv2nNFic36KhvtzQt4gp9oq5fToBPW9v6Nfj2hjmRnmnbWicib6TR2CuVWfW6eCDmicRrXxs/640?wx_fmt=png&from=appmsg)

**二、 厦门银行**

**主机安全智能体体系建设**

**1.主机安全运营总体架构**

厦门银行依托既有主机安全平台采集的进程、文件、账号、网络连接等数据，以及资产查询、日志检索等基础能力，通过数据标准化和工具能力封装，为智能体自主开展安全调查提供支撑，逐步构建“真实数据支撑、智能体自主调查、专家审核决策”的主机安全智能体体系架构（如图1所示）。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/iaDf0iaGn69rkn2CB64H6yxIm54wRTfG89fNUlTiahzuC2b70Ze8hwaUhWCAJMNwy5ER9SD7yOjP39dia0ibF4DsutRciawxcY8nOzBia5FgmsjalA/640?wx_fmt=png&from=appmsg)

*图1 厦门银行主机安全智能体体系架构示意*

在数据工具层，围绕智能体调查需求，重点开展数据与工具改造：在数据改造方面，对进程、文件、网络连接、账号等采集信息开展标准化、结构化与语义标注，便于智能体理解和关联；在工具改造方面，将资产查询、日志检索、进程排查等调查类能力封装为标准化工具，对策略下发等环境变更操作按照权限隔离与人工确认要求设计调用边界。

在智能体层，以大模型为决策核心、以标准化工具为执行手段，围绕线索自主拆解调查任务，按需调用工具，获取证据，并根据新发现动态扩展对象、调整调查路径，形成可供复核的结论与依据。人工确认的规则、业务标注与经验反哺调查流程，实现迭代优化。

在智能体应用层，围绕告警研判、漏洞排查、深度调查及响应处置等重点环节，开展专项智能体建设，推动既有安全数据和调查能力在不同场景中复用。

在运营层，围绕智能体输出的研判结论、核查结果及处置建议，探索打造“智能体调查—证据输出—人工复核—处置反馈”的运营闭环。在运营控制设计中区分只读查询与环境变更操作，对策略变更、进程处置等高风险动作明确最小权限、人工确认与调用审计要求；将复核形成的业务标注、误判修正和规则用于后续优化。

**2.典型场景实践**

（1）告警研判智能体：提升研判质量与规则建设效率

告警研判智能体以主机告警为线索，调用工具关联原始日志与资产数据，减少重复上机排查次数，以证据交叉核验降低模型幻觉、提升研判准确性，并基于研判结果智能生成白名单规则，经人工审核通过后生效。告警研判智能体工作流程如图2所示。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/iaDf0iaGn69rksSGX3bLz7Ip4ba27NicSY8FAd6I5gvIYiaN2TibctyeZVFnj8zOQZICibD84amZy2I2DqhOWkEdrbTOsYoSibs8gHQ2g71dUxtibbk/640?wx_fmt=png&from=appmsg)

*图2 告警研判智能体工作流程示意*

一方面，告警研判智能体可关联主机数据，核实告警实际行为。以“可疑命令执行”告警为例，智能体关联执行账号、父子进程、文件操作及网络连接，结合主机用途与业务背景输出研判结论和证据。在典型需上机核查场景中，研判耗时由小时级缩短至3～5分钟，研判准确率达到98%。另一方面，告警研判智能体可智能生成白名单，收敛重复告警、减少人工配置。以定时漏洞扫描反复触发“可疑进程参数”告警为例，智能体核查扫描来源及行为特征，经人工确认扫描用途与授权后形成业务标注，为同类告警研判提供依据，并据此提取进程、账号等特征生成白名单规则建议，通过人工审核匹配条件及适用范围后应用。在该典型重复告警场景中，人工处理的重复告警量减少98%，规则编写耗时较人工减少80%。告警收敛与人工审核量变化趋势如图3所示。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/iaDf0iaGn69rn8RnNZHMxcKtChmEmwVibqNjyichfDtYG4QFotOBoHOE626uHu4rZ0k0hnx2icMv9jvsdcqjY7x2eGLiaPHHlibQgZwTWZc4Za998w/640?wx_fmt=png&from=appmsg)

*图3 告警收敛与人工审核量变化趋势示意*

（2）漏洞排查智能体：深化漏洞验证与修复优先级评估

漏洞排查智能体借鉴专家核查思路，从漏洞情报提取组件、版本与触发条件，筛选可能受影响的资产，再调用工具核验利用条件与日志迹象，形成关联证据的风险判断和修复优先级建议，提交人工复核。漏洞情报排查智能体工作流程如图4所示。

![](https://mmecoa.qpic.cn/mmecoa_png/iaDf0iaGn69rlDSHRpQuuOIkjicKOI9sOg1P15icRJY8C6WmDj5Y855UKzjGuRXGoz77ZcxyohI82PFH9uTSbZ1KHCPchsiaIMWlbNHaBEtUibq98/640?wx_fmt=png&from=appmsg)

*图4 漏洞情报排查智能体工作流程示意*

在具体实践中，漏洞排查智能体首先解析漏洞情报，提取受影响的组件、版本范围及利用条件，并将相关信息与资产信息进行比对，初步筛选可能受影响的主机，减少人工跨系统查询和逐台核对的工作量。其次，逐项核验利用条件，深化漏洞验证。对版本匹配的主机，智能体依据情报生成细粒度检查项，核验进程、文件和关键配置，并关联日志排查利用迹象。需要说明的是，此类核验侧重运行环境与利用前提，不等同于主动漏洞利用测试；版本命中也不代表利用条件成立，证据不足时仍需保留待确认事项并交由人工复核。最后，漏洞排查智能体汇总核验结果及证据，结合漏洞风险和业务系统重要性提出修复优先级建议，并形成待复核的工单草稿，交由人工确认后流转。由此，人员由逐项查询比对转向复核关键结论、确认处置安排。漏洞深度验证如图5所示。

![](https://mmecoa.qpic.cn/mmecoa_png/iaDf0iaGn69rmD3Q6HSTMQ4A4iahH67XJz4BDEbIKB5CuMZzLdrPWfhNQbicmpq0iag6Qhm3TYEhqFhvb9ibs0NnQ1rlAjAiawxib97ibl0Lpn0vWcPI/640?wx_fmt=png&from=appmsg)

*图5 漏洞深度验证示意*

（3）深度调查智能体：支撑攻击链路关联分析与还原

深度调查智能体以疑似告警或调查线索为起点，将待调查线索拆解为 IP、文件、进程等独立对象逐一调查，一旦发现新线索即生成新对象纳入调查队列，形成"调查—发现—再调查"的递归式扩展机制（如图6所示），在可观测数据范围内逐步关联还原攻击路径，并从"入侵是否落地"递进到"攻击者做了什么、连接了哪里"。

![](https://mmecoa.qpic.cn/mmecoa_png/iaDf0iaGn69rmRfwibqVpQw9mamkSbT9ibibcicwY5vqhEFFZywwn3q9rzprgiadTgiac36fmmwOB0en8PJeo1hfYjvcxn1mqfsIAPUiaiaF4oFysgoCg/640?wx_fmt=png&from=appmsg)

*图6 递归式调查机制示意*

以典型Web攻击链的WAF疑似命令注入告警为例，仅凭告警特征尚不能确认攻击是否成功，深度调查智能体围绕告警对象关联核查相关进程、文件与网络行为，并依据新线索持续扩展调查对象（此处为模拟调查思路，不代表银行实际发生安全事件）。与人工方式相比，深度调查智能体在入侵告警核查方面实现触发方式、溯源覆盖、响应时效与人员角色四个维度的转变（见表1）。

*表1 深度调查智能体在入侵告警核查方面与人工方式的对比*

![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/iaDf0iaGn69rmBJMqqDDn1CYpuuKehrzSzgUaicklVDSuOiaQtCmicPkKH5NBmIe1zgquR3AxSleAW4H0EkszVWibNevXn5OkiaLttVPTIa4mLSQgU/640?wx_fmt=jpeg&from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_png/iaDf0iaGn69rlevbu88ndVOicKvic9Ou08De25kjXWibDtxU3B19BFYRFekGVgI14sZxaRJPGnWZ6n9aJXt12Q5cYK789IeDt6HL0rMaq9fLV2SE/640?wx_fmt=png&from=appmsg)

**三、应用成效与价值分析**

实践表明，主机安全智能体能够显著提升告警研判、漏洞排查与深度调查的效率和质量，对厦门银行主机安全运营实现提质增效、加快转型升级具有重要推动作用。其应用成效与价值具体体现在以下三个方面。

一是从辅助分析向基于真实证据的自主调查转变。相较于仅对告警、情报文本进行分析，智能体能够围绕线索调用主机安全工具，获取进程、文件和网络行为等原始证据，并在核验与关联中动态扩展调查对象，使安全研判从单点信息判断向证据驱动的自主调查转变。

二是从专家个人经验向可复制的组织能力转变。安全运营的专业差异不仅体现在结论，更在于调查路径和判断方法。将专家常用的检查项、关联思路及经确认的业务标注沉淀为流程和适用规则，有助于减少个人经验差异，使复杂调查能力逐步成为团队可复用、可持续完善的组织能力。

三是从人工操作工具向人机协同运营转变。智能体的价值不仅在于单次核查效率的提升，还在于减少复杂线索调查对专家时间的占用。智能体承担重复查询、证据关联与调查扩展等工作，让安全专家可以把更多精力用于核验证据、判断业务影响和决定处置方式，为更多日常疑似线索开展深度核查创造条件。与此同时，人工复核形成的经验持续反哺规则和调查方法，使人机协同运营具备持续改进的基础。

现阶段，核查主要围绕已有告警或漏洞情报展开，对未产生明确告警异常行为的主动发现能力仍有提升空间。下一阶段，厦门银行将探索主动盯防智能体，结合资产角色、业务特征及主机行为构建动态基线，持续分析行为偏离，为潜在未知威胁提供调查线索；探索主机安全与网络、身份、应用安全等专业智能体的协作，以资产、账号、进程和网络会话等对象为线索关联跨领域证据，逐步构建“主动发现—协同调查—专家决策—持续优化”的人机协同运营模式，推动安全运营从单场景智能化向体系化、协同化、主动化方向演进。

**-完-**

**热门动态推荐**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/jcrjcnYMMMMppsHT9x2oIGpCTowNLbibsokmVTts8yUCl7DDceWROQGPibs2frkib08ibvaHxZeDnMgBrGXgojdjHIW3fMeWj1QEsyF5dmJDjhI/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851582&idx=1&sn=ccee95907ec492fd00fc3c937867a881&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jcrjcnYMMMMNI7K5bVPczky0bOibtW47dfRacLSfOgf9kKiaaqtKgn7f2YWlV8ETWj6PLico2vLbtQeCKThzCfbXLjZUZUorjqoqhbL10LN4Ho/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851901&idx=1&sn=ee388d4cd4f66712099275e2b6fd6ee2&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/jcrjcnYMMMPePsAK9dUILU8XlCj122NnxjU7yXPnEpdVgGYu75zK1YmUiaGhSCiaKyMQBZU0Gn96xoibRbT3IDn14Odm9bO0yhfSPW5RKJXes0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851740&idx=1&sn=de59a36e4afcae310d9476afc6778355&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7EpcyTBK4P1WPTQaAScoCKkianCbxMW6Ws340jzw69l94hzH56I696TJ4Z02pPVML9Tf2EVAvUGF99ll2PkO7rg/0?wx_fmt=png)

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