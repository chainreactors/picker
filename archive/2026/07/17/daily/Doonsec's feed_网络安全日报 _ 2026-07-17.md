---
title: 网络安全日报 | 2026-07-17
url: https://mp.weixin.qq.com/s/4Nx_eTLuhClgODsHnK26kA
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:43:12.707831
---

# 网络安全日报 | 2026-07-17

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibWuEZyvfHZHgt6EcJfadrJ6sU8WJaNEo4rozgibNPLPlg4J8newK051HNmbz9KotdzbvTmicSbte2AMQBIsNGsgdxe1Yk1Tic9WUnxBUsCgmww/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-17

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月17日（星期五） | 数据来源：NVD / CISA KEV / Microsoft MSRC / Fortinet PSIRT / Oracle / Siemens / Chromium / The Hacker News / CrowdStrike / SecurityWeek / 安全客 / FreeBuf / Enigma Global / SOCRadar

|  |  |  |  |
| --- | --- | --- | --- |
| 4 极危事件 | 1 高危事件 | 2 中危事件 | 8 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：CISA KEV 7月16日新增 SharePoint 未认证反序列化 RCE CVE-2026-58644（CVSS 9.8）— 补丁星期二后数日即入KEV（联邦07-19前须修复），叠加 7月14日 SMA1000/ADFS/SharePoint 三连发修复窗口今日（07-17）到期，边界VPN与身份基础设施进入"补或下线"最后期限**

**🔴 极危：FortiSandbox 双CVE（CVE-2026-39808 9.8 OS命令注入 + CVE-2026-39813 9.8 路径遍历/认证绕过）被确认在野利用并纳入KEV（07-16），未认证即可接管沙箱设备；同期 Oracle E-Business Suite CVE-2026-46817（CVSS 9.8）入KEV（07-15）持续发酵**

**🟠 高危：Windows User Profile Service 未修补0day "LegacyHive"（无CVE）7月15日公开PoC，可在完全打补丁的Windows上以标准用户挂载任意用户（含管理员）注册表hive，实现本地提权；Cursor IDE git.exe 0day（无CVE）同样无补丁，克隆恶意仓库即触发RCE**

**🟠 高危：Chromium 内核关键漏洞 CVE-2026-15773（CVSS 9.6 Critical）7月16日披露，影响 Chrome/Edge/Brave/Vivaldi 全系桌面浏览器，须立即更新；同一补丁周期内 BitLocker GreatXML（CVE-2026-50661，6.1）绕过亦需处置**

**🟡 中危：Cybernews 发现 240亿条被盗凭据（8.3TB Elasticsearch 暴露）聚合，叠加 07-14 AsyncAPI npm Miasma RAT 供应链投毒 — 身份攻击已超越漏洞利用成为勒索首要入口，企业须默认自身凭据已泄露并启用MFA/条件访问**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

CISA KEV 7月16日新增 SharePoint 未认证反序列化 RCE CVE-2026-58644（CVSS 9.8）— 补丁后数日即入KEV，联邦07-19前须修复

📰 CISA / Rescana / NCSC-FI / The Hacker News · 📅 2026-07-16

CISA于7月16日将 Microsoft SharePoint Server 反序列化漏洞 CVE-2026-58644（CVSS 9.8）纳入已知在野利用漏洞(KEV)目录，距7月补丁星期二仅数日，修复截止07-19。该漏洞允许未认证攻击者经特制网络请求在SharePoint应用池（常为SYSTEM）上下文执行任意代码，无需用户交互、低复杂度，EPSS预测约1.3%。这是继 CVE-2026-56164、CVE-2026-45659 之后第三个被利用的SharePoint缺陷，表明攻击者正系统性地将企业协作平台作为初始访问支点。各机构须将SharePoint累积更新列为最高优先。

FortiSandbox 三CVE（CVE-2026-39808/CVE-2026-39813/CVE-2026-25089）在野利用确认 + 07-16入KEV — 未认证接管沙箱设备

📰 Defused Cyber / SOCRadar / Cyberpress / Enigma Global · 📅 2026-07-16

