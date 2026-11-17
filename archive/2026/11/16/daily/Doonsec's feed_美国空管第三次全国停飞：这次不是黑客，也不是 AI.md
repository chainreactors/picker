---
title: 美国空管第三次全国停飞：这次不是黑客，也不是 AI
url: https://mp.weixin.qq.com/s/TgK8uXHtvJJH2Vp2eMnY0g
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:53:14.415702
---

# 美国空管第三次全国停飞：这次不是黑客，也不是 AI

# 美国空管第三次全国停飞：这次不是黑客，也不是 AI

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

**↓****以下为文字阅读版**

11 月 13 日，美东时间下午 3 点 36 分，美国空管的雷达与通信数据开始“不稳定”。

18 分钟后，联邦航空管理局（FAA）发布指令：全美所有机场，暂停起飞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZiaZ63PiczNyhR5haiazmQufIZU87fZK4gcmBN9iatOlyx8qhrq22tI2RarrQa8vX2Ra4HJ0USeiaIriaHXZeXM5b6PT7DZRiaMbTyu4A/640?wx_fmt=png&from=appmsg)

当时空中有 3,500 多架飞机。它们继续飞，继续降落，一架接一架被安全接回地面；而地面上，离港通道被整体关闸——除了医疗、关键货运和执法飞行，几乎没有航班被放行。直到晚上 8 点 15 分，指令解除。整整 4 小时 40 分钟，美国空域没有正常放行一个离港航班 。

这是美国历史上第三次全国停飞。前两次，是 2001 年 9 月 11 日，和 2023 年 1 月 11 日的 NOTAM 系统故障。

而这一次的起因，听起来近乎荒诞：一个偏远机房里，一台正在更换的路由器。

## 数据洪水：每 4 到 5 秒，1000 次连接尝试

出事的那张网叫 FTI——FAA 电信基础设施。它不属于某家航空公司，也不属于某个机场，而是把全国塔台、雷达站、管制中心串起来的骨干网，跑的是语音、雷达、气象和飞行数据。

这张网由防务承包商 L3Harris 运营。按交通部长肖恩·达菲（Sean Duffy）的说法，网络甚至是 L3Harris 自己的资产，这家公司为 FAA 干了二十多年。它连接着 4,400 多个设施，支撑每天约 4.5 万个航班。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhrlibHWfM1It4Coo0C3tLScbd1m5oOiaHNr0Rk5VIpbNUlH0Kjnl4AdjtR0dmkaewA9TWrfsqMPmYdISquViaMB8dBNAR055HEdw/640?wx_fmt=png&from=appmsg)

11 月 13 日下午，L3Harris 在一个偏远站点做例行维护：把老化的铜缆换成光纤，从 TDM 转向 IP，从模拟转向数字。达菲在发布会上反复强调这件事有多普通——“美国几乎每一家机构都完成了铜转光纤，也许 FAA 是最后一个，因为过去没人愿意投钱”。

然后，新换上的那台路由器开始“发疯”。

“它开始向空管系统里的其他路由器灌数据。具体来说，每 4 到 5 秒，就有超过 1000 次连接尝试。”达菲说，这导致与飞机的通信出现问题，雷达数据也受到干扰。

注意这里的措辞：不是“断了”，是“灌”。一台设备持续、高频地敲邻居的门，把邻居的控制面资源吃到饱和，然后整张共享网络开始输出前后矛盾的数据。

从工程角度看，这类故障并不神秘（以下是技术分析，不是官方结论）：设备在反复尝试建立某种会话或邻居关系，失败就立刻重试，形成高频风暴；吃掉的是路由器的 CPU、会话表和邻居状态机，而不是带宽。所以外行看到的现象是“网没断，但数据不对”。如果缺少速率限制、路由抖动抑制和足够的隔离策略，异常就会从一个远端站点扩散到整个共享域 。

代表 FAA 安全人员的工会 PASS 事后表示，问题被锁定在周五更新的两台路由器上，而他们代表的技术人员并未参与此次升级作业；一名官员对路透社说，这两台设备据信位于阿肯色州和得克萨斯州。

据信位于阿肯色与得州的两台偏远站点路由器，最终波及 22 个航路管制中心中的 17 个。FAA 的隔离，显然没兜住。

## 为什么不能“绕开几个坏掉的中心”

这是整件事里最容易被低估的一段。

如果只是几条链路断了，管制员立刻就知道：这条线没了，切备用、限流、局部绕行。但这次是数据本身不可信。屏幕上还有数字，只是这些数字可能是错的、互相矛盾的、滞后的。你没法判断该相信哪一个。

“我们的交换机、路由器被数据淹了，开始给出不一致的数据，所以我们关掉了系统。”达菲说。

于是 FAA 选了最保守的一条路：全国停飞，把空中的飞机先安全落下，再定位问题。

