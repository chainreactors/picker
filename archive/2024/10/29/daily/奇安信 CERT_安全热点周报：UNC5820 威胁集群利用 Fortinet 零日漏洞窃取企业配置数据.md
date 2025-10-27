---
title: 安全热点周报：UNC5820 威胁集群利用 Fortinet 零日漏洞窃取企业配置数据
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502343&idx=2&sn=f3ecf71ee875550a542839608c722045&chksm=fe79ee9fc90e6789619f3e2ad7f4f170cabde1967b8e0962c9452f64c9bc1819341bc8960307&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-10-29
fetch_date: 2025-10-06T18:50:27.539243
---

# 安全热点周报：UNC5820 威胁集群利用 Fortinet 零日漏洞窃取企业配置数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibSyP2CThAK1IGwovXztT5LJrrVOeAJ0MibK7E588u6MoejDmXnGPkH1vk9hZvbeqBaQw2ncEXA8Gw/0?wx_fmt=jpeg)

# 安全热点周报：UNC5820 威胁集群利用 Fortinet 零日漏洞窃取企业配置数据

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 美国政府发布首份关于人工智能的国家安全备忘录 |
| • 河南两公司泄露大量敏感数据被罚10万元 |
| • 国家网络安全通报中心：多个与某大国政府有关的境外黑客组织持续攻击国内单位企业 |

**PART****0****1**

**漏洞情报**

**1.Fortinet FortiManager身份认证绕过漏洞在野利用通告**

10月24日，奇安信CERT监测到官方修复Fortinet FortiManager身份认证绕过漏洞(CVE-2024-47575)，未经身份验证的远程攻击者可以使用有效的FortiGate证书在FortiManager中注册未经授权的设备。成功利用漏洞后攻击者将能够查看和修改文件（例如配置文件）以获取敏感信息，并能够管理其他设备执行任意代码或命令。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为39073个，关联IP总数为39674个。鉴于此漏洞已发现在野利用，建议客户尽快做好自查及防护。

**PART****0****2**

**新增在野利用**

**1.****Cisco ASA 和 FTD 拒绝服务漏洞(CVE-2024-20481)**

10 月 24 日，思科修复了其 Cisco ASA 和 Firepower Threat Defense (FTD) 软件中的一个拒绝服务漏洞，该漏洞是在4月份针对思科 VPN 设备进行的大规模暴力攻击中发现的。该漏洞的编号为 CVE-2024-20481，影响 Cisco ASA 和 Cisco FTD 的所有版本，直至软件的最新版本。

CVE-2024-20481 安全公告中写道：“思科自适应安全设备 (ASA) 软件和思科 Firepower 威胁防御 (FTD) 软件的远程访问 VPN (RAVPN) 服务中存在一个漏洞，可能允许未经身份验证的远程攻击者对 RAVPN 服务发起拒绝服务 (DoS) 攻击 。”

此漏洞是由于资源耗尽造成的。攻击者可以通过向受影响的设备发送大量 VPN 身份验证请求来利用此漏洞。成功利用此漏洞可能会使攻击者耗尽资源，导致受影响设备上的 RAVPN 服务出现 DoS。

思科表示，一旦此次 DDoS 攻击影响设备，可能需要重新加载才能恢复 RAVPN 服务。尽管思科产品安全事件响应团队 (PSIRT) 表示他们已经意识到此漏洞被积极利用，但该漏洞并未被用于针对思科 ASA 设备发起 DoS 攻击。

这些攻击旨在获取企业网络的有效 VPN 凭证，然后将其在暗网市场上出售或卖给勒索软件团伙以获取初始访问权限，或用于在数据盗窃攻击中破坏网络。然而，由于针对设备发出大量连续且快速的身份验证请求，攻击者在不知不觉中耗尽了设备上的资源，导致思科 ASA 和 FTD 设备处于拒绝服务状态。

思科表示，只有启用 RAVPN 服务才能利用此漏洞。受影响的客户可以通过其技术援助中心解决此问题。

参考链接：

https://www.bleepingcomputer.com/news/security/cisco-fixes-vpn-dos-flaw-discovered-in-password-spray-attacks/

**2.****RoundCube Webmail 跨站脚本漏洞(CVE-2024-37383)**

10 月 24 日，黑客一直在利用 Roundcube Webmail 客户端中的漏洞来攻击独立国家联合体 (CIS) 地区（前苏联继承国）的政府组织。

俄罗斯网络安全公司 Positive Technologies 于 9 月发现了一次攻击，但研究人员确定黑客的活动早在 6 月就已开始。

