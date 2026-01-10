---
title: 安全资讯汇总：2026.1.5-2026.1.9
url: https://mp.weixin.qq.com/s/IzAwdorVqhztbOVLj7Y7ZA
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:17.041844
---

# 安全资讯汇总：2026.1.5-2026.1.9

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/41AD92vfadTT6W8UysI8hrqmKYNZyDBvH09lm1uAZI183D0axKTOl4gEAWR0E0hf6rkmU3vSOhYQH255hfQNTA/0?wx_fmt=jpeg)

# 安全资讯汇总：2026.1.5-2026.1.9

江南信安

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注江南信安**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/41AD92vfadSmGv36Z8hDtibLcicK5wXWGYx7otjSPeIl1emFfcFbyjCDNMlIOyUH86FuzoQKPdlUHH2dRun2IfeQ/640?wx_fmt=png)

**安全专栏**

**2026/1/5-2026/1/9**

江南信安网络安全汇总专栏，每周为您提供网络安全领域「标准规范、安全热点、行业发展、深度好文、融资信息」等最新资讯的追踪与共享。

**标准规范**

**1、**国家数据局领导班子调整，明确2026年“数据要素价值释放”重点任务

1月7日，国务院任命张建民为国家数据局副局长。张建民曾任国家发改委投资司司长等职，上任后该局领导架构恢复为“一正四副”。国家数据局负责协调数据基础制度建设、统筹数字中国建设等。近日召开的全国数据工作会议将2026年定为“数据要素价值释放年”，部署了推进数据科技与产业融合、强化数据赋能人工智能发展等八大重点任务，旨在推动数据“供得出、流得动、用得好、保安全”，促进数据要素融入经济价值创造。

原文链接：

