---
title: 网络安全日报 | 2026-07-23
url: https://mp.weixin.qq.com/s/qvEEtHkzZdeqbsFj30fk7w
source: Doonsec's feed
date: 2026-07-23
fetch_date: 2026-07-24T05:02:35.570828
---

# 网络安全日报 | 2026-07-23

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibWuEZyvfHZGSjEmUaJvkuiccNVbL4JK6nC98YxiaTdo1uen6sI4XnfaSiczyYFlF9nYTONSyyrVQjcjC6Rmxa0yia3JT0MFRibHbUD4KxcP2BAb0/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-23

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月23日（星期四） | 数据来源：NVD / CISA KEV / CNVD / CNNVD / Hackread / Infosecurity Magazine / Qualys / The Hacker News / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 4 极危事件 | 3 高危事件 | 3 中危事件 | 5 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：WordPress wp2shell 双 CVE 大规模利用激增（CVE-2026-63030 / CVE-2026-60137，CVSS 9.8 / 9.1）— Shadowserver 07-22 确认数千 webshell 已落地、新 PoC 变种绕过常见 WAF 正则，5 亿+ 站点暴露窗口未闭合**

**🔴 极危：Citrix NetScaler ADC/Gateway 新未认证 RCE 入 CISA KEV（CVE-2026-53890，CVSS 9.8）且确认在野 — 边界设备再遭预认证打击，约 12 万实例暴露，修复版本已发布**

**🔴 极危：SharePoint CVE-2026-50522 反序列化 RCE 大规模在野 + CISA 紧急指令 ED 26-04（联邦 07-28 前修补并轮换机器密钥）— 窃取 IIS 机器密钥实现"补丁后持久化"，ToolShell 级影响**

**🟠 高危：Langflow CVE-2026-0770 未认证 root RCE 遭大规模扫描与失陷 + HOLLOWGRAPH 滥用 M365 日历 C2 扩展目标 + Qilin 借 PAN-OS CVE-2026-0257 持续入侵 — AI/云/边界多面受击**

**🟡 中危：Suno 5500 万泄露引发凭证复用与 Operation SilentLogin 设备码 OAuth 钓鱼 + JadePuffer/EncForge 精准加密 AI 资产 + Roundcube CVE-2026-53912 SSRF 披露 — 身份与 AI 资产风险并行升温**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

WordPress "wp2shell" 链大规模利用激增：Shadowserver 07-22 扫描确认数千 webshell 已落地，新 PoC 变种绕过常见 WAF 正则

📰 Shadowserver / Wiz / VulnCheck / KEVIntel / Searchlight Cyber · 📅 2026-07-22 ~ 07-23（持续发酵）

在 CISA 07-21 将 wp2shell 双 CVE（CVE-2026-63030 / CVE-2026-60137）纳入 KEV 后，利用规模急剧放大。Shadowserver 07-22 扫描显示数万实例仍暴露在公网，数千个 webshell（如 94uh9ubh6e1x.php）已部署于 /wp-content/cache/；研究者发布的新 PoC 变种调整了 batch 路由混淆的嵌套结构，可绕过基于 "batch/v1" 字面量的常见 WAF 正则。Wiz/VulnCheck/KEVIntel 确认 13+ 攻击 IP 来自 7 国并持续扩张。全球超 5 亿站点暴露窗口仍未闭合，强制自动更新因缓存/对象缓存未启用而未真正生效的比例可能偏高，逐站核验成为唯一可靠手段。

CISA 07-22 发布紧急指令 ED 26-04 应对本地 SharePoint 在野利用：联邦机构须于 07-28 前修补并轮换 IIS 机器密钥

📰 CISA / Microsoft / BleepingComputer / Decipher · 📅 2026-07-22

针对 SharePoint CVE-2026-50522（CVSS 9.8，CWE-502 反序列化 RCE）公开 PoC 后数小时内的在野利用与机器密钥窃取，CISA 于 07-22 发布紧急指令 ED 26-04，要求联邦民事行政部门机构在 07-28 前完成：①部署 7 月累积更新②修补后必须轮换 IIS 机器密钥（窃取到的密钥可伪造有效令牌实现"补丁后持久化"）③启用 AMSI Full Mode④限制外网直连。该指令罕见地将"密钥轮换"列为强制项，侧面印证攻击者已将持久化目标从单纯 RCE 升级为身份层控制，watchTowr 称其具备 ToolShell 级影响。

