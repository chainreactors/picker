---
title: 网络安全日报 | 2026-07-15
url: https://mp.weixin.qq.com/s/5i0uzkCgYM2QiPvZDojRRQ
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:55:41.931845
---

# 网络安全日报 | 2026-07-15

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibWuEZyvfHZEfZJZH4gBvK40elKQfxzTG8MZu7DO06zickwyWu5iaric29BdWicpc1PKZjW7Ehk67hL86ic1QibLjCjfuOmRSvpLZULofttKLnPqBQ/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-15

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月15日（星期三） | 数据来源：NVD / CISA KEV / Oracle / Microsoft MSRC / SonicWall PSIRT / ServiceNow / Broadcom / The Hacker News / SecurityWeek / BleepingComputer / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 2 极危事件 | 2 高危事件 | 2 中危事件 | 5 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：CISA KEV 7月14日一口气新增4个在野利用漏洞——SonicWall SMA1000双CVE（CVE-2026-15409/15410）+ Microsoft ADFS（CVE-2026-56155）+ SharePoint Server（CVE-2026-56164），联邦机构须在7月17日前完成修复或下线**

**🔴 极危：Oracle 7月关键安全补丁更新（CPU）披露第二个PeopleSoft未认证RCE CVE-2026-35278（CVSS 9.8），ShinyHunters已将CVE-2026-35273与该漏洞链式利用，攻陷300+实例、100+组织（以高等教育为主）**

**🟠 高危：ServiceNow AI Platform未认证沙箱逃逸RCE CVE-2026-6875（CVSS 9.5）披露（Assetnote，07-13），可绕过隔离层在实例内执行任意代码，影响Brazil/Australia/Zurich/Yokohama全系**

**🟠 高危：Microsoft 7月补丁星期二修复622个CVE（57个Critical），其中2个零日已在野利用（ADFS CVE-2026-56155 + SharePoint CVE-2026-56164）；SharePoint被链式为RCE并窃取IIS机器密钥实现持久化**

**🟡 中危：VMware Avi Load Balancer 7个漏洞含关键认证绕过CVE-2026-47865（Broadcom 07-14）；Progress ShareFile紧急关停持续发酵（CVE-2026-2699/2701链式RCE，厂商停用Storage Zone Controller账户）**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

CISA KEV 7月14日新增4个在野利用漏洞 — SonicWall SMA1000双CVE（CVE-2026-15409/15410）+ Microsoft ADFS（CVE-2026-56155）+ SharePoint Server（CVE-2026-56164），联邦7月17日前须修复

📰 CISA / SonicWall PSIRT / Microsoft MSRC · 📅 2026-07-14

CISA于7月14日将4个已确认在野利用的漏洞加入KEV目录：SonicWall SMA1000设备的服务端请求伪造CVE-2026-15409与代码注入CVE-2026-15410、Microsoft Active Directory Federation Services（ADFS）访问控制粒度不足CVE-2026-56155、Microsoft SharePoint Server关键功能缺失认证CVE-2026-56164。联邦机构修复/下线截止日为7月17日（仅3天）。SMA1000是直接面向互联网的远程接入网关，被攻陷即直入内网；SharePoint漏洞被攻击者链式为RCE并窃取IIS机器密钥实现持久化。这是7月以来罕见单日KEV四连发，边界设备与身份/协作平台成为重点靶心。

Oracle 7月关键安全补丁更新（CPU）披露第二个PeopleSoft未认证RCE CVE-2026-35278（CVSS 9.8）— ShinyHunters将CVE-2026-35273与该漏洞链式利用，攻陷300+实例、100+组织

📰 Oracle / GTIG(Mandiant) / Arctic Wolf · 📅 2026-07-14

