---
title: 安全热点周报：黑客利用自定义恶意软件对受感染的 Ivanti 设备发起零日攻击
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502754&idx=2&sn=71834c7ec593bc49ee831cf81afb0628&chksm=fe79ef3ac90e662c0938869f54ea887addd6c578f54932f05bf3901d6b96b1048e3ae3fee67c&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2025-01-14
fetch_date: 2025-10-06T20:10:45.108067
---

# 安全热点周报：黑客利用自定义恶意软件对受感染的 Ivanti 设备发起零日攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibX9f2xQnFgqGibwvwNQseawNlGXoVPyZ42ibpqVc70e63HsARdyA0nnSk5E6FqthycfkJ7HgRdLCDA/0?wx_fmt=jpeg)

# 安全热点周报：黑客利用自定义恶意软件对受感染的 Ivanti 设备发起零日攻击

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 国家发改委等三部门印发《国家数据基础设施建设指引》 |
| • 俄罗斯运营商Nodex遭乌克兰黑客攻击，网络被“摧毁” |
| • 国家网络安全通报中心：境外黑客组织持续对中国和其他国家发起网络攻击 |

**PART****0****1**

**漏洞情报**

**1.Ivanti多款产品缓冲区溢出漏洞在野利用风险通告**

1月9日，奇安信CERT监测到官方修复Ivanti多款产品缓冲区溢出漏洞(CVE-2025-0282)，Ivanti Connect Secure、Ivanti Policy Secure和Ivanti Neurons for ZTA网关中存在一个基于堆栈的缓冲区溢出漏洞，未经身份验证的远程攻击者可以在易受攻击的设备上实现远程代码执行。奇安信鹰图资产测绘平台数据显示，该漏洞关联的全球风险资产总数为232290个，关联IP总数为93719个。目前该漏洞已发现在野利用，鉴于此漏洞影响范围较大，建议客户尽快做好自查及防护。

**2.SonicOS SSLVPN认证绕过漏洞安全风险通告**

1月8日，奇安信CERT监测到官方修复SonicOS SSLVPN认证绕过漏洞(CVE-2024-53704)，该漏洞存在于SonicOS SSLVPN的认证机制中，允许远程攻击者绕过认证。攻击者可以利用这一漏洞在未经过适当认证的情况下访问受保护的资源。奇安信鹰图资产测绘平台数据显示，该漏洞关联的全球风险资产总数为15818个，关联IP总数为15683个。鉴于此漏洞影响范围较大，建议客户尽快做好自查及防护。

**PART****0****2**

**新增在野利用**

**1.****Ivanti 多款产品缓冲区溢出漏洞(CVE-2025-0282)**

1月8日，Ivanti 警告称，黑客利用 Connect Secure 远程代码执行漏洞 (CVE-2025-0282) 进行零日攻击，在设备上安装恶意软件。

该公司表示，在 Ivanti 完整性检查工具 (ICT) 检测到客户设备上的恶意活动后意识到了这些漏洞。Ivanti 展开了调查，并确认威胁行为者正在积极利用 CVE-2025-0282 作为零日漏洞。

CVE-2025-0282 是存在于 Ivanti Connect Secure 22.7R2.5 版本之前、Ivanti Policy Secure 22.7R1.2 版本之前以及 Ivanti Neurons for ZTA 网关 22.7R2.3 版本之前的一个严重 (9.0) 基于堆栈的缓冲区溢出漏洞，允许未经身份验证的攻击者远程在设备上执行代码。

尽管该漏洞影响范围广泛，但该供应商明确表示仅针对 Connect Secure 设备发起了攻击，同时还指出受影响的客户数量“有限”。据网络安全公司 Mandiant（现为 Google Cloud 的一部分）称，攻击者自 12 月中旬开始利用该漏洞并使用自定义 Spawn 恶意软件工具包。

该恶意框架通常与该公司追踪为 UNC5337 的间谍活动有关，并且很可能是追踪为 UNC5221 的更大集群的一部分。然而，在一些受感染设备上发现的先前未知的“Dryhook”和“Phasejam”恶意软件家族目前尚未被归类为任何威胁组织。

建议系统管理员恢复出厂设置并升级到 Ivanti Connect Secure 22.7.R2.5，即使内部和外部 ICT 扫描没有发现恶意活动的迹象。

