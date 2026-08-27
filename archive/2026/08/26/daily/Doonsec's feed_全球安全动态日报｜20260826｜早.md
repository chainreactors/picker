---
title: 全球安全动态日报｜20260826｜早
url: https://mp.weixin.qq.com/s/W876vycUVpHOCTMC8JbJWQ
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:11:39.988148
---

# 全球安全动态日报｜20260826｜早

# 全球安全动态日报｜20260826｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260826｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年8月25日共收录12条安全动态，内容涵盖恶意软件传播、身份认证攻击与AI及企业软件漏洞成为标题焦点。

The Hacker News **12**  ·  HackerOne **0**

## The Hacker News

### 01 交付的 AI 代码多到无法确保安全？看看如何控制修复债务

**公开时间：**2026年08月25日 01:41

AI 解读

文章指出，AI编程工具虽提升开发速度，但会快速引入开源组件，使安全团队难以同步评估漏洞、许可、维护与归属，形成持续积累的修复债务（remediation debt）。随着AI工具更自主，该缺口可能扩大。ActiveState对技术、金融、医疗、制造及政府领域300名安全与工程负责人展开调查，研究团队如何应对AI驱动的开源风险、修复计划困境及债务与审计失败、违规频率和生产力损失的关系。网络研讨会基于数据解读这些发现，供企业对照自身项目，并分析有效的治理模式及可能适得其反的做法。

原文：https://thehackernews.com/2026/08/shipping-more-ai-code-than-you-can.html

### 02 Weedhack 恶意软件通过虚假《我的世界》客户端和 SEO 投毒传播

**公开时间：**2026年08月25日 01:41

AI 解读

研究人员发现，名为Weedhack的恶意软件仍通过伪装成Minecraft客户端的仿冒网站传播，攻击者利用SEO投毒、YouTube及Discord、Reddit等渠道引流，并借助文件托管服务、GitHub及合法的Minecraft工具平台分发JAR文件。仿冒站点复制真实项目的品牌、功能说明、安装指南和开发者信息，部分甚至在搜索结果中压过官方来源。McAfee Labs称已拦截逾6,300次恶意网站访问，49.6%的恶意链接来自Discord。该攻击通过多阶段流程部署JAR载荷，可收集系统信息、设置Microsoft Defender排除项并窃取受害主机敏感数据。

原文：https://thehackernews.com/2026/08/weedhack-malware-spreads-via-fake.html

### 03 美国制裁涉伊朗黑客，指其实施关键基础设施入侵事件

**公开时间：**2026年08月25日 00:00

AI 解读

美国财政部对伊朗情报部安全部（MOIS）下属马布纳研究所（Mabna Institute）的五名成员实施制裁，针对其自2023年底起入侵美国能源、防御承包商、医疗、IT和金融公司关键基础设施并外泄数据的行动。制裁是“经济孤立行动”（Operation Economic Outcast）的一部分，旨在切断伊朗政权全球金融生命线，包括近60个实体、个人和船舶，以及数字资产领域。TRM Labs分析显示，该集团通过30个钱包获利1600万美元，其中莫伊塔巴·加莱赫库希等主要从事加密货币盗窃。制裁还延伸至次级制裁和前公司Zedcex、Zedxion帮助IRGC处理10亿美元资金。美国还提供1000万美元奖励征集此类针对关键基础设施的恶意活动情报，伊朗黑客还攻击水务设施及盟国英国小型电厂，并有亲伊朗黑客主义者网络通过Telegram合作。

原文：https://thehackernews.com/2026/08/us-sanctions-iran-linked-hackers-behind.html

### 04 恶意网页可能毒害 NVIDIA NemoClaw 背后的本地 AI 模型

**公开时间：**2026年08月25日 00:00

AI 解读

Oasis Security披露NVIDIA NemoClaw存在弱点，攻击者控制的网页可未经身份验证接管本地Ollama实例，修改AI模型聊天模板向每轮对话注入隐藏指令。NemoClaw是NVIDIA开源参考栈，支持Ollama作为本地推理后端，在macOS和Linux上将Ollama绑定至0.0.0.0:11434，结合DNS回绕和CORS绕过认证。Windows和WSL路径未修复。毒化模板为模型级属性不可见于API，影响代理工具访问。框架在v0.0.106引入绑定检查但在某些路径跳过。未报告CVE，未发现利用。

