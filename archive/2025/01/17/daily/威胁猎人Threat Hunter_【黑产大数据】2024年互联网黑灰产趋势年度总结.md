---
title: 【黑产大数据】2024年互联网黑灰产趋势年度总结
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498891&idx=1&sn=9f040f1179476893f7e090a25d5c7db6&chksm=eb12dab0dc6553a6688a1502538c0a93299a3ae6095c314d0db7c1c3f67008f121543a1aa9df&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2025-01-17
fetch_date: 2025-10-06T20:14:16.122673
---

# 【黑产大数据】2024年互联网黑灰产趋势年度总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqGPRJmV536oicIUzrnqKnzk1LKV58YY0ejK8miayYLMUELoQhnQIYTNYmr0AMkg4ZvUicktlpmDFV6qg/0?wx_fmt=jpeg)

# 【黑产大数据】2024年互联网黑灰产趋势年度总结

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif)

2024年，互联网黑灰产攻击依旧严峻。不管是在黑灰产团伙规模，还是攻击资源、攻击技术的应用以及攻击场景的演变，均出现了较大的变化。

**在攻击资源方面**，2024年威胁猎人捕获全球新增**作恶手机号1600多万**例，**日活跃作恶IP1170万例**，较2023年大幅提升。为躲避风控监测，黑灰产不断升级技术寻找更加隐蔽的攻击资源，如通过在正常用户设备植入木马将其IP作为攻击资源、“商户洗钱”产业链快速发展等。

**在攻击技术方面**，2024年黑产团伙对通用技术的应用也有新的发展，如滥用“**子母机**”绕过身份认证、利用“**NFC远程传输软件**”进行境外洗钱、定制化云手机系统提升攻击效率等等。

**在攻击场景方面**，线上业务欺诈、金融贷款欺诈、品牌广告欺诈、API攻击、钓鱼仿冒、数据泄露、电信网络诈骗等场景热度持续高涨。**线上业务欺诈已进入深水区，全行业、全业务环节无差别攻击**；“王星事件”更是进一步提升了公众对电信网络诈骗的关注度。

威胁猎人发布**《2024年互联网黑灰产趋势年度总结》**，基于对2024年互联网黑色产业链的深入研究，从2024年黑灰产攻击资源、攻击技术、攻击场景等维度进行分析，客观呈现2024年互联网黑灰产的整体发展态势，旨在从情报维度帮助各行各业企业提升对黑灰产的认知，从而进一步完善风控策略。

**报告目录**

**一、2024年互联网黑灰产攻击资源分析**

**二、互联网黑灰产通用型攻击技术分析**

**三、2024年互联网黑灰产攻击场景分析**

3.1 线上业务欺诈

3.2 金融贷款欺诈

3.3 品牌广告欺诈

3.4 API攻击风险

3.5 钓鱼仿冒风险

3.6 数据泄露风险

3.7 电信网络诈骗

**一、2024年互联网黑灰产攻击资源分析**

***1.1*****2024年作恶手机号资源分析**

**1.1.1 2024国内作恶手机号新增数量超800万，较2023年提升30%**

据威胁猎人情报数据显示，近年来国内作恶手机号数量持续上涨，2024年新增量级**超800万**，较2023年增长30%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSnNHxF1E4jSt3pDG2zmeib1PlmYNhEWxt5A3LnVAhicQicTv0Q4HYnh4fQ/640?wx_fmt=png&from=appmsg)

作恶手机号资源中，**“猫池卡”和“拦截卡”占比最高**，下文1.1.2 和1.1.3将重点分析2024年“猫池卡”和“拦截卡”资源的变化情况。

**1.1.2 2024年「猫池卡」资源分析**

**（1）2024年国内新增猫池卡615万，较2023年增加4.86%**

据威胁猎人情报数据显示，2024年国内新增猫池卡615万个，较2023年上升4.86%。

**猫池卡：**指通过“猫池”网络通信硬件实现同时多个号码通话、群发短信等功能的作恶手机卡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSw9m2cInhfRBOqybCrZ5gTQdZOw4qWVRs7NoxiaDHdibicKeoPednWiap8A/640?wx_fmt=png&from=appmsg)

从2024年国内猫池卡数量的变化趋势来看，2月、6月到9月期间，新增国内猫池手机卡数量呈现下滑趋势。

**经威胁猎人情报专家分析，出现这一趋势的主要原因是：**

1、2月因春节期间黑产交易放缓，攻击者活跃度降低导致数量显著下降，节后恢复稳步上涨趋势；

2、6-9月期间，由于监管机构加强打击，多个发卡平台被关停，部分卡商被捕，造成供应减少，导致新增猫池卡数量下降。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSVlhJAr8ETyIMMtvIT7VjReyRYibIf7bqTaEfUNfXMulMB087mSs6Lfw/640?wx_fmt=png&from=appmsg)

**（2）2024年国内新增猫池卡归属省份TOP3：上海、北京、辽宁**

