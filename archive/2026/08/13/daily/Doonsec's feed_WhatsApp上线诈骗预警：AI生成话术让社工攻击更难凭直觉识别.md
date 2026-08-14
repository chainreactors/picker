---
title: WhatsApp上线诈骗预警：AI生成话术让社工攻击更难凭直觉识别
url: https://mp.weixin.qq.com/s/6BW_uUO493H60d2O4_TVJg
source: Doonsec's feed
date: 2026-08-13
fetch_date: 2026-08-14T03:58:36.992412
---

# WhatsApp上线诈骗预警：AI生成话术让社工攻击更难凭直觉识别

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AyvgaRYHWDb03prmrkq6yqr5kC6XRsSIUEU4nK17iaWjcbBkHZL78lUIjCciaibpX1wGkFQ2EMGRg3FRv6OcHLaXlx01Vg09VkzYLVia089naac/0?wx_fmt=jpeg)

# WhatsApp上线诈骗预警：AI生成话术让社工攻击更难凭直觉识别

汇能云安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/AyvgaRYHWDaIdxGFvFQRNI1slBUPTHewu7O71FFoia9hzfBdtoZ2baMeJ9d0SsfpmldUzrYicup7d188CYT46mQcPWdQEEibnKDjZYpKtpASg4/640?wx_fmt=jpeg&from=appmsg)

**8****月****13****日，星期四****，您好！中科汇能与您分享信息安全快讯：**

