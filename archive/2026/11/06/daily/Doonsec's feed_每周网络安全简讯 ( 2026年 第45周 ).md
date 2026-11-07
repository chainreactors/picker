---
title: 每周网络安全简讯 ( 2026年 第45周 )
url: https://mp.weixin.qq.com/s/rVE5_1elRMUvNVYLtHEjLQ
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:58:28.439743
---

# 每周网络安全简讯 ( 2026年 第45周 )

# 每周网络安全简讯 ( 2026年 第45周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年10月31日至2026年11月6日，国家信息技术安全研究中心在线监测技术研究实验室对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计19条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织DarkBlinders对以色列、伊拉克目标用户实施网络攻击

近日，安全研究人员发布报告称，疑似与伊朗存在关联的APT组织DarkBlinders于2026年8月至10月针对以色列及伊拉克库尔德斯坦地区实施网络攻击，致使以色列一名知名人士及库尔德斯坦地区政府云环境遭到入侵。报告指出，该APT组织以鱼叉式钓鱼为主要初始访问手段，利用仿冒政府、网页邮箱及云服务的域名窃取凭据或投放恶意文件，并搭建虚假视频会议应用StarkMeet，诱导用户安装后执行加载器ShelbyLoaderV2及借助GitHub实施命令控制的后门SHELBYC2，最终对目标用户实施持久性远控。

**链接：https://thehackernews.com/2026/11/darkblinders-compromises-israeli-target.html**

02

APT组织Bitter利用PapRAT远控木马持续针对南亚地区目标实施网络攻击

近日，FortiGuardLabs安全团队声称，APT组织Bitter使用三条不同的感染链，分别借助LNK文件、VHDX磁盘镜像和URL快捷方式针对南亚地区多个目标组织实施网络攻击，在入侵过程中滥用ftp.exe、计划任务、MSI安装程序及WebDAV等Windows合法功能掩盖自身攻击行为，并最终投放定制远控木马PapRAT，其中一条攻击链还会进一步投放WmRAT。其中，PapRAT已由C++改用Rust重写，指令由8个增至11个，新增PowerShell执行、休眠等功能。安全研究人员建议称，相关组织应谨慎处理来源不明的LNK文件、URL快捷方式、磁盘镜像及MSI安装包，加强对可疑执行链和出站C2流量的检测，以降低遭受攻击的风险。

**链接：https://www.darkreading.com/cyberattacks-data-breaches/paprat-cyberespionage-campaign-bitter-south-asia**

03

APT组织APT29开展大规模水坑攻击，针对iOS和安卓目标用户实施网络攻击

近日，安全研究人员披露APT组织APT29实施代号为“Poisoned Source”的大规模水坑攻击行动。该行动综合采用三类感染途径，包括：入侵合法网站注入恶意JavaScript、搭建仿冒美国、乌克兰、捷克及保加利亚知名网站的相似域名，以及在8月27日至9月3日期间篡改乌克兰网络分析服务Plerdy SEO Tracker的脚本文件实施供应链投毒。受害网站涉及美国化工行业协会、欧洲极右翼政党及保加利亚军事相关站点。注入脚本会采集访客浏览器与设备属性，随后分发平台定制的N-day漏洞利用链，针对iOS 16.7设备利用CVE-2025-43529与CVE-2024-27834窃取Cookie；针对iOS 18.5设备尝试由CVE-2025-43529、CVE-2026-20700等5个漏洞组成的DarkSword利用链，入侵成功后可窃取短信、iMessage、邮件、WhatsApp与Telegram数据库、iCloud钥匙串、Wi-Fi密码、通话记录及照片等完整设备数据；针对使用Chrome 139至145版本的Android设备则利用CVE-2026-3910与CVE-2025-27038实现远程代码执行与权限提升，投递AndroSnitch载荷窃取Chrome数据与Wi-Fi密码。报告指出，该行动凸显国家背景APT组织持续复用DarkSword等商业监控厂商的移动漏洞利用框架的攻击趋势，而成套N-day漏洞利用链也显著降低了移动端攻击的成本与技术门槛。

**链接：https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html**

04

APT组织Gorbag利用WinRAR漏洞投递BeautyStealer窃密程序，持续针对乌克兰执法与国防部门实施网络攻击

