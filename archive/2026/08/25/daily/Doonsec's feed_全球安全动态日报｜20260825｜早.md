---
title: 全球安全动态日报｜20260825｜早
url: https://mp.weixin.qq.com/s/ivuNOVVD86VCjCDl0l7hiA
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:00:57.458976
---

# 全球安全动态日报｜20260825｜早

# 全球安全动态日报｜20260825｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260825｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年8月24日共收录8条安全动态，内容涵盖恶意软件传播、账户接管漏洞与AI驱动攻击活动。

The Hacker News **8**  ·  HackerOne **0**

## The Hacker News

### 01 Weedhack 恶意软件通过虚假《我的世界》客户端和 SEO 投毒传播

**公开时间：**2026年08月24日 00:00

AI 解读

研究人员发现，名为Weedhack的恶意软件仍通过伪装成Minecraft客户端的仿冒网站传播，攻击者利用SEO投毒、YouTube及Discord、Reddit等渠道引流，并借助文件托管服务、GitHub及合法的Minecraft工具平台分发JAR文件。仿冒站点复制真实项目的品牌、功能说明、安装指南和开发者信息，部分甚至在搜索结果中压过官方来源。McAfee Labs称已拦截逾6,300次恶意网站访问，49.6%的恶意链接来自Discord。该攻击通过多阶段流程部署JAR载荷，可收集系统信息、设置Microsoft Defender排除项并窃取受害主机敏感数据。

原文：https://thehackernews.com/2026/08/weedhack-malware-spreads-via-fake.html

### 02 ⚡ 本周回顾：AI驱动的PLC攻击、GitLab攻击、Stripe密钥泄露及其他

**公开时间：**2026年08月24日 00:00

AI 解读

本周安全动态显示，攻击者正将合法工具、身份认证流程和开源依赖转化为攻击入口，并借助人工智能降低利用门槛。美国政府称，针对互联网暴露的西门子S7系列PLC的AI辅助攻击已构成现实威胁，可能影响关键基础设施运行；GitLab高危代码注入漏洞在披露数日内遭利用。另有14个木马化npm包投递RedC2 4.0后门，研究人员展示了利用过期Visa卡进行非接触支付的“Zombie Card”技术，以及Cloudflare Workers远程Spectre泄露JWT。疑似俄罗斯团伙滥用认证流程和 captive portal 窃取凭据，Cl0p则利用Windchill漏洞部署定制Web Shell并开展勒索。

原文：https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html

### 03 Operation QUICSILVER（行动代号“速银”）针对缅甸政府及IT部门，植入QUICAgent后门

**公开时间：**2026年08月24日 00:00

AI 解读

Seqrite Labs披露“QUICSILVER”网络间谍行动，首次观察于2026年4月，疑似中等置信度关联中\*背景行为者，目标为缅甸政府和信息技术部门。攻击者以节日安排或缅甸语毕业典礼邀请为诱饵，通过VHD中的伪装PDF快捷方式启动微软签名的ftp.exe，重组隐藏文件中的载荷并部署Go编写的QUICAgent后门。该后门利用延迟和哈希运算规避沙箱，经Cloudflare Workers动态获取地址，使用QUIC/UDP 443与C2通信，可执行命令、传输文件、浏览目录及调整信标间隔，并通过启动项实现持久化。

原文：https://thehackernews.com/2026/08/operation-quicsilver-targets-myanmar.html

### 04 Keycloak 严重密码重置漏洞可能允许未认证攻击者接管任意账户

**公开时间：**2026年08月24日 00:00

AI 解读

红帽和Keycloak项目发布了补丁修复关键漏洞CVE-2026-18963，该漏洞评分为9.1（CVSS），属于CWE-640弱密码恢复机制，允许未认证远程攻击者无需用户交互，通过不正确的重置凭据身份验证流程状态验证，直接进入密码更新阶段，强制重置任意用户账户密码，实现完全接管包括管理账户。攻击者发送特殊请求至重置凭据端点即可触发，无需邮箱操作令牌。用\*应升\*至上游Keycloak 26.7.2或Red Hat构建26.4.15及26.6.6等版本。无已知被利用证据。

原文：https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html

### 05 交付的 AI 代码多到无法确保安全？看看如何控制修复债务

**公开时间：**2026年08月24日 00:00

AI 解读

文章指出，AI编程工具虽提升开发速度，但会快速引入开源组件，使安全团队难以同步评估漏洞、许可、维护与归属，形成持续积累的修复债务（remediation debt）。随着AI工具更自主，该缺口可能扩大。ActiveState对技术、金融、医疗、制造及政府领域300名安全与工程负责人展开调查，研究团队如何应对AI驱动的开源风险、修复计划困境及债务与审计失败、违规频率和生产力损失的关系。网络研讨会基于数据解读这些发现，供企业对照自身项目，并分析有效的治理模式及可能适得其反的做法。

原文：https://thehackernews.com/2026/08/shipping-more-ai-code-than-you-can.html

### 06 WordlistLoader 利用 ClickFix 投递 Amatera，SynkLoader 网络钓取 Windows 密码

**公开时间：**2026年08月24日 00:00

AI 解读

研究人员披露了WordlistLoader和SynkLoader两种恶意软件。WordlistLoader被用于ClearFake的ClickFix假验证码活动，通过受入侵网站、区块链EtherHiding及远程WebDAV等方式投递，重构并加载Amatera窃取器；其以英文单词或UUID编码保存Shellcode，并利用硬件断点规避ETW。SynkLoader则通过伪装成IT服务台的Microsoft Teams钓鱼邮件诱导安装伪装成清理工具的MSI，随后加载多个模块，可收集系统信息、建立持久化、伪造Windows锁屏窃取密码，并提供远程命令、桌面控制和流量转发能力。两者可能用于投递后续载荷或向勒索软件团伙出售访问权限。

原文：https://thehackernews.com/2026/08/wordlistloader-delivers-amatera-via.html

### 07 不成比例的阴影：为什么5%的人工智能用户是您最大的安全风险

**公开时间：**2026年08月24日 00:00

AI 解读

Akamai《2026企业AI使用风险报告》基于实际使用与遥测数据称，企业AI使用最频繁的前5%用户与模型互动频率约为后50%员工的12倍，平均对话也由约5次增至18次以上，AI因而嵌入关键业务并形成集中的“影子AI”风险。47.11%的企业AI对话通过个人身份进行，14.4%使用企业邮箱注册的个人免费订阅，可能造成数据可见性缺口及提示内容被用于公开模型训练。员工还在使用未经管理的工具、SaaS及浏览器或IDE扩展；17.7%的中型企业员工使用此类扩展，其中近75%申请高危或关键权限，16.31%含已知CVE。报告指出，恶意配置文件、扩展和网页提示注入可诱导AI助手生成易受攻击代码、窃取密钥或会话令牌，并访问本地文件，扩大数据泄露和自动化攻击面。

原文：https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users.html

### 08 UAT-10147 利用 AI 扩大服务器攻击规模，部署具备 EDR 绕过能力和 Linux Rootkit 的 SPECTRE

**公开时间：**2026年08月24日 00:00

AI 解读

研究人员披露了中文网络犯罪组织UAT-10147的活动：该组织面向全球教育、媒体、科技和游戏行业的Windows及Linux Web服务器，主要目标位于巴西、玻利维亚、中\*、加拿大和越南，并使用约17万条URL开展规模化攻击。其利用公开漏洞取得远程代码执行权限，结合Metasploit、PentestGPT、DeepAudit等开源或AI工具自动化侦察、漏洞利用、后渗透和持久化，在Windows上部署Quasar RAT、Gh0stCringe、BadIIS及跨平台后门SPECTRE，在Linux上通过已知提权漏洞获取root权限并部署Noodle RAT、SPECTRE和Meterpreter。攻击还涉及配置Microsoft Defender排除、伪装计划任务、WebShell及通过合法云配置服务转移数据，以混入正常管理流量。

原文：https://thehackernews.com/2026/08/uat-10147-uses-ai-to-scale-server.html

## HackerOne

昨日暂无符合标准的漏洞发布

![一个不正经的黑客 · 全球安全动态与知识分享](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0wxk6alKwgl2znYoglw9fzyQU1dNd3QicIdQ2gekg7VXOz7LPmL1Kl2dpO5I60zgwgGuO6fVrTAo2PpLibVdWOo4OZYc7FQ4W7Q/640?from=appmsg)

继续阅读

点击文末「阅读原文」，可前往网站主页查看完整资讯与 AI 解读。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoPgcybP7CdwQuthRKXPkpYnwaQcOnXgEZT4r1rNWBU8D1I9HAMGWEWricXrOJ2UZNjo3YghpiaevyQ/0?wx_fmt=png)

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