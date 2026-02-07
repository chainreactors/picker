---
title: 每周蓝军技术推送（2026.1.31-2026.2.6）
url: https://mp.weixin.qq.com/s/IGi02_O3c1zcDTOxcyJpdA
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:06:05.139340
---

# 每周蓝军技术推送（2026.1.31-2026.2.6）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbD5z6C0g2NAp2OicEl3fdbRrPUY2MuWIcreXMC0tGBdfWBviaqDPPyN63iawoWIujD6l1Fx5keMUib4w/0?wx_fmt=jpeg)

# 每周蓝军技术推送（2026.1.31-2026.2.6）

原创

天元实验室
天元实验室

M01N Team

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jCk7wNPnxwue9JoGAuElhhYI7OZfjT73gEzX05Zwpa03r6OugQbQrOFDlE1lLxx2fCibf9G6xHDaVkI7x2iax9K3VCjuXjKtneebI/640?wx_fmt=png&from=appmsg)

**Web安全**

Web应用渗透测试和漏洞赏金指南，涵盖方法论、工具和漏洞识别利用资源

https://github.com/xalgord/Massive-Web-Application-Penetration-Testing-Bug-Bounty-Notes

Upload Forge：用于检测和利用Web应用文件上传漏洞的安全工具

https://github.com/errorfiathck/upload\_forge

CVE-2025-68613和CVE-2026-25049：分析n8n平台RCE漏洞，详细描述沙箱逃逸和绕过修复的技术细节

https://fatihhcelik.github.io/posts/n8n-RCEs-A-Tale-of-4-Acts/

**内网渗透**

MANSPIDER：扫描网络SMB共享中敏感文件

https://github.com/blacklanternsecurity/manspider

**终端对抗**

DumpBrowserSecrets：从Chromium和Gecko浏览器提取凭据

https://github.com/Maldev-Academy/DumpBrowserSecrets

利用WFP等阻断EDR代理与云端通信的EDR静默技术

https://ipurple.team/2026/01/12/edr-silencing/

分析2020-2025年间终端安全规避技术的发展演变，涵盖BYOI、BYOVD、DLL劫持等多种EDR绕过技术

https://windshock.github.io/en/post/2025-05-28-endpoint-security-evasion-techniques-20202025/

介绍Windows投影文件系统(ProjFS)的内部机制和技术原理

https://www.huntress.com/blog/windows-projected-file-system-mechanics

GhostKatz：通过利用易受攻击的内核驱动程序的物理内存读取原语来转储LSASS内存的工具

https://github.com/RainbowDynamix/GhostKatz

CustomDpapi：直接调用未记录的DPAPI RPC接口，绕过公开的CryptUnprotectData函数

https://github.com/EvilBytecode/CustomDpapi

滥用来阻止EDR进程执行的技术，包括AppLocker工作原理和攻击者如何利用该机制绕过安全检测

https://ipurple.team/2026/02/02/applocker-rules-abuse/

通过Windows内部机制实现持久化

https://www.praetorian.com/blog/corrupting-the-hive-mind-persistence-through-forgotten-windows-internals/

卡巴斯基研究团队分析Notepad++供应链攻击事件，揭示多个执行链和新IoC

https://securelist.com/notepad-supply-chain-attack/118708/

**漏洞相关**

分析Windows内核驱动中的MSR读写原语漏洞，揭示通过未验证用户输入实现本地提权的技术细节

https://hackyboiz.github.io/2026/02/01/Libera/whs3-project-part3/En/

探讨Windows内核模式硬件强制堆栈保护（Intel CET Shadow-Stack）的技术实现和逆向工程分析

https://connormcgarr.github.io/km-shadow-stacks/

介绍如何手动创建Java反序列化gadget库，包括Java对象流分析和Golang利用技术

https://www.vulncheck.com/blog/making-java-gadgets

分析APT28组织利用CVE-2026-21509漏洞针对欧洲国家的攻击活动，涉及Office漏洞利用和地理围栏技术

https://blog.synapticsystems.de/apt28-geofencing-as-a-targeting-signal-cve-2026-21509/

**人工智能和安全**

OpenClaw开源AI代理的安全风险分析

https://1password.com/blog/its-openclaw

https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare

https://blog.virustotal.com/2026/02/from-automation-to-infection-part-ii.html

https://atum.li/cn/blog/openclaw\_risk/

