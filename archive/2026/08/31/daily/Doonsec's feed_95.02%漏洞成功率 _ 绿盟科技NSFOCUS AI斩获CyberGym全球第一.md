---
title: 95.02%漏洞成功率 | 绿盟科技NSFOCUS AI斩获CyberGym全球第一
url: https://mp.weixin.qq.com/s/KBwto0VeECB2FdgibnvRfg
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:56:28.339286
---

# 95.02%漏洞成功率 | 绿盟科技NSFOCUS AI斩获CyberGym全球第一

# 95.02%漏洞成功率 | 绿盟科技NSFOCUS AI斩获CyberGym全球第一

M01N Team

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于绿盟科技
，作者绿盟君

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM5hQWTd2AHZRBvI0pibt2oAA2HeHMTOqTNt5kkrQUmdaYQ/0)

**绿盟科技**
.

绿盟科技 官方微信

![](https://mmbiz.qpic.cn/mmbiz_gif/2icibGKbYdhcwueLEggyPhKuibn1YBGoOBZ0JYxnRqM7yZBurze4okckSMwiaZgvqibmGzzZtBk1q7o3ZVFdCxYATw93Gkz68f0rthBCicBBjpcls/640?wx_fmt=gif)

在AI安全能力国际权威基准测试**CyberGym**全球榜单中，绿盟科技自主研发的NSFOCUS AI漏洞挖掘智能体以**95.02%**的漏洞复现成功率斩获**全球第一**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2icibGKbYdhcw8kzxDmfSMv2zbbnWLdZq24vZhiaDYRRW16HkfHwOrpo5JLcOlFXbxxH5AM8th4lbkauC88M0zBAVia4tX2kM8HFzxECMQ366ws/640?wx_fmt=jpeg)

榜单官网截图

CyberGym主要评估智能体自主复现已知漏洞的能力。参测系统需根据简要的漏洞描述，在真实开源项目的漏洞版本源码中分析目标函数、构造可验证的输入，并仅提交一个最终 PoC。评测采用差分验证：PoC 必须能够在漏洞版本中触发问题，且不能在修复版本中触发。该基准较好地还原了实际漏洞挖掘和复现工作的核心过程。

NSFOCUS AI基于**智谱 GLM-5.3大模型**底座，通过将绿盟科技长期积累的攻防经验转化为可执行、可验证的分析流程，系统且充分释放模型在复杂推理、长程规划与代码理解上的能力边界，在真实的漏洞挖掘任务中体现强大实战效能。

**专家范式：假设驱动 · 证据导向 · 闭环迭代**

NSFOCUS AI 能够模拟人类漏洞研究员的认知范式，形式化为一套可计算、可审计的工作流，像专家一样**提出假设、固化证据、在试错中逼近真相：**

* **基于语义约束的漏洞假设生成：**模拟专家进行漏洞审计，通过静态分析识别脆弱模式，推导触发所需的路径条件与输入约束，构建"可证伪"的漏洞假设，而非堆砌模式匹配告警。
* **调试器辅助的运行时证据固化：**用 GDB 在关键路径谓词与内存操作点细粒度插桩，核验运行时内存布局、约束求解状态与控制流转移，将静态的"可触发"推断，转化为基于执行轨迹的确凿证据；并据此过滤相邻缺陷干扰（误报）。
* **约束导向的定向模糊测试：**采用符合语法规范的种子输入，围绕关键字段实施约束变异，减少无目标的随机测试，提高计算和测试资源的利用效率。
* **闭环式假设修正：**验证失败的样本不会被简单丢弃，而是用运行时反馈反向修正种子结构、路径假设与约束条件，形成"假设—生成—验证—修正"的迭代闭环。

绿盟AI漏洞挖掘解决方案，也正是基于这种思路，为客户提供更高效的AI安全治理能力。

**深度融合：非预期态收敛重新定义漏洞**

绿盟科技智能化攻防团队提出并实践**USC（非预期态收敛，Unexpected-State Convergence）理论框架**，在该理论指引下漏洞被重新定义为：软件"设计意图"与"实际行为"之间的风险偏差；基于AI进行漏洞挖掘的本质，是引导推理系统持续向目标软件的"非预期态"收敛。绿盟AI漏洞挖掘智能体 NSFOCUS AI 把这一理论落地为一个清晰的乘法关系：

**高效漏挖 = 收敛引导（策略层）× 编排执行工程（Harness）**

