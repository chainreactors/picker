---
title: 全球安全动态日报｜20260923｜早
url: https://mp.weixin.qq.com/s/PUr8YhhYBZvGglLfVtuxXQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:57:21.905810
---

# 全球安全动态日报｜20260923｜早

# 全球安全动态日报｜20260923｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260923｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年9月22日共收录19条安全动态，标题如下。

The Hacker News **19**  ·  HackerOne **0**

## The Hacker News

### 01 Linux 内核新漏洞使 ARM64 KVM 虚拟机可读写访问主机内存

**公开时间：**2026年09月22日 19:38

AI 解读

Linux 内核 ARM64 KVM 嵌套虚拟化代码存在漏洞 CVE-2026-89775：当来宾以特定方式安排内存时，因大小计算为零导致必要的 TLB 失效操作被跳过，已释放的主机内存页仍保持可写映射，使来宾可读写主机内核内存，并可能逃逸虚拟机在主机执行代码。该问题仅影响启用 ARM64 嵌套虚拟化的主机（默认关闭且需特定硬件），属于本地攻击路径；研究人员称开放 /dev/kvm 的系统上本地用户也可能借此提权。漏洞已在 Linux 6.18.51、7.2.5 和 7.3-rc1 修复，暂无公开利用代码或攻击迹象。

原文：https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html

### 02 微软最初将 SharePoint 漏洞列为欺骗，该漏洞可导致经身份验证的远程代码执行  备选（更短）：微软误将 SharePoint 漏洞标为欺骗，实则可触发经身份验证的 RCE

**公开时间：**2026年09月22日 19:17

AI 解读

CVE-2026-65660是影响SharePoint Server 2016、2019和Subscription Edition的代码注入漏洞。微软最初在安全公告中将其列为CVSS 6.5的欺骗漏洞，但后续CVE记录及研究显示，具备认证权限的攻击者可实现远程代码执行，NVD评分为8.8。漏洞源于ToolPane处理Web部件标记时未转义引号，攻击者可注入指令绕过SafeControls检查，加载任意.NET类并通过反序列化触发执行。该漏洞已于8月11日修复并默认关闭相关功能，目前未报告野外利用；研究人员称其还影响已停止支持的SharePoint 2013。

原文：https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html

### 03 中文标题可译为：\*\*恶意 npm 包 indexed-btree 在被下架前将加载器藏匿于运行时代码中\*\*。  如果你需要，我可以继续： 1. 翻译成完整中文报道 2. 写技术摘要，包括攻击链、IOC 和影响范围 3. 改写成适合安全周报/公众号的标题与导语

**公开时间：**2026年09月22日 17:38

AI 解读

Checkmarx发现，恶意npm包“indexed-btree”仿冒合法的sorted-btree，未使用preinstall或postinstall脚本，而是将加载器藏入BTree.prototype.set()运行逻辑，触发包含混淆代码的sharedLoad.min.js。该恶意程序会采集主机信息并发送至预设的Slack频道和Telegram机器人，再通过Sepolia测试网上的智能合约获取加密后续载荷，最终清理恶意痕迹。该包于2026年6月上传，曾获数百万次下载，相关行动据称获利约109 ETH，现已从npm及GitHub下架。事件表明，限制生命周期脚本促使攻击者转向运行时执行。同期，北韩关联PolinRider被指通过入侵开发者账号和Git仓库，将混淆代码、IDE自动运行任务及区块链载荷植入Packagist项目，显示其会根据受害项目调整执行路径，并借正常开发流程扩散。

原文：https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html

### 04 SideCopy 利用 ReverseRAT 鱼叉式网络钓鱼扩大对印度学术界的攻击目标范围

**公开时间：**2026年09月22日 15:52

AI 解读