![](https://mmbiz.qpic.cn/mmbiz_gif/AyvgaRYHWDbaXwJTRgEC2wMeVZtfoicibAmia8laxb9C0S4SrZ13oo16ianWyARaibA5nTXrgTBPyicicWXaQFzicNiaTJwsicWTnQnKIQnZJ4boEJAm4/640?wx_fmt=gif&from=appmsg)

**01**

**Palo Alto Networks 一次修复 11 个漏洞：边界安全设备不能慢半拍**

Palo Alto Networks 发布安全公告，修复 11 个影响 PAN-OS、GlobalProtect App、Prisma Access Agent、Prisma Browser 等产品的新漏洞。**这批问题覆盖信息泄露、本地权限提升、缓冲区溢出、证书校验绕过和反篡改绕过，虽然不是每一项都等于远程接管，但放在防火墙、VPN、云接入代理这类位置上，风险权重会被放大。这个事件值得关注的点在于，出问题的不是普通办公软件，而是企业边界和远程接入链路。**很多攻击并不需要一开始就打到核心业务，只要先拿到边界设备、VPN 客户端或接入代理的薄弱点，就有机会继续摸到账号、内网和云资源。建议企业不要只看 “有没有被公开利用”，而是先确认资产清单里是否有 PAN-OS、GlobalProtect、Prisma Access 相关组件，尽快应用 8 月安全更新；同时检查管理面是否暴露公网，审计异常登录、配置变更、证书校验失败和终端代理异常行为。

**02**

**City-Forum 攻击 Salesforce 和 ServiceNow：SaaS 门户正在变成数据入口**

一个被称为 “City-Forum” 的新攻击活动正在全球范围内攻击 Salesforce Experience Cloud 站点和 ServiceNow Service Portals。报道提到，该活动持续时间较长，目标覆盖电信、银行、金融服务、企业软件厂商和公共部门门户，攻击者主要目的并不是炫技，而是静默获取门户里的业务数据。这类事件最容易被低估。**很多企业把 Salesforce、ServiceNow 当成 “外部系统” 或 “业务工具”，但现实是，它们往往连接客户资料、服务工单、内部流程、附件、审批和第三方集成。一旦门户权限配置不当、接口暴露或 Token 被滥用，攻击者拿到的就不是一个页面，而是一条通往业务数据的通道。**建议企业重点检查 Experience Cloud、Service Portal 的公开访问策略、匿名用户权限、对象级权限、API 调用日志和批量导出记录。涉及第三方插件、自动化流程和 Webhook 的，还要排查密钥是否长期未轮换。

**03**

**AI Agent 被用于攻击台湾政府网站：自动化攻击正在从辅助走向执行**

研究机构称疑似与中国有关的攻击者使用开源 AI Agent 攻击台湾政府网站和关键基础设施目标。**报道将其描述为一次高度自动化的网络行动，AI 工具参与侦察、漏洞利用、路径尝试等环节，这里需要保持克制：具体归因仍应以更多证据为准，但 “AI Agent 进入攻击链” 本身已经值得重视。过去企业谈 AI 安全，更多关注数据泄露、提示词注入、模型幻觉。但这类报道提醒我们，AI Agent 的风险不只在 “回答错”，还在 “能执行”。当 Agent 能调用工具、访问网络、写代码、跑扫描、整理结果，攻击效率和低成本试错能力都会被放大。**建议企业把 AI Agent 纳入安全边界管理：限制网络访问范围，隔离运行环境，控制工具调用权限，禁止默认携带生产凭据，并保留完整操作日志。对政府、能源、通信、金融等高价值目标，还要重点监测异常自动化访问和高频探测行为。

**04**

**Adobe ColdFusion 修复关键漏洞：老牌 Web 平台仍是高价值入口**

Adobe 发布 ColdFusion 2025 和 ColdFusion 2023 安全更新，修复多项关键漏洞。报道提到，这些漏洞可能导致任意代码执行、安全控制绕过、权限提升、敏感内存暴露或服务不可用。ColdFusion 虽然不像新框架那样常被讨论，但在政企、传统行业和老业务系统里仍有存量部署。**这个事件真正要警惕的是 “老系统还在跑，但没人持续盯”，ColdFusion 常出现在内部管理系统、旧门户、报表平台和业务后台里，一旦暴露在公网或与数据库、文件服务相连，远程代码执行类漏洞就可能变成攻击者进入内网的跳板。**建议相关单位立即确认 ColdFusion 版本，优先升级 2025 和 2023 分支的官方安全更新；如果短期无法升级，应限制公网访问、加固管理后台、检查异常模板文件、WebShell 痕迹、可疑进程和应用日志中的异常请求。

**05**

**风险Eclipse 勒索软件招募加盟者：Windows、Linux 和 ESXi 都在目标里**

一个名为 Eclipse Ransomware 的新勒索软件即服务平台正在网络犯罪论坛招募加盟者。报道提到，该组织声称可攻击 Windows、Linux 服务器、NAS 存储、VMware ESXi 虚拟化平台和 Nutanix 基础设施。**这意味着它不是只盯单台办公电脑，而是冲着企业核心运行环境去的，勒索软件发展到今天，真正危险的地方是 “平台化”。一个 RaaS 组织只要把加密器、泄露站、谈判流程和加盟分成搭好，就能让不同攻击者快速复用同一套能力。**对企业来说，攻击源头可能不同，但最后的后果都很相似：业务停摆、备份被删、数据被挂网。建议企业重点检查虚拟化平台、NAS、备份服务器和域控权限，不要让备份系统与生产域使用同一套高权限账号。关键数据要有离线或不可变备份，并定期演练恢复，而不是只在采购方案里写 “已备份”。

**06**

**VMware vCenter 遭在野利用：虚拟化管理面不能暴露成公网入口**

研究人员发现攻击者正在利用 CVE-2026-59310 攻击公网可访问的 VMware vCenter 实例。该漏洞被描述为 vCenter 中的严重目录遍历问题，攻击者可借此获得初始访问，并部署反向 SSH 工具维持远程后门。**vCenter 的风险从来不只是 “一个管理后台被打”。它管理的是虚拟机、宿主机、集群、快照和大量业务系统。如果攻击者进入 vCenter，后续可能影响多台服务器，甚至借管理权限扩展到备份、域控和核心业务环境。**很多企业对业务服务器很重视，却容易忽略虚拟化管理面的公网暴露和弱口令、旧版本问题。建议立即排查 vCenter 是否暴露公网，核查是否受 CVE-2026-59310 影响，尽快修复或采取访问控制措施。安全团队还应检查异常反向 SSH 连接、新增账号、异常任务、快照操作、插件变更和管理日志中的可疑访问。

**07**

**Cl0p再盯PTC Windchill/FlexPLM：数据窃取型勒索仍在打供应链软件**

CN-SEC 8 月13日发布文章称，ReliaQuest 监测到 Cl0p 相关的大规模数据窃取攻击，攻击者利用 PTC Windchill 和 FlexPLM 等工业 / 产品生命周期管理软件中的高危漏洞进入企业系统，并窃取敏感商业信息。原文关键词列出 PTC Windchill、FlexPLM、WebShell、反序列化漏洞、CVE-2026-12569、CVE-2026-4681 等线索。**这类系统的价值很高，因为它们往往保存产品设计、供应链协作、工程文档、客户项目和生产相关资料，攻击者如果只是加密服务器，企业还能谈恢复；但如果先把商业机密拖走，再用泄露施压，谈判压力会明显更大。**建议使用 PTC Windchill、FlexPLM 的企业立即核查版本和官方补丁，排查可疑 WebShell、异常文件上传、未知管理账号、批量下载和外联流量。涉及研发、制造、供应链协作的系统，应单独纳入高优先级资产管理，而不是当普通业务后台处理。

**08**

**Cisco防火墙零日漏洞已遭利用：一次恶意请求就可能让VPN掉线**

Cisco确认CVE-2026-20349已出现真实攻击。漏洞影响Cisco Secure Firewall ASA与FTD软件的远程访问SSL VPN服务。**攻击者无需登录，只要向暴露的SSL VPN接口发送特制HTTP请求，就可能迫使设备异常重启，造成拒绝服务，远程办公、站点互联以及依赖防火墙的业务连接都可能随之中断。这次风险的重点不是窃取数据，而是直接打断网络边界。受影响设备需要运行存在漏洞的ASA或FTD版本，并启用了WebVPN、IKEv2远程访问客户端服务，或FTD上的零信任网络访问功能；Cisco FMC不受影响。**Cisco表示目前没有能够彻底消除风险的临时绕过措施。建议管理员立即对照Cisco公告核查版本和配置，优先升级到修复版本，同时检查设备异常重启、可疑HTTP请求和VPN会话集中断开记录。对外开放的SSL VPN接口应限制来源并加强监控，但访问控制不能替代补丁。

**09**

**WordPress恶意PNG可触发远程代码执行：图片上传也能成为服务器入口**

WordPress 7.0.4修复了CVE-2026-65640。该漏洞影响使用Imagick和Ghostscript处理图片的网站，拥有Author作者级权限的攻击者可上传伪装成PNG的恶意文件，在服务器端触发代码执行。问题源于扩展名与文件真实内容识别不一致，恶意PostScript内容可能绕过部分上传路径并被交给Ghostscript处理。这个漏洞说明，文件上传风险不能只看“是否允许PHP”。**图片、PDF、音视频封面等文件只要进入复杂解析链，就可能触发底层组件漏洞。多作者博客、媒体站、投稿平台和允许普通账号上传素材的网站风险更高，因为攻击者不必先取得管理员权限。**建议立即升级WordPress 7.0.4或更高修复版本，并同步检查ImageMagick、Ghostscript版本。安全团队还应审计XML-RPC上传、媒体库异常文件、作者账号登录和Web进程拉起Shell命令等行为；无法及时升级的站点应暂时收紧上传权限并限制XML-RPC入口。

**10**

**WhatsApp上线诈骗预警：AI生成话术让社工攻击更难凭直觉识别**

WhatsApp推出可选的Scam Alert功能，利用下载到手机本地的轻量机器学习模型，分析陌生联系人消息中的对话结构和诈骗语言模式。命中风险后，系统会在聊天中向接收者显示警告，并提供屏蔽、举报、继续对话或标记可信等选项。这项功能值得关注，因为社工诈骗正从生硬模板转向AI生成的个性化话术。**攻击者会冒充客服、老板、招聘人员或亲友，通过长对话建立信任，再诱导转账、交出验证码或点击钓鱼链接。WhatsApp强调识别过程在设备本地完成，消息不会为了分类而离开手机，也不会自动上报给Meta或第三方。**企业仍不能把安全责任交给客户端提示。建议持续培训员工识别紧急转账、验证码索取、远程控制和陌生链接等信号，为财务及高权限人员建立二次核验流程；个人用户应开启可用的诈骗预警功能，对陌生联系人提出的资金和账号要求通过其他渠道复核。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AyvgaRYHWDbaCKLlv4qpwa3CaIMdhoXL5tlnjeHqqfccgyBe17DIrnH6ibicOrkTevU2SEThYOPt0XRDThdZeloUiaZ3D10ciajZbXntNfiaqfEA/640?wx_fmt=gif&from=appmsg)

信息来源：人民网 国家计算机网络应急技术处理协调中心 国家信息安全漏洞库 今日头条 360威胁情报中心 中科汇能GT攻防实验室 安全牛 E安全 安全客 NOSEC安全讯息平台 火绒安全 亚信安全 奇安信威胁情报中心 MACFEESy mantec白帽汇安全研究院 安全帮  卡巴斯基 安全内参 安全学习那些事 安全圈 黑客新闻 蚁景网安实验室 IT之家IT资讯 黑客新闻国外 天际友盟

![](https://mmbiz.qpic.cn/mmbiz_png/AyvgaRYHWDbS6rAa7epM3ibTqVbtAAQBeckib3XSFqibteIQqhF3VFp9ax7H82m9uQ1YQfIALDtoib0RGlGZibBbibAialGujbFm7vFU4CZ8RaSicWU/640?wx_fmt=png&from=appmsg)

本文版权归原作者所有，如有侵权请联系我们及时删除

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NSXvotEG4JxfVX9phMzJeKxa6TJkRkiad551HzMtpQVE1WJGiaB2n35mb3ponQiblLvDVPs7yb9iaq1ulcBl8ibpveg/0?wx_fmt=png)

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