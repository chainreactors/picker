---
title: 安全热点周报：大规模 PSAUX 勒索软件攻击瞄准 22,000 个 Cyber​​Panel 实例
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502393&idx=1&sn=56da5e531eb88ae8b5bfc24fea45484f&chksm=fe79eea1c90e67b722d74edcc3a5b08f2ebab56072a7893670316a87fcd2790352b202f20743&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-11-12
fetch_date: 2025-10-06T19:18:59.405287
---

# 安全热点周报：大规模 PSAUX 勒索软件攻击瞄准 22,000 个 Cyber​​Panel 实例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibJYVaicpJO1bIutLibcyXbQltImQJTxPyNN0PHgVgq9r4E0T8W7SibibW2ZicUMaiccJgibkegZcjMdwskw/0?wx_fmt=jpeg)

# 安全热点周报：大规模 PSAUX 勒索软件攻击瞄准 22,000 个 Cyber​​Panel 实例

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 德国司法部发布计算机刑法修正草案，保护白帽黑客行为 |
| • 美国政府发布《联邦零信任数据安全指南》 |
| • 美国知名军工芯片厂商因勒索攻击损失超1.5亿元 |

**PART****0****1**

**新增在野利用**

**1.****Palo Alto Networks Expedition 身份认证绕过漏洞(CVE-2024-5910)**

11 月 7 日，Palo Alto Networks 的 Expedition 工具中存在身份认证绕过漏洞，现在危及各个部门的防火墙配置，攻击者正在积极利用此漏洞。

美国网络安全和基础设施安全局 (CISA) 就 Palo Alto Networks 的 Expedition 工具中存在一个被积极利用的漏洞发出紧急警报。该漏洞编号为 CVE-2024-5910，它构成严重威胁，允许攻击者接管管理帐户，使配置机密和凭据面临风险。

Expedition 在防火墙迁移和管理中的广泛使用使得该漏洞对于依赖此工具从其他防火墙无缝过渡到 Palo Alto 的 PAN-OS 的组织尤其令人担忧。

10 月份，来自 Horizon3.ai 的安全研究员 Zach Hanley 发布了漏洞 PoC，此后 CVE-2024-5910 带来的风险可能进一步升级。该 PoC 演示了如何将 CVE-2024-5910 与另一个漏洞CVE-2024-9464（命令注入漏洞）结合使用，从而在易受攻击的系统上实现远程任意命令执行。通过串联这些漏洞，攻击者能够重置管理员凭据，并可能控制 PAN-OS 防火墙配置。

这种复合风险加剧了人们的担忧，因为攻击者可以利用 Expedition 身份认证绕过漏洞，从而未经授权访问敏感网络资源。

CVE-2024-5910 漏洞体现了保护重要网络管理工具的持续挑战。此漏洞（尤其是由于其与关键防火墙迁移软件集成）强调了立即主动进行漏洞管理的必要性。定期修补、严格的凭证轮换和限制网络访问仍然是防范此类漏洞的重要措施。

尽管 Palo Alto Networks于 7 月份发布了补丁，但现在仍发现存在漏洞，敦促使用 Expedition 1.2.92 以下版本的任何组织立即采取补救措施。

参考链接：

https://thecyberexpress.com/cisa-alerts-of-cve-2024-5910-exploitation/

**2.****Google Android 输入验证不当漏洞(CVE-2024-43093)**

11 月 7 日，谷歌警告称，影响其 Android 操作系统的安全漏洞已遭到广泛利用。

根据代码提交消息，该漏洞的编号为 CVE-2024-43093，被描述为 Android 框架组件中的权限提升漏洞，可能导致未经授权访问“Android/data”、“Android/obb”和“Android/sandbox”目录及其各自的子目录。

目前尚无关于该漏洞如何在现实世界的攻击中被利用的详细信息，但谷歌在其月度公告中承认，有迹象表明该漏洞“可能受到有限的、有针对性的利用”。

该科技巨头还指出，高通芯片组中现已修复的安全漏洞 CVE-2024-43047 已被积极利用。该漏洞是数字信号处理器 (DSP) 服务中的一个释放后使用漏洞，成功利用该安全漏洞可能会导致内存损坏。

