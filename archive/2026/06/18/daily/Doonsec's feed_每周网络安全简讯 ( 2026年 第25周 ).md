---
title: 每周网络安全简讯 ( 2026年 第25周 )
url: https://mp.weixin.qq.com/s/4kIuWXVelhkaXpd8B0ZgIw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:01:34.637243
---

# 每周网络安全简讯 ( 2026年 第25周 )

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qyzTicOO6WeWU1njHDZibBickCas3zrYZYjibbnbNXyHgku7qbbic9iaLw1KnxyCkjVI9om18E2KGV8WhFsj6ibXFHzjVPd1hy75w4ga6ENdn2V2No/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第25周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年6月13日至2026年6月18日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计19条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织APT37利用NarwhalRAT恶意程序对韩国目标用户实施网络攻击

近日，安全研究人员监测发现APT组织APT37利用新型恶意程序NarwhalRAT对韩国用户实施定向网络攻击。此次攻击活动以伪造微软安全团队名义的钓鱼邮件为起点，谎称用户账户存在异常并反复生成一次性验证码，诱导用户查看附件。一旦用户点击附件中的恶意快捷方式（.lnk）后，系统在打开正常诱饵文档的同时即被植入NarwhalRAT恶意程序载荷。经分析发现，NarwhalRAT具备键盘记录、屏幕截图、麦克风录音、USB设备文件窃取、远程命令执行等30余项功能，并采用数据本地暂存、定时批量外传的方式规避实时网络检测。安全研究人员建议称，用户应在文件检测基础上进一步强化基于行为的检测能力，以防范后续变种攻击。

**链接：https://biz.chosun.com/jp/jp-it/2026/06/15/DR2D55TICREXNJDSG7DDTLKGSM/**

02

APT组织Fancy Bear转向劫持家用路由器与滥用云服务，构建高隐蔽通联渠道

