---
title: 每周蓝军技术推送（2026.2.7-2026.2.27）
url: https://mp.weixin.qq.com/s/8YiqciP6G4gnPi_8qxbw8g
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:44.363990
---

# 每周蓝军技术推送（2026.2.7-2026.2.27）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbD5z6C0g2NAp2OicEl3fdbRrPUY2MuWIcreXMC0tGBdfWBviaqDPPyN63iawoWIujD6l1Fx5keMUib4w/0?wx_fmt=jpeg)

# 每周蓝军技术推送（2026.2.7-2026.2.27）

原创

天元实验室
天元实验室

M01N Team

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/uZT6kWW1jCkjwTZiaTbxy5fyYZlWFGZTnibEeepEiceqXKXt8B2jIk0Re0R60z9xPZ57ic13fH17NericGsL3uLicRk8xyaYnNf1v6WwXAClD80Fg/640?wx_fmt=png&from=appmsg)

**WEB安全**

PortSwigger发布的2025年十大Web黑客技术，包含新的错误注入和SSTI利用技术

https://portswigger.net/research/top-10-web-hacking-techniques-of-2025

phpggc：PHP反序列化漏洞利用工具库

https://github.com/ambionics/phpggc

**内网渗透**

关于检测Kerberos协议异常活动的研究，帮助红队评估其技术在环境中的隐蔽性

https://blog.nviso.eu/2026/02/12/capture-the-kerberos-flag-detecting-kerberos-anomalies/

**终端对抗**

lnk-it-up：Windows LNK文件欺骗技术分析及工具套件

https://www.wietzebeukema.nl/blog/trust-me-im-a-shortcut

https://github.com/wietze/lnk-it-up

LnkParse3：用于解析Windows快捷方式文件的工具，可用于安全分析和取证

https://github.com/Matmaus/LnkParse3

reflektor：Go语言库和CLI工具，用于从字节加载共享库并调用导出函数

https://github.com/sliverarmory/reflektor

Adaptix C2的Crystal Palace RDLL加载器，包含Ekko睡眠混淆、PICO IAT钩子和按节权限恢复功能

https://github.com/MaorSabag/Adaptix-StealthPalace

CobaltStrike-Linux-Beacon：用于创建自定义Cobalt Strike Beacon的PoC植入程序

https://github.com/EricEsquivel/CobaltStrike-Linux-Beacon

BusterCall：绕过HVCI修改只读代码页并调用链式内核函数

https://github.com/zer0condition/BusterCall

Rex：用Rust编写的红队工具包，包含各种渗透测试和红队操作工具

https://github.com/rex-rs/rex

通过内核级rootkit绕过eBPF安全工具的技术实现

https://matheuzsecurity.github.io/hacking/ebpf-security-tools-hacking/

利用Azure Blob Storage白名单创建Mythic C2配置文件

https://specterops.io/blog/2026/01/30/weaponizing-whitelists-an-azure-blob-storage-mythic-c2-profile

**漏洞相关**

CVE-2025-61969：AMD uProf软件权限分配不当漏洞分析及POC

https://bad-jubies.github.io/amduprof-1

https://github.com/Bad-Jubies/Exploits/tree/main/AMD\_uProf

Munge认证守护进程存在20年的缓冲区溢出漏洞，可导致本地提权并泄露集群密钥

https://blog.lexfo.fr/munge-heap-buffer-overflow.html

Google介绍了一种检测eBPF漏洞的新方法

https://security.googleblog.com/2023/05/introducing-new-way-to-buzz-for-ebpf.html

介绍如何利用本地大语言模型辅助逆向工程，分析CLFS中的use-after-free漏洞

https://clearbluejar.github.io/posts/how-llms-feed-your-re-habit-following-the-uaf-trail-in-clfs/

**人工智能和安全**

Anthropic发布Claude Opus 4.6模型，展示AI在发现高危漏洞方面的能力提升，探讨LLM发现0-day漏洞的风险与防御

https://red.anthropic.com/2026/zero-days/

Anthropic发布Claude Code Security AI代码审计功能

https://claude.com/solutions/claude-code-security

vulnerability-spoiler-alert-action：通过LLM工作流发现负天数漏洞

https://spaceraccoon.dev/discovering-negative-days-llm-workflows/

OpenClaw安全工程师速查表，包含大量实用工具链接、命令、加固建议和相关参考资料

https://semgrep.dev/blog/2026/openclaw-security-engineers-cheat-sheet

ClawShield：OpenClaw安全围栏工具，覆盖网关暴露、恶意群组、Skills投毒防护