近日，安全研究人员披露，APT组织Gorbag至少自2025年2月起活跃，专门针对乌克兰目标开展情报窃取活动，重点覆盖执法与司法机构、前线附近地方行政部门及国防领域。该APT组织早期使用PSSW100AVB衍生的Prime ReverseShell反向Shell，核心工具为C/C++编写的GIFTEDCROOK窃密程序，可从Chrome、Edge、Firefox等浏览器窃取Cookie、浏览历史与认证数据，自2025年12月底起已完全转向使用其演进版本BeautyStealer，该变种可额外采集OpenVPN配置、Office文档、压缩包、邮件、KeePass数据库及RDP配置等文件，并将数据打包后经Telegram或基于FastAPI的自建C2服务器回传，任务完成后自行删除，不维持持久化访问。

**链接：https://thehackernews.com/2026/11/russia-aligned-gorbag-hackers-exploit.html**

02

网络动态

01

美国CISA启动2026年“关键基础设施安全与韧性月”活动

11月2日，据美国网络安全和基础设施安全局（CISA）官网消息，CISA当日正式启动2026年“关键基础设施安全与韧性月”活动。今年的活动与特朗普政府的《国家韧性战略》相衔接，背景是超级智能等快速发展的技术带来新的、不断演变的威胁。活动期间，CISA将重点推广四项实践，即识别最重要的系统及其依赖的外部服务、了解组织面临的关键风险、制定明确的响应与恢复计划，以及根据实际经验跟踪进展并更新计划。

**链接****：https://www.cisa.gov/news-events/news/cisa-kicks-critical-infrastructure-security-and-resilience-month-2026**

02

澳大利亚关键基础设施安全中心更新风险管理计划指南，强化网络与供应链管控要求

澳大利亚关键基础设施安全中心（CISC）近日发布更新版《关键基础设施风险管理计划》（CIRMP）指南及配套概要文件，敦促责任实体对照审视其关键基础设施资产与风险管理安排。该指南依据《2018年关键基础设施安全法》第2A部分制定，要求责任实体采取“全危害”方法，围绕网络与信息安全、凭据失陷、横向移动、人员、供应链、物理安全与自然灾害等七类危害向量识别重大风险，并在“合理可行”范围内予以消除或缓解，同时对风险评估与控制决策形成文档记录。指南明确，适用增强版要求的实体须达到所选网络安全框架成熟度二级，对已识别系统实施抗钓鱼多因素认证，隔离关键系统以确保其在其他系统恢复期间可独立运行至少三个月，绘制供应链图谱并评估主要供应商，并对关键岗位人员实施更严格的适任审查。指南还要求实体至少每24个月审查一次CIRMP，并在财年结束后90天内向监管机构提交经治理机构批准的年度报告，违规可能面临150个罚款单位的民事处罚。

**链接：https://industrialcyber.co/critical-infrastructure/australias-cisc-sharpens-critical-infrastructure-risk-guidance-urges-stronger-cyber-and-supply-chain-controls/**

03

通用动力信息技术公司扩大与AppGate零信任合作，强化美国联邦政府网络韧性与跨机构安全访问

通用动力旗下业务单元通用动力信息技术公司（GDIT）宣布与零信任厂商AppGate签署战略合作协议，扩大双方合作，面向美国联邦政府提供零信任解决方案并强化网络韧性。GDIT将把AppGate的零信任网络访问能力整合进其Everest零信任解决方案，以支持企业级、跨机构及战术边缘任务的快速部署。此次合作聚焦四个优先方向：一是跨机构安全信息共享，为分布式环境中的多机构提供受控快速访问；二是战术与边缘作战，支持有限或无连接的争议、偏远环境下的安全数据共享与协同；三是运营技术防护，强化国家安全关键基础设施与工业控制系统防御；四是AI赋能零信任，将人工智能应用于网络数据处理以加速威胁响应与任务决策。

**链接：https://industrialcyber.co/news/gdit-taps-appgate-zero-trust-technology-to-strengthen-federal-cyber-resilience-and-secure-interagency-access/**

04

美国海军推进“海军创新单元”计划，借直接委任军官项目引进私营部门技术人才

