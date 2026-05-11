---
title: 【OSG10变化】 Domain 1  风险管理框架（RMF）与合规治理
url: https://mp.weixin.qq.com/s/BFKkc7M8Mp6jGEn03xnXdQ
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:52:06.533068
---

# 【OSG10变化】 Domain 1  风险管理框架（RMF）与合规治理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zicib4mibicnb8xr3eeKu0KyhkXqxXSyLakGuDWjQ1fsVeDOxKYugZyXauDdmDRX8sbyiarWTnnoA34R6y3UvH0GIW9QxFPTibnuSYGxok5ic02iatc/0?wx_fmt=jpeg)

# 【OSG10变化】 Domain 1 风险管理框架（RMF）与合规治理

原创

CISSP Learning
CISSP Learning

CISSP Learning

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 在上一篇文章中，我们深入解析了Domain 1新增的威胁情报、供应链安全与零信任架构。本篇继续聚焦Domain 1的另一核心主题：风险管理框架（RMF）与合规治理。

       这是OSG第十版相对第九版变化最显著的领域之一。合规环境从"区域性碎片化"走向"全球化覆盖"，治理框架从"单一标准"走向"多元并存"，而风险管理本身也从定性描述走向结构化、可量化、可迭代的成熟体系。

**一、风险管理框架：从分散到统一**

**1.1****第九版的状态**

第九版（2015年）对风险管理的处理相对分散：

•风险管理的概念在多个章节中分别提及，缺乏统一的端到端流程描述

•主要依赖ISO 27005作为风险管理方法论参考

•对NIST SP 800-30（风险评估指南）和FedRAMP框架几乎没有系统性介绍

•框架之间的对比和应用场景指导不足

**1.2****第十版的重大升级：****NIST Risk Management Framework (RMF)**

第十版将NIST RMF作为Domain 1风险管理的核心框架进行了系统性引入，这是备考者必须掌握的重要内容。

NIST RMF的七步流程：

第十版新增的关键概念：

•信息系统授权边界（Authorization Boundary）：明确定义纳入RMF管理的信息系统范围

•安全控制基线（Security Control Baseline）：基于FIPS 200低/中/高影响等级选择控制措施

•Plan of Action and Milestones（POA&M）：记录已识别控制缺陷的修复计划和进度

•持续监控（Continuous Monitoring）：从一次性评估走向持续的风险管理生命周期

**1.3****风险框架的多元化：****ISO****、****NIST****、****COBIT****、****SABSA**

第十版显著扩展了框架并存的格局，备考者需要理解各框架的定位和应用场景：

各框架对比：

考试中的关键区分点：

•ISO 27001是"认证标准"，通过后可以声明符合性

•NIST SP 800-53是"控制目录"，详细列出每个控制的预期结果

•COBIT 2019强调治理与管理的分离（Governance vs Management）

•SABSA是一个分层的安全架构框架，从业务风险到技术实现的映射

**二、合规治理：全球化与碎片化的博弈**

**2.1****第九版的合规背景**

第九版写作时期（2011-2015年），全球合规环境相对简单：

•GDPR尚未生效（2018年才正式实施）

•中国《网络安全法》尚未出台（2017年）

•美国各州尚未大规模立法数据隐私（加州CCPA 2020年才生效）

•合规重点主要集中于PCI DSS、HIPAA、SOX等垂直行业标准

第九版对合规的描述偏向"了解法律法规"的基础层面，缺乏对合规体系设计和持续维护的深度讨论。

**2.2****第十版：合规治理的系统性升级**

第十版大幅扩展了合规治理的内容，将其从"了解法规"提升为"系统性合规体系设计"：

新增合规管理维度：

1.跨境数据传输合规

 - 欧盟GDPR的"充分性认定"（Adequacy Decision）机制

 - 中国《个人信息保护法》（PIPL）的域外效力

 - 美国CLOUD Act对跨境数据披露的要求

 - 数据本地化要求对全球运营企业的实际影响

2.隐私工程（Privacy Engineering）

 - NIST Privacy Framework的核心概念

 - Privacy-by-Design的六项基本原则

 - 隐私影响评估（Privacy Impact Assessment / DPIA）的实施流程

3.合同合规与第三方风险管理

 - 供应商合同中的安全条款设计（SLA、安全责任、违约赔偿）

 - 第三方合规认证的验证方法（SOC 2、ISO 27001、FedRAMP）

 - 外包环境下的合规责任归属

4.合规性监控与持续审计

 - 持续合规监控的技术手段（CASB、SSPM）

 - 自动化合规报告的生成逻辑

 - 合规差距评估（GAP Analysis）的标准化方法

**2.3****隐私法规的全球化覆盖**

第十版新增了大量全球化隐私法规的内容：

**三、安全治理体系：从政策到运营**

**3.1****安全策略层次结构的强化**

第十版对安全策略文档层次（Policy → Standards → Procedures → Guidelines）的阐述更加系统化：

新增内容：

•安全策略的维护生命周期：策略制定→审查→批准→发布→定期审查→废止

•策略与法规的对应关系矩阵：建立策略条款与具体法规的映射，便于审计追踪

•安全策略的传播与培训：明确策略必须传达到所有相关人员，并留下培训记录

•异常处理机制：当业务需求需要偏离安全策略时的正式审批和记录流程

**3.2****安全治理与业务战略的对齐**

这是第十版新增的重要主题，也是CISSP考试场景题的高频考点：

核心概念：

