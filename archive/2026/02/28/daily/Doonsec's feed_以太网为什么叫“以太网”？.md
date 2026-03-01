---
title: 以太网为什么叫“以太网”？
url: https://mp.weixin.qq.com/s/Zog4kpmz7zmsI4anHYgjZQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:26:50.275379
---

# 以太网为什么叫“以太网”？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Dibzmm9niba06tEPxPiauKjicESByaxGKxKcVEAWlvEaVmsyWlp1ScI0d5vQV448qb0Z6Ke7LDb32baZpibICTgicNVvoHh1p0QbJKschicYt2kYaA/0?wx_fmt=jpeg)

# 以太网为什么叫“以太网”？

原创

你信任的
你信任的

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYQNIyABHZrCWcZT6asQr23iaO5wvXibL4CtruQ1E2AY6iaaH3X4LxMnSrBXvjhQND7Y4ibRahz9FhPVBw/640?wx_fmt=gif)

> 公众号：网络技术联盟站

每天我们都在跟“Ethernet”打交道：服务器网卡插的是Ethernet，交换机跑的是Ethernet，数据中心Spine-Leaf架构底层还是Ethernet。从10M同轴电缆到今天的400G/800G光模块，以太网早已成为现代数字世界的“血液”。

可你们有没有好奇过：**为什么叫“以太网”？** “以太”这个词听起来像玄学，为什么不叫“局域网”或“电缆网”？今天这篇文章，带大家穿越时空，从19世纪物理学家的“光以太”假设，一直到Bob Metcalfe在Xerox PARC的1973年备忘录，再到我们公司AI训练集群的800G链路，一次性讲透这个名字背后的传奇故事。看完后，你再也不会觉得“Ethernet”只是个普通技术名词，而是会感慨：一个“不存在”的物理概念，竟然定义了整个互联网时代！

![1973年Bob Metcalfe在Xerox PARC办公室，正是他写下Ethernet备忘录的时刻](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba04JBdvC4MwmeV6xe9Z5Babdc5s0hlNFC7uDicPo9dDgJChSdiaALZ3X2oJmbC26FL8pJomWTOSW3TRZlfHVykQbwZ92uwaSGia0qw/640?wx_fmt=png&from=appmsg)

1973年Bob Metcalfe在Xerox PARC办公室，正是他写下Ethernet备忘录的时刻

一切要从1973年说起。那一年，美国Xerox公司帕洛阿尔托研究中心（PARC）有一位年轻工程师叫**Robert Metcalfe**（鲍勃·梅特卡夫）。当时PARC正在开发世界上第一台个人计算机——Xerox Alto。Alto有图形界面、鼠标、激光打印机，但这些“神器”彼此孤立，无法联网共享文件和打印。

Metcalfe的任务是把它们连起来。他先做了一个实验网络，叫**Alto Aloha Network**。这个名字来自夏威夷大学的**ALOHAnet**——世界上第一个无线分组无线电网络（1970年）。ALOHAnet用无线电波在岛屿间传输数据，节点像广播一样“喊话”，听不到回应就重发。

Metcalfe深受启发，但他不想只服务Alto计算机。他希望这个网络能连接**任何**计算机。于是1973年5月22日，他给老板写了一份著名备忘录，正式把网络改名为**Ethernet**。

为什么是“Ethernet”？Metcalfe后来回忆：在备忘录里，他把共享的物理介质（当时是同轴电缆）比作“以太”（ether）。就像19世纪物理学家认为“光以太”是一种无所不在、无形的介质，能被动传播电磁波一样，以太网的电缆也把数据比特“被动”广播给所有连接的站点。

![晚年Bob Metcalfe手持以太网电缆，象征他发明的“以太”介质](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05oK1OAC4ic4BsDtg0SLbyxFibicAcoI6tmvopKy3xMphsf9gkeN927Ko6F7vor5aMPZ6NHQgcBYnp4KLXkhzNv2BL3zwpI4AKJq4/640?wx_fmt=png&from=appmsg)

晚年Bob Metcalfe手持以太网电缆，象征他发明的“以太”介质

英文原话出自O'Reilly经典著作《Ethernet: The Definitive Guide》：“He chose to base the name on the word 'ether' as a way of describing an essential feature of the system: the physical medium (i.e., a cable) carries bits to all stations, much the same way that the old 'luminiferous ether' was once thought to propagate electromagnetic waves through space.”

翻译成大白话：**数据像光波一样，在‘以太’这种看不见的介质里被动传播给所有人**。这正是以太网早期“总线拓扑”的精髓——所有设备挂在同一根电缆上，数据像广播电台一样发出去，大家都能听到。

中文翻译“以太网”非常精准，“以太”就是“ether”的音译+意译，完美保留了历史韵味。

## 19世纪的“光以太”

“以太”这个词可不是Metcalfe瞎编的，它来自物理学史上的著名假设——**luminiferous aether**（发光以太）。

19世纪，科学家知道光是电磁波（Maxwell方程），但波需要介质传播，比如声波在空气中。水波在水里。那光在真空中怎么传播？于是大家假设宇宙中充满一种无质量、无摩擦、透明的“以太”，光波就是以太的振动。

