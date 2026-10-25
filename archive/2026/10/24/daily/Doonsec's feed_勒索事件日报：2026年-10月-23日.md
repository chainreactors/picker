---
title: 勒索事件日报：2026年-10月-23日
url: https://mp.weixin.qq.com/s/HTIXJDsXHcmo4K8SOG3xlg
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:59.738949
---

# 勒索事件日报：2026年-10月-23日

# 勒索事件日报：2026年-10月-23日

原创

MasterC
MasterC

企业安全实践

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

导读

10月23日公开勒索事件43起，18个团伙出手，欧洲18起反超北美12起。Qilin单日11起领跑，Whitearmor首秀即拿下惠而浦与JB Hunt，4个新团伙同日冒头。

## 一、勒索数据概述

2026年10月23日（UTC），全球勒索软件泄露站公开新增受害者条目**43起**，涉及**18个攻击团伙**、**20个国家与地区**，另有2条未标注国别。这是近十个自然日的第三高位，前两位是10月16日的74起与10月15日的45起；相比10月22日的30起，单日环比增幅约**43%**。

数量之外，当天更值得警惕的是**区域结构被改写**。按ransomware.live站点自身标注口径，前三依次是美国8起、西班牙4起、德国3起，北美依旧领先；但逐条按名称与域名核实后，真实分布是**欧洲18起、北美12起、拉美4起、亚太4起、中东与非洲3起**——欧洲首次明显反超北美。站点国别字段的缺失（20条中有5条无旗标）会系统性地低估欧洲与亚太，做区域判断时不能直接取字段。

披露节奏同样极端：43条里只有**4条**能回溯到明确的攻击日期，其余39条的攻击预估日与披露日同为10月23日。这4条中，Whirlpool 为10月21日攻击、10月23日曝光，Fresh Farms 为10月20日攻击；而英国 ADL Lift Services 与意大利 Zena Office 两条同属 Auditteam，攻击日均为**10月13日**，潜伏期长达10天。即攻即挂已成主流，但仍有团伙在做长周期经营。

## 二、被攻击单位分析（受害者清单）

以下为10月23日全部43条公开条目。本日清单中出现**1个中国台湾主体**。清单中另有2条为站方自身脱敏条目（Ca**ka、R****b R**-L\*\*），非本地处理。

| 受害者 | 团伙 | 国家/地区 | 行业 |
| --- | --- | --- | --- |
| Hensel Elektrik | Deadlock | 德国 | 电气设备制造 |
| Sanders Law Group | Rhysida | 美国 | 法律服务 |
| Miljaus Producciones S.L | Qilin | 西班牙 | 未分类 |
| von Schaewen | Qilin | 德国 | 未分类 |
| Le Tampon 市政府（留尼汪） | Qilin | 法国 | 政府与公共服务 |
| Company #110 | N0n | 西班牙 | 智能电网工程 |
| Mickey Truck Bodies | Chaos | 美国 | 卡车车身制造 |
| ARX Group SA | Aurora | 瑞士 | 工程咨询 |
| whitearmor.cc | Whitearmor | 未标注 | 团伙自建站点 |
| Dorsia Academy | Lockbit5 | 意大利 | 教育与培训 |
| Mount Lebanon Hospital | Lockbit5 | 黎巴嫩 | 医疗健康 |
| Lido Boutique Hotel | Lockbit5 | 列支敦士登 | 酒店与接待 |
| Zelsior | Lockbit5 | 西班牙 | 债务催收与法律 |
| JS Contractor Inc. | Emperador | 美国 | 人力资源与劳务 |
| Whirlpool（惠而浦） | Whitearmor | 美国 | 家电制造 |
| J.B. Hunt | Whitearmor | 美国 | 运输与物流 |
| Labaid Cancer Hospital | Qilin | 孟加拉国 | 医疗健康 |
| Kale Balata | Qilin | 土耳其 | 汽车零部件制造 |
| MaxiSeguridad | Qilin | 阿根廷 | 未分类 |
| Aryza | Qilin | 阿根廷 | 未分类 |
| Aerotop | Qilin | 智利 | 未分类 |
| CDG Chartered Accounting | Qilin | 澳大利亚 | 会计与专业服务 |
| Revi Group | Qilin | 墨西哥 | 未分类 |
| Bankruptcy Software Specialists | Akira | 美国 | 破产信托软件 |
| Bravilor Bonamat | Akira | 荷兰 | 咖啡设备制造 |
| SCHWAB-SYSTEM | Akira | 德国 | 木结构建筑 |
| Wah Chan Consolidated | Orova | 马来西亚 | 珠宝零售 |
| T**\* T**\*\*（中国台湾，名称已脱敏） | Orova | 中国台湾 | 科技 |
| R**b R**-L\*（站方脱敏） | Doommageddon | 未标注 | 未公开 |
| Don Pickett & Associates | Sarcoma | 美国 | 未分类 |
| VinSolutions | Scarlettgroup | 美国 | 汽车零售软件 |
| ADL Lift Services Limited | Auditteam | 英国 | 电梯工程服务 |
| Zena Office | Auditteam | 意大利 | 办公设备与IT |
| Ca*\**ka（站方脱敏） | Auditteam | 西班牙 | 未公开 |
| Line2Line Coatings | Rhysida | 美国 | 工业涂层制造 |
| Fresh Farms | Pear | 美国 | 食品分销 |
| EMARKETER | Fulcrumsec | 美国 | 市场研究 |
| Horn of Africa 区域环境中心网络 | N0n | 埃塞俄比亚 | 国际环保NGO |
| Prism Medical Products | Wallstreet | 美国 | 医疗耗材 |
| PROTEX Confection | N0n | 突尼斯 | 纺织制造 |
| SunTechnics Fabrisolar AG | N0n | 瑞士 | 太阳能工程 |
| B2Chat | Emperador | 西班牙 | 企业通信平台 |
| Coop Italia | Qilin | 意大利 | 零售与商超 |

