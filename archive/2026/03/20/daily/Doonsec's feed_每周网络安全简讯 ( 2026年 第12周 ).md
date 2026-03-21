---
title: 每周网络安全简讯 ( 2026年 第12周 )
url: https://mp.weixin.qq.com/s/ygZrUgGbs6pC1hr_Uf6q5g
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:04:36.421987
---

# 每周网络安全简讯 ( 2026年 第12周 )

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qyzTicOO6WeUVopkPCtSu0Q0GqToaLgUW0wcjdiaL3G3yG8o48e9w5FHiaqy95q59Tqc983qbNnNvqHDiafTPo9opYQVsPa4l3cibWiczjohchvxA/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第12周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器中沉浸阅读

2026年3月14日至2026年3月20日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计20条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织Konni对韩国目标用户实施网络攻击

近日，安全研究人员监测发现APT组织Konni采用鱼叉式网络钓鱼攻击方式，诱骗用户点击恶意LNK文件实施初始渗透入侵。攻击成功后，该APT组织将会在用户设备中潜伏，植入EndRAT、RftRAT、RemcosRAT等各类恶意程序载荷，长期窃取用户敏感信息并对用户设备实施持久性远控。同时，该APT组织还会对用户设备上的KakaoTalk平台实施未授权访问，在平台好友列表中筛选后进行恶意载荷的二次分发，将现有受控设备转化为新的传播渠道，以此扩大攻击感染面。

**链接：https://www.genians.co.kr/en/blog/threat\_intelligence/kakaotalk?hsCtaAttrib=324686917354**

02

APT组织MuddyWater对中东地区目标用户实施网络攻击

近日，安全研究人员披露了APT组织MuddyWater在过去一年的网络攻击行动情况。据称，该APT组织攻击对象涵盖中东及全球其他战略地区的能源、海事、金融、航空和电信等领域关键基础设施，且正由早期“大规模、低复杂度”的作战方式，转向更具隐蔽性、持续性和定向性的攻击模式。技术层面上，该APT组织正在显著提升武器化能力，采用Rust语言开发后门与远控程序，并引入AI辅助编码以加快恶意软件迭代，其工具链包括BlackBeard、UDPGangster、LampoRAT、GhostBackDoor和Nuso等后门程序载荷，具备反分析、长期驻留、命令执行、数据窃取和多阶段载荷投递能力，均具有较强的规避安全设备检测能力。总体来看，MuddyWater正加快自身攻击技术迭代，具备较强的经济间谍活动与攻击效能，存在较大潜在安全威胁。

