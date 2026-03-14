---
title: 每周网络安全简讯 ( 2026年 第11周 )
url: https://mp.weixin.qq.com/s/GIhJozR1MtusskkDPRToyA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:11:15.086254
---

# 每周网络安全简讯 ( 2026年 第11周 )

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qyzTicOO6WeVuCuCQ2VNbNicOoRoRFPibD54YrlkZTYEtlnwjphiaFc2wYAZhBIT0TpL8FjjeVMQAFWsfpIENfyKIX0lSzDickJjje4jzkSW80LQ/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第11周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器中沉浸阅读

2026年3月7日至2026年3月13日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计22条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织Transparent Tribe对印度目标用户实施网络攻击

近日，安全研究人员监测发现APT组织Transparent Tribe以鱼叉式网络钓鱼攻击作为初始入侵手段，进而利用AI编码工具生成多个使用Nim、Zig、Crystal等小众编程语言开发的恶意程序，对印度目标用户实施网络攻击，包括：一是基于Crystal编写的Warcode加载器，用于将Havoc代理工具注入到目标设备内存中；二是基于Rust编写的SupaServ后门程序，可利用Supabase平台实现C2通信；三是基于Rust编写的LuminousStealer信息窃取程序，可利用Firebase和Google Drive收集所窃的用户特定类型文件；四是基于Crystal编写的CrystalShell后门程序，可对Windows、Linux、macOS系统实施命令执行、设备参数收集等操作；五是基于Zig编写的ZigShell恶意程序，可以通过Slack进行C2通信，且支持文件上传、下载等额外功能；六是基于Rust编写的LuminousCookies恶意程序，可窃取用户浏览器中的Cookie、密码、支付信息等敏感数据；七是基于Rust编写的BackupSpy恶意程序，可监控用户本地文件系统，收集受控设备和外部存储介质中的高价值数据；八是基于Zig编写的ZigLoader加载器，可解密执行任意Shellcode。综上，此次攻击事件表明，AI辅助恶意程序生成，极大提升了网络攻击的工业化能力，使得攻击者能够轻易扩大攻击规模。

**链接：https://thehackernews.com/2026/03/transparent-tribe-uses-ai-to-mass.html**

02

APT组织MuddyWater对美国目标用户实施网络攻击

近日，安全研究人员监测发现APT组织MuddyWater针对美国银行、机场、非营利组织及某美国软件公司以色列分支实施网络攻击。据称，此次攻击事件中，该APT组织在向该软件公司、银行等目标用户实施攻击后，向其受控设备植入Dindoor新后门程序，通过Deno执行各类恶意功能，进而尝试利用Rclone恶意工具将所窃数据向Wasabi云存储桶进行上传。同时，安全研究人员在针对美国机场和非盈利组织的网络攻击事件中，还捕获到从美国Backblaze云存储公司服务器下载的Fakeset后门程序，在植入受控设备后可实施敏感信息窃取、命令执行等恶意操作。

**链接：https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html**

02

网络动态

01

美国发布新版国家网络战略

近日，美国特朗普政府发布新版网络安全战略，为美国政府未来三年的网络政策提供指引。据称，该战略对网络防御及进攻性网络打击提供“常识性监管”和“关键、新兴技术优势”在内的多项支柱策略，强调“零信任架构、安全云、后量子加密、人工智能”等优先事项，同时将私营部门纳入体系，协助相关组织机构识别和对抗网络攻击行为。

**链接****：https://www.whitehouse.gov/articles/2026/03/white-house-unveils-president-trumps-cyber-strategy-for-america/**

02

OpenAI推出Codex Security人工智能安全代理

近日，OpenAI正式推出Codex Security人工智能安全代理，可利用其前沿模型推理能力，结合自动验证功能，对代码仓库进行安全检测。同时，在安全漏洞检出后，可将其置于系统上下文中，在向用户展示前进行结果验证，以最大限度降低误报率。目前，该安全代理在30天的测试期间对120万个外部仓库的提交代码进行检测，识别出OpenSSH、GnuTLS、GOGS、Thorium、libssh、PHP和Chromium等开源项目中的792个关键漏洞和10,561严重漏洞。

