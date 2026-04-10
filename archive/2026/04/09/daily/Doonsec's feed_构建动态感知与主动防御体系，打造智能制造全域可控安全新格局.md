---
title: 构建动态感知与主动防御体系，打造智能制造全域可控安全新格局
url: https://mp.weixin.qq.com/s/6j9wsBqiBKN6lSvyQRgMKg
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:44:00.088148
---

# 构建动态感知与主动防御体系，打造智能制造全域可控安全新格局

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1Vd0DvJG7yRGh7iayUOv1gLpj0WCcic56fwar0CyNwtbPmlzyJsRsdb6rTTO3sLDGynsyuQ5pq8QlWBJuwK1FFpKOQia16zZOUOYCzhibV3jbKQ/0?wx_fmt=jpeg)

# 构建动态感知与主动防御体系，打造智能制造全域可控安全新格局

原创

自主研发技术驱动
自主研发技术驱动

珞安科技

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/eXicedYoc2qUBq2XkibuVB46Wic8VXSpNXhplqfNmFooI0CWrFiagkCiarAuyia5s4gO5t1IgibprGPGb0Mskt144vpNw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![](https://mmbiz.qpic.cn/mmbiz_png/1Vd0DvJG7yQEtiaRVwSkJx6YU6gFvRSkptcbyf8YehsQn9KriaxtsKDEZ8RwDedVjsiba2wE0USWKYoDp1J6sEy7h3dRiaTylnGFaH5QzfmYLlA/640?wx_fmt=png&from=appmsg)

**一**

**行业背景**

智能制造作为新一轮产业变革的重要方向，是推动制造业高质量发展的关键路径。随着工业互联网、5G、云计算、大数据、人工智能等技术与生产环节的深度融合，传统工业控制系统正逐步向网络化、平台化、智能化方向演进，生产设备、控制系统与企业管理系统之间实现高度互联互通，构建起覆盖设计、生产、仓储、物流与运维的全流程数字化体系。

在高度互联的环境下，智能制造工业控制系统的暴露面显著扩大，面临勒索软件、APT攻击、供应链攻击、恶意代码注入等多样化威胁。一旦核心控制系统遭到入侵，可能导致生产线停摆、设备异常运行、关键工艺参数被篡改，甚至引发安全生产事故与重大经济损失。因此，构建适配智能制造场景的纵深防御安全体系，已成为保障生产连续性与数据安全的关键任务。

**二**

**防护范围**

**防护对象**

本方案防护对象为智能制造企业工业控制系统，主要包含但不限于SCADA系统、PLC控制系统、工业机器人控制单元、边缘计算节点及相关数据库与服务器等软硬件系统。

**定级说明**

智能制造企业工业控制系统通常按照“等保三级”进行建设。

**三**

**需求分析**

**网络边界安全防护需求**

工业控制网络需要与办公网络、外部网络进行互联互通，若缺乏有效的边界防护措施，可能导致病毒、攻击流量或非法访问进入工业控制网络，影响生产系统稳定运行，因此需要对关键网络边界进行严格访问控制和隔离防护。

**工业协议安全监测需求**

工业控制网络中大量使用Modbus、OPC、S7等工业协议，这些协议普遍缺乏认证与加密机制，容易被攻击者利用进行非法控制或数据篡改，因此需要具备对工业协议通信行为的识别、监测与异常分析能力。

**终端设备安全防护需求**

工业控制系统中的工程师站、操作员站、服务器等终端设备长期运行，系统补丁更新困难且防护能力有限，一旦感染病毒或被恶意利用，可能直接影响生产控制系统安全与稳定运行。

**运维安全与访问管控需求**

生产系统日常需要运维人员进行维护、配置调整及系统管理，如果缺乏统一的运维访问管控机制，可能导致越权操作、误操作或账号滥用，给生产系统带来安全风险。

**安全审计与日志管理需求**

工业控制系统中的网络设备、安全设备及主机系统会产生大量运行日志，如果缺乏集中审计与分析能力，难以及时发现安全事件，也无法为事后追溯与责任认定提供依据。

**安全统一管理与态势感知需求**

工业控制系统中安全设备类型多、系统复杂，如果缺乏统一管理与安全态势平台，难以全面掌握工业控制网络整体安全状况，也不利于安全事件的快速响应与决策。

**四**

**解决方案**

珞安科技作为国内工控安全领域技术先进、实力深厚的优秀企业，依据GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》、工信部网安〔2024〕14号《工业控制系统网络安全防护指南》，围绕智能制造企业工业控制系统安全需求制定方案，构建分区分域、纵深防御的防护体系，在不影响生产连续性的前提下，全面提升工业控制系统网络安全防护水平。

**01**

**网络边界安全防护能力建设**

在工业控制网络关键边界部署安全隔离设备，通过访问控制策略、协议白名单及网络分区隔离，实现生产网、管理网和外部网络之间的安全隔离，限制非法访问和异常通信，确保工业控制网络边界安全。

**02**

**工业协议安全监测能力建设**

部署工业入侵检测和工业网络监测系统，对工业协议进行深度解析与行为分析，实时监测异常通信、非法指令和异常流量，并通过告警和日志记录实现安全事件可视化，提升工业网络安全监测与预警能力。

**03**

**终端设备安全防护能力建设**

部署工业主机安全防护软件，对关键终端进行主机加固、恶意代码防护、漏洞管理及应用白名单控制，同时限制不必要的系统服务与权限，从终端层面提升工业控制系统的整体安全防护能力。

**04**

**运维安全与访问管控能力建设**

部署运维安全管理平台，实现统一身份认证、访问授权与操作审计，对运维行为进行全过程记录与回溯，同时采用最小权限控制策略，规范运维操作流程，确保运维行为安全可控。

**05**

**安全审计与日志管理能力建设**

部署日志审计与分析平台，对网络设备、安全设备及工业主机日志进行集中采集、存储与分析，通过关联分析和可视化展示实现安全事件识别与溯源，提高安全审计与事件响应能力。

**06**

**安全统一管理与态势感知能力建设**

部署工业安全管理与态势感知平台，对安全设备、网络流量及日志信息进行集中管理与关联分析，通过可视化态势展示、风险评估及告警联动，实现工业控制系统安全的集中监控与统一管理。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1Vd0DvJG7ySMyWurLkZhW8lHEODWibdqDz4su2qBKf2ochfwNoZRZEtjX4APENQTEybNaIqaobVFQaibohjkzXP9FYG5570HsvXvQJJ8TIibAY/640?wx_fmt=jpeg&from=appmsg)

