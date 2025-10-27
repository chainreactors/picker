---
title: 7款流行的用户行为分析（UEBA）工具及特点分析
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651132252&idx=1&sn=00cca6c740753c2e0f3001d060521234&chksm=bd15a18f8a622899cce6a163737b178cd1db0083a688fd91ec33a8975419711fb5915251f9fa&scene=58&subscene=0#rd
source: 安全牛
date: 2024-09-20
fetch_date: 2025-10-06T18:27:11.282299
---

# 7款流行的用户行为分析（UEBA）工具及特点分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCQ6MsciaCLwp5qib1GpmIvfic16kKKk9icToFxzPJo8REQnvTAgcaodHkxL2ib7N4TnanDNIKlXptCBbg/0?wx_fmt=jpeg)

# 7款流行的用户行为分析（UEBA）工具及特点分析

安全牛

为了应对不断创新的网络攻击手段、更好地保护企业的数据安全，用户和实体行为分析（UEBA）技术应运而生，它通过收集和分析来自各种来源的数据全面分析和检测内部人员的可疑行为，并提供行为基准、集成威胁情报和补救工作流程等功能。虽然UEBA这个安全类别的落地应用形态各异，但几项关键功能在整个行业具有高度的一致性，主要包括：

***01***

监测分析

企业必须监测安全基础设施中的网络、设备和应用程序。UEBA工具不断观察IT系统，并在网络流量和设备或应用程序的行为与预先配置的标准不一致时通知管理员。同时，利用机器学习识别用户行为，以确定它们是否符合典型操作的预定标准。如果UEBA工具确定用户的异常行为很危险，它会在仪表板上高亮显示该模式，供安全管理员查看。

***02***

确定警报的优先级

出现足够严重的异常时，UEBA工具会触发警报。由于这类工具长期研究典型的用户和应用程序模式，意外情况发生时它们会留意到。UEBA工具常确定警报的优先级——对风险级别进行排序，这样IT和安全人员可以决定优先处理哪个风险。

***03***

管理用户行为

UEBA解决方案监测用户权限，并确定特定用户的行为是否与分配给他们的权限相冲突。这有助于减少特权访问滥用，还可以暴露恶意的内部活动。UEBA解决方案还经常监测实体或资产（比如笔记本电脑或服务器），以确定它们的行为是否异常，是否需要隔离或关闭。

***04***

高级威胁识别

当UEBA工具监测系统并注意到异常时，它们通常会确定发生了什么类型的问题。这些威胁包括横向移动和数据泄露，UEBA解决方案还可以告诉用户威胁来自企业内部还是外部。这些信息对于帮助应对威胁攻击者非常有用，特别是当他们是内部员工时。

随着网络技术发展加快，攻击技术和恶意内部活动在越来越趋于隐蔽的同时，也呈现出多样化态势。因此，要真正实现用户行为全过程解析并不容易，企业用户需要进一步加强对UEBA技术的研究，并部署应用具有较高处理效率与检测质量的UEBA工具。本文收集整理了7款较热门的UEBA解决方案（详见下表），并对其应用特点进行了分析。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkCQ6MsciaCLwp5qib1GpmIvfic4SibjkdgRJpwRZSkNEesapzy8R7onmOmFgOwRzNMbeblWzcibzd8ia0sQ/640?wx_fmt=png&from=appmsg)

**1、Rapid7 InsightIDR**

Rapid7 InsightIDR是集SIEM和XDR功能于一体的威胁检测平台，可以持续参考正常的用户行为基线，查找已定义的攻陷指标。它旨在检测难以发现的威胁，比如冒充公司员工的攻击者或恶意内部人员企图泄露数据的活动。如果企业正在寻找一款综合的威胁防护安全解决方案，InsightIDR将是不错的选择，因为丰富的功能和出色的管理能力使其成为综合表现完善的整体UEBA应用方案。

主要特点

•将行为活动自动关联：InsightIDR能够将客户网络上的事件与这些事件背后的特定用户和实体关联起来。

•用户活动基准：该解决方案适应网络上的用户和实体，可以持续定义正常的活动行为。

•观察列表：通过InsightIDR仪表板监测，可以发现并重点关注可能构成高风险的用户。

•错误配置检测：InsightIDR使用可视化日志搜索和预构建合规卡来检测异常。

传送门：

https://www.rapid7.com/products/insightidr/

**2、Microsoft Sentine**

Microsoft Sentinel是一款云化的SIEM解决方案，同时也提供了可靠的UEBA功能。功能特性包括事件优先级确定、行为分类和事件时间轴管理等。除了这些功能之外，Sentinel还可以与微软的XDR产品Defender整合，是Azure云客户的理想选择之一。

主要特点

•广泛的数据收集能力：Sentinel可以从本地和多个云中的所有用户、设备、应用程序和基础设施提取行为相关的信息。

•横向移动检测：当Sentinel标记出可疑行为后，安全团队可以通过该方案查看到应用程序或服务之间潜在的横向移动情况。

•基于AI的威胁调查：相比手动搜索威胁，Sentinel具有强大的人工智能能力，可以帮助用户更快地探索威胁和寻找奇怪的行为。

•没有查询限制：由于是云原生工具，Sentinel避免了一些可能阻碍本地系统保护企业的资源限制。

传送门：

https://azure.microsoft.com/en-us/products/microsoft-sentinel

**3、FortiSIEM**