美国海军人力与预备役事务助理部长Ben Kohlmann在由FedScoop主办的Datadog威胁应对论坛上表示，海军正推进一项通过直接委任军官项目将私营部门技术人才引入预备役部队的计划。据介绍，海军正启动名为“海军创新单元”（Navy Innovation Unit）的早期项目，首批挑选15名已在硅谷高水平机构任职的预备役人员投入攻关难题，并初步匹配10名直接来自私营部门的创始人与首席执行官，以少校或中校（04、05）军衔直接入役，授权其深入海军体系推动改进。根据海军今年6月发布的新闻稿，该单元重点招募数据科学、人工智能与机器学习、机器人自主与无人系统、量子技术、软件工程、DevOps、云架构、网络安全、攻防网络作战、先进通信与网络工程等领域的专业人才，相关招募信息在社交媒体发布后，10个名额收到约300份申请，海军希望借此构建一支可在政府与私营部门间灵活流动、兼具两方背景的关键人才层。

**链接****：https://defensescoop.com/2026/11/05/navy-innovation-unit-private-sector-technology-talent/**

05

美国CISA、FBI等五部门联合发布事实说明，警示针对工业制冷与冷链监控系统的网络威胁

11月5日，据美国网络安全和基础设施安全局（CISA）官网消息，CISA联合联邦调查局（FBI）、卫生与公众服务部（HHS）、农业部（USDA）和交通部（DOT）发布一份事实说明，警示各组织当前存在针对工业制冷与冷链监控系统的持续性网络威胁活动，医疗卫生化工、食品与农业、交通运输等关键基础设施行业广泛使用此类系统。据介绍，全球范围内恶意网络行为者正瞄准零售杂货店与冷藏设施中未修补或暴露于互联网的电子温度控制器和商用制冷控制器的漏洞与安全弱点，一旦利用成功，攻击者可篡改温度设定，可能引发火灾隐患、库存损失及设备使用寿命受损等物理影响。同时，该事实说明给出的防护建议包括：将控制系统设备从互联网隔离、更改默认口令并强化口令策略、及时安装补丁并保持设备系统更新、识别并淘汰替换厂商已停止支持的遗留设备。CISA网络安全代理执行助理主任Chris Butera表示，CISA正与政府、行业及国际伙伴密切协作追踪该威胁活动，所有依赖制冷与监控系统的组织均应视自身为潜在目标，尽快弥补已知安全缺口。

**链接****：https://www.cisa.gov/news-events/news/cisa-fbi-hhs-usda-and-dot-urge-critical-infrastructure-strengthen-industrial-refrigeration-and-cold**

03

漏洞资讯

01

开源AI工作流构建工具Langflow存在4个安全漏洞

近日，安全研究人员发现开源AI代理及工作流构建工具Langflow存在4个安全漏洞。其中，第一个是身份验证绕过漏洞（CVE-2026-93680），允许未经身份验证的远程攻击者绕过安全限制；第二个是代码生成控制不当漏洞（CVE-2026-110186），允许未经身份验证的攻击者执行任意代码；第三个是命令执行漏洞（CVE-2026-110193），允许低权限用户诱使智能体助手生成或提交组件代码，在服务器上执行操作系统命令；第四个是凭据保护不足漏洞（CVE-2026-110192），可导致敏感信息泄露。目前，公开渗透测试框架Metasploit中已有模块涉及CVE-2026-93680，用户可通过将版本升级至1.13.0的方式修复上述漏洞。

**链接：https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html**

02

Debian与Ubuntu包管理器APT存在签名校验绕过漏洞

近日，安全研究人员发现Debian与Ubuntu所用APT包管理器存在签名校验绕过漏洞（CVE-2026-109518）。当HTTP重定向使两个不同的软件包下载指向同一地址时，APT可能将二者合并，且在恢复中断下载时对文件处理不当，导致软件包在通过签名验证后仍存在被替换的短暂窗口，最终安装的是攻击者篡改的版本，进而实现任意代码执行。目前，用户可通过版本升级修复上述安全漏洞。

**链接：https://cybersecuritynews.com/debian-apt-flaw-lets-hackers-hijack-updates/**

03

OpenSSH存在认证绕过漏洞

