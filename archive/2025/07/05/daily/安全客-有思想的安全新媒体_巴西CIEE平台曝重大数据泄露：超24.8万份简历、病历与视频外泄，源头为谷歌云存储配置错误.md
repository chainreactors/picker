---
title: 巴西CIEE平台曝重大数据泄露：超24.8万份简历、病历与视频外泄，源头为谷歌云存储配置错误
url: https://www.anquanke.com/post/id/309428
source: 安全客-有思想的安全新媒体
date: 2025-07-05
fetch_date: 2025-10-06T23:16:42.564669
---

# 巴西CIEE平台曝重大数据泄露：超24.8万份简历、病历与视频外泄，源头为谷歌云存储配置错误

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

# 巴西CIEE平台曝重大数据泄露：超24.8万份简历、病历与视频外泄，源头为谷歌云存储配置错误

阅读量**75957**

发布时间 : 2025-07-04 15:06:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/ciee-data-breach-exposes-248k-brazilian-records-medical-reports-cvs-videos-leaked-from-google-cloud/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Resecurity 安全公司披露，一名在地下数据市场活跃的情报贩子 “888” 公布了从巴西知名机构 **CIEE（企业与学校融合中心）** 窃取的 **248,725 条敏感个人记录**。该机构主要负责为学生提供实习与学徒机会。

本次泄露的数据源自一个配置错误的 Google Cloud Storage 存储桶，内容极为敏感，包括**医疗报告、个人简历、证件照**，甚至还有**用于求职的视频材料**。

Resecurity 指出，攻击者 “888” 并非新手，其活跃轨迹可追溯至 2024 年，曾攻击对象涵盖 **微软、宝马（香港）** 以及多家科技、货运、能源企业：“‘888’ 自 2024 年起便在暗网论坛活动，频繁以大型企业为攻击目标，并通过贩售敏感数据获利。”

CIEE 平台因广泛与巴西本地银行、电信、能源与科技公司合作，成为信息集中的重要枢纽，也因此被网络犯罪者盯上：“此类服务聚集了大量用于尽调和招聘流程的敏感 PII（个人可识别信息），极具攻击价值。”

**公开暴露的数据细节：**

Resecurity 威胁情报团队发现，名为 `ciee-storage.storage.googleapis.com` 的云存储桶未设置访问限制，**超过 36.4 万个文件**可被公众访问，涉及总数据量达约 **28 GB**，包含：

* **281,912 张** 个人证件照（JPEG/PNG）
* **约 8,000 条** 求职视频（MP4/MOV）
* **约 40,000 份** 简历（PDF/JPEG）
* **285 个 CSV 文件**，含近 **30 万条** 候选人记录（姓名、邮箱、手机号、CPF 纳税人识别号、职位等）
* **2,838 份** 医疗报告（PDF）
* **264 个 Excel 文件**，包含内部追踪与分析数据

Resecurity 强调了此次泄露的严重性：“这些文件涉及大量个人身份信息（PII）、财务文档、医疗记录、多媒体文件与内部资料。”

**泄露风险极高，部分信息无法更改或撤销**

尤为令人担忧的是，本次泄露不仅包括姓名和联系方式，更涉及**人脸图像、生物信息、医疗记录与身份文件**，这些信息一旦流出，无法像密码那样简单重置或废止。

攻击者 “888” 在地下论坛以“信誉买家”著称，长期以真实数据交易获利，支持使用匿名性更强的门罗币（XMR）进行交易。其行为模式被认为与近期被FBI起诉的著名泄密者 IntelBroker 类似。

为证明数据真实性，攻击者公开了部分样本，Resecurity 随后联系了其中多位受害者，所有人均证实曾在 CIEE 注册使用。

“攻击者未透露数据提取方式，但公布了大批数据样本，Resecurity 核实后确认其为真实信息。”

**根因确认：云存储配置错误，成为攻击切入点**

此次数据泄露的根源是 **Google Cloud 存储桶配置错误**，该类型错误在近年已成为攻击者最常利用的目标：“云存储暴露已成为网络犯罪分子的高频攻击手段。”

攻击者通过自动化扫描工具在互联网上搜索未设访问控制的公开存储桶，CIEE 的云桶未启用任何身份验证机制，导致大量私密信息被直接访问下载。

本文翻译自securityonline [原文链接](https://securityonline.info/ciee-data-breach-exposes-248k-brazilian-records-medical-reports-cvs-videos-leaked-from-google-cloud/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309428](/post/id/309428)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ciee-data-breach-exposes-248k-brazilian-records-medical-reports-cvs-videos-leaked-from-google-cloud/)

如若转载,请注明出处： <https://securityonline.info/ciee-data-breach-exposes-248k-brazilian-records-medical-reports-cvs-videos-leaked-from-google-cloud/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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