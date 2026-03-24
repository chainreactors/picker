---
title: 谁在测绘真实世界？
url: https://mp.weixin.qq.com/s/51YN3YQftDYeuDlLyx75zQ
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:14:16.270745
---

# 谁在测绘真实世界？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAiaicmr9HS5ia43UOehAZXw3S2HS5PoVUL8I6DghSB2CicXLfibsjeaLNbsefTDjTibfAhmfAEHXXQU4J7licTW2qrto9PPjmnjuZ5ATQ/0?wx_fmt=jpeg)

# 谁在测绘真实世界？

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器中沉浸阅读

## 事件概述

2026年3月10日，Niantic Spatial 宣布与配送机器人公司 Coco Robotics 达成战略合作。合作内容很直白：Niantic Spatial 将把从 Pokémon Go 玩家那里收集的超过 300 亿张图像数据，用于训练 Coco 的人行道配送机器人，让它们在 GPS 信号差的城市峡谷中精准导航。

消息一出，Reddit 和 X 上炸了锅。玩家们的愤怒可以浓缩成一句话：「我扫描公园雕像是为了让游戏更好玩，不是为了给送披萨的机器人当免费测绘员。」

Niantic CEO John Hanke 的一句话更是火上浇油——他说让皮卡丘在现实世界里逼真地跑来跑去，和让 Coco 的机器人安全穿行街道，「本质上是同一个问题」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiaYEoic84dv55icucibHfMFIKq3pp1XUIrLz0VwrgNtSwGT1ymWHWfDib0PR6wc2K591obco3DFvXgP54RykLPZZpiaw5xOnYP6RibE8/640?wx_fmt=png&from=appmsg)

这件事之所以值得深入分析，不仅仅因为 Pokémon Go 本身，而是因为它揭开了一个更大的现实：**从你的门铃到卫星轨道，物理世界正在被数十家公司同时测绘，绝大多数人身在其中却浑然不觉。**

## 研判

### 数据收集的特洛伊木马

Niantic 前高管 Brian McClendon（Google Earth 联合创始人）在 TED AI Show 的访谈中坦率地说：「游戏本身不是为了建造这张地图而设计的。地图是让游戏变得更好的一个副作用。」

这个「副作用」一词值得深思。Pokémon Go 破解了一个困扰整个测绘行业的难题——**如何让海量真人自愿、持续、免费地为你采集空间数据**。Google 靠 Street View 车队烧钱巡街，Mapillary 靠行车记录仪用户的善心众包，Hivemapper 靠加密货币激励。而 Pokémon Go 靠的是——抓精灵的快乐。

**这种模式并非 Niantic 独创。** Google CAPTCHA 让用户在证明「我不是机器人」的同时标注了交通标志和自行车，用于训练计算机视觉模型。Tesla 的 Autopilot 在你开车的同时采集道路数据。Strava 在你跑步时记录了轨迹。**游戏/工具是前台，数据采集是后台，这已经是硅谷的标准操作模式。**

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAhM69RkvicO2Xh9KwXf1m67QSNzO0UiaTfjJ3s79JdWIOrOkHib9qXicezK0tumamXxZ1pMOXjva3ib03ksic8DojCWdmVmuTiaRdOHcs/640?wx_fmt=png&from=appmsg)

### 更大的图景：谁在测绘这个世界？

 如果把 Pokémon Go 事件放在更大的空间数据采集版图中看，它甚至算不上最令人担忧的那个。以下是一张按采集层级划分的「世界测绘力量图谱」：

**👤 人体层级** —— Meta Ray-Ban 智能眼镜在2025年售出超过 700 万副。瑞典媒体 Svenska Dagbladet 和 Göteborgs-Posten 的联合调查揭露，用户通过 AI 功能拍摄的影像被发送至肯尼亚外包公司 Sama，由人工标注员审阅，其中包含裸体、性行为、银行卡信息等敏感内容。Meta 目前面临美国的集体诉讼。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiam5BZkBBiaQtUsqQNnRuV5BOLiby6Hd0Cleu2NQibFm8l6s1ZZ34nHBExzhMkW3icr4nlicQQBW2raSOH9hHx4FmiaON8k4TmzxnneQ/640?wx_fmt=png&from=appmsg)

