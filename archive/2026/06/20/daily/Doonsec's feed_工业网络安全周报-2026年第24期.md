---
title: 工业网络安全周报-2026年第24期
url: https://mp.weixin.qq.com/s/gdFg5pTSuSLVlEUs955lAA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:47:32.342159
---

# 工业网络安全周报-2026年第24期

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/O4nsfsdRttyILsE7r03J3xWDe6RdN6OhuzYibib6iaPKVjxzpmDBFHkCBgksmnLpUv6R07zGpuACklFdvXJJuJtot4TWQlXsKdH6LibcEoEMo1c/0?wx_fmt=jpeg)

# 工业网络安全周报-2026年第24期

OT工控安全领导者
OT工控安全领导者

安帝Andisec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/ll2PVky3MmaYz8UWHicLDSC4e3NqcibOLicCiaYtmQm9A0Ied3OLs4Wibj6bLz8jmf0gB3k0h1aQNNVKNqjKFcZV0Mg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

本文预计阅读时间22分钟

BREAKING NEWS

本 期 摘 要

**政策法规方面**，美国白宫发布NSPM-12备忘录，完善国家安全系统网络安全集中治理体系。

**漏洞预警方面**，Rockwell Automation FactoryTalk Analytics PavilionX存在高危权限缺失漏洞（CVSS 7.0/8.3），攻击者可执行特权操作；Cisco SD-WAN Manager曝零日文件上传漏洞（CVSS 7.8），已被积极利用提权至root；Palo Alto PAN-OS命令注入漏洞（CVSS高危）允许认证管理员以root执行任意命令；Palo Alto GlobalProtect VPN认证绕过漏洞（CVSS 7.8）披露后仅4天即遭野外利用；Fortra Access Manager命令注入漏洞（CVSS 9.8）可远程执行任意系统命令；CISA将LiteSpeed cPanel插件权限提升漏洞纳入已知被利用目录，要求限期修复。

**安全事件方面**，意大利亚得里亚港务局遭Anubis勒索软件袭击，仅攻陷IT系统便重创海运关键基础设施；丹麦药企诺和诺德发生数据泄露数日之后，又一家医疗企业遭遇网络攻击；俄罗斯基础软件服务商Astral遭遇定向网络攻击，政企财税政务服务大面积中断洞；澳大利亚第二大制糖企业遭遇勒索软件攻击，工厂生产线全面停工；黑客组织ShinyHunters宣称入侵美国零售巨头杰西潘尼JCPenney，威胁曝光海量消费者数据实施勒索施压；越南黑客组织OceanLotus从境外间谍活动转向国内进行定向供应链攻击；伊朗关联黑客组织Handala宣称入侵美国加州水务企业Cal Water。

**风险预警方面**，现代SaaS中的信任危机：身份认证成功却仍然被攻破，零信任架构须延伸至每一次服务间调用与API令牌生命周期管理。

**安全技术方面**，Meta联合五角大楼供应商为其智能眼镜原型开发面部识别功能，可穿戴智能设备对关键基础设施场所物理安全构成新型社会工程学攻击风险。

**政策法规**

1. 美国白宫发布NSPM-12备忘录，完善国家安全系统网络安全集中治理体系

2026年6月17日，据Industrial Cyber报道，美国白宫发布NSPM-12备忘录，面向军事、情报等涉密国家安全系统重塑网络安全治理框架。文件重启跨部门CNSS委员会统筹多方协同，指定NSA作为统一技术主管，统筹威胁研判、应急指令发布、密码体系及跨密级隔离管控，将NIST规范定为基础安全基线，并设置分阶段时限落地政策整合、涉密云安全优化、网络事件上报标准修订等任务，同时延伸14306号行政令相关安全要求，要求各机构定期梳理上报涉密系统资产。新政打通军方、情报及民用联邦部门协同渠道，压实运营主体安全问责，促进政企、国际安全情报共享，针对性解决过往监管分散、标准不统一、涉密云防护薄弱等治理短板，全面提升涉密关键系统抵御高级网络攻击的整体韧性。

资料来源：

https://industrialcyber.co/regulation-standards-and-compliance/white-house-rolls-out-nspm-12-to-boost-cybersecurity-governance-oversight-accountability-for-national-security-systems/

**漏洞预警**

2. Rockwell Automation FactoryTalk Analytics PavilionX存在高危权限缺失漏洞（CVSS 7.0/8.3）

