---
title: 烽火三十六技丨巴基斯坦海缆故障后，路由还在，部分跨境访问却变慢了
url: https://mp.weixin.qq.com/s/OM8jpQ7NPKJxWK3vvJpHsg
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:40:03.762787
---

# 烽火三十六技丨巴基斯坦海缆故障后，路由还在，部分跨境访问却变慢了

# 烽火三十六技丨巴基斯坦海缆故障后，路由还在，部分跨境访问却变慢了

盛邦安全WebRAY

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于盛邦安全太湖实验室
，作者太湖实验室

![](https://wx.qlogo.cn/mmhead/wprMnqDUJH6KjfPs4j7aGibRR1UT8vyROCM2Z8SnU0ibGoQbQncuTsTfcQ6vgprBkibYh5Jq1r8wnw/0)

**盛邦安全太湖实验室**
.

关注卫星互联网、星地融合网络、互联网基础设施与网络空间地图，用通俗语言拆解复杂技术、产业变化和全球网络格局。

11月18日傍晚，巴基斯坦驻英国高级专员署在伦敦发出通知，暂停办理身份证件、护照和签证，文件认证照常。公告提到，巴基斯坦近海一条国际海缆出现故障，互联网连接和相关服务可能受到影响。[1,2]

在伦敦申请巴基斯坦机读护照，工作人员要按巴基斯坦国家数据库和登记管理局（NADRA）的身份记录录入资料。当天的公告没有披露办理这些业务具体经过哪条线路。据第三方网站保存的巴基斯坦驻米兰总领馆公告，米兰当地11月18日也暂停了 NADRA 业务。[1,3,4]

伦敦的暂停公告发于当地时间18日18:19，已过当日常规受理时间。次日09:14，高级专员署宣布三项业务均已恢复，请申请人按原预约时间到场。两份公告发布时间相隔14小时55分，窗口实际停办的起止时刻没有公布。[5,6,7]

## 故障发生在距巴基斯坦海岸约11公里处

巴基斯坦比当时的伦敦早5小时。下文除特别标注外，均用巴基斯坦当地时间（UTC+5）。11月18日20:48，巴基斯坦电信管理局（PTA）通报，**东南亚—中东—西欧5号海缆（SEA-ME-WE 5）**在距该国海岸约11公里处出现故障，具体故障时间没有公布。这条约2万公里长的海缆系统于2016年投入服务，在卡拉奇接入当地运营商 Transworld Associates（TWA）的登陆站。[8,9,10]

PTA 在通报中说，运营商正把流量转往其他国际线路。[8,11]

![故障海缆与其他国际线路的连接示意](https://mmbiz.qpic.cn/sz_mmbiz_png/oPka9YhZ38jogFLw95DyK0Qibp4tMo7ibNdTtoDdDiaoeDh6Q2icQx9DiaABOBFoYfxEtaPgc5onMlTHVhGNUQSic9W2dcGyvIJibulqiaNExIpoiaQI/640?wx_fmt=png&from=appmsg)

图1　原来经 SEA-ME-WE 5 传输的部分流量改走其他国际线路。两条线示意改道方向，实际使用的替代海缆和各自承担的流量没有在这份通报中列明。[8,11]

## 从巴基斯坦往境外测，哪些连接变慢了

从18日18:00到20日03:42，测量平台 GeoCables 从巴基斯坦境内的9个网络向境外探测，其中4个网络的跨境连接质量下降。平台给出的往返时延读数是236毫秒，常态参考值为135毫秒，丢包率最高约16%。公开记录没有说明236毫秒是均值、中位数还是峰值，也没有列出判断单个网络异常的阈值。[12]

18日22:14，NetBlocks 在 Telegram 通报巴基斯坦网络连通性下降。Cloudflare Radar 随后发布了24小时流量图，报告其观测到的巴基斯坦 HTTP 字节量最大降幅约为 **36%**。据 SnowRock 对同期 Radar 数据的分析，低点在当地时间19日00:30左右，对比的是一周前同一时刻的字节量。[13,14,15]

19日00:30，互联网中断监测项目 IODA 同时记录了路由和探测应答两项数据。把 IPv4 地址每256个划为一块（/24），当时在公开路由里仍有 **21,119**个地址块广泛可见，过去13天同一时刻的中位数是 **21,118**个。可同一时刻，能回应 IODA 主动探测的地址块只有 **5,346**个，平时是 **6,475**个，少了 **17.4%**。单看运营商 TWA，同样的探测收到了31个地址块的回应，过去13天同一时刻通常有71个。这里数的是有应答的地址块。一个块里可以有多个用户，探测无法据此给出断网人数。[16,17,18]

![IODA 观测中公开路由可见数和主动探测应答数的对照曲线](https://mmbiz.qpic.cn/sz_mmbiz_png/oPka9YhZ38gicC6nka45XLof3KEcu49NbO5UOsjnVXtYZIuEbTiciatrfpEoU7mM3pxIRbv9UamuiaP9tFGN4zMI7zHb8NpNibIiaiaLxmvXLLlxls/640?wx_fmt=png&from=appmsg)

图2　两条曲线各以11月5日至17日（UTC）同一时刻的可用观测中位数为100，每半小时取一点。19日00:30，应答地址块数降至基准的82.6%，路由可见数仍贴近100%。[16,18]

## 五分钟内，路由通告增至前一时段的33倍

不同网络用**边界网关协议（BGP）**通告哪些 IP 地址段可以经由自己到达。TWA 的自治系统号（ASN）是 **AS38193**，通告列出的路径如果经过 TWA，就能在其中找到这个编号。[19,20]

RIPE NCC 的 RRC25 路由采集器按协调世界时（UTC）为更新文件命名。11月18日，当地17:35至17:40（UTC 12:35至12:40），路径中含 AS38193 的地址段通告共有 **2,528条**。紧接着的17:40至17:45（UTC 12:40至12:45），同一采集器收到了 **83,551条**，约为前一时段的33倍。其中逾九成集中在当地17:43和17:44两分钟。一周前的11月11日，当地17:40至17:45（UTC 12:40至12:45），同样计数是2,701条。[19]

![RRC25 记录的相邻五分钟路由通告数](https://mmbiz.qpic.cn/mmbiz_png/oPka9YhZ38jqrZl2lQWEvYrbyQBlfe7JS3mLzFUdwC0ibj1SOh0pJ7asZcTJXTV8l5bQeKrMr781XnqwribrjWibZOA3C12lGTzIOQQClStGTk/640?wx_fmt=png&from=appmsg)

图3　巴基斯坦当地时间17:35和17:40开始的两个五分钟，对应 RIPE 原始文件名中的1235和1240。每根柱子按收到的通告条数计数，同一地址段可能出现多次。[19]

在17:35开始的五分钟里，只有2条通告把 TWA 的编号 AS38193 连续写了两次或更多。到了17:40开始的五分钟，这样的通告有7,833条。其中一批记录里，Cogent 的编号 AS174 后面一连写了七个 AS38193。这种写法叫**AS 路径前置（AS-path prepending）**。在其他择路条件相同时，别的网络通常会优先选择较短的路径。重复写入自己的编号，便可能让其他网络发往同一地址段的数据改走另一条路。至于有多少流量真的转走，需要运营商的流量记录才能回答。[19,20]

按 UTC 统计11月18日全天，BGPKIT 在78个公开采集器中共收到约1,442万条带有 AS38193 的通告，是此前13天日中位数的约3.8倍。它还用其中76个采集器的记录，逐时段检查了8,896个巴基斯坦地址段。这些地址段在事前通常至少被5个采集器看到，其中 **8,894个**在每个重建时段都保有至少一半的事前可见度。[20]

## 窗口重新开了，海缆仍在维修

伦敦19日上午发布了恢复业务的消息，运营商的调度还在继续。巴基斯坦《黎明报》21日报道，TWA 在给监管部门的报告中说，约 **80%的受影响流量**已改走其他海缆。在发给客户的邮件里，TWA 把 **12月6日**列为预计修复日期，并提醒高峰时段的网速仍可能受影响。截至11月25日，公开通报尚未确认此次故障的物理原因。[6,8,21]

11月18日晚起，GeoCables 从巴基斯坦境内向境外探测。有些连接来回一趟比平时更久，也有部分探测包丢失。[12]19日凌晨00:30，IODA 向巴基斯坦的地址发出探测，能回应的地址块也比平时少。[16]那一夜，公开路由表里仍能查到通往大多数受测地址段的路径。[20]数据包能不能回来、来回要等多久，还得看实际探测。

## 资料来源

**[1] 巴基斯坦驻英国高级专员署 · 业务暂停公告**
https://phclondon.org/press-release/temporary-suspension-of-nadra-passport-and-visa-services/

**[2] 巴基斯坦驻英国高级专员署 · 身份证件服务目录**
https://phclondon.org/consular-services/

**[3] 巴基斯坦驻英国高级专员署 · 护照办理流程**
https://phclondon.org/mrp-flow/

**[4] GovServ · 驻米兰总领馆 NADRA 业务暂停公告转载**
https://www.govserv.org/IT/Milan/107599867611015/Pakistan-Consulate-General-Milan?lang=it

**[5] 巴基斯坦驻英国高级专员署 · 暂停通告发布时间**
https://x.com/PakistaninUK/status/2123118796575474041

**[6] 巴基斯坦驻英国高级专员署 · 业务恢复公告**
https://x.com/PakistaninUK/status/2123344048379330669

**[7] 巴基斯坦驻英国高级专员署 · 窗口受理时间**
https://phclondon.org/openinghours/

**[8] 巴基斯坦电信管理局 · 海缆故障通报**
https://x.com/PTAofficialpk/status/2123080958098464779

**[9] SEA-ME-WE 5 联盟 · 海缆项目资料**
https://seamewe5.com/about/sea-me-we-5-project-fact-sheet/

**[10] SEA-ME-WE 5 联盟 · 卡拉奇登陆站**
https://seamewe5.com/2016/09/state-of-the-art-high-speed-submarine-cable-sea-me-we-5-lands-at-transworld-landing-station-karachi/

**[11] 巴基斯坦联合通讯社 · 电信管理局改道说明**
https://www.app.com.pk/national/international-submarine-cable-develops-fault-pta/

**[12] GeoCables · 巴基斯坦境内与跨境探测**
https://geocables.com/outages/pk

**[13] NetBlocks · 巴基斯坦连通性通报**
https://t.me/netblocks/1586

**[14] Cloudflare Radar · 巴基斯坦 HTTP 流量**
https://x.com/CloudflareRadar/status/2123214677220217086

**[15] SnowRock · 巴基斯坦故障当日的 Radar 流量对照**
https://snowrock.com/insights/pakistan-internet-smw5-gulf-of-oman-cable

**[16] IODA · 巴基斯坦原始观测数据**
https://api.ioda.inetintel.cc.gatech.edu/v2/signals/raw/country/PK?from=1793750400&until=1795305600

**[17] IODA · TWA 网络原始观测数据**
https://api.ioda.inetintel.cc.gatech.edu/v2/signals/raw/asn/38193?from=1793750400&until=1795305600

**[18] IODA 项目组 · 路由与主动探测方法**
https://blog.apnic.net/2024/09/11/ioda-internet-outage-detection-and-analysis/

**[19] RIPE NCC RIS · RRC25 更新文件（文件名按 UTC 计时）**
https://data.ris.ripe.net/rrc25/2026.11/

**[20] BGPKIT · 海缆故障期间的 BGP 观测**
https://bgpkit.com/blog/smw5-fault-bgp-view-2026-11-18/

**[21] 《黎明报》 · TWA 流量改道报告与修缆通知**
https://www.dawn.com/news/2046093

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r9c6R4tUf9uB7HdX3A7N29rSpIE18nYeDa9Wmic7TdmEgtBje8ZXEWq0yVtDsMUjVODjCgn7Gy5iccMugG2ibS7Cw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过