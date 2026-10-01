---
title: 一个80年代的反毒项目，如何把全美车牌数据汇成联邦监控库
url: https://mp.weixin.qq.com/s/_vVIIQjXno24e2-50Inp5w
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:14.711084
---

# 一个80年代的反毒项目，如何把全美车牌数据汇成联邦监控库

# 一个80年代的反毒项目，如何把全美车牌数据汇成联邦监控库

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

美国路边的小摄像头越来越多，高架桥、红绿灯、学校门口，它们读下车牌，也记下时间地点。数据随后去了哪里？多数人并不清楚，以为这些记录只在本地警局里转一圈。多个境外媒体调查报道显示，从公开记录和法庭文件中还原了一条隐蔽的数据通道：美国正用一个诞生于上世纪80年代的反毒拨款项目，把各地城市持续收集的车牌识别数据，强制汇入白宫管辖的大型联邦监控中心。

# HIDTA：一个“反毒项目”如何变成数据管道

这套系统的起点，是一个叫HIDTA（High Intensity Drug Trafficking Area，高密集毒品贩运区）的拨款项目，官方定位是“多辖区公共安全项目”，为全国各地的HIDTA情报中心和其他缉毒行动提供资金。全美共有33个HIDTA项目，覆盖全部50个州；HIDTA情报中心类似但又独立于政府的fusion center（融合中心），后者是地方、州、联邦执法机构之间共享监控数据的平台。

每个HIDTA情报中心由executive board（执行委员会）管理，成员大多是执法官员和政府律师，这种结构也带来一个现实问题：谁也说不清某个HIDTA收集的数据到底归谁管？HIDTA隶属于白宫下属的ONDCP（Office of National Drug Control Policy，国家药物管制政策办公室），这个办公室常被称作“drug czar”（缉毒沙皇），它此前资助过一个名为Hemisphere（半球计划）的通话记录数据库，收集了超过一万亿条AT&T通话记录和定位数据。部分汇入HIDTA的数据，还会继续流向一个更大的项目，即DEA（Drug Enforcement Administration，美国缉毒局）运行的NLPRP（National License Plate Reader Program，国家车牌读取器项目）。

就在今年4月，白宫还向HIDTA颁发了奖项，休斯顿HIDTA的表彰理由中写着“管理一个汇集了各级执法力量的车牌读取器平台”，这是公开记录里少见的、官方对这套车牌数据系统的直接背书。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqrRoqGFMqw0wmKbpiaxiavS7dddvf21793UztLZjRcNcmHKGPD0cEBQZt8LEUyoXA8cUcicB65oYFgtiagO7d6NJm0cZibn3u0bbGY/640?wx_fmt=png&from=appmsg)

# 不签协议，摄像头装不上路

这套系统最精巧也最麻烦的地方在于，城市想装摄像头，先得签协议。佐治亚州的规定最具代表性：任何ALPR（Automated License Plate Reader，自动车牌识别）摄像头，要装在州属道路的路权范围（right of way）内，必须与HIDTA签署MOU（memorandum of understanding，谅解备忘录），承诺把数据送给HIDTA。

今年早些时候，佐治亚州布伦瑞克市（Brunswick）就撞上了这道门槛。该市想部署Axon的车牌摄像头，却发现必须先与亚特兰大地区的HIDTA签约，协议写得很直白，要“促进其电子数据系统中的信息共享，包括但不限于自动车牌读取器和执法数据共享系统，可能包含从多个个体或区域来源收集的聚合信息”，并汇入“商业化及定制开发的数据整合系统”。说白了，MOU意味着城市收集的ALPR数据必须汇入HIDTA，其他执法机构随后可以通过聚合多家公司数据的软件调取这些记录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpCRic8WlRWiax2bD6bt9lNzooH2f37x539o6lsnEugVhKia53qRPpnaZSR53njjzcOwyTryNDDhbHJiasazBhYKFNCZXibRgxibeL8A/640?wx_fmt=jpeg)

布伦瑞克市议会会议资料包中的说明

