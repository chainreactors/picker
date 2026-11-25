---
title: 勒索事件日报：2026年-11月-23日
url: https://mp.weixin.qq.com/s/Zz8dbVJhQAD5lQbVPKt4dA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:46:03.703049
---

# 勒索事件日报：2026年-11月-23日

# 勒索事件日报：2026年-11月-23日

原创

企业安全实践
企业安全实践

企业安全实践

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

导读

11月23日新增62起、19团伙，反弹195%但过半为匿名占位与域名扫街；中资纺织机械集团540GB财务与研发全量被端，insomnia当日首秀，Ipsos六万余口令与FortiBleed暴露并列。

## 一、勒索数据概述

2026年11月23日（UTC 自然日）勒索软件曝光站新增 **62 起**受害者挂牌、涉及 **19 个**团伙，数据截至 2026-11-24 00:10 UTC。两轮首页抓取与两轮 summary 页逐条枚举完全吻合：面板「过去 24 小时」计数 64，其中 2 条（VHV Company、Home Instead，anubis 团伙）为 11 月 24 日凌晨刚挂、攻击日也标 11 月 24 日，剔除后 11 月 23 日单日恰为 62 起，62 + 2 = 64 口径闭合，无重复条目、无占位空槽。

近十一日序列为 11-13 的 19 起、11-14 的 18 起、11-15 的 31 起、11-16 的 107 起、11-17 的 57 起、11-18 的 69 起、11-19 的 74 起、11-20 的 46 起、11-21 的 24 起、11-22 的 21 起、**11-23 的 62 起**。较前一日反弹 **195%**，面板给出的环比是 **+205%**，连续三日回落后的一次暴力拉升，量级回到 11-18 的 69 起、11-19 的 74 起那一档。

但这次起数反弹的成色要打折。62 起里，**N0n 的 25 条匿名连号条目（Company #244 至 #268）占了 40.3%**，safepay 的 9 条纯域名扫街占 14.5%，两者合计 34 起、**54.8% 属批量占位而非独立事件**；剔除之后真正带企业名、可读描述的挂牌只剩 28 起，与 11-22 的 21 起仍是同一量级。**起数在跳，实际攻势没有同步跳**，这是读今天数据最该先立住的判断。

真正压分量的是一单 540GB 的全量泄露：一家中资控股的全球纺织机械集团被 aurora 一次端掉两台德国文件服务器，未公开年报草案、实时现金头寸、八家银行签字权、审计底稿与 63GB 纺机研发资料同时外流。数量与分量的背离，本周又出现了一次。

## 二、被攻击单位分析（受害者清单）

62 家单位可以分成五堆：**N0n 的 25 条匿名连号占位**、**safepay 的 9 条纯域名扫街**、**qilin / aurora / spacebears 各自成组的企业挂牌**、**insomnia 的康涅狄格市政双连**，以及其余单点。前三堆是同一团伙的成批动作，后两堆才需要逐条读。

| 受害者 | 团伙 | 国家/地区 | 行业 |
| --- | --- | --- | --- |
| Nationwide IT Services, Inc. | rhysida | 美国 | 专业服务 |
| Toyota Chihuahua | qilin | 墨西哥 | 制造 |
| Yahoo（yahoo.com.br） | medusalocker | 巴西 | 科技 |
| Golden State Baptist College | Dark Project | 美国 | 教育 |
| Quetico LLC | aurora | 未标注 | 未标注 |
| Kopron S.p.A. | aurora | 意大利 | 制造 |
| 某纺织机械企业（名称已脱敏） | aurora | 中国 | 制造 |
| Lowell Foods | incransom | 未标注 | 农业与食品 |
| Jager Management Inc. | qilin | 美国 | 专业服务 |
| Ipsos | qilin | 法国 | 专业服务 |
| Connecticut Interlocal Risk Management Agency | insomnia | 美国 | 政府与国防 |
| Connecticut Conference of Municipalities | insomnia | 美国 | 政府与国防 |
| AMI Mechanical Corp | Eclipse | 美国 | 制造 |
| Demas Schaefer Family Lawyers | rhysida | 未标注 | 专业服务 |
| obriengroupaustralia.com.au | lockbit5 | 澳大利亚 | 专业服务 |
| traconelectric.com | safepay | 未标注 | 制造 |
| sinagpawnshop.com | safepay | 菲律宾 | 零售电商 |
| bienefeld-gmbh.de | safepay | 德国 | 制造 |
| elsanj.org | safepay | 未标注 | 未标注 |
| jcatkinson.co.uk | safepay | 英国 | 专业服务 |
| hlbtropical.com | safepay | 德国 | 农业与食品 |
| spiegelberg.com | safepay | 德国 | 专业服务 |
| paisarnmetal.com | safepay | 泰国 | 制造 |
| interprint.es | safepay | 西班牙 | 制造 |
| PSS-Socotherm S.A | qilin | 未标注 | 制造 |
| Aurora Cannabis | osiris | 加拿大 | 零售电商 |
| Yara Sanat Ilia（伊朗螺杆压缩机制造商） | PixelLeaks | 伊朗 | 制造 |
| University Medical Imaging | Aoqin | 美国 | 医疗健康 |
| Corrigan Moving Systems | Aoqin | 美国 | 交通运输 |
| kinkisharyo.com | everstake | 日本 | 制造 |
| PIMENT INTERIM（GROUPE PIMENT） | spacebears | 法国 | 专业服务 |
| MASTER RESULT SOLUÇÕES CONTÁBEIS LTDA | spacebears | 巴西 | 专业服务 |
| Digital Instruments & Control Systems (DICS) | spacebears | 未标注 | 科技 |
| Staufen Baumaschinen GmbH | spacebears | 德国 | 制造 |
| www.suzlon.com | blackout | 印度 | 制造 |
| FULL RELEASE — CLINIC SAGRADA FAMILIA 等四家诊所 | Whitearmor | 哥伦比亚 | 医疗健康 |
| Fisher & Paykel Healthcare | Falcon | 新西兰 | 医疗健康 |
| Company #268（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #267（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #266（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #265（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #264（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #263（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #262（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #261（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #260（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #259（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #258（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #257（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #256（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #255（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #254（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #253（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #252（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #251（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #250（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #249（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #248（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #247（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #246（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #245（N0n 匿名） | N0n | 未标注 | 未标注 |
| Company #244（N0n 匿名） | N0n | 未标注 | 未标注 |