Roundcube Webmail 是一个基于 PHP 的开源网络邮件解决方案，支持插件来扩展其功能，深受商业和政府实体的欢迎。

黑客利用了 CVE-2024-37383 存储型 XSS（跨站点脚本）漏洞，该漏洞允许在打开特制的电子邮件时在 Roundcube 页面上执行恶意 JavaScript 代码。该问题是由电子邮件中 SVG 元素的不当处理引发的，它绕过了语法检查并允许在用户页面上执行恶意代码。

Positive Technologies报告称，攻击使用的电子邮件没有可见内容，只有一个 .DOC 附件。然而，黑客在代码中嵌入了一个隐藏的有效载荷，客户端会处理该有效载荷，但根据特定标签（在本例中为“<animate>”），该有效载荷不会显示在邮件正文中。有效载荷是一段伪装成“href”值的 base64 编码的 JavaScript 代码。它会从邮件服务器下载诱饵文档（Road map.doc）来分散受害者的注意力。同时，它会在 HTML 页面中注入未经授权的登录表单，以从邮件服务器请求消息。

据研究人员称，黑客希望手动或自动填写这两个字段，从而获取目标的帐户凭证。如果他们愿意，数据就会被发送到“libcdn[.]org”的远程服务器，该服务器是最近注册的，并托管在 Cloudflare 基础设施上。

5 月 19 日发布的 Roundcube Webmail 1.5.7和1.6.7 版本已修复此漏洞。最新可用版本（即推荐升级）是9 月 1 日发布的1.6.9 版本。由于重要组织使用该开源工具，Roundcube 漏洞经常成为黑客的目标。CVE-2024-37383 影响 Roundcube 1.5.6 之前的版本和 1.6 到 1.6.6 版本，因此建议仍使用这些版本的系统管理员尽快更新。

参考链接：

https://www.bleepingcomputer.com/news/security/hackers-exploit-roundcube-webmail-flaw-to-steal-email-credentials/

**3.****Fortinet FortiManager 身份认证绕过漏洞(CVE-2024-47575)**

10 月 23 日，Fortinet 公开披露了一个严重的 FortiManager API 漏洞，编号为 CVE-2024-47575，该漏洞被零日攻击利用来窃取包含受管设备配置、IP 地址和凭据的敏感文件。

Mandiant 与 Fortinet 合作，调查了各行业 50 多台可能受到攻击的 FortiManager 设备中 FortiManager 设备的大规模利用情况。漏洞CVE-2024-47575 / FG-IR-24-423允许黑客使用未经授权、受黑客控制的 FortiManager 设备对易受攻击的 FortiManager 设备执行任意代码或命令。

Mandiant 观察到一个新的威胁集群，将其追踪为 UNC5820，它早在 2024 年 6 月 27 日就利用了 FortiManager 漏洞。UNC5820 准备并窃取了被利用的 FortiManager 管理的 FortiGate 设备的配置数据。这些数据包含受管设备的详细配置信息以及用户及其 FortiOS256 哈希密码。UNC5820 可以使用这些数据进一步入侵 FortiManager，横向移动到 Fortinet 设备，并最终瞄准企业环境。

目前，Mandiant 分析的数据源未记录黑客利用 FortiManager 漏洞的具体请求。此外，在调查的这个阶段，没有证据表明 UNC5820 利用获得的配置数据横向移动并进一步破坏环境。因此，在发布时，缺乏足够的数据来评估黑客的动机或位置。Shodan 搜索显示，有 59,534 台 FortiManager 设备的 FGFM 端口（TCP 端口 531）在线暴露，其中大多数位于美国。

Fortinet 在其CVE-2024-47575 (FG-IR-24-423) 公告中分享了更多信息，包括缓解和恢复方法。该公告还包含其他 IOC，包括攻击者使用的其他 IP 地址和用于检测受感染的 FortiManager 服务器的日志条目。

参考链接：

https://cloud.google.com/blog/topics/threat-intelligence/fortimanager-zero-day-exploitation-cve-2024-47575/

**4.****Mozilla Firefox Animation timelines 释放后重用漏洞(CVE-2024-9680)**

10 月 22 日，美国网络安全和基础设施安全局（CISA） 将Microsoft SharePoint 反序列化漏洞CVE-2024-38094 （CVSS v4 评分：7.2）添加到其已知被利用漏洞（KEV）目录中。具有站点所有者权限的攻击者可以利用漏洞在 SharePoint Server 上注入并执行任意代码。