https://github.com/kappa9999/ClawShield

clawsec：通过漂移检测、实时安全建议、自动审计和技能完整性验证来保护OpenClaw

https://github.com/prompt-security/clawsec

clawdstrike：OpenClaw群集检测与响应平台和安全基础设施

https://github.com/backbay-labs/clawdstrike

ironclaw：基于Rust开发的类OpenClaw应用，专注隐私与安全

https://github.com/nearai/ironclaw

介绍AI代理Skills文件中隐藏Unicode指令的安全风险及检测方法

https://embracethered.com/blog/posts/2026/scary-agent-skills/

Nova-Proximity：基于NOVA的MCP和Agent Skills安全扫描器

https://github.com/Nova-Hunting/nova-proximity

PassLLM：基于PyTorch实现的密码猜测AI工具，利用PII和LoRA微调技术，在消费级硬件上性能超越现有工具45%以上

https://github.com/Tzohar/PassLLM

cua-kit：用于攻击计算机使用代理（CUA）的工具套件

https://github.com/preludeorg/cua-kit

探讨AI智能体Rufio如何基于Scattered Spider攻击技术博客，自主执行AWS云环境中的紫队演练操作

https://permiso.io/blog/can-an-ai-agent-run-a-purple-team-exercise

Redamon：AI代理编排器，通过信息收集、漏洞利用和后渗透三阶段自动化攻击流程，并将成功利用记录到图数据库中

https://github.com/samugit83/redamon

SCAM：1Password发布AI代理安全基准测试，通过安全Skills文件训练AI代理避免网络诈骗

https://1password.com/blog/ai-agent-security-benchmark

https://github.com/1Password/SCAM

AI Cyber Model Arena：用于评估网络安全领域AI代理的真实世界基准测试平台

https://www.wiz.io/blog/introducing-ai-cyber-model-arena-a-real-world-benchmark-for-ai-agents-in-cybersec

AI辅助的云入侵攻击在8分钟内获取管理员权限的技术演示

https://www.sysdig.com/blog/ai-assisted-cloud-intrusion-achieves-admin-access-in-8-minutes

**其他**

ElephantPoint：使用SharePoint令牌搜索和下载文件的C#模块

https://github.com/nettitude/ElephantPoint

一个用于检测文件中不可见Unicode字符的工具，旨在识别潜在的ASCII走私、隐藏数据编码和可疑Unicode使用模式

https://github.com/wunderwuzzi23/aid

sandboxec：基于Landlock构建的轻量级Linux命令沙箱工具

https://github.com/dwisiswant0/sandboxec

aznet：使用Azure存储服务作为传输层实现标准net.Conn接口

https://github.com/Atsika/aznet

labca：一个基于Let's Encrypt ACME实现的私有证书颁发机构，用于实验室内部使用

https://github.com/hakwerk/labca

pmg：包管理器保护程序，适用npm、pip等，提供包安装前审计

https://github.com/safedep/pmg

safe-chain：包管理器保护程序，适用npm、pip等，提供包安装前审计

https://github.com/AikidoSec/safe-chain

GitHunt：在GitHub上追踪供应链攻击活动，包括Web应用、CLI工具和可疑活动识别工具

https://speakerdeck.com/ramimac/the-forensic-trail-on-github-hunting-for-supply-chain-activity

开发者笔记本电脑作为供应链攻击中最脆弱的目标，拥有特权访问但缺乏监控

https://labs.boostsecurity.io/articles/unveiling-bagel-why-your-developers-laptop-is-the-softest-target-in-your-supply-chain

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uZT6kWW1jCmCYib1ADqrOs3cv5AtdyGv0qKvtWxZ76XCN669wJ38Iw3sQ9sQ6JF0vib6JhZiblia59s0II85B65cic6qQfHKPjPiasBfRZ5wibg7U0/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jClIxQ1Qso87dj85zibgwgLplkluO224sX3fkIe1fVDZDWZrOiaiblztPyYOSibuAZEVQ3Dr4ZEa7tsicnsLmwt1ujIo4ibT2H7BhZtwQ/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[每周蓝军技术推送（2026.1.31-2026.2.6）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494679&idx=1&sn=d41cda123693d36a363a9dc35c43bdb4&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.1.24-2026.1.30）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494671&idx=1&sn=ea47d2c5e0669f117aa653c5ee762b95&scene=21#wechat_redirect)

[每周蓝军技术推送（2026.1.17-2026.1.23）](https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494621&idx=1&sn=733a1bb43252aa69db431b21ced9d399&scene=21#wechat_redirect)

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