当天最重的一击来自**Whitearmor**：这家从未出现过的团伙在首日同时挂出**Whirlpool（惠而浦，NYSE: WHR）**与**J.B. Hunt（北美头部多式联运物流商）**两家上市企业，外加自己的清网域名 whitearmor.cc。新团伙冷启动直接对准世界级品牌，指向性极强。

Qilin 的11起里藏着另一个高价值目标：**Coop Italia（意大利最大零售合作社之一）**。此外，黎巴嫩山医院（Mount Lebanon Hospital University Medical Center）、孟加拉 Labaid 肿瘤医院与超级专科中心两家医疗机构同日上榜，属于典型的**高社会敏感度目标**。留尼汪勒唐蓬市政府（Le Tampon）则是当天唯一的政府主体，公开描述为空，但域名与WHOIS记录已将其指向地方政府基础设施。

## 三、行业维度分析

按行业归并后，**专业服务与制造业同为8起（各18.6%）**并列第一，另有11起因公开描述缺失或过短无法归类。**未分类的11起中有6起来自 Qilin**——该团伙对这6条只给名称不给描述，说明它追求的是挂牌数量与谈判覆盖面，而不是逐个精细化经营。

**专业服务的8起**涵盖律所（Sanders Law Group）、工程咨询（ARX Group SA）、债务催收（Zelsior）、破产信托软件（Bankruptcy Software Specialists）、特许会计师（CDG Chartered Accounting）、人力资源（JS Contractor）、市场研究（EMARKETER）与电梯工程服务（ADL Lift）。这类机构的共性很明确：**自身数据未必值钱，但手上握着几十上百家客户的数据**。Sanders Law Group 一家就被拖走约8TB、450万份文件，内含12,803份客户完整信用报告、20,106份W-9/1099税表，以及2,342份带保密条款的已签署和解协议。打一家律所，等于同时拿到它所有客户的把柄。

**制造业的8起**集中在高价值细分环节：卡车车身（Mickey Truck Bodies）、刹车片（Kale Balata）、家电（Whirlpool）、工业涂层（Line2Line Coatings）、咖啡设备（Bravilor Bonamat）、木结构（SCHWAB-SYSTEM）、纺织（PROTEX Confection）、电气设备（Hensel Elektrik）。其中 Kale Balata 与 Line2Line 均处于汽车供应链上，Line2Line 的泄露清单里直接点名了 Eaton、通用、克莱斯勒、本田研发、水星海事等下游客户——**供应链上下游的身份，本身就是谈判桌上最重的筹码**。

**医疗健康3起**（黎巴嫩山医院、Labaid 肿瘤医院、Prism Medical Products），**科技4起**（VinSolutions、Zena Office、B2Chat 与中国台湾的 T**\* T****）。科技类目标的共同点在于它们多为**服务众多下游客户的平台型产品\*\*：VinSolutions 是汽车经销商 CRM，B2Chat 是多渠道客服平台——敲开一个平台，就能连带触及它背后的全部客户群。