原文：https://thehackernews.com/2026/08/a-malicious-webpage-could-poison-your.html

### 05 WhatsApp 新增多个通行密钥，支持在 iOS 和 Android 上实现抗钓鱼登录

**公开时间：**2026年08月25日 00:00

AI 解读

Meta宣布为WhatsApp账户支持添加多个通行密钥，使同时使用iOS和Android设备的用户可采用抗钓鱼方式登录。通行密钥于2023年10月率先登陆Android，2024年初扩展至iOS；Meta称目前已有超过10亿人使用通行密钥登录WhatsApp。用户可在“设置—账户—通行密钥”中管理。此次更新还将两步验证从六位PIN升级为支持字母、数字和特殊字符的完整密码，并在Android来电中显示来电来源、是否为联系人及共同群组等信息，以提供更多来电背景。

原文：https://thehackernews.com/2026/08/whatsapp-adds-multiple-passkeys-for.html

### 06 24个npm包滥用unpkg镜像托管虚假Cloudflare验证码页面

**公开时间：**2026年08月25日 00:00

AI 解读

研究人员披露了一项利用24个npm软件包及其unpkg等镜像的钓鱼活动。攻击者将单个HTML页面存入包内，借助受信任镜像托管伪造的Cloudflare验证码页面，再把用户引向ClickFix式钓鱼基础设施；下载软件包本身不会造成危害。页面内置验证码和JavaScript逻辑，曾通过仿冒微软登录域名跳转，后改用KeyVal公共键值服务作为“死信解析器”提取并解码跳转地址。目前该逻辑转向真实ChatGPT网站，但攻击者可据此改为其他钓鱼域名。研究人员指出，npm及镜像可充当免费存储和持久化基础设施，即使软件包从官方仓库移除，镜像中的内容仍可能存在。

原文：https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html

### 07 Mirage2FA 攻击激增，波及美国和欧盟 4,500 家企业，滥用 Microsoft 365 登录流程

**公开时间：**2026年08月25日 00:00

AI 解读

ANY.RUN研究称，2024年至2026年间，商业化钓鱼即服务工具Mirage2FA波及美国及欧洲等地，关联4,532个组织邮箱域名，其中美国受害者占63.7%，科技、制造和教育行业较为集中。该活动通过仿冒并滥用Microsoft 365合法登录流程，窃取密码与会话Cookie，绕过双因素认证，研究发现超过9,000起涉及凭据、Cookie、SSO登录和2FA绕过的潜在事件，48%的目标邮箱可能已遭入侵。攻击者劫持已认证会话后，可访问Microsoft 365及SSO关联服务，带来企业邮件、业务账户和敏感数据暴露风险，并为冒充、欺诈及进一步入侵创造条件。

原文：https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html

### 08 Marimo Notebook漏洞：编辑模式下可在单元格执行前运行MCP命令

**公开时间：**2026年08月25日 00:00

AI 解读

Marimo修复了一个高危笔记本软件漏洞CVE-2026-75149，属于代码注入问题，影响0.23.15之前版本。攻击者可借特制笔记本，在受害者于编辑模式打开时，通过笔记本配置提供攻击者控制的MCP服务器命令，并在任何单元格执行前作为本地子进程运行。CVSS v4评分为8.7，v3.1为8.8，需用户交互且无需认证。修复版0.23.15于7月23日发布，CVE于8月19日公布。漏洞由Gregory Tan（Grg0rry）发现。修复补丁将笔记本元数据视为攻击者可控，并通过白名单移除ai、mcp等配置段。另有一个关联的CVE-2026-67618漏洞（CVSS 7.1），涉及攻击者通过笔记本元数据提供AI base\_url，在操作者发出AI请求时，配置端点可获取API密钥而无需执行单元格。此外，更早的CVE-2026-39987漏洞影响0.20.4及更早版本，缺失/terminal/ws端点认证验证，可导致获取完整PTY shell并执行任意命令，0.23.0版本已修复。

原文：https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html

### 09 前沿 AI：漏洞管理的系统性变革

