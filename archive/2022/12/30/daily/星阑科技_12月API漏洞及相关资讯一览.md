---
title: 12月API漏洞及相关资讯一览
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496812&idx=1&sn=a471fd83df5ea6c4d53cc2e86c2cdff4&chksm=c00759f0f770d0e64fc60f3c677050aa7c623003aff223bb6b57abf9f48aef23082347ffb2bc&scene=58&subscene=0#rd
source: 星阑科技
date: 2022-12-30
fetch_date: 2025-10-04T02:45:06.423584
---

# 12月API漏洞及相关资讯一览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaAsVLaXJMSiaJcEZ32msfoIibAxWe1G3DcFpGTL7SebIGBjUaAympjQA3pFo2sj7B26PW70zicW8aag/0?wx_fmt=jpeg)

# 12月API漏洞及相关资讯一览

星阑科技

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif)

为了让大家的API更加安全

致力于守护数字世界每一次网络调用

小阑公司 PortalLab实验室的同事们

给大家整理了

12月份的一些API安全漏洞报告和资讯

希望大家查漏补缺

及时修复自己API可能出现的漏洞

***No.1***

**Zendesk Explore API中的SQL注入漏洞**

**漏洞详情：**Zendesk Explore 是一款报告和分析解决方案，可使组织机构“查看并分析关于客户的关键信息以及支持资源”。Varonis Threat Labs报告了流行的Zendesk票务和支持系统中的两个漏洞，这些漏洞影响着Zendesk Explore安全性。

**漏洞危害：**第一个是SQL注入漏洞，它允许攻击者向底层数据库注入任意命令。第二个涉及API端点中的漏洞，该漏洞提供了执行查询功能来修改平台文档。由于实现中的弱点，研究人员发现API端点没有验证API调用者有权访问指定的数据记录，并且可以修改查询以从其他数据库表中提取任意数据。

**影响范围：**该漏洞和 GraphQL API 中的一个SQL 注入有关，可被攻击者以管理员用户身份提取数据库中的所有信息，包括邮件地址、工单以及和实时代理的会话。

**小阑修复建议**

SQL注入的检测方式目前主要有两大类，第一：动态监测，即在系统运行时，通常在系统验收阶段或上线运行阶段使用该方法，使用动态监测攻击对其系统进行扫描，然后依据扫描结果判断是否存在SQL注入漏洞。第二：静态检测，又称静态代码扫描，对代码做深层次分析。

开发过程中避免 SQL 注入的一些方法：

* **避免使用动态SQL：**避免将用户的输入数据直接放入 SQL 语句中，最好使用准备好的语句和参数化查询，这样更安全。
* **不要将敏感数据保留在纯文本中：**加密存储在数据库中的私有/机密数据，这样可以提供了另一级保护，以防攻击者成功地排除敏感数据。
* **限制数据库权限和特权：**将数据库用户的功能设置为最低要求；这将限制攻击者在设法获取访问权限时可以执行的操作。
* **避免直接向用户显示数据库错误：**攻击者可以使用这些错误消息来获取有关数据库的信息。

***No.2***

**Twitter API漏洞泄露了540万用户数据**

**漏洞详情：**超过540万条推特用户的数据在黑客论坛上免费共享，该数据与此前8月份黑客出售的数据相同，包含5485635条推特用户的数据。这些数据包含私人的电子邮件地址和电话号码，以及推特ID、名称、验证状态等多个公开的信息。这些数据是攻击者利用推特API漏洞进行收集的。

**漏洞危害：**可能导致数百万的Twitter用户将有可能面临潜在的网络钓鱼攻击。

**影响范围：**这次漏洞中带来的最重要的威胁是社会工程。网络犯罪分子可能会利用从这次漏洞中获取的姓名和地址，以用户为目标，进行电子邮件钓鱼、语音钓鱼和网络钓鱼诈骗，试图诱使用户交出个人信息和登录凭证。

**小阑修复建议**

这些骗局会针对终端用户，但安全团队可以及时更新修改Bug，以确保用户了解遭受了什么威胁以及如何应对这些威胁。安全团队还需要提醒员工们，在个人账户上激活双因素认证是一个好办法，可以减少未经授权登录的可能性。

***No.3***

**LEGO Marketplace曝API漏洞，可进行账号接管攻击**

**漏洞详情：**日前，Salt Labs进行的一项调查中发现，在LEGO® Group旗下的乐高转售平台中出现应用程序编程接口 (API) 安全漏洞，这可能会使敏感的客户信息面临风险。报告指出，BrickLink中存在两个API安全漏洞，BrickLink是一个买卖乐高零件、人仔和套装的在线市场，拥有超过一百万的会员。