微软发布的公告称：“经过身份验证且拥有站点所有者权限的攻击者可以利用此漏洞注入任意代码并在 SharePoint Server 环境中执行此代码。”

该漏洞是由于 SharePoint Server Search 组件中的输入验证错误造成的。未经身份验证的用户可以通过向存在漏洞的 SharePoint 服务器发送特制的 HTTP 请求来利用此漏洞。这可能允许攻击者在服务器上执行任意代码，从而可能接管系统。

SOCRadar表示：“PoC 脚本使用 NTLM 自动对目标 SharePoint 站点进行身份验证，创建特定的文件夹和文件，并发送精心设计的 XML 负载以触发 SharePoint 客户端 API 中的漏洞。”

目前尚无关于 CVE-2024-38094 在实际攻击中如何被利用的报告。谷歌威胁分析小组 (TAG) 透露，三星移动处理器中现已修补的零日漏洞已被武器化，成为漏洞利用链的一部分，以实现任意代码执行。虽然三星的简短公告中并未提及该漏洞是否已被利用，但谷歌 TAG 研究人员 Xingyu Jin 和 Clement Lecigne 表示，针对该漏洞的零日漏洞已被用作权限提升链的一部分。

鉴于该漏洞被在野高频利用，建议受影响客户在 2024 年 11 月 12 日之前应用最新修复程序，以保护其网络。

参考链接：

https://thehackernews.com/2024/10/mozilla-warns-of-active-exploitation-in.html

**5.****ScienceLogic SL1 远程代码执行漏洞(CVE-2024-9537)**

10 月 21 日，Rackspace 在第三方 ScienceLogic 应用程序（称为 SL1）打包和交付的非 Rackspace 实用程序中发现了零日远程代码执行漏洞，随后美国网络安全和基础设施安全局 (CISA)将影响 ScienceLogic SL1 的严重安全漏洞添加到其已知被利用漏洞 ( KEV ) 目录中。

ScienceLogic SL1（以前称为 EM7）是一个 IT 运营平台，用于监控、分析和自动化组织基础设施（包括云、网络和应用程序）。它提供实时可见性、事件关联和自动化工作流程，以帮助有效地管理和优化 IT 环境。

Rackspace 是一家托管云计算（托管、存储、IT 支持）公司，它使用 ScienceLogic SL1 来监控其 IT 基础设施和服务。

为了应对发现的恶意活动，Rackspace 禁用了其 MyRack 门户上的监控图表，直到他们可以推送更新来消除风险。由于利用 SL1 漏洞而遭到不当访问的系统是 Rackspace 用来生成内部性能报告的系统，故属于 Rackspace 内部。他们取证调查发现，没有访问客户配置或其托管数据的权限。

Rackspace 立即通知 ScienceLogic 其漏洞。Rackspace 与 ScienceLogic 合作开发补丁来修复其漏洞，ScienceLogic 现已向其全球所有客户提供该补丁。有限的低安全敏感度性能监控信息被不当访问。出于谨慎考虑，所有受影响的客户都已收到通知。客户无需采取任何补救措施。Rackspace 的监控功能不依赖于 ScienceLogic 仪表板，Rackspace 客户性能监控未受到此事件的影响。

虽然数据有限，但公司通常会将其设备的 IP 地址隐藏在内容交付系统和 DDoS 缓解平台后面。黑客可以使用暴露的 IP 地址对公司设备进行 DDoS 攻击或进一步利用。对客户的唯一服务影响是无法访问其关联的 ScienceLogic 监控仪表板，这是一些客户很少使用的可选服务功能。

建议受影响客户升级至 12.1.3、12.2.3 和 12.3 及更高版本。版本 10.1.x、10.2.x、11.1.x、11.2.x 和 11.3.x 也已提供修复。

参考链接：

https://www.bleepingcomputer.com/news/security/rackspace-monitoring-data-stolen-in-sciencelogic-zero-day-attack/

**PART****0****3**

**安全事件**

**1.河南两公司泄露大量敏感数据被罚10万元**

10月23日网信郑州消息，郑州市网信办工作中发现，该市两家公司未履行网络安全保护义务，未采取必要的安全防护，导致大量敏感数据被窃取。经调查核实，公司一在数据库中配置增加了远程登录空口令账户，导致黑客利用该空口令账户成功登录数据库，并窃取了数据库中的数据，被窃取的数据包含姓名、身份证号、手机号、邮箱地址等敏感信息。公司二缺乏网络安全意识，没有正确配置数据库，导致数据库存在未授权访问漏洞，攻击者通过漏洞登录数据库，查看、下载数据，导致敏感数据泄露。郑州市网信办依据《数据安全法》分别对两家公司作出责令改正，给予警告，并处人民币5万元罚款的行政处罚。

