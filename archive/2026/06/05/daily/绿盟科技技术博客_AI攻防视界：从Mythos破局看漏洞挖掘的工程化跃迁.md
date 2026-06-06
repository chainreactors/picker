---
title: AI攻防视界：从Mythos破局看漏洞挖掘的工程化跃迁
url: https://blog.nsfocus.net/ai%e6%94%bb%e9%98%b2%e8%a7%86%e7%95%8c%ef%bc%9a%e4%bb%8emythos%e7%a0%b4%e5%b1%80%e7%9c%8b%e6%bc%8f%e6%b4%9e%e6%8c%96%e6%8e%98%e7%9a%84%e5%b7%a5%e7%a8%8b%e5%8c%96%e8%b7%83%e8%bf%81/
source: 绿盟科技技术博客
date: 2026-06-05
fetch_date: 2026-06-06T05:49:42.892632
---

# AI攻防视界：从Mythos破局看漏洞挖掘的工程化跃迁

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# AI攻防视界：从Mythos破局看漏洞挖掘的工程化跃迁

### AI攻防视界：从Mythos破局看漏洞挖掘的工程化跃迁

[2026-06-05](https://blog.nsfocus.net/ai%E6%94%BB%E9%98%B2%E8%A7%86%E7%95%8C%EF%BC%9A%E4%BB%8Emythos%E7%A0%B4%E5%B1%80%E7%9C%8B%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98%E7%9A%84%E5%B7%A5%E7%A8%8B%E5%8C%96%E8%B7%83%E8%BF%81/ "AI攻防视界：从Mythos破局看漏洞挖掘的工程化跃迁")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 88

日前，针对Mythos Preview模型的最新公开研究表明，该模型不仅能独立发现漏洞，更能将多个低危漏洞串联成完整的攻击链，形成更为严重漏洞利用链，并自动生成可直接验证的PoC代码，AI模型能力已推动漏洞挖掘从”单点识别”跃迁至”全链验证”。绿盟科技针对这一技术革新，提出AI驱动漏洞挖掘的方法论，完成工程化落地与成效验证。

### 1 Mythos对漏洞挖掘能力边界的影响

大模型本身具备代码理解、代码生成、测试生成和上下文推理能力，发现漏洞只是其代码能力在安全场景中的一个具体应用。当前主流大模型（GPT-4、Claude、DeepSeek、GLM 等）在代码理解、逻辑推理和漏洞模式识别方面表现突出，能够支撑针对 C/C++、Java、PHP、Go、Rust 等多语言目标的大规模审计。然而Mythos Preview的突破不只是“发现更多 bug”，而是把**漏洞挖掘从传统规则扫描推进到“语义理解+攻击者视角+可验证证据”**的阶段。

**1.1.规模化漏洞发现**

Mythos在漏洞发现维度展现出工业化级别的扫描与验证能力，规模化漏洞挖掘已具备显著产出，同时针对成熟大型工程仍能通过 Mythos 发现大量增量安全问题。

* **开源软件规模化扫描，90.6%真阳性率：**在Anthropic主导的开源扫描行动中，Mythos覆盖1,000余个开源项目，初步筛选出23,019个候选漏洞，其中高危/严重级别候选达6,202个。经独立安全研究员复核的1,752个样本中，真阳性率高达90.6%，最终确认1,094个高危或严重漏洞。

* **成熟工程的增量挖掘力：**在Project Glasswing首月实践中，合作伙伴借助Mythos合计发现超过10,000个高/严重级别漏洞。其中，Cloudflare单家企业即发现2,000个bug（含400个高/严重级）；Mozilla在Firefox 150版本中修复了271个漏洞，修复数量达到前代版本的10倍以上。

**1.2.自动化漏洞利用**

漏洞挖掘的核心价值不仅在于发现缺陷，更在于评估其可利用性（Exploitability）。Mythos带来的最大范式变革，是首次由大模型自主完成了从”漏洞触发”到”完整利用链”的跨越，且与其他模型形成断崖式能力差。

* **碾压级的实战转化率：**在针对 Mozilla Firefox JS 引擎实测中，Mythos 成功开发了 181 次可运行的漏洞利用代码，并实现了 29 次深度的寄存器控制，而Opus 4.6 在数百次尝试中，仅两次转化为可用攻击。

* **复杂环境工程化能力断代级领先：**在卡内基梅隆大学发布的ExploitBench（大语言模型网络安全智能体能力阶梯基准测试）中，针对41个V8 JavaScript引擎真实CVE漏洞，Mythos成功在21个漏洞上达到了最高利用层级（T1），表现远超公开模型天花板GPT-5.5（仅2个）。Mythos在复杂环境工程化能力上，已对通用大模型形成了显著的代差优势。

**1.3.自动化漏洞修复**

大模型在防守侧同样展现出极强的工程闭环能力。在漏洞暴露后，大模型能够基于上下文直接生成高可用补丁。在Project Glasswing实践中，自发布以来三周内，Opus 4.7已被用于修补超过2,100个漏洞。值得注意的是，企业自有代码的修复速度远快于开源项目。前者可直接内部迭代，后者仍需依赖志愿维护者的协调披露流程。这种”发现-修复”闭环的效率差异，将深刻影响未来漏洞治理的责任分配与响应机制。

**1.4.颠覆性成本下降**

以Mythos为代表的大模型极大地降低了发现和利用漏洞的成本与技能门槛，千万行代码量级的全面漏洞挖掘以往需要安全专家数月的时间，而Mythos的成本不足20,000美元，且在数小时内即可完成，单个漏洞识别在数分钟内即可完成且成本低于50美元。

### 2 AI漏洞挖掘实测数据分析

本次测试选取了两个已公开、已修复的高危 CVE作为测试对象：Jenkins CVE-2024-23897（CLI 任意文件读取）和 Apache ActiveMQ CVE-2023-46604（OpenWire反序列化 RCE）。并基于统一Scaffold（即围绕模型搭建的任务框架，包括prompt、工具集、约束条件和运行方式）、统一提示词、统一仓库版本下开展三轮独立运行。参测模型为 Claude Opus 4.6 与 GLM-5。

实测结果显示，Claude Claude opus 4.6以分钟级速度给出了专业审计员水平的产出，成功完成两个高危CVE的漏洞挖掘，补丁与官方一致。参测模型的能力差异主要体现在对显式威胁API定位能力、端到端的调用链追踪zenglingping和修复建议的可落地性上。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/545be6590d44419aa3109030cf3091e9~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202606051029036B9C49FFFA8098F4CE9F&x-expires=2147483647&x-signature=xbF%2FBympnP6ImGWOgh%2FCTq2wsoE%3D)