Citrix NetScaler ADC/Gateway 新未认证 RCE 入 CISA KEV（CVE-2026-53890，CVSS 9.8）— 在野利用确认，边界设备再遭预认证打击

📰 CISA / Citrix / The Hacker News / BleepingComputer · 📅 2026-07-22

Citrix NetScaler ADC 与 NetScaler Gateway 曝出未认证远程代码执行漏洞 CVE-2026-53890（CWE-787 越界写，CVSS 9.8）：管理接口 / Gateway 特定的 POST 请求在处理未认证输入时对长度字段信任过度，触发 nsppe 数据包引擎堆溢出，可致进程崩溃或以高权限上下文 RCE。CISA 于 07-22 当日将其纳入 KEV（BOD 26-04，联邦截止 08-1X）并确认在野利用——UNC-XXXX 已将其用于初始访问，多区域失陷 IP 出现在日志中。约 12 万实例暴露，修复版本 14.1-8.50 / 13.1-55.34 / 13.0-92.34 已发布，限制管理接口暴露是临时缓解关键。

Langflow CVE-2026-0770 遭大规模主动扫描与失陷：AI 工作流平台 root RCE 暴露面沦为内网跳板

📰 Shadowserver / Trend Micro ZDI / The Hacker News · 📅 2026-07-22（持续）

开源 AI 工作流平台 Langflow 的未认证 root RCE（CVE-2026-0770，validate 端点 exec\_globals 代码执行）在 07-21 入 CISA KEV 后，Shadowserver 于 07-22 检测到针对 /api/v1/validate/code 的大规模探测并确认部分实例已失陷。由于 Langflow 常运行于 root、承载 API 密钥/数据库密码/云令牌，一旦沦陷即成为横向内网的高价值跳板；EPSS 达 95.2% 百分位、公开 PoC 已多份，武器化门槛极低。研究者提醒：即便未启用 AUTO\_LOGIN，暴露在公网的实例仍可能因其他配置缺陷被触及，AI 基础设施的暴露面收敛刻不容缓。

HOLLOWGRAPH 木马扩展目标：滥用 Microsoft 365 日历作 C2 死投的 Cavern 框架出现新 IOC 与行业指向

📰 Group-IB / Enigma Global / Infosecurity Magazine · 📅 2026-07-22（持续发酵）

Group-IB 将 HOLLOWGRAPH 归因于 Cavern 后门框架后，07-22 新增情报显示该木马正扩展攻击目标并出现新 IOC：除早期偏好的以色列实体外，欧洲金融与物流行业亦出现可疑 Graph API 异常调用。攻击者通过被攻陷的 M365 账户，把 C2 指令嵌入日期远在未来的日历预约，借正常业务同步流量规避网络监测；即便部署 EDR，若不审查 Graph API 行为仍难以察觉。该手法将"云原生隐蔽信道"推向生产化，迫使防御从特征检测转向云审计日志与条件访问的行为分析。

Operation SilentLogin 钓鱼复用泄露凭证攻陷 M365：借 Suno/HIBP 泄露库 + 设备码 OAuth 绕过 MFA

📰 Proofpoint / Microsoft / 安全客 · 📅 2026-07-22

新一波名为 Operation SilentLogin 的凭证钓鱼活动于 07-22 被披露：攻击者利用 Have I Been Pwned 收录的 Suno 等近期大规模泄露凭证库做凭据填充，并结合设备码（device code）OAuth 授权流程绕过 MFA——受害者被诱导在攻击者构造的页面完成设备码授权，令牌直接回传攻击者侧，全程无需触碰密码或第二因子。Proofpoint 指出该活动针对制造业与专业服务企业，成功案例多源于"密码复用 + 遗留 M365 应用"组合。建议企业启用条件访问中的"不可信设备/异常位置阻断"并强制令牌绑定。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 5 条 |

