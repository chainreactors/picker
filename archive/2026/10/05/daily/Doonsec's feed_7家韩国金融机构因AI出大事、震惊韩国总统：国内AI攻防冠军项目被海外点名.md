---
title: 7家韩国金融机构因AI出大事、震惊韩国总统：国内AI攻防冠军项目被海外点名
url: https://mp.weixin.qq.com/s/MWDS_V5_PHq8nZHN54oleg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:23:17.546534
---

# 7家韩国金融机构因AI出大事、震惊韩国总统：国内AI攻防冠军项目被海外点名

# 7家韩国金融机构因AI出大事、震惊韩国总统：国内AI攻防冠军项目被海外点名

原创

网络安全透视镜
网络安全透视镜

网络安全透视镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

“

开源工具出现在攻击线索中 ，不等于它已经被证实参与攻击；但这件事足以提醒我们， AI 自动化正在重新放大外围系统的暴露风险 。

—— 网络安全透视镜

10 月 4 日，韩国总统李在明要求对近期银行、金融公司及相关机构的数据泄露事件展开彻底调查。公开报道显示，事件已经涉及新韩银行、KB 国民银行、韩亚银行、BNK 釜山银行、Yegaram 储蓄银行、Welcome 储蓄银行和现代资本等 7 家机构。

这起事件之所以引发安全行业关注，不只是因为受影响规模，还因为调查线索中出现了一个熟悉的名字：ARTEX — 自主渗透测试控制台。

