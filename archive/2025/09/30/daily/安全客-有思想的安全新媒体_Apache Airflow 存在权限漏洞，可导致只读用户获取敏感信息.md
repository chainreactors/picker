---
title: Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息
url: https://www.anquanke.com/post/id/312457
source: 安全客-有思想的安全新媒体
date: 2025-09-30
fetch_date: 2025-10-02T12:03:34.150542
---

# Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息

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

# Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息

阅读量**59581**

发布时间 : 2025-09-29 18:05:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apache-airflow-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Apache Airflow 3.0.3曝出**严重安全漏洞**，向仅具有**读取权限**的用户泄露敏感连接信息。

该漏洞编号为**CVE-2025-54831**，严重级别为“重要”（Important），从根本上破坏了平台在工作流连接中处理敏感数据的预期安全模型。

Apache Airflow 3.0版本对连接中的敏感信息管理方式进行了重大更改，实施了“**只写**”（write-only）模型，旨在将敏感连接字段的访问权限**独家限制给连接编辑用户**（Connection Editing Users）。

这一安全增强措施旨在防止未授权访问Airflow连接中存储的关键认证详情、数据库凭证和API密钥。

然而，3.0.3版本的实现存在**严重缺陷**，直接逆转了这些安全改进。

该漏洞允许具有**标准READ权限的用户**通过Airflow API和Web用户界面访问敏感连接信息。

无论`AIRFLOW__CORE__HIDE_SENSITIVE_VAR_CONN_FIELDS`配置设置如何（该设置专门用于对未授权用户隐藏敏感连接详情），信息泄露都会发生。

这一漏洞使安全配置**完全失效**，给依赖Airflow访问控制的组织带来重大风险。

Apache安全分析师在观察到连接处理机制的异常行为后发现了该漏洞。

该缺陷**专门影响Apache Airflow 3.0.3版本**，而早期的Airflow 2.x版本不受影响——因为它们采用不同的连接处理协议，向连接编辑者公开敏感信息是其文档化的行为。

漏洞源于Airflow 3.0引入的连接访问控制系统**实现不当**。

当具有READ权限的用户通过`/api/v1/connections/{connection_id}`端点查询连接详情或通过Web UI访问连接界面时，系统会错误地返回应隐藏的敏感字段，包括**密码、令牌和连接字符串**。

```
{
  "connection_id": "postgres_default",
  "conn_type": "postgres",
  "host": "localhost",
  "login": "airflow",
  "password": "exposed_sensitive_data",
  "schema": "airflow",
  "port": 5432
}
```

使用Apache Airflow 3.0.3的组织应**立即升级至3.0.4或更高版本**，以修复此安全漏洞并恢复对敏感连接信息的正确访问控制。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apache-airflow-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312457](/post/id/312457)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apache-airflow-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/apache-airflow-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53

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