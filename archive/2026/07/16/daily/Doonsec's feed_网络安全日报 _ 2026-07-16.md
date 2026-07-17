---
title: 网络安全日报 | 2026-07-16
url: https://mp.weixin.qq.com/s/Nn-gISZ1EJSsx4IFPCi-3Q
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:19.549755
---

# 网络安全日报 | 2026-07-16

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibWuEZyvfHZHZS7pcdbBK0KbgtpvymguJAOqjUY4D3aqwAC8dXZS4UsCdUyPYb2VeynbibOkqtY2hzYK0pTNUgMgb9GicGqMOZJjK9LmRFiaERk/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-16

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月16日（星期四） | 数据来源：NVD / CISA KEV / SAP / Microsoft MSRC / Siemens / Rapid7 / Miggo / Socket / The Hacker News / BleepingComputer / SecurityWeek / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 2 极危事件 | 2 高危事件 | 2 中危事件 | 7 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：CISA KEV 7月14日四连发仍在修复窗口内——SonicWall SMA1000双CVE（CVE-2026-15409/15410）、Microsoft ADFS（CVE-2026-56155）、SharePoint（CVE-2026-56164）联邦机构须于7月17日前修复或下线，SMA1000已确认在野利用**

**🔴 极危：Oracle 7月CPU第二个PeopleSoft未认证RCE CVE-2026-35278（CVSS 9.8）被ShinyHunters与CVE-2026-35273链式利用，已攻陷300+实例/100+组织（以高等教育为主），威胁持续活跃**

**🟠 高危：Microsoft 7月补丁补充披露——SharePoint新零日CVE-2026-55040（CVSS 9.1，弱JWT验证未认证认证绕过→RCE，Pwn2Own Berlin）+ Windows RDP蠕虫级CVE-2026-56190（CVSS 9.8）+ VMSwitch CVE-2026-57092（CVSS 9.9）**

**🟠 高危：SAP 7月补丁日修复NetWeaver ABAP内存破坏CVE-2026-44747（CVSS 9.9），Siemens Opcenter X爆出JWT算法混淆认证绕过CVE-2026-56451（CVSS 10.0），制造业OT/ERP暴露面风险骤升**

**🟡 中危：AsyncAPI npm供应链攻击经GitHub Actions投毒投送Miasma RAT（5个包/2.7M周下载）+ RabbitMQ双漏洞CVE-2026-57219（8.7，窃取OAuth密钥接管Broker）/CVE-2026-57221（5.3，多租户隔离绕过）**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

Microsoft 7月补丁补充：SharePoint新零日CVE-2026-55040（CVSS 9.1）+ Windows RDP蠕虫级CVE-2026-56190（9.8）+ VMSwitch CVE-2026-57092（9.9）

📰 Microsoft MSRC / Rapid7 / BleepingComputer / HKCERT · 📅 2026-07-15

在7月14日622 CVE的纪录性补丁星期二之外，Rapid7于7月15日披露SharePoint新零日CVE-2026-55040（CVSS 9.1），根因是弱JWT令牌验证——未认证远程攻击者可凭已知AD Security ID或UPN冒充任意站点用户，并在Pwn2Own Berlin中与另一RCE组合实现未认证RCE（RCE组件微软定于8月补丁周期修复）。同日多家机构细化7月补丁中的关键项：Windows RDP CVE-2026-56190（CVSS 9.8，未初始化资源，无需认证即可网络RCE，BlueKeep级蠕虫特征，应最高优先级）与Windows VMSwitch CVE-2026-57092（CVSS 9.9，UAF权限提升，可触发Hyper-V虚拟机逃逸）。HKCERT建议互联网暴露的RDP/VMSwitch优先修补。

SAP 7月补丁日：NetWeaver ABAP内存破坏CVE-2026-44747（CVSS 9.9）+ Approuter走私 + Commerce Cloud硬编码OAuth2凭据

📰 SAP / CyberSecBrief / Enigma Global · 📅 2026-07-15