Oracle 7月2026 CPU修复CVE-2026-35278（CVSS 9.8），这是PeopleSoft PeopleTools Performance Monitor组件的第二个未认证RCE（CWE-306关键功能缺失认证），与已遭ShinyHunters利用的CVE-2026-35273链式组合，形成"未认证RCE→数据窃取"完整管道。GTIG/Mandiant确认攻击窗口为5月27日–6月9日（早于6月10日官方公告），已攻陷300+实例、100+组织（以高等教育为主），后期利用MeshCentral C2（azurenetfiles[.]net）、SSH spray fanout脚本窃取HR/薪资/PII，并在PeopleSoft目录植入README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT标记文件。同期Oracle还修复5个关键CVE：WebLogic CVE-2026-35263（9.9）、Identity Manager CVE-2026-35268（9.9）、WebCenter CVE-2026-35270/35280/35281（9.1–9.9）。

ServiceNow AI Platform未认证沙箱逃逸RCE CVE-2026-6875（CVSS 9.5）披露 — Assetnote研究员Adam Kues发现，可绕过隔离层在实例内执行任意代码，影响全系发布家族

📰 ServiceNow / Searchlight Cyber(Assetnote) / Secure.com · 📅 2026-07-13

ServiceNow于7月13日发布KB3137947，修复AI Platform中的预认证沙箱逃逸漏洞CVE-2026-6875（CVSS 4.0评分9.5，Critical）。该漏洞位于Now Assist等生成式AI功能依赖的隔离沙箱层，未认证攻击者可逃逸沙箱在ServiceNow实例内执行任意代码，进而窃取业务数据、篡改工作流、 harvest API令牌与凭据并横向移动至所有关联系统。Assetnote披露利用链借助Rhino引擎glueController().evaluateAsObject绕过限制执行代码。影响Brazil/Australia/Zurich/Yokohama全系；托管实例已由ServiceNow自动更新，自托管/伙伴部署须手动升级。截至披露尚无已知在野利用，但严重性要求立即加固。

Microsoft 7月补丁星期二修复622个CVE（57个Critical）— 2个零日已在野利用（ADFS CVE-2026-56155 + SharePoint CVE-2026-56164），SharePoint被链式为RCE窃取IIS机器密钥

📰 Microsoft MSRC / Zero Day Initiative / Cisco Talos / Expel · 📅 2026-07-14

Microsoft 7月补丁星期二修复622个漏洞（57个Critical，含143个RCE类），数量显著高于6月的206个。其中两个已在野利用：ADFS CVE-2026-56155（CVSS 7.8，访问控制粒度不足→本地提权至管理员）与SharePoint Server CVE-2026-56164（CVSS 5.3，关键功能缺失认证）。CISA在补丁发布数小时内将二者加入KEV，并警告攻击者将CVE-2026-56164与CVE-2026-32201、CVE-2026-45659链式组合实现未认证RCE，窃取IIS机器密钥（用于签名/加密的密钥）后即使打补丁仍可伪造可信请求保持持久化。CISA要求启用AMSI Full Mode并修补后轮换IIS机器密钥。其余重点含Azure OpenAI CVE-2026-45499（9.9）、AD CS CVE-2026-54121（8.8）、DHCP Server双RCE（8.8）。

VMware Avi Load Balancer 7个漏洞含关键认证绕过CVE-2026-47865 — Broadcom 7月14日发布修复，无凭据即可认证绕过/RCE/提权/目录遍历

📰 Broadcom / VMware / SecurityWeek · 📅 2026-07-14

Broadcom于7月14日发布VMware Avi Load Balancer的7个安全漏洞修复，其中关键认证绕过漏洞CVE-2026-47865最为严重。成功利用可实现认证绕过、远程代码执行、权限提升与目录遍历，且无需有效凭据。Avi Load Balancer广泛用于本地与云环境的流量负载均衡与应用交付，暴露在外的控制台与管理接口一旦被攻陷，攻击者可进一步深入后端应用与内部网络。运行Avi Load Balancer的企业（尤其面向互联网部署）应立即应用Broadcom补丁，并临时限制管理接口的网络可达性作为缓解。

