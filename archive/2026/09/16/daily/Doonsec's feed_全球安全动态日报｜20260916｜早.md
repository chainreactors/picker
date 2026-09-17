---
title: 全球安全动态日报｜20260916｜早
url: https://mp.weixin.qq.com/s/KHx7IdSGYSw0Q4idmzvlig
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:53:53.026191
---

# 全球安全动态日报｜20260916｜早

# 全球安全动态日报｜20260916｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260916｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年9月15日共收录14条安全动态，内容涵盖多起漏洞利用与恶意软件活动涉及机密计算、Gitea、WordPress、Chrome及银行木马等领域。

The Hacker News **14**  ·  HackerOne **0**

## The Hacker News

### 01 新型 DDRop 攻击攻破英特尔 TDX 和 AMD SEV-SNP 机密计算技术

**公开时间：**2026年09月15日 02:02

AI 解读

研究人员披露硬件攻击DDRop：攻击者若已控制服务器软件并短暂取得物理访问，可在处理器与DDR5内存之间接入成本低于200美元的中间板，静默丢弃写入，使系统继续读取仍能通过加密校验的旧数据。该攻击利用Intel TDX、Scalable SGX和AMD SEV-SNP为支持大规模内存加密而缺少新鲜度检查的设计缺陷；研究者在TDX上实现了受保护虚拟机内存读取、调试模式切换及伪造远程证明，在SEV-SNP上实现页面内容复制。TDX更强的加密完整性模式可阻止部分跨虚拟机攻击，但不能确认旧内容是否被复用。研究者称尚无实验室外利用证据，英特尔和AMD认为物理攻击不在其既定威胁模型内。

原文：https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html

### 02 3BB攻击者利用 MeshCentral 后门获取根权限，窃取用户凭据

**公开时间：**2026年09月15日 02:01

AI 解读

Hunt.io披露，泰国主要宽带服务商3BB遭入侵：攻击者利用MeshCentral合法远程管理工具作隐蔽后门，在内部机器维持root级远程控制。事件因攻击者暴露在互联网的服务器被发现，捕获于2026年6月3日，服务器存有攻击工具及受控设备列表，工具曾在3BB网络内执行。MeshCentral被配置成隐藏后门，回连攻击者控制的www.ayuthayatech[.]com，设备组名TH-3BB；清理脚本会抹日志并删除其他工具但保留agent。攻击者借此对超过55台内网主机喷洒SSH口令、探测内部销售门户、搜集存储凭据，并可用webshell及SSH密钥留后路。其主要目标是3BB的RADIUS用户凭据数据库：相关脚本针对复制该库，但证据只能说明被瞄准，无法确认数据外泄。服务器上另有3BB有效VPN证书与Jasmine网络会话，疑似同时针对两者；Jasmine是否被入侵未证实。初始入口未确定：工具包含针对FortiGate SSL-VPN的CVE-2024-21762完整exploit，相关网关固件受影响，但无证据表明利用成功。攻击者已关闭暴露目录，目前是否仍有权限未知。

原文：https://thehackernews.com/2026/09/3bb-attacker-used-meshcentral-backdoor.html

### 03 Telegram Desktop 漏洞可让隐藏的 JavaScript 从 HTML 导出文件中窃取消息

**公开时间：**2026年09月15日 01:58

AI 解读

ExPatch研究人员9月12日披露，Telegram Desktop的HTML导出功能存在漏洞：机器人可在消息按钮文本中植入脚本标签，利用此前未转义的导出代码。用户将聊天导出为HTML后用浏览器打开时，脚本无需点击即运行，可窃取该文件内全部消息、发送者、时间戳、聊天名称、成员数及本地路径并发送至攻击者服务器，也可篡改页面显示（如替换为伪造验证表单），但不影响Telegram服务器副本和磁盘文件。导出每1000条消息分文件，故单文件仅暴露自身内容。利用需满足：导出由修复前版本生成、含该消息且浏览器启用JavaScript。修复commit 8457d13a于7月14日随7.0.1稳定版发布，但旧导出仍含脚本。研究人员评分CVSS 3.1为8.2，无CVE。

原文：https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html

### 04 Red Heron 利用 Gitea 远程代码执行漏洞，入侵六国 13 个组织

**公开时间：**2026年09月15日 00:56

AI 解读

疑似与中\*有关的威胁组织“红鹭”（Red Heron）在Gitea漏洞CVE-2026-60004披露后迅速将公开PoC改造成自动化框架，扫描七国1,386个实例，并确认入侵加拿大、阿根廷、中\*台湾、美国、卡塔尔和斯里兰卡共13个组织。其活动涉及源代码、凭据和配置数据窃取、持久化及横向移动，部分目标获得Proxmox集群根级权限。攻击者还部署了具备30多项后渗透功能的Linux木马JITTERLY及可隐藏文件、进程和网络连接的SIXZUT rootkit，目标覆盖国防、选举、能源、政府、电信和科研等领域。

