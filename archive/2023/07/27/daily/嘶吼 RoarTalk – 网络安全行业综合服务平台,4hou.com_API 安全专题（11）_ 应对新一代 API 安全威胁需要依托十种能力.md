---
title: API 安全专题（11）| 应对新一代 API 安全威胁需要依托十种能力
url: https://www.4hou.com/posts/K79x
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-27
fetch_date: 2025-10-04T11:51:01.714426
---

# API 安全专题（11）| 应对新一代 API 安全威胁需要依托十种能力

API 安全专题（11）| 应对新一代 API 安全威胁需要依托十种能力 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# API 安全专题（11）| 应对新一代 API 安全威胁需要依托十种能力

梆梆安全
[行业](https://www.4hou.com/category/industry)
2023-07-26 18:00:48

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)73780

收藏

导语：数字化时代，伴随互联网的广泛应用和快速升级，企业内部应用逐渐由单一架构发展为低耦合、高内聚的服务网格架构，业务应用内部的数据交换大量采用 API 方式进行连接，导致企业 API 数量呈现指数级爆发式增长，API安全性受到极大挑战。

**一、API安全挑战**

企业在大量依托 API 接口来完成内部数据交互、外部数据共享、三方组件引用时，衍生出的安全挑战主要包括以下几方面：

01  业务暴露面扩大

随着云计算技术的广泛应用，越来越多的 Saas 化业务系统和服务被迁移上云，API 在为更多用户提供服务的同时，导致大量 API 对外暴露，相对于传统数据中心的单点式调用，云上的东西向和南北向访问都可能成为威胁 API 安全的攻击面。

02 忽视本身存在的脆弱性

敏捷开发模式是当下主流开发模式，敏捷开发周期短，API 接口构建频繁，对于API 接口本身存在的脆弱性难以兼顾。

03 存在未知API

API 是由编码人员所创建，很少有人会意识到这些 API 的存在，这使得大量的 API 缺少维护，并经常容易被忽略。当组织缺乏对于 API 接口的治理机制时，僵尸、影子和幽灵等可怕的 API 威胁就会出现，给企业业务开展造成损害。

04  对API安全风险无认知

一些企业会认为按照开发设计规定来设计 API 接口，不会有什么问题，从而导致API 被攻击的可能性以及其后果被严重低估，因此未采取充分的防护措施。此外，第三方合作伙伴系统的 API，也容易被组织所忽视。

**二、传统安全工具存在缺陷**

由于 API 在设计架构上的特殊性，它们无法通过传统的应用安全工具进行有效的保护，比如API应用网关、日志分析和 WAF 等。据最新的 API 安全研究数据显示，77%的受访者表示，传统的安全工具难以满足其API安全防护需求，主要原因包括：

01 缺乏对于API的检测能力

传统安全工具主要是为保护传统业务应用程序和网络基础设施而设计的，缺乏解决API特有漏洞所需的具体功能，比如无效的对象级授权（BOLA）、输入验证不充分或访问速率限制不足。

02 无法融入API安全生态

现代应用程序常常包含来自不同提供商的大量 API。这种生态的复杂性使得传统安全工具难以全面准确地监控 API 流量和检测可疑活动。

03 安全能力存在局限性

传统安全工具无法提供检测特定 API 攻击（比如撞库攻击和蛮力破解）所需的可见性，因为这类攻击往往会发生在多个 API 之间，需要实现细粒度的API级可见性。

04 身份校验机制无针对性

很多企业中存在大量历史遗留应用程序，因此，使用 API 而不进行身份验证是目前很常见的现象。这些未经身份验证的 API 一旦公开暴露，就会对企业的应用系统安全构成威胁。API 需要提供比传统安全工具更高级的身份验证和授权机制，比如基于令牌的验证和授权。

05  动态多变的环境

API 是在高度动态多变的环境中运行，需要不断部署新的 API，并经常更新现有的API。传统安全工具难以跟上快速的变化，从而导致在 API 安全控制方面出现缺口，可能被人利用。

**三、应对API安全新型风险需依托十种能力**

01 API资产发现与管理

需建立健全 API 管理制度，对 API 进行深度的资产梳理，通过主动、被动多种识别方式，形成清晰的 API 资产台账，帮助安全团队了解不同应用程序使用的 API 的业务属性以及对应 API 的关联性。

02 规范设计API

攻击者经常采用的一种技术就是通过使用无效或不当的输入来诱导 API 错误输出。所以要求所有 API 请求和响应遵守模式和所有规范是保护这些 API 免受攻击和破坏的重要步骤。

03 执行安全策略

企业都会制定相应的 API 安全策略，但若没有严格执行，这些策略将变得没有意义。保证企业的 API 安全策略（速率限制、阻断等）能够得到有效的执行，是对API 安全风险防护的基本要求之一。

04  敏感数据保护

API 的主要安全风险之一就是敏感数据泄露。保护敏感数据应该是任何 API 安全解决方案的一部分。要保护敏感数据避免被泄露，就需要确保 API 上所承载的敏感数据是否经明文传输或未加密传输。

05 防止 Dos 攻击

Dos 攻击对 API 接口可造成业务连续性中断，影响正常用户的访问，所以应对此类风险需要有防止 DoS 攻击的能力。

06 加大攻击防护

现如今攻击者在不断寻找破坏和恶意利用 API 的方法。API 安全技术需要包括基于特征、基于异常和基于 AI 的攻击保护机制，以防范各种各样的新型攻击。

07 访问控制限制

不适当的访问控制（包括身份验证和授权）一直都是困扰 API 安全应用的主要问题之一。无论是由于疏忽、人为错误、主观恶意还是其他任何原因，对 API 的访问控制不当都意味着灾难性后果。API 安全技术必须要能够提供身份威胁发现服务、身份验证服务和 API 访问控制服务。

08  恶意用户检测

通过机器学习可以分析出与 API 与之交互的客户端行为是否存在异常，这有助于在安全攻击实际发生前做好预防。

09 安全配置和管理

API 的配置和管理不当是导致产生安全威胁的原因之一。因此，API 安全技术需要帮助企业确保 API 不会被错误配置，避免人为 API 安全漏洞的产生。

10 API 访问行为分析

通过研究从应用程序的端点和 API 收集而来的各种日志，就能总结出各类 API 应用请求路径的行为，并生成一组行为安全性参照指标，比如请求大小、响应大小、数据延迟、请求率、错误率以及响应吞吐量。这是一个迭代过程，会随时间的推移而持续更新，并不断优化。

**参考链接**

https://hackernoon.com/5-reasons-traditional-security-tools-fall-short-in-protecting-apis

https://www.darkreading.com/edge/10-features-an-api-security-service-needs-to-offer

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YMLdL1yG)

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

![](https://img.4hou.com/portraits/e3b60d4465a093e3518f9cbe37a778ff.png)

# [梆梆安全](https://www.4hou.com/member/qoj2)

梆梆安全|保护智能生活

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/qoj2)

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