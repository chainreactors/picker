---
title: 卡巴斯基发现乌克兰黑客组织BO Team入侵俄罗斯公司的代码签名服务器
url: https://mp.weixin.qq.com/s/9xKx19a-a7GN6EyqqdwJEw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:47.365585
---

# 卡巴斯基发现乌克兰黑客组织BO Team入侵俄罗斯公司的代码签名服务器

# 卡巴斯基发现乌克兰黑客组织BO Team入侵俄罗斯公司的代码签名服务器

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导****读**

卡巴斯基对一家俄罗斯软件开发公司网络内可疑活动的调查，发现其开发基础设施和软件代码签名服务器已遭长达数月的入侵。

![](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyJFqZA7iaaj7QOtUBIz2YeTJcicMOvC0eQu0dtUena7zUmicYTP9icrsEyx0Oume3ICdCJ1FTWTMlgmiaBQjjT2KicCFNb8A26Gs7Rias/640?wx_fmt=jpeg&from=appmsg)

卡巴斯基工业控制系统计算机应急响应团队（ICS CERT）在2025年6月接到受影响开发者通报后进行调查，黑客活动被归因于一个名为BO Team（(别名Black Owl, Hoody Hyena, and Lifting Zmiy)）的威胁组织。

卡巴斯基表示，目标公司的名称未被披露，但该公司在俄罗斯境内运营，开发的软件在“俄罗斯联邦拥有客户群”。

在数月的时间里，此次入侵导致机密信息被盗，同时该组织IT基础设施的所有组件均遭破坏，其中包括Windows和Linux服务器、工作站、管理程序、备份服务器、安全解决方案管理服务器以及网络设备。

该团队至少自2023年起活跃，专注于网络间谍活动和黑客行动主义，历史上曾以俄罗斯实体为目标，利用 Mythic、Cobalt Strike 等工具以及 BrockenDoor、ZeronetKit 等自有恶意软件窃取有价值数据并入侵被攻陷的基础设施。该组织被认定为乌克兰起源。

“他们的主要动机是破坏俄罗斯的军工联合体，以削弱莫斯科在战场上的作战能力。”Orange Cyberdefense 在对该组织的分析中表示。“他们还开展认知战，旨在羞辱俄罗斯机构，并证明俄罗斯机构在乌克兰的数字抵抗面前不堪一击。”

BO Team会部署勒索软件，并在专属的 Telegram 频道上公开其行动，但此次针对未指明软件开发商的攻击，既没有造成任何数据破坏，也没有发布公开声明宣称对此负责。

“攻击者通过建立便捷的命令通道、植入后门以在失去访问权限时恢复连接，逐步在目标网络中站稳脚跟。”卡巴斯基表示。“对软件开发（CI/CD）基础设施和软件代码签名服务器的入侵表明，此次攻击很可能会演变为供应链攻击事件。”

此次攻击中，威胁组织利用暴露的SSH服务入侵了该组织的Linux终端服务器，并借此对内部网络展开侦察，标记出可访问SMB、Kerberos、SSH、Telnet、FTP、HTTP、HTTPS、WinRM和LDAP服务的系统。

经查明，该攻击者还曾试图访问内部门户以及 proxy-sale[.]com、start.duckduckgo[.]com、vcsa.vmware[.]com 和 vulners[.]com 等网站，但均未成功。

事件日志显示，攻击者还试图从被入侵的终端服务器连接到虚拟化系统服务器，包括登录 VMware vCenter 网页界面。这些登录尝试均以失败告终。

威胁参与者成功针对存在CVE-2021-44228漏洞（又称Log4Shell和LogJam）的VMware vCenter服务器（7.0.3版本），获取了具有root权限的远程命令行界面，通过SSH连接至管理程序，并识别出可访问的主机。

该阶段还涉及在管理程序上部署后门，通过在“/etc/cron.hourly/”目录中植入一个 shell 脚本，使其每小时运行一次。该脚本命名为“pgcache”，此举很可能是为了将其伪装成合法的 PostgreSQL 组件。

该后门程序的主要功能是从“lo1yaizaeghaevarooD1ahtaichootae.nofrillsdns[.]com”下载并运行一个辅助 shell 脚本。该 shell 脚本旨在下载并运行全局套接字（GSocket）工具，使攻击者能够远程控制已被入侵的主机。

已发现该脚本的部分变体指向部署在“lo1yaizaeghaevarood1ahtaichootaz.nofrillsdns[.]com”上的特定主机名负载，以传递一个尚未确定的下一阶段负载。

“攻击者使用了nofrillsdns[.]com服务，该服务可通过调用curl工具免费创建域名。”卡巴斯基表示。“默认情况下，当恶意软件的命令与控制服务器未运行时，攻击者会将对应的DNS记录设置为127.0.0.1，这正是脚本所检测的。激活后门仅需修改DNS记录——随后脚本便会下载并运行该恶意软件。”

