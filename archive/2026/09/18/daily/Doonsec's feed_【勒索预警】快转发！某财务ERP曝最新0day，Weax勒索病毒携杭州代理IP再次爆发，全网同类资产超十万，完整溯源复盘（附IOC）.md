---
title: 【勒索预警】快转发！某财务ERP曝最新0day，Weax勒索病毒携杭州代理IP再次爆发，全网同类资产超十万，完整溯源复盘（附IOC）
url: https://mp.weixin.qq.com/s/CeamGBWwohwgcfBS9fC9EQ
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:57:11.593470
---

# 【勒索预警】快转发！某财务ERP曝最新0day，Weax勒索病毒携杭州代理IP再次爆发，全网同类资产超十万，完整溯源复盘（附IOC）

# 【勒索预警】快转发！某财务ERP曝最新0day，Weax勒索病毒携杭州代理IP再次爆发，全网同类资产超十万，完整溯源复盘（附IOC）

原创

州弟学安全
州弟学安全

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

## 写在前面

本文首发于**Solar应急响应团队-「州弟学安全（徐龙州）」**，转载请务必注明出处。

Solar应急响应团队由思而听（山东）网络科技有限公司组建，长期专注勒索病毒应急响应、攻击溯源与数据恢复，为遭遇突发勒索事件的企业提供7×24小时突发危机干预通道。如企业正在遭受勒索攻击，可通过**应急响应.cn(****https://solarsecurity.cn/****)、** 或 **应急响应.com(****https://www.solarert.com/****)** 联系我们。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbQsRVlqJgib48x54pSQKKLvhXLxL6bB1yuXyejBeRDEre13uINtXUM2xo88micj1zYbBsAU1zfiadoMuX7icBCdVtJhfV7vvJLoZ0/640?wx_fmt=png&from=appmsg)

应急响应.cn平台Weaxor勒索家族特征查询，标注家族名称、加密后缀、勒索信样式等关键字段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQb8xXia0tXGgz9lOQzWS4QccN0nQYPjPNSKicZyaV4ZavkYVotAX2Lfv4Se3MhXSFHibqvRuPoVpyaNxscaicVntzekQ3jjzTeUYiac/640?wx_fmt=png&from=appmsg)

应急响应.com平台Weaxor勒索家族特征查询，标注家族名称、加密后缀、勒索信样式等关键字段

先交代一下这起事件的背景。Weaxor勒索家族（Rox、Weax、Roxeaw）的攻击目标非常明确，就是国内中小型企业。截至目前，在我们累计处置的近700起勒索应急案例中，中小型企业占比约八成，其中相当一部分与Weaxor家族有关。这类企业的共同点是防护能力薄弱、安全投入有限、业务系统直接暴露公网，对攻击者而言是投入产出比最高的猎物。

我们一直在持续跟进该家族的攻击事件。六月底，我们发布了Weaxor与TellYouThePass两大家族借管家婆软件攻击国内中小企业的全链路复盘《[【全网首发】Weax与Sorry勒索病毒席卷全国中小企业，深度还原全链路攻击，疑似黑客利用AI挖掘管家婆0day漏洞](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247510579&idx=1&sn=c8ddda3466a9fc0b75f1121ad96b24c4&scene=21#wechat_redirect)》，随后又发布了《[【勒索预警】某ERP曝0day漏洞致Weax勒索病毒在国内爆发，波及资产近4万台（合并修订版）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247511937&idx=1&sn=0b2a89e4a0ab893a71eea71c15d14305&scene=21#wechat_redirect)》。上周，我们发布了该家族改用国内IP发起0day攻击、某地产ERP遭加密的完整复盘《[【勒索预警】警惕！Weax勒索病毒改用国内IP发起0day攻击，某地产ERP遭加密，完整溯源复盘（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247512969&idx=1&sn=bc8ace54cffcaf17252e7c8da0ecb05d&scene=21#wechat_redirect) 》。本文是这一系列的最新一起勒索攻击案例。

梳理该家族近一年的攻击轨迹，可以看到一条清晰的分界线。从开始活跃到2026年6月，其攻击入口几乎全部来自护网期间流出的1day、Nday漏洞；进入7月以后，入口开始转向应用系统的0day，且从软件公开可获取到漏洞投入实战的周期被压缩得极短。这些0day从何而来，是AI辅助挖掘、漏洞交易购买，还是源码泄露后的定向审计，目前没有定论，我们会继续跟踪。结合攻击时段、国内代理池的使用方式与作案流程的熟练程度，我们判断该家族背后大概率为国内人员在操作。关于Weaxor家族的加密后缀、勒索信样式等更多细节，可以在应急响应.com上直接查询，此处不再展开。

还需要说明一点。本周正值国家网络安全宣传周，各行业都在开展安全意识宣贯，而该家族对国内企业的攻击并未收敛，反而在这个时间节点保持高频出手，本文披露的案例正是我们近期处置的一起。选择现在公开完整溯源过程，一是提醒仍在使用同类系统的企业尽快自查，二是把攻击者如何绕过官方防护的手法讲透，让防守方看清自己的防线为什么会失效。

## 阅读说明

按照惯例，本文对受害企业名称、受害资产地址及ERP厂商名称做脱敏处理，配图中的敏感信息已打码。为避免攻击代码扩散，本文不公开完整的可利用载荷，仅展示无害探针与防护验证过程，技术细节以讲清原理为限。

先看影响面。通过资产测绘平台对该ERP相关指纹进行检索，命中资产超过十万条，独立IP四万七千余个。对一款承载财务与核心业务数据的ERP而言，这个暴露面意味着任何一次0day的实战化，波及范围都不会小。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZ037rcQNLZ4pRB3ZPX0JEx3QLZZmaSibPH1jrv17q3v2e6bicVLxpO94vQLMOdmsTSYjNlicRiaEIRBGv13VhfKpqe2I3e6vzHHOw/640?wx_fmt=png&from=appmsg)

