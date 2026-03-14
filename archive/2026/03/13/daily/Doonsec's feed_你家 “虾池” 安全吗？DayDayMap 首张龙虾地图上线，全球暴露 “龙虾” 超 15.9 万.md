---
title: 你家 “虾池” 安全吗？DayDayMap 首张龙虾地图上线，全球暴露 “龙虾” 超 15.9 万
url: https://mp.weixin.qq.com/s/ypyxCG81BymjbCgbJ2Eiow
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:35.308081
---

# 你家 “虾池” 安全吗？DayDayMap 首张龙虾地图上线，全球暴露 “龙虾” 超 15.9 万

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaHzAadq8iaGneLjSanSpnrRFVtvEOKP31Txt3Sb7WCXgrSMVplJUmVAQYvUldmhhfQQPBMS2RJmdsicTVAM9tYYibmWVyCJyEJia3vAES0G1oW0/0?wx_fmt=jpeg)

# 你家 “虾池” 安全吗？DayDayMap 首张龙虾地图上线，全球暴露 “龙虾” 超 15.9 万

原创

烽火台实验室
烽火台实验室

Beacon Tower Lab

![]()

在小说阅读器中沉浸阅读

**一场由AI智能体引发的“龙虾”狂潮，正在将无数企业的内网门户悄然洞开。**

引言：当“养龙虾”成为新时尚

2025年底，一个名为OpenClaw的开源AI智能体框架悄然发布。它能够自主接入飞书、微信、本地文件系统，甚至编写代码、管理日程、远程控制设备——就像一只可以替人干活的“机器龙虾”。因其极高的集成度和自主执行能力，OpenClaw迅速引爆开源社区，GitHub星标一周突破18万，访问量超200万，被开发者亲切地称为“养龙虾”。

然而，这只“龙虾”在带来效率革命的同时，也埋下了巨大的安全隐患。由于默认配置开放、第三方插件泛滥、漏洞频出，大量部署了OpenClaw的“虾池”直接暴露在公网，成为黑客眼中的“自助餐”。

盛邦安全作为网络空间资产测绘的领跑者，通过DayDayMap全球网络空间资产测绘平台，首次对全球暴露的OpenClaw实例（以下简称“龙虾”）进行了全面测绘与风险分析。本文将结合最新测绘数据和深度威胁研究，为您揭开“养虾热”背后的安全真相。

**一、测绘篇：全球“龙虾”分布图，谁在裸奔？**

1.1 全球“虾池”数量激增，单季度增长40倍

根据DayDayMap平台截至2026年3月的数据，全球公网仍在运行或曾经部署的OpenClaw实例已超过 15.9万。其中：

· 中国：6.35万个

· 美国：3.7万个

· 其他地区：5.88万个

2026年3月在线实例数量超过6.8万，相比1月增长了 40倍 。从增长速度来看，中国区的“龙虾”数量在过去三个月内增长了400%，远超全球平均水平，成为全球“养虾”最火热的地区。

