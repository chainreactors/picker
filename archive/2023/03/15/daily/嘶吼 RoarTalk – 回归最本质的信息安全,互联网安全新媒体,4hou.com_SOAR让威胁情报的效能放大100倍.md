---
title: SOAR让威胁情报的效能放大100倍
url: https://www.4hou.com/posts/AOyO
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-15
fetch_date: 2025-10-04T09:34:38.293549
---

# SOAR让威胁情报的效能放大100倍

SOAR让威胁情报的效能放大100倍 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# SOAR让威胁情报的效能放大100倍

雾帜智能
[行业](https://www.4hou.com/category/industry)
2023-03-14 17:54:19

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124184

收藏

导语：2019年8月国内首发的AI+SOAR产品——雾帜智能HoneyGuide，通过虚拟作战室、AI机器人和可视化剧本编排，帮助安全团队加速威胁响应与处置，提升运营自动化，实现安全风险自适应治理。 针对上述威胁情报实战应用场景中遇到的几大痛点，雾帜智能HoneyGuide SOAR安全剧本都能完美解决，帮助安全团队用好威胁情报，实现自动化、智能化的安全应急响应。

**背景介绍**

过去几年，网络安全领域热门关键词“SOAR”和“威胁情报”备受关注。

SOAR是Security Orchestration Automation and Response的缩写，直译为“安全编排自动化与响应”，意指：借助安全排编和自动化技术，对既有安全产品、网络设备、IT系统和SaaS服务等基础能力进行统筹调度；基于可视化剧本编排和调度执行引擎，开展有逻辑、有顺序的自动化流程操作，实现日常安全事件运营和突发事件处置的过程自动化。代表厂商：雾帜智能。

Threat Intelligence——威胁情报是识别和分析网络威胁的过程。“威胁情报”一词可以指关于潜在威胁收集的数据或收集、处理和分析该数据以更好了解威胁的过程。威胁情报还包括筛选数据、根据上下文检查数据以发现问题并针对发现的问题部署解决方案。代表厂商：微步在线。

本文将讨论在安全运营实战过程中如何使用SOAR+威胁情报的方式，开展更快速、更稳定和更智能的安全运营。

**应用场景**

有过一线安全事件运营经验的工程师一定有这样的体会：大量事件运营和处置的过程，需要持续不断丰富的信息上下文，尤其是针对IP、域名、文件相关的特征描述、威胁标签等。至少有两大类场景是高度依赖威胁情报的：

* 批量识别与降噪：企业已有的SIEM平台初次告警往往误报率较高，需要做二次筛选获判，才能实现有效降噪

* 快速判断与处置：应急响应期间，针对特定域名、IP、文件进行快速处置时，往往缺少有效的上下文或背景信息，导致响应过度依赖人工，速率下降，失效不足，风险不可控制

威胁情报刚好能解决上述两个场景的问题。专业的威胁情报厂商通过及时、稳定和持续的情报信息，为安全人员提供个性化的查询服务，在事件处置过程中提供重要决策依据。

**典型困难**

然而，现实情况是，上述两个场景在实战落地时往往遇到巨大的挑战。这些挑战多半是因为人力不可及而导致的，包括：工作量、请求速率、二次判断、数据回传等。

首先，数量大。如果上游SIEM每分钟产生上百条安全告警，而这些告警里的源IP都需要进行威胁情报信息补充的话，就算安全工作人员有三头六臂，也不可能7x24小时手工查询威胁情报。

其次，频次高。安全事件监控和响应通常都有极高的MTTD和MTTR运营指标，单纯依靠人员查询，效率极其低下。一个简单的信息查询，通常包括：复制原始信息，登录情报平台，完成身份认证，查询情报信息，复制查询结果，回传告警系统，少则几十秒，多则几分钟。在实战情况下，往往各种原因导致情报查询缓慢，应急响应贻误战机。

再次：逻辑多。威胁情报查询的结果，通常不是立即使用，而是要结合情报的返回结果和应用场景进行二次判断，实现综合决策。例如：标签、历史、特征、分值、可信度、域名情报引入的IP情报……这些判断靠人工几乎很难标准化、自动化。

最后：操作难。所有的情报查询结果，最终都会应用到事件运营和响应过程中，通常的情报消费方包括：SIEM、SOC、工单、防火墙封禁逻辑、网络微隔离逻辑等等。数据交互的过程除了人机操作界面，绝大多数都是API接口，人类工程师无法直接调用。由此，导致情报查询的结果无法通过安全、高效的途径传递给其它单元。

**这些实战痛点问题该如何解决呢？**

**SOAR增强威胁情报的实战应用**

2019年8月国内首发的AI+SOAR产品——雾帜智能HoneyGuide，通过虚拟作战室、AI机器人和可视化剧本编排，帮助安全团队加速威胁响应与处置，提升运营自动化，实现安全风险自适应治理。

针对上述威胁情报实战应用场景中遇到的几大痛点，雾帜智能HoneyGuide SOAR安全剧本都能完美解决，帮助安全团队用好威胁情报，实现自动化、智能化的安全应急响应。

**解决情报批量识别和降噪的问题**

批量查询威胁情报，并使用情报结果，这是典型的SIEM/SOC安全事件分析场景的基础需求，然而此类场景的并发量大，时间周期短，是人力不可为的，挑战巨大。

**关键步骤**

雾帜智能HoneyGuide SOAR + 微步在线威胁情报，可实现情报批量查询及反馈，主要流程：

1. 安全剧本启动后，获取SIEM（如：IBM Qradar）告警批量文件（客户提供）；
2. 剧本对zip文件解压缩，并拆分为1000个/文件；
3. 循环处置告警文件，并从告警条目中摘取，IP、域名、URL等；
4. 调用微步在线威胁情报接口，查询威胁情报；
5. 整理并聚合威胁情报查询结果；
6. 通过SIEM平台API接口，回传给SIEM；
7. 还可以根据需要增加，其它判断逻辑，通过拖拽即可实现逻辑编排；
8. 将上述安全剧本以定时器方式设置执行。

![1678356194842030.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230309/1678356194842030.png "1678356194842030.png")

实战策略来源：某股份制商业银行、某科技金融公司、某汽车制造业公司

**实战成效**

通过落地上述SOAR + 威胁情报应用的组合，客户安全事件运营效率大幅提升，主要体现在：

* 多！上万次的数据查询，可在数分钟内完成，无需人员手工操作；
* 准！情报查询效率大幅提升，反向给SIEM提供更高质量的情报标签，增强了威胁告警的准确率，实现了大幅降噪；
* 快！因为全自动实现了情报查询，大幅解放安全生产力，工程师可以投入到更需要创造力的安全场景；
* 稳！自动化情报查询和安全运营，将安全团队的运营能力稳定在较高的水准上，不会因为人员职位变动、请假、生病、出差等问道导致运营水平下降。

几十倍上百倍的效率提升！

**解决快速判断和处置的问题**

安全运营团队在应对突发事件或者重保模式下开展应急处置时，往往需要快速决策是否要立即封禁某个IP、关停某个域名、拦截某个URL，隔离某台主机。单凭简单的资产表格，工程师很难下定决心做出处置动作，往往还需要足够的背景知识和上下文信息，此时情报可以充当非常重要的补充。当你决定要不要封禁某个IP地址的时候，威胁情报信息能够给你足够的信心支持。

![10.26-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230309/1678356099161013.png "1678356099161013.png")

情报查询往往涉及到频繁的手工操作，靠工程师徒手应急响应，完全无法满足实战攻防场景下的时效要求。

**关键步骤**

雾帜智能HoneyGuide SOAR + 微步在线威胁情报，可实现日常运营或者护网应急处置IP封禁、威胁遏制、主机隔离等场景的自动化响应，其主要流程包括：

1. 接收安全事件输入，判断是否需要采取应急处置（人工或自动）；
2. 决策需要对IP、域名、主机进行策略拦截，但还需要更丰富的信息；
3. 查询对应的资产属性信息；
4. 查询对应的威胁情报信息；
5. 根据返回的威胁情报信息，再决策采取何种动作（如：地理位置、威胁标记、标签集合等）；
6. 调用下游安全产品进行威胁拦截 ；
7. 在安全事件自动处置流程中引入安全剧本，或者在安全协同作战室中手工执行安全剧本。

![10.26-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230309/1678356415143526.png "1678356415143526.png")

实战策略来源：某能源行业集团公司、某国网电力公司、某大型证券行业客户、某个电信运营商客户

**实战成效**

通过落地上述SOAR + 威胁情报应用的组合，安全人员原本的徒手应急响应将得到全面改观，安全事件响应的时效和水准也得到了极速提升，主要体现在：

* 几乎零等待地查询到需要的情报信息，无需人工登录平台手工查询；
* 自动和上下游能力协作，免人工参与开展自动化应急响应；
* 情报查询结果可以结构化使用，便于灵活定制风险决策逻辑；
* 极速、精准并高效低地完成安全事件应急响应，MTTR得到实质性的保障；

分钟级甚至秒级的事件响应！

**总结**

目前雾帜智能HoneyGuide SOAR产品已经实现支持联动国内外主流威胁情报系统，包括：微步在线、腾讯威胁情报、VirusTotal、微软SRC、奇安信威胁情报（沙箱）、Scamalytics、守望者(watcherlab)威胁情报Feed系统、alieVault开源威胁情报等，并且还在持续扩充中。

SOAR + 威胁情报，应急响应SOAR Easy！

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4VqkXQL2)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/b0fab1927d88da9f7da8efe2f1bb29c4.jpg)

# [雾帜智能](https://www.4hou.com/member/lgY1)

专注SOAR,全面加速应急响应！

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/lgY1)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)