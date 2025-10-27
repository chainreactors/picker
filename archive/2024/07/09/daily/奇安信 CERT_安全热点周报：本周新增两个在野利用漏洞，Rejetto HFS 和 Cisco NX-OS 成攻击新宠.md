---
title: 安全热点周报：本周新增两个在野利用漏洞，Rejetto HFS 和 Cisco NX-OS 成攻击新宠
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501601&idx=3&sn=5a721709a3e5979ffcd7cec5b864469e&chksm=fe79e3b9c90e6aafcb24bdd898611c1af81431e26390014f34f2f32906b5737047b819609e87&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-09
fetch_date: 2025-10-06T17:45:42.449059
---

# 安全热点周报：本周新增两个在野利用漏洞，Rejetto HFS 和 Cisco NX-OS 成攻击新宠

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48e0HwtNShIEv3GUPwMXgGCsfSjkXicFjMHm8XicHNbzI5n7MkU5aznwiaRshq9lmaMnhLqF7a5DKicNw/0?wx_fmt=jpeg)

# 安全热点周报：本周新增两个在野利用漏洞，Rejetto HFS 和 Cisco NX-OS 成攻击新宠

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 美国空军部首席信息官办公室发布《空军部零信任战略》 |
| • 美国大型银行因勒索攻击关闭系统多天，客户无法访问账户或交易 |
| • 著名远控软件TeamViewer IT系统遭APT攻陷，安全专家建议暂时删除 |

**PART****0****1**

**漏洞情报**

**1.Apache Tomcat拒绝服务漏洞安全风险通告**

7月5日，奇安信CERT监测到官方修复Apache Tomcat HTTP/2拒绝服务漏洞(CVE-2024-34750)，该漏洞是一个拒绝服务漏洞，Apache Tomcat在处理HTTP/2流时，未能正确处理某些异常HTTP头情况，导致HTTP/2流计数错误，从而导致处理该请求时允许无限超时，无法关闭本应该终止的连接。鉴于此漏洞影响范围较大，建议客户尽快做好自查及防护。

**2.Artifex Ghostscript格式字符串漏洞安全风险通告**

7月3日，奇安信CERT监测到官方修复Artifex Ghostscript格式字符串漏洞(CVE-2024-29510)，Ghostscript中存在格式字符串注入可导致Shell命令执行，未经身份认证的本地攻击者通过特制文件利用该漏洞可以实现代码执行，在Linux操作系统上可用于鱼叉攻击，如将恶意esp文件嵌入到LibreOffice文档文件，用户通过LibreOffice打开文档将导致代码执行。目前该漏洞技术细节与EXP已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**3.GeoServer远程代码执行漏洞安全风险通告**

7月3日，奇安信CERT监测到官方修复GeoServer远程代码执行漏洞(CVE-2024-36401)，由于该系统不安全地将属性名称解析为XPath表达式，未经身份认证的远程攻击者可以通过该漏洞在服务器上执行任意代码，从而获取服务器权限。目前该漏洞技术细节与EXP已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**4.OpenSSH远程代码执行漏洞安全风险通告**

7月1日，奇安信CERT监测到官方修复OpenSSH远程代码执行漏洞(CVE-2024-6387)，该漏洞是由于OpenSSH服务器（sshd)中的信号处理程序竞争问题，未经身份验证的攻击者可以利用此漏洞在Linux系统上以root身份执行任意代码。目前该漏洞技术细节和POC已在互联网上公开，该漏洞为之前CVE-2006-5051的二次引入，当前的漏洞利用代码仅针对在32位Linux系统上运行的OpenSSH，64位Linux系统上利用该漏洞的难度会更大，在Linux系统上以Glibc编译的OpenSSH上成功利用，不过利用过程复杂、成功率不高且耗时较长。平均要大于10000次才能赢得竞争条件，需要6~8小时才能获得远程root shell。在以非Glibc编译的OpenSSH上利用此漏洞也是可能的，但尚未证实。虽然目前还没有发现真正实现远程代码执行的POC，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**PART****0****2**

**新增在野利用**

**1.****Rejetto HTTP File Server 模板注入漏洞(CVE-2024-23692)**

