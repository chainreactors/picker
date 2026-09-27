---
title: 每周网络安全简讯 ( 2026年 第39周 )
url: https://mp.weixin.qq.com/s/3JI4Qo6GsCdR-jtY7uiejQ
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:22:50.146768
---

# 每周网络安全简讯 ( 2026年 第39周 )

# 每周网络安全简讯 ( 2026年 第39周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年9月19日至2026年9月24日，国家信息技术安全研究中心在线监测技术研究实验室对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计20条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织WaterPlum利用虚假招聘传播恶意软件，窃取逾千万美元加密资产

APT组织WaterPlum于2025年12月至2026年7月开展“Contagious Interview”攻击活动，影响100多个国家至少3万台计算机，从7000多个加密货币钱包获取资金或凭据，转移至少1070万美元加密资产。WaterPlum冒充招聘人员，以编程测试或修复面试软件故障为由，诱导开发者运行携带BeaverTail、InvisibleFerret等恶意软件载荷的项目或文件，实现远程控制与信息窃取。其中，StoatWaffle可利用VS Code配置，在用户打开并信任项目文件夹后执行恶意代码。安全研究人员建议相关组织机构加强招聘身份核验与测试代码隔离，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/north-korean-waterplum-hackers/**

02

APT组织TraderTraitor利用虚假Terraform面试任务投放macOS后门

朝鲜关联组织TraderTraitor通过GitHub托管虚假Terraform面试任务项目，诱导具备DevOps及金融科技经验的求职者加载恶意提供程序，在macOS设备上部署FLATROOF和ROOFDECK后门。其中，FLATROOF可收集浏览器数据、终端历史及登录钥匙串，通过Telegram外传文件；ROOFDECK支持命令执行、剪贴板读取和文件窃取，利用LaunchAgent实现持久化，并通过去中心化Nostr网络解析C2服务器地址。目前，安全研究人员已在一家印度IT服务商发现相关感染情况，建议相关组织机构加强面试项目审查及凭据保护，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/tradertraitor-hackers/**

02

网络动态

01

美国海岸警卫队拟设人工智能与机器学习中心，强化任务支撑与人才培养

美国海岸警卫队计划于今年秋季在海岸警卫队学院设立人工智能与机器学习中心，作为“2028年部队规划”的组成部分，提升任务执行、技术研发及人才培养能力。该中心将联合政府、学术界和产业界，与技术准备局及数据与人工智能办公室协同，重点开展实用AI工具开发、任务导向研究及军文职人员培训，推动获批AI工具的安全、负责任使用。中心计划在六个月内形成可运行原型，现有项目涉及浮标布局优化、巡逻舰艇调度及海上边界安全，并将与约翰霍普金斯大学、麻省理工学院林肯实验室及美国国家安全局等机构开展合作，加快AI技术向实际任务应用转化。

**链接****：https://industrialcyber.co/ai/us-coast-guard-launches-ai-and-machine-learning-center-to-advance-operational-readiness-workforce-development/**

02

特朗普提出组建“人工智能军队”，具体职责与组织定位尚未明确

近日，美国总统特朗普提出组建“人工智能军队”（AI Force），并计划任命新的人工智能事务负责人，在推动AI产业发展的同时识别和应对潜在风险。特朗普将该构想类比其首任期内成立的太空军，但尚未说明其是否属于军事机构，以及在模型监管中的权限、任务和资源安排。白宫科技政策办公室负责人强调，AI影响涉及多个联邦机构，需要加强白宫层面的跨部门协调能力。

**链接：https://www.nextgov.com/artificial-intelligence/2026/09/trumps-floats-creating-ai-force/416124/**

03

NIST发布OT安全指南修订草案，强化零信任与后果导向风险管理

美国国家标准与技术研究院（NIST）发布《运营技术安全指南》SP 800-82r4初步公开草案，围绕网络安全框架2.0重构指导内容，扩展资产管理、网络监测与零信任应用要求，覆盖水务、农业、货运铁路及船舶等领域。草案强调以潜在物理后果为导向开展风险管理，将网络防护与工程措施结合，保障人员安全及生产连续性；建议分离OT与企业网络，并在OT内部区分生产控制与管理网络，通过独立凭证、最小权限及持续监测降低横向移动风险。

**链接：https://industrialcyber.co/nist/nist-sp-800-82r4-draft-expands-ot-security-guidance-with-zero-trust-csf-2-0-consequence-driven-risk-management/**

04

CISA发布CVE项目质量框架白皮书，推动漏洞治理与数据质量提升

9月23日，美国网络安全与基础设施安全局（CISA）发布《CVE项目：建立质量时代框架》（CVE Program: Establishing a Quality Era Framework）白皮书，推动通用漏洞披露（CVE）项目由“增长时代”向“质量时代”转型。针对全球CVE编号机构及根级管理机构持续扩展、人工智能技术给软件生命周期带来新压力等情况，白皮书衔接既有战略，明确质量标准、实施路线图及成效衡量方式，重点围绕透明有效的项目治理、广泛活跃的全球生态参与、稳健的数据基础设施及可信赖的CVE记录内容四个维度推进改进。CISA表示将持续支持CVE项目运行，并邀请全球产业界、政府及安全社区参与反馈与协作。

**链接****：https://www.cisa.gov/news-events/news/cisa-whitepaper-charts-path-establishing-and-maturing-cve-program-quality**

05

OpenAI与乌克兰开展“Daybreak”合作，利用人工智能加强关键基础设施网络防护

OpenAI与乌克兰政府宣布合作，通过“Daybreak”（黎明）计划提供网络安全人工智能模型及补贴算力资源，支持电网、水务等关键基础设施抵御网络攻击。乌方表示相关工具将用于事件响应、威胁分级、登录分析、系统资产盘点、代码分析及漏洞验证，通过加快海量日志处理和威胁研判，辅助安全人员提升防御效率。OpenAI表示，希望与更多政府及行业建立类似合作，推动防御方在人工智能能力进一步扩散前加快漏洞修复与网络加固。

**链接****：https://cyberscoop.com/openai-ukraine-cybersecurity-critical-infrastructure/**

03

漏洞资讯

01

研究人员公布BigDiskBuster概念验证代码，可干扰Microsoft Defender更新

安全研究人员MSNightmare公布拒绝服务概念验证代码BigDiskBuster，可通过耗尽磁盘空间与文件锁定，干扰Microsoft Defender平台及安全情报更新。该工具监测更新目录变化，创建临时文件占用剩余磁盘空间，并限制恶意软件删除工具MRT.exe的写入或删除操作，阻碍更新安装与回滚。该技术不会直接关闭Defender，但可能使其在保持运行的情况下因更新受阻而降低新型恶意软件识别能力。目前代码仍处于实验阶段，其声称的全受支持Windows版本兼容性尚未经独立验证。安全研究人员建议相关组织机构关注磁盘空间骤降、异常临时文件及反复更新失败情况，避免仅凭通用安装错误码误判攻击情况。

**链接：https://cybersecuritynews.com/defender-bigdiskbuster-dos-flaw/**

02

WordPress存在安全漏洞

近日，安全研究人员发现WordPress核心组件存在跨站请求伪造漏洞Click2Shell，是由主题预览参数处理缺陷所导致，攻击者无需账户，只需诱导已登录且具备主题安装权限的管理员访问特制链接，就可强制授权安装官方目录中的主题，如果结合存在漏洞的主题，自定义器预览可加载未激活主题的PHP代码，便会实现服务器端远程代码执行，可能导致敏感数据泄露、文件篡改及恶意管理员账户创建。上述安全漏洞影响7.1.0及更早版本，技术细节与概念验证代码已公开，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/security/wordpress-click2shell-flaw-lets-hackers-execute-php-on-the-server/**

03

OpenAI Codex存在2个沙箱逃逸漏洞

近日，安全研究人员披露OpenAI Codex存在Heapjack和Overpatch两项沙箱逃逸漏洞。Heapjack利用node\_repl组件共享内存堆缺陷，获取认证令牌并冒充可信组件调用沙箱外进程，可在只读模式下绕过审批执行主机命令。Overpatch则利用apply\_patch工具的权限计算缺陷，结合符号链接越界修改用户Shell启动文件，在用户后续打开终端时执行恶意代码。上述安全漏洞已于8月12日报告，OpenAI在八天内完成修复，用户可通过将相关产品升级至Codex Desktop 26.818.21641和Codex CLI 0.149.0的方式修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/**

04

D-Link DIR-822A路由器存在2个安全漏洞

近日，安全研究人员发现D-Link DIR-822A路由器A\_101固件存在2个安全漏洞。其中，第一个安全漏洞是位于udhcpcd组件中的栈缓冲区溢出漏洞（CVE-2026-86296），未经身份验证的远程攻击者可通过向目标设备发送特制请求的方式引发设备崩溃、服务中断，甚至可能执行任意代码；第二个安全漏洞是位于L2TP控制消息解析中的越界写入漏洞（CVE-2026-86510），允许具备低访问权限的攻击者通过使用特制L2TP控制消息的方式致使内存损坏。目前，受影响硬件版本、区域产品范围及修复情况仍在核实中，相关组织机构应核对设备型号与固件版本，关闭非必要远程管理，限制管理接口访问，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/d-link-router-hit-by-cvss-10-0-flaw/**

05

Linux KVM存在安全漏洞

近日，安全研究人员发现Linux内核KVM嵌套虚拟化代码模块存在安全漏洞（CVE-2026-89775）。攻击者可通过构造特定客户机内存布局的方式，使地址转换缓存（TLB）失效操作被跳过，导致已释放的宿主机内存仍可被客户机读写。研究人员表示，该漏洞可用于虚拟机逃逸，在宿主机执行恶意代码，具备/dev/kvm访问权限的本地用户也可借此获取root权限。目前，用户可通过将操作系统内核版本升级至Linux 6.18.51、7.2.5及7.3-rc1的方式修复上述安全漏洞。

**链接：https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html**

06

微软SharePoint存在代码注入漏洞

近日，安全研究人员发现微软SharePoint Server存在代码注入漏洞（CVE-2026-65660），是由ToolPane组件重构注册指令时未正确转义引号所导致，允许经初步身份验证的攻击者无需用户交互即可绕过SafeControls检查，进而远程执行任意代码。目前，技术细节及可用利用代码已在互联网公开，用户可通过补丁更新修复上述安全漏洞。

**链接：https://cybersecuritynews.com/microsoft-sharepoint-rce-flaw/**

07

Next.js存在安全漏洞

近日，安全研究人员发现Next.js图像生成功能ImageResponse存在安全漏洞（CVE-2026-94545），是由内置Satori库对部分输入转义不当所导致，当应用将攻击者特制数据传入SVG内容、属性或样式时，可能结合下游依赖库缺陷实现任意代码执行。目前，用户可通过将版本升级至16.3.6及更新版本的方式修复上述安全漏洞。

**链接：https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html**

08

GitLab存在安全缺陷

近日，安全研究人员发现，GitLab邮件创建工作项功能的私有地址包含长期有效的账户级令牌，且不同项目复用同一令牌。攻击者获取该地址、目标项目路径及ID后，可通过邮件提交Git补丁，以令牌所属用户的权限写入代码，篡改CI/CD配置还可能造成源码及敏感凭据泄露。该邮件通道不受项目IP访问限制，也不要求发件地址为用户已验证邮箱，实际影响取决于用户权限、分支保护及流水线配置。目前，GitLab官方将此行为视为设计缺陷，已更新说明，但保留相关电子邮件机制，建议相关组织机构将项目邮件地址按账户凭证保护，排查泄露并及时重置令牌，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/gitlab-email-private-repository-flaw/**

04

木马病毒

01

ChainScript远控木马借助ClickFix传播并利用区块链动态切换C2基础设施

近日，安全研究人员披露一款名为ChainScript的新型远程访问木马。攻击者利用ClickFix诱饵，诱导用户执行伪装成Spotify等软件的恶意Windows安装程序，通过隐藏的PowerShell和VBScript部署Node.js运行环境并启动木马，借助计划任务及注册表Run键实现持久化。经分析，ChainScript支持远程命令执行、文件操作、截屏、载荷投放及加密货币钱包枚举，并利用Polygon智能合约获取活跃的WebSocket服务器地址，使攻击者无需替换木马即可切换C2基础设施，一定程度上增加了封堵与基于固定指标检测的难度。

**链接：https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html**

02

BragJack攻击技术利用恶意扩展劫持浏览器AI代理

Forever Security研究人员披露BragJack攻击技术，并在Chrome Gemini、Comet、Edge、Opera Neon及Claude in Chrome五类浏览器或助手中完成概念验证。攻击以受害者已安装恶意扩展为前提，利用Chromium网络请求规则功能篡改受信任页面或资源，突破AI组件权限边界，通过“强制提示”直接向代理下达指令，无需进一步用户交互即可滥用其权限。演示显示，攻击可读取本地文件、浏览记录及截图，并驱使代理汇总邮件后外传。相关研究涉及两项CVE漏洞，谷歌与微软已修复各自对应问题。

**链接：https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/**

03

思科Talos发布CAIRN工具，追踪集成AI的恶意软件

近日，思科Talos发布开源工具包CAIRN，通过分析提示模板、模型接口、API密钥前缀及编排逻辑等元数据，结合YARA规则、关系图谱与语义聚类，辅助识别和追踪集成AI的恶意软件。研究同时披露Windows植入程序CLOSEDQUORUM，其设计通过调用最多四种大语言模型投票选择后续行动，涉及凭证窃取、进程注入、持久化及通过Discord外传数据。Talos强调，AI相关特征与聚类结果仅提供调查线索，不能直接作为恶意判定或攻击归因依据，需结合逆向分析及终端行为进行深入验证。

**链接：https://cybersecuritynews.com/cairn-tool-for-tracking-ai-malware/**

04

开发文档占位域名被用于ClickFix攻击，诱导Windows用户执行恶意命令

长期用于开发文档和代码示例的占位域名third-party[.]com被发现承载ClickFix攻击页面。攻击者伪造Cloudflare人机验证，将恶意PowerShell命令写入剪贴板，诱导Windows用户手动执行，进而下载并运行后续载荷。该域名并非专用保留域名，被多处开发文档、AI技能及MCP服务器文档引用，直接复制示例可能使应用或工具访问恶意页面。目前，安全人员经测试发现载荷域名已无法解析，攻击链暂时中断，最终载荷功能尚未确认，也无证据表明是否存在实际感染情况，建议排查示例代码中的外部域名，以专用保留域名进行替换，同时加强对伪造验证及异常脚本执行的防范力度，以降低遭受此类攻击的风险。

05

可窃取文档及Wi-Fi凭据的TASK#STOMP后门被披露

近日，安全研究人员披露Windows后门TASK#STOMP，可在植入用户设备后，扫描固定磁盘中的办公文档和压缩文件，持续监控文件变化，利用VBS脚本、PowerShell及计划任务实施持续窃密与远程控制，并对Wi-Fi密码、剪贴板内容及屏幕截图进行窃取。同时，该后门采用双PowerShell模块相互重启、备用控制服务器切换及文件时间戳篡改增强自身隐蔽性和恢复能力。安全研究人员建议相关组织机构关联监测脚本创建任务、隐藏PowerShell及C#编译器调用行为，处置时同步清除全部驻留组件，防止残留模块恢复感染。

**链接：https://cybersecuritynews.com/new-taskstomp-backdoor/**

![](https://mmbiz.qp...