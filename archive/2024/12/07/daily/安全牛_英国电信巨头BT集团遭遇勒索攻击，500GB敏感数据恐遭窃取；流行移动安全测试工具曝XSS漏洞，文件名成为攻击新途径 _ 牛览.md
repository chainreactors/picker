---
title: 英国电信巨头BT集团遭遇勒索攻击，500GB敏感数据恐遭窃取；流行移动安全测试工具曝XSS漏洞，文件名成为攻击新途径 | 牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651133870&idx=1&sn=bbdb0d6ade319897ba8d80e124901b49&chksm=bd15a77d8a622e6b8a009b9c77717ac002be4c6326296ad17b7e71b54840a5e6c8dea4bdee76&scene=58&subscene=0#rd
source: 安全牛
date: 2024-12-07
fetch_date: 2025-10-06T19:39:23.528348
---

# 英国电信巨头BT集团遭遇勒索攻击，500GB敏感数据恐遭窃取；流行移动安全测试工具曝XSS漏洞，文件名成为攻击新途径 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkDbptuP6rFqQX076b7OVc0Re2YhAOibxaicXMGcwM3oOKNhUia7tSyTNnlQ9v3icIf3F5uOscibQTYMM4w/0?wx_fmt=jpeg)

# 英国电信巨头BT集团遭遇勒索攻击，500GB敏感数据恐遭窃取；流行移动安全测试工具曝XSS漏洞，文件名成为攻击新途径 | 牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•首份欧盟网络安全状况报告发布：DoS和勒索软件成为头号安全隐患

•警惕！错误配置的WAF系统导致企业后端服务器直接暴露

•英国电信巨头BT集团遭遇勒索攻击，500GB敏感数据恐遭窃取

•百年伏特加品牌Stoli因勒索攻击遭重创，美国子公司申请破产保护

•间谍软件威胁升级：Pegasus攻击目标或已面向普通用户群体

•伪装成热门应用诱导安装，77款金融应用遭遇"DroidBot"攻击

•SolarWinds平台爆危险XSS漏洞，可导致代码注入风险

•流行移动安全测试工具曝XSS漏洞，文件名成为攻击新途径

•I-O Data路由器零日安全缺陷遭攻击利用，用户数据面临严重威胁

•Orange  Cyberdefense发布年度安全研究报告：欧洲网络安全面临严峻挑战

•小米手机安全更新有望步入月更时代，与谷歌、三星等国际大厂看齐

**热点观察**

**首份欧盟网络安全状况报告发布：DoS和勒索软件成为头号安全隐患**

欧盟网络安全局（ENISA）于12月3日发布了首份《欧盟网络安全状况报告》，揭示了2023年7月至2024年6月期间欧盟面临的网络安全威胁。报告指出，欧盟实体在此期间面临的网络威胁级别为"实质性"，这意味着欧盟实体可能直接成为威胁行为者的目标，或可能通过最近发现的漏洞遭受攻击。

报告强调，在此期间，网络攻击呈现明显升级趋势，攻击的种类、数量和后果都创下新高。ENISA预警，未来欧盟机构、机构和机关（EUIBA）可能因网络攻击而遭受严重中断，这已成为一种现实可能性。拒绝服务（DoS）和勒索软件攻击是目前最常报告的攻击形式，占观察到事件的一半以上，其次是针对数据的威胁。

报告还指出了几个值得关注的趋势：

1. 黑客行动主义活动增加且变得更加不可预测：
2. 勒索软件仍然是对欧盟成员国影响最大的威胁，呈现出从加密转向数据窃取、针对中小企业、双重勒索成为常态等趋势；
3. 针对欧盟成员国和EUIBA的网络间谍活动持续存在；
4. 黑客雇佣服务的兴起令人担忧。

原文链接：

https://www.infosecurity-magazine.com/news/enisa-launches-first-state-eu/

**警惕！错误配置的WAF系统导致企业后端服务器直接暴露**

近日，安全公司Zafran的研究人员发现，许多依赖内容分发网络（CDN）提供商的Web应用防火墙（WAF）服务的组织，可能因一个常见的配置错误而无意中将其后端服务器暴露在互联网上，面临直接攻击的风险。