## 四、区域维度分析

**欧洲18起（41.9%）**是当天绝对的震中，且分布极散：西班牙5、德国3、意大利3、瑞士2、法国1、荷兰1、英国1、列支敦士登1、土耳其1。跨度从上市公司的零售巨头到列支敦士登的精品酒店，说明攻击并不挑选经济体量，而是在**按暴露面随机推进**。法国那一起需特别说明：Le Tampon 位于印度洋留尼汪，属法国海外省，虽计入法国，但实质是地方政府基础设施。

**北美12起（27.9%）**全部在美国，仍是单一国家里体量最大的受害者来源。值得注意的是，美国目标中大企业占比明显高于其他地区——Whirlpool、J.B. Hunt、EMARKETER、VinSolutions 都是有全国性知名度的品牌。攻击者对美国目标的判断逻辑很清楚：**品牌知名度与合规披露压力，直接等于支付意愿**。

**拉美4起**（阿根廷2、墨西哥2、智利1中计入2起）与**亚太4起**（澳大利亚、孟加拉国、马来西亚、中国台湾各1）。亚太这一天的特征与欧洲相反，全部是单点命中且行业分散：会计、肿瘤医院、珠宝零售、科技。亚太统计口径长期偏低，与区域内披露机制不完善有关，实际发生率大概率被低估。

**中东与非洲3起**（黎巴嫩、突尼斯、埃塞俄比亚各1），其中埃塞俄比亚的 Horn of Africa 区域环境中心网络是一家国际环保NGO，被 N0n 拖走了完整的 SAP Business One 生产数据库。 NGO 通常防护预算最薄，但持有的跨国项目与捐助方数据并不少，正在成为勒索团伙新的低成本目标。另有**2条未标注国别**，做区域统计时不应直接忽略。

## 五、攻击团伙分析（团伙分布）

| 团伙 | 起数 | 占比 | 状态 |
| --- | --- | --- | --- |
| Qilin | 11 | 25.6% | 高度活跃，跨11国批量挂出 |
| N0n | 4 | 9.3% | 活跃，含1条匿名倒计时条目 |
| Lockbit5 | 4 | 9.3% | 活跃，欧非中东四线作业 |
| Akira | 3 | 7.0% | 活跃，美德荷三地制造业与专业服务 |
| Whitearmor | 3 | 7.0% | 新团伙，首日即打两家上市巨头 |
| Auditteam | 3 | 7.0% | 活跃，含1条脱敏条目，潜伏期达10天 |
| Rhysida | 2 | 4.7% | 活跃，数据清单式挂牌 |
| Emperador | 2 | 4.7% | 新团伙，西班牙与美国双线 |
| Orova | 2 | 4.7% | 低频，东南亚与东亚 |
| Deadlock | 1 | 2.3% | 低频 |
| Chaos | 1 | 2.3% | 低频 |
| Aurora | 1 | 2.3% | 新团伙，瑞士工程咨询 |
| Doommageddon | 1 | 2.3% | 新团伙，仅公布倒计时不公布内容 |
| Sarcoma | 1 | 2.3% | 新团伙，美国本土 |
| Scarlettgroup | 1 | 2.3% | 低频 |
| Pear | 1 | 2.3% | 低频 |
| Fulcrumsec | 1 | 2.3% | 低频 |
| Wallstreet | 1 | 2.3% | 低频 |

**Qilin 以11起（25.6%）继续领跑**，且是全球扫射式打法：一天内横跨美国、德国、西班牙、意大利、法国、阿根廷、智利、墨西哥、澳大利亚、孟加拉国、土耳其11个国家。这个体量已经不是单点突破能支撑的，背后是成熟的 RaaS 附属网络在并行作业。它的弱点也很明显——11条里6条没有描述、只挂名字，说明**运营重心在数量而不在情报质量**，对防守方来说，Qilin 条目的内容威胁反而相对可控。

**当天最值得盯的是 Whitearmor**。它同时被站方标记为新团伙，首日上榜3条，其中两条是 Whirlpool 与 J.B. Hunt。新团伙冷启动就打上市巨头，通常只有两种解释：要么是老牌团伙换皮重开，要么是在用高知名度目标做**造势式亮相**——先立威，再谈钱。对这类团伙的归因应保持保留态度，基础设施复用、泄露站互借在勒索生态里是常态。