那家中资纺织机械集团是当日唯一需要逐字读的通告。aurora 挂出的是 **540GB、两台德国企业文件服务器的全量镜像**：HR 侧有瑞士实体 2023—2025 年工资单（含 AHV 社保号、养老金与税务）、高管雇佣合同薪酬条款、英国子公司 2024—2026 年薪资与一份产假证明（GDPR 第 9 条特殊类别健康数据）、德国职工委员会 2026 年 4 月生效的工资表与短时工协议；财务侧是 **2025 年 HGB 法定年报未公开草案**、63MB 实时现金头寸主文件、德银 / UBS / Helaba / OLB / DZ / BHF / Bank CIC 等八家以上银行的账户总览与签字授权、MT940 电子对账单、33MB 投资者 factbook、Deloitte 转让定价文档、2016—2025 全套 HGB 账目与 PwC 审计底稿；工程侧是 **63GB 以上 AUTOCORO 转杯纺纱机研发资料**（含代号项目 101\_Luchs、102\_01\_Gecko）、SolidWorks CAD 模型、EPLAN P8 电气原理图、68 个以上 MDESIGN 机械设计库；另有 73 个 Outlook PST（覆盖 25 个以上客户国）与 AS400 订单、应收应付、总账的月度导出。一家中国上市主体、瑞士总部、德英印中多国子公司，被一次平推到同一份目录里，**共享盘权限过宽与跨国目录统一身份**是这单最刺眼的两处结构性缺陷。

Ipsos 那条则相反，描述只有 N/A，但取证栏厚得反常：ParanoidLab **61,552 个口令（1,721 个 critical）**、650 个 Cookie，HudsonRock **136 名员工、904 个用户、268 条第三方凭据**，外部攻击面 **196**，并明确标注 FortiOS SSL-VPN 凭据已在 FortiBleed（CVE-2022-40684）与 2026 年 10 月的 FortiBleed 2.0 两次泄露中流出；DNS TXT 里堆着 OpenAI、Anthropic、Atlassian、Docker、DocuSign、Figma、MongoDB、Zoho、Proofpoint、Microsoft 365、Amazon SES 等几十条 SaaS 域名验证串。**没放料，不代表没打穿**。

Yahoo 与 Toyota Chihuahua 是另一种极端。前者域名 yahoo.com.br，描述仅「1511 个邮箱被抽取」，口令 0、Cookie 0、无任何 SaaS 命中；后者描述 N/A，0 口令、8 个 Cookie，只识别到 Brevo 一个服务，SPF 指向单一 IP。**全球品牌名配近乎空白的证据栏**，挂牌的是名字不是数据，读的时候要按「借势」而不是「失陷」处理。

## 三、行业维度分析

**制造业 13 家（21.0%）居首**，而且不是零散命中：Toyota Chihuahua、Kopron、脱敏的纺织机械集团、AMI Mechanical、traconelectric、bienefeld、paisarnmetal、interprint、PSS-Socotherm、伊朗 Yara Sanat Ilia、日本 kinkisharyo、德国 Staufen、印度 suzlon，横跨欧亚拉美，从汽车、纺机、金属加工到风电与铁路车辆。这个分布与站点 30 天口径里制造业 176 起、环比 +8% 的结论一致，但当日更值得注意的是**制造业被拿走的东西变了**——不再是名单和发票，而是 CAD 模型、电气原理图、机器参数、代号研发项目与未公开年报。工程 IP 与财务内幕信息正在成为同一份勒索包里的双重筹码。