CVE-2024-43093 是继 CVE-2024-32896 之后第二个被积极利用的 Android 框架漏洞，谷歌早在 2024 年 6 月和 9 月就修复了该漏洞。目前还不清楚这两个安全漏洞是否被设计成一个漏洞利用链，以提升权限并实现代码执行。虽然该漏洞最初仅针对 Pixel 设备得到解决，但该公司后来证实该漏洞影响了更广泛的 Android 生态系统。

建议受影响的客户尽快升级至最新的安全版本。

参考链接：

https://thehackernews.com/2024/11/google-warns-of-actively-exploited-cve.html

**3.****CyberPanel upgrademysqlstatus 远程命令执行漏洞(CVE-2024-51567)**

11 月 7 日，超过 22,000 个 CyberPanel 实例在线暴露于关键的远程代码执行 （RCE） 漏洞，成为 PSAUX 勒索软件攻击的大规模目标，该攻击导致几乎所有实例离线。

安全研究员 DreyAnd 透露，CyberPanel 2.3.6（可能还有 2.3.7）存在三个不同的安全问题，这些问题可能导致漏洞利用，允许未经身份验证的远程 root 访问。

威胁情报搜索引擎 LeakIX 报告称，有21,761个存在漏洞的CyberPanel实例在网上曝光，其中近一半（10,170个）位于美国。然而，一夜之间，实例数量神秘地下降到仅剩约 400 个，LeakIX 称受影响的服务器不再可访问。

网络安全研究员 Gi7w0rm 在 X 上发推文称，这些实例管理着超过 152,000 个域和数据库，而 CyberPanel 充当着中央访问和管理系统。黑客大规模利用暴露的 CyberPanel 服务器来安装PSAUX 勒索软件。

PSAUX 勒索软件自 2024 年 6 月以来一直存在，通过漏洞和错误配置来攻击暴露的 Web 服务器。在服务器上启动后，勒索软件将创建唯一的 AES 密钥和 IV，并使用它们加密服务器上的文件。加密文件的文件名将附加 .psaux 扩展名。勒索软件还会在每个文件夹中创建名为 index.html 的勒索信，并将勒索信复制到 /etc/motd，以便在用户登录设备时显示。完成后，使用封闭的 RSA 密钥加密 AES 密钥和 IV，并将其保存为/var/key.enc和/var/iv.enc。

LeakIX 和 Chocapikk 获得了此次攻击所使用的脚本，其中包括一个用于利用 CyberPanel 漏洞的 ak47.py 脚本，以及另一个用于加密文件的名为 Actually.sh 的脚本。

由于 PSAUX 勒索软件加密文件的方式存在缺陷，因此可以使用 LeakIX 创建的解密器免费解密文件。

需要注意的是，如果黑客使用了不同的加密密钥，那么使用错误的密钥解密可能会损坏数据。因此，在尝试使用此解密器之前，请务必备份数据，以先测试其是否有效。

由于 CyberPanel 漏洞遭到积极利用，强烈建议用户尽快升级到GitHub 上的最新版本。

参考链接：

https://www.bleepingcomputer.com/news/security/massive-psaux-ransomware-attack-targets-22-000-cyberpanel-instances/

**4.****PTZOptics PT30X-SDI/NDI 摄像机身份认证绕过漏洞(CVE-2024-8956)****&****PTZOptics PT30X-SDI/NDI 摄像机操作系统命令注入漏洞(CVE-2024-8957)**

11 月 4 日，黑客正试图利用工业、医疗保健、商务会议、政府和法庭环境中使用的 PTZOptics 云台变焦 (PTZ) 实时流媒体摄像机中的两个零日漏洞。

在今年 4 月，GreyNoise 的人工智能威胁检测工具 Sift 在其蜜罐网络上检测到与任何已知威胁都不匹配的异常活动，发现了 CVE-2024-8956 和 CVE-2024-8957。在检查警报后，GreyNoise 研究人员发现了一个针对摄像机基于 CGI 的 API 和嵌入的“ntp\_client”的漏洞攻击尝试，旨在实现命令注入。GreyNoise 研究员 Konstantin Lazarev 通过技术深入研究提供了有关这两个漏洞的更多信息。

CVE-2024-8956 是摄像机“lighthttpd”网络服务器中的一个弱身份验证问题，允许未经授权的用户在没有授权标头的情况下访问 CGI API，从而暴露用户名、MD5 密码哈希和网络配置。CVE-2024-8957 是由于“ntp\_client”二进制文件处理的“ntp.addr”字段中的输入清理不足引起的，允许攻击者使用特制的有效载荷插入命令以进行远程代码执行。