2026年6月16日，据CISA公告ICSA-26-167-01披露，Rockwell Automation FactoryTalk Analytics PavilionX存在高危漏洞CVE-2025-14272（CVSS v3 7.0 / v4 8.3），源于API端点的授权执行不当（CWE-862），攻击者可执行未授权的特权操作，包括用户/角色管理及其他管理操作。受影响版本为PavilionX< 7.01。该平台广泛用于能源、制造与水处理行业的集中数据分析，一旦被利用可能导致生产调度数据被篡改或窃取。Rockwell已发布7.01及以上修复版本，建议OT运营方立即升级并限制API对外暴露面，同时参照SD1777安全公告执行访问控制加固。

资料来源：

https://www.cisa.gov/news-events/ics-advisories/icsa-26-167-01

3. Cisco SD-WAN Manager零日漏洞（CVE-2026-20262，CVSS 7.8）已被积极利用，攻击者可提权至root

2026年6月16日，The Register报道，Cisco Catalyst SD-WAN Manager存在零日漏洞CVE-2026-20262（CVSS 7.8），源于文件上传功能对用户输入验证不足，低权限远程攻击者可通过特制HTTP请求在系统上创建或覆盖任意文件，最终以root权限执行代码。Cisco PSIRT于本月早些时候发现该漏洞正被"高度复杂的网络威胁行为者"积极利用，影响所有部署类型（本地/云托管）。同批披露的CVE-2026-20182为身份验证绕过漏洞，允许攻击者以高权限非root身份登录并执行特权操作。Cisco已发布多版本补丁（20.9.9.2、20.12.7.2等），建议立即升级并审计vmanage-admin账户SSH密钥文件中是否存在异常公钥注入。

资料来源：

https://www.theregister.com/2026/06/16/cisco\_sdwan\_manager\_vulnerability/

4. Palo Alto PAN-OS命令注入漏洞（CVE-2026-0273）允许认证管理员以root执行任意命令

2026年6月12日，Palo Alto Networks披露PAN-OS多个新漏洞。CVE-2026-0273为命令注入漏洞，允许已认证管理员通过CLI或Web管理界面以root权限执行任意命令；CVE-2026-0272为CLI权限提升漏洞；CVE-2026-0269为隧道流量拒绝服务漏洞。其中CVE-2026-0273对PA-Series和VM-Series防火墙构成重大威胁，攻击者可完全控制设备配置与网络流量。Palo Alto已于5月13日发布补丁，建议所有企业级防火墙管理员立即更新并审计管理接口访问日志，排查是否存在异常命令执行记录。

资料来源：

https://security.paloaltonetworks.com/PAN-OS/PAN-OS-command-injection-vulnerability-CVE-2026-0273

5. Palo Alto GlobalProtect VPN认证绕过漏洞（CVE-2026-0257，CVSS 7.8）披露后仅4天即遭野外利用

2026年6月15日，Palo Alto Networks Unit 42发布紧急警告，确认CVE-2026-0257正被积极利用。该漏洞影响PAN-OS软件的GlobalProtect门户和网关组件，允许未认证远程攻击者绕过安全控制，建立未授权VPN连接。从漏洞披露（5月13日）到首次野外利用仅间隔4天，体现了边界设备漏洞利用的加速趋势。攻击者利用该漏洞可直连内网PLC/HMI等工控设备。Palo Alto建议所有GlobalProtect用户立即升级至修复版本，并审查VPN认证日志中是否存在异常登录事件，重点关注来源IP与登录时间异常。

资料来源：

https://unit42.paloaltonetworks.com/cve-2026-0257-globalprotect-authentication-bypass/

6. Fortra Access Manager严重命令注入漏洞（CVE-2026-9862，CVSS 9.8）

2026年6月17日，Fortra披露其Core Privileged Access Manager（BoKS）产品存在严重OS命令注入漏洞CVE-2026-9862（CVSS v3.1评分9.8）。该漏洞位于BoKS的自动注册服务（boks\_autoregisterd）中，允许未认证远程攻击者通过特制请求以高权限执行任意系统命令，可能导致完整系统沦陷。Fortra已发布安全补丁，建议所有使用BoKS进行特权访问管理的企业立即升级，并审查自动注册服务的访问日志中是否存在异常请求模式。该漏洞对拥有大量Unix/Linux服务器基础设施的企业构成严重威胁，尤其是金融、能源等关键行业。

