---
title: CISA称黑客利用GeoServer漏洞成功入侵一联邦机构
url: https://www.anquanke.com/post/id/312347
source: 安全客-有思想的安全新媒体
date: 2025-09-25
fetch_date: 2025-10-02T20:37:54.669610
---

# CISA称黑客利用GeoServer漏洞成功入侵一联邦机构

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# CISA称黑客利用GeoServer漏洞成功入侵一联邦机构

阅读量**121463**

发布时间 : 2025-09-24 16:45:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-says-hackers-breached-federal-agency-using-geoserver-exploit/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全和基础设施安全局（CISA）披露，攻击者去年通过攻陷**未打补丁的GeoServer实例**，侵入了某未具名美国联邦民事行政部门（FCEB）机构的网络。

该安全漏洞（编号**CVE-2024-36401**）是一个**严重的远程代码执行（RCE）漏洞**，已于2024年6月18日修复。在多名安全研究人员公开漏洞利用证明（PoC）后，CISA于约一个月后将其添加至**已知被利用漏洞目录**，PoC演示了如何在暴露的服务器上实现代码执行。

尽管CISA未透露野外利用细节，但威胁监控服务Shadowserver观察到，针对CVE-2024-36401的攻击始于2024年7月9日，而开源情报搜索引擎ZoomEye当时已追踪到**超16,000台暴露在互联网上的GeoServer服务器**。

首次攻击被检测到两天后，威胁行为者入侵了美国联邦机构的GeoServer服务器，并在约两周后攻陷了另一台服务器。在攻击的下一阶段，他们通过该机构网络**横向移动**，入侵了一台Web服务器和一台SQL服务器。

“侵入组织网络后，网络威胁行为者主要依赖**暴力破解技术（T1110）** 获取密码，以进行横向移动和权限提升。他们还通过利用关联服务来访问服务账户。”

攻击者**潜伏三周未被发现**，直至2024年7月31日，该联邦机构的**端点检测与响应（EDR）工具**向安全运营中心（SOC）发出警报，标记SQL服务器上的一个文件为可疑恶意软件。

在攻击者的恶意活动触发更多EDR警报后，SOC团队隔离了服务器，并在CISA协助下启动调查。

CISA现敦促网络防御者**加快修补关键漏洞（尤其是已列入已知被利用漏洞目录的漏洞）**，确保安全运营中心持续监控EDR警报以发现可疑网络活动，并加强事件响应计划。

今年7月，CISA在对美国某关键基础设施组织进行主动狩猎式评估后发布了另一则公告。尽管未发现网络上的恶意活动证据，但发现了诸多网络安全风险，包括但不限于**凭证存储不安全、多台工作站共享本地管理员凭证、本地管理员账户无限制远程访问、日志记录不足以及网络分段配置问题**。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-says-hackers-breached-federal-agency-using-geoserver-exploit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312347](/post/id/312347)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-says-hackers-breached-federal-agency-using-geoserver-exploit/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-says-hackers-breached-federal-agency-using-geoserver-exploit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)