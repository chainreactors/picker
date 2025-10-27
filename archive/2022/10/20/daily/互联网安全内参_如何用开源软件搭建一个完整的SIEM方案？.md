---
title: 如何用开源软件搭建一个完整的SIEM方案？
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247506395&idx=2&sn=646e30d18bf4d6ab03a730792fb4c227&chksm=ebfa9efbdc8d17ed8aaf59e641bc9f770a791e225d8eb3f199762ffb62edc6bec401073d1efa&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2022-10-20
fetch_date: 2025-10-03T20:23:29.513369
---

# 如何用开源软件搭建一个完整的SIEM方案？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tvPSbBiaP03Iriafdj25YxfqowSWic3qUEKo0jWRWacuRHia42iasL9tSTeXVLMtBdQzP6Le8nRTj45bg/0?wx_fmt=jpeg)

# 如何用开源软件搭建一个完整的SIEM方案？

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNngiapqpBUIn9rAtvc5vdR9k48HAynbz7S2LgVkovbG3EHap8hpZichxaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

SIEM是企业安全运营中心的核心引擎，用于收集、分析和存储安全事件信息并为安全运营的各个流程提供决策信息。SIEM极为复杂，因此绝大多数企业都选择购买价格不菲的商业产品/服务。

但是，高企的价位和运营成本使SIEM成为大型企业才能享用的网络安全“奢侈品”，对于很多安全预算有限的中小型企业，部署SIEM会挤占大量研发、营销和人才预算。

云安全公司SOCFortress认为，网络安全是一种权利，而不应该是特权。该公司推荐了一整套开源工具来帮助企业搭建功能不输商业产品的开源SIEM（甚至SOC）方案，整理如下：

**构成SIEM堆栈的关键要素**

我们首先需要了解SIEM堆栈的关键构成。如果没有合适的工具，安全团队将很难检测、评估、分类和响应安全事件。随着网络的增长和采集日志量的增加，这一点尤其重要。

以下是**必须整合****到**SIEM堆栈中的关键功能模块。

1. 日志采集

2. 日志分析

3. 后端存储

4. 可视化

5. 智力充实

6. 案例管理

7. 自动化

8. 调查与应对

9. 监测

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNnIK5V6LHajmjJs42mVmic51GuBNOlgwibkYicXmF7WPVBKGRPGPaO33sUA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**日志采集**

在SOC分析师查看安全日志之前，首先需要确定采集哪些日志源。常见的日志包括：

* 端点日志（Windows事件、Sysmon、Powershell日志等）
* 网络设备（防火墙(IDS/IPS)、交换机、接入点）
* 代理（Apache、NGINX等）
* 第三方（AWS Cloud Trail、O365、Tenable等）

当我们开始从多个来源采集日志时，确保日志被规范化为通用字段名称，这一点至关重要。例如，source\_ip、source\_ipv4\_ip都应重写为src\_ip字段。当我们开始开发仪表板和警报策略时，这将节省时间和精力。

通过日志规范化，我们现在可以搭建一个通用仪表板，显示所有日志来源的网络连接。

**GrayLog**

在日志采集方面，Graylog是我们的首选工具。Graylog负责从各种日志源收集日志：

* Wazuh管理器
* 网络设备
* 来自第三方的Syslog转发器（例如Cylance、Crowdstrike等）
* 以及其他大量功能

Graylog还能处理存储在Wazuh-Indexer后端中的索引管理，以适应所选的索引生命周期。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNnwictwImK5t5lt05a7FYW8FkTOSWDe585hevDlqloJib59o7Qcv9hicmog/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**日志分析**

虽然采集大量日志是一个很好的起点，但我们还需要能够分析收集到的日志中的元数据细节，以提高警报准确率并确定安全事件的优先级。

* 分析从端点/服务收到的日志。
* 通过日志分析确定采集的日志的严重性，支持自定义规则的功能。
* 能够丢弃警报噪音以限制不必要的数据溢出。

