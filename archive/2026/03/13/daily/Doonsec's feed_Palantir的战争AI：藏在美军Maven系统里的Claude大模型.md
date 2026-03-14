---
title: Palantir的战争AI：藏在美军Maven系统里的Claude大模型
url: https://mp.weixin.qq.com/s/38oME9QkVcQs78dKR_kwaA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:03:34.404870
---

# Palantir的战争AI：藏在美军Maven系统里的Claude大模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqoTFQyfcGJqtevxqic9rV6aotUdBOGRBrL5hgSXn5qFw0vn9tftI7nPRoYibgRzOUTNbiaicbvsSU9JibmscoQX4iciajZRSjyqKSKhM/0?wx_fmt=jpeg)

# Palantir的战争AI：藏在美军Maven系统里的Claude大模型

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

近期，美国 AI 初创公司 Anthropic 与五角大楼的激烈争端，将生成式 AI 的军用边界问题推到了公众视野中央。

2026 年 2 月下旬，Anthropic 明确拒绝向美国政府无条件开放旗下 Claude 大模型，同时划出两条核心红线：该 AI 系统**不得用于大规模监视美国公民，不得用于研发完全自主武器**（即无需人类干预即可自主完成识别、决策、攻击全流程的 “杀手机器人”，是全球 AI 伦理领域公认的核心红线）。

五角大楼随即以 “供应链风险” 为由，将 Anthropic 的全线产品列入风险清单，这一认定直接导致美军相关部门无法正常采购、使用其产品。

2026 年 3 月，Anthropic 正式提起两起诉讼，指控特朗普政府此举属于非法报复，要求法院推翻五角大楼的风险认定。

这场争端的核心争议点在于：Anthropic 一方面公开为 AI 军用划定伦理边界，另一方面其核心产品 Claude 早已通过美国军工情报巨头 Palantir 的系统集成，深度嵌入了美军的核心作战与情报体系，其在美军内部的实际应用方式，早已突破了公众对其 “民用 AI 厂商” 的认知。而伊朗相关战事的快速升级，进一步放大了外界对 Claude 军用落地的关注与质疑。

Palantir Technologies 是美国顶级军工情报软件承包商，核心业务是为美国国防部、CIA 等机构提供大数据分析、情报整合的标准化平台，是美军数字化作战体系的核心供应商之一。[Palantir的Ai技术被曝用于以色列在黎巴嫩的致命寻呼机任务](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184106&idx=1&sn=b76a6145cadc2edd3a7833787f716472&scene=21#wechat_redirect)

2024 年 11 月，Palantir 正式官宣与 Anthropic 达成合作，将 Claude 大模型集成到其面向美国情报机构、国防部门销售的软件体系中。Palantir 官方口径称，Claude 的集成可帮助情报分析人员挖掘 “数据驱动的洞察”、识别数据中的隐藏模式，支撑其在 “时间紧迫的战场环境中做出明智决策”。

截至目前，已有公开报道证实 Claude 已参与美军的真实海外军事行动：

1、该 AI 工具已在美军多场海外军事行动中投入使用，包括伊朗相关战事；

2、2026 年 1 月，Claude 在美军针对委内瑞拉总统尼古拉斯・马杜罗的抓捕行动中，发挥了关键作用。

但 Palantir 与 Anthropic 始终拒绝披露 Claude 在美军内部的具体运作方式、五角大楼哪些核心作战系统依赖该模型，这也成为外界质疑的核心焦点。

Palantir 与美国国防部的合作已持续多年，其打造的两大核心系统，是美军情报分析与作战决策的核心基础设施，也是 Claude 大模型最主要的军用落地载体。

### 1. Maven 项目（算法战跨职能团队）

Maven 项目是美国国防部 2017 年启动的、专为战争场景部署 AI 能力的核心计划，Palantir 是该项目的主要承包商，为其开发了核心产品**Maven 智能系统**（下文简称 Maven 系统）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrWxrM9XykuEyMX876VHSNGyX6ngI8Q0bUqexEPQImrwtFZ5UZrDibydnuTxXZpzAfp6icVvu6KooAznNHZtjVOCYMHdWo3VFbkA/640?wx_fmt=jpeg&from=appmsg)

该系统由美国国家地理空间情报局（NGA，负责美军卫星数据收集与分析的核心情报机构）管理，美国陆军、空军、太空军、海军、海军陆战队，以及负责伊朗方向军事行动的美国中央司令部，均有权限访问该系统。五角大楼首席数字和人工智能官卡梅伦・斯坦利曾公开表示，Maven 系统正在美军 “全部门” 推广部署。

