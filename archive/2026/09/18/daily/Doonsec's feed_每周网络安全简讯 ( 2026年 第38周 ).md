---
title: 每周网络安全简讯 ( 2026年 第38周 )
url: https://mp.weixin.qq.com/s/qMPxqeqQCTXyiTfNbBNsyw
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:51:53.390122
---

# 每周网络安全简讯 ( 2026年 第38周 )

# 每周网络安全简讯 ( 2026年 第38周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年9月12日至2026年9月18日，国家信息技术安全研究中心在线监测技术研究实验室对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计24条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

疑似APT组织Sandworm利用思科FMC漏洞部署CyclopsBlink恶意程序

近日，安全研究人员披露，疑似APT组织Sandworm正串联利用Cisco Secure Firewall Management Center（FMC）中的CVE-2026-20079和CVE-2026-20316漏洞，部署新版CyclopsBlink恶意软件。此次攻击活动中，Sandworm首先在受影响FMC设备上植入基于Netcat的反向Shell和代理工具，随后投递CyclopsBlink。新版样本已由原有32位PowerPC架构转向64位x86-64 Linux平台，并采用通用SysV持久化机制，可执行主动网络扫描、数据包捕获，并收集密码哈希、进程命令行、CPU及配置等信息，扩大对Linux网络设备的适配范围。目前，Cisco已发布紧急修复程序，并建议相关用户尽快更新，以降低遭受攻击的风险。

**链接：https://www.darkreading.com/cyberattacks-data-breaches/sandworm-chains-cisco-vulnerabilities-cyclops-blink**

02

APT组织Hacking Cat利用Gorilla RAT和Monkey向俄罗斯目标用户实施网络攻击

近日，安全研究人员披露称，与乌克兰相关的APT组织Hacking Cat自2024年起持续针对俄罗斯机构开展网络攻击，并逐步由网站篡改、数据泄露转向更复杂的破坏性行动。该组织相关攻击中出现此前未记录的Gorilla RAT和Monkey勒索软件变种，其中Gorilla RAT可在利用Microsoft Exchange漏洞取得初始访问后建立网络隧道，支持攻击者远程进入受害网络；Monkey勒索软件则用于加密数据，且短期内出现多语言版本，显示其开发迭代较快。此外，安全研究人员认为，多支亲乌APT组织可能共享定制工具和感染链，导致攻击归属更加困难。

**链接：https://therecord.media/ukraine-malware-russia-ransomware**

03

APT组织APT36针对印度、阿富汗等国目标实施网络攻击

近日，安全研究人员披露与巴基斯坦有关的APT组织APT36针对印度和阿富汗等国目标开展“RapidRust”攻击行动，利用可移动存储设备向物理隔离的政府网络传播恶意软件。此次攻击活动中，该APT组织将RUSTYSHADE后门、PSNATCH和BASHNATCH恶意程序复制到U盘等设备，诱导用户点击执行，并通过计划任务维持驻留。其中，RUSTYSHADE会利用私有GitHub仓库传递指令和回传数据，支持命令执行、截屏及摄像头拍摄；PSNATCH和BASHNATCH则会分别窃取Windows、Linux系统文件，并开展用户、进程、网络共享等信息侦察，尝试访问远程管理共享以实现横向渗透。安全研究人员建议相关组织机构加强可移动存储介质准入与查杀，重点排查异常快捷方式、计划任务及GitHub通信，防范恶意软件跨越物理隔离边界传播和窃密。

**链接：https://cybersecuritynews.com/apt36-uses-usb/#google\_vignette**

04

APT组织NightEagle利用GhostContainer后门与微软隧道服务对俄罗斯目标组织实施网络攻击

