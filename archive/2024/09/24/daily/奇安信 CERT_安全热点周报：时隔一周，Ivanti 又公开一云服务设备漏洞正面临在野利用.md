---
title: 安全热点周报：时隔一周，Ivanti 又公开一云服务设备漏洞正面临在野利用
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502185&idx=1&sn=4c979dfd0e63af2bb96c91360d9e23d9&chksm=fe79edf1c90e64e7751ef785fcb7e26cf09d317648d2b36002ac1b42ec41a60b323d60527343&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-09-24
fetch_date: 2025-10-06T18:27:31.923784
---

# 安全热点周报：时隔一周，Ivanti 又公开一云服务设备漏洞正面临在野利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icjnXcBWBSHEiaBnOrJNiaOhs98kopBLGusaGzPc4wyFERa44nUzYUgDNy2IdMb5icXIPkfoiaa4qlmzw/0?wx_fmt=jpeg)

# 安全热点周报：时隔一周，Ivanti 又公开一云服务设备漏洞正面临在野利用

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 《网络安全标准实践指南——敏感个人信息识别指南》发布 |
| • 供应商泄露用户数据，美国电信巨头AT&T被罚超9000万元 |
| • 黎巴嫩寻呼机遭远程攻击大规模爆炸，致使9人死亡数千人受伤 |

**PART****0****1**

**漏洞情报**

**1.GitLab SAML认证绕过漏洞安全风险通告**

9月19日，奇安信CERT监测到官方修复GitLab SAML认证绕过漏洞(QVD-2024-40180)，由于GitLab对SAML响应的不当处理，使得攻击者可以插入任意值，攻击者从而通过构造特定的SAML响应，绕过GitLab实例的身份验证机制，无需正确的凭证即可访问受保护的资源。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为1372328个，关联IP总数为24944个。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**2.Ivanti Cloud Service Appliance命令注入漏洞在野利用风险通告**

9月19日，奇安信CERT监测到Ivanti Cloud Service Appliance命令注入漏洞(CVE-2024-8190)技术细节与EXP已公开，该漏洞是由于后台未对传入的TIMEZONE参数做校验，而是直接传给exec() 函数执行，从而导致拥有管理员权限的攻击者执行任意命令。奇安信鹰图资产测绘平台数据显示，该漏洞关联的全球风险资产总数为11321个，关联IP总数为2249个。奇安信威胁情报中心安全研究员已成功复现漏洞，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**3.VMware vCenter Server堆溢出漏洞安全风险通告**

9月18日，奇安信CERT监测到官方修复VMware vCenter Server堆溢出漏洞(CVE-2024-38812)，VMware vCenter Server在DCERPC协议实施过程中存在堆溢出漏洞，攻击者可发送特制的网络数据包来触发此漏洞从而导致远程代码执行。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为13314个，关联IP总数为3017个。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**PART****0****2**

**新增在野利用**

**1.****Ivanti Cloud Service Appliance 任意文件读取漏洞(CVE-2024-8963)**

9月19日，Ivanti 警告称，黑客正在利用一个云服务设备 (CSA) 安全漏洞针对有限数量的客户发起攻击。该漏洞编号为CVE-2024-8963 ，是由路径遍历引起的。成功利用该漏洞可让远程未经身份验证的攻击者访问易受攻击的 CSA 系统（用作网关，为企业用户提供对内部网络资源的安全访问）上的受限功能。

攻击者将 CVE-2024-8963 与 CVE-2024-8190 链接在一起来绕过管理员身份验证并在未修补的设备上执行任意命令。

Ivanti 建议管理员检查端点检测和响应 (EDR) 或其他安全软件的警报以及新管理用户或修改后的管理用户的配置设置和访问权限，以检测攻击尝试。他们还应确保双宿主 CSA 配置，以 eth0 作为内部网络，以大幅降低被利用的风险。

该公司进一步警告称：“如果您怀疑受到攻击，Ivanti 建议您使用补丁 519（发布于 2024 年 9 月 10 日）重建您的 CSA。强烈建议尽可能升级到 CSA 5.0”。

Ivanti CSA 4.6 已停用，不再接收针对操作系统或第三方库的补丁。此外，随着停用状态的出现，9 月 10 日发布的修复是 Ivanti 将向后移植到该版本的最后一个修复。

参考链接：

https://www.bleepingcomputer.com/news/security/ivanti-warns-of-another-critical-csa-flaw-exploited-in-attacks/

**2.****Apache HugeGraph-Server 远程命令执行漏洞(CVE-2024-27348)**

9月18日，美国网络安全和基础设施局 (CISA) 在其已知利用漏洞 (KEV) 目录中添加了影响 Apache HugeGraph-Server 的远程代码执行 (RCE) 漏洞。该漏洞的编号为CVE-2024-27348，级别为严重（CVSS v3.1 评分：9.8），是一个不当的访问控制漏洞，影响 HugeGraph-Server 1.0.0 及以上版本（但不包括 1.3.0）。

Apache 于 2024 年 4 月 22 日发布 1.3.0 版本修复了该漏洞。除了升级到最新版本外，还建议用户使用 Java 11 并启用 Auth 系统。此外，还提出了启用“白名单IP/端口”功能以提高RESTful-API执行的安全性，该功能涉及潜在的攻击链。

本周，CISA 警告称，已经发现有人在野积极利用 CVE-2024-27348 ，并要求联邦机构和其他关键基础设施组织必须在 2024 年 10 月 9 日之前采取缓解措施或停止使用该产品。

