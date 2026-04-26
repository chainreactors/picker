---
title: 速度与激情2-宝剑到手，基于deepseek V4 构建网安攻防图谱
url: https://mp.weixin.qq.com/s/uEYsub5fGiR1Dw1D8HV6zw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:58:20.720399
---

# 速度与激情2-宝剑到手，基于deepseek V4 构建网安攻防图谱

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibANIaIJODOnmXEFW51Hib9LAhB3A18iaqMc4XQF0p8Vux59jqPqyH8nbibic2Xr9MibI6fkV83ibrS5qL3G1dI4lVvG6jILEHgJZJbwOBDsBCgXFU/0?wx_fmt=jpeg)

# 速度与激情2-宝剑到手，基于deepseek V4 构建网安攻防图谱

原创

DIMU
DIMU

AI简化安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOnKTVjsV9whflMoMLT0sFaAhIHlEfElzaDyThum6DXiagd5icRBRQ8QEalicvWkJewzgdaExoxDLgnJwbrgy8O5ynA0FXBiaGUibKa4/640?wx_fmt=png&from=appmsg)

《速度与激情》**第1篇**讨论的是：用 **OpenClaw 将安全售前能力产品化**——以 **Skill 契约、结构化规划、规范驱动成稿** 为主轴，将方案与汇报材料**从长周期制作压缩为可复用、可复现的交付**（见同系列[速度与激情1：基于openclaw的安全方案智能体](https://mp.weixin.qq.com/s?__biz=MzI5NTQ3NzIxMw==&mid=2247486255&idx=1&sn=1fdcbfec76b13bde0dda74729d9f541d&scene=21#wechat_redirect)）。**第2篇**沿**同一技术栈，但新建workspace-cyber-ad-atlas**工作区，聚焦**安全工程侧**——依靠deepseek V4将 **网安攻防图谱** 建成**可引用的知识层**：以**业务流**组织场景，用**实体与外部标准**（ATT&CK、ATLAS、OWASP、NIST/ISO 等）建立可追溯映射，并配套**数据域与智能体域的交叉分析**及**可交付的威胁建模样例**。

先看效果：演示流程为原知识关系图谱--智能体攻防知识-数据安全攻防知识-智能体&数据安全交叉分析--政务咨询数字人系统威胁建模

在智能体系统（RAG、工具链、多角色数据）已成为常态的背景下，**威胁建模**的难点往往不在于缺少名词（ATT&CK、OWASP LLM/Agentic 等），而在于**首笔如何与真实部署对齐**：攻击技术、数据生命周期与**具体控制**之间的**可验证关系**是否能在同一套**架构视图**中展开。

**提示注入、过度代理、供应链与记忆/上下文面风险**等，若仅分散在不同文档中叙述，**数据侧与模型侧**可能出现**对同一类事件的两种表述**；若缺少**业务流**索引，**评审与整改**也易停留在条款对照层面。

本实践在 **OpenClaw** 中建设独立 **网安攻防图谱** 工作区：以 **LLM Wiki** 组织 **场景、业务流、攻击/防守实体** 与 **主题页**，并将 **CAA-ATK / CAA-DEF** 与 **OWASP、MITRE ATLAS、NIST AI RMF / ISO 42001 等** 形成可引用的**外键**关系。在样例上，选取**政务咨询数字人**类架构，完成**从数据流、到威胁路径、再到控制回映**的**端到端**梳理，用于验证该知识层**在评审与交付中的可用性**。

在节奏上，**数小时级**可形成**可演示的目录与主案例骨架**；后续**持续 ingest** 标准与场景区块，等价为**在既有图谱上增边、增点**，而非另建文档池。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOnY34gWNiaB4neo5NuLB2NDmxezKlOCwzcvrzwr2BriakFBPe8AR7h9rcRwfOCNLLsXN9hmwZXibwJANcNVO88bLY3UGZttibjDZsE/640?wx_fmt=png&from=appmsg)

## 二、工程侧说明：DeepSeek V4 与 OpenClaw 在「思考模式 + 多轮/工具」下的兼容现状

**DeepSeek V4** 发布后，本工作区将主模型**切换至 V4 代际**，用于**表格补全、交叉引用扩写、长文组织**。需要说明的一处**工程现象**：在**开启「思考 / reasoning 模式」**并叠加**多轮对话与工具调用**时，**接口可能返回 HTTP 400**。这与 **API Key 或 model 标识误配** 通常**不属同一类问题**；根因在于 **DeepSeek 在思考模式下对多轮请求**所要求的**上一轮流式推理内容回传**与当前 **OpenClaw 所采用的「OpenAI 兼容对话栈 + 内嵌智能体 + 历史拼接」** 在行为上**未完全对齐**，导致**请求被服务端按协议拒绝**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOmnHGV8E1OicwVbVWCAgpcB4S2BCMugjdH14KZ4UQ2tqrmufVeDunPiaqEnuWutcjBedFBLvDoricYp1rBKwJXn45dsAC26hzicS14/640?wx_fmt=png&from=appmsg)

## 三、知识层形态：可导航的互链网，非静态文档堆

知识层至少包含**四层**可组合使用：

1. 1. **场景（Scenarios）**：明确边界与适用前提；2. **业务流（Flows）**：将**生命周期 / 建设阶段**与资产、信任面绑定；3. **攻击/防守实体**：具备 **ID、ref、与缓解关系** 的可点击定义；4. **主题页**：如 **OWASP Agentic T1–T17 与缓解矩阵、ATLAS 交叉、防守对照表、威胁建模样例** 等，支撑**一次评审所需的多张视图**。

