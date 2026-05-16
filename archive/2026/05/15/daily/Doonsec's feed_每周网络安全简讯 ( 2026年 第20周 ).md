---
title: 每周网络安全简讯 ( 2026年 第20周 )
url: https://mp.weixin.qq.com/s/uSnkL9l9VMeinuzms1bqog
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:10:28.864367
---

# 每周网络安全简讯 ( 2026年 第20周 )

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qyzTicOO6WeVbZyYxCWxNPZMHJx3EFoShicKNnwZ38IzicICgRGP4RZ9iaoJzJRIBVTRBoW2PHlZB60OzLDvg1bMUlJ7zbfNHF5Wb4L1hWbQkRo/0?wx_fmt=jpeg)

# 每周网络安全简讯 ( 2026年 第20周 )

国信中心
国信中心

极客安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年5月9日至2026年5月15日，国家信息技术安全研究中心威胁监测部对境内外互联网上的网络安全信息进行了搜集和整理，并按APT攻击、网络动态、漏洞资讯、木马病毒进行了归类，共计20条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ficzEsma1eib1exIHxlrhz8tk5C2sQkc1tsPgmT9Wk2BNYLL020LAibiaAN5Oa5esWyoKv6VwNblEhJjibcYp7tfOyw/640?wx_fmt=png)

01

APT攻击

01

APT组织利用Chaos勒索程序实施网络攻击

近日，Rapid7安全研究人员将一起Chaos勒索程序攻击事件归因于APT组织MuddyWater。该APT组织截至2026年初活动频率明显增加，主要针对西方和中东网络开展网络间谍活动。在此次行动中，攻击者通过Microsoft Teams受控账户发起一对一社交工程攻击，建立屏幕共享会话，并部署AnyDesk和DWAgent等合法远程管理工具实现持久化控制，同时利用RDP横向移动、篡改多因素身份验证设置以维持长期访问。综上，这种“混合入侵模型”反映出国家支持型APT与网络犯罪手法日益融合的趋势，勒索软件不再是最终目的，而是用于隐蔽并提升攻击灵活性的手段，同时也警示相关组织应将Teams、Slack等协作平台视为与电子邮件和VPN同等级别的高风险攻击面。

**链接：https://industrialcyber.co/ransomware/rapid7-links-chaos-ransomware-campaign-to-iranian-state-sponsored-muddywater-espionage-operation/**

02

网络动态

01

欧盟拟推出“技术主权一揽子计划”，全面重塑数字基础与战略自主

欧盟即将正式推出“技术主权一揽子计划”（Tech Sovereignty Package），旨在减少对非欧洲技术供应商的依赖，同时提升其在半导体、云计算、人工智能和开源软件等关键领域的自主能力。该方案并非新增一层监管，而是对现有规则进行简化与协同，以服务欧盟“开放战略自主”（Open Strategic Autonomy）整体目标。一揽子计划聚焦四大支柱：一是《云与人工智能发展法案》（CAIDA），统一“主权云”定义并放宽欧盟境内数据中心建设规则；二是《芯片法案 2.0》，进一步强化半导体制造与供应链安全；三是欧洲开放数字生态系统，首次将开源技术正式定位为关乎主权、民主韧性与网络安全的“数字公地”（Digital Commons），通过“数字公地欧洲数字基础设施联盟”（DC-EDIC）汇集成员国资源、共建跨境开源基础设施，同时借助《网络韧性法案》（CRA）中的“开源软件管理者”角色为开源基金会提供差异化合规路径；四是《能源领域数字化与人工智能战略路线图》，将能源AI视为高风险关键基础设施，强制对接NIS2指令和CRA，同步推动建设“欧洲通用能源数据空间”、能源电网数字孪生及欧洲能源电网AI基础模型。

**链接****：https://commons.ngi.eu/2026/05/08/understanding-the-tech-sovereignty-package-what-to-expect**

02

ENISA强化欧盟漏洞协调：四家机构加入ENISA Root旗下CVE计划

