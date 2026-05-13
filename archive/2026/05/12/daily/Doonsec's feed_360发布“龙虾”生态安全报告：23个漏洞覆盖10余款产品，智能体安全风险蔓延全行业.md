---
title: 360发布“龙虾”生态安全报告：23个漏洞覆盖10余款产品，智能体安全风险蔓延全行业
url: https://mp.weixin.qq.com/s/AKyjmlv4vfperRsGS8njsQ
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:43:18.833830
---

# 360发布“龙虾”生态安全报告：23个漏洞覆盖10余款产品，智能体安全风险蔓延全行业

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzziczmozuOQQBda8OIq7ibicTRftyE0hfPLKsH7T5Exf0SZ2JFj3cM8ibWib7Mg1afjRUrTbJegYB1BBRzdTpylYxvyiabRs4EDAMEsnk/0?wx_fmt=jpeg)

# 360发布“龙虾”生态安全报告：23个漏洞覆盖10余款产品，智能体安全风险蔓延全行业

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgbJxnOxcKdRicA5Vlgv8VdjNEa8tGFyzVgC6Q6dlYR7JSnqNf6hodTZqXAibl0ZqFHlNgZKH8hT2jQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxMNcESnNywDGrJsq2F56KIFm24IU0uFkbLfYtia0VZiaapeGsSURP1WYV9nYBoagWxUkccsPhKquFQPDYZp8SGff3ibEUQ5Gm3Gao/640?wx_fmt=png&from=appmsg#imgIndex=1)

近日，**360数字安全集团发布《OpenClaw生态安全风险分析》报告**，首次系统性地对AI智能体生态安全问题进行“家底盘点”。

通过自研漏洞挖掘智能体对OpenClaw核心及10款主流衍生产品展开深度安全审计，从原生架构特征与防护失效、供应链安全债传递、开源自研安全挑战三大维度，完成对龙虾生态核心安全风险的系统剖析，**累计发现23个独立安全漏洞，涵盖远程代码执行、认证绕过、权限提升、信息泄露等多种高危类型。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxObeCXEHib8xLGU2aAdSCthKbLCloR95icebfUE2Wo4kqY4iaP7skj8utTgibgR0KxDBrEExLKC4QZ19BDRo9C9Xzl9rg0ArPGKK84/640?wx_fmt=png&from=appmsg#imgIndex=2)

目前，所有漏洞均已反馈至相关厂商与开发者跟进修复，并上报国家信息安全漏洞库（CNNVD）、国家信息安全漏洞共享平台（CNVD）等权威机构。

报告指出，以OpenClaw为代表的“龙虾类”智能体产品，正在快速渗透至代码开发、数据处理、终端运维等高价值场景。这类产品的核心特点是“替用户干活”，它需要获取文件读写、网络服务调用、系统命令执行等高权限，才能真正完成复杂任务。

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxMKo7icUdFXibadicxAb9l0PYfooNaVUOmIXymSdlNYokrvjND1DlExJ5fI50kdDicfCNWhAJP27Jy3Ko8p7tEopwJ16hoD2zdP6MM/640?wx_fmt=png&from=appmsg#imgIndex=3)

OpenClaw生态图概览

问题在于，当这些具备高权限能力的智能体运行在不可信网络环境中，失控的风险将被急剧放大。报告显示，OpenClaw GitHub已累计披露超过535个安全公告，仅2026年第一季度后，相关安全通告新增数量已达到日均4条以上。更值得警惕的是，这些漏洞并非孤立的代码错误，而是呈现出典型的“多米诺效应”——认证边界、网络边界、执行边界、控制边界四层防线高度耦合，任何单一维度的突破都可能引发连锁崩塌。

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxNfWJ6WsWPx96WthZRMAZZHIJ3o3MzwJEcCDISpT8e5ttHnsm5LfLbZCaAJaWXC576AVzE1HO8IUK5bYicxNibfUql7gXmicpyWKQ/640?wx_fmt=png&from=appmsg#imgIndex=4)

OpenClaw生态安全报告增长曲线图

随着OpenClaw作为核心技术基座被广泛落地，智能体生态的安全风险正在通过代码继承和功能叠加向全行业扩散。一方面，部分衍生产品直接打包OpenClaw核心组件，当上游出现安全修复时，下游往往缺乏快速响应的渠道，形成“补丁时间差”；另一方面，为追求差异化竞争而引入的新功能模块，往往缺乏充分的安全审计，反而带来了新的攻击敞口。

