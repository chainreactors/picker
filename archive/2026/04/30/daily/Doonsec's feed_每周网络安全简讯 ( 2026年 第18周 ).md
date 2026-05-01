---
title: 每周网络安全简讯 ( 2026年 第18周 )
url: https://mp.weixin.qq.com/s/8VF8zKzPVGTlXCkmn1NccQ
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:34:19.431766
---

# 每周网络安全简讯 ( 2026年 第18周 )

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qyzTicOO6WeVy7o1tchRXvd0ojG3JNZpqzAOztboU7vibNqib0PwicPMChJ9h7yJAdiaMHwAhXia7avk9efdicYAf2acKlPaLHSwzuY9sGsVVjaKiaE/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第18周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年4月25日至2026年4月30日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计20条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织Kimsuky对制药、生命科学等公司实施网络攻击

近日，APT组织Kimsuky借助伪装成Excel文档的恶意软件，针对制药、生命科学等公司实施网络攻击。钓鱼邮件以ERP规范、生产计划、研发文档等看似正规的话题为诱饵，一旦用户点击邮件ZIP附件内伪装成Excel表格的Windows快捷方式文件（LNK）时，将会静默调用cmd.exe执行PowerShell命令下载第二阶段恶意程序载荷，同时弹出一个含有制药业务相关数据的诱饵Excel工作簿以掩人耳目。后续阶段，相关载荷会通过Dropbox API作为隐蔽的C2通道进行系统信息收集和命令执行，并借助计划任务（schtasks）实现持久驻留。

**链接：https://gbhackers.com/malware-laced-excel-attacks/**

02

APT组织“蔓灵花”利用NUITKA打包恶意程序对目标用户实施网络攻击

安全研究人员监测发现APT组织“蔓灵花”在近期的攻击活动中对自身武器库进行更新迭代，利用NUITKA打包恶意Python脚本，并通过网络钓鱼方式向目标用户进行投递。一旦用户点击执行，Python脚本将会自动与C2服务器建立通联关系，实施系统信息收集、计划任务配置等操作，同时植入Shell后门、文件窃密组件、Remcos恶意程序载荷，对受控设备实施持久性远控。