此外，独立安全机构AISLE的验证则呈现另一维度：3.6B参数的小模型在精心设计的Agent框架下也能复现高水平漏洞分析链，0.5B小模型甚至能复现DeepSeek-R1的思维链模式，DeepSeek-V3-0324等Agent能力大幅提升的模型也证明了优秀框架可充分挖掘模型潜力。当然，AISLE的scaffold包含入口点提示、漏洞类型引导等针对性领域知识。当框架回归通用、不预设漏洞方向时，模型自身的审计直觉与推理深度差异立即显现，这在本次实测数据中也得以应证。

综上，实测结果表明：**工程框架决定能力下限，模型自身决定能力上限。**模型能力是攻防对抗领域能力的核心基础，但围绕模型搭建的应用框架，包括Agent、prompt、Skills、工具集等，也会显著影响模型能力释放效果，定制化越强，模型间差距越小。

### 3 漏洞挖掘智能体工程化实践

为了稳定、可控、规模化的开展智能化漏洞挖掘工作，**绿盟科技漏洞挖掘智能体**，采用”控制面—执行面—工具链”三层解耦架构，以任务调度中枢为纽带，以容器化隔离为底座，以全过程事件流为脉络，构建可弹性扩展、可观测追溯的漏洞挖掘智能体的工程化体系。

* **控制面与执行面解耦，分布式任务调度机制：**审计平台负责任务创建与规则路由，将任务分发至目标队列；审计节点基于能力池完成注册，自主从队列领取匹配任务执行。节点故障时支持自动切换，有效消除了单点瓶颈。
* **审计节点容器化隔离，执行环境安全可控：**审计节点主进程（eagle-node）通过Docker隔离运行底层安全工具链，实现编排层与工具执行层解耦，提升稳定性、安全性与可维护性。