[张建民任国家数据局副局长，此前系国家发改委投资司司长](https://mp.weixin.qq.com/s?__biz=MzkwODMxNjY5NA==&mid=2247524924&idx=1&sn=f64b71f154498d9d70dd311aa3bf2756&scene=21#wechat_redirect)

2、国家密码管理局公告（54号）

国家密码管理局发布**GM/T 0031-2025《安全电子签章密码技术规范》等20项密码行业标准，自2026年7月1日起实施。**

**原文链接：**

**[国家密码管理局公告（54号）](https://mp.weixin.qq.com/s?__biz=MzUzNTU2NTYwNQ==&mid=2247518614&idx=1&sn=77ac7bc7765b15e72801574daafa44f6&scene=21#wechat_redirect)**

**安全热点**

1、**美国打击委内瑞拉总统行动中疑似动用网络武器致首都断电**

在美军1月3日对委内瑞拉发动大规模军事打击并抓捕总统Nicolás Maduro后，该国互联网连接出现明显异常。独立监测机构NetBlocks确认，加拉加斯部分地区在军事行动期间因断电导致网络连接中断。

特朗普总统在新闻发布会上暗示，美国可能使用了网络攻击或技术手段切断了加拉加斯的电力供应。他表示“首都陷入黑暗是由于我们拥有的某种专业技术”。如果属实，这将是美国罕见公开使用网络战能力的案例。

Tor Metrics数据显示，委内瑞拉的Tor网络使用量在事件发生后出现显著激增，达到之前基准的数倍。这一模式表明，在常规通信渠道不安全的情况下，数万名委内瑞拉民众转向使用匿名工具规避审查和监控。

值得注意的是，去年12月委内瑞拉国家石油公司PDVSA曾遭受网络攻击导致出口业务中断，该公司当时指控美国政府实施了这次攻击。此次事件进一步加剧了委内瑞拉在信息安全和网络主权方面面临的严峻挑战。

原文链接：

https://securityaffairs.com/186509/intelligence/what-is-happening-to-the-internet-in-venezuela.html

**2、****沉寂十年的Careto组织重现江湖，利用邮件服务器漏洞攻击关键基础设施******

在消失十年后，高级持续性威胁组织Careto(又称“面具”)于2022年重新活跃，针对拉丁美洲知名组织和关键基础设施发动复杂攻击。该组织自2007年起就以利用零日漏洞植入复杂程序著称，主要目标为政府机构、外交实体和研究机构。

Securelist研究人员发现，Careto采用了更为精细的攻击手段。攻击者入侵网络后，重点攻击MDaemon邮件服务器，利用其WorldClient网络邮件组件实现持久化。建立立足点后，Careto部署了此前未知的FakeHMP植入体进行横向移动。攻击者滥用HitmanPro Alert驱动程序(hmpalert.sys)等合法系统驱动，将恶意代码注入winlogon.exe和dwm.exe等特权Windows进程。FakeHMP具备全面监控能力，包括键盘记录、屏幕截图捕获、文件检索和额外载荷部署。

原文链接：

https://cn-sec.com/archives/4862752.html

3、**电信基础设施遭挑战：Brightspeed数据泄露与服务中断风险引发关注**

近日，美国光纤宽带服务提供商Brightspeed正紧急调查一起疑似安全事件，黑客组织Crimson Collective声称成功入侵其系统并获取超过1 百万名客户的敏感信息，同时造成部分用户网络连接中断。

据威胁方透露，窃取的数据包括客户姓名、电子邮箱、电话号码、账单地址、账户状态、服务记录及部分支付信息等个人可识别信息（PII），并已向第三方安全研究人员提供泄露样本作为“证明”。安永信息 此类做法不仅增加对目标企业的压力，也反映出现代威胁行为者常用的公示与勒索策略。

Brightspeed目前尚未确认数据泄露细节，但已在调查中，并表示将及时通知受影响的客户与监管机构。该公司服务覆盖20个州、超过730万户家庭与企业，在美国电信基础设施中占重要地位，因此此次安全事件若被证实，可能对用户隐私和网络可用性造成实质性影响。

原文链接：

https://www.infosecurity-magazine.com/news/hackers-disconnect-brightspeed/

**行业动态**

**1、**2025年网安融资激增47%，AI治理成资本宠儿****

****2025年全球网络安全公司共完成392轮融资，募资总额达139.7亿美元，同比2024年的95亿美元增长47%，成为自2021年高点以来最强劲的一年。报告指出，此轮回暖并非资本泛滥，而是投资人更强调技术深度、商业执行力及与企业真实需求的匹配度。****

****从轮次看，种子轮和Series A占比约三分之二，但资金高度集中于后期项目。全年共有30笔融资超过1亿美元，虽仅占8%的轮次，却吸纳近一半资金。代表性项目包括Saviynt（7亿美元）、Cyera（5.4亿美元）、Armis（4.35亿美元）等。****

****投资方向上，围绕AI安全的治理、风险管理与合规（GRC）成为热点，身份安全被视为现代风险控制的核心执行点，同时欺诈防护、ICS/OT与关键基础设施保护也受到关注。Pinpoint指出，在预算趋紧背景下，企业更青睐能交付可量化安全效果的平台型厂商，推动市场加速整合。****

原文链接：

https://www.securityweek.com/cybersecurity-firms-secured-14-billion-in-funding-in-2025/

**2、****PCI DSS 4.0合规困境:密码管理器从便利工具转变为合规基础设施******

PCI DSS 4.0将合规重点从技术控制转向员工行为，密码复用、凭证存储在电子表格、共享登录等日常习惯成为合规失败的主要原因。新标准要求12.6强调基于角色的持续培训和安全意识活动，要求组织证明员工理解其行为对持卡人数据安全的影响。

传统密码规则如长度、复杂度和轮换策略虽满足技术要求，但实际增加了员工负担，导致更多密码重置、可预测模式和重复使用变体，并未改善安全结果。密码管理器可作为合规基础设施，同时满足PCI DSS多项要求:生成唯一凭证减少复用，消除电子表格等不安全存储方式，集中访问审查，配合基于角色的权限支持最小权限原则。

Passwork CEO Alex Muntyan指出，当安全工具与员工工作方式对抗时合规就会崩溃，密码管理器改变了这一动态。Passwork作为本地部署解决方案，帮助组织在自有基础设施内集中管理凭证，提供基于角色的访问控制和审计日志，满足PCI问责期望。

有效的PCI DSS合规项目通过设计减少违规，使安全路径比不安全路径更容易。将密码管理器整合到培训和日常操作中，将合规从项目转变为日常运营的一部分，这正是PCI DSS 4.x衡量员工行为的核心要求。

原文链接：

https://www.helpnetsecurity.com/2026/01/08/passwords-pci-dds-compliance/

3、**攻击面管理陷ROI困境，AI技术推动网络安全价值重塑**

攻击面管理（ASM）正面临投资回报率（ROI）证明危机。传统ASM工具虽能识别漏洞，但难以量化其业务价值，导致安全团队在预算审批时陷入困境。

研究显示，企业平均每年在网络安全工具上投入数百万美元，但75%的安全主管无法清晰展示这些投资的实际回报。ASM工具发现的大量漏洞往往缺乏优先级排序和业务影响分析，使得修复工作效率低下。更严峻的是，传统ASM依赖人工分析和手动修复，响应周期长达数周甚至数月。

AI技术正在改变这一局面。新一代ASM解决方案通过机器学习算法实现风险自动评估、威胁优先级智能排序和修复建议生成。AI能够关联漏洞与业务资产，量化每个安全漏洞的潜在财务影响，将抽象的安全风险转化为可衡量的业务指标。

行业专家指出，AI驱动的ASM不仅缩短了从发现到修复的时间，更重要的是建立了安全投资与业务成果之间的可见联系，帮助企业将网络安全从成本中心转变为价值创造部门。

原文链接：

https://www.webpronews.com/cybersecuritys-asm-roi-crisis-ai-driven-shift-to-measurable-outcomes/

**深度好文**

1、金融行业网络钓鱼攻击的范式演进与防御体系的适应性强化

当前，云计算、大数据、人工智能、物联网等数字化核心技术全方位重塑传统金融业务模式，推动金融服务向智能化、便捷化、高效化迈进。金融数字化为行业带来诸多机遇的同时，也面临着一系列挑战。据APWG 2025年第二季度报告，全球钓鱼攻击达113万起，创近两年新高，其中，针对金融机构的钓鱼攻击占比达18.3%，支付行业亦高达12.1%，二者合计超过三成，已成为网络钓鱼攻击的首选目标。

网络钓鱼攻击正加速向服务化、高隐蔽性与智能化演进，对高度依赖数字信任机制的金融行业构成系统性威胁。深入研判其演化趋势、剖析金融体系的结构性脆弱点，并探索技术与治理协同的适应性防御路径，不仅关乎金融机构的安全韧性，更对维护国家金融稳定与用户数字权益具有重要现实意义。

# 原文链接：

[专题·金融安全 | 金融行业网络钓鱼攻击的范式演进与防御体系的适应性强化](https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664256933&idx=1&sn=fcf948c45d5941b93a182775314c2c0b&scene=21#wechat_redirect)

**2、**卫星+密码技术典型应用

卫星技术与密码技术的融合，是空天信息安全保障的核心路径，既解决卫星系统自身的身份认证、数据保密、抗篡改需求，也支撑卫星应用向民用、商用领域安全延伸。二者结合的核心逻辑是：用密码技术为卫星全生命周期、全业务链路提供可信安全底座。

原文链接：

[密码场景 | 卫星+密码技术典型应用（案例学习）](https://mp.weixin.qq.com/s?__biz=MzIyNDQxNjQzOQ==&mid=2247492669&idx=1&sn=635847dd8a94b231664c348863107edf&scene=21#wechat_redirect)

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/41AD92vfadSXHTH1scEGm9rr9ibJduPzOEm2eQUpLPWJwpsmlqCzCVuLrGgxBAlbjCqHzYrAhYfaP1XFyId58ew/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/XYUkuDD17Pickg7BesWrKzNdf4JtoCtsOH2Xibib98vGeiaQO53BHoFtelNwib4eLvZmeXPSRfM9hRFYC4Fl0MXEzvQ/640?from=appmsg)

**点点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/XYUkuDD17Pickg7BesWrKzNdf4JtoCtsOGmgiaibiat2qwrCSseEOYfyb86icshIsLqZ0YMHks4NsBvahmiaaofz1QTA/640?from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/B7LNzOKP0LJXMuChCUaliaCusxMWdjA128apnzfhqdEI9FH69rRrCIHzPyQ33nPQiakSUxhFxF5LhOKenaz5rjEQ/640?from=appmsg)

**点喜欢**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/41AD92vfadTn69kCsyd3JGMOAQ1beOTiba8Tg48QcxWibG2CPEWxAZcrpOj9noP6fCPUIELUGayNJEeZVdhWia0rw/0?wx_fmt=png)

江南信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/41AD92vfadTn69kCsyd3JGMOAQ1beOTiba8Tg48QcxWibG2CPEWxAZcrpOj9noP6fCPUIELUGayNJEeZVdhWia0rw/0?wx_fmt=png)

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