威胁猎人情报数据统计显示，2024年国内新增猫池卡归属地省份（含直辖市）主要集中在上海、北京和辽宁省。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMS783VTCSyibKUVPSTeQ0R5EXribL0NorT0jmTgfDn3GZ3JzicEkbXXl7zw/640?wx_fmt=png&from=appmsg)

其中，**归属地在上海的猫池卡数量同比2023年增长了87.86%**。威胁猎人关注到，今年上海的猫池卡在全年各月均保持较高数量，活跃在发卡平台的头部卡商今年也持续提供上海猫池卡。

通过对上海今年新增的猫池卡来源渠道分析，发现来自发卡平台的猫池卡数量占比超过一半：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSGj8BZRgm7HxHzOUnEAvsdYtpG4NvWHcPytMoMD9YmDdIP7qhw817Yg/640?wx_fmt=png&from=appmsg)

**2024年国内新增猫池卡归属地TOP10对比2023年变化情况：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSV2GX7F40h18Ijvd1stXfe5nKQiaHcNgepbO6D7Njj8Adjc7dwKsUhYQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSDYib7NTCyLtia4DsTAdqA14qOtKntOHPRg0wqKK2PgxcevnibtvYsFhRg/640?wx_fmt=png&from=appmsg)

**2024年归属地为中国香港的作恶手机号持续增长，全年捕获78.25万例**

值得关注的是，威胁猎人情报数据显示，自2024年3月起，归属地为中国香港的风险手机卡交易数量大幅增长，9月份达到峰值。

由于下游诈骗黑产需求旺盛，中国香港手机号因可注册国内外应用、成本低、可用时间长等特点，仍被黑产大量需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSsHCPMibIE3dc6lAbU0jItWj1r3HeHVVibKticR87SrIzff4VIAYonyOibw/640?wx_fmt=png&from=appmsg)

**对比其他境内手机卡，中国香港手机卡具备如下特点：**

**1、注册范围广：**香港手机卡注册范围广，可注册Telegram、WhatsApp等海内外应用；

**2、在线使用时间长：**香港手机卡接码服务的在线使用时间相对其他境内卡更长，一般可保证一个月重复使用，而其他境内手机卡一般为数日；

**3、价格较低：**香港手机卡的价格相对其他境内卡接码价格更低；

**4、支持多种接码形式：**香港卡支持多种接码形式，目前威胁猎人在接码平台、发卡网站、私域接码均发现了香港相关手机卡的作恶记录。

**（3）2024年国内新增猫池卡归属为三大运营商的占比为76.42%，比去年提升14.51%**

威胁猎人情报数据显示，今年国内新增猫池卡的归属运营商主要为基础运营商，占比高达76.42%，相比去年提升了14.51%。

威胁猎人情报人员通过调研发现，今年三大运营商占比提升，主要是很多企业进一步提升对虚拟运营商手机卡的风险控制，导致黑产对国内三大运营商的手机卡资源需求增加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSDL0zbyz22Z7Ln50ziaCYMnH09noheibtEIsDvzoQDp7sKqfcFq1RI6QA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSDYib7NTCyLtia4DsTAdqA14qOtKntOHPRg0wqKK2PgxcevnibtvYsFhRg/640?wx_fmt=png&from=appmsg)

**（4）2024年猫池卡发卡平台数量增加了39.37%，但平台生存周期缩短**

威胁猎人持续监控黑灰产作恶资源来源渠道变化趋势，发现作为猫池卡主要贡献渠道的发卡平台在2024年数量大幅增加，但生存周期缩短：

2024年新出现了171个猫池卡发卡平台，同步2023年增长39.37%，但其中**有24%的猫池卡发卡平台运营时间不足一周**。威胁猎人进一步调研发现，**今年发卡平台遭受了较强的监管压力，多个发卡平台以及活跃的猫池卡卡商因遭受监管打击而停止运营或活跃**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGPRJmV536oicIUzrnqKnzk1U1PUPvSrRbpvx1tP5uBWBBbVqPd9SbZVr14MjQZD2txoTYnib5Dfrew/640?wx_fmt=png&from=appmsg)

此外，威胁猎人对目前还存活的猫池卡相关发卡平台进行测试发现，一些黑灰产为了防止被监管打击，会采取一些较高的安全措施，包括但不限于**周期性订单删除、使用加密货币支付、频繁修改接码地址、限制异常访问和支付**等。

**1.1.3 2024年「拦截卡」资源分析**

**（1）2024年国内新增拦截卡196万例，较2023年增长405.50%**

据威胁猎人情报数据显示，2024年国内新增拦截卡大幅增加，共有196.64万例，较2023年增长405.50%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSBuwb3ex3kiagz5W7AMTfaqnjXZmibMa5cJLKJzOp7mI2Iiaje93wdNtUg/640?wx_fmt=png&from=appmsg)

威胁猎人研究发现，一月份拦截卡数量大幅提升是因为去年年底新出现的一个拦截卡渠道，投放了大量拦截卡资源，2024年该渠道贡献拦截卡数量近百万余例，占今年整体数量的48.82%。但该渠道在2024年6月到7月期间暂停活跃，最终在2024年12月停止运营。

