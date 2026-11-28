---
title: 一些红队AI安全的资料，关于靶场、工具和培训
url: https://mp.weixin.qq.com/s/ZuqjLMpATiXUvsEmpF81nw
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:40:12.748843
---

# 一些红队AI安全的资料，关于靶场、工具和培训

# 一些红队AI安全的资料，关于靶场、工具和培训

原创

小白哥
小白哥

小白安全成长记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

看大家对AI安全的兴趣很高，周末了，我把我找到的一些关于AI的靶场、安全工具、培训认证相关的资料给大家，大家各取所需吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ueoom4Tb3S8dV6gqDQuF45bCEmXb6fEBh7nIIm3PLRbMXYh4tQ33SIAiaLWaNkt3pagqml3Aoic1IpYzPicd6k5qWXzXVZ6Z3CCibj2ynBxQQKA/640?wx_fmt=png&from=appmsg)

## AI靶场

| 实验室 | 类型 | 主要练习的技术 |
| --- | --- | --- |
| Gandalf: Agent Breaker | 免费 | 针对一组模拟 GenAI 应用程序和代理发起快速攻击，从系统提示提取到通过文档、网页和 MCP 服务器描述进行间接注入。 |
| 微软人工智能[红队演练实验室] | 免费 | 微软的 AI 红队实战课程首次在 2024 年美国黑帽大会上开设，课程内容涵盖凭证窃取和多轮攻击等挑战。 |
| Damn Vulnerable LLM Agent | 免费 | 针对使用工具的代理进行快速注入，其中注入会转化为行动。 |
| Damn Vulnerable MCP Server | 免费 | 针对故意设置漏洞的 MCP 服务器的十项挑战，包括工具投毒、撤回、工具遮蔽和令牌窃取。 |
| PortSwigger网络安全学院的Web LLM 攻击 | 免费 | LLM 在 Web 应用程序中的功能包括过度代理、不安全的输出处理和间接提示注入。 |
| Wiz的Prompt Airlines | 免费 | 一场 CTF 挑战赛，你需要说服客服机器人给你一张免费的（虚构的）机票。 |
| Pwned Labs AI 安全实验室 | 托管 | 在真实环境中，人工智能和智能体攻击场景，以及它们通常依赖的云实验室。 |

### ▍靶场链接（忘了写了，补上，和上面是对应的）

* https://play.lakera.ai/agent-breaker
* https://github.com/microsoft/AI-Red-Teaming-Playground-Labs
* https://github.com/ReversecLabs/damn-vulnerable-llm-agent
* https://github.com/harishsg993010/damn-vulnerable-MCP-server
* https://portswigger.net/web-security/llm-attacks (挺有意思的)
* https://promptairlines.com
* https://pwnedlabs.io/explore

## AI红队工具

* garak: https://github.com/NVIDIA/garak。一款 LLM 漏洞扫描器。
* PyRIT: https://github.com/microsoft/PyRIT。用于生成式人工智能的 Python 风险识别工具。
* promptfoo：https://github.com/promptfoo/promptfoo。对提示、代理和 RAG 进行测试和红队演练。

## 可参考的一些权威机构

* OWASP-Top-10针对LLM应用: https://genai.owasp.org
* OWASP十大代理应用安全风险:https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
* MITRE-ATLAS:https://atlas.mitre.org
* NIST-AI-600-1:https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

## 相关课程和认证

| 课程 | 格式 | 重点 |
| --- | --- | --- |
| 来自 Pwned Labs的人工智能系统攻击与防御训练营 (AISRTP) | 按需进行的实践考试 | 涵盖直接和间接提示注入、RAG投毒、工具和代理滥用以及MCP和CI/CD代理攻击路径，并针对每种攻击路径提供相应的防御措施。无需具备人工智能安全经验或Python编程知识。 |
| AI-300： OffSec 的高级 AI 红队 (OSAI) | 自主安排进度的24小时实践考试 | 对集成人工智能的系统进行攻击性测试，包括低层代理（LLM）和多代理设置。高级课程，面向经验丰富的安全从业人员。 |
| SANS SEC411：人工智能安全原则与实践 | 自主学习，包含实验课 | GenAI 和 LLM 从业者辩护。 |
| 来自 DeepLearning.AI 的红队 LLM 应用 | 短期课程，免费 | 对聊天机器人进行手动和自动红队演练的简要介绍。 |

OSCP的AI-300认证大家应该不陌生了吧，好多地方都介绍这个了，今天就到这吧，排版可能有点乱，大家凑合看吧，现场条件不允许。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EhWx22VKFBg0hrB58Q3PaRC6G2rPMW7pruxicEKOicpBXrickYY3FNnkPwknibIgaEH9dTVfhpAiafhHkhkZ7O8iaeNQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过