研究显示，这个问题影响了近40%使用CDN提供商WAF服务的财富100强公司。其中包括Chase、Visa、Intel、Berkshire Hathaway和UnitedHealth等知名品牌。Zafran发现了属于135家财富1000强公司的2,028个域名中，至少有一个本应受WAF保护的服务器可能被攻击者直接通过互联网访问，从而发起拒绝服务（DoS）攻击、分发勒索软件和执行其他恶意活动。

Zafran首席技术官Ben Seri解释说，问题的根源在于组织没有充分验证发送到托管实际内容、应用程序或数据的后端源服务器的Web请求。在正确配置的CDN集成WAF服务中，所有进入组织Web应用程序的流量都应通过CDN的WAF（位于供应商边缘网络内的反向代理服务器）进行路由。反向代理识别特定Web请求的目标后端服务器或资源，然后以加密方式将其路由到那里。

然而，Zafran发现许多组织没有采用CDN提供商推荐的验证预防措施，如IP过滤机制、预共享数字密钥和相互TLS身份验证。这导致后端服务器可以直接通过互联网访问。Seri将这种情况比作将私有S3存储桶作为公共存储桶向互联网开放。

原文链接：

https://www.darkreading.com/application-security/misconfigured-wafs-heighten-dos-breach-risks

**网络攻击**

**英国电信巨头BT集团遭遇勒索攻击，500GB敏感数据恐遭窃取**

近日，英国电信控股公司BT集团（前身为英国电信）宣布，由于遭受Black Basta勒索软件攻击，该公司已关闭部分服务器。BT集团发言人表示："我们发现了有人试图入侵BT会议平台。这次事件仅限于平台的特定元素，我们迅速将其离线并隔离。"

目前尚不清楚威胁行为者是否从这家电信巨头那里窃取了数据。但目前Black Basta勒索软件团伙已在其Tor泄露网站上将BT集团列入受害者名单。该团伙声称已窃取500GB数据，包括财务数据、组织数据、用户数据和个人文件、保密协议、机密数据等。作为数据泄露的证据，该团伙公布了多张截图，包括护照和其他文件的图片。

今年5月，美国联邦调查局（FBI）、网络安全和基础设施安全局（CISA）、卫生与公众服务部（HHS）和多州信息共享与分析中心（MS-ISAC）发布了一份联合网络安全咨询（CSA），作为"停止勒索软件"计划的一部分，针对Black Basta勒索软件活动发出警告。

原文链接：

https://securityaffairs.com/171668/breaking-news/black-basta-ransomware-attack-bt-group.html

**百年伏特加品牌Stoli因勒索攻击遭重创，美国子公司申请破产保护**

近日，拥有百年品牌历史的伏特加制造商Stoli集团的美国子公司Stoli Group USA和Kentucky Owl申请了第11章破产保护。这一决定是在遭受勒索软件攻击数月后做出的。

Stoli Group USA和Kentucky Owl总裁兼首席执行官Chris Caldwell在11月29日的申请文件中表示，网络攻击是导致公司寻求破产保护的几个因素之一。据报道，2024年8月对Stoli集团的攻击导致美国子公司无法满足贷款方的报告要求，并影响了Stoli集团内所有公司的运营，包括使集团的企业资源规划（ERP）系统瘫痪。自攻击发生以来，大多数内部流程（包括会计功能）都是手动执行的，预计系统要到2025年第一季度才能完全恢复。

Stoli Group USA和Kentucky Owl并非今年第一家因网络攻击申请破产的公司。今年早些时候，数据经纪公司National Public Data和护理院运营商Petersen Health Care也因网络攻击相关原因申请了破产保护。

原文链接：

https://www.scworld.com/news/stoli-group-usa-files-for-bankruptcy-after-ransomware-attack

**间谍软件威胁升级：Pegasus攻击目标或已面向普通用户群体**

近日，安全研究公司iVerify在一项针对3,500部移动设备的威胁扫描中，发现了七起新的Pegasus间谍软件感染案例。这些感染目标包括记者、政府官员和企业高管，涉及iPhone和Android设备，显示出这款臭名昭著的间谍软件的影响范围可能比此前认为的更广。