一个月前，我刚写过这个拿下百度 Agent 攻防赛总冠军的开源项目,介绍过这个项目：[拿下百度Agent攻防赛总冠军、TSecBench跑分89.78：拆解AI自主渗透系统ARTEX的架构解析](https://mp.weixin.qq.com/s?__biz=MzIxMTg1ODAwNw==&mid=2247502798&idx=1&sn=b10c4834b71b1716dea55d027758056d&scene=21#wechat_redirect)

现在，它被韩国金融事件的公开报道点名了。

但文章开头必须先把边界说清楚：截至 2026 年 10 月 4 日，公开材料只能证明存在与 ARTEX 相关的间接线索，不能证明 ARTEX 已经被官方认定为攻击工具，也不能证明 7 起事件全部由同一个组织、同一种手法完成。

📌 本文看点

01

事件边界与关键数据

02

ARTEX 线索能证明什么

03

架构启示与防守重点

01

THE EVENT

### 先把这起事件的口径说清楚

这不是一场已经被完全调查清楚的单一攻击行动，而是一组在时间、目标和攻击迹象上存在相似性的安全事件。不同机构披露的受影响对象、数据范围和调查状态并不完全相同。

![](https://mmbiz.qpic.cn/mmbiz_png/lETfxQqKSMZKqn1c3UxDIZ6tqyRhmwLza8MKvqDWvwI929iaKVKunS2tMm6KUCXP7xZISr2zCyaRE7HTmTdE17glbKF7sABGFuGiaItxOiav4g/640?wx_fmt=png&from=appmsg)

— 根据公开报道整理的机构、攻击对象、数据类型与影响规模汇总。统计口径截至 2026 年 10 月 4 日，Welcome 储蓄银行的具体影响范围仍以调查和后续披露为准。

从公开报道看，较明确的信息包括：

1

新韩银行的一项贷款中介查询服务被绕过身份验证，约 2.5 万名客户的信息受到影响，涉及姓名、电话号码、年收入、贷款测算额度等内容，部分记录还包含居民登记号码和关联识别信息。

2

KB 国民银行、韩亚银行和 BNK 釜山银行的问题，集中在员工或外包人员使用的移动办公、营业支持等辅助系统。

3

Yegaram 储蓄银行涉及第三方解决方案程序的已知漏洞，攻击者被指通过漏洞植入恶意程序，并获取包含客户信息的日志文件。

4

Welcome 储蓄银行和现代资本也被纳入相关事件调查，但部分影响规模仍处于披露或核查阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/lETfxQqKSMbquvwd6c1LDyicFCiaVSh9IwEDuIlSicelqVCCygso3LXGmkj5VdM9PicccUglDthqE7YL9XgrquhvzgUYFicULlWKsvryTAMOzVUY/640?wx_fmt=png&from=appmsg)

— 新韩金融集团向美国 SEC 提交的披露文件截图。本文不对该文件的具体表单类型作额外推断。

重点：互联网银行和手机银行等核心客户服务尚未被确认受到影响；公开报道没有确认资金损失；不同机构的攻击 IP 和入侵路径并不完全一致。

韩国金融监管部门随后向约 500 家金融机构共享攻击 IP 和检查清单，要求机构核查外网暴露资产、访问控制和补丁状态。银行、信用卡公司以及证券、保险、储蓄银行和电子金融企业分别在 10 月 6 日和 10 月 8 日前完成阶段性检查，行业基础 IT 控制整改预计持续到 11 月。

![](https://mmbiz.qpic.cn/mmbiz_png/lETfxQqKSMYfwEr2hbsMju6E5ib6XkZUZkCg9ofMCTPZwmqlo0QMwfr0dOFuMkAdWduYop293pDt8NrusnAktMAJWzIggKVic05pNt9Luc8Z8/640?wx_fmt=png&from=appmsg)

— 韩国金融委员会紧急会议现场，图片来自公开报道。

02

THE EVIDENCE

### ARTEX 到底被发现在哪里

目前传播最广的线索，不是某个攻击者公开留下的账号，也不是一份官方报告直接写明“ARTEX 发起了攻击”，而是调查人员在部分 Web 服务器的 HTML 标题或相关基础设施线索中，看到了 ARTEX — 自主渗透测试控制台 这一字符串。

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPqHicwyx94b9S4H39H8Ra2QN6EHjetxkeferYia5ojUkLGyHydhNwwqCvhcojlpLLDQUJPCY82yddkA87ShOKBaY9N0SUalntzjM/640?wx_fmt=png&from=appmsg)

据公开报道，Genians 安全中心负责人文钟贤曾将其描述为一种间接证据：它可能说明相关环境曾运行过 ARTEX，或者与使用该工具的环境存在联系；但仅凭一个 HTML 标题，无法推出以下结论：

ARTEX 一定执行了这次攻击

7 家机构一定由同一个组织负责

攻击者完整使用了 ARTEX 的全部能力

所有入侵步骤都由 AI 自主完成，没有人工介入

![](https://mmbiz.qpic.cn/mmbiz_png/lETfxQqKSMatJ741moFAicvh99HrGPJQVgYZw4aJjIicc05BGIYibAyfm5zaGu0wzxm9D6loLNGjvlZkKFU63COldJgG4XL7qw2sIk8zWLwFxo/640?wx_fmt=png&from=appmsg)

— 银行安全事件概念示意图，不代表本次事件的真实攻击现场或取证画面。

这也是为什么我不愿意把标题写成“ARTEX 攻破了韩国银行”。更准确的表达应该是：

韩国金融事件的调查报道中出现了与 ARTEX 相关的间接线索，AI 工具是否实际参与攻击仍待官方调查确认。

ARTEX 本身是一个公开的开源项目，核心思路是让大模型和多个 Agent 协作完成资产收集、漏洞搜索、路径规划、工具调用和验证。在授权的安全测试环境中，这是一种自动化能力；如果被滥用，它也可能降低大规模探测和验证的操作成本。

但工具具备这种能力，和工具已经被用于某次真实入侵，是两件不同的事。

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPpFRlEPwqazzRjiaKpLEP2ZoS1wJPuRWBTYLjHbFKfvaiaxx5YibAjkHQJlRavDZRMKH266icicicoRfFiabLow5ibp7EST1YDmKnGRac0/640?wx_fmt=png&from=appmsg)

03

THE METHOD

### 真正的攻击面不是“AI 黑客”四个字

韩国金融监管部门公开归纳的攻击方式，至少包含三类，而且不能被简单压缩成“凭据填充”一种手法：

1

**缺少身份验证的信息查询服务**。某些服务能够在身份验证不足的情况下查询贷款申请、客户或企业相关信息。

2

**员工和贷款中介使用的辅助系统**。部分移动办公、营业支持或中介查询系统的访问控制没有达到核心交易系统的安全强度。

3

**已知漏洞与日志文件暴露**。某些网站服务器或第三方程序未及时修补，攻击者利用漏洞植入恶意程序，并进一步获取包含客户信息的日志。

一些评论把这类活动描述为“机会主义扫描”，也有人讨论了凭据填充的可能性。但就目前公开材料而言，不能把 7 起事件统一归因于 Credential Stuffing，更不能据此断言“主要手法就是撞库”。

更稳妥的判断是：AI 可能扩大了资产搜索、漏洞验证和目标筛选的速度，但真正造成数据暴露的，仍然是身份验证、服务端访问控制、补丁管理和敏感日志保护等基础控制失效。

这也是这起事件最容易被传播标题带偏的地方。把所有问题都叫作“AI 攻击”，反而会掩盖最实际的修复点。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m3tfzlbEQPp2ia19zAmudy6GhJjb9FX8vy06R6icWlIn6120IImCibNChRSrdrzMRvWcLvM88GxvMEJPd5DXtAx9HkZIxF3ZbIP0Hd7Dh5LhNI/640?wx_fmt=jpeg&from=appmsg)