Flock官网甚至专门为佐治亚执法机构开设了合规页面，页面写明：在GDOT（Georgia Department of Transportation，佐治亚州交通部）路权内安装或运营摄像头的机构，必须与HIDTA签署MOU，才能符合佐治亚州警察的新政策；协议签完后，GDOT路权摄像头读取的车牌，会通过Flock界面向佐治亚州的HIDTA国家车牌系统用户开放。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpIY31MMlmFsRlRwVTznBDxib1eEuZU3sicAZ99JcTFKvRPtz9wVIkBSLFmhHibUEybf3AXNJtMlDwW32WF6cnA8rpFeQeB0e2Eq4/640?wx_fmt=jpeg)

Flock为佐治亚州执法机构设置的合规页面

全美有几十个HIDTA，到底有多少辖区在往数据库里送数据，报道给出的答案是“不清楚”。404 Media看到的全国HIDTA系统登录门户，运营方是休斯顿HIDTA。堪萨斯州公路巡逻队的一份演示文稿，把运作细节摆在了明面上：摄像头读到车牌后，数据被传送到位于休斯顿HIDTA、达到CJIS（Criminal Justice Information System，刑事司法信息系统）安全级别的服务器；数据保留6个月后删除，不可恢复；配套审计工具可以追踪用户的每一次查询；公开记录请求必须由公路巡逻队接收，再由休斯顿HIDTA判断数据是否受保护、能否对外公开。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpPxzzCQ6F2A95gEdptsA2B8XJV6NJhVDBiciaASTsvYq3mFqSrQLv1kx8Egicpl9OviceIGIfsc7TDXqynwibr25eNyvsyWwAm9Er4/640?wx_fmt=jpeg)

堪萨斯州公路巡逻队演示文稿截图

亚特兰大-卡罗莱纳HIDTA的谅解备忘录全文同样摆出了类似的规则：数据经加密VPN专线传至运营中心服务器，保留期不超过两年，到期清除；任何对外发布信息，都要求先验证接收方是否具备“need to know”（知悉必要）与“right to know”（知悉权利）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDr7dJtoP23iaRO58oJLFsg4r6GErtxbwN5p2uCW8o2TPFnDqoV36tR409SHRFy5x9G2LodSy05cPzPgBwSQicaefaNapEoVrXuc8/640?wx_fmt=jpeg)

亚特兰大-卡罗莱纳HIDTA谅解备忘录中的“数据共享”条款

# 30万美元，把各家厂商的数据“搬”进一个库

亚特兰大并非唯一在聚合车牌数据的HIDTA。休斯顿HIDTA曾支付306,800美元给一家名为Recruitful LLC的公司，用于“创建和维护一个LPR数据库”，也就是一个可以检索多家ALPR公司数据的搜索工具。合同的工作说明书写明，系统要把“第三方”数据整合进一个数据库，把地方实体的数据“迁移”或复制到中央数据库；换句话说，Flock、Axon、ELSAG、Vigilant等厂商摄像头采集的数据，都会在这个独立数据库里被检索，项目还列了一条硬性标准：“所有API和第三方集成（Unification Platform、FLOCK）在新环境中无缝运行。”

面对报道的置评请求，Flock和Axon没有回应；DEA表示自己对HIDTA没有管辖权，拒绝置评，连自家车牌系统与HIDTA如何交互都不愿谈；CBP（Customs and Border Protection，美国海关与边境保护局）和白宫ONDCP同样没有回应。

# DEA自己的评估，白纸黑字承认风险

2024年12月，DEA发布了一份关于NLPRP和DEASIL（DEA Special Intelligence Link，DEA特别情报链接）的隐私影响评估（Privacy Impact Assessment，PIA）。评估说明，DEA既运营自己的车牌读取设备，也通过HIDTA和其他“提供数据的执法机构”获取“非DEA设备”的数据；评估中写道：“这些提供数据的机构依据各自的MOU，将LPR数据传输至区域枢纽维护的服务器，这些数据可与NLPRP系统共享。”DEA还透露，它正在寻求与CBP的车牌摄像头系统整合。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoOlO6A4joCib6vKsg5iazrntiaeOr7FuDoiaKlGU2ZwtnTdJm7CmEk9YPZ6TNpI9ucKbgibwIqBs3xNdkibh4rzxyKHjkD2CvtKLsqs/640?wx_fmt=jpeg)