欧盟网络安全局（ENISA）继2025年11月正式成为通用漏洞披露（CVE）项目根机构后，宣布已有四家新机构加入CVE计划，成为ENISA Root旗下的CVE编号机构（CNA），同时另有七家现有欧洲CNA已从MITRE Root迁移至ENISA Root。ENISA首席网络安全和运营官Hans de Vries称此举为欧洲网络安全发展的重要里程碑，将加强欧洲对全球CVE计划的运营贡献，并提升欧盟范围内漏洞处理的可靠性、及时性和协调性。作为CVE Root，ENISA负责在其授权范围内招募、培训、支持和管理CNA，协助其过渡，并确保CVE标识符的有效分配和CVE记录的发布。该工作与美国网络安全和基础设施安全局（CISA）及非营利组织MITRE密切协调，旨在加强全球共享的漏洞标识符体系。

**链接：**https://industrialcyber.co/vulnerabilities/enisa-strengthens-eu-vulnerability-coordination-as-four-organizations-join-cve-program-under-enisa-root/

03

NIST修订PNT服务网络安全指南，应对GPS中断、AI与供应链风险

美国国家标准与技术研究院（NIST）发布NISTIR 8323 Rev. 2修订草案，更新其定位、导航和授时（PNT）网络安全基础规范，使其与NIST网络安全框架 2.0（CSF 2.0）保持一致，旨在帮助组织管理依赖PNT服务的系统和资产所面临的风险，涵盖GPS、网络时间协议服务器、商业授时服务和内部授时基础设施。该规范围绕CSF 2.0的六大职能展开：治理职能为其他职能奠定基础；识别职能帮助组织理解PNT依赖关系和相关风险；保护职能侧重于防止因PNT服务中断或被篡改导致的功能丧失；检测职能负责发现和分析潜在攻击；响应职能在事件发生后控制影响范围；恢复职能则支持运营连续性。

**链接****：https://industrialcyber.co/nist/nist-revises-pnt-services-cybersecurity-guidance-under-csf-2-0-to-address-gps-disruption-ai-risks-supply-chain-threats/**

04

GhostLock工具滥用API实施文件锁定的拒绝服务攻击

一位安全研究人员近日发布了一款名为GhostLock的概念验证工具，该工具演示了如何滥用合法的Windows文件API函数进行攻击，从而阻止用户或应用程序访问存储在本地或SMB网络共享上的文件。这项技术由以色列航空航天工业公司的Kim Dvash研发，其核心在于滥用Windows的“CreateFileW”API及其文件共享模式参数，阻断其他进程对文件的访问。为将这一技术自动化，Dvash在GitHub上发布了GhostLock工具。该工具能够递归地打开SMB共享上的大量文件，在保持文件句柄活跃的状态下，使任何新的文件访问尝试都被系统拒绝。值得注意的是，该工具可以由标准域用户运行，无需任何提升的权限。攻击者甚至可以从多台受感染的设备同时发起攻击，并在先前进程终止后不断重新获取文件句柄，从而延长阻断时间。不过，一旦关联的SMB会话结束、GhostLock进程被终止，或者受影响的系统重启，Windows会自动关闭所有文件句柄，恢复正常的文件访问。

**链接****：**https://www.bleepingcomputer.com/news/security/new-ghostlock-tool-abuses-windows-api-to-block-file-access/

05

谷歌发布报告称：AI生成零日漏洞利用工具并实施网络攻击

谷歌威胁情报小组（GTIG）的研究人员表示，一款针对流行开源Web管理工具的零日漏洞利用程序，很可能由AI生成。该漏洞利用程序可用于绕过一款流行的Web开源系统管理工具中的双因素认证（2FA）保护，但该工具名称尚未公开。尽管此次攻击在进入大规模利用阶段前就被成功阻止，但这一事件表明，威胁行为者正越来越依赖AI辅助开展漏洞发现与漏洞利用活动。

**链接****：**https://www.bleepingcomputer.com/news/security/google-hackers-used-ai-to-develop-zero-day-exploit-for-web-admin-tool/

06

OpenAI推出Daybreak网络安全计划摘要

近日，OpenAI推出一项结合前沿AI模型与代码安全的网络安全计划Daybreak，旨在帮助组织在攻击者之前识别和修复漏洞。该计划可为代码库构建威胁模型，将安全代码审查、威胁建模、补丁验证、依赖风险分析等功能整合到日常开发流程中。同时，该计划基于三个底层模型进行构建：通用版GPT-5.5、用于授权防御工作的GPT-5.5 with Trusted Access for Cyber，以及用于红队演练的GPT-5.5-Cyber。

