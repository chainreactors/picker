---
title: 工信部CSTIS发布关于防范Remcos RAT恶意软件新变种的风险提示；内核级BYOVD攻击再现，威胁超百款安全产品 | 牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651133585&idx=2&sn=3253dd09cf450ad4ac0083d84fb9100f&chksm=bd15a6428a622f543d707590fa5672e1ee4b2f5c75bacce3d84168cc509c8cbcab68084fa011&scene=58&subscene=0#rd
source: 安全牛
date: 2024-11-27
fetch_date: 2025-10-06T19:18:05.065160
---

# 工信部CSTIS发布关于防范Remcos RAT恶意软件新变种的风险提示；内核级BYOVD攻击再现，威胁超百款安全产品 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCoIlP51FfmZtibPkdF5A11asW6AYJtWpEzticia4EwhvSicTdUTkdC5ibOSKfLMcAFgWA2mPkgT1hCqLQ/0?wx_fmt=jpeg)

# 工信部CSTIS发布关于防范Remcos RAT恶意软件新变种的风险提示；内核级BYOVD攻击再现，威胁超百款安全产品 | 牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•以可信安全促数据要素流通，《可信数据空间发展行动计划（2024—2028年）》发布

•工信部CSTIS发布关于防范Remcos RAT恶意软件新变种的风险提示

•内核级BYOVD攻击再现，威胁超百款安全产品

•全球最大线上博彩服务商IGT遭勒索攻击，关键系统紧急下线

•PyPI平台现高仿AI接口包，1700余次下载埋下安全隐患

•暗网信用卡黑市PopeyeTools被捣毁，22.7万人隐私信息遭窃取

•可轻松突破SSO安全防线，跨IdP仿冒技术成为新型攻击手段

•NVIDIA核心组件曝重大安全隐患，无需特权即可实施远程攻击

•Fortinet  VPN曝重大设计缺陷，暴力破解行为或难以被追踪

•Google  OSS-Fuzz首批发现26个新开源漏洞，模糊测试进入AI时代

•微软将发布Quick  Machine Recovery工具，可远程修复无法启动设备

**特别关注**

**以可信安全促数据要素流通，《可信数据空间发展行动计划（2024—2028年）》发布**

为引导和支持可信数据空间发展，促进数据要素规模化流通共享使用，加快构建以数据为关键要素的数字经济，近日，国家数据局印发《可信数据空间发展行动计划（2024—2028年）》（以下简称《行动计划》）。

《行动计划》提出到2028年，可信数据空间运营、技术、生态、标准、安全等体系取得突破，建成100个以上可信数据空间，基本建成广泛互联、资源集聚、生态繁荣、价值共创、治理有序的可信数据空间网络，各领域数据开发开放和流通使用水平显著提升，初步形成与我国经济社会发展水平相适应的数据生态体系。

《行动计划》主要包括三大行动。一是**实施可信数据空间能力建设行动**，通过构建可信管控能力，提高资源交互能力，强化价值共创能力，打造可信数据空间的核心能力体系。二是**开展可信数据空间培育推广行动**，主要是布局企业、行业、城市、个人、跨境五类可信数据空间建设和应用推广，探索各类数据空间的场景创新、模式创新、机制创新。三是**推进可信数据空间筑基行动**，围绕制订关键标准、攻关核心技术、完善基础服务、强化规范管理、拓展国际合作五个方面，全面夯实可信数据空间发展基础。

原文链接：

https://mp.weixin.qq.com/s/DRQvoYdkVMKVtmepri3kyQ

**工信部CSTIS发布关于防范Remcos RAT恶意软件新变种的风险提示**

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）监测到一种Remcos RAT恶意软件新变种持续活跃，主要以Windows用户为攻击目标，可能导致敏感信息泄露、勒索攻击、业务中断等风险。