每个企业的网络环境都不尽相同，因此需要灵活地创建自己的自定义规则。企业可以尝试Wazuh的自定义规则——免费的高级Wazuh检测规则。

**Wazuh**

Wazuh是一个很棒的工具，它不仅可以从端点收集日志，而且还内置了内置规则，可以分析日志内容以检测攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNncSS1Xp5fcSt4sU1WEauVE9kQBzdGkm6Z8yxGUdkicq7wSNW9tXa9JTg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Wazuh还提供：

* 配置评估
* 文件完整性监控
* 漏洞检测
* 以及更多

**后端存储**

采集和分析日志很棒，但这些日志将存储在哪里？我们必须搭建一个后端存储架构，具备如下功能：

* 存储、搜索和查看数据（收集的安全事件）
* 高可用性
* 强大的性能
* 扩展能力

**Wazuh索引器**

Wazuh-Indexer是Wazuh的OpenSearch的分叉版本，让我们能够做到这一点。它功能丰富的API还允许我们将其他工具插入Wazuh-Indexer堆栈，例如Grafana、Elastalert等。

**可视化**

存储日志只是一个开始，SOC分析师还需要能够轻松查看、调整、分类和搜索安全威胁或堆栈。大海捞针式的查询体验很快就会导致分析师们精神崩溃。

因此，我们还需要整合可视化工具以便：

* 通过小部件/仪表板/等查看日志。
* 快速搜索和查看数据。
* 支持从多个日志存储（Wazuh-Indexer、csv文件、MySQL等）读取的能力。

**Grafana**

Grafana是值得推荐的可视化工具，速度快（与Kibana相比）、完全可定制、丰富的预构建小部件、强大的社区支持，并提供多租户支持！Grafana允许我们搭建一个“单屏”界面来查看所有的安全事件。

**情报富化**

除了分析日志之外，我们还需要一种方法来富化日志，以帮助分析师快速发现潜在的恶意活动。例如，与网站交互的某个IP地址是否恶意？我们需要一个具备如下功能的日志富化工具：

* 使用来自多个提供商的威胁情报富化采集到的日志。
* 解析并存储选定的响应，以便仅存储关键数据。
* 自动化，因此SOC分析师不必手动尝试富化收到的日志。

**OpenCTI**

OpenCTI平台的首要目的是提供一个强大的知识管理数据库，该数据库具有一个专门为网络威胁情报和安全运营量身定制的强化模式。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNna8mTQF2xbYrIb6j1ftWQYlBqCLicZ9s7c1HCWIuP9DoWIbSB3jgNW8Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**MISP**

MISP提供元数据标记、提要、可视化，甚至可与其他工具集成以进行进一步分析，这要归功于其开放的协议和数据格式。

这两种工具都提供了丰富的API，使我们能够及时自动执行威胁情报查找！

**案例管理**

随着SOC团队的壮大，我们需要提供一个平台，让他们能够协作、丰富和响应警报。为您的SOC分析师提供剧本、任务和程序将帮助指导他们完成检测到的警报，并让他们专注于关键警报。

* 用于查看和响应高严重性事件的平台。
* 允许与多个SOC分析师协作。
* 允许响应操作，以便分析师可以在其端点上触发事件。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNnnEWjTPxsEdqGnibJgaM718duMB6zaEo9hvlCS0xD2ZIwnnIHyIHacJA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNnXM6FhUliatAotoz0QiaibSYQq8bzLvqhmGNpj5EOY8Z77XX7dOicwaJubw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**TheHIVE/Cortex**

TheHIVE使我们能够管理、组织、关联事件并自动化取证分析，同时利用强大的协作能力。

而Cortex提供对来自第三方或遗留服务和自动主动响应的可观察数据（文件哈希、IP、域等）的调查。

**自动化**

