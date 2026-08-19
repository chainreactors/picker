---
title: 腾讯云AIxa0Agent安全网关护航银河证券启睿Skill上架WorkBuddy ——从“能查询”走向“放心调用”
url: https://mp.weixin.qq.com/s/exzBrAr2oSrGdXHfF2VINg
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:54:58.303435
---

# 腾讯云AIxa0Agent安全网关护航银河证券启睿Skill上架WorkBuddy ——从“能查询”走向“放心调用”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iczOE5KEJun5R0bhMWLFZI0N2KF12j857JHHSubBunLHT2iaiaPMfAkpzjiaYHJzNpwWx31WE6lPgadv5cs9adLNRqrvEsBPrq36RWjKxTyU6K0/0?wx_fmt=jpeg)

# 腾讯云AI Agent安全网关护航银河证券启睿Skill上架WorkBuddy ——从“能查询”走向“放心调用”

腾讯安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

大模型在投研里的角色正在变化：从读研报、写摘要，走向直接调用专业系统的能力。可当业务能力真的交到Agent手上，安全的提法也变了——过去问“这个接口安不安全”，现在要问四个问题：身份是否可信，授权是否最小，凭据是否泄露，行为是否偏离预期。

近期，中国银河证券启睿策略中心5个Skill正式上线Workbuddy及Skillhub，把数据服务、策略构建、策略回测、策略分析等能力标准化封装，开放给兼容 MCP 协议的大模型调用。腾讯云提供 AI Agent 安全网关及配套安全能力，完成Skill上线前的安全加固。

Workbuddy访问接入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun5sUoKr7pf4ePlqS3mbVsAp8RPt8UKKuPcK9DeF3QL8E4YNICqvDjibJPFQxUAf6zgqicAicTJfkSiavb8q5gn8R8Wq80G3lsLo86Q/640?wx_fmt=png&from=appmsg)

Skillhub下载地址：https://skillhub.cn/enterprise/org-0ueytgdu

➢ 银河证券开放了哪些能力？

五项能力覆盖策略量化全流程：

* 启睿金融数据 Skill：覆盖行情、财务、技术指标、因子等 12 大类金融数据接口，支持模型按需调用，适配投研取数、基本面分析、行情复盘、因子研究等场景。
* 启睿策略构建 Skill：用户用自然语言描述投资思路，模型结合平台 Skill 生成合规的量化策略代码，把策略开发门槛降到“说清楚想法”。
* 启睿策略回测 Skill：执行日线或分钟级历史回测，自动生成收益、风险、交易明细等核心绩效指标。
* 启睿策略对比分析 Skill：把多组回测结果放进同一坐标系，从收益表现、风险特征等维度横向比较。
* MCP 接入能力：支持行情与技术指标、上市公司资讯、财务数据等数据获取，可在机构自有 AI 应用中灵活组合。

五项能力共享同一个前提：Agent要访问策略中心、业务 API 和数据服务，权限和凭据就要跨越对话、Skill、网关和业务系统流转。这条流转链，才是安全建设真正的工作面。

➢ Agent自主调用带来五类风险

传统应用的调用路径是固定的，前端到后端一条线。Agent不一样——它自主选择Skill、发现 MCP 工具、生成参数、连续执行动作。上线前的安全评估梳理出五类风险：

Agent 场景五类风险与控制方向

![](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun42ydLibicX4AlbGcsMiauj30tO5o2BiaFH8oNmxrcD4gzC1BoiaoAmicyLlkO7rX9ibyLLic08CLYuNw0As8Gmj7TDShMgtJST48jopRw/640?wx_fmt=png&from=appmsg)

五类风险的共同点是：它们都不发生在“接口”上，而发生在Agent的“行为”里。

➢ 腾讯云 AI Agent 安全网关，让每一次调用身份可验

腾讯云的方案是把 AI Agent 安全网关放在Agent与模型、Skill、MCP 及业务系统之间。网关既是调用代理，也是安全决策点。

MCP 资源先发布到网关，再下发给Agent，一次完整调用是这样走完的：