CVE-2026-50522CVSS 9.8

**受影响产品：**Microsoft SharePoint Enterprise Server 2016（build < 16.0.5561.1001）、SharePoint Server 2019（build < 16.0.10417.20175）、SharePoint Server Subscription Edition（build < 16.0.19725.20434）；据 Shadowserver 超 1000 个实例暴露（约半数在北美），面向互联网的企业内网文档/协作系统，SharePoint Online 不受影响

**漏洞描述：**CWE-502 不可信数据反序列化 — 攻击者在 WS-Federation 登录响应中将恶意 .NET `BinaryFormatter` 负载作为伪造 `SecurityContextToken` 的 cookie 投递至 `/\_trust/default.aspx` 端点→若被脆弱反序列化路径处理即触发任意代码执行（RCE）；公开 PoC（Janggggg）经伪造 WS-Federation cookie→反序列化 gadget→以 SharePoint 应用池身份 RCE，ZDI 同期给出 working exploit

**利用状态：**07-14 微软补丁（7月补丁星期二）/ 07-20 watchTowr 识别 PoC / 数小时内蜜罐捕获成功利用 / 07-22 CISA 发布紧急指令 ED 26-04 要求联邦机构在 07-28 前修补并轮换机器密钥 + 多 APT（UNC-XXXX）利用窃取 IIS 机器密钥实现"补丁后持久化"（CVSS 9.8 NVD，AV:N/AC:L/PR:N/UI:N，SSVC automatable:yes，EPSS 97% 百分位）→ 大规模在野，具备 ToolShell 级影响  ·  **补丁状态：**修复版本 16.0.5561.1001 / 16.0.10417.20175 / 16.0.19725.20434 → ①立即部署 7 月累积更新②修补后必须轮换 IIS 机器密钥（否则窃取密钥可伪造令牌持久化）③启用 AMSI Full Mode 监控含序列化对象请求④监控 `/\_trust/default.aspx` 异常 POST 与异常 machine-key 访问⑤将暴露 SharePoint 置于 L7 反向代理后并限制外网直连⑥假设已遭尝试入侵猎杀 WebShell 与凭据窃取

CVE-2026-63030CVSS 9.8

**受影响产品：**WordPress 核心 6.9.0–6.9.4 与 7.0.0–7.0.1（批处理端点 /wp-json/batch/v1 于 6.9 引入），全球超 5 亿个网站（约 43% 公网 Web），含大量面向互联网的企业门户与媒体站点，默认安装即可被利用，无需插件

**漏洞描述：**CWE-436 解释冲突 + CWE-89 SQL 注入 — /batch/v1 端点解析缺陷使内部请求追踪数组错位→恶意子请求被错误调度至非预期处理器→绕过方法白名单→将用户可控输入喂入 WP\_Query 的 author\_\_not\_in 参数→该参数以字符串传入时 sanitization 被跳过、原始值直接插值进 NOT IN 子句→特制 /wp-json/batch/v1 请求触发路由混淆→author\_\_not\_in 字符串注入 SQL→盲注/时间盲注(SLEEP)读 admin 哈希→破解后登录→上传 webshell 实现 RCE（链同伴 CVE-2026-60137 为 WP\_Query SQLi，CVSS 9.1）

**利用状态：**07-17 披露 + 07-19 公开 PoC(wp2shell.py) + 07-21 入 CISA KEV（BOD 26-04，联邦截止 08-11）+ 07-22 大规模利用激增（Shadowserver 扫描：数万实例仍暴露、数千 webshell 已部署于 /wp-content/cache/，新 PoC 变种绕过常见 WAF 正则）（CVSS 9.8 NVD，链式 Critical，AV:N/AC:L/PR:N/UI:N）→ 已连续第3天纳入关注表（has\_new 重大更新豁免）  ·  **补丁状态：**WordPress 6.9.5 / 7.0.2 / 6.8.6 / 7.1 Beta2 修复→①逐站核验公网 WordPress 是否真正完成强制自动更新②WAF 临时拦截 /wp-json/batch/v1 及 rest\_route=/batch/v1 并升级正则覆盖新变种③监控异常 POST /wp-json/batch/v1 与异常 SQL 时序(SLEEP)④审计 plugins/uploads 目录新增 PHP webshell（如 94uh9ubh6e1x.php）⑤轮换被疑泄露的管理员凭据并启用 2FA⑥封禁 UA: wp2shell / rezwp2shell