Greynoise 指出，利用这两个漏洞可能会导致摄像头完全被接管、被机器人感染、转移到连接同一网络的其他设备或中断视频源。该网络安全公司报告称，虽然初始活动的源头在蜜罐攻击后不久就消失了，但 6 月份观察到了使用 wget 下载 shell 脚本进行反向 shell 访问的单独尝试。

受这两个缺陷影响的设备是基于海思 Hi3516A V600 SoC V60、V61 和 V63 的支持 NDI 的摄像机，运行的 VHD PTZ 摄像机固件版本早于 6.3.40。其中包括 PTZOptics、Multicam Systems SAS 摄像机和 SMTAV Corporation 设备的几种型号。

PTZOptics 于 9 月 17 日发布了安全更新，但 PT20X-NDI-G2 和 PT12X-NDI-G2 等型号由于已达到使用寿命而未获得固件更新。后来，GreyNoise 发现至少有两款较新的型号 PT20X-SE-NDI-G3 和 PT30X-SE-NDI-G3 也受到了影响，这两款型号也没有收到补丁。

用户应该咨询其设备供应商，了解其设备的最新可用固件更新中是否已包含针对 CVE-2024-8956 和 CVE-2024-8957 的修复。

参考链接：

https://www.bleepingcomputer.com/news/security/hackers-target-critical-zero-day-vulnerability-in-ptz-cameras/

**PART****0****2**

**安全事件**

**1.美国知名军工芯片厂商因勒索攻击损失超1.5亿元**

11月6日SecurityWeek消息，美国知名军工半导体厂商微芯科技（Microchip）5日发布最新财报披露，因近期网络安全事件，公司已产生2140万美元（约合人民币1.53亿元）的相关费用。此次事件在8月首次曝光，当时微芯科技发现其网络系统中出现了可疑活动，并直接导致公司部分制造设施的生产中断。大约一周后，勒索软件团伙Play宣称对此次攻击负责。该团伙公布了一个4GB大小的压缩文件，声称其中包含微芯科技的内部数据。这些数据据称包括个人信息、客户文件以及与预算、工资、会计、合同、税务和财务等相关的文件。9月初，在恢复大部分运营后，微芯科技确认，威胁行为者确实从其系统中窃取了一些信息，其中包括员工的联系方式和密码哈希值。

原文链接：

https://www.securityweek.com/microchip-technology-reports-21-4-million-cost-from-ransomware-attack/

**2.施耐德电气遭数据勒索：开发平台访问凭证暴露 40GB数据失窃**

11月4日BleepingComputer消息，能源管理巨头施耐德电气确认，内部一个开发平台遭入侵。此前有威胁行为者声称，利用暴露的凭证从该公司JIRA服务器窃取了40GB数据，并威胁索要价值12.5万美元的赎金。施耐德电气表示：“公司正在调查一起网络安全事件，涉及未经授权访问我们内部的项目执行跟踪平台之一，该平台位于一个隔离的环境中。公司全球事件响应团队已立即动员应对此事件。施耐德电气的产品和服务未受到影响。”

原文链接：

https://www.bleepingcomputer.com/news/security/schneider-electric-confirms-dev-platform-breach-after-hacker-steals-data/

**3.德国大型药品批发商遭勒索攻击，欲扰乱超6000家药房供应**

11月1日GovinfoSecurity消息，德国药品批发商AEP在10月28日遭遇勒索软件攻击，部分IT系统被加密，通信系统也受到影响，无法处理订单导致供应链中断，只能向药店提供有限范围的供货。AEP负责向全德境内6000多家药房供应药品，据悉目前尚未导致药品短缺。巴伐利亚药剂师协会表示，巴伐利亚州的药品供应不存在风险，药房通常会多家批发商合作。

原文链接：

https://www.govinfosecurity.com/german-pharma-wholesaler-aep-targeted-in-ransomware-attack-a-26704

**PART****0****3**

**政策法规**

**1.美国运输安全管理局发布拟议规则，要求管道和铁路公司必须建立网络风险管理计划**

