---
title: 每周网络安全简讯 ( 2026年 第28周 )
url: https://mp.weixin.qq.com/s/ADcEdekV4MUk9Gl3VyC5rA
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:27:02.475540
---

# 每周网络安全简讯 ( 2026年 第28周 )

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qyzTicOO6WeWBftVBCbibYicQmicm2Tia69Be1a3ZJDSfpvgElibpj63sMxJzPc5yeLEWxZiaQ0ib7dJmiaJfljzF96q9hKP6zAUYQV0FoogXDFy0Its/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第28周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年7月4日至2026年7月10日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计20条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织Armored Likho利用BusySnake窃密木马对多国目标用户实施网络攻击

近日，卡巴斯基研究人员披露一个此前未知的APT组织Armored Likho，正针对俄罗斯、巴西、哈萨克斯坦的政府机构与关键基础设施组织发动攻击。经分析，Armored Likho通过伪装为政府公文或社会救助材料的鱼叉式钓鱼邮件投递压缩包，内含恶意可执行文件或伪装成心理测试、人道援助申请等文档的Windows快捷方式，第一阶段载荷运行诱饵文档迷惑受害者，后台释放器则静默投放后续恶意程序。研究人员指出，部分加载器组件存在冗余注释与代码块，显示攻击者疑似借助大型语言模型（LLM）生成第一阶段载荷以拓展攻击手法。同时，最终载荷为此前未记录的Python编写的窃密木马BusySnake Stealer，可窃取浏览器密码与Cookie、剪贴板内容、加密密钥、Telegram会话等敏感数据，并可建立反向SSH隧道、部署远控软件及C2通道维持持久交互访问。该木马还采用PyArmor Pro加密字节码、按需解密后即时重加密、无控制台静默运行及内置网络功能等手法对抗检测与逆向。综上，考量该APT组织近期以AI辅助攻击的技术特点，安全人员应加强相应环节安全监测、检测能力，以降低遭受攻击的风险。

**链接：https://www.darkreading.com/cyberattacks-data-breaches/busysnake-infostealer-critical-infrastructure-networks**

02

APT组织Cavern Manticore利用新型模块化C2框架Cavern对以色列目标用户实施网络攻击

近日，安全研究人员披露称，一个隶属于伊朗情报与安全部（MOIS）的APT组织Cavern Manticore滥用SysAid软件更新功能进行DLL侧载，向以色列的IT供应商、政府部门等目标设备上植入内含模块化C2框架Cavern的木马化DLL（uxtheme.dll）和通信模块（n-HTCommp.dll），进而通过HTTPS或WebSocket连接C2服务器并按需拉取后渗透模块。经分析，Cavern框架基于.NET Framework进行开发，采用混合模式C++/CLI及原生AOT三种编译格式与分模块AppDomain隔离机制的方式对抗安全人员的逆向分析与取证机制，且其内置了5个DLL功能性模块，分别用于文件操作、SQL数据库操作、Active Directory侦察、网络侦察端口扫描及SOCKS5代理隧道，可对受控设备实施持久性远控。

**链接：https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html**

03

APT组织APT-C-36对哥伦比亚、南美洲等国家或地区目标用户实施网络攻击

近日，安全研究人员发现APT组织APT-C-36对哥伦比亚、南美洲等国家或地区目标用户实施网络攻击。此次攻击活动中，该APT组织将钓鱼诱饵伪装为"银行交易调整"相关文件以邮件形式进行投递，用户点击后将释放6个"白加黑"文件，其中恶意DLL（libwinpthread-1.dll）伪装成pthread库、由合法Git工具Scalar加载。该加载器疑似为QuirkyLoader变体，采用.NET AOT预先编译技术将.NET代码编译为原生机器码，增强自身隐蔽性与安全分析难度，其运行后采用ChaCha20变体、XOR等算法解密配置字符串与API名称，将存于.reloc节的加密载荷经凯撒密码与ChaCha20变体两阶段解密后，注入合法进程AddInProcess32.exe，而后经过一系列进程注入流程后，部署DcRAT功能性载荷，实施进程管控、摄像头开启、敏感信息窃取等恶意操作。