SAP在7月补丁日发布20条安全通告，头号CVE-2026-44747为NetWeaver Application Server ABAP内存破坏漏洞（CVSS 9.9），影响大量承载企业核心ERP的NetWeaver实例。第二条CVE-2026-27690为Approuter的HTTP请求走私（非Cloud Foundry部署，CVSS 9.1），第三条CVE-2026-44761为Commerce Cloud示例脚本中硬编码OAuth2凭据（CVSS 9.1）。SAP同时发布6条高危通告覆盖Integration Suite、SAProuter、NetWeaver Java等。NetWeaver作为企业ERP枢纽，一旦被未授权RCE将直接威胁财务/供应链数据，须立即排查暴露面。

AsyncAPI npm供应链攻击：5个包经GitHub Actions投毒投送Miasma RAT，含2.7M周下载量的specs包

📰 Socket / CyberSecBrief · 📅 2026-07-15

Socket研究员发现5个AsyncAPI npm包版本（含@asyncapi/generator@3.3.1与@asyncapi/specs@6.11.2，后者周下载量达270万）被植入混淆JS，被导入即执行，并绕过npm生命周期脚本从IPFS下载二阶Miasma RAT载荷。恶意发布可追溯至一个被投毒的源提交所构建的GitHub Actions可信发布（trusted publishing）工作流。Miasma框架支持持久化、加密C2、shell执行、文件操作与载荷更新。这是继Red Hat/Miasma系列之后又一起以AI/云原生生态为目标的供应链攻击，开发者须立即审计依赖树与CI/CD发布流水线。

RabbitMQ双漏洞：CVE-2026-57219（8.7）单次请求窃取OAuth客户端密钥接管Broker + CVE-2026-57221（5.3）多租户隔离绕过

📰 Miggo / 安全客 · 📅 2026-07-15

Miggo披露RabbitMQ自3.13.0起存在的两个访问控制缺陷：CVE-2026-57219（CVSS 8.7）位于废弃接口GET /api/auth——只要OAuth 2配置用过management.oauth\_client\_secret键，攻击者单次请求即可拿到客户端密钥并兑换管理员令牌，整个消息代理（队列/用户/Broker设置）尽归其手；该端点权限检查被硬编码为始终放行。CVE-2026-57221（CVSS 5.3）则允许任意已登录用户枚举同虚拟主机内其他租户的队列/交换机元数据。二者于4月发布的4.3.0/4.2.6/4.1.11/4.0.20/3.13.15修复，官方称披露前未见利用；公网裸奔管理界面的用户应核查访问日志。

Siemens Opcenter X JWT算法混淆认证绕过CVE-2026-56451（CVSS 10.0）— 未认证可伪造任意令牌接管制造执行系统

📰 Siemens / Enigma Global / CERT · 📅 2026-07-15

Siemens Opcenter X（V2604之前全版本）因未正确验证JWT算法头，允许未认证远程攻击者伪造任意令牌、完全绕过认证。Opcenter X是制造执行系统（MES），一旦被攻陷将影响生产计划、质量管理和供应链运营。该漏洞属文档化的JWT算法混淆攻击，有公开工具可用，未认证+CVSS 10.0意味着利用门槛极低，制造业组织须立即升级至V2604。鉴于俄方对关键基础设施的活跃定向，OT运营方应将此列为高优先修补项。

xAI Grok Build CLI误传整个Git仓库至Google Cloud Storage + Claude for Chrome信任边界缺陷（ClaudeBleed）8次补丁后仍可复现

📰 TechRadar / Manifold Security / The Hacker News · 📅 2026-07-15

研究者披露xAI的Grok Build CLI在上传文件时误将整个Git仓库（而非单个文件）推送到Google Cloud Storage存储桶，构成代码/凭据外泄风险。同时Manifold Security报告Claude for Chrome扩展的信任边界缺陷（关联早前ClaudeBleed披露）在经历8次后续补丁后仍然可复现，任意拥有claude.ai页面脚本执行权限的扩展可在用户不知情时触发Agent访问Gmail/Docs/Calendar。这延续了AI Agent作为攻击面的趋势——当Agent拥有代码执行与数据访问权限时，传统威胁模型需重新评估，沙箱隔离与权限收敛愈发关键。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 7 条 |

CVE-2026-55040CVSS 9.1

**受影响产品：**Microsoft SharePoint Server（本地部署Subscription Edition / 2019 / 2016），承载企业文档协作与内部门户，多面向互联网且常存历史攻击面

