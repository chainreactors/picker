---
title: 从《人工智能安全治理框架3.0》看 AgentGuard：智能体安全如何实践
url: https://mp.weixin.qq.com/s/Up22GZNnMWhDg79k_uRDyA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:00:49.169527
---

# 从《人工智能安全治理框架3.0》看 AgentGuard：智能体安全如何实践

# 从《人工智能安全治理框架3.0》看 AgentGuard：智能体安全如何实践

原创

复旦白泽战队
复旦白泽战队

复旦白泽战队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrp6qh3m1PvLlia1sWKYvNjCV4tvmefpVlVHJgHUYT2TvobicJ3ozEv5qXSicAOL1L7yKrUAphv9WQ6S2XNerBVdfyONMj4pIycaMg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrr2HMEZjnwcdL1Ueeg4P4HgNM9NGXicR96A6Uibib2eB5eARSqKxKfhX5f3MkNdaI3qPibBqf9v3zJ5sVLRzicj9b79VrwZBb1xBlwM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrqXuib5KfCHUW5ibT5fJNV5VluTpbBwq7zNibH2ibvichooibPo8kcjnRNmFwemk6nFJ6icTUgwUkNdo60wGlXoEqX4ibCMe1WjvPF8IDM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrohENib0aDkiaXfQRibnWOcyGbibJE2MEtKYh6HMvBgY2C0WHvRBIg8dC1CRVF44ORmk7sZ4u3q6KXFx5tlZ65xW5PPFOqiazVqVwPE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrovdEia6Tc9VMKwgAZKY3t4RpAdn82vMA2HRUglOxetdl0xC1tibZojXoPQicYH8wibUrjiaU6XcRghPvpqJdOb3xT8qnmRJvqklIz0/640?wx_fmt=png&from=appmsg)

2026 年 9 月 14 日，在 2026 年国家网络安全宣传周开幕式上，全国网络安全标准化技术委员会发布**《人工智能安全治理框架3.0》**（以下简称《框架3.0》）。

新版本延续“风险分类、技术应对、综合治理”的核心逻辑，并结合人工智能技术和应用的新变化，对风险分类和应对措施进行了更新。值得关注的是，在此前框架已有讨论的基础上，《框架3.0》进一步**将智能体风险单独展开**，并在附件中给出专门的“智能体风险管理框架”，从风险识别到防范措施形成了较为完整的治理思路。

对照《框架3.0》，我们尝试对防护实践进行梳理。本文以《框架3.0》中提出的七类智能体防范措施为主线，结合AgentGuard已有的技术能力，探讨这些安全要求如何落实到实际系统中。

1

智能体安全风险解读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrrVO90kibC8NRGm3bkCfXTNOXEYuxAVVwUZdP2wgK9tdibAGQ7Sg0nKQd58X1AnKewp0UjsicO4Ya94NHwQkvJMmz6QpcC9911nCc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrricC8JXk1xguSF3SPdCMmOiaR5Cjt4ywicp4Wt6Mzk6oSKicU4VKicGVeRmm4OiaMiacaqcJU3NJK2CBt5QLaULeDqtpC0gjcHtDeDXc/640?wx_fmt=png&from=appmsg)

《框架3.0》对智能体风险的讨论已经不局限于提示注入或有害输出，而是覆盖**设计研发、安装部署、指令输入、推理规划、调用执行、记忆存储、结果输出和停用下线**等完整生命周期。

其中既包括权限滥用、目标劫持、工具投毒、记忆污染等已经受到广泛关注的问题，也纳入了行为逃逸、异常自主行为等随着 Agent 能力增强而逐渐出现的新风险。相比单纯关注模型“说了什么”，这里讨论的安全对象已经扩展到了 Agent “能够做什么”以及“实际做了什么”。

针对这些风险，《框架3.0》进一步提出七类防范措施：**风险预防前置、身份与权限管理、加强人工审批、供应链与工具管理、运行时动态管理、持续监测与审计、停用安全管理。** 这七类措施从上线前的风险评估和安全测试开始，覆盖身份授权、工具接入、运行时控制和人工接管，并一直延伸到日志审计和最终下线，构成了一套面向智能体全生命周期的安全控制思路。

|  |  |
| --- | --- |
| **防范措施** | **核心内容** |
| 01 风险预防前置 | 开展风险识别与分级，上线前进行安全测试和评估，制定相应安全控制策略 |
| 02 身份与权限管理 | 建立智能体身份标识，遵循最小必要原则授权，加强凭证和访问权限管理 |
| 03 加强人工审批 | 在关键决策和高风险操作前设置二次确认或人工审批，保留必要的人工控制 |
| 04 供应链与工具管理 | 对工具、插件和技能进行安全验证，管理版本、配置以及实际执行行为 |
| 05 运行时动态管理 | 在任务规划、工具调用和结果输出等环节设置检测与拦截，及时处置异常行为 |
| 06 持续监测与审计 | 对智能体运行过程开展全链路监测和日志审计，并持续进行安全测试与验证 |
| 07 停用安全管理 | 在智能体停用后终止相关服务、撤销授权，并妥善处置数据、凭证和运行环境 |

2

