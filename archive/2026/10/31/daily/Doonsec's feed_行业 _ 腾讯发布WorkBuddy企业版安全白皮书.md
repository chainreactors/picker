---
title: 行业 | 腾讯发布WorkBuddy企业版安全白皮书
url: https://mp.weixin.qq.com/s/3olY2DYF7qm7wnKgbMNcjg
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:20:47.576421
---

# 行业 | 腾讯发布WorkBuddy企业版安全白皮书

# 行业 | 腾讯发布WorkBuddy企业版安全白皮书

中国信息安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20Cj2v7VWpXCGW7TbCyH6oTOUPZ56LBZwFIye0T2a3QSA2kA4tba6nuHbMic3Yh2WMxfQiaG0gtCiakI3J2QJjNGmAVz4lve1CYkoQw/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?navIndex=3)

10月30日，在2026腾讯全球数字生态大会WorkBuddy超级组织专场现场，腾讯发布《WorkBuddy企业版安全白皮书》（以下简称“白皮书”），首次系统披露WorkBuddy全链路安全管控体系。WorkBuddy围绕“行为可控、过程可溯、数据可管”建立可信AI治理体系：事前识别风险，事中拦截危险操作，事后支持恢复，并记录拦截与放行事件，方便查询和追溯。

![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20Cj8u0H64jtHnk2GAOQglW09RDlrPQWEfpkHnkkn03BxXBLVAmHaVsxicrGdic7vhiaHJfrrrYPqY6dsgR4TYo00zu7XiaH5I8nzNmc/640?wx_fmt=png&from=appmsg)

《WorkBuddy企业版安全白皮书》发布现场

**企业最担心Agent四类安全问题**

AI从“能对话”走向“能干活”之后，风险环境也变得更为复杂。除了说错话，Agent还有可能删错文件、执行危险命令，甚至引发敏感数据外发、加载被投毒的第三方能力包等安全风险。

白皮书根据客户问询与反馈，将企业应用Agent核心顾虑归纳为四类：“会不会失控，或者背着我干坏事？”“会不会乱删我的东西，能拿回来吗？”“我能知道它做了哪些事情吗？”“会不会泄露我的数据和隐私？”。

企业之所以有这些顾虑，核心原因在于Agent的能力更为强大。它不仅能读写终端文件、在终端执行命令，而且，为了完成任务还要获得员工的账号、API Key与企业系统访问凭据，还能通过技能与连接器不断扩展能力。Agent一旦出现安全问题，企业的业务系统、数据资产都将受到冲击。

针对四类顾虑，WorkBuddy将安全控制放在Agent动手之前并强制生效：在加载外部能力时，先经过风险检测，确认安全后方可调用；高危命令执行前需要确认，员工也能随时一键叫停。文件改动则留有退路，每轮修改前自动备份、删除先进回收站，一轮任务造成的改动可以整体回滚。所有拦截与放行统一留痕，每次拦截都说明拦了什么、依据哪条规则，实现记录可查询、可导出。敏感信息则在本地完成识别与脱敏，全链路加密，推理侧可选可信计算，实现明文不出域。

**WorkBuddy让Agent可控可溯可管**

这套安全防线建立在腾讯20多年的安全积累经验之上。WorkBuddy把终端安全运营、红蓝对抗、威胁情报与风控合规的实战积累沉淀，形成面向企业的全链路安全管控体系。

WorkBuddy以“可控、可溯、可管”为目标，为企业构建“事前识别、事中拦截、事后恢复、全程留痕”四道防线，让企业更安心地把Agent用起来。

行为可控。 WorkBuddy客户端提供Mac、Windows、Linux原生级沙箱，把文件读写与命令执行收敛在授权工作目录内，目录以外默认不可写。SSH密钥、云平台凭据等8类敏感路径默认受保护，内置预设文件规则106条；rm -rf、sudo等高危命令默认前置询问；员工可随时终止任务，关闭客户端时沙箱随之退出并回收Agent拉起的全部后台进程。无论对话进行多少轮，执行层的硬性规则都不受影响。