资料来源：

https://www.fortra.com/security/advisories/cve-2026-9862

7. CISA将LiteSpeed cPanel插件权限提升漏洞（CVE-2026-54420，CVSS 8.5）纳入已知被利用目录

2026年6月16日，美国CISA将LiteSpeed Web Server的cPanel插件高危漏洞CVE-2026-54420（CVSS 8.5）列入已知被利用漏洞（KEV）目录，要求联邦民用行政分支（FCEB）机构在6月18日前完成修复。该漏洞允许已获得cPanel基础权限的攻击者通过构造恶意HTTP请求写入任意文件，最终以root权限执行任意脚本。该漏洞已在多起针对托管服务商与能源企业官网服务器的入侵事件中被利用，作为横向移动跳板。CISA建议立即应用补丁，并加强Web服务边界日志审计与入侵检测规则，重点监控Web目录下的异常文件写入行为。

资料来源：

https://www.cisa.gov/news-events/alerts/2026/06/16/cisa-adds-litespeed-cpanel-plugin-vulnerability-known-exploited-vulnerabilities-catalog

**安全事件**

8. 意大利亚得里亚港务局遭Anubis勒索软件袭击，仅攻陷IT系统便重创海运关键基础设施

2026年6月16日，据Industrial Cyber援引Resecurity情报报道，2025年12月意大利亚得里亚中部港务局遭Anubis勒索团伙定向攻击，攻击者以钓鱼邮件附件为初始入口，借助未修复漏洞与权限提升手段在内网横向渗透，全程仅针对港口IT业务系统实施加密与数据窃取，未触碰港口OT工控设施，却造成货物追踪、船期调度、海关申报等核心业务全面瘫痪，海量合同、员工涉密资料被窃取，黑客索要1000万美元比特币赎金，逾期不支付则在暗网外泄全部数据。此次事故迫使亚得里亚区域船舶改道绕行，港口供应链停滞并产生巨额经济损失，老旧备份机制进一步拉长系统恢复周期。该事件清晰证明港口等海陆交通关键基础设施存在严重IT、OT边界防护割裂短板，仅IT侧失守即可引发实体物流大面积停摆，同时暴露航运行业网络安全成熟度普遍偏低、员工钓鱼防范薄弱、云端办公账号缺乏强认证等共性隐患。

资料来源：

https://industrialcyber.co/transport/resecurity-details-anubis-ransomware-attack-on-adriatic-port-authority-exposing-maritime-infrastructure-risks/

9. 丹麦药企诺和诺德发生数据泄露数日之后，又一家医疗企业遭遇网络攻击

2026年6月16日，据 SecurityWeek报道，丹麦药企诺和诺德曝出数据泄露事件仅数日，美国医疗企业iRhythm便遭遇勒索网络攻击，该企业早在6月8日监测到内网入侵异常并启动调查，次日黑客发送勒索通告，宣称窃取患者健康隐私与企业商业机密并索要赎金，企业核实存在数据外泄，但表示本次攻击未影响产品运营、临床业务及患者安全，受损系统已完成修复。该接连发生的安全事件形成医疗行业攻击集群态势，不但印证医疗健康领域是网络不法分子重点瞄准的目标，也集中暴露医药、医疗相关企业普遍忽视OT生产运行环境防护，工控链路、生产调度体系极易被横向渗透入侵，企业IT与OT隔离防护存在明显短板，生产业务连续性、核心研发与运营数据面临持续性APT攻击风险，行业OT安全体系建设与纵深防御整改工作亟待加快落地补强。

资料来源：

https://www.securityweek.com/another-healthcare-firm-attacked-days-after-novo-nordisk-breach/

10. 俄罗斯基础软件服务商Astral遭遇定向网络攻击，政企财税政务服务大面积中断洞

2026年6月15日，据The Record报道，俄罗斯卡卢加Astral作为本土主流财税、电子公文、数字认证基础设施供应商，于6月9日遭受系列定向网络攻击，全平台服务中断长达一周，大量企业商户与政府机关业务停摆。攻击造成收银终端、财政报税系统、电子文档流转、数字证书身份认证、企业人事线上管理等核心功能瘫痪，商户无法合规售卖管控类商品、政企端无法按时提交监管报表，衍生经营与政务业务阻滞。企业联合俄信息安全主管部门开展溯源排查，为保障恢复后系统安全，所有业务需完成完整安全审计再分批上线，原定6月16日实现全部系统修复；官方核查暂未发现客户隐私、财税数据泄露痕迹，未锁定攻击组织与作案动机。该事件暴露出国家财税、政务类关键IT基础设施单点受袭即可引发连锁式行业停摆，上下游政企共享第三方服务商的集中化架构存在重大供应链安全短板。