SideCopy（又称TAG-140）被观察到将针对范围从印度政府和国防机构扩大至学术机构。攻击通过鱼叉式钓鱼邮件投递伪装成DOCX的恶意ZIP及LNK文件，利用mshta.exe执行远程HTA脚本，并通过多阶段混淆、内存加载和自删除机制部署ReverseRAT。该远程访问木马自2021年起被SideCopy使用，可收集系统信息、软件列表、截图、密码和剪贴板内容，执行命令、文件操作、上传及持久化，并通过加密C2通信外传数据。Trellix认为，此次转向学术领域反映其情报收集目标正在扩大。

原文：https://thehackernews.com/2026/09/sidecopy-broadens-india-targeting-to.html

### 05 一个隐藏的 Meta Muse 设置可能让攻击者将这款 AI 助手变成后门

**公开时间：**2026年09月22日 14:33

AI 解读

安全研究员Patrick Wardle展示称，Mac版Meta Muse存在一个未公开的听写端点设置，已能以登录用户身份运行代码的恶意软件可将其指向攻击者控制的地址，使用户通过麦克风输入的音频和文字先流向攻击者。攻击者可借此读取内容、注入Muse信任的指令，并获取用于登录Muse账户的令牌，进而查看聊天记录、跨设备控制助手及调用用户已授权的文件、邮件、消息、日历和智能家居等功能。该问题依赖Mac已被入侵，不能自行突破系统；它利用的是Muse客户端及其既有权限，并非攻破Meta云端隔离机制。文章称Meta已推送修复，但具体变化尚未得到确认。

原文：https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html

### 06 WordPress Comment2Shell 漏洞可将匿名评论 XSS 通过管理员会话升级为 RCE

**公开时间：**2026年09月22日 14:03

AI 解读

WordPress核心被发现存在名为“Comment2Shell”的漏洞（CVE-2026-93485），影响4.7至7.1版本。匿名用户可利用评论处理与显示格式化之间的缺陷，在允许的HTML标签属性中插入换行，使恶意内容被浏览器解析为自动执行的事件处理器。登录管理员打开包含该评论的页面后，脚本可借用其会话上传含Web Shell的插件，进而在服务器执行命令。漏洞主要影响区块主题及部分经典主题，评论需先出现在页面上；文章称尚无被用于攻击的迹象。WordPress已在7.1.1等安全版本中修复。

原文：https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html

### 07 Zyxel和Veeam漏洞正被积极利用，可获得命令和SYSTEM权限访问

**公开时间：**2026年09月22日 13:31

AI 解读

CISA将影响Zyxel GS1900系列交换机的CVE-2026-7273列入已知被利用漏洞目录。该漏洞位于CGI程序，属于基于栈的缓冲区溢出，局域网内未认证攻击者可通过特制HTTP请求执行操作系统命令。GreyNoise称，自2026年8月17日起疑似中文攻击者已利用该漏洞，从48个国家的996台交换机窃取配置、哈希化根凭据和网络信息，并通过TFTP运行定制采集脚本。与此同时，Arctic Wolf报告Veeam Agent for Windows的CVE-2026-32996正遭利用，具备本地访问权限者可利用服务会话UID处理缺陷取得SYSTEM级控制。

原文：https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html

### 08 伪造的 LastPass Authenticator 安装程序滥用微软签名驱动，终止杀毒软件和 EDR 工作者

**公开时间：**2026年09月22日 01:31

AI 解读

LastPass与Delphos Labs披露，GitHub上的假冒LastPass Authenticator安装程序利用经微软硬件兼容性计划签名的内核驱动终止145个安全进程，进而窃取浏览器密码、加密货币钱包及Discord、Steam、Telegram会话等数据。该驱动实为CnCrypt产品CcProtect.sys的改名版本，通过DLL侧加载与BYOVD技术获取SYSTEM权限，在内核层关闭杀软和EDR，且因重命名产生新哈希而未被微软易受攻击驱动阻止列表拦截。微软认为该非自家组件不构成安全漏洞。LastPass称其系统未受影响，攻击者仅冒用其名。该载荷每次重启都会重新运行，应视为内核级入侵。

原文：https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html

### 09 Contagious Interview”攻击活动入侵3万台设备，窃取1071万美元加密货币

