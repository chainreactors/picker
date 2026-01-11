---
title: 每周网络安全简讯 ( 2026年 第1-2周 )
url: https://mp.weixin.qq.com/s/Pl99RPYEFYL_tl9cz91uwQ
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:22.717977
---

# 每周网络安全简讯 ( 2026年 第1-2周 )

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KGUe0T1OnhtXXNEbNt9muskB1yliaFvGwKVib09qljXZ4pMCicAf5T10nicDOC3l43Ex6G2XHm7a03OyIBFTsInJXA/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第1-2周 )

国信中心

极客安全

![]()

在小说阅读器中沉浸阅读

2026年1月1日至2026年1月9日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计22条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织APT36对印度目标用户实施网络攻击

近日，安全研究人员发现APT组织APT36采用鱼叉式网络钓鱼攻击方式对印度政府、大学等目标用户实施入侵。一旦用户点击邮件内嵌入的恶意PDF文件，将会在受控设备上自动释放ReadOnly和WriteOnly恶意程序载荷，根据用户设备上已安装的杀毒软件调整自身行为，并对其实施敏感数据窃取、截屏、剪贴板活动监控、远程桌面访问等恶意操作。此外，安全人员声称，该APT组织与Cosmic Leopard组织有重叠之处，而后者曾对印度政府、国防和技术等领域机构进行了长达数年的间谍活动。

**链接：https://therecord.media/pakistan-linked-hacking-group-targets-indian-orgs**

02

APT组织UAC-0184利用Viber对乌克兰目标实施网络攻击

近日，安全研究人员监测发现APT组织UAC-0184以“军人档案”“阵亡补偿”等敏感话题为诱饵，利用乌克兰本土广泛使用的即时通讯平台Viber作为初始攻击载体，投放伪装成官方文件的恶意ZIP压缩包。一旦用户点击ZIP压缩包内的恶意LNK文件时，将会启动多阶段感染流程，通过恶意PowerShell脚本下载附加载荷，调用合法程序CFlux.exe侧载恶意DLL，进而采用非标准控制流跳转、模块篡改、内存注入及图片隐写等高级规避技术，部署HijackLoader和Remcos RAT恶意载荷，实现对用户设备的远程控制、数据窃取与持续驻留。此次攻击事件再次凸显近期APT攻击对即时通讯应用平台的滥用趋势，以及对目标用户群体敏感话题的实时关注，上述攻击手段联合利用，将构成更大的潜在安全威胁。

**链接：https://securityaffairs.com/186571/apt/russia-linked-apt-uac-0184-uses-viber-to-spy-on-ukrainian-military-in-2025.html**

03

APT组织BlueDelta对土耳其目标用户实施网络攻击

近日，Insikt Group安全团队监测发现，APT组织BlueDelta在2025年2月份至9月份采用土耳其语或区域化主题，针对土耳其能源与核能研究、欧洲智库及北马其顿、乌兹别克斯坦等相关机构人员实施网络钓鱼攻击，诱使用户访问伪造的Microsoft OWA、Google、Sophos VPN等常见平台登录或密码重置页面以窃取登录凭证，同时嵌入真实PDF诱饵文件提升自身可信度，规避安全设备的自动化检测。同时，在上述攻击流程中，该APT组织在钓鱼页面中嵌入了多种定制化JavaScript实现凭证捕获、用户活动追踪、自动化重定向等多种功能，攻击特点逐步趋向于“流程自动化”，攻击效率、成功率、隐蔽性均得到进一步提升。

**链接：https://www.recordedfuture.com/research/gru-linked-bluedelta-evolves-credential-harvesting**

02

网络动态

01

ISACA获授权主导CMMC认证体系，规范国防网络安全标准

