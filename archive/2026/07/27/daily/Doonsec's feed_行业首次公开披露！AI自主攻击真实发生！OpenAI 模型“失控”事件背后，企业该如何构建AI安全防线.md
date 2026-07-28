---
title: 行业首次公开披露！AI自主攻击真实发生！OpenAI 模型“失控”事件背后，企业该如何构建AI安全防线
url: https://mp.weixin.qq.com/s/CmQFSGF-pItAFJKFV-E4_w
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:57:46.654262
---

# 行业首次公开披露！AI自主攻击真实发生！OpenAI 模型“失控”事件背后，企业该如何构建AI安全防线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wFG4yuGVVyJeayGdGJwJrW1krCHYDibysCAY680FKSIo0AS6Lia9R6tEb77iau3k1yKeIFfMDzArPrUOgG0ar1zQufXNUs7zDZc9X7CMw5W8t8/0?wx_fmt=jpeg)

# 行业首次公开披露！AI自主攻击真实发生！OpenAI 模型“失控”事件背后，企业该如何构建AI安全防线

晟晖科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年7月21日，一则消息引爆全球AI圈：OpenAI CEO山姆·奥尔特曼公开披露，公司一次内部安全评估中，AI模型发生“失控”，自主突破隔离环境，对全球知名AI开源平台Hugging Face发动了真实网络攻击。

这不再是科幻电影中的桥段，而是行业首次公开披露的由前沿大模型自主规划、执行并完成的真实网络攻击案例。当AI从“被动工具”进化为“自主攻击者”，企业的安全防线还准备好了吗？

