---
title: 存在22年的 BMC 漏洞使数千个数据中心面临攻击
url: https://mp.weixin.qq.com/s/_VrAlxmN-zEhUdtnr3jeZA
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T05:00:19.261478
---

# 存在22年的 BMC 漏洞使数千个数据中心面临攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PaFY6wibdwyLV9ianE7W8mupNZkTJBrwqX6XyojqLU6sfSzEjqA9H8lSKl49PA2h1lEaFZCyaroOwn82RAziaBdoVwx36DZWzBic0cMyX7X5riac/0?wx_fmt=jpeg)

# 存在22年的 BMC 漏洞使数千个数据中心面临攻击

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

超过2.4万个可通过互联网访问的服务器管理界面在登录前泄露了认证哈希值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyI5QLXH2W1s8MBh9eP66aH1rkBom7dTrP9SCUVHQJLuxXq6t9OLA6GrQvKmK2PN2Rg0rNicUicAB9hgt51wicsDBj5XqaeUNNsa5s/640?wx_fmt=jpeg&from=appmsg)

数据中心安全公司 Lava 报告称，由于基板管理控制器（BMC）管理处理器存在一个存在22年的漏洞，数千个数据中心面临被入侵的风险。

BMC 存在于大多数服务器平台中，即便操作系统无法正常运行，它也能支持服务器管理操作，且通常是数据中心中权限最高的控制点之一。

通过基板管理控制器（BMC），管理员可借助多种管理界面执行主机断电重启、固件更新、底层平台配置修改、读取硬件传感器等操作，这些管理界面包括带外智能平台管理接口（IPMI）协议、基于超文本传输协议安全（HTTPS）的红鱼（Redfish）管理应用程序接口（API）以及基于网页的管理界面。

“在许多实现中，这些接口共享同一个用户数据库。适用于IPMI的凭据也可能适用于Web界面或Redfish API。这一点很重要，因为IPMI身份验证过程可能会泄露信息，从而允许离线恢复密码。”Lava 指出。

据这家网络安全公司称，有近3.7万个暴露在公网的服务器管理接口运行着IPMI协议，其中超过2.4万个会在登录前泄露基于密码生成的认证哈希值。

核心问题是 CVE-2013-4786，这是 2004 年在 IPMI 2.0 认证协议中引入的一个漏洞。美国国家标准与技术研究院（NIST）的一份公告称，该漏洞允许攻击者通过“从基板管理控制器（BMC）的 RAKP 消息 2 响应中获取哈希消息认证码（HMAC）”来获取密码哈希并离线破解。

“在身份验证过程中，基板管理控制器（BMC）可以返回一个使用请求方已知的账户密码和会话值计算得出的 HMAC-SHA1 身份验证码。能够访问 UDP 623 端口的未身份验证远程方可以请求该响应，并离线测试猜测的密码。”Lava解释道。

攻击者可利用该安全缺陷恢复弱密码、重复使用的密码或默认密码，无需像重复进行在线登录尝试那样，为每个潜在密码候选发送新请求。

更糟糕的是，Lava 还发现，有 6240 台主机接受空用户名搭配弱密码的登录方式，其中 2340 台主机还存在名为 Admin 或 root 等的账户，这些账户使用的密码是公开密码字典中常见的弱密码。

据这家网络安全公司称，除了常见密码外，一些 BMC 还使用了受限且可预测的出厂默认密码格式。

“这一漏洞暴露了数据中心管理平面中一个更广泛的安全漏洞。基板管理控制器（BMC）掌控着关键基础设施，但其所受到的监控和保护往往远少于其管理的系统。再加上现代显卡破解技术以及可预测的出厂密码，这一漏洞可能会让单个暴露的基板管理控制器（BMC）成为整个管理网络中具有特权且难以被发现的入侵点。”Lava指出。

漏洞详情：

https://lavahq.io/research/bmc-exposure-alert

新闻链接：

https://www.securityweek.com/decades-old-bmc-vulnerability-exposes-thousands-of-data-centers-to-attacks/

![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg)

**今日安全资讯速递**

**APT事件**

Advanced Persistent Threat

