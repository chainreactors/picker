---
title: 每周网络安全简讯 ( 2026年 第35周 )
url: https://mp.weixin.qq.com/s/r0LagLE-xDxho_cfLoIOjw
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:59:09.559651
---

# 每周网络安全简讯 ( 2026年 第35周 )

# 每周网络安全简讯 ( 2026年 第35周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年8月22日至2026年8月28日，国家信息技术安全研究中心在线监测技术研究实验室对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计20条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织Tortoiseshell利用新型后门与反向SSH隧道对目标用户实施网络攻击

近日，安全研究人员披露APT组织Tortoiseshell进一步扩展网络间谍活动，新增Windows后门及反向SSH隧道工具，目标范围疑似覆盖中东及欧洲多个国家。该组织自2018年以来持续针对国防、航空航天、IT服务商和军事机构，并曾利用供应链入侵、被控网站及虚假招聘门户获取初始访问。此次发现的隧道组件伪装为wtsapi32.dll，通过443端口主动建立反向SSH连接，可绕过传统入站边界限制，为攻击者提供进入受害网络内部的隐蔽通道；另一款C++后门则通过DLL搜索顺序进行劫持加载，进而实施命令执行、文件上传下载、数据窃取、内存加载DLL、硬编码C2服务器通信等恶意操作。安全研究人员建议称，相关组织应重点监测异常DLL侧载、Windows进程发起的SSH连接、443端口非典型SSH流量及周期性HTTPS信标，以降低长期潜伏和二次访问风险。参考原文见：附件A1。

**链接：https://www.group-ib.com/blog/tortoiseshell-apt-toolset-infrastructure/**

02

网络动态

01

美国CISA发布联邦机构日志参考架构

8月20日，美国网络安全和基础设施安全局（CISA）发布《日志参考架构》（LRA），为联邦民事行政部门落实OMB备忘录M-26-14中的日志记录和网络可见性要求提供实施指导。该架构覆盖日志源、数据流、规范化、保留、完整性保护、访问控制和持续验证等环节，重点支持事件监控、威胁搜寻、事件响应和数字取证。CISA强调，日志建设不应单纯追求数据采集规模，而应确保遥测数据具备完整性、及时性、可追溯性和可用性，并建议结合MITRE ATT&CK评估检测覆盖情况。LRA还提出，可利用AI和机器学习提升异常检测、告警排序、事件关联和调查效率，但应保留人工审核、验证和回退机制。参考原文见：附件B1。

**链接****：https://www.cisa.gov/resources-tools/resources/logging-reference-architecture**

02

美国CISA红队演练揭示关键基础设施SOC、Active Directory与云安全薄弱环节

8月25日，美国网络安全和基础设施安全局（CISA）发布"A Tale of Two SOCs"红队评估结果，对政府服务设施和水务系统两类关键基础设施组织实施攻击链测试。两次演练中，红队均通过钓鱼获取初始访问权限，随后利用Active Directory默认Machine Account Quota、AD CS证书模板配置不当等问题实施权限提升和横向移动，并进一步尝试访问敏感业务系统、云资源及关键凭据。其中，组织A虽然部署了多个SOC和EDR平台，但因团队间缺乏联动、误报数量过大、缺少标准化升级流程及分析人员处置权限不足，导致红队长期未被发现，甚至成功读取SOC人员邮件并在防御人员终端部署键盘记录器。相比之下，组织B在钓鱼载荷执行后2至20分钟内即隔离受感染终端、切断C2通信，后续即使在"假设已失陷"条件下继续测试，防御人员仍能隔离OT非军事区堡垒主机，并阻断异常Azure登录。CISA指出，安全工具投入并不能替代成熟的运营流程，关键在于告警研判、跨团队协同、权限下放和快速隔离能力。参考原文见：附件B2。

**链接：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-237a**

03

美国CISA发布《互联网暴露降低指南》，降低IT/OT/ICS系统互联网暴露风险

