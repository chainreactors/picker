---
title: 每周蓝军技术推送（2026.4.4-2026.4.10）
url: https://mp.weixin.qq.com/s/xKG1g95kRXu3DToH3KQEpg
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:17:52.892197
---

# 每周蓝军技术推送（2026.4.4-2026.4.10）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbD5z6C0g2NAp2OicEl3fdbRrPUY2MuWIcreXMC0tGBdfWBviaqDPPyN63iawoWIujD6l1Fx5keMUib4w/0?wx_fmt=jpeg)

# 每周蓝军技术推送（2026.4.4-2026.4.10）

原创

天元实验室
天元实验室

M01N Team

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jCkickNLlacmH5o0psfGK1MVLoQ4GBFKWN1MTHZgO7ichEQql5AAsicaH68Bia0QJwftcsr0sJF41lz0ua7S0Yy89JmXfNmt8Y2VPe0/640?wx_fmt=png&from=appmsg)

**内网渗透**

使用mitmproxy设置透明代理环境，包括Linux网络命名空间、WiFi AP创建和Android系统证书安装

https://www.synacktiv.com/en/publications/mitmproxy-for-fun-and-profit-interception-and-analysis-of-application-traffic

Making CloudFlare Workers Work for Red Teams：利用CloudFlare Workers进行红队操作，包括多轮攻击、载荷轮换及检测对抗技术

https://blog.zsec.uk/capd

发布 supabase-exposure-check 脚本，扫描网站暴露的 Supabase JWT 令牌并枚举可访问数据库表

https://bour.ch/how-rep-helped-me-identify-a-critical-supabase-jwt-exposure

OWASP Top 10 2025版更新，基于280万应用数据，SSRF归入访问控制类

https://owasp.org/Top10/2025/0x00\_2025-Introduction

**终端对抗**

FancyBear开发模块化多平台利用工具包，受害者仅打开恶意邮件即可窃取凭证、绕过2FA、外传邮件并建立持久转发规则

https://ctrlaltintel.com/threat%20research/FancyBear

How Kernel Rootkits Blind Observability Tools：攻击者控制内核后，可操纵eBPF工具依赖的内核到用户空间数据传递机制，使安全监控失效

https://matheuzsecurity.github.io/hacking/ebpf-security-tools-hacking

威胁组织扩大滥用Visual Studio Code，载荷包含AI辅助生成的代码特征

https://www.jamf.com/blog/threat-actors-expand-abuse-of-visual-studio-code

GachiLoader 变种使用"Vectored Overloading"技术，欺骗Windows加载器从内存加载恶意PE而非合法DLL

https://research.checkpoint.com/2025/gachiloader-node-js-malware-with-api-tracing

Keeping Secrets Out of Logs：防止密钥泄露到日志的整体策略，包括建立明确预期、理解数据流、保护关键点、实施纵深防御和规划应急响应

https://allan.reyes.sh/posts/keeping-secrets-out-of-logs

MMC MSC EvilTwin 本地提权漏洞，利用恶意 .msc 文件执行任意代码，影响 Win10/11/Server 2016-2025

https://www.exploit-db.com/exploits/52498

**漏洞相关**

Cortex XDR Live Terminal主机名验证绕过漏洞，攻击者可劫持跨租户会话或构建自定义C2服务器

https://labs.infoguard.ch/posts/abusing\_cortex\_xdr\_live\_response\_as\_c2

研究人员泄露Windows提权零日漏洞BlueHammer，攻击者可获取SYSTEM权限，微软尚未发布补丁

https://www.bleepingcomputer.com/news/security/disgruntled-researcher-leaks-bluehammer-windows-zero-day-exploit

攻击者利用Cline漏洞发布新版CLI，在生命周期脚本中植入npm install -g openclaw@latest

https://adnanthekhan.com/posts/clinejection

Postman实施五级成熟度模型管理第三方依赖漏洞，包括仓库扫描、PR扫描/阻断、客户端扫描/阻断

https://blog.postman.com/engineering/product-security-scorecards-coupling-security-issues-with-preventative-controls-to-drive-security-maturity

分析AWS云环境中Lambda、EC2、IAM/STS等服务的配置错误导致的初始访问向量

https://www.paloaltonetworks.com/blog/cloud-security/aws-initial-access-cloud-perimeter-security

React Server 19.2.0 存在远程代码执行漏洞，影响版本 19.0.0 至 19.2.0，CVE-2025-55182

https://www.exploit-db.com/exploits/52506

RomM <4.4.1 存在文件上传 XSS 与 CSRF 令牌复用链，可绕过 SameSite 防护实现管理员账户接管

https://www.exploit-db.com/exploits/52505

Jumbo Website Manager v1.3.7 存在远程代码执行漏洞，Exploit-DB 已发布 PoC 代码

https://www.exploit-db.com/exploits/52504