报告同时借助360漏洞挖掘智能体在语义级代码理解、跨文件数据流追踪与逻辑推理能力，对多款开源自研产品进行了安全审计，发现即使完全脱离OpenClaw代码库，仅因沿用相同的设计范式，同类漏洞依然高频出现。有些产品为了修补已知安全缺陷而专门新增了防护机制，结果却由于安全设计缺陷，反而制造了新的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxPqx1Zl89ompy2qbKzTSKyq89FFiauvBfupK71hRdH1Or0qpKTT8BGp73qADod2vqHaibib4CvDxrHXJ49ErH1QbK1dDLYGXlnskQ/640?wx_fmt=png&from=appmsg#imgIndex=2)

**报告认为，当前AI智能体安全面临的核心挑战，不再是单点漏洞修复，而是功能快速迭代过程中系统性安全风险的持续扩散。传统的边界防御思路，在面对高自主性的智能体系统时已明显力不从心。**

360漏洞挖掘智能体的实战表明，要真正解决智能体生态的安全问题，必须用“Agent对抗Agent”的创新范式展开全流程自动化审计。它不仅能够帮助开发者识别上游遗留漏洞、阻断风险在软件供应链中的扩散，更能深入审计产品自身代码中的安全问题，从源头构建更稳固的防护体系。

此次报告基于360漏洞挖掘智能体实践所沉淀的漏洞分布形态与风险演进路径，不仅是对当前Claw生态的一次全面安全体检，更将为我国未来大规模智能体系统的安全建设提供可落地的工程参考与防御支撑。

↓《OpenClaw生态安全风险分析》报告原文如下↓

一、 概述

OpenClaw 核心能力的不断成熟与全面开放，引发了业界的关注热潮。得益于其底层架构的灵活性与高扩展性，OpenClaw 不仅支撑了大量基于它的二次开发，更启发了众多团队借鉴其理念开启独立自研，推动生态向多极化方向发展。

这种繁荣同时也伴随着产品形态的能力转变。当前的 Claw 系应用正逐渐打破传统工具“被动响应”的局限，向着具备自主决策能力的 Agent 跨越。这种能力跃迁不可避免地要求系统赋予其更复杂的接口与更宽泛的权限边界。当这些高权限、高自治的实体运行在不可信的网络环境中，或是面临潜在的恶意攻击时，失控的风险将被急剧放大。面对此类具备高度主观能动性的新型应用目标，传统的安全测试手段往往难以有效覆盖其动态逻辑与模糊边界。

基于此，本报告开展了一次深度的“漏洞挖掘智能体实践”。360 漏洞研究院引入自研的漏洞挖掘智能体，以“Agent 对抗 Agent”的创新范式，对 OpenClaw 生态产品展开了系统性的安全分析。借助漏洞挖掘智能体高效的全流程自动化漏洞挖掘能力，我们成功突破了复杂应用的测试瓶颈，累计挖掘出安全漏洞 20 余个，涵盖远程代码执行、认证绕过、权限提升、信息泄露等多种高危漏洞类型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNxCk0M8x4icfUrGemIEtmE9CsmzBU0l6G9recUzyomBMH5fnl7G07wAtU7nLqY1o80iaaLvr7IRW6lxBY4O5ib6LmIS9TMQBsgb3Usa3PmRTA/640?wx_fmt=png&from=appmsg)

图 1-1 OpenClaw 生态图概览

在对智能体在实战中捕获的丰富漏洞数据与攻击链路进行归纳分析后，我们发现，由于 OpenClaw 生态演进的独特性，其潜在的安全风险呈现出多样化、普遍性与可传播性，并深度渗透至各类衍生产品之中。本报告将结合此次智能体实践的成果，将 OpenClaw 生态划分为三大核心分析维度：OpenClaw 架构特征与防护失效、二次开发中的安全债传递、以及开源自研的安全挑战。围绕上述维度，本报告将系统性地剖析不同应用场景下潜藏的安全风险，旨在为 Claw 生态的持续、健康与积极发展夯实安全底座，贡献实质力量。

二、 漏洞列表

本研究共覆盖 OpenClaw 核心及 10 款 Claw 衍生产品，经系统性分析共确认 23 处独立安全漏洞。所有漏洞均已反馈至相关厂商与开发者跟进修复，并上报国家信息安全漏洞库（CNNVD）、国家信息安全漏洞共享平台（CNVD）等权威机构。下表按产品归属和漏洞类型进行汇总：