7月 4 日，黑客瞄准 Rejetto 的旧版本 HTTP 文件服务器 (HFS)，以投放恶意软件和加密货币挖掘软件。该漏洞于 2024 年 5 月披露，此后被攻击者利用来安装恶意软件并控制易受攻击的系统。Rejetto HTTP 文件服务器（包括 2.3m 版本）存在模板注入漏洞。此漏洞允许远程未经身份验证的攻击者通过发送特制的 HTTP 请求在受影响的系统上执行任意命令。

安全公司 AhnLab 的威胁研究人员发现威胁行为者正在积极利用 CVE-2024-23692，这是一个严重程度极高的安全漏洞，允许在无需身份验证的情况下执行任意命令。

研究人员表示，在攻击期间，黑客会收集有关系统的信息，安装后门和各种其他类型的恶意软件。攻击者执行“whoami”和“arp”等命令来收集有关系统和当前用户的信息，发现连接的设备，并通常计划后续操作。在许多情况下，攻击者在将新用户添加到管理员组后会终止 HFS 进程，以防止其他威胁行为者使用它。

在攻击的下一阶段，ASEC 观察到用于挖掘门罗币加密货币的 XMRig 工具的安装。研究人员指出，XMRig 至少在四次不同的攻击中被部署，其中一次是由 LemonDuck 威胁组织实施的。

传送到受感染计算机的其他有效载荷包括：

XenoRAT – 与 XMRig 一起部署，实现远程访问和控制。

Gh0stRAT – 用于从被攻破的系统中实施远程控制和窃取数据。

PlugX – 一种主要与讲中文的威胁行为者相关的后门，用于持续访问。

GoThief - 一种使用 Amazon AWS 窃取数据的信息窃取程序。它会捕获屏幕截图、收集桌面文件信息并将数据发送到外部命令和控制 (C2) 服务器。

随着黑客不断开发复杂的方法来利用漏洞，保持警惕和主动的网络安全实践比以往任何时候都更加重要。

参考链接：

https://www.bleepingcomputer.com/news/security/hackers-attack-hfs-servers-to-drop-malware-and-monero-miners/

**2.Cisco NX-OS Software命令执行漏洞(CVE-2024-20399)**

7月 2 日，美国网络安全和基础设施安全局 (CISA) 在其已知利用漏洞 (KEV) 目录中添加Cisco NX-OS Software命令执行漏洞(CVE-2024-20399)，Cisco NX-OS 在命令行界面 (CLI) 中包含命令注入漏洞，该漏洞可能允许经过身份验证的本地攻击者在受影响设备的底层操作系统上以 root 身份执行命令。

思科已修复 4 月份攻击中利用的 NX-OS 零日漏洞，该漏洞可使易受攻击的交换机以 root 身份安装之前未知的恶意软件。网络安全公司 Sygnia 向思科报告了这些事件，并将这些攻击与其追踪的名为 Velvet Ant 的黑客组织联系起来。

Sygnia 事件响应主管 Amnon Kushnir 回答说：“Sygnia 在对我们追踪的 Velvet Ant 黑客组织进行更大规模的取证调查时发现了这种攻击。”

威胁行为者收集了管理员级别的凭证，以获得对思科Nexus交换机的访问权限，并部署了一种之前未知的自定义恶意软件，允许他们远程连接到被入侵的设备，上传其他文件并执行恶意代码。该安全漏洞还使攻击者能够在不触发系统 syslog 消息的情况下执行命令，从而允许他们隐藏被黑客入侵的 NX-OS 设备上的入侵迹象。

思科建议客户定期监控和更改网络管理员和 vdc 管理员管理用户的凭证。管理员可以使用思科软件检查器页面来确定其网络上的设备是否面临针对 CVE-2024-20399 漏洞的攻击。

参考链接：

https://www.bleepingcomputer.com/news/security/cisco-warns-of-nx-os-zero-day-exploited-to-deploy-custom-malware/

**PART****0****3**

**安全事件**

**1.美国大型银行因勒索攻击关闭系统多天，客户无法访问账户或交易**

