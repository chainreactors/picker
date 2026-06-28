---
title: 工业网络安全周报-2026年第25期
url: https://mp.weixin.qq.com/s/ilUWk1ccn1M7XWsNWXsZUA
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:11:00.533473
---

# 工业网络安全周报-2026年第25期

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/O4nsfsdRttw57ZuHRnqlepm4EKxwo6ks86WTuiayGrmZpgekXM3Grm7QGiahxKEdV03rpXV4lmyHOyfJLR3nzY5JsbaskDsQ9dWVXZicT8qYJM/0?wx_fmt=jpeg)

# 工业网络安全周报-2026年第25期

OT工控安全领导者
OT工控安全领导者

安帝Andisec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/ll2PVky3MmaYz8UWHicLDSC4e3NqcibOLicCiaYtmQm9A0Ied3OLs4Wibj6bLz8jmf0gB3k0h1aQNNVKNqjKFcZV0Mg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

本文预计阅读时间27分钟

BREAKING NEWS

本 期 摘 要

**政策法规方面**，美国国家标准与技术研究院提出新的水务基础设施远程访问安全指南。

**漏洞预警方面**，瑞士ABB公司发布其Freelance分布式控制系统产品线关键漏洞安全公告；西门子百余款工控产品曝“核弹级”OpenSSL漏洞，CISA紧急预警；美国网络安全和基础设施安全局更新已知被利用漏洞目录；美国达科公司发布安全更新修复控制器漏洞；美国Lantronix公司网络设备漏洞正被积极利用；Cisco Catalyst SD-WAN Manager零日特权提升漏洞（CVE-2026-20245）正被利用获取Root权限；Siemens SIMATIC WinCC Unified PC Runtime Certificate Manager存在密钥明文存储漏洞 。

**安全事件方面**，俄罗斯军用战斗控制平台（Glaz/Groza）被攻破致战术手册与技术规格外泄；美国加州水务公司遭黑客宣称入侵，官方核查工控系统未受攻击 ；加拿大安大略省London Hydro公司发生数据泄露事件；伊朗关联APT组织MuddyWater伪装勒索团伙实施情报窃取行动；印度塔塔电子公司发生数据泄露事件；巴西国家民用防护紧急预警播发平台遭入侵并发送虚假极端警报，关键基础设施通信安全警示。

**风险预警方面**，英国SAFE-Matter公司发文指出安全治理存在举证短板。

**安全技术方面**，美国Forescout公司推出后量子密码就绪度与加密运维可视化仪表盘。

**政策法规**

1. 美国国家标准与技术研究院提出新的水务基础设施远程访问安全指南

2026年6月25日，美国国家标准与技术研究院联合工控厂商、各地水务运营机构推出面向供水、污水处理行业 OT 远程运维全套参考架构，远程接入通道长期是水务工控系统最高危攻击入口，此前多起供水设施入侵事件均源于无防护远程工具滥用。指引针对小型、大中型水务企业分别设计本地部署、云端两套隔离访问方案，统一明确身份认证、会话审计、网络分区、权限最小化四项强制安全基准，要求运维远程操作全程留存操作日志，杜绝共享账号、公网直连控制器等高危操作模式。整套方案无绑定特定软硬件，全部采用市面通用工控安全设备即可落地，兼顾小型水厂预算不足、大型跨区域水务集团多级管控两类场景。同时文件配套资产盘点、数据完整性校验配套管控细则，要求水务企业定期排查远程接入漏洞，完成网络隔离改造。若水务机构未遵循该指引加固远程通道，黑客可借助公开工具渗透水厂SCADA系统，篡改水处理药剂配比、切断居民供水，直接危害公众饮水安全与民生基础设施稳定运行，该规范已成为美国EPA、CISA推荐水务行业合规核心参考依据。

资料来源：

https://www.cybersecuritydive.com/news/water-utilities-remote-access-nist-guidance/823776/

**漏洞预警**

2. 瑞士ABB公司发布其Freelance分布式控制系统产品线关键漏洞安全公告