| 序号 | 产品名称 | 漏洞类型 | CNNVD | 危害程度 |
| --- | --- | --- | --- | --- |
| 1 | OpenClaw | 信息泄露 | CNNVD-2026-50773322 | 高危 |
| 2 | OpenClaw | 信息泄露 | CNNVD-2026-45978429 | 中危 |
| 3 | OpenClaw | 拒绝服务 | CNNVD-2026-18369523 | 高危 |
| 4 | OpenClaw | 授权绕过 | CNNVD-2026-24759492 | 中危 |
| 5 | LobsterAI | 远程任意文件读取 | CNNVD-2026-71027986 | 中危 |
| 6 | LobsterAI | 路径穿越 | CNNVD-2026-82655690 | 高危 |
| 7 | AutoClaw | 远程命令执行 | CNNVD-2026-01108369 | 高危 |
| 8 | ClawX | 信息泄露 | CNNVD-2026-31313202 | 中危 |
| 9 | CoPaw | 远程命令执行 | CNNVD-2026-22285599 | 严重 |
| 10 | CoPaw | 远程命令执行 | CNNVD-2026-43521646 | 严重 |
| 11 | Nanobot | 提示词注入 | CNNVD-2026-78883522 | 中危 |
| 12 | Nanobot | 服务端请求伪造 | CNNVD-2026-20334794 | 中危 |
| 13 | Nanobot | 访问控制绕过 | CNNVD-2026-20084544 | 中危 |
| 14 | Nanobot | 访问控制绕过 | CNNVD-2026-96922764 | 中危 |
| 15 | Nanobot | 服务端请求伪造 | CNNVD-2026-22577557 | 中危 |
| 16 | Nanobot | 访问控制绕过 | CNNVD-2026-68396869 | 高危 |
| 17 | Nanobot | 路径穿越 | CNNVD-2026-86246607 | 高危 |
| 18 | Molili | 远程命令执行 | CNNVD-2026-55617819 | 高危 |
| 19 | PicoClaw | 访问控制绕过 | CNNVD-2026-99907553 | 高危 |
| 20 | PicoClaw | 访问控制绕过 | CNNVD-2026-83686554 | 高危 |
| 21 | QClaw | 逻辑缺陷 | CNNVD-2026-78347890 | 中危 |
| 22 | Winclaw | 认证绕过 | CNNVD-2026-30781760 | 中危 |
| 23 | ZeroClaw | 认证绕过 | CNNVD-2026-86380766 | 高危 |

表格所示漏洞涵盖远程代码执行、认证与访问控制、越权文件操作、提示词注入与信息泄露、拒绝服务类等漏洞类型。这一分布特征与 OpenClaw 及其衍生产品的形态相符：多入口、高权限、重本地服务、弱组件间隔离。

为避免安全风险外溢及防止潜在的恶意利用，本报告中涉及的所有具体漏洞案例均进行匿名化处理。

三、 OpenClaw 架构特征与防御失效分析

在 OpenClaw 开源仓库中，与其 37 万 GitHub Stars 同样引人注目的，是其居高不下的安全公告数量。截至 2026 年 5 月 11 日，OpenClaw GitHub 已累计披露超过 535 个安全公告，在同期开源项目中处于显著高位。这客观反映出一个事实：在 OpenClaw 功能日益丰满的同时，其暴露的攻击面正被快速拓宽，深层的安全隐患也在同步积聚。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNxCk0M8x4ib5FtBYtdveOEFYKibiafcQURLPvnibibNcCjzP1yia7lvHRIdS1LBxIdL3uwEd1UOb2Gvibiap6V9GR7FfWichHjiaXhsu0DL4uY4E36P4/640?wx_fmt=png&from=appmsg)

图 3-1 OpenClaw 生态安全报告增长曲线图

从时间维度观察，这些安全风险的暴露正呈现出明显的加速趋势。在项目早期，安全公告大多以“周”为单位零星发布；然而进入 2026 年第一季度后，其披露频率已骤然攀升至日均 4 个以上。这种由疏到密的转变，其深层原因在于当前生态中普遍存在“能力扩展优先于安全约束”的开发倾向，激进的功能迭代与相对滞后的安全内建，最终催生了日益严峻的系统性风险。

3.1 架构特征

为了更好理解这些安全公告所反映的漏洞根因与攻击场景，需结合 OpenClaw 的核心运行架构进行分析。作为一个以本地资源操控为设计哲学的 AI Agent 网关，OpenClaw 的运作依赖于三个相互嵌套的基础组件：

**本地工具层（Tool Calling Layer）：**负责将大模型的决策转化为对本地资源的实际操作，包括文件读写、命令行执行、浏览器自动化、代码动态编译等。该层直接触及操作系统核心，必须严格验证操作主体身份并限定操作权限范围。

