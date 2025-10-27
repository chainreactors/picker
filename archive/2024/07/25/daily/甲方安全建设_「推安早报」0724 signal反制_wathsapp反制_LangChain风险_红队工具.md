---
title: 「推安早报」0724 signal反制/wathsapp反制/LangChain风险/红队工具
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487679&idx=1&sn=7e802630f8041f90bdddc6a282aa66f7&chksm=fb35b977cc423061f6ec07db383c786e980f87caf7e62537e1aee8b2e2a922bf7deb95fe9c36&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-25
fetch_date: 2025-10-06T17:45:53.652586
---

# 「推安早报」0724 signal反制/wathsapp反制/LangChain风险/红队工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46Y82W05NaSKtPqZAIYtvicolsbBc9s2j9kB23fAwd8QgB6WWCnprkptw/0?wx_fmt=jpeg)

# 「推安早报」0724 signal反制/wathsapp反制/LangChain风险/红队工具

bggsec

甲方安全建设

# 2024-07-24 「红蓝热点」每天快人一步

> 1. 推送`「新、热、赞」`，帮部分人`阅读提效`
> 2. 学有`精读浅读深读`，艺有`会熟精绝化`，觉知此事`重躬行`。推送只在`浅读预览`
> 3. 机读为主，人工辅助，每日数万网站，10w推特速读
> 4. 推送可能`大众或小众`，不代表本人偏好或认可
> 5. 因渲染和外链原因，公众号`甲方安全建设`发送`日报`或日期,如`20240724`获取`图文评论版pdf`

### 目录

> 0x01 【2024-0723】通过中间人网络过滤攻击有效阻止EDR遥测
> 0x02 【2024-0723】EDR遥测数据拦截器
> 0x03 【2024-0723】WebRTC安全漏洞研究：远程代码执行风险
> 0x04 【2024-0724】LangChain开源生成式AI框架中的漏洞
> 0x05 【2024-0724】高级SQL注入技术
> 0x06 【2024-0724】macOS Sequoia 15 Beta 4 SDK更新与SwiftUI改进
> 0x07 【2024-0724】攻击活动目录：从0到0.9
> 0x08 【2024-0724】FlowAnalyzer：OAuth 2.0和OpenID Connect流分析工具
> 0x09 【2024-0724】SCCMHunter：简化SCCM资产识别与攻击的工具
> 0x0a 【2024-0724】PumpBin：植入生成平台
> 0x0b 【2024-0724】WhatsApp漏洞：Android恶意软件伪装成PDF文件

### 0x01 通过中间人网络过滤攻击有效阻止EDR遥测

> 网页主要介绍了如何通过实施人在中间（PitM）攻击和过滤电子防御响应（EDR）遥测数据包来有效地阻止EDR遥测到达云服务器，从而隐藏安全操作中心（SOC）团队的警报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46SHwH3AfS7axUCHJKA0mABSC06tW5ENfzGK3wOhbBlAed0rRk3gAj1Q/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46iauiaGpkRPB2bRmjxPvNhtcahD87Y2nicyL3ibEfXvoPhloLZ1RaOrWwyg/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46Y6FY6x4RqeIKyzPDT0M5kgv28g5icb5aeVXzmJUC3jnInr4gibrTYRWg/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* 「编者注」:致盲edr的一个操作，日志链路阻断, 实战里有很多类似的举一反三.
* 绕过EDR控制台的有趣方法

### 关键信息点

* ARP欺骗是实施PitM攻击的有效方法，可以用来拦截和过滤EDR遥测数据包。
* 传统的`iptables`规则，基于IP地址或子网来阻断流量，对于大量的EDR通信服务器地址来说是不够高效的。
* 利用TLS握手中的SNI可以更精确地识别EDR遥测流量，并通过更新`iptables`规则来有效地阻断这些流量。
* `edr_blocker.py`工具提供了一个更高效的解决方案，能够解析TLS握手中的SNI并动态更新`iptables`规则。

🏷️: EDR, 中间人攻击, ARP中毒, iptables, TLS

### 0x02 EDR遥测数据拦截器

> EDR Telemetry Blocker 是一个通过进行人在中间（Person-in-the-Middle）攻击并使用 iptables 进行网络过滤来阻止终端防御（EDR）遥测的工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip460gMvvW0vfrjMFBniakJzk7Zfx2kumO6Tr7o2IJcV1NT3N62dp6aqoTg/640?from=appmsg)

### 热评

* 通过PitM网络过滤阻止EDR遥测
* EDR Blocker：利用 ARP 欺骗执行中间人攻击的工具

### 关键信息点

* EDR Telemetry Blocker 工具通过中间人攻击和 iptables 过滤来阻断 EDR 遥测数据。
* 该工具可以在监控模式下仅检测和日志记录被阻断的 IP 地址，而不会添加 iptables 规则。
* 工具的使用需要指定网络接口、被阻止服务器名称列表文件、目标 IP 地址或范围以及网关 IP 地址。
* 工具支持详细输出，便于用户了解工具的运行情况。

