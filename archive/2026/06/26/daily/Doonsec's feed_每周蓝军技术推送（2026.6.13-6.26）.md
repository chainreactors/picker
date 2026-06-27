---
title: 每周蓝军技术推送（2026.6.13-6.26）
url: https://mp.weixin.qq.com/s/3m0pWQWGt9cEl24OsaJ36w
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:47:50.673338
---

# 每周蓝军技术推送（2026.6.13-6.26）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jCnwmVXD2CBqTSdNAyLyHM6myia20TxewnFVdKlI0usYNkPJ9BRf2sfo49aofw82pXazibLdUricPiaaNIiaFIZ0qOGxwibfdYuYxK4rA/0?wx_fmt=jpeg)

# 每周蓝军技术推送（2026.6.13-6.26）

M01N Team

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jCkic4rQibhGIjbOac4NqlvfqVkbL1S1WsfvOKjtfrLM5FSIbU9zGotjpDjlvkecl4ibrmKycu9CEOeHBHsBgRMq4HbnJ0yhKn2JS0/640?wx_fmt=png&from=appmsg)

**内网渗透**

Session Switcher：自动检测Burp代理流量中的cookie/header变化并更新会话，实现一键切换

https://blog.doyensec.com/2026/06/17/session-switcher.html

**终端对抗**

malsnitch：内存转储扫描与二进制模式检测的恶意软件分析工具

https://github.com/grepstrength/malsnitch

**漏洞相关**

Bumblebee：只读扫描开发者机器风险包和扩展，直接读取元数据避免触发恶意脚本

https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee

介绍一种利用HTTP/2协议快速消耗Apache和Envoy服务器内存的攻击技术与PoC

https://github.com/Codex Discovered a Hidden HTTP/2 Bomb

总结包管理器客户端和注册表常见的CWE漏洞模式，包括路径穿越、授权绕过等

https://nesbitt.io/2026/05/04/package-manager-cwes.html

**人工智能和安全**

GitHub利用LLM进行上下文推理，减少秘密扫描误报提升可信度

https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/

Zealot AI代理自主注入SSH密钥实现持久化，利用常见云配置错误快速攻击

https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks

Anthropic 发布 Mythos 模型系统卡，包含网络应用细节及 Glasswing 项目

https://pylos.co/2026/04/11/myth-mythos-where-do-we-go-from-here

Anthropic 承认 Mythos 无法突破沙箱，Glasswing 缺乏独立验证与传统 Fuzzer 对比

https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic

实验证实开源及旗舰模型难以在无提示下复现 Mythos 漏洞发现

https://semgrep.dev/blog/2026/needles-and-haystacks-can-open-source-flagship-models-do-what-mythos-did

Claude Mythos Preview：自主编写浏览器漏洞利用链，结合JIT堆喷绕过沙箱

https://www.anthropic.com/research/mythos-preview

GitHub发布100多个AI代理工作流，用于自动化代码库问题处理、代码重构和积压任务清理

https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows

通过HTML注释隐藏prompt注入，绕过安全过滤读取并截取API key的恶意Claude Code Github action分析

https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/

visa-vulnerability-agentic-harness：利用LLM进行多阶段漏洞发现与利用链构建的自动化框架

https://github.com/visa/visa-vulnerability-agentic-harness

Foundry安全规范：通过agent与CodeGuard规则协同，实现检测到预防的飞轮机制

https://github.com/CiscoDevNet/foundry-security-spec

LangGraph Checkpointer漏洞：从SQL注入到RCE，利用用户控制的filter参数

https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/

AI代理攻击中金丝雀提前8分钟预警，欺骗感知使完全攻破率从20%降至3%

https://agentic.tracebit.com/

Daybreak：OpenAI推出的安全自动化工具，集成威胁建模与补丁生成

https://openai.com/index/daybreak-securing-the-world/

研究LLM在漏洞发现中的使用，探讨模型与扫描器协作优化方法

https://shad0wmazt3r.github.io/ai-security

使用AI代理对Llama Scout进行红队测试，发现232个严重漏洞

https://dreadnode.io/research/redefining-ai-red-teaming-in-the-agentic-era

Symphony：将Linear任务板化为编码代理控制平面的开源规范，实现500% PR增长

https://openai.com/index/open-source-codex-orchestration-symphony

**云安全**

分析 AWS notyet 持久化，常规 IR 手段均失效，仅 SCP 策略可有效遏制

https://sonraisecurity.com/blog/fighting-eventual-consistency-based-persistence-an-analysis-of-notyet

AWS CodeBuild 可提取 CodeConnections 高权 Token，控制组织所有代码库

https://thomaspreece.com/2026/03/23/part-2-aws-codebuild-escalating-privileges-via-aws-codeconnections

分析 AWS Bedrock AgentCore 组件存在的 IAM God Mode 权限风险

https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode

AWS更新威胁技术目录，强调攻击者滥用合法API调用需关注上下文异常

https://aws.amazon.com/blogs/security/what-the-march-2026-threat-technique-catalog-update-means-for-your-aws-environment

ELBaph：用于映射AWS负载均衡器路由并执行可达性探测的Go CLI工具

https://blog.doyensec.com/2026/05/25/cloudsectidbits-elbaph-alb.html

发布 SmokedMeat 红队工具，扫描 GitHub Actions 注入缺陷与 Token 权限

https://labs.boostsecurity.io/articles/introducing-smokedmeat

滥用云日志服务进行防御规避，通过篡改或禁用日志隐藏攻击活动

https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/

GCP serviceData字段在日志导出时被丢弃，导致安全规则静默失效

https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous

研究Salesforce威胁模型与检测方法，提供针对攻击行为的查询指南

https://securitylabs.datadoghq.com/articles/mapping-out-your-unknown-threat-hunters-guide-to-salesforce/

**其他**

SpecterOps发布Janus工具，解析C2日志以识别操作摩擦与改进点

https://specterops.io/blog/2026/04/10/janus-listen-to-your-logs

EvidenceForge：利用AI代理生成ATT&CK攻击场景，确定性日志生成并多维度评估

https://github.com/Cisco-Talos/EvidenceForge

Shai-Hulud：利用OIDC滥用投毒npm包并伪造Sigstore来源信息

https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis

Package Proxy：无客户端供应链安全检查，包括包年龄和上传机制回归检测

https://blog.thinkst.com/2026/06/introducing-package-proxy-supply-chain-safety-checks-without-client-side-software.html

![](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jClIKhhunzJMgeYEbVqYs8GoozOyOggicaNhY32ibayEWv8Exib1BjOFBu1HiajwPsgn8hB9Z3wyUibcjgRonJqIbZB911nF65aZ1MAQ/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jCkIDPrZax8NKovNrnJESMqtBYx69I05GoYSVLXWXLmxrHjJ8DdxujC5QTic8SznoMr2uFiaI8XzLjs47AQDSfEGveToIed12avIY/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[每周蓝军技术推送（2026.6.6-6.12）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247495144&idx=1&sn=8992a84a011da619208763c41939f05d&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.5.30-6.5）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247495125&idx=1&sn=7ad029e48cf6f3d21beadb2e5807397b&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.5.23-5.29）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247495105&idx=1&sn=627e6f56e615e28b757cf22f9c309691&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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