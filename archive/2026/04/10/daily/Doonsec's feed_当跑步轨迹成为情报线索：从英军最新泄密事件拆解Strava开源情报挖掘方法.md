---
title: 当跑步轨迹成为情报线索：从英军最新泄密事件拆解Strava开源情报挖掘方法
url: https://mp.weixin.qq.com/s/MDW9T3cBJFZXrgaE4H1vgA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:19:12.584244
---

# 当跑步轨迹成为情报线索：从英军最新泄密事件拆解Strava开源情报挖掘方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SmpxklM1IWyxicu8s5ibEaOk38icqHHthRJzOltI72pPtbqNOb3ssVfiaXcDveTVfSw97icrXBnw2qQP5054QKLlt8YjyEXLaI1M1YTQdlHV1HAM/0?wx_fmt=jpeg)

# 当跑步轨迹成为情报线索：从英军最新泄密事件拆解Strava开源情报挖掘方法

原创

猫头鹰OSINT
猫头鹰OSINT

猫头鹰OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近，继法国海军军官通过热门健身应用Strava意外泄露法国“戴高乐”号航母实时位置之后，英国又爆出一起Strava军事泄密事件。

2026年4月3日，英国媒体 The i Paper披露，自2026年1月以来，至少有519名驻扎在敏感军事设施的英国军人、承包商及其家属，在Strava上公开公开记录了自己的跑步和训练数据。从部队指挥官、少尉到情报专家，各级军官都在记录数据。

这些数据不仅包含精确的GPS运动轨迹，还关联着用户的姓名、头像、社交网络信息以及活动时间，从而在无意中暴露了大量敏感信息。

# 哪些军事基地成为数据源

调查显示，这些公开运动记录来自英国及其海外的一系列关键军事设施，包括：

* 英国核潜艇基地——克莱德海军基地（HMNB Clyde）；

* 英国在中东的重要空军枢纽——阿克罗蒂里皇家空军基地（RAF Akrotiri）；

* 印度洋战略基地 Diego Garcia；

* 美英联合间谍基地——英国皇家空军门威斯山基地（RAF Menwith Hill）；

* 以及英国唯一的弹道导弹预警站——弗林代尔斯皇家空军基地（RAF Fylingdales）等敏感地点。

# 克莱德海军基地：核潜艇母港的跑步路线

其中，在位于苏格兰的克莱德海军基地，仅2026年前三个月就有约110人公开记录了跑步路线。该基地不仅是英国皇家海军潜艇部队的母港，也是英国核威慑力量“三叉戟”导弹系统的部署地点。部分运动路线甚至位于基地禁区内部，通过这些轨迹的细节，可以推测人员活动区域，甚至间接判断某些军官可能部署在哪一艘核潜艇上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWyQbeXhrgPomQ7e3mEfEKibPPYMLFG1S37dPiaP0uW6qciauSFK5IyAyasy8aLQqpglyCD6NiaAr4IO9ib4NqrF3LCp2p7aNDZHZXtU/640?wx_fmt=png&from=appmsg)在英国四艘先锋级核动力潜艇的母港——克莱德海军基地记录的位置信息

# 阿克罗蒂里空军基地：中东枢纽的核心禁区

在塞浦路斯的阿克罗蒂里皇家空军基地，研究人员同样发现大量运动记录。该基地是英国在中东地区最重要的军事枢纽之一，长期承担对中东地区军事行动的支援任务。数据显示，仅2026年前三个月，就有333人在基地安全警戒范围内记录运动活动。其中一名情报专家记录的路线甚至穿越基地核心禁区，被标注为“阿克罗蒂里自然步道”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWwjpNC7xBTVLg95xP0dS2qnc9KGOyfTXjNpaVBGbBdqkPyaWXuxVfsQJIfzFooNYeHGuEBArzibd5LmFAJXmdq0dj2LmaARXWIw/640?wx_fmt=png&from=appmsg)位于塞浦路斯的阿克罗蒂里皇家空军基地（RAF Akrotiri）已确定多条跑步路线

# 迪戈加西亚基地：自嘲式路线名称