**专业服务与法律 9 家（14.5%）**排第二，Ipsos、Jager Management、两家律所、澳洲 O'Brien 集团、英国 jcatkinson、德国 spiegelberg、法国 PIMENT INTERIM、巴西 MASTER RESULT，覆盖市场调研、管理咨询、家事法律、人力派遣与会计事务所。这类机构自身数据未必值钱，但手里握着客户名册、合同与 NDA，是横向进入下游的跳板。

医疗健康 4 家、政府与国防 2 家、农业食品 2 家、科技 2 家、零售电商 1 家、教育 1 家、交通运输 1 家，另有 **27 家未标注（43.5%）**，其中 25 条是 N0n 匿名条目。未标注占比接近一半，本身就在提醒：今天的行业结论只能覆盖可核实的实名条目，不能拿站点行业标签去推全量结构。

## 四、区域维度分析

按名称、域名与描述原文逐条核实（不直取站点旗标），62 起的区域分布如下：

•︎ **北美 11 家（17.7%）**：美国 9 家、加拿大 1 家（Aurora Cannabis）、墨西哥 1 家（Toyota Chihuahua）。康涅狄格两家市政机构同日成对上榜是本节最该看的信号。

•︎ **欧洲 9 家（14.5%）**：德国 4 家、法国 2 家、意大利 1 家、英国 1 家、西班牙 1 家。德国占比偏高主要由 safepay 的域名扫街贡献，不是真实攻势倾斜。

•︎ **亚太 7 家（11.3%）**：中国 1 家（已脱敏）、日本 1 家、印度 1 家、泰国 1 家、菲律宾 1 家、澳大利亚 1 家、新西兰 1 家。**中国内地 1 家、港澳 0 家、中国台湾 0 家**。

•︎ **拉美 3 家（4.8%）**：巴西 2 家、哥伦比亚 1 家。

•︎ **中东北非 1 家（1.6%）**：伊朗 Yara Sanat Ilia，条目直接点名 Sepidar ERP 资产。

•︎ **未标注 31 家（50.0%）**：N0n 的 25 条匿名条目，加上 6 个无旗标、无可核实地域的 .com / .org 域名。

站点 30 天地图口径给出美国 523、德国 63、加拿大 55、英国 50，只统计带旗标、带描述的条目。当日逐条核实后，**欧洲与亚太被系统性低估**：safepay 9 条里只有 4 条挂了旗标，spacebears 4 家横跨法国、巴西、德国全无旗标，日、印、泰、菲、新西兰五国靠域名与名称才认得出来。区域判断必须回到条目原文，这一点本周已反复验证。

## 五、攻击团伙分析（团伙分布）

| 团伙 | 起数 | 占比 | 状态 |
| --- | --- | --- | --- |
| N0n | 25 | 40.3% | 匿名连号占位，待转实名 |
| safepay | 9 | 14.5% | 纯域名扫街，老团伙复现 |
| qilin | 4 | 6.5% | 活跃，跨欧美拉美 |
| spacebears | 4 | 6.5% | 跨洲极简挂牌 |
| aurora | 3 | 4.8% | 当日最重一单（540GB） |
| rhysida | 2 | 3.2% | 律所与 IT 服务定向 |
| insomnia | 2 | 3.2% | **当日首秀** ，甩近四周库存 |
| Aoqin | 2 | 3.2% | 医疗与搬运 |
| medusalocker | 1 | 1.6% | 极简挂牌 |
| Dark Project | 1 | 1.6% | 单点 |
| incransom | 1 | 1.6% | 单点 |
| Eclipse | 1 | 1.6% | 单点 |
| lockbit5 | 1 | 1.6% | 单点 |
| osiris | 1 | 1.6% | 单点 |
| PixelLeaks | 1 | 1.6% | 单点 |
| everstake | 1 | 1.6% | 单点 |
| blackout | 1 | 1.6% | 单点 |
| Whitearmor | 1 | 1.6% | 哥伦比亚诊所续报兑现 |
| Falcon | 1 | 1.6% | 单点 |

**前五家合计 45 起、占 72.6%**，集中度很高，但头部两家都是占位型产能，不能读成两个团伙当天打了 34 家。

近两周稿件逐名核对后，**19 家里只有 insomnia 是当日真首秀**：2 起全打康涅狄格市政体系（CIRMA 市政风险池与其上级的市政联盟 CCM），攻击估算日统一回填到 **10 月 26 日**，描述直接复制官网「四十余年前由 CCM 创立、康州最大的市政风险融资与理赔服务机构」，没有数据样本、没有倒计时——**首秀即甩近四周库存、用官网简介代替证据**，是典型的立信誉动作而非当日攻势。站点给 Aoqin、PixelLeaks、everstake 挂了 New 徽章，但这三家首秀分别在 11 月初与 11 月上旬，近两周稿件里命中 8 至 9 次、3 次、9 次，**徽章只反映站点收录时间，不能当首秀依据**。

Whitearmor 那条是 11 月 21 日哥伦比亚四家诊所「DROP 1」的续报，标题直接写 FULL RELEASE，从分阶段放料走到全量公开，谈判周期能看到完整节奏。

## 六、攻击...