![](https://mmbiz.qpic.cn/mmbiz_png/iaHzAadq8iaGlvVFYawnibtrWyHanh5cPF89gzokel7DGdiaWSLric5y3arcv1l9icDC1PcWabq7p0bHcDRgh54nodohZKTGP7MFfeMuxflodFM7A/640?wx_fmt=png&from=appmsg)

1.2 大家都在哪“养虾”——云服务商托管商提供大型养殖基地

通过对暴露IP的归属分析，我们发现：

· 云服务商托管：超过43.7%的暴露实例部署在阿里云、腾讯云、华为云等公有云上。

· 互联网科技公司：多个头部高新科技企业均有多个IP暴露了OpenClaw服务，部分甚至直接绑定在公司域名下。

· 高校与科研机构：约1.5%的实例位于教育网内，可能用于科研或教学。

· 制造业与金融业：少量实例出现在制造业和金融企业的网络中，暴露了内部敏感系统。

典型暴露厂商TOP5（按暴露实例数量排序）：

![](https://mmbiz.qpic.cn/mmbiz_png/iaHzAadq8iaGmRB051l1g2x1sya8ibBnllUhkDrEHrkrbMostogbXDSllp6V5kwOlY7j0IwgjhGcgicpEhjxMWdAEfl6zPsiaZGMeriaWFcPKIXUw/640?wx_fmt=png&from=appmsg)

注：仅统计公网可访问的OpenClaw实例，不代表厂商自身已遭入侵。

![](https://mmbiz.qpic.cn/mmbiz_png/iaHzAadq8iaGmFGeqNicn4tfnaQ4pfcqHsvNjQWhNRia4r7ibjm1dSjF2Dzu8hpoz9PKtN46KqCBL0NzicnzoPANknl6WKXagjJt3CaP15DUIDKvg/640?wx_fmt=png&from=appmsg)

1.3 “虾池”暴露的端口与协议

OpenClaw默认使用 18789端口 提供Web控制界面，同时通过WebSocket进行实时通信。DayDayMap监测到：

· 超过57.3% 的暴露实例使用了默认端口18789，且未启用身份认证。

· 约 4.5% 的实例同时开放了其他高危服务（如22、3306、6379等），形成风险聚集。

· 部分实例使用了自定义端口，但通过指纹特征仍可被识别。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaHzAadq8iaGm4cHBE8tA4W30K4riaM3ibn4LKZKYfchoxIAPFiaZqaT6UxIjxzhwaMWL9UTgy4PVJkmupibZfUneEwJGMCEXDmBppGEaExfiaAOP0/640?wx_fmt=jpeg&from=appmsg)

1.4 增长趋势：谁在加速“养虾”？

从2026年1月至今，全球暴露实例的增长曲线呈指数型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHzAadq8iaGlBuLibKd2lYiaUFJgqUQAIwuy5TVHMvCzfmsmzudibvtQDFwCxo4bc4WcmAUOpWthQcHyjnsP019LUoumGiaYgL8u1iabvlpiaDeicA4/640?wx_fmt=png&from=appmsg)

· 1月爆发式增长期：OpenClaw于2026年1月初在GitHub发布，用户跟随快速入门指南部署在VPS上，默认配置未启用身份验证，导致大量实例直接暴露于公网。

· 2月安全危机高峰期：2月暴露实例达到高峰，其中39.2%的实例与之前的泄露活动相关，官方发布补丁后，部分用户升级，但暴露总量仍在增加。

· 3月现状：

DayDayMap龙虾地图揭示了真实的暴露面现状：面对互联网上高达27万的公开情报，DayDayMap通过持续监测和多重去重验证，给出了更精准的数据——实际累计可确认的暴露实例为15.9万。其中大量实例因临时部署、IP地址变动或服务关闭而快速下线，目前全球日活在6万左右，趋于稳定。这一数据表明，尽管早期暴露规模庞大，但实际持续在线的“活虾”数量约为高峰期的四分之一，攻击面依然可观。

**二、威胁篇：你的“龙虾”正在被黑客“烹饪”**

OpenClaw的爆火不仅吸引了开发者，也引来了无数猎食者。根据盛邦安全烽火台实验室的持续监测，当前针对OpenClaw的攻击手段层出不穷，威胁形势极为严峻。

2.1 威胁分类：六种最致命的“虾病”

根据攻击向量，OpenClaw面临的安全威胁可分为以下六大类：

（1）系统级漏洞：根基动摇

OpenClaw早期版本追求“开箱即用”，牺牲了部分隔离性。研究发现，本地Gateway通信协议与执行引擎之间存在身份验证绕过漏洞，攻击者可借此直接劫持宿主机Shell权限，将智能体变为远程控制的“僵尸虾”。此类漏洞一旦被利用，整个系统将完全沦陷。

（2）提示词注入攻击：AI的“认知战”

不同于传统代码注入，OpenClaw面临着更隐蔽的间接提示词注入威胁。当智能体自主读取被污染的外部网页、邮件或文档时，隐藏在自然语言中的恶意指令能够绕过系统预设的安全护栏，误导LLM做出违背用户意愿的决策——例如在处理发票时偷偷将资金转入黑客账户。这种利用模型语义解析特性的攻击，挑战了现有的所有特征码检测机制。

【复现示例】

一般来说可以将在飞书中接入OpenClaw ，构造一个携带特殊指令的文档

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHzAadq8iaGmYtvU6ZPWsLiah0kbgNwneqGtSYHP2ofwSU3yG9eIEeQPaooJ7GSJ0KpX0aHf3MUnu8icCvgK8xLhDDhNsibyI8QjRREuYdibKByM/640?wx_fmt=png&from=appmsg)

让模型进行分析总结，会触发指令执行，一般大模型不受影响，小模型会收到影响。

（3）插件/技能投毒：毒虾饵

OpenClaw强大的扩展性依赖于其插件生态系统ClawHub。然而，由于缺乏严格的中心化审核与代码签名机制，恶意开发者通过“插件投毒”手段，将带有后门或敏感数据外泄逻辑的“技能包”上架。用户在追求功能扩展时，极易在无感知的情况下引入恶意组件，导致API密钥、本地私钥等核心凭证被静默截获。

【复现示例】