**链接****：**https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html

07

苹果与谷歌为跨平台RCS消息引入端到端加密

苹果和谷歌正式推出一项备受期待的更新，允许iPhone和Android用户通过富通信服务（RCS）发送端到端加密（E2EE）短信。该功能目前以测试版形式推出，面向运行iOS 26.5的iPhone用户，以及使用最新版Google Messages的Android用户。在此之前，虽然苹果和谷歌各自的生态系统内都已支持端到端加密，但iPhone与Android用户之间的跨平台消息一直未加密，此次合作填补了这一空白。端到端加密可保护消息在设备间传输时不被黑客、政府机构、电信运营商甚至平台公司读取。除加密功能外，跨平台交互还将支持编辑已发送消息、删除消息、跨平台点击回复反应（tapback）以及对特定消息进行内联回复等现代消息功能。

**链接****：**https://www.businesstoday.in/technology/story/iphone-and-android-rcs-messages-get-end-to-end-encryption-530984-2026-05-12

08

英国水务公司66万人信息泄露被罚96万英镑

英国信息专员办公室（ICO）近日对南斯塔福德郡水务有限公司及其母公司南斯塔福德郡有限公司处以96.39万英镑（约130万美元）的罚款，原因是该公司因网络攻击导致超过66万名客户和员工的个人数据泄露。这家每天向160万消费者供应3.3亿升饮用水的公司，于2022年披露成为网络攻击目标并导致IT运营中断。当时，公司曾驳斥Cl0p勒索软件团伙声称对此次攻击负责的说法，但事后证实泄露的数据样本属实。攻击可追溯至2020年9月，但主要发生在2022年5月至7月之间，暴露了该公司在数据安全方面存在的重大缺陷，使客户和员工在近两年时间里处于易受攻击状态。调查显示，此次事件是通过网络钓鱼攻击造成的，攻击者利用钓鱼手段在公司系统中安装恶意软件，该恶意软件长达20个月未被发现。2022年5月至7月期间，攻击者成功提升网络权限并获得域管理员访问权，直到当年7月因IT性能问题引发调查后才被发现。泄露的数据极为敏感，包括全名、实际地址、电子邮件地址、电话号码、出生日期、客户账户凭证、银行账户详细信息，以及员工人力资源数据如国民保险号码等。

**链接****：**https://www.bleepingcomputer.com/news/security/uk-fines-water-supplier-13m-for-exposing-data-of-664k-customers/

09

法国国防巨头泰雷兹集团疑似发生数据泄露事件

据称与北约关联的法国国防巨头泰雷兹集团有关的数据集出现在知名网络犯罪论坛上，仅包含两条记录的样本，但这一事件已引发外界对欧洲各国政府所使用的敏感身份基础设施可能遭到入侵的新的广泛担忧。泰雷兹集团是全球领先的国防电子和航空航天企业，年收入达258亿美元，拥有超过85000名员工，对法国和北约而言具有战略性关键意义。审查了数据样本的研究人员表示，数据格式与第三方或面向客户的数据集更为一致，而非LuxTrust自身的内部系统。样本中包含了全名、电子邮件地址以及一个“公司”字段，这表明数据很可能来自提供商的基础设施而非LuxTrust的原始内部数据。研究人员指出，这种结构更像是通过外部服务层或合作伙伴平台处理的数据。由于LuxTrust作为总部位于卢森堡的数字身份提供商，其业务涉及政府、金融和企业身份验证，即便只是用户身份数据的有限泄露，也可能带来不成比例的严重风险，尤其是在网络钓鱼和社会工程攻击方面。

**链接****：**https://cybernews.com/security/thales-group-luxtrust-data-breach/

10

OpenAI证实遭遇TanStack供应链攻击

近日，OpenAI发布安全公告，首次证实其在Shai-Hulud软件供应链攻击中遭遇波及。攻击者通过被植入恶意代码的广泛使用开源库TanStack npm，入侵了OpenAI内部两台员工设备，并成功窃取部分源代码仓库的访问凭证，迫使公司启动大规模证书轮换与安全加固响应，包括对CI/CD管道中的敏感凭证进行加固、在包管理器中应用minimumReleaseAge锁定策略，以及部署验证新包来源的额外安全软件等。