CVE-2026-60137CVSS 9.1

**受影响产品：**WordPress 核心 6.8.0 起至 7.0.1 的 WP\_Query 组件（含 6.8.6 修复版之前的 6.8/6.9/7.0 系列），全球所有运行上述版本的站点（6.8 仅受此 SQLi 影响、6.9+ 可借批量路由混淆升级为未认证 RCE），覆盖数亿实例

**漏洞描述：**CWE-89 SQL 注入 — WP\_Query 的 author\_\_not\_in（及同类参数）在接收字符串类型输入时 sanitization 逻辑被跳过，攻击者可注入原始 SQL 片段进入 NOT IN 子句；当与 CVE-2026-63030 的 /batch/v1 路由混淆链式组合时，匿名请求即可将可控字符串送达 WP\_Query→触发时间盲注(SLEEP)读取 wp\_users 表中管理员密码哈希→破解后登录后台→上传恶意插件/主题实现 RCE

**利用状态：**07-17 与 CVE-2026-63030 同期披露 + 07-19 随 wp2shell 链公开 PoC + 07-21 入 CISA KEV（BOD 26-04，联邦截止 08-11）+ 07-22 随链大规模利用激增（CVSS 9.1 NVD / 7.5 CISA-ADP，AV:N/AC:L/PR:N/UI:N）→ KEV 重大更新纳入关注表（连续第3天 has\_new 豁免）  ·  **补丁状态：**WordPress 6.8.6 / 6.9.5 / 7.0.2 修复→①升级至修复版本②对无法立即升级的 6.8 站点至少先打 6.8.6 阻断 SQLi③WAF 拦截含 author\_\_not\_in 异常字符串的请求④监控数据库异常查询与失败登录激增⑤审计管理员账户异常创建与提权

CVE-2026-0770CVSS 9.8

**受影响产品：**Langflow（开源 AI 工作流/智能体可视化构建平台）1.4.2 及之前版本（pypi langflow 0 / langflow-ai/langflow），常运行于 root 且 API 暴露公网，承载 LLM 与数据工具编排，存储 API 密钥、数据库密码与云令牌，是 AI 基础设施的高价值跳板

**漏洞描述：**CWE-829 从未受信任控制域引入功能 — validate 端点（/api/v1/validate/code）将用户可控的 exec\_globals 参数直接并入代码求值（Python 生成器异常抛出执行 subprocess.run），未限制来源；当 AUTO\_LOGIN=true 时攻击者可无认证（默认凭据 langflow/langflow 自动登录）提交恶意 exec\_globals→在 root 上下文执行任意系统命令，完全控制主机（ZDI-CAN-27325 / ZDI-26-036）

**利用状态：**公开 PoC 多份（0xgh057r3c0n / Ez4rd1x1 / affix）→ 07-21 入 CISA KEV（BOD 26-04，联邦截止 08-11）+ 07-22 Shadowserver 检测到大规模 /api/v1/validate/code 探测并确认失陷（EPSS 95.2% 百分位，CVSS 9.8，AV:N/AC:L/PR:N/UI:N，SSVC automatable:yes）→ 未认证 root RCE 已工具化、AI 平台暴露面直接沦为内网跳板  ·  **补丁状态：**升级至官方修复版本 → ①升级 Langflow 至最新版②禁止 API 公网暴露、仅限可信网络③禁用 AUTO\_LOGIN 并修改默认凭据④避免以 root 运行 Langflow 进程⑤监控 /api/v1/validate/code 异常 POST 与默认凭据登录尝试⑥对 AI 平台存储的 API 密钥/云令牌做泄露排查与轮换

CVE-2026-53890CVSS 9.8

**受影响产品：**Citrix NetScaler ADC 与 NetScaler Gateway 14.1 / 13.1 / 13.0（管理...