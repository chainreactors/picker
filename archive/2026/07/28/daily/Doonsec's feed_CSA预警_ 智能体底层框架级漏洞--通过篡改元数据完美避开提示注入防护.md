---
title: CSA预警| 智能体底层框架级漏洞--通过篡改元数据完美避开提示注入防护
url: https://mp.weixin.qq.com/s/OAWs3646H1y7W85v9igdYg
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:01:44.518336
---

# CSA预警| 智能体底层框架级漏洞--通过篡改元数据完美避开提示注入防护

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dJ6206EMFEhwZPAHHnsSX8AgcdqbgInAnNVXod4Q86K90gvm4aTUzicVIVUkHhIOsIB7zS1aib8M5ibAegibjQMo5btRofwIO9TCDHPwh1gWGkY/0?wx_fmt=jpeg)

# CSA预警| 智能体底层框架级漏洞--通过篡改元数据完美避开提示注入防护

姜来
姜来

国际云安全联盟CSA上海代表处

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年7月16日，云安全联盟（CSA）官网发布研究简报“**Agent Data Injection: A New Attack Class Beyond Prompt Injection”。**该报告由首尔国立大学、伊利诺伊大学香槟分校与安全厂商Largosoft联合研究产出，揭露全新攻击类别**ADI（Agent Data Injection，智能体数据注入）**，彻底突破行业现有针对提示注入的全套防护体系，对浏览器AI智能体、代码开发智能体形成全覆盖威胁。

**一、攻击原理详解：**

**篡改可信元数据的概率分隔符注入**

**（一）什么是ADI攻击？**

ADI属于新一代间接提示注入攻击，与传统提示注入存在本质区别：传统攻击植入显性指令诱导AI执行恶意操作；ADI不传递任何命令文本，而是篡改AI智能体默认信任的底层元数据（页面DOM元素ID、代码评论作者身份、工具调用执行记录等事实信息），欺骗AI基于虚假信息自主做出高危操作。

**（二）恶意载荷如何实现隐藏篡改？**

攻击核心技术为概率分隔符注入：常规程序依靠固定语法规则解析JSON、HTML等结构化数据；大模型以概率方式识别文本边界。攻击者嵌入特殊Unicode引号、转义符号、模板符号等伪装成合法分隔符，在正常数据字段内伪造全新数据边界，模型会将伪造内容判定为可信上下文，全程无恶意指令文本。

**（三）如何绕过现有AI安全防护？**

行业近两年主流防护手段（输入/输出护栏、指令分层校验、基础沙箱）均以识别“恶意指令”为核心目标，ADI不存在可被检测的命令语句，防护体系无风险信号触发，可直接放行恶意篡改内容。

**（四）攻击载荷拆分部署策略**

攻击者分两类场景落地载荷，隐蔽性极强，人工及常规安全检测难以识别：

1. 网页侧：在页面评论、商品描述中植入伪造DOM元素标识，无任何可疑代码、恶意指令；

2. 代码仓库侧：伪造PR评论作者、工具测试结果记录，文档、代码、注释外观完全合规，无异常特征。

**二、攻击触发流程：**

**静默篡改、多层诱导的隐蔽风险**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEh2xjYicI88HIRhLAvP77nNa7I3c04ZZKjHIA1vTLyqYibjLLd4SvVS5OiaoiaL7dEAU0ebluahBib1NIh8bLibvcIlpMOGI8BVXAJzE/640?wx_fmt=png&from=appmsg)

该攻击无即时破坏效果，具备潜伏性、持续性特征，完整触发流程分为五个阶段：

1. **预埋阶段**：恶意篡改后的网页内容、代码PR正常加载合并，自动化安全检测无任何告警，成功潜伏在业务及代码环境中；

2. **读取阶段**：AI智能体正常开展工作，自主读取页面元数据、仓库工具执行记录，默认采信所有数据为可信有效信息；

