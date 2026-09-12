---
title: 分享的图片、视频、链接
url: https://mp.weixin.qq.com/s/_g8t4CZEd8MKGyal1bqLFQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:46:22.178952
---

# 分享的图片、视频、链接

# 黑客在不直接攻击域控制器的情况下窃取 Active Directory 密码哈希

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导****读**

攻击者利用 Active Directory 复制机制窃取密码哈希，而无需直接攻陷域控制器。

![Windows Active Directory Logo Identity Governance For Microsoft Active](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyIaAkiauib1kLYe7E5oVZvSwOicTCjzxsPXQ7THkvcJQYvjaN5zWjdl4Jibz3B85ia53WhJwoOwpgose6zIxNc9PicC52ZgXEAznKxgo/640?wx_fmt=webp&from=appmsg)

这种被称为 DCSync 的技术允许拥有特权域凭据的攻击者冒充合法域控制器并请求敏感的目录复制数据。

与那些利用服务器上的恶意软件或试图从域控制器内存中提取凭据的嘈杂攻击不同，DCSync 无缝融入了关键的 Windows 企业流程：活动目录复制。

在典型的 Active Directory 环境中，多个域控制器同步身份信息，以便用户能够在不同位置和服务之间进行身份验证。

当员工更改密码、修改组成员身份或更新账户属性时，域控制器会通过微软的目录复制服务远程协议（DRS/RPC）复制这些信息。

据 Trellix 称，攻击者利用这一受信任的进程，从网络上的另一台系统向合法域控制器发送复制请求。

DCSync攻击的工作原理

DCSync 攻击不需要攻击者在域控制器上运行代码。相反，攻击者需要拥有目录复制权限的账户凭据。

这些权限通常与高权限组相关联，如域管理员、企业管理员和管理员组，但也可显式委派给服务账户或其他身份。

攻击者可利用 Mimikatz、Impacket 等工具或复制协议的自定义实现，调用包括 DRSGetNCChanges 在内的复制操作。

目标域控制器随后返回与所选账户相关的凭据相关数据，其中可能包括NTLM 密码哈希值和 Kerberos 密钥材料。

高价值目标通常包括：

* krbtgt 账户，该账户用于为 Kerberos 票据授予票据（Ticket Granting Tickets）签名。
* 域管理员账户。
* 特权服务帐户。
* 可以访问备份系统、云基础设施或安全工具的帐户。

一旦攻击者获得krbtgt帐户的哈希值，他们就可以伪造被称为黄金票证的Kerberos身份验证票证。这些伪造的票证使入侵者能够获得对视窗域的持久、高特权访问，即使在原始受损用户帐户被重置或禁用之后也是如此。

DCSync 攻击尤为危险，因为其恶意流量与普通域控制器复制流量极为相似。传统终端安全产品通常侧重于检测已知的凭证转储工具、可疑二进制文件或恶意内存活动。安全培训课程

当攻击者使用重命名工具、内置功能、远程执行工具或自定义代码且这些内容与已知特征不匹配时，此方法可能会失效。

一个更相关的检测信号是行为层面的：一个未被识别为域控制器的系统试图执行目录复制操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyJo6iafTHVjiaicibKnd9nbmicGfc3qXxnlAjCQqiabQITuck1qiaOLqtl5W9ExMSw2LF41ZLibfTNsiaf3mwuM0urXE89JmnxNUqwP5mo0/640?wx_fmt=png&from=appmsg)

安全团队应调查源自工作站、应用服务器、跳板机或非常规管理系统的复制请求。

有效的监控来源包括Active Directory审核、Windows安全事件ID 4662、DRS/RPC活动的网络遥测、特权账户日志以及身份检测与响应平台。

组织应将复制权限仅限制给真正需要的身份，并定期审核域命名上下文的访问控制列表。拥有委托复制权限的服务账户应受到特别审查，因为它们可能成为凭证盗窃的诱人目标。

DCSync攻击表明，攻击者并非总需要入侵“主”服务器。通过冒充其中一台服务器，他们就能诱使活动目录交出整个企业的密钥。

详细技术报告：