原文链接：

https://mp.weixin.qq.com/s/TNdGXuqWwebR0xfcK6DPvA

**2.国家网络安全通报中心：多个与某大国政府有关的境外黑客组织持续攻击国内单位企业**

10月21日国家网络安全通报中心消息，中国国家网络与信息安全信息通报中心发现一批境外恶意网址和恶意IP，有多个具有某大国政府背景的境外黑客组织，利用这些网址和IP持续对中国和其他国家发起网络攻击。这些恶意网址和IP都与特定木马程序或木马程序控制端密切关联，网络攻击类型包括建立僵尸网络、网络钓鱼、勒索病毒等，以达到窃取商业秘密和知识产权、侵犯公民个人信息等目的，对中国国内联网单位和互联网用户构成重大威胁，部分活动已涉嫌刑事犯罪。相关恶意网址和恶意IP归属地主要涉及：美国、波兰、荷兰、保加利亚、土耳其、日本等。

原文链接：

https://mp.weixin.qq.com/s/uYVx7bAP7Oqey-DeSUjZJA

**3.卡西欧遭遇灾难式勒索攻击：系统瘫痪、交付延迟、财报推迟**

10月21日The Record消息，日本知名手表制造商卡西欧计算机株式会社宣布，由于10月5日发生的勒索软件攻击影响了公司的会计流程，原定于11月6日发布的第二季度财报将推迟至11月中旬。该公司官网声明称，此次攻击导致“交货日期严重推迟，并积压了大量维修请求。公司目前正全力应对这一情况，计划在11月底之前恢复系统的正常运行。”“Underground”勒索软件团伙声称对这次攻击负责。该组织称他们窃取了公司204.9 GB的数据，并发布了部分被盗数据作为证据。

原文链接：

https://therecord.media/japan-casio-delays-watchmaker-ransomware

**PART****0****4**

**政策法规**

**1.美国政府发布首份关于人工智能的国家安全备忘录**

10月24日，美国白宫公开发布首份关于人工智能的国家安全备忘录，旨在确保美国在抓住人工智能机遇和管理人工智能风险方面发挥领军作用，鼓励联邦政府采用人工智能来推进国家安全使命，并寻求塑造围绕人工智能使用的国际规范。除了该备忘录外，美国白宫还发布了《国家安全领域推进人工智能治理和风险管理框架》，对此前针对非国家安全任务的指南进行了补充。该框架提供了实施备忘录的进一步细节和指导，包括要求建立风险管理、评估、问责和透明度机制。

原文链接：

https://www.whitehouse.gov/briefing-room/presidential-actions/2024/10/24/memorandum-on-advancing-the-united-states-leadership-in-artificial-intelligence-harnessing-artificial-intelligence-to-fulfill-national-security-objectives-and-fostering-the-safety-se

**2.美国CISA发布数据安全拟议新规，防止外国获取敏感数据**

10月21日，根据美国总统拜登2月签署的第14117号行政命令《关于防止受关注国家获取美国人大量敏感个人数据和美国政府相关数据的行政命令》，美国网络安全与基础设施安全局（CISA）发布拟议实施文件公开征求意见。该文件主要针对参与受限交易领域的企业，特别是那些可能持有、处理大量美国政府和公民敏感数据，提出了多项安全措施。该文件提出了一系列组织级别与数据级别的具体要求，包括维护资产清单、漏洞修补、网络拓扑维护、多因素认证、数据加密与脱敏、限制未授权硬件连接等。

原文链接：

https://www.cisa.gov/sites/default/files/2024-10/Proposed-Security-Requirements-EO-14117-21Oct24508.pdf

**3.美国司法部发布拟议新规，防止外国获取敏感数据**

10月21日，美国司法部公布了《应对美国敏感数据面临的国家安全风险拟议规则》（NPRM），并再次征求公众意见。该项拟议规则以今年2月美国总统签署第14117号行政命令后司法部同日制定的拟议规则预通知（ANPRM）为基础。NPRM在分析对ANPRM的相关公众反馈后再次对外发布，以解决美国人的敏感数据和政府相关数据被包括中国在内的“关注国、地区、个人”获取的国家安全威胁。该文件定义了六类美国人敏感数据和两类美国政府敏感数据，将禁止数据经纪公司与关注国进行敏感数据交易、限制与敏感数据相关的投资和合作协...