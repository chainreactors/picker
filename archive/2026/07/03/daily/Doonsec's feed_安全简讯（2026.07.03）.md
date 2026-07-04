---
title: 安全简讯（2026.07.03）
url: https://mp.weixin.qq.com/s/tSCy51rmIA8-EF6YkUBOng
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:42:36.104770
---

# 安全简讯（2026.07.03）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309Zrw9yJRibdg61icu3LCrMls9MWIISB5D8dghWurzkh2zhJUxuyEicFyWHWqYRNdCpxKg33ITnuh5GWYLP2aGgxQf0brQlibuqUygL54/0?wx_fmt=jpeg)

# 安全简讯（2026.07.03）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. 恶意PyPI包伪装PoC依赖，定向攻击研究员**

7月1日，网络安全领域再曝针对性攻击活动，多个托管于GitHub的概念验证（PoC）漏洞利用程序被植入后门，最终会向受害者系统投递一款名为ChocoPoC的Python远程访问木马（RAT）。该木马具备命令执行与敏感数据窃取能力，攻击矛头直指网络安全研究人员、渗透测试人员及低技能黑客群体。虽然将恶意代码伪装进PoC漏洞利用文件并非新鲜手段，但本次攻击的独特之处在于：恶意载荷并未直接嵌入漏洞脚本，而是被巧妙隐藏在PoC项目的依赖项列表中，通过Python包索引（PyPI）平台进行分发，从而使得漏洞利用代码本身保持“干净”以规避静态检测。网络安全公司Sekoia已在GitHub上识别出至少七个分发ChocoPoC的PoC仓库，分别针对FortiWeb、React2Shell、MongoBleed、PAN-OS、Ivanti Sentry、Check Point VPN及Joomla SP Page Builder等热门高危漏洞，其中“skytext”包在Linux系统上累计下载约2400次，且在某一高危漏洞披露后下载量急剧攀升，显示攻击者利用研究人员急于验证新漏洞的心理进行精准诱捕。

https://www.bleepingcomputer.com/news/security/new-chocopoc-malware-targets-researchers-via-trojanized-poc-exploits/

**2. HSIN服务器遭攻击，DHS启动紧急调查**

7月1日，美国国土安全部（DHS）近日证实，其用于联邦、州、地方及私营部门合作伙伴间共享敏感信息的核心平台国土安全信息网络（HSIN）遭受了一起网络入侵事件。据Nextgov报道，此次攻击由一名身份不明的威胁行为者于今年5月下旬至6月初期间实施，DHS已启动调查，但尚未将攻击归咎于任何特定行为者或外国政府，系统中是否有文件被盗亦不明确。知情人士透露，攻击者主要针对HSIN服务器及其配套的SharePoint协作系统，DHS情报与分析办公室已对漏洞开展损失评估。此次事件引发外界高度关注，因为美国目前正负责监督在全国多地举办的世界杯比赛安全事务，Nextgov担忧该漏洞可能暴露安全计划、机构间协调及应急响应程序等敏感内容。DHS发言人在声明中确认了此事件，同时强调机密系统未受影响。DHS在发现攻击后立即隔离受影响的系统、缓解漏洞并启动全面取证调查，目前尚无迹象表明机密网络受损，HSIN对合作伙伴仍保持可用，但因调查仍在进行中，暂无法披露更多操作细节。

https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/

**3. 欧洲防务巨头Indra遭Gentlemen勒索软件攻击**

7月1日，欧洲最大的国防承包商之一、西班牙跨国公司Indra集团近期成为勒索软件组织Gentlemen的攻击目标。该团伙于6月30日在暗网泄密网站发布公告，给予Indra集团9天时间进行沟通，否则将公开据称被盗的数据。这是勒索软件团伙施压受害者支付赎金的常见手段。截至目前，尚不清楚此次疑似泄露涉及何种类型的数据。Indra集团已证实其一家子公司遭受勒索软件攻击，但强调公司已立即启动计算机安全事件响应团队，对可能被入侵的环境进行分析、验证和安全审查，并评估攻击仅限于局部区域，已排除集团旗下其他子公司受波及的风险。公司表示调查仍在进行中，安全程序和控制措施的审计同步推进。此次针对Indra的攻击不仅威胁到企业自身的数据安全，更因其北约承包商身份和关键国防业务性质，引发对欧洲防务供应链安全及国家敏感信息泄露的广泛担忧。目前事件仍在调查中，Indra能否在倒计时结束前化解危机、数据是否已被外泄，均有待进一步观察。