* **收敛引导（策略层）：**源自绿盟科技多年沉淀的实战攻防经验。我们把一线研究员"从哪里下手、何时收手、如何确证"的直觉，形式化为可计算的收敛引导，让 GLM-5.3 的每一次推理都精准瞄准"非预期态"，避免在大模型常见的盲目探索中空耗预算。
* **编排执行工程（Harness）：**绿盟自主研发的Harness工程，为智能体任务提供稳定的运行环境、可信的证据采集与严格的提交闸门，将模型的"判断"固化为可审计的"证据"。

NSFOCUS AI所做的，正是以绿盟的攻防经验与工程体系为杠杆，把 GLM-5.3 的推理潜力，精准兑换为漏洞挖掘的实战胜率。

**模型跃迁：GLM-5.3 提升复杂任务处理与 PoC 质量**

为验证模型迭代效果，团队在相同的 1,507 项任务、系统流程和判定标准下，对 GLM-5.2 与 GLM-5.3 进行了内部对比。GLM-5.3 完成 1,432 项任务，严格 Pass@1 成功率达到 95.02%；相比 GLM-5.2 的结果成功率提高 1.39 个百分点。

提升集中体现在复杂文件格式、深层调用链、严格字段约束和苛刻触发条件等高难度任务。GLM-5.3 能更快锁定关键字段，结合 GDB、Sanitizer 和定向 Fuzzing 调整输入结构，减少无关崩溃，在提高任务完成量的同时保持 PoC 的针对性、稳定性与可复现性。

**持续进化：做能力的开拓者与边界的守护者**

随着前沿人工智能攻防能力的快速演进，漏洞的发现、利用与扩散节奏正在加快，安全防御面临更短的响应窗口。面对 AI 加速的威胁，我们坚持 “以AI对抗AI”理念，帮助客户建立更加智能、更加主动的安全体系——在威胁抵达之前识变，在风险成型之前消解，让安全真正"跑在攻击前面"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jCnKkPka4us0Jf9EfOrsdP4RMtsgx7QzWjHOyDSnXKS6VSN8Z7D5QX21pUKticctRsHMYmN6OpodSg0xFz2uic98QRIpgGFYRFUI4/640?wx_fmt=png)

「关于CyberGym」

CyberGym 是由加州大学伯克利分校提出的 AI 智能体网络安全实战测评基准，被业界视为衡量 AI 安全攻防能力的"黄金标准"。其题库包含来自 188 个主流开源项目的 1507 个真实已修复漏洞（主要聚焦 C/C++ 内存安全问题）。赛制要求 AI 智能体仅凭漏洞描述和未修补代码库，自主完成漏洞理解、定位、复现及 PoC 生成全流程，并通过自动化评审严格验证 PoC 是否可稳定触发目标漏洞。该榜单被 Anthropic、微软、Wiz 等视为关键标尺，是当前全球覆盖最广、认可度最高的 AI 安全实战测评体系。

![](https://mmbiz.qpic.cn/mmbiz_gif/xZBrQScF24AJKSgyOaF9TQSR5SKr3RZr8ticxvFEMOH1CvB0IDwDcRzCrhDX8wZcXzibA4XibYFwVcnH0iblicWKCWA/640?wx_fmt=gif)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jCnpjj4Ooktjlo9cOFK8h2IWbj30ygS7rA4stLmKvPSqic7mG40AKII6UxJfCBQgVEz0yl8SRo0aYUv1icSoPLUE3387s5icPsFSOM/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**绿盟科技M01N战队**以“研战一体，以攻促防”为核心理念，持续深耕WEB安全、终端安全、云安全、身份安全等传统核心阵地，更重点攻关大模型安全、智能化网络威胁以及AI赋能的新型网络攻防，旨在将AI的颠覆性潜力转化为防御者的战略优势，为关键信息基础设施与数字社会应对日益复杂和智能化的网络威胁，提供基于实证的洞察、技术与解决方案。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uZT6kWW1jCkrTRDm3k0XdGJAstEQKkiah1fKNwe2cibnfP2qiaIg6klsxDpoBFvDNmFNJX0pMP2picl77IWJUoWlbWJ1QQOqK2N6OibfCzzCUeQQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![图片](https://mmbiz.qpic.cn/mmbiz_png/uZT6kWW1jClZZ89iclh8L2W80hzG890OnK2J8cSLPK7o9tgHkibgF6471eXmc40aufh3y6fqY2R1CNubo5xXkpZfxBtYFibwkSORUYbpDDlTZc/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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