2026年6月23日，美国网络安全和基础设施安全局（CISA）发布了关于ABBFreelance Security Lock认证绕过漏洞（CVE-2025-7064）的安全通告（ICSA-26-174-05）。该漏洞被评定为中危级别（CVSS 6.6），影响ABB Freelance分布式控制系统（DCS）的全系列版本，包括2013、2016、2019及2024版。漏洞根源在于系统锁定机制存在设计缺陷，攻击者在获得本地物理接触或已登录普通用户权限的情况下，可利用现代键盘的未公开特殊组合键，绕过Freelance Operations的全屏安全锁定界面，非法访问底层Windows操作系统功能。这意味着原本用于隔离操作人员的“安全锁”形同虚设，攻击者可借此突破OT环境的操作限制，对用户管理模块发起进一步攻击，甚至可能破坏工业现场的生产流程完整性。鉴于该漏洞无法通过远程利用，CISA强烈建议各关键基础设施运营单位实施纵深防御策略，严格限制控制网络的物理访问权限，将工业网络与企业网进行物理或逻辑隔离，并参考ABB官方PSIRT公告（7PAA020361）进行安全配置加固。目前CISA尚未监测到针对该漏洞的在野利用，但鉴于其针对OT操作站的特定攻击场景，建议相关单位尽快排查并落实缓解措施，防止因本地旁路导致严重的安全事故。

资料来源：

https://www.cisa.gov/news-events/ics-advisories/icsa-26-174-05

3. 西门子百余款工控产品曝“核弹级”OpenSSL漏洞，CISA紧急预警

2026年6月23日，美国网络安全和基础设施安全局（CISA）转发了西门子公司关于多款工业产品中所使用 OpenSSL 密码库存在高危栈缓冲区溢出漏洞（CVE-2025-15467，CVSS 9.8 Critical）的安全通告。该漏洞位于OpenSSL 3.x版本的CMS解析逻辑中，在处理经 AES-GCM封装的恶意AuthEnvelopedData结构时，未正确校验初始化向量（IV）长度，导致栈缓冲区越界写入，攻击者可构造特制PKCS#7/S/MIME 消息，在无需认证、无需用户交互的条件下触发拒绝服务甚至远程代码执行。受影响 OpenSSL 版本为 3.0、3.3、3.4、3.5 及 3.6（1.1.1 及 FIPS 模块不受影响），波及西门子百余款工控产品，包括 SCALANCE 全系工业以太网交换机与路由器、SIMATIC WinCC V7.5/V8.x 及 WinCC OA、SIMATIC HMI Comfort / Basic / Mobile Panels等。鉴于部分SCALANCE路由器和SINEC NMS处于OT网络边界且可能处理外部证书或配置推送，此漏洞若被利用可作为横向移动或持久化驻留的突破口。西门子已针对部分产品发布修复固件/版本，其余待更新。CISA 与西门子建议运营单位立即排查资产清单，优先升级边界设备与工程师站至安全版本；暂无法升级时，应在邮件网关过滤CMS附件类型（.p7m/.p7c），严格隔离OT网络避免直接从外网访问设备管理端口，并按西门子工业安全操作指南强化主机与网络层防护。

资料来源：

https://www.cisa.gov/news-events/ics-advisories/icsa-26-174-03

4. Daktronics控制器固件多漏洞通告，未授权可达Root访问风险

2026年6月25日，美国网络安全和基础设施安全局（CISA）发布关于Daktronics公司VFC-DMP-5000、DMP-5000及DMP-8000系列LED显示屏网络控制器固件存在多处高危安全缺陷的安全通告。受影响漏洞主要包括：CVE-2026-28701——目录遍历（CWE-22），允许未认证攻击者通过特制 HTTP 请求读取系统敏感文件（含配置文件、日志）；CVE-2026-33560——不受限的危险类型文件上传，Web管理界面未充分校验上传文件类型与路径，攻击者可上传恶意可执行文件或脚本；以及部分固件版本中存在硬编码默认凭证，可被低权限探测获取管理访问权。上述漏洞组合利用可使攻击者完全绕过认证、上传 Webshell或二进制程序，最终获取设备root级完全控制权，进而篡改显示内容、作为内网跳板横向移动或造成拒绝服务。受影响固件版本为低于v8.117.x.x、v9.43.x.x及v10.34.x.x的各型号控制器，常见于体育场馆、交通枢纽及公共信息发布大屏系统。Daktronics已发布修复版本，建议运营单位立即核查资产清单、升级至安全固件版本、修改所有默认及硬编码密码为强唯一凭据，并通过防火墙限制设备管理端口（HTTP/HTTPS/Telnet）仅允许可信网段访问，禁止从互联网或未授权内网直接可达。

资料来源：

https://www.cisa.gov/news-events/ics-advisories/icsa-26-176-04

5. 台达电子DTM Soft反序列化漏洞通告 (CVE-2026-12578)