**公开时间：**2026年08月25日 00:00

AI 解读

文章指出，以Anthropic Mythos为代表的前沿AI模型正从根本上改变漏洞管理领域，其能识别零日漏洞、串联复杂利用链并实时适应，迫使现有漏洞管理程序反思是否已做好准备。许多组织现有程序本就脆弱，漏洞积压严重，尚远未过渡至CTEM模式，因而应对不足。文章主张漏洞与补丁管理团队需打破各自为政，协同升级。仅依赖CVSS、EPSS及CISA KEV清单已不够，因前沿AI正以机器速度将漏洞武器化，需引入暴露管理职能，综合评估攻击面真实风险、可利用性与业务影响，并纳入错误配置、可达性及威胁情报，借助持续监控、入侵与攻击模拟及自动化渗透测试来验证。补丁管理亦需革命，从等待Patch Tuesday转向基于环状方法的自动化识别、测试与部署，以匹配机器速度，但这可能打破可用性与停机要求的既有平衡，需与业务方就停机要求、弹性投资及灾备集成提前开展艰难对话。文章最终为作者所授SANS LDR516课程作宣传。

原文：https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html

### 10 E4del 与 PINHOLE RAT 将 FTP Banner 变成传递恶意软件命令的“死信箱

**公开时间：**2026年08月25日 00:00

AI 解读

SOCRadar披露一项利用FTP服务器欢迎横幅充当“死信解析器”的恶意活动，这是该技术首次被发现用于野外攻击。攻击者通过西班牙语诱饵和LNK快捷方式诱导用户执行命令，再从FTP横幅获取后续指令，投递Node.js远控木马E4del；另一木马PINHOLE则结合Pinterest、SurveyMonkey及Cloudflare Workers解析并代理C2通信。两者均具备下载执行文件、窃取文件、截图、运行PowerShell等能力，并通过多阶段加载、加密通信、进程注入和动态通信间隔规避检测。研究人员认为该方式隐蔽性低于传统Web解析器，相关活动当时仍处于早期阶段。

原文：https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html

### 11 攻击者瞄准 miniOrange SAML 漏洞，可获取 WordPress 管理员权限

**公开时间：**2026年08月25日 00:00

AI 解读

攻击者正利用 Xecurify miniOrange SAML 2.0 Single Sign-On 插件的两个未授权认证绕过漏洞，冒充任意 WordPress 用户登录，包括管理员。CVE-2026-61979（CVSS 8.1）源于签名算法混淆，CVE-2026-15981（CVSS 9.8）则因插件将 PHP openssl\_verify() 返回的错误值误判为验证成功；攻击者可提交带有自控 NameID 和畸形签名的 SAMLResponse，触发 wp\_set\_auth\_cookie() 获取目标账户会话。Patchstack 已观察到来自多个 IP 的扫描，认为更像针对安装该插件网站的机会主义批量扫描；相关漏洞已有 PoC，可能导致受影响站点被接管。

原文：https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html

### 12 遭积极利用的 Oracle WebLogic 漏洞可让未认证攻击者访问关键数据

**公开时间：**2026年08月25日 00:00

AI 解读

美国CISA于8月25日将影响Oracle HTTP Server和WebLogic Server的CVE-2026-21962（CVSS 10.0）纳入已知被利用漏洞目录，称存在活跃利用。该不当访问控制漏洞允许未认证攻击者通过HTTP网络访问，导致未授权访问或修改关键数据。Oracle已于1月发布补丁，但据GreyNoise和CloudSEK报告，此后仍遭活跃利用；2月发现单一IP尝试利用多个已知漏洞，3月CloudSEK蜜罐捕获针对该漏洞及多个旧版WebLogic RCE漏洞的攻击。依据BOD 26-04，联邦机构被建议在8月27日前完成修复。

原文：https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html

## HackerOne

昨日暂无符合标准的漏洞发布

![一个不正经的黑客 · 全球安全动态与知识分享](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0wxk6alKwgl2znYoglw9fzyQU1dNd3QicIdQ2gekg7VXOz7LPmL1Kl2dpO5I60zgwgGuO6fVrTAo2PpLibVdWOo4OZYc7FQ4W7Q/640?from=appmsg)![]()

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