04

THE ARCHITECTURE

### 为什么 ARTEX 架构会让人联想到这种场景

我在上个月的文章里拆过 ARTEX 的架构。按照项目公开资料和前篇文章的记录，它在百度 Agent+ 攻防能力挑战赛中获得了总冠军，TSecBench 盲测得分为 89.78。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m3tfzlbEQPrn4F4pYhs9GtTv4hMoicCsWib31gJHD07zrGNU3NqDaIl7WCzES57YurI7ArLDiaqUkvGv0Qb0Xfs3VNZruaLh6d98nQAr3LC33A/640?wx_fmt=jpeg)

— 前篇文章中的项目赛绩资料，不是韩国金融事件的取证证据。

它最值得分析的地方，不是“会不会调用某个工具”，而是把多 Agent 的探索过程组织成了可持续推进的状态机。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m3tfzlbEQPqN8U0Nq3KUyKpXVEh7xxO9Pggsm085gsQSnZAxOqM724b9zHXVXzSvdypEkdgUeMeNib9b6W7HfFT7cJ5AdSAGXXHl9OlicYbhI/640?wx_fmt=jpeg)

— 资产图与探索图双图状态机示意，来自前篇文章，不是本次事件的攻击链还原。

这套设计可以拆成两张图：

资产图

跨任务共享资产真值，包括根域、子域、IP、服务、应用和端点等节点。资产去重、父子关系和关联关系由数据库约束维护。

探索图

记录单个任务的目标、意图、事实、发现和提示，通过 spawns / derived\_from / yields / proves 等关系形成因果链。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m3tfzlbEQPrv0r9bBxzRZZHFiaojBLmzbsjSe2GYS3Qh7lUBTqIH2DKsYExXpMoOFo4ChRJgxYnnxh0d6NYMwib45Y3QjXqDxkSMFyZkomtIw/640?wx_fmt=jpeg)

— Planner–Worker 调度示意，图片来自前篇文章。该图用于解释项目架构，不代表韩国事件中的实际调度过程。

在调度层，Planner 根据事件变化推进任务，Worker 并发执行具体动作，数据库行级 CAS 负责抢单，过程记录还可以被其他 Worker 检索复用。这种架构理论上适合持续、并发、广覆盖的安全验证。

也正因为如此，当公开报道出现“多家机构、多个外围系统、多个国家和地区 IP、相似的攻击迹象”时，安全从业者自然会把它与自主化测绘和验证能力联系起来。

但这仍然只是架构能力与事件特征之间的技术类比，不是对攻击工具、攻击者或完整攻击链的事实认定。

