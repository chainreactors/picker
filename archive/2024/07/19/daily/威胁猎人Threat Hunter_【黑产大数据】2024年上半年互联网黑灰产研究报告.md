---
title: 【黑产大数据】2024年上半年互联网黑灰产研究报告
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247497634&idx=1&sn=4dac09059461a678e549d30ac8e421e9&chksm=eb12d199dc65588f56576066e7a31fb9220e026d04ca103a2cc1063cb85bbc63ecccd7e2bc8b&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2024-07-19
fetch_date: 2025-10-06T17:42:30.868271
---

# 【黑产大数据】2024年上半年互联网黑灰产研究报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aiaKFJLPvWtfxlYOEKCEmfzgndoFG0picpRwMuWicTWBsjROWVpa8E2YiaQ/0?wx_fmt=jpeg)

# 【黑产大数据】2024年上半年互联网黑灰产研究报告

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

2024年上半年，黑灰产从业人员人数超过427万，威胁猎人监测到**国内作恶手机号数量高达323万，日活跃风险IP数量1136万，涉及洗钱银行卡数量19.5万**。

近年来，数字化与实体经济的融合日渐深入，大规模业务线上场景下，黑灰产对企业业务安全的扰乱更加突出，**恶意刷量、薅羊毛、金融欺诈等**攻击事件层出不穷。

逐渐智能化和链条化的网络黑产运作，给企业带来真金白银的经济损失，影响了企业正常运营及长期发展，打击网络黑灰产，加强有效防御成为各行业企业的目标与共识。

威胁猎人发布**《2024年上半年互联网黑灰产研究报告》**，从2024年上半年互联网黑灰产发展现状、黑灰产攻击资源、黑灰产攻击技术及场景等维度进行全面梳理分析，力求通过客观呈现黑灰产情报数据，帮助更多企业深入直观了解黑灰产业，有效防控各类攻击风险。

**相关名词定义**

**1、风险IP：**业内也称黑IP，指存在攻击风险（包括代理、秒拨等恶意行为）的IP；

**2、风险手机号：**存在被滥用盗用等风险的手机号，如被黑产用于接收短信，实施批量恶意攻击的手机号，通常从接码平台或发卡平台捕获；

**3、风险邮箱：**指被黑产用于恶意注册生成的临时邮箱，用以骗取用户重要信息、传播恶意程序等；

**4、黑手机卡：**指未进行实名登记或以假身份进行实名登记的，并被不法分子利用实施违法犯罪活动的电话卡；

**5、猫池卡：**指通过“猫池”这一网络通信硬件，实现同时支持多个号码通话、群发短信等功能的黑手机卡；

**6、拦截卡：**指通过病毒木马控制真实用户手机短信/验证码收发权限的手机卡，通常捕获自拦截卡平台；

**7、洗钱银行卡：**指被黑产用于非法资金清洗（将违法所得收入合法化）的银行卡，例如赌博及诈骗团伙通过银行卡消费、转账等方式转移洗钱资金；

**8、涉赌卡：**指常被用于赌博平台内进行充值收款的银行卡，关联资产涉及到赌博洗钱行为。威胁猎人通过人工和自动化结合的方式，从各类赌博平台中监测用于收款行为的银行卡账号信息；

**9、跑分卡：**指活跃在跑分平台，常被用于各种非法来源资金的流通交易的银行卡。威胁猎人通过自动化的方式，从跑分平台APP中获取到跑分订单中的银行卡账号信息；

**10、涉诈卡：**指常被用于社交黑产群聊中进行诈骗资金转移的银行卡，关联资产涉及到诈骗洗钱行为。威胁猎人通过自动化的方式，从各大匿名社交黑产群聊中发送记录中，提取诈骗团伙使用银行卡账号信息；

**11、洗钱对公账户：**指被黑产用于非法资金清洗的银行对公账户，因对公账户具有收款额度大、转账次数多等特点，使得“对公账户”常常作为黑钱转账的集中点及发散点；