iVerify的研究人员在12月4日发布的博客文章中披露，他们发现多台设备被以色列NSO集团的间谍软件入侵，攻击始于2021年至2023年间，影响了Apple iPhone iOS 14、15和16.6版本，以及Android系统。研究人员在设备的诊断数据、关机日志和崩溃日志中检测到了取证痕迹。调查发现，每1000次扫描中有2.5台受感染设备，这个比率显著高于任何先前公布的报告。

Pegasus是一种特别恶劣的间谍软件，允许控制者利用操作系统漏洞和零点击攻击来访问和提取被入侵移动设备上的任何内容。攻击者可以在用户不知情或不交互的情况下拦截和传输消息、电子邮件、媒体文件、密码和详细的位置信息。

原文链接：

https://www.darkreading.com/endpoint-security/pegasus-spyware-infections-ios-android-devices

**伪装成热门应用诱导安装，77款金融应用遭遇"DroidBot"攻击**

近日，安全研究公司Cleafy发现了一种名为"DroidBot"的新型Android银行恶意软件，该软件试图窃取英国、意大利、法国、西班牙和葡萄牙等国家超过77个加密货币交易所和银行应用程序的用户凭据。

尽管DroidBot缺乏新颖或复杂的功能，但对其中一个僵尸网络的分析显示，在英国、意大利、法国、土耳其和德国共有776个独特的感染案例，表明其活动规模相当可观。Cleafy还指出，该恶意软件目前正在积极开发中，并有迹象表明正试图扩展到拉丁美洲等新地区。

DroidBot通常伪装成Google Chrome、Google Play商店或"Android Security"等流行应用程序，以诱骗用户安装恶意应用。其主要功能包括键盘记录、覆盖显示、短信拦截和虚拟网络计算（VNC）。该恶意软件滥用Android的无障碍服务来监控用户操作并模拟滑动和点击。

原文链接：

https://www.bleepingcomputer.com/news/security/new-droidbot-android-malware-targets-77-banking-crypto-apps/

**漏洞预警**

**SolarWinds平台爆危险XSS漏洞，可导致代码注入风险**

近日，IT管理软件巨头SolarWinds披露了其Platform产品中存在一个严重的安全漏洞。该漏洞被编号为CVE-2024-45717，允许经过身份验证的攻击者通过跨站脚本（XSS）漏洞注入恶意代码，从而可能危及受影响系统的完整性和机密性。

这个XSS漏洞影响了SolarWinds Platform用户界面的搜索和节点信息部分。尽管漏洞利用需要身份验证和用户交互，但其潜在影响仍然显著。虽然攻击者需要与易受攻击的系统处于同一网段，这在某种程度上限制了潜在攻击的范围，但对于共享网络环境的组织来说，其严重性并未减弱。

如果成功利用，这个XSS漏洞可能允许攻击者：窃取经过身份验证用户的敏感信息；操纵平台功能；潜在获得对连接系统的未授权访问。

原文链接：

https://cybersecuritynews.com/solarwinds-platform-xss-vulnerability/

**流行移动安全测试工具曝XSS漏洞，文件名成为攻击新途径**

近日，广受欢迎的移动安全框架（Mobile Security Framework，简称MobSF）被发现存在一个严重的安全漏洞（CVE-2024-53999），可能使用户面临重大风险。该漏洞允许攻击者通过存储型跨站脚本（XSS）攻击在应用程序的"Diff或Compare"功能中执行恶意脚本。

该漏洞源于MobSF的文件上传机制未能正确清理包含特殊字符（如<、>、/和"）的文件名。这一疏忽使恶意行为者能够上传带有注入脚本的文件名，这些文件随后会被存储在服务器上，并在其他用户访问"Diff或Compare"功能时被执行。

安全研究人员通过使用拦截代理工具上传一个名为"test.zip"的zip文件演示了这个漏洞。当其他用户尝试使用"Diff或Compare"功能比较这个文件时，嵌入的JavaScript代码就会在他们的网络浏览器中执行。尽管目前没有证据表明该漏洞存在公开的概念验证漏洞利用或活跃的在野利用情况，但滥用的潜在可能性仍然很大。

原文链接：