这个决定背后还有一个尴尬的细节。FAA 局长布莱恩·贝德福德（Bryan Bedford）说，他们花了大约 45 分钟排查系统为什么不稳定，没查出来。原因之一，是这类维护作业在 FAA 这边**仍然靠纸质登记**——技术人员得翻着一摞纸，才能确认到底谁在哪个站点动了什么 。

45 分钟之后，全国停飞令下达。贝德福德后来补了一句很重要的澄清：“没有任何设施全黑，没有任何东西完全丢失。”

也就是说，这不是一次“空管瘫痪”，而是一次“不敢再信”的自锁。从安全的角度，这个选择无可指摘——3,500 架飞机全部安全落地，没有发生任何事故。但从系统设计的角度，它暴露的问题比故障本身更值得看：一个国家的空域，被一台路由器的重试风暴按停了近五个小时。

## 第三次：一次是 9·11，一次是误删文件

把三次全国停飞排在一起看，会发现一个不太舒服的规律。

2001 年 9 月 11 日，是外部袭击。

2023 年 1 月 11 日，NOTAM 系统（给飞行员发航行通告的系统）故障。FAA 的初步结论是：合同人员在修正主数据库与备份数据库同步时，“无意删除了文件”。当天早上 7 点 15 分停飞，9 点 07 分解除，超过 1.1 万个航班受影响，同样没有网络攻击证据。

2026 年 11 月 13 日，铜转光纤维护，路由器异常，全国停飞 4 小时 40 分钟。

三次里，有两次的起因都是“维护”。不是黑客，不是恐怖袭击，是人按流程去动一个正在服役的系统。

2023 年那次之后，FAA 加了两道护栏：给主备数据库之间加同步延迟，确保坏数据不会污染备份；以及要求数据库操作时必须有两个人在场、互相监督。

三年多以后，另一场维护事故里，被翻出来的是纸质工单。

## 三天前，AI 刚刚“全国上线”

现在说那个让这件事在中文互联网上格外有传播力的巧合。

9 月 21 日，FAA 在华盛顿特区空域“有限模式”启用了一套叫 SMART 的系统——战略空域、航路与轨迹管理（Strategic Management of Airspace, Routes and Trajectories）。它把大约 200 路数据（天气、航路、流量、管制员排班）汇到一个平台，由“AI 支持的引擎”给出建议，帮 FAA 从“事后反应”转向“提前预测”。

11 月 10 日，FAA 宣布 SMART 扩展到全美 22 个航路管制中心。

11 月 13 日，全国停飞。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhgga8qQ0wCqMTCm3WNE8ZlobjyMBiaS6LkUzVYnqtMgjkErQ1eEVeAldsyiaybiaSibNbibCyNaiakP7cnJLHheMaYYPX419LuiamuDI/640?wx_fmt=png&from=appmsg)

三天。这个时间差，足够让任何一个人在社交媒体上打出“AI 把空管搞崩了”。

但这条推断是错的，而且官方在事发当晚就把它掐掉了。

达菲的解释很具体：SMART 只是给管制员和流量管理提建议，所有建议都要经过 FAA 人员审核，地方管制机构可以接受也可以拒绝；更关键的是，SMART 根本没有接入 STARS 或 ERAM——那两个才是直接支撑终端与航路管制的自动化系统。“SMART 不可能影响到发生了什么。”

国安部长马克韦恩·穆林（Markwayne Mullin）的说法更直接：目前“零证据”表明事件源于网络攻击或“失控的 AI 系统”，但也没有完全排除，调查仍在进行。SMART 的开发商 Air Space Intelligence 同样否认其技术与此有关。

所以，这是一个巧合。而且是一个必须被明确指认为巧合的巧合——把两件在时间上相邻、在技术上不相干的事写成因果，是这类事件报道里最常见、也最有害的错误。

但巧合之外，还有另一条线索，它不是巧合。

10 月 9 日，20 多名议员联名致信交通部和 FAA，要求暂停 SMART 在华盛顿地区的初始推广，直到安全评估、人员培训与监督机制的问题得到回答。他们追问的是：原定的 90 天评估期怎么做的？达到什么标准才能全国推广？

11 月 10 日，FAA 宣布全国扩展。那份公告没有回应这些问题。

这就是“监管疑云”的真实形状：不是“AI 导致了事故”，而是**一套 AI 系统在评估问题尚未公开回答的情况下，用七周时间从区域试点走到了全国覆盖**。它的推荐不直接控制飞机，风险等级和自动驾驶完全不同；但“建议”本身会改变流量、改变排班、改变人的决策节奏，而这些影响该怎么评估、谁来审、出了问题怎么回滚，公开信息里几乎是空白。

巧合不需要解释，治理缺口需要。

## 真正的脆弱，藏在“正在变新”的过程里

如果只记住一个数字，记这个：5,170。

这是 FAA 全国范围内 1960 年代铜缆连接的数量。政府问责局（GAO）9 月 14 日的报告显示，截至 2026 年 5 月，其中只有 2,560 条换成了光纤——不到一半。同一份报告还写了另一件事：FAA 手上不是一份整合的现代化总进度表，而是 11,389 个彼此独立的项目进度表，很多安装作业被排到同一个站点，却没有统筹优化以减少对管制运行的影响。