牛顿、麦克斯韦、洛伦兹等大牛都相信以太存在。1887年Michelson-Morley实验本想证明以太“风”，结果测到零漂移，后来爱因斯坦狭义相对论直接说“以太不需要存在”，光速在真空中恒定。

以太被科学界“枪毙”了，但Metcalfe借用这个概念，简直神来之笔！因为早期以太网确实像“以太”一样：

* **被动**：电缆不主动处理数据，只是传输
* **广播**：一个站点发包，全网都能收到（靠MAC地址过滤）
* **无所不在**：任何设备插进去就能“感受到”网络

这个名字一出，瞬间让技术有了哲学感和诗意。Metcalfe后来开玩笑：“以太网的‘以太’就像幽灵，物理学家说它不存在，但我们让它活在了网络里。”

![以太网速度演进时间线，从1980年10Mbps到2030年可能1.6Tbps，名字却从未变](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba06jF1QbvKpaFkYSx9a0jvm5f5HjEzmZjJFwnUicn1C4ibbHiaBEZynB52JAAbLU5lkEgiawTfH3ZRsvy0tz66AxfLW0BymG9PiaAuCU/640?wx_fmt=png&from=appmsg)

以太网速度演进时间线，从1980年10Mbps到2030年可能1.6Tbps，名字却从未变

## CSMA/CD

早期以太网（10BASE5粗缆、10BASE2细缆）采用**总线拓扑**，所有设备共享同一根“以太”电缆。这就带来碰撞问题：两个站点同时发数据，就像两个人在同一根电话线上同时说话。

Metcalfe的伟大发明是**CSMA/CD**（Carrier Sense Multiple Access with Collision Detection）：

1. **Carrier Sense（载波侦听）**：发包前先听听“以太”上有没有别人在说话（电压变化）
2. **Multiple Access（多点接入）**：大家都可以接入
3. **Collision Detection（碰撞检测）**：发包过程中如果检测到碰撞，就立即停止，发“JAM”信号，然后指数退避重发

这套机制完美对应“以太”概念：你得先“感受”以太里的信号，才能决定是否说话。

![CSMA/CD协议流程图，经典“监听-发送-碰撞重发”](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04ClNDiabUduzficQXj65WaXYxN4hkjhEDQY6j1uol3znNPDuiaEzpp2ZaLWaqRkQ5t0pOw0tnhSExibEQKhE5WgVa9CEGTk7tjvkg/640?wx_fmt=png&from=appmsg)

CSMA/CD协议流程图，经典“监听-发送-碰撞重发”

今天我们用交换机全双工，已经没有碰撞了，但CSMA/CD的灵魂仍活在半双工和无线Wi-Fi（CSMA/CA）中。

## 从Xerox到IEEE 802.3

1979年Metcalfe离开Xerox创办3Com，联合DEC、Intel、Xerox（DIX标准）推动标准化。1980年9月30日，第一个以太网标准提出。1983年IEEE正式发布**802.3**标准，从此“以太网”成为通用名词。

有趣的是：早期以太网是“黄电缆”（10BASE5，10Mbps，500米），粗如手臂，安装要用“吸血鬼夹”刺破电缆。Metcalfe曾说：“我们当时以为这玩意儿能卖几百套就够了。”

谁能想到，今天全球99%的有线局域网都是以太网！

![早期以太网硬件实物，同轴电缆+收发器，奠定“以太”介质基础](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06pkqJZ9KS8UUUiaVKyyVckibwqMBZ1Uz8zOv6ZVjZavWZ3Y94Dm2GsKnlJ84kibqWXeaUEZ1e63Bz4Wu5by0cVwnhqPjAeIfzVfs/640?wx_fmt=png&from=appmsg)

早期以太网硬件实物，同轴电缆+收发器，奠定“以太”介质基础

## 为什么“以太网”活了50年没被换掉？

对比其他技术：

* Token Ring（令牌环）——IBM推，但名字太技术化，已消亡
* ARCNET——名字枯燥
* FDDI——光纤分布式数据接口，太长

“以太网”简洁、上口、有历史底蕴。哪怕从共享总线进化到交换式、从铜缆到光纤、从10M到800G，底层仍是“以太”精神：**简单、可靠、兼容**。

![400G以太网交换机集群，现代“以太”仍在高速进化](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05Ixy4N0H1Qrqw0udyLsfWWkEToRlglfcCuvmzu0vBKLicRyia2qyMibw4pia5QDz4iaZWQmpiakX0ibSMTJgVFmEibiaYHqTt3dScnrJoc/640?wx_fmt=png&from=appmsg)

400G以太网交换机集群，现代“以太”仍在高速进化

Metcalfe还提出了**Metcalfe定律**：网络价值与节点数平方成正比。这进一步巩固了以太网的统治地位。

**喜欢就****分享**

**认同就****点赞**

**支持就****在看**

**一键四连，你的技术也四连**

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYRJ20XxicqZhK1qicQFqicZN3BDMEIvovHPnsWicnRgkibCNOtcZf7icVkErP0b18JZia29GVKLkhR5IJ1ibQ/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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