https://cybernews.com/security/indra-group-ransomware-attack-data-leak/

**4. Alta Montclair云存储泄露21万份文件**

7月1日，美国加利福尼亚州退休计划管理公司Alta Montclair近日曝出重大数据泄露事件：一个配置错误的亚马逊网络服务（AWS）云存储桶被公开置于互联网上，导致大量客户敏感信息暴露。据调查团队估计，该存储桶包含多达219,000份文件，涉及该公司管理的多个退休计划及金融服务提供商的相关文档，受影响的机构包括龙金融服务、PDL金融服务、退休教育伙伴（REP）及SPARK研究所等。泄露的数据涵盖极为广泛的个人与财务信息，包括全名、出生日期、社会安全号码、家庭住址、联系信息、现任及前任雇主详情、退休计划文件、财务记录、法律文件（含遗嘱），部分记录甚至包含完整的信用卡信息。更令人担忧的是，存储桶中还泄露了SPARK Institute相关的公钥和私钥PGP密钥对，这可能破坏加密通信和文件传输的机密性。此外，佣金跟踪日志、客户文档模板、用户手册、内部服务文档、传真记录（含跟踪号码、收件人信息、员工电子邮件及电话号码）以及网站资源文件等内部业务资料也一并暴露。文件时间跨度从2014年公司成立至今，但存储桶公开访问的具体时长尚不明确。

https://cybernews.com/security/alta-montclair-retirement-data-leak/

**5. ShinyHunters入侵美敦力致数据泄露**

7月2日，全球医疗器械巨头美敦力（Medtronic）近日向受影响客户发出通知，确认其部分企业IT系统于今年4月遭到黑客攻击，导致客户个人数据被未经授权的第三方获取。此次攻击由知名数据勒索组织ShinyHunters声称负责，该组织宣称掌握了美敦力约900万条包含个人身份信息及内部公司数据的记录。根据美敦力披露的调查结果，异常活动发生于2026年4月13日至19日期间，公司在4月15日察觉后立即联合第三方网络安全专家展开调查，以确定事件的影响范围。泄露的数据类型可能包括客户姓名、联系信息、出生日期、社会安全号码及健康相关信息等高度敏感的个人资料。ShinyHunters组织惯常在赎金谈判失败后公布被盗数据，该组织于4月18日将美敦力列入暗网勒索门户网站，并威胁若在4月21日前未收到赎金便将公开据称超过900万条记录。然而，当月晚些时候美敦力的条目从该组织的受害者列表中悄然删除。美敦力在向客户发出的通知中强调，被盗数据并未在实际网络中被公开泄露，但仍敦促受影响者保持警惕，并为受影响客户提供为期24个月的信用监控和身份盗窃保护服务。

https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/

**6. 思科Unified CM高危漏洞遭在野利用**

7月2日，思科公司近日证实，攻击者正积极利用其统一通信管理器（Unified CM）产品中的一个高危漏洞（CVE-2026-20230），该漏洞已于6月初获得修复。Unified CM作为思科IP电话系统的核心控制平台，承担着呼叫路由、设备管理与电话功能调度等关键任务。此漏洞允许未经授权的远程攻击者通过构造特定的HTTP请求，以较低复杂度发起服务器端请求伪造（SSRF）攻击，从而威胁系统安全。思科于6月3日发布安全补丁时曾表示，其产品安全事件响应团队已注意到该漏洞的概念验证利用代码在公开渠道流传，但当时并未发现实际攻击案例。然而，事态在随后数周迅速升级：6月22日，威胁情报公司Defused披露攻击者已开始利用该漏洞，通过精心构造的file://协议有效载荷在目标设备上创建恶意文件；次日，SSD Secure发布详细技术文章并公开了概念验证利用程序，进一步加剧了风险。直到本周三，思科最终确认该漏洞已遭在野积极利用，并在安全公告更新中敦促客户立即采取防护措施。

https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/

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