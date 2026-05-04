---
title: 黑客利用cPanel漏洞入侵亚洲政府和军方服务器
url: https://mp.weixin.qq.com/s/dTnmXzJbrQf6pY9YjZr_2A
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:32:01.022483
---

# 黑客利用cPanel漏洞入侵亚洲政府和军方服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyLMN5Hu7diaziaric9icwiaKMoQ9NpZNI365nrQTCJ2w6vGmrxj3tWGvZzC7UaKXQ5Zib6WHMqmqVYBcibF7icRY4eqibqJu2VshmJBViauc/0?wx_fmt=jpeg)

# 黑客利用cPanel漏洞入侵亚洲政府和军方服务器

会杀毒的单反狗
会杀毒的单反狗

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

一个针对亚洲多国政府和军事基础设施的复杂攻击活动，结合了对关键cPanel认证绕过漏洞的快速利用，以及针对印尼国防领域门户的定制零日漏洞利用链，并最终转向泄露超过4GB的东亚某国铁路文件。

该攻击活动的初始访问途径以CVE-2026-41940 为中心，这是一个严重的 CVSS 9.8 身份验证绕过漏洞，影响 cPanel 和 WHM 中 v11.40 之后的所有版本。

该漏洞利用登录和会话加载过程中的 CRLF 注入，允许未经身份验证的攻击者操纵whostmgrsessioncookie 并获得完整的 root 级管理权限，而无需有效的凭据。

在 cPanel 于 2026 年 4 月 28 日发布补丁之前，该漏洞已被证实已被实际利用，CISA 随后将其添加到其“已知已利用漏洞”目录中。

在此次攻击活动中，cPanel 漏洞利用只是一个更广泛、更令人担忧的攻击行动的一部分，该行动源于一个暴露的命令与控制 (C2) 服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyIBQibUSmnLiaRXdMx8YxA6xIia1z1sh0CuDnq5RseK3AEFxc3Uzq5IZWzmvGx6DgEQCBKumZVc7u5tLicDUY5ehcibHvzI1XgGP9ib0/640?wx_fmt=png&from=appmsg)

cPanel漏洞被利用

更重要的是，Ctrl-Alt-Intel 恢复了一个针对印尼国防部门培训门户网站的自定义漏洞利用程序。

攻击者已经拥有有效的凭证，并通过直接从服务器颁发的会话 cookie 中读取预期的 CAPTCHA 值来绕过门户网站的 CAPTCHA 机制，使得在未解决挑战的情况下，该挑战完全无效。

攻击者进入系统后，瞄准了文档管理功能，通过一个存在漏洞的保存端点，将 SQL 注入到文档名称字段中。

然后，攻击者利用 PostgreSQL 的一项功能（允许数据库服务器生成任意 shell 命令），将 SQL 注入攻击升级为对操作系统的完全访问权限。

命令输出被捕获到，经过 base64 编码，并使用——一个隐蔽的、基于文件读取的外泄通道，完全是数据库层原生的——/tmp重新摄入到应用程序记录中。

该漏洞利用脚本名为exploit\_siak\_bahasa.py，其中包含越南语注释，但Ctrl-Alt-Intel 明确警告说，这不足以确定攻击者身份，并且可能代表故意误导。

为了进行命令和控制，攻击者部署了一个 AdaptixC2 有效载荷（名为 的 ELF 二进制文件1），配置为向 发送信标delicate-dew.serveftp[.]com:4455，服务器端遥测数据证实了 C2 地址为95.111.250[.]175。

![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyIibWpI7icyzibicNgdALMYvJRj4D9qab5YAERLYLE3nYvQwRicSIL8ln5Xmy8NChHxEjG5ibTuHu8iaiaWFVMDnglhFaeIqy5zN2r3UWU/640?wx_fmt=png&from=appmsg)

C2 服务器（来源：Ctrl-Alt-Intel）

还恢复了PowerShell 反向 shell ( init.ps1)，建立了到同一 IP 地址 4444 端口的 TCP 连接。

95.111.250[.]175:1194/UDP为了确保持久稳定的访问，攻击者将 OpenVPN 和 Ligolo 结合成一个分层枢纽协议栈。早在 2026 年 4 月 8 日，就部署了一台 OpenVPN 服务器，并通过10.8.0.0/24客户端子网进行路由。

Ligolo 代理安装在一个隐藏的目录下/usr/local/bin/.netmon/，伪装成名为 的 systemd 服务systemd-update.service，并配置为自动重启——即使在重启后也能提供持久的重新进入。

通过此枢纽基础设施，攻击者到达了内部主机10.16.13.88并部署了exfil\_docs\_v2.sh自定义的基于 SFTP 的数据泄露脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyKUSjBEMU53psKunXzqFA2Rnyhgd0DEaE9GDUKcY08QU86I43lduUiaUaFBnXiaPrnIciaRa3V1NibHYia6HEHmvKyaSRJYsJ2GfnBE/640?wx_fmt=png&from=appmsg)

数据泄露（来源：Ctrl-Alt-Intel）

总共有 110 个文件（约 4.37GB）从某国铁路学会电气化委员会被盗，这些文件涵盖了.pptx、.pdf、.docx和.xlsx格式，日期从 2020 年到 2024 年。

其中最敏感的材料包括 2021 年的财务工作簿，其中包含全名、身份证号码、银行账户详细信息和电话号码。

Ctrl-Alt-Intel 虽然没有给出确切的归因，但东南亚军事和政府目标的受害者，以及与相关的交通运输部门数据的窃取，都表明这是一起蓄意的区域情报收集行动。