GAO 的原话说得很克制：这些风险会提高 FAA 重复“超支、延期、未达标”历史的可能性。TechSpot 对这份报告的概括更刺耳——FAA 正在“用交付速度换取……潜在中断的风险”。

这不是事后诸葛。2024 年 GAO 就报告过，FAA 的 138 个空管系统里，超过 75% 已不可持续或潜在不可持续。今年 9 月，新泽西州一支施工队挖断光纤，导致东北部航班被暂停。两个月后，是一次更彻底的路由器事件。

而讽刺的地方在于：达菲反复强调，“所有新装的设备，一台都没倒。倒的全是存在了很多年的老设备”。

从系统可靠性的角度看，这几乎是教科书式的场景：**系统最容易出事的时刻，不是它最老的时候，而是它正在变新的时候。** 因为改造意味着在带电的、不能停机的系统上动手；意味着新旧两种技术范式（TDM 与 IP）要在同一张网里共存；意味着变更窗口、回滚方案、隔离边界、双人复核，每一个环节都不能靠“老师傅记得”。

而这一次，变更记录是纸。

## 钱、责任，和下一次

事故之后的华盛顿，迅速进入了熟悉的流程。

达菲把预算请求从 300 亿美元提到了 500 亿美元，说“这是紧急状态” 。国会去年已经批了 125 亿美元。民主党议员里克·拉森和安德烈·卡森回应说：拿到 125 亿之后，交通部授出了 43 亿美元合同，实际只花了 10 亿美元。

L3Harris 表示会认真对待此事、配合调查，股价盘后跌了约 4%。达菲的表态则留了一半余地：“我们需要 L3Harris，或者任何给我们提供那台路由器的人，做得更好。”

至于根因，还没有答案。可能是安装或操作失误，可能是设备本身故障，FAA 说会在调查完成后公布根因分析报告。据彭博社报道，FBI 正在核查“软件更新是否有关”，但不认为存在网络攻击或犯罪行为。事发当天，白宫在战情室开了紧急会议；据国安部长穆林的说法，NSA、国防部、CISA 等机构都参与了调查。

对普通旅客来说，这件事的余波是具体的：周五约 9,200 个航班取消、7,500 个延误；周六再取消 6,400 个、延误 8,000 个；至少 827 个航班被迫改航。而且因为是 FAA 的系统故障、不是航空公司的责任，美国航司没有法定义务为滞留旅客提供补偿。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgjMvoCrGzQmXeURYJRoFufJGzUcgJkEFGLxPNNKibU7YODib4RrBkb6TRTvE0hbt0BpSMpww4RGaE1ic9UexFKwU04IN4TVUun2c/640?wx_fmt=png&from=appmsg)

对技术人员来说，余波应该是另一个问题。

过去二十年，我们习惯把“关键基础设施的风险”想象成两种：老得掉渣，或者被黑客打穿。这次两样都不是。它是一次计划内的、事前做过安全评估的例行维护；出问题的设备，是一台刚换上去的新路由器；按下的，却是整个国家的暂停键。

真正的教训可能很朴素，也很难听：**当一个系统正在被加速替换时，变更管理的重要性不低于新技术的先进性。** 灰度发布、速率限制、故障域隔离、可回滚、双人复核、把纸面工单变成可审计的数字记录——这些都不性感，也不会出现在任何一场“AI 重塑空管”的发布会上。

但下次让全国航班停在地上的，大概率还是它们中的一个。

---

## 参考资料

1. A network crash grounded every flight in the US, only the third time in history
2. No Signs of Hacking in FAA Ground Stop as FBI Reportedly Probes Software Update
3. ICYMI: U.S. Transportation Secretary Sean P. Duffy Provides Update on Restoration of Airspace Following Nationwide Ground Stop
4. US air travel disruptions to persist until late on Sunday, FAA head says
5. US to resume flights after air traffic network failure sparks chaos
6. FAA blames telecommunications issue for nationwide ground stop
7. FAA contractor, router focus of investigation into air traffic halt
8. Trump's Transportation Secretary Sean P. Duffy Delivers State-of-the Art Air Traffic Control Management Tool
9. FAA Rules Out SMART AI System as Cause of Nationwide Ground Stop
10. FAA Expands AI-Assisted Traffic Management Nationwide
11. Air Traffic Control Systems: Ambitious New Modernization Effort Needs to Improve Cost and Schedule Planning (GAO-26-107992)
12. FAA NOTAM Statement
13. U.S. FAA says 'unintentionally deleted files' prompted computer outage
14. Statement of Billy Nolen, Acting Administrator, FAA — NOTAM System

- END -

**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZj0vZ4HI9JCibQwzj9ZHia88e3thicG9MD8BG7hfmbSq8EeqG0WROTia6wbHU9BYw0kZjo37eohmhibDUgJKMPXXgRe4COyEQoYjwWA/0?wx_fmt=png)

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