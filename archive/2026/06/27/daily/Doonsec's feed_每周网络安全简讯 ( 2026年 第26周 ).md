---
title: 每周网络安全简讯 ( 2026年 第26周 )
url: https://mp.weixin.qq.com/s/UrmSaahEd4X--brd5kITPQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:11:09.148384
---

# 每周网络安全简讯 ( 2026年 第26周 )

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qyzTicOO6WeXIGSXpgUBv626KJ04WH0xeUkaB3z6IY9GplPaxorTxz579YkGaYA7HGmvvK8h26yEOw4FGpNBTCKOSJFWLIPWwo6YY4Rx2ibick/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第26周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年6月19日至2026年6月26日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计21条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织APT-C-36利用Remcos恶意程序对哥伦比亚目标用户实施网络攻击

近日，安全研究人员监测发现APT组织APT-C-36正在针对哥伦比亚境内的政府部门、金融及保险等行业机构实施新一轮定向攻击。此次攻击活动以携带SVG格式诱饵文件的钓鱼邮件为初始入侵手段，邮件内容伪装为银行业务申请，诱导目标用户点击后，内嵌的JavaScript脚本将会自动解密释放PowerShell下载器，在本地完成载荷投递而无需联网下载。随后，该APT组织利用Hijackloader加载器通过“白加黑”方式将恶意模块注入合法进程，最终在内存中运行Remcos恶意程序。经分析发现，Remcos具备命令执行、屏幕截取、键盘记录、音频录制及摄像头控制等功能，并可与C2服务器持续保持加密通信。此外，研究人员注意到该APT组织在本次攻击中采用的部分恶意程序引入了人工智能生成的代码，此举显著降低了开发门槛。安全人员建议称，相关组织应加强对SVG附件的邮件过滤与终端行为检测，在内存执行环节部署防护措施，以降低遭受攻击的风险。