**链接：[【查看原文】](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247508740&idx=1&sn=7462e1127fcbe10281f7af3e1ea494d6&scene=21#wechat_redirect)**

04

APT组织APT-C-20利用PNG图像隐写技术投递无文件C#后门

近日，安全研究人员披露称，APT组织APT-C-20以"东欧国家国防相关文件"为话题制作钓鱼邮件，诱使目标用户点击实施渗透入侵。一旦用户启用宏并点击相关恶意附件，将会向用户设备释放DLL文件dnxstore.dll与伪装成Edge图标的图片EdgeLogo.png，并通过COM劫持加载攻击代码。该DLL在检测调试与沙箱环境后，利用最低有效位隐写术（Least Significant Bit Steganography）从图像像素中提取并解密ShellCode，于内存中反射加载经过高度混淆的C#后门Publish.exe。经分析，该后门放弃传统C2架构，转而借助云存储服务Filen.io进行C2通联，且配置多个备份网关以维持连接。综上，此次攻击活动叠加宏加密、注册表隐藏、图像隐写等多层规避手段，且载荷全程不落地，存在较大潜在安全威胁，相关组织应警惕启用宏的可疑文档，加强对explorer.exe异常行为及云API出站流量监测，以降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/apt-c-20-hackers-hide-shellcode-in-png-images/**

02

网络动态

01

滥用微软"设备授权许可"功能的新型钓鱼攻击方式被披露

安全公司Securelist披露一起滥用微软"设备授权许可"（Device Code Flow）功能的新型钓鱼攻击，该功能原用于智能电视、打印机等无键盘设备通过一次性代码登录账户，攻击者借此在全程不使用仿冒登录页的情况下窃取账户访问令牌。据分析，攻击者以伪装成律师事务所通知的邮件投递密码保护PDF附件，诱导受害者点击链接跳转至含CAPTCHA验证的伪造法律门户，页面显示一次性代码并引导其复制。受害者随后将代码粘贴至微软真实认证页面完成登录，而攻击者此前已向微软服务器请求该代码，登录获批后即取得可读写邮件、提取OneDrive文件及查看Teams会话的访问令牌。研究人员指出，因最终登录界面真实，该手法可绕过"核对网址"等安全机制，且代码获批后即使采用多因素认证也难以提供防护。安全研究人员建议称，用户不应批准非本人发起的设备登录请求，组织可通过条件访问策略禁用非必要的设备代码流，并监控DeviceCodeSignIn事件与异常位置登录，以降低遭受攻击的风险。

**链接****：https://cybersecuritynews.com/microsoft-device-code-phishing-attack/**

02

美国DHS与FRA推进CHARIOT项目，强化货运铁路OT通信安全与关键基础设施网络韧性

美国国土安全部科技局（S&T）联合联邦铁路管理局（FRA）通过"CHARIOT"项目（Critical Infrastructure Hardening Achieved through Risk Reduction in Informational and Operational Technology），推进货运铁路网络的网络安全韧性建设。该项目聚焦货运铁路运营中数字化控制的OT系统，重点检验对监测列车状态、保障行车安全至关重要的列车头部（Head-of-Train）与末端（End-of-Train）设备间通信，通过实地测试研究网络干扰对日益互联的铁路环境运营可靠性与安全的影响。项目由跨机构工作组统筹，整合交通运输领域利益相关方，兼顾铁路与油气关键基础设施组件测试。据CISA专家介绍，相关成果已推动业界更新标准，FRA正联合爱达荷国家实验室制定末端设备（EOT）风险评估与缓解指南。

**链接：https://industrialcyber.co/transport/dhs-and-fra-use-project-chariot-to-boost-freight-rail-cyber-resilience-secure-ot-communications-protect-rail-infrastructure/**

03

欧盟委员会发布《网络安全与人工智能行动计划》，统筹推进AI安全应用与网络韧性建设

欧盟委员会发布《网络安全与人工智能行动计划》（Action Plan on Cybersecurity and Artificial Intelligence），旨在支持人工智能安全、负责任地应用，同时强化欧洲网络安全能力。行动计划指出，AI在助力漏洞检测、防范网络攻击、保护关键基础设施的同时，也可能被恶意行为者滥用以自动化攻击、发现弱点并以前所未有的速度和规模实施网络行动。基于欧盟现有AI与网络安全法律框架，该计划围绕三项互补目标展开：促进先进AI的安全负责任使用、强化欧盟网络安全与韧性、提升欧洲面向网络安全的AI能力。具体举措方面，委员会将依据《人工智能法》强化AI模型上市前评估能力，并联合欧盟网络安全局（ENISA）制定安全测试平台，供能源、交通、医疗、金融及公共行政等关键领域安全测试与部署AI方案。

**链接****：https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence**

04

英国NCSC与DSIT推进"网络盾牌"计划

NCSC联合科学、创新与技术部（DSIT）推进一项名为"网络盾牌"（Cyber Shield）的国家级计划，拟将前沿智能体（agentic）AI嵌入网络防御体系，构建协同化的自主网络防御能力，以识别、降低并化解国家层面网络风险。该计划背景在于英国面临的网络威胁在规模、速度与复杂度上持续攀升，且前沿AI正加速这一趋势，AI已能协助攻击者以更大规模、更快速度开展漏洞发现与侦察，使原需数周的活动缩短至几分钟，压缩防御方响应窗口，未来更可能贯通从初始访问到目标行动的完整攻击生命周期。"网络盾牌"设想由"红队"智能体自主发现系统弱点、"蓝队"智能体实时防御，逐步从漏洞识别迈向自动化修复，并在各机构授权控制下跨组织边界协同。该计划明确了可靠可解释AI、联邦化智能体、漏洞发现与缓解、协同检测响应、国家级扫描与国家级缓解六项核心能力，并采取"测试—迭代—扩展"路径，先与政府及关键领域网络防御方合作试点，再转向可商业化扩展的方案。

**链接****：https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence**

05

可诱导AI编程助手安装恶意程序构建僵尸网络的HalluSquatting新型攻击手法被披露

近日，特拉维夫大学等机构安全研究人员披露一种名为HalluSquatting的新型攻击手法。该手法结合大模型"幻觉"与间接提示词注入两类缺陷，攻击者先诱使AI编程助手对热门代码仓库或插件反复生成其最常虚构的虚假名称，随后在GitHub或插件市场抢注该名称并植入恶意指令，待真实用户要求助手获取相关资源时，助手便会拉取攻击者版本，并利用自身命令执行工具运行恶意载荷。测试显示，该手法可使Cursor、Windsurf、GitHub Copilot、Gemini CLI等多款主流工具执行攻击者代码，仓库请求场景下同一错误名称复现率最高达85%，且无需口令爆破或漏洞利用即可批量控制运行不同操作系统的主机、组建僵尸网络。研究人员建议称，开发方应使AI代理在获取资源前先行检索验证名称真实性，用户应避免启用自动执行模式，并在拉取前核验仓库或软件包的实际来源。

**链接****：https://thehackernews.com/2026/07/new-hallusquatting-attack-could-trick.html**

06

新型数据勒索组织Helix被披露

7月8日，网络安全公司ReliaQuest发布报告披露了一个名为Helix的新型数据勒索组织，以伪造身份为核心从SharePoint环境中窃取数据。报告指出，Helix将语音钓鱼作为初始入侵手段，冒充目标组织经理借助其姓名或伪造来电显示骗取信任，进而诱导受害者落入设备代码钓鱼陷阱以获取账户权限，得手后迅速注册新的多因素认证应用以维持持久访问，随后枚举并批量导出SharePoint文件。其自动化枚举与收集行为在各起攻击事件中高度一致，基于技术手法与基础设施相似性，Helix可能脱胎于ShinyHunters与已解散的BlackFile勒索组织，但尚未发现确凿关联。研究人员建议称，相关组织应尽可能禁用设备代码认证，并将SharePoint访问权限限制为受管设备，同时实时监测其与新注册域名的通信行为，以降低遭受攻击的风险。

**链接****：https://reliaquest.com/blog/threat-spotlight-helix-new-name-in-data-extortion-ecosystem/**

03

漏洞资讯

01

Linux内核KVM虚拟机管理程序存在虚拟机逃逸漏洞

近日，安全研究人员发现Linux内核KVM虚拟机管理程序存在一个称为Januscape的虚拟机逃逸漏洞（CVE-2026-53359），影响KVM的影子MMU（shadow MMU）代码，可从虚拟机内部触发以破坏主机内核的影子页面状态，攻击者仅需租用单个云实例，即可通过触发主机内核崩溃使同一物理机上其他租户虚拟机瘫痪（DoS），或在主机上以root权限执行代码。目前，用户可通过内核版本更新等方式修复上述安全漏洞。

**链接：https://www.securityweek.com/linux-kernel-vulnerability-allows-vm-escape-on-intel-and-amd-systems/**

02

谷歌云GCP存在代码注入漏洞

近日，安全研究人员发现谷歌云GCP存在名为"Rogue Agent"的代码注入漏洞，位于GCP Playbook代码块Dialogflow CX功能组件中，是由code\_execution\_env.py文件权限存在缺陷所导致，允许攻击者仅需单个编辑权限即可向目标设备AI聊天机器人流程中注入持久化恶意代码，进而窃取对话内容或发起大规模钓鱼活动。目前，用户可通过补丁更新修复上述安全漏洞。

**链接：https://cybersecuritynews.com/gcp-dialogflow-vulnerability/**

03

Adobe ColdFusion存在路径遍历漏洞

近日，安全研究人员发现Adobe ColdFusion存在路径遍历漏洞（CVE-2026-48282），允许未经身份验证的攻击者远程执行任意攻击指令。目前，该漏洞已出现在野利用，目前用户可通过版本升级、补丁更新等方式修复上述安全漏洞。

**链接：https://securityaffairs.com/194837/hacking/adobe-coldfusion-flaw-cve-2026-48282-now-exploited-in-the-wild.html**

04

XWiki Platform存在路径遍历漏洞

近日，安全研究人员发现开源的企业级Wiki平台XWiki Platform存在路径遍历漏洞（CVE-2026-34151），该漏洞源于/skin/action端点在处理资源路径时，针对Jetty 12应用服务器URL解码方式存在缺陷所导致，允许攻击者通过发送双重URL编码"%252f"序列的方式绕过路径限制。漏洞影响XWiki Platform < 17.10.5等版本，目前用户可通过补丁更新修复上述安全漏洞。

**链接：https://securelayer7.net/lab/cve-2026-34151-xwiki-skin-path-traversal-jetty12**

05

Claude Code、Augment等6款AI编码辅助工具存在符号链接漏洞

近日，安全研究人员发现Amazon Q Developer、Anthropic Claude Code、Augment、Cursor、Google Antigravity及Windsurf六款主流AI编码助手存在称为"GhostApproval"的符号链接漏洞。攻击者可在恶意仓库中植入伪装的符号链接文件（如指向SSH登录文件~/.ssh/authorized\_keys或Shell启动文件~/.zshrc），并借助README诱导AI代理"配置工作区"，使其在用户以为仅编辑普通配置文件时，将攻击者的SSH密钥等内容越权写入敏感文件，进而实现免密登录或代码执行。目前，Amazon Q Developer（CVE-2026-12958）、Cursor（CVE-2026-50549）、Google Antigravity已进行修复，Augment与Windsurf尚未修复，Anthropic则认为该场景不属于其威胁模型。

**链接：https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants**

04

木马病毒

01

疑似首例由AI代理全程自主执行的JadePuffer勒索软件攻击被披露

云安全公司Sysdig披露一起名为JadePuffer的勒索软件攻击事件，研究人员称其疑似首例完全由大型语言模型（LL...