在印度洋的迪戈加西亚基地，调查人员发现25条来自基地内部的跑步路线，其中一些路线名称甚至带有明显的自嘲意味，例如“Security Leak（安全漏洞）”或“Fools Must Be Punished（愚蠢者必受惩罚）”。这些路线位于基地内部区域，而迪戈加西亚正是美英在中东行动的重要战略跳板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWxPNaMmeSWibYeu8DUJeANA2nmOyLx8iaCtib3UbMeCtzOynibCxT8zXuBaCUnj0FoRMcTCkYq7Nw94CrDriaIYGyTL1bRwt28b4ic10/640?wx_fmt=png&from=appmsg)印度洋迪戈加西亚军事基地记录的一条跑步路线

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWxlYNfRjjGC5X3c1vKYdcPpvufWLHUJJBBVC3TIFeiaO4Lrib8GYK6dJ21t93hliboN0sKrYpSHRQib5Wdhf30xLVxtGutRLccMR0s/640?wx_fmt=png&from=appmsg)在英国唯一的弹道导弹预警站——弗莱因代尔斯皇家空军基地进行跑步训练

英国安全与情报界人士认为，这类信息虽然不属于高度机密，但其中包含的细节——例如人员身份、活动规律、家庭住址以及社交网络关系——可能帮助敌对情报机构拼接出军事人员结构与基地活动图景，从而支持监视、接触甚至勒索活动。

在此次英国事件发生前不久，法国军方也遭遇了类似的“Strava泄密”。2026年3月13日上午10时35分左右，一名年轻的法国海军军官在“戴高乐”号核动力航空母舰的甲板上进行了一次跑步训练。他使用智能手表记录了约35分钟、略超过7公里的运动轨迹，并以公开设置上传至Strava应用。凭借GPS定位数据，法国《世界报》几乎实时锁定航母当时正位于地中海东部、塞浦路斯西北方向，距离土耳其海岸约100公里的海域，正与其护航舰队（至少包括三艘护卫舰和补给舰）一同向中东部署。

这类事件也并非近年才出现。早在2018年，Strava发布全球运动热力图后，研究人员就在其中发现了多个偏远地区的军事设施轨迹，包括中东地区的美军基地、非洲情报据点以及南大西洋的军事设施。2024年，法国《世界报》还通过运动数据识别出多名与法国总统马克龙安保团队有关联的人员活动轨迹。

这些案例表明，Strava不仅仅是一款记录运动成绩的应用，更逐渐演变为一个规模庞大的开源数据集。该平台目前在全球190多个国家拥有超过1.8亿注册用户，其数据已经被广泛应用于不同类型的调查场景。例如，保险调查人员曾利用Strava骑行记录推翻伤残索赔案件；企业尽职调查人员可以通过运动轨迹验证某人是否真实出现在某个地点；人权研究机构则能够利用活动记录确认某个人在特定日期是否出现在某一地区。

# 开源情报挖掘方法：三种核心技术路径

那么，开源情报研究人员如何系统化地从Strava海量数据中挖掘有效情报？核心方法主要围绕三条技术路径展开。

# 第一，热力图分析：识别潜在设施与活动区域

Strava长期发布全球运动活动汇总热力图。研究人员可以在地图上查看不同运动类型（跑步、骑行、划艇）的活动密度。在沙漠、森林或偏远地区，如果出现明显的高亮轨迹聚集区，往往意味着存在稳定的人类活动。

将这些数据与卫星影像进行交叉分析，可以进一步确认其性质。例如，可以利用 Google Earth Pro 或 Sentinel Hub 对疑似区域进行比对。如果某一设施在卫星影像中难以识别，但热力图仍显示持续活动，则可能说明该设施仍在运行。

![](https://mmbiz.qpic.cn/mmbiz_png/SmpxklM1IWxN0zL56296XHwrlcyRw9pRFCk0qPVeZOCE0HawNxyz5ycg2OyEfWoViawBicEVTMebM06EaG2iaRk1XmtpImOUmkttiaibKEB78SHU/640?wx_fmt=png&from=appmsg)

此外，热力图中清晰的线性轨迹往往代表固定的慢跑或巡逻路线。这些路线可以帮助研究人员推测基地外围道路、内部通道甚至巡逻路径。

2018年，澳大利亚研究人员Nathan Ruser正是通过这种方式，在Strava热力图中发现了发现了索马里的中央情报局据点、叙利亚和伊拉克的美国基地、福克兰群岛的英国基地，以及一名独自骑自行车绕着 51 区转悠的人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWwNMeP3ZOibAppGlAnzrCzzYp4nJ6p4LVJSVuy9bpMYfiaWFWuicXibRibpc9iatb4zZeJgZFfHX9yZYwjIVwFjZiaDVwkib0WWEgyX0VI/640?wx_fmt=png&from=appmsg)