威胁情报公司 Defused 观察到 CVE-2026-39813、CVE-2026-39808、CVE-2026-25089 在过去24小时内遭利用，蜜罐捕获来自 141.11.43.175（AS136510）针对 /jsonrpc/ 端点的恶意 JSONRPC POST。CVE-2026-39808（OS命令注入，CVSS 9.8）与 CVE-2026-39813（JRPC API 路径遍历/认证绕过，CVSS 9.8）Fortinet已于4月修补，CVE-2026-25089 于6月初修补，但大量设备未升级。沙箱设备沦陷尤为危险——攻击者可压制自身恶意软件检测、窃取威胁情报并横向至安全基础设施。CVE-2026-39808/39813 于7月16日纳入KEV（截止07-19）。

Windows User Profile Service 未修补0day "LegacyHive" 公开PoC（无CVE）— 完全打补丁的Windows仍可被本地提权

📰 Chaotic Eclipse / Rescana / SecurityAffairs / xploitzone · 📅 2026-07-15

研究员 Chaotic Eclipse（原 Nightmare-Eclipse）于7月15日公开 "LegacyHive" PoC，瞄准 Windows User Profile Service(ProfSvc) 任意hive加载提权漏洞：标准本地用户可借对象管理器符号链接(oplock暂停hive加载)将目标用户(含管理员)的 UsrClass.dat 挂载至自身会话，读取/篡改其注册表。该漏洞无CVE、无微软补丁，且经多方验证在装有7月累积更新的全系Windows 10/11/Server(2016-2022)上仍可复现。同期该研究员还披露 BitLocker GreatXML 绕过(CVE-2026-50661)。虽需本地用户凭据、暂非远程RCE，但作为后渗透提权原语价值极高。

Cursor IDE git.exe 0day（无CVE）公开 — 克隆恶意仓库即静默RCE；DeepJack deeplink 缺陷亦未修复

📰 Mindgard / Hackvolt / Adversa AI / The Hacker News · 📅 2026-07-14 ~ 07-16

AI安全公司 Mindgard 于7月14日全文披露 Cursor IDE 二进制植入漏洞：Cursor 在 Windows 上解析 git 时会在工作区目录查找 git.exe，攻击者将恶意二进制命名为 git.exe 置于仓库根目录，开发者克隆并打开即静默以登录用户权限执行（不需点击/批准）。该缺陷自2025-12-15报告后7个月无补丁，最新版仍复现。Adversa AI 同期披露 DeepJack：经 cursor:// deeplink 安装攻击者控制的MCP服务器、单行文本框溢出藏匿恶意命令尾，构建3.9.8仍含该缺陷。同类缺陷亦见于 Copilot CLI / Gemini CLI / Codex 桌面端，反映AI编码助手普遍安全投入滞后。

Chromium 内核关键漏洞 CVE-2026-15773（CVSS 9.6 Critical）7月16日披露 — Chrome/Edge/Brave/Vivaldi 全系须更新

📰 WA SOC / Google Chrome Releases · 📅 2026-07-16

西澳政府安全运营中心(WA SOC)于7月16日发布公告，Google 修复影响 Chromium 内核的多个安全漏洞，其中 CVE-2026-15773 评级 Critical（CVSS 9.6），波及 Google Chrome、Microsoft Edge、Brave、Vivaldi 等桌面浏览器。浏览器内核漏洞一旦公开即被快速武器化，常被用于钓鱼凭据窃取与恶意载荷投递。建议管理员按厂商指引在预期时间窗内为所有受影响设备应用更新，并启用 Site Isolation 与浏览器沙箱。

Cybernews 发现 240亿条被盗凭据（8.3TB Elasticsearch 暴露）— 身份攻击成为勒索首要入口

📰 Cybernews / Enigma Global / Sophos · 📅 2026-07-16

Cybernews 研究员发现一个公开暴露的 Elasticsearch 数据库，含超240亿条被盗凭据记录（总计8.3TB），包括用户名、邮箱、明文密码、登录URL及来源归因，主要由 infostealer 恶意软件家族窃取聚合。这是迄今记录的最大凭据聚合之一。Sophos 同期指出钓鱼与身份攻击已超越漏洞利用成为勒索软件首要入口。鉴于暴露凭据体量，几乎所有组织都应假设部分员工凭据已泄露，须全面启用MFA、条件访问与身份威胁检测，并审计凭据填充与横向移动。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 8 条 |

