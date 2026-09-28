---
title: 全球安全动态日报｜20260927｜早
url: https://mp.weixin.qq.com/s/DXDDPeWM49am3Iw1jrZxOA
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:34.930244
---

# 全球安全动态日报｜20260927｜早

# 全球安全动态日报｜20260927｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260927｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年9月26日共收录6条安全动态，内容涵盖恶意软件窃取凭据、软件漏洞利用与AI代理可见性问题。

The Hacker News **6**  ·  HackerOne **0**

## The Hacker News

### 01 Lunex Stealer 滥用 AMD 驱动禁用安全监控并窃取浏览器凭据

**公开时间：**2026年09月26日 00:00

AI 解读

Ontinue称，Psychedelic Stealer是名为Lunex的恶意软件即服务平台组件，针对乌克兰语用户，通过遭入侵网站投放仿冒Cloudflare验证页面和恶意MSI，形成四阶段攻击链。LunexLoader利用CMSTPLUA绕过UAC，并借助存在CVE-2023-20598漏洞的AMD Radeon驱动PDFWKRNL.sys实施BYOVD，使安全进程保持运行但失去监控能力，随后部署窃密程序。该程序可窃取七种Chromium浏览器的凭据、会话Cookie及多类加密货币钱包数据，并通过注册表、计划任务和Chrome原生消息主机持久化，获得文件读写、下载和执行程序等能力；平台还被发现扩展至品牌冒充和钓鱼。

原文：https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html

### 02 攻击者绕过WAF利用Oracle PeopleSoft漏洞部署Web Shell

**公开时间：**2026年09月26日 00:00

AI 解读

Google警告，ShinyHunters关联的UNC6240正在全球多行业大规模利用Oracle PeopleSoft高危漏洞CVE-2026-35273（CVSS 9.8），可在未认证情况下远程执行代码。攻击者通过在请求路径中将“P”编码为“%50”，绕过基于字符串匹配的WAF规则，利用PSEMHUB的Java反序列化部署JSP Web Shell并执行无文件命令，继而投放后门、隧道工具和远程管理组件，窃取凭据、管理文件及建立持久访问。受影响领域包括高校、科技、医疗、交通和政府等，数十套系统已发现Web Shell，部分命令以root或SYSTEM权限执行，活动可能导致数据窃取及后续勒索曝光。

原文：https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html

### 03 AI 代理的零信任始于解决零可见性问题

**公开时间：**2026年09月26日 00:00

AI 解读

文章认为，AI代理的部署速度已超过安全团队对其可见性和治理能力，零信任的前提是先建立完整清单。Veeam数据显示，70%的组织承认AI工作流已接触敏感企业数据但缺乏全面监督，67%的组织无法完全追踪员工创建的自主工作流。文中以METR事件说明风险：攻击者利用员工个人EC2实例中的代理获取模型提供商API密钥，三周消耗约60万美元令牌。文章指出，代理分布于网络、终端、浏览器和SaaS中，单一监测渠道难以识别加密流量、嵌入式工具及短生命周期代理，定期审计也可能错过它们。

原文：https://thehackernews.com/2026/09/zero-trust-for-ai-agents-starts-with.html

### 04 Elementor 存在 CSRF 漏洞，攻击者可在管理员点击特制链接后接管网站

**公开时间：**2026年09月26日 00:00

AI 解读

Elementor Website Builder WordPress 插件存在高危 CSRF 漏洞（CVSS 8.8），影响 4.3.0 和 4.3.1 版本，涉及超 200 万个站点。该漏洞源于 Editor Events 模块在请求 URI 任意位置出现字符串 "elementor/v1/events/" 时，跳过对基于 Cookie 认证的 REST API 请求的 CSRF 保护。由于查询字符串由链接构造者控制，攻击者可通过附加无害参数使任意 REST 请求绕过保护，影响整个站点 REST API 面。未认证攻击者可诱使已登录管理员点击嵌入邮件、聊天或评论中的普通链接，利用 /wp/v2/users 创建恶意管理员账户接管站点。该攻击无需 JavaScript、表单提交或攻击者控制的网页。4.3.0 之前版本不受影响，问题已在 4.3.2 版本修复。

原文：https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html

### 05 SharePoint 远程代码执行和 MikroTik RouterOS 漏洞正遭到野外积极利用

**公开时间：**2026年09月26日 00:00

AI 解读

美国网络安全和基础设施安全局（CISA）以存在主动利用证据为由，将影响 Microsoft SharePoint 和 MikroTik RouterOS 的两个漏洞列入已知被利用漏洞目录。CVE-2026-65660（CVSS 8.8）可使已授权攻击者通过网络执行代码，微软随后确认其可导致远程代码执行，并称已观察到相关攻击，但未披露攻击者、受害范围及入侵后行为。CVE-2026-67279（CVSS 6.9）与 CVE-2026-86060 被组成“MikroTrick”攻击链，使未认证客户端建立会话并操控登录策略，进而无需密码取得互联网暴露的 RouterOS 7.x 路由器完整管理权限。

原文：https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html

### 06 Kiteworks因潜在网络攻击敦促客户关闭系统9小时

**公开时间：**2026年09月26日 00:00

AI 解读

Kiteworks（前身为 Accellion）称，从联邦情报部门获得可信情报，某威胁行为者可能在周末攻击部分 Kiteworks 系统，因此建议客户将系统预防性关闭约 9 小时。公司表示目前未发现客户系统遭入侵，此举并非针对已确认的攻击；其未披露告警机构或攻击者身份，并称已知漏洞已在 9.5.1 版本中修复。Zivver、DRACOON、totemo、ownCloud 等其他子公司不受影响。该公司过去曾因文件传输产品漏洞遭 Clop 数据窃取与勒索活动波及。

原文：https://thehackernews.com/2026/09/kiteworks-urges-customers-to-shut-down.html

## HackerOne

昨日暂无符合标准的漏洞发布

![一个不正经的黑客 · 全球安全动态与知识分享](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0wxk6alKwgl2znYoglw9fzyQU1dNd3QicIdQ2gekg7VXOz7LPmL1Kl2dpO5I60zgwgGuO6fVrTAo2PpLibVdWOo4OZYc7FQ4W7Q/640?from=appmsg)![]()

继续阅读

点击文末「阅读原文」，可前往网站主页查看完整资讯与 AI 解读。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR1oKre7rbnJe6BxfvWUT6Uibz0WwGqXuvtRFYicibfTQDhDymFj0rTsyTLlVvOFdzm3wDV9TlqibHDG5UHRfLBPKMiadz3SYOjk0Bo4/0?wx_fmt=png)

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