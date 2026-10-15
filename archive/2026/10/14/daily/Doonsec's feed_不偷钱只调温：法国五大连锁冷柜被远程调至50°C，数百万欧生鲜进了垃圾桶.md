---
title: 不偷钱只调温：法国五大连锁冷柜被远程调至50°C，数百万欧生鲜进了垃圾桶
url: https://mp.weixin.qq.com/s/DcAV6ou6sB5pj4_72UeFmA
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:43.934493
---

# 不偷钱只调温：法国五大连锁冷柜被远程调至50°C，数百万欧生鲜进了垃圾桶

# 不偷钱只调温：法国五大连锁冷柜被远程调至50°C，数百万欧生鲜进了垃圾桶

原创

赤霄攻防实验室
赤霄攻防实验室

赤霄攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![封面｜行业观察（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8acqET9VPnqHlD4FxkXxphjic9W7G3DQGpUOCcqnLgibicTpdGDqr5iahPgxxjOmbvHrLw72REpVgicq9aD7EIrmpyibH5o4ib6RmDOBrQ/640?wx_fmt=png)

▲ 封面｜行业观察（制图：赤霄攻防实验室）

TL;DR

**是什么**：法国五大连锁超市（Intermarché/U/Leclerc/Monoprix/Carrefour）的制冷系统遭网络攻击，温度被远程调至 50°C

**有多糟**：AFP 确认口径超 430 家门店受影响，冷冻生鲜整柜销毁；部分门店水淹、起火，损失或达数百万欧元

**根因指向**：丹麦厂商 Danfoss 的制冷远程管理平台被攻破——供应商权限即门店控制权

**看点**：没有勒索信的纯物理破坏——OT 安全的盲区，这次肉眼可见

![事件档案卡（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8af7fQsTUEibibpzvJyVp9BJ7xq9sYnBU4yrfhWrAx4iaHiauZYZFEECibR2pzY7zRaJG2RlhAQQpRaZDC6icsria1oDm5k15TGiciaSRjV8/640?wx_fmt=png)

▲ 事件档案卡（制图：赤霄攻防实验室）

## 事件全景：一夜之间，冷链变成「解链」

10 月 11 日深夜到 12 日凌晨，法国零售业经历了一场前所未有的攻击：Intermarché、Coopérative U、E.Leclerc、Monoprix、Carrefour 五大连锁的门店制冷系统被远程篡改，温度被调高至 50 摄氏度。据 Radio France 与 AFP 向各家集团确认的口径，受影响门店包括 Intermarché/Netto 至少 300 家、U 系近 100 家、E.Leclerc 数家、Monoprix 约 30 家——合计超过 430 家门店，部分统计口径称总数达数百家。

后果是肉眼可见的：冷冻与生鲜食品整柜销毁，Intermarché 母公司直言这是「史无前例」的攻击并痛陈食物浪费；更荒诞的是物理连锁反应——部分门店的洒水系统被误触发，店内水淹，甚至出现起火。法国媒体的评价是两个字：inédite（史无前例）。巴黎检察院网络犯罪科已立案调查，截至目前尚无组织认领。

![供应链攻击链（制图：赤霄攻防实验室，据 AFP 确认信息整理）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8afsaGbM5ibqwv9jNNnaKAgCUibbL2OZia7CWfO9ENTLiauJhYCDhWUuGiblcC4v56xVJz73muPWtHSdSFFgicCI5GkciclIWZ7LWAaE2M/640?wx_fmt=png)

▲ 供应链攻击链（制图：赤霄攻防实验室，据 AFP 确认信息整理）

![影响面矩阵](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8ad4bEBDhVkm8T3BWMQjyAQloaYfNlvouic6tgPkxpQaRKoLdHZgtKnkr0rS4h66WlbiaF9m9xr9laiavs4ka0Fc0wFjX6GoF9oEOk/640?wx_fmt=png)

▲ 影响面矩阵（制图：赤霄攻防实验室，AFP 确认口径）

## 关键细节：Danfoss 平台是那个「单点」

法国媒体向 Les Mousquetaires 集团（Intermarché 母公司）求证后得到一个关键信息：这些连锁的冷柜由丹麦工业巨头 Danfoss 的远程管理平台统一管理，而正是这家供应商在 11 日夜间遭到了攻击。换句话说，五家互相竞争的零售集团，因为共用同一家温控供应商的管理平台，被一锅端了。