卡巴斯基研究人员发现了BO Team连接各类Windows服务器的大量痕迹，攻击者仅在一个案例中使用了恶意软件。让黑客格外感兴趣的那台服务器，被用于对受攻击组织开发的商业软件的编译版本进行签名。他们可能试图在产品构建即将签名前注入恶意代码，从而实施供应链攻击。其次，攻击者可能试图窃取组织的数字签名，以便日后用其对恶意软件进行签名。

攻击者很可能试图执行恶意WMI脚本，并在临时文件目录中安装与Linux变种类似的后门程序。

但在该事件被发现并采取应对措施后，攻击者失去了受损基础设施的访问权限，于是在7月底策划了一场钓鱼活动，试图获取员工的凭证。这封钓鱼邮件的主题为“账户与邮件服务器断开连接”，目的是诱骗收件人点击链接修改密码。

“综合所有间接证据来看，比如攻击者对源代码代码仓库和软件构建签名服务器的兴趣，以及他们使用软件成分分析（依赖项分析）平台的行为，我们认为BO团队可能旨在向被攻击组织发布的解决方案中注入恶意代码，以便后续入侵其客户，也就是实施所谓的供应链攻击。”卡巴斯基总结道。

技术报告：

https://ics-cert.kaspersky.com/publications/reports/2026/11/05/supply-chain-attack-bo-team-in-a-software-developers-infrastructure/

技术报告全文：

https://thehackernews.com/2026/11/bo-team-exploits-log4shell-in-vmware.html

![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg)

**今日安全资讯速递**

**APT事件**

Advanced Persistent Threat

1. 黑客部署 PerfectPioneer 远程访问木马与 KUKURAT 后门程序窃取敏感政府数据

间谍组织耗时九个月，针对东南亚政府网络优化了两款定制化远程访问木马。

🔗https://gbhackers.com/kukurat-backdoor-activity/

2. 卡巴斯基发现乌克兰黑客组织BO Team入侵俄罗斯公司的代码签名服务器

卡巴斯基对一家俄罗斯软件开发公司网络内可疑活动的调查，发现其开发基础设施和软件代码签名服务器已遭长达数月的入侵。

🔗https://thehackernews.com/2026/11/bo-team-exploits-log4shell-in-vmware.html

3. 新的 GitDoor 和 GraphDoor 后门将 GitHub 和 SharePoint 变成隐蔽 C2 通道

亚洲和非洲的政府部门成为了一场活跃的网络入侵活动的目标，该活动会部署此前未被记录的后门程序，这些程序利用微软SharePoint和GitHub等合法服务作为命令与控制（C2）渠道。

🔗https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html

**一般威胁事件**

General Threat Incidents

1. Optimizely 遭黑客攻击，CNN、福克斯新闻、BBC、Salesforce 等网站被植入恶意软件

一起针对 Optimizely 的供应链攻击已导致包括 Zoom、CNN、福克斯新闻、BBC、Salesforce 以及 GitLab 在内的众多热门网站加载恶意 JavaScript 代码，这些网站的访问者面临着旨在窃取加密货币和支付信息、利用 iOS 设备漏洞的脚本攻击。

🔗https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-infects-major-brands-sites-with-malware/

2. Cursor 称被盗的 Fireworks AI 密钥导致被植入木马的 Claude Code 扩展事件

Cursor 扩展市场上Anthropic 官方 Claude Code 扩展程序遭入侵事件，是因Fireworks AI遭黑客攻击后泄露访问密钥所致。

🔗https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html

3. 黑客利用恶意 DLL 和虚假 PDF 文件投递 PureLogs 和 PureRAT 有效载荷

一个以货运为主题的ZIP压缩包正在投放多阶段恶意软件链，该恶意软件链结合了DLL侧载、伪装工具和加密Python代码，以部署与PureLogs和PureRAT基础设施相关的有效载荷。

🔗https://gbhackers.com/malicious-dll-payload/

4. 旧的 Bitly 链接被劫持，将用户从麦当劳、汉堡王和政府 X 帖子重定向

嵌入在麦当劳、汉堡王、政府机构和知名政客的历史 X 帖子中的旧 Bitly 链接已被重新利用，将访问者重定向到不相关的网站。

🔗https://gbhackers.com/old-bitly-links-hijacked-to-redirect-users/

5. Uber 通知司机数据泄露波及近 15 万人

Uber 正在通知近 15 万名司机，称攻击者在 10 月初攻破 AI 基础设施提供商 Fireworks 后窃取了他们的数据。

