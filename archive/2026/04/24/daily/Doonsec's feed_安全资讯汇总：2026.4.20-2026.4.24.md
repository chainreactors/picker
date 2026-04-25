---
title: 安全资讯汇总：2026.4.20-2026.4.24
url: https://mp.weixin.qq.com/s/0_o4PU4SlW9L2BbnTfg3eQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:35:41.897943
---

# 安全资讯汇总：2026.4.20-2026.4.24

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/41AD92vfadTT6W8UysI8hrqmKYNZyDBvH09lm1uAZI183D0axKTOl4gEAWR0E0hf6rkmU3vSOhYQH255hfQNTA/0?wx_fmt=jpeg)

# 安全资讯汇总：2026.4.20-2026.4.24

江南信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注江南信安**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/41AD92vfadSmGv36Z8hDtibLcicK5wXWGYx7otjSPeIl1emFfcFbyjCDNMlIOyUH86FuzoQKPdlUHH2dRun2IfeQ/640?wx_fmt=png)

**安全专栏**

**2026/4/20-2026/4/24**

江南信安网络安全汇总专栏，每周为您提供网络安全领域「标准规范、安全热点、行业发展、深度好文、融资信息」等最新资讯的追踪与共享。

**安全热点**

1、**美国两州医疗数据泄露波及60万人，配置错误成主因**

美国医疗行业再曝大规模数据泄露事件。根据SecurityWeek报道，Illinois和Texas两地医疗相关机构近期发生数据泄露，合计影响约60万名个人，暴露出医疗系统在数据安全和配置管理方面的持续风险。

在Illinois事件中，Illinois Department of Human Services（IDHS）因内部系统配置错误，导致用于资源规划的mapping工具被错误设为公开访问。该问题持续时间较长（约2021年至2025年），期间大量敏感数据处于可访问状态。泄露信息包括姓名、地址、case numbers、人口统计信息以及医疗援助计划相关数据，涉及Medicaid和Medicare Savings Program等项目，受影响人数超过60万。

技术层面来看，此次事件属于典型的“misconfiguration”问题，即访问控制或隐私设置未正确实施，导致本应内部使用的数据被暴露至公网。这类问题在云服务和数据平台中尤为常见，往往难以及时发现，且缺乏访问日志进一步加大了溯源难度。IDHS表示，系统无法确认是否存在数据被访问或滥用的情况。

与此同时，Texas相关事件则同样涉及医疗数据保护不足，进一步反映出医疗行业在数据生命周期管理、访问控制以及第三方系统治理方面的薄弱环节。虽然具体攻击方式未完全披露，但整体趋势显示，医疗机构既面临外部攻击（如ransomware、data exfiltration），也频繁因内部配置失误导致数据暴露。

事件发生后，相关机构已采取补救措施，包括修正访问权限、限制数据共享范围，并建立新的安全策略（如禁止将客户数据上传至公开平台）。此外，受影响人员将收到通知，以便采取后续防护措施。

从行业视角看，此类事件再次强调：相比复杂攻击手段，基础安全控制（如access control、data classification、least privilege）失效，往往才是导致大规模数据泄露的关键因素。对于网络安全从业者而言，加强配置审计、持续监控以及数据暴露面管理（attack surface management），仍是医疗行业防护的核心方向。

原文链接：

https://www.securityweek.com/data-breaches-at-healthcare-organizations-in-illinois-and-texas-affect-600000/

**2、****损害金融主权？俄交易所疑遭敌对国黑客攻击，近亿元被盗后停止运营******

Grinex是一家在吉尔吉斯斯坦注册、已被美国制裁的加密货币交易所，被认为主要在俄罗斯经营。该公司表示，遭遇了一起由“西方特种部门”黑客发起的攻击事件，导致价值达1300万美元（约合人民币8863万元）的加密货币被盗，交易所现已停止运营。

区块链安全公司TRM实验室也观测到了这起盗窃事件。研究人员发现约70个被清空的钱包地址（这一数字比Grinex报告的多出约16个），将被盗资产的价值估算为1500万美元。

TRM实验室及另一家区块链研究公司Elliptic均未说明，攻击者如何突破Grinex的防御。Grinex表示，自16个月前成立以来，其系统几乎一直遭受攻击尝试，此次最新攻击主要针对该交易所的俄罗斯用户。

原文链接：

