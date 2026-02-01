---
title: 2026年人工智能安全摘要
url: https://mp.weixin.qq.com/s/MKRU2L5qTWUrgKVHEriwYg
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:01.508388
---

# 2026年人工智能安全摘要

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/niaMibh6Pic6RYpPrnXwRDOuXLSwzpeM9OpCQGCemk5ibuFDjGQdcRJY1Xb2Gdn4RwtpvlY4PcviczYDkPvUKuqBNgA/0?wx_fmt=jpeg)

# 2026年人工智能安全摘要

原创

破天KK
破天KK

KK安全说

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/niaMibh6Pic6RYpPrnXwRDOuXLSwzpeM9OpNlRbt022XuG8lqQUhQibb6Uo2XdmhsjR1I9GuWZPhRE9jyS6XvU2Ahg/640?wx_fmt=png&from=appmsg)

n8n 中存在严重的未经授权的远程代码执行漏洞，Claude Code 存在信任边界和依赖项劫持漏洞，NIST AI 代理安全 RFI 漏洞，4 个 Copilot 问题（提示泄露、上传绕过、沙箱逃逸），“模型混淆”供应链攻击，恶意 Chrome 扩展程序窃取 LLM 聊天记录，IDE 扩展程序命名空间声明攻击，以及使用 Claude 进行 Flutter 流量代理。

1️⃣ 允许未经身份验证的威胁行为者完全控制 n8n 实例的漏洞 — CVE-2026-21858 — CVSS 10.0 https://www.cyera.com/research-labs/ni8mare-unauthenticated-remote-code-execution-in-n8n-cve-2026-21858 Cyera 的 Dor Attias

2️⃣ Claude 代码中的隐藏后门：为何其强大之处也正是其最大的漏洞https://www.lasso.security/blog/the-hidden-backdoor-in-claude-coding-assistant或阅读 Lasso 网站上 Oxenberg 和 Eliran Suisa 的文章

3️⃣ 关于人工智能代理安全考虑因素的信息请求https://public-inspection.federalregister.gov/2026-00206.pdf

`|`4️⃣ 使用分隔符和 JSON 有效载荷进行间接提示注入，可在 Copilot 中启用系统提示披露https://medium.com/@d\_f4u1t/indirect-prompt-injection-using-delimiter-and-json-payload-enables-system-prompt-disclosure-in-996a7b15dc01

5️⃣ 直接提示注入功能使 Copilot 中的系统提示信息披露成为可能https://medium.com/@d\_f4u1t/direct-prompt-injection-enables-system-prompt-disclosure-in-copilot-feeefddeac97

6️⃣ Copilot 中的 Base64 文件上传绕过功能允许受限文件类型内容进入会话进行分析https://medium.com/@d\_f4u1t/base64-file-upload-bypass-in-copilot-allows-restricted-file-type-content-to-enter-session-for-de36e4c3096a

7️⃣ 利用 Python 沙箱逃逸技术在 Copilot 隔离的 Linux 环境中执行任意命令https://medium.com/@d\_f4u1t/arbitrary-command-execution-within-copilots-isolated-linux-environment-via-python-sandbox-escape-c8ce6d9ac480

8️⃣ Vibe Hacking：使用 Claude 在 Android 上代理 Flutter 流量https://randywestergren.com/vibe-hacking-proxying-flutter-traffic-on-android-with-claude/ Randy Westergren

9️⃣ AI模型混淆：LLM/AI模型供应链攻击https://checkmarx.com/zero-post/hugs-from-strangers-ai-model-confusion-supply-chain-attack/ Ori Ron 和 Tal Folkman，Checkmarx Zero

🔟 90万用户信息泄露：恶意AI Chrome扩展程序窃取ChatGPT和DeepSeek对话https://astrix.security/learn/blog/900k-users-compromised-malicious-ai-chrome-extensions-steal-chatgpt-and-deepseek-conversations/ Astrix Security的Alon Berger

1️⃣1️⃣ 当你的插件开始选择你的依赖项时：Claude Code 中的 Marketplace Skills 和依赖项劫持https://prompt.security/blog/when-your-plugin-starts-picking-your-dependencies-marketplace-skills-and-dependency-hijack-in-claude-code David Abutbul，Prompt Security

1️⃣2️⃣ 个 VSCode IDE 分支版本使用户面临“推荐扩展”攻击风险https://www.bleepingcomputer.com/news/security/vscode-ide-forks-expose-users-to-recommended-extension-attacks/ Koidex 的 Oren Yomtov