**12、数据泄露事件：**威胁猎人安全研究专家针对数据泄露情报的样例等进行分析及验证，确认为真实、有效的数据泄露事件；

**13、暗网：**指隐藏的网络，普通网民无法通过常规手段搜索访问，需要使用一些特定的软件、配置或者授权才能登录。

**一、2024年上半年互联网黑灰产发展现状**

***1.1*** **2024年上半年互联网黑灰产从业人员达427万，较2023年下半年下降6.03%**

威胁猎人调研统计发现，2024年上半年互联网黑灰产从业人员数量达到427万，较2023年下半年略有下降6.03%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aMpLuR3lm2oJxRr6OkC48qRVVuWssg9pFL482n8l2XMmGAibibJdTuNJw/640?wx_fmt=png&from=appmsg)

***1.2*** **2024年上半年黑灰产资源概况**

***1.2.1*** **2024年上半年新增国内风险手机号总量较2023年下半年增长8.8%**

据威胁猎人风险情报平台数据显示，2024年上半年国内风险手机号数量达到323万，较2023年下半年增长8.8%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aiaqR5DHqwnge2a1AQr4qdgYjqlLkFm1dNGwArJ5929PfJ2Ax2RC57Rw/640?wx_fmt=png&from=appmsg)

***1.2.2*** **2024年上半年风险IP总量较2023年下半年增长44.8%**

2024年上半年，威胁猎人监测发现日活跃风险IP数量持续上升，风险IP数量达到1136万，较2023年下半年增长44.8%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aPEtwQ6ah4BgonbLMRphTg91SV91F9A9O0N37WoZL1Dj2U8GkdAZXDg/640?wx_fmt=png&from=appmsg)

***1.2.3*** **2024年上半年涉及洗钱银行卡较2023年下半年下降28%，主要由跑分卡大幅减少所致**

2024年上半年涉及洗钱银行卡数量19.5万，较2023年下半年下降28%。涉及洗钱银行卡主要包括跑分卡、涉赌卡、涉诈卡。

其中，跑分卡新增数量的降幅最大，较2023年下半年下降50.3%，威胁猎人针对黑产团伙的跑分方式深入挖掘发现，2024年上半年跑分团伙逐渐由跑分平台转向通过Telegram进行跑分，使得监测难度大幅提升。

**涉赌卡：**指常被用于赌博平台内进行充值收款的银行卡，关联资产涉及到赌博洗钱行为。威胁猎人通过人工和自动化结合的方式，从各类赌博平台中采集用于收款行为的银行卡账号信息。

**跑分卡：**指活跃在跑分平台，常被用于各种非法来源资金的流通交易的银行卡。威胁猎人通过自动化的方式，从跑分平台APP中获取到跑分订单中的银行卡账号信息。

**涉诈卡：**指常被用于社交黑产群聊中进行诈骗资金转移的银行卡，关联资产涉及到诈骗洗钱行为。威胁猎人通过自动化的方式，从各大匿名社交黑产群聊中发送记录中，提取诈骗团伙使用银行卡账号信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aa1LmfQCtqjwm91G0t82Q68Q83CI5U5HYzDmhF6iaLczDBqnibulhbsDw/640?wx_fmt=png&from=appmsg)

**二、2024年上半年黑产攻击资源分析**

***2.1*** **2024年上半年风险手机卡资源分析**

***2.1.1*** **2024年上半年猫池卡资源变化趋势**

**（1）****2024年上半年国内猫池卡较2023年下半年增加7.71%**

据威胁猎人情报平台数据显示，2024年上半年捕获新增猫池卡309万个，较2023年下半年上升7.71%。

**猫池卡：**指通过“猫池”这一网络通信硬件，实现同时支持多个号码通话、群发短信等功能的黑手机卡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aa3zWiar4rtGSTa0wN5ZfsTfbcb0yyvnrKlXHkibTu0bE7AA9kH2Bm4Jw/640?wx_fmt=png&from=appmsg)