🔗https://www.bleepingcomputer.com/news/security/uber-notifies-drivers-of-data-breach-affecting-nearly-150-000-people/

6. Infoblox 确认发生供应链入侵，此前攻击者已访问敏感数据

Infoblox 一家供应商的数据泄露事件暴露了客户网络快照和员工数据，凸显了可信第三方访问的风险。

🔗https://securityaffairs.com/203309/data-breach/infoblox-confirms-supply-chain-breach-after-attackers-access-sensitive-data.html

7. 黑客利用 SEO 毒害感染 1,000 个 WordPress 站点上的 Gootloader 恶意软件

Gootloader 的幕后网络犯罪分子已攻陷了超过 1,000 个 WordPress 网站，并运营着 216 个管理员控制的域名。

🔗https://gbhackers.com/gootloader-malware-attack/

8. SANSAR Linux 加密货币挖矿木马使用修改过的 NVIDIA 库来隐藏 GPU 活动

入侵的核心是一个名为 SANSAR 的工具包，这是一个基于 Rust 的编排器，通过 TOR 匿名网络接收命令以管理 CPU 和 GPU 挖矿机。

🔗https://thehackernews.com/2026/11/sansar-linux-cryptomining-malware-uses.html

9. 在 Docker Hub 镜像中泄露的云密钥在几秒钟内被盗

攻击者会在公开的 Docker Hub 镜像发布后短短八秒内，提取并利用其中暴露的凭证和访问密钥。

🔗https://www.bleepingcomputer.com/news/security/cloud-keys-leaked-in-docker-hub-images-are-stolen-within-seconds/

**漏洞事件**

Vulnerability Incidents

1. Oracle 今日将修补 11 个 Java 漏洞，以修复关键 OpenJDK RCE (CVE-2026-114938) 漏洞被曝光

Oracle公司将于2026年11月17日（周二）为Java SE的11个漏洞发布安全补丁，所有这些漏洞均可在未认证的情况下被远程利用，另有独立报告警告存在一个可能严重的远程代码执行（RCE）漏洞，该漏洞影响OpenJDK。

🔗https://thehackernews.com/2026/11/oracle-to-patch-11-java-flaws-today-as.html

2. ScreenConnect 中的关键漏洞被利用，在 MSP 技术人员账户上运行恶意文件

根据安全研究人员的数据，不到一个月内就发出了近 69 万次文件传输请求。

🔗https://www.cybersecuritydive.com/news/critical-flaw-screenconnect-malicious-files-msp/874900/

3. 一名研究员在一小时内发现六个 Danfoss 冰箱控制器零日漏洞

一名荷兰网络安全研究员称，他在不到一小时内就在丹佛斯制冷控制器固件中发现了六个零日漏洞，随后对该厂商针对内存破坏问题的防护措施给出了严厉的批评。

🔗https://www.theregister.com/security/2026/11/17/not-rocket-surgery-claims-researcher-who-found-six-danfoss-fridge-controller-zero-days-in-under-an-hour/5310197

4. CVE-2026-130622 和 CVE-2026-130623 – AWS Private CA Connector for Kubernetes (aws-privateca-issuer) 中命名空间范围颁发者凭据加载和处理时的错误授权

在 Kubernetes (aws-privateca-issuer) 的 AWS Private CA 连接器中，1.12.0 版本之前的凭证加载逻辑存在错误的授权，这可能允许具有创建命名空间范围颁发者权限的经过身份验证的远程用户，通过...获取由另一个命名空间的 AWS Private CA 签发的证书，包括从属 CA 证书，该 CA 使用该命名空间存储的 AWS 凭证。

🔗https://aws.amazon.com/security/security-bulletins/rss/2026-187-aws/

5. 黑客利用 ß 与 ss 文件名技巧绕过 macOS 安全检查并覆盖文件

macOS 文件名命名方式中的一个 Unicode 特性缺陷，使多款常用开发者工具面临文件覆盖和绕过排除机制的攻击风险。苹果文件系统（APFS）与多个应用程序比较文件路径的方式之间存在不匹配。攻击者可以提供替代的Unicode拼写，例如用ß代替ss，以绕过安全过滤器。

🔗https://gbhackers.com/hackers-exploit-the-s-vs-ss-filename-trick-to-bypass-macos-security-checks/

6. N-able 修补了 17 个 N-central 漏洞，同时攻击者利用早期漏洞部署加密货币挖矿程序

该公司称 N-central 2026.4 热修复 3 是一个关键安全更新，其中包含多个增强远程监控和管理 (RMM) 和统一端点管理 (UEM) 平台安全性的安全补丁和修复程序。

🔗https://thehackernews.com/2026/11/n-able-patches-17-n-central-flaws-as.html

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

爱拍照的老李

**讲述普通人能听懂的安全故事**

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过