FortiSIEM是由网络安全厂商飞塔设计研发的综合性SIEM产品，其整合的UEBA功能全面包括了内部威胁识别、用户行为风险评分和受攻击账户检测等能力。FortiSIEM是一款强大的网络威胁防护解决方案，理论上说适用于任何企业，不过在实际应用时，它尤其适用于已经使用飞塔防火墙等设备的用户，因为通过与FortiGate设备集成，可以更加方便地共享数据。

主要特点

•检测异常端点行为：广泛的端点数据可以反映出受攻击的系统或账户，或者疏忽或恶意的内部人员。

•威胁情报：FortiSIEM支持提供CSV文件或支持STIC/TAXII标准1.0、1.1和2.0的威胁源。

•实时关联引擎：FortiSIEM可以动态运行数百条与用户活动相关联的监测规则。

•基于机器学习的检测：管理员可以通过机器学习，自动化查看异常行为和用户，无需自己来人工编写所有规则。

传送门：

https://www.fortinet.com/products/siem/fortisiem

**4、LogRhythm SIEM**

LogRhythm是一款提供了强大UEBA功能的新型SIEM平台，主要特点就是使用机器学习技术来检测内部威胁、蛮力攻击和管理滥用等异常情况。LogRhythm的文件完整性监测功能可以快速查询到不合规的文件访问。如果用户存储大量含有敏感数据的文件，不妨考虑部署应用LogRhythm。LogRhythm可能需要几个月的时间来进行全面定制。但是对于具有高级SIEM需求的专业安全运营团队来说，它是一个很好的UEBA解决方案。

主要特点：

•威胁情报集成：LogRhythm SIEM可以与目前主要的商业威胁源和开源威胁源集成。

•针对个别异常的评分机制：通过个别异常评分和汇总用户评分，用户可以优先确定哪些潜在威胁需要调查和缓解。

•自动威胁响应操作：LogRhythm可以通过自动实施威胁响应（比如文件隔离和URL阻止）帮助减少人员工作量。

•威胁分析模型：通过该模型，平台可以将用户身份对照自己的基准或所有被监测的身份进行威胁比对。

传送门：

https://logrhythm.com/products/logrhythm-siem/

**5、Cynet 360 AutoXDR**

Cynet 360 AutoXDR是一款应用广泛的威胁检测和响应平台，能够为企业提供单一的多租户平台化服务，将端点、用户和网络安全功能融合在一个完整的服务套件中。UEBA也属于该平台的网络安全能力范畴，提供了广泛的UBA特性及其他安全工具，因此它是适合大企业的不错选择，尤其适合希望快速增强网络威胁检测和响应能力的安全团队。

主要特点

•网络响应编排：剧本式的威胁处置操作可帮助团队处理受感染的主机、恶意文件、网络流量和受攻击的用户账户。

•CyOps：Cynet提供由专业SOC专家辅助的24/7 MDR服务，协助深入调查、主动威胁搜索和攻击报告。

•用户行为监测：Cynet查找表明用户账户受攻击的异常行为。

•风险级别识别：平台的UEBA功能使用全面的用户信息来确定用户的整体风险级别。

传送门：

https://www.cynet.com/cynet-360-for-compliance-frameworks/

**6、Exabeam**

Exabeam是一家安全运营服务提供商，UEBA是其主要服务功能之一，主要特点包括事件时间线管理、基于角色的访问控制以及常规性SIEM平台服务。Exabeam的最大特点就是可以与数百个第三方安全工具集成，并支持众多的数据源格式，包括Salesforce应用等非安全数据源，因此非常适合需要众多数据源的企业使用。

主要特点

•可以与SIEM系统集成：Exabeam允许客户将其UEBA解决方案与那些已经在使用的SIEM解决方案集成。

•其他预构建系统集成：除了SIEM外，Exabeam还与Microsoft 365、VMware ESXi、Salesforce和CrowdStrike等产品集成。

•异常行为分析能力：Exabeam结合来自多个产品的可疑信号以发现复杂的行为威胁。

•用户群体分类：Exabeam根据关系（比如同一个业务部门的内部用户）对用户和其他实体（比如设备）进行分类。

传送门：

https://www.exabeam.com/

**7、Splunk UEBA**

Splunk UBA是一款较为少见的独立用户行为分析产品，提供了团队监测、分析和检测用户威胁所需的各项功能。企业可以使用Splunk的威胁监测工作流程来改善当前的安全状况。这项技术将企业中海量的原始事件警报聚焦到几个最有可能发生的威胁。对于想要一个专门用于用户分析独立解决方案的团队，可以选择使用Splunk UEBA。

主要特点

•事件优先级确定：每个异常都有自己的风险评分，Splunk可以帮助团队优先响应最关键的问题。

•多重异常和威胁模型：这些Splunk模型专注于检测企业外部的威胁。

•高级威胁检测：该产品旨在检测账户接管、指挥和控制活动以及浏览器漏洞。

•数据泄露检测：Splunk可以搜寻从存储位置提取或传输敏感公司信息的活动。

传送门：

https://www.splunk.com/en\_us/products/user-behavior-analytics.html

参考链接：

https://www.esecurityplanet.com/products/best-user-and-entity-behavior-analytics-ueba-tools/

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMnicXSRCtG4URyLibbqPegjnnibfRB0z4zIzwghbLOkV5fqGYM8vhuQdqw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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