# 第二，路段数据分析：识别人员活动与单位结构

Strava会将常见运动路线划分为“路段（Segments）”，并记录用户在这些路段上的成绩。通过分析这些路段排行榜，可以识别哪些用户曾在特定路线活动。

虽然Strava近年来将许多功能转为付费，但一些第三方平台仍能提供一定程度的数据访问。例如，通过Veloviewer等工具，可以查看部分路线的用户排行榜，从而识别具体参与者。

在偏远地区的军事基地，这种方法尤为有效。例如在阿富汗北部的 Camp Marmal，研究人员曾通过路段数据识别出大量驻军人员的运动记录，从而推测基地规模和人员轮换情况。

![](https://mmbiz.qpic.cn/mmbiz_png/SmpxklM1IWyA42PNwNLtXc8NAJIHJqJe3gwyQjibibX0uFIghgdGiaHDYOibV6UftqHia618p4GvcSDWvibOByD2EcuUxszicbLEcF9OwLaCqAQERg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWxicXEZoBcQG3cEMUleJh5ibLATiare47cpDcLicXmEOkZE4UPl1Bu4hre9Dm0QBDrgMpczqCuQKMOBkuXmf7pvcaetpecSt8gJsGE/640?wx_fmt=png&from=appmsg)

类似方法也曾用于分析伊拉克 Camp Taji、马里 Camp Castor 以及南苏丹联合国基地的人员活动情况。英国媒体识别出519名军人的调查，本质上也是这一方法的延伸应用。

# 第三，跨平台归因：确定真实身份

在许多情况下，Strava用户会使用真实姓名或包含个人信息的用户名。研究人员可以将这些信息与其他平台进行交叉比对，例如 Google、LinkedIn 或 Facebook。

个人头像同样可以成为重要线索。利用反向图片搜索工具，例如 Google Lens 或 Yandex Images，可以快速找到同一照片在其他网站上的出现位置。

此外，一些用户还会公开运动设备型号。例如使用 Garmin Tactix 等战术级手表的用户，往往与军队或执法机构存在一定关联。

Strava的“俱乐部”功能同样具有情报价值。一些军事单位内部会建立非官方跑步俱乐部，通过成员列表即可识别所属单位及人员网络。

法国《世界报》采用此类手法确认了多名与法国总统马克龙有关联的人员。

# 数字时代的“行为情报”

从情报研究角度来看，Strava所揭示的问题不仅仅是个别用户的安全意识不足，而是数字时代信息结构的一种变化。随着可穿戴设备和运动应用的普及，人类日常行为正在不断转化为可记录、可分析的数据。

这些数据虽然最初并非为情报用途而设计，但在开放互联网环境中，它们逐渐构成了一种新的“行为情报”来源。军事人员的跑步轨迹、工程师的骑行路线、外交人员的周末活动——这些看似零散的数据，经过长期积累和分析，往往能够拼接出完整的组织结构与活动图景。

从这个角度来看，Strava既是一款运动应用，也是一座持续更新的开源情报数据库。在未来的信息竞争环境中，这类由日常行为产生的数据，很可能继续成为情报分析的重要来源，同时也将对个人隐私与行动安全提出更高要求。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/biarWYvQqiaDic4snvC23OLhiaMAjLibbsp65I4VAh9Wtkq9VEtls6dEpuHbQAdNcdqwHkUGtpylW3dr0lzWwPTjR7g/0?wx_fmt=png)

猫头鹰OSINT

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/biarWYvQqiaDic4snvC23OLhiaMAjLibbsp65I4VAh9Wtkq9VEtls6dEpuHbQAdNcdqwHkUGtpylW3dr0lzWwPTjR7g/0?wx_fmt=png)

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