🏷️: EDR, iptables, 网络安全, 中间人攻击

### 0x03 WebRTC安全漏洞研究：远程代码执行风险

> 本文介绍了如何通过研究和利用 WebRTC 和 Signal-iOS 的漏洞来实现远程代码执行（RCE）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46kFv2Qsk3tacXrOXkjd8FZMQeMFicNQJuw63soh07lM0siaJeFzkgfVpA/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46XhTK7LowQPDQK5dX6O5Lrf3CtnuPCoYcBvicgCgicZj6OkwyN1AQS48Q/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* WebRTC 中的 RCE 漏洞：第一部分
* Signal 的 WebRTC 通话库漏洞研究：深入研究

### 关键信息点

* WebRTC 是一个复杂的实时通信工具库，它处理音视频通话，是一个值得研究的目标，因为它涉及解析序列化数据和维护状态协议，这些都是复杂的任务。
* Signal-iOS 的复杂性和 iOS 的特性使得对这些应用程序的安全研究变得具有挑战性。
* 通过注入合成的漏洞和使用 Frida 等工具，研究人员可以更深入地了解 Signal 和 WebRTC 的内部工作机制，以及如何在 iOS 上进行漏洞利用。
* 构建一个 ARM64 ROP 链是实现远程代码执行的关键步骤，它需要精心设计，包括条件循环和堆栈偏移技术。

🏷️: WebRTC, Signal, iOS, 网络安全, 远程代码执行

### 0x04 LangChain开源生成式AI框架中的漏洞

> Palo Alto Networks 的研究人员发现了 LangChain 中两个重要的安全漏洞，分别是服务器端请求伪造（SSRF）和提示注入漏洞，已经得到了修补。这些漏洞可能允许攻击者执行任意代码和访问敏感数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46jicXZsW5ibTu21ibibvu2oByFicVcGRWeeEa8J8a3HceqZz7I3tV0eDxibqQ/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46AaH283LmXTGb17d0XdHPuUI9Ziblxj1ILeWFibqbDiauoWQWawvfYVibtw/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46pyfOGKzzDV2Fm6jyen4bM2TfWzo5VzXPG7tpknKFD0CY4KOo68t5CQ/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* 开源 AI 工具 LangChain 曝出漏洞，CVE-2023-46229 和 CVE-2023-44467 影响 LLM 构建

### 关键信息点

* LangChain 的生成式人工智能框架在开发者中非常流行，但其安全漏洞可能导致敏感数据泄露和任意代码执行。
* 研究人员强调了在使用大型语言模型时，对用户输入进行严格验证和清理的重要性，以防止恶意的提示注入攻击。
* 尽管 LangChain Experimental 提供了强大的功能，但开发者在使用该库时必须谨慎，并采取适当的措施来减少被植入恶意代码的风险。
* Palo Alto Networks 提供了一系列产品和服务来保护其客户免受这些漏洞的攻击，包括但不限于下一代防火墙、Cortex XDR 和 Prisma Cloud。

🏷️: LangChain, AI, 漏洞, Palo Alto Networks

### 0x05 高级SQL注入技术

> 这篇网页内容主要介绍了一系列高级的 SQL 注入技术，包括错误注入、联合查询、盲注入、二次注入以及如何绕过 WAF 和自动化工具的使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46m4aTlp6OOFCu1SReBjnib6G7KUicYBBJKBExfqvGmt2A5hGEJPTbhia2g/640?from=appmsg)

### 热评

* 「编者注」:sqli的一些基础知识
* 开源高级 SQL 注入技巧仓库

### 关键信息点

* 合法和授权的测试：网页强调高级 SQL 注入技术应该仅在合法和授权的测试环境中使用。
* 高级注入技术的多样性：文章展示了多种高级注入技术，包括错误注入、联合查询注入、盲注入和二次注入等。
* 自动化和定制化工具的重要性：提到了自动化工具如 SQLMap 和自定义 Python 脚本的使用，以及如何编写定制的篡改脚本来绕过 WAF。
* 数据库特定的攻击方法：文章指出了不同 DBMS（如 MySQL、PostgreSQL、MSSQL、Oracle 和 SQLite）的特定攻击方法和错误生成技术。

🏷️: SQL注入, 网络安全, 技术

### 0x06 macOS Sequoia 15 Beta 4 SDK更新与SwiftUI改进

> macOS Sequoia 15 Beta 4 发布说明详细介绍了 Sequoia 15 Beta 4 版本的 macOS SDK 更新，包括 SwiftUI 的新特性、bug 修复以及开发者需要注意的行为变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip466aaTb55ObfhsezqqMVtMicOfmdqxfTic8IsQWFYMrIlPVZjIh4BX72Dg/640?from=appmsg)

### 热评

* 「编者注」:18不想了，先等一波iOS 17的巨魔🤣
* iOS 18/macOS 15 Beta 4 出现 iBoot 未加密漏洞

### 关键信息点