1. 与 OctLurk 相关的黑客针对中东政府部署 BINDCLOAK 后门

发布了关于 BINDCLOAK 的两篇技术分析的第二部分，该后门此前未被记录，由一个与东亚有关联的威胁行为体 OctLurk 部署在中东的政府实体上。

🔗https://gbhackers.com/bindcloak-backdoor-deployed/

2. 黑客声称窃取了一份包含 13.5 万名英国警察联系人的目录

一个新的黑客组织声称从英国警方平台窃取了 13.5 万条记录，暴露了可能被用于网络钓鱼和冒充的联系方式。

🔗https://www.esecurityplanet.com/cybersecurity/news-uk-police-pnld-data-breach-exfilsquad-emea/

3. SharePoint漏洞被用于攻击瑞士联邦信息技术机构

瑞士联邦信息技术与通信局（简称 BIT 或 FOITT）披露，未知攻击者已入侵其本地 SharePoint 服务器上约 200 个账户。该局表示，未知攻击者疑似利用了微软 SharePoint 软件中的漏洞。

🔗https://securityaffairs.com/196625/hacking/sharepoint-flaws-used-to-hack-switzerlands-federal-it-agency.html

**一般威胁事件**

General Threat Incidents

1.SonicWall零日漏洞被INC勒索软件积极利用

Resecurity 研究报告称，INC 勒索软件已成为利用近期披露的 SonicWall 安全移动访问（SMA）1000 漏洞的主要威胁组织。该组织自8月初以来加快了行动速度，目标涵盖美国、澳大利亚、阿联酋、哥伦比亚、瑞士等国的机构。

🔗https://securityaffairs.com/196607/malware/inc-ransomware-is-calling-victims-pressure-tactics-post-sonicwall-zero-day-exploit.html

2. 列支敦士登公司和基金会登记册数据泄露，31,000 条记录受损

一次网络攻击导致列支敦士登与公司、基金会和信托相关的受益所有人登记册中约 31,000 人的数据被泄露。

🔗https://securityaffairs.com/196558/cyber-crime/31000-records-compromised-in-breach-of-liechtenstein-companies-and-foundations-register.html

3. GitHub 账号遭入侵引发 Shai-Hulud npm 供应链攻击

一个被入侵的GitHub账号引发了供应链攻击，导致窃取凭据的恶意软件在数百个软件包中传播。

🔗https://www.esecurityplanet.com/threats/github-account-breach-fuels-shai-hulud-npm-supply-chain-attack/

4. Greatness PhaaS 新增设备代码网络钓鱼功能以绕过 MFA 并窃取 Token

名为Greatness的商业钓鱼即服务（PhaaS）工具包成为最新一款支持设备代码钓鱼的犯罪软件解决方案，这是一种快速增长的网络威胁，它滥用合法的OAuth 2.0设备授权授权流程，以绕过多因素认证（MFA）并夺取用户账户的控制权。

🔗https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html

5. QuickFox 供应链攻击被用于部署 FDMTP 植入程序

FortiGuard 实验室正在追踪一场与针对 QuickFox 应用的长期供应链攻击相关的活动。QuickFox 是一款 VPN 代理和游戏加速器，中国用户通常使用它来加快访问国内资源的速度，以提升电子游戏的用户体验。

🔗https://feeds.fortinet.com/~/966214247/0/fortinet/blog/threat-research~QuickFox-Supply-Chain-Attack-Used-to-Deploy-FDMTP-Implant

6. 15万人受Madera社区医院数据泄露影响

加利福尼亚州的马德拉社区医院正在通知刚刚超过15万人，他们的个人信息、财务和医疗信息在数据泄露中被泄露。

🔗https://www.securityweek.com/150000-impacted-by-madera-community-hospital-data-breach/

7. 网络保险公司称，人工智能让代价高昂的鱼叉式网络钓鱼攻击变得更加容易

网络保险公司 Resilience 在一份近期报告中称，2026 年上半年，Ransomware 勒索造成了约四分之三的业务损失。

🔗https://www.cybersecuritydive.com/news/ai-spearphishing-cyber-insurance-claims/826732/