**总目录**为入口；在 **Obsidian 等**工具中，**图视图上的边**反映**互链强度**，**稀疏处**可视为**待补的建模任务**，而非版式问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkmVWMC8slsT90Z25iaeD71j77fWqH72mcqs7o4K8iaWXpAWibgcwlYLDq9kQCBRDiaOftozy7FsS6PXd8OXSiaISs1mZc2xZtyqj4s/640?wx_fmt=png&from=appmsg)

## 四、智能体安全：在业务流上挂载攻防与缓解

**智能体安全攻防图谱** 将 **CAA-ATK-AGT-** 与 **CAA-DEF-AGT-** 的**缓解关系**以 **Mermaid 总图** 呈现，便于**先总览、再下钻**至各实体页。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkvdZ5ibPicPe8eDWlYwpr0SoV5uAtLpMleecibZv5o2XbfPzCiaA2NsCl2o1rRH3JiaiauRFwHbHxzwiaEEvKX3Jf0ZPznppQdoEXbuE/640?wx_fmt=png&from=appmsg)

读图时建议**优先核对三类接口**：**输入与编排**（与注入、意图、身份相关面）；**工具与下游**（**模型输出不得单独构成授权**）；**多智能体 / 互操作协议**。

## 五、数据安全：独立生命周期，同一套方法论

**数据安全攻防图谱** 与 **六阶段数据生命周期** 业务流**配对**：**CAA-ATK-DAT-** 与 **CAA-DEF-DAT-** 成组出现，**治理叙事**可**一图**对齐**采集、传输、存储、处理、共享、销毁** 各环节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOmGQTyNZRnQQiccswp43tlsC6qj44Y0d15nR0Snyib0M8iamfmE83E9iaW19y0zvBOw3GY3wdPquqctJZ4XsQLbgCZc7UCpTIc3w4M/640?wx_fmt=png&from=appmsg)

**与上一节对读**的价值在于：**同一条被污染或不可信数据**，在**数据工程叙事**中常归因为 **ETL/管道/完整性**，在**模型与检索叙事**中则与 **向量库、RAG、记忆/上下文** 勾连；**不建立跨域映射**，**整改验证**易**分段闭环、整体失真**。

## 六、跨域：训练数据供应链上的复合链

在 **「AI 训练数据与供应链安全」** 的交叉专页中，**同一安全事件**在**数据域与 AI 域**可有**不同事故命名与指标**；文中给出**复合攻击链**（**含 Mermaid 子图**）与**缓解对照**，用于**联合评审**时**共用语境**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkJXrBibPFDPMTuPDbASzqBvX49fKrsWVmYUWvPUwZrLwJ7eqcjynJTIy8DDKt2h9yNP8fxTD7GiaGYVyJ2TymwK3utoe7ICrRiaM/640?wx_fmt=png&from=appmsg)

对甲方或监管沟通时，可简化为**三条可验收命题**：**仅修复管道/ETL 不等同于**向量与训练入侧已恢复可信；**仅增加对话与提示侧防护** 不解决**元数据、源数据与入模数据** 的可信与溯源；**两域**需**同一条**整改与**验收**标准。

## 七、样例：政务咨询数字人系统的威胁建模

在 **「政务咨询数字人」** 案例中，**公众入口、ASR/NLU、RAG、大模型、TTS、可选工具、内容运营与 ETL、政务业务与第三方运维** 等**组件与数据流** 均映射至 **CAA-ATK / CAA-DEF** 与数据侧实体，**形成可对照检查清单的完整路径**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOlBZvONZ6I2hEsIGibntwdMFibUibBRJYk6D19CU4vQwdFDG4XvVgMGwU9TfrVOFkQ3ic45Uv1RpyxfWLrDyuo5vGjokPHu1BfwFOc/640?wx_fmt=png&from=appmsg)

**可写入汇报或评审纪要的归并要点**包括：

公众与声誉相关面**与**提示注入/人类侧社会工程面**同卷**；

**RAG 与内容发布通道** 作为**知识面总控制点**，**数据完整性与元数据、模型/记忆面投毒** 宜**联测**；

**已认证个人数据** 与**非人身份/特权（NHI）** 与**数据域访问与审计** 宜**同屏**表述，**避免**「业务故事」与**「技术控制」** 脱节。

## 八、能力边界与适用场景

本知识层可直接支撑：**威胁建模工作坊**、**合规与标准对拍**、**红队/蓝队基于长链的想定**、**安全产品/云服务选型时的控制覆盖对比**、**向管理层的双场景图谱 + 跨域链 + 单一样例的叙事结构**；在叠加 **OWASP Agentic、ATLAS 技术级交叉、NIST/ISO 防守矩阵** 时，**材料厚度来自可引用的外键，而非单端叙述的堆叠**。

与 **第1篇** 的售前工作区在**工作区/目录**上**隔离**（**多域 Wiki 分库** 约定），**事实与材料分层**，**避免**同一事实在**两套**知识层中**重复或冲突**。

## 九、后续可扩展域（规划占位）

**工控/OT、供应链独立场景深化、多云与非人身份（NHI）专章** 等，可在**同构**的 **Wiki** 中**增场景**而不改**元模型**；**数小时至数日级** 可复现的，是**建库方法**，**非一次性的版式**。

## 十、总结

**被动引用标准**与**主动将攻击—防守—业务流写成可点进去的网络**，是两种工作方式。当**数据域与模型域的因果链**能在**同一张可复核的网**上指认，**评审盲区**会显著外显。建议**以**「单场景、单条主业务流、有限实体、一张总图、一个可讲透的案例」**为最小闭环**，**再水平扩展**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkJsibJQdJGLnriaOhyiaU0sKNqTnBxj4ic9yuVO55azIiadMCtba7ianeicTXZrgvRX9eRI5qDANaMeiaEnZ58o88XsibhbuYY7kuBPbicw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

AI简化安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

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