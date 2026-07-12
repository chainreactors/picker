---
title: 06 AI Detection Engineering：让大模型辅助写 Sigma 与 YARA
url: https://mp.weixin.qq.com/s/9Ez4pObVxsIgpnZXgvnIxw
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:09:21.817891
---

# 06 AI Detection Engineering：让大模型辅助写 Sigma 与 YARA

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JEth9NwFY4FfUlW7tKAAq8nia7EtHCnyZQ52YeibbNDpM6yPzzn0zhFoyaibfhY40kfor91QXEI0aQ1Rn19DicQZsicXX0CM9mbWMGibaicLeSx0yo/0?wx_fmt=jpeg)

# 06 AI Detection Engineering：让大模型辅助写 Sigma 与 YARA

lidasimida
lidasimida

安全学习之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

重要边界：本文只面向防守运营、内部治理、授权验证和安全建设；不提供攻击复现步骤、payload、绕过脚本、凭证获取或真实目标入侵路径。

# 目录

·先给结论：AI 可以辅助起草检测规则、字段映射和测试思路，但规则能否上线取决于样本验证、误报评估、覆盖范围和回归测试。

·一、对象和机制：SOC 不是告警收件箱，而是证据系统

·二、看什么材料：每个判断都要能回到证据

·三、AI 如何介入：只做证据工程，不做最终裁判

·四、资料核验：本文判断依赖哪些权威来源

·五、技术加深：真正决定成败的工程细节

·六、案例拆解：材料、AI、人工验证和闭环

·七、扩展场景：生产环境里更复杂的问题

·八、落地实施方案：从低风险场景开始

·九、上线检查清单：别让 AI 输出直接进生产

·十、读者最容易误解的问题

·专业术语注释

·参考资料

# 先给结论：AI 可以辅助起草检测规则、字段映射和测试思路，但规则能否上线取决于样本验证、误报评估、覆盖范围和回归测试。

Detection Engineering 不等于写一条查询。它是一套从检测目标、数据源、规则表达、样本验证、误报治理到上线回归的工程流程。AI 能减少起草和迁移成本，但不能跳过验证。没有样本、负样本和回归，规则文本再像样也只是草稿。

