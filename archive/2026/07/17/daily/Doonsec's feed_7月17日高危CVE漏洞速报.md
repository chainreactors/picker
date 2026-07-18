---
title: 7月17日高危CVE漏洞速报
url: https://mp.weixin.qq.com/s/6OWnpcSne6uRX6UJ6ouloQ
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:43:50.134662
---

# 7月17日高危CVE漏洞速报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nZrMrH4FF0ILmX05eWkueRr8zDVurP8oIvAOD4zGzjZFeflB9Ds29yJKL9BWnUrllYBqgjajEkHhglCj0F4S27JQEXKfQQMMImUSGD1zb0w/0?wx_fmt=jpeg)

# 7月17日高危CVE漏洞速报

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

安全速报

# 【安全速报】07月17日高危漏洞紧急预警

2026年07月17日  |  探知安全

微软7月补丁星期二622漏洞破纪录：SharePoint JWT认证绕过CVSS 9.1首个未认证RCE攻击链（Rapid7/Pwn2Own发现·CISA紧急警报）、SharePoint满分RCE CISA KEV 7/16紧急新增·ZDI已提交Pwn2Own可工作exploit、Microsoft Copilot RCE CVSS 9.6 Hyper-V逃逸·AI工具首次高危、Hyper-V VMSwitch逃逸CVSS 9.9虚拟机边界突破宿主机沦陷、Hermes WebUI 4个HTTP请求获取Shell CVSS 9.8未认证RCE——请立即排查修复。

## 漏洞详情

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-55040 | CVSS 9.1 |

### 微软SharePoint JWT认证绕过CVSS 9.1：Rapid7在Pwn2Own Berlin发现·首个未认证RCE攻击链第一步·CISA紧急发布SharePoint全线硬防警报

CVE-2026-55040是微软7月补丁星期二（7月14日发布，共修复622个CVE创历史纪录）中最重要的漏洞之一，由Rapid7高级安全研究员Stephen Fewer在Pwn2Own Berlin黑客大赛上发现并演示。该漏洞源于SharePoint Server的JWT令牌验证管道存在多重弱点（CWE-1390弱认证），远程未认证攻击者仅需获知目标用户的Active Directory安全标识符（SID）或用户主体名称（UPN/邮箱格式），即可伪造JWT令牌冒充任意站点用户或管理员——执行该用户的所有SharePoint操作权限。更危险的是，Rapid7已证实该漏洞可与第二个目前未公开的RCE漏洞（预计8月补丁星期二修复）链式利用，实现完整的未认证远程代码执行。CISA于同日（7月14日）发布专门SharePoint硬防警报，紧急敦促所有组织立即修补。CVE-2026-55040的补丁可完全破坏此攻击链的第一步。此漏洞影响所有受支持的自托管SharePoint Server版本（2016/2019/Subscription Edition）。同一天还是SharePoint Server 2016和2019扩展支持终止日——两者不再接收安全更新，未升级至Subscription Edition的组织将永久暴露于后续漏洞。

影响范围

Microsoft SharePoint Enterprise Server 2016（低于16.0.5561.1001）、SharePoint Server 2019（低于16.0.10417.20175）、SharePoint Server Subscription Edition（低于16.0.19725.20434）；注意：SharePoint Server 2016/2019扩展支持已于7月14日终止，不再接收安全更新

修复建议：立即部署2026年7月SharePoint累积更新：KB 5002891/5002892（2016）、KB 5002883/5002885（2019）、KB 5002882（Subscription Edition）；遵循CISA硬防指南：公网暴露的SharePoint置于L7反向代理之后并强制认证；阻止外部访问Central Administration；启用AMSI Full Mode进行请求体扫描；轮换IIS机器密钥前先排查入侵痕迹（机器密钥收割器）；SharePoint 2016/2019用户应尽快迁移至Subscription Edition

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-58644 / 56164 / 56155 | CVSS 9.8 |

### 微软7月补丁星期二三大零日：SharePoint RCE满分CVSS 9.8 CISA KEV 7/16紧急新增+AD FS在野提权（Mandiant/FLARE/DART三方IR团队发现·勒索软件疯抢）

