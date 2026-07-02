---
title: 当“信任”成为AI漏洞：你的代码还安全吗？
url: https://mp.weixin.qq.com/s/Nc6eyiNSGo48A9T4uTDi9A
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:55:57.782307
---

# 当“信任”成为AI漏洞：你的代码还安全吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cGdNCBNfYO2mTwoI9ibdmRicAMlImEaTWTx4R3qPbx8YYkSoAfemwP4rjkdbq1MRVwBKvGibIXPPCyD1M2fWk38P3qEN6BpaGibcibOBYGDictbZo/0?wx_fmt=jpeg)

# 当“信任”成为AI漏洞：你的代码还安全吗？

小铭团队 - M
小铭团队 - M

观初科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/FRYKuBWVC12RPuIIejajDhNPViaJlBTRNBLIS2CnVGIAVmuVfz6ViaZFXTzDx0O0yBsZNMpia9oQmjEfDDEK7VeQQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cGdNCBNfYO3W3AAeXskXib8LaBxUwpfXYF9jAA4t4g3JbNlDBdkpOLQ0k0MFydAQzgkGwmDQT9zXHgia2vuLFoObZhaBiaHt0gPmvmZRyOujDM/640?wx_fmt=gif&from=appmsg)

**虚假漏洞报告大规模劫持AI编码代理**

“代理劫持”（Agentjacking）最新的例证展示了攻击者如何轻易利用AI代理无法区分内容与指令的缺陷。

近期，有研究人员提供了新的证据，表明AI编码代理已成为威胁行为者窃取凭证、操纵数据和破坏开发环境的一个切实可行的攻击面。研究展示了一种攻击方法：攻击者只需在公共漏洞追踪服务中植入一份虚假的错误报告，就能劫持AI编码代理，使其在开发者的机器上运行任意代码。在对这种“代理劫持”技术的受控测试中，Claude Code、Cursor和Codex等广泛使用的AI编码助手会检索被投毒的的错误数据，并在许多情况下，在开发者的机器上执行了攻击者控制的代码。

**01**

**利用虚假报告进行“代理劫持”**

在真实攻击场景中，其后果可能包括窃取云凭证、AWS密钥、GitHub令牌、SSH密钥以及CI/CD流水线机密。攻击者可能利用这些凭证访问私有源代码仓库、破坏云基础设施，或在整个组织范围内对软件依赖项进行投毒。

安全人员指出：已部署的AI代理现已成为系统的薄弱攻击入口，且现有技术栈对此类风险缺乏可见性。代理劫持攻击并非依赖高度复杂的漏洞利用手段，其核心仅在于一份伪造的错误报告。代理在读取该报告后予以采信，并利用开发者自身的访问权限执行了攻击者控制的代码。由于整个操作链中的每一步均在授权范围内完成，因此身份与访问管理、端点检测与响应及网络控制机制均未能触发任何告警。

**02**

**AI代理仍缺乏辨别力**

有安全公司在近期报告中指出，问题的根本症结在于AI编码代理缺乏对“读取内容”与“可执行指令”的有效区分能力。当模型上下文协议（MCP）连接器从外部源（如：文档、工单以及各类工具输出，而这些内容此前从未被视作攻击面）检索信息时，AI代理将所获内容一概视为输入数据，攻击者即可借机将恶意指令混入其中，攻击手法极具隐蔽性。

在今年的RSA 2026大会简报会上就有一位研究人员演示了攻击者如何向目标发送带有恶意指令的电子邮件，如果用户要求AI助手总结该消息，AI助手将盲目执行这些指令。建议组织禁用安装脚本，并要求代理在执行shell命令或安装从其读取的数据之前获得人工批准，代理以最小权限原则运行。从长远来看，组织需要实现实时监控代理意图与用户原始意图是否一致的能力，并在代理执行操作时捕捉任何偏差。“当攻击的本质是一个受信任的代理完全按照被投毒数据的指示行事时，唯一剩下的阻止点就在代理的运行时环境中。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGdNCBNfYO3yDlVa7zCV8uXPqMuC19IROXYEY6zkV4qhRwOQicmK0b6Y6l05b3g55iapIesibByKPbWZQyRYNVvfJA29RAw06ZGicBSiczxL6LDE/640?wx_fmt=png&from=appmsg)

**03**

**观初科技：AI解决方案**

观初科技，从信息安全合规咨询起步，历经十年发展，观初科技已从1.0时期的业务架构搭建，演进至2.0创新期的多项关键突破，如今正全面迈向3.0+AI智能时代。观初科技始终秉承“创造价值，不负初心”的使命，构建起覆盖“规划-建设-运营-优化”的全栈式服务体系。公司创新化布局AI领域，形成了六大核心业务能力：

**01**

**AI合规**

提供覆盖安全评估、数据治理与伦理审查的全栈式合规解决方案。紧密跟踪国家及行业监管动态，将法律合规要求转化为可落地的技术基线，协助企业在创新与风险控制间建立平衡，确保AI业务行稳致远。

**02**

**ASOC安全运营平台**

实现从“单点式检测”向持续化、体系化AI安全运营的跃迁。平台以“可扩展安全架构”为核心，整合资产感知、威胁研判与响应编排能力，帮助企业构建自适应、可生长的新一代安全运营体系，从容应对不断演进的AI攻击面。

**03**

**AI生态与基础设施**

覆盖MCP、Skills、插件及远程工具服务的深度安全审计，同时对支撑AI应用运行的底层基础设施进行全栈安全扫描。同步提供自研NEO-SCAN安全审计自测工具，助力企业在上线前自主完成生态组件及基础设施的安全验证。

**04**

**AI攻防验证**

依托RTaaS智能体红队审计服务，以真实攻击者视角，对AI应用进行动态对抗测试，系统性挖掘业务逻辑漏洞与模型安全风险。辅以自研大模型安全体检工具，从提示词注入、数据泄露、护栏有效性等多个维度，为模型安全提供量化评估报告。

**05**

**AI智能体定制开发**

提供从0到1的AI智能体全链路开发服务，涵盖大模型基础搭建、应用场景化开发、模型微调训练以及企业级知识库的梳理与构建。通过将行业KNOW-HOW与基础模型能力深度融合，打造贴合业务场景的专属智能体。

**06**

**AI资产治理**

推出自研NEO-BOM资产扫描工具（支持风险量化评分），通过主动探测与被动解析相结合的方式，为企业建立完整、准确、实时更新的AI资产台账。对模型、数据集、API及依赖组件进行全生命周期管理，让AI资产全景可视、风险可管。

**更多AI相关咨询，****联系我们：**

**sales@insightsec.cn**

部分文章来源：Dark Reading

本文选材/撰写/翻译/校对/排版：小铭团队M

![](https://mmbiz.qpic.cn/mmbiz_gif/cGdNCBNfYO2gouicQxsyMQicVAQMpiahAz0am2CILCPf64pI0l5o3ia3TQgAOswyrbPAZKX8WymrN9l48niacp2HXH2ibKgapHQv6WHjNMdGBk5zE/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FRYKuBWVC11Ncn5nvkrpJHqHq4yYzJL8yR2jtMBGREicZexKchD45OobIBaqgDBz40AYqYFADeKaicDgiag1be1IQ/0?wx_fmt=png)

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