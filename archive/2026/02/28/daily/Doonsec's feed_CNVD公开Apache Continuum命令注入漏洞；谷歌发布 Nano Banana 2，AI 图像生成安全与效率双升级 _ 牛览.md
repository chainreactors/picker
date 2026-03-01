---
title: CNVD公开Apache Continuum命令注入漏洞；谷歌发布 Nano Banana 2，AI 图像生成安全与效率双升级 | 牛览
url: https://mp.weixin.qq.com/s/U_FhbFQ9StnqNM93CPyjaQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:23:38.853113
---

# CNVD公开Apache Continuum命令注入漏洞；谷歌发布 Nano Banana 2，AI 图像生成安全与效率双升级 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wKeDC5RjIzEDCBqzGER5lUekuym18J5J3s4Uye1hNG2gDuMl5Z1ZWM0cIMQ9LSPRfod7wBFScGDZ4NW3tkQhEtlT44IcHyvzC1PoBGCTza4/0?wx_fmt=jpeg)

# CNVD公开Apache Continuum命令注入漏洞；谷歌发布 Nano Banana 2，AI 图像生成安全与效率双升级 | 牛览

安全牛

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/wKeDC5RjIzGHRGffrIKl0IgicdMInKwaJ6dyMH3m72SNApkCpjTUHp8oXSjMKMCPEGBJhW5YkUTIN9oZ0pUvAwlUZetbo8BGq9Fn6QPHicM3w/640?wx_fmt=png&from=appmsg)

新闻速览

* 俄罗斯 AI 主权法案落地：强制认证、设备预装、安全审查三重合规
* CNVD 公开Apache Continuum命令注入漏洞
* 209亿美元教训：数据经纪商的"隐形陷阱"如何让消费者成为诈骗猎物
* 非工作时间成重灾区：88% 勒索软件在下班时段加密
* 美军强索 AI 技术遭抵制，Anthropic 坚守监控与武器红线
* 法甲马赛俱乐部遭网络攻击，近 40 万球迷及员工数据疑似泄露
* 谷歌发布 Nano Banana 2，AI 图像生成安全与效率双升级
* 北约认证民用 iPhone 处理涉密信息，消费级设备迎安全新标杆
* 警惕 Windows 文件资源管理器陷阱，黑客借其植入远控木马静默入侵
* 男子利用AI伪造医院诊断证明敲诈商家 非法获利2500元被采取刑事强制措施

特别关注

**CNVD 公开Apache Continuum命令注入漏洞**

2026年2月28日，CNVD公开Apache Continuum命令注入高危漏洞（CNVD-2026-11796/CVE-2016-15057），危害等级高，漏洞评分符合 AV:N/AC:L/Au:S/C:C/I:C/A:C 标准，该产品全版本均受影响。

Apache Continuum 是 Apache 基金会的企业级持续集成服务器，此次漏洞因命令特殊元素中和不当引发，攻击者获取产品 REST API 访问权限后，可注入恶意指令在服务器执行任意操作，最终导致远程代码执行（RCE）。

需注意该项目已正式退役，官方明确不会发布修复补丁，此前标注的厂商修复程序链接无实际修复作用。Apache 基金会建议用户尽快替换该产品，或严格限制实例仅对可信用户开放，以此规避漏洞攻击风险。

原文链接：

https://www.cnvd.org.cn/flaw/show/CNVD-2026-11796

**俄罗斯 AI 主权法案落地：强制认证、设备预装、安全审查三重合规**

2026年2月27日，俄罗斯拟定AI法案，计划2027年9月1日生效。法案将AI模型划分为主权型、国家型与可信型三类，主权模型需全程在俄境内研发、训练与运营，仅可用本土数据集；国家模型允许使用海外开源组件与数据集。两类模型均需通过 FSTEC与FSB强制认证，用于关键信息基础设施的可信模型安全需两部门联合确认。

法案要求智能终端预装认证AI程序，明确生成内容归属、合成内容标记与AI交互告知义务。业内指出，俄市场几乎无纯主权AI方案，从零研发成本超千亿卢布，将推高企业成本、加剧人才流失，或导致行业陷入模型竞赛，削弱产品竞争力。

原文链接：

https://www.securitylab.ru/news/569846.php

热点观察

**209亿美元教训：数据经纪商的"隐形陷阱"如何让消费者成为诈骗猎物**

美国国会联合经济委员会民主党发布报告显示，四家数据经纪商相关重大数据泄露事件，已造成超 209 亿美元消费者身份盗窃损失。