首先创建一个插件所需要的文件，在安装文件 install.js中添加恶意代码，这里我代码的功能的是将/agents/main/agent下的模型配置文件打包至/app/dist/control-ui/assetsweb目录文件下，这样既可以绕过模型对恶意代码的检测，又达到了获取大模型api-key的目的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHzAadq8iaGnjYSTL6Ae2tmEoHKnPCQ60xIjibaupicdVwTaTCiaa1F1VYxxD6QBhCbqnnVEDmVviapmRv3pUeb0vVaGFwx1prbsBlkAZepbXnU4/640?wx_fmt=png&from=appmsg)

紧接着，将插件打包，上传到公网服务器中，然后给openclaw说安装

![](https://mmbiz.qpic.cn/mmbiz_png/iaHzAadq8iaGlRoTaBfVxeFCHyaFBX02AU4Ec5wWRSiayL44tdETibN939WiaNpSLB5fZnSGmeSicZblZ2kul8zurVicOe8R8V1h9ax0pecdJKYibLk/640?wx_fmt=png&from=appmsg)

等待一段时间的安装后，通过页面访http://x.x.x.x:18789/assets/agent-backup.zip，解压即可拿到备份的modle.json

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHzAadq8iaGmHibiaQ1ib3Hdqhp1MH40bzjVmTk6h7l9EPiazoQKNvt9mPezB3iaPGk5L1tLIT2krUDcmMBNw2OtRuuRzELwvMqgbia2XtADaGMs58/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/iaHzAadq8iaGkjPPVyD1KrtaR3PSJxkja8YBeJVVUWaVZZHBff839XXcxJZ4wYoQ8vsmSGCAzqZfUlnEVRHsLcR5MZCHANvW9RulqaOZjK7Uo/640?wx_fmt=png&from=appmsg)

（4）恶意伪装攻击：真假龙虾

攻击者伪装OpenClaw安装包，部署远程访问木马（RAT），窃取系统凭据。例如“GhostClaw”攻击：分发伪造的安装包，诱导用户下载运行，随后在后台窃取macOS钥匙串中的密码，并可能进行横向渗透。

（5）供应链污染：ClawHub成重灾区

2026年2月，安全研究人员发现ClawHub（官方技能市场）成为供应链攻击的目标，超过1184个恶意技能包被上传，其中部分用于分发Atomic Stealer窃密木马，目标直指用户的Desktop、Documents、Downloads等敏感目录。尽管官方随后与VirusTotal合作进行扫描，但历史遗留的恶意包仍可能影响未及时清理的用户。

2.2 重大安全漏洞详解

CVE-2026-25253：认证令牌窃取导致RCE

该漏洞（CVSS 8.8）源于OpenClaw对用户控制的gatewayUrl参数的不当信任。攻击者构造恶意链接，将gatewayUrl指向自己控制的服务器，当受害者点击链接后，OpenClaw自动建立WebSocket连接并将认证令牌发送给攻击者。攻击者利用令牌获取API凭证，进而禁用确认机制、逃逸容器、在宿主机上执行任意代码。所有2026.1.29之前的版本均受影响，可导致存储在本地存储中的Claude、OpenAI、Google AI等服务的API凭证被窃取。

ClawJacked：恶意网站劫持本地AI代理

2026年2月发现的高危漏洞ClawJacked允许恶意网站暴力破解并控制本地AI代理实例。该漏洞源于OpenClaw处理WebSocket连接、身份验证和网络请求验证的设计缺陷，攻击者只需诱导用户访问恶意网站，即可劫持OpenClaw代理。该漏洞在2026.2.26版本中修复。

2.3 历史安全审计：512个漏洞的警示

2026年1月底进行的安全审计（当时OpenClaw仍名为Clawdbot）发现了512个安全漏洞，其中8个为关键漏洞，涵盖身份验证绕过、权限提升、命令注入等多种类型。这一数据表明，OpenClaw从诞生之初就存在严重的先天不足。

2.4 安全事件时间线：漏洞与攻击的赛跑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHzAadq8iaGnswjianU818ics1cwiasdbCDibnNTMMTYnJE36I4Alq2EKDQ7Qpefgm7ZiblbRZL59u0LgBWhtfib9vibS3GS9679vKpheqfHC9pBNh4/640?wx_fmt=png&from=appmsg)

2.5 官方安全通报

国内：CNCERT、中国网络空间安全协会先后发布关于OpenClaw安全风险提示。自2026年1月至3月9日，国家信息安全漏洞库（CNNVD）共采集OpenClaw漏洞82个，其中超危12个、高危21个。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHzAadq8iaGl91MYkdAkrHU4QK5zVKGDToOr5GmuTGoFuXF3YFcmibV05JAuftsWiaB1veejZ2EPvBu0kkPo7eC4iabmj1xsO9pPLuIE9HNiaiajE/640?wx_fmt=png&from=appmsg)