经威胁猎人情报专家分析，**出现这一趋势的主要原因是：**

1、2月因春节期间黑产交易放缓，下游作恶者活跃度降低导致供应量显著下降，节后恢复稳步上涨趋势；

2、6月猫池卡数量下降主要受到高考期间风控加强的影响，高考期间各大平台账号批量注册、恶意引流等监测力度大大加强（如不可修改账号名称、头像、介绍等），多个渠道卡商主动反馈受该原因干扰，黑卡供给存在问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aM4iasrlbolTCRyC8ZUgPDyfC0smoIdvwfBvyjOl1mfEhVTo53PMjWfg/640?wx_fmt=png&from=appmsg)

**（2）****2024年上半年新增猫池卡归属最多的三个省份为：上海、山东、辽宁**

威胁猎人对2024年上半年新增国内猫池卡进行统计分析，发现上海、山东、辽宁三省（含直辖市）为猫池卡归属地最多的三个省份；针对归属城市分析发现，猫池卡归属地最多的三个城市为上海、重庆、武汉。

由下图可见，2024年上半年上海的猫池卡新增数量远超其他省市，深入分析发现，其主要原因在于2024年3月及5月，国内两大头部发卡平台持有并出售大量归属地在上海的风险手机卡，其数量在新增总量的40%以上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aGCkbOOcLQqaibV2mZQJRYkbQqicrMRkz7TUZtiaiaJyJYfghsN0tn6FicPQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aiadALmA92KBOlgNIkC8zia6HpYHNofDicNJA613pgTAIvcIw0L01GVeew/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7a4rF3I4L9hQFR7Ycibsriah0EMdM3ia2IBibmicNzjnyJH0fQeiblb99ky2Zg/640?wx_fmt=png&from=appmsg)

**（3）****2024年上半年捕获的猫池卡中，归属国内三大运营商的占76.1%**

2024年上半年监测到猫池卡364万张，其中归属国内三大运营商的猫池卡占比76.1%，归属其他运营商的占比23.9%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7a3tRG8gcAhDOedXjS2Gic732fnIuhQrViaNQggib7B942QPtcgxmvxWjhg/640?wx_fmt=png&from=appmsg)

***2.1.2*** **2024年上半年拦截卡资源变化趋势**

**（1）****2024年上半年国内拦截卡较2023年下半年增加42.57%，从新增渠道首次捕获的拦截卡占比高达94%**

2024年上半年，威胁猎人捕获新增拦截卡达13.18万，较2023年下半年增加42.57%。

针对捕获的拦截卡进一步分析发现，2024年上半年新增6个拦截卡来源渠道，同时捕获的拦截卡多为系统首次捕获，首次捕获占比高达94%，拦截卡供应渠道的增加与快速更新，无疑增加了业务方风控难度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7awTxEtECM4DLUA5YBA1XjIZF64m5Ocf4aiaa1ibG8gcZJia7E08jJFgTFQ/640?wx_fmt=png&from=appmsg)

**（2）****2024年上半年拦截卡归属最多的三个省份为：福建、广东、四川**

针对2024年上半年捕获到的国内拦截卡统计分析发现，福建、广东、四川三省为拦截卡归属地最多的三个省份；从归属城市来看，重庆市、三明市（福建）、上海市三城市为拦截卡归属地最多的城市，与猫池卡归属城市存在较大的重合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aOLvHqvkPduFDcxHJyWpnCibgarGEGL9icMroENy5wZr92icrLBahFSB5A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aicOnSbicQ99jOrzBRK9pKVVdsSEQvfsQd9xWKicshDhaThmiamC3F2D85Q/640?wx_fmt=png&from=appmsg)

**（3）****2024年上半年捕获的拦截卡中，归属国内三大运营商的占98.29%**

2024年上半年威胁猎人情报运营平台捕获拦截卡39.8万张，归属国内三大运营商的拦截卡占比达98.31%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aOu806p1Ey5RVKGyQYjSwfp4TGsWNlVhxyswTolvu3VapeFFksWiaVqA/640?wx_fmt=png&from=appmsg)

