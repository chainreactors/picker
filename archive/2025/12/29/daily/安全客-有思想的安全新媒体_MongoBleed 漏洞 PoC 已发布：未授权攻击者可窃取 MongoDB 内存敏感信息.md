---
title: MongoBleed 漏洞 PoC 已发布：未授权攻击者可窃取 MongoDB 内存敏感信息
url: https://www.anquanke.com/post/id/314075
source: 安全客-有思想的安全新媒体
date: 2025-12-29
fetch_date: 2025-12-30T03:25:43.332906
---

# MongoBleed 漏洞 PoC 已发布：未授权攻击者可窃取 MongoDB 内存敏感信息

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

# MongoBleed 漏洞 PoC 已发布：未授权攻击者可窃取 MongoDB 内存敏感信息

阅读量**19880**

发布时间 : 2025-12-29 15:36:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源： securityonline

原文地址：<https://securityonline.info/poc-released-mongobleed-exploit-allows-unauthenticated-attackers-to-drain-mongodb-memory/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

作为全球应用最广泛的数据库系统之一，MongoDB 曝出高危漏洞，数据库管理员正面临严峻的安全紧急事件。该漏洞编号为**CVE-2025-14847**，未授权远程攻击者可通过漏洞诱导服务器泄露内存（堆区）中的敏感数据，甚至可能暴露系统内部状态及内存指针。

安全研究员乔・德西蒙已公开该漏洞的验证代码（PoC），此漏洞的 CVSS 评分达 8.7 分，意味着未打补丁的系统将面临极高安全风险。

该漏洞根源在于 MongoDB 对 Zlib 压缩协议头的处理机制存在缺陷，被归类为 \*\*“长度参数不一致处理不当”\*\* 漏洞。核心问题在于，服务器会盲目信任客户端声明的数据解压后长度，即便该数值与实际数据大小完全不符。

漏洞利用需通过一套巧妙的五步流程实现：

1. 发送压缩消息，虚报解压后的预期数据长度（uncompressedSize）；
2. MongoDB 根据攻击者虚报数值分配超大内存缓冲区；
3. Zlib 库将实际数据解压至该缓冲区起始位置；
4. 漏洞触发后，MongoDB 误将整个缓冲区判定为合法有效数据；
5. BSON 解析器从缓冲区未初始化的内存区域读取 “字段名”，直至读取到空字节为止。

CVE 官方漏洞描述警示：“Zlib 压缩协议头中长度字段不匹配，可能导致未授权客户端读取服务器未初始化的堆内存数据。”

CVE-2025-14847 漏洞最令人担忧的一点，是其**无需任何身份认证**即可利用。MongoDB 在官方安全公告中确认：“攻击者可通过客户端侧利用服务器端 Zlib 库实现漏洞，无需认证即可获取服务器未初始化堆内存数据。”

OP Innovate 专家指出，该漏洞可能导致**内存中敏感数据泄露**，包括系统内部状态信息、内存指针，以及其他可辅助攻击者实施进一步渗透的核心数据。

此次漏洞影响范围极广，覆盖 MongoDB 多款新版本及老旧遗留系统，受影响版本如下：

* 8.2.0 至 8.2.3 版本
* 8.0.0 至 8.0.16 版本
* 7.0.0 至 7.0.26 版本
* 6.0.0 至 6.0.26 版本
* 5.0.0 至 5.0.31 版本
* 4.4.0 至 4.4.29 版本
* 4.2、4.0、3.6 系列所有版本

MongoDB 已发布漏洞修复版本，强烈建议用户立即升级。安全补丁版本包括：8.2.3、8.0.17、7.0.28、6.0.27、5.0.32 及 4.4.30。

对于暂时无法升级的企业，可采用临时缓解方案：**禁用 Zlib 压缩功能**。管理员可在启动 mongod 或 mongos 实例时，配置 net.compression.compressors 参数，明确剔除 Zlib，改用 snappy 或 zstd 等替代压缩算法。

目前该漏洞验证代码（PoC）已在 GitHub 公开，安全防护人员亟需争分夺秒为数据库打补丁，避免威胁攻击者抢先利用漏洞，从受影响服务器的暴露内存中窃取核心机密。

本文翻译自 securityonline [原文链接](https://securityonline.info/poc-released-mongobleed-exploit-allows-unauthenticated-attackers-to-drain-mongodb-memory/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314075](/post/id/314075)

安全KER - 有思想的安全新媒体

本文转载自:  [securityonline](https://securityonline.info/poc-released-mongobleed-exploit-allows-unauthenticated-attackers-to-drain-mongodb-memory/)

如若转载,请注明出处： <https://securityonline.info/poc-released-mongobleed-exploit-allows-unauthenticated-attackers-to-drain-mongodb-memory/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **870**

* 粉丝
* **6**

### TA的文章

* ##### [EmEditor 遭攻陷：“沃尔沙姆” 伪装者篡改官方安装包，植入间谍软件](/post/id/314096)

  2025-12-29 15:40:16
* ##### [性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线](/post/id/314100)

  2025-12-29 15:39:28
* ##### [圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元](/post/id/314091)

  2025-12-29 15:39:18
* ##### [70 美元芯片争夺战：谷歌缘何高管换人，苹果又为何要直面 230% 的价格暴涨](/post/id/314077)

  2025-12-29 15:38:41
* ##### [CVE-2025-54322（CVSS 10 分满分）：AI 智能体发现全球网络设备高危零日漏洞](/post/id/314086)

  2025-12-29 15:38:37

### 相关文章

* ##### [EmEditor 遭攻陷：“沃尔沙姆” 伪装者篡改官方安装包，植入间谍软件](/post/id/314096)

  2025-12-29 15:40:16
* ##### [性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线](/post/id/314100)

  2025-12-29 15:39:28
* ##### [圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元](/post/id/314091)

  2025-12-29 15:39:18
* ##### [70 美元芯片争夺战：谷歌缘何高管换人，苹果又为何要直面 230% 的价格暴涨](/post/id/314077)

  2025-12-29 15:38:41
* ##### [CVE-2025-54322（CVSS 10 分满分）：AI 智能体发现全球网络设备高危零日漏洞](/post/id/314086)

  2025-12-29 15:38:37
* ##### [终结 “内存占用税”：微软新方案让文件资源管理器搜索速度翻倍](/post/id/314084)

  2025-12-29 15:38:15
* ##### [黑客攻陷 Trust Wallet 谷歌浏览器插件，用户称数百万资产被盗](/post/id/314073)

  2025-12-29 15:37:47

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