国际信息系统审计协会（ISACA）获授权担任美国CMMC（Cybersecurity Maturity Model Certification）项目的评估员与讲师认证机构（CAICO），将统一负责CMMC生态从业人员的培训、考试与职业资质管理，覆盖CMMC Certified Professional（CCP）、CMMC Certified Assessor（CCA）、CMMC Certified Instructor（CCI）以及Lead CCA等关键证书体系，旨在提升评估与教学的标准化与一致性，支撑国防工业基础（DIB）范围内大规模合规需求落地。ISACA CEO Erik Prusch表示，此次授权强化了ISACA在全球安全治理与职业认证领域的角色，并指出CMMC是面向DIB数十万组织的统一网络安全标准，将对国际安全、供应链与全球经济产生重要影响，同时这一角色也为从业者提供新的职业路径与认证通道。

**链接****：https://industrialcyber.co/training-development/isaca-takes-lead-in-cmmc-assessor-and-instructor-certification-shaping-defense-cybersecurity-standards/**

02

英国发布《政府网络安全行动计划》

1月6日，英国政府官方网站发文称，英国科学、创新与技术部（Department for Science, Innovation and Technology，DSIT）正式发布《政府网络安全行动计划》（Government Cyber Action Plan）。官方强调，该文件是英国“国家更新（national renewal）”战略的重要组成部分，承诺投入超过2.1亿英镑构建政府网络安全单位（Government Cyber Unit），推动公共部门网络防御能力的“跃迁式提升”，且通过制度化手段，为整个政府体系构建一个可信、稳定、具备快速恢复能力的数字基础环境，确保关键公共服务即便在遭遇攻击时，也能持续运行或迅速恢复。

**链接：**https://www.gov.uk/government/publications/government-cyber-action-plan/government-cyber-action-plan

03

美国防部拟设立企业指挥与控制项目办公室，整合AI与联合全域作战能力

近日，美国防部筹划设立新的企业级指挥与控制（Enterprise Command and Control,EC2）项目办公室，旨在系统整合扩展现有数字与人工智能办公室（CDAO）旗下的Maven智能系统（MSS）及边缘数据网格（Edge Data Mesh）能力，通过用户定制化AI工具强化实时敌情感知、目标定位与决策支撑，打造统一的“企业级C2套件”，全面支撑“联合全域指挥与控制”（CJADC2）及AI赋能作战体系建设。该举措标志着美军在指挥控制架构、数据融合与智能决策能力方面进入新阶段。

**链接****：https://news.defcros.com/dod-outlines-strategy-for-new-command-and-control-program-office-and-c2-suite-development/**

04

NIST启动SP800-56密码学标准更新与修订，强化密码安全合规性

1月6日，据NIST官方网站报道，近日，美国国家标准与技术研究院（NIST）在审议公众意见后，正式启动对其核心密钥标准800-56系列的结构性调整，包括：一是更新《基于离散对数密码学的成对密钥建立方案建议（2018）》（SP 800-56Ar3），批准仅使用x坐标的ECC密钥协商实现方式；二是确认维持《基于整数分解密码学的成对密钥建立建议（2019）》（SP 800-56Br2），仅更新原有参考文献部分；三是实质性修订《密钥建立方案中的密钥派生方法建议（2020）》（SP 800-56Cr2），允许混合密钥结构中将通过“密钥封装机制”（KEM）获取的共享密钥引入到共享密钥Z中，提升结构灵活性。同时，NIST还在密钥治理层面同步明确了“确认、更新、修订、转换、分阶段撤回”五种处理路径，为密码算法生命周期管理提供更清晰的合规机制与迁移路径。

**链接****：**https://csrc.nist.gov/news/2026/nist-to-revise-key-establishment-recommendations

05

美国众议院启动进攻性网络能力听证会，强化“以攻促防”国家网络安全战略

1月7日，据美国土安全委员会官方网站报道，近日，美国众议院网络安全与基础设施保护小组委员会举行专题听证会，围绕“以攻促防：审视美国网络能力以威慑和干扰针对美国本土的恶意外国活动”主题，系统评估美国进攻性网络行动在国家安全体系中的战略定位、法律基础与政策框架。此次听证会重点关注三大方向：一是明确联邦机构与私营部门在进攻性网络行动中的分工与责任边界；二是强化国会与私营部门合作力度，提升国家层面的网络行动统一性；三是确保美国利用人工智能、量子计算和超大规模云基础设施等新兴技术，提升自身网络安全防护能力。此前，针对相关讨论方向的政策配套措施已逐步推进，如：2025年11月，美国众议院通过两项重要法案，其中PILLAR法案（HR 5078）重新授权国土安全部对州与地方网络安全的拨款计划；二是《加强网络韧性以应对国家支持威胁法案》（HR 2659），设立跨部门工作组，重点应对敌对国家网络威胁。