微软2026年7月补丁星期二创下史上最大单次补丁量——622个CVE（63个严重+552个重要），为上月206个的三倍多，AI驱动的自动化漏洞挖掘被认为是爆炸式增长的关键推手。本次确认三个零日漏洞：两个在野积极利用，一个公开披露。  ① CVE-2026-58644（CVSS 9.8）是SharePoint Server远程代码执行漏洞，7月16日（即昨天）被CISA紧急加入KEV已知利用漏洞目录。ZDI在Pwn2Own Berlin上提交了该漏洞的可工作exploit，无需认证、低复杂度、远程利用，攻击者一旦获取初始权限即可完全控制SharePoint服务器。微软虽标注「利用成熟度未知」，但ZDI指出「我们亲手把可工作的exploit给了他」。  ② CVE-2026-56164（CVSS 5.3）是SharePoint未认证权限提升，允许远程攻击者无需凭据即可通过网络提升权限。此漏洞由Mandiant事件响应团队和Google FLARE团队在真实攻击中发现（CISA KEV 7/14新增）。虽然CVSS评分仅5.3，但Rapid7指出「这正是一个低分掩盖高风险的典型——无需认证、远程利用、低复杂度」。  ③ CVE-2026-56155（CVSS 7.8）是AD FS活动目录联合身份验证服务权限提升漏洞，由微软自有DART事件响应团队在攻击中发现（CISA KEV 7/14新增）。AD FS负责签署整个企业信任链的安全令牌，本地提权至管理员后可直接伪造签名凭证，横向移动至域内任意系统。  三大零日可形成攻击链：SharePoint RCE获取边界入口→AD FS提权获取域控令牌→横向蔓延全企业网络。安全社区普遍认为AI自动化审计正带来「补丁爆炸」的新常态。

影响范围

Microsoft SharePoint Server 2016/2019/Subscription Edition（所有本地部署版本）；Active Directory Federation Services（AD FS）；Windows BitLocker全盘加密；覆盖Windows 10/11、Windows Server、Office、Microsoft 365、Azure、Hyper-V等全线产品；Edge浏览器44个CVE、Office 82个CVE、SQL Server 8个CVE、Exchange Server 4个CVE已在本次更新中修复

修复建议：立即部署2026年7月安全更新（Patch Tuesday完整升级）；SharePoint Server优先安装CVE-2026-58644补丁；AD FS服务器立即安装CVE-2026-56155；启用AMSI Full Mode检测可疑请求体（签名SuspSignoutReqBody.A/C、ToolPaneAuthBypass.A/C）；部署MDAV监测Backdoor:MSIL/LeakFang.A!dha特征（IIS受保护密钥窃取后门）；SharePoint 2016/2019因扩展支持已终止，强烈建议迁移至Subscription Edition或云版本；BitLocker用户安装CVE-2026-50661防止物理绕过

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-48561 | CVSS 9.6 |

### Microsoft Copilot远程代码执行CVSS 9.6：低权限Hyper-V Guest可逃逸至宿主机·恶意网站自动发送Crafted Prompt无需用户感知（AI工具首次突破高危·全新攻击范式）

CVE-2026-48561是微软7月补丁星期二修复的Copilot远程代码执行漏洞，CVSS 9.6严重级，标志着AI编码助手首次达到如此高危评分。  攻击向量极为隐蔽：攻击者托管一个恶意网站，当受害者使用Microsoft Edge for Android访问时，浏览器会自动向设备上的Copilot（iOS/Android均可）发送精心构造的提示（prompt），整个过程中受害者无感知——无弹窗、无确认、无交互。由于受影响组件在接收请求时不做确认或来源检查，这些注入的prompt会被Copilot直接执行，可能导致数据被非授权访问或修改。  更致命的是在虚拟化场景中：一个低权限Hyper-V虚拟机Guest中的攻击者，可以穿越Guest安全边界，在Hyper-V宿主机上执行任意代码——本质上是VM逃逸+宿主机RCE的复合攻击。在共享托管、VPS、企业私有云等多租户环境中，一个低权限VM Guest可危及同物理机上的所有其他客户。  该漏洞由Enclave的Ofek Levin发现并通过协调漏洞披露（CVD）报告。微软7月补丁还同时修复了Azure OpenAI权限提升CVSS 9.9（CVE-2026-45499）和Microsoft 365 Copilot权限提升CVSS 9.3（CVE-2026-41106），三者共同构成企业AI基础设施的全面攻击面——从AI助手RCE到云AI服务EoP，攻击者可以「AI as Attack Surface」策略一路穿透至核心业务。