**（2）2024年国内新增拦截卡归属省份TOP3：广东、山东、四川**

威胁猎人情报数据统计显示，2024年国内新增拦截卡归属地省份（含直辖市）主要集中在广东、山东和四川。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSXQTQNRqrGHC5qNyRu6PMz8SBiafaY5jSdKqReDodQemQQreMaW4qbHw/640?wx_fmt=png&from=appmsg)

****2024年国内新增拦截卡归属地TOP10对比2023年变化情况：****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMS10iaLxf2BIJPQkPyUFl59Nzd0EWtVPVKVkarNCtRLreeEWDxvt932Tg/640?wx_fmt=png&from=appmsg)

**（3）2024年国内新增拦截卡归属为三大运营商的占比为98.99%**

威胁猎人情报数据显示，今年国内新增拦截卡的归属运营商98.99%为基础运营商，归属其他运营商的占比1.01%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSTLhsnLRo1aPbzuv7ia2NvC8niaYydZFH6k0HAftVrXr39JXhqgZekdSQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSDYib7NTCyLtia4DsTAdqA14qOtKntOHPRg0wqKK2PgxcevnibtvYsFhRg/640?wx_fmt=png&from=appmsg)

**（4）“群接码”模式简化黑产使用拦截卡的流程，并使拦截卡真实平台更隐蔽**

威胁猎人研究发现，拦截卡的接码方式也逐渐从传统的拦截卡平台接码模式转变为“群接码”模式 。

这种模式下，**拦截卡卡商隐藏真实号码，仅展示打码号码，只有黑卡购买者可获取完整号码完成接码作恶**。

**传统的拦截卡平台接码样例：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSAicGnMdnibbeFiaHss4fMia7S736ZEXeSuUm0ET2DhrjdxwIQh9gm5cIXQ/640?wx_fmt=png&from=appmsg)

**“拦截卡”的群接码模式接码样例：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMS7txXbyZC6gfYUlBArvunjDN0vBYViaY2gjQA1cvBnvvrqcJGMaIVraA/640?wx_fmt=png&from=appmsg)

**相比传统拦截卡平台使用专属接码工具接码，这种模式的优势在于：**

**1、使用更便利，**卡商只需提供号码和接码链接，无需为下游代理或黑卡使用者开设账户或配置权限；

**2、更高隐蔽性，**卡商可通过“群接码”模式隐蔽真实的平台信息，不将平台的敏感信息暴露于使用者。

目前，通过“群接码”渠道日均捕获作恶短信记录1269例，作恶记录最高峰为11月，捕获作恶短信记录近6万例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMS8FkYJuhkPucjyqCuwWW2zjhDpSAgiaBvMfpSyVYBaHyXHmcEx5Fs2XA/640?wx_fmt=png&from=appmsg)

***1.2*****2024年作恶IP资源分析**

**1.2.1 2024年日活跃作恶IP有1178万，较2023年提升95.68%**

据威胁猎人情报数据显示，近年来日活跃作恶IP数量持续上升，2024年日活跃作恶IP数量达到1178万，较2023年增长95.68%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSGfd34L6po9MScWhN7Qu6ic15K8tWkF4vQpImNh52lDcubwGPJqKsd1w/640?wx_fmt=png&from=appmsg)

**1.2.2 2024年国内作恶IP资源分析**

**（1） 2024年国内作恶IP有7794万个，同比2023年增长31.96%**

2024年，威胁猎人共捕获国内作恶IP7794万个，同比2023年增长31.96%。

威胁猎人研究发现，2024年国内作恶IP的大幅增长**主要是劫持共用代理IP数量急剧增长导致**。2024年，国内劫持共用代理平台发展迅速，威胁猎人捕获劫持共用代理IP数量超4000万，占比从去年14.91%提升至今年的51.47%，且超过普通代理IP的占比。

**劫持共用代理IP：**指被黑产恶意劫持的正常用户IP资源。黑产通过在正常用户设备中植入木马，通过木马在正常用户网络上建立代理通道，且每次使用时间很短，因此普通用户难以感知到自己的IP被盗用。

威胁猎人在2024年1月已把这类IP标记为“劫持共用代理IP”风险标签。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSq4epkkt668B0mcNrurmdaHENsECicgwuH9bZ6ialoazd5FPicN1XqSWgw/640?wx_fmt=png&from=appmsg)

**（2）2024年国内作恶IP归属省份TOP3：江苏、广东、河南**

威胁猎人情报数据统计显示，2024年国内活跃的作恶IP归属省份（含直辖市）主要集中在江苏省、广东省和河南省。其中，河南省量级提升最大，提升了54.45%，排名也从23年的第六到了第三。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSh2X2mu255f0ZDR1IHCic1bPJ0ibZa1iarxqt6EvJlHraHPcGwEbOJg2uw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGNXvnMBJaNQFq2ovZyXHMSDYib7NTCyLtia4DsTAdqA14qOtKntOHPRg0...