8月21日，美国网络安全和基础设施安全局（CISA）发布《互联网暴露降低指南》（Internet Exposure Reduction Guidance），旨在降低信息技术（IT）、运营技术（OT）、工业控制系统（ICS）及工业系统暴露于互联网所面临的网络安全风险。该指南呼吁各组织评估可从互联网访问的系统，限制不必要的远程访问权限，并保护必须保持外部可访问的系统。CISA指出，2026年7月曾监测到针对水和废水系统行业100余个互联网暴露系统的恶意网络活动，多经由直接连接蜂窝调制解调器的可编程逻辑控制器（PLC）实施。同时，指南敦促关键基础设施组织将必要的远程访问经由安全网关、防火墙或VPN等集中管理的方案实施，而非直接连接PLC、人机界面或远程终端单元，并建议更改默认密码、应用安全补丁、部署跳板机与多因素认证，定期扫描互联网暴露资产。参考原文见：附件B3。

**链接****：https://www.cisa.gov/resources-tools/resources/exposure-reduction**

04

美国CISA发布《漏洞审查报告》

8月26日，美国网络安全和基础设施安全局（CISA）发布《漏洞审查报告》（Vulnerability Review），基于2024和2025财年数据，分析安全漏洞根因及关键基础设施暴露风险，并推动"安全设计"（Secure by Design）理念从源头降低漏洞风险。报告指出，CVE数据仍普遍存在CVSS字段缺失、CWE归类不足及描述不完整等问题，影响漏洞研判和自动化处置。同时，内存安全和输入验证不当漏洞在已知被利用漏洞（KEV）中的占比明显偏高，2024和2025财年分别达到19.7%和16.7%，被扫描关键基础设施实体中有26%仍暴露存在风险的网络服务，FTP、RDP、SMB和Telnet等协议可能成为初始入侵或横向移动入口。CISA建议软件厂商在开发生命周期中强化安全设计、内存安全及输入验证，相关组织应优先修复KEV、减少不必要的互联网暴露服务，加强补丁和配置管理，以降低安全风险。参考原文见：附件B4。

**链接****：https://www.cisa.gov/resources-tools/resources/cisa-vulnerability-review**

05

美国NIST发布《使用人工智能开展CSF分析与报告快速入门指南》草案

美国国家标准与技术研究院（NIST）发布SP 1353《使用人工智能开展CSF分析与报告快速入门指南》草案，探索利用生成式人工智能辅助网络安全框架（CSF）2.0合规分析和报告。该指南提供结构化提示词及3类示例用例，可用于评估组织网络安全政策、战略和风险治理与CSF 2.0要求的匹配程度，同时根据CSF2.0对相关安全实践进行映射。NIST同时强调，AI应用应保留人工监督和数据保护机制，避免将生成结果直接替代专业判断。综上，美国正推动AI逐步进入治理、风险与合规（GRC）流程，以降低框架映射、差距分析和报告编制的人力成本，并可能对后续联邦采购和审计实践产生影响。参考原文见：附件B5。

**链接****：https://techjacksolutions.com/ai-brief/nist-sp-1353-ai-cybersecurity-framework-compliance-guide/**

06

美国陆军推进"格里芬计划"，探索低成本高安全AI网络防御代理

美国陆军正通过"格里芬计划"（Project Griffin）推进AI网络防御代理建设，核心能力"智能响应与协调节点"（Intelligent Response and Orchestration Node,IRON）拟接入现有网络传感器数据，自动识别恶意活动并执行防御操作，以提升对高速、海量网络威胁的响应效率。美国陆军强调，相关AI代理必须在降低模型调用和Token成本的同时，避免因代理自身脆弱性扩大攻击面，并能够区分真实威胁与误报，对每项操作保留完整审计记录。IRON将采用零信任架构和开放API，通过端点管理、Microsoft Defender等策略执行点实施临时阻断、漏洞修补等操作，同时支持人工设置响应置信阈值，并配置"主终止开关"和撤销机制，以便快速停止或回滚高风险自主行为。参考原文见：附件B6。

**链接****：https://defensescoop.com/2026/08/21/army-wants-fast-ai-cybersecurity-agents-wont-run-up-costs-create-vulnerabilities/**

07

ISASecure与美国国家安全局合作推出高关键性OT组件HCSA认证方案