**链接：[【查看原文】](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247508516&idx=1&sn=a869f67294b5777615ad597c3730105e&chksm=f8528aae58ce3ba85c8b0a69caed267d327a7089a6d50056b4bc55a1f0fbd7b3c64a9b72e333&scene=21#wechat_redirect)**

03

APT组织Lazarus利用“Mach-O Man”恶意程序套件对MacOS用户实施网络攻击

近日，安全研究人员披露APT组织Lazarus的“Mach-O Man”新恶意程序套件，Lazarus采用ClickFix社会工程技术，通过Telegram紧急会议邀请的方式诱骗使用MacOS操作系统的目标用户执行恶意指令，进而触发“Mach-O Man”四个阶段感染链，一是下载伪造的会议应用并通过反复“密码错误”的提示骗取用户凭据，二是全面采集系统信息和浏览器配置，三是构造“Antivirus Service”目录和OneDrive组件实现持久化驻留，四是窃取浏览器凭据、会话Cookie和macOS钥匙串内容，并通过Telegram Bot API回传后自删除清除痕迹。安全人员建议称，相关组织应采取提升网络安全意识、加强MacOS原生二进制文件安全检测等措施降低遭受攻击的风险。

**链接：https://www.cryptika.com/lazarus-hackers-attacking-macos-users-with-mach-o-man-malware-kit/**

02

网络动态

01

北约合作网络防御卓越中心举办“锁定盾牌2026”网络防御演习

近日，由北约合作网络防御卓越中心（CCDCOE）在爱沙尼亚塔林组织的全球最大规模实弹网络防御演习“锁定盾牌2026”（Locked Shields 2026）落下帷幕，共吸引来自41个国家的4000多名参与者。演习模拟针对关键基础设施和军事系统的实时网络攻击，16支多国联合团队需保护防空系统、电子投票平台等关键设施，同时应对虚假信息和政治压力的挑战。CCDCOE主任Tõnis Saar指出，参与者展现了出色的威胁检测与响应能力，并强调在人工智能持续重塑网络攻防格局的背景下，需将演习经验转化为实战能力。本届得分最高的三支联合团队为：法国与瑞典队、拉脱维亚与新加坡队，以及德国、奥地利、卢森堡和瑞士联队。

**链接****：https://ccdcoe.org/news/2026/locked-shields-2026-united-the-power-of-41-nations-to-defend-cyberspace/**

02

欧盟拟依据《数字市场法》强制谷歌向竞争对手共享搜索数据

近日，欧洲委员会发布新闻稿，提议根据《数字市场法》（DMA）强制谷歌向第三方搜索引擎共享关键搜索数据，包括排名数据、搜索查询、点击信息和浏览数据，且共享必须遵循公平、合理和非歧视性条款。该措施旨在帮助规模较小的搜索服务商改善服务、与谷歌展开竞争，相关规定还可能延伸适用于具备搜索功能的AI聊天机器人，反映出DMA正被越来越广泛地用于应对新型数字竞争。此外，提案还要求个人数据在共享前必须匿名化处理，并明确数据定价、申请流程等技术与法律细节，以防数据访问机制被模糊规则削弱。

**链接：**https://gbhackers.com/eu-proposes-forcing-google-to-share-search-data/

03

美国海军试点人工智能人才管理系统

美国海军已启动一项利用人工智能为水兵推荐岗位的试点项目，并计划将其扩展到更大规模的人员范围，作为海军现代化进程中改进人才管理的重要举措。海军人力和预备役事务助理部长Ben Kohlmann指出，海军拥有20多万名入伍水兵，每三年就需要进行一次大规模岗位调动，过去依靠人工方式很难为每位水兵提供个性化的职业安排。此次试点由田纳西州米灵顿的海军人力资源相关部门初级人员开发，通过结合水兵的心理画像与职业发展前景，由人工智能主动向每位水兵推送10个最匹配的推荐岗位，水兵无需被动接受，但能直观感受到海军对其职业规划的重视。经过初步试点应用显示，选择续签第二任期的水兵比例较以往提升了40%。

**链接****：https://defensescoop.com/2026/04/28/navy-looking-to-expand-ai-enabled-pilot-for-talent-management/**

04

谷歌与五角大楼达成AI合作，划定监控与自主武器红线

谷歌已正式与美国国防部达成协议，允许其人工智能技术应用于五角大楼运营的机密系统。该协议范围广泛，允许将谷歌AI工具用于“任何合法用途”，可能涵盖后勤、网络安全、情报分析乃至军事行动。但谷歌同时明确划定了两条伦理红线：其AI技术不会用于对美国公民的大规模监控，也不会用于研发和部署自主武器系统。

**链接****：**https://undercodenews.com/google-secures-pentagon-ai-deal-while-drawing-a-red-line-on-surveillance-and-autonomous-weapons/

05

美国防部即将成立"自主作战"子联合司令部

美国国防部长皮特·赫格塞斯在众议院军事委员会2027财年预算听证会上宣布，美军将很快成立一个专注于“自主作战”的新子联合司令部（Sub-unified Command）。国防部2027财年预算中，AI与“联合全域指挥控制”（CJADC2）获得585亿美元拨款，其中约540亿美元用于空、陆、海上及水下的自主与遥控系统，包括392亿美元的“无人机主导”（Drone Dominance）强制性资金，用于多年期投资自主系统采购、国内生产能力和先进能力建设。此外，国防部去年成立的“国防自主作战工作组”（DAWG）在2027财年研发测试评估预算从2026年的2.259亿美元飙升至546亿美元，将与产业界实时合作测试自主系统及编排工具。

**链接****：**https://defensescoop.com/2026/04/29/hegseth-autonomous-warfare-sub-unified-command/

03

漏洞资讯

01

Firefox浏览器存在安全漏洞

近日，安全研究人员发现Firefox浏览器存在安全漏洞（CVE-2026-6770），与其IndexedDB API接口有关，允许攻击者即使在隐私浏览模式下也可对目标用户进行指纹识别。目前，用户可通过将浏览器升级至150或更新版本的方式修复上述安全漏洞。

**链接：https://www.securityweek.com/firefox-vulnerability-allows-tor-user-fingerprinting/**

02

Linux操作系统存在2个安全漏洞

近日，安全研究人员发现Linux操作系统存在2个安全漏洞。其中，第一个安全漏洞是CVE-2026-41651，位于PackageKit守护进程中，允许非特权本地用户在受影响Linux操作系统上获取root权限；第二个安全漏洞是CVE-2026-31431，是由Linux内核身份验证加密模版存在缺陷所导致，允许攻击者篡改目标设备setuid二进制文件，进而获取root权限。目前，用户可通过将PackageKit升级至1.3.5版本，以及更新操作系统内核版本等方式修复上述安全漏洞。

**链接：https://www.scworld.com/brief/pack2theroot-flaw-allows-linux-privilege-escalation、https://xint.io/blog/copy-fail-linux-distributions**

03

Windows RPC存在安全漏洞

近日，安全研究人员发现Windows远程过程调用（RPC）存在一个称为PhantomRPC的安全漏洞，是由相关组件处理不可用RPC服务器连接方式中的架构设计缺陷所导致，允许攻击者将本地权限提升至SYSTEM。目前，用户可通过启用RPC监控、严格限制进程权限等方式降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/new-windows-rpc-vulnerability/**

04

Notepad++存在2个安全漏洞

近日，安全研究人员发现Notepad++存在2个安全漏洞。其中，第一个安全漏洞是CVE-2026-3008，允许攻击者造成目标用户应用程序崩溃，进而提取内存地址信息；第二个安全漏洞是CVE-2026-6539，允许攻击者对相关人员工作流程造成干扰。漏洞影响Notepad++ 8.9.3或更早版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://www.cryptika.com/notepad-vulnerability-allows-attackers-to-crash-application-leak-memory-data/**

05

Gemini CLI存在远程代码执行漏洞

近日，安全研究人员发现Gemini CLI存在远程代码执行漏洞，是由工作区信任处理机制及yolo模式工具允许机制存在缺陷所导致，允许攻击者通过在特定目录放置恶意程序并调用CLI执行的方式实现远程任意代码执行。目前，用户可通过版本升级的方式修复上述安全漏洞。

**链接：https://cybersecuritynews.com/gemini-cli-rce-vulnerability/**

06

LiteLLM存在SQL注入漏洞

近日，安全研究人员发现开源大语言模型统一接口库LiteLLM存在SQL注入漏洞（CVE-2026-42208），是由LiteLLM Proxy处理Authorization API Key存在缺陷所导致，允许攻击者无需任何有效凭证即可实现SQL注入，窃取用户敏感信息。漏洞影响1.81.16≤version<1.83.7等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://blackhatnews.tokyo/archives/98802**

07

GitHub存在远程代码执行漏洞

近日，安全研究人员发现一个影响GitHub.com和GitHub Enterprise Server的安全漏洞（CVE-2026-3854），是由Git push过程中用户提供的推送选项值未经过适当处理所导致，允许攻击者在Git push过程中通过构造恶意值的方式注入额外的元数据字段，进而实现远程任意代码执行。目前，用户可通过将GitHub Enterprise Server升级至3.14.25、3.15.20、3.16.16、3.17.13、3.18.8、3.19.4、3.20.0或更高版本的方式修复上述安全漏洞。

**链接：https://thehackernews.com/2026/04/researchers-discover-critical-github.html**

08

Cursor存在安全漏洞

近日，安全研究人员发现被广泛应用的AI代码编辑平台Cursor存在安全漏洞（CVE-2026-26268），是由其Git Hooks和Bare Repositories功能联合使用存在缺陷所导致，允许攻击者通过诱骗用户克隆恶意代码库的方式实现远程任意代码执行。目前，用户可通过版本升级修复上述安全漏洞。

**链接：https://cybersecuritynews.com/cursor-ai-coding-agent-vulnerability/**

04

木马病毒

01

伪装成银行KYC的安卓恶意程序被披露

近日，安全研究人员披露称，一种新型安卓恶意软件正伪装成“银行KYC”验证应用，通过WhatsApp向印度银行用户进行投递。攻击者以“账户即将冻结、需立即完成验证”为诱饵，诱导用户安装恶意APK，随后在后台静默部署不显示图标的二级载荷。该恶意程序可拦截短信窃取一次性验证码（OTP）、控制拨打电话，并通过精仿的银行KYC界面骗取手机号、ATM密码、Aadhaar号码及完整银行卡信息（卡号、有效期、CVV、PIN码），之后又以“验证进行中，请等待24小时”为由拖延，为攻击者实施欺诈交易争取时间。

**链接：https://gbhackers.com/fake-kyc-android-malware/**

02

针对巴基斯坦政府机构实施攻击的新恶意程序被披露

近日，安全研究人员披露了一起针对巴基斯坦旁遮普安全城市管理局（PSCA）的新型恶意程序活动。攻击者通过冒充内部顾问、以“安全监狱项目”为话题发送包含Word和PDF附件的鱼叉式钓鱼邮件。Word文档中的恶意宏在用户启用内容后会下载主载荷，而PDF则伪装成Adobe Reader更新提示，诱导用户下载第二阶段恶意程序。在成功植入受控设备后，该恶意程序将会通过微软Visual Studio Code隧道服务建立持久远程访问，并利用Discord webhook窃取数据，使恶意流量与可信平台正常访问数据混杂在一起，以提升安全人员监测难度。同时，该恶意程序还会采用进程枚举、滥用ClickOnce清单空公钥、CDN托管基础设施等方式，综合提升其针对传统安全手段的规避能力。

**链接：**https://gbhackers.com/obfuscation-and-staged-payloads/

03

安全人员开发新工具以评估Linux恶意程序针对机器学习防御的绕过能力

布拉格捷克理工大学研究人员开发了一款新工具，用于评估Linux恶意程序绕过现代机器学习防御的难易程度。该工具采用“语义保留转换”技术，在不破坏程序原有执行流程的前提下，通过12种修改方式和7种数据源（如在ELF文件末尾添加新节、修改填充空间、附加良性文件内容、篡改字符串表中的静态符号等）改变文件签名，从而欺骗安全扫描器。在针对广泛使用的机器学习恶意软件检测器MalConv进行测试时，该工具取得了67.74%的规避率，超过三分之二的修改样本成功绕过AI防御系统。安全人员声称，尽管机器学习被广泛用于检测未知威胁，但通过简单调整即可将其欺骗，建议安全厂商升级优化扫描方案，以综合提升恶意程序检测效率。

**链接：**https://gbhackers.com/linux-elf-malware-generator-evades-ml-detection/

04

SLOTAGENT新恶意程序被披露

近日，安全研究人员披露了一款名为SLOTAGENT的恶意程序。经分析发现，SLOTAGENT通过网络钓鱼方式进行传播，一旦植入成功则会在用户操作系统后台静默运行，以最低限度网络活动与C2服务器保持通联。同时，该恶意程序最显著的技术特点是采用了两个较强的反分析手段，一是通过为每个函数名计算哈希值并扫描已加载的系统模块进行匹配解析，使静态分析工具无法看到任何函数名；二是服务器地址、注册表路径和配置值等关键数据不以明文存储，仅在使用时才在内存中临时解密，使常规字符串提取工具失效，即便是动态分析若未在恰当时点捕获内存也难以获得完整的行为视图。

**链接：**https://cybersecuritynews.com/slotagent-malware-uses-api-hashing/

![](https://mmbiz.qpic.cn/mmbiz_gif/TN05MmJLxMoZzCMWO6v9zhQw2WyD663ia0G3nGuKWdpCclhyCzBhC9sed3qMxSV0y37GlN59gfYgUV9oGxLn82g/640?wx_fmt=gif)

编辑：林青

![](https://mmbiz.qpic.cn/mmbiz_gif/TN05MmJLxMoZzCMWO6v9zhQw2WyD663ia0G3nGuKWdpCclhyCzBhC9sed3qMxSV0y37GlN59gfYgUV9oGxLn82g/640?wx_fmt=gif)

往期推荐

[每周网络安全简讯...