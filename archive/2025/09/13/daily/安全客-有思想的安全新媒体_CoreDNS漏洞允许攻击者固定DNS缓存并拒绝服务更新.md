---
title: CoreDNS漏洞允许攻击者固定DNS缓存并拒绝服务更新
url: https://www.anquanke.com/post/id/312096
source: 安全客-有思想的安全新媒体
date: 2025-09-13
fetch_date: 2025-10-02T20:04:23.429281
---

# CoreDNS漏洞允许攻击者固定DNS缓存并拒绝服务更新

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

# CoreDNS漏洞允许攻击者固定DNS缓存并拒绝服务更新

阅读量**57749**

发布时间 : 2025-09-12 17:35:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/coredns-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

CoreDNS中发现一个严重漏洞，**攻击者可通过固定DNS缓存条目中断服务，导致更新无法生效，形成拒绝服务。**

该漏洞存在于CoreDNS的**etcd插件**中，源于关键逻辑错误：etcd租约ID被误解释为生存时间（TTL）值，导致DNS记录缓存周期异常延长。

漏洞根源位于`plugin/etcd/etcd.go` 文件的`TTL()`函数，该函数错误地将64位etcd租约ID截断为32位无符号整数，并将结果用作DNS记录的TTL。租约ID是租约授权的随机标识符，与租约持续时间无关。当生成大租约ID时，截断后的值可能代表极长的TTL（有时长达数十年）。

### **TTL混淆导致缓存固定**

接收该记录的下游DNS解析器和客户端会按指定时长缓存记录，从而实现“缓存固定”攻击——攻击者可创建恶意或过时DNS条目并长期留存，阻止后续更新传播到受影响客户端。

**攻击者若通过受损服务账户或配置不当环境获得etcd数据存储的写入权限，即可利用此漏洞：创建或更新DNS记录并附加租约（租约实际持续时间无关，仅租约ID起作用）。CoreDNS会以被误读的超大TTL提供该记录，导致客户端和解析器缓存过时信息。**

即使etcd中的恶意条目被修正或删除，且CoreDNS重启，客户端仍会在本地缓存过期前持续解析错误地址。这对高可用性影响严重，关键服务更新、IP地址轮换或故障转移流程将被缓存固定的客户端忽略。

完整性影响被评为低——因为拥有etcd写入权限的攻击者本可将服务重定向至恶意端点，但该漏洞放大了此类攻击的持久性。

### **受影响版本与缓解措施**

漏洞于CoreDNS 1.2.0版本引入，影响所有使用etcd插件进行服务发现的后续版本。

G**itHub用户“@thevilledev”披露了该漏洞并贡献修复方案。建议缓解措施包括：更新`TTL()`函数，通过etcd租约API正确获取剩余租约时间，而非滥用租约ID；此外，应实施可配置的最小/最大TTL限制，防止极端值被下发。**

使用CoreDNS etcd插件的用户需立即更新至补丁版本，以防潜在服务中断。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/coredns-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312096](/post/id/312096)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/coredns-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/coredns-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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