**2.1.3** **归属地为香港的风险手机卡大幅增加，2024年6月捕获香港相关风险手机卡近10万**

针对黑卡主要来源渠道进一步研究发现，2024年上半年，归属地为香港的风险手机卡交易数量呈现大幅增长趋势，2024年3月香港卡交易量级仅为数千张，2024年6月香港卡交易量级达到近10万。

香港相关风险手机卡数量的大幅增长，从需求侧来看，2024年5月至6月，香港发生多起线上诈骗事件，事件过程中，下游诈骗黑产利用香港手机卡注册whatsapp等境外聊天软件，对受害者展开线上诈骗，一定程度上导致了香港卡数量的大幅增长，也反映了风险手机卡在地域上的风险趋势及供需变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aVlicAYqhIRkEhNBJZJlum1D37BafVHeXJGcibuibicSl2nZabvib79WhW4w/640?wx_fmt=png&from=appmsg)

**对比其他境内手机卡，香港手机卡具备如下特点：**

**1、注册范围广：**香港手机卡注册范围广，可注册Telegram、WhatsApp等海内外应用；

**2、在线使用时间长：**香港手机卡接码服务的在线使用时间相对境内卡更长，一般可保证一个月重复使用，而境内手机卡一般为数日；

**3、价格较低：**香港手机卡的价格相对境内卡接码价格更低；

**4、支持多种接码形式：**香港卡支持多种接码形式，目前威胁猎人在接码平台、发卡网站、私域接码均发现了香港相关手机卡的作恶记录。

**2.1.4** **黑卡物料资源标签更加丰富，提升下游黑产筛卡效率、实现精准作恶**

威胁猎人研究发现，2024年上半年，黑产在非法交易中对黑卡物料的筛选及使用更为精细，相较于2023年黑卡商品描述字段，除了会提供黑卡类别，注册情况等信息外，**卡商还会标识号码“已筛选”**，即卡商在购买后的订单页面中展示号码的历史账户信息，并将信息提供给下游购买方，使其确定是否为目标卡类，减少筛卡成本，大幅提升下游黑产作恶效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aEllibkLPWWDdfmQpp6tkLiaCL4SDNuw7lcr4wnlxNYEzibLXQ37RvyDDQ/640?wx_fmt=png&from=appmsg)

与此同时，威胁猎人研究发现，黑灰产之所以能提供精确的账号及相关信息，主要借助了**黑灰产新老号检测工具**实现，该工具通过恶意调用业务相关的应用接口API，来检测号码是否注册或存在历史绑定记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7a4Ts8F5PS2u0bicQhOE7sC3ruFqR1FBYT8MHrYDm7C6vAmHDR5fmww4w/640?wx_fmt=png&from=appmsg)

***2.2*** **2024年上半年风险IP资源分析**

***2.2.1*** **2024年上半年风险IP资源变化趋势**

威胁猎人持续提升国内外风险IP监测能力，为互联网平台优化国内外风控规则提供了有力支持，2024年上半年威胁猎人持续监测国内风险IP5503万个，国外风险IP10273万个，较2023年下半年分别提升18.62%和22.44%。我们对国内及国外两种类型的风险IP分析发现：

**（1）****2024年上半年国内风险IP归属最多的三个省份：江苏、广东、河南**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7aoZNslq7OARzv5SPAQSutFUEVA8XHByNmIYv5u5kcXjgf2HTaibhUdNA/640?wx_fmt=png&from=appmsg)

**（2）****2024年上半年国内风险IP归属最多的三个城市：重庆、上海、北京**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGmWdCGg4M0LYMJiaTWVgt7a1WEFcbwXl90SlZ5v2iaYIGWhJdhib1d0CPicFoFUPLRjDfFQUUkCsCQQQ/640?wx_fmt=png&from=appmsg)

**（3）****202...