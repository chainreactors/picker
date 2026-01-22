---
title: AI+军用有没有搞头？
url: https://mp.weixin.qq.com/s/tgDbhtPHz3-5yj_5IrtmZg
source: Doonsec's feed
date: 2026-01-21
fetch_date: 2026-01-22T03:34:06.735933
---

# AI+军用有没有搞头？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5F1cGSkUffO3OicFx6asESiaV1M9bOauyawrsVgSRQ54wbKJAmyDCH3jibobrk34sXgEKh6dzofticmokGrEygejrw/0?wx_fmt=jpeg)

# AI+军用有没有搞头？

原创

Ghost Wolf Lab
Ghost Wolf Lab

Ghost Wolf Lab

![]()

在小说阅读器中沉浸阅读

## 导语

在过去的二十年间，技术的迭代速度与冲突形态的演变，已远远超越了传统国防政策与军事流程的适应步伐。为了应对这一挑战，一家名为 Sandtable 的新兴国防科技公司，正通过其创新的人工智能平台，为作战规划的现代化注入新的活力。通过深度融合 AI、人类判断与沉浸式三维地理空间技术，Sandtable 旨在重塑军事决策的速度、精度与深度。

---

## Sandtable

传统的军事规划、协同与推演，在很大程度上仍依赖于二维图像、电子表格、纸质文档，乃至实体的沙盘。这种模式不仅效率低下，而且将关键决策人员集中于同一物理空间，本身就构成了巨大的安全风险。

在2024 年，由美国陆军退伍军人和研究人员组成的 Sandtable 公司，敏锐地洞察到了这一痛点。他们认识到，现代战争的要素——无论是无人机、反无人机技术，还是电磁频谱战——都真实存在于三维空间之中。因此，任何作战规划都必须能够真实地复现这个三维世界。

![](https://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffO3OicFx6asESiaV1M9bOauyaGyl5uNibPtec2LNKO6AO0Epp0tlLI8n5ULiaORw5kr7iaTUEUfUaudqtQ/640?wx_fmt=png&from=appmsg)

“我们所模拟和规划的一切，都发生在现实的三维空间里，我们必须有能力再现这个现实，” Sandtable 的首席运营官 Brady Moore 指出，“而这，正是我们需要 Cesium 的原因。”

Sandtable 的核心理念，是将时间动态的三维地理空间技术引入军事规划的核心。其平台致力于打造一个交互式的、融合多源异构数据的作战环境，支持人类指挥团队与自主系统（如无人机集群）在任何地点进行协同规划与评估。

---

## AI + 3D

Sandtable 的解决方案通过其两大核心原型产品——**Mentat** 和 **Navigator**——将人工智能与人类判断力相结合，旨在加速军事决策流程 (Military Decision-Making Process, MDMP) 的关键阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffO3OicFx6asESiaV1M9bOauya8jSZ2q2bzD2Y8R5ibUtzfEf4QpaOlhKvuThJX09eezibhQia7KOOuib18w/640?wx_fmt=png&from=appmsg)

### Mentat

* **技术栈**: 基于 **CesiumJS** 构建。
* **功能**: Mentat 是一个作战方案 (Course-of-Action, COA) 的快速开发与分析平台。它能够在一个标准浏览器中，将书面命令、概念草图以及各类开放数据集（如土壤密度与成分数据）叠加在真实世界的三维地形之上。
* **AI 赋能**: 借助 AI，该平台能够帮助参谋人员快速解析战场模式、对比多种行动方案的优劣、并对关键假设进行压力测试，从而让指挥官能将精力集中在最需要人类判断的环节。

### Navigator

* **技术栈**: 基于 **Cesium for Unity** 构建。
* **功能**: Navigator 提供了一个共享的虚拟环境，支持身处各地的参与者通过多种设备（从桌面到 VR/AR）进行作战方案的分析和任务推演。
* **创新闭环**: Navigator 的价值远不止于对 Mentat 制定方案的单向演练。它能够将在推演过程中获得的洞察（例如，某条路径对于特定车辆的通行性问题），实时反馈回 Mentat 的规划环境中，形成一个“**规划-推演-优化**”的持续迭代闭环，而不是一次性的执行。

---

## Cesium 生态

https://ion.cesium.com/（可以注册自行尝试）

