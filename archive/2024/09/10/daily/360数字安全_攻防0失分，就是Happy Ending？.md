---
title: 攻防0失分，就是Happy Ending？
url: https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247575212&idx=1&sn=e0b1f04bf8d82e500fcbdfe9d87a0cc4&chksm=9f8d36a4a8fabfb24b9b856e185a07e7c5d740ef58beb27aa214c21a9bae5c0eb3980ae023a9&scene=58&subscene=0#rd
source: 360数字安全
date: 2024-09-10
fetch_date: 2025-10-06T18:31:38.254524
---

# 攻防0失分，就是Happy Ending？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pLEuriaaPnU02SCfIwCvQJibozHpLYCfiavMkl2BDXb8GNB0HyXgicEqu1dpKG6wJRKvJpWIt8OUW7UicAaHIic8xxTQ/0?wx_fmt=jpeg)

# 攻防0失分，就是Happy Ending？

360数字安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)

事情发生在8月31日凌晨00:30，某区域性金融机构的HW驻场人员陆续撤场，小明作为驻场团队中的技术担当，看着团队“0失分”的成绩单，不由地嘴角上扬。

从今年起，攻防已经趋于常态化。对于小明这种网安人来说，取经路九九八十一难，这次HW结束，也算是网安人直面天命的日子终于暂告一段落。

然而，事情远没有想象的简单。

**谁搞的鬼？一键锁定**

当天早上6点，小明被手机提醒叫醒。屏幕上，他收到了一则高危告警，称该某区域性金融机构遭遇了一起疑似APT攻击事件。

要知道，APT攻击的火力值和紧急程度可谓是最高。但小明却异常淡定，睡眼惺忪地点了几下手机，就继续美梦了。

这天早上9点，该金融机构的信息安全主管一个电话追来。“我手机收到了APT告警信息，怎么回事，对业务有什么影响，哪些资产被盯上了？怎么处置，尽快给我一份报告吧”。

“领导，针对今天早晨6点集团疑似遭受APT攻击的报告，刚刚已经发到您邮箱了，已经处置完毕。”

主管打开这份报告，报告里详细记录者这次事件的时间线：

**06:30** 通过推推收到来自安全运营中心的高危告警

**06:31** 云端专家将受害者主机实行隔离措施

**06:32**从告警中发现，受害主机（192.x.x.165）触发针对威胁情报-APT情报IOC (tomcruefrshsvc.com)告警事件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU02SCfIwCvQJibozHpLYCfiav0sz4nicaVSQcrMfzbpLETPblXaUlowr11R5ZUH6Sc5hribknUPgZrMWQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU02SCfIwCvQJibozHpLYCfiavyQbUWehibWp8Kw8SyabUib0V6ibr1kZWsuY54r5jErmaoB6yWicKDXa0ibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU02SCfIwCvQJibozHpLYCfiav9sICD3cSRZb91UKxOQNMTeFnxNOKBoOy850C0XCqibgSTpLT74lHrkw/640?wx_fmt=png&from=appmsg)

**06:33**：随后，打开流量智能体告警界面，在线访问360 NDR流量智能体进行分析，360 NDR捕获了受害主机上特种木马与C2之间的实质性通信活动内容。

**06:35**：经与二线专家和一线现场技术人员排查后，从360 NDR设备上取证通信载荷可以看到该特种木马采用明文HTTP协议通信，URI中携带了受害主机的主机名、用户名、操作系统等资产标示信息，然后通过通信协议负载内容来完成命令与控制的数据交换。

**触发高危告警→受害主机隔离→流量分析→确认攻击行为→溯源取证→发现关键线索→锁定攻击，**一顿操作猛如虎，360 NDR智能体不仅捕捉到了特种木马与C2之间的通信活动，还通过智能分析揭示了攻击者的行为模式和关键线索，实现了对APT攻击的精准打击和快速溯源，**且仅仅用时5min。**

**不具备APT检测能力的NDR**

**不是好的攻防利器**

小明在事后不禁暗自庆幸，正是360 NDR流量智能体，才能在这次APT攻击事件中化险为夷。在360安全大模型的赋能下，360NDR智能体不仅实现了对网络流量的智能监控与异常检测，更将APT攻击的全过程抽丝剥茧，展现得淋漓尽致。

对于一款优秀的NDR产品而言，其核心价值在于实战中的高效表现：

首先，**它必须具备精准识别加密流量的能力。**360 NDR智能体能够精准识别APT组织远控木马产生的伪装类SSL流量，并利用先进的AI小模型对异常检测结果进行深入分析与解读，确保不漏过任何潜在威胁。

此外，**丰富的技战术储备也是优秀NDR不可或缺的一部分**。360 NDR智能体集成了ATT&CK和Killchain双模型，能够精准推导出资产、组织、攻击资源之间的复杂关系，为防御工作提供坚实的理论基础。

然而，仅有防御能力还远远不够。在攻防演练的激烈竞争中，加分项同样重要。**360 NDR流量智能体利用本地内置数十种安全AI小模型对数据进行深度分析，**识别出异常流量、恶意代码、弱口令、钓鱼邮件等安全威胁，确保能够迅速定位攻击源头，还原攻击全过程。

扣分少，加分多！听说部分区域下一阶段的攻防演练已经开始，希望各位蓝军战士们，在360NDR智能体的加持下，上分冲榜变王者！

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ●ISC.AI 2024周鸿祎：安全大模型要与安全业务深度融合 | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247573108&idx=1&sn=2739b368d965fe0ae4dd4319e17f0d23&chksm=9f8d4e7ca8fac76a06d8fac278c8289eade5b8df25d9c1b82ef9053101d55afe3bab84dde90a&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ● 亿级安全能力礼包免费ING | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247572983&idx=1&sn=9147a7f55e9a9c8afafc2fe4dac249c5&chksm=9f8d4dffa8fac4e92facb80ff7ec30700c688e13eb4035429d1c9666eb137147c92cd80a02bd&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● 揭露美国情报机构炮制内幕 “伏特台风”行动炒作真相 | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247572798&idx=1&sn=0574d1a9a4d18cba4d76f6a8d57b4d96&chksm=9f8d4d36a8fac420017cd3cd65b23bf947d0fb5e5d9364ab3beafd6815f5a752a98cf321e0a1&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 攻防演练正当时，360 AI军团已就位！ | | ► [点击阅读](http://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247572083&idx=1&sn=b79201d4c49fcf1074bc763ca03dee63&chksm=9f8d4a7ba8fac36d52ae82649d961032c3c0d3857f8e65d4311b595cfc944311fdfdb79b2170&scene=21#wechat_redirect) | |

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

360数字安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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