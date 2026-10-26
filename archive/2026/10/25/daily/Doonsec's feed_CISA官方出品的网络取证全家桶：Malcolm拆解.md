---
title: CISA官方出品的网络取证全家桶：Malcolm拆解
url: https://mp.weixin.qq.com/s/dXEmOPecNJoLR8vSnZJZ0w
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:13:59.859339
---

# CISA官方出品的网络取证全家桶：Malcolm拆解

# CISA官方出品的网络取证全家桶：Malcolm拆解

原创

赤霄攻防实验室
赤霄攻防实验室

赤霄攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![封面｜武器库评测（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8adLxf9Zc1oF74jHHalpTDiaODnQibQKOCASbz8tA5TAAP9ibw2Hoef0X9gDMCnyj8hjDFcicZ6HUoEN3JOev2ibOPUicM3hibibhOHvc9s/640?wx_fmt=png)

▲ 封面｜武器库评测（制图：赤霄攻防实验室）

TL;DR

**啥工具**：Malcolm，CISA 官方维护的网络流量分析全家桶，把 Zeek、Suricata、Arkime、OpenSearch 缝成了一个开箱即用的取证平台

**给谁用**：SOC、应急响应、工控（ICS/OT）监控——从机房服务器到树莓派传感器都能部署

**为啥值得看**：网络可见性是检测的前提。看不见流量，再好的检测规则也是摆设

![工具档案卡（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8acW6icmecMwkiaknBgrsQWVv5nQkoibI8qFM3ZFJAHRPoo0SnQoxIlVfuhWica3NPfXa4fibNtLYZL8bDOPia9xiaGUPnJkoamDzDL3AM/640?wx_fmt=png)

▲ 工具档案卡（制图：赤霄攻防实验室）

## 安全团队的老大难：流量看得见吗

问个扎心的问题：你现在用的网络，流量进出了什么，你能说清楚吗？大多数团队的答案是不能。防火墙日志只有拦截记录，交换机不存历史，真出了事想查「上周这台机器连过谁」，抓瞎。

Malcolm 就是冲着这个问题来的。它是美国网络安全与基础设施安全局（CISA）官方维护的开源网络流量分析全家桶：把 Zeek（协议元数据日志）、Suricata（特征告警）、Arkime（全包检索）、OpenSearch（存储可视化）这些单打独斗的工具编排成一个平台。采集、解析、存储、下钻，一条龙全包。

2.6k 星，Apache 2.0，从 2019 年迭代到现在，昨天还在推代码。出品方是 Battelle Energy Alliance——CISA 的运营承包商，背书够硬。

![仓库主页（来源：GitHub）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8afnVibCbIbHuuFzdvf59y9RrClgaFbLkgqZs1CrDWTRn0K2073JOia6Jjd203iaR0JQS9zgbQnsX3mZBBn1XkRzaKtdfEA8tbgib3c/640?wx_fmt=png)

▲ 仓库主页（来源：GitHub）

## 一条流量的旅程

Malcolm 的工作方式可以用一条流量的旅程来讲。第一步捕获：交换机做端口镜像，流量进到 Malcolm 的采集节点，全量 PCAP 落盘，同时元数据被抽出。第二步解析：Zeek 把每条连接变成结构化日志（DNS、HTTP、SSL 握手全都有），Suricata 按规则出告警，Strelka 拆解传输中的文件喂给 YARA 扫描。

第三步聚合：所有数据进 OpenSearch 归一化存储，Arkime 给原始数据包建索引，想看哪个会话点开就是完整的包内容。第四步研判：几十个预置仪表盘开箱即用，协议分布、异常连接、文件哈希命中一目了然。

这套东西单独搭你也能搭，但把 Zeek、Suricata、Arkime、OpenSearch、Strelka、YARA、Keycloak、NetBox 全部缝好、调好参数、配好认证的工作量，够一个工程师折腾一个月。Malcolm 的价值就是把这个月省下来。

![一条流量的旅程（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8adVx9SJb5KNaSbtWnIQkpUJfA1nJJiarJrRO65f0yVD30yibuNjcVYufw9gOjebrL6gKFmkbhsCeKnCUegLM6pGGfSGu48jVdq5Q/640?wx_fmt=png)

▲ 一条流量的旅程（制图：赤霄攻防实验室）

## ICS/OT：CISA 为什么亲自下场

Malcolm 有个特殊使命：工控环境（ICS/OT）的协议可见性。电厂、水厂、工厂里的 Modbus、DNP3、S7 这些工控协议，通用流量工具要么不认识，要么解析得浅。CISA 的职责覆盖关键基础设施，他们见够了「工控网络被入侵了却没人发现」的案例，所以持续给 Malcolm 加工控协议解析器。

对国内读者，这个方向同样成立：电力、水务、制造的网络里有大量「永不更新、不能停机」的设备，唯一可行的监测方式就是被动看流量。这正是 Malcolm 的舒适区。

## 部署形态：从 SOC 到树莓派

部署方式有三档。SOC 长期部署：malcolm-iso 做成裸机 ISO，装在服务器上接交换机镜像口；项目内响应：Docker Compose 起一套，笔记本就能带着出差；边缘采集：Hedgehog 是配套的树莓派传感器镜像，插上网线就能把分支机构的流量回传中心。

资源要求别抱幻想：全量 PCAP 的磁盘消耗是真实的，OpenSearch 吃内存也是真实的。小环境可以只收日志不全抓包，Malcolm 的组件都是可选的。

## 给你的三句话

SOC 团队：如果商业 NDR 预算批不下来，Malcolm 加一台好的采集服务器能覆盖八成日常可见性需求。应急响应：手里常备一套 Malcolm，取证时不用现场搭环境。开发运维：哪怕只用 Zeek 的日志能力，DNC 查询、异常外联这些问题的答案也比你想象中好拿。

## 参考

1. 仓库：https://github.com/cisagov/Malcolm（Apache 2.0）
2. 文档：docs/README.md
3. Hedgehog 传感器：仓库内 hedgehog-raspi/ 目录

免责声明：本文仅用于安全研究与防御交流。

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