过程可溯。拦截与放行事件统一进入审计中心，每次拦截都说明拦了什么、依据哪条规则，记录可查询、可导出。管理端操作日志覆盖操作内容、操作人员、IP、时间等六要素。

数据可管。敏感信息在输入框、工具返回、数据外发三个入口于本地完成识别，按允许放行、加密保护、拒绝三种策略处置，识别与脱敏全程不出网。推理侧可选可信计算，明文只在客户端与可信执行环境可见，云服务商与运维人员均无法访问；传输环节采用“TLS 1.2+加密”。

误删和误改有兜底。Agent每轮修改文件前自动备份，删除操作默认移入系统回收站，一次删除或修改的文件数量超过阈值时自动暂停等待确认，一轮任务产生的全部改动可整体回滚。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20CgCm7MD98p2aGzY3BhjgVJWibtU53ibzy8x7AnzWAOkaVY8krwqiazKwMYFy3702dYHkicVvJo5lv9XRNmdjicWXq0K57FJIwzkqa00/640?wx_fmt=png&from=appmsg)

WorkBuddy 企业版全链路安全管控闭环

面对开放的第三方生态，WorkBuddy建立了一套覆盖全生命周期的生态安全检测机制。每一个技能与专家连接器在提交上架时，均须先通过风险文件检测与沙箱行为检测，确认不含恶意文件与高危行为后，再进入开发者实名与资质核验、真实任务能力评测环节；上架后仍持续接受动态检测。过去三个月，该机制已拦截超300个问题技能与专家上架。

WorkBuddy联合腾讯iOA把防护延伸到终端环境，识别并管控未经审批的影子AI应用，检测终端病毒与漏洞，防止企业敏感数据通过 Agent外泄到互联网，为企业提供更多定制化的安全防护方案。

**WorkBuddy在金融、政务等多行业落地**

WorkBuddy这套安全能力也得到了广泛的认可：WorkBuddy首批通过“可信AI-智能助理智能体（Claw）”评估，全国首个且唯一获颁“自动化决策-智能助理（Claw类）二星+级标识证书”，并获评Claw类智能体应用优秀产品。WorkBuddy内置的可信计算获评“企业级大模型推理安全成熟度‘最高等级’引领级”。与此同时，WorkBuddy参编了深圳《人工智能可信办公智能体标准体系》，把自身的可信AI办公实践写进标准。

自2026年3月初上线以来，WorkBuddy已迭代100个大版本，累计完成90亿次用户任务请求。WorkBuddy企业版已落地政务、教育、零售、金融、传媒、出行等50多个行业，覆盖50%中国企业500强，受到政企客户广泛认可，融入真实场景，助力生产力升级。在金融行业，WorkBuddy已入职超250家金融机构，进入对公信贷尽调、投研投顾、合规审查、客户经营、财富资配等上百个业务场景。

当Agent加速走进办公场景，安全已不再是附加题，而是规模化落地的必答题。白皮书围绕企业最为关注的安全顾虑，从制度建设到数据分级，再到治理措施给出完整落地路径，并与WorkBuddy自身的安全能力深度对齐，让企业每一次调用Agent都可控、可溯、可管，把“敢用”变成“放心用”。

![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20Cg3VWD80bLcLibz5sicGIcvtbNCjyNd9IS5ziaYOd9iaicSsJQpt8glXnTebzKmvBM70ZxM5jgniaOiaOAPEnk9xaficgialls6qlWxGt7s/640?wx_fmt=png&from=appmsg)

扫描二维码查阅《WorkBuddy企业版安全白皮书》完整版

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20CgzSibQGWAGCQZmiczKibuibyTaeLj1AG46SqCTPFicibJfMZ7LkvufAonoangXAhkKylWbCia6FomhaPCZb0Eiaf3iczjfkUx8ddic9KdDE/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20ChW3fARGIBuXqzRQJmqOfA7D2dLp1kp3NdV3mS8LJ7B138RJUwPNfwOARSkk8hjvicpNYZE8s0ibX9CNvEfQqia7MlABmYKTcSMZQ/640?wx_fmt=png&from=appmsg)](https://cisat.cn/)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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