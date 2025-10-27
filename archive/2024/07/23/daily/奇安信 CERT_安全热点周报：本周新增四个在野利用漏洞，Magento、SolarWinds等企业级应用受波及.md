---
title: 安全热点周报：本周新增四个在野利用漏洞，Magento、SolarWinds等企业级应用受波及
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501769&idx=1&sn=2edeb62bd20fc5bd84da63caa890e03e&chksm=fe79e351c90e6a4753944bb594a30e2b7bf1dddd44e2f6071ae200c622e71290e1d1d89607eb&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-23
fetch_date: 2025-10-06T17:43:23.319087
---

# 安全热点周报：本周新增四个在野利用漏洞，Magento、SolarWinds等企业级应用受波及

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48DY4j1CRItIqWibMmzgicnS7HiaVyHl1oglSG0YDDWvrAXaE76NfmZRWBmlVAFkBwhMVoeolGXOmS3g/0?wx_fmt=jpeg)

# 安全热点周报：本周新增四个在野利用漏洞，Magento、SolarWinds等企业级应用受波及

奇安信 CERT

| **安全资讯导视** |
| --- |
| • Crowdstrike更新导致全球近千万台Windows蓝屏死机 |
| • 重大事故！美国电信巨头AT&T几乎所有用户的电话记录泄露 |
| • 北约发布新版《人工智能战略》概要 |

**PART****0****1**

**漏洞情报**

**1.JumpServer多个高危后台漏洞安全风险通告**

7月19日，奇安信CERT监测到官方修复JumpServer后台文件写入漏洞(CVE-2024-40629)和JumpServer后台文件读取漏洞(CVE-2024-40628)。攻击者可以利用Ansible脚本读取或写入任意文件，从而导致Celery敏感信息泄露和远程代码执行。奇安信鹰图资产测绘平台数据显示，该批漏洞关联的国内风险资产总数为124880个，关联IP总数为22031个。目前该漏洞技术细节与PoC已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**2.Nacos Derby远程命令执行漏洞安全风险通告**

7月19日，奇安信CERT监测到官方修复Nacos Derby远程命令执行漏洞(QVD-2024-26473)，由于Alibaba Nacos部分版本中derby数据库默认可以未授权访问，恶意攻击者利用此漏洞可以未授权执行SQL语句，最终导致任意代码执行。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为40575个，关联IP总数为8171个。目前该漏洞PoC已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**3.泛微e-cology9 WorkflowServiceXml SQL注入漏洞安全风险通告**

7月15日，奇安信CERT监测到泛微e-cology9 WorkflowServiceXml SQL注入漏洞(QVD-2024-26136)在野利用行为，在默认配置下，未授权攻击者可利用该漏洞执行任意SQL语句，从而造成任意命令执行。奇安信鹰图资产测绘平台数据显示，该漏洞关联的国内风险资产总数为51855个，关联IP总数为8761个。目前该漏洞PoC已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**PART****0****2**

**新增在野利用**

**1.****Magento Open Source XML外部实体注入漏洞(CVE-2024-34102)**

7月 17 日，美国网络安全和基础设施安全局 (CISA) 在其已知利用漏洞 (KEV) 目录中添加Magento Open Source XML外部实体注入漏洞(CVE-2024-34102)，Adobe Commerce 和 Magento Open Source 的受影响版本存在 XML 外部实体引用的不当限制漏洞，这可能导致任意代码执行。攻击者可以通过发送一个引用外部实体的精心构造的XML文档来利用这个漏洞，造成敏感信息泄露或远程代码执行。

影响 Adobe Commerce 和 Magento 网站的“CosmicSting”漏洞在安全更新发布九天后仍未得到修补，导致数百万个网站面临灾难性攻击。根据 Sansec 的统计，使用受影响电子商务平台的网站中大约四分之三尚未修补 CosmicSting，这使它们面临 XML 外部实体注入 (XXE) 和远程代码执行 (RCE) 的风险。

