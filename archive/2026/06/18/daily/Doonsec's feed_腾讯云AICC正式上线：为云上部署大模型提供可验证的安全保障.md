---
title: 腾讯云AICC正式上线：为云上部署大模型提供可验证的安全保障
url: https://mp.weixin.qq.com/s/yzGYd2lhXvuIO80UbEQaKQ
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:04:45.080816
---

# 腾讯云AICC正式上线：为云上部署大模型提供可验证的安全保障

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iczOE5KEJun6Lxc6pGnlIPXiaIzMATBGQhGRWyicaXmibibczpiak8IZayN7picqCfA4Nqo2iaLcItGZ9zUCWoddTR5NUQyLUIaaicVa18XYUXPOrwkI/0?wx_fmt=jpeg)

# 腾讯云AICC正式上线：为云上部署大模型提供可验证的安全保障

腾讯安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

当企业把大模型接入核心业务时，一个绕不开的问题是：数据放到云端，会不会有泄露风险？尤其是金融、政务、医疗等行业，对数据安全的要求极为严格。为了解决这一问题，不少企业选择将模型部署在本地，但随之而来的是成本高、运维重的现实压力。

针对这一痛点，腾讯云推出可信集群AICC（AI Confidential Computing），并参编了中国信通院《企业级大模型推理安全成熟度》标准，为企业云端AI推理提供可验证的安全保障。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iczOE5KEJun6swQLfNpKRBdGCtRiakZd2qsDGR29aalichiaDnAEHon7UicaoKMlHQNcbUaaZia85QPlrhdNtutRCTqiaFfRInAEYaCToGR2B2NDFw/640?wx_fmt=png&from=appmsg)

# ➢ 四大应用场景，适配不同业务的安全需求

腾讯云AICC并非单一的安全加固方案，而是围绕不同业务场景的推理需求提供对应的可信能力。

企业Agent：覆盖知识问答、流程协同与工具调用，企业在搭建智能助手时，往往需要在长业务链路中打通代码库、文档处理、BI分析等多个系统权限边界。AICC的可信集群让这些跨系统的复杂调用在安全边界内完成落地，确保数据不出可控范围。

AI Coding：覆盖开发者日常的代码补全、Code Review、DevOps辅助等操作对推理性能要求较高的场景，AICC通过可扩展集群提供弹性算力支持，在保障安全的同时满足组织级AI Coding的高频调用需求。

智能终端：针对于智能座舱、AI PC、AI手机等消费电子终端，当这些设备需要借助云端模型来增强本地AI能力时，AICC为上云的推理环节提供可信算力保障，确保用户数据在传输链路中不被截获，在计算节点上不留存，保障用户隐私安全。

高安全可信推理：聚焦金融、医疗、政务等数据敏感行业，AICC基于机密算力池提供可信推理能力，满足智能投研、辅助问诊、政务问答、公文辅写等高敏感数据场景的安全落地需求。

# ➢ 两层安全机制，让每一笔推理都有迹可循

当企业调用AICC时，系统会在两个环节建立安全保障。

第一层是算力一致性校验。通过密码学技术对硬件、资源、算力进行完整性验证，确保企业实际调用的这批算力与约定的配置一致，中途没有被替换。

第二层是数据全链路加密与自动销毁。推理请求和结果在传输和计算过程中全程加密，任务完成后会话密钥自动销毁，数据零残留。

两层安全机制叠加的效果是：企业的数据从进入系统到完成计算的整个生命周期中，始终处于受控状态——进门有凭证验证，离开不留任何痕迹。

➢ 服务端无额外损耗，加密损耗控制在5%以内

"加了安全层，性能还跟得上吗？"这是企业最为常见的顾虑之一。

企业调用腾讯云AICC后，服务端无额外性能损耗，GPU-TEE加密带来的性能开销控制在5%以内。同时，AICC支持国内外多种芯片生态，兼容Hy3、DeepSeek、Kimi、GLM、Qwen等主流大模型，企业无需为适配安全方案更换现有技术栈。

当大模型从概念验证走向规模化落地，企业对算力的诉求早已不只是"跑得够快"。数据去了哪里、谁能看到中间过程、任务结束后是否还有残留——这些问题如果给不出可信答案，再强的模型也只能停在实验室阶段。依托腾讯云AICC，企业在安全和好用之间，不需要做取舍。

目前腾讯云AICC已在腾讯云HAI平台上线，企业可在平台内勾选"可信推理安全增强"开通使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iczOE5KEJun7mjB0TKvNPsygmn1V7icKbod3GttKQkr3oHGMicZeQxZvwVwDia6u9iaOmcyjXeV1ZHQJptVObu8IQibC7iavibGo6aN5nnsPJdjkiacY/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkden5qImICHSWibmMCI4FicszTR8S7nlM2YCmuB5GWQtBfqLicRmcu06jzFXmIOgiaeUQheLIDaw8vfpBdw/0?wx_fmt=png)

腾讯安全

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