11月6日，美国运输安全管理局发布《加强地面网络风险管理》拟议规则，要求部分铁路、轨道交通和管道等地面运输系统的所有者和运营者执行网络风险管理和事件报告要求。该文件沿袭了运输安全管理局2021年以来年度安全指令的基于绩效的网络安全要求，并基于NIST网络安全框架、CISA跨部门网络安全绩效目标等成果，主要提出三方面要求，一是建立健全网络风险管理计划，二是向CISA报告网络安全事件，三是指定一名物理安全协调员专门向运输安全管理局报告重大物理安全问题。该文件将在2025年2月5日截止征求意见。

原文链接：

https://www.federalregister.gov/documents/2024/11/07/2024-24704/enhancing-surface-cyber-risk-management

**2.《网络安全技术 终端计算机通用安全技术规范》等3项国家标准获批发布**

11月5日，根据2024年10月26日国家市场监督管理总局、国家标准化管理委员会发布的中华人民共和国国家标准公告（2024年第24号），全国网络安全标准化技术委员会归口的3项网络安全国家标准正式发布。具体包括《网络安全技术 终端计算机通用安全技术规范》《网络安全技术 存储介质数据恢复服务安全规范》《网络安全技术 网络弹性评价准则》。

原文链接：

https://mp.weixin.qq.com/s/k-8W75M4HrN8is8iQjeEmQ

**3.德国司法部发布计算机刑法修正草案，保护白帽黑客行为**

11月4日，德国联邦司法部发布计算机刑法修正草案公正征求意见，明确研究IT安全漏洞的法律责任。该文件主要提出了两方面修改，一是将发现安全漏洞行为排除犯罪，确保发现并负责任报告安全漏洞的研究人员不会有承担刑事责任的风险；二是加大对网络间谍活动的处罚，如刺探和拦截数据符合特别严重案件标准或导致德国关键基础设施、国家安全受到损害，可处以3个月到5年有期徒刑。德国联邦司法部长Marco Buschmann博士表示：“那些致力于弥补IT安全漏洞的人，应该得到的是表彰，而不是检察官的诉讼通知。”此前美国、欧洲比利时、马其他等国均有修订法律，对白帽黑客行为可豁免起诉。

原文链接：

https://www.bmj.de/SharedDocs/Gesetzgebungsverfahren/DE/2024\_ComputerStrafR.html

**4.美国政府发布《联邦零信任数据安全指南》**

10月31日，美国联邦首席数据官委员会、联邦首席信息安全官委员会等联邦政府IT领导层联合发布了《联邦零信任数据安全指南》，旨在强化数据安全实践。该文件共42页，重点强调了“保护数据本身，而非保护数据的边界”。官方认为这一理念是“有效实施零信任的基础支柱”之一。该文件提出了5个步骤的零信任安全路线图，概述了实践者可以采取的具体行动，包括发现、清点、分类、标记和映射数据流，进行风险分析，与零信任架构对齐，设计控制和监控，拥抱自动化和编排。

原文链接：

https://www.cio.gov/assets/files/Zero-Trust-Data-Security-Guide\_Oct24-Final.pdf

**往期精彩推荐**

[安全热点周报：墨西哥大型机场集团疑遭勒索攻击，旗下13个机场紧急切换备用系统](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502377&idx=1&sn=cdd8a31fd2656366935dc52ad269c97a&chksm=fe79eeb1c90e67a7c77f1742759fc5656294e63519978cad3a07aa7397c9e9759c111677ad7e&token=1825665179&lang=zh_CN&scene=21#wechat_redirect)
[【已复现】Spring Security 静态资源权限绕过漏洞(CVE-2024-38821)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502372&idx=1&sn=400ea5c9c064b177d0b240c397a749d5&chksm=fe79eebcc90e67aa16307551e35b7b7002d193a6cdbe965ed72a47d1db7eed6fd3f08142a32d&token=1825665179&lang=zh_CN&scene=21#wechat_redirect)

[【已复现】Apache Solr 身份认证绕过漏洞(CVE-2024-45216)安全风险通告第二次更新](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502355&idx=1&sn=d02ee95b980e1540ef75c5a0f0f10f5b&chksm=fe79ee8bc90e679d2beeef7ce3ff4a032f4e9bd79fe2e0f3f690b65ed6e720af290e491fcc2a&token=1825665179&lang=zh_CN&scene=21#wechat_redirect)

本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅...