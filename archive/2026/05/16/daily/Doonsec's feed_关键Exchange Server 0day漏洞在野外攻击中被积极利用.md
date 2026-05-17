---
title: 关键Exchange Server 0day漏洞在野外攻击中被积极利用
url: https://mp.weixin.qq.com/s/9pUyo4DPM4zPlpSml9Hx-w
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:03.980124
---

# 关键Exchange Server 0day漏洞在野外攻击中被积极利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyISibXZiaNMkmOcktacM4uNJvOU7V6B7aLZ8iaPZXfW6GoSYg77HFK9JQuIibDJrR52C3cV0niaR2ucZJRhjgJRFtwnomFNcGCb0C68/0?wx_fmt=jpeg)

# 关键Exchange Server 0day漏洞在野外攻击中被积极利用

会杀毒的单反狗
会杀毒的单反狗

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

微软发布一条紧急安全警报，涉及Exchange服务器中发现的一个新漏洞，该漏洞正在野外被利用。此漏洞编号为CVE-2026-42897，这是一个严重级别欺骗漏洞，CVSS 3.1严重性评分为8.1，直接影响本地电子邮件基础设施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyKjlxemZRKI9rQ1tX8W0ezCvWB3xzX7sacZEM95icC1xb05Uf91tRibzg4FRfiaH2YUzN4ZpDHBjLuibvcFm11ElDgSphfrwwnHJx0/640?wx_fmt=png&from=appmsg)

在永久补丁最终发布之前，攻击者正在积极利用这一基于网络的漏洞来破坏组织系统。网络安全分析师已确认，该漏洞专门针对微软 Exchange Outlook Web Access 服务。

由于该漏洞已被用于正在进行的攻击活动中，因此敦促系统管理员立即采取临时防御措施。

安全风险完全集中在本地部署上，这意味着使用基于云的 Microsoft Exchange Online 的组织不受此威胁的影响。

该漏洞利用了网页生成过程中输入处理不当的问题，这是一个常见的跨站脚本攻击漏洞。未经授权的攻击者可以通过向目标用户直接发送精心构造的电子邮件来利用此漏洞。

如果收件人在 Outlook Web Access 中打开恶意邮件并满足某些交互条件，则有效载荷允许任意 JavaScript 在用户的浏览器中执行。

安全研究人员指出，这种执行路径可以有效地实现网络级欺骗，而无需事先获得管理权限。

该漏洞影响 Exchange Server 2016、Exchange Server 2019 和 Exchange Server 订阅版的所有更新级别。

攻击复杂度低，加上基于网络的执行模型，使得该攻击成为威胁组织劫持用户会话或操纵本地浏览器数据的高效工具。

永久性安全更新正在开发和测试中，微软已通过自动化的 Exchange 紧急缓解服务部署了临时安全措施。对于启用此默认服务的组织，系统会自动应用标识为 M2.1.x 的特定缓解措施来保护易受攻击的环境。

在断开连接或物理隔离的网络中运行的管理员必须通过提升权限的管理 shell 手动下载并执行最新的 Exchange 本地缓解工具脚本，才能实现这种必要的保护。

实施这项紧急缓解措施会带来一些轻微的运行副作用，IT 团队必须对此进行管理。微软文档显示，Outlook Web Access 的打印日历功能可能无法正常工作，用户需要依赖桌面客户端或手动截屏。

此外，内嵌图像可能无法在阅读窗格中正确显示，因此需要采取一些变通方法，例如将图像作为直接附件发送。

尽管存在这些表面和功能上的干扰，安全专家仍强烈建议各组织采取缓解措施。

微软软件工程师正在积极完善符合质量保证标准的永久性官方修复方案。安全更新发布后，将面向 Exchange Server 订阅版用户公开提供。

只有积极参与第二阶段 Exchange Server 扩展安全更新计划的客户才能获得 Exchange 2016 和 2019 等旧版本的永久更新。

强烈建议依赖旧版累积更新的组织立即升级其基础架构，以确保与最终补丁部署时兼容。

微软官方安全公告：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42897

新闻链接：

https://cybersecuritynews.com/microsoft-exchange-server-vulnerability-exploited/

![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg)

**今日安全资讯速递**

**APT事件**

Advanced Persistent Threat

1. 黑客利用 OrBit Rootkit 从 Linux 系统中窃取 SSH 和 sudo 凭据

一个名为 OrBit 的rootkit多年来一直默默针对 Linux 系统，窃取登录凭据并在受感染的设备中深度隐藏，而不会触发大多数安全工具。

🔗https://cybersecuritynews.com/hackers-use-orbit-rootkit-to-harvest-ssh/

2.俄黑客组织Turla 将 Kazuar 后门转变为模块化 P2P 木马网络以实现持久访问

俄黑客组织 Turla 将其定制的后门 Kazuar 改造成了一个模块化的点对点 (P2P) 僵尸网络，该网络旨在隐蔽地持续访问受感染的主机。

🔗https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html

3. 黑客组织对一家全球制造商的印度分支机构部署新型 TencShell 恶意软件

研究人员发现了一种未记录的恶意软件植入程序，威胁组织针对一家全球制造商的印度分支机构，利用了一个开源进攻性工具包。

🔗https://www.infosecurity-magazine.com/news/china-hackers-tencshell-malware/

4. Ghostwriter组织恢复对乌克兰政府目标的袭击

ESET发现针对乌克兰政府机构的新Ghostwriter（又名FrostyNeighbor）活动，该活动自2026年3月以来持续进行。

🔗https://securityaffairs.com/192196/apt/ghostwriter-group-resumes-attacks-on-ukrainian-government-targets.html

**一般威胁事件**

General Threat Incidents

1. OpenAI 在 TanStack 供应链攻击中遭到入侵

OpenAI披露，其广泛使用的JavaScript库框架TanStack遭到供应链攻击，导致两名员工的设备被入侵。此次事件导致OpenAI代码库中的凭证材料被盗。

🔗https://www.cybermaterial.com/p/openai-compromised-in-tanstack-supply

2. TeamPCP黑客利用CI/CD管道窃取云端凭证

TeamPCP威胁组织积极针对现代软件供应链攻击，大规模窃取敏感的开发者云凭证。TeamPCP的核心策略简单但非常有效：不是攻击终端用户系统，而是入侵受信任的构建和发布流程，将恶意代码注入CI/CD管道。

🔗https://gbhackers.com/teampcp-hackers-exploit-ci-cd/

3. Gunra勒索软件从基于Conti的Locker迁移后，扩大了攻击范围

Gunra勒索软件迅速从一种新威胁发展成为严重的全球性问题，在不到一年的时间里攻击了数十家组织。其背后的团体不仅加密数据，还开展类似商业的运作，出售访问权限、泄露被盗文件，并招募合作伙伴传播其恶意软件。

🔗https://cybersecuritynews.com/gunra-ransomware-expands-raas-operations/

4. 黑客利用 PyInstaller 和 AMSI 补丁传播 XWorm RAT v7.4

黑客将 XWorm 恶意软件隐藏在 PyInstaller 文件中，以绕过 Windows 安全机制、窃取数据并通过广告远程控制设备。

🔗https://hackread.com/hackers-pyinstaller-amsi-patching-xworm-rat-v7-4/

5. 微软警告攻击者使用受信任的 HPE 操作代理进行无文件攻击

安全研究人员发现一起入侵事件揭示了一场精心策划的攻击活动，该活动利用合法的企业管理工具作为武器。攻击者通过被入侵的第三方 IT 服务提供商获得访问权限，然后使用已经获得批准并正在运行的工具悄悄地在受害者的环境中移动。

🔗https://cybersecuritynews.com/microsoft-warns-of-attackers-using-trusted-hpe-operations-agent/

6. 黑客利用 OAuth 设备流程窃取 Microsoft 365 令牌

黑客正在迅速将一项鲜为人知的微软身份验证功能武器化，以劫持企业账户，同时设备代码钓鱼攻击在威胁环境中激增。活动激增与犯罪工具包和钓鱼即服务（PhaaS）平台的公开发布密切相关，使得这一曾经冷门的技术变得广泛可用。

🔗https://gbhackers.com/hackers-exploit-oauth-device/