近日，安全研究人员披露一个涉及OpenSSH与musl C库的认证绕过漏洞，代号“sshole”，攻击者仅需提交超长密码，即可登录Alpine Linux等musl系发行版上已禁用密码认证的账户。该漏洞自2016年起便已存在，不影响拥有有效密码哈希的账户，利用需同时满足系统基于musl（如Alpine Linux、OpenWrt、Buildroot、Yocto）、PAM认证关闭（Alpine openssh-server包默认如此）、SSH密码认证开启等条件，另外，使用glibc的Debian、Ubuntu、Fedora及启用PAM的系统也不受影响。研究人员警告，Alpine Linux官方AWS与Azure云镜像默认的“alpine”账户受此影响且具备免密doas权限，可能被用于获取root权限。目前，用户可通过将软件版本升级至OpenSSH 10.6p2或更新版本的方式修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/**

04

ChatGPT锁定模式存在绕过漏洞，可在无需用户交互情况下窃取聊天数据

近日，安全研究人员发现OpenAI ChatGPT锁定模式（Lockdown Mode）存在绕过漏洞。锁定模式于2026年6月推出，作为可选设置，通过限制外发网络请求降低提示注入引发的数据外泄风险。该安全漏洞源于ChatGPT代码块内的HTML页面预览功能，预览内容虽被置于嵌套沙箱框架中，且直接打开新窗口的尝试会被拦截，但底层沙箱权限仍允许弹窗并使其逃逸沙箱。攻击者通过在渲染页面内再创建一层嵌套框架，即可调用未受限制的弹窗函数，由此打开的内容不再受沙箱约束，从而绕过锁定模式防护。研究人员表示，攻击者可借助特制提示词、恶意GPT或共享对话触发该漏洞，实现静默窃取聊天数据、钓鱼及投递恶意载荷，在ChatGPT桌面应用中甚至可以零点点击数据外泄。同时，由于弹窗内容完全受攻击者控制，还可伪装成ChatGPT更新提示等诱饵诱导用户下载恶意软件。目前，OpenAI已于2026年9月18日修复该漏洞，但该案例表明AI模型之外的应用功能缺陷同样可能削弱AI安全控制，AI安全防护的强度取决于其所处的整体应用环境。

**链接：https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html**

05

Android系统存在GhostMap漏洞

近日，安全研究人员披露了一个代号“GhostMap”的Android漏洞，攻击者可借助无需任何权限、仅需安装即可生效的特制应用，使设备陷入持续启动循环，造成持久性拒绝服务。该漏洞源于两个Android库对ZIP压缩方式的解释不一致，致使畸形APK文件可绕过大小校验，被映射到文件实际内容之外的未分配内存区域，任何读取该条目的进程都会因SIGBUS信号而崩溃。研究人员构造了一款不含可执行代码、安装时不申请权限且无需启动的演示应用，其内置资源会在安装后被核心系统服务SystemServer自动读取，由此触发崩溃并不断重启、重复读取，形成无限循环。在搭载Android 17、安装8月5日安全补丁的Pixel 10设备上测试显示，安装约1秒后即开始崩溃，正常模式下循环110次、安全模式下72次，用户亦无法借助安全模式排障恢复。目前仅可通过恢复出厂设置（将清除全部本地数据）或在已开启调试选项的前提下经ADB在系统崩溃前删除畸形文件予以消除。安全研究人员于8月20日向谷歌报告该问题，收到“不予修复（无法复现）”答复，8月25日补充提交后谷歌仍认定其不属于安全更新范围，但在后续更新中予以考虑。此外，阻断此类攻击的唯一时机在安装阶段，第三方安全工具可提示风险但无权限阻止安装，相关用户应提高安全意识，慎防第三方应用程序安装，以降低安全风险。

**链接：https://www.bleepingcomputer.com/news/security/ghostmap-android-flaw-lets-malicious-app-trigger-persistent-boot-loop/**

06

Ruby on Rails Active Storage存在高危漏洞

近日，Ruby on Rails团队发布公告披露Active Storage组件存在安全漏洞，源于ImageMagick依据文件内容而非文件名选择编码器，部分编码器会对图片内引用的其他文件执行操作，而Active Storage此前未对这些编码器加以限制，且图片分析器在文件附加时即自动运行。未经认证的攻击者仅需上传特制图片即可使服务器写入文件，若应用使用Disk存...