Sansec 表示：“CosmicSting（又名 CVE-2024-34102）是两年来 Magento 和 Adobe Commerce 遭遇的最严重的漏洞” 。

Sansec 表示，尽管 Adobe 在其公告中省略了技术细节以避免引发主动攻击，但可以从补丁代码中轻松推断出有效的攻击方法，其分析师使用该补丁代码重现了此次攻击。

供应商发布了针对CVE-2024-34102的修复程序，建议电商平台管理员尽快应用最新版本。

参考链接：

https://www.bleepingcomputer.com/news/security/cosmicsting-flaw-impacts-75-percent-of-adobe-commerce-magento-sites/

**2.SolarWinds Serv-U 目录遍历漏洞(CVE-2024-28995)**

7月 17 日，美国网络安全和基础设施安全局 (CISA) 在其已知利用漏洞 (KEV) 目录中添加SolarWinds Serv-U 目录遍历漏洞(CVE-2024-28995)，SolarWinds Serv-U 容易受到目录横向漏洞的影响，未经身份认证的远程攻击者通过构造特殊的请求可以下载读取远程目标系统上的任意文件，对机密性造成很高的影响。

威胁行为者目前正在利用 SolarWinds Serv-U 中的关键路径遍历漏洞CVE-2024-28995。攻击者利用公开的概念验证 (PoC) 漏洞，利用此漏洞获得未经授权的访问权限，从而无需身份验证即可读取目标服务器上的敏感文件。这些不断增加的攻击对全球用户构成了重大而直接的威胁。

GreyNoise Intelligence 部署了一个高级蜜罐来收集漏洞利用尝试的数据。蜜罐与易受攻击的 Serv-U 应用程序非常相似，并像真正的系统一样做出响应。几天之内，GreyNoise 捕获了几次漏洞利用尝试，包括动手操作键盘的活动。GreyNoise 的蜜罐揭示了各种针对关键文件（如 /etc/passwd 和 Serv-U 启动日志）的有效载荷。数据显示，其中既有常用的有效载荷，也有自定义的有效载荷，表明攻击者的复杂程度各不相同。

SolarWinds 建议所有用户更新到 Serv-U 15.4.2 HF 2 或更高版本以缓解漏洞。

参考链接：

https://www.labs.greynoise.io/grimoire/2024-06-solarwinds-serv-u/

**3.****VMware vCenter Server信息泄露漏洞(CVE-2022-22948)**

7月 17 日，美国网络安全和基础设施安全局 (CISA) 在其已知利用漏洞 (KEV) 目录中添加VMware vCenter Server信息泄露漏洞(CVE-2022-22948)，VMware vCenter Server 存在信息泄露漏洞，具有非管理访问权限的攻击者可利用该漏洞来获取对敏感信息的访问权限。

2022 年 9 月，在 ESXi 虚拟机管理程序中发现恶意软件后，Mandiant 开始调查 UNC3886 发起的多次入侵活动。UNC3886 是一个网络间谍组织，其目标是全球范围内的知名战略组织。

2024 年 1 月，Mandiant 发布了一篇博客文章，详细介绍了UNC3886 自 2021 年底以来利用 CVE-2023-34048（VMware vCenter）的活动。该漏洞允许在易受攻击的 vCenter 服务器上执行未经身份验证的远程命令。Mandiant 在易受攻击的 VMware 服务崩溃几分钟后就观察到攻击者后门的部署。CVE-2023-34048 并不是 UNC3886 在这些入侵过程中利用的唯一零日漏洞。VMware vCenter 中的 CVE-2022-22948 被利用来获取 vCenter 的 postgresDB 中的加密凭据，以便进行进一步访问。在利用零日漏洞访问 vCenter 服务器并随后管理 ESXi 服务器后，攻击者获得了与 vCenter 服务器共享同一 ESXi 服务器的客户虚拟机的完全控制权。Mandiant 观察到攻击者在客户虚拟机上使用两个公开可用的 rootkit（REPTILE 和 MEDUSA）来保持访问权限并逃避检测。