**链接：**https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html

03

国际电子商务顾问理事会扩充人工智能认证套件，以加强美国人工智能教育培训

近日，国际电子商务顾问理事会（EC-Council）对企业人工智能认证套件进行扩充，并对Certified CISO v4认证进行了优化。其中，扩充的四项新认证包括：一是“人工智能基础”（Artificial Intelligence Essentials,AIE），构建了基础的人工智能技能素养；二是“认证AI项目经理”（Certified AI Program Manager,CAIPM），需具备将AI战略转换为落地执行的能力，协调团队进行具体项目的治理和支付；三是“认证进攻性人工智能安全专业人员”（Certified Offensive AI Security Professional,COASP），需具备人工智能精英能力，用于测试大型语言模型安全漏洞，模拟漏洞利用过程，并以此保护人工智能基础设施，增强企业对新型网络安全威胁的防护能力；四是“认证负责任人工智能治理与伦理”（Certified Responsible AI Governance & Ethics,CRAGE），需具备企业级管理人员相关能力，在合规（NIST/ISO）前提下进行人工智能的治理与管控。同时，Certified CISO v4认证的更新内容涉及针对AI驱动风险环境的高管网络领导教育，且将智能系统纳入核心业务运营和安全决策环节，以增强管理人员的AI治理意识和决策能力。

**链接****：https://www.bleepingcomputer.com/news/security/ec-council-expands-ai-certification-portfolio-to-strengthen-us-ai-workforce-readiness-and-security/**

04

欧空局与英国航天局将在英国建设卫星通信人工智能中心

近日，欧洲航天局（ESA）和英国航天局（UKSA）宣布在英国牛津郡“欧洲空间应用与电信中心”（ECSAT）部署新人工智能中心。据欧洲航天局声称，该人工智能中心将重点开发智能自主机器人和无人机系统，提供专门环境测试和扩展卫星融合通信的AI驱动能力，同时充分利用可用频段构建跨多卫星轨道的认知网络，以综合推动英国卫星链接的发展进程。

**链接****：**https://orbitaltoday.com/2026/03/08/esa-and-uksa-announce-new-ai-hub-for-satellite-communications-in-the-uk/

05

可通过Wi-Fi信号绘制人体姿势的监测方式被披露

近日，安全研究人员披露一款名为π RuView的开源边缘AI系统，可利用Wi-Fi硬件捕捉人体在无线环境中移动时对OFDM子载波产生的扭曲影响，提取幅度和相位变化，进而借鉴计算机视觉深度学习架构，对收集到的“信道状态信息”（CSI）元数据进行分析，并最终实现对人体动态姿势和表面区域的模型重建和人员实时监测。该AI系统仅依靠ESP32微控制器即可实现基本功能，部署4至6个节点即可完成全房间覆盖，穿墙检测深度达5米。目前，GDPR已将Wi-Fi追踪标识符归类为个人数据，但基于CSI的身体姿势提取仍处于监管灰色地带，建议相关用户将被动射频感知视为新兴物理层网络安全威胁，采取射频屏蔽、网段内ESP32设备监控等方式降低安全风险。

**链接****：**https://cybersecuritynews.com/wifi-signals-reveal-human-activities/

06

英国发布国家反欺诈战略，将网络诈骗治理责任扩展至科技平台与通信运营商

