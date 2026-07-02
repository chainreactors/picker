---
title: RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具
url: https://mp.weixin.qq.com/s/QTl4ILYulvQgU75Yj6HZvA
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:56:12.946779
---

# RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH3tPHsN4icp5icicASOWxPXDfZ2WYdNUvicV4qGtue1iaDkywdSYv26ZibIaGAagzp97htGdjyXBpIqpgiawyfyVic0bPeH6dwc7bnWDhk/0?wx_fmt=jpeg)

# RedAmon：串联侦察、漏洞利用与后渗透的 AI 安全工具

原创

安全ker
安全ker

安全客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一款全新开源攻击性安全平台 RedAmon 重构自动化渗透测试流程，将**资产侦察、漏洞利用、后渗透操作、AI 漏洞分级研判、自动化代码修复**整合为一套端到端完整流水线，最终可自动生成附带修复代码的 GitHub 合并请求（PR）。

RedAmon 是基于 Docker 构建的模块化容器化渗透测试框架，无需在本地主机直接安装各类安全工具。

![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH0XRpv3B8aFUCJHPjsb04nzsHjxO3MQPLBia4BFQyAYyel9WowETYZjGrsjsVSqcKXPmhXFwqwIs64K06FF2vqfKdibkbwlTk9ic0/640?wx_fmt=webp&from=appmsg)

该平台架构依托六大核心模块：并行化资产侦察流水线、AI 智能体调度器、攻击面图谱、跨会话情报演化图谱 EvoGraph、CypherFix 漏洞修复引擎，以及支持 500 余项配置参数的项目设置引擎。其完整杀伤链流程可概括为：资产侦察 → 漏洞利用 → 后渗透操作 → AI 漏洞研判 → 代码修复智能体 → 提交 GitHub 合并请求。

资产侦察模块

RedAmon 的侦察流水线可在 Kali Linux 容器内并行调度 40 余款行业主流安全工具，包含 Subfinder、Amass、Naabu、Masscan、Nuclei、Katana、FFuf、Arjun 等。所有工具输出数据统一汇入共享 Neo4j 知识图谱，图谱内置17类实体节点、20 余种关联关系，数分钟内即可为 AI 智能体构建结构完整、全域连通、可检索查询的可视化攻击面，省去传统工具数小时的数据整理耗时。

专属 AI 安全测试模块「AI Gauntlet」专门针对大模型 / AI 业务面开展拓展侦察，集成四款红队专用工具 garak、PyRIT、Giskard、promptfoo，对探测到的接口端点开展安全检测，覆盖提示注入、模型越狱、数据泄露等风险，检测结果统一映射至 OWASP 大模型安全规范与 MITRE-ATLAS 大模型攻防框架。

核心自主AI智能体

RedAmon 的核心是基于 LangGraph 搭建、采用 ReAct（推理 + 行动）模式的自主智能体。智能体按顺序执行三大阶段：信息搜集阶段、漏洞利用阶段、后渗透阶段，通过运行在沙箱隔离 Kali 环境中的模型上下文协议（MCP）服务，可调用 14 款以上安全工具：

Metasploit：漏洞载荷执行

Hydra：凭证暴力破解

Playwright：浏览器自动化测试

完整 Kali 命令行环境，预装 70 余款命令行安全工具

平台内置「分队并行模式（Fireteam）」，主根智能体可拆分出多支专业子智能体同步作业，例如同时执行：Hydra 校验账号密码策略、通过权限提升链路验证 CVE 漏洞利用路径、全域扫描前端跨站脚本（XSS）漏洞。

自动化漏洞修复引擎CypherFix

绝大多数攻击性安全工具仅止步于漏洞发现，而 RedAmon 搭载双智能体修复流水线 CypherFix 实现漏洞闭环处置：

1. 漏洞研判智能体：针对 Neo4j 图谱执行 9 套预设图查询语句，聚合数百条扫描结果、自动去重，并根据漏洞可利用难度完成风险分级；
2. 代码修复智能体：拉取目标代码仓库，依托 11 款代码分析工具遍历源码，通过循环推理迭代生成针对性修复代码，自动创建 GitHub 合并请求，交由人工审核合并。

人机协同与访问管控