**漏洞描述：**CWE-287/CWE-347 弱JWT令牌验证（认证绕过→RCE）— SharePoint对JWT令牌的签名/算法验证不足→未认证远程攻击者凭已知AD Security ID(SID)或User Principal Name(UPN)伪造令牌→冒充任意站点用户→借Pwn2Own Berlin展示的链式组合升级为未认证RCE→攻击链：提交含已知SID/UPN的特制JWT→绕过认证冒充用户→触发RCE组件→实例内任意代码执行

**利用状态：**Rapid7 07-15披露（Pwn2Own Berlin验证）→CVSS 9.1 Network/无需认证→RCE组件微软定于8月补丁周期修复、当前仅缓解→未认证认证绕过已可独立利用→所有受支持本地版均受影响→CVSS高且暴露面大→高危  ·  **补丁状态：**Microsoft缓解（RCE组件8月补丁）→①立即评估SharePoint JWT/身份校验配置、禁用已知SID/UPN直接冒充路径→②启用AMSI Full Mode并监控异常请求→③将SharePoint纳入身份断言硬编码清单审计→④等待8月补丁并先行网络层收敛暴露面→⑤审查IIS配置与WebShell痕迹

CVE-2026-44747CVSS 9.9

**受影响产品：**SAP NetWeaver Application Server ABAP（企业ERP核心集成与运行平台，承载财务/供应链/HR等大量敏感业务，全球众多大型企业部署且常面向内网/外网）

**漏洞描述：**CWE-119 内存破坏（缓冲区/堆相关）— NetWeaver AS ABAP在处理特制请求时存在内存破坏→未授权攻击者经网络触发→导致远程代码执行或拒绝服务→攻击链：发送特制网络请求→触发内存破坏→AS ABAP进程内任意代码执行→接管ERP枢纽→进一步接触财务/供应链数据

**利用状态：**SAP 7月补丁日(07-15)修复→CVSS 9.9 Network/无需认证→作为7月头号SAP漏洞、影响面广→企业ERP枢纽一旦RCE破坏性强→虽无公开在野确认但暴露面大、易被逆向→高危  ·  **补丁状态：**SAP 7月2026安全通告修复→①立即应用NetWeaver AS ABAP对应补丁→②将NetWeaver实例限制于受信任网络、收敛互联网暴露→③排查异常进程/外连与可疑请求→④对ERP主机启用EDR与日志审计→⑤按暴露面优先修补面向互联网实例

CVE-2026-56190CVSS 9.8

**受影响产品：**Microsoft Windows Remote Desktop Protocol（RDP）服务，是互联网上暴露最广泛的服务之一，也是勒索软件首要初始访问向量

**漏洞描述：**CWE-908 使用未初始化资源 — Windows RDP在处理连接时使用了未初始化资源→未授权攻击者经网络发送特制RDP请求即触发→无需认证即远程代码执行→攻击链：发送特制RDP握手/数据→触发未初始化资源→网络层RCE→与BlueKeep(CVE-2019-0708)机理相似、具备蠕虫传播特征

**利用状态：**Microsoft 7月补丁星期二(07-14)修复→CVSS 9.8 Network/No privileges/No interaction→未认证网络RCE且具蠕虫特征→RDP暴露面广→历史RDP漏洞数日内即被武器化→极高危须最优先修补  ·  **补丁状态：**Microsoft 7月补丁修复→①立即修补互联网暴露的RDP服务（最高优先级）→②启用网络层MFA/网关(NPS/RDG)并限制RDP源IP→③禁用不必要的RDP暴露、启用NLA→④部署RDP暴力破解与异常会话监控→⑤对未及修补资产临时隔离

CVE-2026-57092CVSS 9.9

**受影响产品：**Microsoft Windows VMSwitch（Hyper-V虚拟网络组件），运行于云服务商与多租户虚拟化基础设施的宿主机

**漏洞描述：**CWE-416 释放后使用(UAF) — Windows VMSwitch在处理虚拟网络操作时存在UAF→已授权攻击者经网络触发→权限提升至更高特权→攻击链：触发VMSwitch UAF→提升权限→在Hyper-V宿主上下文执行代码→实现客户虚拟机逃逸→攻陷宿主机及其他租户