https://www.trellix.com/blogs/platform/impersonating-the-boss-how-attackers-drain-active-directory/

新闻链接：

https://gbhackers.com/hackers-steal-active-directory-password-hashes/

![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg)

**今日安全资讯速递**

**APT事件**

Advanced Persistent Threat

1. BlueMoon 漏洞利用工具包将 Chrome 和 Windows 漏洞转化为攻击

四个不同的间谍组织使用了相同的漏洞利用工具包来针对最近修复的漏洞，这说明了为什么“稍后修补”是一种危险的赌博。

🔗https://www.malwarebytes.com/blog/bugs/2026/09/bluemoon-exploit-kit-turns-chrome-and-windows-flaws-into-attacks

2. 黑客利用 Claude 和 GPT 驱动的工具协助入侵政府和金融网络

黑客利用商业AI大模型入侵拉丁美洲各地的政府、交通和金融网络。这些行动并非仅依赖AI生成的新型恶意软件家族。其中一组行动滥用合法的Windows工具和重复的批处理脚本，另一组则采用与求职相关的钓鱼攻击、远程访问恶意软件以及代理工具，以渗透巴西金融行业目标。

🔗https://cybersecuritynews.com/gpt-powered-tools/

**一般威胁事件**

General Threat Incidents

1. MantaxOtax Android 恶意软件结合勒索软件与间谍软件

MantaxOtax 安卓恶意软件将文件加密与全面监控相结合，使攻击者能够窃取短信、凭证和设备数据，同时限制对受感染手机的访问。

🔗https://www.infosecurity-magazine.com/news/mantaxotax-android-malware/

2. 新型钓鱼攻击利用 Blob 网址隐藏恶意页面以躲避安全扫描器

Blob 网址是一种临时的浏览器地址，它引用存储在本地内存中的内容，而非远程托管的网页。因此，该钓鱼页面没有持久的公共网址，仅存在于活跃的浏览器会话中。

🔗https://gbhackers.com/phishing-attack-uses-blob-urls/

3. 自主 AI Agent在六小时内窃取数千个凭据

谷歌威胁情报团队（GTIG）表示，他们观察到动机各异的攻击者针对医疗、政府和媒体行业的专有人工智能模型展开攻击，窃取应用程序接口（API）凭证，并控制受害方的云环境，以维持未经授权的人工智能工作负载。

🔗https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html

4. 黑客可利用存在漏洞的 LiteLLM AI 网关获取 Root 权限窃取云凭据

近十分之一的互联网暴露 LiteLLM AI 网关接受了广泛记录的默认主密钥 sk-1234，或无需认证，这为 LLMjacking、敏感凭证泄露以及（在易受攻击版本中）网关容器内的根级代码执行创造了直接途径。

🔗https://gbhackers.com/litellm-ai-gateways/

5. Liquid 黑客归还通过 Elements 漏洞盗取的 3400 枚比特币，仍持有价值 4700 万美元的比特币

比特币的公开记录显示，9月6日周日从Liquid Network拿走近4000枚比特币的人，在次日退回了其中3400枚。仍有约598.5枚比特币未被归还。

🔗https://thehackernews.com/2026/09/liquid-hackers-return-3400-bitcoin.html

6. BigBear 钓鱼组织窃取数千个 Microsoft 365 账号凭据

研究人员进入了这些骗子的管理后台，发现了与461个组织相关的5137条被盗记录。

🔗https://www.theregister.com/security/2026/09/08/bigbear-phishing-crew-nets-thousands-of-microsoft-365-credentials/5294944

7. 黑客在不直接攻击域控制器的情况下窃取 Active Directory 密码哈希

攻击者利用 Active Directory 复制机制窃取密码哈希，而无需直接攻陷域控制器。

🔗https://gbhackers.com/hackers-steal-active-directory-password-hashes/

8. 数百个AI Agents 协助PaperCut攻击者入侵395家以上机构

一名未知攻击者利用数百个AI代理，利用PaperCut MF/NG的两个漏洞入侵了至少395家机构。受害者主要集中在美国教育领域，且入侵行动进展迅速。其中有一例，一所美国高中从初步获取访问权限到获得域管理员权限仅用了7分钟。