随着采集的日志不断增加，我们需要一个可以自动执行许多任务的工具，例如：

* 案例创建
* 网络钓鱼分析
* 健康检查失败
* 报告生成
* 其他种种

这篇文章中提到的所有开源工具都自带API，我们可以将SOAR平台插入其中以自动化几乎所有任务！

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNnGvBibzB67Su0ot7Dia8gXRvpH5ogj3UAzVlrGVQxTq6iaH7pxB97jDJQQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**Shuffle**

Shuffle是SOAR的开源实现，通过即插即用应用程序带来在整个企业中传输数据所需的所有功能，使每个人都可以使用自动化。它能消除团队中对编码器的需求（但仍然建议至少有一个），Shuffle能够在几分钟内（而不是几小时或几天）部署新的、复杂（或简单）的工作流程。

**事件调查**

接收警报只是成功的一半，我们必须让我们的SOC分析师能够通过可扩展的方式与受监控的端点快速交互来彻底调查警报。一些技术包括：

* 列出正在运行的进程
* 枚举登录用户
* 检测监听端口
* 查看下载的文件
* 隔离设备
* 等等

如果没有上述功能，SOC分析师就很难快速评估警报的实际严重性。

**Velociraptor**

Velociraptor是一种先进的数字取证和事件响应工具，可增强对端点的可见性。只需按下（几个）按钮，我们就可以在所有端点上精准高效地同时进行有针对性的数字取证收集，其可靠的API支持在需要时自动化和触发证据收集。

**健康监测**

SIEM堆栈构建完成后，我们需要监控整个SIEM堆栈的运行状况，以确保顺利运行并将丢失警报的风险降至最低。我们通常将监控分为两个阶段：

* 端点资源（CPU、RAM、磁盘、进程等）
* WebUI正常运行时间

例如，也许Grafana服务运行良好，但如果防火墙更改禁止了用户访问Grafana WebUI，会导致分析师无法访问WebUI查看警报，并最终使Grafana无法使用。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvaHpzZcwicdr05N3HCc2LZNn3pEiaxuYqB6V4k27lDFYeKpoAfYVmaJmQqNXe2ciakhMVoYPgMfw6T2g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**InfluxDB/Telegraf**

InfluxDB与Telegraf代理相结合，使我们能够收集所有的端点指标，并在达到阈值或关键进程（例如wazuh-indexer）未运行时触发内置警报。这使工程团队能够在潜在问题产生严重影响之前主动应对。

**Uptime Kuma**

Uptime Kuma是一种监控工具，可用于实时监控网站和应用程序。特点包括：

* 监控HTTP(s)网站、TCP端口和Docker容器的正常运行时间，并检索DNS记录等信息。
* 通过电子邮件(SMTP)、Telegram、Discord、Microsoft Teams、Slack、Promo SMS、Gotify和90多种通知服务发送通知。
* 支持多种语言。
* 提供多个状态页面。
* 提供代理支持。
* 显示SSL证书信息。
* 将状态页面映射到域。

**结论**

安全运营是一件高度复杂且费钱的事情，但企业也没必要为此破产。有大量开源工具可供我们以最低成本搭建我们自己的SIEM技术堆栈。开源的灵活性还允许我们根据自身的需求进行灵活定制。本文我们介绍的本地SOC开源工具，功能上可以媲美商业工具，如果您的团队有足够的人才和试错空间，那么尝试在本地自行搭建开源SOC方案未尝不是一个有趣的选择。

本文介绍的开源SOC部署策略涉及的工具清单如下：

1.Wazuh Indexer(OpenSearch)

2.Wazuh Dashboards(OpenSearch Dashboards)

3.Graylog

4.Wazuh Manager/Agents

5.Grafana

6.MISP

7.OpenCTI

8.TheHIVE/Cortex

9.Velociraptor/Agents

10.Shuffle

11.InfluxDB/Telegraf

12.Uptime Kuma

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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