面向智能体生命周期的防范实践

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBroC4cUUzxJ1srkDezlDQcScFk1X4CNLd5s8tK20Mmib5zFB5RdIo7wyDZH6SaiaPoQeTju9Xic3jgwp2Xg7XGbyTLzNHNjb7BKBMM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrpnEKrnAfr9fWhaK9Db07v9B5wddPYMgegnYdunE9JPecwADE65OhFzLibKyKZ7z0QsZEElg7Axk6vxxH19P6icqbT1r2I5Mlm2w/640?wx_fmt=png&from=appmsg)

**01 风险预防前置：在 Agent 上线之前发现问题**

**《框架3.0》要求**：在智能体投入使用前开展风险评估，明确风险等级和安全控制策略，并“**对智能体及选用的大模型进行安全测试和评估**”，将安全验证前置到部署阶段。

**AgentGuard实践**：AgentGuard 提供覆盖**模型、知识库、MCP、Skill、智能体** 五类对象的安全评测能力，支持批量测试并输出量化结果和逐用例证据，持续验证系统能力边界和防护效果。

**02 身份与权限管理：让 Agent 在授权范围内行动**

**《框架3.0》要求**：为智能体配备唯一身份标识，并按照最小必要原则进行授权，对访问凭证的授权范围、有效期和使用过程进行管理，避免身份冒用和权限滥用。

**AgentGuard实践**：AgentGuard 将 **Agent 身份与访问权限绑定**，可针对不同 Agent 分别配置允许访问的模型、工具和外部资源，并对实际调用进行权限校验。

**03 加强人工审批：高风险操作执行前再确认**

**《框架3.0》要求**：在关键决策节点设置强制人工审批，对删除文件、发送数据、修改系统配置等重要操作进行二次确认或人工审批，并完整记录审批过程。

****AgentGuard实践**：**AgentGuard 内置**高危操作识别与审批机制**，覆盖破坏性命令、提权与远程执行、数据外发等风险类型。命中策略后，可根据风险等级执行记录、支持二次确认、人工审批或直接阻断等多类安全措施。

**04 供应链与工具管理：管住 Agent 接入的外部能力**

**《框架3.0》要求**：将工具、插件和技能纳入智能体供应链管理，要求在接入和调用过程中验证其安全性与完整性，并检查版本、描述、参数、元数据以及实际执行行为。

**AgentGuard实践**：AgentGuard 面向 **MCP、Skill 和 知识库等插件** 提供安全检测能力，通过源码与配置扫描识别危险 API、系统命令、敏感资源访问等异常行为，确保供应链安全。

**05 运行时动态管理：在执行链路中持续判断风险**

**《框架3.0》要求**：在智能体运行过程中设置多层检测与拦截点，对任务规划、工具调用和输出结果进行动态安全检查，并针对高风险或异常行为采取告警、限制、拦截或终止等措施。

**AgentGuard实践**：AgentGuard 在**模型调用前后和工具执行前后**设置运行时安全检查点，覆盖 Prompt Injection、敏感信息泄露以及高风险工具调用等安全风险。同时结合任务上下文分析跨步骤行为链，有效识别危险执行链路。

**06 持续监测与审计：让 Agent 的执行过程可追溯**

**《框架3.0》要求：**开展智能体全链路安全监测，对文件操作、指令执行、网络连接和技能调用等行为进行记录，并通过日志审计、红队测试和安全回归持续发现风险。

****AgentGuard实践**：**AgentGuard 对**模型调用、工具调用、策略判断、人工审批和执行结果**进行全链路记录。运行过程中发现的新风险可以进一步沉淀为评测用例，形成从运行监测到安全评测和回归验证的闭环。

**07 停用安全管理：安全边界延伸到 Agent 下线**

**《框架3.0》要求**：将安全管理延伸到智能体停用阶段，要求终止相关服务、撤销第三方授权，并对工作文件、知识库、插件配置、账号凭证等数据和资源进行妥善处置。

**AgentGuard实践**：AgentGuard 提供**安全策略管理、访问权限控制和审计记录留****存**等能力，可配合 Agent 平台、身份系统及基础设施，在智能体停用后完成权限与凭证撤销、相关服务关停、数据清理和运行环境回收，保障 Agent 安全退出业务系统。

3

结语

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrqkv9vziayHYjZVaw3UoP6pbRVvOAJ5QkCayNFLmwE9W2FzcbhupMZauDSDE4cRvcNpX6CiaWEdTFswibzgIKbPmyibQSPgdgwbVFo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBroiaHe95sL6OIibnRfWCTOyfemJfRWYyW6bibWKibMribibQzRreZ9Zhtniaibwm7axAEV6oykDqGH3c0OK8iaPCR2ZwZSrO8iajmbYycXicQ/640?wx_fmt=png&from=appmsg)

面向《框架3.0》，AgentGuard 希望通过上线前评测、身份与权限管理、工具供应链检测、运行时防护、人工审批和持续审计，让 Agent 的每一次关键操作有边界、可控制、可追溯。随着智能体能力不断扩展，我们也将持续完善 AgentGuard，希望让更强的自主执行能力能够建立在更可靠的安全基础之上。

AgentGuard 持续更新中，欢迎试用与反馈，也欢迎提交代码，与我们一同构建更安全的 AI Agent 生态。

AgentGuard项目地址：https://github.com/WhitzardAgent/AgentGuard

参考：《人工智能安全治理框架》1.0（2024）、2.0（2025）、3.0（2026），全国网络安全标准化技术委员会

供稿：陈沛、罗嘉骐

排版：陈家桂

责编：董佳仪

审核：洪赓

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、小红书搜索：复旦白泽战队也能找到我们哦～

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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