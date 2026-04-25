---
title: 安全简讯（2026.04.24）
url: https://mp.weixin.qq.com/s/s1AXhLiZWCmSjMYAfGNSLQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:35:44.489030
---

# 安全简讯（2026.04.24）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZrxT3Ytj8JniaVZTIOzlxSsSjyt5Y4vEgCQTtv6JeoOr4djVFpBRvMdiaRS02HlKPdCxdiaSOPic9dIBS4yc7CJ9IMjSGaH4dHthGp0/0?wx_fmt=jpeg)

# 安全简讯（2026.04.24）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. WordPress Breeze Cache严重漏洞遭黑客利用**

4月23日，黑客正在积极利用WordPress Breeze Cache缓存插件中的一个严重安全漏洞，该漏洞允许未经身份验证的攻击者向服务器上传任意文件。该漏洞被追踪为CVE-2026-3844，严重性评分为9.8分（满分10分）。安全公司Wordfence已检测到超过170次针对该漏洞的实际攻击尝试，表明其已被黑客在真实网络环境中大规模利用。Breeze Cache插件由Cloudways开发，活跃安装量超过40万个。该插件的主要功能是通过缓存、文件优化和数据库清理来提高网站性能和加载速度。该漏洞由安全研究员Hung Nguyen发现并报告，其根源在于插件中“fetch\_gravatar\_from\_remote”函数缺少对上传文件的类型验证，导致未经身份验证的攻击者可以向服务器上传任意恶意文件，进而实现远程代码执行并完全接管目标网站。CVE-2026-3844影响Breeze Cache的所有版本，包括2.4.4及更早版本。Cloudways已在本周早些时候发布了2.4.5版本，修复了这一安全漏洞。

https://www.bleepingcomputer.com/news/security/hackers-exploit-file-upload-bug-in-breeze-cache-wordpress-plugin/

**2. Bitwarden CLI npm包遭供应链攻击**

4月23日，Bitwarden CLI的npm分发渠道曾一度被攻破，攻击者将恶意版本的@bitwarden/cli包（版本2026.4.0）上传至npm仓库，该包包含一个能够窃取凭证并自我传播的有效载荷。该恶意版本于2026年4月22日美国东部时间下午5:57至晚上7:30期间可供下载，随后被删除。Bitwarden证实了此次事件，并表示泄露仅影响了CLI的npm分发渠道，且仅限于下载了恶意版本的用户。调查未发现任何证据表明最终用户存储库数据、生产数据或生产系统遭到破坏。一旦发现问题，Bitwarden立即撤销了被盗用的访问权限，弃用了恶意npm版本，并启动了补救措施。该恶意软件能够收集受害系统中的npm令牌、GitHub认证令牌、SSH密钥以及AWS、Azure和Google Cloud的云凭证。该恶意软件还具有自我传播能力，它能够利用窃取的npm凭据识别受害者有权修改的软件包，并将恶意代码注入其中。Socket还观察到有效载荷针对CI/CD环境，试图收集可用于扩展攻击的密钥。

https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/

**3. Trigona勒索软件启用定制数据窃取工具**

4月23日，近期发现的Trigona勒索软件攻击中，攻击者使用了一款名为“uploader\_client.exe”的自定义命令行工具来窃取数据。这款定制工具能够更快、更高效地从受感染环境中窃取数据，同时规避安全解决方案的检测。赛门铁克研究人员认为，攻击者转向使用定制工具，表明他们正在投入时间和精力开发专有恶意软件，以期在攻击的关键阶段保持较低的可见度，从而避免使用Rclone和MegaSync等公开工具，这些工具通常会触发安全警报。该定制工具连接到一个硬编码的服务器地址，在性能与规避能力上做了多项优化：支持每个文件同时建立五个连接，通过并行上传实现更快的数据泄露；每传输2GB流量后轮换TCP连接，以规避网络监控；可选择性地筛选文件类型，排除大型、低价值的媒体文件；使用身份验证密钥限制外部人员对被窃数据的访问。在一次已记录的攻击事件中，该工具被用来窃取网络驱动器上的高价值文档，例如发票和PDF文件。