3.**误判阶段**：模型通过概率化解析逻辑，识别攻击者伪造的分隔符，将虚假元素ID、伪造作者信息、虚假测试结果判定为合法可信数据；

4. **误操作阶段**：网页AI智能体被诱导误点击支付、确认订单等高风险按钮；代码AI智能体违规执行恶意命令、放行存在后门的漏洞代码；

5. **持续危害阶段**：污染的元数据可跨会话留存，后续每一次智能体调用都会复用污染数据，长期处于被操控状态，持续引发安全风险。

**三、实测案例：**

**全主流模型均存在攻击成功率**

CSA联合研究团队针对市面主流前沿大模型、AI智能体开展量化实测，验证该攻击的通用性与高危害性，核心实测数据如下：

1.**结构化JSON数据场景**：攻击成功率稳定在31.3%~43.3%，多款主流模型均无法有效抵御；

2. **非结构化网页DOM场景**：攻击成功率浮动区间为33%~100%，页面结构简单时可实现百分百攻击成功；

3. **传统防护对抗测试**：无防护基线攻击成功率为49.1%，主流输入护栏防护无任何防御效果，仅严格全链路数据流跟踪可100%阻断攻击，但会导致AI任务完成性能暴跌至基线值的36.5%（对比无防护时完成性能86.5%），严重影响业务可用性；

4.**实测典型危害场景**：搭载Claude的Chrome浏览器智能体被诱导触发误支付操作；Claude Code、OpenAI Codex被伪造维护者评论欺骗，自动将含后门的恶意代码合并至主代码分支。

**四、受影响工具与模型：**

**底层框架缺陷，无单一厂商幸免**

本次漏洞属于AI智能体框架底层结构性缺陷，非单一模型训练问题，覆盖主流厂商产品，具体风险分级如下：

**（一）高风险工具**

1. 网页浏览智能体：Chrome内置Claude、Google Antigravity、开源Nanobrowser；

2. 代码开发智能体：Claude Code、OpenAI Codex、Gemini CLI。

**（二）受影响模型**

GPT-5.2、GPT-5-mini、Claude Opus 4.5、Claude Sonnet 4.5、Gemini 3 Pro、Gemini 3 Flash。

**（三）具备天然缓解能力产品**

ChatGPT Atlas浏览器：采用随机不可预测页面元素ID设计，这一措施在研究团队的基准测试中可将攻击成功率从49.1%降至28.7%，仅能缓解风险，无法完全阻断ADI攻击。

**五、检测盲区分析：**

**现有安全体系三重短板**

ADI攻击能够大规模得逞，核心是利用了当前AI安全防护体系的结构性盲区，主要包含三大短板：

1. **防护逻辑错位**：现有提示注入检测工具仅聚焦识别显性恶意命令文本，无法识别无指令、纯元数据篡改的隐蔽攻击；

2. **数据边界缺失**：绝大多数AI智能体框架未做可信数据与不可信元数据的隔离校验，外部未校验污染数据可直接混入智能体可信上下文；

3. **静态检测失效**：传统代码扫描、网页安全检测仅识别显性恶意代码，无法识别隐藏在字符、分隔符中的隐性篡改行为。

**六、防御建议：**

**分层落地，从即时整改到长期架构升级**

**（一）立即排查动作**

全面梳理所有生产级AI智能体依赖的元数据来源，包括页面元素ID、评论作者信息、工具调用返回记录、测试校验结果等；全面停用顺序式、可预测式资源标识符；核验现有AI安全防护体系，确认是否针对元数据篡改场景完成专项测试，仅适配传统提示注入的防护机制会产生虚假安全认知。

**（二）短期缓解手段**

1. 替换资源标识体系：将顺序化、可预测的页面及资源ID，统一替换为随机、不可猜测的标识符，降低篡改利用风险；

2. 固化工具执行数据：对代码仓库的工具测试结果、安全扫描报告、审核记录等数据进行密码学绑定，禁止随意篡改、伪造；

3. 部署临时防护架构：落地智能体沙箱、双大模型分层架构，隔离可信业务逻辑与不可信外部内容，有效降低攻击成功率。

**（三）长期战略改造**

ADI攻击属于底层框架结构性漏洞，无法通过简单补丁修复。企业需将全链路数据流跟踪、可信与不可信数据流隔离作为AI安全核心建设方向，平衡安全防护效果与AI业务性能损耗；同步迭代威胁模型，将元数据篡改、上下文污染列为独立高危风险类别，纳入常态化安全管控。

**（四）配套CSA官方资源落地加固**

1. 参考《Agentic AI红队指南》，扩充元素ID伪造、作者身份篡改、工具记录伪造等专项测试用例；

2. 依据《大模型系统安全授权规范》，搭建代码PR场景旁路校验机制，拦截虚假审核记录；

3. 依托MAESTRO智能体威胁建模框架，精准定位业务中ADI风险入口，完善全链路风险管控。

**七、厂商披露反馈**

研究团队在报告发布前，已提前向Anthropic、OpenAI、Google、Nanobrowser四大相关项目团队同步漏洞细节与验证方法。其中，Anthropic、OpenAI、Google均确认漏洞真实有效、风险属实，但截至报告发布，暂无厂商发布正式修复补丁及迭代计划；Nanobrowser项目未做出任何回应。目前，研究团队已公开完整测试基准与攻击代码，面向全网安全厂商及科研社区开放，供各界复现验证、研究防御方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEiaERgznMGzsh4yI67X8icqkHsRQ74tSMdFF3PhPX1Ng6qmQo6DbyYkecLxqXc917FTK7uTyeR9okib6tz2vfWS87sdBoYumy2VRM/640?wx_fmt=png&from=appmsg)

**八、结语**

随着AI智能体全面深度融入网页交互、代码开发、自动化运维等核心业务场景，ADI智能体数据注入攻击开辟了超越传统提示注入的全新高危攻击面。过去两年行业重点搭建的指令级AI防护体系已完全失效，无法应对元数据层级的隐蔽篡改攻击。企业需彻底重构AI智能体的信任边界认知，摒弃单一的提示词安全防护思维，通过即时排查、短期缓解、长期架构升级的分层方案，全方位加固AI智能体运行环境，杜绝AI智能体成为新型供应链攻击、数据泄露的核心突破口。

**关注公众号，回复关键词** **“****ADI”**

即可获取报告完整版

---

**大会预告**

2026 CSA大中华区大会暨AI+安全大会将于9月11日在北京清华大学举办。大会由云安全联盟大中华区（CSA GCR）与清华大学联合主办，以“智序·本体：以可信智能时代筑基”为主题，聚焦AI安全、人工智能治理、产业应用及人才培养等核心方向，汇聚政产学研各界力量，共同探索可信智能时代的发展路径，推动人工智能安全生态建设。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEg9llYJljJ9CNGdecVhTyGO2BRicH4T3QVibr7wdAj6ictoPoy27ag6SpGLtx6W4hIMnlECz0VccousaRcU459hibhpez5qmpe5ptA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEgsy9Cj8pqKbIAxRTrEtf8DvncKosR6o4jCwEYPPTv156O6kojJatRLhBiadU9msWurkECGLqM6icXwpiaERaoyoBMG7WjaPoRw9Q/640?wx_fmt=png&from=appmsg)

扫码报名CSA GCR大会

---

**阅读推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEiaZ33CBjyE2TCT5pL2BCLPcNUzST2IHLnj95EdwwUZ5mMPvUGB320bjrkFx9xUiaob9HR8NgcS7HYChVRhiaUc4FaTeMaBYUEAlo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwMTM5MDUxMA==&mid=2247512270&idx=1&sn=e273f6cf2c0ca5789a5dd5319889a421&scene=21#wechat_redirect)

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