**🚗 车辆层级** —— Tesla 车队的行车记录仪持续采集道路数据。Waymo 为其运营城市构建了厘米级3D地图。每一辆自动驾驶汽车同时也是一台移动测绘站。

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAjoYlYZW9LIdQhTEic36jasyMxWJWksfP3wZUSyAINNoyp2mzYUmAqW4DibxOVypr0KU5Je0IxnVUiaYXcMWw3micYIgDAibM0GLHY8/640?wx_fmt=png&from=appmsg)

**🏠 街道与家庭层级** —— Amazon Ring 门铃摄像头覆盖了数百万家庭门口。2026年2月超级碗期间，Ring 的「Search Party」功能广告因被指控「美化大规模监控」而遭到强烈抗议，随后 Ring 宣布取消与车牌识别公司 Flock Safety 的合作。Amazon 此前还曾试图以17亿美元收购 iRobot（Roomba 制造商），被美欧反垄断监管机构联手阻止——人们担心 Amazon 通过 Roomba 的室内地图功能获取家庭户型数据。

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgRpPDpmb6FT4KNOlkhR7CtSah2aPNwHkDMy40DTl5QK6ibNzKCLcdOMdAe8VjcicJqFVy6Hzdb7ibBZYUvczFibzicAP0YQKr7FJrY/640?wx_fmt=png&from=appmsg)

**🥽 头显层级** —— Apple Vision Pro 和 Meta Quest 每次使用时都会3D建模你所在的房间，这是它们实现空间追踪的基础。也就是说，你的家可能同时被 Ring（门口）、Roomba（地板）、头显（整个房间）三种设备在空间上「理解」。

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAjPHAfz2yTO5LCSd2MAYaHjDIn6rRibMCuNXEydokHlicnxLvAGfKFhVfl8ibFL9ke7iaT4ZJld6N3agetOLKbaj5oCG5PBKTjcZZk/640?wx_fmt=png&from=appmsg)

**🏃 轨迹层级** —— 2018年，澳大利亚研究员 Nathan Ruser 发现 Strava 全球热力图在叙利亚和阿富汗的沙漠中呈现出明亮的跑步路线——那正是美军和盟军秘密基地的位置。士兵们的日常慢跑暴露了基地周长、巡逻路线甚至兵力集中区域。美国国防部随后审查了军人使用健身追踪器的政策。2026年3月，法国航母「戴高乐」号的位置也因一名军官在 Strava 上公开分享跑步记录而泄露。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAgUXmyJX7Y1x6rj6xPt0aQyWs68wz7DcxDrhaML1pTJySEFAyOmKIpQEvMdYaZ4hTwG1vr9mnoDDMTEIy14HRKibnZicjBdSwBXI/640?wx_fmt=webp&from=appmsg)

**🛰️ 太空层级** —— Planet Labs 每天从轨道上拍摄整个地球陆地表面。Iceye 使用合成孔径雷达进行3D成像。任何地面变化——建筑施工、森林火灾、军事调动——24小时内就有前后对比影像。

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAiappUmQQxvlZjiatpV4nQiaHXoUbG9BmcvSbydI8KEzVgzUBHeXfHDzNMlfqCXIdfkhW5HXXzga7A2omuRVwyNHQEibHrmVCicdMG8/640?wx_fmt=png&from=appmsg)

## 影响评估与趋势展望

**短期影响**：Niantic Spatial 与 Coco 的合作本身对普通用户的直接隐私威胁有限——公共地标的3D扫描确实远不如 Ring 门铃或 Meta 智能眼镜那样具有入侵性。但这一事件的舆论发酵会加速全球对「副作用式数据收集」的监管讨论。

**中期趋势**：随着具身 AI 和机器人行业的爆发式增长，**空间数据正在成为新的石油**。Hanke 自己说得很清楚：「我们看到了机器人领域的寒武纪大爆发。」谁拥有最精确、最鲜活的空间地图，谁就掌握了机器人导航的基础设施。Niantic Spatial 的定位不是游戏公司转型，而是要成为「空间智能的基础设施供应商」。

**长期风险**：当人体层级（智能眼镜）、车辆层级（行车记录仪）、家庭层级（门铃+扫地机器人+头显）、轨迹层级（运动App）和太空层级（卫星影像）的数据被融合在一起，物理世界的每一个角落都将被持续、实时、多维度地「理解」。这不再是某一家公司的隐私问题，而是**整个技术文明的基础架构正在被重写**，而大多数身处其中的人甚至还没意识到自己是数据源。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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