组织必须确保其 VMware 系统已修补并保持最新状态，以防止被旧漏洞利用。

参考链接：

https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations

**4.GeoServer远程代码执行漏洞(CVE-2024-36401)**

7 月 15 日，CISA 警告称，GeoServer GeoTools 的一个严重远程代码执行漏洞（CVE-2024-36401）正在被攻击积极利用。

GeoServer 是一个开源服务器，允许用户共享、处理和修改地理空间数据。6 月 30 日，GeoServer 披露了其 GeoTools 插件中存在一个严重的 9.8 级远程代码执行漏洞，该漏洞是由不安全地将属性名称评估为 XPath 表达式引起的。

GeoServer 咨询报告中写道：“GeoServer 调用的 GeoTools 库 API 会以不安全的方式将要素类型的属性名称传递给 commons-jxpath 库，而该库在评估 XPath 表达式时可能会执行任意代码。”此 XPath 评估仅适用于复杂特征类型（即应用程序模式数据存储），但也被错误地应用于简单特征类型，这使得此漏洞适用于所有GeoServer 实例。

虽然 CISA 没有提供任何有关如何利用这些漏洞的信息，但威胁监控服务 Shadowserver 表示，他们观察到 CVE-2024-36401 从 7 月 9 日开始被积极利用。OSINT 搜索引擎ZoomEye 表示，大约有 16,462 台 GeoServer 服务器在线暴露，其中大部分位于美国、中国、罗马尼亚、德国和法国。

尽管该机构的 KEV 目录主要针对联邦机构，但 GeoServer 建议私人组织也应优先修补此漏洞以防止攻击。尚未修补的用户应立即升级到最新版本，并彻底检查其系统和日志是否存在可能的危害。

参考链接：

https://www.bleepingcomputer.com/news/security/cisa-warns-critical-geoserver-geotools-rce-flaw-is-exploited-in-attacks/

**PART****0****3**

**安全事件**

**1.Crowdstrike更新导致全球近千万台Windows蓝屏死机**

综合消息，7月19日中午开始，CrowdStrike问题更新导致全球Windows大面积蓝屏死机，致使航班停飞、火车晚点、银行异常、巴黎奥运服务受影响等，全球至少二十多个国家受到波及。由于事件发生时亚太地区在白天，美欧在夜晚，初期社交媒体上的反馈主要集中在亚太地区，主要是日本、澳大利亚。随着时间的推进，欧美用户也大量出现服务中断反馈。大量的机场、医院、媒体与银行由于系统的崩溃，导致服务中断，数以万计的航班延误取消，有些医院不得不转移病人，很多受影响企业的不得不提前放假。CrowdStrike于当天下午发布相关通知承认了这一问题，并承诺将在45分钟后修复。微软官方后续表示，估计CrowdStrike的更新影响了850万台Windows设备，占所有Windows设备不到1％。奇安信表示，基于其数据视野估计国内的CrowdStrike软件装机量在万级，相关单位数在百级，用户主要集中在北上广深等发达地区。受影响的主要是外企、外企在华分支机构及合资企业，大量这类机构中招，有反馈某个在华外企大量终端中的40%崩溃。

原文链接：

https://www.secrss.com/specials/01085b1f4d1b076f

**2.美国家具巨头遭勒索攻击：工厂被迫关闭 业务受到严重影响**

7月17日The Record消息，美国最大的家具公司之一巴西特家具（Bassett Furniture）表示，本月10日遭遇勒索软件攻击后被迫关闭部分IT系统，导致制造设施停运多天。该公司在15日公布的SEC文件中写道，黑客“通过加密某些数据文件扰乱了公司的业务运营”，迫使公司启动事件响应计划关闭部分系统。“公司的零售店和电子商务平台仍然开放，客户可以下单并购买现有商品。然而，公司目前的订单履行能力受到了影响。”巴西特家具罕见地承认，此次攻击“已经并且可能继续对公司的业务运营产生重大影响。”