https://www.bleepingcomputer.com/news/security/trigona-ransomware-attacks-use-custom-exfiltration-tool-to-steal-data/

**4. UNC6692借Teams发起社交工程攻击**

4月23日，此前未记录在案的威胁活动集群UNC6692被发现利用Microsoft Teams进行社交工程攻击，在受感染的主机上部署名为SNOW的定制模块化恶意软件套件。与近年来许多其他入侵事件类似，UNC6692严重依赖冒充IT服务台员工，诱骗受害者接受来自其组织外部账户的Microsoft Teams聊天邀请。该集群已被证实与一场大规模电子邮件轰炸活动有关，攻击者首先通过大量垃圾邮件淹没目标用户的收件箱制造虚假紧迫感，随后通过Teams冒充IT支持团队，声称可协助解决邮件问题。ReliaQuest报告显示，攻击者正利用此方法针对企业高管和高级员工以获取企业网络初始访问权限，进而进行数据窃取、横向移动、勒索软件部署和敲诈勒索。UNC6692在获得初始访问后还执行了横向移动（扫描135/445/3389端口）、通过PsExec建立会话、利用WMT提取LSASS进程内存进行权限提升，以及使用Pass-The-Hash技术横向移动到域控制器，下载FTK Imager捕获Active Directory数据并通过LimeWire泄露。

https://thehackernews.com/2026/04/unc6692-impersonates-it-helpdesk-via.html

**5. Checkmarx KICS Docker镜像与VSCode扩展遭入侵**

4月23日，黑客入侵了Checkmarx KICS分析工具的Docker镜像、VSCode和Open VSX扩展，旨在从开发人员环境中窃取敏感数据。Socket在收到Docker关于恶意镜像被推送到官方checkmarx/kics Docker Hub仓库的警报后展开调查，发现此次入侵不仅限于被植入木马的Docker镜像，还波及VSCode和Open VSX扩展。这些扩展下载了一个隐藏的“MCP插件”功能，该功能用于获取窃取秘密的恶意软件。Socket发现，“MCP插件”功能是从硬编码的GitHub URL下载的“多阶段凭证窃取和传播组件”，该恶意软件专门针对KICS处理的数据，包括GitHub令牌、云凭证、npm令牌、SSH密钥、Claude配置和环境变量。需要注意的是，Docker标签被暂时重定向到一个恶意摘要，因此影响取决于镜像被拉取的时间。TeamPCP黑客公开声称对此次攻击负责。Checkmarx已发布安全公告，确认所有恶意程序已删除，泄露的凭据已被撤销并轮换，目前正与外部专家合作调查。建议受影响用户阻止访问特定恶意域名，使用固定SHA值，恢复到已知安全版本。

https://www.bleepingcomputer.com/news/security/new-checkmarx-supply-chain-breach-affects-kics-analysis-tool/

**6. CISA紧急敦促政府机构修补Defender零日漏洞**

4月23日，美国网络安全和基础设施安全局（CISA）已下令联邦机构在两周内采取措施，保护其Windows系统免受一个已被用于零日攻击的Microsoft Defender权限提升漏洞的侵害。该漏洞被追踪为CVE-2026-33825，代号“BlueHammer”，属于高危级别。它允许低权限的本地威胁行为者利用访问控制粒度过细的弱点，在未打补丁的设备上获得SYSTEM最高权限。微软于4月14日在“补丁星期二”活动中修复了该漏洞。此前一周，安全研究员“Chaotic Eclipse”为抗议微软安全响应中心（MSRC）的漏洞披露流程，不仅将漏洞命名为BlueHammer，还公开发布了概念验证利用代码。更为严峻的是，Huntress Labs安全研究人员于4月16日披露，已有攻击者利用这些零日漏洞发动实际攻击，且显示出“实际操作键盘的威胁行为者活动”的明确证据。调查发现，受感染环境存在可疑的FortiGate SSL VPN访问记录，包括一个位于俄罗斯的源IP地址，并在其他地区也发现了可疑基础设施。

https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-microsoft-defender-flaw-exploited-in-zero-day-attacks/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

启明星辰安全简讯

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过