OpenClaw代理的遥测与安全防护工具

https://github.com/knostic/openclaw-telemetry

https://github.com/knostic/openclaw-shield

分析假冒Clawdbot VS Code扩展程序如何安装ScreenConnect RAT恶意软件，伪装成AI编程助手进行攻击

https://www.aikido.dev/blog/fake-clawdbot-vscode-extension-malware

用于检测MDM部署中OpenClaw安装的检测脚本工具

https://github.com/knostic/openclaw-detect

分析openClaw加载的恶意Skills如何通过SKILL.md投毒窃取加密货币

https://opensourcemalware.com/blog/clawdbot-skills-ganked-your-crypto

AgenticRed：利用LLM元学习能力自动设计和优化红队系统的AI安全项目

https://github.com/yuanjiayiy/AgenticRed

腾讯玄武实验室发布AI网络爬虫安全白皮书，分析服务端浏览器在AI系统中的安全风险并提出防御框架

https://xlab.tencent.com/cn/2026/02/02/ai-browser-crawler-whitepaper/

研究揭示视觉提示注入攻击可劫持自动驾驶汽车和无人机，通过环境中的文本指令误导AI决策，攻击成功率高达95.5%

https://www.cysecurity.news/2026/02/visual-prompt-injection-attacks-can.html

Trail of Bits开发的Claude Code安全沙箱开发容器，用于安全审计和不受信任代码审查

https://github.com/trailofbits/claude-code-devcontainer

MoltThreats：面向AI代理的威胁情报平台，通过AI代理检测威胁并报告，由安全专家审核后发布防护信息

https://promptintel.novahunting.ai/molt

Anitigravity+Burp Suite的漏洞挖掘

https://github.com/momika233/Burp\_Suite-Antigravity\_AI-Bug\_Bounty\_Hunter

AI-System-Prompts：包含XBot高级AI网络安全代理系统提示词，用于自动化渗透测试和安全评估

https://github.com/xalgord/AI-System-Prompts

探讨LLM发现0-day漏洞的风险与防御

https://red.anthropic.com/2026/zero-days/

Julius：开源LLM服务指纹识别，帮助识别和分类不同的大语言模型服务

https://www.praetorian.com/blog/introducing-julius-open-source-llm-service-fingerprinting/

提出一种实用的扫描器，用于检测因果语言模型中的后门触发器，通过记忆提取技术识别中毒模型

https://www.arxiv.org/abs/2602.03085

介绍如何从零开始构建自定义LLM记忆层，实现自主记忆检索系统的逐步指南

https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/

**其他**

介绍如何在GitHub Action中运行Renovate依赖更新工具，避免使用易被盗用的个人访问令牌(PAT)，提升供应链安全

https://www.chainguard.dev/unchained/running-renovate-as-a-github-action

Wiz公司发布首个专注于SDLC基础设施的威胁框架SITF，用于可视化、映射和阻止生产SDLC基础设施攻击

https://www.wiz.io/blog/sitf-sdlc-threat-framework

Google威胁情报团队破坏全球最大的住宅代理网络IPIDEA，该网络被550多个威胁组织用于恶意活动

https://cloud.google.com/blog/topics/threat-intelligence/disrupting-largest-residential-proxy-network

TOTAL-REPLAY：重放攻击数据以测试安全检测规则，无需搭建完整攻击靶场

https://www.splunk.com/en\_us/blog/security/total-replay-splunk-attack-data-testing.html

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uZT6kWW1jCnM6QEblOyPtXuWB5CGzSJxv03JicKC0W5UdaEaoiaibXxxNJVdKrv9W8MwH3bbKALuKqy7krdibHh7bIR8mFHWw7gwsfMEBficeaCk/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/uZT6kWW1jCnK4Prsv2c4sAzsUsOLpr97a3ZAzJjSIJd34RwW9dEBR52yQmd6CI41dq4z87yzdl7xCzgrzD7Sgtj6aMI759xlY6YEejbw21c/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[每周蓝军技术推送（2026.1.24-1.30）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494671&idx=1&sn=ea47d2c5e0669f117aa653c5ee762b95&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.1.17-1.23）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494621&idx=1&sn=733a1bb43252aa69db431b21ced9d399&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.1.10-1.16）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494616&idx=1&sn=db8698bf035a665e476f8190873fe656&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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