Remcos RAT最早出现于2016年，是一种使用高级技术感染 Windows 系统、窃取数据并获得远程控制权的远程访问木马。该恶意软件主要利用欺骗性钓鱼邮件附件（如OLE Excel格式的订单通知文档等），诱骗用户打开文件并利用已知漏洞下载、部署、执行恶意代码，实现对目标系统的远程控制，向控制端服务器发送包含受感染系统用户、网络和版本信息的注册数据包，并接收用于收集信息、执行命令、操作文件、键盘记录、屏幕录像的命令。在感染目标系统过后，Remcos RAT新变体采用多层混淆、修改注册表添加自启动项、反调试技术、进程空洞化（Process Hollowing，恶意软件将合法进程内存清空，再注入恶意代码，伪装成合法程序并隐蔽运行）等多种持久性机制和先进的反分析技术以逃避检测，实现长期驻留于已感染系统中。

建议相关单位和用户立即组织排查，及时更新防病毒软件，实施全盘病毒查杀，警惕来源不明的邮件或文档，并可通过保持软件更新，及时修复安全漏洞，定期备份数据等措施，防范网络攻击风险。

相关链接：

https://mp.weixin.qq.com/s/unSjYE6oI-JUhL3U7p4qQw

**网络攻击**

**内核级BYOVD攻击再现，威胁超百款安全产品**

近日，网络安全公司Trellix研究人员发现了一起新型攻击活动，攻击者利用Avast反rootkit驱动程序的旧版本漏洞，通过"自带易受攻击驱动程序"（BYOVD）方式，成功关闭目标系统上的安全产品。

这款恶意软件是一个未归类家族的杀毒软件终止器（AV Killer）变种，内置了142个来自不同厂商的安全进程名称列表。攻击链程序会将名为"ntfs.bin"的易受攻击驱动程序投放到Windows用户默认文件夹中，随后通过服务控制（sc.exe）创建"aswArPot.sys"服务并注册驱动程序。

由于该驱动程序可在内核级别运行，因此能访问操作系统的关键部分。恶意软件会将其硬编码的进程列表与系统活动进程快照进行比对，一旦发现匹配项，就会创建一个句柄引用已安装的Avast驱动程序，并利用DeviceIoControl API发送必要的IOCTL命令来终止目标进程。

受影响的安全产品包括McAfee、Symantec（Broadcom）、Sophos、Avast、Trend Micro、Microsoft Defender、SentinelOne、ESET和BlackBerry等知名厂商的超百款解决方案。一旦防护被停用，恶意软件就可以在不触发警报或被拦截的情况下执行恶意活动。值得注意的是，类似的攻击手法目前已在多起勒索软件攻击中被发现。

原文链接：

https://www.bleepingcomputer.com/news/security/hackers-abuse-avast-anti-rootkit-driver-to-disable-defenses/

**全球最大线上博彩服务商IGT遭勒索攻击，关键系统紧急下线**

国际游戏科技公司（IGT）于11月17日遭遇到一起网络攻击事件，并立即启动了事件响应程序。IGT是全球领先的博彩技术供应商，主要生产老虎机等博彩设备。

根据IGT向美国证券交易委员会（SEC）提交的说明，未经授权的第三方获取了该公司部分系统的访问权限，导致其内部信息技术系统和应用程序出现中断。公司在发现问题后迅速激活了网络安全事件响应计划，并在外部顾问的支持下展开调查，以评估和修复未经授权的活动。同时，公司主动使部分受影响系统离线以加强保护。

虽然IGT尚未确定此次网络攻击的完整影响范围，但已开始与利益相关者沟通并实施业务连续性计划，以减轻服务中断带来的影响。尽管公司没有公开攻击的具体细节，但从其所采取的应对措施来看，这很可能是一起勒索软件攻击事件。

原文链接：

https://securityaffairs.com/171311/hacking/cyberattack-on-gambling-giant-igt.html

**PyPI平台现高仿AI接口包，1700余次下载埋下安全隐患**

研究人员近期发现，两个号称可以集成知名聊天机器人功能的Python包在向潜在数千名受害者传播信息窃取程序。这些攻击者正利用生成式AI的热度，瞄准那些技术经验较少、警惕性不足的开发者，诱使他们在未经严格审查的情况下下载这些开源Python代码包。

据Endor Labs创始工程师George Apostopoulos介绍，攻击者利用了AI服务需付费使用的特点，通过提供"免费访问"来吸引不谨慎的用户。大约在去年此时，一个用户名为"Xeroline"的账号在Python包索引（PyPI）上发布了两个自制包："gptplus"和"claudeai-eng"，分别号称提供OpenAI的GPT-4 Turbo和Claude的API访问功能。