Claude for Chrome缺陷披露：任意浏览器扩展可触发Agent任务访问Gmail/Docs/Calendar — AI Agent攻击面扩大，Anthropic已被告知

📰 The Hacker News / 研究者披露 · 📅 2026-07-14

研究者披露Claude for Chrome存在设计缺陷：任何在claude.ai页面拥有脚本执行权限的浏览器扩展，均可在用户不知情/未同意的情况下，触发Claude for Chrome的Agent任务，定向访问用户的Gmail、Google Docs与Google Calendar。根因在于Claude for Chrome扩展与其他浏览器扩展之间隔离不足。这是继GhostCommit（PNG图像隐藏提示注入攻击AI编码代理）之后，又一起将AI Agent作为攻击面的代表性事件，凸显"Agent被第三方扩展/网页诱导执行敏感操作"的新型风险。用户应审查已安装扩展权限，Anthropic已获通知。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 5 条 |

CVE-2026-35278CVSS 9.8

**受影响产品：**Oracle PeopleSoft Enterprise PT PeopleTools 8.61 / 8.62（Performance Monitor组件）。PeopleTools是PeopleSoft企业应用的核心开发与运维平台，承载HR/薪资/财务等敏感业务，全球大量高校与大型企业部署且多面向互联网

**漏洞描述：**CWE-306 关键功能缺失认证 — Performance Monitor组件的HTTP入口未对未认证请求做访问控制→未认证远程攻击者经HTTP发送恶意请求即被当作受信任的内部调用解析→突破PeopleTools身份验证边界→获取系统级控制权→攻击链：网络发送特制HTTP请求至Performance Monitor→绕过认证→接管PeopleTools→与已利用的CVE-2026-35273链式组合→未认证RCE→数据窃取管道

**利用状态：**Oracle 7月2026 CPU(07-15)修复→CVSS 9.8 Network/No privileges/No interaction→ShinyHunters已确认将CVE-2026-35273+CVE-2026-35278链式利用→攻陷300+实例/100+组织（高等教育为主）→GTIG/Mandiant确认利用窗口5-27至6-9→MeshCentral C2(azurenetfiles[.]net)→影响所有面向互联网的PeopleSoft实例→高危持续活跃  ·  **补丁状态：**Oracle 7月2026 Critical Security Patch Update（cspujun2026）修复→①立即应用PeopleTools 8.61/8.62补丁→②将PeopleSoft HTTP端点限制于受信任网络/不暴露公网→③排查/PSIGW/HttpListeningConnector等利用URI与README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT标记→④阻断攻击IP(142.11.200.186-190/108.174.202.99/176.120.22.24)与azurenetfiles[.]net→⑤复查HR/薪资/PII数据泄露→⑥对PeopleSoft主机监控445出站NetNTLM胁迫

CVE-2026-6875CVSS 9.5

**受影响产品：**ServiceNow AI Platform（Now Assist等生成式AI功能依赖的隔离沙箱层），影响Brazil（EA/GA）、Australia（Patch 2）、Zurich（Patch 7b/9）、Yokohama（Patch 12 HF 1b / Patch 13）等全系发布家族。ServiceNow连接身份系统/云/终端/内部业务应用，是企业核心工作流中枢

**漏洞描述：**CWE-? 沙箱逃逸（预认证RCE）— 隔离沙箱本应将不可信AI代码限制在受控环境→漏洞使代码逃逸至沙箱外执行→未认证攻击者经特定条件触发→借助Rhino引擎GlideController().evaluateAsObject('...')执行任意代码（如gs.addInfoMessage）→攻击链：预认证请求→绕过沙箱隔离→Rhino引擎执行任意JS→实例内任意代码执行→窃取业务数据/篡改工作流/harvest API令牌→横向移动至关联系统