ZSH 5.9 本地权限提升漏洞，Exploit-DB 收录 PoC 代码

https://www.exploit-db.com/exploits/52503

FortiWeb 8.0.2 存在认证绕过+路径遍历+任意文件上传漏洞链，可导致远程代码执行

https://www.exploit-db.com/exploits/52502

7-Zip 24.00 存在目录遍历漏洞，恶意ZIP文件可导致RCE，影响Windows系统

https://www.exploit-db.com/exploits/52501

Xibo CMS 3.3.4 存在Zip Slip路径遍历漏洞，攻击者通过恶意ZIP文件实现任意文件上传和远程代码执行

https://www.exploit-db.com/exploits/52500

SQLite 3.50.1 winsqlite3.dll 堆溢出漏洞，影响 Windows Server 的 Active Directory、组策略等组件

https://www.exploit-db.com/exploits/52499

Horilla v1.3 存在认证RCE漏洞CVE-2025-48868，PoC脚本通过创建项目实现反向Shell

https://www.exploit-db.com/exploits/52497

**人工智能和安全**

Claude Mythos Preview 模型可自主编写浏览器漏洞利用链，实现沙箱逃逸和本地提权，还能逆向闭源软件并利用 N-day 漏洞

https://red.anthropic.com/2026/mythos-preview

https://www.anthropic.com/glasswing

AI 编码代理将改变漏洞研究经济，通过指向源码树即可发现零日漏洞，从 Chrome 到数据库和打印机等目标

https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked

AWS Security Agent采用多智能体架构实现自动化渗透测试，支持DVWA扫描

https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/

分析LLM在漏洞研究中的应用，探讨其通过组合已知原语发现新型漏洞的能力

https://devansh.bearblog.dev/on-llms-and-vuln-research

提出将AI Agent技能作为新型软件包管理，需建立安全治理体系

https://jfrog.com/blog/agent-skills-new-ai-packages

IronCurtain通过MCP代理和策略引擎实现AI助手安全，支持V8隔离TypeScript和无网络容器两种沙箱模式

https://www.provos.org/p/ironcurtain-secure-personal-assistant

初创公司AI代理被黑导致麦肯锡敏感数据泄露，暴露大量机密信息

https://www.thestack.technology/mckinsey-ai-agent-hacked-lilli

AI代理发布恶意诽谤文章，展示了自主恶意AI对声誉系统的威胁

https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me

开源GitHub Action和实时仪表板，使用LLM工作流发现负日漏洞

https://spaceraccoon.dev/discovering-negative-days-llm-workflows

Coding Agents. The Insider Threat You Installed Yourself：工具集成NOVA框架对抗提示检测能力

https://blog.securitybreak.io/coding-agents-the-insider-threat-you-installed-yourself-35644a1d5409

Slack 分享其安全调查代理架构，包含 Hub、Workers 和 Dashboard，代理能识别非调查重点的凭据泄露

https://slack.engineering/streamlining-security-investigations-with-agents

Promptfoo测试332个对抗场景，发现AI代理在15轮对话后失去安全训练约束

https://www.promptfoo.dev/blog/claude-code-attack

Parsia 提出 AI-Native SAST 演进路径

https://parsiya.net/blog/wtf-is-ai-native-sast

**其他**

分析SHA pinning在GitHub Actions和CI/CD中的局限性，讨论伪造提交的供应链攻击风险

https://www.vaines.org/posts/2026-03-24-the-comforting-lie-of-sha-pinning

通过追踪云日志中独特告警种类与日均告警量，实现主动威胁狩猎

https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging

Plaid 将组织特定安全基线编码为 Semgrep 规则，实现自动修复漏洞和统一漏洞管理，通过软失败模式达到 95%+ 仓库覆盖率

https://plaid.com/blog/security-as-a-platform

删除IAM用户前未更新KMS密钥策略导致权限问题

https://sirantd.com/how-i-overlooked-the-problem-and-shot-myself-in-the-foot-06841414e1de

![](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jCnEMuZ8QIiamuby5ctOakGcriaGSPFic7FnjglYwNR22U4qsj6Pty7ibmJbYia1R2Ym18yj5hQJvq69EZK6gzXPRpUjmurWd8WNw958/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/uZT6kWW1jClp6LPKGIY9OlUe9J0DPfv5jOpic4oQQSPwjuDNaARQUrGOicof0h94Yo4qiaCZ2QPmY9Faj6ueA2Mdia6pYSAHDVEJZQJpzP0v7hU/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[每周蓝军技术推送（2026.3.28-2026.4.3）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494916&idx=1&sn=b01106658b570c0d850fb0a21ccbb036&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.3.21-2026.3.27）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494891&idx=2&sn=9fea43e1c6cc95791e2f62f236fdb987&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.3.14-2026.3.20）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494762&idx=1&sn=ca8490675064f1b8b18de2a02a4134b5&scene=21#wechat_redirect)

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