7月2日Bleeping Computer消息，美国最大的信用合作社之一Patelco披露，公司6月29日遭遇了一次勒索软件攻击，为了控制事件影响主动关闭了多个面向客户的银行系统。Patelco公告显示，网银、移动应用、电子交易等多类服务均不可用，借记卡、信用卡交易服务可用单功能受影响。7月3日，Patelco透露核心系统已经通过网络安全专家检查，客户资金安全不存在问题。由于此次勒索软件攻击事件，超40万客户至少连续5天无法访问账户或进行交易。

原文链接：

https://www.bleepingcomputer.com/news/security/patelco-shuts-down-banking-systems-following-ransomware-attack/

**2.著名远控软件TeamViewer IT系统遭APT攻陷，安全专家建议暂时删除**

6月29日The Record消息，国际知名远程连接软件厂商TeamViewer在28日确认，一家极其活跃的俄罗斯黑客组织在本周早些时候入侵了其内部IT环境。TeamViewer后续将此次攻击事件归咎于APT29，据悉该组织隶属于俄罗斯的对外情报局（SVR），曾发起2020年的SolarWinds黑客事件和2016年对美国民主党全国委员会的攻击。TeamViewer公司多次更新公告强调，此次攻击的受影响范围仅限内部IT环境，不涉及产品、TeamViewer连接平台或任何客户数据。由于近年来供应链攻击屡创纪录，有安全专家建议暂时删除TeamViewer。

原文链接：

https://therecord.media/teamviewer-cozy-bear-hack-confirmed

**PART****0****4**

**政策法规**

**1.四部门联合印发《国家人工智能产业综合标准化体系建设指南（2024版）》**

7月2日消息，工业和信息化部、中央网信办、国家发展改革委、国家标准委等四部门近日联合印发《国家人工智能产业综合标准化体系建设指南（2024版）》。该文件提出，人工智能标准体系结构包括基础共性、基础支撑、关键技术、智能产品与服务、赋能新型工业化、行业应用、安全/治理等7个部分。在安全标准方面，要求规范人工智能技术、产品、系统、应用、服务等全生命周期的安全要求，包括基础安全，数据、算法和模型安全，网络、技术和系统安全，安全管理和服务，安全测试评估，安全标注，内容标识，产品和应用安全等标准。该文件还提出，到2026年我国新制定国家标准和行业标准50项以上，引领人工智能产业高质量发展的标准体系加快形成。

原文链接：

https://www.miit.gov.cn/cms\_files/filemanager/1226211233/attach/20246/c1a193215d5c4b08872362d0f8673303.pdf

**2.美国空军部首席信息官办公室发布《空军部零信任战略》**

7月2日，美国空军部首席信息官办公室发布《空军部零信任战略》，旨在加强空军部网络安全态势，为作战人员提供有保障且安全的数据访问，以应对战争并阻止对手实现信息优势。该文件结合《国防部零信任战略》提出了7个战略目标，包括实现应用级可见性和控制、数据成为新的边界、向合理的实体和诉求提供合理的访问权限、降低单一设备风险、随时随地访问受保护资源、基于安全策略的自动安全响应、改进检测和响应时间。

原文链接：

https://www.safcn.af.mil/Portals/64/Documents/Strategy/DAF%20Zero%20Trust%20Strategy%20v1.0.pdf

**往期精彩推荐**

[Apache Tomcat 拒绝服务漏洞(CVE-2024-34750)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501571&idx=1&sn=574d5dec651b6103d4d6e0e82d891092&chksm=fe79e39bc90e6a8dacf59710b83f675ab7664964c63de9aa806e385bde1a9b195dd4a826e6d5&token=1331452273&lang=zh_CN&scene=21#wechat_redirect)
[AI助手免费来相助，攻防演习效率飙升如神助](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501562&idx=1&sn=4a00c3abdcbb76fc2e00deb2c0a09b6b&chksm=fe79e262c90e6b74fc3b0222716306fe40798a051ad0be0a6d6f6eaf15c204113dda23001c5f&token=1331452273&lang=zh_CN&scene=21#wechat_redirect)

[【已复现】Artifex Ghostscript 格式字符串漏洞(CVE-2024-29510)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501557&idx=1&sn=2f95ff3464d185b4263b8acc95558791&chksm=fe79e26dc90e6b7b242e9542acdefc3d46ec39ec55f8a6ac358497e43cd0eab437359fd962c1&token=1331452273&lang=zh_CN&scene=21#wechat_redirect)

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