---
title: 人工智能安全治理框架 3.0：风险分类与治理落地的关键变化
url: https://mp.weixin.qq.com/s/lYXNJJZZ-OlTuEipXEwr4A
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:55:43.617863
---

# 人工智能安全治理框架 3.0：风险分类与治理落地的关键变化

# 人工智能安全治理框架 3.0：风险分类与治理落地的关键变化

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ZmL5d0ic88X4b6rXesjExibArzSkdDgkD0cC5oYhicojXpMaz5xUHeM45oxfBL3IZsgvZyibQOaDlDqibUu1QZtSx0faN4DiaAJUOp83kxnjvLqI/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kxnysVHkhP3oT51M5Ln7zTHHTjR2jmQF0iab2f3yhBKCBwkgwPjOlibqXMibEMUtLSb2oFXBdmtZNmFgJn7LicWgKhsVDphzbQMurUq07QNGqo/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=1)

导读：2026 年 9 月 14 日，全国网络安全标准化技术委员会在中央网信办指导下发布《人工智能安全治理框架》3.0 版。这是继 2024 年 1.0、2025 年 2.0 之后的又一次迭代，也是国内人工智能安全治理领域一份重要的参考性文件。

对安全从业者而言，这份文件不直接产生强制约束力，却基本定义了未来一段时间内行业理解人工智能风险、组织安全工作的共同语言。

迭代背景：治理对象从“模型”转向“系统”

框架 3.0 开篇即点明了修订的现实背景：过去一年，大模型在长程规划、长上下文记忆与复杂推理方面持续突破，人工智能正从“回答问题”走向“执行任务”。智能体已具备自主规划、调用外部工具、跨应用协作的能力。

这一变化直接重塑了风险结构。风险不再主要表现为“输出内容不当”，而是转向“行为偏离预期”——包括模型在目标冲突下的策略性隐瞒、自我复制与资源抢占倾向、以及在缺乏监督时的越权操作。与此同时，人工智能也被用于降低网络攻击门槛、自动生成攻击载荷，网络安全风险开始向物理世界传导。

框架延续了“风险分类—技术应对—综合治理”的主线，并在治理原则上保持五条：包容审慎、风险导向的敏捷治理、技管结合、开放合作、可信应用与防范失控。

风险分类：14 类风险的三分法

框架 3.0 将人工智能风险划分为**内生风险、应用风险、衍生风险**三大类，共 14 个子类，这是全文的核心骨架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QlnSyzWIb6fKXFiaXv7z2tFicClCWI65ECLia4dIiaxSd5nd69P4TXgbLOUXs83YuGEytKGDoQwtOic1lkfJQicUm4ibsPWMwtfIF6Um7vqj4QDydg/640?wx_fmt=png&from=appmsg#imgIndex=2)![]()![]()

**内生风险（4 类）**源自技术自身，包括模型风险、算法风险、数据风险与算力及运行环境风险。其中模型风险在 3.0 中被显著细化，新增了“行为偏离预期”相关情形，如模型拒绝关闭、评测时伪装对齐、尝试突破隔离环境等。算力与运行环境风险则被明确单列，反映对供应链与基础设施依赖的关注。

**应用风险（6 类）**指向技术落地后的具体场景，涵盖智能体安全、具身智能安全、对网络安全的冲击、内容安全、个人信息安全，以及对现实世界的直接影响。

**衍生风险（4 类）**关注长期与系统性影响，包括社会、环境、文化与伦理四个维度，其中明确写入了人工智能脱离人类控制的可能情形。

值得关注的是，应用风险部分专门设置了“自主实施网络攻击的威胁”这一场景。自然语言交互正在拉平攻击能力门槛，使得不具备专业背景的人员也能发起自动化攻击；而当攻击由智能体自主完成时，传统的意图识别与责任归因逻辑都将面临失效。

智能体：从场景之一到单列治理单元