[损害金融主权？俄交易所疑遭敌对国黑客攻击，近亿元被盗后停止运营](https://mp.weixin.qq.com/s?__biz=MzI5NTM4OTQ5Mg==&mid=2247639658&idx=4&sn=fc3fb2393c79b42f37f722922a5a1611&scene=21#wechat_redirect)

3、**法国国家身份系统 ANTS 遭网络攻击，1900 万公民数据疑似泄露**

2026 年 4 月 20 日，Security Affairs 报道，法国负责身份证、护照、驾照等安全证件管理的国家机构 ANTS 官网于 4 月 15 日遭网络攻击，疑似发生大规模数据泄露，涉事数据规模最高达 1900 万条。

法国内政部已确认事件成立，泄露数据包含公民全名、电子邮箱、手机号、出生日期、出生地、住址、账户元数据等 PII 信息，未涉及证件扫描件与账户直接登录凭证。官方已通报法国数据保护机构 CNIL、检察院及国家网络安全部门，开展溯源与影响范围调查，并强化平台防护措施。

黑客组织 breach3d/ExtaseHunters 在黑客论坛公开宣称窃取数据，并以私下议价方式兜售 1800 万至 1900 万条用户信息，声称数据真实未篡改，支持第三方托管交易。该数据若被滥用，可引发大规模身份盗用、金融诈骗、合成身份欺诈等长期安全风险。

目前官方尚未完全证实黑客所售数据的真实性，仅提醒用户警惕钓鱼短信、电话与邮件等后续诈骗行为。此次事件再次凸显政务身份系统作为高价值目标的安全脆弱性，对各国政务平台数据防护提出严峻挑战。

原文链接：

https://securityaffairs.com/191069/data-breach/frances-ants-id-system-website-hit-by-cyberattack-possible-data-breach.html

**行业动态**

**1、**国家安全部预警 AI 投毒风险，两类攻击机制及危害详解****

据国家安全部2026年4月21日发布的安全提示文章，近期，AI“投毒”隐蔽产业链被曝光，引发社会广泛关注。

所谓AI“投毒”，是指通过恶意数据污染AI模型的行为，不仅扰乱商业秩序、影响信息传播，更会危害国家安全。当前这类攻击日益呈现出链条化、隐蔽化、跨境化特征，常被用于恶性市场竞争，甚至可能涉及间谍活动。

AI“投毒”主要分为两类，一类是数据投毒，即向AI大模型训练数据中注入伪装成正常样本的恶意数据，达到削弱模型性能、降低准确性的攻击目的。不法分子借助GEO（生成式引擎优化）工具批量、高权重生成虚构产品介绍、虚假测评、恶意对比信息等虚假内容，定向投放至各类网络平台。AI大模型在训练与检索增强生成阶段会自动抓取网络信息，少量虚假内容经迭代学习后就能固化为“标准答案”，最终输出失真结果。

另一类是模型投毒，该方式更具隐蔽性与危害性，不法分子会通过模型微调、插件植入、接口篡改，在模型权重中嵌入触发式恶意指令。模型日常运行并无异常，遇到特定关键词、产品类别时会自动输出预设虚假内容。

文章指出，人工智能在赋能千行百业的同时，其安全风险也不容忽视。推动AI治理向善，守住数据安全底线，既是行业责任，也需要全社会共同参与。

原文链接：

https://baijiahao.baidu.com/sid=1863066548529045071&wfr=spider&for=pc

**2、****电科网安2025：业务重心调整之下的现金流转正******

2025年电科网安营收22.68亿元（同比-8.08%）跌至近五年新低，连续两年下滑，较2022年峰值34.38亿元累计缩水34%。归母净利润0.58亿元（-63.55%）、扣非净利润0.33亿元（-67.64%），利润降幅远超营收降幅。综合毛利率37.56%（-3.21pct），较2023年高点42.33%累计下降4.77pct。最大结构性变化是密码业务收入10.36亿元（-27.19%）被网络安全业务11.76亿元（+26.18%）首次反超——密码占比从57.66%降至45.67%，网安从37.78%升至51.86%，但两者毛利率差距悬殊（53% vs 24%），结构切换直接拖低综合毛利率。数据安全板块从1.12亿腰斩至0.56亿，规模仍小。

渠道策略上主动向渠道销售转型，渠道占比从5.27%升至8.91%、绝对规模同比+55.42%。人员战略"围绕密码核心技术聚焦重点业务、强化管理提升人效"，在收入下行期主动收缩技术团队，押注单人产出提升；销售人员仅降6.32%说明公司认为营销覆盖已无太多压缩空间。AI方向年报提及"探索人工智能等领域网络安全业务"，属方向性表态，未披露收入数字，暂无可量化商业化进展。

原文链接：

[电科网安2025：业务重心调整之下的现金流转正](https://mp.weixin.qq.com/s?__biz=MzkzMDE5MDI5Mg==&mid=2247511054&idx=1&sn=e234a0f6a999d3930449fe9587bf4f5b&scene=21#wechat_redirect)

3、******Todyl 上线全新安全保障市场 助力 MSP 完成合规认证与风险管控******

近日，网络安全厂商 Todyl 正式推出全新的Todyl Assurance Marketplace平台，该节点被企业创始人兼 CEO John Nellen 定义为公司发展历程中的第三大里程碑。本次升级重点围绕风险管理、合规管控、网络保险适配能力展开，同时联动 Optimize Cyber、GTIA、Spectra 三家行业机构达成生态合作。

该市场平台面向 MSP 服务商，围绕评估、加固、验证、担保四大流程，完善安全体系闭环。合作方可依托 GTIA 与 Spectra 提供的合规框架完成第三方安全认证，结合 Optimize Cyber 的攻防检测能力补齐安全服务能力，向终端客户直观佐证自身安全建设成效，同时凭借合规验证资质获取更优的网络保险费率。

Todyl 平台发展历经多个阶段，企业最初于 2020 年以 SASE 服务商入局，依托能力迭代先后集成 SIEM、终端安全、GRC 治理模块。此次新阶段升级，还融入自研 Janus AI 技术，打通平台各模块数据链路，优化事件分析与业务流转效率。

面对日益复杂的漏洞挖掘、供应链攻击与凭证泄露风险，Todyl 强调 SASE 架构可有效缩减攻击面，结合 ITDR 身份威胁检测响应能力，覆盖传统 VPN、防火墙等基础设施防护盲区。平台此次生态扩容，旨在提升 MSP 整体服务能力，助力服务商跳出纯技术表述，从业务风险视角向客户展示安全建设实效，完善全链路安全保障体系。

原文链接：

https://www.crn.com/news/security/2026/todyl-ceo-on-elevating-the-capabilities-of-msps-with-new-assurance-marketplace

**深度好文**

1、合规运营：视角转变带来的安全运营3.0时代 将重构行业价值

在网络安全监管趋严、攻防对抗智能化、企业数字化纵深推进的三重背景下，国内安全运营正经历一场底层逻辑的范式迁移。过去以攻防为核心、以合规为附属的传统思路已难以为继，以合规为底座、攻防能力为组件的全新运营框架正在成为行业共识。安全 419 观察到，一个全新的“合规运营”概念目前正悄悄浮出水面，而推动这一概念的北京小西牛认为，未来的安全运营即将进入到3.0时代。

# 原文链接：

[合规运营：视角转变带来的安全运营3.0时代 将重构行业价值](https://mp.weixin.qq.com/s?__biz=MzUyMDQ4OTkyMg==&mid=2247553019&idx=1&sn=06effa47b649b25b2aba84045c7195cd&scene=21#wechat_redirect)

**2、**全球未来信息产业安全发展战略研究

随着信息安全深度融入未来信息产业发展，其已成为国民经济增长的关键引擎。当前，我国未来信息产业安全仍面临科学基础能力薄弱、核心技术存在短板、要素供给不足、安全产品缺乏国际竞争力等制约。为解决此类问题，首先，系统审视全球未来信息产业安全的发展格局，从宏观战略、关键能力及力量支撑3个维度，分析我国未来信息产业安全发展的现状与基础；其次，围绕“传统产业的未来化跃升、未来技术的产业化落地”这一主线，进一步从产业安全发展主体、产业安全发展动力、产业安全发展基础和信息安全行业保障4个方面，给出了相应的对策建议，以期为未来信息产业安全发展提供路径参考。

原文链接：

[产业研究｜全球未来信息产业安全发展战略研究](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247604753&idx=1&sn=3ef617e96b8fe8c39b7a8fe74f82fda1&scene=21#wechat_redirect)

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