其核心作战功能，搭载计算机视觉算法，可对卫星等 “天基资产” 拍摄的图像进行智能分析，自动识别疑似 “敌方系统” 的目标，可精准区分人员与车辆；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpQLJe7m3yugBLfUhBpBiaN56ImAiaLsEQYFhLfuMthTpF0sLwJVsZjic2Uavibf7Ey7e3JwxIOGAk4hTib04o08yV2l5BVjmwiaSZ3Q/640?wx_fmt=png&from=appmsg)

并且支持潜在目标的可视化呈现，具备目标 “提名” 功能，可标记目标供地面或空中轰炸使用；

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrlOKrVzOPNzbNpxNA5pafTrwbLQK7AZgrZfc0ej6zana8JXOoW27EWGexY8kEYpxH742I2Gwd2DTWCMlcmKiayebTWK99TYdo0/640?wx_fmt=png&from=appmsg)

内置 “AI 资产任务推荐器”，可自动为不同目标匹配适配的轰炸机型号、弹药类型；

支撑美军内部跨部门的目标情报数据、敌情报告传递。

PS：外媒均曾报道，Maven 系统的核心能力依赖 Anthropic 的 AI 技术。

### 2. 陆军情报数据平台（AIDP）

2022 年起，Palantir 开始向美国陆军交付该平台，是美国陆军的核心情报整合系统，可整合 Maven 系统及至少其他 4 个美军官方系统的数据。目前公开的核心能力包括：军事行动前的情报准备工作、以图形化方式实时呈现部队与武器的部署位置；平台内置名为 Dossier 的工具，专门用于编制 “情报运行评估”，这是战场动态信息的实时集合，会在最终情报摘要生成前高频更新，是一线作战决策的核心依据。

截至目前，尚无公开信息确认 Claude 是否已集成到 AIDP 系统中。

尽管 Palantir 从未公开 Claude 具体集成到哪套五角大楼的涉密系统中，但其通过官方发布的演示、新闻稿，清晰披露了 Claude 的军用落地载体 ，**人工智能平台（Artificial Intelligence Platform，简称 AIP）**。

AIP 并非独立的操作系统，而是一款可嵌入式的 AI 应用，可直接集成到 Palantir 的核心成熟系统（包括面向商业的 Foundry、面向政府情报的 Gotham）中。

其核心功能分为两部分：一是自动化处理标准化任务，二是提供名为 “AIP 助手 / AIP 代理” 的自然语言聊天机器人界面，用户可通过日常对话的方式提问、下达指令，直接完成系统内的情报分析、作战规划等操作。

最关键的设计在于：AIP 助手的底层能力由 Anthropic、Google、Meta 等厂商的第三方大语言模型提供，**客户可自主选择底层使用的大模型，同时可严格限定大模型生成回复时可访问的专属数据库**。这一权限管控对于军方场景至关重要，美军的情报数据多为涉密级别，该设计可确保机密数据仅在受控范围内被调用，不会对外泄露，这也是美军愿意使用商用大模型的核心前提。

Palantir发布的官方演示，完整还原了 AIP 助手（底层可搭载 Claude）辅助军事操作员完成作战全流程的真实路径，场景设定为 “负责监控东欧地区活动的军事操作员，针对敌方装甲单位策划地面攻击行动”，具体流程如下：

1. **预警触发**

   AIP 助手先发送自动警报，提示通过 AI 算法处理雷达图像，发现了 “潜在的异常敌方活动”（注：此处的异常目标检测由计算机视觉算法完成，而非大语言模型）；
2. **情报研判**

   操作员向 AIP 助手提问 “该区域内有哪些敌方军事单位？”，助手基于装备特征与行为模式，快速研判该单位 “很可能是一个装甲攻击营”；
3. **侦察部署**

   基于研判结果，操作员申请调派 MQ-9 “死神” 无人机前往目标区域实施抵近侦察，核实目标信息；
4. **行动方案生成**

   操作员向 AIP 助手下达指令 “生成三种针对该敌方装备的行动方案”，助手在极短时间内给出三个可落地的选项：空中力量打击、远程火炮打击、战术小组突袭；
5. **方案上报与决策**

   操作员指令助手将三套方案发送给上级指挥官，指挥官最终选定战术小组突袭方案；