参考链接：

https://www.bleepingcomputer.com/news/security/google-chinese-hackers-likely-behind-ivanti-vpn-zero-day-attacks/

**2.****Mitel MiCollab 路径遍历漏洞(CVE-2024-41713、CVE-2024-55550)**

1月7日，美国网络安全机构 CISA 警告称，最近披露的两个影响 Mitel MiCollab 企业协作平台的漏洞已被利用进行攻击。

这两个漏洞的编号分别为 CVE-2024-41713 和 CVE-2024-55550，是影响 Mitel MiCollab 9.8 SP1 FP2（9.8.1.201）及更早版本的路径遍历漏洞。

CVE-2024-41713（CVSS 评分为 9.8）是一个严重漏洞，可能允许未经身份验证的攻击者访问配置信息并在服务器上执行未经授权的管理操作。CVE-2024-55550（CVSS 评分为 2.7）是一个低严重性漏洞，可利用该漏洞访问通常限制为管理员访问级别的资源，但不允许文件修改或特权升级。成功利用此漏洞需要以管理员身份进行身份验证。

Mitel 于 2024 年 10 月发布了针对该严重漏洞的补丁，但并未提及低严重性漏洞。该漏洞于 12 月初披露，且没有 CVE 标识符，当时攻击面管理公司 WatchTowr 警告称，该漏洞仍未得到修补。

Mitel 在其公告中表示，MiCollab 版本 9.8 SP2（9.8.2.12）解决了严重程度较高的漏洞、缓解了低严重程度的漏洞，并解决了其他严重程度和高严重程度的安全缺陷。

12 月，WatchTowr 发布了有关这两个漏洞的技术信息，以及结合这两个漏洞进行数据泄露的概念验证 (PoC) 漏洞代码，但没有提及这两个漏洞在野利用的情况。

目前还没有任何关于利用 CVE-2024-41713 和 CVE-2024-55550 的攻击的公开信息，建议所有组织在其环境中识别易受攻击的 Mitel MiCollab 实例并尽快更新或删除它们，以降低受到攻击的风险。

参考链接：

https://www.securityweek.com/cisa-warns-of-mitel-micollab-vulnerabilities-exploited-in-attacks/

**PART****0****3**

**安全事件**

**1.俄罗斯运营商Nodex遭乌克兰黑客攻击，网络被“摧毁”**

1月8日The Record消息，俄罗斯网络运营商Nodex称，遭遇网络攻击致使网络基础设施被“摧毁”，正在努力从备份数据中恢复系统，暂时无法提供全面恢复的时间表。公司称将会优先恢复电话、呼叫中心等业务。互联网监控服务NetBlocks数据显示，Nodex的网络在7日午夜出现中断，固定电话、移动网络等服务均受到影响。黑客组织乌克兰网络联盟宣称对此负责，并表示该公司的系统已经被彻底洗劫和摧毁，包括备份数据在内。近三年来，俄乌网络战持续高强度对抗，重大网络攻击事件数量不断增长。

原文链接：

https://therecord.media/russian-internet-provider-says-network-destroyed-cyberattack

**2.教育科技巨头PowerSchool被黑，美国超千万中小学生个人数据疑似泄露**

1月7日Bleeping Computer消息，美国教育科技巨头PowerSchool旗下客户支持系统、学校信息系统等产品遭到未授权访问，攻击者使用泄露凭证成功访问系统，并通过“数据导出”支持工具窃取了美国和加拿大巨量学生和老师的个人数据，目前影响规模尚未公布。此次事件中暴露的信息包括姓名、地址，还可能包含社会安全号码、医疗信息、成绩及其他可识别个人身份的信息。PowerSchool声称未遭遇勒索软件攻击，公司为防止黑客泄露被盗数据而支付了一笔费用，但未披露支付的具体金额。据悉，PowerSchool是美国最大的中小学教育SaaS软件提供商，为北美超过75%的学生提供服务。

原文链接：

https://www.bleepingcomputer.com/news/security/powerschool-hack-exposes-student-teacher-data-from-k-12-districts/

**3.国家网络安全通报中心：境外黑客组织持续对中国和其他国家发起网络攻击**