**利用状态：**Microsoft 7月补丁星期二(07-14)修复→CVSS 9.9 Network/需低权限→UAF+CVSS 9.9+靶向Hyper-V→虚拟机逃逸价值极高→云/托管服务商须极度紧急修补→高危  ·  **补丁状态：**Microsoft 7月补丁修复→①云/托管服务商立即修补Hyper-V宿主机→②审查多租户隔离与VMSwitch配置→③对宿主机启用EDR与异常VM逃逸监控→④评估租户间隔离强度→⑤非紧急窗口期先行收敛管理接口

CVE-2026-56451CVSS 10.0

**受影响产品：**Siemens Opcenter X（制造执行系统MES，V2604之前全版本），用于生产计划、质量管理和供应链运营，广泛应用于制造业OT环境

**漏洞描述：**CWE-287/CWE-347 JWT算法混淆（认证绕过）— Opcenter X未正确验证JWT令牌的alg头→未认证远程攻击者将alg置为none或对称算法并自签令牌→伪造任意用户令牌→完全绕过认证→攻击链：构造alg混淆JWT→伪造管理员/任意用户令牌→未认证接管MES→篡改生产计划/质量数据/供应链流程

**利用状态：**Siemens 07-15披露并修复→CVSS 10.0 Network/No privileges→JWT算法混淆有公开工具、未认证即利用→制造业MES暴露即高危→俄方对关键基础设施活跃定向背景下须立即升级→极高危  ·  **补丁状态：**Siemens修复（升级至V2604）→①立即升级Opcenter X至V2604→②审计JWT验证配置、强制固定可信alg(如RS256)拒绝alg:none→③限制MES管理接口网络可达性→④监控异常登录与令牌签发→⑤对OT网络施行分段与严格访问控制

CVE-2026-57219CVSS 8.7

**受影响产品：**RabbitMQ消息代理（自3.13.0起所有版本，全球数百万开发者用于异步消息与任务队列，常承载内部服务通信与凭据交换）

**漏洞描述：**CWE-284/CWE-522 不当访问控制（OAuth密钥泄露）— 废弃接口GET /api/auth的权限检查被硬编码为始终放行→只要OAuth 2配置用过management.oauth\_client\_secret键，攻击者单次请求即拿到客户端密钥→兑换管理员令牌→接管整个消息代理→攻击链：GET /api/auth→返回oauth\_client\_secret→兑换管理员令牌→控制队列/用户/Broker设置→横向至依赖该Broker的所有服务

**利用状态：**Miggo 07-15披露（4月已修复于4.3.0/4.2.6/4.1.11/4.0.20/3.13.15）→CVSS 8.7 Network/需一定权限获取端点→披露前未见利用但公网管理界面高风险→密钥泄露即Broker沦陷→高危  ·  **补丁状态：**RabbitMQ 4.x/3.13.15修复→①升级至已修复版本→②将management插件限制于受信任网络、禁止公网暴露→③轮换所有OAuth客户端密钥与Broker凭据→④审计访问日志中的GET /api/auth异常请求→⑤对消息代理启用mTLS与最小权限

CVE-2026-15409CVSS 9.8

**受影响产品：**SonicWall SMA1000系列安全移动接入设备（SMA1000 Appliances），直接面向互联网、为企业员工与承包商提供远程接入的内部网络网关

**漏洞描述：**CWE-918 服务端请求伪造(SSRF) + CVE-2026-15410 代码注入 — CVE-2026-15409为未认证SSRF，使设备代攻击者为非预期请求（常达内网不可达系统）；CVE-2026-15410为需管理员权限的代码注入可执行OS命令→攻击链：未认证SSRF→打管理控制台→触发CVE-2026-15410代码注入→设备上任意OS命令执行→接管SMA1000→直入内网

**利用状态：**SonicWall PSIRT 07-14(SNWLID-2026-0008) + CISA KEV 07-14 + 确认在野利用→CVSS 9.8（SonicWall评Critical）Network/No privileges→未认证 foothold 即可接管设备→联邦07-17前须修复/下线→互联网边界...