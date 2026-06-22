---
title: SecEBL: 基于意图识别的入侵检测
url: https://mp.weixin.qq.com/s/qJ4l6FVxfwCd13xW38h4xg
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:49.313659
---

# SecEBL: 基于意图识别的入侵检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/haeEa6u0cicDeEnFXNmrG9CibOvcibupbcQPGqJ7xp2Mg8prRySD2p5Uibz3Im2SSmDOlUPeibrU1Aw6icZGOPEZ5D3ULdngOOWtM44ySd2YDnPrw/0?wx_fmt=jpeg)

# SecEBL: 基于意图识别的入侵检测

原创

EBwill
EBwill

灾难控制 局

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# /SecEBL(Security Event Behavior Labeler)/

###

**项目简介**

SecEBL 是一个两层架构的试验性项目：

* 第一层是经过一个基于 `Alibaba-NLP/gte-modernbert-base` 微调的 Embedding 模型，目标是针对各类单条遥测数据实现**意图识别**；
* 第二层是一个简单的机器学习模块，目的是可以在行为序列或 Session 维度识别一组行为是正常行为还是恶意行为。

SecEBL 的目标是通过**意图检测**来替代部分的黑白名单、传统机器学习检测，期望让入侵检测系统在未来可以真正在基于**理解行为**的维度去实现。

###

**L1 Behavior-Intent Labeler**

在第一层，我们不想解决：**“这条命令是不是恶意？”**，我们想认真回答：**“这条事件里可见的客观行为是什么？”**。

比如：

* read\_credential\_material
* execute\_remote\_command
* create\_scheduled\_task
* grant\_cloud\_privilege
* upload\_sensitive\_content
* query\_service\_health

这些标签本身不是最终告警，**它们只是可解释的行为标签**，一条命令可能是正常运维，也可能是攻击链的一部分，这取决于上下文、序列和环境。SecEBL 的 L1 层只负责输出行为证据，把最终判断留给后续的 session reasoning、规则、策略、人工分析或其他模型。

当前公开版本面向 Linux cmdline 和 Kubernetes auditLog（少量） 训练与评估，但设计目标更广：endpoint telemetry、audit logs、cloud audit records、identity events、container events，以及其他安全相关事件流。

###

**L1 Data, Benchmark, Accuracy and Performance**

**Data, Benchmark**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicD9suibibC6Gf8QkZ8e4apOu1whIjA681icmD05RQwCqicJdwz2PUoWPfyeic51h47f2tiaicMAKJfxCRQdaibWxrBsx9axzCCg1Dcjq5Y/640?wx_fmt=png&from=appmsg)

**Accuracy**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicBHQJYwTSSedw0cO1iby8m1OsH8oKJjJCZf7FXRuDDkYcMRoZbt52CHialon7NCc7lOs3asMzxdYghTFG5bboKLoI6sLibwY7XV78/640?wx_fmt=png&from=appmsg)

**Runtime Performance**

![](https://mmbiz.qpic.cn/mmbiz_png/haeEa6u0cicAv8pibMF1aiaF1kQP3xVrUmicbKY9bdSj7uMYtBZAqiaLvElNYbUEmkVDTEu79WYCaAiasG8S2QMk7MNaVShXp7qcnmUxRwhGJpMHk/640?wx_fmt=png&from=appmsg)

###

**L1 Examples**

**Fine-Grained Contrast Examples**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicBgVkc10fa4Rs8b2Idx1Oyr26j37nvkFyCjC6Htc3S80cGvUPFpUJQQ70KwOib47MQByz8aTZXhZQOMuxWAGUicZg8rFt3MGBibOY/640?wx_fmt=png&from=appmsg)

**Intrusion-Like Examples**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicDXIhoqt4VAhvxX0dtBPgRcMDLxRl0U76NicU8PEF7aacuLjibXiaCkJSqJ0uu88dcoUH7eHibeGDUX5HiccWnicRibJe3ulW5YbP43FI/640?wx_fmt=png&from=appmsg)

**Normal Operation Examples**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicAg3dM9e2rHj4Dn9iaicfURgJFBbLjN1ESUtrNiadBCdJexRo763884VIbU0ZuXLabA7gmmwCrdYPb0ACT31ytzUyEcHSQ6AwkYsI/640?wx_fmt=png&from=appmsg)

**Normal Maintenance Examples**

![](https://mmbiz.qpic.cn/mmbiz_png/haeEa6u0cicD4ILFb9yBZakUt7eL4oA84xZv0yUKxe3iaiaC8M6OON1tYyv6HPe70nib4j1r4JxzuCw3DNjOfMhIibvjJDRFRTg8e3cRuRZdxxOs/640?wx_fmt=png&from=appmsg)

###

**L2 Session Risk Scorer**

L2 是一个实验性的 session-level 风险评分层。

它不直接看原始命令文本，也不使用用户名、主机名、session\_id 作为评分特征。它只先读取 L1 已经生成的 `top_labels`，也就是每条事件的行为意图标签和相似度分数，然后按 `session_id` 把多条事件聚合成一个 session。

聚合时会提取一些语义特征，例如：

* 高风险行为标签的数量和比例；
* 行为家族的多样性；
* L1 retrieval score 的统计特征；
* credential access、persistence、remote execution、data staging 等攻击链信号；
* normal operation / routine maintenance / professional operation 相关上下文比例；
* 行为转移和组合模式。

当前发布的 L2 是一个轻量的 logistic regression 模型，输入是这些 session-level 语义特征，输出 session 是否更接近 `intrusion` 或 `normal_operation`，所以它的核心思路是：

```
1L1 单事件行为标签
2  -> 按 session 聚合
3  -> 提取行为链和上下文特征
4  -> logistic regression session scorer
5  -> session-level verdict
```

L2 目前是实验性组件，可能存在过拟合的问题，但它主要用于验证“基于行为意图链做 session 检测”这条路径。

针对 L2 的 Internal benchmark 结果与性能数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/haeEa6u0cicBaafGucHc0uA7iaVMhaW76VsKPuKA81uVaYoPE8mcndptalibniaXI0rRyibzy1lDwqfEicmLYw1ZuXV730sgkJqWAL78N5blOtPbU/640?wx_fmt=png&from=appmsg)

###

**项目地址**

https://github.com/EBWi11/SecEBL

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jEESHeKDyVxhtbAawicDNOVJB5zLyiaibU8WAjT97QyuTCNoCXIlq0o7fYIMu3Tp1Pw7fZQicTYGHKOib7EmCa4tUVA/0?wx_fmt=png)

灾难控制 局

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jEESHeKDyVxhtbAawicDNOVJB5zLyiaibU8WAjT97QyuTCNoCXIlq0o7fYIMu3Tp1Pw7fZQicTYGHKOib7EmCa4tUVA/0?wx_fmt=png)

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