近日，安全研究人员发现APT组织Fancy Bear正在对其攻击基础设施进行结构性调整，放弃传统租用的虚拟专用服务器，转而劫持家用路由器、消费级设备及边缘设备搭建难以追踪的“影子网络”，使攻击流量混入正常互联网活动。在战术层面，Fancy Bear通过代号为FrostArmada的网络攻击行动，控制MikroTik、TP-Link等路由器并篡改DNS设置，借此静默窃取Microsoft 365等服务凭据与OAuth令牌，同时利用合法云存储API构建隐蔽通联渠道，灵活轮换云后端以规避安全检测。此外，Fancy Bear还转向部署“用后即弃”的短生命周期单一用途工具，以及依靠实时AI模型动态生成攻击指令的信息窃取工具LameHug，攻击手法持续演进。安全人员建议称，相关组织应及时更新路由器固件、更改默认凭据、关闭闲置的远程管理功能，并对云服务强制实施多因素认证、定期审计OAuth令牌权限，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/fancy-bear-hackers-abuse-edgerouters-and-cloud-services/**

03

APT组织Ghostwriter对波兰目标用户实施网络攻击

近日，安全研究人员发现APT组织Ghostwriter正在持续开展针对波兰用户Gmail账户的网络钓鱼活动。此次攻击活动中，该APT组织通常伪装成Gmail安全团队或邮件管理员，使用“检测到新设备登录”“账户存在可疑活动”“违反服务条款将被封禁”等主题诱导受害者点击链接，跳转至仿冒Gmail登录页面，窃取邮箱账号、密码及双因素认证验证码。在攻击流程上，攻击者会通过专门注册的钓鱼域名、Netlify等网站托管平台子域名，以及被入侵的波兰机构网站部署虚假登录面板，并结合密送（BCC）投递、重复发送和压缩处置时间等方式提升诱导成功率。一旦攻击成功，该APT组织即可利用获取的登录凭据自动尝试登录，并进一步搜集联系人、敏感文件及关联社交媒体账户信息。安全人员建议，相关用户应重点核验登录页面域名，避免通过邮件链接进入账号认证页面，并对异常登录、OAuth授权、账户恢复方式及关联应用权限进行定期检查。

**链接：https://cert.pl/en/posts/2026/06/UNC1151-gmail-campaign/**

04

APT组织CNC对政府、军工等行业目标实施网络攻击

近期，360安全大脑监测到具有南亚地区政府背景的APT组织CNC发起多起定向钓鱼攻击活动，其攻击目标涵盖政府、军工、教育、科研、医疗、媒体等重点行业。攻击者沿用“招聘”“简历”为话题的经典社会工程学手段，通过钓鱼邮件投递恶意压缩包，内嵌采用双后缀伪装成PDF文档的可执行文件，诱导用户点击运行。该样本获取主机信息后，从代码中解密出隐藏链接，解密流程为字符串反转、Base64解码、异或及二次Base64解码，进而连接服务器下载诱饵文档与VBS脚本，并最终下载远控木马。核心载荷静态链接OpenSSL实现加密通信，与C2服务器完成TLS握手后发送上线包，可执行文件上传及CMD命令下发等远控操作。经研判，本次活动在诱饵话题、攻击链路、载荷代码序列及加密通信方式等方面均与该组织既往攻击高度一致，结合受害目标行业特征，确认此次活动由APT组织CNC发起。该组织持续活跃，相关单位需加强对钓鱼邮件及伪装文档的防范。

**链接：[【查看原文】](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247508669&idx=1&sn=045cca89facb1bc6be4e565bc6fa09d8&scene=21#wechat_redirect)**

02

网络动态

01

美国总统特朗普签署第12号国家安全总统备忘录《针对国家安全系统的网络安全国家政策》

美国总统特朗普签署第12号国家安全总统备忘录《针对国家安全系统的网络安全国家政策》，旨在为美国国家安全系统构建更加主动、适应性强和具备韧性的网络安全生态体系，推动国家安全系统治理现代化，以应对2026年及以后的网络安全挑战。该备忘录明确国家安全系统治理架构、权限划分、角色责任和问责机制，重新设立并现代化改造国家安全系统委员会，要求在所有国家安全系统中建立统一网络安全基本要求，强化国防部、情报界和联邦民事行政部门之间的协调与责任落实。同时，备忘录授权美国国家安全局局长担任国家安全系统国家管理者和密码权威，负责技术咨询、事件响应建议、密码能力建设、安全评估、跨域解决方案、加强联邦文职机构NSS安全监管及网络安全协作等工作。备忘录还要求相关机构限期完成政策修订、旧规清理、事件报告标准更新、系统清单编制和人员派遣等任务，并将第14306号行政命令有关要求延伸至国家安全系统，重点围绕云安全配置、共享服务利用和非密语音视频通信能力建设等领域推进落实。整体看，该备忘录意在通过重塑国家安全系统网络安全治理机制、强化国家安全局统筹作用和推动跨部门协同，提升美国政府最敏感信息系统及军事、情报支撑系统的整体防护能力。

**链接****：https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-12/**

02

澳大利亚国防军网络司令部拟参加“澳大利亚之盾”演习，强化关键基础设施防护与跨部门协同

澳大利亚国防军将于7月3日至19日在昆士兰北部和西澳大利亚举行“澳大利亚之盾”（Austral Shield）全军演习，检验应对国内威胁、保护关键基础设施及国家资源的能力。此次演习中，国防军网络司令部将与陆军、海军、空军及太空司令部联合行动，超过1500名人员与州、联邦机构代表共同参与。联合集体训练总干事菲利帕·海准将表示，此类演习有助于政府机构提升威胁应对准备度，并在高压情境下协同作战，确保国防军保持战备、灵活与一体化能力。

**链接：**https://www.cyberdaily.au/security/13756-adf-s-cyber-command-to-take-part-in-exercise-austral-shield

03

美国反情报机构拟引入人工智能加速安全审查

美国国防反情报与安全局（DCSA）计划运用人工智能工具，加快对拟代表政府从事敏感工作的个人和企业的安全许可审查。该局分析与创新主管马克·内默在弗吉尼亚州举行的国防科技峰会上表示，先进AI可将部分审查流程从数月缩短至数小时。受国会近期批准的采购改革影响，DCSA预计每年须处理约4.3万份许可申请。内默强调，AI将用于辅助作出细微判断并整理证据，最终决策仍交由人类高级分析师把关。

**链接****：https://www.nextgov.com/defense/2026/06/us-counterintelligence-agency-looks-ai-accelerate-background-checks/414218/**

04

美国海岸警卫队发布扩展性网络安全指南，将风险评估确立为海上韧性核心

美国海岸警卫队发布了额外的政策与实施指导，协助受监管的海事实体落实网络安全法规，为悬挂美国国旗的船只、设施及外大陆架（OCS）设施设定基线网络安全要求，以提升海运系统的安全性与韧性。新指南明确将网络安全评估（CSA）作为持续成熟流程的基础性第一步，要求据此识别可能导致运营中断或运输安全事件的漏洞、威胁及运营依赖关系，并引入与NIST网络安全框架对齐的可选风险过滤流程，以判定哪些资产应被正式认定为关键IT或OT系统。同时，根据指定的相关法规，船舶及设施所有者须维护经批准的网络安全计划、指定全天候待命的网络安全官员（CySO）、开展评估与演练、实施网络事件响应计划，并按要求向国家响应中心报告应报告事件。此外，海岸警卫队还配套发布了网络安全培训核查工作辅助工具，以规范检查员在例行检查中的合规评估方式，推动法规在整个海事生态系统中的一致执行。

**链接****：**https://industrialcyber.co/regulation-standards-and-compliance/us-coast-guard-issues-expanded-cybersecurity-guidance-making-risk-assessments-central-to-maritime-resilience/

05

比利时在Cyber Europe 2026演习中检验网络危机应对能力

比利时网络安全中心披露，该机构近日参加由欧盟网络安全局协调、成员国共同组织的Cyber Europe 2026大型网络危机演习，重点围绕铁路和海运运输领域开展跨国网络危机处置测试。此次演习并非针对理论风险，而是结合比利时现实威胁态势设计情景。数据显示，2025年比利时组织向该中心提交635起事件通知，同比增长近70%，其中556起与网络安全相关，账户失陷、勒索软件、DDoS攻击、网络钓鱼、漏洞利用和供应链事件仍持续施压，在NIS2定义的关键组织中，交通运输已成为受影响较重的行业之一。演习期间，比利时重点检验了新通过的《国家网络应急计划》下的危机响应流程，包括事件报告接收、分诊研判、跨团队跟进、信息共享和决策协调等环节，并模拟国家危机架构与欧洲层面机制的联动。此次演习还测试了比利时与CSIRTs Network、EU-CyCLONe及欧盟网络危机管理蓝图之间的衔接能力，以综合提升重大网络事件下关键服务保护和欧洲协同响应水平。

**链接****：**https://ccb.belgium.be/news/belgium-tests-cyber-crisis-response-during-cyber-europe-2026

06

MITRE推出Grid Watch模拟器提升电网OT网络安全实训能力

近日，MITRE Caldera for OT团队推出一款名为Grid Watch的纯软件化DNP3外站模拟器，旨在降低电力行业OT网络安全培训和对手仿真的硬件门槛。该平台可在普通笔记本电脑上运行，模拟小型配电场景，覆盖断路器、备用发电机、母线电压监测和功率缺口追踪等关键对象，并与Caldera for OT直接集成，支持围绕DNP3协议开展侦察、未授权控制和多阶段电网扰动等演练。相关进展表明，MITRE正持续通过Wildcat Dam、Aloha Water Treatment Plant、HVACSim和Grid Watch等软件化仿真环境，推动低成本、可复现的OT网络攻防训练体系建设。

**链接****：**https://medium.com/@mitrecaldera/caldera-for-ot-grid-watch-a-virtual-dnp3-electrical-grid-sandbox-761e8c83ab77

03

漏洞资讯

01

Splunk Enterprise存在安全漏洞

近日，安全研究人员发现Splunk Enterprise存在安全漏洞（CVE-2026-20253），是由PostgreSQL sidecar服务端点缺乏身份验证控制所导致，允许未经身份验证的攻击者通过相关服务端点创建任意文件。漏洞影响Splunk Enterprise 10.0.0至10.0.6等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html**

02

开源AI网关LiteLLM存在3个安全漏洞

近日，安全研究人员发现开源AI网关LiteLLM存在3个安全漏洞。其中，第一个安全漏洞是授权绕过漏洞（CVE-2026-47101），允许非管理员权限的普通用户创建可访问所有路由的密钥；第二个安全漏洞是权限提升漏洞（CVE-2026-47102），允许普通权限用户通过更改自身用户名的方式，将自身权限提升为代理管理员；第三个安全漏洞是沙箱逃逸漏洞（CVE-2026-40217），允许攻击者通过利用自定义代码防护机制缺陷，在目标设备上编译并运行管理员提供的Python代码。目前，用户可通过将版本升级至v1.83.14-stable或更高版本的方式修复上述安全漏洞。

**链接：https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html**

03

Cisco Catalyst SD-WAN Manager存在路径遍历漏洞

近日，安全研究人员发现Cisco Catalyst SD-WAN Manager存在路径遍历漏洞（CVE-2026-20262），是由Web用户界面UI文件上传组件输入数据验证机制存在缺陷所导致，允许攻击者通过向特定API端点发送恶意HTTP请求的方式，在目标用户设备底层操作系统上创建或覆盖任意文件，甚至提升自身访问权限至root。漏洞影响20.9.9.1及更早版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://ccb.belgium.be/advisories/warning-cisco-issues-security-updates-actively-exploited-sd-wan-vulnerability-patch**

04

Linux Kernel net/sched act\_pedit存在本地权限提升漏洞

近日，安全研究人员发现Linux Kernel net/sched act\_pedit存在本地权限提升漏洞（CVE-2026-46331），该漏洞源于tcf\_pedit\_act()函数在处理数据包编辑操作时存在缺陷所导致，允许本地普通用户获取目标设备系统root最高权限。漏洞影响v5.18 <= Linux Kernel < v7.1-rc7等版本，目前用户可通过内核版本升级修复上述安全漏洞。

**链接：https://access.redhat.com/security/cve/cve-2026-46331**

05

Microsoft 365 Copilot Enterprise Search存在安全漏洞

近日，安全研究人员发现Microsoft 365 Copilot Enterprise Search存在名为SearchLeak的安全漏洞（CVE-2026-42824），允许攻击者通过诱导用户点击指向真实microsoft.com域名的链接，在无需输入密码、无需二次确认的情况下，触发Copilot检索并外传用户可访问的数据。目前，该漏洞已被微软公司进行后台修复，用户可通过超链接检查、异常Copilot异常行为报告等方式进一步降低遭受攻击的风险。

**链接：https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html**

04

木马病毒

01

DPAPISnoop工具新增CREDHIST提取功能，加剧Windows凭据离线破解风险

近日，LRQA安全团队对开源工具DPAPISnoop进行了功能增强，使其能够解析Windows系统中的CREDHIST凭据历史文件，并将其转换为可离线破解的哈希格式。CREDHIST文件以密钥链形式存储用户历次更改的密码，长期未受到攻防研究的充分关注，此次更新可将相关条目导出为带有特定前缀的哈希值，配合新引入的两种Hashcat模式直接进行GPU离线暴力破解。一旦某条目被攻破，即可回溯解锁链中其他条目，从而重建用户完整的密码历史。该研究虽不构成系统漏洞，但揭示了攻击者在获得文件系统访问权限后，可借助合法Windows机制获取凭据，进而加速横向移动与权限提升，对企业内网安全构成潜在安全威胁。

**链接：**https://cybersecuritynews.com/dpapisnoop-tool-extracts-credhist-hashes/

02

可窃取210余款应用凭据的OnyxC2新型恶意程序被披露

近日，安全研究人员监测发现一款名为OnyxC2的新型恶意程序在网络犯罪地下市场流通。该工具以“恶意软件即服务”模式按每月250美元打包出售，配备Web控制面板、载荷生成器及分级定价等机制，运营高度商业化，显著降低了攻击门槛。OnyxC2单次运行即可覆盖210余款应用及浏览器扩展，涉及多款主流浏览器、密码管理器、加密货币钱...