影响范围

Microsoft 365 Copilot for iOS所有版本（修补前）；Microsoft 365 Copilot for Android所有版本（修补前）；涉及Copilot App与Hyper-V虚拟化交互的所有场景；关联漏洞：CVE-2026-45499 Azure OpenAI EoP CVSS 9.9、CVE-2026-41106 M365 Copilot EoP CVSS 9.3

修复建议：立即更新Microsoft 365 Copilot iOS/Android至最新版本；Hyper-V管理员优先部署2026年7月安全更新修复CVE-2026-48561；审查Copilot与AI服务之间的OAuth令牌权限最小化；在具备条件的环境启用网络分段隔离AI推理端点；关注即将修复的CVE-2026-45499（Azure OpenAI EoP）和CVE-2026-41106（M365 Copilot EoP）

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-57092 | CVSS 9.9 |

### Hyper-V VMSwitch虚拟机逃逸CVSS 9.9：Use-After-Free突破虚拟边界·低权限Guest直取宿主机·多租户云环境危急（Pwn2Own同类技术已演示）

CVE-2026-57092是Windows Hyper-V VMSwitch中的Use-After-Free漏洞，CVSS评分达到惊人的9.9——距理论满分仅0.1分。该漏洞允许低权限攻击者从虚拟机内部（Guest）穿越虚拟化安全边界，在宿主机（Host）上提升权限并执行任意代码。  攻击路径：低权限Guest用户利用VMSwitch网络虚拟化组件中的UAF漏洞，先破坏内核内存结构获取代码执行原语，再通过Hyper-V管理接口渗透至宿主机操作系统。一旦宿主机沦陷，攻击者即可横向访问同物理机上的所有虚拟机、窃取各VM中的敏感数据和凭据、植入持久化后门——典型的「一机沦陷，全云失守」场景。  Zero Day Initiative指出，类似技术已在Pwn2Own Berlin黑客大赛上被演示（针对VMware ESXi），证明此类虚拟化逃逸漏洞的利用技术已经成熟。在云托管、VPS、企业私有云等广泛使用Hyper-V的环境中，该漏洞的风险被进一步放大——一个受感染的租户可危及其他所有租户。  此漏洞与同月修复的Copilot Hyper-V逃逸（CVE-2026-48561 CVSS 9.6）和Secure Kernel Mode提权（CVE-2026-42982/50392 CVSS 7.8+）共同构成2026年7月虚拟化安全的「三重打击」。

影响范围

Windows Server Hyper-V所有受支持版本；Windows 10/11 Pro/Enterprise启用Hyper-V功能的主机；Windows Server Core及带桌面体验版本；Azure Stack HCI和Windows Server数据中心版（多租户云环境高危）

修复建议：立即部署2026年7月安全更新修复CVE-2026-57092（KB5101650等对应补丁）；云服务商和租户优先在Hyper-V宿主机集群滚动更新，减小业务中断窗口；VPS/共享托管用户应确认服务商已完成Hyper-V宿主机补丁；启用Credential Guard和HVCI虚拟化安全增强功能作为纵深防线；同时修补CVE-2026-48561（Copilot Hyper-V逃逸）和Windows Secure Kernel漏洞CVE-2026-42982/50392

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-58123 | CVSS 9.8 |

### Hermes WebUI未认证远程代码执行CVSS 9.8：仅需4个HTTP请求获取Unix Shell·嵌入式终端API零认证·影响20余行业（VulnCheck 7/9披露·PoC已在野外流传）