**公开时间：**2026年09月22日 01:19

AI 解读

联合网络安全通报称，朝鲜关联组织自至少2022年起通过领英等平台冒充雇主，以高薪工作和编程测试诱骗网页设计师、工程师及加密货币、区块链和Web3从业者，触发BeaverTail、InvisibleFerret等恶意软件感染链，获取持久远程访问并窃取数据。Contagious Interview已影响逾100个国家至少3万台设备，从7000多个加密钱包窃取账户凭据或资金，涉案加密货币价值至少1071万美元；感染还可能被用于渗透受害者所在组织、窃取知识产权和横向活动。报告同时披露，相关朝鲜IT工人通过虚假身份及代理人绕过制裁、身份核验和地域招聘限制。

原文：https://thehackernews.com/2026/09/contagious-interview-campaign.html

### 10 谷歌因与位置数据相关的 GDPR 违规被罚款 4.03 亿欧元

**公开时间：**2026年09月22日 00:57

AI 解读

爱尔兰数据保护委员会认定，Google在2018年5月至2020年2月期间通过Web与应用活动、位置记录和位置精度功能处理用户位置数据时违反GDPR。前两项涉及处理缺乏合法性、公平性和透明度，并且保存时间超过必要期限；位置精度功能则未能证明处理具备合法、公平、透明基础，违反透明度和问责要求。监管机构认为，这可能使用户不知情地被用于广告影响或兴趣推断，并削弱其对个人数据的控制。Google被处以4.03亿欧元罚款，并须在六个月内使相关处理合规；罚款仍待爱尔兰法院确认，Google可提出上诉。

原文：https://thehackernews.com/2026/09/google-fined-403-million-over-gdpr.html

### 11 WordPress 发布补丁，修复可在部分服务器上实现代码执行的严重漏洞

**公开时间：**2026年09月22日 00:00

AI 解读

WordPress披露并修复了编号CVE-2026-87902的严重漏洞，CVSS评分9.2，影响4.7.0至7.1.1版本。未登录攻击者可利用页面模板文件选择逻辑中未过滤的路径穿越值，使站点加载主题目录外的PHP文件；若服务器已有可被利用的PHP文件，部分环境可能进一步执行攻击者代码，权限通常为Web服务器账户权限。漏洞修复于9月22日发布，覆盖仍受支持的各版本分支。截至当日，暂无在攻击中被利用的报告，也未列入美国CISA已知被利用漏洞目录。

原文：https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html

### 12 Check Point 警告：管理服务器零日漏洞遭定向攻击利用

**公开时间：**2026年09月22日 00:00

AI 解读

Check Point称，攻击者于2026年7月23日在少数针对性攻击中利用Security Management Server零日漏洞CVE-2026-93616。该漏洞存在于管理服务器Web服务的路径遍历机制，攻击者只需能访问该服务即可在无需登录的情况下上传并运行脚本，CVSS评分为9.8；厂商未披露目标、攻击者身份及后续行为。另有证据显示，自9月12日起，攻击者尝试利用9月9日修复的VPN漏洞CVE-2026-85102攻击Spark防火墙客户，但尚无证据表明相关尝试成功。

原文：https://thehackernews.com/2026/09/check-point-warns-of-management-server.html

### 13 微软关停 EvilTokens 设备代码钓鱼服务，该服务与 1.2 万起邮箱入侵事件有关

**公开时间：**2026年09月22日 00:00

AI 解读

微软宣布在美国弗吉尼亚东区联邦法院授权下取缔EvilTokens设备代码钓鱼服务，并将其开发和运营者追踪为Storm-2992；伦敦警方于2026年9月11日逮捕两名嫌疑人。该平台被指与约1.2万起邮箱入侵有关，利用OAuth 2.0设备授权流程诱导受害者在微软官方页面输入设备代码，使攻击者获得访问和刷新令牌，进而窃取邮件、建立隐藏规则或维持长期访问。平台还以AI分析邮箱、识别付款和可信关系、筛选诈骗目标并生成冒充邮件，将账户接管、邮箱分析和商业邮件欺诈工具整合为商业化服务。