2026年6月25日，美国CISA发布工业控制系统安全公告，TrendAI Zero Day Initiative 研究员 kimiya 发现露台达电子（Delta Electronics）DTM Soft软件存在高危安全漏洞。受影响产品为 Delta Electronics DTM Soft 全版本，该漏洞编号为CVE-2026-12578，属于CWE-502不受信任数据的反序列化（Deserialization of Untrusted Data）。攻击者可通过诱导用户在DTM Soft中打开特制的恶意项目文件（.xml 或序列化对象文件），触发反序列化缺陷并在本地执行任意代码。CVSS v3.1评分为7.8（高），CVSS v4.0评分为8.4。此漏洞不可远程利用。台达电子暂未发布修复补丁，建议用户采取临时规避方案如切勿打开来历不明的项目文件、邮件附件或未知链接中的文件；避免使用"以管理员身份运行"启动软件，应限定在标准用户权限下运行以降低影响；参照台达官网产品安全公告等待官方补丁。此外应遵循工控系统典型防护原则：限制控制设备互联网暴露、将工控网络隔离在防火墙后方、谨慎使用VPN远程访问。目前CISA尚未收到该漏洞被野外利用的报告。

资料来源：

https://www.cisa.gov/news-events/ics-advisories/icsa-26-176-06

6. 美国Lantronix公司网络设备漏洞正被积极利用

2026年6月24日，美国CISA发出紧急通告，披露朗特罗尼克（Lantronix）EDS5000系列串口转IP设备存在严重代码注入漏洞CVE-2025-67038（CVSS 3.1 评分 9.8），且已在现实中被主动利用，要求联邦民行机构（FCEB）于2026年6月 26日前完成修复。漏洞详情：该漏洞位于设备的 HTTP RPC 模块——当用户认证失败时，模块会将用户名拼接进Shell 令写入日志，而未对用户名参数做任何过滤/转义，导致攻击者可在登录用户名字段中注入任意操作系统命令，并以 root 特权执行。此漏洞无需认证、可远程利用，危害极高。该缺陷由Forescout Vedere Labs在2026年4月首次披露，影响Lantronix及Silex的部分串口转IP转换器，CISA暂未公布具体利用者及攻击手法细节。Lantronix 已发布固件修复版本，建议立即升级受影响的EDS5000设备至最新固件。

资料来源：

https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html

7. Cisco Catalyst SD-WAN Manager零日特权提升漏洞（CVE-2026-20245）正被利用获取Root权限

2026年6月24日，疑似国家级APT组织正在活跃利用Cisco Catalyst SD-WAN Manager（原 vManage）的零日特权提升漏洞CVE-2026-20245（CVSS 3.1评分7.8，CWE-116输出编码/转义不当）实施攻击。该漏洞位于控制器CLI的文件上传功能中，拥有netadmin权限的已认证攻击者可上传特制CSV文件触发命令注入，将任意账户写入/etc/passwd和/etc/shadow实现root级命令执行。攻击链显示威胁者先可能利用了两个未公开认证绕过漏洞（类 CVE-2026-20127 / CVE-2026-20182，CVSS 10.0）获取管理员权限，随后使用默认账号 vmanage-admin登入、篡改密码并导出设备配置，再通过上传恶意evil\_tenant.csv提升至root 并系统性清除日志与文件以抹除入侵痕迹。受影响的部署形态含本地、云端及FedRAMP政务云环境。Cisco已发布修复版本（20.9.9.2、20.12.7.2、20.15.4.5、20.15.5.3、20.18.3.1、26.1.1.2 及以上），应立即升级。

资料来源：

https://cybersecuritynews.com/cisco-catalyst-sd-wan-manager-0-day/

8. Siemens SIMATIC WinCC Unified PC Runtime Certificate Manager存在密钥明文存储漏洞

2026年6月23日，西门子（Siemens）发布安全通告，披露SIMATIC WinCC Unified PC Runtime所集成的 Certificate Manager组件存在明文存储密钥材料缺陷。WinCC Certificate Manager在本地磁盘上对证书私钥或敏感密钥信息进行未加密存储（Cleartext Storage in a File or on Disk），攻击者在获得本地系统访问权限（物理接触或已入侵工程师站）后，可直接读取明文密钥材料，进而伪造证书、解密通信流量或冒充受信任节点，严重威胁OT环境身份认证与通信保密性。CVSS v3.1 评分为 7.1，属本地攻击，不可远程利用。受影响产品涵盖SIMATIC WinCC Unified PC Runtime V16、V17、V18、V19、V20 全版本等；Siemens 已发布修复版本，建议优先升级或在不可升级场景下严格限制工程师站本地访问权限、使用专用账户并启用磁盘加密（BitLocker/全盘加密）。CISA同步建议通过防火墙隔离OT网络、禁止从互联网或非信任内网直连设备管理平台。

