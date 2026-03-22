---
title: 1.2亿美元，机器身份管理厂商Oasis获B轮融资
url: https://mp.weixin.qq.com/s/5WoQpw3lpzwn7IJNeuizdA
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:16:52.265176
---

# 1.2亿美元，机器身份管理厂商Oasis获B轮融资

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ccVb6wGibibCHGg8xe6kcg8aTvc2JA5OIyDlCYtvphGOBIcicXUk6EOC8qyicEYjiaGbNniaDmQ8txDZEdjiaib86vdia6S0knpSichfTKocC8gJBibLng/0?wx_fmt=jpeg)

# 1.2亿美元，机器身份管理厂商Oasis获B轮融资

原创

孙志敏
孙志敏

AI与安全

![]()

在小说阅读器中沉浸阅读

2026 年 3 月，专注于非人类身份（‎Non-Human Identities,NHI，也可称为机器身份）安全管理的初创公司 Oasis Security 宣布完成 1.2 亿美元 B 轮融资，本轮由 Craft Ventures 与红杉资本（Sequoia Capital）联合领投。至此，Oasis 累计融资总额已超过 1.6 亿美元。这是非人类身份安全赛道迄今为止金额最大的单轮融资，标志着该赛道正从小众安全方向迅速走向主流企业级市场。

1

为什么"机器身份"成了安全新战场？

身份和资产管理一直是安全管理的基础要求。人类身份通过统一身份认证系统，技术上基本已经解决，但机器身份是个越来越大的麻烦。研究表明，企业环境中 NHI 的数量通常是人类身份的 10 至 45 倍，但针对 NHI 的治理成熟度不足人类身份管理的十分之一。比如，连接数据库需要用户名密码，这个用户名密码丢了，就意味着身份被盗用了。

NHI 涵盖所有非人类主体所使用的数字身份，包括：

* 服务账号 / 服务主体 （Service Account / Service Principal）
* 工作负载身份（Workload Identity）
* OAuth 授权应用
* （第三方集成）AI 智能体
* （Agentic Identity）API 密钥 / RPA 机器人凭据

这些身份无处不在：CI/CD 流水线调用 GitHub 的 Token、数据平台访问 Snowflake 的服务账号、Salesforce 对接 ERP 的 OAuth 连接……每一个都是潜在的攻击入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCGicPfPXdIKQYleGdka4ALLUeYybzAHR0wNeOkll0hRFzibEjAicmBoJq4tMMUcvt650lsw47UZFFjqdjv2iavxoicddAlboSlqOBbc/640?wx_fmt=png&from=appmsg)

2

Oasis的方案

NHI 与人类身份最大的区别在于：没有 HR 系统锚点，没有管理者，权限因"省事"而被放大，凭据因"怕出故障"而永不轮换。

Oasis 身份管理平台**Oasis NHI Security Cloud 的核心要解决两件事：① 每个 NHI 都有明确的问责链（所有者 + 上报路径）；② 每次认证决策都基于证据（用量和依赖关系），而非猜测。 这些的基础首先是建立信任链，然后是生命周期管理。Oasis机器身份的技术信任链如下：**

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCFnVfRgZrRDoBSgdwx8Gyr7Pvicqf9wr3bXtuSRJmvomgNuk9I9Ghps0OJnz11yRtwlK16jBf5pqAZlpsmBTQoOuYLgheZu4mjA/640?wx_fmt=png&from=appmsg)

3

生命周期管理：六阶段端到端闭环

大多数企业运行的是"意外生命周期"：创建 → 遗忘 → 被入侵。Oasis 将其替换为有意识的生命周期六个阶段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCGPCibnmVSQUJK1DA1YZPkcTicyLjk0fM7E8BKQHNTRCicwIPBn1zicLiaeyI6mYnssck8HsBfic8cvaSia8RysibEOlvGB0CVjDMlEj80/640?wx_fmt=png&from=appmsg)

各阶段的核心机制说明：

① **供给（Provisioning）**：通过 IaC 或标准化 API 创建 NHI，强制绑定命名规范、标签与所有者，从源头落实最小权限原则。

② **所有权（Attribution）**：结合云、SaaS 与日志数据识别身份归属，利用规则与 ML 推荐 Owner，持续消除“无主身份”。

③ **密钥管理（Vaulting）**：统一接入 KMS/Secrets 平台集中存储与调用凭证，避免硬编码与明文暴露，实现安全托管。

④ **姿态评估（Posture）**：持续扫描权限与配置，识别过权、长期未使用等风险，并提供修复建议与优先级排序。

⑤ **退役（Decommission）**：对不再使用的 NHI 执行禁用、撤权与删除，确保身份全生命周期可审计、无残留风险。

⑥ **安全轮换（Rotation）**：对密钥与凭证进行周期性或事件驱动轮换，支持分级策略与审计追踪，降低长期泄露风险。

**持续监控（Monitoring）**：通过行为基线与异常检测持续监控 NHI 活动，及时发现凭证滥用与账户接管风险，并自动响应。

4

最新战略重心：Agentic Access Management

这是 Oasis 在 AI Agent 普及背景下的差异化定位，是业界首个专为AI代理构建的身份解决方案，也是获得融资的关键产品。

传统 IAM 无法应对 AI Agent 时代的挑战：Agent 由任何人在任何地方创建，缺乏一致的治理机制，也没有大规模管控工具。Oasis的治理引擎AAM是专门为AI代理设计的意图感知、策略驱动的访问管理方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCH7kKBSBdt4Sp4ib98fZa4KVcna8I247l4d9T1lWChPNydHPKjQuLtS4Z4FiceaEibyQa46dNibDxiaOZiayX9c3acibnULiazia16hD3Vg/640?wx_fmt=png&from=appmsg)

Oasis AAM 的核心特点可归纳为三个层面：

意图感知：不再依赖静态的角色或权限列表，而是深入理解 AI 代理每一次行动的真实意图（如“读取Q3活动线索”而非“访问CRM”），使访问控制与任务目标精准对齐。

最小权限 + 即时生效：为每个代理按需授予恰好够用的访问权限，且仅在任务执行期间有效。任务完成后权限自动撤销，消除长期存在的“特权闲置”风险。

AI-SPM（AI安全态势管理）：持续检查 AI 代理的配置、权限分配及风险态势，帮助企业发现并修复不当授权、过度权限等隐患，确保代理行为始终处于可观测、可治理的状态。

这三者共同构成了从“意图理解”到“权限执行”再到“持续监控”的闭环，让企业在启用 AI 代理时，既能保障业务敏捷性，又能将安全与合规风险控制在可预期的范围内。

5

小结

很多的安全手段在防攻击，但身份管理才是更致命的问题：对人，各种钓鱼攻击，以及各种凭据的窃取，无意丢失，都是身份管理的问题，很多案例来自于此。在做云安全的过程中，我也曾被其严重困扰。

Oasis的方案是一个重要的方向，尤其是AI时代，我们确实需要一套身份管理的机制和系统。同时，身份管理也需要借助AI的能力。

![](https://mmbiz.qpic.cn/mmbiz_gif/NB91guJr0w3nSyvUF9MgTABODeoVticjUljjdKUictmqNBvykumXicg13ic8CwNJJbA0sjhaB1vet4oCLQ0QTWz28w/640?from=appmsg)

关注我，始终为您提供最有价值的前沿信息和分析判断。

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCER0EHOuGPhhVGxic9ryGDF6ib71t3NkonW8MngdCmXcRAQicferhrMvlKuTMickmXysrxyvFVASTf0xoIPAbpBo0At5O35lKhFJs8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

AI与安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

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