CVE-2026-58123是VulnCheck于7月9日披露的Hermes WebUI（开源AI Agent管理面板）未认证远程代码执行漏洞，CVSS满分级9.8（CVSS v3.1: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H）。该漏洞被评为可自动化利用——最致命的漏洞类型。  攻击极为简单：任何远程攻击者在无任何认证凭据的情况下，仅需发送四个顺序HTTP请求即可获取完整的Unix Shell：① 创建WebUI会话 → ② 通过终端API挂载PTY伪终端 → ③ 向终端输入端点写入任意命令 → ④ 命令以服务器进程用户身份执行，完全控制服务器。整个过程全自动、无需用户交互、无需前置权限。核心原因是嵌入式终端API端点（/api/auth/passkey/register等）完全没有任何认证检查（CWE-306关键功能缺少认证）。  受影响版本：Hermes WebUI所有0.51.788之前的版本。影响范围涵盖20余个行业（制造业、金融保险、医疗保健、专业服务、信息技术等），EPSS评分0.9%表明已存在野外攻击尝试。CISA已将其标记为「总技术影响+可自动化」，虽然暂未列入KEV目录但威胁评估极高。  该漏洞还关联同一项目中的认证绕过漏洞CVE-2026-55196（CVSS 9.1），攻击者可在无凭据环境下注册任意Passkey并获得永久管理控制权。两个漏洞结合使用可实现「零信任」的全系统接管——先绕过认证，再直接执行命令。

影响范围

Hermes WebUI 0.51.788之前所有版本（GitHub开源项目nesquena/hermes-webui）；AI Agent管理面板典型部署场景；影响20+行业：制造业、金融保险、医疗保健、信息技术、教育、零售等；关联漏洞：CVE-2026-55196（同项目Passkey认证绕过CVSS 9.1）

修复建议：立即升级Hermes WebUI至v0.51.788或更高版本（GitHub Release已发布）；如无法立即升级，在网络层（反向代理/防火墙）阻止对/api/terminal/\*\*端点的外部访问；禁用不再需要的嵌入式终端功能；审查所有HTTP API端点确保实施认证和输入验证；审计服务器日志中是否存在/api/terminal相关异常调用模式（4个连续未认证请求）

紧急提醒

本次速报为微软7月补丁星期二特刊。622个CVE修复创下历史纪录，其中63个为严重级（Critical），2个零日确认在野利用，1个零日有公开PoC。三大安全机构（Mandiant、Google FLARE、微软DART）在真实攻击中同时发现不同漏洞，表明针对微软生态的APT攻击已达到空前烈度。SharePoint Server 2016/2019扩展支持已于7月14日终止，不再接收安全更新——所有使用这两个版本的机构必须立即迁移，否则Unified Attack Chain的下一波攻击将无补丁可打。  CISA已发布SharePoint专用硬防警报（7月14日，7月16日更新新增CVE-2026-58644至KEV），要求联邦机构14天内完成修补。AI工具首次进入CVE高危排行榜（Copilot RCE CVSS 9.6、Azure OpenAI EoP CVSS 9.9），标志着「AI as Attack Surface」时代正式开启——安全团队必须将AI基础设施纳入威胁模型和补丁管理流程。

处置建议

① 立即部署微软2026年7月安全更新（KB5101650/相应累积更新），优先修补CVE-2026-55040（SharePoint JWT绕过）、CVE-2026-58644（SharePoint RCE满分）、CVE-2026-48561（Copilot RCE）、CVE-2026-57092（Hyper-V VMSwitch逃逸）

② SharePoint Server 2016/2019用户：扩展支持已终止，立即迁移至Subscription Edition或Microsoft 365云端版本，否则后续漏洞无补丁可打

③ 遵循CISA SharePoint硬防指南：公网暴露的SharePoint置于L7反向代理之后强制认证、阻止外部访问Central Administration、启用AMSI Full Mode请求体扫描

④ 启用AMSI签名检测：SuspSignoutReqBody.A（请求体扫描）、ToolPaneAuthBypass.A/C（请求头扫描/RCE覆盖）；部署MDAV监测Backdoor:MSIL/LeakFang.A!dha（IIS密钥窃取后门）

⑤ Hyper-V虚拟化环境：优先在宿主机集群滚动更新CVE-2026-57092补丁；云服务商商户确认宿主机已完成补丁；启用Credential Guard和HVC...