DEA国家车牌读取器项目隐私影响评估封面

更值得注意的是评估对风险的自我表述：系统“可能纳入数量庞大的其他政府LPR网络摄像头，或可能在未来获取足够大量的商业LPR摄像头数据，从而有效实现持续追踪个人行程，对个人隐私构成风险”，还“存在过度收集每个经过LPR摄像头位置的车牌个人可识别信息的风险，其中包含大量与刑事调查无关的守法司机的行程图像”。连运营方自己都承认，这套系统可能让每一个路过的守法司机，都变成被持续记录的对象。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDosBK5R2G5EHokZsVSrIKC3C9PPGftB6z4eTVRicjk773EiaIYY5LWt4wMvmoQkKlOMh4PrVQP1icEicXbk9oRzeyQQGdCZ4Mf4oZk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpaC0mW3PjnJ5RafsSIx4KTGiaOv9PichlR71C4cknENA7FFVAlBVvmNaH7Oel6XrdIDI1rmXCS4JDvDS9zDPz6VMVqsRHBHjaCk/640?wx_fmt=png&from=appmsg)

# 一个绕开公众监督的监控黑洞

数据进了这套系统，公众几乎无法查询和审计。部分地方辖区表示，他们的数据直接进入了HIDTA，而HIDTA不受FOIA（Freedom of Information Act，信息自由法）约束。北卡罗来纳州伦道夫县（Randolph County）警长办公室在回应公开记录请求时说，“所有数据都保存在联邦休斯顿HIDTA数据库”，无法与公众共享。

DEA甚至在法庭上抗辩，称HIDTA记录不受公共记录法约束，理由是它们是受“执行委员会”管理的复杂实体。奥巴马时期的白宫则把HIDTA描述为拨款项目而非实体，但这并不改变HIDTA们正与地方实体签署数据共享备忘录的事实。在一宗公民索要自己HIDTA记录的诉讼中，DEA律师这样写道：“在地方层面，HIDTA由执行委员会指导和引导，委员会由数量相等的联邦与非联邦（州、地方、部落）执法负责人组成……DEA不创建、不持有、不维护、不控制HIDTA项目记录，也不在其任何记录系统中存储这些记录。”

与此同时，资金还在加码。2026年7月，特朗普政府宣布向HIDTA追加2.77亿美元拨款，白宫称这是该项目历史上最大的一笔投入；33个区域HIDTA上一年共缴获410万磅芬太尼等毒品、追回5.763亿美元现金、让贩毒者损失216亿美元利润、协助逮捕4.2万名逃犯，白宫还给出一个回报数字：每投入1美元，收益82.78美元。

本文事实均来自以下公开来源，黑鸟已逐一查阅核实。感兴趣的读者可以按图索骥：

[1] 404 Media调查报道：How Cities Are Forced to Funnel License Plate Data to a Massive Federal Surveillance Program，Jason Koebler，2026年9月30日https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/。本报告核心事实出处，包含公开记录与法庭文件的完整引述。

[2] 亚特兰大-卡罗莱纳HIDTA谅解备忘录（全文PDF）https://cdn.muckrock.com/inbound\_request\_attachments/RandolphCountySheriffsOffice\_cLtyGqCx/218744/Atlanta-Carolinas\_High\_Intensity\_Drug\_Trafficking\_Area\_Memorandum\_of\_Understanding.pdf。2023年5月签署，含数据共享、加密VPN传输、两年保留期、审计要求、LPR项目政策与隐私规定全文。

[3] 白宫公告：追加2.77亿美元拨款（2026年7月9日）https://www.whitehouse.gov/releases/2026/07/white-house-announces-additional-277-million-to-fight-cartels-and-drug-traffickers/。项目历史上最大投入；含33个区域HIDTA上年战果统计与每1美元投入82.78美元收益的说法。