该框架设计上并非完全无人自主运行，配套**工具确认机制**实现人机介入管控：执行高风险操作（Nmap 大规模扫描、Metasploit 漏洞载荷、Hydra 暴力破解等）前会暂停智能体流程，在交互界面弹出「允许 / 拒绝」操作弹窗，人工确认后方可继续。

支持上传《授权测试范围文档（RoE）》一键配置全项目操作约束；内置目标防护机制，框架底层永久拦截政府、军工、教育类域名，杜绝违规扫描。

开发团队与模型兼容

RedAmon 由具备 15 年企业级 AI 智能体系统研发经验、AWS 认证 AI 平台架构师萨穆埃莱・詹皮耶里（Samuele Giampieri）主导开发维护；协同开发者瑞泰什・戈希尔（Ritesh Gohil）任职 Workday 网络安全工程师，拥有 7 年渗透测试实战经验，累计发布 11 个通用漏洞编号（CVE）。

框架兼容主流大模型服务商：OpenAI（GPT-5）、Anthropic（Claude Opus 4.6）、亚马逊 Bedrock，以及适配 Ollama 的本地离线模型，单项目可动态切换 400 余款大模型，项目开源仓库托管于 GitHub。

信息来源：cybersecuritynews.com

![](https://mmbiz.qpic.cn/mmbiz_png/e8XlCTfPrcM4SD27bheY74gn8dPagfIOekOMj8iapjKdXVeHY08GT5wjvb73xa77ZwB1FseR8zphAc9pMg7icqx4t2AmAvLQiaibZR5IGmEWc18/640?from=appmsg)

END

推荐阅读

[「智弈」AI智能体攻防实战沙龙 · 6.24圆满落幕](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790137&idx=1&sn=c190a20f51331ae2aefb4495eda5f549&scene=21#wechat_redirect)

2026-06-30

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH2ibgu9GSLv7389KPia6EJhdKCvcN10WZwGkFZYRLVS1ygxC9GMj4YrNfLX59eKRgMZlaEYBtkTfeIRD9ibvXrwWfuT98pgBh5Pfc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790137&idx=1&sn=c190a20f51331ae2aefb4495eda5f549&scene=21#wechat_redirect)

[【FDE前沿部署工程师】全国百城上岗计划二期来啦！](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790132&idx=1&sn=63a6ceb5693d788e3fa50aafc4df3365&scene=21#wechat_redirect)

2026-06-29

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH2CBkwV2w4bhhMD2KQvZvz3lxomgCxGCeWGvAlgVjVUl2pX3m0kE9ktFJJZt4hB4duXv9LmzddfRrZSxQXIFBKHcIrZBf91uzA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790132&idx=1&sn=63a6ceb5693d788e3fa50aafc4df3365&scene=21#wechat_redirect)

[一款完全离线的自主渗透测试智能体AIRecon](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790127&idx=1&sn=159cac76ec5b9ebd71809086b4edae5e&scene=21#wechat_redirect)

2026-06-26

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH1sB5A3Ot2mZ1UCUo7tvY08WcsibPkdPo9JFHX4icNEb5uZaNib6zkL5HE3BZicIot6IXrDBLuvCtd9UiblTGGgJdBpqzW0mUpk6aNs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790127&idx=1&sn=159cac76ec5b9ebd71809086b4edae5e&scene=21#wechat_redirect)

[360纳米Work Box全国渠道伙伴招募正式启动](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790124&idx=1&sn=e856b70dd849add1b371b803ae1f8885&scene=21#wechat_redirect)

2026-06-25

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH13PbWg8pKT6DGibn7o2IUZvQPQqdCsQuhuwnUFDCOojMVian9loj2tX98SJfTvKIvPkibqa8Jbf5yy8RkBpprl0Pxlicl90xXuNOA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790124&idx=1&sn=e856b70dd849add1b371b803ae1f8885&scene=21#wechat_redirect)

[新开源网络安全平台CyberSentinel AI v3.0 正式亮相](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790104&idx=1&sn=76da3eee9bf9a9d214f46131cf15c8fe&scene=21#wechat_redirect)

2026-06-22

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH3aWvevMbHzlrLsUib6ORkV0l7Wfr42l0Bs38mUPlB4xe8ZtibFo65myPVdafzodMP3latGG0ibVYAkBR2vBrM8BM6jhSkz7Otaq0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790104&idx=1&sn=76da3eee9bf9a9d214f46131cf15c8fe&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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