**链接****：**https://homeland.house.gov/2026/01/07/media-advisory-subcommittee-chairman-ogles-announces-hearing-on-strengthening-americas-offensive-cyber-capabilities/

06

美国防部拟利用人工智能和自动化技术实施零信任评估工作

随着美国防部（DoD）零信任“目标级别（Target）”合规期限临近，零信任项目管理办公室发布信息征询书（RFI），面向产业界征集方案，探索如何利用自动化技术、人工智能与机器学习（ML）在全部门范围内加速并规模化零信任评估工作，重点聚焦用于独立验证的“紫队评估（Purple Teaming）”流程。DoD指出，目前“紫队”在初始合规验证与持续评估方面能力受限，极为耗时，且易占用作战与防护力量资源，因此DoD希望“紫队”能够在未来依赖各项新兴技术，支撑更高频、自动化的评估工作，涉及：模拟真实攻击场景、辅助红蓝对抗交互测试、自动化收集与分析证据、识别核心零信任要求实施缺陷与效率瓶颈等，可根据收集的各类参数快速生成完整评估报告与整改建议。总体看，DoD此次征求意见，表明其零信任评估工作正从“人工密集型合规检查”向“AI驱动持续验证与自动化评估”升级，以在时间要求更为敏感的情况下提升零信任评估的覆盖面、效率与持续能力。

**链接****：https://defensescoop.com/2026/01/06/dod-zero-trust-assessments-ai-automation/**

07

可绕过PatchGuard等安全机制的新型Windows内核进程隐藏技术被披露

Outflank安全团队披露了一种全新的Windows内核级隐藏技术，证明攻击者即使在PatchGuard、HVCI等现代内核防护机制启用的情况下，仍可通过操纵内核数据结构而非代码本身，使恶意进程在整个运行周期内对系统监控工具保持不可见状态。该技术通过篡改Windows进程管理“进程双向链表”（ActiveProcessLinks）的EPROCESS关键数据结构，将目标进程从系统进程链中“摘除”，从而对Task Manager、Process Hacker 等常规检测工具完全隐藏。同时，在恶意程序的进程终止时通过注册PsSetCreateProcessNotifyRoutineEx回调函数的方式，在内核执行清理与完整性校验前利用系统驱动程序对篡改的数据结构进行动态修复，使PspProcessDelete的校验逻辑检测不到任何异常，进程最终完全退出，全程不触发系统崩溃或蓝屏。上述方式无需攻击者禁用PatchGuard或HVCI，而是完全在可写内核数据结构上操作，即可成功规避当前主流内核完整性防护模型。该技术具备极高隐蔽性与稳定性，为攻击者提供了一种持久、无痕、抗检测的内核级隐藏能力。

**链接****：https://cybersecuritynews.com/hackers-can-leverage-kernel-patch-protection/**

03

漏洞资讯

01

GNU Wget2存在安全漏洞