资料来源：

https://therecord.media/cyberattack-on-russian-tech-firm-astral-disrupts-business-government-se

11. 澳大利亚第二大制糖企业遭遇勒索软件攻击，工厂生产线全面停工

2026年6月15日，据SecurityWeek报道，澳大利亚第二大原糖生产商MackaySugar在甘蔗榨季初期遭受勒索软件攻击，入侵同时波及企业IT办公网络与OT工控系统，导致昆士兰州两座核心制糖厂全线停产，当地近1300家甘蔗农场被迫暂停收割与原料运输，大量甘蔗无法进厂加工存在变质损耗风险；企业6月10日对外披露安全事件，紧急聘请安全专家联合监管部门开展排查修复，6月12日仅在其中一座工厂恢复小规模人工压榨，原料调度、物流管控等关键 OT 配套系统仍未修复，暂不接收新采收甘蔗，直至6月15日系统恢复工作仍在推进。本次攻击直接中断食品加工全产业链运转，凸显涉农工业、民生制造行业普遍忽视OT工控隔离防护。

资料来源：

https://www.securityweek.com/ransomware-attack-shuts-down-mills-of-australias-second-largest-sugar-producer/

12. 黑客组织ShinyHunters宣称入侵美国零售巨头杰西潘尼JCPenney，威胁曝光海量消费者数据实施勒索施压

2026年6月15日，据Cybernews报道，知名数据勒索黑客团伙ShinyHunters在暗网泄露站点公示，宣称已攻破美国大型线下零售企业JCPenney及其旗下多个子品牌系统，窃取海量消费者个人信息、消费记录、会员账户数据，以此向企业发起数据勒索，限期支付赎金否则全网公开全部被盗数据。该团伙长期针对零售、互联网、教育行业云CRM客户管理系统实施入侵，惯用语音钓鱼、仿SSO登录页面窃取员工账号凭证，突破企业云端业务系统窃取用户隐私数据。本次事件尚未得到JCPenney官方证实，企业暂未发布安全事件通报，但黑客公示泄露名单已引发消费者隐私恐慌与品牌声誉风险。该事件集中暴露零售行业客户云存储、会员管理系统边界防护薄弱，员工身份认证、多因素认证落地存在大量漏洞，零售企业面向海量用户的客户数据资产缺少分级防护与入侵监测机制。

资料来源：

https://cybernews.com/security/shinyhunters-jcpenney-retail-data-leak-claim/

13. 越南黑客组织OceanLotus从境外间谍活动转向国内进行定向供应链攻击

2026年6月12日，WeLiveSecurity报道，越南关联的APT组织OceanLotus（APT32）正在调整其作战模式，从传统的境外间谍活动转向针对越南国内实体的定向攻击。该组织近期利用供应链攻击手法，入侵了越南本土投资软件平台，部署了名为SpectralViper的后门程序，针对越南基础设施和交通建设公司以及股票投资者发动持续性网络间谍行动。此外，OceanLotus还针对中国"信创"IT生态系统发起供应链攻击，利用国产软硬件框架的独特架构植入恶意代码。该组织的战术演进表明，国家级APT正在将攻击面从跨境数据窃取扩展至国内经济稳定破坏和金融市场操纵，对关键基础设施构成多维威胁。

资料来源：

https://www.welivesecurity.com/en/oceanlotus-from-external-espionage-to-domestic-targeting/

14. 伊朗关联黑客组织Handala宣称入侵美国加州水务企业Cal Water

2026年6月12日，据SecurityWeek报道，与伊朗情报部门相关的国家级威胁组织Handala对外宣称攻陷美国大型水务公用事业企业加州水务Cal Water，以此作为美方针对伊朗基础设施行动的报复，并公开约5GB泄露数据作为攻击佐证。攻击者以对外暴露的RTKBase地理GPS运维平台为入口完成入侵，横向渗透进入客户计费数据库，窃取覆盖加州7个供水片区的用户隐私账单信息、运维账号凭证，本次入侵仅波及企业IT业务系统，未突破供水SCADA、水处理等OT生产控制网络，城市供水业务未出...