https://cybersecuritynews.com/mobsf-vulnerability/#google\_vignette

**I-O Data路由器零日安全缺陷遭攻击利用，用户数据面临严重威胁**

日本计算机应急响应小组（CERT）近日发出警告，黑客正在利用I-O Data路由器设备中的零日安全缺陷修改设备设置、执行命令，甚至关闭防火墙。这些安全缺陷已经被厂商I-O Data在其官网发布的安全公告中确认，分别涉及信息泄露、远程任意操作系统命令执行，以及禁用防火墙的能力。

具体来说：

* 第一个缺陷属于敏感资源的权限配置错误，允许低权限用户访问关键文件。例如，知道访客账户凭据的第三方可能访问包含身份验证信息的文件；
* 第二个缺陷允许经过身份验证的管理用户在设备上注入和执行任意操作系统命令，这是由于配置管理中的输入验证不足所致；
* 第三个缺陷是固件中的未记录功能或后门，允许远程攻击者在未经身份验证的情况下关闭设备防火墙并修改设置。

这些漏洞影响了UD-LT1混合LTE路由器及其工业级版本UD-LT1/EX。目前最新的固件版本v2.1.9仅修复了第三个安全缺陷，其他两个缺陷的修复将在v2.2.0版本中提供。

原文链接：

https://www.bleepingcomputer.com/news/security/japan-warns-of-io-data-zero-day-router-flaws-exploited-in-attacks/

**产业动态**

**Orange Cyberdefense发布年度安全研究报告：欧洲网络安全面临严峻挑战**

Orange Cyberdefense于12月5日发布了年度安全研究报告《Security Navigator 2025》，揭示了当前复杂的网络安全态势。报告通过广泛的数据分析，详细阐述了在地缘政治冲突和威胁行为者日益复杂的背景下，组织面临的网络安全挑战。

报告指出，一个激进黑客组织自2022年3月以来发起了超过6,600次攻击，其中96%的目标是欧洲国家。攻击者不仅直接制造技术破坏，还试图操控公众舆论、削弱对机构的信任，并企图破坏社会信心。

在运营技术（OT）系统方面，报告显示近四分之一（23%）的复杂攻击与黑客活动有关。46%的OT网络攻击导致了"控制操纵"，公用事业部门受到的影响尤为严重，有46%的攻击与OT系统相关。网络勒索对中小企业的影响正在显著增加，针对小型企业的相关事件同比增长了53%。医疗保健和社会援助部门的攻击同比增长了50%，成为受影响的第四大行业。

此外，人工智能（AI）在网络安全中扮演着双重角色。一方面，AI提高了对高级威胁的检测率，将事件响应时间缩短高达30%。另一方面，生成式AI被用于制作逼真的网络钓鱼内容、假图像和深度伪造视频，推动所谓的"认知攻击"的实施。

原文连接：

https://mp.weixin.qq.com/s/AQ34hIw3BOFdzFiJLBwy8w

**小米手机安全更新有望步入月更时代，与谷歌、三星等国际大厂看齐**

近期，小米全球副总裁谢子阳在社交媒体上针对用户反馈做出了积极回应，透露了小米未来在手机安全更新策略上的重大调整。谢子阳透露，小米计划从2025年起，显著提升其旗下手机的安全更新推送频率，目标是与谷歌、三星等国际大厂看齐，实现月度安全更新。

这一消息的发布源于一位网友在X平台上对小米14手机的评论。该网友对小米14的拍照功能赞不绝口，但同时也指出，与市场上其他旗舰品牌相比，小米14在安全更新的频率上略显不足。面对用户的这一反馈，谢子阳迅速回应，明确表示：“我们计划从2025年开始，为小米手机提供每月的安全更新。”

回顾以往，小米手机的安全更新策略通常遵循每两个月一次的频率，这一安排在一定程度上限制了用户及时获取最新安全补丁的速度。

原文链接：

https://news.zol.com.cn/924/9246437.html

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAibeib6HUSIXJ4IhpazTYic3uwicySgIEk8ZeMC7X5evYXoNPHxoUlibqgo6Ilq0dRkGrMKibWtfcibYwsg/640?wx_fmt=jpeg)

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

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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