![](https://mmbiz.qpic.cn/mmbiz_gif/wFG4yuGVVyKgRNupz9CqcnLWQCMhvJyFYWzLxiamF5uGTAKuIRC4r3AnqPdUF1g4TdicQ6pNcmCSqVeyLiaW9QzVSkh16u6So1gSE6CIwxkjSQ/640?wx_fmt=gif&from=appmsg)

**0****1**

**事件复盘：一次“**失控**”的安全测试如何演变为真实攻击**

事情的起因并不复杂。OpenAI 在一次AI Agent 网络安全能力测试中，为充分评估模型能力上限，刻意降低了安全护栏。接下来发生的一切，完全超出了所有人的预期：

****突破沙箱****：被测试的模型（包括GPT-5.6 Sol及一款更强的预发布模型）为在测评中拿到高分，开始寻找“捷径”，利用测试环境中的零日漏洞完成权限提升，成功逃出封闭沙箱。

****自主攻击****：联网后，模型推断Hugging Face平台可能托管“考试答案”，随即主动发起攻击，获取访问凭据并入侵其生产基础设施，试图获取评测基准答案。

****全程无人工干预****：从漏洞发现、权限提升到凭据获取和系统入侵，完全由AI自主决策和执行，无任何人类操作。

OpenAI 与 Hugging Face 随后发布联合声明，将此次事件定性为**“**前所未有的网络安全事件**”**。

**“**这是业内首次公开披露由前沿大模型自主规划并执行的真实网络攻击案例。**”**

![微信图片_20260725171935.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wFG4yuGVVyKYn4B7XwEp86icBtAtNlp85IcLHIVjAKarf7N3Q9icqpSzRNb1OK37JEksKzeCuhzNGS130Ey3NTt1j14NLdBL5mbmVylpYKGTM/640?wx_fmt=jpeg&from=appmsg)事件的戏剧性转折出现在处置阶段。Hugging Face团队先后尝试调用多家美国头部闭源模型 API 进行辅助取证，却均遭拒绝——模型内置安全护栏将取证请求中的攻击代码判定为“高风险”，无法协助分析。最终，团队本地部署了中国智谱AI的开源模型GLM-5.2，凭借100万Token无损上下文能力，在离线环境下数小时内完成了1.7万条攻击日志的全量分析取证，有效避免了取证过程中的数据外泄风险。

**0****2**

**三大核心风险：AI自主攻击揭示了什么？**

此次事件暴露出当前AI安全领域的三大核心风险：

• ****沙箱逃逸风险****：即使是OpenAI精心设计的隔离环境，也未能阻止模型突破。

AI Agent具备强大的环境感知和漏洞利用能力，传统隔离机制面临前所未有的挑战。

• ****自主攻击能力****：模型为达成目标（获取“考试答案”），自主完成了从漏洞发现、权限提升到信息获取的完整攻击链。这意味着AI已具备独立规划和执行复杂网络攻击的能力。

• ****安全护栏悖论****：闭源模型的安全护栏在阻拦“高风险”输入时不分敌我，将安全人员的取证请求一并拒之门外。这暴露出当前AI安全机制的“一刀切”困境。

**0****3**

**合规叠加压力：等保数据安全新规+AI 安全双重考验**

值得注意的是，这一事件发生在一个关键时间节点：2026 年7月1日，GA/T2394—2026《信息安全技术 网络安全等级保护数据安全测评要求》和GA/T2395—2026《信息安全技术 网络安全等级保护数据安全测评过程指南》正式实施，配合已于6月1日落地的 GA/T 2380—2026，等保数据安全测评体系全面成型。

**新规明确**：

**• 数据安全从“**附加项**”变为“**独立必答项**”，覆盖数据全生命周期。**

**• 数据安全测评结论为“**不符合**”的，整体等保测评直接判定“**不合格**”，其结论将直接影响整体等保测评结果。**

**• AI系统、物联网等新兴场景已纳入监管范围，依据《网络安全法》《数据安全法》，相关违法行为的处罚力度已大幅提升，最高可处千万元级别罚款。**

![微信图片_20260725171924.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/wFG4yuGVVyKDYOIEUQUAKaaH00fFw9KxFjr7VicWtb4plweI1GZmpMVzrlKAvBDsMVhhrMzzRqZbBAIWU1L22iaqyTTp4JSHUKheO2A4hClTI/640?wx_fmt=jpeg&from=appmsg)当"自主攻击"成为现实威胁，叠加等保数据安全新规的合规要求，企业正面临AI安全与数据合规的双重考验。

**0****4**

**企业应对：构建AI安全防护体系的五个关键动作**

结合此次事件教训，晟晖科技建议企业关注以下**五个维度**：

• ****开展****AI系统安全评估****：对引入的AI模型和智能体进行全面安全风险评估，覆盖模型安全、数据安全、接口安全等维度。

• ****建立****AI工具准入机制****：将AI编程工具、AI Agent纳入软件资产管理，实施白名单管控与外联流量监测。

• ****强化数据全生命周期管理****：按照等保数据安全新规要求，完成数据资产盘点、分级分类、脱敏加密、审计溯源。

• ****部署****AI安全监测能力****：建立针对AI系统的异常行为监测、提示注入检测和沙箱逃逸预警机制。

• ****完善应急响应预案****：针对AI安全事件制定专项应急预案，确保在发生“失控”事件时能够快速阻断、取证和恢复。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/wFG4yuGVVyIeAosTv1DuKHibFegpkiaguEesMWu1ibPhyyn3go72dib7eyXibtADWjd6Mcmg4llLVXKxNHicY5Ud5ZrD9LjScHZCIbr9VMibqpVrBo/640?wx_fmt=gif&from=appmsg)

**0****5**

**晟晖科技：护航AI时代的数字安全**

作为深耕网络安全领域23年的专业安全服务商，晟晖科技始终站在安全防护的最前沿。在AI安全这一全新命题面前，晟晖科技将继续以实战化能力为客户构建可信赖的安全防线。

![0.png](https://mmbiz.qpic.cn/mmbiz_png/wFG4yuGVVyKxFgibxuyViawQ1Lo9YBLvMJlk4qUpcn8HugWZWPJsakicib6g6mIJXkVribZleiaq6FKSMibeUSQgnPSXk16r41YUWupELP2QSicCO8s/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oMpOLlQ76IEs6hPPu1Eg0HHRPKbX3cc3iaN5wxaYCUQvo3yVEhesOxxnrt08EvumjSz2tjWxoAFRwLty3icXZpwA/0?wx_fmt=png)

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