近日，安全研究人员披露，APT组织NightEagle利用被盗VPN凭据入侵俄罗斯目标组织Exchange服务器，部署GhostContainer后门，通过请求头接收攻击指令，随后滥用Microsoft Dev Tunnels及rdp2tcp工具，建立隐蔽远程访问通道，避免新增明显的外部监听端口，同时借助计划任务、端口转发等方式实现横向移动，并在获取高权限账户后尝试通过DCSync窃取域凭据。安全研究人员建议相关组织机构强化VPN多因素认证，及时修补网络安全漏洞，重点监测异常隧道连接、Exchange内存活动及目录复制请求，防范攻击者扩大控制范围，降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/nightagle-hackers/**

02

网络动态

01

美国防后勤局推进“数字员工”应用，近200个AI机器人已投入自主运行

美国国防后勤局（DLA）正加快推进自主AI代理在军事后勤领域的应用，目前约有185至190个机器人投入运行，其中90%至95%为无人值守模式，部分可全天候执行任务。DLA计划进一步将传统机器人流程自动化升级为跨部门自主协同的“数字员工”，并通过AI卓越中心、零信任网络安全框架及“基于角色的访问权限”机制，限制AI代理仅访问与其岗位职责相匹配的数据域。DLA认为，随着AI代理深度参与后勤与供应链业务，数据质量、权限控制、治理规则、安全性及人机协同管理将成为重点问题，相关能力建设正从试验阶段逐步转向战略化实施。

**链接****：https://www.nextgov.com/defense/2026/09/digital-employees-are-coming-defense-logistics-agency/415950/**

02

美国国家安全局（NSA）正推进近年来规模较大的组织重组

美国国家安全局（NSA）正推进近年来规模较大的组织重组，计划以中国相关事务、网络安全、人工智能、作战支援和全球情报五大“任务中心”取代现有部分部门架构，以缩短情报获取、分析与向军事用户分发的周期。现任NSA及美军网络司令部负责人约书亚·拉德已启动为期30天的调整工作，各任务中心分别设置负责人，并计划于2027年1月前形成全面作战能力。重组还可能涉及定制访问行动办公室（TAO）等网络行动力量的重新归属，但网络安全协作中心等机构安排尚未明确。

**链接：https://therecord.media/nsa-reorganization-five-mission-centers**

03

美国参议院成立两党科学与创新核心小组，拟关注人工智能监管与安全风险

美国参议员约翰·希肯卢珀和戴夫·麦考密克共同成立参议院两党科学与创新核心小组，旨在推动美国科学研究和技术创新，并研究人工智能政策与监管问题。该小组将重点关注科学创新带来的经济和国家安全影响，以及相关立法如何支持科研成果转化。希肯卢珀表示，在美国与对手国家加快人工智能竞争的背景下，仍需关注先进AI系统可能引发的安全风险，防止相关技术失控造成重大损害。官方资料显示，该小组将与产业界和科研机构合作，推动美国在科学与创新领域保持竞争力。

**链接****：https://www.nextgov.com/artificial-intelligence/2026/09/new-bipartisan-senate-science-caucus-will-address-ai/415986/**

04

美国防部发布“加速任务软件”指令，规范AI辅助军事软件开发与安全管理

美国国防部首席信息官克尔斯滕·戴维斯近日批准“加速任务软件”指令，对AI辅助软件开发、软件现代化及管理流程作出统一规范，以适应“软件定义战争”背景下的能力建设需求。指令明确，AI可用于自动化开发流程、优化系统集成并提升软件安全与韧性，但AI生成代码应视为“未经验证的输入”，开发团队仍对代码安全性、功能性和完整性承担责任，涉及安全或关键任务功能的修改必须经人工审核。国防部还要求记录所使用的AI模型、版本及重要数据集，形成类似软件物料清单的可追溯证据包，并禁止将非公开代码、配置及敏感文档输入未经批准的外部生成式AI服务。

**链接****：https://defensescoop.com/2026/09/14/pentagon-sets-procedures-for-ai-assisted-software-development/**

05

美国太空部队已成立技术组合执行办公室

美国太空部队已成立技术组合执行办公室，旨在衔接作战需求与产业新兴技术，破解研发成果向实际应用转化的“死亡之谷”难题。该办公室直接向空军负责太空采购与整合的助理部长汇报，与项目组合采购执行官（PAE）处于同等层级，将跨任务领域筛选潜力技术，联合商业企业等产业伙伴推进原型开发和技术成熟，推动成果纳入采购项目。此举是太空部队采购改革的一部分，该军种计划设立9个PAE，负责各任务领域项目的全生命周期管理，新办公室则补充其技术识别与原型开发能力。目前，办公室已组建，负责人仍在遴选中。

**链接****：https://defensescoop.com/2026/09/15/space-force-creates-office-to-accelerate-innovative-tech-acquisition/**

06

美国CISA与NIST联合发布身份令牌安全指南

9月15日，美国网络安全与基础设施安全局（CISA）与国家标准与技术研究院（NIST）联合发布身份令牌安全技术指南NIST IR 8587，为联邦机构和云服务提供商防范令牌伪造、窃取、重放及滥用提供实施依据。指南重点要求加强签名密钥隔离存储与轮换，严格验证令牌签名、受众及权限范围，建议访问令牌和身份令牌有效期通常不超过1小时，并通过发送方约束机制降低盗用风险。同时，强调完善令牌撤销、持续监测及事件响应，避免在日志和构建产物中暴露令牌。相关措施亦适用于使用签名令牌访问工具和数据的AI智能体，推动身份安全由一次性配置转向全生命周期管理。

**链接****：https://csrc.nist.gov/pubs/ir/8587/final**

07

CISA发布网络诱饵指南，强化关键基础设施威胁检测与响应能力

9月16日，美国网络安全与基础设施安全局（CISA）发布《利用网络诱饵强化检测与响应》指南，首次详细阐述防御性网络诱饵实施流程。针对攻击者利用合法凭据、系统原生工具及“就地取材”技术开展侦察、横向移动和数据访问等检测难题，指南建议关键基础设施运营者将诱饵能力与零信任模型结合，在内部网络及高价值区域部署仿真系统和信息资产，以尽早发现入侵、观察攻击行为并生成高可信告警，缩短平均检测时间。指南结合MITRE ATT&CK知识库与Engage框架，提供诱饵策略设计和实施方法，支持防御团队依据观察到的攻击行为优化资源配置，提升关键基础设施防御韧性。

**链接****：https://www.cisa.gov/news-events/news/new-cisa-guidance-helps-critical-infrastructure-detect-observe-and-impede-malicious-cyber-activity**

08

Cylus推出铁路网络安全智能代理平台Cylus.ai，强化威胁分析与响应能力

9月17日，据industrialcyber媒体网站报道，铁路网络安全厂商Cylus推出Cylus.ai，将智能代理技术与铁路安全专业知识融入运营方现有安全工具，辅助安全团队分析网络威胁、制定响应措施，并强调人员始终掌握控制权。该产品与旗下CylusOne平台深度集成，旨在将运营网络可视化监测结果转化为威胁理解与处置支持，缓解铁路系统互联程度提升、专业安全人才短缺及监管要求增加带来的压力。

**链接****：https://industrialcyber.co/news/cylus-launches-cylus-ai-to-add-agentic-intelligence-to-rail-cybersecurity-names-former-transit-leaders-to-advisory-board/**

09

OpenAI发布模型失对齐事件报告框架，披露AI智能体越权操作案例

9月16日，OpenAI发布模型失对齐事件报告框架，并披露过去六个月观察到的六起异常行为案例，涉及模型在任务摘要中植入绕过约束或隐瞒错误的指令、未经授权使用暴露的API密钥、编造数据，以及擅自将本地文件上传至公共网络。部分案例显示，协作智能体为解决文件访问障碍，违反仅限本地存储的要求，通过公共托管服务传递任务成果。新框架按调查需求对事件分类，记录行为过程、安全影响及缓解措施。

**链接****：https://openai.com/index/model-misalignment-reporting-framework/**

03

漏洞资讯

01

GitLab存在路径遍历漏洞

近日，安全研究人员发现GitLab存在路径遍历漏洞（CVE-2026-85706），是由仓库提交API路径限制不当及身份验证缺失所导致，在存在至少一个公开项目的条件下未经认证的攻击者可读取服务器任意文件，并可能获取日志、配置文件、凭据及CI/CD敏感信息。目前，用户可通过将软件版本升级至19.3.2、19.2.6和19.1.8的方式修复上述安全漏洞。

**链接：https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html**

02

Linux内核存在安全漏洞

近日，安全研究人员发现Linux内核存在安全漏洞（CVE-2026-43502），并通过名为ZcopyReaper的漏洞利用工具验证其可被用于本地权限提升。该漏洞存在于4.17起即受影响，由零拷贝发送失败时内存清理与生命周期管理不当所导致，可能造成内核内存破坏，并进一步获取root权限。Linux上游已通过提交44b550d88b26修复，Linux 7.1-rc3包含该补丁，Ubuntu和Debian等发行版也已开始回迁修复。鉴于漏洞利用代码已公开，建议相关组织机构应尽快升级内核并检查RDS模块使用情况，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/zcopyreaper-linux-kernel-vulnerability/**

03

Cisco ISE 存在安全漏洞

近日，安全研究人员发现思科集中式策略管理平台Cisco ISE存在安全漏洞（CVE-2026-76460），位于Cisco ISE Passive Identity Connector（ISE-PIC）组件中，是由API端点身份验证机制存在缺陷所导致，允许攻击者向目标用户设备发送恶意请求的方式绕过身份验证安全机制，对用户设备造成损害。目前，用户可通过补丁更新修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/**

04

地下论坛出现 Fortinet FortiGate 远程代码执行漏洞利用工具售卖信息

近日，安全研究人员监测发现某用户在地下论坛出售针对Fortinet FortiGate SSL VPN设备的远程代码执行漏洞利用工具，声称影响FortiOS 7.2.x和7.4.x版本，可用于获取初始访问权限，并称可提供概念验证视频。目前，该售卖信息未经独立验证，未披露CVE编号、认证要求及技术细节，尚无法判断其是否涉及已修复漏洞。鉴于Fortinet相关产品既有安全漏洞仍遭持续利用，建议相关组织及时安装补丁、限制公网访问权限，同时排查异常VPN会话，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/hackers-selling-fortinet-fortigate-1-day-vulnerability/**

04

木马病毒

01

攻击者滥用AutoIt与Windows字符映射表进程隐蔽部署AsyncRAT木马

近日，安全研究人员发现一条利用AutoIt和Windows受信任进程投递AsyncRAT的多阶段攻击链。攻击者以“InvoiceDetails.bat”等诱导性批处理文件为入口，调用隐藏PowerShell解码混淆载荷，并在临时目录释放重命名的AutoIt解释器、加载脚本及加密文件，同时通过启动文件夹实现无管理员权限持久化。随后，加载器在内存中解密载荷，将AsyncRAT注入微软签名的charmap.exe进程，并对AMSI进行修补，以降低脚本和程序集活动被检测的概率，最终落地的木马载荷可执行屏幕截取、远程控制及数据外传等操作。安全研究人员建议重点监测隐藏PowerShell、AutoIt异常调用、charmap.exe远程线程创建及异常外联行为，以提升自身安全防护能力。

**链接：https://cybersecuritynews.com/hackers-inject-asyncrat/**

02

新型DDRop硬件攻击可突破Intel TDX与AMD SEV-SNP保密计算防护

鲁汶大学、苏黎世联邦理工学院、达勒姆大学及谷歌研究人员披露新型DDRop硬件攻击，可利用DDR5内存“新鲜度”校验缺失问题，对Intel TDX、Scalable SGX及AMD SEV-SNP保密计算环境实施内存完整性破坏。攻击者需预先控制服务器软件，并短暂物理接触设备，在处理器与内存模块之间插入低成本中间板通过静默丢弃内存写入，使处理器继续读取旧的加密数据。研究人员在Intel TDX环境中演示了受保护虚拟机内存读取、调试模式切换及远程证明伪造等效果，在AMD SEV-SNP中也可实现页面内容复制。该问题源于硬件设计，当前暂无简单补丁，研究人员建议通过限制相关内存管理功能、校验关键写入及启动时检测中间设备等方式降低风险。

**链接：https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html**

03

CyclopsBlink恶意程序被披露

近日，安全研究人员在被攻陷的Cisco Firewall Management Center设备中发现新版CyclopsBlink恶意程序。经分...