这就是供应链攻击最典型的形状：真正的目标也许只是其中一家，但供应商平台是所有客户共享的单点——打穿一次，全部客户陪葬。法国国家信息系统安全局（ANSSI）已介入，正在排查「其他可能受影响的法国企业」——这句话本身就说明，影响面可能还没收敛。

## 为什么不偷钱，只搞破坏

截至目前没有勒索信、没有组织认领、攻击动机不明。几种可能性值得冷静分析：其一，地缘动机的破坏行动——以关键民生基础设施为目标制造社会恐慌；其二，商业竞争或私人恩怨驱动的定向破坏；其三，为后续勒索「铺垫士气」——先展示破坏力，谈判筹码随后再谈；其四，攻击者能力验证或利益冲突方的恶意委托。无论哪种，对受害企业的损失都是真实的：数百万欧级的生鲜销毁、门店停业、 plus 食品安全连锁责任。

需要强调：以上动机分析均为公开信息下的合理推测，官方尚未公布任何归因结论。巴黎检方网络犯罪科的立案调查结果，才是这个问题最终的答案。

## OT 安全的系统性盲区，这次肉眼可见

多数企业的安全预算都花在 IT 资产上：终端、服务器、云。但真正与物理世界相连的是 OT——制冷机组、温控传感器、洒水阀、门禁、电梯。这些系统近年大批量接入厂商云端管理平台，获得「远程运维便利」的同时，也把控制权暴露在了互联网威胁模型里。IT 被打的损失是数据，OT 被打的损失是物理世界——食品报废、设备损坏、甚至消防联动的人身风险。

这起事件的特殊警示在于：温控系统被调高，首先被察觉的往往是货架上的商品而非安全告警——传感器数据在生产，但没人把它当安全信号消费。当温度异常、洒水误动这些「物理世界日志」没有被纳入安全监控时，攻击者已经用你的基础设施完成了攻击。

![Radio France/ICI 综合报道：数百家超市受影响（来源：ici.fr）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8af3t3ebrAuMtPtXQViaJNMSLNiaaFvicFFRRtQoRX0QxQfU3KhFI0uS9ObSMPeLHIWYHJc9Faa8HIYdrfKEDeyJ9OVMpzd8VibsbMg/640?wx_fmt=png)

▲ Radio France/ICI 综合报道：数百家超市受影响（来源：ici.fr）

## 防御视角：四步给 OT 补课

### 1. 给 OT 资产做一次盘点

把冷柜、温控器、门禁、摄像头这类「会碰物理世界」的资产单独列册：接了哪个厂商平台？走什么网络？谁有远程权限？答不出这三个问题的，就是盲区。

### 2. 安全参数变更必须告警

温度、压力、阀门状态这类参数的异常变更，应当触发独立于业务系统的安全告警——50 度的冷柜在业务报表里只是「温度高了」，在安全监控里应该是「立即派人到场」。

### 3. 供应商平台访问治理

厂商远程管理平台的账号最小化、操作留痕、异常登录告警，三项缺一不可。这次事件里，供应商平台就是那个被打开的正门。

### 4. 物理联动的熔断设计

温控失灵不应触发洒水，洒水误喷不应淹没电气——关键系统之间的物理联动需要熔断与人工确认环节。安全设计要回答一个问题：最坏情况下，怎么让损失停下来。

## 参考来源

1. Radio France / ICI：Frigos à 50 degrés, produits frais jetés（2026-10-12）
2. AFP 向五大连锁集团确认的影响门店口径
3. RTL / MCETV（Ouest-France）/ Nice-Matin 相关报道
4. MSN France：网络安全专家分析文章
5. Financial Times 相关报道（中文媒体转引口径）

免责声明：本文仅用于安全研究与防御交流；事件信息以官方调查结论为准，动机分析系公开信息下的合理推测。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8acyYZfmKJeSLQ7Quiag7TKhsm6Z5yHicU9D1f8on7dzPIKTE1LJpnoT3TmcTlngd8BRNH8cf30FeI94XtDOrUOJibW2Jh16nvMQ6g/0?wx_fmt=png)

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