**链接：https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/**

03

疑似APT组织APT28对乌克兰目标用户实施网络攻击

近日，安全研究人员披露称，疑似APT组织APT28利用Zimbra协作套件中的存储型XSS漏洞，在无需恶意附件、可疑链接或宏的情况下，对乌克兰航运、海事目标用户设备实施入侵。攻击成功后，恶意脚本便会在浏览器上下文中静默执行，继承合法会话权限，进而窃取登录凭证、会话令牌、备份双因素认证恢复码、浏览器保存密码等敏感信息，进而通过DNS与HTTPS双通道方式对所窃数据进行外传。

**链接：https://www.seqrite.com/blog/operation-ghostmail-zimbra-xss-russian-apt-ukraine/**

02

网络动态

01

波兰核研究中心遭受黑客攻击

近日，波兰核研究中心（NCBJ）声称，某黑客组织针对其IT设施实施网络入侵，在攻击过程中被安全人员响应阻断，暂未对MARIA反应堆正常运行造成影响，波兰当局将此次网络入侵事件与伊朗黑客组织进行关联。目前，NCBJ已通知波兰相关部门启动联合调查，且内部安全团队正式调整为高度戒备状态，以应对后续网络安全威胁。

**链接****：https://www.bleepingcomputer.com/news/security/polands-nuclear-research-centre-targeted-by-cyberattack/**

02

美国能源部将发布首个网络安全战略计划

美国能源部正推进发布其网络安全战略计划，旨在系统阐明该部门在当前威胁环境下强化能源电网防护的总体思路。美国能源部副部长兼网络安全、能源安全与应急响应办公室（CESER）主任亚历克斯·菲茨西蒙斯表示，该计划将作为对最新国家网络战略的配套补充，重点围绕提升能源行业安全性与韧性展开，尤其强调在关键基础设施面临网络与物理复合威胁背景下，增强防护、响应与恢复能力。同时，该计划还在提升政府与私营部门协作力度、基于人工智能的网络安全防护、关键能源基础设施加固及韧性建设等方面提出更高要求，以提升美国能源部门应对新兴网络安全威胁和各类安全事件的综合防护能力。

**链接：**https://therecord.media/energy-department-set-to-release-first-ever-cyber-strategy

03

欧盟理事会发布应对混合威胁的综合战略文件

3月16日，欧盟理事会发布战略文件指出，当前国家和非国家行为体持续实施针对欧盟及其成员国、伙伴国的混合行动，具体表现包括针对关键基础设施的破坏、恶意网络活动、外国信息操纵与干预、选举干预等，这些行动通常具有隐蔽性、组合性和持续性，目的在于削弱欧盟安全稳定、破坏民主制度、撕裂社会共识并干扰政治决策。因此，该战略文件重申将综合运用“混合工具箱”“网络外交工具箱”及相关立法、限制性措施等各类政策手段，全面强化对混合威胁的预防、威慑和应对能力，以提升欧盟应对混合威胁的能力。

**链接****：https://www.consilium.europa.eu/en/press/press-releases/2026/03/16/council-adopts-conclusions-on-advancing-the-eu-s-capacity-to-counter-hybrid-threats/**

04

莫斯科推行“白名单”制度限制互联网访问，旨在应对网络中断

近日，在持续网络中断背景下，俄罗斯正加快推进对互联网访问的选择性管控，开始启用一种“白名单”机制，在移动互联网受限期间，仅允许访问经政府预先批准的俄本土网站和服务，包括社交媒体、电商平台、出租车与配送应用、电信服务及政府网站等。从技术路径看，“白名单”机制主要依托深度数据包检测（DPI）技术实现，通过运营商对流量进行精细过滤，在屏蔽大部分互联网活动的同时保留特定平台访问权限。纳入“白名单”的企业还需满足一系列本地化和可控性要求，包括通过俄罗斯本土基础设施路由流量、在境内部署服务器，并确保用户无法隐藏IP地址。这表明，相关制度并非单纯的应急通信保障方案，而是与俄罗斯长期推进“主权互联网”（Runet）建设目标高度一致，旨在增强在特殊安全环境下对网络空间的自主运行与管控能力。

**链接****：**https://therecord.media/moscow-seeks-to-limit-internet-to-state-approved-sites

05

美国纽约推出关键水基础设施网络安全法规

近日，美国纽约州推出关键水基础设施网络安全法规，实施针对饮用水和污水系统的新网络安全监管要求，并同步推出总额250万美元的“SECURE”专项资助计划，以提升关键水基础设施的网络防御和运行韧性。该举措由州长霍楚尔推动，一方面通过法规为水务运营单位设定最低网络安全标准，另一方面通过资金和技术支持帮助地方落实整改。其中，资助项目可为公用事业单位提供最高5万美元的网络安全评估资金，以及最高10万美元的安全升级改造资金，重点支持系统加固、漏洞整改和防护能力建设，以应对日益复杂的网络威胁。

**链接****：**https://industrialcyber.co/utilities-energy-power-water-waste/new-york-introduces-cybersecurity-rules-2-5-million-grant-program-to-strengthen-water-infrastructure-defenses/

06

日本政府允许自卫队开展“主动网络防御”行动

日本政府近日决定，自10月1日起允许自卫队在法定授权框架下开展“主动网络防御”行动，标志着其网络安全政策由传统防御向更具干预性的处置模式进一步演进。日方称，此举是基于当前网络空间面临二战以来最复杂的国家安全环境，以及全社会数字化加速推进背景下作出的政策调整。根据相关安排，日本网络管理委员会将有权对网络行动启动申请进行审查批准，经授权后警方和自卫队可对用于实施网络攻击的基础设施采取“攻击并瘫痪”措施，同时兼顾公民隐私保护。

**链接****：**https://www.theregister.com/2026/03/18/japan\_proactive\_cyber\_defense\_enabled/

07

俄罗斯拟立法监管人工智能

俄罗斯拟推进人工智能专项立法，通过联邦法律框架引入风险导向监管模式，依据人工智能系统对个人生活和社会运行的影响程度实施差异化约束。根据俄数字发展部公布的信息，法案重点围绕人工智能应用边界规范、公民权益保护和技术安全维护等方面展开，目前已进入公众讨论阶段，拟于2027年9月1日生效。同时，草案提出如下要求：一是对人工智能生成内容实施强制标识管理，所有AI辅助生成的视听内容附加警示标记；二是大型社交平台需核查相关标识，若缺失则应自行标注或删除内容；三是开发者应排除歧视性算法，阻断违法内容生成；四是运营方需开展安全测试并向用户说明系统局限范围；五是AI服务提供方需采取相关措施防止人工智能被非法滥用。整体来看，该法案体现出俄罗斯正加快构建兼顾安全可控、公民权利保护与技术发展的人工智能治理体系。

**链接****：**https://www.interfax.ru/digital/1078702

08

谷歌等科技巨头联合签署国际反网络诈骗协议

谷歌近日在维也纳举行的联合国全球反欺诈峰会上签署《反网络诈骗与欺诈行业协议》，并与Adobe、亚马逊、Meta、微软、OpenAI、LinkedIn、Pinterest、Target等多家国际科技与零售企业共同承诺，加强跨行业协同打击全球网络诈骗活动。该协议发布之际，网络诈骗已由零散个案演变为跨国有组织犯罪问题，对公众造成持续加剧的经济损失和心理伤害。根据谷歌披露，签署各方将整合行业能力，共享威胁情报，协调防御措施，以提升对在线诈骗活动的识别、预警和联合应对水平。与此同时，谷歌还将依托Google.org已投入的1500万美元资金，进一步扩大反诈骗技术与专业支持，推动人工智能驱动的侦测与处置能力建设。2026年，谷歌计划通过“全球信号交换”机制加强信息共享，深化与执法机构及国际合作伙伴的联动，并联合发布有关数据共享、私营部门线索移交执法机关及公共政策框架的系列指引，显示出国际科技企业正加快构建面向跨境网络诈骗威胁的协同治理体系。

**链接****：**https://blog.google/innovation-and-ai/technology/safety-security/google-industry-accord-combat-scams-fraud/

03

漏洞资讯

01

联发科Dimensity 7300芯片存在安全漏洞

近日，安全研究人员发现联发科Dimensity 7300存在安全漏洞，位于芯片Boot ROM中，允许攻击者通过在芯片启动时通过USB线连接电脑，向其施加精确时控电磁脉冲的方式，扰乱正常执行流程，进而窃取设备PIN码，解密用户数据，提取Trust Wallet、Kraken Wallet、Phantom、Base、Rabby等加密货币钱包敏感信息。目前，相关用户可通过固件补丁更新降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/mediatek-vulnerability-android-phone/**

02

Linux内核AppArmor模块存在多个安全漏洞

近日，安全研究人员发现在Linux内核AppArmor模块存在一组被称为CrackArmor的安全漏洞，相关安全漏洞自2017年便已存在，允许无特权用户绕过命名空间限制，提升自身访问权限，甚至在目标设备内核执行任意代码。目前，用户可通过将Linux内核升级至4.11及以上版本的方式修复上述安全漏洞。

**链接：https://securityaffairs.com/189487/hacking/unprivileged-users-could-exploit-apparmor-bugs-to-gain-root-access.html**

03

Wing FTP存在信息泄露漏洞

近日，安全研究人员发现Wing FTP存在信息披露漏洞（CVE-2025-47813），允许低权限攻击者获取目标用户Wing FTP服务器软件完整本地安装路径，进而可结合利用远程代码执行漏洞（CVE-2025-47812）和另一个信息泄露漏洞（CVE-2025-27889），对用户设备实施远控。漏洞影响7.4.3及更早版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://thehackernews.com/2026/03/cisa-flags-actively-exploited-wing-ftp.html**

04

Windows路由与远程访问服务管理工具存在远程代码执行漏洞

近日，安全研究人员发现Windows路由与远程访问服务（RRAS）管理工具存在远程代码执行漏洞（CVE-2026-25172、CVE-2026-25173和CVE-2026-26111），允许攻击者通过诱骗用户利用路由与远程访问服务（RRAS）向特定服务器发送请求的方式，实现远程任意代码执行。目前，用户可通过安装KB5084597补丁的方式修复上述安全漏洞。

**链接：https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-11-oob-hotpatch-to-fix-rras-rce-flaw/**

05

GNU InetUtils telnet守护进程存在安全漏洞

近日，安全研究人员发现GNU InetUtils telnet守护进程（telnetd）存在安全漏洞（CVE-2026-32746），是由LINEMODE Set Local Characters（SLC）子选项处理器存在缓冲区溢出缺陷所导致，允许未经身份验证的攻击者通过连接23端口并发送一个带有恶意SLC数据包的方式实现远程任意代码执行。目前，该漏洞尚未修复，用户可通过限制telnetd运行权限或禁用该服务的方式降低遭受攻击的风险。

**链接：https://thehackernews.com/2026/03/critical-telnetd-flaw-cve-2026-32746.html**

06

Kubernetes容器存储接口驱动存在路径穿越漏洞

近日，安全研究人员发现Kubernetes容器存储接口（CSI）驱动存在路径穿越漏洞，是由卷标识符subDir参数验证机制存在缺陷所导致，允许攻击者修改或删除目标用户NFS服务器上的未预设目录（unintended directories）。漏洞影响CSI驱动4.13.1之前的版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://cybersecuritynews.com/kubernetes-csi-driver-nfs-vulnerability/**

04

木马病毒

01

针对乌克兰实施攻击的DRILLAPP后门程序被披露

近日，安全研究人员披露了一款针对乌克兰目标用户实施攻击的DRILLAPP后门程序。经分析，该后门程序通过网络钓鱼方式进行传播，在植入用户设备后会首先将自身载荷写入到Windows启动文件夹实现自身持久性驻留，然后通过“画布指纹”（canvas fingerprinting）技术生成受控设备指纹，与所窃取的用户麦克风音频、摄像头视频、屏幕截图等敏感信息整合，进而通过Pastefy获取C2服务器通联地址后进行文件上传。

**链接：https://thehackernews.com/2026/03/drillapp-backdoor-targets-ukraine.html**

02

Payload勒索软件被披露

近日，安全研究人员披露了一款名为Payload的新勒索软件，自2026年2月份就十分活跃，已对多个国家的医疗、房地产、能源、电信等行业组织构成威胁。经分析，该勒索软件与2021年泄露源代码的Babuk勒索软件较为相似，且在原有代码上进行了针对性强化，核心加密机制采用Curve25519椭圆曲线密钥交换与ChaCha20流密码相结合的方式，为每个文件生成独立密钥，对大于2G的用户文件则采用间隔块方式实施20%加密策略，同时兼顾文件加密效率和对用户设备的破坏效果。此外，该勒索软件还具备较强的反取证与防御规避特征，通过修改Windows事件追踪相关函数干扰端点检测安全机制，在加密完成后清除系统事件日志和自身文件，尽可能减少落地痕迹，进一步提升了安全人员的分析与溯源难度。

**链接：**https://cybersecuritynews.com/new-payload-ransomware-uses-babuk-style-encryption/

03

针对iOS用户实施攻击的DarkSword恶意工具包被披露

近日，安全研究人员披露了一款名为DarkSword的新型恶意工具包，内置6个漏洞利用组件，允许攻击者通过水坑攻击等方式，对18.4至18.6.2版本的iOS设备实施“零交互”入侵，突破WebContent沙箱，进而利用WebGPU方式将功能性载荷注入系统进程，批量窃取设备唯一标识、短信与即时通信记录、通话记录、通讯录、WiFi登录凭证、浏览器历史、地理位置、照片、邮件、iCloud数据及主流交易所和加密钱包应用中的敏感信息。

**链接：**https://www.lookout.com/threat-intelligence/article/darksword

![](https://mmbiz...