资产测绘平台对该ERP相关指纹的检索结果，命中100,993条，独立IP 47,514个（敏感信息已打码）

## 一、攻击时间线还原

### 1.1 时区换算说明

受害站点的IIS访问日志默认使用UTC时区，Windows系统日志使用UTC+8本地时间。下文凡涉及IIS日志与系统日志对照之处，均按"IIS日志UTC时间加8小时等于本地时间"进行换算。

### 1.2 事发前的持续扫描探测（8月22日至8月29日）

勒索事发前一周，多个浙江杭州代理IP对受害站点发起针对性的反序列化漏洞扫描。从IIS日志看，扫描请求集中指向**SaveReport.common.kdsvc**接口，请求的User-Agent均为**WindowsPowerShell/5.1.26100.8655**，请求之间间隔数小时至一天不等，期间未伴随加密器落地等实际入侵行为，判断为自动化脚本的漏洞探测，攻击者在确认目标可利用后才投放加密器。逐条记录如下。

2026年8月22日 19:23:00（本地时间，对应IIS日志UTC时间11:23:00），攻击者IP 36.137.66.81 对受害站点8013端口发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQb094ibvtgZODca3IudSpVA4pueISIiawdhiaKvR6GGcAFXEUghicXubBew2bSIOUE7ep5DLX9VuyFpbAiaudS1FvAUUufM6IfQUic9I/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-22 11:23:00（UTC）36.137.66.81对SaveReport.common.kdsvc接口的扫描请求（高亮行），User-Agent为WindowsPowerShell/5.1.26100.8655

2026年8月22日 19:45:06（本地时间，对应IIS日志UTC时间11:45:06），攻击者IP 36.137.66.31 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQaljGaiaVSg2nibtTicMnKUhRia4RVV5TdRnQ80DT6GnH15vKYbrZq4GdMLkqDjgymjC6o2qbh4n2oB8LFRiasL7XTEGNavdBTyONZk/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-22 11:45:06（UTC）36.137.66.31的扫描请求（高亮行）

2026年8月22日 20:00:36（本地时间，对应IIS日志UTC时间12:00:36），攻击者IP 36.134.184.170 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZJ9tiak0nIia58TnO9plZ4YzTnltbCBOK5HlGctWyUZvElU9tY4yElTTaqUR6iah4VyPKm9NtfZ6lwmHkyHTlMyWKH3bwyJfdMlg/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-22 12:00:36（UTC）36.134.184.170的扫描请求（高亮行）

2026年8月23日 19:36:17（本地时间，对应IIS日志UTC时间11:36:17），攻击者IP 36.137.66.114 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYZlJFvCibE0AcuMewyFicrk8cDPo5vjx57hOicmm0nHK7TV0Kia9u7pFefiaANDSABA9BdGrKjUj3KkxkGjnBwcnFHiaYWDTK67J0Cw/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-23 11:36:17（UTC）36.137.66.114的扫描请求（高亮行）

2026年8月24日 19:18:29（本地时间，对应IIS日志UTC时间11:18:29），攻击者IP 36.137.66.249 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQaVtBn9046wLQwQHWVkK5pM8T1hKpPgUNpddrelQTPj78dPiaMfqWeyDiaMIyYBdiaD0ELHUHibG2KyXOPMUoYJcnrJwbLEMAJiaX2Q/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-24 11:18:29（UTC）36.137.66.249的扫描请求（高亮行）