6. **作战计划细化与执行**

   操作员连续下达指令，要求助手 “分析战场环境”→“生成部队抵达敌方阵地的最优隐蔽路线”→“部署干扰器破坏敌方通信设备”，所有指令均在数秒内完成；最终操作员完成作战计划的最终审核，正式下达部队集结与行动命令。

在这套完整流程中，Claude 大模型承担的核心角色，就是 AIP 助手的交互入口，以及生成回复、制定方案、逻辑推理的核心引擎。需要特别说明的是：该系统的聊天机器人不会直接下达攻击指令、直接建议打击目标，但它全程参与了从异常预警到作战计划落地的全链条，是将情报观察转化为实战行动的核心辅助工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibO9kiauylaDr2icxNST4YQZRKHsszJqWC7KOBSun6JoWQHe2lnTPZweWgD2zgCtjSf5VNO1tqOJYIB0EjQaFD920onl42pzBBfSZ15YQ3TEQA/640?wx_fmt=gif&from=appmsg)

除了一线作战规划，Palantir 的官方演示与公开信息，还披露了 Claude 在军用场景的更多应用方式：

1. **多模型适配的标准化战术生成**

   Palantir 披露，其客户北约已在 Maven 智能系统中使用 AIP 代理功能。演示界面显示，用户可在系统内自主选择内置的多个 AI 模型，包括 OpenAI 的 ChatGPT、Meta 的 Llama 系列，也可选择 Claude；在演示中，分析人员选定模型后，系统可在 “行动方案（COA）” 模块中，一键生成多套完整军事战略方案，其中包含名为 “火力支援 - 渗透 - 冲击 - 摧毁” 的全流程战术方案。
2. **卫星图像智能解读与行动建议**

   演示中，分析人员可在数字地图上选中 AI 识别出的 3 个油罐车目标，直接加载到 AIP 代理的聊天界面，下达指令 “解读图像并提出下一步操作建议”，系统即可完成卫星图像的专业解读，并输出可落地的行动建议。

   ![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpXiaCVAj6hLGic32iaHWOYMDkZ2jebaiaurZPcV7DJEib63NKDoL4zKAkwfqYHWprlUnMPYzic3eLwnSmQbW2EfJSTOy1SRlenNoqDE/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrb2cx1ibgTgxqx25zibNXejWDXUeFoSIrtHex1V4VwlVI0rbLfneKYIjyGVTbNTtibX41RO9xg6R2h0LWbdJ4iaDZKIsLAliakJvCc/640?wx_fmt=png&from=appmsg)
3. **高阶情报报告快速生成**

   Claude 可大幅压缩情报分析的耗时，为后续打击计划提供支撑。

   2025 年 6 月，Anthropic 公共部门负责人库纳尔・夏尔马曾公开演示：Claude 企业版可基于公开信息，快速生成关于乌克兰 “蜘蛛网行动” 无人机袭击事件的高阶分析报告，还可制作交互式数据仪表盘、将非结构化信息转换为 Palantir Foundry 系统可分析的标准化数据格式，同时可按要求生成指定主题的详细地缘政治分析、军事与政治影响摘要。夏尔马明确表示，原本需要资深分析师花费 5 小时完成的报告撰写工作，Claude 可在极短时间内完成；而通过与 Palantir 的合作，美国联邦政府可让 Claude 调用内部机密数据集完成上述工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoibW9uLvWZROB1FTrHx1vc7ibhx7YOqVibgSmPss3y2uZOBbfQndxRlRkpTKEgE3f99DjcibaQFBzJNmDgdAyTcheNTaQNIiarGWxU/640?wx_fmt=png&from=appmsg)

此次事件暴露的核心矛盾，至今仍无明确答案，Anthropic 一方面公开拒绝为美军开放无限制的模型权限，划定了民用监视、自主武器的伦理红线；另一方面，其核心产品 Claude 早已通过 Palantir 的集成，深度嵌入了美军的情报分析、作战规划、目标打击全链条。

外界的核心质疑始终聚焦于：Claude 在美国军方内部的实际应用，是否已经突破了 Anthropic 自身设定的伦理边界？而五角大楼以 “供应链风险” 打压拒绝无条件配合的 AI 厂商，也暴露了美国政府在军用 AI 领域的管控逻辑与双重标准。

此次事件，也首次为全球清晰展现了生成式 AI 在现代战争中的落地路径：商用大模型厂商通过军工承包商完成军方场景的适配与集成，无需直接与军方签订涉密合同，即可让自身的 AI 能力深度嵌入作战全流程。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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