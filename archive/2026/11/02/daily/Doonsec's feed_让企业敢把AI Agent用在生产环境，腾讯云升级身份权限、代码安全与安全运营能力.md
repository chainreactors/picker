---
title: 让企业敢把AI Agent用在生产环境，腾讯云升级身份权限、代码安全与安全运营能力
url: https://mp.weixin.qq.com/s/OB506wloFaxldMrpRzF6ag
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:48:53.938215
---

# 让企业敢把AI Agent用在生产环境，腾讯云升级身份权限、代码安全与安全运营能力

# 让企业敢把AI Agent用在生产环境，腾讯云升级身份权限、代码安全与安全运营能力

腾讯安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在刚刚结束的2026腾讯全球数字生态大会Agent安全专场上，腾讯云携手荣耀、PPIO等产业伙伴，从治理原则、平台防护、代码开发与安全运营，到企业落地、执行环境与算力底座，逐层拆解了AI Agent进入生产环境后的风险变化与应对方式，并升级身份权限、代码安全与安全运营能力。

当前，AI正从“能聊天、会回答”的ChatBot，演进为可自主规划、拆解并执行任务的AI Agent。企业对AI的治理重点，也从担忧“说错话”转向警惕“做错事”。腾讯云副总裁董志强表示，今年3月，腾讯云切入AI安全赛道，基于巨大业务体量的实战与沉淀，将AI安全治理归纳为“Agent行为可控、过程可回溯、结果可撤销”三大核心准则，护航企业AI Agent规模化落地，并为腾讯WorkBuddy、TokenHub、ClawPro等Agent类产品保驾护航。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iczOE5KEJun7lUf66xPQbzTeyBklTvg0CIPaAPAaWDxh9bxGFyomLgyjNwrpMjld8BvOibAVTvTFsUynOJnfbPheY8XR7gJicRxvudIMCcCibsA/640?wx_fmt=jpeg&from=appmsg)

（腾讯云副总裁董志强）

# 当Agent成为新操作主体

# 企业权限模型需要重新划分

腾讯云Agent安全负责人柯灵杰介绍，随着访问主体、权限模型、数据出口和攻击方式同时变化，Agent在企业落地中的风险集中在身份与权限、模型与内容、AI供应链、基础设施与平台、运行时与行为五类。其中尤其难防的是数据出向：入向可以设白名单，出向却要回答“数据要去哪”这个开放性问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iczOE5KEJun5SaMsvwSKtSdsF7nm18HxYDFWrxzQK3JIa0UgXv1VxXSbHEMCHIZ6P2ot2dHCcIibmLUkGmeK4WP4DMhH4bbBibLiapUgAGRsc6A/640?wx_fmt=jpeg&from=appmsg)

（腾讯云Agent安全负责人柯灵杰）

这意味着，企业权限模型不能只“以人为中心”，而需转向“人与Agent双主体”。与之对应的是，企业必须回答五个问题：是哪个Agent在操作？它使用的是谁的凭证？访问了哪些数据？异常行为能否被及时阻断？已产生的结果能否撤回或回滚？为此，腾讯将iOA从终端办公产品升级为AI Agent安全产品，提供身份发现与治理、访问与权限管理、运行时防护、数据安全与全流程审计五类能力，并在模型输入、终端环境和敏感信息处置环节设置卡点。

此外，腾讯云 TC-AICC可信计算还能在云端提供机密环境，确保模型推理过程中数据“可用不可见”。目前，TC-AICC可信计算已在WorkBuddy落地；同时，WorkBuddy联合腾讯iOA将防护延伸至终端，通过识别并管控未经审批的影子AI应用，防止敏感数据经Agent外泄。

# 代码审计从“能不能发现”

# 转向“值不值得处理”

风险不只出现在运行环节，也提前到了代码编写环节。随着大模型对代码理解能力提升，业界要解决的问题已从“AI能不能发现漏洞”变成“发现的漏洞太多、运营团队消化不过来”。

