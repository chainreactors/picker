---
title: 有毒组合：当跨应用权限叠加成风险时
url: https://mp.weixin.qq.com/s/VDqNVXjz0WCDvMs1IvJ_LQ
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:53:42.232552
---

# 有毒组合：当跨应用权限叠加成风险时

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs8buFia22lNxEIf93YOZSsUDkMZ8icWPyeQ0Y1CNUZXNHJCoL7ibXpaCxlO9ehEUIXI3Ju2UawBphheL1fHWoGEPbxeLVR2rz7Ao8/0?wx_fmt=jpeg)

# 有毒组合：当跨应用权限叠加成风险时

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oPZcPicUADs8IBnngsfTjFKjZwUk8t1JhdzH6FTlj3bu5R68GVGmLUpyONKMTgnH5lOKzuTpRu9GiaEd6v9wrviaHseWKB4GAm13uxp4BGXRpg/640?wx_fmt=png&from=appmsg)

2026年1月31日，研究人员披露，为人工智能代理打造的社交网络Moltbook公开了其数据库，公开了77万名活跃代理中的3.5万个电子邮件地址和150万个代理API令牌。

更令人担忧的是私信里。其中一些对话包含明文第三方凭证，包括代理间共享的OpenAI API密钥，存储在与劫持代理自身所需令牌相同的未加密表中。

这是一种有毒组合的形态：两个或多个应用之间的权限崩溃，通过AI代理、集成或OAuth授权桥接，而单个应用所有者从未将其作为自身的风险表面。

Moltbook的代理人坐在那座桥上，携带着主机平台和用户连接的外部服务的凭证，而这两个平台所有者都无法看到。大多数SaaS访问评审仍然一次只关注一个应用，这正是攻击者正在学习的盲点攻击目标。

## 有毒组合的形成

## 有毒的组合很少是单一错误决定的结果。当AI代理、集成或MCP服务器通过OAuth资助、API范围或工具使用链桥接两个或多个应用时，它们就会出现，桥的每一侧单独看起来都很好，因为桥本身没有人评审过。

举个例子，想象一个开发者安装了一个MCP连接器，以便他们的IDE可以根据请求将代码片段上传到Slack频道。Slack管理员批准了机器人;IDE管理员会批准该外站连接;双方都没有认可源编辑与业务信息之间存在的信任关系，这种信任关系在双方实时存在。它双向运行：IDE 内的提示注入将机密代码推送到 Slack，Slack中植入的指令流在下一次会话中回传到 IDE 上下文中。

无论AI代理连接Drive和Salesforce、机器人将源代码库接入团队渠道，还是任何中介通过一个看起来正常的资助让两个应用相互信任，都会出现同样的形状。

## 为什么单一应用的评价总是让人忽略它们

## 常规访问审查很少能捕捉到这种形状。这在现代SaaS开辟的领域中显得压力很大：非人类身份如服务账户、机器人和AI代理，背后没有人类支持，信任关系在运行时而非配置时形成，OAuth和MCP桥接在应用之间却未被治理目录察觉。

回答“谁持有这个范围加上另外两个范围，这些范围能共同实现什么”，一旦这些范围存在于一个没有人通过任何身份系统配置的令牌上，这个问题就变得更加困难。

遥测差距正在迅速扩大。

AI代理、MCP服务器和第三方连接器默认分布在两到三个相邻的应用之间，而在大多数SaaS环境中，非人类身份数量超过了人类。云安全联盟2025年SaaS安全现状报告发现，56%的组织已经担心其SaaS到SaaS集成中API权限过高的问题。

## 值得深思的事情

## 缩小差距主要是调整审核地点，从每个应用内部转移到它们之间。以下是一些值得考虑的事项，以应对这类问题：

| 需要复习的区域 | 实际操作中的样子 |
| --- | --- |
| 非人类身份清单 | 每个AI代理、机器人、MCP服务器和OAuth集成都作为用户账户存放在同一个登记簿中，拥有所有者和审核日期。 |
| 跨应用范围资助 | 在一个身份上新写作用域，而该身份在其他应用中已经持有已读示程，是在批准前被标记，而不是在批准后。 |
| 桥梁创作回顾 | 每个连接两个系统的连接器都有一条审查轨迹，标明双方的名称以及它们之间的信任关系。 |
| 长寿象征性卫生 | 活动范围偏离原授权范围的代币可被撤销，而非续期候选。 |
| 运行时漂移监控 | 跨应用范围的异常和新应用组合中的身份是有毒组合形成的迹象。 |

这些更多是程序性学科，而非产品选择，且它们与现有的访问审查工具配合使用。现实是，没有一个持续监控运行时图表的平台，很难大规模看到这些联系。手动审核不会超过前几十次集成。

## 动态SaaS安全平台的定位

## 动态SaaS安全平台自动化了程序审查所建立的跨应用视图。IGA会为已接入系统盘点角色，而动态SaaS安全则持续监控运行时图表：哪些身份存在，哪些应用被触及，哪些范围依赖哪些令牌，以及在上次配置审查后建立了哪些信任关系。

监控必须持续运行，因为这些平台需要接通的桥接速度相当于MCP安装或OAuth同意点击。

Reco就是这一类别的一个例子。其平台连接了整个SaaS环境中的身份、权限和数据流，因此Slack、Drive和Salesforce中的多个范围组合被视为一个曝光，而非三个独立审批。

第一步是发现环境中运行的每一个AI代理、集成和OAuth身份，确保任何跨应用评测所依赖的库存都真实存在。安保团队不知道存在的特工，或在初次入职后悄悄建立新关系的特工，都会与被授权的特工一同出现。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADsicHDrFWeMaSuGp8jr25pxSbSJIlAUVjH6B1pRdsRzian8sZ02l9SV96q7XeEwyb90Xk8DgZTCScicmNlmDNYH5dhL5CDoEULVFak/640?wx_fmt=jpeg&from=appmsg)

|  |
| --- |
| Reco 的 AI 代理清单，显示已发现的代理与 GitHub 关联。 |

一旦对代理进行清点，Reco的知识图谱会将每个人类和非人类身份映射到它访问的应用及其间的桥梁。当MCP服务器将IDE连接到消息通道，或AI代理将文档存储接入CRM时，图表会自动显示组合，并标记为未被单个应用所有者授权的权限拆解。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADsibScqBpXXUN8sNqiasibpbpx0BE733eSPSanu3II4vaVibXrlQBCE0sX6TFTrVqAvnbVYYVmO8LibqSp7M1zHWkiclicTwHC9OUbeibuE/640?wx_fmt=jpeg&from=appmsg)

|  |
| --- |
| Reco的知识图谱展示了Slack和光标之间的有毒组合。 |

从那时起，Reco会抓住集成开始超出批准范围的行为，并在任何人使用之前撤销高风险访问权限。链条，而不是应用，成为你审查的对象，这种转变正是让有毒组合显现的原因。

大多数组织的下一次泄露不会通过新的零日漏洞来宣布。看起来就像特工完全按照授权执行任务，直到撤离。这是否会在审批时被发现，还是在事后审查中被记录，关键在于是否有人能看到完整的链条。

看到完整的链条正是Reco动态SaaS安全平台的初心。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

HackSee安全生活

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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