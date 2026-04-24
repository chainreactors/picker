---
title: AI嵌入企业核心业务：安全体系面临结构性挑战
url: https://mp.weixin.qq.com/s/lkMh2SxJq9HI-UC5z5XrDA
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:54:40.432306
---

# AI嵌入企业核心业务：安全体系面临结构性挑战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xCpgJcagficnLMacIBTyNKyIJWTIWpIPliawsXZEsDG8qEuB50sZeIffLRd9icUYT0MjKTL98iaG1wEG9zZ3b52vNxC4acdSniavH8EHdQT2vU4/0?wx_fmt=jpeg)

# AI嵌入企业核心业务：安全体系面临结构性挑战

松杨网络安全资料库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

AI技术正在以超出大多数安全团队预期的速度嵌入企业核心业务流程。从智能客服到自动化审批，从RAG知识库到AI Agent自主决策，企业的数字化基础设施中正在快速增加一个全新的攻击面。

与传统的IT系统不同，AI系统的风险特征具有明显的独特性：它既暴露了传统安全控制的盲区，又创造了传统防御体系无法覆盖的新威胁向量。

## 身份边界正在消失

传统安全架构建立在清晰的身份边界基础上。然而，当企业同时运行数十个AI Agent，且每个Agent拥有调用CRM、ERP、财务系统的权限时，这个边界正在逐渐消失。

这些AI系统在没有人工审批的情况下自主完成订单处理、合同审批、数据归档。它们拥有高权限账号，但传统的静态访问控制模型在"机器速度"面前形同虚设。

面对这个问题，Check Point的建议是，将身份视为动态的、具备数据感知能力的控制平面，对人、机器、AI智能体实施同等的可见性、审计和追责制度。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xCpgJcagf8MZajTGzxoWawNsOKVaCghYjKeMFYJHnOPXDk1xMu686nJYscQ27nskQ5ORRuUArU40dBbOxGez64nQsEAia2AzqjSqqWQwXmM/640?wx_fmt=jpeg)

## 提示词注入成为新的注入攻击

提示词注入的本质是：攻击者将"指令"伪装成"数据"，欺骗AI系统执行恶意行为。它存在两种形态：

直接注入是用户在对话接口中输入恶意指令，要求系统泄露数据或绕过安全限制。间接注入则隐蔽得多——攻击者将指令嵌入网页、PDF、邮件或日历邀请中，当AI系统自动读取这些内容时，恶意指令被触发执行。

对于RAG系统而言，风险尤其突出。RAG从外部数据源检索内容作为回答依据，如果数据源被污染，攻击者可以通过操纵检索内容来间接控制AI输出。

与SQL注入不同，提示词注入的检测技术尚未成熟，防御主要依赖输入输出过滤、语义异常检测等手段，缺乏像WAF那样经过验证的通用防护手段。

提示词注入与SQL注入区别：

| 层面 | SQL注入 | 提示词注入 |
| --- | --- | --- |
| 攻击位置 | 数据库查询层 | AI 推理层 / 数据源 |
| 攻击原理 | 闭合 SQL 语句，注入恶意命令 | 混淆指令与数据，劫持 AI 行为 |
| 防御成熟度 | WAF / 参数化查询 | 输入输出过滤，语义异常检测 |
| 检测难度 | 语法特征明显，易检测 | 语义模糊，极难识别 |
| 攻击形态 | 直接：用户输入 | 直接 + 间接（数据污染） |
| 防护手段 | WAF、参数化查询、最小权限 | 仍未有成熟方案 |

AI供应链比传统软件供应链更不透明

AI模型的供应链复杂度远超传统软件，一个企业级AI应用可能涉及基础模型、微调框架、向量数据库、Embedding服务等多个层级，任何一个环节的安全缺陷都可能向下游传导，且透明度远低于传统软件依赖管理。

2025年国内首次大模型众测发现了281个漏洞，其中60%为AI系统特有漏洞。

重要的是供应链投毒风险。开源模型可能被植入恶意代码，训练数据可能被注入偏见或后门，第三方API可能在悄悄收集企业数据。

悬镜AIST研究团队提出的AI-SBOM（AI软件物料清单）概念，是将传统SBOM理念延伸至AI领域的一次重要尝试——为每个AI应用建立完整的物料清单，是实现供应链可见性的第一步。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xCpgJcagf8RclR4ia2VH4qHd7n2cB3A3pgfyeRynymIoeC0YxRxWlvnbK8kNJ8fxQOibgsM0ySeYok4QuEMfOQpnOFmqmia14d8a89t2kYfqU/640?wx_fmt=jpeg)

## 深度伪造正在瓦解传统身份验证

社会工程学攻击因AI深度伪造技术的普及而进入了一个全新阶段。

2024年1月，某跨国公司香港分部财务人员参加一场"高层视频会议"，所有参会者包括董事长、CEO、CFO均为AI生成的深度伪造影像，最终被诱导转账2亿港元。

传统的电话验证和视频确认已不再具有较高的可信度。音频以及视频都可以伪造，数字人格可以批量生成。这意味着企业现有的身份验证流程——尤其是涉及资金转账和敏感操作的高风险场景——需要进行系统性重新评估。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xCpgJcagf9gJFE0tRolhQZAwicPrR05Ajd3fAwVfKWfwODH34ovV1CuhsUZvFLepIkXqbib1L7zkGJA9HAsurnynaOnMoib4giauOGRjah7pcs/640?wx_fmt=jpeg)

## AI驱动的自动化攻击正在压缩防御窗口

AI不仅创造了新的攻击面，还加速了已有攻击方法的利用效率。

Sophos数据显示，AI生成的钓鱼邮件使攻击成功率提升了47%。借助AI工具，攻击者可以实现规模化凭证撞库、批量生成个性化社工内容，并显著缩短从发现漏洞到完成利用的时间窗口。

有报告显示，2025年通过AI语音进行的欺诈和账户盗用事件造成损失超过2.5亿美元。这个数字代表着：攻击门槛的持续降低与攻击效率的持续提升。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2xCpgJcagficn2Ff2ziaEibibsAA4fbAcUF5hCgznxf1G28Wpd2G7x22nGGCbQMM4R6yt9brXnHpTJPHefdQjpSeicX1aibFMmpQthicoJeibDicOJg8/640?wx_fmt=jpeg)

## 应对建议

1.盘点企业AI资产，建立AI系统身份与权限台账。

2.对检索增强系统的数据来源实施安全审查，限制非可信数据源接入。

3.为高风险操作（资金转账、敏感数据访问）建立多通道验证机制。

4.建立AI安全事件应急预案，明确事件分级与处置流程。

5.定期开展AI深度伪造相关的安全意识培训与模拟演练。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

松杨网络安全资料库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

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