05

THE DEFENSE

### 这次事件真正给防守方的提醒

这起事件最值得记住的，不是“AI 会不会攻击银行”，而是核心系统之外的那些服务，往往才是最容易被忽略的入口。

第一，盘点外网暴露资产

员工门户、贷款中介查询页、第三方解决方案、移动办公接口和调试服务，都应该进入统一资产清单，不能因为“不属于核心交易系统”就降低安全等级。

第二，服务端执行授权

查询客户、贷款、企业或员工信息的接口，不能只依赖前端隐藏字段、来源页面或网络位置。高敏感查询应启用多因素认证，并对每个对象执行服务端授权检查。

第三，优先修复已知漏洞

第三方程序、网站服务器和远程办公组件一旦长期暴露在公网，补丁状态就应该成为持续监控指标，而不是发生事件后才集中排查。

第四，减少日志中的敏感信息

日志不应该成为客户身份证件、联系方式和业务详情的第二份数据库。必须进行字段脱敏、访问隔离、最小化留存，并对异常批量读取建立告警。

第五，用自动化监测自动化攻击

资产发现、异常枚举、跨地区 IP 轮换、短时间内的大量查询和重复错误码，都适合通过自动化规则和模型辅助发现；但 MFA、补丁、访问控制和数据最小化仍然是最先要做的事情。

∞

THE END

### 写在最后：先把证据和想象分开

目前最准确的结论不是“AI 已经攻破韩国银行”，而是：韩国金融机构发生了一组涉及外围和辅助系统的数据安全事件，公开报道中出现了与 ARTEX 相关的间接线索，AI 工具是否实际参与、参与到什么程度，仍在调查。

这件事提醒安全行业两点：一方面，开源 Agent 和自动化安全工具的能力扩散速度，确实值得认真讨论；另一方面，任何新技术都不能替代对身份验证、补丁管理、对象授权和敏感数据保护的基本投入。

技术评价和技术影响，是两套坐标系。ARTEX 的架构设计可以很有价值，但不能因为它出现在一条报道线索里，就跳过证据链直接完成归因。

如果你也在做 Agent 安全或企业防守，欢迎在评论区聊聊：当自动化能力越来越强，组织最应该先补上的，究竟是哪一道基础控制？

事件时间线

9 月 30 日

新韩银行公开披露贷款中介查询服务相关安全事件。

10 月 2 日前后

韩国安全行业公开讨论部分 Web 服务器 HTML 标题中的 ARTEX 字符串线索。

10 月 4 日

公开报道将涉及机构扩大到 7 家；韩国金融监管部门召开紧急会议，韩国总统李在明要求彻底调查。

10 月 6 日、10 月 8 日

监管要求不同类别金融机构分别在上述日期前完成阶段性外网资产、访问控制和补丁检查。

11 月

金融行业基础 IT 控制整改和自查继续推进。

参考来源

韩国 ChosunBiz：https://biz.chosun.com/en/en-finance/2026/10/04/JULRT3U25NG47AICMCH76TE5TY/

AJU Press：https://m.ajupress.com/view/20261004152058987

ARTEX GitHub 项目：https://github.com/Autumn-27/ARTEX

前篇架构解析：https://mp.weixin.qq.com/s/Bv0eVA64YjVtdL7pxO18cg

本文按 2026 年 10 月 4 日前后可检索到的公开报道整理。ARTEX 与本次事件的关联尚未获得官方最终确认；文中的架构图来自前篇文章，银行安全事件概念图仅作示意，不代表真实攻击现场。

END

我是网络安全透视镜，持续关注 AI 攻防、Agent 架构与安全技术拆解。

如果你觉得今天这篇有收获，欢迎**点赞、在看、转发**三连，我们下篇见。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS4XfIhhBCwvehx3nP0V2gBqhs9I9AU7GWibxufhGXcjLMNMk2ia7ibpBibhD1qJLmNDcwAGiaTIgyFVQAw/0?wx_fmt=png)

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