原文：https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html

### 14 恶意 npm 软件包伪装成 Twilio 漏洞赏金探测工具，可窃取凭证

**公开时间：**2026年09月22日 00:00

AI 解读

研究人员披露，npm恶意包“tw-pkgprobe-7731”伪装成面向Twilio开发者的授权漏洞赏金安全探针，2026年8月中旬由账号“twdepprobe7731”发布，并在约45分钟内连续推出11个版本。它会检测Twilio开发环境，提取环境变量、挂载信息及系统配置并通过Webhook外传；部分版本搜索Twilio账户目录、扫描npm依赖并植入文件，1.0.4还窃取ACCOUNT\_SID和AUTH\_TOKEN，可能导致凭据及计费、通信权限遭滥用。末期版本又回退部分功能并探测Twilio主机及AWS元数据。其行为不符合Twilio漏洞研究指南，研究人员认为具有恶意意图，但攻击者目标尚不明确且技术复杂度较低。

原文：https://thehackernews.com/2026/09/malicious-npm-package-poses-as-twilio.html

### 15 研究人员公开 BigDiskBuster 零日漏洞 PoC，可阻止 Microsoft Defender 更新

**公开时间：**2026年09月22日 00:00

AI 解读

9月19日，研究人员Abdelhamid Naceri在GitHub发布BigDiskBuster零日概念验证工具，可监视Defender更新目录，在更新下载时创建填满系统盘剩余空间的隐藏临时文件，使平台或病毒特征更新失败；工具随后会释放空间并等待下一次更新，还会占用MRT.exe句柄，阻止Windows Update替换该组件。Defender本身仍可运行，但检测内容可能过时。目前该问题没有补丁、CVE或微软公告，相关行为尚未获独立研究人员确认；其作者称工具适用于所有受支持的Windows版本但仍存在缺陷。该技术不同于微软5月修复的UnDefend漏洞，是否已被覆盖尚不明确。

原文：https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html

### 16 Bifrost AI Gateway 严重漏洞允许攻击者无需凭据执行命令

**公开时间：**2026年09月22日 00:00

AI 解读

开源AI网关Bifrost存在严重漏洞CVE-2026-90898（CVSS 9.8）：在HTTP传输版本2.1.0之前且管理认证默认关闭时，未认证攻击者可通过一次POST请求向/api/mcp/client注册stdio型MCP客户端，网关会立即以进程用户身份执行指定命令。由于网关保存各LLM提供商的API密钥，攻击者可能进一步获取这些凭据。官方Docker镜像将管理接口绑定至0.0.0.0，外部暴露风险更高。另有CVE-2026-86242可通过注册远程插件触发代码加载或服务器端请求伪造；两者根因均为管理API默认未认证。

原文：https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html

### 17 AI 代理正在改写横向移动规则

**公开时间：**2026年09月22日 00:00

AI 解读

文章称，AI代理的风险由访问权限与自主性共同决定：代理能够持续尝试多条路径、切换工具、发现凭据并跨越信任边界，因此其实际影响范围不止于直接授权，还包括经身份、工具、存储凭据和服务账户串联出的间接路径。文中援引的案例显示，代理曾跨云、Kubernetes、内部网络和代码仓库行动，并通过共享基础设施实现通信。由于代理执行合法任务时也可能产生类似横向移动的行为，单凭移动本身难以判断意图；代理目的、所有者及完整身份链成为理解其行为和风险的关键。

原文：https://thehackernews.com/2026/09/ai-agents-are-rewriting-rules-of.html

### 18 CVSS 10.0 新漏洞：VeloCloud Orchestrator 在基于证书的部署中正被积极利用  备选：VeloCloud Orchestrator 曝 CVSS 10.0 新漏洞，基于证书的环境已遭在野利用

**公开时间：**2026年09月22日 00:00

AI 解读

Arista于2026年9月22...