近日，安全研究人员发现被广泛应用的网络文件下载命令行工具GNU Wget2存在安全漏洞（CVE-2025-69194），是由Wget2处理Metalink文件时对文件路径验证机制存在缺陷所导致，允许攻击者构造包含路径遍历序列的恶意Metalink文件，并诱骗用户使用Wget2执行该文件的方式，将其写入文件系统中的非预期位置，致使用户数据丢失，甚至对用户设备实施远控。目前，尚无符合企业部署标准的完整缓解措施，用户应避免处理来自不受信任来源Metalink文件的方式降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/gnu-wget2-vulnerability/**

02

QNAP Qfiling存在安全漏洞

近日，安全研究人员发现QNAP NAS应用程序Qfiling存在安全漏洞（CVE-2025-59384），允许未经身份验证的攻击者远程读取目标NAS设备配置文件、系统数据等敏感信息。漏洞影响version < Qfiling 3.13.x版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://rocket-boys.co.jp/security-measures-lab/qnap-qfiling-path-traversal-vulnerability-fixed-cve-2025-59384/**

03

jsPDF存在路径遍历漏洞

近日，安全研究人员发现用于在客户端生成PDF文件的开源JavaScript库jsPDF存在路径遍历漏洞（CVE-2025-68428），如果开发者使用MultipartFile.move()函数时没有指定第二个选项参数，或者没有显式对文件名进行清理，攻击者就可以通过提供包含遍历序列文件名的方式，将文件写入预期上传目录之外的目标路径，进而实现任意文件写入。漏洞影响version < 10.1.1等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://thehackernews.com/2026/01/critical-adonisjs-bodyparser-flaw-cvss.html**

04

苹果MacOS操作系统存在安全漏洞

近日，安全研究人员发现苹果MacOS操作系统存在安全漏洞（CVE-2025-43530），是由MacOS文件验证机制与“检查时间-使用时间”(TOCTOU)缺陷所导致，允许攻击者在目标设备进程“执行前”到“通过初始检查后”的时间段内对其进行修改，从而绕过安全验证，并利用该时间差在受信任系统服务上下文中执行敏感操作。该安全漏洞无需管理员权限即可在本地利用，目前用户可通过将MacOS升级至26.2或更高版本的方式修复上述安全漏洞。

**链接：：https://www.esecurityplanet.com/threats/macos-flaw-enables-silent-bypass-of-apple-privacy-controls/**

05

谷歌Chrome浏览器存在安全漏洞

近日，安全研究人员发现谷歌Chrome浏览器WebView标签组件存在安全漏洞（CVE-2026-0628），是由该标签组件策略执行流程存在缺陷所导致，允许攻击者绕过安全控制，未授权访问用户敏感信息，甚至在采用WebView的应用程序中执行任意恶意代码。漏洞影响Chrome < 143.0.7499.192等版本，目前用户可通过Chrome浏览器版本升级修复上述安全漏洞。

**链接：https://cybersecuritynews.com/chrome-webview-vulnerability/**

06

杜比编解码器存在远程代码执行漏洞

近日，安全研究人员发现安卓设备杜比编解码器存在远程代码执行漏洞（CVE-2025-54957），位于杜比通用解码器核心(UDC)中，是由该组件存在越界写入缺陷所导致，允许攻击者将恶意代码嵌入媒体文件并诱使用户使用相关设备播放的方式，实现远程任意代码执行。目前，用户可通过安卓补丁更新的方式修复上述安全漏洞。

**链接：https://cybersecuritynews.com/dolby-codec-android-vulnerability/**

07

Apache Kyuubi存在目录访问控制绕过漏洞

近日，安全研究人员发现Apache基金会旗下的分布式SQL网关与多租户计算服务平台Apache Kyuubi存在目录访问控制绕过漏洞（CVE-2025-66518），是由服务器端在处理本地路径时缺乏必要的路径规范化校验所导致，允许攻击者绕过kyuubi.session.local.dir.allow.list配置限制，未授权访问本地文件资源。漏洞影响1.6.0 <= Apache Kyuubi <= 1.10.2等版本，目前用户可通过版本升级等方式修复上述安全漏洞。

**链接：https://securityonline.info/cve-2025-66518-high-severity-flaw-in-apache-kyuubi-exposes-local-server-files/**

08

Linux电池优化程序TLP存在身份验证绕过漏洞

近日，安全研究人员发现Linux笔记本电脑电池优化程序TLP存在身份验证绕过漏洞（CVE-2025-67859），是由Polkit授权机制存在竞争条件缺陷所导致，允许非特权本地用户绕过身份验证机制，控制目标设备电源管理配置。目前，用户可通过将Linux TLP版本升级至1.9.1会更高版本的方式修复上述安全漏洞。

**链接：https://cybersecuritynews.com/linux-battery-utili...