1月6日国家网络安全通报中心消息，中国国家网络与信息安全信息通报中心第三次公告，发现一批境外恶意网址和恶意IP，境外黑客组织利用这些网址和IP持续对中国和其他国家发起网络攻击。这些恶意网址和IP都与特定木马程序或木马程序控制端密切关联，网络攻击类型包括建立僵尸网络、网络钓鱼、窃取商业秘密和知识产权、侵犯公民个人信息等，对中国国内联网单位和互联网用户构成重大威胁，部分活动已涉嫌刑事犯罪。相关恶意网址和恶意IP归属地主要涉及：美国、荷兰、新加坡、土耳其、墨西哥、越南等。

原文链接：

https://mp.weixin.qq.com/s/NsO3lMyIf8DxxQ0R7JZYFw

**PART****0****4**

**政策法规**

**1.国家网信办《网络信息内容多渠道分发服务机构相关业务活动管理规定》公开征求意见**

1月10日，国家互联网信息办公室起草了《网络信息内容多渠道分发服务机构相关业务活动管理规定（草案稿）》，现公开征求意见。该文件所称网络信息内容多渠道分发服务机构（MCN机构）是指在网络信息内容服务平台入驻，为网络信息内容生产者提供策划、制作、营销、经纪等相关服务的机构。网络信息内容服务平台应当要求在本平台开展互联网信息内容相关业务活动的MCN机构办理入驻手续，重点审核：是否设立内容管理负责人，有与业务范围和服务规模相适应的内容审核人员；是否有健全的内容安全、人员管理培训等制度。网络信息内容服务平台应当根据MCN机构合规情况、旗下账号数量及其粉丝总数量等指标维度，建立分级管理制度，并采取相应管理措施防范信息内容风险。

原文链接：

https://www.cac.gov.cn/2025-01/10/c\_1738209405008163.htm

**2.美国土安全部发布《公共部门生成式人工智能部署手册》**

1月7日，美国国土安全部发布《公共部门生成式人工智能部署手册》，旨在帮助政府官员通过负责任、有效地部署生成式人工智能（GenAI）技术来改进公共服务。手册基于试点经验，提供了七个可操作步骤，包括开发任务增强型的GenAI用例、建立联盟和实施有效治理、利用工具和基础设施、使用负责任和可信任的AI、测量和监测、员工培训和人才招聘、建立用户反馈机制，为公共部门负责任地使用GenAI技术提供指导框架。

原文链接：

https://www.dhs.gov/sites/default/files/2025-01/25\_0106\_ocio\_dhs-playbook-for-public-sector-generative-artificial-intelligence-deployment-508-signed.pdf

**3.国家发改委等三部门印发《国家数据基础设施建设指引》**

1月6日，国家发展改革委、国家数据局、工业和信息化部印发《国家数据基础设施建设指引》。该文件共9章，包括概念内涵、发展愿景、总体架构、重点方向、算力底座、网络支撑、安全防护、组织保障等。该文件提出，国家数据基础设施是从数据要素价值释放的角度出发，面向社会提供数据采集、汇聚、传输、加工、流通、利用、运营、安全服务的一类新型基础设施。国家数据基础设施安全保障体系建设重点是构建多层次、全方位、立体化的国家数据基础设施安全保障框架，贯穿数据生命周期全流程。该文件专门设立了“安全防护”章节，重点对国家数据基础设施安全保障、数据流通利用安全提出具体要求。

原文链接：

https://www.ndrc.gov.cn/xxgk/zcfb/tz/202501/P020250106319424108511.pdf

**往期精彩推荐**

[【已发现在野利用】Ivanti 多款产品缓冲区溢出漏洞(CVE-2025-0282)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502739&idx=1&sn=dfc7e53a7f1679e3893025a8bbeaaf98&token=477793876&lang=zh_CN&scene=21#wechat_redirect)
[ALPC 之殇 - 8月未知 Windows 在野提权 Nday 漏洞研究](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502729&idx=1&sn=7ef5d7ec018d1cb5555c10fcdd5b2159&token=477793876&lang=zh_CN&scene=21#wechat_redirect)

[SonicOS SSLVPN 认证绕过漏洞(CVE-2024-53704)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502727&idx=1&sn=08794a77a389f88e8cac276f31020a10&token=477793876&lang=zh_CN&scene=21#wechat_redirect)

本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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