2026年8月24日 20:10:31（本地时间，对应IIS日志UTC时间12:10:31），攻击者IP 36.137.66.245 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQapsblvOT11E9HKgXOTMCBFA1bHuf7qplb9MqfBpb6icEia4gtYpqpOgy4ldU3UK1oSlUXPRsibjqyicBQiafgNqJGINJlKxvicjvx9M/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-24 12:10:31（UTC）36.137.66.245的扫描请求（高亮行）

2026年8月25日 19:57:03（本地时间，对应IIS日志UTC时间11:57:03），攻击者IP 36.137.66.108 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbjTIbU69PIicxTicHia0kYgJ63jfWtoSLxMWkficm9tianSc1s5RkP1CnMqm9wvrM6zwHmtsAs25BsjqZo0rdLqiblP2xZjPNsm8x9Y/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-25 11:57:03（UTC）36.137.66.108的扫描请求（高亮行）

2026年8月25日 20:20:04（本地时间，对应IIS日志UTC时间12:20:04），攻击者IP 36.137.66.81 再次对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQb0rhGGdvBcicV4GbpfECo9ibEDeW2yBdliawttdQQfmjibUfU4V6AR6qhFYicHGpRq25Z4A3A13DrUwRUYDXJVfSx0oexRBicvedy74/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-25 12:20:04（UTC）36.137.66.81的扫描请求（高亮行）

2026年8月25日 20:49:18（本地时间，对应IIS日志UTC时间12:49:18），攻击者IP 36.137.66.114 再次对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbH0gz8vX50Bt98mTmh04U7VxAB04bttfsZiaS2TOfJFnAOYI6pQeqtzvmP4iaCQWrpJFcTpb0LPK3VLtsv33O5lxoeKfu6G0lEo/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-25 12:49:18（UTC）36.137.66.114的扫描请求（高亮行）

2026年8月26日 20:16:26（本地时间，对应IIS日志UTC时间12:16:26），攻击者IP 36.134.184.90 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYAibHx7YalBTWw1SDkSALvdQiaCKWibyk7wMLQLodqiaa0LgV7keOVmcQjs4LiaJfIKWyCERRBQN4PIJGEtvwpCp4yNdmiaoVUMHicCw/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-26 12:16:26（UTC）36.134.184.90的扫描请求（高亮行）

2026年8月26日 20:36:28（本地时间，对应IIS日志UTC时间12:36:28），攻击者IP 36.137.66.70 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYctGjz4pk8omicnW97R4acibnicYQ8tdKiaibycTvPDGrlibds9BdqKCzF5licIKvwzRAbn2U6Oerlrvv0pqboThgFLibyia3HBYs6n52I/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-26 12:36:28（UTC）36.137.66.70的扫描请求（高亮行）

2026年8月27日 19:37:08（本地时间，对应IIS日志UTC时间11:37:08），攻击者IP 36.137.66.70 再次对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQY8iaV8WL1AOJJib7yTF3ZicficyEhmsPW51EpuvBWYNibibtLeHPOMgUdxA5dEPKdJPicdAfxfuZg5ntmoTWt0GWCaazInGOgwFwj93o/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-27 11:37:08（UTC）36.137.66.70的扫描请求（高亮行）

2026年8月27日 20:53:32（本地时间，对应IIS日志UTC时间12:53:32），攻击者IP 36.137.66.229 对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZiaDgiaj2ChibOnwkReicZYpYCMfiaOZct5D5xxpYeFmc3pQ5aMkq0xzs4lFQN2DZQ0s6UxmicpnvnPpFHyhiccboRH87mhqKD6IenWI/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-27 12:53:32（UTC）36.137.66.229的扫描请求（高亮行）

2026年8月29日 20:13:12（本地时间，对应IIS日志UTC时间12:13:12），攻击者IP 36.134.184.170 再次对受害站点发起反序列化漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYpFdC8D7hH2RfI2LSJlgLmhDHZM7oS1sknEIs2oVGHtTic7o3h9bibyrONAniar7l48TYoTof02c4ub19W2bkxyTN7ygF8NGiaocs/640?wx_fmt=png&from=appmsg)

8013站点IIS访问日志，2026-08-29 12:13:12（UTC）36.134.184.170的扫描请求（高亮行）

综合以上日志可以推断，攻击者疑似使用浙江杭州代理池IP段36.137.66.\* 与36.134.184.\* ，以自动化脚本对互联网上该ERP资产进行反序列化漏洞探测，扫描时间、请求特征与既往Weaxor勒索家族案例一致。该家族...