CVE-2026-58644CVSS 9.8

**受影响产品：**Microsoft SharePoint Server（本地部署 Subscription Edition / 2019 / 2016），企业文档协作与内部门户，常面向互联网且承载历史攻击面

**漏洞描述：**CWE-502 反序列化不可信数据 — SharePoint 对反序列化对象校验不足→未认证攻击者发送特制网络请求→触发序列化对象反序列化→以应用池身份(常为SYSTEM)执行任意代码→攻击链：特制请求含恶意序列化对象→绕过认证→应用池上下文RCE→接管Web服务器→横向至内网

**利用状态：**CISA KEV 07-16新增(Due 07-19)→CVSS 9.8 Network/无需认证/低复杂度/EPSS 1.3%→SharePoint为勒索初始访问热点、已确认在野→未认证RCE即极高危  ·  **补丁状态：**Microsoft 7月补丁星期二修复→①立即应用SharePoint累积更新(最高优先)→②审计入站含序列化对象的可疑请求→③限制SharePoint网络暴露至受信任IP→④部署WAF阻断已知反序列化载荷→⑤轮换IIS机器密钥并猎杀WebShell

CVE-2026-46817CVSS 9.8

**受影响产品：**Oracle E-Business Suite（Oracle Payments 模块），承载企业财务支付核心流程，常面向内网/外网且含敏感支付数据

**漏洞描述：**CWE-269/CWE-287/CWE-306 不当权限管理(未认证权限提升) — Oracle EBS Payments 模块对HTTP访问的权限校验不足→未认证远程攻击者经网络访问HTTP即可 compromising Oracle Payments→攻击链：未认证HTTP请求→绕过权限管理→接管Oracle Payments→访问财务支付数据/供应链

**利用状态：**Oracle 7月CPU + CISA KEV 07-15(Due 07-18)→CVSS 9.8 Network/No auth→未认证接管财务支付、暴露面广→虽无公开在野确认但KEV收录即高危  ·  **补丁状态：**Oracle 7月2026 CPU修复→①立即应用Oracle 7月CPU(Payments模块)→②限制EBS HTTP端点网络暴露、不暴露公网→③审查支付模块异常访问与可疑请求→④监控财务数据外泄→⑤按暴露面优先修补面向互联网实例

CVE-2026-39808CVSS 9.8

**受影响产品：**Fortinet FortiSandbox 4.4.0–4.4.8（升级4.4.9+），威胁检测沙箱设备，常面向互联网且具安全基础设施与威胁情报可见性

**漏洞描述：**CWE-78 OS命令注入 — FortiSandbox API端点的 jid GET参数未正确校验→未认证攻击者经特制HTTP请求注入OS命令→以root执行任意命令→攻击链：特制HTTP请求(jid参数)→OS命令注入→root权限RCE→完全接管沙箱→压制自身恶意软件检测/横向

**利用状态：**Fortinet 4月补丁 + CISA KEV 07-16(Due 07-19) + 07-16确认在野(Defused/SOCRadar蜜罐141.11.43.175)→CVSS 9.8 Network/No auth/No UI→沙箱设备沦陷即泄露威胁情报→极高危  ·  **补丁状态：**Fortinet修复(升级4.4.9或5.0.6+)→①立即升级FortiSandbox②禁管理接口公网暴露③监控/jsonrpc/异常POST与异常源IP(AS136510)④将设备视为潜在失陷威胁狩猎⑤阻断相关ASN

CVE-2026-39813CVSS 9.8

**受影响产品：**Fortinet FortiSandbox 4.4.0–4.4.8 及 5.0.0–5.0.5（升级4.4.9+/5.0.6+），JRPC API 组件

**漏洞描述：**CWE-22 路径遍历 — FortiSandbox JRPC API的 ../filedir 路径遍历→未认证攻击者经特制HTTP请求绕过认证→权限提升→攻击链：特制HTTP请求(JRPC API)→../filedir路径遍历→绕过认证→提权至更高权限→进一步接管沙箱