原文链接：

https://therecord.media/furniture-giant-manufacturing-shut-down-cyberattack

**3.重大事故！美国电信巨头AT&T几乎所有用户的电话记录泄露**

7月12日TechCrunch消息，美国电话电报公司（AT&T）披露，将向约1.1亿客户通知发生了一起新的数据泄露事件。该公司发言人表示，网络犯罪分子窃取了“几乎所有”客户的电话记录。被盗数据包含从2022年5月1日至2022年10月31日期间移动和固定电话客户的电话号码，以及AT&T网络内的通话和短信记录，例如谁通过电话或短信联系了谁。被盗数据还包括2023年1月2日以后的小部分客户的较新记录，但未具体说明数量。AT&T在4月19日得知该事件，由于事涉重大，美国司法部和FBI两度同意推迟在SEC披露文件中公开事件。

原文链接：

https://techcrunch.com/2024/07/12/att-phone-records-stolen-data-breach/

**PART****0****4**

**政策法规**

**1.美国海军陆战队发布新版《人工智能战略》**

7月10日，美国海军陆战队发布《人工智能战略》，将指导其整合人工智能技术工作。该战略提出改善海军陆战队态势的五个关键目标，包括全面了解可由人工智能提供解决方案的特定任务问题；提高部队各级人员在建立、支持和维护人工智能系统及相关技术方面的专业技能；改善基础设施并制定和发布标准；建立人工智能政策、管理和沟通渠道；加强与国防部其他部门、国际盟友、工业界和学术界合作等。该文件是海军陆战队推进数字现代化的重要里程碑。

原文链接：

https://www.marines.mil/Portals/1/Publications/USMC%20AI%20STRATEGY%20(SECURED).pdf

**2.北约发布新版《人工智能战略》概要**

7月10日，北约发布了新版《人工智能战略》概要，旨在以安全和负责任的方式推进在北约内部采用人工智能技术。新版战略以2021年版本为基础，纳入了人工智能技术的最新进展，如生成式人工智能和人工智能赋能的信息工具。该战略确定了几个优先事项，包括推进北约负责任使用原则的实施；提高整个联盟中人工智能系统之间的互操作性；将人工智能与其他新兴颠覆性技术相结合；通过与盟国工业和学术界、北约国防创新加速器、北约创新基金和合作伙伴开展更密切的合作，扩大北约的人工智能生态系统。此外，该战略首次将人工智能赋能的虚假信息、信息战等确定为联盟关注的问题。在新版人工智能战略的指导下，北约将通过增加战略远见和分析工作来阻止对手使用人工智能。

原文链接：

https://www.nato.int/cps/en/natohq/official\_texts\_227237.htm

**往期精彩推荐**

[CrowdStrike导致全球IT基础设施中断事件分析报告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501763&idx=1&sn=3714d555ecf347d22ba237fc80c5131a&chksm=fe79e35bc90e6a4d32699034dcf6c752d63eb31305f62c9a2ff63f852f69c24b89743c314aca&token=46374034&lang=zh_CN&scene=21#wechat_redirect)
[【已复现】Nacos Derby 远程命令执行漏洞(QVD-2024-26473)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501756&idx=1&sn=d2a6bccad06819cf70176bc02a7ee944&chksm=fe79e324c90e6a32139fd6113ec70cea92a332ab1c089e0b8e3b4676c71774730911e98195de&token=46374034&lang=zh_CN&scene=21#wechat_redirect)

[【已复现】JumpServer 多个高危后台漏洞安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501756&idx=2&sn=df4016bd9cdbf9046656891f477b8bbe&chksm=fe79e324c90e6a32eb519c03daf43b2a21637c818171618482583076f652528551b0d4fbb9fc&token=46374034&lang=zh_CN&scene=21#wechat_redirect)

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