![](https://mmbiz.qpic.cn/mmbiz_png/JEth9NwFY4F7jXPt7lvjHmNkYPAsDUa6Py8sOZUnZb96nHKaicG4WPfxkAGU1ib3kePKzLyluQ4uAnxbpkcPhKzOsarRiaY5Mgmia9G7quRibSaQ/640?wx_fmt=png)

图 1：AI Detection Engineering：让大模型辅助写 Sigma / YARA核心链路

#

# 一、对象和机制：SOC 不是告警收件箱，而是证据系统

Sigma 更适合表达日志和 SIEM 检测逻辑，YARA 更适合表达文件、样本和字节/字符串特征。AI 可以帮助解释字段、起草逻辑和生成测试清单，但不能提供规避检测的细节，也不能把未经验证的规则直接上线。

一个可运行的 AI SOC 不是把所有日志丢给模型，而是先把对象、字段、实体、权限和证据边界固定下来。模型可以帮助人更快组织材料，但不能替代数据治理、权限设计、人工审批和事件响应责任。

#

# 二、看什么材料：每个判断都要能回到证据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JEth9NwFY4HOLyWia2TEBvprwjibCaMMZcicex3C4lc8B3ReXyCRUDj5cEK1FicAJiayg45w8PNDcmjEXDyzfY6bFqUQYvh5qpxO5icJVY0Ld8MMk/640?wx_fmt=png)

图 2：AI Detection Engineering：让大模型辅助写 Sigma / YARA对象-材料-判断矩阵

下面这张表把文章里的关键对象拆成材料、AI 任务和人工闸门。写 SOC 类文章时，只有这三列都能说清楚，结论才算站得住。

|  |  |  |  |
| --- | --- | --- | --- |
| 对象 | 看什么材料 | AI 适合做什么 | 人工必须验什么 |
| 检测目标 | ATT&CK 技术、历史事件、情报、漏洞利用行为 | 抽取行为模式 | 确认目标是否值得检测 |
| 规则表达 | Sigma、YARA、SIEM 查询、EDR 规则 | 起草和迁移语法 | 确认语义正确 |
| 验证样本 | 正样本、负样本、历史误报、回放日志 | 生成测试矩阵 | 确认误报和漏报 |
| 生命周期 | 评审、灰度、上线、回滚、版本记录 | 生成发布材料 | 审批和回归 |

#

# 三、AI 如何介入：只做证据工程，不做最终裁判

AI 在 SOC 中最稳妥的定位，是把分散材料变成结构化证据包。证据包至少包含：evidence\_id、source、timestamp、entity、summary、supports、does\_not\_prove、confidence、next\_question。`supports` 写它支持什么，`does\_not\_prove` 写它不能证明什么，这能显著减少模型把推断写成事实。

AI 输出默认分成四栏：事实、推断、待验证问题、反证记录。事实必须能回到来源；推断必须写依据；待验证问题不能冒充结论；反证记录要进入关闭原因或规则优化。这个分层比“让模型给一个风险等级”更慢一点，但更适合生产 SOC。

#

# 四、资料核验：本文判断依赖哪些权威来源

为了避免把 AI SOC 写成概念堆砌，本文把关键判断绑定到公开资料和可复核框架。资料只作为方法依据，不把厂商产品能力直接等同于企业落地效果。

|  |  |  |
| --- | --- | --- |
| 资料或框架 | 可以确认什么 | 对本文的约束 |
| Sigma Specification | Sigma 规则由 title、logsource、detection、condition 等结构组成，用于表达日志检测逻辑并转换到不同后端。 | AI 写 Sigma 必须同时处理字段语义和后端转换差异。 |
| YARA Documentation | YARA 用字符串、条件和模块描述文件/样本特征。 | YARA 更适合样本和文件特征，不应和日志查询混用。 |
| ATT&CK | 检测目标通常要映射到具体技术和数据源。 | 规则生成前先定义行为目标，而不是先让模型写语法。 |

#

# 五、技术加深：真正决定成败的工程细节

Detection Engineering 的主语是“检测目标”，不是“规则文本”。先明确要检测哪种行为、需要哪些数据源、哪些字段可用、哪些合法业务会误报，再决定写 Sigma、YARA、KQL、SPL 还是 EDR 规则。

AI 适合做四类事情：把事件复盘转成检测目标，把字段字典转成规则草稿，把规则迁移成目标后端语法，把测试样本转成回归清单。AI 不适合跳过样本验证直接上线。

规则质量要看 precision、recall、coverage、cost、stability 五类指标。只看“能不能命中样本”会导致过拟合；只看“误报少”又可能漏掉变种。

技术上要特别警惕一种假象：模型把材料说得很顺，并不代表材料已经足够。SOC 场景里的可靠性来自字段、来源、权限、时间、证据强度和人工复核，而不是来自语言表达本身。

#

# 六、案例拆解：材料、AI、人工验证和闭环

## 案例一：把一次确认事件转成 Sigma 草稿

材料怎么收：确认事件证据包、原始日志字段、ATT&CK 映射、误报样本。

AI 怎么做：抽取行为条件，起草 Sigma 逻辑和字段映射说明。

人工怎么验：验证字段是否存在、条件是否过宽、误报是否可接受。

修复怎么闭环：进入规则评审、灰度发布和命中监控。

不能证明什么：AI 生成的规则不能直接上线。

## 案例二：YARA 规则如何避免过拟合

材料怎么收：授权样本、同类变种、正常软件样本、字符串和元数据。

AI 怎么做：整理候选特征和测试矩阵，不输出规避思路。

人工怎么验：确认特征稳定性、误报范围和样本合法来源。

修复怎么闭环：保留版本、测试集和回归结果。

不能证明什么：命中 YARA 不能单独证明恶意，需要上下文。

## 案例三：规则迁移为什么不能只靠模型翻译

材料怎么收：原 Sigma、目标 SIEM 字段、数据样例、查询结果和性能数据。

AI 怎么做：提出字段映射和语法迁移草案。

人工怎么验：运行查询，检查字段类型、时间窗口、性能和误报。

修复怎么闭环：记录迁移差异和回归结果。

不能证明什么：语法可运行不代表语义等价。

#

# 七、扩展场景：生产环境里更复杂的问题

## 扩展场景 1：Sigma 字段迁移失败

现场材料：源规则使用 process.command\_line，目标 SIEM 字段叫 CommandLine 且大小写和分词规则不同。

AI 介入：AI 给出字段映射候选和转换后查询草稿。

人工校验：检测工程师用样例日志验证字段类型、大小写、分词和时间窗。

闭环产出：形成后端转换备注，避免下次重复踩坑。

## 扩展场景 2：YARA 规则过拟合

现场材料：规则只命中一个样本，因为字符串来自编译路径或临时文件名。

AI 介入：AI 提醒候选特征可能不稳定，建议补正样本和负样本验证。

人工校验：样本分析人员确认字符串稳定性、家族共性和误报范围。

闭环产出：将规则改为多条件组合并保留测试集。

这些场景的共同点是：AI 先把复杂材料组织成可讨论对象，再由人确认事实边界和业务影响。只要跳过人工校验，AI SOC 就会从提效工具变成风险放大器。

#

# 八、落地实施方案：从低风险场景开始

|  |  |  |
| --- | --- | --- |
| 阶段 | 具体做法 | 产出标准 |
| 定检测目标 | 写清要检测的行为，不从工具语法开始。 | 目标明确。 |
| 准备测试集 | 至少有正样本、负样本、历史误报和边界样本。 | 能验证。 |
| AI 起草 | 让模型输出规则、字段解释、测试清单和不确定点。 | 减少重复劳动。 |
| 人工上线 | 评审、灰度、监控命中和回滚。 | 工程闭环。 |

落地时不要从自动封禁、自动隔离、自动删除这类高风险动作开始。更稳妥的顺序是：先做摘要和证据包，再做历史案例检索和检测规则辅助，最后才在低风险 playbook 上做受控自动化。每一步都要保留输入、输出、人工修改和回归结果。

#

# 九、上线检查清单：别让 AI 输出直接进生产

|  |  |  |
| --- | --- | --- |
| 检查项 | 怎么检查 | 合格标准 |
| 行为目标 | 先写检测对象和 ATT&CK 映射。 | 不从语法开始。 |
| 数据源确认 | 确认日志源、字段、采集延迟、保留周期。 | 查询能跑。 |
| 测试集 | 准备正样本、负样本、历史误报、边界样本。 | 上线前可回归。 |
| 发布流程 | 评审、灰度、监控、回滚、版本记录。 | 规则生命周期完整。 |

检查清单不是为了增加流程负担，而是为了把模型输出从“看起来合理”变成“可以上线承担责任”。如果某一项无法检查，说明当前能力还应该停留在辅助阶段。

#

# 十、读者最容易误解的问题

## Sigma 和 YARA 区别是什么？

Sigma 面向日志检测，YARA 面向文件和样本特征。

## AI 能自动写规则吗？

能起草，不能替代验证和上线审批。

## 为什么规则需要负样本？

负样本用于估计误报，防止规则过宽。

## 什么叫规则过拟合？

只匹配单个样本特征，遇到变体失效或误报正常样本。

## 规则上线前要看什么？

语义、字段、性能、误报、覆盖范围和回滚方案。

## ATT&CK 映射有用吗？

有助于说明检测目标，但映射本身不是验证。

## AI 生成规避建议怎么办？

删除，不进入正文或规则评审材料。

## 规则生命周期怎么管？

版本、评审、灰度、命中、误报、回滚、复盘都要记录。

#

# 专业术语注释

·\*\*SOC\*\*：Security Operations Center，安全运营中心，负责监测、研判、响应和复盘安全事件。

·\*\*SIEM\*\*：Security Information and Event Management，集中采集、关联和查询安全日志的平台。

·\*\*SOAR\*\*：Security Orchestration, Automation and Response，用于编排响应流程和自动化动作。

·\*\*EDR\*\*：Endpoint Detection and Response，终端检测与响应系统。

·\*\*XDR\*\*：Extended Detection and Response，跨终端、网络、云和身份的扩展检测响应。

·\*\*ATT&CK\*\*：MITRE ATT&CK，描述攻击战术、技术和过程的知识库。

·\*\*Sigma\*\*：跨平台日志检测规则格式。

·\*\*YARA\*\*：用于文件和样本特征匹配的规则语言。

·\*\*Detection Engineering\*\*：围绕检测目标、规则、验证和生命周期的工程实践。

#

# 参考资料

·SigmaHQ Sigma, https://github.com/SigmaHQ/sigma

·YARA documentation, https://yara.readthedocs.io/en/stable/

·MITRE ATT&CK, current website version v19.1 since 2026-04-28, https://attack.mitre.org/resources/versions/

·Elastic Common Schema reference, https://www.elastic.co/docs/reference/ecs

·SigmaHQ Sigma Specification, https://github.com/SigmaHQ/sigma-specification

预览时标签不可点

作者提示: 内容由AI生成

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pYEnsj4YvnYs2BY22GDib8jhEE8xY5526beMxibcJGWEp2DTvp7C8kGhmsXsDcsSZbibibDibII8uPW27ibynSMJYbyg/0?wx_fmt=png)

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