国际自动化协会旗下ISASecure正与美国国家安全局（NSA）合作开发高关键性组件安全保障（HCSA）认证方案，面向美国政府采购用于国家安全系统的商用运营技术（OT）组件。该方案以ISA/IEC 62443-4-2组件安全要求为基础，结合NSA运营技术保障伙伴关系计划新增技术要求，旨在提升高关键性OT产品的安全可信度。待HCSA方案完成并获NSA相关项目办公室认可后，可作为OT OEM组件进入国家安全系统OT产品合规清单的重要认证依据。参考原文见：附件B7。

**链接****：https://www.automationworld.com/cybersecurity/news/55400131/isasecure-launches-hcsa-certification-scheme-for-high-criticality-industrial-components**

08

特朗普签署第14420号行政命令，强化美国大容量电力系统外国设备与供应链安全管控

8月26日，美国白宫官方网站发文称，美国总统特朗普发布第14420号行政命令，宣布因外国供应的大容量电力系统设备可能带来网络安全和供应链风险而进入国家紧急状态。行政命令指出，先进制造、数据中心、人工智能及国防生产对可靠电力依赖持续上升，外国实体可能通过设备漏洞、数字后门、远程访问能力或供应中断影响美国关键基础设施安全。命令授权能源部长限制与特定外国实体相关的电力设备及其软件、固件、数字服务和远程访问功能交易，并可要求对已部署的高风险设备实施识别、隔离、监控、断开、更换或移除。同时，美国将加强相关设备和供应商审查，并推动联邦采购规则调整，优先考虑美国制造的能源基础设施。参考原文见：附件B8。

**链接****：https://www.whitehouse.gov/presidential-actions/2026/08/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system/**

09

英国小型发电设施疑遭伊朗黑客组织攻击停运

英国一家小型发电设施据称于7月遭伊朗黑客组织攻击，并停止运行约4天。英国政府表示，事件未造成大范围停电，也未对全国电力系统构成风险，目前官方尚未正式完成攻击归因。事件发生后，英国政府已向能源行业高管通报加强关键基础设施防护的措施，并与国家网络安全中心、监管机构共同评估威胁。相关专家认为，暴露在互联网的设备、远程访问凭证、脆弱网关和第三方账户仍是OT环境常见薄弱环节。参考原文见：附件B9。

**链接****：https://www.telegraph.co.uk/news/2026/08/22/iranian-hackers-shut-down-uk-power-plant/**

10

GPUThor新型攻击方式可绕过NVIDIA GPU ECC防护并实现Root提权

近日，安全研究人员披露新型GPU Rowhammer攻击GPUThor，可绕过NVIDIA部分GPU的纠错码（ECC）防护，造成拒绝服务并实现Root级权限提升。该攻击通过设计非均匀内存反复访问"锤击"（Rowhammer）模式，规避GDDR6目标行刷新（TRR）机制，并利用GPU内存请求合并等特性显著提高比特翻转效率，进而造成数据损坏等安全问题，同时GPUThor还可通过破坏GPU页表，使低权限CUDA程序获得任意内存访问能力，进而在宿主机打开Root Shell，以Root权限执行任意指令。研究显示，该攻击方式在RTX A4000、A4500、A5000和A6000等Ampere架构GPU上均得到验证，A100等服务器级Ampere GPU及部分Blackwell GPU同样可能面临类似风险。目前，NVIDIA已发布安全建议，要求启用SYS-ECC和IOMMU/DMA隔离、监控GPU错误告警，并限制不受信任CUDA任务及跨租户GPU共享，以降低遭受攻击的风险。参考原文见：附件B10。

**链接****：https://www.bleepingcomputer.com/news/security/new-gputhor-attack-defeats-nvidia-ecc-protection-for-root-access/**

03

漏洞资讯

01

NVIDIA NemoClaw存在本地AI模型投毒漏洞

安全研究人员披露NVIDIA NemoClaw存在本地AI模型投毒漏洞（CVE-2026-65105），与部分平台上的Ollama服务配置有关，当Ollama绑定至0.0.0.0:11434且缺少身份认证时，攻击者可结合DNS重绑定绕过浏览器同源限制，访问本地推理接口，并通过/api/create修改模型聊天模板。被篡改后的模板可在后续推理过程中持续向系统消息附加攻击者控制的隐藏指令，从而影响AI代理行为，并可能进一步滥用其已获授权的工具和访问权限。目前，安全人员建议相关用户限制Ollama仅监听本地回环地址，避免暴露11434端口，以降低遭受攻击的风险。参考原文见：附件C1。