8. PLEASE\_READ\_ME 勒索软件摧毁了MySQL服务器

Guardicore Labs 发现了一个针对 MySQL 服务器的 Ransomware 检测活动。攻击者利用 Double Extortion 手段并发布数据来向受害者施压。

🔗https://www.akamai.com/blog/security/please-read-me-opportunistic-ransomware-devastating-mysql-servers

9. 俄罗斯访问代理在监视乌克兰的同时向勒索软件团伙出售网络访问权限

与讲俄语的初始访问经纪人（ IAB ）相关联的暴露服务器揭示了一项庞大的操作，该操作同时助长了全球勒索软件入侵，并支持俄罗斯针对乌克兰国防和航空航天目标的国家情报收集。

🔗https://gbhackers.com/russian-access-broker-sells-network/

10. 假冒 AI 工具利用信息窃取器针对开发者窃取凭证和云密钥

一场针对开发者和人工智能用户的大规模恶意软件活动已被揭露，这揭示了攻击者如何利用伪造的人工智能工具和克隆的GitHub代码仓库来分发信息窃取程序，并窃取敏感数据。

🔗https://gbhackers.com/fake-ai-tools/

**漏洞事件**

Vulnerability Incidents

1. 新的 cPanel 严重漏洞可能让托管客户以数据库 root 身份运行 SQL

cPanel 修复了一个漏洞，该漏洞允许经过身份验证的托管客户在数据库的 root 上下文中执行 SQL，从而跨越了 cPanel 账户与服务器管理数据库身份之间的权限边界。漏洞编号为 CVE-2026-58048 (CVSS 4.0 评分：9.4)。

🔗https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html

2. Gitea 严重任意文件读取漏洞可导致远程代码执行攻击

Gitea 中存在一个严重安全漏洞，编号CVE-2026-59774。允许未经身份验证的远程攻击者从易受攻击的服务器读取任意文件，并可能将攻击升级为远程代码执行。

🔗https://cybersecuritynews.com/gitea-arbitrary-file-read-vulnerability/

3. 六个 Flowise 漏洞允许在 AI 工作流服务器上执行远程代码

Flowise 是一个流行的开源平台，用于构建 AI 代理和 LLM 工作流，其中披露的六个新漏洞允许未经身份验证和低权限攻击者在运行有漏洞版本的托管和云 AI 工作流服务器上实现远程代码执行 (RCE)。

🔗https://gbhackers.com/six-flowise-vulnerabilities/

4. 黑客利用离线硬钱包漏洞窃取超过 1.3 亿美元

加密货币硬钱包 Coldcard 中的一个安全漏洞允许黑客从受害者的钱包中盗取加密货币。据区块链监测机构称，总损失金额超过 1.3 亿美元。

🔗https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/

5. 存在22年的 BMC 漏洞使数千个数据中心面临攻击

超过2.4万个可通过互联网访问的服务器管理界面在登录前泄露了认证哈希值。

🔗https://www.securityweek.com/decades-old-bmc-vulnerability-exposes-thousands-of-data-centers-to-attacks/

6. 严重 Adobe Campaign 漏洞允许未认证攻击者执行任意代码

Adobe 发布针对 Adobe Campaign Classic 的紧急安全更新，解决了多个严重漏洞，这些漏洞可能允许远程攻击者在无需身份验证的情况下在易受攻击的服务器上执行任意代码。该更新记录在 2026 年 8 月 3 日发布的公告 APSB26-120 中，并获得了 Adobe 的最高优先级 111 评级。

🔗https://gbhackers.com/critical-adobe-campaign-flaws/

7. CISA 警告 N-able N-central 认证绕过漏洞遭攻击利用

CISA 警告称，攻击者正在积极利用 N-able N-central 中的一个关键身份验证绕过漏洞。该漏洞被追踪为 CVE-2026-18577，影响运行版本早于 2026.3.1.7 的 N-central 服务器。

🔗https://cybersecuritynews.com/n-able-n-central-auth-bypass-exploited/

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

爱拍照的老李

**讲述普通人能听懂的安全故事**

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