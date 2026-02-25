---
title: 大模型蒸馏攻击
url: https://mp.weixin.qq.com/s/ITlC5awNX6kn3vZD_oPtJA
source: Doonsec's feed
date: 2026-02-24
fetch_date: 2026-02-25T04:12:50.717964
---

# 大模型蒸馏攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zicib4mibicnb8w8fYiaEX0raHjyJnnfsSrgOl81G1FHbpsJHBIUTYPPbKhnk5KyciadX4rowdOZ83emRtCY48R5GuB16ydlu0icQdU0iajWyRuJUgU/0?wx_fmt=jpeg)

# 大模型蒸馏攻击

王水江
王水江

CISSP Learning

![]()

在小说阅读器中沉浸阅读

大模型蒸馏攻击（模型萃取/克隆攻击）介绍

一、定义

蒸馏攻击（Model Distillation Attack / Model Extraction Attack）
是指攻击者在黑盒条件下，通过向目标大模型发起海量、结构化、高覆盖率的批量查询，收集模型的输出结果、推理逻辑与行为特征，再通过知识蒸馏技术训练出一个能力高度近似的“影子模型”，从而实现低成本窃取模型知识与能力的攻击方式。

二、攻击核心逻辑
- 不入侵服务器、不获取权重、不利用漏洞
- 只通过公开 API 正常调用
- 用“海量问答”把大模型的知识“榨”出来
- 训练一个小模型复刻其能力

三、典型攻击流程
1. 构造探针数据集
覆盖逻辑、代码、数学、边界、多模态、指令遵循等场景。
2. 批量高频查询
多账号、多IP、分布式调用，规避限流与检测。
3. 采集模型行为
记录回答、思维链、输出分布、响应特征。
4. 知识蒸馏训练
用采集数据训练轻量“影子模型”。
5. 形成高仿克隆模型
能力接近原版，成本仅为原版的 0.1%～1%。

四、近期真实典型场景
- Google Gemini 被大规模蒸馏
单次攻击可达 10万～100万次查询，专门克隆推理、多模态能力。
- Anthropic 指控蒸馏攻击
针对 Claude 发起 数百万次交互，批量探针、伪造账号、负载均衡躲避检测。
- 这类攻击已从学术研究变成工业级商业窃取。

五、主要危害
1. 模型知识产权被窃取
2. 安全对齐规则被破解，更容易被越狱、诱导
3. 商业价值大幅稀释
4. 克隆模型可用于钓鱼、诈骗、恶意内容生成、黑产自动化

六、通用防御手段
- 异常行为检测：识别批量、高频、结构化探针
- 输出扰动与噪声：降低知识可萃取性
- 隐形模型水印：实现克隆溯源
- 访问控制、账号核验、QPS 限流
- 对敏感/探针类问题模糊化、统一化回答

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