资料来源：

https://www.cisa.gov/news-events/ics-advisories/icsa-26-174-01

**安全事件**

9. 俄罗斯军用战斗控制平台（Glaz/Groza）被攻破致战术手册与技术规格外泄

2026年6月25日，据多家安全媒体援引SC World报道，乌克兰黑客组织宣称成功入侵俄罗斯联邦武装部队使用的Glaz/Groza（格拉兹/格罗扎）战斗控制与指挥平台（C2 System），并获取大量敏感军事文档，包括系统操作手册（Operator Manuals）、专利技术申请书（Patent Filings）、训练教材、战术程序说明及系统技术规格书。Glaz/Groza是俄军用于协调战场分队行动、下达指挥指令的军用OT/C2 系统，此次泄露暴露了该平台的系统架构设计细节、作战流程逻辑、潜在安全弱点及部署局限性，理论上可为对手提供逆向分析、漏洞挖掘乃至电磁/网络干扰的切入点，属高价值军事情报损失。目前尚无证据表明攻击者对C2系统本身植入后门或造成实时作战中断，主要损害为指挥控制体系知识资产失密。此事件凸显军用 OT/C2、关键基础设施指挥平台面临定向网络入侵（Cyber Intrusion against C2）的高风险。

资料来源：

https://www.cybermaterial.com/p/ukrainian-hackers-breach-russian

10. 美国加州水务公司遭黑客宣称入侵，官方核查工控系统未受攻击

2026年6月25日，据媒体报道，关联伊朗的黑客组织宣称入侵美国加州水务公司Cal Water，放出5GB窃取数据，声称可操控系统扰乱供水，以此报复美方针对伊朗基础设施的举措，并称未实施破坏行为。泄露内容包含用户住址、账单等隐私信息，以及管网测绘平台账号、内网IP等内部资料。事发后，加州水务联合安全机构全面排查供水OT工控系统，调查确认不存在OT系统遭入侵的证据。黑客仅入侵计费、管网测绘类IT系统，该网络与管控水泵、水处理的核心供水设备物理隔绝，攻击者无法干预供水设施，当地供水未出现中断、水质管网均未受影响。安全专家表示，黑客夸大破坏能力是制造恐慌的网络心理战，该组织此前也常有夸大攻击成果的行为。本次事件风险集中在用户隐私泄露，虽未引发供水事故，但该黑客曾部署破坏性病毒，隐患仍存。目前企业已重置泄露账号、加固内网隔离，并协同各级监管部门持续监测相关网络威胁。

资料来源：

https://www.securityweek.com/cal-water-finds-no-evidence-of-ot-activity-after-hackers-claimed-they-could-disrupt-water-supply/

11. 加拿大安大略省London Hydro公司发生数据泄露事件

2026年6月24日，据媒体报告，该公司近日确认发生客户数据泄露事件，未经授权方获取了一定规模的客户敏感信息。据披露，被泄露数据涵盖客户姓名、实际住址、电子邮箱、电话号码、账户编号、账单编号、服务地址、资费套餐、合同起始日期及电表信息等，几乎覆盖公用事业客户的核心个人身份与消费数据。London Hydro目前尚未公布受影响客户数量、入侵手段及发现时间，事件具体成因仍在调查中。由于账单编号与账户信息可直接用于账户接管（ATO），结合客户完整联系方式与服务地址，攻击者可精准实施定制化钓鱼攻击（Spear Phishing），伪造电力公司或第三方服务商名义诱导受害者转账或泄露更多敏感信息；服务地址与账户信息的关联还可能导致身份盗用（Identity Theft）及更复杂的欺诈链条。建议受影响客户密切监控账户异常变更、开启账单/账户变动提醒、核实所有自称London Hydro的来电及邮件真实性（通过官方渠道二次确认），切勿点击可疑链接或提供额外个人信息；运营单位应以此事件为鉴，审查客户数据访问权限、强化数据库及API接口安全管控、部署异常访问行为检测并完善数据外泄应急响应预案。

资料来源：

https://www.scworld.com/brief/london-hydro-customer-dat...