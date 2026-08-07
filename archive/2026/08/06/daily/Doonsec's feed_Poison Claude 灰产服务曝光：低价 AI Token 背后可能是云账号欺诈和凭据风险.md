---
title: Poison Claude 灰产服务曝光：低价 AI Token 背后可能是云账号欺诈和凭据风险
url: https://mp.weixin.qq.com/s/0lNQVsSE4JWQ9EaWgWIwgw
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:25:34.286213
---

# Poison Claude 灰产服务曝光：低价 AI Token 背后可能是云账号欺诈和凭据风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AyvgaRYHWDb6C3Qw0tA1U44hn2p4yX0VVWgEMRQbdZA92IRb5xMrfic2ykcgLZqicPcNZWJmgJJjy5tsMFziavxbLib47aI4xicu7VKxwuEuia96Q/0?wx_fmt=jpeg)

# Poison Claude 灰产服务曝光：低价 AI Token 背后可能是云账号欺诈和凭据风险

汇能云安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/AyvgaRYHWDa4Hc9ukZZiceA2T3ORMGlSoGWPNiaO5Us1fmkSHbaNp3iceFLbJ66vyTDbVWDpmhngtGnYia8yI4HTBpNr1oXG4QGszAR0Eq0cDFs/640?wx_fmt=jpeg&from=appmsg)

**8****月****6****日，星期四****，您好！中科汇能与您分享信息安全快讯：**