**链接：https://www.cyera.com/research/nemoclaw-one-website-visit-to-hijack-your-ai-agent**

02

Next.js存在2个安全漏洞

近日，安全研究人员发现Next.js存在2个安全漏洞。其中，第一个安全漏洞是路径遍历漏洞（CVE-2026-75604），影响运行于Windows文件系统、使用Pages Router或未启用Cache Components的App Router应用，攻击者无需身份验证即可通过构造恶意请求访问预期目录之外的位置，可能造成敏感数据泄露、服务器内容篡改或服务中断。第二个安全漏洞位于Next.js图像优化API及其依赖的libheif库，攻击者可提交恶意AVIF图像，在服务器处理过程中触发远程代码执行，对用户系统造成影响。目前，用户可通过将版本升级至15.5.24和16.3.3的方式修复上述安全漏洞。参考原文见：附件C2。

**链接：https://cybersecuritynews.com/next-js-vulnerabilities/**

03

Adobe Campaign Classic存在3个安全漏洞

近日，安全研究人员发现Adobe Campaign Classic存在3个安全漏洞。其中，CVE-2026-76197和CVE-2026-76195属于操作系统命令注入漏洞，攻击者无需身份验证或用户交互即可通过构造恶意输入，以Campaign Classic进程权限执行任意系统命令；CVE-2026-76193为服务端请求伪造（SSRF）漏洞，可被用于访问内部服务及原本不可访问的系统，并可能进一步形成代码执行攻击链。漏洞影响Windows和Linux平台上的Adobe Campaign Classic 7.4.4 build 9400及更早版本，目前用户可通过版本升级等方式修复上述安全漏洞。参考原文见：附件C3。

**链接：https://cybersecuritynews.com/adobe-campaign-classic-code-execution/**

04

TeamViewer存在路径遍历漏洞

近日，安全研究人员发现TeamViewer存在路径遍历漏洞（CVE-2026-16444），是由桌面客户端对远程会话中文件路径校验不当所导致，已获取初步身份认证的攻击者可在文件传输或虚拟文件剪贴板过程中构造路径遍历文件名，将文件写入本地预期目录之外的位置。攻击者如将恶意可执行文件、脚本、快捷方式或配置文件写入启动、应用或系统目录，可能进一步实现持久化、数据破坏或以当前用户权限执行代码。漏洞影响Windows、macOS和Linux平台的TeamViewer Full Client、Host及QuickSupport 15.81.5之前版本，目前用户可通过版本升级修复上述安全漏洞。参考原文见：附件C4。

**链接：https://cybersecuritynews.com/multiple-teamviewer-vulnerability/**

05

Apache Log4j2存在反序列化绕过安全缺陷

近日，安全研究人员披露Apache Log4j2存在编号为#4255的安全缺陷，位于FilteredObjectInputStream中，其允许反序列化的java.rmi.MarshalledObject可封装恶意对象，并在后续调用过程中通过未过滤的ObjectInputStream加载隐藏载荷，从而在特定部署环境下绕过反序列化允许列表并触发远程代码执行。同时，安全人员声称，该安全缺陷利用条件较为苛刻，并非类似Log4Shell的通用漏洞，仅影响接受不可信序列化Log4j事件的遗留或自定义接收器。Apache官方建议停止使用Java序列化传输日志，改用JSON或RFC 5424 over TLS，并排查未经身份验证的旧式日志接收服务，以降低遭受攻击的风险。参考原文见：附件C5。

**链接：https://cybersecuritynews.com/new-apache-log4j2-flaw/**

04

木马病毒

01

借虚假Minecraft客户端和SEO投毒持续传播的Weedhack恶意软件被披露

近日，安全研究人员发现Weedhack恶意软件持续针对Minecraft玩家进行传播。攻击者搭建仿冒Minecraft客户端和模组网站，并利用SEO投毒提高搜索排名，诱导用户下载携带恶意JAR载荷的客户...