**链接****：**https://www.bleepingcomputer.com/news/security/openai-confirms-security-breach-in-tanstack-supply-chain-attack/

03

漏洞资讯

01

Ollama存在越界读取漏洞

近日，安全研究人员发现Ollama存在越界读取漏洞（CVE-2026-7482），是由GGUF模型加载器存在缺陷所导致，允许攻击者通过构造恶意GGUF文件的方式远程读取目标设备内存内容，造成敏感信息泄露。目前，用户可通过将Ollama版本升级至0.17.1或更高版本的方式修复上述安全漏洞。

**链接：https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vulnerability.html**

02

Exim存在代码执行漏洞

近日，安全研究人员发现开源邮件传输代理Exim存在代码执行漏洞（CVE-2026-45185），是由GnuTLS处理TLS连接时二进制数据传输(BDAT)消息体解析存在缺陷所导致，允许攻击者通过向目标设备发送恶意TCP连接请求的方式造成堆损坏或代码执行。漏洞影响4.97到4.99.2等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://thehackernews.com/2026/05/new-exim-bdat-vulnerability-exposes.html**

03

Cline人工智能代理存在安全漏洞

近日，安全研究人员发现Cline人工智能代理Kanban服务器存在安全漏洞（CVE-2026-44211），是由本地服务器对公开软件包缺乏来源验证机制所导致，允许攻击者通过诱骗用户使用本地服务器访问恶意网站的方式窃取文件系统路径、git分支、聊天消息等敏感信息。目前，用户可通过启用随机会话令牌、验证源标头等措施降低遭受攻击的风险。

**链接：https://cybersecuritynews.com/cline-ai-agent-vulnerability/**

04

微软公司发布5月份安全漏洞更新公告

近日，微软公司发布5月份安全漏洞更新公告，涉及Windows、Office、Azure等产品的120个安全漏洞，其中有29个安全漏洞较为严重，部分包括：Microsoft Dynamics 365（CVE-2026-42898、CVE-2026-42833）、Microsoft Office和Word远程代码执行漏洞（CVE-2026-42831、CVE-2026-40363、CVE-2026-40358等）、Windows DNS客户端（CVE-2026-41096）、Netlogon（CVE-2026-41089）、Windows Graphics/Win32k（CVE-2026-40403）、Windows GDI（CVE-2026-35421）、Windows原生Wi-Fi微型端口（CVE-2026-32161）及Microsoft SharePoint Server（CVE-2026-40365等）。目前，用户可通过补丁更新修复上述安全漏洞。

**链接：https://cybersecuritynews.com/microsoft-patch-tuesday-may-2026/**

05

FortiSandbox平台存在安全漏洞

近日，安全研究人员发现Fortinet的FortiSandbox平台存在安全漏洞（CVE-2026-26083），是由FortiSandbox Web UI缺少授权检查机制所导致，允许未经身份验证的攻击者发送恶意HTTP请求，进而在目标设备底层系统实现代码执行。漏洞影响FortiSandbox 5.0:Versions 5.0.0–5.0.1等版本，目前用户可通过版本升级修复上述安全漏洞。

**链接：https://cybersecuritynews.com/fortinet-fortisandbox-vulnerability/**

06

Linux内核存在安全漏洞

近日，安全研究人员发现Linux内核存在本地权限提升漏洞（CVE-2026-46300），位于XFRM ESP-in-TCP子系统中，允许攻击者在无需任何竞争条件的情况下即可向内核只读文件页面缓存中写入任意数据。目前，用户可通过限制非特权用户命名空间权限等措施降低遭受攻击的风险。

**链接：https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html**

04

木马病毒

01

PamDOORa新型恶意程序通过劫持Linux PAM框架窃取SSH凭证

安全研究人员披露了一款名为PamDOORa的新型恶意程序。PamDOORa属于后渗透工具，需攻击者预先获取目标设备root权限方可部署，其核心攻击手法是劫持Linux系统用于处理登录与身份验证的可插拔身份验证模块（PAM）框架，通过滥用合法模块pam\_exe...