原文：https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html

### 05 WordPress 增加自动化插件审查，在发布前阻止高风险更新

**公开时间：**2026年09月15日 00:00

AI 解读

WordPress宣布对插件每个版本在通过WordPress.org更新API分发前进行自动安全审查，以弥补插件更新缺乏持续审核的空档。审查在现有冷却期内由AI模型和Jetpack Scan分析变更并生成风险评分，高风险版本将自动暂停分发，低于阈值的版本继续正常流程。该机制曾于2026年7月28日检测出一个约有2万活跃安装的插件版本包含后门，使其未通过更新API发布。高风险评分既可能源于恶意代码，也可能来自无意引入的漏洞。

原文：https://thehackernews.com/2026/09/wordpress-adds-automated-plugin-reviews.html

### 06 KREMLIN银行木马劫持Chrome和Edge浏览器，窃取凭据与会话令牌

**公开时间：**2026年09月15日 00:00

AI 解读

Elastic Security Labs披露了一项至少自2025年5月活跃、针对巴西用户的银行木马行动REF9334，攻击者冒充约12家巴西银行，通过多阶段JavaScript加载器、C++安装器和恶意Chrome/Edge扩展投递KREMLIN。该恶意软件利用以太坊智能合约动态解析C2及载荷地址，并篡改浏览器Secure Preferences和相关校验信息绕过扩展完整性机制。扩展可窃取凭据、Cookie、会话及本地存储、浏览历史、页面HTML、标签信息和截图，并支持页面重定向及请求拦截。行动已关联至少7次活动；研究人员发现1515台系统访问其网络探针，其中98%以上位于巴西。

原文：https://thehackernews.com/2026/09/kremlin-banking-malware-hijacks-chrome.html

### 07 伊朗黑客利用Telegram控制的恶意软件监视异见人士和记者

**公开时间：**2026年09月15日 00:00

AI 解读

美国、英国和荷兰机构称，伊朗情报部门自2023年秋季起使用仅针对Windows的恶意软件HEAVYGRAM（英国称CHOSEN BRICK），主要监视海外伊朗异议人士、反政府记者和活动人士，相关行动至少自2025年持续。攻击者通过冒充熟人、技术支持或合法软件发送文件，诱导受害者运行后以Telegram机器人控制，窃取邮件、聊天记录、密码等，截屏并开启麦克风录音，还可下载其他恶意软件、删除或擦除设备。机构称，窃取信息可能暴露受害者的联系人、位置和日常活动，并被发布到亲伊朗泄密网站，增加人身安全风险。

原文：https://thehackernews.com/2026/09/iranian-hackers-use-telegram-controlled.html

### 08 BambooToken恶意软件利用MQTT控制Windows和Linux系统

**公开时间：**2026年09月15日 00:00

AI 解读

安全研究人员披露了跨平台恶意软件BambooToken，其至少自2023年2月活跃，近期活动持续至2026年7月，主要针对亚洲和南美组织。该恶意软件利用Tendyron OnKey软件实施DLL侧加载，在Windows和Linux主机上通过MQTT发布/订阅协议与控制端通信，收集系统信息并接收插件加载、停止插件、终止运行等指令；其Windows插件还借助WMI获取已安装的杀毒软件信息。基础设施使用Cloudflare代理，受害者涉及移动应用、金融、酒店、医疗等机构，研究人员认为行动可能支持大规模数据收集，但幕后组织尚未确定。

原文：https://thehackernews.com/2026/09/bambootoken-malware-uses-mqtt-to.html

### 09 人类攻击者利用 Marimo 远程代码执行漏洞，在 8 秒内攻入 SSH 堡垒机

**公开时间：**2026年09月15日 00:00

AI 解读

Sysdig披露，一名熟练攻击者利用Marimo所有版本受影响的高危未授权远程代码执行漏洞CVE-2026-39987，在取得初始访问后仅用8秒从受害笔记本转移至SSH堡垒主机。攻击者手工编写Python工具，先获取交互式Shell，再调用AWS Secrets Manager取得凭据和私钥并完成SSH登录；其持续约9小时、执行逾850条命令，未使用可识别的公开攻击工具。该案例表明，熟练人工操作者已能达到类似AI辅助攻击的速度，并可能更善于规避检测。文章还提到，另一场活动利用Redis配置弱点部署挖矿程序，已影响3562台服务器。

原文：https://thehackernews.com/2026/09/human-attacker-exploits-marimo-rce.html

### 10 大规模扫描活动利用 Vite 漏洞从暴露的开发服务器中窃取云凭据

**公开时间：**2026年09月15日 00:00

AI 解读