Shadowserver基金会于 2026 年 4 月 30 日确认，有 44,000 个独立的 IP 地址被观察到正在扫描受害者、发起漏洞利用或对其蜜罐传感器进行暴力攻击。

强烈建议使用 cPanel/WHM 的组织立即升级到最新版本，并审核服务器日志，查找基于 CRLF 的会话操纵迹象。

技术报告：

《东南亚军事实体成为 cPanel 攻击目标 (CVE-2026-41940)》

https://ctrlaltintel.com/research/SEA-CPanel/

新闻链接：

https://cybersecuritynews.com/cpanel-vulnerability-exploited/

![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg)

**今日安全资讯速递**

**APT事件**

Advanced Persistent Threat

1. Lazarus黑客在跨链攻击中从KelpDAO窃取2.9亿美元

KelpDAO已成为最新一个遭遇重大安全危机的DeFi项目，据调查人员称，这起价值2.9亿美元的抢劫案可能与朝鲜的Lazarus集团有关。这次攻击针对的是rsETH，一种在多个协议中使用的重新质押以太币资产，数小时内约116,500个代币被耗尽。

🔗https://www.cysecurity.news/2026/05/lazarus-hackers-steal-290m-from-kelpdao.html

2. 新的 Deep#Door RAT 使用隐匿性和持久性针对 Windows

Deep#Door在批处理文件中隐藏了一个Python RAT，关闭Windows防御，通过多种持久化方法存活，并通过公共TCP隧道泄露数据。

🔗https://securityaffairs.com/191567/malware/new-deepdoor-rat-uses-stealth-and-persistence-to-target-windows.html

3. 黑客利用cPanel漏洞入侵亚洲政府和军方服务器

一个针对亚洲多国政府和军事基础设施的复杂攻击活动，结合了对关键cPanel认证绕过漏洞的快速利用，以及针对印尼国防领域门户的定制零日漏洞利用链，并最终转向泄露超过4GB的东亚某国铁路文件。

🔗https://cybersecuritynews.com/cpanel-vulnerability-exploited/

**一般威胁事件**

General Threat Incidents

1. PyTorch Lightning 和 Intercom 客户端用户面临凭证窃取活动的风险

Python 的软件供应链已被入侵，针对流行的 PyPI 包 Lightning，通过复杂的软件供应链攻击，使下游机器学习环境面临隐蔽的凭证窃取风险。

🔗https://www.cysecurity.news/2026/05/pytorch-lightning-and-intercom-client.html

2. npm 威胁态势：攻击面与缓解措施（更新于5月1日）

Unit 42分析了Shai Hulud事件后npm供应链的演变。发现可传播的恶意软件、CI/CD持久化、多阶段攻击等。

🔗https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/

3. 勒索软件攻击利用 QEMU 溜过企业防御

为了绕过传统的安全控制，黑客越来越多地依赖虚拟化作为隐蔽的执行层，将恶意操作嵌入到QEMU环境中。

🔗https://www.cysecurity.news/2026/05/ransomware-campaign-leverages-qemu-to.html

4. Trellix源代码泄露——黑客未经授权访问代码库

网络安全巨头Trellix披露了一起重大安全事件，涉及对其部分源代码库的未经授权访问。该公司在其网站上发表官方声明，证实了此次数据泄露事件，并表示在发现入侵后立即聘请了顶尖的取证专家。

🔗https://cybersecuritynews.com/trellix-source-code-breach/

5. 攻击者部署 AiTM 网络钓鱼页面以访问 SharePoint、HubSpot 和 Google Workspace

威胁行为者正在迅速将其入侵技术转向高速、以SaaS为中心的攻击，完全绕过传统的端点安全防护。

🔗https://cybersecuritynews.com/attackers-deploy-aitm-phishing-page/

6. 全新 Bluekit 钓鱼工具包具备 AI 助手功能

Bluekit 目前仍在开发中，它为用户提供自动域名注册和人工智能助手。

🔗https://www.securityweek.com/new-bluekit-phishing-kit-features-ai-assistant/

7. ZenBusiness 超过500万条数据泄露

2026年3月，勒索集团“ShinyHunters”声称从ZenBusiness（一家企业注册与合规平台）获取了大量数据。该集团称这些数据是从Snowflake、Mixpanel和Salesforce等平台泄露的，并威胁称如果未支付赎金，将公布这些数据。

🔗https://haveibeenpwned.com/Breach/ZenBusiness

**漏洞事件**

Vulnerability Incidents

1. cPanelSniper——cPanel漏洞利用程序曝光，44000台服务器受感染

一个名为“cPanelSniper”的武器化概念验证（PoC）漏洞利用框架已公开发布，针对的是CVE-2026-41940，这是一个在cPanel & WHM中的最高严重性身份验证绕过漏洞，该漏洞已导致全球数以万计的服务器被入侵，攻击活动可追溯至2026年2月下旬。

🔗https://cybersecuritynews.com/cpanelsniper-poc-exploit/

2. CVE-2026-31431：Copy Fail漏洞允许跨云环境提升 Linux 权限

一个高严重性Linux漏洞，“Copy Fail”（CVE-2026-31431），可在云环境和Kubernetes工作负载中实现根权限提升。目前已有可用的漏洞利用代码在野外出现，组织应迅速采取行动进行检测、缓解并降低风险。

🔗https://www.microsoft.com/en-us/security/blog/2026/05/01/cve-2026-31431-copy-fail-vulnerability-enables-linux-root-privilege-escalation/

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