该调查由参议员Maggie Hassan发起，针对 Comscore、Findem、IQVIA Digital、Telesign、6Sense Insights 五家数据经纪商。调查发现，多家企业利用 “no index” 代码屏蔽搜索引擎收录，故意隐藏隐私退订页面，形成暗黑模式，大幅提升用户信息被诈骗分子利用的风险。涉案数据包含出生日期、地址、社保号等敏感信息。

在国会施压后，Comscore、Telesign、6sense、IQVIA 均移除 “no index”、优化退订入口或更换合规页面。仅 Findem 未回应问询，且未移除相关代码。其 2024 年披露信息显示，该公司 80% 的用户隐私请求未处理。

报告聚焦Equifax、Exactis、National Public Data、TransUnion四起重大泄露事件，涉事人数从440万至2.7亿不等。研究显示，超30%泄露受害者遭遇身份盗窃，其中近六成产生经济损失。

原文链接：

https://www.wired.com/story/data-broker-breaches-fueled-dollar209-billion-in-identity-theft-losses/

**非工作时间成重灾区：88%勒索软件在下班时段加密**

Sophos 发布《2026主动攻击者报告》，基于 2024年11月1日至2025年10月31日全球70国661 起安全事件分析，揭示当前攻击核心特征。

报告显示，身份相关技术占攻击根源的67%，包括凭证泄露、暴力破解、钓鱼等身份滥用行为，远超漏洞利用等技术入口，成为最主要初始入侵途径。

攻击者得手后快速转向核心身份基础设施，入侵 Active Directory 的中位时间仅3.4 小时，整体攻击驻留时间中位值为3天，为横向移动、权限提升与勒索部署留出充足窗口。

时间规律上，88%的勒索软件加密、79%的数据窃取发生在非工作时间，大幅降低被即时阻断概率。生成式 AI 暂未实现自主攻击，主要用于提升钓鱼话术质量、降低攻击门槛，成为现有攻击手段的效率放大器，未改变身份入侵、目录攻击、勒索加密的核心攻击链路。

原文链接：

https://www.helpnetsecurity.com/2026/02/27/sophos-identity-driven-breaches-report/

安全事件

**美军强索 AI 技术遭抵制，Anthropic 坚守监控与武器红线**

Anthropic与美国国防部就军方无限制获取其AI技术的要求陷入僵局，五角大楼设定周五下午为合规最后期限，还以将其列为供应链风险、援引《国防生产法》（DPA）相威胁，Anthropic则坚决反对 AI 用于国内大规模监控和自主武器研发。

事件引发行业声援，超300名谷歌员工、60余名 OpenAI员工签署公开信，呼吁企业高层联手支持 Anthropic，坚守其划定的技术使用红线，指责军方试图分化企业的策略。谷歌、OpenAI暂未正式回应，但非正式表态显示对Anthropic持同情态度，OpenAI CEO还直言反对军方以DPA威胁企业。

谷歌DeepMind首席科学家Jeff Dean也以个人名义发声，反对政府大规模监控，称其违反宪法第四修正案。据悉美军目前可将多款主流AI用于非机密任务，正洽谈将其纳入机密工作，而Anthropic虽与五角大楼有合作，却始终坚持技术使用边界。

原文链接：

https://techcrunch.com/2026/02/27/employees-at-google-and-openai-support-anthropics-pentagon-stand-in-open-letter/

**法甲马赛俱乐部遭网络攻击，近40万球迷及员工数据疑似泄露**

2026年2月27日，法国足球俱乐部Olympique de Marseille确认遭遇网络攻击。黑客声称已入侵俱乐部内部系统，并在黑客论坛发布部分数据样本，宣称泄露约40万人信息，涵盖姓名、地址、订单记录、邮箱及手机号等球迷与员工个人数据，同时泄露超过2050个 Drupal 相关账户，含员工、管理员等账号。

俱乐部表示已联合技术团队快速控制攻击，各项服务正常运行，银行数据与密码未受影响，正全面核查事件规模。目前俱乐部已向法国数据保护机构 CNIL报备并报案，同时提醒球迷警惕钓鱼邮件与可疑信息。

此次攻击并非法国足坛首例，此前法国足协也曾发生类似数据泄露事件。

原文链接：

https://www.securitylab.ru/news/569835.php

**男子利用AI伪造医院诊断证明敲诈商家 非法获利2500元被采取刑事强制措施**

2026年2月25日，上海杨浦警方通报一起利用AI 工具伪造材料实施敲诈勒索的案件，犯罪嫌疑人杨某已被依法采取刑事强制措施，其通过AI伪造凭证累计非法获利2500元。