**利用状态：**Fortinet 4月补丁 + 07-16开源报告确认在野(CVSS 9.8/9.1)→未认证认证绕过+提权、无公开KEV但活跃利用→高危  ·  **补丁状态：**Fortinet修复(升级4.4.9+/5.0.6+)→①立即升级②禁管理接口公网暴露③监控JRPC API异常请求④威胁狩猎⑤与CVE-2026-39808/25089统一处置

CVE-2026-15773CVSS 9.6

**受影响产品：**Chromium 内核浏览器（Google Chrome / Microsoft Edge / Brave / Vivaldi）桌面版，全球数十亿用户

**漏洞描述：**Chromium 内核关键漏洞（具体CWE待NVD细化，V8/渲染相关高概率）→处理特制HTML/JS触发→浏览器进程上下文代码执行(沙箱逃逸或RCE)→攻击链：诱导访问恶意页面→触发内核漏洞→浏览器进程代码执行→钓鱼/凭据窃取/载荷投递

**利用状态：**WA SOC 07-16披露 Critical(CVSS 9.6)→暂无在野确认但浏览器漏洞武器化快、面向互联网用户极广→高危  ·  **补丁状态：**Google 07-16稳定版更新→①立即更新Chrome/Edge等至最新②企业推送浏览器更新策略③启用浏览器沙箱与Site Isolation④监控漏洞利用指示器

CVE-2026-56190CVSS 9.8

**受影响产品：**Microsoft Windows Remote Desktop Protocol（RDP）服务，是互联网上暴露最广泛的服务之一，也是勒索软件首要初始访问向量

**漏洞描述：**CWE-908 使用未初始化资源 — Windows RDP在处理连接时使用了未初始化资源→未授权攻击者经网络发送特制RDP请求即触发→无需认证即远程代码执行→攻击链：发送特制RDP握手/数据→触发未初始化资源→网络层RCE→与BlueKeep(CVE-2019-0708)机理相似、具备蠕虫传播特征

**利用状态：**Microsoft 7月补丁星期二(07-14)修复→CVSS 9.8 Network/No privileges/No interaction→未认证网络RCE且具蠕虫特征→RDP暴露面广→历史RDP漏洞数日内即被武器化→极高危须最优先修补  ·  **补丁状态：**Microsoft 7月补丁修复→①立即修补互联网暴露的RDP服务(最高优先级)→②启用网络层MFA/网关(NPS/RDG)并限制RDP源IP→③禁用不必要的RDP暴露、启用NLA→④部署RDP暴力破解与异常会话监控→⑤对未及修补资产临时隔离

CVE-2026-57092CVSS 9.9

**受影响产品：**Microsoft Windows VMSwitch（Hyper-V虚拟网络组件），运行于云服务商与多租户虚拟化基础设施的宿主机

**漏洞描述：**CWE-416 释放后使用(UAF) — Windows VMSwitch在处理虚拟网络操作时存在UAF→已授权攻击者经网络触发→权限提升至更高特权→攻击链：触发VMSwitch UAF→提升权限→在Hyper-V宿主上下文执行代码→实现客户虚拟机逃逸→攻陷宿主机及其他租户

**利用状态：**Microsoft 7月补丁星期二(07-14)修复→CVSS 9.9 Network/需低权限→UAF+CVSS 9.9+靶向Hyper-V→虚拟机逃逸价值极高→云/托管服务商须极度紧急修补→高危  ·  **补丁状态：**Microsoft 7月补丁修复→①云/托管服务商立即修补Hyper-V宿主机→②审查多租户隔离与VMSwitch配置→③对宿主机启用EDR与异常VM逃逸监控→④评估租户间隔离强度→⑤非紧急窗口期先行收敛管理接口

CVE-2026-56451CVSS 10.0

**受影响产品：**Siemens Opcenter X（制造执行系统MES，V2604之前全版本），用于生产计划、质量管理和供应链运营，广泛应用于制造业OT环境

**漏洞描述：**CWE-287/CWE-347 JWT算法混淆（认证绕过）— Opcenter X未正确验证JWT令牌的alg头→未认证远程攻击者将alg置为none或对称算法并自签令牌→伪造任意用户令牌→完全绕过认证→攻击链：构造alg混淆JWT→伪造管理员/任意用户令牌→未认证接管MES→篡改生产计划/质量数据/供应链流程

**利用状态：**...