[4] 白宫ONDCP颁奖公告（2026年4月）https://www.whitehouse.gov/briefings-statements/2026/04/ondcp-honors-law-enforcements-role-in-fighting-against-drug-trafficking/。全国HIDTA颁奖典礼记录，休斯顿HIDTA因管理车牌读取器平台等受到表彰。

[5] DEA：国家车牌读取器项目（NLPRP）与DEASIL隐私影响评估（2024年12月）https://www.documentcloud.org/documents/28710394-dea-nlprp-pia/。DEA官方对NLPRP数据来源、区域枢纽共享机制及隐私风险的自我评估。

[6] Flock官网：佐治亚州GDOT路权合规页面https://www.flocksafety.com/gdot。明确要求GDOT路权内摄像头机构须与HIDTA签署MOU，LPR读取经Flock界面接入HIDTA国家系统。

[7] EPIC事实清单：数据解析服务项目（DAS，前身Hemisphere）https://epic.org/documents/fact-sheet-data-analytical-services-das-program-formerly-known-as-hemisphere/。超万亿条AT&T通话与定位记录、无司法监督、政府刻意保密的先例说明。

[8] 伦道夫县警长办公室公开记录请求（MuckRock）https://www.muckrock.com/foi/randolph-county-4639/public-records-request-flock-randolph-county-sheriffs-office-217933/。其回应“所有数据都保存在联邦休斯顿HIDTA数据库”的记录页面。

[9] 奥巴马白宫：关于HIDTA项目的说明https://obamawhitehouse.archives.gov/ondcp/high-intensity-drug-trafficking-areas-program。把HIDTA定性为“拨款项目”的官方表述。

[10] 休斯顿HIDTA的LPR数据库合同相关文件（贝敦市条例16-319）https://www.documentcloud.org/documents/28710392-baytown-ordinance-16-319-hidta-lpr/。306,800美元LPR数据库合同的文件记录。

[11] 该合同工作说明书（贝敦市公开记录系统）https://weblink.baytown.org/WebLink/DocView.aspx?id=1183546&dbid=0&repo=Baytown&cr=1。第三方数据整合、迁移复制及Unification Platform、FLOCK接口标准。

[12] HaveIBeenFlocked.com车牌查询工具http://haveibeenflocked.com/。可查询车牌是否被Flock搜索过，汇总公开审计记录。

[13] Footnote4a调查博客（Cris van Pelt）https://footnote4a.org/。围绕ALPR监控与政府合同的持续调查。

[14] SASSI：南方反监控组织https://sassisouth.org/。监控科普与调查项目，Ed所属组织。

[15] 404 Media：《Police Unmask Millions of Surveillance Targets Because of Flock Redaction Error》（2026年1月13日）https://www.404media.co/police-unmask-millions-of-surveillance-targets-because-of-flock-redaction-error/。警方未脱敏公开记录泄露数百万车牌搜索记录，催生HaveIBeenFlocked的背景报道。

这里黑鸟着重介绍一下这个网站。

Have I Been Flocked是一个独立网站：你输入车牌号，它会在已经公开的 Flock Safety 审计日志里查，这个车牌有没有被执法用户在系统里搜索过。它查的是“谁搜过这块牌”，不是“摄像头拍没拍到你”。

Flock公司曾向主机商施压，称网站危及调查与警员安全；网站回应是，材料本就是政府公开记录，只是被重新整理。部分警局脱敏失败，日志里直接露出大量车牌和案情字段，这才让按车牌反查搜索记录成为可能。

数据来自 Flock 系统的 audit log（审计日志），记录的是操作员在软件里做了一次查找：时间、搜索机构、有时是操作员姓名或缩写、检索理由、案号、搜索类型、触及了哪些网络等。

来源主要有三类：

1. 各警局应信息公开（FOIA / 州公开记录法）放出的机构审计日志

通常最完整，可能含操作员姓名、被搜车牌、案号。van Pelt 和志愿者做过大量申请；站点还提供按州写好的申请模板，自称参考了数百次成功申请。

网络...