Apache HugeGraph-Server 是 Apache HugeGraph 项目的核心组件，这是一个开源图形数据库，旨在以高性能和可扩展性处理大规模图形数据，支持深度关系开发、数据聚类和路径搜索所需的复杂操作。该产品主要被电信供应商用于欺诈检测和网络分析、金融服务用于风险控制和交易模式分析、社交网络用于连接分析和自动推荐系统。

随着积极开发的进行和产品在高价值企业环境中的使用，尽快应用可用的安全更新和缓解措施势在必行。

参考链接：

https://www.bleepingcomputer.com/news/security/cisa-warns-of-windows-flaw-used-in-infostealer-malware-attacks/

**PART****0****3**

**安全事件**

**1.供应商泄露用户数据，美国电信巨头AT&T被罚超9000万元**

9月17日CyberScoop消息，美国联邦通信委员会（FCC）与AT&T就2023年1月发生的重大数据泄露事件达成了一项1300万美元（约合人民币9181万元）的和解协议，该事件导致AT&T超过890万名移动客户的信息被窃取。根据和解协议，AT&T向一家提供用于营销、账单处理和生成个性化视频内容服务的供应商共享了大量客户数据，双方签署合同明确了数据保护和删除要求，此前多年评估均显示该供应商遵循了数据删除政策，但本该被删除的数据却在2023年1月泄露。FCC最终认定，AT&T对这一失误负有不可推卸的最终责任，并要求其实施安全改进计划。FCC执法局局长Loyaan Egal指出，这份和解协议提醒企业，FCC正对企业在供应链中如何确保客户数据安全进行更为严格的审查。

原文链接：

https://cyberscoop.com/att-agrees-to-13-million-dollar-fcc-fine/

**2.黎巴嫩寻呼机遭远程攻击大规模爆炸，致使9人死亡数千人受伤**

9月17日综合消息，黎巴嫩真主党17日发表声明，该组织多名成员携带的寻呼机当天下午发生爆炸，已造成多名黎巴嫩真主党成员死亡，并在全国范围内造成大量人员受伤。黎巴嫩公共卫生部长阿卜亚德称，爆炸已造成9人死亡，约有2800人受伤，其中约200人伤情危重。据悉，黎巴嫩真主党武装人员近来较为普遍地使用寻呼机，以通过这种技术含量较低的通信设备避免以色列追踪他们的位置。此次发生寻呼机爆炸的地点主要集中在贝鲁特南郊、黎巴嫩南部以及贝卡谷地等地，这些都被认为是黎巴嫩真主党据点所在地。多方消息显示，可能是真主党采购的某批次寻呼机被以色列截获篡改植入炸药，真主党未发现继续分发使用。纽约时报称，这些寻呼机在当天下午同时收到一条看似来自真主党领导层的消息，发出振动/蜂鸣声几秒后发生爆炸，尚不确定引爆指令是这条消息还是其他信号。

原文链接：

https://www.latimes.com/world-nation/story/2024-09-17/pagers-explode-in-lebanon

**PART****0****4**

**政策法规**

**1.《网络安全标准实践指南——敏感个人信息识别指南》发布**

9月18日，全国网络安全标准化技术委员会秘书处组织编制了《网络安全标准实践指南——敏感个人信息识别指南》。该文件给出了敏感个人信息识别规则以及常见敏感个人信息类别和示例，可用于指导各组织识别敏感个人信息，也可为敏感个人信息处理和保护工作提供参考。

原文链接：

https://www.tc260.org.cn/upload/2024-09-18/1726621097544005928.pdf

**2.美国CISA发布《联邦民事行政部门运营网络安全协调计划》**

9月16日，美国网络安全与基础设施安全局（CISA）发布《联邦民事行政部门（FCEB）运营网络安全协调计划》，以指导对各FCEB的协调支持和服务，推动优先事项有效开展，协调集体运营防御能力。该计划包括五个优先事项，资产管理、漏洞管理、可防御架构、网络供应链风险管理、事件检测与响应。该计划并非一份全面清单，而是旨在将资源集中在可实质推动运营网络安全改进和协调目标的行动上。CISA表示，通过与各FCEB合作共同推进计划，将实现美国联邦机构网络安全现代化。

原文链接：

https://www.cisa.gov/sites/default/files/2024-09/FY2024%20FOCALPlanPublicVersion%20TLP%20Clear%20508.pdf

**往期精彩推荐**

[【已复现】Ivanti Endpoint Manager反序列化漏洞(CVE-2024-29847)安全风险通告第二次更新](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502180&idx=1&sn=162866a32a0466de02a7e97212e45005&chksm=fe79edfcc90e64eabf7c347da74ba93f7855ace35b296f6ca338f9ed0ce3b3a1a9701c15a1e9&token=160916285&lang=zh_CN&scene=21#wechat_redirect)
[GitLab SAML 认证绕过漏洞(QVD-2024-40180)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502168&idx=1&sn=218d2b0e656b39a5e0ba5453cb151804&chksm=fe79edc0c90e64d60068b582d417b2f2df79b628fed0b9f6868a071dc3c2b6fd6480d3d17ed5&token=160916285&lang=zh_CN&scene=21#wechat_redirect)

[【在野利用】Ivanti Cloud Service Appliance 命令注入漏洞(CVE-2024-8190)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502168&idx=2&sn=5331760540fabf360fd05ab9f060c51d&chksm=fe79edc0c90e64d64b3af5b90275bf2792a703588343e49cddfcce7b2981be18577010f48589&token=160916285&lang=zh_CN&scene=21#wechat_redirect)

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