腾讯云安全总经理谢飞介绍，为解决这一问题，腾讯云代码安全产品CodeBuddy Security采用“双引擎协同+沙箱实证”模式，所有发现的漏洞都须在隔离环境中完成复现验证，只交付“带确凿证据”的漏洞。与之配合的AI自主渗透测试产品“无境”，则以自主发现、自主利用、自主验证、输出证据为核心，将渗透测试从纯手工转向全自动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iczOE5KEJun4b1YUCsbozTN2n34YIQKiaQzZ6HcOrCEQYhiaHFkfvcBUyiaibrB7FFlKulJL36Vdfld5fWDib4ppnRt9m0gqetOicXaxz2DcQpe65E/640?wx_fmt=jpeg&from=appmsg)

（腾讯云安全总经理谢飞）

腾讯云安全运营专家郭显杰补充，面对数量激增的漏洞，传统静态扫描面临业务逻辑理解难、覆盖难的问题。为此，腾讯在原有SDLc体系上叠加AI能力：传统扫描速度快、产出稳定，继续承担发布流程中的基础卡点；AI则补位原先依赖人工的代码审计与资产识别，提升漏洞确认效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iczOE5KEJun4dmcbsKSdzMuXzvTWN6l4Sb4fibX5Ctrk6B6fv4ibMdnMHbEqJkLmRJrxfP6E9u3zwg7lRAamKuLoktnMXkmZ30w8tDicbVCzIgk/640?wx_fmt=jpeg&from=appmsg)

（腾讯云安全运营专家郭显杰）

# 从应用治理到算力底座

# AI Agent落地需要多层协同

现场，荣耀、PPIO、NVIDIA分别从AI应用治理、Agent沙箱隔离和运行时算力层，展示如何将AI Agent规模化落地。

荣耀安全产品部部长林结斌介绍，荣耀的AI安全实践已推进两年。进入AI Agent阶段，荣耀在组件准入、运行时和意图检测等环节重建管控，结合腾讯大模型防火墙管住模型输入输出安全，并在可信部署环节与腾讯打造了面向AI应用的可信执行环境。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iczOE5KEJun6qlc1FWrCrY13ISt6HeXYMkiaaEpIj89FoD1BxOU7jX9UXHZRMDj1vP7icIzUibv0PE1bVGiapblukSlqCeX1pF3sMhhAeT7ltAvo/640?wx_fmt=jpeg&from=appmsg)

（荣耀安全产品部部长林结斌）

PPIO Sandbox产品专家宋书豪介绍，PPIO的Agent沙箱运行在腾讯云之上，通过凭证隔离、双向网络管控和访问认证限制Agent行为，异常可溯源到具体Agent与命令。双方还把防护延伸到主机层与应用层，由腾讯云主机安全能力对运行负载巡检，沙箱底层基于硬件级隔离。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iczOE5KEJun6Jf8ckQJibLztqbeXtmaoPziaPeCjp74nAcs8WopW3ptyurtcXvlpBibxm8ebMiba49x1xU1gGAqJPf835rSOOJ7jYdl1m7ribByZo/640?wx_fmt=jpeg&from=appmsg)

（PPIO Sandbox产品专家宋书豪）

NVIDIA解决方案架构师杨赟介绍了面向Agent的运行时与算力层方案：本地设备可让数据不离开设备完成推理；运行时约束Agent对文件与网络的访问，管理权限层级高于Agent自身权限，并由芯片级独立监控实现快速阻断；数据中心侧提供全链路加密的可信执行环境。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iczOE5KEJun5xe8fTB6TRfrukDJicbaOeHeTHJ4DabnFDjxaQNibF2eQDWEjDgRCZpc4FQ5dW96BO3bB8gsbFpRepR1oRoJX4YOCKibwfYIzib9c/640?wx_fmt=jpeg&from=appmsg)

（NVIDIA解决方案架构师杨赟）

# 结语

从治理原则、平台防护、代码开发到安全运营，腾讯云正通过全栈安全能力，助力产业伙伴实现AI Agent落地实际场景的行为可控、过程可回溯、结果可撤销。未来，腾讯云将携手更多产业伙伴，推动AI Agent从好用走向可信可控，加速AI在千行百业的规模化落地。

预览时标签不可点

不喜欢

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