这两个包虽然无法实现号称的功能，但提供了一个简单的替代机制用于与ChatGPT免费演示版交互，以此制造合法性表象。而在后台，这些程序会投送包含JarkaStealer的Java存档（JAR）文件。这两个恶意包在PyPI平台上存在了整整一年，直到最近被卡巴斯基研究人员发现并报告。在此期间，它们在30多个国家的Windows和Linux系统上被下载超过1700次。

原文链接：

https://www.darkreading.com/application-security/faux-chatgpt-claude-api-packages-jarkastealer

**暗网信用卡黑市PopeyeTools被捣毁，22.7万人隐私信息遭窃取**

美国司法部近日宣布成功查封黑市交易平台PopeyeTools，并对其三名管理员提起刑事诉讼。他们被控共谋实施访问设备欺诈、非法交易访问设备，以及教唆他人提供访问设备等罪名。

PopeyeTools自2016年以来一直在暗网上运营，专门销售被盗信用卡信息和网络犯罪工具。美国司法部透露，该平台提供超过22.7万人的银行账户、信用卡和借记卡信息及相关交易数据，累计获利至少170万美元。执法部门已从与嫌疑人有关的账户中查封了约28.3万美元的加密货币，并接管了相关运营域名。

美国司法部刑事司司长Nicole M. Argentieri表示："这个长期存在的在线黑市主要销售用于实施网络犯罪（包括勒索软件攻击和金融欺诈）的非法商品和服务。此次查封PopeyeTools域名、起诉其运营者并扣押加密货币的行动，展示了司法部门打击网络犯罪的全方位策略。"

原文链接：

https://securityaffairs.com/171319/cyber-crime/doj-seized-credit-card-marketplace-popeyetools.html

**可轻松突破SSO安全防线，跨IdP仿冒技术成为新型攻击手段**

网络安全公司Push Security的研究人员最近发现了一种名为"跨IdP仿冒"的新型攻击技术，攻击者可以在不破坏企业主要身份提供商（IdP）的情况下，劫持单点登录（SSO）流程，实现对下游应用程序的未经授权访问。

据介绍，跨IdP仿冒攻击利用SSO配置中的弱点，使攻击者能够创建模仿目标组织域名的欺诈性IdP账户。通过这些虚假账户，攻击者可以绕过主IdP的防御机制，访问下游应用程序。近期已出现多起相关案例，其中一位研究人员利用Zendesk的漏洞，成功创建了与多个合法公司域名关联的虚假Apple SSO账户，进而获取了包括Slack在内的各种连接应用的未经授权访问权限。

安全研究人员表示，跨IdP仿冒可以被比作加强版的幽灵登录。这种攻击方法绕过了保护主IdP账户的传统安全措施；如果攻击者能够为用户的域名创建新的IdP账户，那么主IdP账户的安全程度就变得无关紧要了。而且这类攻击通常不需要用户交互，而是利用配置漏洞。

为降低跨IdP仿冒攻击的风险，Push Security建议组织实施自动化邮件警报以监控未经授权的IdP连接，限制个人账户向企业账户的转换，并在添加新SSO方法时强制要求通过原始方法重新验证。

原文链接：

https://www.sdxcentral.com/articles/stringerai-announcements/push-security-highlights-cross-idp-impersonation-threat-to-sso-security/2024/11/

**漏洞预警**

**NVIDIA核心组件曝重大安全隐患，无需特权即可实施远程攻击**

NVIDIA近日发布安全公告，披露了其Base Command Manager软件中存在的一个严重漏洞（CVE-2024-0138）。该漏洞位于CMDaemon组件中，由于缺少身份验证机制，可能导致远程代码执行、拒绝服务、权限提升、信息泄露和数据篡改等多重安全风险。

值得注意的是，攻击者无需用户交互或特殊权限就能远程利用该漏洞，这使其具有极高的危险性。一旦被成功利用，攻击者可以远程执行任意代码、中断服务、提升用户权限、获取敏感信息或篡改数据。

受影响的版本包括NVIDIA Base Command Manager 10.24.09，NVIDIA已在10.24.09a版本中修复了该漏洞。该公司确认10.24.07及更早版本不受此漏洞影响。