**漏洞事件**

Vulnerability Incidents

1. 关键 Next.js 漏洞泄露云凭证、API 密钥和管理面板

一个高严重性漏洞影响Next.js，可能对自托管的网络应用造成严重的数据泄露。攻者利用服务器端请求伪造（SSRF）漏洞，静默窃取云凭证、收集API密钥并访问敏感的内部管理面板。

🔗https://cybersecuritynews.com/next-js-vulnerability-exposes-credentials/

2. Palo Alto 防火墙遭0day漏洞攻击，允许以Root权限执行任意代码

Palo Alto Networks 防火墙中存在一个严重0day漏洞，据信是由国家支持的黑客积极利用，使未授权攻击者能够完全控制企业安全基础设施。该漏洞编号为 CVE-2026-0300，CVSS 评分为 9.3，属于严重级别，针对 PAN-OS 软件中的用户身份验证门户服务，并已被武器化……

🔗https://gbhackers.com/palo-alto-firewalls-hit-by-pan-os-zero-day/

2. 思科修补一个正在被积极利用的 SD-WAN 0day漏洞 (CVE-2026-20182)

CVE-2026-20182 漏洞影响Cisco Catalyst SD-WAN 控制器（Cisco Catalyst SD-WAN 解决方案的“大脑”）和 Cisco Catalyst SD-WAN 管理器（整个 SD-WAN 架构的管理平台），漏洞根源在于存在缺陷的对等身份验证机制，漏洞会影响本地部署和云部署，已被“高度复杂的威胁组织”作为0day武器利用。

🔗https://www.helpnetsecurity.com/2026/05/15/cisco-sd-wan-zero-day-cve-2026-20182/

3. 关键Exchange Server 0day漏洞在野外攻击中被积极利用

微软发布一条紧急安全警报，涉及Exchange服务器中发现的一个新漏洞，该漏洞正在野外被利用。此漏洞编号为CVE-2026-42897，这是一个严重级别欺骗漏洞，CVSS 3.1严重性评分为8.1，直接影响本地电子邮件基础设施。

🔗https://cybersecuritynews.com/microsoft-exchange-server-vulnerability-exploited/

4. Amazon Redshift JDBC 驱动程序漏洞允许远程代码执行攻击

亚马逊 Redshift JDBC 驱动程序中的一个关键漏洞使企业应用程序面临远程代码执行（RCE）的严重风险。攻击者只需操纵数据库连接 URL 就可以利用这个新披露的漏洞。这个隐藏的漏洞允许攻击者从内部劫持应用程序进程，可能导致敏感企业数据被未经授权的访问。

🔗https://cybersecuritynews.com/amazon-redshift-jdbc-driver-vulnerabilities/

5. PraisonAI 漏洞在公开后数小时内被积极利用

PraisonAI的一个高严重性漏洞在公开披露后不久就引起了安全研究人员的紧急关注。该漏洞被追踪为CVE-2026-44338，并在GitHub通告GHSA-6rmh-7xcm-cpxj中进行了记录，暴露了该平台旧版API服务器中的关键身份验证绕过问题，可能导致攻击者在无需认证的情况下执行AI工作流...

🔗https://gbhackers.com/praisonai-vulnerability-actively-exploited/

6. 四个 OpenClaw 漏洞允许数据窃取、权限提升和持久化

网络安全研究人员披露了OpenClaw中的一组四个安全漏洞，这些漏洞可以被利用以实现数据窃取、权限提升和持久化。

🔗https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html

7. VMware Fusion 漏洞允许攻击者提升权限至 Root

在VMware Fusion中发现了一个高严重性权限提升漏洞，VMware Fusion是博通公司流行的macOS虚拟化软件，该漏洞允许本地攻击者在受影响的系统上获得根级别访问权限。该漏洞被追踪为CVE-2026-41702，已私下报告给博通，并于2026年5月14日通过安全公告VMSA-2026-0003进行修补。该漏洞源于TOCTOU...

🔗https://cybersecuritynews.com/vmware-fusion-toctou-vulnerability/

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

军哥网络安全读报

**讲述普通人能听懂的安全故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

爱拍照的老李

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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