![](https://mmbiz.qpic.cn/mmbiz_gif/AyvgaRYHWDbdJYdia9HZLjlXR8zmSG8IkyrzzG5wRklYj3FDJWS7tcgflmr118lzzDs5fKgiaJ9mIXqYR6e9CIKLXtml2gRlsKm1acGcTogHc/640?wx_fmt=gif&from=appmsg)

**01**

**TeamCity 被 CISA 加入 KEV：CI/CD 服务器一旦被打穿，后果不是 “构建失败” 这么简单**

CISA 在8月5日将 JetBrains TeamCity 漏洞 CVE-2026-63077 加入已知被利用漏洞目录。JetBrains 官方公告显示，这个漏洞影响所有 TeamCity On-Premises 版本，未认证攻击者只要能通过 HTTP (S) 访问 TeamCity 服务器，就可能经 Agent 轮询协议绕过认证，并以 TeamCity 服务进程权限执行任意系统命令。官方修复版本为 2025.11.7 和 2026.1.3，无法升级的环境可安装安全补丁插件。这个事件真正危险的地方，**是 TeamCity 处在软件交付链核心位置。它连接源码仓库、构建脚本、制品库、部署凭据和云环境密钥。一旦 CI/CD 服务器被拿下，攻击者不只是进入一台机器，而是可能篡改构建产物、窃取部署 Token，甚至向下游发布被污染的软件。**建议所有使用 TeamCity 本地部署的单位立即核查版本和公网暴露情况，优先升级或安装补丁插件。修复后还要回看近期构建任务、插件变更、Agent 连接、管理员登录和密钥访问记录；凡是保存在 TeamCity 中的 Git、云服务、制品库和部署凭据，都应评估是否需要轮换。

**02**

**77 个仿冒 Open VSX 扩展出现：开发者插件正在变成供应链入口**

Manifold 研究人员发现 77 个仿冒 Open VSX 扩展。这些扩展复制合法扩展的名称、命名空间和描述，再把数据发送到同一个新注册域名。活动出现在 7 月 26 日至 8 月 1 日之间，其中大多数扩展收集主机名、工作区目录或编辑器版本，另有 19 个扩展执行更深入侦察，收集私有仓库名称、项目路径、分支信息和 CI 标识。这个事件值得警惕，是因为开发者扩展经常被默认信任，很多人安装插件时只看名字和图标，很少核对发布者身份。**一旦恶意扩展进入开发机或构建环境，攻击者拿到的不是普通浏览记录，而是企业内部项目结构、私有仓库线索和持续集成信息，后续可以用来做精准钓鱼、供应链入侵或凭据窃取。**建议企业建立开发工具扩展白名单，只允许来自可信发布者和官方市场的插件进入开发环境。对已经安装过可疑 Open VSX 扩展的机器，应检查网络连接、工作区访问日志和 CI 变量访问记录，并轮换可能被暴露的 Git、CI/CD 和包仓库凭据。

**03**

**TP-Link Omada ZTP 曝 15 个漏洞：零接触配置方便，也可能放大整网风险**

TP-Link Omada 零接触配置机制被披露 15 个漏洞，影响 Omada 云、软件和硬件控制器，以及 Omada、Festa VPN 路由器等设备。报道提到的问题包括硬编码 TLS 证书和私钥、可预测序列号、弱密码哈希保护、不安全证书校验、设备接管竞态以及设备采用流程中的认证缺陷。Omada 这类平台用于集中管理路由器、交换机、网关和无线 AP，本来是为了提高大规模部署效率。但**正因为它站在网络管理链中心，一旦控制器与设备之间的信任关系被破坏，攻击者就可能不只接管单台路由器，而是拿到配置数据、管理员凭据哈希、站点凭据和 VPN 密钥，进而影响整个企业网络。**建议使用 TP-Link Omada 的单位尽快关注并应用厂商更新，尤其是控制器、VPN 路由器和云端接入组件。管理面不要暴露到公网，设备首次采用和批量配置应放在受控网络内完成。企业还应排查异常设备注册、未知 MAC 冒充、管理账号登录和配置导出记录。

**04**

**Greatness 钓鱼服务绕过 MFA：邮箱安全不能只靠 “已经开了多因素认证”**

Greatness 钓鱼即服务平台正在针对 Microsoft 365 账号。近期活动使用伪造的 RingCentral 语音邮件和绩效评审邮件作为诱饵，邮件虽然未通过 SPF、DKIM 和 DMARC 检查，但由于域名安全发件人排除规则覆盖了失败结果，仍然进入受害者收件箱。**攻击链重点不是简单偷密码，而是窃取有效登录 Token，这个风险对企业很现实，很多单位觉得启用了 MFA 就安全了，但 AiTM 中间人钓鱼、设备码钓鱼和实时登录中继的目标，正是让用户完成真实 MFA 后，把会话 Token 交给攻击者。攻击者拿到 Token 后，可能访问 Outlook、Teams、SharePoint、OneDrive、日历、联系人和企业应用。**建议企业重新审查 “安全发件人”“域名白名单” 等放行策略，不要让它们覆盖基础邮件认证失败结果。对 Microsoft 365 环境，应监控异常 Token 使用、跨地域登录、设备码授权、可疑邮箱规则和 OAuth 应用授权。涉及财务、法务和高管邮箱的租户，建议启用条件访问、风险登录阻断和硬件安全密钥。

**05**

**Django 发布安全更新：GIS 空间查询可能导致服务器端写文件和请求伪造**

Django 官方发布 6.0.8 和 5.2.17 安全版本，修复多项漏洞，其中最值得关注的是 CVE-2026-15307，官方评级为高危。漏洞位于 GeoDjango 空间查询处理逻辑中，历史实现允许字符串和字典形式的栅格值被传给 GDALRaster。根据不同栅格驱动，恶意输入可能导致服务器写入文件，部分场景下甚至可能演变为远程代码执行，也可能以 Django 进程用户身份发起网络请求。**这个漏洞的影响范围不是所有 Django 站点，但对启用了 GIS 功能、后台管理界面暴露给员工用户、并且存在空间字段模型的系统，需要重点关注。官方说明中还提到，Django admin changelist 过滤功能可能让拥有查看权限的员工用户触发相关路径。**建议使用 Django 5.2 和 6.0 分支的团队尽快升级到 5.2.17 或 6.0.8。涉及 GeoDjango、GDALRaster、空间查询和后台筛选的项目，应单独做回归测试。对非必要的管理后台公网访问要收紧，员工权限也要按最小化配置，不要默认把 “内部员工可访问” 当成安全边界。

**06**

**Cursor、VS Code 等代码编辑器曝一键 RCE 风险：开发机就是新的高价值目标**

AISLE 研究人员披露一个影响 Cursor、Microsoft VS Code 和Google Antigravity 的 “一键远程代码执行” 漏洞。报道称，攻击者可以把恶意链接嵌入 Git 提交信息中，当开发者在编辑器内点击该链接时，应用可能在没有明显确认提示的情况下执行任意代码。相关平台据称已完成修复。**这个事件的重点不是 “点击链接危险” 这么简单，而是开发者工作站的权限太高。开发机里经常保存 OpenAI、Anthropic、Stripe、Git、云服务和数据库密钥，也能访问源码和内部文档。如果攻击者通过编辑器拿到执行权限，就可能直接窃取环境变量、安装持久化木马、读取项目文件，甚至进入企业供应链。**建议开发团队立即更新相关编辑器和扩展，避免在 IDE 中直接点击来源不明的提交链接、Issue 链接和 Markdown 链接。开发机应减少长期明文密钥，尽量使用短期 Token、密钥代理或凭据管理器。企业还应监控开发机异常出网、可疑启动项、未知扩展和 CI 凭据使用记录。

**07**

**7-Zip 默认处理可能绕过 Mark-of-the-Web：压缩包仍是钓鱼投递老入口**

Attackd 分析人员在测试钓鱼投递链路时发现，7-Zip 24.09 在解压从互联网下载的 ZIP 文件时，可能不会把 Windows 的 Mark-of-the-Web 来源标记传递给解压后的可执行文件。报道强调，这不是一个新披露的 7-Zip 代码漏洞，而是工具默认处理方式造成的安全控制缺口。这个问题很现实。**Windows 的 Mark-of-the-Web 标记会告诉 SmartScreen 等安全机制：“这个文件来自互联网，需要额外检查”。如果压缩包本身带有标记，但解压后的可执行文件失去这个标记，用户双击运行时就可能少一道早期声誉检查。攻击者可以继续用 “发票、更新包、共享文档” 这类老套路，把恶意程序藏进 ZIP 里投递。**建议企业不要只依赖 SmartScreen 拦截未知文件。终端侧应限制用户直接运行邮件附件中的可执行文件，网关侧加强压缩包检测，EDR 侧关注临时目录、下载目录和解压目录中的进程启动行为。用户层面，收到 ZIP 附件后不要随手解压运行，尤其是来自陌生邮件、即时通讯和网盘链接的文件。

**08**

**Microsoft 登录页、Zoom 活动和政府网站被武器化：攻击者越来越会 “借真平台做假事”**

ANY.RUN 在 7 月威胁观察中发现，攻击者正在系统性滥用可信业务平台，包括 Microsoft 认证页、SharePoint、OneDrive、Microsoft Forms、Zoom 活动页面和部分政府门户。**攻击方式包括 Kratos 钓鱼即服务、Kali365 设备码钓鱼、假冒 AI 大会注册页，以及借合法公共部门域名作为跳转入口。这类攻击的难点在于，它不一定依赖假域名，受害者看到的可能是真实 Microsoft 登录页面、真实 Zoom 活动页面，甚至是看起来可信的政府网站跳转链。安全网关和普通用户都更容易放行这种流量，攻击者的目标也不只是密码，而是 OAuth Token、会话凭据和长期云访问权限。**建议企业把设备码登录、OAuth 授权和异常跳转链纳入监控。员工看到 “去 Microsoft 输入代码完成登录”“参加 AI 大会需要重新授权邮箱” 等提示时，要先确认来源。管理员应限制设备码登录范围，审计新增企业应用授权，清理不必要的 SharePoint 外链和 Forms 公开表单，并对异常云访问建立自动告警。

**09**

**Poison Claude 灰产服务曝光：低价 AI Token 背后可能是云账号欺诈和凭据风险**

Okta Threat Intelligence 发现一个名为 Poison Claude 的灰产服务，以极低价格转售 Anthropic 高级模型访问能力。研究人员认为，其低价来源可能是大量欺诈注册的云账号和免费额度。该服务接受加密货币付款，并向用户提供 API Key 和环境变量配置，让用户把 Claude Code 请求转向其自有服务器。这个事件不是传统意义上的漏洞，但对 AI 安全很有警示意义。**企业或开发者如果为了便宜接入这种非官方代理服务，实际上是在把提示词、代码片段、API 请求、上下文数据和可能包含的商业秘密交给未知第三方，另一方面，云厂商和 AI 平台的免费额度、创业扶持额度，也正在成为灰产套利目标。**建议企业禁止在生产代码、客户数据和内部项目中使用来历不明的 “低价 AI API”。开发团队应统一 AI 服务出口，记录模型调用域名和代理配置，排查环境变量中是否出现非官方 Endpoint。云服务商侧也应关注批量注册、额度套取、异常 API 转售和密集 Token 消耗行为。

**10**

**Check Point 管理服务器认证绕过：安全设备的管理面不能成为最脆弱入口**

Check Point 披露 CVE-2026-18574 认证绕过漏洞，可能导致 Security Management Server 和 Multi-Domain Security Management Server 被完全接管。报道称，未认证攻击者只要能访问目标管理服务器，就可能绕过管理认证并执行任意命令。受影响版本包括多个已停止支持的 R80、R81 早期版本，以及 R81.20、R82、R82.10 等支持版本。这个事件真正关键的地方，是安全管理服务器掌握着防火墙策略、网关配置、管理员权限和安全基础设施控制权。它不是普通业务后台，一旦被攻陷，攻击者可能直接改规则、开通访问路径、隐藏持久化入口，甚至削弱企业边界防护能力。**Check Point 称该漏洞由内部发现，未发现野外利用证据，但潜在影响足够高。建议相关单位尽快安装 Jumbo Hotfix Accumulator 更新，使用不受支持版本的环境应优先升级。临时缓解上，要在 SmartConsole 中限制 Trusted Clients，只允许批准的管理员 IP 和网段访问，避免使用 “Any” 作为可信客户端定义，并确保管理服务不暴露给公网或普通办公网。**

![](https://mmbiz.qpic.cn/mmbiz_gif/AyvgaRYHWDaIebUqjp0cUibFVOr0N8ocumaZdyX3X05HUOLt9VdLmUW865mbvPq7jqbsjBia5jicFP1vOSUe0IKX6g0OZBjjmFgZoPjVuUdU7A/640?wx_fmt=gif&from=appmsg)

信息来源：人民网 国家计算机网络应急技术处理协调中心 国家信息安全漏洞库 今日头条 360威胁情报中心 中科汇能GT攻防实验室 安全牛 E安全 安全客 NOSEC安全讯息平台 火绒安全 亚信安全 奇安信威胁情报中心 MACFEESy mantec白帽汇安全研究院 安全帮  卡巴斯基 安全内参 安全学习那些事 安全圈 黑客新闻 蚁景网安实验室 IT之家IT资讯 黑客新闻国外 天际友盟

![](https://mmbiz.qpic.cn/mmbiz_png/AyvgaRYHWDa1y2DviaO1yo4ibjWyZOovz16Hm6VWMYV9icSib8icHekK8AFjvEib6ibJH1vXjjcoOyibMsfjwIfr9erxjtP0HzjEFeDCGQ079vDNsHg/640?wx_fmt=png&from=appmsg)

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