**五**

**结 语**

当前，智能制造行业的工控网络安全正处于数字化转型与安全威胁深度交织的关键阶段。以物理隔离与防火墙为核心的被动式边界防护体系，已难以有效应对日益复杂的攻击形态。随着IT与OT融合进程的持续深化，工控网络安全架构正经历从静态、被动边界防御向动态、主动智能防护的根本性演进。

珞安科技将秉持“守护工业网络空间安全，为国家关键信息基础设施保驾护航”的愿景使命，充分发挥专精特新企业的技术与创新优势，依托前沿技术积淀与自主研发产品矩阵，构建具备动态感知、主动防御与智能决策能力的新一代安全防护体系。筑牢关键信息基础设施的网络空间安全屏障，深度赋能国家工业体系的抗风险韧性，为提升产业链自主可控水平提供坚实的安全底座。

**珞安科技**

**北京珞安科技有限责任公司（简称：珞安科技）成立于2016年，是专注工业网络空间安全的创新型高科技企业和国家专精特新“小巨人”企业，并于2022年行业内率先通过CMMI5级认证。**

珞安科技拥有业内顶尖工控安全专家团队、工业网络空间安全研究实验室和四大研发中心，坚持自主研发和技术创新，以零信任理念和体系化思想为指导，打造“实战化、易部署、易维护”工控网络安全产品体系，覆盖工控安全、业务安全和工业互联网安全，构建了全方位的工业网络空间安全防护体系。

依托强大的技术原厂商实力，积极开展安全服务和安全运营，业务遍布20多个行业的2000余家工业企业。在全国设有20+分子公司及办事处，提供7\*24h安全应急服务响应，保障国家关键信息基础设施安全稳定运行。

![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn5JEGIJwk3K7YskNAsooBaDicu1JBb0qCgYF4MlIgbasEibZPiaxIO5vvIicSkppgrgic3iaYqUJuR0O43w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn6YThhy11Smc2QOP8zOBxpqd8SpV8ic7Fc3BjiaKwDfBzpy76Lf5ianBDGL2BoXWicJm8U4ZnYI3CSQ3g/640?wx_fmt=gif)

[![](https://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qU4pYSOiboDSQCY4yT9vE5zjnXibn1fbLrd5VdUJt7ia9aBuNPrAqP0TGVsuKj5JpOVPvmmQa5KzTnbg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247513919&idx=1&sn=9f32651c7632a68a21045998a4404155&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qU4pYSOiboDSQCY4yT9vE5zj2QFzg1ich8FPfrL4kRxibseRKmopkH9GRld6o6FQCQwx8ClVZBwuFiaBA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247513842&idx=1&sn=65365348dabb59355d00d5f625577259&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qU4pYSOiboDSQCY4yT9vE5zjd79eibpjFB0AicY6o9BRcLqMxc9hsXSBb60Pp6qhgu1ha7aYZb3nfK3A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247513502&idx=1&sn=940447340ce70594fa53fbbabd7cddaf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qU4pYSOiboDSQCY4yT9vE5zjib4WT76Nh9PO7qxdvtsa8ECh4iapB90aBX8IWWAaf6gsIBvOoUg324LA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247513694&idx=1&sn=a8d71e1a0f04d2c7939dc5f47e275c12&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/eXicedYoc2qU6L7OdM6LWJZ3NrSxRiasZrBX7nKAn9QxSI5xT77YSJXFoohNZeuyb1moicaxZe3vEw9jNGkogEJ6w/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qVC3qT2LCRbwyVyLJibgFSxJDHwh311aUAdeibE2vWyZ7pAkpH4c2pyrLDvYOt48Lhd9D8NutFeMTCg/0?wx_fmt=png)

珞安科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qVC3qT2LCRbwyVyLJibgFSxJDHwh311aUAdeibE2vWyZ7pAkpH4c2pyrLDvYOt48Lhd9D8NutFeMTCg/0?wx_fmt=png)

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