近日，英国政府发布《2026-2029年度国家反欺诈战略》，并宣布成立新的在线犯罪中心（Online Crime Centre），计划自4月起联合政府、警方、情报机构、银行、通信运营商及大型科技企业开展协同打击行动。该战略提出，未来3年将投入2.5亿英镑，其中逾3000万英镑用于支撑新机构建设，通过整合跨部门情报、即时共享数据、识别并关停诈骗团伙依赖的账户、网站和电话号码，系统性打击诈骗短信、诈骗电话、虚假社交媒体账号及跨境诈骗基础设施。战略特别强调，面对东南亚、西非、东欧、印度和中国等地海外诈骗窝点加速扩张、超过三分之二诈骗活动源自境外的趋势，英国将进一步强化国际执法合作，并推动人工智能在诈骗模式识别、可疑转账拦截和诱骗取证等场景中的应用。同时，英国还将通过建立全国统一受害者服务标准、部署重点人群保护警员网络、加快司法处置和强化民事追责等措施，形成政府、监管机构、执法部门与产业界共同负责的系统性反欺诈治理框架。

**链接****：**https://www.gov.uk/government/news/new-disruption-unit-launched-in-crackdown-on-fraud

07

美国发布反无人机系统测试指南并强调隐私合规

美国联合跨机构特遣部队401（JIATF-401）近日宣布采纳《反无人机系统技术测试与评估标准指南》，要求所有反小型无人机系统（C-sUAS）评估统一采集核心数据，以构建可在国防体系内共享、对比和综合利用的统一证据基础。该举措旨在应对敌方小型无人机在情报侦察和直接打击方面带来的双重威胁，解决当前反无人机测试数据来源分散、标准不一、质量不稳等问题。新框架通过建立统一术语体系和评估准则，将提升不同反无人机系统测试结果的一致性、可重复性和可比性，支撑更高效的能力验证、采购决策和技术研发，同时减少重复测试、优化资源投入，并增强作战人员对相关装备可靠性和实战适用性的信心。美方表示，此举将进一步推动军种间及跨机构反无人机能力建设协同，加快先进反无人机技术向规模化、实战化应用转化。

**链接****：**https://www.war.gov/News/Releases/Release/Article/4429866/the-standard-guidelines-for-test-and-evaluation-of-counter-unmanned-aircraft-sy/

08

美国陆军拟建立新数据运营中心

美陆军正推进组建“陆军数据运营中心”（Army Data Operation Center，ADOC），拟将其打造为面向全球的信息流转与数据调度枢纽，统筹合作伙伴、联合部队及作战司令部之间的数据传输与融合。美陆军认为，当前制约作战效能提升的关键问题并非数据不足，而是数据长期处于孤岛化状态，缺乏统一的权威来源、标记规则和访问控制机制。为此，ADOC将重点解决数据发现、标签治理、基于属性的访问控制及数据支撑决策等问题，提升战场环境下的信息共享效率和决策优势。美军方表示，该中心未来不仅服务于陆军自身，还可能进一步拓展至更广泛的联合部队乃至国防部层面，显示出其正加快推动以数据为核心的全球作战支撑体系建设。

**链接****：**https://breakingdefense.com/2026/03/new-army-data-operation-center-will-be-9-1-1-for-moving-info-around-the-globe/

09

美国医疗设备制造商Stryker遭受黑客组织Handala攻击

近日，美国医疗设备制造商Stryker向美国证券交易委员会（SEC）提交8-K文件并称，该制造商近期遭受一起黑客攻击事件，已导致其部分信息技术系统受影响，造成内部Microsoft环境的全球性中断，且订单处理、产品制造和发货等也受到一定影响。与此对应，黑客组织Handala宣称对此攻击事件负责，声称已窃取50TB数据并对该制造商超过20万台系统、服务器、移动设备的数据进行了擦除操作。目前，受影响设备的规模尚未经明确证实，Stryker表示正在对此次攻击事件的具体性质、影响范围进行联合调查。

**链接****：**https://therecord.media/stryker-tells-sec-unknown-timeline-recovery

03

漏洞资讯

01

WordPress用户注册及会员插件存在安全漏洞

近日，安全研究人员发现由 WPEverest开发的WordPress会员插件（User Registration & Membership plugin）存在安全漏洞（CVE-2026-1492），允许攻击者在无需任何身份验证的情况下创建管理员账户，进而拥有目标用户站点的完全访问权限，对用户数据造成损害。漏洞影响5.1.2或更早版本，目前用户可通过将版本升级至5.1.3的方式修复上述安全漏洞。