**当天共有4个团伙首次出现：Whitearmor、Emperador、Aurora、Sarcoma**，合计出手7起，占全天的16.3%。Emperador 打的是西班牙的 B2Chat 与美国的 JS Contractor，Aurora 打瑞士工程咨询 ARX Group，Sarcoma 打美国本土的 Don Pickett & Associates——四个新团伙的目标选择没有交集，不像同一批基础设施在分身。

长尾同样醒目：18个团伙里有**7个当天只出手1次**。Qilin 一家占25.6%，但前四名合计才51.2%，说明**头部集中度并不高**，勒索生态仍在持续碎片化。对防守方而言，这意味着跟踪单一团伙的战术收益正在下降。

## 六、攻击手法分析

•︎ **数据清单式挂牌成为主流话术。** Rhysida 把两起目标的家底逐项摊开：Sanders Law Group 是8TB、450万份文件、2005至2026年的完整沿革，含33个PST邮件归档（约120GB）、2,479个邮箱转储、全量 ARES 案件管理库（30,671起案件，单案和解上限400万美元）；Line2Line Coatings 是79.6万文件、641GB，含34个邮箱、1,232份 QuickBooks 备份、3,614个社保号、64,907份含PII的文件。这不是炫耀，是**用可核验的细节把谈判对手逼到墙角**。

•︎ **「预告—倒计时—曝光」三段式流程化。** Akira 在 Bankruptcy Software Specialists 条目里直接写明「即将上传19GB企业数据」；Doommageddon 对脱敏目标只给一个倒计时——最后期限2026-10-25T12:00:00Z，内容一字不提。攻击者连内容都不需要透露，光靠最后期限就足够制造决策压力。

•︎ **匿名占位与实名曝光是同一批目标的两个阶段。** N0n 的 Company #110 标记为 PENDING EXPOSURE，描述里已写明「西班牙智能电网工程公司」，但名称保留匿名。结合长期观察，这类匿名条目通常在**1至2天内转为实名**——匿名期是防守方唯一还能低成本处置的窗口。

•︎ **专业服务机构的目录与财务系统是主攻点。** Sanders Law Group 被拖走的是完整案件管理数据库、IOLTA 律师信托账户流水、电汇指令、合伙税表与全量 HR 档案；B2Chat 泄露的是员工姓名、邮箱、电话以及客户与合作伙伴数据。攻击者很清楚，这些数据一旦公开，受害者面对的就不只是赎金，而是**客户追责与监管问责**。

•︎ **暴露面情报暴露了初始入口的成色。** ParanoidLab 对三条 Qilin 目标的扫描显示：von Schaewen 有**68个密码**、4个cookie；Miljaus Producciones 有**17个密码**；Le Tampon 市政府有**3个密码且全部为高危**，另有40个cookie。密码数量不算惊人，但「3个里3个高危」这种比例说明口令质量极差，是凭证填充与密码喷洒的标准猎物。

•︎ **攻击面已经延伸到 AI 与 SaaS 层。** von Schaewen 的 DNS TXT 记录里赫然有一条 Anthropic 域名验证记录，同时整域跑在 Microsoft 365 上；Le Tampon 使用 Google Workspace 与 GlobalSign。勒索团伙现在的入口清单里，云邮箱、协作套件、乃至新接入的 AI 工具都在其中——而这些往往不在传统 EDR 与边界防护的视野内。

## 七、攻击动机分析

•︎ **财务勒索仍是主线，但赎金只是收入的一部分。** 43条里明示金额的一条都没有，取而代之的是容量与期限：Akira 预告19GB、Rhysida 摆出8TB、Doommageddon 只给最后期限。收益结构已经固化为「赎金 + 数据二次售卖 + 下游钓鱼诈骗」三件套，受害者不付钱，攻击者照样能变现。

•︎ **连带施压的收益高于直接勒索。** Emperador 在 B2Chat 的条目里直接写明：如果不付赎金，将主动联系并攻击其员工、客户与合作伙伴，摧毁其业务。Line2Line 的清单里点名了 Eaton、通用、克莱斯勒、本田研发等下游客户——**攻击者的真正目标不是受害者的钱包，而是受害者下游关系的延续性**。

•︎ **合规与声誉是最有效的杠杆。** Sanders Law Group 被点名拖走了1,315份该律所自身的制裁与纪律文件、含保密条款的2,342份和解协议，以及律所自己负有保密义务的客户信用报告。攻击者挑这些文件，是因为它们一旦公开，会直接触发律师执...