**链接：[【查看原文】](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247508673&idx=1&sn=daeb4f0be09db6a3012e51ac7e7be079&scene=21#wechat_redirect)**

02

APT组织Gamaredon针对乌克兰政府和军事机构实施网络攻击

近日，安全研究人员监测发现APT组织Gamaredon在2025年持续针对乌克兰政府和军事机构发起高强度网络攻击活动，在下半年共实施35起大规模鱼叉式钓鱼活动，以恶意附件投递HTA下载器获取初始访问权限，滥用WinRAR漏洞（CVE-2025-8088）将下载器植入Startup文件夹实现持久化驻留，进而通过PteroPaste和PteroSetup恶意载荷实现横向移动，并部署6个新PowerShell下载器最终实现对受控设备的全面远控。此外，该APT组织还会在C2通联阶段利用Telegram、Dropbox等平台服务进行C2地址解析和载荷分发，同时试图将通信流量隐藏在Cloudflare、devtunnels等第三方服务，以此规避部分安全设备的监测。安全人员建议称，相关组织应加强对钓鱼邮件和PowerShell进程的安全过滤与监测力度，以降低遭受攻击的风险。

**链接：https://www.welivesecurity.com/en/eset-research/gamaredon-2025-leveraging-tunnels-workers-dead-drops-new-alliances/**

02

网络动态

01

五眼联盟警告人工智能正加速重塑网络安全风险

澳大利亚信号局、加拿大网络安全中心、英国国家网络安全中心、美国国家安全局，以及网络安全与基础设施安全局等五眼联盟主要网络安全机构联合发布行动呼吁，指出人工智能正在迅速改变网络安全风险格局。相关机构认为，AI一方面可提升漏洞发现、异常监测和事件响应能力，另一方面也在降低攻击门槛、提升攻击速度和复杂度，并进一步压缩漏洞披露到被利用之间的时间窗口。声明强调，网络安全不应仅被视为技术问题，而应纳入核心业务风险治理，董事会和管理层需确保网络韧性在真实事件压力下有效运行。五眼联盟建议各类组织优先落实安全设计、默认安全和纵深防御原则，重点采取减少攻击面、加快补丁修复、主动处置遗留系统、强化身份与访问管理、提前开展事件响应演练共五项关键措施，以应对AI驱动威胁带来的持续冲击。

**链接****：https://www.cyberdaily.au/security/13787-ai-is-rapidly-transforming-cyber-security-risk-five-eyes-agencies-warn**

02

澳大利亚参加美主导“勇敢盾牌26”多域联合演习

澳大利亚国防军将参加由美国主导的“勇敢盾牌26”（Exercise Valiant Shield 26）联合演习，与美国、日本、加拿大和新西兰等国部队在日本、夏威夷、关岛和澳大利亚等地开展协同训练。此次演习覆盖陆、海、空、太空和网络等多个作战域，重点检验盟友伙伴之间的防御互操作能力，以及在复杂威胁环境下共同探测、应对和压制威胁的能力。澳方将派出澳大利亚皇家空军P-8A“波塞冬”海上巡逻机，并投入指挥人员、空中战场管理及综合防空反导力量。澳军方表示，演习有助于提升澳大利亚与盟友伙伴的无缝协同能力，增强威慑军事侵略和应对潜在对手的能力。近年来，“勇敢盾牌”演习持续扩展，网络、太空、指挥控制、信息共享和电子战等能力在演习中的地位进一步上升。

**链接：**https://www.cyberdaily.au/security/13786-australia-joins-us-led-exercise-valiant-shield-26-to-test-cyber-and-other-domain-capabilities

03

USCG CTIME报告警示：IT-OT融合与遗留系统扩张重塑海事网络攻击面

美国海岸警卫队（USCG）发布第五份年度《海洋环境网络趋势与洞察》（CTIME）报告，指出海上运输系统正面临人工智能应用、IT与OT融合、遗留系统暴露等因素叠加带来的网络安全风险。报告显示，2025年海事网络事件报告数量同比增长17%，网络钓鱼仍是主要初始入侵方式，43%的相关事件涉及钓鱼侦察或入侵路径；内部漏洞占56%，密码破解率达47%，账户泄露、弱口令、MFA配置不当、外部暴露服务、过时协议和网络分段不足等基础性问题依然突出。报告还指出，AI安全平台在正确配置和充分调优后可有效提升检测能力，但配置不当则难以发挥作用。海岸警卫队建议海事运营方强化资产管理、网络分段、密码与身份治理、远程访问管控、日志监测和事件响应演练，并将合规建设与韧性治理相结合，以降低运营中断风险。

**链接****：https://industrialcyber.co/reports/uscg-ctime-report-flags-maritime-cyber-risk-as-ai-adoption-it-ot-convergence-legacy-systems-reshape-attack-surfaces/**

04

DIA拟引入AI采购平台，简化联邦采购全流程

美国国防情报局（DIA）发布信息征询书（RFI），拟推进下一代人工智能驱动的采购平台原型项目。该平台旨在通过集成《联邦采购条例》（FAR）、《国防采购条例》（DFAR）等，构建AI赋能的采购环境，提升联邦采购生命周期的有效性、透明度与执行速度，减少手动任务、工作流及需求编写带来的低效，并提高重复性任务的准确性。平台能力将支持采购专业人员、项目办公室、法律及政策利益相关者，涵盖市场调研、招标起草、提案评估、合规检查及授予后分析等全流程。该举措与五角大楼及情报界近期广泛寻求AI工具以消除繁琐工作、简化后台职能的趋势一致，DIA局长詹姆斯·亚当斯此前亦强调需以人工智能加速情报生成与决策支持。

**链接****：**https://defensescoop.com/2026/06/22/dia-ai-powered-platform-streamline-procurement-system/

05

美国白宫发布两项行政命令，加速量子创新并推动联邦系统向后量子密码学转型

美国白宫发布两项行政命令，旨在加速国内量子创新并推动联邦系统向后量子密码学（PQC）转型。命令要求各机构30天内指定PQC迁移负责人，2030年底前完成密钥系统迁移，2031年底前完成数字签名过渡，同时将在180天内更新国家量子战略，并启动大规模量子计算机研发计划。相关机构指出，此举意在应对“先收获、后解密”攻击等未来网络威胁，巩固美国在量子信息科学领域的全球领导地位。该命令反映出网络安全与量子战略已深度融合，需持续关注后续进展。

**链接****：**https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/

06

美国海军陆战队将于7月发布ODIN数字报告工具，整合Maven智能系统提升作战态势报告效率

美国海军陆战队宣布将于7月7日正式发布作战数据集成枢纽（ODIN）应用，作为作战态势报告（SITREPs）的官方报告工具。ODIN将部署于由Palantir开发的Maven智能系统（MSS），通过与权威数据库集成实现数据录入自动化，消除信息孤岛并支持单位间数据共享。相关官员指出，该系统将分散数据转化为可操作的洞察参数，使指挥官能够动态管理风险，在分布式作战环境中高效决策。此举反映出美军正加速推进数字化作战指挥能力建设，需持续关注后续部署进展。

**链接****：**https://defensescoop.com/2026/06/23/marine-corps-mandates-use-of-new-digital-app-for-sitreps/

07

Casepoint独家获得美国战争部9880万美元BPA合同，支持机密法律运营AI现代化

Casepoint宣布获得美国战争部（DOW）独家综合采购协议（BPA），合同金额9880万美元，为DOW总法律顾问办公室、国防信息系统局及国防法律服务局28个办公室提供AI驱动的电子发现、调查及解密审查等SaaS平台服务。该平台具备IL5、IL6和FedRAMP High授权，可在机密及非机密网络环境中运行，旨在通过自动化工作流替代传统手工流程，提升法律运营效率与可审计性。据称，相关诉讼团队借助该平台已将文档审阅时间缩短50%至75%。此次合作反映出DOW法律机构正加速推进AI驱动的数字化转型，以应对日益增长的数据量与合规压力。

**链接****：**https://www.prnewswire.com/news-releases/casepoint-wins-exclusive-98-8-million-department-of-war-bpa-to-support-classified-legal-operations-as-defense-agencies-face-rising-pressure-to-modernize-and-leverage-ai-302808798.html

08

美国联邦航空管理局授予空域情报公司合同，部署新一代空管预测系统以提升国家空域效率

美国交通部长肖恩·P·达菲与联邦航空管理局局长布莱恩·贝德福德宣布，美国联邦航空管理局（FAA）已授予空域情报公司（ASI）合同，部署流量管理数据与服务（FMDS）及空域航线轨迹战略管理（SMART）两项互补技术。FMDS将作为空中交通管制系统指挥中心的技术核心，整合多源数据以平衡航空需求与容量；SMART则通过预测性建模在航班起飞前协调航线与时刻表，主动识别潜在延误与可用空域。据称，该系统计划于今年秋季开始初步运营。相关负责人指出，此举将从根本上重塑空域管理方式，减少航班延误并降低管制员工作负荷。

**链接****：**https://www.faa.gov/newsroom/modern-skies-trumps-transportation-secretary-sean-p-duffy-selects-air-space-intelligence

09

美国联邦通信委员会通过新规，强化国家应急警报系统与海底电缆网络安全

6月25日，据FCC官方网站报道，美国联邦通信委员会（FCC）批准两项新的网络安全规则。第一项规则针对国家紧急警报系统（EAS）和无线紧急警报（WEA），要求相关组织用户采用强密码、及时安装安全补丁及防火墙等基础网络卫生措施，并建立新的认证ID系统，防止未经授权的警报提交与传播。第二项规则是数十年来首次对海底电缆法规进行全面更新，允许符合高安全标准且无事故记录的运营商免除“Team Telecom”国家安全许可审查，同时新增海底线路终端设备许可要求，以加强供应链关键环节的安全监管。

**链接****：**https://docs.fcc.gov/public/attachments/DOC-422584A2.pdf、https://cyberscoop.com/fcc-undersea-cable-regulations-national-security/

03

漏洞资讯

01

FFmpeg存在堆缓冲区溢出漏洞

近日，安全研究人员发现FFmpeg广泛使用的MagicYUV解码器中存在堆缓冲区溢出漏洞（CVE-2026-8461，代号PixelSmash），是由帧分配器与解码器计算色度平面高度不一致所导致，允许攻击者通过向目标设备发送特制AVI、MKV或MOV格式恶意视频文件的方式，在Jellyfin、Kodi、Nextcloud、PhotoPrism、OBS Studio等依赖libavcodec的应用中触发拒绝服务，甚至在ASLR被禁用或配合其他安全漏洞实现远程代码执行。漏洞影响FFmpeg 8.1.2之前版本，目前用户可通过升级至8.1.2版本的方式修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/security/ffmpeg-fixes-pixelsmash-flaw-in-widely-used-video-decoder/**

02

Dify AI平台存在4个安全漏洞

近日，安全研究人员发现开源AI平台Dify存在4个安全漏洞。其中，第一个安全漏洞是跨租户数据泄露漏洞（CVE-2026-41947），是由追踪系统组件存在缺陷所导致，允许攻击者通过配置追踪端点的方式，在目标应用上创建持久化数据外泄通道，窃取消息与模型响应；第二个安全漏洞是路径遍历漏洞（CVE-2026-41948），是由插件守护进程未对请求参数进行过滤所导致，允许未经身份验证的攻击者通过GET或POST请求访问任意内部API端点；另外两个安全漏洞（CVE-2026-41949、CVE-2026-41950）均为文件访问控制缺陷，分别允许任意用户预览系统中全部文档以及通过跨租户文件UUID附件获取其他用户文件内容。目前，用户可通过将版本升级至v1.14.2的方式修复上述安全漏洞。

**链接：https://securityaffairs.com/194081/hacking/difytap-four-bugs-put-over-1-million-ai-apps-at-risk.html**

03

Cisco Unified Communications Manager存在服务器端请求伪造漏洞

近日，安全研究人员发现Cisco Unified Communications Manager存在服务器端请求伪造漏洞（CVE-2026-20230），是由Webdialer组件对HTTP请求输入验证不当所导致，允许未经身份认证的远程攻击者通过发送精心构造的file:// URI请求，在目标设备上写入任意文件，进而提升权限至root。目前，用户可通过安装思科6月3日发布的安全补丁修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/security/cisco-unified-cm-sme-flaw-cve-2026-20230-now-exploited-in-attacks/**

04

libssh2存在整数溢出漏洞

近日，安全研究人员发现libssh2存在整数溢出漏洞（CVE-2026-55200），是由ssh2\_transport\_read()函数对SSH数据包packet\_length字段缺少上界检查所导致，允许攻击者通过向目标设备发送恶意构造的超大packet\_length值，触发整数溢出并在目标系统上实现堆越界写入，进而实现无需认证的远程代码执行、触发拒绝服务或导致系统全面崩溃。由于该漏洞基于网络攻击向量且无需用户交互，影响范围涵盖企业环境、云服务及嵌入式系统中广泛使用的SSH客户端、自动化框架和文件传输工具。目前，用户可通过安装补丁等方式修复上述安全漏洞。

**链接：https://cybersecuritynews.com/libssh2-vulnerability/**

05

Cisco Catalyst SD-WAN存在本地权限提升漏洞

近日，安全研究人员发现Cisco Catalyst SD-WAN存在本地权限提升安全漏洞（CVE-2026-20245），是由相关组件对用户输入验证不足所导致，允许已初步认证的本地攻击者通过上传恶意CSV文件的方式，在目标系统上执行任意命令并提升权限至root。目前，用户可通过安装思科发布的安全补丁修复上述安全漏洞。

**链接：https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html**

06

Squid网络代理存在内存泄露漏洞

近日，安全研究人员发现Squid网络代理存在内存泄露漏洞（CVE-2026-47729），是由Squid FTP目录列表解析组件中的strchr函数处理逻辑存在缺陷所导致，当攻击者控制的FTP服务器发送无文件名的列表行时，解析循环无法终止，进而越界读取缓冲区中残留的相邻内存数据，进而允许攻击者从同一代理实例的其他用户流量中提取明文HTTP请求。目前，用户可通过升级至Squid 7.6及以上版本，或在配置中...