为解决这一问题，NVIDIA建议用户更新所有头节点和软件映像上的CMDaemon组件。更新后，系统需要重启或与更新后的软件映像重新同步，以确保修复完全生效。NVIDIA同时建议用户通过NVIDIA产品安全页面及时了解最新的安全动态。

原文链接：

https://cybersecuritynews.com/nvidia-base-command-manager-vulnerability/

**Fortinet VPN曝重大设计缺陷，暴力破解行为或难以被追踪**

安全研究公司Pentera近日披露，Fortinet VPN服务器的日志记录机制存在设计缺陷，攻击者可利用该缺陷在暴力破解攻击中隐藏成功验证凭据的记录，使防御人员无法发现账号已被攻破。

据介绍，FortiClient VPN服务器的登录过程分为认证和授权两个阶段。只有当这两个阶段都完成时，系统才会记录成功登录。研究人员发现，失败的尝试会在认证阶段被记录，而成功的记录则在授权阶段生成。如果攻击者在认证阶段之后停止进程，VPN服务器将只记录失败的尝试，而不会记录成功的验证，这是因为进程没有继续到后续的授权步骤。这种情况下，事件响应团队无法判断暴力破解攻击是否成功，只能看到失败的进程日志。

虽然Fortinet管理员仍能通过失败的认证尝试发现设备正遭受暴力破解攻击并采取阻止措施，但他们无法知道攻击者是否已成功验证某些凭据。这些被验证的凭据可能被出售给其他威胁行为者，或在管理员警惕性降低时用于后续的网络入侵。

原文链接：

https://www.bleepingcomputer.com/news/security/fortinet-vpn-design-flaw-hides-successful-brute-force-attacks/

**产业动态**

**Google OSS-Fuzz首批发现26个新开源漏洞，模糊测试进入AI时代**

Google近日宣布，其开源模糊测试工具OSS-Fuzz在引入人工智能能力后，成功发现了26个新的开源项目漏洞，其中包括一个在OpenSSL库中存在了20年之久的缺陷。

在过去一年半时间里，Google不断改进其AI驱动的模糊测试框架，增加了自动修复编译问题和其他错误的功能，并能够在分类任何崩溃的同时持续运行最终目标。通过在大语言模型提示中自动生成更多相关上下文信息，降低了幻觉产生的可能性。这些改进使272个C/C++项目的代码覆盖率得到提升，新增覆盖代码超过37万行。

目前，Google的AI驱动OSS-Fuzz系统遵循四步流程：第一步，根据项目详细信息起草初始模糊测试目标；第二步，编译目标并由大语言模型分析和修复编译错误；第三步，运行模糊测试目标以识别和解决可能导致运行问题的问题；第四步，持续运行最终目标并使用大语言模型对崩溃进行分类以确定根本原因。

Google计划进一步完善AI驱动的OSS-Fuzz流程，使其更加自主，减少人工审查的需求。该框架自2024年1月已开源，其公共GitHub仓库中包含使用指南和已发现漏洞的详细信息。

原文链接：

https://www.scworld.com/news/googles-ai-powered-fuzzing-tool-discovers-26-new-vulnerabilities

**微软将发布Quick Machine Recovery工具，可远程修复无法启动设备**

微软在年度Ignite大会上宣布，将于明年初在Windows Insider Program中推出Quick Machine Recovery工具，并计划于2025年7月向安全产品生态系统合作伙伴提供私有预览版本。

该工具可通过定向Windows Update修复来实现对无法启动设备的远程恢复。此举是对今年早些时候因CrowdStrike Falcon更新失误导致的Windows大规模宕机事件的积极响应。

微软表示："这种远程恢复功能将帮助企业员工比过去更快地解决广泛性问题。"除了推出新工具，微软还在推进安全部署实践（Safe Deployment Practices）的实施，这包括反恶意软件供应商逐步推进安全产品更新，以及最小化更新不良影响等措施。

原文链接：

https://www.scworld.com/brief/new-microsoft-tool-allows-remote-fixes-for-unbootable-devices

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMnicXSRCtG4URyLibbqPegjnnibfRB0z4zIzwghbLOkV5fqGYM8vhuQdqw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=p...