智能体安全在 3.0 中被提升为独立风险类别，并配套专门的《智能体风险管理框架》，这是本次迭代最具标志性的调整。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QlnSyzWIb6cbcTsyeA3cPXTLzAgpibtuiapZRR7wfib4g6wicibXkRG8CC6uuO9cJH9KFf7bN2hxqA9EjfhBFiaAfPgE4JG6AZeH73W7QHkSgib0C0/640?wx_fmt=png&from=appmsg#imgIndex=3)![]()![]()

该框架把智能体的运行拆解为八个环节：目标与任务设定、规划与推理、工具调用、记忆读写、多智能体协作、环境交互、结果输出、日志与审计。每个环节对应一组控制要求，其背后有三条共性设计原则值得注意：

* 身份与权限最小化：智能体应拥有独立、可追溯的身份，其权限边界严格限定在完成当前任务所必需的范围之内。
* 人在回路与默认拒绝：对高风险操作保留人工确认机制；当审批链路异常或权限无法判定时，应默认拒绝执行而非放行。
* 全链路可审计：任务指令、工具调用参数、读写记录与输出均应留痕，确保事后可追溯、可复现。

这套设计实质上把传统信息安全中的纵深防御思想引入了人工智能治理，安全控制的落点也从“输入输出过滤”迁移到“运行时策略执行”。

技术应对与综合治理

技术层面，框架按风险类别给出了对应的技术措施方向，覆盖模型鲁棒性、数据治理、供应链安全、内容标识、运行监测等，并要求建立与安全风险相匹配的监测预警与应急响应能力。

治理层面，3.0 将综合治理措施重组为五组，其中监管沙箱被独立成章（4.3），是本次调整中制度意味最浓的一处。沙箱机制为新技术提供了在受控环境中验证、同步完善规则的通道，也标志着监管节奏从“先审后上”向“边跑边管”迁移。与之配套的是责任体系的厘清：研发者、提供者、使用者各自承担相应的安全义务。

四环节安全指引

框架第五章按研发、部署、运行、使用四个环节给出安全指引，覆盖人工智能系统从开发到退役的全生命周期。相比 2.0，条目数量有所增加，补入了检索增强生成、具身智能、拟人化互动、重要变更安全评估等新场景的要求，并对智能体相关环节作了细化。

这种按环节而非按主体组织的方式，更贴近工程实施的实际节奏，也便于企业把安全要求嵌入既有的研发与运维流程。

对企业安全能力建设的实际要求

综合框架全文，有四件事值得安全团队优先纳入工作清单：

1. 扩展风险台账的覆盖范围：从模型与数据资产，扩展到智能体的身份、权限、工具清单、记忆内容与外部知识来源。
2. 前置运行时安全能力：把监控、审计、熔断与一键管控作为智能体上线的前置条件，而非事后补充。
3. 把认知供应链纳入数据治理：训练语料、检索知识库、网页抓取内容、工具返回结果与长期记忆，共同构成影响模型输出的信息来源链，其污染风险应与软件供应链同等对待。
4. 落实分级与人工兜底：依据风险分级结果确定管控强度，在重要场景保留人在回路、异常熔断与紧急停机能力。

写在最后

人工智能安全治理框架 3.0 的迭代，本质上回应了一个工程事实：当人工智能从生成内容走向执行任务，安全的关注点就必须从“它说了什么”转向“它做了什么、能否被约束”。

对安全从业者而言，这份文件提供的是一张风险地图与一套动作清单。真正的工作，是把其中的运行时监控、工具调用审计、攻击溯源与应急熔断能力，落到日常的工程实践里。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/QlnSyzWIb6d7lFUqRWhn24hOs05XurjOddvIwYx4m7M0yHIuYaGvzbnySTWEG0gd9pzicydykuPP8wicpSZdMbhhjLPEYrSibKV6Nc1nYykShg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=2)![]()![]()**