该案案发于2025年12月，杨某利用AI软件篡改他人就诊记录，替换姓名、调整日期、伪造金额并添加虚假病因，生成假医院诊断证明、收费单据等材料，以 “就餐致病” 为由向烤肉店索赔 2000元，还持伪造材料向监管渠道投诉施压。商家赔付后发现疑点报案，警方核查证实材料系伪造，且杨某共实施敲诈2起既遂、2起未遂。

杨某的作案手段暴露了AI 工具普及背景下，伪造电子凭证的违法犯罪新趋势，也对各类机构的内容真实性核验能力提出新要求，需通过技术手段强化对电子材料的溯源与真伪鉴别，防范AI伪造带来的安全风险。

原文链接：

https://mp.weixin.qq.com/s/Ulim-WuzaO\_rXjVOeB945g

攻防技术

**警惕Windows文件资源管理器陷阱，黑客借其植入远控木马静默入侵**

安全研究发现黑客利用Explorer Trap攻击手段，将 Windows 系统原生的文件资源管理器变为隐蔽入口，向设备植入远程访问木马（RAT），实现无感知的远程控制。该攻击利用文件资源管理器的功能漏洞，绕开常规安全软件的检测，木马植入后全程静默运行，不会触发系统告警，黑客可借此窃取设备数据、操控设备操作。

此类攻击的核心威胁在于利用系统原生组件的信任属性，突破防护边界，常规的病毒查杀、防火墙策略难以识别拦截。受攻击设备会被黑客长期控制，成为网络攻击跳板，对企业内网、个人终端的数据安全造成严重威胁。

安全从业者需重点监控文件资源管理器的异常进程与注册表修改，及时修补系统漏洞，同时强化对原生系统组件的行为审计，避免其成为黑客的攻击跳板。

原文链接：

https://securityonline.info/the-explorer-trap-how-hackers-turn-windows-file-explorer-into-a-silent-portal-for-remote-access-trojans/

产业动态

**北约认证民用iPhone处理涉密信息，消费级设备迎安全新标杆**

2026年2月，北约正式认证苹果 iPhone、iPad 为可处理联盟受限级别涉密信息的消费级移动设备，成为全球首款且唯一获此资质的民用终端，相关系统已纳入《北约信息安全保障产品目录》。

此次认证由德国联邦信息安全办公室 BSI 完成全维度检测，设备无需改装或加装专用安全软件，仅需满足 A16 及以上芯片、iOS26/iPadOS26 系统、原厂未越狱并开启 Apple ID 双重认证三个条件，即可凭借原生安全架构实现合规。

其底层安全能力覆盖硬件信任根、内存实时加密、生物识别防破解等12大维度，端到端加密、权限隔离等机制全程静默运行。该认证简化了北约项目中苹果设备的审批流程，也为政府、军工等领域的安全终端选型提供了新方向，印证了消费级设备全栈式安全架构的落地价值。

原文链接：

https://securityonline.info/standard-hardware-military-guard-nato-certifies-retail-iphones-for-restricted-state-intelligence/

**谷歌发布 Nano Banana 2，AI 图像生成安全与效率双升级**

谷歌推出 AI 图像生成模型 Nano Banana 2，底层基于 Gemini 3.1 Flash Image，兼顾 Nano Banana Pro 的知识推理能力与 Flash 架构的低延迟特性，已成为 Gemini App、Google Search AI 模式、Google Lens、Flow AI Creative Studio 默认模型。

该模型支持单工作流保持 5 个角色视觉一致，最高输出 4K 分辨率，强化文本渲染与复杂指令遵循能力，可快速迭代编辑并生成高精度图文内容。Google AI Pro 与 Ultra 用户可按需调用 Nano Banana Pro 处理专业任务。

Nano Banana 2 内置 SynthID 数字水印并兼容 C2PA 内容凭证，提升 AI 生成内容可追溯性与合规性，解决行业内容溯源痛点，标志谷歌在生成式 AI 安全与规模化落地方面进一步完善。

原文链接：

https://securityonline.info/google-unveils-nano-banana-2-to-standardize-4k-ai-imaging-across-gemini/

**联系我们**

合作电话：18610811242

合作微信：aqniu001

联系邮箱：bd@aqniu.com

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/wKeDC5RjIzG0r9PBe2QsdR03e3XfH8prOV2wicE4GO80PbJFRGI5wmMMaD6Eibux9YbBhticXhNZ6xpZTWA6AkbUM6ia9fcgRgFdtpw6VvGfEHI/640?wx_fmt=gif&from=appmsg)

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