🔗https://www.theregister.com/security/2026/09/10/hundreds-of-ai-agents-helped-papercut-attacker-hit-395-orgs-and-some-went-off-script/5295650

9. AdaptHealth 数据泄露影响 410 万人

医疗公司 AdaptHealth 发生数据泄露事件，超过 410 万人的个人、健康及保险信息被盗。

🔗https://www.securityweek.com/4-1-million-impacted-by-adapthealth-data-breach/

10. 黑客利用虚假 GTA 6 下载部署 RATs、Infostealers 和数据擦除恶意软件

网络犯罪分子正利用人们对《侠盗猎车手 VI》（GTA VI）的高度关注，推送虚假的游戏下载链接，这些链接安装的是多种类型的恶意软件，而非可玩的游戏。该活动针对的是在游戏发布前寻找早期版本、泄露版本或非官方演示版的用户。

🔗https://cybersecuritynews.com/fake-gta-6-downloads/

**漏洞事件**

Vulnerability Incidents

1. 严重 Check Point VPN 漏洞导致远程代码执行攻击

Check Point Software 已披露并修补了两项关键的 VPN 相关漏洞，CVE-2026-85102 和 CVE-2026-85103，两者的最高 CVSS 评分均为 9.8，且在特定条件下均允许未经身份验证的远程代码执行。

🔗https://cybersecuritynews.com/check-point-vpn-vulnerabilities/

2. CISA 将 Cisco、Google Chromium V8、Fortinet 和 Citrix NetScaler 漏洞添加到其已知被利用漏洞目录中

美国网络安全和基础设施安全局 (CISA) 将 Cisco、Google Chromium V8、Fortinet 和 Citrix NetScaler 的漏洞添加到其已知被利用漏洞目录中。

🔗https://securityaffairs.com/198850/security/u-s-cisa-adds-cisco-google-chromium-v8-fortinet-and-citrix-netscaler-flaws-to-its-known-exploited-vulnerabilities-catalog.html

3. 黑客利用思科防火墙严重漏洞获取 Root 权限并部署恶意软件

思科Talos团队已确认有针对两款影响思科安全防火墙管理中心（FMC）软件的漏洞被主动利用，国家支持的黑客组织及勒索软件关联方利用这些漏洞获取Root权限、植入恶意软件，并对企业网络发起攻击部署。

🔗https://cybersecuritynews.com/cisco-firewall-root-access-flaw/

4. Adobe 修复被用于部署 Rust 后门和 PHP Web Shell 的 Magento 零日漏洞

该漏洞目前被追踪为 CVE-2026-75650（CVSS 评分：10.0），Sansec 将其命名为 StyleSmuggler，该机构于 2026 年 9 月 4 日发现了零日利用活动。

🔗https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html

5. FreeIPA 漏洞链让匿名客户端创建可复用的管理员凭据

红帽公司表示，FreeIPA 存在一个漏洞，使得从未登录过的客户端可以在目录中自行创建一个 Kerberos 身份，并最终加入管理员组。

🔗https://thehackernews.com/2026/09/freeipa-flaw-chain-lets-anonymous.html

6. N-able 发布针对零日漏洞的补丁

安全公司 N-able 已发布紧急热修复程序，以修复其 N-central 平台中的一个关键零日漏洞。编号为CVE-2026-86218的N-central预认证漏洞可能使攻击者实现远程代码执行。研究人员表示，该漏洞的严重程度评分为10分，属于评分体系中的最高值。

🔗https://www.cybersecuritydive.com/news/n-able-issues-patch-zero-day-flaw/829808/

7. Palo Alto PAN-OS 漏洞允许以 Root 用户身份执行任意代码

Palo Alto披露了一个高严重性的 PAN-OS 漏洞，该漏洞可能允许未认证的远程攻击者在受影响的 PA-Series 硬件防火墙上以 root 权限执行任意代码。该漏洞编号为 CVE-2026-0310，存在于 XML 处理中，厂商已将其评为最高建议紧急程度。

🔗https://cybersecuritynews.com/palo-alto-pan-os-vulnerability-code-execution/

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