**网络连接层（Network Layer）：**支撑 Agent 与外部世界的双向数据交换。一方面，Agent 需要主动抓取网页、调用外部 API、下载资源；另一方面，系统又在本地暴露 HTTP 服务、WebSocket 连接、RPC 端口以接收外部请求。该层必须确保入口合法与出口可控性。

**决策核心层（Control Plane）：**以大型语言模型为中枢，将自然语言指令转化为任务计划并调度工具执行。该层需要持续接收并理解多源输入（用户指令、网页内容、工具反馈），必须确保指令来源可信、决策过程不可篡改。

这三层组件的交互关系决定了 OpenClaw 的安全防御不能依赖单点机制，必须构建涵盖四个维度的纵深防御体系：认证边界（谁有权接入本地服务）、网络边界（哪些网络面允许被触及）、执行边界（高权限操作如何被物理隔离）以及控制边界（决策指令如何被验证）。理想情况下，这四层边界应逐层递进、互为依托：认证边界阻挡未授权访问者，网络边界缩小攻击暴露面，执行边界将突破者限制在隔离环境内，控制边界确保即使前三层失守，核心决策仍不可被劫持。

3.2 防护边界失效

尽管架构设计上具备良好的防御蓝图，但在 OpenClaw 的实际代码实现与复杂运行环境中，上述理想的纵深防御体系却往往难以维系。某一层的破坏往往会为其他边界打开缺口，使得任何单点突破都可能横向扩散为系统性失控。本节将结合安全公告中披露的具体问题进行攻击路径分类，逐一分析每层防御边界上真实发生过的安全隐患。

3.2.1 认证边界：多路径认证与授权缺口

认证边界的核心职责是确认“操作主体的合法性”。为了适配多样化的交互需求，OpenClaw 设计了从设备配对到多级管理的复杂权限体系，并开放了本地 CLI、WebUI、API 调用等多种访问通道。理想状态下，每一个访问入口都应在对应入口完成权限校验，从而形成严格的认证验证控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNxCk0M8x4icTpzxK1ARLITZjyImibWolEQpFq8tkicCnAfbCgvXyxx2ictSA6ZpxOPLMeK16OYODQMR2tBNrRdwquEhwibyK0myDcTs82ulMfME/640?wx_fmt=png&from=appmsg)

图 3-2 通过 gatewayUrl 绕过认证边界漏洞

然而，安全公告数据显示，认证与访问控制类漏洞在 OpenClaw 安全公告中占比极高。其根因在于，多层权限模型与错综复杂的访问通道交叉叠加后，容易在代码实现中产生校验盲区。攻击者可通过本地未授权接口、WebSocket 身份验证绕过、跨平台凭证复用等路径，以较低成本突破第一道防线，获得后续横向移动的机会。

3.2.2 网络边界：双向数据流转与暴露面失控

如果说认证边界管控的是访问主体，网络边界管控的则是“数据与连接的合法流向”。作为一个强交互的 Agent，OpenClaw 既需要主动外联（如抓取网页、调用第三方 API）以获取上下文，又必须提供本地服务监听以接收外部指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNxCk0M8x49jy7rq49qFUvdRaKXKUjw6ZKb4XLP6YCiaxGg7jwfAexxb87l9YjbAKmncDnFhHzW4FLlgQ15iaZ0WUJfbwW4U54SiawKAgfRibfU/640?wx_fmt=png&from=appmsg)

图 3-3 SSRF 突破网络边界漏洞

这种“保持高频外部感知”与“收敛自身暴露面”之间的诉求冲突，导致传统边界防御在此处趋于模糊，SSRF（服务器端请求伪造）、协议绕过等网络层风险反复出现。更为严峻的是，一旦前置的认证边界存在校验盲区，OpenClaw 内置的强大外部资源获取工具链便会成为内网探测与横向穿透的跳板工具。此时，网络边界防御不再是单纯的阻断外部恶意流量，而是演变为应对系统攻击面扩张问题。

3.2.3 执行边界：碎片化隔离与沙箱穿透

执行边界负责解决“高权限操作在物理和逻辑层面上的隔离”。OpenClaw 的设计初衷赋予了 Agent 极高的系统底层操控力，这也迫使系统必须依赖沙箱机制来限制潜在的破坏影响。这构成了执行边界最本质的挑战：既要无限逼近操作系统的核心能力，又要限制其破坏范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNxCk0M8x4ibVPUb20T4YMMrMbiacdzAnNAWx...