* **节点按需弹性注册，能力生态开放可扩展：**支持审计节点的自主开发与开源审计智能体的注册接入。通过持续心跳机制实现节点状态的实时感知，配套健康检查、自动下线、多租户隔离与权限管控等机制，保障开放生态下的稳定可靠运行。

* **阶段化执行链与产出物归档，可信约束：**定义审计节点的标准化运行流程，构建阶段化执行链。约束交付产物，形成完整的执行证据链，实现自动化审计的可信、可解释、可追踪与可复现。

* **实时观测状态，可持续的交互体验：**打破任务执行期的信息壁垒，将节点运行状态、收集的证据链实时同步至前端界面，实现全局可视。同时建立上下文持久化策略，在生成最终报告后，仍支持用户持续对话与追问，形成闭环式交互体验。

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/8075483b730c4c4fa75e7573033a68fe~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=202606051029036B9C49FFFA8098F4CE9F&x-expires=2147483647&x-signature=d5F6Xni72h4PhQ%2FAEYvXRyeyHL0%3D)

绿盟漏洞挖掘智能体的工程化实践，目前已在多项实战化攻防演练、安全竞赛中取得了优异成绩，技术先进性与实战可靠性在高压对抗环境下得到充分验证。特别是在第十四届信息通信网络安全管理员职业技能竞赛中，绿盟科技烈鹰战队针对大模型开源组件、安全产品、CMS、办公产品、信创组件进行漏洞挖掘，提交30+个RCE，覆盖JAVA、NET、Python等多种语言，最终取得了一等奖的好成绩。

### 4 漏洞挖掘智能体应用价值

绿盟漏洞挖掘智能体的工程化实践将前沿且充满不确定性的大模型技术，成功转化为具备企业级交付标准、可信可控的生产力基础设施，其应用价值可归纳为以下几点：

* **全过程透明留痕，满足可信诉求：**阶段化执行链与事件流机制确保每次审计具备完整的操作轨迹与证据归档，用户可直接复用系统输出的执行记录应对内外部审计与监管检查，实现结果的可解释、可追踪、可复现，并可对漏洞挖掘结果以自然语言方式发起追问。

* **多模型解耦与异构适配，标准化输出：**大模型的技术迭代日新月异，智能体框架建立了一道关键的能力隔离层，不绑定于单一外部供应商的 API，还可无缝切换至客户本地部署的私有化大模型；同时突破模型的上下文天花板，无需用户理解复杂的 Prompt 编排，即可输出标准、可信的漏洞挖掘报告。

* **极致的降本增效，规模化自动漏洞挖掘：**依托控制面与执行面的彻底解耦及容器化底座，实现“一键下发、自动调度、故障自愈”的无人值守工作流，压缩人工介入时间与运维成本，也可避免”全量任务涌向大模型”导致的算力浪费与API成本激增。

**绿盟蓝军一体化平台（NICP）**目前已支持漏洞挖掘智能体，非战时作为常态化漏洞挖掘引擎，针对开源组件供应链及已掌握源码的业务系统持续开展批量审计；战时直接调用已武器化漏洞插件快速取得突破，彻底改变”临战找洞”的被动局面。

随着模型能力的持续迭代与方法论的不断优化，漏洞挖掘领域将迎来更高效率、更广覆盖、更深洞察的技术新周期。绿盟科技也将持续深耕AI与安全融合的创新前沿，把技术突破转化为安全能力输出，释放AI赋能的深层价值，与客户及行业伙伴共建更安全的数字未来。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E3%80%90%E5%85%AC%E7%9B%8A%E8%AF%91%E6%96%87%E3%80%912026%E5%B9%B4ai%E6%8C%87%E6%95%B0%E6%8A%A5%E5%91%8A%EF%BC%88%E4%B8%89%EF%BC%89/)

[Next](https://blog.nsfocus.net/%E4%BA%91%E7%AB%AFwireshark/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)