**利用状态：**ServiceNow 07-13披露(KB3137947)→CVSS 9.5(CVSS 4.0) Network/无需认证→截至披露无已知在野利用（但严重性高、公开后即可能被逆向）→影响所有面向互联网的ServiceNow实例→暴露面大、潜在爆炸半径广→须立即加固  ·  **补丁状态：**ServiceNow修复（托管实例已自动更新）→①自托管/伙伴部署核对家族并升级至修复版本（Brazil EA/GA、Australia Patch 2、Zurich Patch 7b/9、Yokohama Patch 12 HF 1b/13）→②验证托管实例已收到更新→③限制AI Platform端点网络可达性→④审查管理员活动/集成凭据/API使用/工作流变更异常→⑤ServiceNow引入Guarded Script（仅允许单表达式）强化沙箱

CVE-2026-56155CVSS 7.8

**受影响产品：**Microsoft Active Directory Federation Services（AD FS）15个Windows版本（含Windows Server 2012起多代），作为企业单点登录(SSO)令牌分发组件，广泛连接应用与数据

**漏洞描述：**CWE-269/CWE-285 访问控制粒度不足（权限提升）— ADFS对访问授权的粒度控制不足→已授权攻击者可得比预期更多的访问→本地提权至管理员→攻击链：利用访问控制缺陷→提升本地权限至管理员→接触本不应触及的应用与数据→SSO令牌层面的越权

**利用状态：**CISA KEV 07-14新增 + 确认在野利用→CVSS 7.8 Local/需低权限→补丁发布数小时内即入KEV→影响多代Windows Server（回溯至2012）→ADFS作为SSO枢纽一旦被提权可横向触及大量业务系统→高危活跃  ·  **补丁状态：**Microsoft 7月补丁修复→①立即修补ADFS（优先于暴露面排序）→②审查ADFS信任关系与授权策略粒度→③监控异常令牌签发与权限提升→④对ADFS服务器启用EDR与日志审计→⑤按暴露面优先修复域控/暴露服务器

CVE-2026-56164CVSS 5.3

**受影响产品：**Microsoft SharePoint Server（本地部署Subscription Edition / 2019 / 2016），承载企业文档协作与内部门户，多面向互联网且常存历史攻击面

**漏洞描述：**CWE-306 关键功能缺失认证（权限提升/欺骗）— SharePoint Server关键功能缺失认证→未授权攻击者可经网络提升权限→攻击链：缺失认证入口→未授权提权→与CVE-2026-32201、CVE-2026-45659链式组合→远程代码执行→窃取IIS机器密钥（SharePoint签名/加密用密钥）→伪造可信请求持久化

**利用状态：**CISA KEV 07-14新增 + 确认在野利用（CVSS 5.3 Moderate但已武器化）→攻击者链式CVE-2026-32201/45659实现未认证RCE→窃取IIS机器密钥后即使打补丁仍可保持访问→CISA要求启用AMSI Full Mode并轮换密钥→所有受支持本地版均受影响→高危活跃  ·  **补丁状态：**Microsoft 7月补丁修复 + CISA强化指引→①立即修补所有本地SharePoint版→②启用Antimalware Scan Interface(AMSI) Full Mode→③修补后必须轮换IIS机器密钥（被盗密钥可幸存于更新）→④假设已遭尝试入侵，猎杀CISA所述恶意软件与WebShell→⑤审查IIS配置与异常请求

CVE-2026-15409CVSS 9.8

**受影响产品：**SonicWall SMA1000系列安全移动接入设备（SMA1000 Appliances），直接面向互联网、为企业员工与承包商提供远程接入的内部网络网关

**漏洞描述：**CWE-918 服务端请求伪造(SSRF) + CVE-2026-15410 代码注入 — CVE-2026-15409为未认证SSRF，使设备代攻击者为非预期请求（常达内网不可达系统）；CVE-2026-15410为需管...