•安全功能必须与组织战略目标（Mission、Goals、Objectives）对齐

•安全投资必须基于业务优先级，而非技术驱动

•安全治理委员会（Security Governance Committee）的组成与职责

•安全在组织变革（Acquisitions、Divestitures、Mergers）中的角色

新增治理要素：

•安全策略委员会（Security Policy Committee）：负责策略制定、审查和更新

•首席信息安全官（CISO）的角色定位：向CEO、董事会或CIO报告，职责边界清晰化

•安全意识培训项目：年度培训计划、定期钓鱼测试、社交工程防御

•安全绩效度量：关键安全指标（KSI）的设计与监控

**四、****Due Care****与****Due Diligence****：从概念到实践**

**4.1****第九版的处理方式**

第九版对Due Care（应尽关注）和Due Diligence（应尽勤勉）的概念有提及，但缺乏实际应用的深度解析。大多数备考者对这两个概念的区分感到困惑。

**4.2****第十版的深化**

Due Care（应尽关注）：

•定义：组织和个人在处理信息资产时应尽的合理注意义务

•核心问题：采取了哪些合理的安全措施？

•典型场景：如果发生了数据泄露，能否证明"我们采取了合理的安全措施"？

Due Diligence（应尽勤勉）：

•定义：在决策前进行充分调查和评估的系统性过程

•核心问题：在做出决策前，我们是否充分评估了风险？

•典型场景：收购目标公司前，是否进行了完整的网络安全尽职调查？

实际应用场景：

•供应链安全：在选择供应商前进行安全评估（Due Diligence），在合作期间持续监控（Due Care）

•并购交易：交易前的网络安全尽职调查、交易后的安全整合计划

•数据泄露响应：能否证明组织尽了合理注意义务，影响法律责任认定

**五、****BCP/DR****与风险管理的整合**

**5.1****第十版的整合视角**

第九版将BCP（业务连续性计划）和DR（灾难恢复）作为独立主题处理。第十版从风险管理视角重新整合了这些内容：

•业务影响分析（BIA）：识别关键业务功能、恢复时间目标（RTO）、恢复点目标（RPO）

•恢复策略：基于风险评估结果选择恢复策略（热备/温备/冷备、云恢复等）

•测试与维护：BCP/DR计划的定期测试、更新流程与文档管理

**5.2****灾难恢复与风险应对**

**六、合规治理的考试重点与备考建议**

**6.1****高频考点**

根据第十版的内容，以下是Domain 1合规治理部分的高频考点：

5.NIST RMF七步流程：能够正确排序并描述每一步的核心活动

6.ISO 27001 vs NIST SP 800-53的适用场景区分：理解两者的适用范围和各自侧重点

7.Due Care vs Due Diligence的实际应用：给定场景，能判断是哪个概念的体现

8.跨境数据传输合规：理解主要法规（GDPR、PIPL、Cloud Act）的基本要求和数据转移机制

9.安全策略文档层次：能够区分Policy、Standard、Procedure、Guideline的层级关系和效力范围

10.安全治理与业务对齐：理解CISO的角色定位和安全委员会的组织结构

**6.2****备考策略**

11.建立框架体系：先理解各框架（ISO、NIST、COBIT、SABSA）的核心定位，再记忆具体细节

12.案例化学习：每个概念都尝试联系一个真实企业场景，帮助理解和记忆

13.对比记忆：通过表格对比相似概念（Due Care vs Due Diligence、Risk vs Control、Policy vs Standard）

14.关注新增内容：第十版新增的内容在考试中出现频率显著高于既有内容

**总结**

OSG第十版在Domain 1的风险管理和合规治理部分实现了从"概念介绍"到"体系化设计"的质量跨越。风险管理不再是孤立的流程，而是与业务战略、合规要求、供应链安全紧密集成的持续生命周期。合规治理也不再是单一法规的遵循，而是横跨多个司法管辖区、多种法规框架的系统性治理能力。

备考的核心策略是：理解框架之间的定位差异（而非记忆所有细节），理解概念在实际场景中的应用逻辑。

# 下一篇文章，我们将继续解析OSG10 vs 9系列的第四篇：Domain 3 安全工程——云原生安全、硬件安全与密码学应用的变化"。敬请期待。

本公众号各类文章仅供学习**交流*之用！*

![](https://mmbiz.qpic.cn/mmbiz_gif/tKJiatjhgPQicctRH5tiaBSpQfj6XrGWib7OiaqgBku2wAAgAWE0fh1InALLYoX0WLibr4qNQ6WLFQFp6OBNiciaSWX0tQ/640?wx_fmt=gif)

**更多资料获取，请加入【CISSP Learning】知识星球**

**![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zicib4mibicnb8xX4aOrjmQnibTSR1I8lcn57PNmkSw0FFu8lNYV8UdPFK2Jugl5ibpBUe2eFzFbw2xb0pmp0WN71x06I7zJAu6sZxJm5KvH0vw2g/640?wx_fmt=jpeg&from=appmsg)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tKJiatjhgPQicXA44Z0Ds3Y6mFjIeCTiczun0kFAFDmTge40H2PBHDL8NrMib0cdia9sza4jfOHkWM578KMZ4usSxew/0?wx_fmt=png)

CISSP Learning

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tKJiatjhgPQicXA44Z0Ds3Y6mFjIeCTiczun0kFAFDmTge40H2PBHDL8NrMib0cdia9sza4jfOHkWM578KMZ4usSxew/0?wx_fmt=png)

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