**漏洞危害：**研究人员表示，这些漏洞可能使威胁行为者能够对客户账户进行大规模账户接管 (ATO) 攻击，访问平台存储的个人身份信息 (PII) 用户数据，并获得对内部生产数据的访问权限，从而可能导致完全妥协 BrickLink 的内部服务器。

**影响范围：**该漏洞会让系统的每个用户都处于危险之中，攻击者可以访问用户存储的所有信息，包括个人信息数据和信用卡详细信息。

**小阑修复建议**

身份验证缺陷是API不安全的主要原因之一。当API暴露给公众调用时，为了保障用户的可信性，必须对调用用户进行身份认证。因设计缺陷导致对用户身份的鉴别和保护机制不全而被攻击。需要确保使用标准模式和组件，以及使用一致的身份验证处理程序来实现，并加强保护机制审查和代码规范。

***No.4***

**Web应用程序和API在金融服务领域攻击激增257%**

**内容详情：**日前，Akamai披露称，在过去12个月里，金融服务行业检测到的web应用程序和API攻击数量同比激增3.5倍。并称，针对WEB应用程序和API的威胁增加，反映出金融机构对数字服务的投资增加，这是欧洲PSD2等开放银行授权的结果。虽然这些技术有助于向第三方提供商开放银行服务，为客户创造更精简的体验，但它们也扩大了企业的攻击面。此外，还发现bot活动（81%）和DDoS攻击（22%）同比大幅增加，同时针对客户的网络钓鱼攻击也出现激增。

**攻击危害：**报告的叙述了造成这一趋势的两个主要原因：首先，攻击表面越来越快，为攻击者提供了更多机会；其次，组织缺乏保护其资产的必要技能。报告指出，API攻击的自动化程度是导致基于API的攻击增加的主要因素。

**影响范围：**针对网络应用程序和API的威胁增加，反映出金融机构对数字服务的投资增加。这些技术有助于向第三方提供商开放银行服务，为客户创造更精简的体验，但它们也扩大了企业的攻击面。银行是第三大受网络应用和API攻击的垂直领域，占总攻击数的15%。一旦攻击者成功发起网络应用攻击，他们就可以窃取机密数据，在更严重的情况下，他们还可以获得对网络的初始访问权，并获得更多的证书，从而允许他们横向移动。除了入侵的影响外，窃取的信息还可能在地下兜售或用于其他攻击。考虑到金融垂直服务所持有的大量数据，如个人身份信息和账户详细信息，这非常令人担忧。

**报告指出：**

* 澳大利亚、日本和印度是该区域遭受 Web 应用程序和 API 攻击最多的国家。
* 24 小时内，利用新发现的零日漏洞针对金融服务业发起的攻击可能高达每小时数千次并且迅速达到高峰，让人几乎没有时间去修补并做出反应。
* 本地文件包含 (LFI) 和跨站点脚本 (XSS) 攻击大幅增加，表明攻击者正转向远程代码执行尝试，对内部网络安全带来更大压力。
* 针对金融服务业客户的网络钓鱼活动正在采取一些可绕过双重身份验证解决方案的技术，给日常客户造成了更高的风险。
* 40% 以上的攻击属于客户帐户接管尝试类型，另外 40% 专注于网站内容抓取，后者用于创建更容易让人相信的网络钓鱼诈骗。

**小阑建议**

金融行业是DDoS攻击最趋之若鹜的目标，并且受到网络钓鱼攻击活动的持续关注，而他们的客户会首当其冲地受到网络钓鱼攻击的重创。攻击者总会设法渗透金融服务业的网络或影响其客户。在了解攻击面之后，企业能够得出对关键风险的见解，进而制定多样化的安全控制措施和缓解计划，更好地保护客户。

***No.5***

**Google Cloud：云计算引爆API安全危机**

**内容详情：**根据Google Cloud的一项调查，企业最头疼的API安全问题是安全配置错误（占比40%），其次是过时的API和组件以及垃圾邮件和滥用机器人（三分之一）。根据对500多名技术领导者的调查，三分之二的受访企业（67%）在测试阶段发现了与API相关的安全问题和漏洞，但大多数企业（超过60%）在软件开发、应用程序部署以及实时监控过程中发现了API安全问题。

**攻击危害：**API是企业数字化转型的关键，但谷歌的两项调查发现，数字化转型（上云）同时也导致针对API的网络攻击和API自身的攻击面正在达到一个临界点。API（Web应用程序编程接口）是将云应用程序和基础架构结合在一起的粘合剂，但这些端点越来越多地受到攻击，50%的受访企业承认在过去12个月中发生了与API相关的安全事件。企业对API安全的信心与调查揭示的事实不符，企业安全格局已经发生了重大变化——随着API数量的急剧增长，API已经成为应用安全的新战场。