![](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun6a8jJLP4e2QTGSQAsSVujLicT82YydL9LCCKOTbxAiatqpu4hIyS1k3db7LlQT1GP40yrOEIsAGymjlF34OvESMon4p4y07zm5c/640?wx_fmt=png&from=appmsg)

五步走完，Agent端从头到尾没有出现过一次明文密钥

![](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun4kicCl8SFGSqwoPkGZg3H9nVVgdQMBgficmzp2eLQBbBS9Pqm0VHEHoa2iarlJBEPMp4Iicapk23EycOU7upiaicDqtgt7IgmteRkBo/640?wx_fmt=png&from=appmsg)

背后是Tencent OneID 身份安全承担统一身份认证，支持 OAuth2、账密、手机号验证码等方式，把“谁在调用”确认下来并与业务权限关联。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun72zrWwIkPChj9JYcEN9NR2SyGfa7FayEtqvvZ37yueYMQeTT0ib1ZTdXJ25O8bF64R7am1LichM4HWDpXfchTOwcxG5lBAf6D4g/640?wx_fmt=png&from=appmsg)

凭据不落地不等于业务系统不再使用密钥，而是让长期凭据不再进入Agent配置、对话和普通日志，网关只在经过认证授权的调用窗口内获得最小化使用能力。

➢ 腾讯云AI Agent安全网关，覆盖Agent运行全流程

只检查模型输出内容是不够的，工具权限和业务参数同样要看住。

AI Agent安全网关在四个层面同时施加控制：

四层控制的检测重点与处置方式

![](https://mmbiz.qpic.cn/mmbiz_png/iczOE5KEJun6GNic6RN9D7d39YlGMmicicwVDBvwaiaNlMxtLPzicrxJHMcP7LABgD4PQbGXgnrEzUqAWjicicsxmD5F9PtC7U6Fian46FYGS0hTpdQI/640?wx_fmt=png&from=appmsg)

银河证券原有的网络安全体系继续在外围构成纵深防御，策略中心和真实源站不再直接暴露，攻击面随之收窄。

➢ 让AI投研能力可用、可控、可追溯

安全能力看似在后台，实际上决定了 AI 投研能力能否安全开放、使用过程能否保持可控，具体体现在两方面：

一是能力能不能真的开放出来。如果密钥必须手工配置、MCP 必须裸暴露，专业能力的开放半径就会被安全边界死死限制在少数人的试点环境里。凭据不落地和调用即认证解决了这个矛盾，数据、因子、策略、回测这些原本留在机构内部的能力，才有条件通过标准化方式交到更多用户手上。

二是用起来放不放心。每一次调用都能确认身份、执行策略、检查内容并留下证据——策略是自己的，数据是受控的，这是“敢用”的底线。

过去，给Agent接入业务能力，意味着把密钥交出去，把暴露面赌进去。

现在，从静态密钥配置在Agent，到使用时认证、按需签发、网关代理调用；从获取与使用分离，到谁调用、谁认证、谁负责；从单点产品堆叠，到身份、凭据、模型、MCP 协同联防。

AI Agent 的价值来自能理解、能规划、能调用、能执行，风险也来自同样的能力。安全落地的关键不是给模型再加一个孤立的过滤器，而是建立贯穿身份、凭据、工具、数据、网络和运行时的统一控制面。

启睿策略中心的 MCP 与 Skill 服务只是首批功能。腾讯云会和金融机构一起，把这条链路继续走宽——让 AI 投研从“可以用”，走到“放心用、可证明、可运营”。

风险提示：本文仅介绍启睿 Skill 的功能、安全加固方案，所有数据及计算结果仅供研究学习参考，不构成任何投资建议。所有历史及回测数据仅供参考，过往表现不代表未来收益。投资有风险，入市需谨慎。请根据自身风险承受能力做出独立投资决策。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkden5qImICHSWibmMCI4FicszTR8S7nlM2YCmuB5GWQtBfqLicRmcu06jzFXmIOgiaeUQheLIDaw8vfpBdw/0?wx_fmt=png)

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