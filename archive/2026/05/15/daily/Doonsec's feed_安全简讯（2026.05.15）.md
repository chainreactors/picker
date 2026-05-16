---
title: 安全简讯（2026.05.15）
url: https://mp.weixin.qq.com/s/_Phb-Ya0yUfuG37ucCLPzg
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:12:57.785382
---

# 安全简讯（2026.05.15）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309Zrw4ndwZzHLAuydQKibIwiaMvDv3OrZC2qzcMYGBvnWRrp2UnhnLBRd2IicJcUh0nqTw9hhjqicEEcfB2mqetngeU9ibChrnDNa9drys/0?wx_fmt=jpeg)

# 安全简讯（2026.05.15）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. Linux曝新高危内核提权漏洞“Fragnasia”**

5月14日，Linux发行版正在紧急推出补丁，以修复一个名为“Fragnasia”的新高危内核权限提升漏洞，编号为CVE-2026-46300。该漏洞源于Linux XFRM ESP-in-TCP子系统中的一个逻辑错误，可使非特权本地攻击者通过向只读文件的内核页面缓存写入任意字节，从而获得root权限，并以最高权限运行恶意代码。漏洞由Zellic安全主管William Bowling发现，他还发布了一款概念验证利用程序，该程序利用内核中的内存写入原语破坏/usr/bin/su二进制文件的页面缓存，进而获取具有root权限的shell。Bowling指出，Fragnasia属于上周披露的Dirty Frag漏洞类别，影响2026年5月13日之前发布的所有Linux内核。与依赖两个独立内核缺陷（CVE-2026-43284和CVE-2026-43500）的Dirty Frag不同，Fragnasia是一个独立的漏洞，不需要任何竞争条件即可实现对只读文件页面缓存的任意字节写入。两者的缓解措施相同。建议Linux用户尽快应用内核更新。对于无法立即修补的设备，可通过删除易受攻击的内核模块进行临时缓解，但此举会破坏AFS分布式网络文件系统和IPsec VPN功能。

https://www.bleepingcomputer.com/news/security/new-fragnesia-linux-flaw-lets-attackers-gain-root-privileges/

**2. 黑客威胁泄露Mistral AI源代码，索要2.5万美元**

5月14日，近期，名为TeamPCP的黑客组织声称成功入侵了法国人工智能公司Mistral AI的代码库管理系统，并窃取了近450个存储库、总计约5GB的内部源代码及相关数据。该组织在黑客论坛上公开叫卖这些数据，设定了2.5万美元的“立即购买价”，并威胁称，如果一周内找不到买家，将把全部文件免费泄露到论坛上。同时，TeamPCP表示愿意谈判，潜在买家可以提交自认为合理的报价，且数据仅售予一人。Mistral AI由前谷歌DeepMind和Meta研究人员创立，专注于开源及专有的开放权重大型语言模型。该公司证实，此次事件源于一起名为“Mini Shai-Hulud”的软件供应链攻击。攻击者通过窃取CI/CD凭证和合法工作流程，首先入侵了TanStack和Mistral AI的官方软件包，随后将影响扩散至npm和PyPI注册表上的数百个其他项目，包括UiPath、Guardrails AI和OpenSearch等。Mistral AI承认，黑客确实短暂污染了其部分SDK软件包，但强调法证调查表明，受影响的数据不属于核心代码库，公司的托管服务、管理用户数据以及任何研究和测试环境均未受到损害。

https://www.bleepingcomputer.com/news/security/teampcp-hackers-advertise-mistral-ai-code-repos-for-sale/

**3. WordPress插件漏洞致20万网站面临管理员劫持风险**

5月14日，近日，一款名为Burst Statistics的WordPress分析插件被曝存在严重身份验证绕过漏洞，攻击者可借此无需密码即可获取网站的管理员级别访问权限。该插件主打隐私保护，作为Google Analytics的轻量级替代品，已在超过20万个WordPress网站上部署。漏洞编号为CVE-2026-8181，于2026年4月23日随插件3.4.0版本引入，并在后续的3.4.1版本中依然存在。据安全公司Wordfence披露，该漏洞于5月8日被发现，其核心问题在于插件错误地处理了“wp\_authenticate\_application\_password()”函数的返回值，将“WP\_Error”对象误判为身份验证成功，同时在特定条件下对返回“null”的情况也未能正确拒绝，从而允许未经身份验证的攻击者在REST API请求期间冒充已知管理员用户。Wordfence警告称，该漏洞预计将成为攻击者的重点目标，其检测系统在过去24小时内已拦截超过7400次针对该漏洞的攻击，表明恶意活动已大规模展开。对此，Burst Statistics已于2026年5月12日发布修复版本3.4.2，强烈建议用户立即升级或暂时禁用该插件。

