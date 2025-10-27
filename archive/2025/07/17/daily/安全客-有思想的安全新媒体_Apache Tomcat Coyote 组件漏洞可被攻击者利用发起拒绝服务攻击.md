---
title: Apache Tomcat Coyote 组件漏洞可被攻击者利用发起拒绝服务攻击
url: https://www.anquanke.com/post/id/310176
source: 安全客-有思想的安全新媒体
date: 2025-07-17
fetch_date: 2025-10-06T23:27:44.975344
---

# Apache Tomcat Coyote 组件漏洞可被攻击者利用发起拒绝服务攻击

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

# Apache Tomcat Coyote 组件漏洞可被攻击者利用发起拒绝服务攻击

阅读量**113454**

发布时间 : 2025-07-16 18:17:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apache-tomcat-coyote-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

最新发布的 HTTP/2 安全公告披露，Apache Tomcat 的 **Coyote 引擎**存在一个新漏洞**（编号 CVE-2025-53506）**。

美国国家漏洞数据库于 5 天前首次记录该漏洞，其成因是**当 HTTP/2 客户端始终不确认服务器初始的 SETTINGS 帧时，Coyote 引擎未对并发流数量实施严格限制**。

攻击者可通过**反复创建永不关闭的流，耗尽服务器的线程池**，迫使容器进入**长时间的拒绝服务状态**，不过**数据的机密性和完整性不会受到影响**。

由于攻击流量通过常规的 **TCP 443 端口传输**，防火墙无法识别异常；且该漏洞攻击**复杂度低**，无需验证凭据即可实施。

GitHub 分析师追踪发现，该问题源于**添加动态流限制的代码重构过程中引入的竞态条件**，并发布了概念验证流量捕获数据，可稳定导致未打补丁的版本崩溃。

所有**仍在维护**的版本均受此漏洞影响，包括 **11.0.0-M1 至 11.0.8、10.1.0-M1 至 10.1.42，以及 9.0.0.M1 至 9.0.106 版本**。

Apache 已发布修复版本 11.0.9、10.1.43 和 9.0.107；无法立即升级的管理员应**至少禁用 HTTP/2**，或**在反向代理层限制**

```
maxConcurrentStreams
```

**参数**，以避免服务中断。

该漏洞的 CVSS v4 评分为 **6.3**，其中可用性影响等级为 “高”，其他影响指标为 “无”，凸显其**以拒绝服务为核心**的攻击特征。

#### **流泛洪机制的利用方式**

实际攻击中，攻击者保持单个 TLS 会话打开，并循环发送以下 payload：

```
PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n      ; connection pre-face
…SETTINGS (ACK omitted)            ; server settings ignored
HEADERS  END_STREAM=0  …           ; open stream 1
HEADERS  END_STREAM=0  …           ; open stream 2
/* repeat until thread pool saturation */
```

由于 Tomcat 在接收实际数据前就为每个流分配工作线程，**每个 “孤儿流” 会无限期占用一个线程**。

一旦执行器队列达到上限，合法请求将超时失败，**导致网站实际下线**，但 Java 虚拟机（JVM）不会崩溃。

**具有 SETTINGS 确认超时限制或严格流数量上限的现代反向代理**，可有效阻断此类攻击，因此在全面部署补丁前，**上游防护措施**具有实际可行性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apache-tomcat-coyote-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310176](/post/id/310176)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apache-tomcat-coyote-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/apache-tomcat-coyote-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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