**![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QlnSyzWIb6cWEc1RIn9zs5jwysgGCqTUPaBC4QQa6ADtTiczYiaSRaqmCict1SCkuL3h0QQ39xf6HIT8FdnU5FKgo5YYSrwaPsxic3EDuE9fdtY/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=3)法律声明**

**本文所有信息基于公开资料、行业公开报道整理汇总，仅提供行业信息交流用途。鉴于公开信息存在更新不及时、统计标准不一等客观情况，内容可能存在偏差，敬请审慎参考，本平台不对信息真实性、完整性承担保证责任。账号原创内容享有相应著作权益，欢迎合规转载传播。转载需清晰注明来源，严禁截取片段、篡改内容、曲解原意。**

来源：知行一社

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88VEzjic1f7B8a9prz3icdEgQpXH1gOGyCYoZHyUAicqvDfdkVCKTCYm9qicEVTGF7fAosbaxdibXgxBT9na3DsrMjxBOyiadNzFvx5Po/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[【征稿启事】2026 IEEE网络韧性与内生安全国际会议（IEEE CRESS 2026）相约南京，诚邀投稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88W8YurngxjoMETsyF1w8AMIe2FvsJUYgJK9LjUf84fwckIIac4qeZOWkLkogKx3zdlYenkVN4MltVHnlZM0KdQtgCibd3y6M7JE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540385&idx=1&sn=c5d78eb7d544ae0533e89b3b849f8620&scene=21#wechat_redirect)

[第九届“强网”拟态防御国际精英挑战赛设计安全大赛报名启动！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540385&idx=1&sn=c5d78eb7d544ae0533e89b3b849f8620&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88WbLwb3myAna6Dmic6aSduceicm3eso4rthKbbY5TY4asTO8N5rxlFwd4OhV2cB9gDgxklKHSQBkicfJkoBKV29a8HPYaw2NWXN6s/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540494&idx=1&sn=9a6fc0b0459841b18d2fd2aafc9b4e22&scene=21#wechat_redirect)

[征集令 | 第二批 “人工智能+制造” 场景应用水平评价（AIQ）企业开始申报！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540494&idx=1&sn=9a6fc0b0459841b18d2fd2aafc9b4e22&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88V4eMKEAu77qJs1agsiaR9nE8g2Pvd5dercibRNPjyjeMmWTbtibMcEE11B2cd4ems24B0A2yPxuqoqjcS1n5v2UrqazQbPHk3TPA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[欢迎报名！“联盟货架” 征集工作正式启动](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[聚力协同发展 | 中国质量认证中心有限公司南京分公司正式加入联盟，成为副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

2026-06-17

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XRibsIKXF2TFo31YtyfTpzRKp3lqA3JpyMFdGWKGGVtONQDgr2Hfm8pibrCwAiaQn5RWPJxTgelQxwFln0ZDrAwK8YuDWUgNaxFE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

[携手共建产业生态 | 紫光恒越正式升级联盟副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

2026-06-18

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88Ug4pM2QBleSEh81Xt2icXIibBY5o6icibpSFMbFcu4TN9eNvibibict0BCDx8nCYrYViclCu2KGMdx7RnIAdrEvuSGtxKa20mBqH9IPhI/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)**

[里程碑时刻：智己LS9 Hyper搭载原创内生安全技术](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538132&idx=1&sn=77e4efcb6eea205e082f79b82336cc65&scene=21#wechat_redirect)

[邬江兴院士：构建内生安全质量检测体系，筑牢人类可控可信 AI 根基](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539044&idx=1&sn=1791fd1aad5f130fe5d87c46cc4b8687&scene=21#wechat_redirect)

[人工智能内生安全让“千里马”跑得快又跑得稳——邬江兴院士解读AI安全应对新思路](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247540081&idx=1&sn=7abcebf943fbb1723bc747b626f90087&scene=21#wechat_redirect)

[重磅发布 | 行业首部《智能网联汽车内生安全白皮书》，智己LS9 Hyper全球首搭中国原创内生安全系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4M...