https://www.bleepingcomputer.com/news/security/hackers-exploit-auth-bypass-flaw-in-burst-statistics-wordpress-plugin/

**4. 初始访问代理KongTuke转战Teams**

5月14日，初始访问代理（Initial Access Broker，IAB）KongTuke近期改变了攻击策略，将社交工程攻击的主战场转移至Microsoft Teams，声称只需五分钟即可获得对企业网络的持久访问权限。该组织通常将入侵所得的公司网络访问权出售给勒索软件运营商，后者随后部署文件窃取和数据加密恶意软件。据ReliaQuest研究人员观察，这是KongTuke首次使用协作平台进行初始访问，此前该组织仅依赖基于网页的“FileFix”和“CrashFix”诱饵。此次Teams活动是对原有方法的补充而非替代，且至少从2026年4月起便已活跃。KongTuke轮流使用五个Microsoft 365租户以规避封锁，并利用Unicode空格技巧伪造显示名称，使伪装更显可信。攻击过程中，恶意PowerShell命令从Dropbox下载包含可移植WinPython环境的ZIP存档，进而启动ModeloRAT。该恶意软件具备系统信息收集、屏幕截图捕获及文件窃取功能。值得关注的是，本次使用的ModeloRAT版本相较以往有显著改进：采用更具弹性的命令与控制（C2）架构、内置多条独立访问路径、扩展了持久性机制。

https://www.bleepingcomputer.com/news/security/kongtuke-hackers-now-use-microsoft-teams-for-corporate-breaches/

**5. NGINX曝18年高危漏洞，可致拒绝服务与远程代码执行**

5月14日，自主扫描系统发现，广泛使用的NGINX开源网络服务器中存在一个存在约18年的高危漏洞，追踪编号为CVE-2026-42945，CVSS评分高达9.2。该漏洞位于ngx\_http\_rewrite\_module模块中，属于堆缓冲区溢出问题，影响NGINX版本0.6.27至1.30.0。NGINX为全球约三分之一的头部网站提供支持，被云服务商、银行、电商平台及Kubernetes集群广泛采用。据人工智能安全公司DepthFirst AI的研究人员解释，当NGINX配置同时使用“rewrite”和“set”指令时可能触发该漏洞。研究人员演示了通过精心构造的HTTP请求实现未经身份验证的代码执行，破坏相邻内存池结构并覆盖清理处理程序指针，最终强制NGINX执行“system()”命令。值得注意的是，即使在地址空间布局随机化（ASLR）内存防护功能开启的情况下，漏洞利用仍具有可行性。此外，NGINX的多进程架构反而降低了利用难度：工作进程崩溃后，主进程会生成一个内存布局完全相同的新进程，攻击者可以反复尝试直至成功，甚至通过逐字节覆盖指针来泄露ASLR信息。

https://www.bleepingcomputer.com/news/security/18-year-old-nginx-vulnerability-allows-dos-potential-rce/

**6. CISA将Catalyst SD-WAN的一个漏洞加入KEV目录**

5月14日，美国网络安全和基础设施安全局（CISA）近日将思科Catalyst SD-WAN中的一个严重漏洞（编号CVE-2026-20182）纳入其已知利用漏洞（KEV）目录。该漏洞的CVSS评分为满分10.0，影响Catalyst SD-WAN控制器（vSmart）和管理器（vManage）中的SD-WAN控制连接握手及对等身份验证机制。由于受影响系统中的对等身份验证机制无法正常工作，未经身份验证的远程攻击者可发送精心构造的请求，利用验证失败绕过身份验证，从而获得管理权限。成功利用后，攻击者能够以内部高权限非root用户账户登录控制器，进而访问NETCONF并操纵整个SD-WAN网络架构的配置。思科PSIRT于2026年5月检测到该漏洞已被有限利用，并紧急敦促客户升级至已修复的软件版本。CISA已命令联邦机构在2026年5月17日之前完成修复。

https://securityaffairs.com/192157/hacking/u-s-cisa-adds-a-flaw-in-cisco-catalyst-sd-wan-to-its-known-exploited-vulnerabilities-catalog.html

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