* SwiftUI 的进一步增强：Sequoia 15 Beta 4 版本继续增强 SwiftUI，提供了更多的 UI 组件和功能，以及更好的开发者体验。
* 兼容性和行为一致性的重视：苹果公司对于新旧版本之间的兼容性和行为一致性表现出了高度重视，通过详细的发布说明帮助开发者平滑过渡。
* 性能优化和 Bug 修复：Sequoia 15 Beta 4 关注了应用程序的性能优化和 Bug 修复，以提升用户体验和开发者的开发效率。
* 开发者需要关注的变化：开发者需要注意新版本中的行为变化，如默认尺寸、导航行为和视图生命周期等，以确保应用程序的正确运行和用户体验。

🏷️: macOS, SwiftUI, 软件开发, SDK更新, 操作系统

### 0x07 攻击活动目录：从0到0.9

> 网页主要介绍了如何攻击Active Directory环境，包括了对Active Directory的基本概念、结构、用户管理、组管理、计算机管理、服务管理以及数据库的详细信息，并且提供了一系列的攻击技术和方法，如密码 hash的提取、Kerberos票证的利用、信任关系的滥用、域控制器的嗅探等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46Z7v4eROoz8riaTo4XdnZtVE4whaB9mAKM8T0q9D9rwMhubjQg0Pichwg/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46Tibu2mOaPR22SlIcymTldSkTM9gQsUdkQP2fkfjsVMx0L4IMjb62cwA/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46TsI9fxSFKvbPeMS59GjibxUUXqGe1mYWCZsgibTVPDHUGaE1T0X5toVA/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* 「编者注」:历史老文，今天有人讨论，扫盲101类
* 免费学习 Active Directory 攻击技巧

### 关键信息点

* Active Directory是企业网络安全的核心，其设计和配置对网络安全至关重要。
* 攻击者可以通过了解Active Directory的结构和组件来识别关键目标，如域控制器、高权限用户和敏感组。
* 密码哈希和Kerberos票证是攻击者获取对域内资源的未授权访问的关键资产。
* 信任关系和服务 principal name（SPN）可能成为攻击者横向移动和提升权限的途径。

🏷️: 活动目录, 攻击, 渗透测试

### 0x08 FlowAnalyzer：OAuth 2.0和OpenID Connect流分析工具

> FlowAnalyzer 是一个帮助理解和测试 OAuth 2.0 授权流程及 OpenID Connect（OIDC）的工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46456CfibZZ1dxgiczFiatGM6lWxFSzC2aulKA9KRMP0KUT6WYEMc7gYvCA/640?from=appmsg)

### 热评

* OAuth 2.0 流程分析工具 FlowAnalyzer

### 关键信息点

* FlowAnalyzer 是一个专门为了帮助理解和测试 OAuth 2.0 授权流程和 OpenID Connect（OIDC）而设计的工具。
* 工具提供了执行授权流程的笔记本和详细的流程说明，以及如何设置证书认证的指南。
* 强调代码仅供测试使用，不应在生产环境中部署。
* 建议使用 Microsoft 身份验证平台的认证库或 JWT.io 上的库来处理生产环境中的认证和授权。

🏷️: OAuth, OpenID Connect, 安全测试, 工具

### 0x09 SCCMHunter：简化SCCM资产识别与攻击的工具

> SCCMHunter是一个针对微软系统管理中心配置管理器（SCCM）的后期渗透工具，旨在简化识别、描述和攻击AD域中的SCCM相关资产。

### 热评

* 「编者注」:bh us 马上要讲这个，SpecterOps发布

### 关键信息点

* SCCMHunter是一个专门针对SCCM的后期渗透工具，它能够帮助渗透测试人员在Active Directory域中更有效地识别和攻击SCCM相关的资产。
* 开发者建议使用Python虚拟环境来安装SCCMHunter，以避免潜在的依赖冲突。
* 工具的开发和测试在实验室环境中进行，实际使用效果可能因环境而异，开发者鼓励用户在遇到问题时寻求帮助。
* SCCMHunter的开发受到了社区多位研究者的研究成果和实践经验的影响，这些研究者在SCCM的安全研究领域做出了显著贡献。

🏷️: SCCM, 网络安全, 攻击工具, Active Directory, 实验室环境

### 0x0a PumpBin：植入生成平台

> PumpBin 是一个用于生成植入物（Implant）的平台，支持本地和远程插件类型，并采用 Extism 插件系统提供强大的扩展性，每个生成的植入物都具有唯一的随机加密密钥和随机化数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46rKoVh5fDG0lWROxGIbvockRoXuueyw1msqMlAvbblVCs2avq0NzIyw/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46NnUYtqPiboSFypUN8NYoLicia52X6FAF9icQ1GIfsRbZWiaQKMwObIOPSag/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* PumpBin：一款植入程序生成平台
* Rust 编写的植入物生成平台：支持 Extism 插件系统

### 关键信息点

* PumpBin 旨在简化和标准化最终植入物的生成过程，提高网络安全研究人员和攻击人员的工作效率。
* 通过使用 PumpBin，网络安全团队可以更灵活地生成定制的植入物，而无需频繁的直接沟通。
* Pu...