· 国际：CVE-2026-25253被NVD正式收录，Kaspersky、SecurityWeek等安全厂商发布警报。

**三、威胁行为者画像：谁在盯着你的“虾池”？**

· 黑产团伙：利用暴露实例植入挖矿木马、勒索病毒，或搭建代理进行非法活动。他们通过自动化扫描工具批量捕获“裸奔”的虾池，形成僵尸网络。

· APT组织：已有迹象表明，某国家级APT组织利用OpenClaw漏洞入侵科研机构和高科技企业，窃取敏感数据和知识产权。他们更倾向于针对特定目标进行精准投递恶意链接或文档。

· 脚本小子：使用公开的漏洞利用工具，在互联网上大规模扫描，以炫耀技术或小范围破坏。

· 内部威胁：员工私自部署OpenClaw并暴露，或使用弱口令，导致企业内网门户洞开，成为攻击者的跳板。

**四、如何科学“养虾”？——DayDayMap的安全建议**

4.1 网络隔离：别把“虾池”建在大街上

· 禁止公网暴露：OpenClaw应部署在内网，通过VPN或堡垒机访问。

· 防火墙策略：仅允许特定IP访问18789等端口。

· 本地模式优先：尽量使用localhost绑定，避免监听0.0.0.0。

4.2 版本管理：及时打补丁，预防“虾病”

· 立即升级：确保版本 ≥ 2026.2.25，修复已知高危漏洞。

· 关注公告：定期查看OpenClaw官方GitHub的更新日志和安全通报。

4.3 插件管理：不投喂“毒虾饵”

· 非必要不安装：第三方插件风险极高，尽量使用官方自带功能。

· 代码审计：安装前审查插件源码，尤其是install.js等关键文件。

· 权限限制：限制插件的网络访问和文件读写权限。

· 使用VirusTotal扫描：对下载的技能包进行哈希比对，确认无恶意记录。

4.4 访问控制：给“虾池”加把锁

· 强制认证：启用密码或OAuth，避免空密码。

· 密钥轮换：定期更换API密钥、数据库密码等敏感凭证。

· 日志监控：部署日志分析系统，及时发现异常访问和命令执行。

· 令牌保护：防止令牌泄露，避免点击不明链接。

4.5 数据保护：核心资产加密存储

· 配置加密：敏感配置文件加密存储。

· 安全备份：定期备份并安全存储，避免备份文件暴露。

· 日志脱敏：限制日志输出敏感信息。

4.6 最佳实践：最小权限原则

1. 最小权限：限制OpenClaw的访问权限，仅赋予必要功能。

2. 网络分段：与其他关键系统隔离，即使被攻破也难以横向移动。

3. 监控告警：设置异常行为检测，如频繁的命令执行、未知外连等。

4. 应急响应：制定安全事件响应计划，确保快速处置。

5. 安全培训：提高团队对AI Agent安全风险的认识。

4.7 持续监测：用DayDayMap掌控暴露面

盛邦安全DayDayMap平台提供全球资产测绘服务，可帮助您：

· 发现暴露资产：输入关键词，一键检索公网上的OpenClaw实例。

· 漏洞关联：实时关联最新漏洞，评估暴露资产的风险等级。

· 攻击面管理：持续监控企业外部暴露面，及时发现影子IT。

DayDayMap 现已正式上线**龙虾地图！**

访问地址：

```
https://www.daydaymap.com/openclaw/index.html
```

欢迎前往查询暴露态势、检索资产分布、跟踪风险趋势，一键掌握全网 “龙虾” 安全状况！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaHzAadq8iaGmz8yOkFNGAnPIMjibT9dZxVPhqjpyuXDWia0E6I1heZt3lk4UnR1qW2oxvPzMgbicHm2MrQqCxPLKGgIkhNMaZHQdIoI2ib220yHw/640?wx_fmt=jpeg)

**五、结语：热潮之下，安全是“养虾”的底线**

OpenClaw作为AI Agent的标杆项目，其潜力不可估量。但任何技术的普及都伴随着安全挑战。从DayDayMap的测绘数据来看，大量“龙虾”正在公网裸奔，随时可能被黑客操控。

我们呼吁所有“养虾人”：

· 别图省事：默认配置不一定是安全的，请务必按最佳实践加固。

· 别存侥幸：你的“虾池”可能已经被扫描，只是还未被利用。

· 别忘监测：定期检查暴露面，让DayDayMap成为您的安全哨兵。

盛邦安全将持续关注OpenClaw及相关生态的安全动态，为您的数字资产保驾护航。如需获取更详细的测绘...