**影响范围：**谷歌的调查发现，46%的受访企业只在企业内使用API，但超过一半（54%）的企业允许合作伙伴、客户和其他外部开发人员使用其API，作为刺激第三方开发的一种方式。过去两年由于新冠病毒大流行导致业务中断，加速了企业数字化转型，企业对Web API的重视与日俱增。在另外一项调查中，受访的770名技术领导者的绝大多数（93%）都表示其运营“主要依托云”，高于两年前的83%。据估计，自2020年以来，与API相关的安全事件造成了120-230亿美元的损失。而且企业的攻击面正在不断扩大：如今大企业的平均API数量是一年前的三倍，高达15,600个。

**小阑认为**

API安全成熟度高的企业在向云原生运营的过渡取得了更大的成功。Google Cloud给低成熟度企业的定义是：拥有孤立API，也许还有API安全网关，但没有集中管理API安全的企业。

研究表明，与低成熟度的企业相比，API安全成熟度高的企业在数字化转型方面遥遥领先。显然，技术领导者已经意识到了API带来的价值。根据谷歌的报告，对于转向基于API的应用程序基础设施的企业来说，API安全被认为是API计划中最重要的组成部分，66%的受访企业认为它很重要。其他企业最关心的问题还包括API性能分析和API治理。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaAsVLaXJMSiaJcEZ32msfoIF6HmW7ZpGIbL68AjEq3PVGsAEWnANwZsD2LlQHS5rCZnDMxN290PAQ/640?wx_fmt=png)

星阑科技“萤火”API安全分析平台可以支持多种API漏洞的检测。有相关需求的可以在公众号进行留言，或添加“小阑本阑”客服微信进行咨询。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaAsVLaXJMSiaJcEZ32msfoIk7XDMOUEUmSooEmRqe5OibteDko9rYhCfecWwu98MOj4JXdYCf7a0ow/640?wx_fmt=jpeg)

（长按或扫描图中二维码即可添加）

**关于Portal Lab 实验室**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOeiaAsVLaXJMSiaJcEZ32msfoI1uVribMia2VIVAOcG0PBE9oGUHzsUP03z526lk7q3VMrpt7aozvbwfIA/640?wx_fmt=png)

星阑科技 Portal Lab 致力于前沿安全技术研究及能力工具化。主要研究方向为API 安全、应用安全、攻防对抗等领域。实验室成员研究成果曾发表于BlackHat、HITB、BlueHat、KCon、XCon等国内外知名安全会议，并多次发布开源安全工具。未来，Portal Lab将继续以开放创新的态度积极投入各类安全技术研究，持续为安全社区及企业级客户提供高质量技术输出。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeiaAsVLaXJMSiaJcEZ32msfoIwNNE548ibYtCia6OZVJKlGRQ1xtuXeSoPEslgFjUhPPlyibkqn9g5ZxvQ/640?wx_fmt=jpeg)

**关注“星阑实验室”公众号**

**了解更多关于API安全的技术知识**

**往期 · 推荐**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxP3pibVtoiaCUZGthg56a6z1z2iaMtbvQxDhslcNy0m8SDnJXKC6oEfq0zg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496481&idx=1&sn=34b4f474a19214348695f8cee0ab4541&chksm=c0075ebdf770d7ab73cc7c37967acf1b872f79a3b89cea3e833cfab23695457edc5f114142d4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxP1Cux4Jq5JmBsTgpMZa5VIVkPGf3icyJU8RKTibyicceQXU8SeZia1ZJAQQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496462&idx=1&sn=29d5714db225ce0b4e696d5dab8761db&chksm=c0075e92f770d78488e96475b830f59093b7b57194412b077c3dbdbc3a88b6e3893290db6ddf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxPauwnqJkiaibLzRyEiaXRIUV2CkJYDfET6dtXYGGhEJ1NKojuSOcvBRItQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496376&idx=1&sn=d450da5b2728e9bdad4e0eda8c6666db&chksm=c0075f24f770d6329bc57fbc5c7f3c6af22651f548d5ed4ded7e1b4e2e0129976abe05acf5d4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxPH6Sl8FGnoPGEObDiaibLTSLhMvDCr05R4h4rePNNAUolWlnBJL0AMf0Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496333&idx=1&sn=ad3e2bf315a250313eb12bc9c41332d0&chksm=c0075f11f770d60788921156547538ab7b6113d616e01e8c08e30dbc589dae7d7cafb1cedcd9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOehwcHoxicoOah5mxDjLHMZ9RHUxNeibERphRXOj3AEupxt7JyOt3LF1RmmWQibYmicTv2DxM93iaEJhLxw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

星阑科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

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