安全研究人员披露针对Vite部署的大规模扫描活动，利用CVE-2026-39364（CVSS 8.2）窃取云端凭证。该漏洞允许未认证攻击者向/@fs/端点发送带?raw、?import&raw等查询参数的HTTP请求，绕过server.fs.deny限制，获取.env、证书等敏感文件内容。触发需满足三个条件：开发者以--host或server.host暴露dev server、敏感文件位于server.fs.allow目录、且被server.fs.deny匹配。F5 Labs观测到2026年8月的活动，目标包括AWS/Azure凭证、环境配置、terraform.tfstate等基础设施状态文件、/etc/passwd及进程环境。攻击者使用仿冒Googlebot等的User-Agent和伪造X-Forwarded-For头规避访问控制，主要来源为美国、比利时、荷兰、新加坡、台湾，并使用GCP IP段。

原文：https://thehackernews.com/2026/09/mass-scanning-campaign-exploits-vite.html

### 11 攻击链，而不仅仅是攻击面：为何测试单一技术会错失重点

**公开时间：**2026年09月15日 00:00

AI 解读

安全团队通常针对EDR、钓鱼模拟、SIEM规则等单点技术进行测试，但文章指出真实攻击者（越来越多AI驱动）是链式行动：钓鱼→凭据窃取→初始立足→提权→横向移动→数据暂存与外渗。单步可能被某控制捕获，但整个链条能从工具/团队/告警的缝隙穿过。Filigran报告称93%安全领导称过去12个月遭遇业务影响攻击，88%称AI加速攻击者内部移动，84%归因于工具孤立与脱节测试；2025年法国DGFiP入侵即由普通步骤串成重大事件。为此文章介绍OpenAEV的“攻击链”（Attack Chaining）场景：自动化多阶段路径，用前一步真实输出（凭据、端口、令牌、配置）实时决定后续分支，在交互图呈现，可识别卡点；范围可控，社交工程作为链节点；支持操作员主导或XTM One AI自主规划执行，以接近红队的真实感持续运行。

原文：https://thehackernews.com/2026/09/attack-chains-not-just-attack-surfaces.html

### 12 LiteSpeed Enterprise 漏洞可能允许单个主机账户在共享服务器上获取 Root 权限

**公开时间：**2026年09月15日 00:00

AI 解读

cPanel于9月14日警告，LiteSpeed Web Server Enterprise 6.3.7之前版本存在严重权限提升漏洞，共享主机上的低权限网站账户可能绕过包括CloudLinux CageFS在内的账户隔离机制，访问或修改其他网站及服务器并取得root权限。厂商未公开漏洞原理、对应修复项、CVE编号、严重性评分或是否已遭利用；公告仅涉及Enterprise版，未说明OpenLiteSpeed受影响情况。该漏洞是5月以来第三起被指可令cPanel主机账户获得root权限的LiteSpeed相关问题，但首次涉及Web服务器本身。

原文：https://thehackernews.com/2026/09/litespeed-enterprise-flaw-could-let-one.html

### 13 思科安全邮件网关漏洞已遭在野利用，可实现 Root 命令执行

**公开时间：**2026年09月15日 00:00

AI 解读

Cisco警告其Secure Email Gateway所用AsyncOS软件存在高危漏洞CVE-2026-76461，CVSS评分9.8，已被在野利用。漏洞源于邮件解析逻辑验证不足，未认证远程攻击者可通过向受影响设备发送含恶意SQL语句的构造邮件，执行任意SQL并最终以root权限在底层操作系统上执行命令。该漏洞影响物理与虚拟Secure Email Gateway，与设备配置无关；Secure Email and Web Manager及Secure Web Appliance不受影响。Cisco已针对AsyncOS多个版本提供修复，无变通方案。Cisco本月发现活跃利用并公布入侵指标，还直接联系了检测到恶意活动的云设备客户，但未披露攻击规模。由于攻击者可获root权限，可能清除或隐藏利用痕迹。CISA已将CVE-2026-76461列入KEV目录，要求联邦机构9月17日前\*。另据报道，Arctic Wolf在8月26至28日发现针对Fortinet VPN的大规模凭据攻击，利用组织特定身份信息，成功认证后出现恶意活动。

原文：https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html

### 14 与中\*有关的黑客利用 Chrome-Windows 零日漏洞链部署 GRIMWEDGE

**公开时间：**2026年09月15日 00:00

AI 解读

Volexity称，疑似中\*关联组织UTA0560于2026年9月1日通过鱼叉式钓鱼邮件，利用美国大学网站反射型XSS将受害者引向攻击基础设施，并串联两个Chrome漏洞（CVE-2026-85046、CVE-2026-87491）与Windows ALPC漏洞（CVE-2026-85880）突破浏览器沙箱、实现代码执行，投递JavaScript后门GRIMWEDGE。该后门可侦察主机、管理文件和进程、执行命令及下载载荷，但缺乏内置持久化、横向移动和独立外传能力。Volexity还观察到APT31使用同一链投递SUPERSTOMP和窃密扩展LONGTALE；多组织近同时使用该链，可能表明其被共享或出售。Chrome补丁未及时纳入稳定版本形成的“补丁窗口”扩大了攻击机会。

原文：https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html

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