![](https://mmbiz.qpic.cn/mmbiz_jpg/5F1cGSkUffO3OicFx6asESiaV1M9bOauyaLTicWv0uxBXDHACCpDA0TBXjbPeCickau2HuzzGboPC9ohzcdZwMNT0A/640?wx_fmt=jpeg&from=appmsg)

Cesium 的技术生态系统是 Sandtable 实现其愿景的基石，为平台提供了权威的地理空间上下文和高效的数据流。

* **高精度数据融合**: 通过 **Cesium ion**，平台能够高效地优化、托管并流式传输来自公共和政府部门（如 NOAA, USDA）的多种地理空间数据，包括 3D Tiles、量化网格 (Quantized Mesh) 和 KML/KMZ。这意味着作战人员和自主载具不仅知道山脉和树木的位置，更能感知到影响机动性和视线的**微地形特征**（如植被高度），这对于无人机的侦察视窗分析至关重要。
* **数据无关性与互操作性**: Cesium ion 使 Sandtable 的平台能够保持“数据无关性”。由于 **3D Tiles** 是一个开放地理空间信息联盟 (OGC) 的社区标准，平台不仅能消费各类开放数据，还能在需要时无缝接入军方自有的标准格式数据（如陆军的 Well Formed Format）。
* **部署模式**: 目前，Sandtable 在连接互联网时使用 **Cesium ion SaaS** 服务，并计划在未来的断网或拒止环境 (Disconnected, Denied Environments) 以及安全飞地 (Secure Enclaves) 中，利用 **Cesium ion Self-Hosted** 进行私有化部署。

---

## 结语

Sandtable 的成功关键在于其“嵌入式”的开发模式——与平台的最终用户（一线士兵）紧密合作。在 2025 年 10 月的陆军 xTechOverwatch 竞赛中，团队在野外直接让士兵们在平板电脑上测试 Mentat。他们白天收集反馈，晚上调整功能与界面，第二天便能带着一个改进后的产品回到现场。

这种“以小时计，而非以天计”的快速迭代能力，得益于 **3D Tiles** 格式的适应性和开源运行时引擎的灵活性。

目前，Mentat 和 Navigator 已被列入 **Tradewinds Solutions Marketplace**，获得了政府直接采购的资格，这预示着国防工业与前沿科技公司之间的合作将更加紧密。Sandtable 的实践清晰地表明，将 AI 决策智能与高精度数字孪生战场相结合，不仅是“有搞头”的探索，更是塑造未来智能化联合作战能力的关键所在。

虽然 Sandtable 平台所呈现的实时、交互式三维战场态势，在视觉上容易让人联想到俄乌冲突中乌克兰军队使用的、以“三角洲”（Delta）为代表的战场指挥面板，但两者在核心设计理念与战略意图上存在着本质区别。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5F1cGSkUffO3OicFx6asESiaV1M9bOauyaiaR3J41VBMpu9YDlYu6ulEaseEDZ1D8z0uGPAwOOhQNLicyYL3mA8WiaA/640?wx_fmt=jpeg&from=appmsg)

乌克兰的系统更侧重于**战术执行与态势感知**——即整合来自无人机、卫星和一线士兵的实时情报，为分散的作战单元提供一个统一的、即时的共同作战图景 。它的核心价值在于“**看清当下**”，赋能小规模部队的快速决策与精准打击。

PS:与俄乌战场上乌克兰被入侵和缴获的呼叫火炮支援面板不同，Delta只做战术协同和态势感知作用，然而它的安全策略可见一斑，仅不到三个月就被远程入侵^v^。

而 Sandtable 的核心则更进一步，它聚焦于**作战规划与决策推演 **。它将物理世界的复杂性（如地形、天气、电磁频谱）与人类指挥官的战略意图相结合，在一个高保真的数字孪生环境中反复“彩排”战争。因此，如果说前者是赋能士兵的“数字化步枪瞄准镜”，那么 Sandtable 则更像是为指挥官打造的“******智能化战争罗盘**”，其最终目标是在冲突发生之前，就通过海量的数据与模拟，找到通往胜利的最优路径。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffMjPelmXP6PVz3ggEh1icEAF87iaeIb4TlVN9ZPSUCrNXlBqYYNIT7EjRhT5QBTZawC4Iro4ia1MZFEw/0?wx_fmt=png)

Ghost Wolf Lab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffMjPelmXP6PVz3ggEh1icEAF87iaeIb4TlVN9ZPSUCrNXlBqYYNIT7EjRhT5QBTZawC4Iro4ia1MZFEw/0?wx_fmt=png)

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