![](https://mmbiz.qpic.cn/mmbiz_png/niaMibh6Pic6RYpPrnXwRDOuXLSwzpeM9OpHORawN6AGUvlBalvF0bZHK1Gbx8hsgDrzPLjKJucLS0kEribT8ybb8Q/640?wx_fmt=png&from=appmsg)

ZombieAgent 持久化和数据窃取、OWASP Agentic AI Top 10 漏洞实战、工具投毒和隐藏指令、ServiceNow 代理劫持、IBM AI 代理执行恶意软件、破解 Claude 代码的八种方法、AI 生成的暴力破解活动、AI 系统在生命周期中泄露数据的情况、代理浏览器隔离失败以及现代 AI 和 ML 库中的 RCE 风险。

1️⃣ ZombieAgent 和 ChatGPT 的新漏洞导致数据窃取持续蔓延 — https://www.radware.com/blog/threat-intelligence/zombieagent/ — Zvika Babo，Radware

2️⃣ OWASP Agentic AI Top 10：野外威胁 — https://labs.lares.com/owasp-agentic-top-10/ — Lares Labs 的 Raúl Redondo

3️⃣ AI 工具投毒：隐藏指令威胁 AI 代理 — https://www.crowdstrike.com/en-us/blog/ai-tool-poisoning/ — Vanessa Villa，CrowdStrike

4️⃣ ServiceNow 中的身份验证漏洞和代理劫持漏洞，BodySnatcher — https://appomni.com/ao-labs/bodysnatcher-agentic-ai-security-vulnerability-in-servicenow/ — AppOmni 的 Aaron Costello

5️⃣ IBM AI（“Bob”）下载并执行恶意软件 — https://www.promptarmor.com/resources/ibm-ai-%28-bob-%29-downloads-and-executes-malware — PromptArmor

6️⃣ 安全团队在人工智能项目中应该提出的第一个问题 — https://cloudsecurityalliance.org/blog/2026/01/09/the-first-question-security-should-ask-on-ai-projects — 云安全联盟的 Rich Mogull

7️⃣ 用 8 种不同的方法攻破 Claude Code — https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/ — RyotaK，GMO Flatt Security

8️⃣ GoBruteforcer 内部机制：AI 生成的服务器默认设置、弱密码、加密攻击活动 — https://research.checkpoint.com/2026/inside-gobruteforcer-ai-generated-server-defaults-weak-passwords-and-crypto-focused-campaigns/ — Check Point Research

9️⃣ 人工智能系统数据泄露：真实暴露路径的生命周期回顾 — https://www.praetorian.com/blog/where-ai-systems-leak-data-a-lifecycle-review-of-real-exposure-paths/ — Justin Copeland，Praetorian

🔟 代理浏览器缺乏隔离性导致旧漏洞重现 — https://blog.trailofbits.com/2026/01/13/lack-of-isolation-in-agentic-browsers-resurfaces-old-vulnerabilities/ — Lucas Bourtoule，Trail of Bits

1️⃣1️⃣ 将苹果人工智能武器化用于进攻性行动，第二部分 — https://hxr1.ghost.io/weaponizing-apples-ai-for-offensive-operations-part-2/ | https://www.youtube.com/watch?v=UooCY59nQSQ — hxr1 at hxr1

1️⃣2️⃣ AI代理能教会我们哪些关于国家健康保险（NHI）治理的知识 — https://blog.gitguardian.com/what-ai-agents-can-teach-us-about-nhi-governance/ — GitGuardian的Dwayne McDaniel

1️⃣3️⃣ 威胁行为者正积极攻击LLM — https://www.greynoise.io/blog/threat-actors-actively-targeting-llms — GreyNoise 的 boB Rudis

1️⃣4️⃣ 人工智能的瓶颈不在于模型或工具，而在于安全——https: //zkorman.com/posts/ai-bottleneck-is-security/12——Zack Korman，zkorman.com

1️⃣5️⃣ 利用 HITL 对话伪造技术将 AI 安全措施转化为武器 — https://checkmarx.com/zero-post/turning-ai-safeguards-into-weapons-with-hitl-dialog-forging/ — Ori Ron，Checkmarx

1️⃣6️⃣ 代理安全悖论：Cursor 中的可信命令会成为攻击向量 — https://www.pillar.security/blog/the-agent-security-paradox-when-trusted-commands-in-cursor-become-attack-vectors — Dan Lisichkin，Pillar Security

1️⃣7️⃣ 糟糕的氛围：比较热门编码代理的安全编码能力 — https://blog.tenzai.com/bad-vibes-comparing-the-secure-coding-capabilities-of-popular-coding-agents/ — Onzai 的 Ori David

1️⃣8️⃣ 为什么你的 AI 代理需要不同的监控方式（第一部分）— https://medium.com/@michael.hannecke/why-your-ai-agent-needs-different-monitoring-and-how-to-build-it-1702b48ee605 — Michael Hannecke 在 Medium 上的文章

1️⃣9️⃣ 利用现代 AI/ML 格式和库进行远程代码执行 — https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries — Curtis Carmony，Unit 42，Palo Alto Networks

2️⃣0️⃣ 地图并非疆域，代理工具的信任边界 — https://niyikiza.com/posts/map-territory/ — Niki A. Niyikiza，niyikiza.com

2️⃣1️⃣ AI 安全指南，300 多页关于保护 AI 和数据中心系统的实用指导 — https://owaspai.org — OWASP AI 安全项目

2️⃣2️⃣ 构建组织内代理的流程，构建安全流程 — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/build-secure-process — Microsoft

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/niaMibh6Pic6RZBtYmiaJBItDCOn2HTsEH2xPkboCfSdwRIptZeQ8cVhB2Yicund3DyiaO2mc2mibrPJ2F4G6k00icDMZQ/0?wx_fmt=png)

KK安全说

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/niaMibh6Pic6RZBtYmiaJBItDCOn2HTsEH2xPkboCfSdwRIptZeQ8cVhB2Yicund3DyiaO2mc2mibrPJ2F4G6k00icDMZQ/0?wx_fmt=png)

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