**链接：https://www.sentinelone.com/vulnerability-database/cve-2026-1321/**

02

Nginx UI存在安全漏洞

近日，安全研究人员发现Nginx UI存在安全漏洞（CVE-2026-27944），是由/api/backup目录访问权限设置不严格且X-Backup-Security响应数据存在加密密钥所导致，允许攻击者无需身份验证即可下载和解密完整服务器备份。漏洞影响Nginx UI version < 2.3.3等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://securityaffairs.com/189123/security/critical-nginx-ui-flaw-cve-2026-27944-exposes-server-backups.html**

03

微软公司发布3月份安全漏洞更新公告

近日，微软公司发布3月份安全漏洞更新公告，涉及多个产品的84个安全漏洞，其中有6个安全漏洞较为严重，包括：一是位于.NET的拒绝服务漏洞（CVE-2026-26127）；二是位于SQL Server的权限提升漏洞（CVE-2026-21262）；三是Microsoft设备定价计划页面存在的远程代码执行漏洞（CVE-2026-21536）；四是位于Winlogon进程组件中的权限提升漏洞（CVE-2026-25187）；五是位于Azure模型上下文协议（MCP）服务器中服务器端请求伪造漏洞（CVE-2026-26118）；六是由Excel网页生成过程存在安全缺陷所导致的信息泄露漏洞（CVE-2026-26144）。目前，用户可通过补丁更新修复上述安全漏洞。

**链接：https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html**

04

惠普Aruba Networking AOS-CX存在多个安全漏洞

近日，安全研究人员发现惠普企业（HPE）Aruba Networking AOS-CX存在多个安全漏洞，其中认证绕过漏洞（CVE-2026-23813）较为严重，是由AOS-CX交换机基于网络的管理界面存在缺陷所导致，允许未经身份验证的攻击者绕过认证机制，甚至重置目标设备管理员密码。目前，用户可通过补丁更新、版本升级等方式修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/security/hpe-warns-of-critical-aos-cx-flaw-allowing-admin-password-resets/**

05

n8n工作流程自动化平台存在2个安全漏洞

近日，安全研究人员发现被广泛应用的n8n工作流程自动化平台存在2个安全漏洞，其中第一个安全漏洞是远程代码执行漏洞（CVE-2026-27577），是由表达式编辑器沙箱转义存在安全缺陷所导致，允许攻击者远程执行任意代码；第二个安全漏洞是“双重评估漏洞”（CVE-2026-27493），是由n8n表单端点存在认证缺陷所导致，允许攻击者在“联系我们”表单中注入恶意代码的方式实现任意shell命令执行。漏洞影响n8n version < 1.123.22等版本，目前用户可通过将版本升级至2.10.1、2.9.3和1.123.22的方式修复上述安全漏洞。

**链接：https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html**

06

SolarWinds Web Help Desk存在反序列化漏洞

近日，安全研究人员发现SolarWinds Web Help Desk存在反序列化漏洞（CVE-2025-26399），是由AjaxProxy组件对数据包处理验证存在缺陷所导致，允许攻击者通过发送恶意载荷的方式，在目标设备系统内存中直接执行任意指令。目前，用户可通过补丁更新等方式修复上述安全漏洞。

**链接：https://cybersecuritynews.com/solarwinds-web-help-desk-deserialization-vulnerability/**

07

ZIP压缩格式文件存在安全漏洞

近日，安全研究人员披露了一种名为“Zombie ZIP”的攻击技术，可利用ZIP压缩格式文件安全漏洞（CVE-2026-0866），通过篡改ZIP文件头压缩方式字段，将实际采用DEFLATE方式压缩的数据伪装成未压缩内容，从而误导杀毒软件、EDR按照正常文件的方式对压缩格式文件进行扫描，导致恶意载荷的漏报。研究显示，该攻击技术对现有检测体系具有较强规避能力，在VirusTotal测试中可绕过约98%的杀毒引...